# 第 8 章 · AI / Agent 时代专题 / The AI / Agent Era

> 这一章回答一个 AI-Agent 创始人最该问、也最容易想岔的问题:**当模型每两个月变强一次、写代码近乎免费时,一家 Agent 公司到底该建什么、护城河在哪、怎么打**。它把 16 支 YC 视频里反复出现的判断拧成一根绳——从"现在有多早"、到"好的 AI 产品长什么样"、再到"护城河搬到了哪里"和"先把自己公司改造成 AI 原生组织"。如果你正准备做 agent-first 产品,这一章是把 YC 一线共识落到你下一个 commit 的行动清单。

## 核心原则 / Core Principles

### 现在是"电力发明后第六个月"——相信曲线,在能力边缘建造 / We're six months into electricity — build at the edge, believe the curve

几乎每位讲者都在提醒你:**别用今天的能力评判 AI 的机会**。Pedro Franceschi 给团队的比喻是"电力去年 12 月才被发明,那台电力就是 Opus 4.5"——我们只站在电力问世五六个月的时点,蒸汽机还要 20 年才来,大多数人却还在研究"蜡烛能干什么"。落到产品上,Amjad Masad 的建议是"接受你今天做出的是烂产品",因为两个月后模型变强,你的产品会突然可用;所以要把产品做在"当前能力的边缘(edge of what's possible)",赌曲线会来接你。Replit 据此每 6 个月发一个 Agent 版本、既预测也主动拉高"什么是可能的";Bob McGrew 则点出真正的机会:**能力(capabilities)跑得远快于采用(adoption)**,那道越拉越大的鸿沟就是创业空间。常见误区是等模型完美了再做——那时窗口早已关上;Mark Pincus 和 Garry Tan 甚至推算,理想的消费级时刻还差三个数量级、消费级革命约在 2029,所以现在就该用"当推理无限免费时会怎样"去倒推、先把原语造出来。

