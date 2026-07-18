# YC 内部 AI 手册:把公司变成"超级智能组织" / Inside YC's AI Playbook

📄 **[点此查看全文转录 / Full transcript »](../transcripts/B246K_G7mHU.md)**

> **来源**: [Inside YC's AI Playbook](https://www.youtube.com/watch?v=B246K_G7mHU) · Y Combinator · 2026-05-27 · 时长 46:30
> **讲者**: 主持 Garry Tan(SPEAKER_00);嘉宾 Pete Koomen(SPEAKER_02,Optimizely 创始人、YC 内部 agent 基础设施主导者、《Horseless Carriages》作者);Jared Friedman(SPEAKER_03,亲手写了 SQL 只读工具);另有两位 Lightcone 主持 Diana Hu 与 Harj Taggar(对应 SPEAKER_01 / SPEAKER_05,字幕未明确逐一对应,故保留标签)。
> **一句话定位**: 讲的不是"给产品加个 AI 功能",而是把 agent 变成整个组织运行的底层——对想做 AI Agent 创业的人,这是一份"如何用 agent + 共享上下文 + 自我改进 skill 把组织能力复利化"的一线实操蓝图。

## 🎯 TL;DR(中文核心要点)
- **别把 AI 当 co-pilot**,那是 2023 的玩法;要把它当成"所有工作的构建层(building layer)",并且开始把一切工件(会议记录、对话、转录稿)都录下来喂回系统。
- **最大的解锁是"上下文集中在一处"**:YC 把公司所有数据放在一个 Postgres 库里,给 agent **只读 SQL 权限**,就能用自然语言问任意复杂问题。上下文集中 > 到处接 MCP。
- **限制越少,威力越大**:Jared 半夜偷偷把"完整生产库访问权"给了 agent,结果好到离谱——真正卡住世界的是对安全/隐私的过度担忧(safetyism),敢放松一点就会发现这些东西强得可怕。
- **Jevons 悖论**:让问一个问题变得极其便宜后,你问的问题数量和复杂度会暴涨,而不是省下时间——组织的"提问带宽"被打开。
- **工具注册表(tool registry)是把 agent 变得"在工作里有用"的关键**:YC 从 20 个工具长到 350+,每个团队自己加工具,同一套工具既给内部 agent 用,也给每个人机器上的 Cloud Code 用。
- **自我改进循环 = 组织级超级智能**:把一个 skill(如"两句话简介")+ 真实使用的转录稿喂回去让 agent 自我改写,skill 会一夜变得"比我们任何单个人都强"。对所有工作重复这一步,就得到超级组织。
- **文化是硬前提**:要"egalitarian(平权)+ trust by default(默认信任)+ 默认公开广播"。默认公开反而成了一种社会性风控,让高信任小团队敢给 agent 大权限。
- **一次性时间穿越**:愿意每年在 token 上花 1–10 万美金 + 投入建 skill,你就"提前活在 2028",能一次性越过所有 Fortune 500 和现有创业公司。

## 🧭 适合谁 / 什么时候看
- 正在做 **AI Agent / agent harness / 内部工具平台** 的创始人,想看"多人 agent 基础设施"到底长什么样。
- 想把自己团队/公司改造成 **AI-native 组织** 的技术负责人(尤其是 2 年以上的"传统"组织)。
- 在纠结"agent 产品该做成 chat 还是自定义 UI"、"该不该给 agent 大权限"的人。
- 认同"AI 应赋能而非替代人"、关心 AI 中心化 vs 去中心化路线的人。

## 📝 分段精读

### 1. 起点:财务团队的问题,YC 为什么自建 AI 栈 / The Finance Team Problem That Started It All `[00:39–05:07]`
**要点(中文)**: YC 一直跑在自研软件上,所有关键数据都在自家系统里,这是它做 AI-native 的最大先发优势。一年多前 Pete 和几个工程师本要给财务团队搭一套确定性工具,但发现"工程师听懂复杂工作流→写死成 Ruby 软件→交还财务"这个循环极其低效;而同期 Cursor/Cloud Code 让个人"像有了超能力"。于是想法反转:不要让工程师夹在中间,直接给财务团队工具,让他们**用英语(prompt)而不是 Ruby 来编码自己的工作流**。
> 🗣️ "give the finance team the tools that they could use to encode their own workflows, not as, you know. Not as Ruby, but as English, with prompts, right?" —— Pete Koomen
> 译:给财务团队一套工具,让他们能自己编码自己的工作流——不是用 Ruby,而是用英语、用 prompt。

### 2. SQL 直连:一切的解锁,"一个数据库统治一切" / SQL Access & One Database to Rule Them All `[05:07–09:14]`
**要点(中文)**: 第一个魔法时刻不是 agentic coding,而是给 agent 两个工具:对生产库跑**只读 SQL**、读数据模型文件。Jared 承认自己"像在破规矩",半夜偷偷把完整库访问权推上线,结果好得离谱。关键洞察:YC 所有重要上下文都在**一个 Postgres 库、一套 schema** 里,配一点 schema 说明,agent 就能回答任意业务问题("过去四批里投过太空公司的投资人有哪些")。真正的护城河是"上下文集中",而不是把功能外包给一堆第三方 SaaS。
> 🗣️ "what if we just gave the thing... complete access to the production database, where we could just, like, trample on anything? ... the thing that was hampering the world was being worried about security and privacy... And when you, like, worry a bit less, you're like, oh, my god. These things are unbelievably powerful." —— Jared Friedman
> 译:干脆给它完整的生产库访问权、能随便动任何东西会怎样?……真正拖住世界的是对安全和隐私的担忧……当你敢少担心一点,就会惊觉:这些东西强得不可思议。
> 🗣️ "when all of that context is in one place, with a little bit of additional information about how the scheme is laid out, an agent can go and ask or answer arbitrary questions about our business." —— Pete Koomen
> 译:当所有上下文都在一处、再加一点关于 schema 布局的信息,agent 就能对我们的业务提出并回答任意问题。

### 3. Jevons 悖论 & 为 Agent 反规范化(G-Brain) / Jevons Paradox & Denormalizing for Agents `[09:14–12:15]`
**要点(中文)**: 让"问一个复杂问题"从"写几小时 SQL / 敲数据团队的门排 backlog"变成一句话,结果不是省时间,而是**提问的数量和复杂度暴涨**(Jevons 悖论)——以前不值得问的问题现在都会问。Garry 补充:这在数据侧正上演"Bigtable 化"——你要把散在各系统的数据**反规范化(denormalize)**成为 agent 检索优化的格式,配上 RAG / graph RAG / 重排,再"给 agent 一个灵魂 + 你的数据 + 它懂你",它就能"看到拐角后面的东西"。他倾向 CLI 而非 MCP。
> 🗣️ "it didn't just make it easier to answer questions. It dramatically increased the number of questions that we would ask and dramatically increased the scale and complexity of the questions that we would dare to ask." —— Jared Friedman
> 译:它不只是让回答问题更容易,而是极大地增加了我们会问的问题数量,以及我们敢问的问题的规模和复杂度。
> 🗣️ "you're going to denormalize it and you're going to put it in a format that is optimized for agent retrieval and understanding." —— Garry Tan
> 译:你要把它反规范化,放进一个为 agent 检索和理解而优化的格式里。

### 4. 从单人到多人:共享工具注册表(350+)、Skillify 与 DRY/MECE / The Single-Player Era, 350 Tools, Skillify `[12:15–18:23]`
**要点(中文)**: Pete 判断我们仍在 agent 的"单人时代"——Cloud Code / Codex / Pi / OpenClaw / Hermes 都是"一个人一台机器"。**尚未被解决的大问题是"多人 harness"**:把这种超能力提升到团队/组织层面。YC 的基础设施就是在探索哪些原语能做到这点:①一个集中的上下文层(数据仓库);②一个**内部工具注册表**——从 20 个工具长到 **350+**,每个团队自己加,同一套工具既供内部 agent 也供个人的 Cloud Code。Garry 补充了 Skillify(把有效做法自动固化成 skill)和 **check-resolvable** 元技能:让 skill 表保持 DRY(别重复)+ MECE(互斥且穷尽),模型天生懂这两个词,于是"一个带参数的 skill" 胜过"十个做同一件事的 skill"。
> 🗣️ "one of the big problems that I don't think has been solved well yet by anybody is the multiplayer harness, right? It's enabling that kind of superpower, but on a team or an organizational level." —— Pete Koomen
> 译:我认为还没被任何人很好解决的大问题,是"多人 harness"——把这种超能力扩展到团队或组织层面。
> 🗣️ "there's more than 350 today. I just checked... Every team is adding their own tools." —— Pete Koomen
> 译:今天已经有 350 多个工具了,我刚查过……每个团队都在加自己的工具。
> 🗣️ "it's bad to have 10 skills that do all the same thing it's good to have one skill or one tool that has parameters that then let you call them." —— Garry Tan
> 译:有十个做同一件事的 skill 是糟糕的;好的做法是一个带参数、能被调用的 skill 或工具。

### 5. 自我改进循环 & "两句话简介" skill:超级智能如何复利 / The Self-Improving Cycle & How Super Intelligence Compounds `[18:23–25:10]`
**要点(中文)**: 演进路径是:自己写 system prompt → 写 skill → meta-prompt 让 AI 自动改进 prompt → **自主自改进循环**。样例是 YC 的"两句话简介(two-sentence description)"skill:某合伙人先手写,后来几位合伙人在一次 group office hours 让每个创始人试写、给反馈,把这场会议的**转录稿**喂回去说"根据你读到的内容改进这个 skill",skill 就明显变强——"现在它比我更会写"。Garry 把这升华成方法论:对你做的**每一件事**都这样做(有人写 prompt→大家用→产生工件→用工件 meta-prompt 每天自动改进),组织就变成超级组织。**也正因此你应该去创业**:大多数掌权者不信这套、把上下文锁死,而你不受此限。
> 🗣️ "given... what you've learned by reading through this context improve the two-sentence description skill and they got noticeably better after that... this thing is now better than i am... at writing those." —— Pete Koomen
> 译:"根据你读这些上下文学到的东西,改进这个两句话简介 skill"——之后它明显变好了……现在它写得比我还好。
> 🗣️ "how do you build super intelligence inside a company you do that on everything you do and it's not more complicated than that like you literally just compose everything that you do." —— Garry Tan
> 译:怎么在公司内部造出超级智能?就是把这件事做在你做的每一件事上,没有比这更复杂;你只是把你做的每一件事组合起来。
> 🗣️ "that's why you should start a startup because people are going to be trapped in organizations... that do not believe what we just said because they keep all the contacts locked down." —— Garry Tan
> 译:这正是你该创业的原因——很多人会被困在那些不相信我们刚说的话、把上下文全锁死的组织里。

### 6. 把一切录下来 · 共享的组织大脑 · 默认信任 · 抬高地板 / Recording Everything, the Shared Brain, Trust-Default & Raising the Floor `[25:10–32:35]`
**要点(中文)**: 别把 AI 当 co-pilot,要当"所有事的构建层",并**录下所有工件**(这也是会议记录器爆火的原因)。一个"两句话简介 skill"不只是生成文本,而是让每个人接入 Diana、Harj 等人多年沉淀下来的判断——"共享的组织大脑""最接近把我们的大脑连起来"。YC 做对的几个反直觉选择:agent 对话**默认全员可见**、广播到 Slack 频道——这带来两个必需特质:**平权 + 默认信任**;而"默认公开"本身构成社会性风控,反而让高信任团队敢放开权限。它还**抬高了地板**:新人本要 6 个月上手,现在自动继承公司上下文、以"学徒制"方式模仿明星员工;那些不好意思问人的蠢问题,现在都敢问 agent。代价:每年在 token 上花 1–10 万美金,但这让你**提前活在 2028**,一次性越过所有在位者。
> 🗣️ "Part of the key thing is not to just use AI as a co-pilot. This is the thing where you use it as the building layer for everything and you need to start recording all the artifacts." —— SPEAKER_01
> 译:关键之一是别只把 AI 当 co-pilot;要把它当成一切的构建层,并且开始录下所有工件。
> 🗣️ "you have to be relatively egalitarian and you also have to be trust by default." —— Garry Tan
> 译:你必须相对平权,而且必须默认信任。
> 🗣️ "there's a one-time time warp where you can leapfrog every incumbent all fortune 500s all startups that exist by doing this." —— Garry Tan
> 译:这是一次性的时间穿越——靠这么做,你可以一次越过所有在位者、所有 Fortune 500、所有现存创业公司。
> 🗣️ "they know how the best people... do things by apprenticeship automatically with AI." —— SPEAKER_01
> 译:他们通过 AI 自动地、以学徒方式,学会组织里最优秀的人是怎么做事的。

### 7. Horseless Carriages · Chat 是最好的界面 · Just-in-Time 软件 / Horseless Carriages, Chat Interface & Just-in-Time Software `[32:35–40:49]`
**要点(中文)**: Pete 的爆款文《Horseless Carriages》批评当时的 AI 软件"在一大堆确定性软件里塞一小块 AI",还把 prompt 上下文对用户藏起来(典型 safetyism)。真正的方向是**控制权从开发者转移到用户**,未来软件会是"agent 包裹确定性工具",而不是"确定性软件包裹 AI"。界面之争:大家一开始以为 chat 不是终极 UI,但用下来结论是——**chat 就是好**:它最接近人类语言,而语言/写作最接近思维的表达,是通向智能最近的踏脚石;你越信任 agent,越不需要 UI。由此引出"**just-in-time software**":需要时 agent 现场生成一个只为此刻定制的单页应用/skill。Garry 举例自己用 Cloud Code 三天写 4 万行做开源的 G-Brain,让团队直接用 OpenClaw + Telegram + 他的检索系统,而不再维护 50 万行 Rails。最佳 AI 软件都"极小"——只写"让模型发光所需的最少代码"。
> 🗣️ "the potential for AI is to shift control of software from the developer to the user." —— Pete Koomen
> 译:AI 的潜力在于把软件的控制权从开发者转移到用户手里。
> 🗣️ "it's going to look a lot more like the agent wrapping software deterministic tools rather than deterministic software wrapping in AI." —— Pete Koomen
> 译:未来更像是 agent 包裹着确定性工具,而不是确定性软件里包着一点 AI。
> 🗣️ "why chat is probably the better interface is because it's the closest thing to human language... So chat is the closest stepping stone to clear intelligence." —— SPEAKER_01
> 译:chat 之所以可能是更好的界面,是因为它最接近人类语言……所以 chat 是通向清晰智能最近的踏脚石。
> 🗣️ "The best AI software that I've used... tend to be very small and just add kind of the smallest amount of code ahead of time that you need in order to let the model shine." —— Pete Koomen
> 译:我用过最好的 AI 软件往往都很小,只事先加上"让模型发光"所需的最少代码。

### 8. 中心化 vs 去中心化 & 个人 AI 革命 / Centralizing vs. Decentralizing AI & The Personal AI Revolution `[40:49–46:30]`
**要点(中文)**: AI 既可能中心化也可能去中心化,而 Gmail"不让你改 prompt"就是中心化的缩影。未来 18–24 个月要在两条路里选:一是"1984"式——五个巨头垄断算力与模型、连你的 prompt 都不让你碰,AI"发生在你身上,你活在 API 线以下";二是"个人电脑/Homebrew Computer Club"式——像当年 Apple I 一样,让十亿人**自己运行、自己改 prompt、自己选模型(甚至开源权重)、拥有只属于自己的私有仓库**。这正是 G-Brain / OpenClaw / Hermes 想推动的"真正的个人 AI 时刻"。Pete 收尾:每次看到把 AI 框定为"替代人"他都很抵触——它是**赋能**,延续了从大型机→PC→互联网的个人赋能叙事,消除让工作痛苦的杂役。这些都是选择,而看视频的人就是要去建这些东西的人。
> 🗣️ "This should be an extension of yourself and what you care about, not what... meta or alphabet or even opening our anthropic care about." —— Garry Tan
> 译:这应该是你自己、你所在乎之事的延伸,而不是 Meta、Alphabet、甚至 OpenAI 或 Anthropic 所在乎的东西。
> 🗣️ "I always really bristle when I see AI framed as a way to replace people... Not for humans, but as a thing that empowers." —— Pete Koomen
> 译:每次看到 AI 被塑造成"替代人"我都很反感……它不是替代人类,而是一种赋能的东西。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **先把上下文收拢到一处再谈 agent**:与其到处接 MCP,不如把关键数据 denormalize 进一个为 agent 检索优化的库/schema,配 schema 说明 + RAG/重排——这是 YC 全部魔力的根。
- [ ] **从"只读 SQL / 读模型文件"这种小而狠的工具起步**,验证"非技术但聪明的人能用自然语言问复杂问题",而不是一开始就做大而全的 UI。
- [ ] **把产品做成"agent 包裹确定性工具"**,只写"让模型发光的最少代码";别做"确定性软件里塞一小块 AI",别把 prompt 对用户藏起来(拒绝 safetyism)。
- [ ] **建一个 DRY + MECE 的工具/skill 注册表(resolver)**,同一套工具既供你的产品 agent 也供团队的 Cloud Code;上线一个"check-resolvable"式元技能防止 skill 重复膨胀。
- [ ] **搭自我改进循环**:把真实使用的会议/对话**转录稿**当作训练燃料,让 agent 读完后自动改写对应 skill——这是你产品护城河的复利来源。
- [ ] **把创业公司文化设成 egalitarian + trust-by-default + 默认公开广播**(agent 对话进共享频道):既让大家互相学会用法,又用"默认公开"当社会性风控来敢于放开权限。
- [ ] **预算上敢在 token 上花钱(团队级每年 1–10 万美金量级)**,把它当作"提前活在 2028"的越迁成本,而不是省钱对象。
- [ ] **押注去中心化/个人 AI**:让用户能自带模型、改自己的 prompt、拥有私有仓库——把"控制权交给用户"做成产品定位,而非又一个锁死的 API 之上的壳。

## 🔑 关键术语 / 概念
- **Harness(harness / 单人 vs 多人)** — 承载 agent 运行的外壳/框架(Cloud Code、Codex、Pi、OpenClaw、Hermes)。当前多为"一人一机"的单人 harness;尚未解决的是把超能力扩展到团队的"多人 harness"。
- **Tool Registry(工具注册表)** — 集中存放组织专用工具的地方,是让 agent"在工作中真正有用"的关键;YC 已有 350+ 工具,同一套既供内部 agent 也供个人 Cloud Code。
- **Skill / Skillify** — 建在工具之上的抽象层;Skillify 指把一次有效做法自动固化成可复用 skill,进而 meta-prompt 让 skill 自我改进。
- **Resolver(解析器)** — 一张列出"agent 能做什么"并链接到入口(如 AGENTS.md、skill 注册表、工具注册表)的表;理想的 resolver 表要满足 DRY + MECE。
- **DRY / MECE** — DRY = Don't Repeat Yourself(别重复);MECE = Mutually Exclusive, Collectively Exhaustive(互斥且穷尽,源自麦肯锡)。模型天然理解这两个原则,用来约束 skill/工具表的结构。
- **Denormalization for agents(为 agent 反规范化)** — 把散在各系统的数据打平成"为 agent 检索/理解优化"的格式(类比 Bigtable),配 RAG / graph RAG / 混合 RRF / 重排。
- **Jevons 悖论** — 让某资源使用成本骤降后,总用量反而暴增;此处指提问成本降到近零后,提问数量与复杂度激增。
- **Horseless Carriages(无马马车)** — Pete 的文章,批评"在确定性软件里塞一点 AI、并藏起 prompt";主张把控制权从开发者转移到用户。
- **Just-in-time software(即时软件)** — 需要时由 agent 现场生成、只为此刻定制的软件(如单页应用或可随时调用的 skill file)。
- **G-Brain** — Garry 三天写 ~4 万行、开源版的"Gary's list 2.0",含 agentic 检索、语音抽取、事实核查,团队直接以 OpenClaw 实例使用。
- **"Under the API line"(在 API 线以下)** — 指中心化路线下,普通人无法碰模型/prompt,AI "发生在你身上"的处境。

## 🔖 高价值金句时间戳
- `[06:29]` "what if we just gave the thing... complete access to the production database, where we could just, like, trample on anything?" —— 半夜偷偷放权的那次实验,恰恰揭示"限制越少威力越大"。
- `[07:17]` "when all of that context is in one place... an agent can go and ask or answer arbitrary questions about our business." —— 全部魔力的根:上下文集中在一个库/一套 schema。
- `[09:10]` "in order to ask some kind of complex question... I have to go and knock on... the data science team's door... I'm just going to ask far fewer questions." —— Jevons 悖论的日常版:摩擦决定提问量。
- `[12:12]` "one of the big problems that I don't think has been solved well yet by anybody is the multiplayer harness." —— 给创始人的空白市场:多人 agent 基础设施。
- `[23:04]` "how do you build super intelligence inside a company you do that on everything you do." —— 组织级超级智能的方法论一句话总结。
- `[29:53]` "there's a one-time time warp where you can leapfrog every incumbent." —— 现在多花 token = 提前活在未来,一次性越迁。
- `[34:46]` "It's time for just-in-time software." —— 未来软件形态:用时现造、只为此刻。
- `[44:51]` "I always really bristle when I see AI framed as a way to replace people." —— 立场:AI 是赋能而非替代,延续个人赋能叙事。
