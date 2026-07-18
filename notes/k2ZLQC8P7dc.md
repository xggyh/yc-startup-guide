# 为什么只靠 Scaling 造不出 AGI:François Chollet 谈符号程序合成、可验证奖励与创业机会 / François Chollet: Why Scaling Alone Isn't Enough for AGI

> **来源**: [François Chollet: Why Scaling Alone Isn't Enough for AGI](https://www.youtube.com/watch?v=k2ZLQC8P7dc) · Y Combinator · 2026-03-27 · 时长 57:24
> **讲者**: 嘉宾 François Chollet(ARC Prize 创始人、Keras 作者、新 AGI 实验室 Ndea 创始人,即 SPEAKER_03);主持为 YC《Lightcone》播客团队(多位主持人,对应 SPEAKER_00/01/02/04,含 Diana Hu 等,转录未逐一点名故保留 SPEAKER 编号)
> **一句话定位**: 一位顶级 AI 研究者拆解"为什么可验证奖励让 coding agent 突然爆发、纯 scaling 到不了 AGI、以及非共识技术路线该怎么押注",对判断 AI Agent 创业该做什么、护城河在哪、如何避免被下一层能力吞掉极具参考价值。

## 🎯 TL;DR(中文核心要点)
- **可验证奖励(verifiable reward)是这一波 agent 能力爆发的真正原因**:凡是解答能被形式化验证、奖励信号可信任的领域(代码、数学),用现有 LLM 栈就能"跑 RL 循环、暴力挖掘整个解空间",实现近乎完全自动化。这是判断"哪个 agent 赛道现在能做成"的第一性标准。
- **模型不是变聪明了,而是变有用了**:coding agent 的强不是 IQ 提高,而是"训练得更好"——在可验证环境里试错 + 学会在脑中模拟代码执行(跟踪变量值)。创业者要押的是"能被可验证化的领域",而不是等模型智力提升。
- **不可验证领域会长期卡住甚至停滞**:写文章、法律这类没有可信奖励信号的任务,进步会非常慢,因为只能靠昂贵的人类标注。别把 agent 创业押在这类"模糊输出"上,除非你能自己造出一个可验证的奖励函数。
- **harness(任务脚手架)是当下最有价值的落地手段,但不是通往 AGI 的路**:harness 本质是人把"高层解题策略"喂给模型。Chollet 直言"需要人来写 harness 恰恰说明我们还没到 AGI"——但对创业者而言,harness 工程正是把 LLM 变成可交付产品的核心杠杆。
- **要押就押"能随算力/数据自动变强、把人移出改进回路"的东西**:任何"只能靠人类工程师加班才能提升能力"的系统,能力上限会被人力锁死。这既是选技术栈的标准,也是设计 agent 产品自我改进机制的标准。
- **非共识押注的逻辑**:一个大想法即使只有 10–15% 成功率,只要"成了就很大、且没别人在做、你不做就没人做",就值得试——这正是 YC 的信条,也是 Chollet 做 Ndea 的理由。
- **AGI 的定义之争**:Chollet 认为"自动化大多数经济任务"是自动化、不是智能;真正的通用智能是"用与人类相同的数据/算力效率去掌握任意新任务"。ARC 系列基准就是为测这个"残差能力差距"而设计的移动靶。
- **时间表与机会**:Chollet 预测 AGI 大约在 2030 年代初到来;当下仍有大量新范式(遗传算法、状态空间模型、符号程序合成等)值得创业者从 70/80 年代老论文里翻出来重做。

## 🧭 适合谁 / 什么时候看
- 正在做或准备做 **AI Agent 创业**、需要判断"哪个领域现在真能自动化、护城河在哪"的创始人/工程师。
- 想理解 **coding agent 为什么突然能打**、以及这套 RL + 可验证奖励范式还能复制到哪些领域的人。
- 对 **AGI 技术路线、符号程序合成、ARC-AGI 基准**感兴趣,想在共识之外找差异化技术押注的研究型创业者。
- 想学**如何做爆款开源项目 / 社区**(Keras 经验)的独立开发者。

## 📝 分段精读

### 1. Ndea 的愿景:用最短符号程序替代神经网络 / A New ML Paradigm & Symbolic Programs `[00:31–03:04]`
**要点(中文)**: Ndea 不是在做"另一个 coding agent",而是想在深度学习之下重建整个机器学习栈。核心思路:把深度学习里"用梯度下降拟合参数曲线"换成"寻找解释数据的最短符号模型",并造一套"符号下降(symbolic descent)"来代替梯度下降。理论依据是最小描述长度原理——最能泛化的模型就是最短的模型。好处是数据需求极少、推理极快、泛化和组合能力更强。

> 🗣️ "we are replacing the parametric curve with a symbolic model that is meant to be as small as possible. It's like the simplest possible model to explain the data" —— François Chollet
> 译:我们把参数曲线换成一个尽可能小的符号模型——就是能解释数据的最简单的那个模型。

> 🗣️ "the minimum description length principle that the model of the data that is most likely to generalize is the shortest" —— François Chollet
> 译:最小描述长度原理告诉我们:最可能泛化的那个数据模型,就是最短的那个。

### 2. 为什么值得押非共识、且不与 coding agent 竞争 / Betting on the Non-Consensus Path `[03:04–07:22]`
**要点(中文)**: 所有人都在往 LLM 栈上堆钱,因为"它确实在 work"。但 Chollet 认为这套栈虽好、甚至可能到 AGI,却远非最优;AI 长期一定会趋向最优,所以他选择"直接跳到最优的地基"。他给出的押注逻辑非常创业化:大想法 + 低成功率(10–15%)+ 成了就很大 + 没人做 = 值得试。这句被主持人当场认成"YC 的使命宣言"。

> 🗣️ "if you have a big idea and it has very low chance of success, but if it works, it's going to be big and no one else is going to be working on it... If you don't do it, no one else will do it." —— François Chollet
> 译:如果你有一个大想法,它成功率很低,但一旦成了就会很大,而且没有别人在做——如果你不做,就没人会做。

> 🗣️ "that's almost like the mission statement of Y Combinator, the thing that you just said." —— SPEAKER_02(主持人)
> 译:你刚说的这句,几乎就是 Y Combinator 的使命宣言。

### 3. 可验证奖励:coding agent 突然变强的真正原因 / Why Coding Agents Suddenly Work `[07:22–10:48]`
**要点(中文)**: 代码之所以先"沦陷",是因为它提供了**可验证的奖励信号**(单元测试、编译、报错)。任何"解答可被形式化验证、奖励可信任"的领域,用现在的 LLM 栈就能完全自动化;数学是下一个。反过来,写文章、法律这类不可验证领域,只能靠昂贵的人类标注,进步会极慢甚至停滞。关键机制:模型不再只"补全代码",而是在可验证环境里试错生成海量训练数据,并学会在脑中模拟代码执行、跟踪变量值。对创业者:先问"我这个领域的奖励能不能被可信地验证"。

> 🗣️ "any problem where the solutions you propose can be formally verified and you can actually trust the reward signal... can be fully automated with current technology, with the LLM-based stack." —— François Chollet
> 译:任何一个"你提出的解可以被形式化验证、且你能真正信任那个奖励信号"的问题,用现有的 LLM 栈就能被完全自动化。

> 🗣️ "writing essays is the typical example of a domain that's not verifiable... progress of reasoning models... on this type of domain is going to be very slow... Maybe it's even going to stall." —— François Chollet
> 译:写文章是"不可验证领域"的典型例子……推理模型在这类领域的进步会非常慢……甚至可能停滞。

### 4. 什么是真正的 AGI & ARC 的由来 / Defining AGI and ARC's Origin `[10:48–18:20]`
**要点(中文)**: Chollet 反对"能自动化多数经济任务就是 AGI"的定义——那是自动化,不是智能。他的定义:能以**与人类相同的效率**(相同数据量、相同算力)去理解并掌握任意新问题/新领域。他承认"先实现自动化定义、再实现智能定义"这条路正在发生。ARC 的起源:2016 年他在 Google Brain 发现梯度下降学不会"可泛化的推理程序"——问题不在深度学习能不能表达,而在梯度下降只会做过拟合式的模式匹配。于是他想做"推理界的 ImageNet",2019 年发布了 ARC。

> 🗣️ "AGI is basically going to be a system that can approach any new problem, any new task, any new domain, and make sense of it, like model it, become competent" —— François Chollet
> 译:AGI 本质上是这样一个系统:面对任何新问题、新任务、新领域,它都能理解它、建立它的模型、变得胜任。

> 🗣️ "Gradient descent would not find generalizable programs. It would instead... end up doing... over fit pattern matching" —— François Chollet
> 译:梯度下降找不到可泛化的程序,它最终只会做过拟合式的模式匹配。

### 5. ARC V1→V3 与驱动今日 agent 的 RL 循环 / The RL Loop Powering Coding Agents `[18:20–27:03]`
**要点(中文)**: ARC 是行业变化的"晴雨表":V1 长期被 base LLM 卡在 10% 以下(哪怕规模放大 5 万倍),直到 2024 年底推理模型(o1/o3)出现才阶跃式突破;V2 更难,直到 coding agent 兴起才被快速刷爆。背后是同一个 RL 循环:生成任务→用推理模型求解→验证→用成功的推理链微调模型→重复上百万次(只要肯花钱)。结论振聋发聩:**不是模型变聪明了,而是换了一种后训练范式,让它们在特定领域突然变得更有用**。有主持人提到 W26 batch 的 Confluent Labs 几个月就把 ARC V2 刷到 97%,靠的正是搭 harness。

> 🗣️ "if you can run this kind of loop you can... brute force mine effectively the entire space and get extremely high performance" —— François Chollet
> 译:只要你能跑起这个循环,你就能有效地暴力挖掘整个解空间,拿到极高的性能。

> 🗣️ "it's not that the models are smarter it's that they're suddenly more useful. It is possible to be more useful in particular domains without being smarter" —— SPEAKER_01(主持人)
> 译:不是模型更聪明了,而是它们突然更有用了——在特定领域,变得更有用并不需要变得更聪明。

> 🗣️ "the fact that you need humans to engineer these harnesses is also a sign that we're short of agi today because if we had agi... agi would just make its own harness" —— François Chollet
> 译:你需要人来设计这些 harness,这件事本身就说明我们离 AGI 还差得远——真有了 AGI,它会自己造 harness。

### 6. ARC-AGI V3:测量"智能体智能" / Measuring Agentic Intelligence `[27:03–35:31]`
**要点(中文)**: V1/V2 是被动的因果建模(数据给你,找规则);V3 完全不同,测的是**智能体智能**:把 agent 丢进一个陌生小游戏,不给说明、不告诉目标、不告诉操作键,它必须自己探索、自己设定目标、建世界模型、规划并执行——而且**按效率评分**,要匹配人类的动作效率。为防被"造更多同类游戏来训练"刷分,V3 专门做了与公开集差异很大的私有集。ARC 团队为此建了一个真正的游戏工作室,做了 250+ 只靠"核心先验(物理、物体、agent 意图)"、不含语言/文化符号的游戏。

> 🗣️ "we are trying to measure agentic intelligence so it's interactive it's active... the data is not provided to you you must go get it" —— François Chollet
> 译:我们要测的是智能体智能,它是交互的、主动的……数据不会给你,你必须自己去获取。

> 🗣️ "with r3 you actually must gather the data and you must do so efficiently... you're scored on your efficiency you must match human level efficiency" —— François Chollet
> 译:在 V3 里你必须自己去采集数据,而且必须高效地采……你是按效率评分的,你得达到人类级别的效率。

### 7. AGI 会不会只有一万行代码 & 如何搭复利式研究栈 / 10K Lines of Code and Building Ndea `[35:31–46:46]`
**要点(中文)**: Chollet 大胆预测:回头看,AGI 的"流体智能引擎"会是一个不到 1 万行的代码库(模型仅 MB 级),知识库另算且很大;甚至 1980 年代的算力就够跑。他把这套方法类比为"科学的化身"——科学本质是符号压缩(把一堆观测压成一条简洁的符号规则),而这必须用符号模型、不能靠拟合曲线。关于建实验室的实操建议:从明确愿景(符号程序合成 + 深度学习引导的程序搜索,类似 AlphaZero 破组合墙)出发,前半年疯狂试错找地基,但**关键是要建一个"复利式"的可复用栈,别老是从零开始换新方向,也别过早锁死地基**。

> 🗣️ "when you create a gi retrospectively it will turn out that it's a code base that's less than 10 000 lines of code and that if you had known about it back in the... 1980s you could have done a gi back then using the computer resources available" —— François Chollet
> 译:等 AGI 被造出来,回头看会发现它是一个不到一万行的代码库;而且如果 1980 年代就知道它,用当时的算力就能造出 AGI。

> 🗣️ "science is fundamentally a symbolic compression process... the NDI[Ndea] approach to program synthesis is that we are building science incarnate, the scientific method in algorithmic form." —— François Chollet
> 译:科学本质上是一个符号压缩过程……Ndea 的程序合成路线,就是在把科学本身、把科学方法以算法形式重新造出来。

> 🗣️ "You want a compounding stack. You want to build reusable foundations... don't commit to the foundation layer too early, but also make sure that at some point you're building this compounding structure." —— François Chollet
> 译:你要的是一个能复利叠加的栈,要搭可复用的地基……别过早把地基定死,但也要确保到某个点你开始构建这种复利式结构。

### 8. 给创业者、研究者与开源作者的建议 / Advice for Founders and Builders `[46:46–57:24]`
**要点(中文)**: (1)新范式仍有巨大机会:计算是"大均衡器",若把砸给深度学习的钱砸给遗传算法、状态空间模型等,同样可能出惊人结果;想做新 lab 的人应去读 70/80 年代的老论文,因为当年探索更多元,后来"坍缩"成了单一路线。(2)选路线的硬标准:**押能随算力/数据 scale、能把人移出改进回路的方法**;凡是"只能靠人类工程师投入才能提升能力"的,能力上限就被人力锁死。(3)开源经验(Keras):把 API 做得极简直观(对标 scikit-learn)、把上手体验/文档做到能"教会人这个领域"、大力投入社区、并"雇你的铁粉"。(4)给 18 岁的人:AI 是赋能而非替代,越懂编程和目标领域,越能把这波浪潮变成自己的工具——"你阻止不了 AI,问题是你怎么利用它、怎么乘上这股浪。"

> 🗣️ "you are looking for approaches that scale... It will not work... capabilities are going to be bounded... by human investment... You want to be in a setup where the system can improve its capabilities with no human in the loop" —— François Chollet
> 译:你要找的是能 scale 的方法……否则不行,能力会被人力投入锁死……你要的是一个系统能在没有人参与的情况下自己提升能力的局面。

> 🗣️ "hire your power users, like hire your fans... find the most enthusiastic users from your community and just hire them on your team." —— François Chollet
> 译:雇你的深度用户、雇你的粉丝……从社区里找出最有热情的用户,直接招进团队。

> 🗣️ "you're not gonna stop... ai progress... the next question is okay, ai progress is here, it's actually going to keep accelerating, how do you make use of it, how do you leverage, how do you ride the wave" —— François Chollet
> 译:你阻止不了 AI 的进步……接下来的问题是:AI 已经来了、而且会持续加速,你要怎么利用它、怎么借力、怎么乘上这股浪?

## 🚀 给 AI Agent 创始人的行动项
- [ ] **用"可验证奖励"筛赛道**:对你想做的每个 agent 场景,先问"输出能否被形式化、可信地验证?"能→可跑 RL 循环、可自动化、值得押;不能→要么自己设计一个可信奖励函数,要么绕开。
- [ ] **把 harness 工程当核心能力**:短期内产品竞争力主要来自把问题结构化、把高层解题策略喂给模型的 harness(参考 ARC V2 被 harness 刷爆的案例),而不是等基座模型变聪明。
- [ ] **给你的 agent 造"可验证训练环境"**:像 coding agent 那样,用少量人力搭一个能自动生成海量试错数据的验证环境(单测/仿真/规则),让数据随算力指数增长,把人移出改进回路。
- [ ] **别把公司押在不可验证的"模糊输出"上**:纯写作/法律意见/主观创意类任务进步慢、易停滞;若必须做,先想清楚你的可信奖励信号从哪来。
- [ ] **设计"复利式"技术栈,别老推倒重来**:早期可以疯狂试错找地基,但一旦找到就沉淀可复用的层,一层叠一层;避免"每换一个方法上一次的经验全作废"。
- [ ] **警惕被"上一层能力"吞掉**:随着模型自带更多能力(甚至自己造 harness),今天靠脚手架赚的钱可能被平台方收编——持续问"我这层价值,一年后还会不会被基座模型直接覆盖"。
- [ ] **做开源/社区时"雇你的铁粉"**:把 API 做到极简、文档做到能教会领域新人、把最活跃用户招进团队,这是 Keras 验证过的增长与护城河打法。

## 🔑 关键术语 / 概念
- **Verifiable reward(可验证奖励)** — 解答能被形式化、可信地判定对错的奖励信号(如代码的单元测试、数学的证明)。是当下能被完全自动化的领域的分水岭。
- **RL loop(强化学习循环)** — 生成任务→用推理模型求解→验证→用成功的推理链微调→重复百万次;coding agent 和 ARC 被刷爆背后的通用后训练范式。
- **Harness(任务脚手架)** — 人为模型注入高层解题策略/结构的外层封装;当前落地价值极高,但 Chollet 认为"需要人写 harness"恰恰说明尚未到 AGI。
- **Program synthesis(程序合成)** — 直接搜索出能解释数据的显式程序,而非拟合参数;Ndea 的核心路线,用深度学习引导的搜索来破"组合爆炸"墙(类比 AlphaZero)。
- **Symbolic descent / MDL(符号下降 / 最小描述长度)** — 用"寻找最短符号模型"代替梯度下降拟合曲线;依据 MDL:最能泛化的模型就是最短的模型。
- **Agentic intelligence(智能体智能,ARC-AGI V3 测量目标)** — 在陌生、无说明的环境里自主探索、设目标、建世界模型、规划执行,并以人类级效率完成。
- **Skill-acquisition efficiency(技能获取效率,Chollet 的 AGI 定义)** — 用与人类相同的数据/算力效率去掌握任意新任务的能力,区别于"自动化多数经济任务"。
- **Core knowledge priors(核心知识先验)** — ARC 游戏只依赖基础物理、物体、agent 意图等人类天生先验,不含语言/文化符号,以测纯流体智能。

## 🔖 高价值金句时间戳
- `[06:26]` "it's really because code provides you with a verifiable reward signal" — 一句话点破 coding agent 爆发根因;选赛道请以此为第一性标准。
- `[07:55]` "writing essays is the typical example of a domain that's not verifiable... Maybe it's even going to stall." — 反面清单:别把 agent 创业押在没有可信奖励的模糊输出上。
- `[22:36]` "It is possible to be more useful in particular domains without being smarter" — 提醒创业者:红利来自"变有用"的后训练范式,不必等模型 IQ 提升。
- `[25:07]` "if we had agi... agi would just make its own harness" — harness 是当下最强杠杆,却也是"尚未到 AGI"的证据;想清楚你的护城河会不会被吞掉。
- `[35:33]` "it will turn out that it's a code base that's less than 10 000 lines of code" — 对"AGI 必然是万亿参数大 scale"的反叙事,给非共识技术押注者打气。
- `[50:21]` "you are looking for approaches that scale... the system can improve its capabilities with no human in the loop" — 选技术栈/设计产品自改进机制的黄金标准:别让人力锁死能力上限。
- `[53:14]` "hire your power users, like hire your fans" — 做开源/社区最实用的一条增长与团队建议。
- `[56:39]` "how do you make use of it, how do you leverage, how do you ride the wave" — 全篇心态收束:阻止不了 AI,就想清楚怎么乘浪。
