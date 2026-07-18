# 我们认识的最"AI 上头"的 CEO / The Most AI-Pilled CEO We Know

📄 **[点此查看全文转录 / Full transcript »](../transcripts/mPAHvz8kW24.md)**

> **来源**: [The Most AI-Pilled CEO We Know](https://www.youtube.com/watch?v=mPAHvz8kW24) · Y Combinator · 2026-06-10 · 时长 54:07
> **讲者**: Pedro Franceschi(Brex 联合创始人兼 CEO,嘉宾);主持为 Y Combinator《The Lightcone》partners —— SPEAKER_01(疑为 Garry Tan,反复谈自建 G-Brain/G-Stack),另有 SPEAKER_00、SPEAKER_05 等提问的合伙人
> **一句话定位**: 一位把整个公司围绕 AI Agent 重建的 fintech CEO,示范如何用"Agent loop + tools + 网络层安全 + 自学习 eval"把公司从 day 0 重造 —— 对想做 AI Agent 创业的人,这是一份"如何以 LLM 为地基造公司"的实操心法。

## 🎯 TL;DR(中文核心要点)
- **好的 AI 产品本质只有一个形态:agent loop + tools。** 别过度工程化 harness,别把 LLM 当"昂贵易碎品"锁进"富士康工厂"式的 if 判断里 —— 给它 token,"放开爪子"(free the claw)让它跑。
- **企业级 Agent 安全要做在网络层,不是在 shell/工具层。** Brex 开源了 CrabTrap:HTTP 代理整个 Agent 的网络边界,录一天流量→自动生成策略→98% 请求自动放行、2% 交给 LLM-as-judge。这是他们敢在生产环境放开 Agent 的关键解锁。
- **"AI 上头"的检验标准:生活中任何问题,你是否默认先想"能不能用 AI 解"。** 80% 用 chatbot 能解,剩下 20% 解不了的地方,去搞清楚为什么、并亲手造个东西解决它 —— 目的是获得对技术边界的"手感",而非立刻变现。
- **从 day 0 起把"能不能只有我一个人"当作公司前提。** 当公司边界变成"类型系统"、接口变成"Agent 之间对话而非人",公司的肌理(fabric)会长得完全不同,token 消耗自然更高。
- **执行力已经外包给模型了,稀缺的是"选择的智慧"。** 客户不会把答案塑造成你能直接喂给 LLM 的 prompt —— 创始人的 alpha 在于捕捉"模型训练数据里没有的信号"(客户没说出口的东西)。
- **别把 AI"贴"在旧流程上,要把问题重新定义。** Brex 重做 KYC 时不是"给旧流程加个 Agent",而是端到端重设计:KYC 变免费后,可以把风控前移到漏斗顶端给 lead 做资格判定 —— 问题的边界因此改变。
- **CEO 必须是 Chief AI Officer。** 只有掌握全局 context 的人能重构系统本身;而且"除了董事会没人能对 CEO 说不",打破旧流程的成本 CEO 比高管低 10 倍、高管比员工低 10 倍。
- **把公司做成自学习系统:让每一次人工介入都变成一个 eval case。** 多数公司花大力气"让 Agent 能跑",却从不想"如何让 Agent 每天变好" —— 后者才是最大解锁。

## 🧭 适合谁 / 什么时候看
- **正在或即将做 AI Agent 创业的工程师**:想知道"以 LLM 为地基"该如何设计产品形态、安全边界、公司结构。
- **已经在用 Claude Code / OpenClaw 但仍"舍不得烧 token"、习惯过度控制 context 的开发者**:本集专治这种"富士康式"心态。
- **正在为大公司做 AI 转型的人**:看 CEO 视角如何"重founding"公司、打破组织抗体(antibodies)。
- **不适合**:想要具体融资/招聘战术手册的人 —— 本集几乎不谈钱和 term sheet,谈的是心法与组织。

## 📝 分段精读

### 1. 如何变得"AI 上头" + 电力类比 / How Pedro Became AI-Pilled + The Electricity Analogy `[01:13–05:21]`
**要点(中文)**: Pedro 从疫情期玩 GPT-3(觉得像"研究项目,玩 10 分钟就停")到被"推理模型 + 工具"点燃。他给团队的比喻:"电力是在去年 12 月被发明的,那台电力就是 Opus 4.5"。现在是 2026 年 5 月,我们只是站在"电力发明后五六个月"的时点上,大多数人还在研究蜡烛能干什么,而蒸汽机还要 20 年才来 —— 意思是:今天的一切都还极早,别用"蜡烛的视角"评判 AI。
> 🗣️ "the way I describe it to my team is like, electricity was invented in December, and I think electricity was Opus 4.5." —— Pedro Franceschi
> 译:我跟团队这样描述:电力是在(去年)12 月被发明的,而那台"电力"就是 Opus 4.5。
> 🗣️ "you're sort of five or six months after electricity was invented. And most people are still playing with candles and questioning, what can you do with candles and fire?" —— Pedro Franceschi
> 译:我们大概就处在"电力被发明后五六个月"的位置,而大多数人还在摆弄蜡烛,追问"蜡烛和火能干什么"。

### 2. 放开爪子 / Free the Claw `[05:21–06:56]`
**要点(中文)**: 全场核心隐喻。多数软件人仍把 LLM 当"昂贵易碎品",于是写几十万行代码(半百万行 Rails)去严控模型看到的 context,像"把 Agent 关进富士康工厂、6 点不起床就电击"。Pedro 认为这完全错了:每一个好的 AI 产品,本质都只是"带工具的 agent loop",别过度工程化 harness。让 Agent 去它想去的"Esalen 疗养院"(比喻:给它自由与 token)。个人实践里,他先给 Agent 对邮件/Slack/一切的**只读**访问权,惊讶于能走多远。
> 🗣️ "every single good AI product you've used is an agent loop with tools. That's it." —— Pedro Franceschi
> 译:你用过的每一个好的 AI 产品,本质都是一个"带工具的 Agent 循环"。就这么简单。
> 🗣️ "they've been treating the LLM like this very precious thing that's very expensive, and so as a result, you have to literally put the agent inside a Foxconn factory." —— SPEAKER_01(疑为 Garry Tan)
> 译:大家一直把 LLM 当成一种极其昂贵、极其珍贵的东西,结果就是你真的把 Agent 塞进了一座"富士康工厂"里(层层管控)。

### 3. 让 AI 在企业里安全落地:CrabTrap / Making AI Safe for Enterprise `[06:56–10:57]`
**要点(中文)**: 从"只读"到"可写"是最难的一步,安全团队最初一律说不。Pedro 花了约四周,结论是:安全必须做在**网络层**,而不是像 NVIDIA 等做的"给 shell/工具加控制"(因为模型绕过工具也能直接发 HTTP 请求)。Brex 因此造了并开源 **CrabTrap**:HTTP 代理 Agent 的整个网络边界,让每个请求可审计;由于模型是在数百亿网页文档上训练的,它读懂 HTTP 流量的能力异常强,"看一千个请求就能判断在发生什么"。录一天流量→生成策略→98% 自动放行、2% 用 LLM-as-judge 判定(如招聘 Agent "Jim")。他强调 Brex 不想做 HTTP 代理生意,只是为了站上前沿不得不做 —— 希望有 YC 公司做出更好的版本给他们用。
> 🗣️ "i don't see any reason why a yc company shouldn't be at the bleeding edge" —— Pedro Franceschi
> 译:我看不出有任何理由,一家 YC 公司不该站在(这项技术的)最前沿。

### 4. 为什么多数公司落后 + AI 是"同事"不是聊天机器人 / Why Most Companies Are Behind + AI Teammates, Not Chatbots `[10:57–14:22]`
**要点(中文)**: 公司内 AI 采用分三层:① token maxer(泡在编码 harness 里疯狂推代码的工程师);② 普通工程师(生产力约为前者 1/10);③ 公司其余所有人 —— 他们用 AI 的方式停留在"Google 搜索模式"(带几个 MCP 的 chatbot)。真正的价值来自 harness,所以关键是**为非技术团队造出等效的 harness**:不是"给几个 MCP 让他们自己玩",而是把 Agent 做成有 Slack、有邮箱、能进会议记笔记的"虚拟员工";这种 harness 会更像 OpenClaw 而非编码模型。主持人举例:YC 团队用语音(Aqua voice)在 Slack 里对着 claw 说话,就自动排出了 60 场晚宴×20 人×21 位合伙人的方案,"没人打开过 Claude Code"。
> 🗣️ "people forget that Claude code is a. Magic. It's just, it's just literally a harness around the same models." —— Pedro Franceschi
> 译:大家忘了 Claude Code 就是……魔法(其实不是)。它不过是围绕同一批模型的一层 harness 罢了。

### 5. Tokenmaxxing 的理由 / The Case for Tokenmaxxing `[14:22–18:24]`
**要点(中文)**: 很多创始人"舍不得烧 token"。Pedro 说成本只是其一,更本质的检验是"AI 药丸测试":生活里任何问题,你是否**默认先用 AI**。当这成为第二天性,大脑会被重塑到无法用旧方式思考。他反问:现在花很低的成本就能"亲密地摸清一个问题的边界",为什么很多人还没做?对创业者最重磅的一句:如果今天开公司,前提应该是"为什么不能只有我一个人",从这里出发 token 消耗自然更高 —— 因为公司的**接口从"人对人"变成"Agent 对 Agent"、边界变成类型系统**。
> 🗣️ "the AI pill test in my opinion is whatever problem shows up in your life, do you default to AI first or not?" —— Pedro Franceschi
> 译:在我看来,"AI 药丸测试"就是:生活中冒出任何问题时,你是否会默认先想到用 AI 去解。
> 🗣️ "the fabric of the company just looks very different when the boundaries become type systems. The interface is agents talking to each other versus people." —— Pedro Franceschi
> 译:当公司的边界变成"类型系统"、接口变成"Agent 之间对话而非人与人对话",公司的整个肌理会长得完全不同。

### 6. 一人公司 + 最小接触面 / The Company of One + Minimal Surface Area `[18:24–20:54]`
**要点(中文)**: 成功公司的共同模式是"最小接触面":早期 Stripe 就是一个 API、Brex 就是终端命令行、Airbnb 就是一个表单、DoorDash 也极简 —— 创始人的全部带宽都砸在打磨那**唯一一个交互模式**上。AI 时代的风险是"选择的能动性消失":你能同时实验一堆东西,反而丧失了"聚焦什么才重要"的纪律。如果你无法把问题压缩到清晰边界内,说明你还没找到对的问题。他的金句:"智能即压缩","好点子能写在一张餐巾纸上 —— 你的餐巾纸是什么?"
> 🗣️ "if you can't minimize your surface area and, and solve the problem with a very clear set of boundaries, you haven't found the right problem to solve" —— Pedro Franceschi
> 译:如果你没法把接触面压到最小、用一组清晰的边界去解决问题,那说明你还没找到那个真正该解决的问题。
> 🗣️ "intelligence is compression ... great ideas fit in a napkin" —— Pedro Franceschi
> 译:智能即压缩……真正伟大的点子能写在一张餐巾纸上。

### 7. AI 唯一替代不了的东西 / The One Thing AI Can't Replace `[20:54–28:06]`
**要点(中文)**: 找 idea/做 pivot 的方法仍是"两周为周期,在探索与利用间切换"。但 AI 时代最难的仍是"和客户聊、并从对话里萃取没说出口的信号"。为什么不能"prompt 出一家成功公司"?因为**这些信号不在模型的训练数据里**:客户只会给你基于其局部世界观的、次优的答案,不会替你塑造成能直接产出十亿美金产品的 prompt。执行力已被模型接管,稀缺的是"选择的智慧"。他还点出 LLM 最大陷阱:你无从知道模型对你所问的确切问题见过多少训练数据(采样频率)—— 分布外(out of distribution)的部分,正是创始人要亲手填补的地方。判断如何分配时间的好代理指标:**只有你能做、而模型做不了的事**。
> 🗣️ "The execution is out, right? The execution is gone and the model is going to do that better. The wisdom to choose is still, I think the, the missing bottleneck." —— Pedro Franceschi
> 译:执行力已经出局了,对吧?执行这件事没了、模型会做得更好。而"选择的智慧"依然是那个缺失的瓶颈。
> 🗣️ "the biggest pitfall of LMS is you have no sense of how much training data the model has seen for the exact thing that you're asking it" —— Pedro Franceschi
> 译:LLM 最大的陷阱在于,你完全没有概念:对于你正在问的那个确切问题,模型到底见过多少训练数据。
> 🗣️ "a good proxy for how to spend your time is what are things that only you can do and the models cannot do" —— Pedro Franceschi
> 译:判断该把时间花在哪的一个好指标,就是问:有哪些事只有你能做、而模型做不了。

### 8. 构建客户世界模型 / Building Customer World Models `[28:06–32:58]`
**要点(中文)**: Brex 在造"客户世界模型":把客户与公司的**每一个触点**(从点了几次 dashboard 按钮,到邮件、电话里说了什么)全部摄入,再推理"这个客户接下来需要什么、会遇到但还没遇到的问题是什么"—— 本质仍是个"分布问题"。他提醒:模型出厂时的"世界模型"是有偏的(如给会计科目举例默认蹦出"AI CapEx",因为造模型的人满脑子只有 AI CapEx),要专门去让 LLM 适配"和你很不一样的人"。关于"做多推理"的著名数据:全球 84% 的人从没用过 AI,16% 至少用过一次免费 chatbot,0.3% 付费 20 美元/月,2500 个方格里只有 1 格真正用上了 Agent —— 所以推理需求才刚开始。即便 token 成本降 10 倍,用量也会涨 10 倍,它仍会是公司最大开支;Brex 为此内建了 token 花费管理工具 Magpie。
> 🗣️ "84% of the world never used AI, 16% have used at least once a free chat bot then 0.3% ... paid 20 bucks a month for AI and one box out of the 2,500 actually use agents" —— Pedro Franceschi
> 译:全世界 84% 的人从没用过 AI,16% 至少用过一次免费聊天机器人,0.3% 付了每月 20 美元,而 2500 个方格里只有 1 格的人真正用上了 Agent。
> 🗣️ "building this customer world model is a similar idea where we're trying to get every single touch point that the customer has of us" —— Pedro Franceschi
> 译:构建这个"客户世界模型"是同一个思路:我们试图抓取客户与我们之间的每一个触点。

### 9. 围绕 AI 重建 Brex / Rebuilding Brex Around AI `[32:58–39:02]`
**要点(中文)**: 别只盯 token 的 ROI —— 就像"电力发明六个月后有人抱怨电费太高、要少用点、把蒸汽机推迟 20 年"一样荒谬(而且电力早期 ROI 确实很烂,若那时按会计算账就会放弃)。真正的做法是承认存在一个"不连续点":不只是"怎么解决问题"变了,连"问题的定义本身"都变了。Brex 的最大正向跃迁,都来自"把旧做法搁到角落里,问:如果今天从零开始会怎么设计?"以 KYC 为例:与其给旧流程加 Agent,不如端到端重做 —— 当 KYC 变"免费",就能对 lead(而非已成交客户)做资格判定,把风控前移到漏斗顶端,进而改变你到底该瞄准谁。这需要一点"创始人能量"去推动。
> 🗣️ "there is a discontinuity in in the not just in how we solve the problem but on what the definition of the problem actually even is" —— Pedro Franceschi
> 译:这里存在一个不连续点 —— 变的不只是我们"怎么解决问题",还有"问题的定义本身到底是什么"。
> 🗣️ "when you have kyc for free you can you can kyc a lead versus the customer so you start to have risk orientation up in your funnel and that changes who you even target" —— Pedro Franceschi
> 译:当 KYC 变得免费,你就能对一个"潜在线索"而不只是"已成交客户"做 KYC,于是风控被前移到漏斗顶端,而这会改变你到底该瞄准谁。

### 10. CEO 必须是首席 AI 官 / The CEO Must Be the Chief AI Officer `[39:02–43:50]`
**要点(中文)**: AI 不是工程团队或产品团队的事,CEO 必须比任何人都更懂技术的边界 —— 因为只有掌握全局 context 的人才能重构"系统本身"(KYC 团队永远想不到用 KYC 技术去给 lead 打分)。而且"除了董事会没人能对 CEO 说不,董事会又不在细节里",所以打破旧流程 CEO 成本最低:CEO 比高管低 10 倍、高管比员工低 10 倍。公司会像免疫系统一样长出"抗体"去排斥任何破坏社交和谐的变化,所以要**给升级/审批路径"脱敏"**、让它更快。AI 分三条线:产品 AI、运营 AI、公司内部 AI(corporate AI),三者都重要、权重随公司阶段变化。若你是非 AI 原生的大公司,本质是在做一场"turnaround"。
> 🗣️ "I think the CEO needs to be the chief AI officer. Like it's not an engineering team thing. It's not like a product team thing. It's like you have to understand the bounds of the technology better than anyone." —— Pedro Franceschi
> 译:我认为 CEO 必须是首席 AI 官。这不是工程团队的事,也不是产品团队的事,而是你得比任何人都更清楚这项技术的边界在哪。
> 🗣️ "you have to sort of refound the very concept of what the company self-identity is" —— Pedro Franceschi
> 译:你几乎得把"公司的自我身份认同究竟是什么"这件事,重新奠基一遍。

### 11. 构建公司 AGI + 自学习 eval / Building Company AGI + Self-Learning Evals `[43:50–51:43]`
**要点(中文)**: 认同 Jack Dorsey"每家公司都在造自己的 company AGI",但方式不同:不信"单一大模型塞进所有数据无判断",而信"虚拟员工"路线 —— 让一个 Agent 把"某类问题(如彻底理解某个客户)"做到极致,边界清晰、可自包含、可上 eval;再让别的 Agent 在其之上做产品路线图,像"虚拟高管团队"。判断标准是"AI 界的 Tesla":不信任何没有真实使用的东西 —— 它是否真的替代了招人、真的省下了小时数?最强解锁是把公司做成**自学习系统**:让每一次人工介入都变成一个 eval case(如 KYC 例外、报销 Agent 对话出问题→自动触发 Agent 改代码和 prompt 让该 eval 通过),需要一个"每晚回看一切的 dream cycle"。多数公司只让 Agent"能跑",却不想"如何让它每天变好"。
> 🗣️ "how do you have every single human interaction in a company becoming an eval when you have an AI agent?" —— Pedro Franceschi
> 译:当你有了 AI Agent,怎么让公司里的每一次人类互动都变成一个 eval(评测样本)?
> 🗣️ "they spend a lot of time getting an agent working, but never thinking how to make the agent improve every day" —— Pedro Franceschi
> 译:他们花大量时间让一个 Agent 能跑起来,却从没想过如何让这个 Agent 每天都变得更好。
> 🗣️ "We're kind of like the Tesla for AI. We're like, I don't believe in anything that doesn't have real usage." —— Pedro Franceschi
> 译:我们有点像"AI 界的特斯拉":我不相信任何没有真实使用量的东西。

### 12. 为什么现在还极早 / Why We're Still So Early(收尾寄语) `[51:43–54:07]`
**要点(中文)**: 给创始人的三条:①牢记电力类比 —— 站在人类 200 年时间轴上,你正处在"电力问世六个月"的时点,若你知道它未来的一切会怎么做?去做那些不同的事。②在电脑上贴张便利贴:醒来后,你生活里任何问题,为什么不能用 AI 解?80% 用 chatbot,剩 20% 解不了的,搞清原因并亲手造工具解决 —— 为的是获得对技术可能性的"手感"。③度量你的 token 消耗、逼近公司极限,以"为什么不能只有我一个人"为前提;你会撞上模型能力的墙,而你作为创始人真正该花时间的,是"哪些问题值得解"和"LLM 做不了、必须我亲自做的是什么"。
> 🗣️ "have a post-it on your computer, which is you wake up, whatever problem you have in your life, why can't you solve it with AI?" —— Pedro Franceschi
> 译:在电脑上贴一张便利贴:每天醒来,你生活里遇到的任何问题,为什么不能用 AI 来解?
> 🗣️ "why can't it just be one person? Like, why can't it just be me that builds the whole thing?" —— Pedro Franceschi
> 译:为什么不能只有一个人?为什么不能就我一个人把整件事做出来?
> 🗣️ "rebuilding it the way you would do it in 2026, with electricity being six months old." —— Pedro Franceschi
> 译:以"2026 年、电力才诞生六个月"的姿态,把它(公司/产品)重新造一遍。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **先做减法,再做 Agent**:把产品压到"最小接触面"——能写在一张餐巾纸上的单一核心交互;写不出来,说明还没找到对的问题。
- [ ] **产品形态就用 agent loop + tools**:别为了控制 context 写几十万行 harness/if 判断("富士康工厂"心态);先给只读访问、放开跑,再逐步收权。
- [ ] **把安全做在网络层**:参考并直接用 Brex 开源的 **CrabTrap** —— HTTP 代理 Agent 的网络边界,录流量→生成策略→高频请求自动放行、边缘 case 交 LLM-as-judge;这是拿到"生产环境放行"信任的关键。
- [ ] **为非技术用户造"虚拟员工"harness**,而不是丢几个 MCP:给 Agent 配 Slack/邮箱/会议记录能力,让它能自举(self-bootstrap)技能(skills/markdown)。
- [ ] **从第一天起把"为什么不能只有我一个人"当公司前提**,并主动度量 token 消耗、逼近极限 —— 别做"舍不得烧 token"的创始人。
- [ ] **把每一次人工介入变成 eval**:搭建"自学习 dream cycle",让线上异常/人工纠正自动触发 Agent 改 prompt 与代码,使评测通过 —— 目标是 Agent 每天变好,而非仅仅"能跑"。
- [ ] **亲手填补"分布外"信号**:去和客户聊、捕捉他们没说出口的需求(模型训练数据里没有的信号),这是你相对模型唯一的持久 alpha。

## 🔑 关键术语 / 概念
- **Free the claw / OpenClaw** — "放开爪子":本集反复出现的隐喻,指停止过度管控 Agent、给它 token 与自由去自主完成任务;OpenClaw 指一种开放的 Agent 运行环境/harness(对应个人化、可深度定制的 Agent 栈)。
- **Foxconn factory(反面隐喻)** — 把 LLM 当昂贵易碎品、用大量 if 语句严控它看到的一切,像血汗工厂般压榨 Agent;与之相对是让 Agent 去"Esalen Institute"(自由发挥)。
- **CrabTrap** — Brex 开源(约两个月前)的 Agent 安全方案:HTTP 代理 Agent 整个网络边界,使每个请求可审计,并用另一个 Agent/LLM-as-judge 基于策略放行或拦截流量。
- **LLM-as-judge** — 用一个 LLM 依据既定策略判断某请求/输出是否该被批准,承担人工审核之外的边缘判定(Brex 招聘 Agent "Jim" 约 2% 请求走此路径)。
- **Token maxing / tokenmaxxing** — 刻意最大化 token 消耗、把 AI 用到极限的实践;公司内采用分三层:token maxer、普通工程师、"Google 搜索模式"的其余员工。
- **Customer world model(客户世界模型)** — 把客户与公司的每个触点全部摄入,用于预测客户接下来的需求;把"该客户需要什么"当成一个分布/建模问题。
- **Company AGI / virtual employee** — 不追求单一全知模型,而是造一批边界清晰、可上 eval 的领域 Agent(如"极致理解某客户"),再组合成"虚拟高管团队"。
- **Corporate AI / Operational AI / Product AI** — Brex 内部把 AI 分三条线:内部办公、直接支撑客户服务的运营、以及交付给客户的产品。
- **Out of distribution(分布外)** — 模型训练数据里稀疏/缺失的部分;创始人的价值在于识别并亲手填补这些盲点(数据标注公司 Mercor 等亦在做此事)。
- **Magpie** — Brex 内建的 token 花费管理/归因工具,用于追踪每一美元 token 支出并做 ROI 分析。

## 🔖 高价值金句时间戳
- `[02:45]` "every single good AI product you've used is an agent loop with tools. That's it." — 一句话定义 AI 产品形态:别过度设计,本质就是带工具的循环。
- `[03:13]` "electricity was invented in December, and I think electricity was Opus 4.5." — 全集的时间坐标:我们只在"电力问世半年"的起点,别用蜡烛视角评判。
- `[15:11]` "the AI pill test in my opinion is whatever problem shows up in your life, do you default to AI first or not?" — 判断自己是否真"AI 上头"的单一测试。
- `[18:38]` "great ideas fit in a napkin" — 逼自己做减法:说不清的餐巾纸,就不是对的问题。
- `[20:50]` "The execution is out ... The wisdom to choose is still ... the missing bottleneck." — 执行外包给模型后,创始人的稀缺能力是"选择的智慧"。
- `[30:06]` "84% of the world never used AI ... one box out of the 2,500 actually use agents" — "做多推理"的最直观论据:Agent 采用率几乎为零,一切刚开始。
- `[39:21]` "the CEO needs to be the chief AI officer ... you have to understand the bounds of the technology better than anyone" — 组织层面的核心结论:AI 转型是 CEO 的活。
- `[46:31]` "how do you have every single human interaction in a company becoming an eval when you have an AI agent?" — 自学习公司的落地机制:人工介入即评测样本。
