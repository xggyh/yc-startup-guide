# 从零开始用 AI 搭建一家公司 / How To Build A Company With AI From The Ground Up

> **来源**: [How To Build A Company With AI From The Ground Up](https://www.youtube.com/watch?v=EN7frwQIbKc) · Y Combinator · 2026-04-24 · 时长 10:27
> **讲者**: Diana Hu(YC 合伙人 / Partner at YC)
> **一句话定位**: 讲的不是"用 AI 提效",而是把 AI 当成公司运行的操作系统——教 AI Agent 创始人如何从第一天起就把整家公司搭成"可被 AI 查询、自我改进的闭环",用最小团队跑出 10-1000 倍的速度。

## 🎯 TL;DR(中文核心要点)
- **重新定义 AI 的位置**:不要把 AI 当成插进现有流程的 copilot,而要当成公司运行的操作系统(operating system),每个流程、决策都从这层智能流过。
- **闭环 vs 开环**:旧公司是开环(做决策→执行→不系统性测量结果),天然"有损";AI 时代要把每个重要流程做成闭环——采集信息→喂回智能系统→持续自我改进。
- **让整家公司"可查询"(queryable)**:每个重要动作都要产出一个 AI 能学习的 artifact——AI 记会议、少用 DM/邮件、在所有沟通渠道嵌入 agent、给营收/销售/工程/招聘/运营建统一 dashboard。
- **给模型的上下文要像给员工一样多**:这是拿到 AI 全部能力的前提;做到后,工程 sprint 时间可砍半、单位时间产出接近 10 倍。
- **软件工厂(AI software factories)**:TDD 的下一步——人写 spec 和测试定义"成功",agent 生成实现并迭代到测试通过;有公司代码库里已"没有手写代码,只有 spec 和测试框架"(如 StrongDM)。
- **中层管理消失**:公司速度只取决于信息流速度;如果公司可查询、artifact 丰富、对 AI legible,就几乎不需要人肉中间层(human middleware),砍掉每一层人肉转发都是直接提速。
- **三种员工原型 + token maxing**:未来只有 IC(人人都是 builder,开会带能跑的原型而非 PPT)、DRI(一人一结果,无处躲)、AI-founder 型(创始人亲自站在最前沿);关键指标是最大化 token 用量而非人头,愿意背"不舒服的高 API 账单"。
- **创始人自己去建立信念**:不能外包对这些工具的 conviction,必须亲自坐下来用 coding agent,直到打破自己对"什么可做"的旧认知;早期创始人没有历史包袱,这是对巨头的最大优势。

## 🧭 适合谁 / 什么时候看
- 正在从 0 到 1 搭团队、想把公司"AI 原生"化的早期创始人(尤其 AI Agent 方向)。
- 纠结"AI 到底是提效工具还是范式转变"、想要一套具体内部实践清单的技术型 founder。
- 想理解为什么小团队能打过大公司、以及如何把"闭环 / 可查询 / 软件工厂"落到日常运营的人。

## 📝 分段精读

### 1. 引言:不是提效,是全新能力 / New capabilities, not productivity `[00:09–00:58]`
**要点(中文)**: 大多数人谈 AI 只谈"让工程师更高效、加 copilot、多发功能",这套框架错过了真正的转变。真正的变化不是效率提升,而是**全新能力**——一个对的人配上 AI 工具,现在能做出过去需要整个团队、甚至根本不可能做的东西。这一认知会改变创始人经营公司的方式。
> 🗣️ "This framing misses the shift we're currently seeing, which is less about productivity boosts than entirely new capabilities." —— Diana Hu
> 译:这套框架错过了我们正在经历的转变——它关乎的不是效率提升,而是全新的能力。
> 🗣️ "The right person with AI tools can now build features that used to require an entire team, or were just impossible." —— Diana Hu
> 译:一个合适的人配上 AI 工具,现在能造出过去需要一整个团队、甚至根本不可能做出的功能。

### 2. 把 AI 当成公司的操作系统 / AI as your company's operating system `[00:58–01:57]`
**要点(中文)**: 核心比喻——AI 不该是公司"用的一个工具",而应是公司"运行在其上的操作系统"。每个 workflow、每个决策、每个流程都从这层持续学习、持续改进的智能层流过。具体落法:每个重要流程都要被一个"智能闭环"捕获——采集信息、喂回智能系统、随时间改进流程。
> 🗣️ "The way to think about AI is that it should not be a tool your company just uses. It should be the operating system your company runs on." —— Diana Hu
> 译:对 AI 正确的理解是:它不该只是你公司用的一个工具,而应该是你公司运行于其上的操作系统。
> 🗣️ "Every workflow, every decision, and every process should flow through an intelligent layer that is constantly learning and improving." —— Diana Hu
> 译:每一个工作流、每一个决策、每一个流程,都应该流经一个持续学习、持续改进的智能层。

### 3. 开环 vs 闭环公司 / Open vs closed loop companies `[01:57–03:00]`
**要点(中文)**: 借控制系统的概念:开环(open loop)是没有反馈回路的受控系统,旧世界的公司基本都是开环——做决策、执行,但不系统性测量结果并调整流程,因此天然"有损"(lossy)。闭环(closed loop)会自我调节:持续监控输出、调整流程以更好地达成目标,对正确性和稳定性极强。配合能自我改进的 agent,公司应作为闭环运行。
> 🗣️ "Open loops are inherently lossy. A closed loop, on the other hand, is self-regulating. It continuously monitors its output and adjusts its process to better meet the stated goal." —— Diana Hu
> 译:开环天然是有损的;而闭环会自我调节,持续监控自己的输出,并调整流程以更好地达成既定目标。
> 🗣️ "With self-improving agents, your company should run as a closed loop." —— Diana Hu
> 译:有了能自我改进的 agent,你的公司就应该作为一个闭环来运行。

### 4. 让公司全面可查询 / Making your company fully queryable `[03:00–05:00]`
**要点(中文)**: 要建闭环,必须让整家公司"可查询"、对 AI"可读(legible)"——每个重要动作都产出一个 artifact,让公司中心的智能能学习并自我改进。具体动作:AI 记会议、少用 DM/邮件、在所有沟通渠道嵌 agent、给营收/销售/工程/招聘/运营建统一 dashboard。举例:把 Linear 工单、Slack 工程频道、来自邮件/Pylon/GitHub 的客户反馈、Notion/Google Doc 里的高层计划、销售通话和每日站会录音都接给一个 agent,它就能分析上个 sprint 到底交付了什么、是否真的满足客户,并给出更可预测、更准的下个 sprint 计划。核心原则:**给模型的上下文要像给员工一样多**。
> 🗣️ "To build these closed loops, you will need to make your entire company queryable. In other words, the whole organization should be legible to AI." —— Diana Hu
> 译:要建这些闭环,你必须让整家公司变得可查询;换句话说,整个组织都应该对 AI 是"可读"的。
> 🗣️ "To get their full capabilities, you need to provide models with as much context as you would provide an employee." —— Diana Hu
> 译:要拿到模型的全部能力,你得像给一个员工那样,给模型足够多的上下文。
> 🗣️ "I've seen teams that do this cut their engineering sprint time in half and get close to 10x more than in that time." —— Diana Hu
> 译:我见过这样做的团队把工程 sprint 时间砍掉一半,并在这段时间里做出接近 10 倍的产出。

### 5. 1000 倍工程师的崛起(软件工厂)/ The rise of the 1,000x engineer `[05:00–07:12]`
**要点(中文)**: 高速公司正在用一种新范式造产品——**AI 软件工厂**,是 TDD 的下一步进化:人写 spec 和一组定义"成功"的测试,AI agent 生成实现代码并迭代到测试通过;人负责"造什么"和"判断输出好坏",写代码交给 agent。有公司已推到极致——代码库里没有手写代码,只有 spec 和测试框架(以 StrongDM 的 AI 团队为例:用基于场景的规则和验证,驱动 agent 写、测、迭代到达到某个"概率性满意阈值")。这正是 Steve Yegge 说的"1000 倍工程师"的实现路径:用一整套 agent 系统包裹单个工程师。
> 🗣️ "With software factories, humans write a spec and a set of tests that define success. And then AI agents generate the implementation code and iterate until the tests pass." —— Diana Hu
> 译:在软件工厂里,人写下 spec 和一组定义"成功"的测试,然后 AI agent 生成实现代码,并不断迭代直到测试通过。
> 🗣️ "Some companies have already pushed this to the point where their repos contain no handwritten code, just specs and test harnesses." —— Diana Hu
> 译:有些公司已经把这套推到了这种地步——他们的代码库里没有任何手写代码,只有 spec 和测试框架。
> 🗣️ "This is how you achieve the thousand x engineer that Steve Yege talks about by surrounding a single engineer with a system of agents." —— Diana Hu
> 译:这就是实现 Steve Yegge 所说"千倍工程师"的方式——用一整套 agent 系统去环绕单个工程师。

### 6. 为什么中层管理会消失 / Why middle management disappears `[07:12–09:12]`
**要点(中文)**: 当公司到处是 AI 闭环、可查询、有软件工厂,传统管理层级就不再成立:旧世界靠中层管理者上下低效地转发信息,新世界由智能层承担这个职责。公司速度只取决于信息流速度,砍掉每一层人肉转发都是直接提速(引 Jack Dorsey 在 Block 的做法:公司要被重建成一个智能层,人在边缘引导,而不是充当信息的转发管道)。未来每家公司只有三种员工原型:**IC**(builder/operator,人人都建东西,开会带能跑的原型而非 PPT)、**DRI**(直接负责人,只管战略与客户结果,一人一结果、无处躲)、**AI-founder 型**(创始人亲自在最前线示范能力跃迁,不把 AI 战略外包给别人)。关键指标从"堆人头"变成"最大化 token 用量"(token maxing),要愿意背"不舒服的高 API 账单"。
> 🗣️ "If your company is queryable, artifact-rich, and legible to an AI, you should have almost no human middleware." —— Diana Hu
> 译:如果你的公司是可查询的、artifact 丰富的、对 AI 可读的,那你几乎不该有任何人肉中间层。
> 🗣️ "Everyone comes to meetings with working prototypes, not pitch techs." —— Diana Hu
> 译:每个人来开会都带着能跑的原型,而不是一份路演 PPT。
> 🗣️ "Maximizing token usage, not headcount, will be the critical shift. The best companies will be the ones that are token maxing." —— Diana Hu
> 译:关键的转变是最大化 token 用量、而不是人头数;最好的公司会是那些在"token maxing"的公司。

### 7. startup 会赢下这场转变 / Startups will win this shift `[09:12–10:27]`
**要点(中文)**: 对这些工具的信念(conviction)不能外包,创始人必须亲自坐下来用 coding agent,用到打破自己对"什么可做"的旧认知为止。早期创始人有巨大优势:没有遗留系统、固化的组织架构、成千上万要再培训的人,小到可以从第一天就把公司搭对。大公司则要一边维护/增长现有产品,一边拆掉多年的标准流程和"软件如何被写"的核心假设(有些靠内部 skunk works 小队从零搭 AI 原生系统,如 Mutiny),天然更难转向。这正是 startup 的最大 edge——从一开始就围绕 AI 设计系统、流程和文化,从而比巨头快上千倍。
> 🗣️ "You need to develop it yourself by actually sitting with coding agents and using them until you start to break your own priors about what is now possible to build." —— Diana Hu
> 译:你得亲自去建立这份信念——真的坐下来用 coding agent,一直用到你开始打破自己对"现在什么能做出来"的旧有成见。
> 🗣️ "You are small enough to build your company right from day one." —— Diana Hu
> 译:你足够小,小到可以从第一天起就把公司搭对。
> 🗣️ "You can design your systems, workflows and culture around ai from the start and as a result operate thousand times faster than the incumbents." —— Diana Hu
> 译:你可以从一开始就围绕 AI 来设计你的系统、工作流和文化,结果就是比在位巨头快上千倍运转。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **把自家产品先用在自己身上**:立刻接一个 agent 到你的 Linear/Slack/GitHub/客户反馈/站会录音,做一次"上个 sprint 到底交付了什么、是否满足客户"的自动复盘,把它变成每周闭环。
- [ ] **为每个关键流程设计闭环**:对招聘、销售、支持、工程各挑一个流程,明确"采集什么信息→喂回哪个智能系统→如何自我改进",替换掉当前"做完就不测量"的开环。
- [ ] **让公司可查询**:上 AI 会议记录、把决策从 DM/邮件搬到能被 agent 读取的渠道,建一个覆盖营收/销售/工程/招聘/运营的统一 dashboard,让每个动作都产出 artifact。
- [ ] **搭一个最小软件工厂**:在自己代码库里试"人写 spec + 测试、agent 写实现并迭代到测试通过"的流程,选一个模块尝试"零手写代码",定义清晰的 pass/满意阈值。
- [ ] **按三原型组队**:招人时按 IC(人人都 build)/DRI(一人一结果)设计,而不是招中层协调者;开会强制"带能跑的原型,不带 PPT"。
- [ ] **接受 token maxing 的成本结构**:主动把预算从人头转向 API/token,允许"不舒服的高 API 账单",并把"每人 token 用量/产出"作为观察指标。
- [ ] **创始人亲自练 conviction**:每周固定时间亲手用 coding agent 造东西,记录哪些旧假设被打破,不要把 AI 战略外包给某个负责人。

## 🔑 关键术语 / 概念
- **Closed loop / Open loop(闭环 / 开环)** — 来自控制系统:开环无反馈、天然有损;闭环持续监控输出并自我调整,用来让公司流程自我改进、稳定可靠。
- **Queryable / Legible to AI(可查询 / 对 AI 可读)** — 组织的每个重要动作都产出 artifact,使中心智能能随时查询、学习并优化流程。
- **Artifact(产出物)** — 会议记录、工单、文档、录音等可被 AI 学习的结构化痕迹;"每个动作都产出 artifact"是可查询的前提。
- **AI software factory(AI 软件工厂)** — TDD 的进化:人写 spec + 测试,agent 生成并迭代实现,直到达到"概率性满意阈值";极致形态是代码库无手写代码。
- **1,000x engineer(千倍工程师)** — Steve Yegge 提出的概念:用一整套 agent 系统包裹单个工程师,使其造出过去不可能造的东西。
- **Human middleware(人肉中间层)** — 旧组织里上下转发信息的中层管理/协调者;AI 智能层替代其职责后应几乎归零。
- **IC / DRI / AI-founder(三种员工原型)** — IC 是人人皆 builder 的执行者;DRI 是一人一结果的直接负责人;AI-founder 型是亲自示范能力跃迁的创始人。
- **Token maxing** — 以最大化 token 用量(而非人头)为核心指标;宁可背高 API 账单,因为它替代的是更贵、更臃肿的人力成本。

## 🔖 高价值金句时间戳
- `[01:21]` "It should be the operating system your company runs on." — AI 定位的一句话总纲:操作系统,而非附加工具。
- `[02:26]` "To build these closed loops, you will need to make your entire company queryable." — 想要闭环,先让全公司可被 AI 查询。
- `[04:12]` "You need to provide models with as much context as you would provide an employee." — 拿到 AI 全部能力的前提:上下文要像给员工一样足。
- `[05:18]` "Their repos contain no handwritten code, just specs and test harnesses." — 软件工厂的极致形态,给工程组织一个清晰的进化终点。
- `[08:25]` "Maximizing token usage, not headcount, will be the critical shift." — 从堆人头到 token maxing 的成本观转变。
- `[09:06]` "Using them until you start to break your own priors about what is now possible to build." — 创始人建立信念的唯一方法:亲手用到认知被打破。
