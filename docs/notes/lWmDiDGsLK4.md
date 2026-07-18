# 软件创造的未来:Replit CEO 谈应用软件价值归零与 Agent 栖息地 / The Future of Software Creation with Replit CEO Amjad Masad

📄 **[点此查看全文转录 / Full transcript »](../transcripts/lWmDiDGsLK4.md)**

> **来源**: [The Future of Software Creation with Replit CEO Amjad Masad](https://www.youtube.com/watch?v=lWmDiDGsLK4) · Y Combinator · 2025-09-12 · 时长 42:02
> **讲者**: Amjad Masad(Replit 联合创始人兼 CEO);现场为 AI Startup School 演讲 + 观众 Q&A(提问者为 SPEAKER_02~11 等,身份多不可考)
> **一句话定位**: 一位做了近 10 年"让人人都能编程"的 CEO 告诉你:写代码的 Agent 是易事,难的是 Agent 的"栖息地"(基础设施);应用软件价值终将归零,而做 Agent 创业最重要的护城河是领域知识。

## 🎯 TL;DR(中文核心要点)
- **写代码是 Agent 最容易的部分,真正的护城河是"栖息地"(habitat)**:沙箱化的云端 VM、可扩展、支持任意语言/包、内置 auth、数据库、部署、密钥管理、后台任务、存储、支付——把软件工程师用的一切都开放给 Agent。
- **"先做烂产品"是策略而非妥协**:模型每两个月就会变强,今天跑不通的产品两个月后可能突然可用。要把产品做在"当前能力的边缘"(edge of what's possible),赌曲线会来接你。
- **应用软件价值将归零**:当任何人一句 prompt 就能生成任意复杂度的软件,传统 SaaS 的可替代性会从今天的约 15% 走向 100%。案例:HR 同事 Kelsey 三天做出一款可卖数万美元/年的 org chart 软件。
- **用"自主性等级"给 Agent 定位**:L1 语言服务器 → L2 代码补全/Copilot → L3 Replit Agent v2(独立工作 10-15 分钟仍需人测) → L4 v3(接近全自主) → L5(一次开一千个 Agent,95% 可靠)。
- **v3 的三根支柱**:端到端测试(Agent 自己做 QA)、采样与模拟(fork 可回滚文件系统并行试多种解法再合并)、为每个功能自动生成测试防止改坏。可靠性的上限更多来自"环境反馈+快速试错",而非只靠训练。
- **组织将从层级变网络**:通才员工(设计/工程/PM 常常集于一人)成为常态,每个人的 KPI 不是"写这封营销邮件"而是"让业务成功";人人都像创业者。领域专精变得"指数级不那么重要"。
- **做 Agent 创业选赛道**:软件工程 Agent、SDR 已很拥挤;从你自己有热情、有领域知识的地方切入——"领域知识是做 Agent 公司最重要的东西"。
- **MCP 解决不了 Agent 之间的协作**:它本质是传统 RPC,agent-to-agent 的市场/协议仍是空白——"也许这就是某人要做的创业"。

## 🧭 适合谁 / 什么时候看
- 正在或准备做 **AI Agent 创业**、纠结赛道与护城河的创始人/工程师。
- 在思考"当写软件近乎免费,平台/公司如何还能赚钱"的产品与商业决策者。
- 想理解 **Agent 基础设施(沙箱、可回滚文件系统、自主性等级、测试闭环)** 该怎么搭的技术负责人。
- 关注 AI 如何重构组织形态(通才员工、主权个人)与个人职业路径的人。

## 📝 分段精读

### 1. 从大型机到 Agent:软件正在被"人人化" / From Mainframes to Agents `[00:00–02:42]`
**要点(中文)**: Masad 用一条历史线做心智模型:大型机(只有专家会用)→ PC(先是玩具,Excel 让它变生产力,如今连数据中心都是 x86)→ 软件工程(70 年代随 Unix/C 兴起,要读四五年书再练两三年)。软件正在经历同样的迁移:从"只有专家做"变成"人人能做"。Replit 九年来的使命就是"solve programming",而 AI 时代这一使命的终极表达,是让你**根本不必写代码**——因为代码本身才是"让更多人做软件"的瓶颈。
> 🗣️ "the ultimate expression of our mission is to make it so that you don't have to code. Code is the sort of bottleneck to actually getting a lot more people making software." —— Amjad Masad
> 译:我们使命的终极表达,是让你根本不必写代码。代码才是"让更多人做软件"的瓶颈。

### 2. 为什么现在全押 Agent:相信曲线,先做"烂产品" / Why Go All-In on Agents Now `[02:42–04:35]`
**要点(中文)**: Replit 在 2023 底/2024 初把全部资源压到 Agent 上。当时 Agent 几乎跑不通,但看 SWE-Bench(用真实 GitHub issue + 单测/PR 来测 Agent 的软件工程基准)就能看出趋势:22 年几乎不行、23 年开始能用、24 年初已明显在自动化大部分软件工程,如今约 70-80%。给所有做 Agent 的人的忠告:**要相信它一定会来**,并接受今天做出的是"烂产品"——因为两个月后模型变强,你的产品会突然变得可行。
> 🗣️ "we need to be okay with building crappy products today because two months down the line, the models will get better and your business, your product will suddenly become viable." —— Amjad Masad `[04:17]`
> 译:我们要接受今天做出的是烂产品,因为两个月后模型会变强,你的业务、你的产品会突然变得可行。
> 🗣️ "if any of you are building sort of agents, startups, just like really believe that it's coming." —— Amjad Masad
> 译:如果你们在做 Agent 创业,请真心相信它一定会来。

### 3. Agent 的"栖息地":基础设施才是难的部分 / The Agent's Habitat Is the Hard Part `[04:35–06:08]`
**要点(中文)**: 能写代码的 Agent 是易事,难的是围绕它的一切——Masad 称之为 Agent 生活的"栖息地"(habitat):云端、沙箱化(Agent 会搞坏你的电脑)、可扩展到百万用户、支持任意语言与系统/语言包(Agent 是在标准 Linux 环境里训练的,要能用 shell、读写文件、装包)。再往上是部署、数据库、内置 auth(Agent 不擅长做认证,一行代码打开 Replit Auth)、密钥管理、后台任务、存储、支付。他呼应 Karpathy 的观点:写代码是易事,难在周边——但很多难题 Replit 其实已经解决了。
> 🗣️ "but agents that can write code is actually the easy part. The hard part is the infrastructure around it. Sometimes I call it the habitat for which the agent lives in." —— Amjad Masad `[04:35]`
> 译:能写代码的 Agent 其实是最容易的部分,难的是围绕它的基础设施。我有时把它叫作 Agent 赖以生存的"栖息地"。

**更激进的设想**:支付不止是让用户付费,还要让 **Agent 自己有钱包**去按需开通服务、甚至去 TaskRabbit 上**雇人类**(比如遇到验证码时找人来解),乃至在市场上**雇其他 Agent**(会计、销售等)。而 MCP 本质是传统 RPC 协议,解决不了这种 agent-to-agent 的协作。
> 🗣️ "you would want your agent to have some kind of wallet to be able to go pay for services." —— Amjad Masad `[08:04]`
> 译:你会希望你的 Agent 有某种钱包,能自己去为服务付费。

### 4. 自主性等级与 Agent V3:测试、采样模拟、自动测试 / Autonomy Levels & Agent V3 `[06:08–15:42]`
**要点(中文)**: 用自动驾驶类比给 Agent 分级:L1=语言服务器/IntelliSense(≈车道辅助)、L2=代码补全/Copilot、L3=Replit Agent v2(能独立干 10-15 分钟,但需你不时测试)、L4=正在做的 v3(接近全自主)、L5=未来两三年可**一次开一千个 Agent 解一千个问题、95% 可靠**,让任何人都能指挥成百上千个 Agent,程序员影响力指数级放大。v3 建在三根支柱上:①端到端测试——让 Agent 自己做 QA,把工作时长拉到 1-2 小时;②采样与模拟——基于**全事务化、可回滚的文件系统**(每次编辑都是原子快照),遇到难题就 fork 出多个环境并行试不同解法,再把最优解合并回主分支,可靠性提升 2-3 倍;③为每个功能自动生成测试,防止 Agent 改着改着把旧功能弄坏(Claude Code、Cursor 都有此病)。
> 🗣️ "You want to build a product at the edge of what's possible. Right now, the edge of what's possible is like computer use." —— Amjad Masad `[11:42]`
> 译:你要把产品做在"当前能力的边缘"。而现在能力的边缘,大概就是 computer use。
> 🗣️ "in the next couple of years, you can really spin up a thousand agents, give them a ... thousand problems and reliably be confident that like 95% of them is going to work." —— Amjad Masad `[10:31]`
> 译:未来两三年,你真的可以开出一千个 Agent、丢给它们一千个问题,并可靠地相信其中约 95% 能做成。

### 5. 预测:应用软件价值归零 / Prediction: Application Software Goes to Zero `[15:56–18:31]`
**要点(中文)**: Masad 放弃预测时间线,但笃定方向:当任何人一句 prompt 就能生成任意类型、任意复杂度的软件,应用软件的价值会趋近于零、变得极其便宜,没人能靠传统 SaaS 赚钱。今天你已经能用 Replit Agent 替换掉一部分采购的 SaaS,这个比例会从约 15% 走向 100%。**注意他限定的是"应用软件(application software)",不是所有软件**。案例最有说服力:从没写过代码的 HR 同事 Kelsey,因为市面上的 org chart 软件贵(数万美元/年)又不满足她连 ADP 薪酬系统等定制需求,自己用三天做出一款——公司如今在用,且完全可以当 SaaS 卖数万美元/年。
> 🗣️ "My prediction is that all application software will go to zero. In other words, software will be dirt cheap." —— Amjad Masad `[15:56]`
> 译:我的预测是所有应用软件的价值都会归零。换句话说,软件会便宜到尘埃里。
> 🗣️ "She took ... three days. And she made an org chart software that we're using today that we can go out on the market and sell it as a SaaS product for tens of thousands of dollars a year." —— Amjad Masad `[17:26]`
> 译:她花了三天,做出一款我们今天在用的 org chart 软件——它完全可以拿到市场上当 SaaS 卖数万美元一年。

### 6. 通才员工与"主权个人":公司会像网络而非层级 / Generalists & the Sovereign Individual `[18:31–26:00]`
**要点(中文)**: 工业革命以来的分工(每人只做产品的一部分、越可替代越好)将被逆转:当 HR 同时也能当工程师、营销、任何角色(因为有 Agent 帮她做任何事),岗位会变得更不专精、更不孤岛化。Replit 已在这样组织:第一次搭建产品团队,而设计师/工程师/PM 常常**集于一人**。组织图会更像开源项目那样的**网络**而非传统层级;每个员工早上醒来的使命不是"写这封营销邮件",而是"让业务产生价值"——人人都是创业者。他引用 80 年代的《主权个人》(The Sovereign Individual):**"想法将成为财富"**,智能时代里清晰的思考者都可能致富,像 Satoshi 那样一个人创造万亿美元价值将成常态。领域专精仍重要,但"指数级不那么重要"了。随着交易成本趋近于零,请一个全职员工的理由会减少——将来找个开发者(无论是 Agent 还是人)会像叫 Uber 一样一键完成,公司可以像临时任务一样快速组建又快速解散。
> 🗣️ "So everyone is sort of an entrepreneur." —— Amjad Masad `[20:45]`
> 译:于是每个人都某种程度上是创业者。
> 🗣️ "Ideas will become wealth. Merits, wherever it arises, will be rewarded as never before." —— Amjad Masad(引自《The Sovereign Individual》)`[21:37]`
> 译:想法将成为财富;才华无论出现在何处,都将得到前所未有的回报。
> 🗣️ "at some point Replit needs to stop being focused on making applications, and start being focused on solving problems with software." —— Amjad Masad `[25:46]`
> 译:某个时点,Replit 必须从"专注于做应用"转向"专注于用软件解决问题"。

### 7. Q&A 精选:怎么开一家 Agent 公司、职业该怎么选 / Q&A Highlights `[26:00–42:02]`
**要点(中文)**: 密度极高的实战问答。
- **多 Agent 世界 & 协议空白**:未来是多 Agent 的——有独门领域知识的专家不会开源、不会卖给数据标注厂,而是把知识灌进一个高度专精的 Agent 来规模化自己;MCP 解决不了 agent-to-agent,这里需要新协议,"也许就是某人要做的创业"。`[26:21]`
- **人还剩什么**:AI 今天无法真正"分布外泛化",一切能力都要在数据里有表征;真正新颖的问题仍需人类的独创性,人会更多坐在"创意的位置"上。`[28:33]`
- **职业建议**:想成为通才,就**尽早加入创业公司**——越早越通才(创始人>1 号员工>……到第 100 号就没那么多了);哪怕是 Series B 公司的 20 号员工也胜过大厂。而且要**主动去找通才机会**:别等人派活,醒来看的不是 to-do list 而是 mission。`[34:01]`
- **护城河 = 领域知识**:软件工程 Agent、SDR 已很拥挤;从你自己有热情、有领域知识的地方入手(比如你就是合规官就去做合规 Agent),因为你学得最快、领域知识最深。`[37:04]`
- **Replit 怎么持续赚钱**:他限定的是"应用软件"归零而非所有软件;Replit 要成为"通用问题解决器",凭"全栈——从想法到部署与扩容"取胜。`[38:22]`
- **Agent 训练的误差累积怎么办**:未来会转向 **AlphaZero 式训练**——在 RL 环境里自生成问题、自我博弈、大规模并行求解,而不是训在人写的代码上(因为将来没那么多人写的代码了)。`[40:13]`
> 🗣️ "domain knowledge is the most important thing to build an agent company." —— Amjad Masad `[38:01]`
> 译:领域知识是打造一家 Agent 公司最重要的东西。
> 🗣️ "Join startups as early as possible. ... I'm not looking at a to-do list. I'm looking at a mission." —— Amjad Masad `[34:01] / [34:57]`
> 译:尽可能早地加入创业公司……我早上醒来看的不是待办清单,而是使命。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **把产品做在"能力边缘",并接受它今天很烂**:选一个当前模型刚够着的任务,先发布,押注 2-3 个月后的模型升级把它抬进可用区;别等模型完美了再做。
- [ ] **护城河先看"领域知识"再看技术**:避开软件工程 Agent、SDR 等红海;从你自身有热情+领域纵深的垂直切入(会计、合规、HR、行业专业等),把独家 know-how 灌进一个专精 Agent。
- [ ] **优先投资"栖息地"而非只投模型**:给你的 Agent 建云端沙箱 VM、开放的包/语言环境、内置 auth、部署、密钥、存储、支付;可靠性上限来自"环境反馈+快速试错",不只靠换更强的模型。
- [ ] **搭一套可回滚/事务化的执行环境 + 测试闭环**:让 Agent 能 fork 并行试多种解法再合并最优解(采样与模拟),并为每个功能自动生成会在每次改动时运行的测试,防止"改一个功能弄坏另一个"。
- [ ] **用"自主性等级"给路线图定位**:明确你现在是 L2/L3/L4,分别投"可靠性(推理+并行试错)"与"自主性(端到端测试、去人类在环)",两条线都要推。
- [ ] **组织按"通才 + 网络"来搭**:让工程/设计/PM 尽量合于一人,每人的 mandate 是"让业务产生价值"而非单一职能;招人优先招能像创业者一样主动找 mission 的人。
- [ ] **提前想清楚"软件归零后如何赚钱"**:把定位从"帮客户做应用"升级为"用软件替客户解决问题"(通用问题解决器),并盘一盘 agent-to-agent 协议/市场这类尚无人做的空白。

## 🔑 关键术语 / 概念
- **Habitat(栖息地)** — Masad 对 Agent 所需基础设施的比喻:沙箱云 VM + 开放包/语言环境 + auth/数据库/部署/密钥/后台任务/存储/支付等,让 Agent 像软件工程师一样在其中工作。
- **SWE-Bench** — 软件工程 Agent 基准:取真实 GitHub 仓库的 issue,配上单测和 PR 终态,把 Agent 放进环境去解;Replit 用它的分数曲线判断"软件工程正在被自动化"(现约 70-80%)。
- **自主性等级 L1–L5** — 借自动驾驶给 Agent 分级:L1 语言服务器、L2 代码补全、L3 Agent v2(独立 10-15 分钟需人测)、L4 v3(近全自主)、L5(千 Agent 并行、95% 可靠)。
- **Sampling & Simulations(采样与模拟)** — 基于可回滚事务化文件系统,对同一难题 fork 出多个环境并行尝试不同解法,再合并最优解,以提升可靠性。
- **事务化/可回滚文件系统** — Replit 每次文件编辑都是原子快照,可 cheap copy-on-write fork,也可回到任意历史 checkpoint 重启应用;是让模型更可靠的关键基础设施。
- **Computer Use** — 模型像人一样进入电脑点击操作(如 OpenAI Operator);当前慢、贵、不够好,但被视为"能力边缘",是 v3 端到端测试的方向。
- **The Sovereign Individual(主权个人)** — 一本 80 年代的书,预言了加密货币、远程办公等;核心观点"想法将成为财富",个人靠技术/Agent 就能独立创造巨额价值。
- **AlphaZero 式训练** — 先用互联网数据训一个 LLM,再在 RL 环境里让它自生成问题、自我博弈、大规模并行求解,以突破"没有人写代码可训"的瓶颈。
- **MCP(此处语境)** — Masad 认为 MCP 本质是传统 RPC 协议,解决不了 agent-to-agent 的协作/发现问题,该领域协议仍是空白。

## 🔖 高价值金句时间戳
- `[04:17]` "we need to be okay with building crappy products today because two months down the line, the models will get better ... your product will suddenly become viable." — 押注模型曲线:今天做烂产品是策略,不是失败。
- `[04:35]` "agents that can write code is actually the easy part. The hard part is the infrastructure around it." — 护城河不在会写代码,在 Agent 的栖息地。
- `[11:42]` "You want to build a product at the edge of what's possible." — 把产品做在能力边缘,等曲线来接。
- `[15:56]` "My prediction is that all application software will go to zero." — 应用软件价值归零,倒逼你重新定义你卖什么。
- `[20:45]` "So everyone is sort of an entrepreneur." — 通才组织里,每人的 KPI 是让业务产生价值。
- `[38:01]` "domain knowledge is the most important thing to build an agent company." — 选赛道的第一性原则:从你有领域知识的地方切入。
