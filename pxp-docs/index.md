---
layout: home
title: PX-Patch 文档
titleTemplate: false

hero:
  name: PX-Patch 文档
  text: 列车解挂与对接 · 模块化机场 · 自定义调度计划
  tagline: 基于 OpenTTD JGRPP 的新补丁，附完整中英文使用说明。
  actions:
    - theme: brand
      text: 开始阅读
      link: /decouple/
    - theme: alt
      text: English Docs
      link: /en/
    - theme: alt
      text: GitHub Release
      link: https://github.com/pulsexlb/OpenTTD-patches/releases/

features:
  - title: 列车解挂与对接
    details: 在车站中解挂、重组、对接列车，支持跨公司对接、调度计划衔接与条件跳过。
    link: /decouple/
  - title: 模块化机场
    details: 自定义机场区域、跑道、滑行道、停机位与景观设施，支持滑行机与垂起机。
    link: /airport/
  - title: 自定义调度计划表
    details: 玩家可命名、可分组、可公开的调度计划表，载具可用“执行调度计划”复用。
    link: /orderlist/
  - title: 载具运输
    details: 火车 / 汽车 / 轮船 / 飞机互运载具，支持重量、站台与跨公司计费限制。
    link: /veh-carry/
  - title: 蓝图与撤回
    details: 快速复制基础设施、查看建造历史并撤回最近操作。
    link: /bluepoint/
  - title: 更多选项
    details: 车库等待与车站维修禁令、联机邀请码保活、随机下雨天气。
    link: /other-options/
---

## 在阅读之前

px-patch 是 OpenTTD 的一个新补丁，基于 OpenTTD JGRPP 版本开发。在阅读此文档之前，您应已经熟悉游戏 OpenTTD 和 JGR Patches。如果您还不了解这个游戏，可阅读 [OpenTTD 社区中文文档](https://ottdzh.readthedocs.io/zh-cn/latest/)、[JGRPP 社区中文文档](https://ottdzh.readthedocs.io/projects/jgrpp/latest/readme.html)。

## 开源与更新

px-patch 基于 GPLv2 许可证开源至 [GitHub（pulsexlb/OpenTTD-patches）](https://github.com/pulsexlb/OpenTTD-patches)，可在 [GitHub Release](https://github.com/pulsexlb/OpenTTD-patches/releases/) 上下载最新版本并保持更新。

::: warning 注意
此分支大量使用大语言模型编写代码，项目可能不稳定。请及时在 GitHub Release 上获取最新版本，往往包含最新的问题修复。
:::

## 全部章节

- [列车解挂](/decouple/)：[简单的列车解挂](/decouple/simple-decouple) · [解挂列车操作](/decouple/decouple-operation) · [解挂时客流分配](/decouple/decouple-passenger)
- [列车对接](/couple/)：[简单的列车对接](/couple/simple-couple) · [列车对接操作](/couple/couple-operation) · [跨公司列车对接](/couple/cross-company-couple)
- [模块化机场](/airport/)
- [自定义调度计划表](/orderlist/)：[编辑调度计划表](/orderlist/orderlist-edit) · [载具使用自定义调度计划表](/orderlist/orderlist-vehicle)
- [载具运输](/veh-carry/)：[载具运输调度计划设置](/veh-carry/orders) · [跨公司载具运输](/veh-carry/cross-company)
- [蓝图与撤回](/bluepoint/)
- [更多选项](/other-options/)：[禁止车库停放启动的列车和车站维修列车](/other-options/enable-depot) · [联机服务器邀请码保活](/other-options/invite-code-alive) · [下雨天气](/other-options/rainy)
