# AI 到底有多聪明?用 ARC-AGI 重新定义"智能" / How Intelligent Is AI, Really?

> **来源**: [How Intelligent Is AI, Really?](https://www.youtube.com/watch?v=pBlIgs6w7Ss) · Y Combinator · 2025-12-17 · 时长 11:59
> **讲者**: 主持 Diana Hu(YC, SPEAKER_00);嘉宾 Greg Kamradt(ARC Prize Foundation 主席 / President, SPEAKER_01)。录制于 NeurIPS 2025(San Diego)。
> **一句话定位**: 用 ARC-AGI 重新定义"智能 = 高效学习新事物的能力",提醒 AI Agent 创始人别追刷榜式的虚荣指标,要投资真正会泛化、可交互、样本与能耗高效的系统。

## 🎯 TL;DR(中文核心要点)
- **智能的定义换了**:不是"能考多高分",而是 François Chollet 的定义——**高效学会新技能的能力**。棋、围棋、自动驾驶都能超人,但让同一系统换个新技能才是难点。
- **ARC 的核心是"普通人能做、模型做不到"**:所有基准都用普通人(会计、Uber 司机)实测过可解性,与"越出越难的 PhD++ 题"路线相反;做不到就说明还缺关键能力。
- **ARC 曾是 LLM 的照妖镜**:2024 年 GPT-4 基座(无推理)只有约 4–5%,o1-preview 一出直接跳到 ~21%。ARC 因此**识别出"推理范式"是转折性突破**。
- **警惕虚荣指标(vanity metrics)**:大厂(OpenAI / xAI Grok4 / Gemini 3 / Anthropic Opus 4.5)都在用 ARC 报成绩,但"被采用"不等于任务完成;刷到一个数字 ≠ 真进展。
- **RL 环境是"打地鼠"**:能造 RL 环境就能刷分,但你**不可能给未来要做的每件事都造一个环境**;人类学新东西并不需要专门环境。要投资**不依赖环境也能泛化**的系统。
- **未来 AGI 是交互式的**:ARC-AGI v3(2026)是 ~150 个不给任何文字/符号说明的游戏环境,靠"行动→反馈"自己摸索目标——这正是现实(和 Agent)的运作方式。
- **超越准确率**:墙钟时间可以靠堆算力压缩、意义不大;真正该测的是**所需训练数据量**和**执行所需能量**,并按"人类完成所需动作数"归一化 AI 表现。
- **解出 ARC 是 AGI 的必要非充分条件**:解出 v1/v2 不是 AGI,但会是"泛化能力"最权威的证据。

## 🧭 适合谁 / 什么时候看
- 正在做 **AI Agent / 需要评测(eval)体系**的创始人:想搞清"我到底该测什么、别被刷榜骗了"。
- 对 **泛化 vs. 拟合、RL 环境边界、样本/能耗效率**有判断需求的技术创始人与研究型团队。
- 在给投资人/客户展示"我们过了 XX 基准"之前,想先自查是不是**假阳性进展**的人。
- 12 分钟短片,适合快速建立"如何评估模型真实能力"的心智框架。

## 📝 分段精读

### 1. ARC Prize 是什么 & 重新定义"智能" / What ARC Prize Is and Chollet's Definition of Intelligence `[00:11–01:48]`
**要点(中文)**: ARC Prize 是一家"技术前倾"的非营利,使命是**推动通向"能像人一样泛化的系统"的开放进展**。其智能观来自 Chollet 2019 年论文《On the Measure of Intelligence》:智能不是 SAT 分数或做多难的数学题,而是**学会新事物的能力**。AI 在棋、围棋、自动驾驶上早已超人,但让同一系统迁移到新技能才是真正的硬骨头。Chollet 同时给出了可被人和机器共同参加的测试(ARC),并刻意做成**普通人能做**——每个基准都用普通人验证过可解性。

> 🗣️ "he actually defined intelligence as your ability to learn new things." —— Greg Kamradt
> 译:他实际上把智能定义为"你学会新事物的能力"。

> 🗣️ "Arc benchmarks, normal people can do these. And so we actually test all of our benchmarks to make sure that normal people can do them." —— Greg Kamradt
> 译:ARC 基准普通人都能做。所以我们会真的去测试每一个基准,确保普通人能完成它们。

### 2. ARC 测什么 & LLM 曾经全线失败 / What ARC Tests and When LLMs Failed `[01:48–02:44]`
**要点(中文)**: 主流基准在往"PhD++"方向越出越难(MMLU → MMLU+ → Humanity's Last Exam),很多已超人;ARC 反其道而行——普通人能做的题反而卡住模型。2019 年基准发布后,直到 2024 年 **GPT-4 基座(无推理)也只有约 4–5%**,清晰地暴露"人能做、基座模型几乎做不到"的鸿沟。ARC 也因此维护**隐藏测试集**来防止拟合。

> 🗣️ "we had MMLU, we had an MMLU+, and now we have humanities last exam. Those are going superhuman... Arc benchmarks, normal people can do these." —— Greg Kamradt
> 译:我们有过 MMLU、MMLU+,现在有"人类最后的考试",这些都在走向超人……而 ARC 基准,普通人就能做。

### 3. 推理范式的突破 & ARC 成为行业标准 / The Reasoning Breakthrough and Becoming the Standard `[02:44–04:17]`
**要点(中文)**: **o1 / o1-preview 一出,ARC 分数从五年才爬到的 ~4% 直接跳到 ~21%**——短时间内的跃迁本身就是信号,ARC 借此识别出"推理范式(reasoning paradigm)"是转折性突破。如今 OpenAI、xAI(Grok4)、Gemini(Gemini 3 Pro / DeepThink)、Anthropic(Opus 4.5)都用 ARC-AGI 报告成绩,它已成为事实标准。**启示:关注"分数曲线的突变",往往对应范式级变化,而非线性的堆料。**

> 🗣️ "So actually we used Arc to identify that reasoning paradigm was huge. That was actually transformational for what was contributing towards AI at the time." —— Greg Kamradt
> 译:所以我们其实是用 ARC 识别出"推理范式"意义重大——它对当时推动 AI 进步是转折性的。

### 4. 虚荣指标与"假阳性" / Vanity Metrics and False Positives in AI Progress `[04:17–06:05]`
**要点(中文)**: 大厂采用 ARC 是好事,但要**警惕虚荣指标**——"被采用"不代表使命完成。谈到最常见的"假阳性进展",Greg 戴上"研究者帽子"(对应"经济价值变现帽子"):当下最典型的是 **RL 环境**——"只要能造出 RL 环境就能刷高分"。但这是**打地鼠**:你不可能给未来想做的每件事都造一个环境;而 ARC 的核心是**新颖性 / 未见过的新问题**(也是设隐藏测试集的原因之一)。人类学新东西并不需要专门环境,所以应投资**不靠环境也能泛化**的系统。

> 🗣️ "as long as we can make an RL environment, we can score well on this benchmark... To me, that's kind of like whack-a-mole. You know, you're not going to be able to make RL environments for every single thing you're going to end up wanting to do." —— Greg Kamradt
> 译:只要我们能造出一个 RL 环境,就能在这个基准上拿高分……对我来说这就像打地鼠。你不可能为你最终想做的每一件事都造一个 RL 环境。

> 🗣️ "I would rather see investment into systems that are actually generalizing and you don't need the environment for it. Because... humans don't need the environment to go and train on that." —— Greg Kamradt
> 译:我更希望看到人们投资于真正会泛化、且不需要专门环境的系统。因为……人类并不需要一个环境去专门训练。

### 5. ARC-AGI 的演进与 v3 交互式基准 / The Evolution of ARC-AGI and Inside v3 `[06:05–08:28]`
**要点(中文)**: v1(2019,Chollet 亲手做了 ~800 题)→ v2(2025 年 3 月,更深的升级版)都是**静态基准**;**v3(2026)将是交互式的**。理由:现实世界是不断"行动→反馈→再行动"的循环,**未来 AGI 会由交互式基准来宣告**。v3 是约 150 个游戏化环境,最关键的是**不给任何文字/符号说明**——测试者必须先动几步、观察反馈,自己推断"目标到底是什么"。每个游戏都会让 10 位普通人先试,过不了最低可解性阈值就剔除。

> 🗣️ "future AGIs are going to be interactive. Future AGI will be declared with an interactive benchmark because that is really what reality is." —— Greg Kamradt
> 译:未来的 AGI 将是交互式的。未来的 AGI 会由一个交互式基准来宣告,因为那才真正是现实的样子。

> 🗣️ "we're not going to give any instructions to the test taker on how to complete the environment. So there's no English, there's no words." —— Greg Kamradt
> 译:我们不会给测试者任何"如何完成这个环境"的说明。没有英文,没有文字。

### 6. 超越准确率:用数据与能量衡量智能 / Measuring Intelligence Beyond Accuracy `[08:28–10:22]`
**要点(中文)**: 用"人类时间"评估模型意义有限——**墙钟时间可以靠堆算力任意压缩**,只是一个"要花多少算力"的选择。真正进入智能方程的另外两个因子是:①**完成任务所需的训练数据量**,②**执行所需的能量**(人脑消耗多少能量做一件事,是有基准的)。在 v3 里,效率的度量方式是**数回合数**:统计人类通关所需动作数,与 AI 所需动作数对比,并把 AI 表现**归一化到人类平均水平**——不再允许 2016 年 Atari 那种"百万/十亿帧暴力穷举"的打法。

> 🗣️ "we actually see time as a little bit arbitrary because if you throw more compute at something, you're going to reduce the time no matter what." —— Greg Kamradt
> 译:我们其实觉得"时间"有点武断,因为只要你往一件事上堆算力,无论如何都会把时间压下来。

> 🗣️ "we're going to count the number of actions that it takes a human to beat the game, and we're going to compare that to the number of actions that it takes an AI to beat the game." —— Greg Kamradt
> 译:我们会统计人类通关所需的动作数,再与 AI 通关所需的动作数做对比。

### 7. 如果有人明天解出 ARC-AGI / What Happens If a Model Solves ARC-AGI `[10:22–11:44]`
**要点(中文)**: 从一开始 Chollet 就说:**解出 ARC-AGI 是 AGI 的"必要非充分"条件**。解出 v1/v2 的系统不会是 AGI,但会是**泛化能力最权威的来源/证据**;v3 亦然——击败它不等于 AGI,却是迄今关于"能泛化的系统"最权威的证据。若真有团队明天就做到,ARC 会去分析这个系统、找出仍存在的失败点,并继续引导世界走向"真正的 AGI",以便在真正到来时有能力去宣告它。

> 🗣️ "the thing that solves Arc AGI is necessary for AGI. It's not sufficient." —— Greg Kamradt
> 译:能解出 ARC-AGI 的东西,对 AGI 而言是必要的,但不是充分的。

> 🗣️ "the thing that solves Arc AGI 1 and 2 will not be AGI, but it will be an authoritative source of generalization." —— Greg Kamradt
> 译:解出 ARC-AGI 1 和 2 的系统不会是 AGI,但它会是"泛化能力"的一个权威来源。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **设计自己的 held-out 评测集**:像 ARC 的隐藏测试集一样,留一批客户从没见过的新颖任务,专门检验 Agent 的泛化而非记忆/拟合。
- [ ] **别把"过了某基准"当里程碑**:上线/融资前自查是不是"假阳性进展"——用户真实新场景能不能扛住,而不是刷到一个数字就宣布搞定。
- [ ] **审视你对 RL 环境/微调的依赖**:如果你的能力提升靠"给每个场景造环境",承认这是"打地鼠",评估长尾场景是否会失控;优先投资**不依赖专门环境也能泛化**的能力。
- [ ] **把效率写进你的评测指标**:除了成功率,量化**样本效率(需要多少示例/数据)**与**单位任务能耗/成本**,并按"人类完成所需步数"归一化 Agent 的动作数,防止暴力穷举式解法。
- [ ] **为交互式/agentic 场景建"行动→反馈"评测**:模拟无明确说明、需自己摸索目标的环境,测 Agent 在稀疏反馈下能否自行推断意图。
- [ ] **盯"曲线突变"而非线性进步**:像 ARC 捕捉到 o1 的 4%→21% 跃迁那样,建立能识别范式级跃变的监控,及时切换技术路线。

## 🔑 关键术语 / 概念
- **ARC-AGI** — ARC Prize Foundation 维护的基准(v1 2019 / v2 2025 / v3 2026),测"高效学会新事物"的能力;普通人可做、含隐藏测试集,现被多家前沿实验室用作发布指标。
- **François Chollet 的智能定义** — 智能 = 高效获取新技能的能力(而非记忆或在既有技能上超人);出自 2019 年论文《On the Measure of Intelligence》。
- **Vanity metrics(虚荣指标)** — 好看但不代表真进展的指标;大厂"采用某基准"本身不等于问题已被解决。
- **False positive(假阳性进展)** — 看起来像进步、实则不是,例如靠造 RL 环境刷分。
- **RL environment / whack-a-mole(打地鼠)** — 为特定任务造强化学习环境刷分;因无法覆盖所有未来任务而不可规模化。
- **必要非充分(necessary, not sufficient)** — 解出 ARC 是 AGI 的必要条件但非充分条件:是权威的泛化证据,但不等于 AGI。
- **智能的三因子** — 准确率之外还看:所需**训练数据量**、执行所需**能量**;时间因可被算力压缩而被视为次要。
- **交互式基准(interactive benchmark)** — 通过"行动→反馈"循环评测,无文字说明,靠试探推断目标;被认为更贴近现实与未来 AGI。

## 🔖 高价值金句时间戳
- `[01:08]` "he actually defined intelligence as your ability to learn new things." — 一切的地基:智能是"学会新东西",不是刷分。
- `[03:29]` "So actually we used Arc to identify that reasoning paradigm was huge." — 好评测能提前发现范式级突破(o1 的 4%→21%)。
- `[04:20]` "we're mindful of vanity metrics that come from there too." — 大厂采用 ≠ 使命完成;别被虚荣指标麻痹。
- `[05:41]` "you're not going to be able to make RL environments for every single thing you're going to end up wanting to do." — RL 环境是打地鼠,泛化才是护城河。
- `[07:06]` "future AGI will be declared with an interactive benchmark because that is really what reality is." — Agent 就活在"行动→反馈"里,评测也该如此。
- `[10:45]` "the thing that solves Arc AGI is necessary for AGI. It's not sufficient." — 对"解出基准=AGI"的清醒纠偏。
