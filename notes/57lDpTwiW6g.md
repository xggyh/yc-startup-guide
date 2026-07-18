# Tokenmaxxing:顶尖构建者如何用 AI 干 400 个工程师的活 / Tokenmaxxing: How Top Builders Use AI To Do The Work Of 400 Engineers

> **来源**: [Tokenmaxxing: How Top Builders Use AI To Do The Work Of 400 Engineers](https://www.youtube.com/watch?v=57lDpTwiW6g) · Y Combinator · 2026-05-08 · 时长 41:29
> **讲者**: Lightcone 播客。嘉宾/主角 **Garry Tan**(YC CEO,SPEAKER_00);主持为 Lightcone 团队(YC 合伙人,SPEAKER_01/02/03,transcript 未点名故保留编号)
> **一句话定位**: 一个 13 年没写代码的 CEO,用 Claude Code / OpenClaw 在几个月里 shipped 数十万行代码——本期把"token maxing、boil the ocean、thin harness fat skills"这套单人 AI 工程范式讲透,是 AI Agent 创始人把"vibe coding 出 slop"升级为可交付产品工程的实操手册。

## 🎯 TL;DR(中文核心要点)
- **Token maxing 是核心心法**:别省 token,该花就花(甚至一天 $500)。类比旧金山房租——越是有品味、懂技术的人,越应该在模型/算力上"多花",回报最大;省 token 反而是在自断双翼。
- **Markdown 就是代码,只是编译方式不同**。核心工程手艺是划分边界:把"能力、判断、泛化情况"写进 skill 的 markdown(交给 LLM 的 latent space),把"确定性真实动作"(API、Twilio 类调用)写进代码。当前 agentic engineering 的大部分失败,都是有人把本该放 markdown 的东西硬写成脆弱的代码。
- **测试是护城河,不是可选项**:不测试就把用户丢进去 = slop,比人写的代码烂 10x。目标 80–90% 覆盖 + 集成测试,让机器去补(boil the ocean,机器不嫌累)。
- **让 agent 先画图再动手**:动工前先要它输出 ASCII 数据流 / 状态机 / 依赖图 / 决策树,能把上下文一次性装进模型,显著提升完成度。
- **可复用工作流 = plan mode + skill 组合**:office-hours(CEO)review → design review → dev-experience review → plan-eng review → 交叉调用 `slash codex`(那个"200 IQ 近乎非语言的 CTO")找 bug → playwright 浏览器 QA。全部排进 Conductor 并行队列,自己只做最后人工验收。
- **人不出局,但角色变了**:GStack 高度依赖 `ask_user_question`——agency、品味、产品判断、真实客户的理解,仍必须由人供给。机器做你不想做的脏活(尤其 QA),你负责"要什么、为谁、为什么"。
- **可行性证据**:Gary's List 博客平台,第一次做要 $400 万、6–7 人、一年半;今年第三次重写只花 $200(Claude Code Max 账号)、5 天,还多出全套 RAG + agentic 深度检索。
- **personal AI 之争**:要么自己写 prompt、掌控自己的数据与工具;要么活在别人 API line 之下,被不了解你的 PM/算法/商业模式支配。这是这一代的"个人计算革命"。

## 🧭 适合谁 / 什么时候看
- 想用 AI agent 以单人/小团队做出"过去需要整个团队"产品的技术创始人。
- 已经在用 Claude Code / OpenClaw,但卡在"vibe coding 出 slop、一上真实用户就崩",不知如何工程化。
- 还在纠结 token 花费、用便宜模型或免费额度,想搞清为什么该"token max"。
- 想搭建自己的可复用 skills / harness 工作流、把 review 和 QA 自动化的 Agent 工程师。

## 📝 分段精读

### 1. 你会掌控 AI,还是被 AI 掌控 / Will you control your AI? `[00:00–01:56]`
**要点(中文)**: 全片的定调问题:你对自己的工具是掌控还是被掌控。Garry 用 OpenClaw 类比法拉利——极度爽快、能解决你想都想不到的问题,但你必须同时是个机械师,因为它会在你最需要的时候抛锚。他 13 年没碰代码,复出后自称在做"400x"于当年的工作量,由此引出这套新范式。
> 🗣️ "i think that's like the defining question like will you have control over your own tools or will your tools have control over you" —— Garry Tan (SPEAKER_00)
> 译:我觉得这是那个决定性的问题——你到底是掌控自己的工具,还是你的工具掌控你。
> 🗣️ "it was 13 years of not coding and then suddenly boom i'm doing about 400x the amount of work that i was that year the last time i was even sort of like two-thirds of the time writing code" —— Garry Tan
> 译:13 年没写代码,然后突然砰地一下,我现在做的工作量大约是当年(上一次还有约三分之二时间在写代码那年)的 400 倍。

### 2. 用 Claude Code 重建一家创业公司 / Rebuilding a startup with Claude Code `[01:56–05:50]`
**要点(中文)**: Garry 因关心加州教育(如中学生该有权学代数)而起了写作、建站的念头,顺手第三次重写了他 2008 年的 YC 项目 Posterous。三次成本对比极具冲击力:$400 万/6–7 人/一年半 → $10 万/2 人/3 个月 → **$200/5 天**。而且这次还叠加了全套 RAG、agentic 深度检索(递归爬取、跨源交叉),等于软件本身就在做高质量调查记者的活,而不只是给记者用的发布工具。
> 🗣️ "in this case it took about two hundred dollars which was my cloud code max account and probably five days full featured blog platform does everything you want and then on top of that like full rag full um agentic retrieval" —— Garry Tan
> 译:这一次大概只花了 200 美元(就是我的 Claude Code Max 账号)、大约 5 天,一个功能齐全、你想要的都有的博客平台,而且还叠加了完整的 RAG、完整的 agentic 检索。

### 3. 像记者一样思考的软件 & "tokenmaxxing"的诞生 / Software that thinks like a journalist + the rise of tokenmaxxing `[05:50–10:07]`
**要点(中文)**: 关键思路来自 Jake Heller(Casetext):要想清"一个人类拿到这个上下文会怎么做"——去哪查、找什么书、搜什么。但现在你不用将就人力上限:接 Perplexity / X / Grok 的 deep research API,把海量上下文一次性喂进核心 prompt。这就是 essay《Boil the Ocean》的精神——20 个来源交叉验证胜过点一个链接读个标题。由此提出 **token max**:凡有增量工作能让结果更完整、更好,就该多花 token 去做。一切知识工作都能被 token max,但人仍要供给 agency。
> 🗣️ "you might be token Maxing but you should token Max like basically if there is incremental work that makes something more complete more awesome" —— Garry Tan
> 译:你可能会觉得这是在"疯狂烧 token",但你就应该 token max——只要有增量工作能让东西更完整、更出色(就去做)。
> 🗣️ "Every thing that we would call knowledge work could be token maxed. And I don't think that it means that we're going to get rid of people... people need to still supply the agency." —— Garry Tan
> 译:一切我们称之为知识工作的东西都能被 token max。但我不认为这意味着淘汰人——人仍然需要供给能动性(agency)。

### 4. GStack 的"意外"诞生 / The accidental creation of GStack `[10:07–14:21]`
**要点(中文)**: GStack 不是设计出来的,而是"受够了反复敲同样的话"堆出来的。Garry 把 Apple Notes 里反复用的 prompt 沉淀成 skill:最有效的一招是让 Claude 在动工前先画 ASCII 图(数据流、状态机、依赖图、处理管线、决策树),把上下文一次装满再干活,完成度立刻上升。第二个教训:自己写代码时最偷懒的就是测试,结果 vibe coding 全是 slop——于是把测试拉到 80–90% 覆盖(100% 太多)。这些沉淀出 plan-eng-review、office-hours(CEO)、10x check 等 skill。
> 🗣️ "before you start your work, make an ASCII diagram of all the data flows, all the inputs and outputs. What are the user flows? What are the error messages?... Once it did that, it loaded all of the context in and then it just did the work more completely. Like it boiled the ocean better." —— Garry Tan
> 译:在开始工作之前,先画一张 ASCII 图,标出所有数据流、所有输入输出、用户流程、错误信息……它这么做之后,就把全部上下文装进去了,然后活儿就做得更完整——它"把海洋煮得更透"了。
> 🗣️ "I've since learned that a hundred percent is probably too much. Like hitting 80 to 90% is usually the best practice at this point." —— Garry Tan
> 译:我后来意识到 100%(测试覆盖)大概太多了,现阶段做到 80% 到 90% 通常才是最佳实践。

### 5. 支撑 400x 产出的工作流 / The workflow behind 400x output `[14:21–20:59]`
**要点(中文)**: 真实日常:48 小时内 drop 13 个 PR。任何新想法进来,用 CEO skill + eng skill 在 plan mode 里规划好、点 approve,让 Claude 跑,几十个功能排队等他人工验收。跨模型协作是关键:Claude Code 适合"ADHD CEO"式快速开干,但有时会一本正经地胡编;遇到硬问题就 `slash codex` 召来那个"200 IQ 近乎非语言的 CTO"专挑 bug,再把反馈交回 Claude Code。全流程走 office-hours → design → dev review → eng review → codex,并高度依赖 `ask_user_question` 让人补齐意图。QA 用包了 Microsoft Playwright 的浏览器 agent 自动跑。
> 🗣️ "you need the 200 iq nearly non-verbal cto so you can just call in a friend and then that's what like slash codex is" —— Garry Tan
> 译:遇到更棘手的问题,你需要那个 200 IQ、近乎不善言辞的 CTO——你可以直接把这位"朋友"叫进来,这就是 slash codex 干的事。
> 🗣️ "the g-stack relies very heavily on ask user question... that's where the human you know vibe coder operator agentic engineer needs to supply their understanding of what's going on what are we building" —— Garry Tan
> 译:GStack 非常依赖 ask_user_question……那正是人类(vibe coder / 操作者 / agent 工程师)需要供给自己理解的地方:现在到底在发生什么、我们在造什么。

### 6. 薄 Harness,厚 Skills / Thin Harness, Fat Skills `[20:59–24:35]`
**要点(中文)**: 被网友嘲"你不就是卖一堆 Markdown"后,Garry 的回击是:Markdown 本身就是代码,只是编译方式不同。名字来自 YC 合伙人 Pete Kuhman——harness 就是"拿用户输入→给 LLM→执行 LLM 动作(含 tool call)"的核心循环,不该重复造,直接用 Claude Code / OpenClaw 这类现成的。你该花时间的是写 markdown:像给下一个人写婚礼筹办清单那样,把"该做什么"用大白话写清;而真正确定性的动作(打 20 个场地电话)则用代码调 Twilio。当今 agentic engineering 的所有难点,都是有人把本该放 markdown 的东西硬塞进脆弱的代码。
> 🗣️ "Markdown is actually code. It's just compiled in a different way, but you can get the computer to do really astonishing things." —— Garry Tan
> 译:Markdown 其实就是代码,只不过是用另一种方式编译的——但你能让计算机做出真正惊人的事。
> 🗣️ "All of the difficulty in agentic engineering today is when people try to do things that should be in Markdown in code, and it fails because code is brittle, it doesn't understand special cases. Code literally doesn't understand what you want or who you are." —— Garry Tan
> 译:如今 agentic engineering 的全部难点,就在于有人试图把本该写在 Markdown 里的事情写进代码——它会失败,因为代码是脆的、不理解特殊情况;代码根本不懂你想要什么、你是谁。

### 7. AI agent 就像法拉利 / AI agents are like Ferraris `[24:35–27:12]`
**要点(中文)**: OpenClaw 现在约 95% 可用、仍有大量失败案例,用它像开法拉利:又爽又快,但你最好是个机械师,因为它会在关键时刻抛锚,你得自己开盖修。Garry 把这一刻类比 Homebrew Computer Club、Apple One 刚出来时——那是钉在木盒里的面包板。现在装一套要花两三小时、$500–$1000 的 token 和云成本,但装好后就进入"套件法拉利"阶段,能开着到处跑。另一位主持补充:真正的心态转变是"东西脆、要修其实没关系,因为你可以让另一个 agent 一直守在那里帮你修"。
> 🗣️ "using OpenClaw these days is like driving a Ferrari... But then it's also like a Ferrari in that you better be a mechanic. It's a Ferrari that will break down on the side of the road when you most need it, and you need to get out with your wrench and pop the hood and fix it." —— Garry Tan
> 译:如今用 OpenClaw 就像开法拉利……但它也像法拉利在于:你最好是个机械师。这是一辆会在你最需要它的时候半路抛锚的法拉利,你得下车、拿出扳手、打开引擎盖自己修。
> 🗣️ "If it's not tested, and you're just throwing users in there, it's slop. 10x worse than human written code, because you just have no idea what's going to happen." —— Garry Tan
> 译:如果没测试就把用户丢进去,那就是垃圾(slop),比人写的代码还烂 10 倍,因为你根本不知道会发生什么。

### 8. 个人 AI 的未来 / The future of personal AI `[27:12–38:37]`
**要点(中文)**: Garry 现在约一半时间在 OpenClaw 而非 Claude Code,主要在做 G-Brain——受 Karpathy 的"LLM 知识 wiki"启发,把自己全部 markdown 上下文做成 PG Vector + 混合 RRF 的个人 RAG(直接从 Gary's List 里"抽"现成的 chunking/embedding 方案)。他坚持"lines of code 有意义"这个争议观点:用标准工具剥离出逻辑代码行后,他 2013 年的自写量降了约 70%,而总产出确实是 400x(因为在同时指挥约 15 个 agent)。落点是一个价值判断:明年人人都会有自己的 personal AI——要么你写自己的 prompt、掌控数据与所见;要么被困在别人的 API line 之下,像不知谁写的 Facebook 算法。有品味、懂技术的人恰恰最该"let it rip、token max"。
> 🗣️ "every single person on the planet will have their own personal AI... unless you have your own prompts, and you can write it for yourself, like you are... below the API line for some PM or developer that is not you, who like will not understand you" —— Garry Tan
> 译:地球上每一个人都会拥有自己的 personal AI……除非你有自己的 prompt、能为自己写它,否则你就处在某个不是你的 PM 或开发者的 API line 之下,而那个人根本不理解你。
> 🗣️ "how do you find good startup ideas, live in the future and build what's missing... this is a profound version of that, where all you have to do is... commit your brain to look at spending $500 in a single day on tokens" —— Garry Tan
> 译:怎么找到好的创业点子?活在未来,然后把缺失的东西造出来——这是它的一个深刻版本:你要做的,就是让自己的脑子接受"一天在 token 上花 500 美元"这件事。

### 9. 用 token 买回时间 / Buying back time with tokens `[38:37–41:29]`
**要点(中文)**: 主持人抛出反直觉观察:Garry 因兼着 YC CEO、时间极度稀缺,反而被逼着把一切自动化、在会议间隙写几十万行代码,比全职工程师更早学会"不亲自点网站测试"。Garry 说他羡慕"time billionaire"(时间亿万富翁,比如他的孩子、Startup School 的年轻人),而 token max 让他能借用机器的时间、逼近这种状态。收尾金句由主持人提炼:你可以通过借用机器的时间,拥有近乎无限的时间。
> 🗣️ "if you can token max, it's like... you can buy millions of years of consciousness of machine consciousness. Now I can be a time billionaire. It's not my own time. It's the time of a machine, like doing work for me" —— Garry Tan
> 译:如果你能 token max……你就能买到数百万年的机器意识时间。这样我就能成为"时间亿万富翁"——那不是我自己的时间,而是一台机器替我干活的时间。
> 🗣️ "You could have infinite time by borrowing the time from the machines." —— Lightcone 主持人 (SPEAKER_01)
> 译:你可以通过借用机器的时间,拥有近乎无限的时间。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **沉淀你自己的 skill 库**:把反复敲的 prompt 从 Apple Notes/脑子里搬进 markdown,做成 plan-eng-review、CEO/10x check、design review、`codex`/`claude` 交叉审查等可复用 skill。
- [ ] **在每个新功能实现前**,强制 agent 先输出 ASCII 数据流 / 状态机 / 依赖图 / 决策树,再进 plan mode,再动手。
- [ ] **把测试当一等公民**:目标 80–90% 覆盖 + 集成测试 + 浏览器端到端 QA(封装 Playwright 的 agent),让机器自己补测试,别自己写。
- [ ] **画清 latent space vs 确定性代码的边界**:能力、判断、泛化写进 skill markdown;真实动作(第三方 API、Twilio 类调用)写进代码——这是当前最值钱的工程手艺。
- [ ] **搭并行 agent 队列**(如 Conductor):把想法排队跑,自己只留最后一道人工验收,并让流程重度依赖 `ask_user_question` 供给意图。
- [ ] **按"房租思维"给 token 花钱**:用最新最强模型 token max,别在算力上抠;把省下的注意力用在 agency、品味、真实客户理解上。
- [ ] **研究/内容类任务用多源 boil the ocean**:接 Perplexity / X / Grok 的 deep research API,20 个来源交叉验证而非只读一个标题。

## 🔑 关键术语 / 概念
- **Tokenmaxxing / token max** — 主动多花 token 与算力,把任务做到极致完整,而非省着用。类比旧金山房租:越是有品味、懂技术的人越该"多花",回报最大。
- **Boil the Ocean** — Garry 的一篇 essay 理念:不将就于"人力能做的量",让机器穷尽所有增量工作(多源交叉、更高完成度)。机器不嫌累,尽管 zap the rocks harder。
- **Thin Harness, Fat Skills** — harness 保持薄(用现成的 Claude Code/OpenClaw),把大量能力写进 markdown skills;Garry 关于这套哲学的 X 长文标题。
- **Harness** — agent 的核心循环:拿用户输入 → 交给 LLM → 运行 LLM 的动作(含 tool call)。名字来自 YC 合伙人 Pete Kuhman。
- **Skill** — 可复用的 markdown 指令包(如 office-hours、plan-eng-review、CEO plan、10x check、`slash codex`)。
- **Latent space vs deterministic space** — LLM 懂"你是谁/你的意图/泛化情况" vs 代码只跑确定的 0 与 1;划分二者边界是核心手艺。
- **Below the API line** — 若你不写自己的 prompt,就活在别人(PM/开发者)的 API 之下,被其价值观与商业模式支配。
- **Time billionaire(时间亿万富翁)** — 拥有海量自由时间的人;token max 让你"借用机器的时间"逼近这种状态。
- **OpenClaw / G-Brain / GStack / Conductor** — Garry 使用的开源 agent 运行环境 / 个人知识 RAG(PG Vector + 混合 RRF)/ skill 仓库 / 并行 agent 管理器。

## 🔖 高价值金句时间戳
- `[00:00]` "will you have control over your own tools or will your tools have control over you" — 全片的价值观内核:自研 prompt 掌控工具,还是被工具与他人算法支配。
- `[04:28]` "it took about two hundred dollars which was my cloud code max account and probably five days" — $200/5 天重建曾需 $400 万/一年半的产品,单人 AI 工程可行性的硬证据。
- `[22:54]` "people try to do things that should be in Markdown in code, and it fails because code is brittle" — 一句话点破当今 agentic engineering 的头号失败模式:边界划错。
- `[24:35]` "using OpenClaw these days is like driving a Ferrari... you better be a mechanic" — 现阶段 AI agent 又快又脆,你必须既是司机又是机械师。
- `[34:33]` "every single person on the planet will have their own personal AI" — 对创始人而言的机会窗口:personal AI 之争即将上演,像当年个人计算革命。
- `[37:37]` "live in the future and build what's missing" — YC 找点子的老箴言,在 token max 时代的深刻新解:先接受"一天花 $500 token"这件事。
