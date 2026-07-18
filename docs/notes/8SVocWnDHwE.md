# AI 正在解锁数百万新一代"建造者" / AI Is Unlocking Millions Of New Builders

> **来源**: [AI Is Unlocking Millions Of New Builders](https://www.youtube.com/watch?v=8SVocWnDHwE) · Y Combinator · 2026-03-16 · 时长 39:32
> **讲者**: The Lightcone 播客(YC 合伙人主持,Garry Tan 因陪审团缺席);嘉宾为 Emergent 联合创始人、双胞胎兄弟 **Mukund Jha(SPEAKER_03)** 与 **Madhav "Maddy" Jha(SPEAKER_02)**;另有主持人 SPEAKER_05 / SPEAKER_01 / SPEAKER_04
> **一句话定位**: 一家从"编码 Agent 研究公司"起步、再打包给非技术用户的 YC 明星公司,讲透了 AI Agent 创业中"验证即护城河、为生产而建、第二名如何赢、精简团队"的实战心法,对做 Agent 工具/平台的创始人极具参考价值。

## 🎯 TL;DR(中文核心要点)
- **把"验证(verification)"当成核心壁垒**:Emergent 最初做软件测试 Agent,顿悟出"能解决验证,就能自动化整个软件工程"——验证回路是让 Agent 长时间自主运行的关键。做 Agent 一定要先把"如何自动判断任务是否完成"做扎实。
- **从工程满配倒推产品,而非从 UI 往上加能力**:他们先做出 SWE-bench 世界第一的编码 Agent(纯研究公司),再把强能力"藏起来"打包给非技术用户;方向与 Lovable/Bolt 相反(后者从 UX 起步、再补能力)。起点决定了能否覆盖完整软件生命周期,某些架构选择"很难逆转"。
- **为生产而建,而非只做原型**:最后一公里(部署、后端、安全、托管)是别人最容易忽略、也最值钱的 20%。他们自建 K8s/容器 沙箱,**让 Agent 在构建期和部署期用同一套基础设施**,从而大幅减少部署问题,并能给 Agent 快速反馈。
- **"你的 Agent 只和你给它的反馈一样好"**:自建 infra 的意义在于闭环反馈;多 Agent 架构 + 跨会话长期记忆(基于历史轨迹自动生成"技能"并过 CI/CD),让 Agent 跨用户、跨会话持续学习。
- **第二名也能赢**:每一代新模型都是"重新想象世界"的新机会;后发者能从对手的失败中学习、以更大的想象力从不同起点切入。但**必须用"碾压式强产品 + 快速铺开分发(如影响者网络)"进入市场**。
- **精简团队靠"高难度问题 + 强 ownership"**:1–2 人做别人整家公司的事(部署 ≈ 两人做出类 Vercel、记忆 1 人搞定);招聘只看"问题解决能力 + ownership",顶尖人才被难题吸引。
- **客户同理心从第 0 天建立**:全员每周与客户对话、全员轮值客服;从印度做全球产品,创始人上线头五天亲自泡在客服台(靠 AI 处理法语/德语工单)。
- **SaaS 面临两大逆风**:工作流被 Agent 吞掉(不转型"Agent-first"很难存活)+ 用户要越来越定制化的自建软件;软件本身正在"Agent 化"(平台上约 20% 已是 agentic app)。

## 🧭 适合谁 / 什么时候看
- 正在做 **AI 编码 Agent / 通用 Agent 平台 / vibe-coding 工具** 的创始人,尤其纠结"要不要自建 infra、面向技术还是非技术用户"。
- 面对 Lovable/Bolt/Cursor/Devon 等强对手、担心"后发无优势"或"被模型公司吃掉"的团队。
- 想用**极小团队**做出大平台、或从非美国本土(如印度)做全球产品的创业者。
- 想理解"个性化软件 / SaaS 何去何从 / Agent 长任务与多 Agent 协作"趋势的产品与技术负责人。

## 📝 分段精读

### 1. Emergent 是什么、创始人背景、从测试 Agent 到通用编码 Agent / What Is Emergent + Backstory + From Testing to Coding Agents `[00:00–02:52]`
**要点(中文)**: 双胞胎兄弟 12 岁开始编程,Mukund 从 Google 出来后在印度做过巨型 quick-commerce 公司 Dunzo(管 300 人工程团队),Madhav 在 Amazon 建深度学习团队。2023 年他们以"自动化软件测试"申请 YC——当时 VC 觉得太疯狂。做测试 Agent 时顿悟:**验证是让 Agent 长时间运行的回路,解决了验证就能自动化整个软件工程**,于是转向通用编码 Agent,两个月做到 SWE-bench 世界第一。他们在那时就"发明"了多 Agent 系统、记忆、Agent 间通信、测试时算力扩展——比 Claude Code 出现还早。
> 🗣️ "verification is the loop which sort of keeps agent running for a longer period of time." —— Mukund Jha (SPEAKER_03)
> 译:验证,就是那个让 Agent 能持续运行更长时间的回路。
> 🗣️ "we were like cloud code before cloud code was a thing." —— Mukund Jha (SPEAKER_03)
> 译:早在 Claude Code 成为一个概念之前,我们就已经是"Claude Code"了。

### 2. 抢在市场前面 & 转向非技术用户 / Getting Ahead of the Market & The Pivot to Non-Technical Users `[02:52–05:22]`
**要点(中文)**: 有了强编码 Agent 后,他们按"常识"先走企业路线,花两三个月发现企业太慢;同时看到 Lovable、Bolt 疯长,于是把强 Agent 打包对外,2025 年 6 月小范围 beta 上线即起飞。原以为技术用户为主,结果**80% 是零编程基础的非技术用户**,遍布 190 个国家,且都在用它跑真实业务。别人当年在死磕的"JSON 结构化输出"等问题,他们判断"下一代模型会解决",于是不投入——把赌注押在模型进步上。
> 🗣️ "80 percent of the users who are on the platform are non-technical users with zero programming knowledge. And they're building like apps that that run real businesses on top of today." —— Mukund Jha (SPEAKER_03)
> 译:平台上 80% 的用户是零编程基础的非技术用户,而且他们正用这些 app 跑着真实的生意。

### 3. 为什么 AI 时代第二名也能赢 / Why Second Movers Can Win in AI `[05:22–09:04]`
**要点(中文)**: 每一代新模型都是"重新想象世界"的机会窗口(如 Opus 这一档模型能撑起超长任务、多 Agent 协同)。后发优势有二:一是能从对手"哪里没跑通"里学习;二是起点不同、"光圈"更大、想象力更大。他们看到多数竞品只擅长前端原型,于是从零重构一个覆盖代码评审/自动测试/调试/部署/安全/托管的端到端平台。但产品必须"碾压式强"才能被注意到;同时**早期重投分发**,搭建大规模影响者(influencer)网络快速铺开。
> 🗣️ "you fundamentally start from a different starting point right. Like ... your aperture of the world is like very different. Like your imagination is really big right." —— Mukund Jha (SPEAKER_03)
> 译:你从一个根本不同的起点出发,你看世界的"光圈"完全不同,你的想象力也大得多。
> 🗣️ "you'll have to enter the market with a really really strong product which is you know head and shoulder above what ... exists in the market today for people to take notice." —— Mukund Jha (SPEAKER_03)
> 译:你必须拿着一个远超市面现有产品、高出一头的强产品进场,人们才会注意到你。
> 🗣️ "We built out a large influencer network and that was a big part of our program" —— Mukund Jha (SPEAKER_03)
> 译:我们搭建了一个庞大的影响者网络,这是我们打法中很重要的一部分。

### 4. 为生产而建,而非只做原型 / Building for Production, Not Just Prototypes `[09:04–18:21]`
**要点(中文)**: 别人做到"能跑的产品"就停了,他们把最难、最被忽视的"最后一公里"(部署上线、后端、安全)也做完——这最后 20% 花了 80% 的功夫。关键工程决策:**自建 K8s/容器沙箱**,让 Agent 在构建期与部署期用同一套 infra,部署阶段几乎不出问题,且能给 Agent 快速反馈("你的 Agent 只和你给它的反馈一样好")。技术栈也不随大流(Python 后端 + React 前端,支持后台任务/队列)。多 Agent 架构上,主 Agent 驱动、子 Agent 承接委派(测试/设计搜索/集成),并把历史轨迹聚合成**跨会话长期记忆/自动生成的技能**(过 CI/CD 才入库),实现一种"持续学习"。同时刻意隐藏 VS Code/diff——非技术用户看到 diff 会"吓到";Mukund 甚至提出内部指标"agent experience(Agent 体验)"。对"Anthropic 会不会通吃"的担忧,他回应:编码只占这活儿的 20%,把 app 送上生产极难,谁更懂用户谁赢;且自建 harness 能在模型之上再榨出 20–30%。
> 🗣️ "the last mile that you mentioned is always what people neglect." —— Madhav Jha (SPEAKER_02)
> 译:你提到的"最后一公里",永远是人们会忽视的地方。
> 🗣️ "if you give your agents the same infra during the build time and the same infra during the deploy time, then during this deployment phase, you don't encounter those many problems" —— Madhav Jha (SPEAKER_02)
> 译:如果你让 Agent 在构建期和部署期用同一套基础设施,那么到部署阶段你就不会遇到那么多问题。
> 🗣️ "your agent is only as good as the feedback that you provide." —— Madhav Jha (SPEAKER_02)
> 译:你的 Agent,只能好到你给它的反馈那么好。
> 🗣️ "your agent learns not just from your own session. It learns across the sessions." —— Madhav Jha (SPEAKER_02)
> 译:你的 Agent 不只从你自己的这一次会话里学习,它跨会话地学习。
> 🗣️ "the coding aspect is only 20% of the job ... taking an app to production is like really, really hard." —— Mukund Jha (SPEAKER_03)
> 译:写代码只占这件事的 20%,把一个 app 真正送上生产才是极其困难的部分。

### 5. 现场 Demo:用 Emergent 造 app / Live Demo `[18:21–24:40]`
**要点(中文)**: Madhav 现场用一句 prompt 造"播客/面试练习"app;prompt 引擎能自动识别该用移动端还是全栈,即使选错 tab 也会在后台纠正。展示的真实用户案例:伊利诺伊做 AV 装修的做了 lead-gen 表单 app、挪威一位自称"business developer"(无编程背景)做了给律师用的 CRM。产品对非技术用户友好:动手前 Agent 会**主动追问澄清需求**、可用内置的 "emergent LLM key" 免去自配第三方 API key。他们还大量"吃自家狗粮":100% 用 Emergent 造了内部 Asana/Jira 克隆(省 3000–4000 美元/月订阅)、市场 CRM、客服系统——"最懂问题的人自己造工具"。
> 🗣️ "before agent goes off to build things, it asks you for some clarification because agent wants to make sure that it understood your ... requirements properly." —— Madhav Jha (SPEAKER_02)
> 译:在 Agent 动手去造之前,它会先问你一些澄清问题,因为它想确认自己真的正确理解了你的需求。
> 🗣️ "non-technical users, they even get panicked as soon as they see a diff" —— Madhav Jha (SPEAKER_02)
> 译:非技术用户一看到 diff(代码差异)就会慌。

### 6. 精简团队的招聘与运营、从印度做全球公司 / Lean Team & Building Globally From India `[24:40–29:04]`
**要点(中文)**: 招聘只看两点:**问题解决能力**与 **ownership**;早期还专挖印度 IT 顶尖排名者(现有 IT rank 1、rank 12 在职),部分初始成员来自 Dunzo。给人极大责任:部署(体量近似 Vercel)两人搞定、记忆一人搞定——人们被难题吸引。团队多在班加罗尔,SF 仅 3–5 人;两兄弟一个常驻 SF、一个两地跑。谈到"为什么印度出不了 Google/Facebook":关键在**从第 0 天就立志做全球一流产品**、敢做大梦;互联网普及后,每个国家都有机会做全球产品。全员每周和客户对话、全员轮客服,创始人上线头五天亲自泡客服台(用 AI 处理法德语工单),从第 0 天建立客户同理心。
> 🗣️ "One is problem solving, like how good are you at problem solving? ... second is ownership." —— Mukund Jha (SPEAKER_03)
> 译:第一是问题解决能力——你解决问题的水平到底如何;第二是 ownership(主人翁式的担当)。
> 🗣️ "everybody talks to a customer once a week, twice a week. Everyone in the entire ... company ... everybody does customer support." —— Mukund Jha (SPEAKER_03)
> 译:公司里每个人每周都要和客户聊一两次,每个人都做客服。
> 🗣️ "why is there no Google or Facebook from India?" —— Mukund Jha (SPEAKER_03)
> 译:为什么印度出不了一个 Google 或 Facebook?

### 7. SaaS 已死?个性化软件的崛起 / Is SaaS Dead? The Rise of Personalized Software `[29:04–34:04]`
**要点(中文)**: SaaS 面临两大逆风:① 越来越多 SaaS 工作流会被 Agent 吞掉,**不转型成"Agent-first"就难存活**;② 用户想要越来越定制化的自建软件(就像他们自己造 Asana)。软件本身正在"Agent 化"——平台上约 20% 已是把 Emergent Agent 嵌进去驱动工作流的 agentic app。对"模型公司自建应用层来抢"的担忧,回应仍是创业基本功:谁最懂用户、离用户最近谁赢。他们判断模型终将商品化,不去正面造"Opus 4.5 替代品",而是**用自定义微调去增强/榨取模型**(不同模型有各自"尖峰":Opus 是主力、Codex 擅后端调试、Gemini 擅前端),并在其上构建"贴近用户"的层。对长任务/多 Agent:METR 的时间-能力曲线是"年度图表",内部在做 agent swarm(overseeing agent 监督、Ralph Wiggum 循环式反复催促),核心仍回到"好的验证回路"。
> 🗣️ "unless your SaaS company pivots into like an agent first company ... that's going to be hard to sort of survive." —— Mukund Jha (SPEAKER_03)
> 译:除非你的 SaaS 公司转型成 Agent 优先的公司,否则会很难生存下去。
> 🗣️ "a lot more software will become agentic in nature." —— Mukund Jha (SPEAKER_03)
> 译:会有多得多的软件,在本质上变成"Agent 化"的。
> 🗣️ "we don't want to like build a Opus 4.5 alternative right away, but we do want to augment it through our custom fine-tune." —— Madhav Jha (SPEAKER_02)
> 译:我们不想现在就去造一个 Opus 4.5 的替代品,但我们确实想用自己的定制微调去增强它。
> 🗣️ "Who understands the customer needs really, really well and ... is able to build for that is going to sort of win the space." —— Mukund Jha (SPEAKER_03)
> 译:谁能真正、真正地理解客户需求并据此去造东西,谁就会赢下这个赛道。

### 8. 未来:小众 app、单人创业者与 AI 赋能 / Niche Apps, Solo Builders and AI Agency `[34:04–39:32]`
**要点(中文)**: 平台已建成 700 万个 app,核心用户是想自动化业务、或想上线业务点子的中小企业主——原本要花 50 万美元请 dev shop,现在自己 5000 美元搞定。经典案例:阿拉斯加一位临床心理学家兼马术教练,把两个领域"联姻"做成 app《Equally Mine》上架,已有数百用户。这不仅是省钱,更是**"表达不再在传译中失真"**——领域专家自己说出口、自己造,比经过开发者转译更好;有 solopreneur 自己就是唯一的"建造者"。主持人升华:这是 PG 那篇文章趋势的延伸——从大公司→创业浪潮→人人经营自己交叉领域的小生意;"在无限软件的世界里,再小众的 app 也能被造出来"。他们要做的是"缩小 idea 与现实之间的鸿沟"。
> 🗣️ "it would have costed you like $500,000 to build the software. Now you can build it for $5,000 completely on your own." —— Mukund Jha (SPEAKER_03)
> 译:过去造这套软件要花你大约 50 万美元,现在你完全靠自己 5000 美元就能造出来。
> 🗣️ "a lot get lost in the translation when you're trying to express your idea to the ... through a developer" —— Madhav Jha (SPEAKER_02)
> 译:当你试图把自己的想法通过开发者去表达时,很多东西会在这层"传译"中丢失。
> 🗣️ "in a world of limited software, that app would never have been built, but in a world of unlimited software, you can build that." —— 主持人 (SPEAKER_04)
> 译:在软件稀缺的世界里,那个 app 永远不会被造出来;但在软件无限的世界里,你能把它造出来。
> 🗣️ "We're getting to the niche of niches." —— Mukund Jha (SPEAKER_03)
> 译:我们正在触达"小众中的小众"。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **先把"自动验证"做成核心资产**:为你的 Agent 建一个能自动判断"任务是否真的完成"的验证回路(自动测试/裁判/CI 校验),这是让 Agent 敢于长时间自主运行、也是最难被模型直接吃掉的壁垒。
- [ ] **构建期与运行/部署期共用同一套 infra**:尽量让 Agent 在开发和上线时面对同一环境,减少"能生成、部署却挂"的最后一公里问题;并把 infra 反馈实时喂回 Agent。
- [ ] **多 Agent + 跨会话记忆/技能库**:主 Agent 驱动、子 Agent 承接委派;把成功轨迹沉淀为经 CI/CD 校验的可复用"技能",让 Agent 跨用户/跨会话越用越强,而不是每次从零。
- [ ] **为你的用户与你的 Agent 同时做同理心设计**:非技术用户面前隐藏 diff/JSON/API key 等吓人细节;设立类似 "agent experience" 的内部指标,持续优化 Agent 的"工作体验"与工具反馈质量。
- [ ] **后发进场就用"碾压式产品 + 分发引擎"**:别指望微弱领先,产品要明显高出一头;同时早期就搭分发(影响者网络/垂直人群 messaging,如"来做真正能上线的 app"),用竞品常见报错做差异化钩子。
- [ ] **不与模型正面竞争,做"增强层"**:利用不同模型的尖峰能力(如后端调试/前端/长任务),用自定义微调 + harness 在模型之上再榨 20–30%,把重心放在"最懂用户、离用户最近"。
- [ ] **用极小团队 + 强 ownership 跑**:招人只认"问题解决 + ownership",给人整块难题;全员每周和客户对话、轮值客服,从第 0 天建立客户同理心(哪怕跨语言/跨时区)。

## 🔑 关键术语 / 概念
- **Verification loop(验证回路)** — 让 Agent 能自动判断任务是否完成、从而长时间自主运行的机制;Emergent 认为"解决验证=能自动化软件工程",是其核心洞见与壁垒。
- **Harness(Agent 外壳/框架)** — 包裹底层模型的编排与约束层;好的 harness 能在模型之上再榨出 20–30% 性能,并随模型变强而"放松控制、给更多自主权"。
- **Agent experience(Agent 体验)** — Mukund 提出的内部指标,类比"用户体验",衡量 Agent 在平台上"干活是否顺手"、拿到的反馈是否够好。
- **Cross-session memory / auto-generated skills(跨会话记忆 / 自动生成技能)** — 把历史轨迹聚合、经 CI/CD 校验后沉淀为可复用技能与长期记忆,实现跨用户、跨会话的持续学习(优于 Agent 现场自己生成技能)。
- **Agent-first / agentic app** — 把 Agent 嵌入产品内部驱动工作流的软件形态;Emergent 上约 20% 已是此类;SaaS 不向此转型将难生存。
- **Ralph Wiggum loop** — 一种"不停催促 Agent'继续、直到完成'"的循环打法,前提是有好的验证反馈判断"活干完没有"。
- **METR 时间-能力曲线** — 衡量模型能自主完成的任务时长在指数增长(讲者称 4.5≈4 小时、4.6≈10 小时),被称为"年度图表",支撑"长任务 + agent swarm"的未来判断。
- **Jevons 悖论(Jevon's paradox)** — 工具越强、需求越膨胀:软件生产越高效,人们想造的东西越多,工程岗位反而增加。

## 🔖 高价值金句时间戳
- `[02:09]` "verification is the loop which sort of keeps agent running for a longer period of time." — 一句话点破 Agent 长任务的命门:先解决"怎么自动判定做对了"。
- `[09:46]` "the last mile that you mentioned is always what people neglect." — 别停在"能跑",最后一公里(部署/安全)才是差异化护城河。
- `[10:20]` "your agent is only as good as the feedback that you provide." — Agent 能力上限=你给它的反馈质量,这也是自建 infra 的根本理由。
- `[15:57]` "the coding aspect is only 20% of the job ... taking an app to production is like really, really hard." — 回应"模型会不会通吃":写代码不是难点,送上生产才是。
- `[26:24]` "why is there no Google or Facebook from India?" — 全球化雄心从第 0 天立起:任何国家都能做全球产品。
- `[29:21]` "unless your SaaS company pivots into like an agent first company ... that's going to be hard to sort of survive." — 对 SaaS 从业者的直接警告:要么 Agent-first,要么被吞。
- `[35:16]` "it would have costed you like $500,000 to build the software. Now you can build it for $5,000 completely on your own." — 用价格塌陷量化"个性化软件"这波解锁的规模。
- `[37:26]` "in a world of limited software, that app would never have been built, but in a world of unlimited software, you can build that." — 无限软件时代,小众中的小众也值得被造。
