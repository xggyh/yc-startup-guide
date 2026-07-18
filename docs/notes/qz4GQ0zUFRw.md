# 人脑真正独有、AI 正拼命追赶的那个东西:世界模型 / The Key Thing Human Brains Have That AI Is Trying To Learn

📄 **[点此查看全文转录 / Full transcript »](../transcripts/qz4GQ0zUFRw.md)**

> **来源**: [The Key Thing Human Brains Have That AI Is Trying To Learn](https://www.youtube.com/watch?v=qz4GQ0zUFRw) · Y Combinator · 2026-07-17 · 时长 74:27
> **讲者**: YC《Decoded》系列两位研究者对谈(transcript 未清晰自报姓名,结尾主持人称嘉宾为 "Francois")。SPEAKER_02 为主讲——在斯坦福讲授强化学习/"不确定性下的决策"课程、参与斯坦福机器人中心;SPEAKER_01 为提问方,经营一家用图卷积网络做药物设计的公司。为稳妥,金句仍按 SPEAKER_xx 标注。
> **一句话定位**: 把"样本效率"这个通向 AGI 的核心难题,用 状态-动作-奖励-转移函数 的强化学习框架讲透,并说清 model-free vs model-based、合成数据护城河、世界模型到底怎么落地——帮做具身/Agent 的创始人判断该做哪种模型、护城河在哪、机会窗口何时到。

## 🎯 TL;DR(中文核心要点)
- AI 现阶段两大瓶颈:**intelligence per watt(每瓦智能)** 与 **intelligence per sample(每样本智能)**;后者就是样本效率,是"世界模型"要解决的核心。人类几次尝试就学会,模型要几万个样本。
- **"世界模型"不是新词**:牛顿力学就是一个完美世界模型——NASA 拦截小行星、SpaceX 落火箭都是 0 样本靠它算出来的;人脑的"品味"(预测别人会不会喜欢)、"预判 VC/客户会说什么"也是世界模型,是十几年创业试错训练出来的。
- 拆解任何 RL/Agent 问题就看四件事:**S(状态)/ A(动作)/ R(奖励)/ 转移函数**。能不能求解主要看**动作空间大小**和**是否可微**——可微才能凸优化/SGD,不可微只能上暴力 RL。
- **AlphaGo/MCTS 不可扩展**:动作空间一大就崩(围棋 361 → 自驾约 36 万 → 机器人 10^16),测试时规划(test-time planning)的模型调用次数指数爆炸。类比:开车时"60 秒才转一次方向盘,车毁人亡"。
- **真正的护城河是"带动作标注的轨迹数据"**:观察类视频(YouTube、第一视角)遍地都是,但"当时到底采取了什么动作"极稀缺——只有 Tesla 有车队级动作数据。"what we don't have is the actions they take."
- **破解数据稀缺的主流打法(Dreamer / 视频扩散 / JEPA)**:先用海量观察数据训一个世界模型,再用极少量数据做 **action conditioning(动作条件化)** 后训练,然后在"想象 rollout"里训练策略。Dreamer 全靠合成数据挖到 Minecraft 钻石;Wave 用这套思路的 Gaia 融了 15 亿美金。
- **model-free vs model-based 先想清**:model-free(VLA/行为克隆,像 LLM 下一 token 预测——快但弱);model-based(带世界模型——强,但推理慢、要做测试时规划)。策略更强的代价是推理更贵。
- **开放问题=创业切入点**:实时规划、测试时自适应(OOD)、更高保真物理(PINs 目前不行)、跨本体(cross-embodiment)泛化、触觉/摩擦感知。2026 是"demo 开始像那么回事"的第一年。

## 🧭 适合谁 / 什么时候看
- 想做具身智能 / 机器人 / 自动驾驶,或任何需要"从环境采数据、训练决策策略"的 AI 创始人与工程师。
- 想真正搞懂 world model、model-based RL、MCTS、JEPA、合成数据 到底是什么、能不能用到自己产品上的人。
- 正在纠结 "model-free 快糙猛 vs model-based 强但贵" 技术路线的团队。
- 想从 AI 底层未解难题里找差异化切入点、判断时机窗口的人——在定技术路线、评估数据战略之前看。

## 📝 分段精读

### 1. 样本效率:通向 AGI 的核心瓶颈 / Sample efficiency & perfect efficiency `[00:00–05:10]`
**要点(中文)**: 开场把问题定死在"样本效率"上:人类几次尝试就学会新游戏/技能,模型要几万个样本。主讲把它拆成两个可量化的目标——每瓦智能、每样本智能;引 François Chollet 的定义:智能是"获取技能的速率",不是已有技能量。完美样本效率的极限是 0 样本,而这**已经存在**——牛顿力学就是完美世界模型,NASA/SpaceX 靠它直接算出轨迹,不需要去环境里采数据。
> 🗣️ "the two major problems that we have left to solve is intelligence per watt and intelligence per sample" —— SPEAKER_02
> 译:我们还剩下要解决的两个大问题,就是"每瓦智能"和"每样本智能"。
> 🗣️ "intelligence as a rate of skill acquisition versus skill acquisition" —— SPEAKER_02(转述 François Chollet)
> 译:智能是"获取技能的速率",而不是"已经掌握的技能量"——两者完全不同。

### 2. 人脑里的世界模型:品味就是预测 / World models in the human brain `[05:10–09:20]`
**要点(中文)**: 把世界模型从火箭拉回创业:创始人的"品味"本质上就是预测别人会不会喜欢这个东西,是十几年试错训练出来的世界模型;预判 VC、客户会说什么,同样是在脑内 rollout。引 1967 年 Richardson 篮球实验(实际投篮 vs 闭眼想象投篮,提升幅度几乎相同 ~24% vs ~23%)佐证人脑有极强的内部模拟能力;并提出神经科学假说:1000 万年前的"大脑皮层大扩张"整个目的就是把世界模型越做越好。对做 Agent 的启示:只做"预测下一个动作"的策略(VLA),不如有一个可依赖的世界模型——无论用于训练还是测试时适应。
> 🗣️ "What is taste? It's like predicting that other people are going to like this thing. And so we've built this world model over years of entrepreneurship, 10 years of like getting it wrong" —— SPEAKER_02
> 译:什么是品味?就是预测别人会不会喜欢这个东西。我们是靠十年创业、不断做错,才建起这个世界模型的。

### 3. 控制论与无人机:可微=可解,不可微=地狱 / Control theory, the drone example & when physics breaks down `[09:20–17:45]`
**要点(中文)**: 用一个会飞的无人机把强化学习的通用词汇讲清:状态 state、动作/推力 u、转移函数(=动力学=世界模型)、策略 policy、价值函数 value、奖励 reward。当世界模型完美(牛顿力学)且问题可微时,落火箭这类问题能用凸优化/模型预测控制(MPC)闭式求解出最优轨迹。一旦引入"对手无人机"这种你无法反向传播穿透的变量,问题瞬间变成**随机且不可微**,只能退回到"残酷、庞杂"的强化学习(Q-learning、actor-critic 等)。**这条可微/不可微的分界线,决定了一个问题是几行代码解出来,还是要烧海量数据去逼近。**
> 🗣️ "If this is non-differentiable, you cannot do convex optimization, and you cannot do SGD." —— SPEAKER_02
> 译:如果它不可微,你就没法做凸优化,也没法做 SGD(随机梯度下降)。
> 🗣️ "I have to resort to this awful area called reinforcement learning, which is just super brutal and it's sprawling" —— SPEAKER_02
> 译:我只能退回到强化学习这个糟糕的领域——它极其残酷、盘根错节。

### 4. 象棋、围棋与"动作空间"问题 / Chess, Go & the action space problem `[17:45–28:00]`
**要点(中文)**: 关键洞察:一个问题好不好解,不看状态空间多大,而看**动作空间(action space)有多小**。象棋状态空间比宇宙原子数还多,但每步只有约 8 个合法走法,所以可解;围棋 19×19、动作空间 361,已经大很多。要向前看一步,就得对每个动作展开所有可能状态并调用价值函数,组合爆炸。AlphaGo 的做法:自我对弈生成 rollout(赢家所有步 +1、输家 -1),训练一个同时输出"落子概率(策略)"和"当前局面价值"的模型,损失函数几乎就是控制问题的翻版。
> 🗣️ "the cardinality of the action space must be extremely small" —— SPEAKER_02
> 译:(要让这套方法有效,)动作空间的基数必须极其小。

### 5. 蒙特卡洛树搜索为何撞墙 / Monte Carlo tree search & why AlphaGo can't scale `[28:00–34:00]`
**要点(中文)**: MCTS 就是"测试时规划":用 UCB(上置信界)在"利用高价值(Q)"和"探索少访问节点"之间平衡,反复采样构建一棵搜索树。AlphaGo 每走一步要做 800 次 MCTS 模拟、每次调用模型约 30 次 → 每一步约 2.4 万次模型调用,而且这棵昂贵的树走完就扔。**动作空间一放大就彻底失效**:假想把围棋放大到 1000×1000(动作空间约百万),同等深度需要约 6000 万次调用才走一步。加上现实世界规则会变(股市、创投、路况都不像围棋规则固定),这套需要"完美确定性环境"的方法根本搬不进现实。类比很扎心:开车时若 60 秒才转一次方向盘,人早就没了。
> 🗣️ "Imagine that we were driving a car and like, you took like 60 seconds to like turn the steering wheel. Everyone's dead." —— SPEAKER_02
> 译:想象一下开车时你花 60 秒才转一次方向盘——所有人都得死。

### 6. 自动驾驶与机器人:状态/动作空间爆炸 + 数据护城河 / Self-driving, model-free vs model-based & why robotics is hardest `[34:00–48:20]`
**要点(中文)**: 自驾状态空间近乎无限(路况、天气、周围一切像素),但深度学习十年练就的"压缩到隐空间"能力把它压得住;真正难的是**动作空间**(方向盘 0–365° × 力度分档,粗算就 36 万量级)以及**动作数据稀缺**——网上有海量驾驶/第一视角视频,却几乎没有"当时采取了什么动作"的标注,只有 Tesla 靠车队拿到了车队级动作数据。这就是**竞争护城河**。区分两条路线:**model-free**(直接从状态预测动作,行为克隆,像 LLM 的下一 token 预测,快但不够);**model-based**(额外学一个转移函数/世界模型,策略更强但推理慢、要做完整测试时规划)。机器人是最难的:一个六轴臂动作空间约 10^16,遥操作(teleop)数据极贵,还有"跨本体差距"(在 Model X 上训的策略搬到 Model 3 直接失效)。主讲断言:**世界模型是通向 AGI 的必经之路,人脑就是这么干的。**
> 🗣️ "what we don't have is the actions they take." —— SPEAKER_02
> 译:我们(从网络视频里)拿不到的,恰恰是他们当时采取的动作。
> 🗣️ "So this is a huge competitive mode of like, what do people do in that state?" —— SPEAKER_02(此处 "mode" 即 "moat" 护城河)
> 译:"人在那个状态下会怎么做"——这本身就是巨大的竞争护城河。
> 🗣️ "the main thing that I believe is that this is required for AGI." —— SPEAKER_02
> 译:我坚信的核心是:这(世界模型)是实现 AGI 的必要条件。

### 7. 真正跑通的世界模型:合成数据 + JEPA / World models that work & JEPA latent tricks `[48:20–59:00]`
**要点(中文)**: 破局思路(源自 Schmidhuber 的 World Models、Hafner 的 Dreamer 系列到 V4):**先用海量廉价的观察数据训一个"状态→下一状态"的世界模型,再用极少量数据加上 action conditioning,让模型不只是"看世界流过",而是能"影响世界";然后在这个神经模拟器里大量采样、训练策略。** Dreamer 完全靠合成的"想象 rollout"成为第一个在 Minecraft 挖到钻石的工作。现在的最佳实现方式是拿现成的视频扩散/flow matching 模型(Sora 类)当底座,加少量动作条件化即可——Wave 的 Gaia(自驾)、NVIDIA 的 Dream(机器人)都是这套;有论文只用约 500 小时遥操作数据就跑得不错,还能跨本体。**JEPA(联合嵌入预测架构)**的技巧:不在昂贵的像素空间预测下一帧,而在隐空间预测下一个 latent;但朴素做会"塌缩"(模型学会全输出 0),需 VICReg/SigReg 之类正则约束分布。同一思路还能搬到 LLM:用隐空间预测下一 token 的 embedding 当作交叉熵的廉价代理,省掉昂贵的交叉熵头。
> 🗣️ "the policy is so good that it's the first paper to mine diamonds in Minecraft... And it did it all on synthetic data, which is kind of crazy." —— SPEAKER_02
> 译:这个策略强到成为第一个在 Minecraft 里挖到钻石的工作……而且全靠合成数据做到,挺疯狂的。
> 🗣️ "I think they raised $1.5 billion to, to basically run with this idea for self-driving car." —— SPEAKER_02(指 Wave 的 Gaia)
> 译:我记得他们(Wave)融了 15 亿美金,就是用这个思路做自动驾驶。

### 8. 尚未解决的问题与"眯眼测试" / Open problems & does this pass the squint test? `[59:00–74:27]`
**要点(中文)**: 未解难题(每一条都是潜在创业切口):物理信息神经网络(PINs)还不灵,分布外场景(比如"撞向房子")因训练数据几乎全是"正常行驶"而会诡异地"脑补成正常路面";SGD 达不到机器精度,世界模型细节保真度不够;测试时快速自适应(人打网球能瞬间适应对手,不用睡一觉重训);触觉/摩擦系数估计缺失(麻醉双手你连鞋带都系不上)。主讲还认同 Sam Altman 的判断——会出现比 Transformer 更强的架构,因为 Transformer 在时间维度上不做压缩。"眯眼测试":像鸟和飞机,眯着眼看,如今 VLA+策略+测试时规划的组合已经比自回归 LLM 更接近人脑;但主讲抛出一个更深的判断——**"大脑是优化器,不是模型"**,睡眠时海马体的短波涟漪在做某种离线再训练,这是当前架构还完全没有的机制。落到创业:YC 已经看到有公司在这条链的每一环创业(采集第一视角数据、遥操作数据、训世界/动作模型、造新本体、做跨本体适配),2026 是 demo "开始像那么回事"的第一年。
> 🗣️ "i think that the brain is the optimizer not the model" —— SPEAKER_02
> 译:我逐渐得出的结论是——大脑是优化器,而不是模型(它调用模型,但它本身也是那个优化器)。
> 🗣️ "feels like this is the first year where you see demos where you're like okay this actually like kind of is starting to look like it's going somewhere" —— SPEAKER_01
> 译:感觉今年是第一年,你看到那些 demo 会觉得"好,这东西真的开始有点样子了"。

## 🚀 给 AI Agent 创始人的行动项
- [ ] 用 **S / A / R / 转移函数** 把你的 Agent 问题写清楚,第一件事先估**动作空间基数**:如果爆炸,任何靠搜索/规划的方案都别指望能扩展——要么压缩动作空间,要么换 model-free 路线。
- [ ] 明确路线:先上 **model-free(行为克隆/VLA,像下一 token 预测,快、上限低)** 拿到能用的 baseline,还是投入 **model-based(世界模型+测试时规划,强但推理贵)**?别默认追最花哨的。
- [ ] 盘点你的**数据护城河**:你捕获的是"观察",还是"带动作标注的轨迹(state→action)"?观察数据满地都是,能持续采到**动作/决策标注**才是壁垒(Tesla 车队即范式)。
- [ ] 若数据稀缺,复刻 **Dreamer 配方**:用海量廉价观察数据预训世界模型 → 少量数据做 action conditioning → 在"想象 rollout"里训策略 → 少量真实数据微调。底座可直接用现成视频扩散/flow matching 模型。
- [ ] 为 **out-of-distribution / 测试时自适应** 留机制:现实规则会变、会遇到训练集里没有的状态,靠"睡一觉重训"不行,要能靠一两个数据点快速适应(考虑在线估计摩擦系数式的思路)。
- [ ] 把**开放问题当作楔子**:实时规划、高保真物理、跨本体泛化、触觉感知——选一个你能做深的窄切口,而不是笼统地"做个通用 Agent"。

## 🔑 关键术语 / 概念
- **Sample efficiency(样本效率)** — 每多一个样本能提升多少智能;完美状态是 0 样本(靠完美世界模型直接推算)。
- **World model(世界模型)/ 转移函数** — 预测"给定当前状态和动作,下一状态是什么"的模型 s_{t+1} | s_t, a_t;牛顿力学是它的完美特例。
- **Model-free vs Model-based RL** — 前者直接学 策略(状态→动作),无世界模型,快但弱;后者额外学世界模型,可做规划,强但推理慢。
- **VLA(Vision-Language-Action)** — 直接从观测预测下一动作的策略模型,本质是行为克隆,类比 LLM 的下一 token 预测。
- **Action conditioning(动作条件化)** — 在已训好的"状态→下一状态"世界模型上,用少量数据注入动作输入,让模型能"影响"而非只"观看"世界;是省样本的关键。
- **Imaginative / synthetic rollout(想象 rollout)** — 在世界模型这个神经模拟器里生成的合成轨迹,用来训练策略,绕开真实数据稀缺。
- **MCTS(蒙特卡洛树搜索)** — 一种测试时规划算法,用 UCB 平衡利用与探索;动作空间大时调用量指数爆炸,不可扩展。
- **JEPA(Joint-Embedding Predictive Architecture,联合嵌入预测架构)** — 在隐空间而非像素空间做预测的世界建模;需 VICReg/SigReg 防塌缩。
- **Cross-embodiment gap(跨本体差距)** — 在一种机体上训的策略搬到另一种机体(甚至 Model X→Model 3)就失效。
- **PINs(物理信息神经网络)** — 试图把物理定律注入神经网络;讲者认为目前"还不太行"。
- **Test-time planning / adaptation(测试时规划/自适应)** — 推理时现场搜索/规划或快速适应新环境,人脑极强,当前模型很弱。

## 🔖 高价值金句时间戳
- `[00:49]` "the two major problems that we have left to solve is intelligence per watt and intelligence per sample" — 把 AI 前沿问题浓缩成两把标尺,后者(样本效率)是本期全部内容的靶心。
- `[03:39]` "What is taste? It's like predicting that other people are going to like this thing." — 创始人的"品味"其实是脑内世界模型,值得反复咀嚼。
- `[11:54]` "If this is non-differentiable, you cannot do convex optimization, and you cannot do SGD." — 可微/不可微这条线,决定你的问题是闭式解还是要烧数据。
- `[35:16]` "the cardinality of the action space must be extremely small" — 判断一个 RL/规划方案能不能扩展,先看动作空间。
- `[41:41]` "what we don't have is the actions they take." — 一句话点破具身 AI 的数据护城河:缺的不是观察,是动作标注。
- `[44:45]` "the main thing that I believe is that this is required for AGI." — 世界模型不是可选项,是主讲眼中通向 AGI 的必经之路。
- `[70:09]` "i think that the brain is the optimizer not the model" — 全片最深的一句:也许当前架构缺的是"睡眠式离线再优化"这个机制。
- `[72:37]` "this is the first year where you see demos where you're like okay this actually like kind of is starting to look like it's going somewhere" — 时机信号:2026 是具身 demo 开始"像那么回事"的第一年。
