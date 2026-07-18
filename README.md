# YC 创业手册 · AI Agent 创始人版 / YC Startup Guide

从 **80 支 Y Combinator 近期(2026)视频**综合而成的**中英双语创业教程**,写给即将下场的 **AI Agent 工程师**。
A bilingual startup handbook synthesized from 80 recent Y Combinator talks — for AI-agent engineers about to build.

### 👉 在线阅读 / Read online: **https://xggyh.github.io/yc-startup-guide/**

[![Deploy](https://github.com/xggyh/yc-startup-guide/actions/workflows/deploy.yml/badge.svg)](https://github.com/xggyh/yc-startup-guide/actions/workflows/deploy.yml)

---

## 里面有什么 / What's inside

- **`handbook/`** — 9 章 + 附录的**中英双语主题手册**。每章把跨视频的共识提炼成 6–7 个"核心原则",配讲者原话金句(英文原文 + 中文翻译)与「🤖 对 AI Agent 创始人」的落地建议:
  1. 创始人心态与素质 · 2. 找方向与选 idea · 3. 验证需求与用户对话 · 4. 做 MVP 与找到 PMF ·
  5. 增长与获客 · 6. 融资与申请 YC · 7. 联合创始人与团队 · **8. AI / Agent 时代专题** · 9. 常见陷阱与反模式
- **`notes/`** — **80 篇逐视频双语笔记**。每篇:中文 TL;DR + 按章节/时间戳的分段精读(英文金句 + 中文小结) + 给 AI Agent 创始人的行动项 + 术语表 + 高价值金句时间戳。
- **`docs/` + `mkdocs.yml`** — MkDocs Material 站点,GitHub Actions 自动部署到 Pages。

## 怎么来的 / How it was built

全流程本地运行(RTX 4090),脚本见 `scripts/`:

```text
80 支 YC YouTube 视频(只下音频, yt-dlp)
   → 本地 Whisper large-v3 转写(faster-whisper)
   → pyannote 说话人分离(谁在说)
   → 逐视频双语笔记 notes/<id>.md(并行生成)
   → 跨视频主题综合 → handbook/ 各章
   → MkDocs Material 站点 → GitHub Pages
```

| 脚本 | 作用 |
|---|---|
| `scripts/01_build_list.sh` | 生成待下载视频清单 |
| `scripts/02_download.sh` | 只下音频 + 字幕 + 元数据 |
| `scripts/03_transcribe.py` | faster-whisper 批量转写 |
| `scripts/04_diarize.py` | pyannote 说话人分离 |
| `scripts/workflows/*.js` | 并行生成笔记 / 综合手册 |
| `scripts/build_site.py` | 生成 MkDocs 站点 |

## 本地预览 / Local preview

```bash
pip install mkdocs-material
mkdocs serve   # http://127.0.0.1:8000
```

## 更新站点 / Update

改完内容后 `python scripts/build_site.py` 重建 `docs/`,`git push` 即自动重新部署。

---

> 内容为对 Y Combinator 公开视频的学习性转写与综合,仅供个人学习;版权归原作者/YC 所有。
> Educational synthesis of public YC videos, for personal study only.
