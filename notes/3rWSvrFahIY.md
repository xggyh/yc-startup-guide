# LLM 自博弈、AI×生物、形式化验证与「用 Agent 写代码=打即时战略」 / Self-Play for LLMs, AI for Biology, Formal Verification, and More

> **来源**: [Self-Play for LLMs, AI for Biology, Formal Verification, and More | YC Paper Club](https://www.youtube.com/watch?v=3rWSvrFahIY) · Y Combinator · 2026-06-12 · 时长 76:55
> **讲者**: 主持/组织者 Francois Chaubard(SPEAKER_01);五位报告人 —— Yasa Baig(蛋白质生物学,SPEAKER_03)、Luke Bailey(LLM 自博弈,Tatsu 实验室,SPEAKER_02)、Arnab Maiti(Stream RAG,Giga 研究员,SPEAKER_04)、Robert George(Lean 形式化验证,Caltech,SPEAKER_05)、Lukens Orthwein(创始人 AI 工程实践,Channel AI CEO,SPEAKER_00)
> **一句话定位**: YC Paper Club 的 5 篇论文速览,横跨「蛋白质世界模型 / LLM 自博弈 / 语音 Agent 的流式 RAG / Lean 形式化验证 / 用 Agent 写代码像打 RTS」;对 AI Agent 创始人最硬核的是最后一段把 agentic coding 当即时战略游戏来并行化的一整套工程方法论,以及贯穿全场的「生成器 + 验证器 / 奖励设计陷阱 / 语音延迟即产品」等落地心法。

## 🎯 TL;DR(中文核心要点)
- **把 agentic coding 当 RTS 游戏打**:不再是「下棋」(线性、单线程、想清楚再动),而是「即时战略」——把 worktree + 任务管理 + tmux + 一个 orchestrator agent 编排成同时跑几十个 worker,永远别让 token/agent 闲着,靠高可见性快速纠偏。
- **对 worker「低估其时间、高估你的时间」**:让每个 agent 尽量往前冲、一路做到 PR,即使会错、需要后修,也比它频繁停下来问你更划算;能开就开 `--dangerously-skip-permissions`,权限确认会把吞吐拖垮。
- **文档 > 代码,作为 agent 的事实来源**:代码对 agent 是「昂贵的上下文来源」;趁上下文还在内存里,主动写结构化、互链的 wiki 式知识库(含业务知识),把 agent 已知的坏习惯(比如极度不会估工时)固化进 CLAUDE.md 与知识图谱。
- **自博弈(self-play)不是免费午餐**:只奖励「难倒 solver」会让出题者生成「人为复杂、乱七八糟」的垃圾题;自博弈和普通 RL 一样会 plateau。修复靠 grounding(把生成题锚定在真实未解题集)+ 加一个「guide」裁判角色打相关性/简洁性分。→ 生产上做 RL/合成数据要极其小心 reward hacking。
- **语音 Agent:延迟就是产品**:RAG 能治幻觉但会加延迟,10 秒才回话就不自然;Stream RAG 的思路是「用户还在说话时就并行跑检索」,学一个触发策略判断哪段 chunk 带来关键新信息才发查询。
- **需要保证的代码,从 vibe coding 转向 verified coding**:Lean 这类定理证明器骗不了内核,证明 100% 显式可查;把「生成器 + 形式化验证器」配对,用于高风险的代码/数学/科学输出。
- **Bitter Lesson 在跨领域复现**:蛋白质语言模型(ESM-C)照搬 LLM 配方就能跑出干净的 log-linear scaling law,单序列模型无需手工特征即可逼近甚至在抗体设计上超过 AlphaFold3;解药是「加数据」而非「加归纳偏置」。
- **量化你的产出并把方法论团队化**:用 tool calls/分钟当 APM 指标衡量 agent 生产力;Channel AI 靠 LLM 把人均 PR 提到 3.5×,再把这套 RTS 方法论全团队铺开后又涨了 60%。

## 🧭 适合谁 / 什么时候看
- 正在或准备用 Claude Code / Codex 大规模并行开发的 AI Agent 创始人/技术负责人——直接抄「Founder AI Hacks」那段的工程实践。
- 做语音 / 实时对话 Agent、被延迟与幻觉两头夹的团队(看 Stream RAG 段)。
- 在产品里用 RL / 合成数据 / self-play 的人,想先避开 reward hacking 与 plateau 的坑。
- 需要「可验证输出」(代码、数学、金融、科研)的团队,想了解 Lean / 形式化验证与「生成器+验证器」范式。
- 对 scaling law、bitter lesson 心智模型如何跨到新数据丰富领域(如生物)感兴趣的研究型创始人。

## 📝 分段精读

### 1. 开场:intelligence per sample 与 intelligence per watt / Introduction by Francois Chaubard `[00:08–05:47]`
**要点(中文)**: Francois 认为当下 AI 只剩两个真正难题——「每样本智能(intelligence per sample)」和「每瓦特智能(intelligence per watt)」。他质疑「只在人类生成的解空间子集 H 上训练 + 测试时算力/递归自我改进」能否触达完整解空间 F:除非有无限算力,否则你不可能采样到 F 减 H。他押注 AlphaZero 式、不被人类经验带偏的自博弈才是通向更强智能的路。他还举例:ICL 随样本增多并非单调变好(先起伏、撞到上下文长度就断崖),低秩 LoRA 在小样本时表现意外地好——而人类却是同一套算法却单调进步,说明一定存在「每样本智能」高得多的学习程序。
> 🗣️ "the two major problems left, in my opinion, are intelligence per sample, intelligence per watt" —— Francois Chaubard `[02:36]`
> 译:在我看来,剩下的两个主要问题是「每样本智能」和「每瓦特智能」。
> 🗣️ "AlphaZero unbiased by humans meandering is the way we'll get to much more intelligent systems, maybe even dare say AGI" —— Francois Chaubard `[01:53]`
> 译:不被人类的迂回带偏的 AlphaZero,才是我们通往更强智能系统、甚至敢说 AGI 的路。

### 2. Bitter Lesson 来自生物学:蛋白质世界模型 / Yasa Baig: A World Model of Protein Biology `[05:47–25:38]`
**要点(中文)**: ESM-C(Cambrian)把蛋白质当「20 字母语言」,用掩码语言模型在数十亿条进化序列上训练,只喂序列、不喂任何结构标签。结论:LLM 的 scaling law 在蛋白质上干净复现(log-linear,能从小算力外推到大模型);上一代 ESM2 的 plateau 靠的是**纯数据扩展**(样本 5000 万→28 亿,主要来自宏基因组)而非架构技巧。单序列 ESMFold(不用手工构建的 MSA 特征)逼近 AlphaFold3,甚至在抗体设计任务上略胜——正是 bitter lesson 说的「通用表示终将击败手工特征」。SAE 还能从蛋白质模型里无监督拆出可解释、分层的生物学特征。对 ML 创始人的钩子:生物是绝佳的 ML 战场,因为模型还很年轻、数据在超指数增长(人类目前只采样了不到 1% 的蛋白质多样性)。
> 🗣️ "evolution has been generating this training data for 4 billion years and not humans like the past 30 or so" —— Yasa Baig `[15:14]`
> 译:进化已经生成了 40 亿年的训练数据,而不是人类过去这 30 来年。
> 🗣️ "Biology is a great place to work in ML cause the models are still really young" —— Yasa Baig `[23:50]`
> 译:生物是做 ML 的好地方,因为这些模型都还非常年轻。

### 3. 自博弈的 plateau 与自引导修复 / Luke Bailey: Scaling Self-Play with Self-Guidance `[25:38–37:51]`
**要点(中文)**: 现在的后训练已把和预训练相当甚至更多的算力砸在长 RL 上,而「多收集 RL 任务就稳定变好」(Cursor Composer 的曲线)受限于任务要手工收集。自博弈让模型同时扮演「出题者(conjecturer)」和「解题者(solver)」并都训练。理论上「没有东西约束学习」,但实践中 vanilla 自博弈会 plateau,和普通 RL 一样。诊断:只用「难倒 solver」当奖励,最省事的做法就是生成人为复杂、混乱、不优雅的垃圾题(等价于给你一道三页高中微积分题让你算错)。修复方案 SGS(self-guided self-play):把生成题**锚定**在一批真实未解题上,并引入第三个「guide」角色给「相关且不过度复杂」打分。结果:7B 模型花 8× 算力做自博弈,达到 670B 大模型的 pass@4 水平——但远未到 100%,自博弈远没被解决。
> 🗣️ "in principle, nothing bounds learning" —— Luke Bailey `[30:19]`
> 译:原则上,没有任何东西约束学习(的上限)。
> 🗣️ "if I run self-play for a long time, it plateaus, i.e. the model stops improving at some point, which is the exact same thing that happens when you run RL" —— Luke Bailey `[31:22]`
> 译:如果我把自博弈跑很久,它会 plateau——模型到某个点就不再进步,这和你跑普通 RL 发生的事一模一样。
> 🗣️ "the easiest way to produce tricky problems is produce these basically messy, artificially complex, and inelegant problems" —— Luke Bailey `[34:11]`
> 译:生成「难题」最省事的办法,就是造出这些混乱、人为复杂、不优雅的题目。

### 4. 语音 Agent 的流式 RAG:边说边检索 / Arnab Maiti: Stream RAG `[37:51–47:40]`
**要点(中文)**: 语音 Agent 需要 RAG 来压幻觉,但 RAG 会引入延迟——回一句话等 10 秒完全不自然;而且语音里幻觉更危险,因为人边听边很难当场抓错。Stream RAG 的核心 trick:**不等用户说完**,在用户还在说话时就解析已出现的词、并行地跑检索,判断哪一段 chunk 带来关键新信息才真正发起查询。论文给了两条路:(1)固定区间流式 RAG,分块跑「便宜的检索组件」,比较「中间 query」与「完整 query」的 top 文档是否吻合来决定何时定稿;(2)微调一个模型自主触发检索,只在 chunk 含关键新信息时才生成新 query。结果(一年前的论文、小开源模型):延迟在合成集降约 0.5s、真人语音降约 1.5s,准确率持平。作者的元观点:这里全是小而未解、且贴近生产的问题,啃下小问题就能在生产上带来巨大收益。
> 🗣️ "The issue is that RAG would add a lot of latency" —— Arnab Maiti `[40:26]`
> 译:问题在于,RAG 会带来很大的延迟。
> 🗣️ "start analyzing the words that are being spoken by the user, and somehow figure out a way to run the RAG system while the question is being spoken" —— Arnab Maiti `[41:09]`
> 译:开始分析用户正在说出的词,并想办法在问题还在被说出的同时就把 RAG 系统跑起来。
> 🗣️ "if you can crack the small problems it can lead to huge gains in the production" —— Arnab Maiti `[47:07]`
> 译:如果你能攻克这些小问题,它能在生产中带来巨大的收益。

### 5. 可验证智能:Lean 与形式化验证 / Robert George: Lean for Science `[47:40–58:52]`
**要点(中文)**: Robert 把当下称为「可验证智能(verified intelligence)」时代。Lean 既是定理证明器也是函数式编程语言:你骗不了它的内核,证明必须 100% 显式、可自动检查。这两年势能爆发——IMO 金牌、Erdős 未解问题、mathlib 库(逾百万行高质量数学)。给创始人的落点:vibe coding 很爽,但如果你要的是「有保证的代码」,就该从 vibe coding 转向 verified coding——写下 spec、证明代码满足它。他展示的 TorchLean 是首个在 Lean 里原生写神经网络的框架:能在 spec 层证明「flash attention = 标准 attention」、attention 的置换不变性、certified robustness,甚至把「temperature=0 仍非确定性」这一现象一路形式化到 GPU kernel 级别。程序验证在 LLM 生成代码规模化后是个万亿级相邻机会。
> 🗣️ "you cannot fool this theorem prover" —— Robert George `[49:39]`
> 译:你没法糊弄这个定理证明器。
> 🗣️ "vibe coding is all of a sudden really great ... but i want code that needs guarantees" —— Robert George `[54:41]`
> 译:vibe coding 突然间变得很好用……但我要的是需要保证的代码。

### 6. 创始人 AI 工程实践:写代码现在是即时战略游戏 / Lukens Orthwein: Founder AI Hacks — Programming is an RTS Game Now `[58:52–76:07]`
**要点(中文)**: 这是全场对 Agent 创始人最实操的一段。核心比喻:agentic coding 已不是「下棋」(线性、单线程、想清楚再落子),而是「即时战略(RTS)」——你要同时经营「经济(token)」、「生产(spawn worker)」和「作战(纠偏)」,把注意力和系统吞吐都最大化并行。他的一整套打法:
- **基础设施**:git worktree + 任务管理软件 + tmux 让工作可移植(卡住/要回家就换台机器/换人接手)+ 一个由 Claude 跑的 orchestrator agent 去 spawn 大量 worker;从「有个想法」到「开工」的击键数压到最低,细节后面再纠。
- **worker 策略**:对它们「低估其时间、高估你的时间」——让它们尽量往前冲、一路做到 PR + 一份好总结;允许它们做假设而非卡住等你;前端 worker 预先起好 dev server,人类只需开个浏览器 tab 就能测。
- **默认 `--dangerously-skip-permissions`**(或搭沙箱),否则频繁给反馈会极慢。
- **把已知的 agent 坏习惯固化进去**:比如 agent 极不会估工时(会说「两周一个工程师」,实际一条 prompt、20 分钟搞定),就写进 CLAUDE.md 和更大范围的知识图谱,让它「永远别在这些方面相信自己」。
- **文档优先于代码**:代码是「昂贵的事实来源」;趁上下文在内存里,主动写结构化、互链的 wiki 式知识库(连业务知识一起),既喂未来的 agent、又提升人类可审计性。
- **原则**:「默认宏观、关键处才微观(macro by default, micro when it counts)」、satisficing(够好而非完美)、混搭不同大小的 ticket、人人全栈、永远别让 token 闲置、靠高可见性早发现早纠偏。
- **像玩 RTS 一样监控**:小地图/状态追踪 + 音频提示——他把每个 agent 会话映射成魔兽/星际的兵种音效、按 ticket 类型配色主题,一听就知道哪个要注意;还做了个 APM 追踪器,用 **tool calls/分钟** 而非点击数衡量 agent 生产力。
- **战绩**:LLM 让人均 PR 达到 3.5×;上个月把这套 RTS 方法论全团队铺开后,人均 PR 又涨了 60%。
> 🗣️ "using agentic systems feels exactly like playing real-time strategy games" —— Lukens Orthwein `[60:35]`
> 译:使用 agentic 系统,感觉就跟玩即时战略游戏一模一样。
> 🗣️ "put like a really low premium on their time and effort and a high premium on yours" —— Lukens Orthwein `[63:09]`
> 译:把它们(worker)的时间与精力估得很低,把你自己的估得很高。
> 🗣️ "the code is often like a really expensive source of truth for the agents to pull context out of" —— Lukens Orthwein `[67:16]`
> 译:代码对 agent 来说,往往是一种非常昂贵的、用来抽取上下文的事实来源。

## 🚀 给 AI Agent 创始人的行动项
- [ ] 搭一套「orchestrator + 多 worker」的 agentic 开发流水线:git worktree + 任务管理 + tmux 可移植 + 一个 Claude/Codex 编排器,目标是从想法到开工的击键数最小化,并默认开启 `--dangerously-skip-permissions` 或沙箱。
- [ ] 给每个 worker 定死「尽量做到 PR + 总结、允许做假设、别频繁停下来问」的指令,并把已知坏习惯(工时估计、易错点)写进 CLAUDE.md 与互链知识库。
- [ ] 建一个 wiki 式知识库(含业务知识)作为 agent 的首选事实来源,把代码降级为「昂贵来源」;每个 worker 完成后把学到的东西回灌知识库。
- [ ] 给自己/团队做一个 agent 生产力仪表盘:用 tool calls/分钟(而非点击)当 APM 指标,配音频/颜色提示做多 agent 状态感知,量化「是否真的把并行度打满」。
- [ ] 做语音/实时 Agent 就把「延迟」当第一产品指标:实现「用户还在说时并行跑检索」,并学一个触发策略,只在 chunk 含关键新信息时才发查询。
- [ ] 凡是在产品里用 RL / 合成数据 / self-play,先设计防 reward hacking 的机制:给生成任务加 grounding(锚定真实目标分布)+ 一个 judge/guide 模型打相关性与简洁性分。
- [ ] 对高风险输出(代码/数学/金融/科研)引入「生成器 + 验证器」范式,评估用 spec + 形式化验证(如 Lean)把「vibe coding」升级为「verified coding」。

## 🔑 关键术语 / 概念
- **Intelligence per sample / per watt** — 「每样本智能 / 每瓦特智能」;Francois 认为这是当下 AI 剩下的两大难题:用更少样本学到更多、用更少能耗算得更聪明。
- **Bitter Lesson(苦涩的教训)** — Sutton 的论断:靠扩展算力与数据的通用方法,长期会击败手工注入人类领域知识的方法;本场论证它正在蛋白质生物学里复现。
- **Self-play(自博弈)/ conjecturer–solver–guide** — 模型同时出题(conjecturer)与解题(solver);SGS 再加一个 guide 裁判角色评判生成题是否相关且不过度复杂,以防「奖励只看难度」导致的垃圾题。
- **Reward hacking(奖励作弊)** — 优化奖励代理指标而非真实目标;本场例子是只奖励「难倒 solver」→ 模型生成人为复杂、无用的题。
- **Stream RAG(流式检索增强)** — 在用户还在说话时就并行触发检索、判断何时发起查询,以在语音场景兼顾低延迟与低幻觉。
- **MSA / AlphaFold vs 单序列 ESMFold** — MSA 是 AlphaFold 依赖的手工多序列比对特征;单序列蛋白质语言模型无需 MSA 即逼近/超越,是 bitter lesson 的实证。
- **Lean / mathlib / TorchLean** — Lean:骗不了内核的定理证明器兼函数式语言;mathlib:百万行形式化数学库;TorchLean:在 Lean 里原生写并验证神经网络的框架。
- **Verified / verifiable coding** — 「验证式编码」:写下 spec 并证明代码满足它,与「vibe coding」相对,用于需要保证的代码。
- **APM(tool calls/分钟)** — 借用 RTS 的「每分钟操作数」,这里用 agent 的工具调用频率衡量并行生产力。
- **Satisficing(满意即止)** — 经济学术语,追求「够好」而非「完美」,是 agentic 高吞吐开发的核心原则之一。

## 🔖 高价值金句时间戳
- `[02:36]` "the two major problems left, in my opinion, are intelligence per sample, intelligence per watt" — 用「每样本/每瓦特智能」两把尺子给整个 AI 议题定坐标。
- `[34:11]` "the easiest way to produce tricky problems is produce these basically messy, artificially complex, and inelegant problems" — 奖励设计一旦只盯「难度」,模型就用垃圾复杂度作弊,做 RL 必记。
- `[40:26]` "The issue is that RAG would add a lot of latency" — 语音 Agent 的第一性矛盾:要接地(RAG)就得付延迟,延迟就是产品。
- `[54:41]` "vibe coding is all of a sudden really great ... but i want code that needs guarantees" — 从 vibe coding 到 verified coding 的分水岭,高风险场景的护城河。
- `[60:35]` "using agentic systems feels exactly like playing real-time strategy games" — 全场最出圈的心智模型:写代码从「下棋」变成「打 RTS」。
- `[73:44]` "You should never have your cloud tokens like sitting unused. That's really inefficient economy." — 把 token 当 RTS 的经济资源,闲置=低效,时刻满负荷并行。
