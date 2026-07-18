# 把 Claude Code 变成你的 AI 工程团队 / How to Make Claude Code Your AI Engineering Team

> **来源**: [How to Make Claude Code Your AI Engineering Team](https://www.youtube.com/watch?v=wkv2ifxPpF8) · Y Combinator · 2026-04-23 · 时长 21:49
> **讲者**: Garry Tan(YC 总裁兼 CEO,前 Palantir 10 号员工、Posterous 联合创始人;GStack 开源作者)
> **一句话定位**: 用"薄骨架 + 厚技能"的方式,把编码 Agent 组织成一个有角色、有流程、有评审的工程团队;并把 YC 的 Office Hours 逼问法内化进 planning,帮 AI Agent 创始人在写第一行代码前就把点子想大、想清楚、想到可落地。

## 🎯 TL;DR(中文核心要点)
- **让 Agent 干活的方式和让人干活一样**:分角色、走流程、做评审。单个"聪明模型"不是瓶颈,缺的是把它组织成团队的脚手架。
- **瓶颈不是模型智能,而是 harness(骨架)**。Garry 的观点是反过来做:骨架要"薄到几乎没有",能力都塞进可复用的 **skills**(技能)里——thin-harness, fat-skills。
- **开箱即用的模型会"乱走"**:它不了解你的数据就靠猜,规模化的猜就是"看起来对、却悄悄崩掉"的代码。要用结构约束它。
- **先跑 Office Hours,再写代码**:GStack 把 16 位 YC 合伙人多年的 Office Hours 蒸馏成一个 skill,开场先抛 6 个"逼问式问题"(最狠的一问:*你有什么最强证据证明真有人想要这个?*)。
- **用 AI 把点子做大**:从"1099 文档聚合器"被逼成"报税撮合平台"——聚合是钩子(hook),报税撮合是可抽成 10 倍的扩张(wedge 楔子策略)。
- **对抗式评审是免费的质量杠杆**:模型对自己的设计文档做多轮 adversarial review,自动发现并修 16 个问题,把评分从 6/10 提到 8/10。
- **并行才是真正的 10x**:Garry 同时跑 10–15 个 Claude Code 会话、几百个待审 PR;把最无聊的 QA 用自己包的 Playwright CLI(/QA、/browse)自动化,才解锁了并行。
- **今天最稀缺的不是能力而是判断力和点子**:"造东西的门槛塌了,唯一剩下的问题是——你要造什么。"

## 🧭 适合谁 / 什么时候看
- 想用 Claude Code / Codex 等编码 Agent "一个人当一个团队"来做 MVP 的 AI Agent 创始人。
- 已经会让 Agent 写代码,但苦于"代码看着对却悄悄坏"、QA 累、无法并行的独立开发者/小团队。
- 想把 YC 式的点子逼问(who/pain/business model/证据)前置到编码流程里的早期创始人。
- 不适合:想听融资、招聘、GTM 体系化方法论的人——这是一支偏"工作流/工具化"的实操演示。

## 📝 分段精读

### 1. 智能体时代:编程被彻底改变 / The Agent Era `[00:00–02:16]`
**要点(中文)**: Garry 自述是写了一辈子代码的工程师(Palantir 10 号员工、Posterous 创始人),1 月起被 Karpathy、Boris Cherny "不再手写代码"的说法勾住,过去两个月写的代码比 2013 全年还多,一个人就重建了当年"两年、1000 万美元、10 个工程师"才做成的 Posterous。核心洞察:让 Agent 真正干活的方式,和人类一直以来一样——组队、分角色、走流程、做评审。开箱模型会"乱走",靠猜,规模化的猜就是"看似合理却悄悄崩坏"的代码。
> 🗣️ "It turns out the way to get agents to do real work is the same way humans have always done it, as a team, with roles, with process, with review." —— Garry Tan
> 译:事实证明,让 Agent 真正干活的方式,和人类一直以来的方式一模一样——组成一个团队,有角色、有流程、有评审。
> 🗣️ "Out of the box, the model wanders. It doesn't know your data well, so it guesses. And guessing at that scale is how you get plausible-looking code that silently breaks." —— Garry Tan
> 译:开箱即用时,模型会到处乱走。它不了解你的数据,所以只能猜;而在那种规模上猜,就是你得到"看起来很像样、却悄无声息就崩掉"的代码的根源。

### 2. GStack:薄骨架、厚技能 / Thin Harness, Fat Skills `[02:16–03:45]`
**要点(中文)**: 瓶颈不是模型智能——"只要把模型配置对,它们已经足够聪明"。真正的错在于大家把脚手架做得太重。GStack 把这套反过来:harness 薄到几乎没有,把能力全部封装成一批像"专家团队"一样的 skills。三周前写的 GStack,GitHub star 数已超过 Ruby on Rails。其中一个 skill 叫 Office Hours,精确复刻 YC 合伙人给创业者做 Office Hours 的过程,开场先抛 6 个"逼问式问题"。
> 🗣️ "The bottleneck here is not the model's intelligence. As long as you set the models up right, they are already smart enough to do extraordinary work on your code base. This is backwards. The scaffolding should be trivially thin." —— Garry Tan
> 译:瓶颈不在模型的智能。只要你把模型配置得当,它们已经足够聪明,能在你的代码库上做出非凡的工作。(现在的做法)是反的。脚手架本该薄到微不足道。
> 🗣️ "GStack is my implementation of the thin-harness, fat-skills approach... turns cloud code into an AI engineering team for you. Skills that act like a team of specialists." —— Garry Tan
> 译:GStack 是我对"薄骨架、厚技能"这套思路的实现……它把 Claude Code 变成一个为你服务的 AI 工程团队。这些技能就像一支专家团队一样运作。

### 3. Office Hours:逼问点子的六个问题 / The Forcing Questions `[03:45–07:13]`
**要点(中文)**: 现场演示做一个"报税 App":自动进 Gmail 翻出所有 1099 表。开启 Office Hours 后,模型不急着写代码,而是先思考"用户是谁、痛点是什么、商业模式怎样、谁想要"。最关键的一问决定其余一切:*你有什么最强证据证明真有人想要这个?* 还会追问竞品(TurboTax、H&R Block 已有 1099 导入,Plaid 能连银行)——为什么它们没解决你的问题?这正是 YC 合伙人每天对创始人做的"reframe(重构)"。
> 🗣️ "Here's the question that determines everything else. What's the strongest evidence? That you have that someone actually wants this?" —— Garry Tan(引述 Office Hours skill 的提问)
> 译:这是决定其余一切的问题——你手上有什么最强的证据,能证明真的有人想要这个?
> 🗣️ "If I just type the original thing... it'll go do that... but it won't think about who's the user, what is this, what is the business model, who wants this, what's the pain point, how does it work." —— Garry Tan
> 译:如果我只是把最初那句话丢给模型……它会照做……但它不会去想:用户是谁、这是什么、商业模式是什么、谁想要它、痛点在哪、它怎么运转。

### 4. 楔子策略:让点子变大 / Making the Idea Bigger `[07:13–08:38]`
**要点(中文)**: Office Hours 把点子从"1099 文档聚合器"推到更大的商业模式:聚合文档只是钩子(解决即时痛点),真正的扩张是——文档到手后,顺势帮你把税报了,即"给报税师做撮合和获客(lead gen)"。这是经典的楔子(wedge)策略。聚合本身一年只能收两三五美元,但从最终成交的报税服务里抽成,可能是 10 倍的收入。AI 帮你在写代码前就把商业模式想大一层。
> 🗣️ "The hook is we'll find all your 1099 ins for you solving an immediate pain. But the expansion is now that you have your docs, let's actually get your taxes prepared, which is matchmaking and lead gen for tax preparers. And it's a classic wedge strategy." —— Garry Tan(复述模型的 reframe)
> 译:钩子是"我们帮你找齐所有 1099",解决当下的痛;而扩张是——你文档都到手了,那干脆把税也报了吧,这就是给报税师做撮合和获客。这是经典的楔子策略。

### 5. "感觉违法"的浏览器自动化黑客 / The "Feels Illegal" Browser Hack `[08:38–12:44]`
**要点(中文)**: 最出彩的方案:不用 Plaid、不存凭证——让用户在自己**可见的本地浏览器**里登录,AI 接管、导航到税务文档、下载 1099 PDF,用户全程看着发生。"云只是别人的电脑",在本地浏览器跑更让用户放心。Garry 顺带给了一个选模型心法:Opus(默认 Claude)像"多动症 CEO",点子多、适合一起喝酒;真到硬骨头,得叫上"自闭症 CTO"——Codex,让它去啃那些疯狂的 bug。他强调:一两年前甚至三个月前,没人会想到用浏览器自动化来解这个问题——现在你能把一个想法推进到过去根本到不了的地方。
> 🗣️ "The user logs in, AI takes over, navigates to tax docs, finds the 1099 ince, downloads it. No plaid, no stored credentials. The user watches the whole thing happen in the visible browser." —— Garry Tan
> 译:用户登录,AI 接管,导航到税务文档,找到 1099、下载它。不用 Plaid,不存任何凭证。用户在可见的浏览器里全程看着这一切发生。
> 🗣️ "The cloud is just someone else's computer." —— Garry Tan
> 译:所谓云,不过是别人的电脑罢了。
> 🗣️ "Opus 4.6 is sort of ADHD CEO, he's the guy you want to get a beer with and he's got a billion ideas, but when the going gets tough you got to call in your autistic CTO, and that's codecs [Codex]." —— Garry Tan
> 译:Opus 有点像多动症 CEO——是你想约去喝一杯、脑子里有十亿个点子的那种人;可一旦碰到硬仗,你就得请出你那位自闭症 CTO,那就是 Codex。

### 6. 对抗式评审 + 设计枪 / Adversarial Review + Design Shotgun `[12:44–16:59]`
**要点(中文)**: Office Hours 自带 feasibility(可行性)判断——Garry 说三次里大概有一次跑到最后,结论是"这事不值得做"。接着模型做多轮 **adversarial review(对抗式评审)**:主动挑设计文档的毛病(没有失败处理、没有隐私章节、2FA 交接无方案),能自动修的就修——两轮评审自动发现并修复 16 个问题,评分从 6/10 升到 8/10。设计阶段用 **Design Shotgun**(视觉头脑风暴):一次生成 3 个方向的 UI(外包给 OpenAI Codex 的图像生成),约 60 秒出稿,让你打分挑选(他挑了对普通人更友好的 B 版)。
> 🗣️ "Our doc survived two rounds of adversarial review, and it automatically caught and fixed 16 issues... the adversarial review improved the score from 6 out of 10 to 8 out of 10." —— Garry Tan
> 译:我们的文档挺过了两轮对抗式评审,期间自动发现并修复了 16 个问题……对抗式评审把分数从 6/10 提升到了 8/10。
> 🗣️ "Sometimes I use office hours and maybe one in three times I get to the end of it and I say, you know what? This isn't something that makes sense." —— Garry Tan
> 译:有时我用 Office Hours,大概每三次里有一次,走到最后我会说:你知道吗?这事儿根本不成立。

### 7. 整套冲刺系统 + 并行工程团队 / The Full System & Parallel Engineers `[16:59–21:20]`
**要点(中文)**: 一次 sprint 的流程:Office Hours → Plan/CEO Review → (可选 auto plan 一键跑完 CEO/工程/设计/DX 评审,用他的默认建议)→ 批准后 Claude Code 写码 → review(staff 级抓 bug)→ ship(合入 main 前最后一道关)。真正的 10x 来自并行:Garry 同时跑 10–15 个 Claude Code 会话、手上约 400 个待审 PR。他吐槽 Claude in Chrome MCP 是"用过最烂的软件之一"(慢、context 爆炸),于是自己在 CLI 层包了 Playwright + Chromium,做出 /QA 和 /browse,让任何 Agent 都能截图、点击、填表、下载、跑回归测试、改 CSS——把最无聊的 QA 自动化,才解锁并行。他也很怕 AI 编码时代的供应链攻击,靠 GStack 分批(in waves)审查社区 PR。他自认能到"level 7"(多窗口、多项目、多分支并行落地)。
> 🗣️ "I run 10 to 15 parallel Claude code sessions all at the same time." —— Garry Tan
> 译:我会同时并行跑 10 到 15 个 Claude Code 会话。
> 🗣️ "Claude in Chrome MCP is one of the worst pieces of software I've ever used... I basically wrapped playwright at the CLI level and now your Claude code and any agent now can actually just use the browser." —— Garry Tan
> 译:Claude in Chrome MCP 是我用过最烂的软件之一……我基本上在 CLI 层把 Playwright 包了一层,现在你的 Claude Code、任何 Agent 都能真正地直接用上浏览器了。
> 🗣️ "One of the things that's been really scary in AI coding right now is supply chain attack. So I'm really really paranoid about it." —— Garry Tan
> 译:眼下 AI 编码里真正吓人的一件事是供应链攻击。所以我对它极度、极度警惕。

### 8. 结语:唯一剩下的问题 / The Only Thing That Matters `[21:20–21:49]`
**要点(中文)**: 跑 /office hours 时,你在真正见到 YC 之前,就能先体验到 YC 对创始人做的那种"逼问 + 重构"。造软件的门槛已经塌了,现在唯一剩下的问题是:你要造什么。放手去干,做人们想要的东西。
> 🗣️ "This is the most incredible time in history to build software. The barrier to building just collapsed. The only question left is what are you gonna build. It's time to let it rip. Go make something people want." —— Garry Tan
> 译:这是历史上造软件最不可思议的时代。造东西的门槛刚刚塌掉了。唯一剩下的问题是——你要造什么。是时候放手去干了。去做人们想要的东西。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **把"薄骨架、厚技能"当成 Agent 架构准则**:别把智能堆在臃肿的编排层里,把可复用能力沉淀成一批独立、可组合的 skills/子 Agent,harness 只做调度。
- [ ] **在写码前先跑一遍"Office Hours"式逼问**:对每个新点子先问 who / pain / business model / 证据,尤其那一问——"你有什么最强证据证明有人真的想要?"没有证据就别急着建。
- [ ] **用"钩子 + 楔子"重构你的 Agent 产品**:找一个能立刻缓解痛点的窄入口(hook),想清楚下游那个能抽成 10 倍的扩张(wedge)在哪。
- [ ] **给你的设计/规划文档加一道 adversarial review**:让模型专门挑失败处理、隐私、认证交接等漏洞并自动修,把评分从"能用"逼到"能上线"。
- [ ] **把最无聊的 QA 自动化**:在 CLI 层封装 Playwright/浏览器,给你的 Agent 提供截图、点击、填表、回归测试能力,这是解锁"并行跑多个 Agent"的前提。
- [ ] **按任务类型选模型**:探索/发散用"点子多"的模型,啃硬 bug 时切到更"死磕细节"的模型(如 Codex);别指望一个模型全程最优。
- [ ] **建立 PR 分批审查 + 供应链防护习惯**:并行产出大量代码时,把社区/Agent 生成的变更分波次审,警惕依赖投毒。

## 🔑 关键术语 / 概念
- **Thin-harness, fat-skills(薄骨架、厚技能)** — Garry 的核心架构主张:编排层(harness)做到极薄,把能力封装进大量可复用的 skills。
- **Skill(技能)** — GStack 里像"专家团队成员"一样的能力单元,如 Office Hours、Design Shotgun、review、ship、/QA、/browse 等(共 28 个命令)。
- **Office Hours(办公室答疑)** — 复刻 YC 合伙人给创始人做的点子逼问/重构过程,开场抛 6 个 forcing questions,自带可行性判断。
- **Forcing question(逼问式问题)** — 强制你在动手前回答的关键问题,最狠一问是"最强证据证明有人想要"。
- **Adversarial review(对抗式评审)** — 模型对自己的设计/代码做多轮"找茬"评审并自动修复的机制。
- **Design Shotgun(设计枪)** — 一次并行生成多个 UI 方向(约 60 秒,借 Codex 图像生成)供打分挑选的视觉头脑风暴工具。
- **Wedge strategy(楔子策略)** — 用一个窄入口切入、再向更大市场/更高抽成扩张的经典打法。
- **Level 7(并行度分级)** — Garry 自评能达到的并行工作状态:多窗口、多项目、多分支同时推进落地。
- **Conductor** — 承载 GStack 的界面工具,可开 work tree、看模型推理轨迹(Geary/"Gary mode")、并行开多个工作项。

## 🔖 高价值金句时间戳
- `[00:53]` "the way to get agents to do real work is the same way humans have always done it, as a team, with roles, with process, with review." — 全片总纲:Agent 要当"团队"来组织,而非当"神灯"来许愿。
- `[01:56]` "guessing at that scale is how you get plausible-looking code that silently breaks." — 一针见血地说清"vibe coding"最大的隐患:看着对、悄悄坏。
- `[02:01]` "The bottleneck here is not the model's intelligence... The scaffolding should be trivially thin." — 反直觉的架构结论:瓶颈是脚手架,不是智能。
- `[05:29]` "What's the strongest evidence... that someone actually wants this?" — 每个创始人动手前都该先回答的那一问。
- `[06:47]` "it's a classic wedge strategy... you can actually charge a percentage of the transaction... which might be 10x more." — 演示了 AI 如何帮你把商业模式想大一层。
- `[08:39]` "The cloud is just someone else's computer." — 一句话讲清"本地可见浏览器自动化"为什么更让用户放心。
- `[19:36]` "I run 10 to 15 parallel Claude code sessions all at the same time." — 真正的 10x 不在单会话速度,而在并行。
- `[21:30]` "The barrier to building just collapsed. The only question left is what are you gonna build." — 收束全片:能力过剩时代,判断力和点子才是稀缺品。
