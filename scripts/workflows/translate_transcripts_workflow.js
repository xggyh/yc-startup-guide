export const meta = {
  name: 'yc-translate-transcripts',
  description: 'Produce full bilingual (EN verbatim + 中文翻译) transcripts from diarized JSON',
  phases: [{ title: 'Translate', detail: 'one agent per video writes transcripts/<id>.bilingual.md' }],
}

let _a = args
if (typeof _a === 'string') { try { _a = JSON.parse(_a) } catch (e) { _a = {} } }
const ids = (_a && _a.ids) || (Array.isArray(_a) ? _a : [])
if (!ids.length) { log('no ids'); return { count: 0 } }
log(`translating ${ids.length} transcripts to bilingual`)

const RESULT_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['id', 'paragraphs', 'ok'],
  properties: { id: { type: 'string' }, paragraphs: { type: 'integer' }, ok: { type: 'boolean' } },
}

const prompt = (id) => `Produce a **full bilingual transcript** (English verbatim + 中文翻译) for a Y Combinator talk. Repo: \`/home/gaoxin/workplace/startup_guidance\`.

VIDEO ID: \`${id}\`
INPUT: \`transcripts/${id}.speaker.json\` — JSON with \`segments\` (each {start, end, text, speaker}) and \`num_speakers\`. (\`start\` is seconds.)

TASK: write \`transcripts/${id}.bilingual.md\` — the COMPLETE transcript, paragraph by paragraph, NOTHING summarized or omitted.

Grouping: merge consecutive segments into natural paragraphs of ~3–6 sentences; ALWAYS start a new paragraph when \`speaker\` changes. For each paragraph output exactly:

\`[mm:ss]\` **SPEAKER_xx:** {English text, verbatim, joined from the segments}

> {这一段的中文翻译:通顺、忠实、可读,不要逐字硬翻,但不得漏译或概括}

(Only include the \`SPEAKER_xx:\` label if num_speakers > 1; if single speaker, drop the label and just use \`[mm:ss]\` before the English.)
Convert \`start\` seconds → mm:ss. Put ONE blank line between the English line and the 中文 blockquote, and a blank line between paragraphs.

HARD RULES:
- Cover the ENTIRE transcript from first to last segment. Do NOT stop early, do NOT summarize, do NOT skip ranges. If it's long, keep going.
- English must be verbatim from the segments (you may fix obvious spacing/casing only).
- Output ONLY the paragraphs (no title/header — that's added elsewhere).

After writing the file, return {id:"${id}", paragraphs:<number of paragraphs written>, ok:true}.`

phase('Translate')
const res = await parallel(ids.map((id) => () =>
  agent(prompt(id), { label: `tr:${id}`, phase: 'Translate', agentType: 'general-purpose',
                      schema: RESULT_SCHEMA, effort: 'medium' })
))
const done = res.filter(Boolean)
log(`done: ${done.length}/${ids.length}`)
return { count: done.length, results: done }
