# YC 创业手册 · AI Agent 创始人版

> 从 **80 支 Y Combinator 近期(2026)视频**综合而成的**中英双语创业教程**,写给即将下场的 **AI Agent 工程师**。
> A bilingual startup handbook synthesized from 80 recent Y Combinator talks — for AI-agent engineers about to build.

<div class="grid" markdown>

| 指标 Metric | 值 |
|---|---|
| 视频 Videos | **80** |
| 音频时长 Audio | **~43.8 h** |
| 转写词数 Words | **~530k** |
| 手册章节 Chapters | **9 + 附录** |
| 逐视频双语笔记 Notes | **80** |

</div>

## 🚀 怎么读 / Reading paths

- **想清楚要不要干** → [第 1 章 心态](handbook/01-mindset.md)
- **找方向 / 选 idea** → [第 2 章 选题](handbook/02-idea.md) → [第 3 章 验证](handbook/03-validation.md)
- **动手做产品** → [第 4 章 MVP/PMF](handbook/04-mvp_pmf.md) → [第 5 章 增长](handbook/05-growth.md)
- **融资与团队** → [第 6 章 融资](handbook/06-fundraising.md) → [第 7 章 团队](handbook/07-team.md)
- **本时代的核心题** → ⭐ [第 8 章 AI / Agent 专题](handbook/08-ai_agent.md) → [第 9 章 陷阱](handbook/09-pitfalls.md)

## 📖 章节地图 / Chapters

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

## 🧭 也可以直接看

- [手册导言](handbook/00-intro.md) — 完整的使用说明
- [视频索引附录](handbook/10-appendix.md) — 80 支视频一览 + 对应笔记
- **逐视频双语笔记** — 左侧「逐视频笔记 Notes」按主题浏览全部 80 篇

---

## 🛠️ 怎么来的 / How it was built

```text
80 支 YC YouTube 视频(只下音频)
   → 本地 Whisper large-v3 转写(RTX 4090)
   → pyannote 说话人分离(谁在说)
   → 逐视频双语笔记 notes/<id>.md
   → 跨视频主题综合 → handbook/ 各章
```

全流程本地运行、脚本开源(见仓库 `scripts/`)。
