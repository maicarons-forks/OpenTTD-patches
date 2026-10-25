"""Convert pxp-docs Typst sources to VitePress Markdown.

Usage: python tools/convert_typst_to_md.py
Reads pxp-docs/content-*/**.typ, writes Markdown pages + copies images.

Routing (language switcher requires parallel paths):
- content-zh/... -> pxp-docs/<chapter>/...   (root locale, e.g. /decouple/)
- content-en/... -> pxp-docs/en/<chapter>/... (en locale, e.g. /en/decouple/)

Top-level index.typ files (zh/en landing intros) are SKIPPED here:
their content is hand-maintained in pxp-docs/index.md and pxp-docs/en/index.md
(home layout pages that the converter must not overwrite).

Conventions applied (re-runnable, all improvements live here):
- `#title[X]` -> frontmatter title + visible `# X` H1 (every page gets one H1)
- Typst `= sec` -> `## sec`, `== sub` -> `### sub` (single H1 per page)
- `#figure(image(...width:N%))` -> centered <img> preserving width %, lazy load
- Standalone `*注...*` / `*注意/⚠️...*` paragraphs -> ::: tip/warning containers
- Chapter index pages get an auto "本节内容 / In this section" child-link list
"""
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path("pxp-docs")
SRC_ZH = ROOT / "content-zh"
SRC_EN = ROOT / "content-en"

DIR_RENAMES = {"carry-vehicles": "veh-carry", "options": "other-options"}
FILE_RENAMES = {"cross-comp.typ": "cross-company.md"}

INDEX_ROUTES: set[str] = set()

# children order follows pxp-docs/main.typ (pedagogical order, not alphabetical)
CHAPTER_KIDS: dict[str, list[str]] = {
    "decouple": ["simple-decouple", "decouple-operation", "decouple-passenger"],
    "couple": ["simple-couple", "couple-operation", "cross-company-couple"],
    "orderlist": ["orderlist-edit", "orderlist-vehicle"],
    "veh-carry": ["orders", "cross-company"],
    "other-options": ["enable-depot", "invite-code-alive", "rainy"],
}
SECTION_LABEL = {"zh": "本节内容", "en": "In this section"}
BOX_TITLE = {"zh": {"warning": "注意", "tip": "注"},
             "en": {"warning": "Warning", "tip": "Note"}}

# 已知上游原文笔误，转换时顺手修正（只改完全匹配的字串）
TEXT_FIXUPS = {
    "即可在游戏中运输载具运输。": "即可在游戏中运输载具。",
}

WARN_PREFIXES = ("⚠️", "❗", "请注意", "注意", "Warning", "Caution")
TIP_PREFIXES = ("注", "提示", "Please note", "Note")
STRIP_RE = re.compile(r"^(请注意|注意|Please note|Warning|Caution|注|提示|Note)\s*[：:\-,.]?\s*")
EMOJI_RE = re.compile(r"^[⚠️❗\s]+")


def src_to_out(src: pathlib.Path) -> tuple[pathlib.Path, str] | None:
    """Map typ source -> (md out path, route). None = top landing, skipped."""
    lang = "zh" if src.parts[1] == "content-zh" else "en"
    parts = [DIR_RENAMES.get(p, p) for p in src.parts[2:-1]]
    if not parts:
        return None  # content-zh/index.typ, content-en/index.typ (hand-maintained homes)
    fname = FILE_RENAMES.get(src.name, src.stem + ".md")
    if lang == "zh":
        out = ROOT.joinpath(*parts, fname)
        route = "/" + "/".join(parts) + "/"
    else:
        out = ROOT.joinpath("en", *parts, fname)
        route = "/en/" + "/".join(parts) + "/"
    if fname != "index.md":
        route = route + fname[:-3]
    return out, route


def collect_pages() -> list[tuple[pathlib.Path, pathlib.Path, str]]:
    pages = []
    for src in sorted([*SRC_ZH.rglob("*.typ"), *SRC_EN.rglob("*.typ")]):
        mapped = src_to_out(src)
        if mapped is None:
            print(f"SKIP {src.relative_to(ROOT)} (hand-maintained home)")
            continue
        out, route = mapped
        pages.append((src, out, route))
        if out.name == "index.md":
            INDEX_ROUTES.add(route)
    return pages


