export const meta = {
  name: 'yc-handbook',
  description: 'Synthesize bilingual thematic startup handbook from per-video notes',
  phases: [
    { title: 'Chapters', detail: 'one agent per thematic chapter, reads its notes' },
    { title: 'Intro', detail: 'write 00 introduction after chapters exist' },
  ],
}

// 章节定义为静态;每个章节 agent 自行从磁盘读取 scripts/workflows/handbook_args.json 拿到本章 ids
const CHAPTERS = [
  { num: 1, key: 'mindset',     zh: '创始人心态与素质',    en: 'Founder Mindset & Traits',        scope: '创业动机、韧性、信念、创始人特质、决策心态与自我管理' },
  { num: 2, key: 'idea',        zh: '找方向与选 idea',     en: 'Finding & Choosing Ideas',        scope: '如何寻找/评估创业点子、Request for Startups、AI-native 机会、市场与赛道选择' },
  { num: 3, key: 'validation',  zh: '验证需求与和用户对话', en: 'Validation & Talking to Users',   scope: '需求验证、用户访谈、validation vs committing、早期信号判断' },
  { num: 4, key: 'mvp_pmf',     zh: '做 MVP 与找到 PMF',   en: 'MVP & Product-Market Fit',        scope: '构建 MVP、快速迭代、找到并度量 product-market fit' },
  { num: 5, key: 'growth',      zh: '增长与获客',          en: 'Growth & Distribution',           scope: "获客、分发渠道、do things that don't scale、销售与增长策略" },
  { num: 6, key: 'fundraising', zh: '融资与申请 YC',       en: 'Fundraising & Applying to YC',    scope: '融资、pitch、估值与条款、如何申请并通过 YC' },
  { num: 7, key: 'team',        zh: '联合创始人与团队',     en: 'Co-founders & Team',              scope: '寻找联合创始人、招聘、团队协作与公司文化' },
  { num: 8, key: 'ai_agent',    zh: 'AI / Agent 时代专题', en: 'The AI / Agent Era',              scope: 'agent-first 产品、YC 对 AI/agent 的判断、护城河与切入点、AI 时代的创业机会与打法' },
  { num: 9, key: 'pitfalls',    zh: '常见陷阱与反模式',     en: 'Common Pitfalls & Anti-patterns', scope: '创始人常犯的错误、反模式、失败教训与如何规避' },
]

const pad = (n) => String(n).padStart(2, '0')

const chapterPrompt = (ch) => `You are writing ONE chapter of a **bilingual (中文/English) startup handbook** synthesized from Y Combinator talks, for a reader who is an **AI-Agent engineer about to start a startup**. Repo: \`/home/gaoxin/workplace/startup_guidance\`.

CHAPTER ${ch.num}: **${ch.zh} / ${ch.en}**
SCOPE: ${ch.scope}

STEP 1 — find your source notes: read \`scripts/workflows/handbook_args.json\`, locate the chapter object whose \`key\` == "${ch.key}", and take its \`ids\` array. Those are the most relevant videos for this chapter.
STEP 2 — read the corresponding \`notes/<id>.md\` files (prioritize the most on-topic; skip any that turn out tangential).
STEP 3 — write \`handbook/${pad(ch.num)}-${ch.key}.md\` as a SYNTHESIZED chapter (weave cross-video principles together — NOT a list of per-video summaries). Structure:

# 第 ${ch.num} 章 · ${ch.zh} / ${ch.en}

> {2–3 句中文导语:这一章解决什么、为什么对 AI Agent 创始人重要}

## 核心原则 / Core Principles
{把跨视频反复出现的原则提炼成 4–7 个小节。每个小节:}
### {原则中文标题} / {English title}
{中文讲解:观点 + 逻辑 + 常见误区,3–6 句}
> 🗣️ "{从某个 note 里摘取的英文金句(保持逐字)}" —— {讲者/来源视频简称}
> 译:{中文翻译}
**🤖 对 AI Agent 创始人**: {1–3 句,把该原则落到做 AI Agent 创业的具体含义/动作}

## ⚡ 本章行动清单 / Action Checklist
- [ ] {5–8 条贯穿全章、可执行}

## 📚 本章取材视频 / Sources
{列出你实际引用/参考的视频:}
- [{English title}](https://www.youtube.com/watch?v={id}) — {一句中文说明它贡献了什么观点} (\`notes/{id}.md\`)

RULES:
- 中英双语:正文中文为主,关键概念/术语给英文;金句保留英文原文 + 中文翻译。
- Synthesize across sources — group ideas by principle, not by video. Cite which video each key quote/idea comes from.
- Concrete, high-signal, specific to what these YC talks actually say. No generic filler.

Return one-line JSON: {"chapter":${ch.num},"key":"${ch.key}","path":"handbook/${pad(ch.num)}-${ch.key}.md","sources_used":<int>}`

phase('Chapters')
const chapterResults = await parallel(CHAPTERS.map((ch) => () =>
  agent(chapterPrompt(ch), { label: `ch:${ch.num}-${ch.key}`, phase: 'Chapters', agentType: 'general-purpose' })
))

phase('Intro')
const introPrompt = `Write the introduction / how-to-use page for a **bilingual (中文/English) YC startup handbook** aimed at an **AI-Agent engineer about to start a startup**. Repo: \`/home/gaoxin/workplace/startup_guidance\`.

The handbook is synthesized from **80 recent Y Combinator videos** (2026), via local Whisper 转写 + pyannote 说话人分离 → 逐视频双语笔记(\`notes/\`)→ 主题综合。Chapters already written in \`handbook/\`:
${CHAPTERS.map((ch) => `- ${pad(ch.num)}-${ch.key}.md — ${ch.zh} / ${ch.en}`).join('\n')}
- 10-appendix.md — 视频索引 / Video Index

Write \`handbook/00-intro.md\` (中英双语,像一本真正手册的开篇):
# YC 创业手册 · 导言 / Introduction
- 中文导语:这套手册是什么、怎么来的、覆盖了什么。
- **给 AI Agent 创始人的推荐读法 / Reading paths**:按阶段(找方向 → 验证 → MVP/PMF → 增长 → 融资 → 团队)给出章节顺序建议;并单独点出 AI/Agent 专题(第 8 章)与护城河/陷阱(第 9 章)。
- **章节地图 / Chapter map**:列出全部章节(markdown 链接如 \`01-mindset.md\`)+ 每章一句话简介。
- 简短的"如何把它用起来"(结合每章行动清单 + 逐视频笔记 \`notes/\`)。
Return the string "intro-done".`
await agent(introPrompt, { label: 'ch:00-intro', phase: 'Intro', agentType: 'general-purpose' })

return { chapters: chapterResults.filter(Boolean) }
