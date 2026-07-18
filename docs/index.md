# YC 创业手册 · AI Agent 创始人版

> 从 **80 支 Y Combinator 近期(2026)视频**综合而成的**中英双语创业教程**,写给即将下场的 **AI Agent 工程师**。
> A bilingual startup handbook synthesized from 80 recent Y Combinator talks — for AI-agent engineers about to build.

## 📚 三个部分怎么配合 / Three parts

<div class="grid cards" markdown>

-   __① 逐视频精读 · One-page__

    每支视频一页,学完就知道它讲了什么:中文 TL;DR + 分段精读(英文金句 + 中文小结)+ 给 AI Agent 创始人的行动项。每页顶部可**一键跳到该视频的全文转录**。

    [:octicons-arrow-right-24: 进入精读](notes/-7Qz7tSTfUU.md)

-   __② 创业手册 · Handbook__

    把 80 支视频的共识抽象成 9 章「核心原则 + 行动清单」,**跟着学、跟着做**。

    [:octicons-arrow-right-24: 从导言开始](handbook/00-intro.md)

-   __③ 全量转录 · Transcripts__

    每支视频的**完整逐字转录**(带时间戳与说话人),从精读页跳转过来,想深挖细节时用。

    [:octicons-arrow-right-24: 视频索引](handbook/10-appendix.md)

</div>

**建议路径**:先在 ② 手册建立框架 → 用 ① 精读逐支吃透 → 需要原话/细节时点进 ③ 转录。

## 🗺️ 手册章节地图 / Chapters

<div class="grid cards" markdown>

-   __第 1 章 · 创始人心态与素质__

    [:octicons-arrow-right-24: 阅读本章](handbook/01-mindset.md)

-   __第 2 章 · 找方向与选 idea__

    [:octicons-arrow-right-24: 阅读本章](handbook/02-idea.md)

-   __第 3 章 · 验证需求与用户对话__

    [:octicons-arrow-right-24: 阅读本章](handbook/03-validation.md)

-   __第 4 章 · 做 MVP 与找到 PMF__

    [:octicons-arrow-right-24: 阅读本章](handbook/04-mvp_pmf.md)

-   __第 5 章 · 增长与获客__

    [:octicons-arrow-right-24: 阅读本章](handbook/05-growth.md)

-   __第 6 章 · 融资与申请 YC__

    [:octicons-arrow-right-24: 阅读本章](handbook/06-fundraising.md)

-   __第 7 章 · 联合创始人与团队__

    [:octicons-arrow-right-24: 阅读本章](handbook/07-team.md)

-   __第 8 章 · AI / Agent 时代专题__

    [:octicons-arrow-right-24: 阅读本章](handbook/08-ai_agent.md)

-   __第 9 章 · 常见陷阱与反模式__

    [:octicons-arrow-right-24: 阅读本章](handbook/09-pitfalls.md)

</div>

---

## 🛠️ 怎么来的 / How it was built

```text
80 支 YC YouTube 视频(只下音频)
   → 本地 Whisper large-v3 转写(RTX 4090)
   → pyannote 说话人分离(谁在说)→ ③ 全量转录
   → 逐视频双语笔记 → ① 精读 one-page
   → 跨视频主题综合 → ② 手册
```

全流程本地运行、脚本开源(见仓库 `scripts/`)。