def extract_title(text: str) -> tuple[str, str]:
    m = re.match(r"\s*#title\[(.*?)\]\s*\n?", text, re.S)
    if not m:
        raise ValueError("no #title found")
    return m.group(1).strip(), text[m.end():]


def convert_inline(s: str) -> str:
    s = s.replace("#linebreak()", "<br>")

    def link_repl(m: re.Match) -> str:
        url, label = m.group(1), m.group(2)
        return f"[{label}]({url})"

    s = re.sub(r'#link\("([^"]+)"\)\[([^\]]+)\]', link_repl, s)
    return s


FIGURE_RE = re.compile(
    r"#figure\(\s*image\(\"([^\"]+)\"(?:\s*,\s*width:\s*([\d.]+)%)?[^)]*\)\s*,?\s*\)", re.S)


def convert_figure(m: re.Match) -> str:
    path = m.group(1)
    try:
        width = float(m.group(2)) if m.group(2) else 80.0
    except ValueError:
        width = 80.0
    filename = pathlib.PurePosixPath(path).name
    alt = pathlib.PurePosixPath(filename).stem.replace("-", " ").replace("_", " ")
    # DocFigure (global component, uses withBase) keeps images working
    # under the /OpenTTD-patches/ Pages sub-path base.
    return (f'\n<DocFigure src="/images/{filename}" alt="{alt}" width="{width:g}" />\n')


def split_cells(inner: str) -> list[str]:
    cells: list[str] = []
    depth = 0
    start = -1
    i = 0
    while i < len(inner):
        ch = inner[i]
        if ch == "[" and depth == 0:
            start = i + 1
            depth = 1
        elif ch == "[" and depth > 0:
            depth += 1
        elif ch == "]" and depth > 0:
            depth -= 1
            if depth == 0 and start >= 0:
                cells.append(inner[start:i].strip())
                start = -1
        i += 1
    return cells


def convert_table(m: re.Match) -> str:
    ncols = int(m.group(1))
    cells = split_cells(m.group(2))
    cells = [convert_inline(c) for c in cells]
    rows = [cells[i:i + ncols] for i in range(0, len(cells), ncols)]
    rows = [r + [""] * (ncols - len(r)) for r in rows]
    header, body = rows[0], rows[1:]
    out = ["| " + " | ".join(header) + " |",
           "| " + " | ".join(["---"] * ncols) + " |"]
    out += ["| " + " | ".join(r) + " |" for r in body]
    return "\n".join(out)


TABLE_RE = re.compile(r"#table\(\s*columns:\s*(\d+),\s*([\s\S]*?)\n\)", re.S)
HEADING_RE = re.compile(r"^(=+)\s+(.*)$")
ADMON_RE = re.compile(r"^\*(.+)\*$", re.S)


def convert_admonition(line: str, lang: str) -> list[str] | None:
    """Standalone *...* note paragraphs -> ::: tip/warning blocks."""
    m = ADMON_RE.match(line.strip())
    if not m:
        return None
    inner = " ".join(m.group(1).split())
    if len(inner) < 2 or len(inner) > 600:
        return None
    kind: str | None = None
    if inner.startswith(WARN_PREFIXES):
        kind = "warning"
    elif inner.startswith(TIP_PREFIXES):
        kind = "tip"
    else:
        return None
    text = EMOJI_RE.sub("", inner)
    text = STRIP_RE.sub("", text)
    text = convert_inline(text)
    if not text:
        return None
    return [f"::: {kind} {BOX_TITLE[lang][kind]}", text, ":::"]


