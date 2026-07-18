export const meta = {
  name: 'yc-notes',
  description: 'Generate bilingual per-video study notes from YC transcripts (one agent per video)',
  phases: [{ title: 'Notes', detail: 'one general-purpose agent per video writes notes/<id>.md' }],
}

// args = { ids: [videoId, ...] }  —— 由外部从磁盘计算后传入(workflow 脚本无文件系统权限)
// args 可能以对象或 JSON 字符串形式到达 -> 两种都兼容
let _a = args
if (typeof _a === 'string') { try { _a = JSON.parse(_a) } catch (e) { _a = {} } }
const ids = (_a && _a.ids) || (Array.isArray(_a) ? _a : [])
if (!ids.length) { log('no ids passed in args.ids'); return { notes: [] } }
log(`generating notes for ${ids.length} videos`)

const SUMMARY_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['id', 'zh_title', 'en_title', 'one_liner_zh', 'themes', 'top_takeaways_zh'],
  properties: {
    id: { type: 'string' },
    zh_title: { type: 'string' },
    en_title: { type: 'string' },
    one_liner_zh: { type: 'string' },
    themes: {
      type: 'array',
      items: { enum: ['mindset','idea','validation','mvp_pmf','growth','fundraising','team','ai_agent','pitfalls'] },
    },
    top_takeaways_zh: { type: 'array', items: { type: 'string' } },
    note_path: { type: 'string' },
  },
}

const notePrompt = (id) => `You are generating a bilingual (中文/English) study note from a Y Combinator YouTube talk transcript, for a reader who is an **AI-Agent engineer planning to start a startup**. Work in the repo \`/home/gaoxin/workplace/startup_guidance\`.

VIDEO ID: \`${id}\`

INPUT FILES (read all that exist):
- Speaker-tagged transcript (PREFERRED if present): \`transcripts/${id}.speaker.txt\` — lines like \`[mm:ss] SPEAKER_00: ...\`. Use it to attribute quotes; map SPEAKER_xx to real names when the transcript makes the identity clear (e.g. an intro "I'm Garry Tan"), otherwise keep SPEAKER_xx.
- Plain transcript: \`transcripts/${id}.txt\` (full English text)
- Timestamps: \`transcripts/${id}.json\` (segments: {start,end,text} in seconds) — convert \`start\` to mm:ss for quote/section timestamps.
- Metadata: \`yc_video/metadata/${id}.info.json\` — use \`title\`, \`upload_date\` (YYYYMMDD→YYYY-MM-DD), \`duration\` (sec→mm:ss), and \`chapters\` (list of {start_time,title}) for section structure if present.

Write the note to \`notes/${id}.md\` using EXACTLY this structure:

# {中文标题} / {English Title}

> **来源**: [{English Title}](https://www.youtube.com/watch?v=${id}) · Y Combinator · {YYYY-MM-DD} · 时长 {mm:ss}
> **讲者**: {若能判断,列出讲者/嘉宾;podcast 多人则列主持与嘉宾}
> **一句话定位**: {一句中文,说明解决什么创业问题、对 AI Agent 创始人的价值}

## 🎯 TL;DR(中文核心要点)
- {5–8 条,具体可执行,不要空话}

## 🧭 适合谁 / 什么时候看
- {2–4 条}

## 📝 分段精读
{按 chapters 分段;无 chapters 则按逻辑切 4–8 段}
### {序号}. {中文标题} / {English title} \`[mm:ss–mm:ss]\`
**要点(中文)**: {2–5 句提炼论点与逻辑}
> 🗣️ "{逐字摘自 transcript 的英文金句}" {—— 讲者/SPEAKER_xx,若有}
> 译:{中文翻译}
{每段挑 1–3 句最值钱的金句}

## 🚀 给 AI Agent 创始人的行动项
- [ ] {3–6 条,把经验落到"做 AI Agent 创业"的具体动作}

## 🔑 关键术语 / 概念
- **{Term}** — {中文解释}
{没有就写 (无)}

## 🔖 高价值金句时间戳
- \`[mm:ss]\` "{quote}" — {中文一句话点评}
{3–6 条}

RULES:
- 🗣️ English quotes MUST be verbatim from the transcript. Chinese 小结/翻译 written by you, faithful & idiomatic.
- Be concrete & specific to THIS talk; no generic filler. Tight & high-signal.
- Also write a machine summary to \`notes/${id}.summary.json\` with the same fields as your structured reply.

After writing both files, return the structured summary object (id, zh_title, en_title, one_liner_zh, themes ⊆ [mindset,idea,validation,mvp_pmf,growth,fundraising,team,ai_agent,pitfalls], top_takeaways_zh, note_path="notes/${id}.md").`

phase('Notes')
const results = await parallel(ids.map((id) => () =>
  agent(notePrompt(id), {
    label: `note:${id}`, phase: 'Notes',
    agentType: 'general-purpose', schema: SUMMARY_SCHEMA,
  })
))
const notes = results.filter(Boolean)
log(`done: ${notes.length}/${ids.length} notes generated`)
return { count: notes.length, notes }
