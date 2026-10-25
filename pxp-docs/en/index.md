---
layout: home
title: PX-Patch Docs
titleTemplate: false

hero:
  name: PX-Patch Docs
  text: Train Coupling & Decoupling · Modular Airports · Custom Order Lists
  tagline: A new patch for OpenTTD based on JGRPP, with full bilingual documentation.
  actions:
    - theme: brand
      text: Get Started
      link: /en/decouple/
    - theme: alt
      text: 中文文档
      link: /
    - theme: alt
      text: GitHub Release
      link: https://github.com/pulsexlb/OpenTTD-patches/releases/

features:
  - title: Train Coupling & Decoupling
    details: Decouple, rearrange and couple trains inside stations, with cross-company coupling, order hand-off and conditional jumps.
    link: /en/decouple/
  - title: Modular Airports
    details: Custom airport areas, runways, taxiways, aprons and landscaping for taxiing and VTOL aircraft.
    link: /en/airport/
  - title: Custom Order Lists
    details: Player-defined, nameable, groupable and shareable order lists reusable via "Execute schedule".
    link: /en/orderlist/
  - title: Vehicle Transport
    details: Trains, road vehicles, ships and aircraft carrying each other, with weight, platform and cross-company fee rules.
    link: /en/veh-carry/
  - title: Blueprint and Undo
    details: Quickly copy infrastructure, browse construction history and undo recent work.
    link: /en/bluepoint/
  - title: More Options
    details: Depot-waiting and station-servicing bans, multiplayer invite-code keep-alive, random rainy weather.
    link: /en/other-options/
---

## Before reading

px-patch is a new patch for OpenTTD, developed on top of OpenTTD JGRPP. Before reading this documentation, you should already be familiar with OpenTTD and JGR Patches. If you are not yet familiar with the game, you can read the [OpenTTD documentation](https://wiki.openttd.org/) and the [JGRPP documentation](https://github.com/JGRennison/OpenTTD-patches/wiki).

## Open source & updates

px-patch is open-sourced under the GPLv2 license at [GitHub (pulsexlb/OpenTTD-patches)](https://github.com/pulsexlb/OpenTTD-patches); the latest version can be downloaded from [GitHub Release](https://github.com/pulsexlb/OpenTTD-patches/releases/) and kept up to date.

::: warning Please note
This branch uses large language models extensively to write code, and the project may be unstable. Please grab the latest version from GitHub Release in time, as it usually contains the newest bug fixes.
:::

## All chapters

- [Train Decoupling](/en/decouple/): [Simple Train Decoupling](/en/decouple/simple-decouple) · [Train Decoupling Operations](/en/decouple/decouple-operation) · [Cargo Distribution when Decoupling](/en/decouple/decouple-passenger)
- [Train Coupling](/en/couple/): [Simple Train Coupling](/en/couple/simple-couple) · [Train Coupling Operations](/en/couple/couple-operation) · [Cross-Company Train Coupling](/en/couple/cross-company-couple)
- [Modular Airports](/en/airport/)
- [Custom Order Lists](/en/orderlist/): [Editing Order Lists](/en/orderlist/orderlist-edit) · [Vehicles Using Custom Order Lists](/en/orderlist/orderlist-vehicle)
- [Vehicle Transport](/en/veh-carry/): [Vehicle Transport Order Settings](/en/veh-carry/orders) · [Cross-Company Vehicle Transport](/en/veh-carry/cross-company)
- [Blueprint and Undo](/en/bluepoint/)
- [More Options](/en/other-options/): [Ban Trains from Waiting in Depots and Station Servicing](/en/other-options/enable-depot) · [Keeping Invite Codes Alive on Multiplayer Servers](/en/other-options/invite-code-alive) · [Rainy Weather](/en/other-options/rainy)