def convert_body(text: str, lang: str) -> str:
    for old, new in TEXT_FIXUPS.items():
        text = text.replace(old, new)
    text = FIGURE_RE.sub(convert_figure, text)
    text = TABLE_RE.sub(convert_table, text)
    out_lines: list[str] = []
    for line in text.split("\n"):
        stripped = line.strip()
        hm = HEADING_RE.match(stripped)
        if hm:
            level = min(len(hm.group(1)) + 1, 6)  # Typst = -> ##, == -> ###
            out_lines.append("#" * level + " " + convert_inline(hm.group(2).strip()))
        elif re.match(r"^\+\s", stripped):
            out_lines.append("- " + convert_inline(re.sub(r"^\+\s", "", stripped)))
        else:
            adm = convert_admonition(line, lang)
            if adm is not None:
                if out_lines and out_lines[-1].strip() != "":
                    out_lines.append("")
                out_lines.extend(adm)
                out_lines.append("")
            else:
                out_lines.append(convert_inline(line))
    return "\n".join(out_lines).strip() + "\n"


def fix_links(md: str, route: str, lang: str) -> str:
    """Rewrite internal .html links to VitePress routes."""
    if route.endswith("/"):
        cur_dir = route.rstrip("/")
    else:
        cur_dir = route.rsplit("/", 1)[0]

    def repl(m: re.Match) -> str:
        label, url = m.group(1), m.group(2)
        if url.startswith("http"):
            return m.group(0)
        path = url.split("#")[0]
        frag = url[len(path):]
        path = path.removesuffix(".html")
        if "dechoule" in path:  # typo in upstream sources
            base = "/decouple/" if lang == "zh" else "/en/decouple/"
            return f"[{label}]({base}{frag})"
        if path.startswith("/zh/"):
            new = path[3:] or "/"
        elif path.startswith("/"):
            new = path
        else:
            parts = [p for p in (cur_dir + "/" + path).split("/") if p not in ("", ".")]
            stack: list[str] = []
            for p in parts:
                if p == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(p)
            new = "/" + "/".join(stack)
        if new in INDEX_ROUTES:
            new = new if new.endswith("/") else new + "/"
        elif new + "/" in INDEX_ROUTES:
            new = new + "/"
        return f"[{label}]({new}{frag})"

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl, md)


def main() -> int:
    pages = collect_pages()
    rendered: dict[tuple[str, ...], tuple] = {}
    titles: dict[tuple[str, ...], str] = {}

    # pass 1: convert every page, remember titles
    for src, out, route in pages:
        raw = src.read_text(encoding="utf-8")
        title, body = extract_title(raw)
        lang = "zh" if src.parts[1] == "content-zh" else "en"
        dirs = [DIR_RENAMES.get(p, p) for p in src.parts[2:-1]]
        slug = FILE_RENAMES.get(src.name, src.stem + ".md")[:-3]
        key = (lang, *dirs, slug)
        titles[key] = title
        md_body = convert_body(body, lang)
        md_body = fix_links(md_body, route, lang)
        rendered[key] = (src, out, route, lang, title, md_body)

    # pass 2: append child navigation to chapter index pages, then write
    for key, (src, out, route, lang, title, md_body) in rendered.items():
        extra = ""
        if len(key) == 3 and key[2] == "index" and key[1] in CHAPTER_KIDS:
            ch = key[1]
            base = "/en" if lang == "en" else ""
            items = []
            for slug in CHAPTER_KIDS[ch]:
                t = titles.get((lang, ch, slug), slug)
                items.append(f"- [{t}]({base}/{ch}/{slug})")
            extra = f"\n## {SECTION_LABEL[lang]}\n\n" + "\n".join(items) + "\n"
        md = f"---\ntitle: {title}\n---\n\n# {title}\n\n{md_body.rstrip()}\n{extra}"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(md, encoding="utf-8")
        print(f"OK {src.relative_to(ROOT)} -> {out.relative_to(ROOT)}")

    # copy images static -> public
    src_img = ROOT / "static" / "images"
    dst_img = ROOT / "public" / "images"
    if src_img.exists():
        dst_img.parent.mkdir(parents=True, exist_ok=True)
        if dst_img.exists():
            shutil.rmtree(dst_img)
        shutil.copytree(src_img, dst_img)
        print(f"images copied: {len(list(dst_img.glob('*')))} files")

    print(f"done: {len(pages)} pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