> 🗣️ "electricity was invented in December, and I think electricity was Opus 4.5." —— Pedro Franceschi / Brex(The Most AI-Pilled CEO）
> 译:电力是在(去年)12 月被发明的,而那台"电力"就是 Opus 4.5。

**🤖 对 AI Agent 创始人**: 把路线图对齐到"能力曲线"而非当下天花板——选一个模型刚够着、甚至还差一点的任务先发布,提前为下一次跃迁(长时自主、并行执行、computer use)改架构;判断标准不是"现在能不能跑",而是"两三个月后的模型会不会把它抬进可用区"。

### 好的 AI 产品就是"agent loop + tools"——放开爪子,别过度工程化 / A good AI product is just an agent loop with tools — free the claw

被反复验证的产品形态出奇地简单。Pedro 的断言是"你用过的每一个好 AI 产品,本质都是一个带工具的 agent 循环,就这么简单";最大的反模式是把 LLM 当"昂贵易碎品",写几十万行代码严控它看到的一切,像"把 agent 关进富士康工厂"——正确做法是"放开爪子(free the claw)",给它 token 和自由。Garry Tan 把这套手艺讲得最透:**harness 要薄、skills 要厚**;markdown 本身就是代码,只是编译方式不同;核心工程手艺是划边界——把"能力、判断、泛化情况"写进交给 LLM 的 markdown skill,把"确定性真实动作"(第三方 API、Twilio 类调用)写进代码;当今 agentic engineering 的绝大多数失败,都是有人把本该放 markdown 的东西硬写成脆弱的代码。Ryan Petersen 补上另一半:对已有强算法(如物流求解器)的领域,**别让 LLM 取代工具,让 LLM 把工具当工具来调用**、并做工具边界之外的事(打电话、发邮件澄清)——于是"agent 就成了那个用户"。而 Francois Chaubard 的递归研究划出一条红线:LLM 单次前向传播有硬天花板,排序、数独、规划这类"不可压缩问题"一次算不完,必须显式拆步或外接确定性工具/求解器。Variance 则示范了最小构件:一个垂直 agent 只要"SOP + 自建工具 + 数据"三块积木,别一上来就造复杂"决策层"。

> 🗣️ "every single good AI product you've used is an agent loop with tools. That's it." —— Pedro Franceschi / Brex（The Most AI-Pilled CEO）
> 译:你用过的每一个好的 AI 产品,本质都是一个"带工具的 agent 循环"。就这么简单。

**🤖 对 AI Agent 创始人**: 别自己造 harness,直接用 Claude Code / OpenClaw 这类现成外壳;把精力花在写 markdown skill、划清"latent space(判断)vs 确定性代码(动作)"的边界上;对需要精确计算的子任务外接工具或专用模型,别指望一次 LLM 调用兜住一切。

### 护城河搬家了——应用软件归零,领域知识、专有数据与上下文才是壁垒 / The moat has moved — app software goes to zero; domain knowledge, proprietary data & context are the wall

当任何人一句 prompt 就能生成任意复杂度的软件,Masad 的预测是"所有**应用**软件价值都会归零"——传统 SaaS 的可替代性会从今天的约 15% 走向 100%(他的 HR 同事三天做出一款可卖数万美元/年的 org chart 软件)。既然代码不再是壁垒,护城河就搬到了别处,而讲者们指向高度一致的几个地方。第一是**领域知识**:Masad 直言"领域知识是打造一家 agent 公司最重要的东西",软件工程 agent、SDR 早已拥挤,要从你自己有热情、有纵深的垂直切入。第二是**专有数据 / 记录系统(system of record)**:Gusto 的护城河是它已掌握的行业与个人数据,Variance 最难的技术活是把散在 5–10 个系统、无 schema、petabyte 级的客户数据接进来(外加那个留给人审的"调查面板")。第三是**上下文集中**:YC 内部把全部数据放进一个 Postgres 库、给 agent 只读 SQL,Garry Tan 强调这比"到处接 MCP"强得多,再叠加自我改进的 skill 就能复利成组织级智能。第四,当写代码变廉价,**taste / 设计 / eval 成了护城河**(Dylan Field:一次性生成不会赢,把生成物打磨成"好"的能力才赢)。反直觉的一点来自 OpenClaw:大厂的护城河在 token 与"数据孤岛",而本地优先 agent 的护城河恰恰是"用户拥有自己的记忆"(一堆存在自己机器上的 markdown)。

> 🗣️ "domain knowledge is the most important thing to build an agent company." —— Amjad Masad / Replit（The Future of Software Creation）
> 译:领域知识是打造一家 Agent 公司最重要的东西。

**🤖 对 AI Agent 创始人**: 假设你的代码一年内会被平台方或竞品复现,先问"我的壁垒是什么"——是别人拿不到的专有数据 / 记录系统、是别人没有的领域 know-how、是集中且自我改进的上下文、还是别人抄不走的 taste?没有其中之一,你多半只是在做一个"feature,不是一家公司"。

### 用"可验证 + 测试 + eval"筑可靠性护城河 / Reliability is the moat: verifiable reward, tests, and evals

为什么 coding agent 突然能打?François Chollet 给的第一性答案是**可验证奖励(verifiable reward)**:代码有单测、编译、报错这样可信的奖励信号,于是能跑 RL 循环、暴力挖掘整个解空间、近乎完全自动化;数学是下一个,而写文章、法律这类不可验证的领域进步会极慢甚至停滞。这直接给你一把筛赛道的尺子:**你的领域输出能否被形式化、可信地验证?** 能就现在能做,不能就得自己造出一个可信奖励函数、或绕开。落到工程上,Garry Tan 的红线是"没测试就把用户丢进去,那就是 slop、比人写的代码还烂 10 倍",目标是 80–90% 覆盖 + 端到端 QA,让机器自己去补测试。Masad 补充:可靠性的上限更多来自"环境反馈 + 快速试错"(可回滚文件系统上 fork 出多个环境并行试解、为每个功能自动生成测试),而不是只靠换更强的模型。Pedro 把它推到组织层面——把公司做成**自学习系统**,让每一次人工介入都变成一个 eval case、每晚自动改 prompt 和代码让评测通过。YC Paper Club 则提醒两个坑:做 self-play / 合成数据极易 reward hacking(只奖励"难倒对手"会生成垃圾题),高风险输出应从 vibe coding 升级到"生成器 + 验证器"的 verified coding(如 Lean)。

> 🗣️ "any problem where the solutions you propose can be formally verified and you can actually trust the reward signal... can be fully automated with current technology, with the LLM-based stack." —— François Chollet（Why Scaling Alone Isn't Enough for AGI）
> 译:任何一个"你提出的解可以被形式化验证、且你能真正信任那个奖励信号"的问题,用现有的 LLM 栈就能被完全自动化。

**🤖 对 AI Agent 创始人**: 先用"可验证奖励"筛你的场景;为核心任务搭一个能自动生成海量试错数据的验证环境(单测 / 仿真 / 规则),把测试当一等公民而非附属;再把"每次人工纠错→自动变成 eval→agent 自我改进"做成闭环——这套自愈能力,才是随时间复利、别人难抄的护城河。

### 切入点:没有在位产品的地方、正在着火的问题、离问题最近的人 / Entry points — no incumbent product, problems on fire, closest to the problem

Bob McGrew 的 FDE(前置部署工程师)手册给出最锋利的切入逻辑:**AI agent 没有既有产品可替代**,产品发现量巨大,而这只能从企业内部做——所以你不是在卖软件安装,而是"卖一个已解决的问题(outcome)",且只该碰客户 CEO 的前五大优先级、带来 3x–10x 阶跃改变的问题。Karine Mellata(Variance)加了两条冷启动铁律:第一个客户先信"创始人"而非产品,且问题空间必须"正在着火(on fire)",否则没人愿赌一个没有背书的小 startup(她的首单花了 8 个月)。Ryan Petersen 给了反向的排除法——先掂量在位者的三大优势(数据、领域 know-how、分发),"有些问题小到不该开公司,它只是一个 feature";但传统、重线下、强监管的行业里,"因太贵而本来不做"的工作才是最大增量。Masad 则把 ICP 从"会写代码的人"重新定义为"**离问题最近、有创始人心态**"的技术相邻者(PM、设计师、领域专家),并劝你避开 SWE agent、SDR 红海。Eddie Kim(Gusto)提供了消费/SMB 侧的落地术:别给用户"空白画布",从他们**已经在做的重复任务**("工作前的工作")反向引导,对小企业主几乎是"hard yes"。而 Mark Pincus 的逆向信号——"消费级现在不可投,正因如此你才该做它"——提醒你别把投资人的"去做 enterprise"当第一性原理。

> 🗣️ "With AI agents, there is no incumbent product... there's so much product discovery to do. And you can only do it from inside the enterprise." —— Bob McGrew（The FDE Playbook for AI Startups）
> 译:对 AI agent 来说,没有既有产品可替代……要做的产品发现太多了,而这只能从企业内部去做。

**🤖 对 AI Agent 创始人**: 选一个"没有在位产品、正在着火、且你有领域纵深"的窄切口;用 FDE/高触达从企业内部做产品发现,按 outcome 定价、先卖创始人、接受首单以月计;若做消费/SMB,就消灭空白画布——从用户每周都在手动做、明知浪费时间的那件事开始自动化。

### 先把自己的公司改造成 AI 原生组织——"为什么不能只有我一个人?" / Rebuild your own company AI-native first — "why can't it just be me?"

一个反复出现的主张:**做 AI Agent 创业,第一个要被 agent 重造的公司是你自己的**。YC 内部手册把方法论讲透——别把 AI 当 co-pilot,要当"一切工作的构建层":把上下文收拢到一处、建一个 DRY + MECE 的工具/skill 注册表(从 20 个长到 350+)、把真实使用的转录稿喂回去让 skill 自我改进,于是"两句话简介 skill 比我们任何单个人都强"。Garry Tan 称这是"**一次性的时间穿越**",敢每年在 token 上花 1–10 万美金 + 建 skill,你就能一次越过所有 Fortune 500 和现存创业公司。Pedro 把它落到 CEO 身上:CEO 必须是首席 AI 官,且开公司的前提应该是"**为什么不能只有我一个人**"——当公司边界变成类型系统、接口变成 agent 对 agent,token 消耗自然更高。Tan 在 Tokenmaxxing 里给出硬证据:13 年没写代码的他用 Claude Code / OpenClaw 做到"400x"产出,靠的是"token max(该花就花,一天 $500 也值)+ boil the ocean + thin harness fat skills",本质是"借用机器的时间"。组织形态也随之变:Masad 说未来公司只剩"建造者 + 销售者"两类岗位、人人都是创始人;Ryan Petersen 用黑客松 + vibe coding 训练营让最懂业务的一线专家自己自动化自己的岗位;Eddie Kim 的团队用"5 人 × 10 周 × 无会议无文档无 Jira,只留一个常开 Zoom + 海量 Claude Code token"跑完了一场公司级发布;YC Paper Club 则把 agentic 开发类比成打即时战略(RTS)——orchestrator 编排几十个 worker、永远别让 token 闲置。

> 🗣️ "there's a one-time time warp where you can leapfrog every incumbent all fortune 500s all startups that exist by doing this." —— Garry Tan（Inside YC's AI Playbook）
> 译:这是一次性的时间穿越——靠这么做,你可以一次越过所有在位者、所有 Fortune 500、所有现存创业公司。

**🤖 对 AI Agent 创始人**: 把"用 agent 重造自己"当作产品直觉的来源和最快的护城河积累——度量并逼近你的 token 消耗极限、把上下文集中到一处、建自我改进的 skill 注册表、以 RTS 方式并行开发;以"为什么不能只有我一个人"为组织默认,你造出的产品会天然长在这套 AI 原生肌理上。

### 执行力已外包给模型,人供给"选择的智慧"、品味与分布外信号 / Execution is outsourced — humans supply the wisdom to choose, taste, and out-of-distribution signal

模型接管了执行,那人还剩什么?Pedro 的回答最凝练:"**执行力出局了,模型会做得更好;稀缺的是选择的智慧(the wisdom to choose)**",而判断该把时间花在哪的好指标,就是"有哪些事只有你能做、模型做不了"。他点出模型最大的盲区:你无从知道模型对你所问的确切问题见过多少训练数据,而客户永远不会把答案塑造成你能直接喂给 LLM 的 prompt——**那些"没说出口的信号"就在分布之外,必须由创始人亲手去和客户聊出来**。Garry Tan 同样强调 GStack 高度依赖 `ask_user_question`:agency、品味、产品判断仍必须由人供给。品味这条线在设计侧被讲得最重:AI 只是"抬高地板",替代不了 craft 和 taste,省下的时间不该用来多发几个"7 分货"(Katie Dill / Stripe),而 Dylan Field 直言当开发变便宜、one-shot 不会赢,把生成物打磨成"好"的能力才是差异化。OpenClaw 的 Peter Steinberger 从另一面印证:别让默认模板输出像"白面包"一样无聊,给 agent 写一个 soul.md、把交互从"敲命令"变成"跟朋友聊天"——人格与体验本身就是护城河的一部分。McGrew 收束了这层意义:AI 不会自己被采用,"需要人的巧思、探索和大量吃苦"才能让它落地。

> 🗣️ "The execution is out, right? The execution is gone and the model is going to do that better. The wisdom to choose is still, I think the, the missing bottleneck." —— Pedro Franceschi / Brex（The Most AI-Pilled CEO）
> 译:执行力已经出局了,对吧?执行这件事没了、模型会做得更好。而"选择的智慧"依然是那个缺失的瓶颈。

**🤖 对 AI Agent 创始人**: 把你稀缺的时间压在"只有你能做"的事上——去和真实客户对话、捕捉训练数据里没有的需求信号,做产品判断,守 taste 底线;给你的 agent 一个 soul、把交互做得像"聪明的同事/朋友";坚决不把 AI slop 丢给用户,因为"通往平庸的引力"每天都在拉你说"够好了"。

## ⚡ 本章行动清单 / Action Checklist

- [ ] 用"电力才六个月"心态排路线图:选一个当前模型刚够着的任务先发布,提前为下一次能力跃迁(长时自主、并行、computer use)改架构,别等模型完美。
- [ ] 产品就用 **agent loop + tools**,别写几十万行 harness;把能力/判断/泛化写进 markdown skill、把确定性动作(API、求解器)写进代码,给需要精确计算的子任务外接工具。
- [ ] 选一个你有领域纵深 + 有专有数据/记录系统的**垂直**切入(避开 SWE agent、SDR 红海),把 know-how 灌进一个专精 agent——护城河是数据与领域,不是代码。
- [ ] 用**可验证奖励**筛赛道:输出能被形式化、可信验证的领域现在就能自动化;搭验证环境 + 80–90% 测试覆盖 + 端到端 QA,把每次人工介入变成一个 eval case。
- [ ] 冷启动锁定一个"**没有在位产品、正在着火**"的问题 + 一个愿赌你的旗舰客户;按 outcome 定价、先卖创始人、接受首单以月计;做消费/SMB 就从用户"已经在做的事"引导,消灭空白画布。
- [ ] 先把自己公司改造成 **AI 原生组织**:上下文收拢到一处,建 DRY+MECE 的 skill/工具注册表,度量并逼近 token 消耗极限,以"为什么不能只有我一个人"为默认。
- [ ] 把 agentic 开发当 **RTS** 打:orchestrator + 多 worker 并行、先开 PR 再讨论、永远别让 token 闲置,同时保留全量人工验收。
- [ ] 守住只有你能供给的东西:去和客户聊出"没说出口的信号",做产品判断与 taste,给 agent 写 soul,坚决不发 slop。

## 📚 本章取材视频 / Sources

- [The Most AI-Pilled CEO We Know](https://www.youtube.com/watch?v=mPAHvz8kW24) — Brex CEO Pedro 的"电力类比""放开爪子(agent loop + tools)""执行力外包、选择的智慧稀缺""CEO 即首席 AI 官""为什么不能只有我一个人",是本章多条主线的骨架 (`notes/mPAHvz8kW24.md`)
- [The Future of Software Creation with Replit CEO Amjad Masad](https://www.youtube.com/watch?v=lWmDiDGsLK4) — "应用软件价值归零""领域知识是 agent 公司最重要的东西""相信曲线、先做烂产品""habitat/自主性等级",贡献了护城河与切入点判断 (`notes/lWmDiDGsLK4.md`)
- [Replit's CEO On The Only Two Jobs Left In The Company Of The Future](https://www.youtube.com/watch?v=kMYeTRqzAfc) — ICP 重定义为"离问题最近的人"、路线图对齐能力跃迁、未来公司=建造者+销售者,补强切入点与组织形态 (`notes/kMYeTRqzAfc.md`)
- [Inside YC's AI Playbook](https://www.youtube.com/watch?v=B246K_G7mHU) — 上下文集中、工具/skill 注册表、自我改进复利成组织级智能、"一次性时间穿越",是"先改造自己公司"一节的核心蓝图 (`notes/B246K_G7mHU.md`)
- [Tokenmaxxing: How Top Builders Use AI To Do The Work Of 400 Engineers](https://www.youtube.com/watch?v=57lDpTwiW6g) — token max、thin harness/fat skills、markdown 即代码、测试即护城河、借用机器的时间,支撑第 2、4、6 节 (`notes/57lDpTwiW6g.md`)
- [The FDE Playbook for AI Startups with Bob McGrew](https://www.youtube.com/watch?v=Zyw-YA0k3xo) — "AI agent 没有在位产品""卖 outcome""能力—采用鸿沟""AI 需要人去推动采用",是切入点与人机角色两节的主来源 (`notes/Zyw-YA0k3xo.md`)
- [AI Is Eating Logistics](https://www.youtube.com/watch?v=KTmxaMdUbHA) — "LLM 编排工具而非取代工具""agent 即用户""feature 不是公司""在位者三大优势""因太贵而本来不做的工作",贡献产品形态与切入点 (`notes/KTmxaMdUbHA.md`)
- [This Startup Catches Fraud at Scale](https://www.youtube.com/watch?v=JF6XIixstmQ) — 垂直 agent 三块积木(SOP+工具+数据)、不做 100% 决策层、数据接入是最难技术活、"问题必须着火/先卖创始人",落地了切入点与产品形态 (`notes/JF6XIixstmQ.md`)
- [Solving the Blank Canvas Problem: Gusto's AI Co-Founder](https://www.youtube.com/watch?v=xpeRVyFFy_Q) — "空白画布问题""从已在做的事引导""工作前的工作""记录系统即护城河""5 人 10 周无 Jira",供 SMB 切入与组织打法 (`notes/xpeRVyFFy_Q.md`)
- [Zynga Founder: Consumer Is Not Investible Right Now](https://www.youtube.com/watch?v=oHwUD9b9_pg) — "消费级不可投=正该做它""常在的 AI 同事是百亿级机会""2029 消费革命/live in the future""别写调用 LLM 的代码、写教 LLM 写代码的 markdown" (`notes/oHwUD9b9_pg.md`)
- [François Chollet: Why Scaling Alone Isn't Enough for AGI](https://www.youtube.com/watch?v=k2ZLQC8P7dc) — "可验证奖励是 coding agent 爆发根因""不可验证领域会停滞""押能 scale、把人移出改进回路的方法",是可靠性护城河一节的第一性依据 (`notes/k2ZLQC8P7dc.md`)
- [OpenClaw Creator: Why 80% Of Apps Will Disappear](https://www.youtube.com/watch?v=4uzGDAoNOZc) — "本地优先/用户拥有记忆是护城河""80% 只管数据的 App 会消失""给 agent 灵魂 soul.md""像跟朋友聊天而非敲命令",补强护城河与人机体验 (`notes/4uzGDAoNOZc.md`)
- [Recursion Is The Next Scaling Law In AI](https://www.youtube.com/watch?v=DGtUUMNYLcc) — "LLM 单次前向传播有硬天花板""不可压缩问题需真实多步计算/外接工具""7M 递归模型打赢万亿参数",支撑产品形态的技术红线 (`notes/DGtUUMNYLcc.md`)
- [Self-Play for LLMs, AI for Biology, Formal Verification | YC Paper Club](https://www.youtube.com/watch?v=3rWSvrFahIY) — "生成器+验证器/verified coding""self-play 的 reward hacking 与 plateau""agentic coding = 打 RTS/别让 token 闲置",服务可靠性与组织打法 (`notes/3rWSvrFahIY.md`)
- [Dylan Field: Scaling Figma and the Future of Design](https://www.youtube.com/watch?v=-7Qz7tSTfUU) — "写代码变便宜后 taste/设计/eval 才是护城河""one-shot 不会赢""我们仍在 AI 的 MS-DOS 时代""让设计师参与写 eval",贡献护城河与人机角色 (`notes/-7Qz7tSTfUU.md`)
- [How Stripe Built Their New Website](https://www.youtube.com/watch?v=ypzNhwpmOD4) — "AI 只抬高地板、替代不了 craft/taste""对抗通往平庸的引力、别发 slop""你的 agent 体验有多好",落到"人供给品味"一节 (`notes/ypzNhwpmOD4.md`)
