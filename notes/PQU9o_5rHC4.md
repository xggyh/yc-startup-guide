# 对话 Claude Code 之父 Boris Cherny:如何为「六个月后的模型」而造 / Inside Claude Code With Its Creator Boris Cherny

> **来源**: [Inside Claude Code With Its Creator Boris Cherny](https://www.youtube.com/watch?v=PQU9o_5rHC4) · Y Combinator · 2026-02-17 · 时长 50:10
> **讲者**: Boris Cherny(Claude Code 创造者、Anthropic 工程师,即 SPEAKER_02)· The Lightcone 主持团(Garry Tan 等,SPEAKER_00/01/03/04,身份未在原片明确自报,保留 SPEAKER 编号)
> **一句话定位**: 从 Claude Code 创造者的第一手经验,提炼 AI Agent 创始人最该内化的产品与心态原则——永远为下一代模型而造、押注「潜在需求」、把脚手架当技术债。

## 🎯 TL;DR(中文核心要点)
- **核心建造哲学:不为今天的模型而造,为 6 个月后的模型而造。** 找到当前模型做不好、但注定会做好的能力边界押注在那里;否则你为当下跑通的产品找到 PMF 后,会被为下一代模型建造的人「蛙跳」超越。
- **用「潜在需求 latent demand」筛想法。** 只把用户「已经在做的事」变得更省力,不要逼他们做一个全新动作——Boris 说这是他产品观里「唯一最大的原则」,前几个创业公司都栽在没懂这点。
- **把 scaffolding(提示工程/胶水代码)当技术债。** 它通常只带来 10–20% 的提升,且下一代模型出来就把收益抹平;能等就等模型「免费」给你,永远不要赌模型不行(never bet against the model / Bitter Lesson)。
- **CLAUDE.md 越短越好。** Boris 自己的只有两行;超长了就直接删掉重来,从空白开始,模型跑偏才逐条加回,每次模型升级都能加得更少。
- **一切靠 dogfooding + 用户反馈逐帧迭代。** Plan mode 是周日晚上看 GitHub issue、30 分钟写出、连夜上线的;终端 spinner 迭代了近百次,80% 没上线——这套「几小时做 20 个原型」的速度本身就是 Claude Code 带来的红利。
- **多智能体拓扑是新前沿。** 用「互不污染的上下文窗口(uncorrelated context windows)」+ 合理拓扑并行,把上下文当作 test-time compute;难的调试/研究任务派 3–10 个子智能体并行;子智能体本质是「递归的 Claude Code」。
- **招聘看初学者心态与第一性原理。** 强观点、资深经验反而可能是包袱;能承认错误、快速迭代的人(和创始人型选手)更适配这个模型天天变的时代。
- **生产力已被重写。** Claude Code 上线后 Anthropic 人均生产力涨 150%,Boris 已 100% 不手写代码、每天合并约 20 个 PR;他预测 "software engineer" 这个头衔会消失,变成 builder / product manager。

## 🧭 适合谁 / 什么时候看
- 正在或计划做 **AI Agent / 开发者工具**创业的技术创始人,尤其在纠结「现在自己写脚手架 vs. 等下一代模型」的取舍时。
- 想掌握「模型快速迭代下如何做产品决策」和「潜在需求」选题法的早期创始人。
- 想借鉴 Anthropic 内部如何用 agent 自动化开发流程、组织多智能体协作的工程/团队负责人。
- **不适合**:想要 Claude Code 使用教程或 prompt 技巧清单的人——本片是理念与故事,不是操作手册。

## 📝 分段精读

### 1. 意外诞生:从终端聊天玩具到 Claude Code / The accidental origin `[00:00–07:09]`
**要点(中文)**: 没人要求 Boris 做 CLI——他只是想搞懂 Anthropic API,于是在终端里搭了个 chat app,再顺手试了 tool use、给模型 bash 工具。当模型写 AppleScript 查出他在听什么音乐时,他第一次感到「模型只想用工具」的 AGI 时刻。团队之所以停在终端,是因为判断「任何 UI 都撑不过 6 个月,模型进步太快」。GA(2 月)时它其实只写了他约 10% 的代码——押注「模型会变好」才是关键。

> 🗣️ "we don't build for the model of today. We build for the model six months from now." —— Boris
> 译:我们不为今天的模型而造,我们为六个月后的模型而造。

> 🗣️ "oh, my God, the model, it just wants to use tools. That's all it wants." —— Boris
> 译:天哪,这个模型,它就是想用工具,它想要的全部就是这个。

> 🗣️ "It's unbelievable that we're still using a terminal. That was supposed to be the starting point. I didn't think that would be the ending point." —— Boris
> 译:难以置信我们居然还在用终端。它本该只是起点,我没想到它会是终点。

### 2. 第一批用例 & CLAUDE.md 的极简哲学 / First use cases & a minimal CLAUDE.md `[07:09–11:29]`
**要点(中文)**: 早期用例是自动化 Git/bash/Kubernetes 和写单测(低风险)。CLAUDE.md 本身就来自「潜在需求」——用户自己在写 markdown 喂给模型,Boris 只是把它产品化。他强调「脚手架 vs. 等模型」的取舍:自己写能提升 10–20%,但下一代模型会把它抹平,不如等着免费拿。他自己的 CLAUDE.md 只有两行(自动合并 PR、发到内部 channel),其余全在版本库里团队共建;CLAUDE.md 太长的解法是**删掉重来**。

> 🗣️ "either you can build the scaffolding and then get some performance gain and then rebuild it again. Or you just wait for the next model and then you kind of get it for free." —— Boris
> 译:你要么自己搭脚手架、拿到一点性能提升、然后不断重搭;要么就等下一代模型,它基本免费送给你。

> 🗣️ "If you hit this, my recommendation would be delete your QuadMD and just start fresh... do the minimal possible thing in order to get the model on track." —— Boris
> 译:如果你的 CLAUDE.md 撑爆了,我的建议是直接删掉、从零开始……只做能把模型拉回正轨的最小干预。

### 3. 终端冗长度之争 & 「永远不要赌模型不行」/ Verbosity & never bet against the model `[11:29–15:44]`
**要点(中文)**: 该显示多少输出没有标准答案,全靠 dogfooding + 用户反馈打磨:Boris 想隐藏 bash 输出,内部员工「集体造反」;隐藏文件读取/搜索时 GitHub 用户不满,于是加了 verbose 模式,再迭代。他反复强调最爱听真实反馈。一个隐喻贯穿全片——agent 能做什么每代模型都在变,他的大脑「还卡在六个月前」,常被新同事更激进的用法震惊(如让 Claude 自己写工具分析 heap dump、比他更快找到内存泄漏)。

> 🗣️ "my favorite thing in the world is just hearing people's feedback and hearing how they actually want to use it." —— Boris
> 译:我在这世上最喜欢的事,就是听人们的反馈、听他们到底想怎么用它。

> 🗣️ "This is just something I have to constantly relearn because my brain is still stuck somewhere six months ago at times." —— Boris
> 译:这件事我得反复重新学,因为我的大脑有时还卡在六个月前。

### 4. 初学者心态、招聘 & 专才 vs 通才 / Beginner's mindset, hiring, specialists vs generalists `[15:44–21:51]`
**要点(中文)**: 模型天天变,资深工程师「强观点」反成包袱——最重要的技能是科学思维和第一性原理。招聘他爱问「你哪次错了」,看对方能否认错、担责、复盘;创始人型选手尤其擅长。团队高效者呈双峰:一端是超级专才(如深懂 JS 运行时的 bun 团队成员),另一端是横跨产品/设计/研究/财务的超级通才——「爱做奇怪事情」的人过去是警讯,如今是加分。Lightcone 主持人透露 YC 已在试点用 Claude Code transcript 招人。

> 🗣️ "the biggest skill is people that can think scientifically and can just think from first principles." —— Boris
> 译:最大的技能,是那些能科学地、从第一性原理去思考的人。

> 🗣️ "I'm wrong probably half the time, like half my ideas are bad and you just have to try stuff... eventually you might end up at a good idea. Sometimes you don't." —— Boris
> 译:我大概有一半时间是错的,我一半的点子都很烂,你只能不断去试……最后你可能得到一个好点子,有时候没有。

> 🗣️ "I really like to see people that just do weird stuff." —— Boris
> 译:我特别喜欢看到那种就爱做怪东西的人。

### 5. Agent 拓扑、Claude Teams、子智能体 & Plan Mode 的宿命 / Multi-agent topologies & the end of plan mode `[21:51–28:38]`
**要点(中文)**: 新领域「agent topologies」的关键子概念是「互不污染的上下文窗口」:多个 agent 各持干净上下文,叠加上下文相当于 test-time compute,配上合理拓扑就能造更大的东西。Claude Code 的 plugins 功能就是一个 swarm 用周末几天、几乎无人干预造出来的(给 Claude 一份 spec + 一块 Asana 看板,它自建工单、派子智能体认领)。多数 agent 如今由主 agent(「mama quad」)以子智能体形式派生。难任务 Boris 会按难度指定 3/5/10 个子智能体并行研究。他预测 **plan mode 寿命有限**——它本质只是往 prompt 里加一句「别写代码」。

> 🗣️ "There's this one sub idea, which is uncorrelated context windows... if you throw more context at a problem, that's like a form of test and compute." —— Boris
> 译:有个子概念叫「互不相关的上下文窗口」……如果你往一个问题里投入更多上下文,那就是一种 test-time compute。

> 🗣️ "a sub-agent is just like a recursive quad code. That's all it is in the code... we call her mama quad." —— Boris
> 译:子智能体本质就是一个递归的 Claude Code,代码层面就这么回事……我们管主 agent 叫「mama quad」。

> 🗣️ "plan mode probably has a limited lifespan... All it does is it adds one sentence to the prompt. That's like, please don't code. That's all it is." —— Boris
> 译:plan mode 的寿命大概有限……它做的全部就是往 prompt 里加一句话,就是「请先别写代码」,仅此而已。

### 6. 给创始人的核心原则:潜在需求 + 为 6 个月后的模型而造 + Bitter Lesson / The founder playbook `[28:38–40:31]`
**要点(中文)**: 两条硬原则。其一「潜在需求」:人只会做自己已经在做的事,你无法让人做新事,只能把他已经在做的事变简单——plan mode 正是把用户「已在浏览器里跟 Claude 谈 spec」这一行为搬进 Claude Code。其二「为 6 个月后的模型而造」+ 墙上裱着的《Bitter Lesson》:更通用的模型终将击败更专用的,永远不要赌模型不行,任何脚手架都当技术债。对 dev tool 创始人的具体框架:先想清楚要为用户解决什么问题,再看「模型自己想做什么」,然后同时满足用户和模型双向的潜在需求——别把模型关进 API 的盒子里。Claude Code 代码几乎每几个月全量重写一遍。

> 🗣️ "people will only do a thing that they already do. You can't get people to do a new thing... you just have to make the thing that they're trying to do easier." —— Boris
> 译:人只会做他们本来就在做的事。你没法让人去做一件全新的事……你只能把他们本来想做的那件事变得更容易。

> 🗣️ "think about the thing that the model wants to do and figure out how do you make that easier?" —— Boris
> 译:去想模型想做的那件事,然后琢磨怎么让它更容易做到。

> 🗣️ "the more general model will always beat the more specific model... never bet against the model... assume that whatever the scaffolding is, it's just tech debt." —— Boris
> 译:更通用的模型永远会打败更专用的模型……永远不要赌模型不行……假设你搭的任何脚手架都只是技术债。

### 7. 生产力涨 150% & 为何加入 Anthropic / 150% productivity & why Anthropic `[40:31–44:46]`
**要点(中文)**: 数据:团队一年翻倍、人均生产力(以 PR 计,并用 commit 生命周期交叉验证)涨约 70%;自 Claude Code 面世,Anthropic 人均生产力涨 150%——对比他在 Meta 负责代码质量时「一年数百人做出 2% 提升」,这是完全不可想象的量级。他从日本乡下用早期 Claude 产品「被震到窒息」而决定加入;打动他的两点:Anthropic 以研究实验室方式运作、模型(而非产品)才是最重要的东西;以及极强的使命感——身为科幻迷,他清楚这事最坏能坏到什么程度,想待在真正内化了 AI 安全的地方。

> 🗣️ "since quad code came out, productivity per engineer at Anthropic has grown 150%." —— Boris
> 译:自 Claude Code 面世以来,Anthropic 的人均工程师生产力增长了 150%。

> 🗣️ "the product was teeny, teeny, tiny. It's really all about building a safe model. That's all that matters." —— Boris
> 译:产品小到不能再小,一切真正围绕的是造一个安全的模型,重要的就只有这件事。

### 8. 编程的未来:「软件工程师」这个头衔会消失 / How coding will change `[44:46–50:10]`
**要点(中文)**: 沿着指数外推:Dario 曾预测 Anthropic 90% 代码由 Claude 写——已成真;Boris 自己自 Opus 4.5 起卸载了 IDE、100% 不手写代码、每天约 20 个 PR。他判断编程将对所有人「基本被解决」,"software engineer" 头衔会消失,变成 builder / product manager,而人转去写 spec、跟用户谈——团队里 PM/设计/EM/财务「人人都在写代码」。上界更吓人:ASL-4(模型可递归自我改进)与灾难性滥用是他们正全力防范的。co-work 也是「潜在需求」的产物——非技术员工挤破头在终端里装 Claude,于是团队用 Claude Code 十天做出一个 GUI 壳(底层就是同一个 agent)。

> 🗣️ "I don't edit a single line of code by hand. It's just 100% Quad code and Opus." —— Boris
> 译:我一行代码都不手写了,完全 100% 靠 Claude Code 加 Opus。

> 🗣️ "I think we're going to start to see the title software engineer go away. And I think it's just going to be maybe builder, maybe product manager." —— Boris
> 译:我认为「软件工程师」这个头衔会开始消失,大概会变成 builder,或者 product manager。

> 🗣️ "Thanks for having me. And send bugs." —— Boris
> 译:谢谢你们请我来,记得(给我们)报 bug。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **画出「能力边界地图」为 6 个月后的模型下注**:列出当前模型做不好、但趋势上即将做好的能力,把产品押在边界外一点,而不是当下能跑通的地方。
- [ ] **用「潜在需求」做选题闸门**:每个功能都问「用户是不是已经在做这件事、我只是让它更省力?」如果是在教用户做新动作,砍掉。
- [ ] **给每段 scaffolding 打上「技术债」标签**:提示工程/胶水代码只为救急,预设下一代模型会让它作废,建立定期删减的机制,别过度投入。
- [ ] **系统提示 / 配置从空白开始**:像 Boris 的两行 CLAUDE.md 一样,模型跑偏才逐条加回;每次模型升级复盘能删掉什么。
- [ ] **为你的 agent 设计多智能体拓扑**:对难的调试/研究任务,用互不污染上下文的 3–10 个子智能体并行,把上下文当 test-time compute;先跑通「主 agent 派生子 agent」的递归结构。
- [ ] **搭 dogfooding + 反馈闭环并追求「小时级原型」**:让团队天天用自己的产品,盯 issue/反馈渠道,练到能几十分钟出原型当天上线;招聘时考察 beginner mindset(能否认错、快速迭代、有系统/测试/产品感)。

## 🔑 关键术语 / 概念
- **Latent demand(潜在需求)** — 用户已经在做某件事,你只是让它更省力;你无法让人做全新动作。Boris 眼中产品第一原则。
- **Scaffolding(脚手架)** — 模型之外你写的一切代码/提示工程,通常只带 10–20% 提升且会被下一代模型抹平,应视为技术债。
- **The Bitter Lesson(苦涩的教训)** — Rich Sutton 名文:更通用的方法/模型终将击败更专用的;推论即「永远不要赌模型不行」。Claude Code 团队墙上裱着它。
- **CLAUDE.md** — 给 Claude Code 的项目级指令文件;主张极简,超长就删掉重来。
- **Plan mode(计划模式)** — 让模型先规划、暂不写码;本质只是往 prompt 加一句「please don't code」,Boris 认为其寿命有限。
- **Uncorrelated context windows(互不污染的上下文窗口)** — 多个 agent 各自持有干净、不被彼此/自身历史污染的上下文;叠加上下文相当于 test-time compute。
- **Agent topologies(智能体拓扑)** — 配置多个 agent 如何布局与通信协作的新兴领域,决定 swarm 能造多大的东西。
- **Sub-agent / mama quad** — 子智能体本质是「递归的 Claude Code」,由主 agent(戏称 mama quad)派生;如今多数 agent 以此形式启动。
- **ASL-3 / ASL-4** — Anthropic 的 AI 安全等级;当前模型处 ASL-3,ASL-4 指模型可递归自我改进,发布前须满足额外安全标准。

## 🔖 高价值金句时间戳
- `[00:00]` "we don't build for the model of today. We build for the model six months from now." — 全片最核心的建造哲学:为下一代模型而造。
- `[01:52]` "It's unbelievable that we're still using a terminal. That was supposed to be the starting point." — 连创造者都没料到终端会成终点,提醒别过度预设 UI/形态。
- `[10:01]` "do the minimal possible thing in order to get the model on track." — 极简 CLAUDE.md / 系统提示的可操作准则:最小干预。
- `[28:47]` "people will only do a thing that they already do. You can't get people to do a new thing." — 「潜在需求」一句话精华,直接用于选题。
- `[37:43]` "the more general model will always beat the more specific model... never bet against the model." — Bitter Lesson,判断脚手架是否值得投入的标尺。
- `[39:26]` "There is no product quad code that was around six months ago. It's just constantly rewritten." — 代码保质期只有几个月的「alpha」,重塑对技术债与重写的预期。
