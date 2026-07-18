# 每个创始人都该懂的机器学习技术:扩散模型 / The ML Technique Every Founder Should Know

> **来源**: [The ML Technique Every Founder Should Know](https://www.youtube.com/watch?v=dC_3ys349bU) · Y Combinator · 2026-01-22 · 时长 27:10
> **讲者**: Ankit Gupta(YC General Partner,《Decoded》主持人,SPEAKER_00)对话 Francois Chaubard(YC Visiting Partner、前 Focal Systems 创始人、Stanford 在读博士,研究基于扩散的世界模型,SPEAKER_01)
> **一句话定位**: 用 10 行代码讲清"扩散(diffusion)"这一底层框架为何正在吃掉除自回归 LLM 与棋类外的整个 AI——对被"一次一个 token"卡住动作空间的 AI Agent 创始人,这是判断技术押注方向的必修课。

## 🎯 TL;DR(中文核心要点)
- **扩散是一个通用框架,不只是画图**:它能学习任意领域的数据分布 p(data),尤其擅长"高维→高维、且数据量很少"的映射(讲者用 30 张 Gary 的照片举例)。图像只是它的出身,不是它的边界。
- **核心机制极简**:不断给数据加噪声直到变成纯随机噪声,再训练一个模型学会"反向去噪"。就这么简单。
- **flow matching 让它变成 ~10 行代码**:不再走曲折路径,而是直接学"噪声→数据"这条直线上的全局速度(velocity = noise − data),训练循环 5 行代码,数学反而越做越简单——这是 ML 里罕见的"越先进越简单"。
- **模型可插拔**:同一份扩散代码,model 可以是 UNet、Diffusion Transformer、RNN……数据可以是图像、蛋白质、DNA、天气、股价、机器人轨迹,代码完全一样。真正难的是工程规模化,不是数学。
- **"眯眼测试(squint test)"看 AGI**:自回归 LLM 的动作空间只有"一次一个 token、从不回头",而大脑是海量递归、一套学习机制、按概念思考。扩散至少给了大脑在做的两件事——利用随机性、以及"整块地"生成而非逐 token 吐出。
- **扩散已经吃掉几乎整个 AI**:图像、视频、代码、蛋白质(DeepMind 因此拿诺奖)、机器人策略(diffusion policy)、天气预报(GenCast,全球最准)。仅剩两块高地:自回归 LLM 与棋类博弈(AlphaGo/MCTS)。
- **给创始人的两条路**:若你自己训练模型——无论做什么应用都该认真看扩散,哪怕只是拿它学一个 latent space;若你不训练模型——请更新你的先验,这些能力五年涨了千倍,继续"滑向冰球要去的地方"。

## 🧭 适合谁 / 什么时候看
- 正在或准备**自己训练/微调模型**的 AI Agent 创始人:判断该不该把扩散放进训练环路。
- 被自回归 LLM"一次一个 token、无法回头修改"卡住的 Agent/推理系统设计者:想了解 diffusion LLM、并行生成、概念级输出的另一条路线。
- 做**机器人、生命科学、多模态、世界模型**方向的创业者:这些领域的 SOTA 大多已是扩散。
- 想在纷杂研究里建立"技术押注直觉"的非研究型创始人:27 分钟拿到一份"该赌什么会变好"的清单。

## 📝 分段精读

### 1. 开场:为什么聊扩散 / Intro `[00:00–00:33]`
**要点(中文)**: 这是 YC 的《Decoded》栏目,Ankit Gupta 对话 Francois Chaubard。Francois 2012 年起在李飞飞实验室做计算机视觉,创办 Focal Systems 十年后回 Stanford 读博,方向是"基于扩散的世界模型走向 AGI"。两人刚从 NeurIPS 回来,发现扩散在各类非自回归模型里反复出现,于是决定系统拆解它。

### 2. 什么是扩散 / What is diffusion? `[00:33–02:50]`
**要点(中文)**: 扩散是一个底层 ML 框架,只要有数据就能学任意领域的概率分布;它的独门优势是"高维到高维、且在低数据下"仍然有效。机制上就是"加噪—反向去噪":正向加噪很容易,难的是从噪声倒推回真实图像,所以把过程翻转过来,训练一个去噪器(de-noiser)去逆转它。
> 🗣️ "Diffusion is a very fundamental machine learning framework that allows you to learn any p-data, any probability of data for any domain as long as you have the data." —— Francois Chaubard `[00:53]`
> 译:扩散是一个非常底层的机器学习框架,只要你有数据,它就能学习任意领域的任意数据分布 p(data)。
> 🗣️ "The thing where it stands out in particular is mapping from high dimensions to high dimensions, especially in low data regimes." —— Francois Chaubard `[01:16]`
> 译:它特别突出的地方,是做"高维到高维"的映射,尤其是在数据很少的场景下。
> 🗣️ "It's hard to walk backwards and create from noise images of you or Gary. And so then we flip it, and then we try to teach the model to reverse that process. And that's basically it." —— Francois Chaubard `[02:04]`
> 译:从噪声反推出你或 Gary 的图像很难,所以我们把过程翻转过来,教模型去逆转这个过程,基本上就是这样。

### 3. 今天扩散有哪些应用 / Applications today `[02:50–04:06]`
**要点(中文)**: 应用之广令人吃惊。它起源于 2015 年的图像论文,如今早已溢出图像:DeepMind 用同一套流程做蛋白质折叠拿了诺奖;diffusion policy 能开车;还能预测天气。Ankit 补充生命科学里的 DiffDock(小分子与蛋白结合)和新版 AlphaFold 都重度使用扩散。
> 🗣️ "DeepMind just won the Nobel Prize for doing this exact procedure on protein folding. You can drive cars with this, with the diffusion policy paper... You can predict the weather. There's really no limit to the things that this can do." —— Francois Chaubard `[03:13]`
> 译:DeepMind 正是用这套完全相同的流程做蛋白质折叠拿了诺奖;用 diffusion policy 论文能开车;还能预测天气。它能做的事几乎没有上限。

### 4. 关键创新 / Key innovations `[04:06–07:01]`
**要点(中文)**: 2015 年 Sohl-Dickstein 的论文其实已备齐现代扩散的所有关键部件,后续都是在"调参数":噪声调度器怎么加噪、损失函数预测什么(预测原始数据 / 预测所加误差 / 预测速度 velocity / 预测首尾全局速度即 flow matching)。整个社区就是在 FID(Fréchet Inception Distance)这个"古怪指标"上不断爬坡——而且发现:让模型去预测误差比预测原始数据更容易,预测速度更容易,预测全局误差又更容易。架构则从 UNet 演进到 Diffusion Transformer + cross-attention。
> 🗣️ "We just kind of hill climbed on this Farashay inception distance metric... And then predicting the velocity was even easier than that. And then predicting the global error across the entire diffusion schedule is even easier than that." —— Francois Chaubard `[05:32]`
> 译:我们就是在 FID(Fréchet Inception Distance)这个指标上不断爬坡……预测速度比预测误差更容易,而预测整条扩散调度上的全局误差又更容易。
> 🗣️ "The math actually got easier. And the code got smaller, which is actually oppositely true in most of the case in most machine learning." —— Francois Chaubard `[06:22]`
> 译:数学其实变得更简单,代码也变得更短——这跟大多数机器学习里"东西越来越复杂"恰好相反。

### 5. 代码实战:从 KL 散度到 flow matching / Code examples `[07:01–19:25]`
**要点(中文)**: Francois 现场对比两代实现。第一代(Sohl-Dickstein)最难懂的其实是**噪声调度(noise schedule)**:线性加噪会极度不稳定,因为一开始加的相对误差太小、末尾又要一次性摧毁全部结构,正确做法是让"每步引入的相对误差大致恒定",这条累积曲线就是 beta 调度,而真正起作用的权重是 alpha-bar;调度一旦调对,别的自然就 work,但这版 KL 散度损失代码很繁琐,FID 高达 222(现代约 8–10)。第二代 **flow matching**(Meta,Yaron Lipman)则优雅到只有 5–15 行:放弃曲折中间步,直接学"噪声→数据"的全局速度(velocity = noise − data),与时间无关、与数据类型无关、与模型架构无关;测试时就是欧拉法(Euler's method),沿速度方向一步步去噪。一个重要限制:训练用多少步,测试就得用多少步,不能靠"多调用几次"变更好(除非蒸馏)。
> 🗣️ "There is a velocity, a global velocity between the noise and the data, and it's just this direction, and it's just this straight line. And I don't care where you are, go in that line." —— Francois Chaubard `[12:47]`
> 译:在噪声和数据之间存在一个全局速度,就是这个方向、就是这条直线;我不在乎你现在在哪儿,沿着这条线走就行。
> 🗣️ "You basically have like 10, 15 lines of code that is the most powerful machine learning procedure ever." —— Francois Chaubard `[13:16]`
> 译:你基本上用 10 到 15 行代码,就写出了有史以来最强大的机器学习流程。
> 🗣️ "This code here has nothing to do with images. It could be weather data... it could be proteins, it could be DNA, it doesn't really matter. It's all the exact same code." —— Francois Chaubard `[14:51]`
> 译:这段代码跟图像没有任何关系。它可以是天气数据……可以是蛋白质、可以是 DNA,都无所谓,全是完全一样的代码。
> 🗣️ "It's the engineering that's the really hard part there, but a lot of the basic machine learning math is actually quite straightforward." —— Ankit Gupta `[16:09]`
> 译:真正难的是工程,而很多底层的机器学习数学其实相当直白。

### 6. "眯眼测试":扩散与通用智能 / The "squint test" `[19:25–22:27]`
**要点(中文)**: Yann LeCun 说造飞机不必模仿扑翼的蝙蝠;Francois 认同,但反驳道"我们确实需要两只翅膀"——眯起眼睛看莱特兄弟的飞机和一只鸟,你会看到共性。智能可能有多种实现路径,人脑是唯一已知的存在证明。眯眼看自回归 LLM:单一堆叠的 transformer、pre-train/SFT/post-train 三段式之后不再学习、且**一次只吐一个 token、从不回头**;再看大脑:海量递归、一套学习机制贯穿始终、按"概念"思考。扩散虽然过不了完整的眯眼测试,但至少给了大脑在做的两件事:**利用随机性**(神经元本就充满随机),以及**整块地生成/思考概念**而非逐 token 挤出。
> 🗣️ "However, we did need two wings. And you look at the Wright Brothers original plane and you squint and you look at a bird." —— Francois Chaubard `[19:51]`
> 译:但我们确实需要两只翅膀。你眯起眼看莱特兄弟最初的飞机,再看一只鸟——它们是有共性的。
> 🗣️ "It's action space is one." / "Is one token at a time." —— Ankit Gupta & Francois Chaubard `[21:36]`
> 译:它的动作空间是 1。/ 就是一次一个 token。
> 🗣️ "Randomness is good. And what is diffusion doing? It's leveraging randomness... The other one is this emission of one thing at a time versus thinking in concepts." —— Francois Chaubard `[21:37]`
> 译:随机性是好东西。扩散在做什么?它在利用随机性……另一件事,是"一次吐一样东西"与"按概念思考"之间的差别。

### 7. 扩散还渗透到哪些地方 / Other areas diffusion is widely accessible `[22:27–24:49]`
**要点(中文)**: 除了大家熟知的 Midjourney/Sora/VO/Flux/SD3 图像与视频,扩散正在写代码(diffusion LLM 是本届 NeurIPS 最热话题之一,含连续型与离散型)、造蛋白质、跑机器人策略(diffusion policy,可能是最大落地之一,"机器人真的动起来了")、做天气预报(GenCast,全球最准)。Francois 的判断:扩散已经吃掉几乎整个 AI,只剩两块高地——自回归 LLM 仍占优,以及 AlphaGo 式棋类博弈仍是 MCTS 的天下。
> 🗣️ "Diffusion has eaten all of AI except two. AR LLMs still are outperforming and gameplay and things like AlphaGo. And so MCTS is still state-of-the-art for those types of things." —— Francois Chaubard `[24:30]`
> 译:扩散已经吃掉了整个 AI,只剩两块:自回归 LLM 仍然更强,还有 AlphaGo 这类棋类博弈——MCTS 在这些任务上仍是 SOTA。

### 8. 给研究者与创始人的落点 / Outro `[24:49–27:10]`
**要点(中文)**: 分两类人。**如果你训练模型**:无论做什么应用都该认真研究扩散,哪怕只是用它学一个能拿来再训练的 latent space,没有理由不把它当作训练环路的核心部件之一。**如果你不训练模型**:请更新先验——五年里图像生成变好了约千倍,答案就是"scale it up",需要钱、时间和数据但都是可解问题;而且扩散的核心流程本身还在变得更简单更好用。策略上就是"滑向冰球要去的地方":押注机器人会进家庭、蛋白质折叠会更好并延伸到 DNA/代谢组学。Ankit 收尾:这会重新定义整个经济。
> 🗣️ "If you're in the business of training models, I would seriously look at diffusion. I don't care what your application is." —— Francois Chaubard `[25:11]`
> 译:如果你是在训练模型的,我会强烈建议你认真研究扩散——我不管你的应用是什么。
> 🗣️ "In the case of people who are not training models, I would just update your prior on how good these things are getting." —— Francois Chaubard `[25:35]`
> 译:对于不训练模型的人,我只想说:请更新你对"这些东西正变得多好"的先验判断。
> 🗣️ "Skate to where the puck's going to go... Bet that the protein folding is only going to get better and now we're going to apply that to DNA." —— Francois Chaubard `[26:05]`
> 译:滑向冰球将要到达的地方……押注蛋白质折叠只会越来越好,并且我们要把它用到 DNA 上。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **重估你的"动作空间"瓶颈**:如果你的 Agent 建在自回归 LLM 上,记住它本质是"一次一个 token、无法回头"。评估在规划/结构化输出/长程推理环节引入 diffusion LLM 或并行/概念级生成,是否能突破逐 token 的动作空间限制。
- [ ] **按"数据结构"而非"惯性"选技术**:只要你的问题是"高维→高维、且高质量数据稀缺"(机器人轨迹、蛋白/分子、多模态状态),就把扩散/flow matching 列为候选,而不是默认套 transformer 自回归。
- [ ] **先跑一版 flow matching 基线**:它只要 ~10–15 行核心代码,model 可插拔。用你自己的领域数据(哪怕几十个样本 + 数据增强)做个最小验证,确认扩散是否比现有方案更省数据。
- [ ] **若你训练/微调模型,至少用扩散学一个 latent space**:即便最终不用扩散做生成,一个好的隐空间也能喂给下游训练,这是 Francois 明确给出的"最低门槛"用法。
- [ ] **做机器人/具身或生命科学 Agent 的,盯紧 diffusion policy 与 GenCast 路线**:这是当前该方向真正 work 的 SOTA,别在自回归上重复造轮子。
- [ ] **把"滑向冰球去处"写进技术路线图**:显式假设"扩散核心会更简单、能力五年再涨一个量级",据此选择在成本/时间可解、但当下还没完全 work 的赛道提前卡位。

## 🔑 关键术语 / 概念
- **Diffusion(扩散)** — 通过"不断加噪声再训练模型反向去噪"来学习任意数据分布的框架;擅长高维、低数据场景。
- **p(data) / p-data** — 数据的真实概率分布,扩散模型要学的目标。
- **Noise schedule / beta schedule(噪声调度)** — 每一步加多少噪声的安排;讲者认为这是扩散里最难懂的部分,目标是让每步引入的相对误差大致恒定(累积成 alpha-bar 权重曲线)。
- **Flow matching(流匹配)** — Meta(Yaron Lipman)提出的简化范式:直接学"噪声→数据"的全局直线速度(velocity = noise − data),训练循环仅约 5 行代码,与时间/数据类型无关。
- **Velocity(速度)** — 从噪声指向数据的方向向量;flow matching 让模型直接预测它,测试时用欧拉法(Euler's method)沿速度迭代去噪。
- **FID(Fréchet Inception Distance)** — 衡量生成图像质量的指标,越低越好;整个社区靠在它上面"爬坡"迭代,现代约 8–10,早期实现高达 222。
- **Diffusion Transformer / cross-attention** — 取代早期 UNet 的现代扩散架构;架构与是否用 flow matching 相互独立。
- **Diffusion policy** — 把扩散用于机器人动作策略,被讲者视为最大落地方向之一。
- **Squint test(眯眼测试)** — 用"眯眼看相似性"的直觉判断某方案是否抓住了通向智能的必要结构(类比莱特飞机与鸟都需要两只翅膀)。
- **AR LLM / MCTS** — 自回归大语言模型与蒙特卡洛树搜索,是扩散尚未攻下的两块 SOTA 高地(棋类如 AlphaGo)。

## 🔖 高价值金句时间戳
- `[01:16]` "The thing where it stands out in particular is mapping from high dimensions to high dimensions, especially in low data regimes." — 一句话定位扩散的独门优势:高维映射 + 数据稀缺,这正是很多 Agent 垂直场景的处境。
- `[06:22]` "The math actually got easier. And the code got smaller." — 罕见的"越先进越简单",降低了非研究型创始人上手门槛。
- `[14:51]` "This code here has nothing to do with images... it could be proteins, it could be DNA, it doesn't really matter. It's all the exact same code." — 说明扩散是可跨领域复用的通用引擎,选它等于选一套可迁移的技术底座。
- `[16:09]` "It's the engineering that's the really hard part there, but a lot of the basic machine learning math is actually quite straightforward." — 创业护城河更多在工程与规模化,而非数学本身。
- `[21:36]` "It's action space is one." / "Is one token at a time." — 一针见血指出自回归 Agent 的根本瓶颈,值得每个 Agent 创始人记住。
- `[24:30]` "Diffusion has eaten all of AI except two." — 用一句话画出技术版图:只剩自回归 LLM 与棋类两块高地,其余都值得押扩散。
- `[26:05]` "Skate to where the puck's going to go." — 创业押注的心法:赌能力会持续变好的方向,而不是当下的静态快照。
