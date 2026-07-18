# 前沿模型是怎么练出来的:Anthropic 预训练负责人谈扩展定律、算力与 AI 的未来 / Anthropic Head of Pretraining on Scaling Laws, Compute, and the Future of AI

📄 **[点此查看全文转录 / Full transcript »](../transcripts/YFeb3yAxtjE.md)**

> **来源**: [Anthropic Head of Pretraining on Scaling Laws, Compute, and the Future of AI](https://www.youtube.com/watch?v=YFeb3yAxtjE) · Y Combinator · 2025-09-30 · 时长 64:04
> **讲者**: Nick Joseph(Anthropic 预训练负责人 / Head of Pre-training,嘉宾,SPEAKER_01) × Ankit Gupta(YC 合伙人 / General Partner,主持,SPEAKER_00)
> **一句话定位**: 一场关于"前沿大模型训练工程"的深聊——表面讲预训练与扩展定律,内核是给 AI Agent 创始人的方法论:算力飞轮、"效率即护城河"、经验主义决策、评测(eval)作为撬动大厂的杠杆,以及在模型每年变强的世界里怎么选赛道、避开脚手架陷阱。

## 🎯 TL;DR(中文核心要点)
- **算力飞轮是这一切的底层引擎**:训模型→做出有用产品→卖钱→买更多算力→训更强模型,Anthropic 把这个循环跑了五年。创业公司要问自己:我的产品能不能接进"模型越强、我越强"的正循环。
- **"效率即护城河"在早期真实存在**:Anthropic 早期资金远少于对手,靠"把算力用到极致"拿到领先。别人不精细,你精细,就能弯道超车——这条对算力/成本敏感的 AI 创业同样成立。
- **几乎一切都要靠经验主义解决**:先有理论,但"第一件事就是去测,而且多数时候你会发现自己错了"。别在会议室里争,快速跑实验拿数据。
- **迭代速度决定命运**:能放到后训练(post-training)做的就别放预训练——后训练能天/小时级迭代,预训练是"几个月一次的一杆进洞"。对 Agent 创业者:把你的核心迭代循环压到最短。
- **评测(eval)是小公司撬动大厂的支点**:大厂被"刷 eval 分"驱动,而"做 eval 没有门槛、模型方也没有比较优势"。你造一个好 eval,大厂就会去优化它——顺带定义了行业方向。
- **好 eval 的三条硬标准**:测你真正在乎的东西 + 低噪声(小差异也可信) + 快且好跑。最难的是第一条,而满足第一条的往往难满足后两条。
- **选赛道:押"模型变强就受益"的方向**;警惕"靠一大堆脚手架现在才勉强能跑、下一代模型就不再需要脚手架"的东西。
- **最缺的是工程师不是研究员**:"把它做对不是一个 ML 问题",架构很简单,难在大规模正确实现、并行化、能把任何一层 bug 深挖到底。
- **一个 bug 能毁掉一整代模型**:训练要跑几个月,某处精度写错、你还发现不了,就白烧一代算力。AI 系统里的 bug 极难定位——这是最让人后背发凉的风险。

## 🧭 适合谁 / 什么时候看
- 想理解"大模型为什么会持续变强、还能变多强"的 AI Agent 创始人——判断你押注的能力曲线还有多少空间。
- 在纠结"该不该自研模型 / 靠 API"、以及怎么在大厂阴影下选赛道的创始人。
- 想学习前沿团队怎么做决策(经验主义、迭代速度、组织设计)、怎么招人(工程 vs 研究、通才 vs 专才)的技术型创始人/技术负责人。
- 不适合:想要具体 Agent 产品打法或 GTM 手册的人——这是一场偏工程与心法的对谈,产品/增长内容需要你自己迁移。

## 📝 分段精读

### 1. 背景:从 AI 安全焦虑到 Anthropic 创始团队 / From safety worries to Anthropic `[00:05–03:17]`
**要点(中文)**: Nick 的路径是 Vicarious(机器人视觉)→ OpenAI(安全团队/代码模型)→ Anthropic。他不是学术路线,反而因为"能马上上手做 AI"而选了它。真正的转折点:在 OpenAI 时,他在乎的安全 leads 集体离职去创立 Anthropic,他跟着一起在公司刚起步时加入。给创始人的启示:入场的动机可以是"两头都不亏"的下注,团队(和你信任的人去哪)往往比赛道分析更决定你的落点。
> 🗣️ "Either, like, the safety thing will turn out to be important, and I'll work on that, or it won't be, and I'll just make cool things with AI." —— Nick Joseph `[01:29]`
> 译:"要么 AI 安全这件事真的重要,那我就去做它;要么不重要,那我就用 AI 做些酷东西。"(一个"怎么下注都不亏"的入场逻辑)

### 2. 预训练是什么 & 为什么"预测下一个词"胜出:算力才是主角 / What pretraining is & why next-word prediction won `[03:17–07:14]`
**要点(中文)**: 预训练的核心诉求是"找一个能吃进最多算力的目标"。互联网是最大的数据源,而"预测下一个词"能从无标注文本里自动造出海量、稠密的训练信号。为什么自回归(autoregressive)胜出而不是 BERT 那类?答案"基本是经验的"——但它有个决定性优势:能直接采样生成文本,天然接得上产品与营收。而这正是"算力飞轮"的燃料:发产品→拿营收→买算力→训更强模型。最反直觉的一条心法:细节(具体架构/目标)没那么重要,**算力才是那个决定性变量**。
> 🗣️ "once you have that, there's this positive feedback loop where you can train a model, you can use it to make something useful and sell that and get more money, use that to buy more compute, and then you just actually train it to make it a better model. And we've sort of run that cycle over and over again over the past five years or so." —— Nick Joseph `[04:52]`
> 译:"一旦有了这个,就出现一个正反馈循环:你训出模型,用它做出有用的东西卖钱,拿钱买更多算力,再去训一个更好的模型。过去五年我们就是把这个循环一遍遍地跑。"
> 🗣️ "compute is the thing that matters ... it's surprising how little these details matter compared to throwing more compute at the problem." —— Nick Joseph `[07:00]`
> 译:"算力才是那个真正要紧的东西……相比多砸算力,这些细节有多不重要,是很令人意外的。"

### 3. 扩展定律的工程现实 & "效率即护城河" / Scaling in practice: efficiency as a moat `[07:14–13:10]`
**要点(中文)**: 扩展定律(scaling laws)让 loss 随算力"以幂律 + 常数"可预测地下降;方法论是"先在小规模按比例验证,再放大"。最扎心的失败模式:如果你搞砸了,曲线会偏离幂律,但你分不清是"到了扩展极限"还是"只是学习率没调对"——而且你没跑够长根本不知道反事实。对创业者最有用的是两点历史事实:其一,GPT-3 当年估算训练成本约 500 万美元——"对个人是很多,对公司不算多",小而有钱的团队完全能站上前沿(当时全球"关心这事的可能就 30 人");其二,大多数人当年用算力并不高效,于是 Anthropic 靠"把算力用到极致"拿到领先。这就是"效率即护城河"。
> 🗣️ "most people weren't very efficient with the compute, so we were like, ah, we can get a big lead by being really efficient at how we use the compute." —— Nick Joseph `[11:21]`
> 译:"大多数人用算力并不高效,所以我们心想:啊,只要我们把算力用得特别高效,就能拿到很大的领先。"
> 🗣️ "it seems like I'm one of 30 people who are working on this in, like, the world." —— Nick Joseph `[10:04]`
> 译:"感觉全世界大概只有 30 个人在做这件事,而我是其中之一。"(前沿常常比你想的更空旷、更够得着)

### 4. 硬核 infra 怎么学 + 通才 vs 专才 / How to learn hard infra, and the generalist–specialist balance `[13:10–21:55]`
**要点(中文)**: Nick 入职第一天把公司所有 Slack 读了一遍——早期团队"一切都与你相关"。他强调**结对编程(pairing)是学这类隐性技能的最佳方式**:你不仅学会"要做的那件事",更学到"别人是怎么做的"——比如怎么用 profiler、怎么用 debugger(他坦承进 Anthropic 前从没用过 debugger,一直觉得 print 就够)。工程侧的硬功夫是"纸笔先把能达到的效率算出来(MFU),再用 profiler 把实际逼近理论"。团队演化上有个真实张力:早期全是通才→人人都懂点、但没人真正吃透一个方向;专才太多→又会出现"只有 lead 能把全局串起来"和"单点故障"。答案是**刻意配平通才与专才**。
> 🗣️ "I mostly learned from pair programming ... you learn the, like, thing you're trying to do ... But you also learn how people do it." —— Nick Joseph `[17:24]`
> 译:"我主要是靠结对编程学会的……你学到的不只是你要做的那件事本身,还学到别人是怎么做的。"
> 🗣️ "I'd never actually used a debugger before joining Anthropic ... print seems fine for me." —— Nick Joseph `[18:11]`
> 译:"进 Anthropic 之前我其实从没用过 debugger……总觉得 print 就够用了。"(顶尖团队里也有人靠 pairing 补上基本功)

### 5. 规模化的隐藏难题:坏芯片、失败域、与供应商协作 / Hidden hard problems at scale `[21:55–28:13]`
**要点(中文)**: 规模变大后,最"非显然"的难题不是 ML,而是系统:标准并行方式让整个集群成为**一个失败域**——一块芯片挂了,整个任务就崩。更颠覆 Python 程序员直觉的是:"计算机真的可能是错的"——GPU 会算错、会变慢、数据中心电源会坏。他讲了个经典段子:自己怎么也调不出的 bug,经理一句"大概是计算机坏了",结果真是 GPU 坏了。跨越 GPU/TPU 时,芯片规格(算力/显存/带宽)差异大到无法轻易抽象,"把所有负载都跑在所有芯片上,等于把工作量乘以芯片种类数"。和云厂商的协作靠"共享 Slack + 小规模可复现样例(把 bug 从大代码库里抽出来、单卡单文件复现)"。
> 🗣️ "one chip fails, the whole thing can crash." —— Nick Joseph `[22:32]`
> 译:"一块芯片挂掉,整个训练就可能崩溃。"(规模化的第一课:整个集群是一个失败域)
> 🗣️ "my manager looked at it and was like, ah, yeah, probably the computer's wrong. And I was like, that seems unlikely. And sure enough, the computer was wrong." —— Nick Joseph `[23:56]`
> 译:"我经理看了一眼说'啊,大概是计算机错了',我心想'不太可能吧'——结果还真是计算机错了。"

### 6. 预训练 vs 后训练、数据、合成数据与评测 / Pretraining vs post-training, data, and evals `[28:13–41:01]`
**要点(中文)**: 这一段对创业者信息密度最高。(1)**经验主义**:预训练/后训练/RL 怎么配比,基本都要实测;别让"我管预训练所以预训练必须赢"这种组织身份绑架科学判断。(2)**数据没枯竭**:"数据非常多,只是增速比算力慢";而且"有用的互联网到底多大,没人真知道"——PageRank 那种给人看的质量指标,未必是给模型的对的质量指标;真正的金块可能藏在长尾里。(3)**合成数据**:蒸馏可行,但你无法靠采样自己的模型训出比自己更强的模型——你只会学到同一个分布(它若认为 5+5=11,新模型也会学成 11)。(4)**评测(eval)是小公司的杠杆**:大厂被 eval 分驱动,而做 eval 没门槛、模型方没有比较优势;你造个好 eval,大厂就会去优化它。好 eval 三标准:测你真在乎的 + 低噪声 + 快好跑。而且"loss 本身其实好得惊人"——想评"AI 医生"?收集一批优秀医患对话记录,测模型预测这些 transcript 的 loss,token 多、噪声低,loss 压到很低就等于模型逼近了那批医生。
> 🗣️ "There's no comparative advantage to having the model to making an eval. So I do think it's actually, like, an interesting way to, like, influence the behavior of the big labs. Like, you make some eval and people will optimize that one." —— Nick Joseph `[40:21]`
> 译:"做 eval 这件事,拥有模型并不带来比较优势。所以我真觉得这是影响大厂行为的有趣办法:你造一个 eval,大家就会去优化它。"
> 🗣️ "there is so much data. It's growing at a slower rate than we're getting more compute." —— Nick Joseph `[31:54]`
> 译:"数据非常多,只是它的增长速度比我们获得算力的速度更慢。"(所谓"数据枯竭"没他想得那么确定)
> 🗣️ "you solved those. It's shockingly narrow and can't do most of the other things." —— Nick Joseph `[38:01]`
> 译:"你把那些题解出来了,但它窄得惊人,大多数别的事情还是做不了。"(设了目标、达成后才发现目标远不是你以为的那回事——eval 陷阱)

### 7. 对齐:先给汽车装上方向盘 & 迭代速度决定放哪儿做 / Alignment as a steering wheel, and where to iterate `[41:01–47:36]`
**要点(中文)**: Nick 描绘 AGI 的冲击力:一旦做成,"每个人都能开出一家由十亿个和他一样聪明、在很多事上更聪明的智能体组成的公司"——远比科幻电影里那"一个类人机器人"更颠覆。对齐(alignment)的核心问题是"怎么让模型和你共享目标",尤其当模型比你更聪明时。他用"给汽车装方向盘"作比:先把方向盘装上(能操控),至于谁来开、开去哪,之后再定;而且长期应当走向"某种民主化控制",而非某一个人的价值观。对创业者最可迁移的一条工程原则:**能在后训练做的就别放预训练**——因为后训练迭代快(天/小时级),而预训练是"几个月一杆进洞"、错了代价极大。把这条翻译成 Agent 创业:凡是能在提示/后处理/轻量微调层快速试错的,就别硬塞进慢环节。
> 🗣️ "every human can spin up a company of, like, one billion, as smart as them at most things, but way smarter at other things." —— Nick Joseph `[41:46]`
> 译:"每个人都能开出一家由十亿个智能体组成的公司,它们在大多数事上和你一样聪明,在另一些事上远比你聪明。"
> 🗣️ "anything you can do in post-training, you probably should because your iteration loop, like, the ability to make progress is really fast." —— Nick Joseph `[45:22]`
> 译:"凡是能在后训练里做的,你多半就该在那里做——因为它的迭代循环、也就是取得进展的速度,真的很快。"

### 8. 未来、算力瓶颈与给创业者的机会 / The future, the compute bottleneck, and where startups can win `[47:36–63:54]`
**要点(中文)**: 面向未来,Nick 最在意两件事:**范式转变**(如向 RL 的转移,未来大概率还有更多)和**极难定位的 bug**——一个藏在几万行代码里的精度错误就能毁掉一整代模型,而且你可能永远发现不了。他强调团队最缺的是**能把任何一层深挖到底的工程师**,不是写论文的研究员("把它做对不是一个 ML 问题")。现实是**算力极度受限**:"你现在用的 Sonnet 4 / Opus 4,都是我们在那个规模上的第一次尝试"——若算力多 10 倍、100 倍,就能天天重训而非几个月一次。给创业者的选赛道建议:押"模型变强就受益"的方向、押"用当前模型几乎能跑通、只差一堆工程活"的方向;**警惕靠厚重脚手架硬撑、下一代模型一来脚手架就作废**的东西。他还给了两个具体机会:给高速扩张公司"免费提供服务/顾问"式的外包,以及"帮我确认这批芯片算得对不对"的芯片校验创业;并提醒创业者认真想想"AGI 来了之后,怎么让它对世界是好事"。
> 🗣️ "a single bug can, like, derail you for months." —— Nick Joseph `[48:54]`
> 译:"一个 bug 就能让你脱轨好几个月。"(在几个月一次的训练里,这等于烧掉一整代)
> 🗣️ "if you're using, like, CloudSonic 4 or Cloud Opus 4, it's, like, it's our first shot at those models at that scale." —— Nick Joseph `[58:56]`
> 译:"你现在用的 Sonnet 4 或 Opus 4,其实是我们在那个规模上的第一次尝试。"(整个行业都被算力卡着脖子)
> 🗣️ "the thing to watch out for is things where, like, they work now with a huge amount of work, like, to build up a scaffold, but the next generation, you're not going to need the whole scaffold you built up." —— Nick Joseph `[60:53]`
> 译:"要当心这种东西:现在得靠搭一大堆脚手架、费很大劲才勉强能跑,但下一代模型一来,你搭的整套脚手架就都不需要了。"

## 🚀 给 AI Agent 创始人的行动项
- [ ] **把产品接进"算力飞轮"的下游**:确认你的价值主张是"模型越强、你越强"(押 `[60:23]` 的"anything that benefits from the model getting smarter"),而不是靠模型的当前缺陷吃饭。
- [ ] **做减法审视你的脚手架**:列出为绕过当前模型能力而搭的 workaround,标注"下一代模型可能让哪些直接作废";要么它能沉淀成业务资产,要么别重投(见 `[60:53]`)。
- [ ] **为你的赛道造一个高质量 eval**:选"你真正在乎、低噪声、快好跑"的评测;它既是你的内部指北针,也可能变成撬动大厂优化方向的公开杠杆(见 `[40:21]`)。
- [ ] **用 loss/transcript 法评测难量化能力**:对"长对话里抽信号"这类难题,收集一批高质量专家对话记录,用模型预测 transcript 的 loss 做低噪声评测,而非只靠单点准确率。
- [ ] **把核心迭代循环压到最短**:凡能在提示/后处理/轻量微调层快速试错的,就别塞进慢环节;像 Nick 说的"能在后训练做就别放预训练"一样对待你的产品实验(见 `[45:22]`)。
- [ ] **决策靠实测、别被身份绑架**:先有假设立刻去测,默认自己会错;别让"这是我负责的模块"影响对数据的解读(见 `[29:50]` 一带的经验主义)。
- [ ] **招"能深挖到底"的工程师**:优先能把 bug 从 ML 一路追到字节层的工程能力,而非只会写论文;并刻意配平通才与专才、消除单点故障。

## 🔑 关键术语 / 概念
- **Pre-training(预训练)** — 用海量无标注文本、以"预测下一个词"为目标灌入尽可能多算力,教模型变聪明的阶段;是模型能力的主要来源。
- **Post-training(后训练)** — 预训练之后的调校阶段(RLHF、推理训练、微调、personality 塑造等),迭代快、可天/小时级试错。
- **Scaling laws(扩展定律)** — loss 随算力/数据/参数以"幂律 + 常数"可预测下降的经验规律;偏离幂律往往意味着出了 bug 或到了极限。
- **算力→模型→营收飞轮** — 训模型→做产品→卖钱→买算力→训更强模型的正反馈循环,自回归目标天然适配这个循环。
- **Autoregressive / next-token prediction(自回归 / 下一词预测)** — 能直接采样生成文本、天然接产品的训练目标;胜出"主要是经验的"。
- **Failure domain(失败域)** — 标准并行下整个集群是一个失败域,单卡故障即全任务崩;规模越大故障率越高。
- **MFU(FLOPs 利用率)** — 衡量 GPU 算力被真正用上的比例;瓶颈常在 HBM 带宽、CPU offload 等约束,可纸笔先算出理论上限再逼近。
- **Eval(评测)** — 判断模型好坏的量化指标;好 eval = 测真在乎的东西 + 低噪声 + 快好跑;是小公司能撬动大厂的支点。
- **Constitutional AI(宪法式 AI)** — 用一套"宪法"规则约束模型行为;可写进系统提示,也可在训练时注入(注入更鲁棒但更难改)。
- **Synthetic data / distillation(合成数据 / 蒸馏)** — 用强模型生成数据训小模型可逼近其能力;但采样自身分布无法训出超过自身的模型。
- **Scaffold(脚手架)** — 为弥补当前模型能力而搭的复杂工程外壳;风险是下一代模型可能让它整体作废。

## 🔖 高价值金句时间戳
- `[04:52]` "there's this positive feedback loop where you can train a model ... buy more compute, and then you just actually train it to make it a better model." — 算力飞轮是整场对谈的底层引擎,创业先问自己接不接得进去。
- `[07:00]` "compute is the thing that matters ... surprising how little these details matter." — 别过度纠结架构细节,算力/规模是决定性变量。
- `[11:21]` "we can get a big lead by being really efficient at how we use the compute." — "效率即护城河":别人不精细,你精细就能反超。
- `[40:21]` "There's no comparative advantage to having the model to making an eval ... you make some eval and people will optimize that one." — 评测是小公司撬动大厂、定义方向的支点。
- `[45:22]` "anything you can do in post-training, you probably should because your iteration loop ... is really fast." — 迭代速度决定命运,把试错放到最快的那一层。
- `[52:20]` "the thing we, like, most need is engineers ... getting it correct isn't really an ML problem." — 最缺能把系统做对、能深挖 bug 的工程师,不是论文研究员。
- `[58:56]` "it's our first shot at those models at that scale." — 整个行业被算力卡着脖子,你用的旗舰模型都只是"第一次尝试"。
- `[60:47]` "anything that just kind of looks like, oh, this almost works with current models but requires, like, a bunch of work is a pretty, pretty promising direction." — 选赛道:押"当前模型几乎能跑通、只差工程活"的方向。
