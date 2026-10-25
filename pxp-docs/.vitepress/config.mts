import { defineConfig } from "vitepress";

// 中文是根 locale（路径无前缀：/decouple/...），英文在 /en/... 下。
// 语言切换要求两边路径平行，这是切换能用的关键。
const zhSidebar = [
  {
    text: "列车解挂",
    link: "/decouple/",
    collapsed: false,
    items: [
      { text: "简单的列车解挂", link: "/decouple/simple-decouple" },
      { text: "解挂列车操作", link: "/decouple/decouple-operation" },
      { text: "解挂时客流分配", link: "/decouple/decouple-passenger" },
    ],
  },
  {
    text: "列车对接",
    link: "/couple/",
    collapsed: false,
    items: [
      { text: "简单的列车对接", link: "/couple/simple-couple" },
      { text: "列车对接操作", link: "/couple/couple-operation" },
      { text: "跨公司列车对接", link: "/couple/cross-company-couple" },
    ],
  },
  { text: "模块化机场", link: "/airport/" },
  {
    text: "自定义调度计划表",
    link: "/orderlist/",
    collapsed: false,
    items: [
      { text: "编辑调度计划表", link: "/orderlist/orderlist-edit" },
      { text: "载具使用自定义调度计划表", link: "/orderlist/orderlist-vehicle" },
    ],
  },
  {
    text: "载具运输",
    link: "/veh-carry/",
    collapsed: false,
    items: [
      { text: "载具运输调度计划设置", link: "/veh-carry/orders" },
      { text: "跨公司载具运输", link: "/veh-carry/cross-company" },
    ],
  },
  { text: "蓝图与撤回", link: "/bluepoint/" },
  {
    text: "更多选项",
    link: "/other-options/",
    collapsed: false,
    items: [
      { text: "禁止车库停放启动的列车和车站维修列车", link: "/other-options/enable-depot" },
      { text: "联机服务器邀请码保活", link: "/other-options/invite-code-alive" },
      { text: "下雨天气", link: "/other-options/rainy" },
    ],
  },
];

const enSidebar = [
  {
    text: "Train Decoupling",
    link: "/en/decouple/",
    collapsed: false,
    items: [
      { text: "Simple Train Decoupling", link: "/en/decouple/simple-decouple" },
      { text: "Train Decoupling Operations", link: "/en/decouple/decouple-operation" },
      { text: "Cargo Distribution when Decoupling", link: "/en/decouple/decouple-passenger" },
    ],
  },
  {
    text: "Train Coupling",
    link: "/en/couple/",
    collapsed: false,
    items: [
      { text: "Simple Train Coupling", link: "/en/couple/simple-couple" },
      { text: "Train Coupling Operations", link: "/en/couple/couple-operation" },
      { text: "Cross-Company Train Coupling", link: "/en/couple/cross-company-couple" },
    ],
  },
  { text: "Modular Airports", link: "/en/airport/" },
  {
    text: "Custom Order Lists",
    link: "/en/orderlist/",
    collapsed: false,
    items: [
      { text: "Editing Order Lists", link: "/en/orderlist/orderlist-edit" },
      { text: "Vehicles Using Custom Order Lists", link: "/en/orderlist/orderlist-vehicle" },
    ],
  },
  {
    text: "Vehicle Transport",
    link: "/en/veh-carry/",
    collapsed: false,
    items: [
      { text: "Vehicle Transport Order Settings", link: "/en/veh-carry/orders" },
      { text: "Cross-Company Vehicle Transport", link: "/en/veh-carry/cross-company" },
    ],
  },
  { text: "Blueprint and Undo", link: "/en/bluepoint/" },
  {
    text: "More Options",
    link: "/en/other-options/",
    collapsed: false,
    items: [
      { text: "Ban Trains from Waiting in Depots and Station Servicing", link: "/en/other-options/enable-depot" },
      { text: "Keeping Invite Codes Alive on Multiplayer Servers", link: "/en/other-options/invite-code-alive" },
      { text: "Rainy Weather", link: "/en/other-options/rainy" },
    ],
  },
];

const editPattern = "https://github.com/maicarons-forks/OpenTTD-patches/blob/px-patch/pxp-docs/:path";
const upstreamUrl = "https://github.com/pulsexlb/OpenTTD-patches";
// 项目站点 base：fork 与上游仓库同名，Pages 子路径一致
const BASE = "/OpenTTD-patches/";

export default defineConfig({
  lang: "zh-CN",
  title: "PX-Patch 文档",
  description: "PX-Patch 文档：列车解挂与对接、模块化机场、自定义调度计划表等。",
  lastUpdated: true,
  cleanUrls: true,
  base: BASE,
  head: [["link", { rel: "icon", type: "image/svg+xml", href: `${BASE}logo.svg` }]],

  locales: {
    root: {
      label: "简体中文",
      lang: "zh-CN",
      title: "PX-Patch 文档",
      description: "PX-Patch 文档：列车解挂与对接、模块化机场、自定义调度计划表等。",
      themeConfig: {
        nav: [
          { text: "文档首页", link: "/" },
          { text: "English", link: "/en/" },
          { text: "GitHub", link: upstreamUrl },
        ],
        sidebar: zhSidebar,
        outline: { label: "本页目录" },
        docFooter: { prev: "上一页", next: "下一页" },
        lastUpdated: { text: "最后更新" },
        editLink: { pattern: editPattern, text: "在 GitHub 上编辑此页" },
      },
    },
    en: {
      label: "English",
      lang: "en-US",
      link: "/en/",
      title: "PX-Patch Docs",
      description: "PX-Patch documentation: train coupling/decoupling, modular airports, custom order lists and more.",
      themeConfig: {
        nav: [
          { text: "中文", link: "/" },
          { text: "Home", link: "/en/" },
          { text: "GitHub", link: upstreamUrl },
        ],
        sidebar: enSidebar,
        outline: { label: "On this page" },
        docFooter: { prev: "Previous page", next: "Next page" },
        lastUpdated: { text: "Last updated" },
        editLink: { pattern: editPattern, text: "Edit this page on GitHub" },
      },
    },
  },

  themeConfig: {
    logo: "/logo.svg",
    socialLinks: [
      { icon: "github", link: upstreamUrl },
    ],
    search: { provider: "local" },
    footer: {
      message: "PX-Patch Docs · CC BY-NC-SA · By PulseX",
      copyright: "Docs rebuilt with VitePress",
    },
  },
});
