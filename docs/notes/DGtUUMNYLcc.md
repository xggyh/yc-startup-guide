# 递归:AI 的下一条 Scaling Law / Recursion Is The Next Scaling Law In AI

> **来源**: [Recursion Is The Next Scaling Law In AI](https://www.youtube.com/watch?v=DGtUUMNYLcc) · Y Combinator · 2026-05-01 · 时长 37:53
> **讲者**: 主持 Ankit Gupta(YC,Decoded 节目主持人,SPEAKER_00);嘉宾 Francois Chaubard(YC visiting partner,SPEAKER_01)
> **一句话定位**: 用 HRM / TRM 两篇论文拆解"推理时递归"如何让 700 万参数小模型在特定推理任务上碾压万亿参数 LLM;给 AI Agent 创始人指明"LLM 单次前向传播的硬性能力天花板"在哪,以及"递归 / 潜空间推理"作为效率与能力护城河的技术机会与选型判断。

## 🎯 TL;DR(中文核心要点)
- **LLM 在"不可压缩问题"上有硬天花板**:精确排序、数独、迷宫这类问题无法在单次前向传播里解决。理论下界是比较排序不低于 n log n;Transformer 层数用完就"没步数可算了"——别指望一次 forward pass 解决需要真实多步计算的任务。
- **CoT 和 tool use 只是绕过限制的 hack,天花板是"人类已有知识"**:链式思维在离散 token 空间里递归,工具调用直接调现成函数;两者都无法发现"人类知识集合之外"的新算法(比如只见过冒泡排序时,发现不了归并排序)。
- **递归带来"计算深度"而非"参数深度"**:同一套权重反复调用,可以在小参数量下换取深层计算。HRM(27M 参数,零预训练,仅 1000 个任务)在 ARC Prize 上拿到约 70%,同期 O3 得 0 分。
- **真正管用的两个机制**:①**外层精修循环(outer refinement loop / deep supervision)**是性能的主要来源、可扩展;②**截断式时间反向传播,T=1 就足够**——只回传一步梯度、其余 stop-grad,反直觉但有效,绕开了 RNN 的梯度爆炸/消失。
- **更小 = 更好**:TRM 把 HRM 从 28M 砍到 7M 参数(合并 H/L 网络、只用 1 层 Transformer、加更多递归),ARC Prize 1 反而从 70% 提到 87%。"变大"是充分非必要条件(Melanie Mitchell 的观点)。
- **这些是任务专用模型,不是通用模型**:训练来解数独的模型不会做 ARC,必须在目标任务上重训。它们能"无需 CoT 教师强制"自行发现解法,这是相对 LLM 最独特的能力。
- **最大机会是"缝合"**:LLM 擅长找出色的 embedding / 潜空间表示,但很少在潜空间里真正推理(几乎都过 token 空间);把巨型 LLM 的表示能力 + 小型递归模型的潜空间推理拼起来,是讲者最看好的方向。

## 🧭 适合谁 / 什么时候看
- 想搞清 LLM 推理能力真实边界、评估"递归 / 推理时算力"能否成为技术护城河的 AI Agent 创始人。
- 在做 narrow 推理任务(规划、约束求解、结构化/组合搜索),纠结"自研小模型 vs 直接调巨型 LLM API"的工程型创始人。
- 关注 inference-time scaling / test-time compute 这条前沿主线的技术人。
- **不太适合**:只想拿 GTM / 融资打法的读者——这是一期硬核研究向对谈,商业结论要靠你自己从技术判断里推。

## 📝 分段精读

### 1. 开场与模型基础:RNN vs LLM / Intro & Foundations (RNN vs LLM) `[00:00–02:36]`
**要点(中文)**: 递归(recursion)= 把同一个模型在自身上反复调用,这是 2016 年前后 RNN 时代大家认定通往强能力的路径。RNN 的死穴是"时间反向传播(backprop through time)":展开越多步,梯度越来越噪、出现消失/爆炸,还要存下每一步的激活值(百万上下文就要"百万份大脑副本")。LLM/Transformer 用因果掩码把所有时间步一次性并行前向+反向,避开了梯度和存激活的问题——但代价是放弃了"时间方向的压缩"和"潜空间里的推理"。
> 🗣️ "There is no compression in LLMs. Every single decode that I do, I still have to retain the entire, you know, Shakespeare novel just to like decode a little bit, and in RNNs, you don't have to do that. It's all compressed in this hidden state." —— Francois Chaubard
> 译:LLM 里没有压缩。我每解码一步,都得保留整本莎士比亚全集才能解码这一点点;RNN 不用这样,一切都压缩在一个不断滚动的隐藏状态里。

### 2. 推理的极限与排序类比 / Reasoning Limits & the Sorting Analogy `[02:36–04:22]`
**要点(中文)**: LLM 的根本局限在"一次前向传播能做多少步计算"。以排序为例:即便喂无限的"乱序→有序"样本,模型也无法一次性完成——比较排序理论下界是 n log n,列表长度超过 Transformer 层数,就"没步数可比了"。数独、迷宫、滚动求和都是这类**不可压缩问题**。Ankit 补充经典算法直觉:超过 n log n 的唯一办法是有外部内存(纸带/桶排序),而 LLM 没有内建的外部记忆纸带,于是丢掉了这部分性能空间。
> 🗣️ "we know a theoretical lower bound that for comparison sort, you can't do better than n log n... if I have a list that's 31 characters or elements long, and my transformer is 30, I run out of steps to do comparisons." —— Francois Chaubard
> 译:我们知道比较排序的理论下界是不可能优于 n log n……如果列表有 31 个元素、而我的 Transformer 只有 30 层,我就没有足够的步数去做完这些比较了。
> 🗣️ "because there's no external memory tape in-built into the model, you lose certain performance possibilities in terms of how fast you can go." —— Ankit Gupta
> 译:因为模型没有内建的外部记忆纸带,你就在"能跑多快"上丢掉了某些性能上限。

### 3. HRM:分层推理模型的架构、直觉与结果 / HRM Architecture, Intuition & Results `[04:22–09:46]`
**要点(中文)**: HRM 属于 RNN 血统,受大脑不同频率区域启发做三层递归:低层模块循环 TL 次、高层模块循环 TH 次、外层再做 N 次精修(outer refinement)。同一套权重反复施加,所以叫"递归"。可类比变量作用域:ZL 是低层局部隐藏状态、ZH 是高层。关键结果:仅 **27M 参数、零预训练、仅 1000 个任务**,在 ARC Prize 1/2 拿到 SOTA,约 70%,而同期 O3 得 0 分。关键 trick:不像 Alex Graves 那样对全部递归步 backprop(会被 BPTT 限死),而是借鉴 DEQ(深度平衡模型)——对同一 batch 反复迭代 16 次、每次都打梯度但只回传一步(stop-grad),等于用"隐藏状态的不同记忆态"当成不同的 mini-batch。
> 🗣️ "this got state of the art on ArtPrize 1 and 2, this was only a 27 million parameter model." —— Francois Chaubard(注:口语 "ArtPrize" 即 ARC Prize)
> 译:这在 ARC Prize 1 和 2 上拿到了 SOTA,而它只是一个 2700 万参数的模型。
> 🗣️ "O3 gets zero, literally zero. And this got like something like 70% on ArtPrize 1 at least at the time, which was just a huge breakthrough." —— Francois Chaubard
> 译:O3 得零分,字面意义上的零;而它当时在 ARC Prize 1 上拿到约 70%,这是巨大的突破。

### 4. CoT / tool use 只是 hack + TRM 概览 / CoT & Tool-Use Are Hacks; TRM Overview `[09:46–13:30]`
**要点(中文)**: Francois 明确:CoT 和 tool use 是为了突破 GPT-2 局限而生的两个"作弊"——CoT 可以逐步教会排序、在测试时达到图灵完备;tool use 直接 `call sort()`,连 backprop 都不用。但两者的天花板都是**人类已有知识**:只喂冒泡排序,模型只会冒泡排序,发现不了归并排序(Einstein test:回到 1911 让它重建全部物理学)。而且 LLM 的"进位/carry"必须被 snap 回离散 token 空间,RNN 则留在更高维、更有表达力的连续潜空间。HRM 最该记住的两点:**外层精修循环可扩展、是性能主因**;**截断式 BPTT,T=1 就够**。
> 🗣️ "If you're using hacks to solve this in COT and tool use, you're bounded by the bounds of human knowledge. In the event it's outside the set of human knowledge, then like you're kind of SOL." —— Francois Chaubard
> 译:如果你靠 CoT 和工具调用这些 hack 来解决问题,你就被人类知识的边界锁死了;一旦问题在人类知识集合之外,你基本就没戏了。
> 🗣️ "the number one piece to take away is this outer refinement loop. The outer refinement loop scales." —— Francois Chaubard
> 译:最该记住的第一点就是这个外层精修循环——它是可扩展的。

### 5. 代码精髓:EM 式优化与"记忆态 mini-batch" / Code Essence: EM-style Optimization `[13:30–20:46]`
**要点(中文)**: 训练像一种期望最大化(EM):在输入 X 和上一步 ZH 条件下反复更新局部状态 ZL(try this / try that),再在 ZL 条件下更新 ZH——ZH 是"候选答案",离真答案只差一次 MLP 查表。以数独为例:每步只能根据已知信息填一两格,ZL 做局部试探、ZH 把找到的填进去,逐步补全。核心工程 trick:前面两层递归包在 `no_grad` 里(不回传),只对最后一次 L/H 调用 backprop;梯度清零后**不重置 ZH/ZL**,于是下一轮虽是同一批数据,却落在潜空间不同位置=一个"跨记忆态构造的 mini-batch"。而且训练时递归次数重要、测试时递归次数其实不太重要(训 16 次、测 1 次能拿到约 7/8 的性能)。
> 🗣️ "it actually is able to discover things without being teacher forced via chain of thought." —— Francois Chaubard
> 译:它真正的酷点在于——无需通过链式思维做教师强制,就能自行发现解法。

### 6. HRM vs TRM:删掉 75%,留下魔法 / Comparing HRM & TRM `[20:46–34:45]`
**要点(中文)**: TRM(Alexia 的论文)= "把第一篇删掉 75%、只留魔法"。两处主改动:①把 L 网络和 H 网络**权重共享**合并成一个 `net`,并从 4 层 Transformer 砍到 1 层(在数独上 MLP 甚至打过 attention,但在迷宫上 MLP 得 0——不是层数越深/attention 越强就一定好);②不再只回传一步,而是**回传"一整个潜空间递归循环"**,配合伪不动点迭代,反而更好。结果:模型从 28M 缩到 **7M**,ARC Prize 1 从 70% 提到 **87%**。这印证 Melanie Mitchell:"变大"只是充分非必要条件——递归能换来同样甚至更好的性能。Francois 最兴奋的:如果能同时"做大 + 大量递归 + 摆脱 BPTT 那一步的内存限制",两边的好处叠加会非常猛。
> 🗣️ "truncated back prop through time, T equals one, completely sufficient. And that's very counterintuitive." —— Francois Chaubard
> 译:截断式时间反向传播,T 取 1 就完全够用——这非常反直觉。
> 🗣️ "it's a 28 million parameter model for HRM. Now she brings it down to a 7 million parameter model and it actually gets from 70% to 87% on ArcPrize 1." —— Francois Chaubard
> 译:HRM 是 2800 万参数;她把它降到 700 万参数,ARC Prize 1 反而从 70% 提升到 87%。
> 🗣️ "it is sufficient, not necessary, to go bigger and get better performance." —— Francois Chaubard(转述 Melanie Mitchell)
> 译:"变大"是获得更好性能的充分条件,而非必要条件。

### 7. 大图景:小递归模型 × 巨型 LLM 的缝合 / Big Picture: Combining Both `[34:45–37:53]`
**要点(中文)**: 三条不会消失的主线:递归本身(Schmidhuber 的论点,谷歌的 recursion language models 已有体现);外层精修循环 + T=1 截断 BPTT 这套还远未被充分探索;以及"7M 参数打赢万亿参数训遍全网的模型"这一事实。正确答案是把两边的"神奇"缝在一起——很可能 Gemini 已部分做到。注意:HRM/TRM 是**任务专用**、非通用模型。讲者的判断:LLM 主要在学出色的 embedding / 潜空间表示,但**几乎不在潜空间里推理,总是过 token 空间**;把"LLM 找到的干净语义潜空间" + "在该空间里跑小型递归推理模型"结合,会真正 work。
> 🗣️ "We have these tiny recursive models that are seven million parameters that can solve what a hundred million, a hundred billion, a trillion parameter model can't solve trained on the entire internet and a seven million parameter wins." —— Francois Chaubard
> 译:我们有这些 700 万参数的微型递归模型,能解决亿级、千亿级、万亿级、训遍整个互联网的模型都解不了的问题——700 万参数赢了。
> 🗣️ "The benefit of both these TRMs and these giant models and you actually slam them together, I think that it's just going to take off and it's going to be really huge." —— Francois Chaubard
> 译:把 TRM 和这些巨型模型的好处真正撞到一起,我觉得它会一飞冲天、影响巨大。
> 🗣️ "they're not general purpose models, right? These were task specific models... The model trained to do Sudoku cannot do ArcPrize inherently." —— Ankit Gupta
> 译:它们不是通用模型,而是任务专用模型……训练来解数独的模型天生做不了 ARC。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **给 Agent 画一条"不可压缩问题"红线**:凡是需要真实多步计算/精确算法(约束求解、排序去重、组合搜索、规划)的子任务,不要指望 LLM 一次前向传播搞定——要么显式拆成多步/多轮,要么外接确定性工具或专用求解器。
- [ ] **诚实评估你的价值在"人类知识边界内还是外"**:如果 Agent 的核心价值是复用人类已有解法(绝大多数应用),CoT + tool use 就够,别过度工程化;如果你声称能"发现新东西",要意识到纯 CoT/工具链天花板就是人类知识集合。
- [ ] **对高频、窄域的推理子任务,做一次"自研小模型 vs 调 API"的账**:7M 级任务专用递归模型在单一推理任务上可能又快又便宜又更准,推理成本远低于反复调用前沿 LLM——值得为你最烧钱/最卡准确率的那个子任务算这笔账。
- [ ] **把 test-time compute 当成可调旋钮**:递归/精修步数可按任务难度动态调节(简单任务少递归、难任务多递归),用它在延迟-成本-准确率之间做产品级权衡。
- [ ] **走"LLM 出表示 + 小模型在潜空间推理"的混合架构**:用大模型/编码器拿到干净的语义 embedding,在该潜空间上训练小型递归推理模块,而不是把所有推理都逼回 token 空间——这是讲者点名最看好、且尚未被拥挤的方向。
- [ ] **持续跟踪 recursion / latent reasoning 这条前沿**:HRM、TRM、Google recursion language models、DEQ、adaptive compute time(Alex Graves)是必读起点;这条线一旦"做大 + 递归 + 绕开 BPTT"打通,可能重排能力/成本格局。

## 🔑 关键术语 / 概念
- **Recursion(递归)** — 用同一套权重(不换权重)在自身输出/状态上反复调用,换来"计算深度"而非"参数深度"。
- **RNN / Backprop Through Time(BPTT,时间反向传播)** — RNN 训练需展开所有时间步回传梯度,步数一多就梯度消失/爆炸并要存全部激活,是把 RNN 做大的核心瓶颈。
- **Incompressible problem(不可压缩问题)** — 无法在少于所需步数内解决的问题,如数独、迷宫、精确排序、滚动求和;LLM 单次前向传播天生解不了。
- **HRM(Hierarchical Reasoning Model,分层推理模型)** — 27–28M 参数、三层递归(低层/高层/外层精修)、零预训练即在 ARC Prize 上 SOTA。
- **TRM(Tiny Recursive Model,微型递归模型)** — HRM 的极简后继:权重共享合并 H/L 网络、1 层 Transformer、更多递归、回传一整个递归循环;7M 参数把 ARC Prize 1 做到 87%。
- **Outer refinement loop / Deep supervision(外层精修循环 / 深度监督)** — 反复"提出候选答案→再精修"的最外层循环,被证明是这类模型性能的主要来源、可扩展。
- **Truncated BPTT, T=1(截断式时间反向传播)** — 只回传最后一步(其余 stop-grad)就足够,绕开 BPTT 限制,反直觉但有效。
- **DEQ(Deep Equilibrium Models,深度平衡模型)** — 对同一 batch 反复迭代到近似不动点、只在末端回传梯度的思路,是"记忆态 mini-batch"trick 的理论渊源。
- **ZL / ZH(低层/高层隐藏状态,latent/carry)** — ZL 是不断被覆盖的局部作用域变量,ZH 是"候选潜答案",离真答案只差一次 MLP 映射。
- **Latent space vs token space(潜空间 vs token 空间)** — 连续潜空间维度更高、更有表达力;LLM 的推理几乎总被 snap 回离散 token 空间,损失表达力。
- **ARC Prize** — 抽象推理挑战基准(视频口语常读作 "ArtPrize");衡量样本外抽象推理的硬基准。
- **"充分非必要"(Melanie Mitchell)** — "把模型做大"能提升性能,但只是充分条件、并非唯一路径;递归是另一条路。

## 🔖 高价值金句时间戳
- `[03:29]` "There is no compression in LLMs... I still have to retain the entire Shakespeare novel just to decode a little bit." — 一针见血 LLM 无压缩、无潜空间记忆的代价,解释了为何需要递归。
- `[04:08]` "we know a theoretical lower bound that for comparison sort, you can't do better than n log n." — 把 LLM 的推理天花板落到可证明的算法下界,不是玄学。
- `[19:47]` "you're bounded by the bounds of human knowledge. In the event it's outside the set of human knowledge, then like you're kind of SOL." — CoT/tool use 的根本上限,决定你的 Agent 能不能"创造新东西"。
- `[22:05]` "truncated back prop through time, T equals one, completely sufficient. And that's very counterintuitive." — 最反直觉也最实用的训练 trick,值得工程师亲手复现。
- `[27:20]` "it actually is able to discover things without being teacher forced via chain of thought." — 递归模型相对 LLM 最独特的能力:无 CoT 教师强制的自主发现。
- `[33:24]` "she brings it down to a 7 million parameter model and it actually gets from 70% to 87% on ArcPrize 1." — "更小反而更好"的硬数据,直接冲击"越大越强"的默认叙事。
- `[34:57]` "a seven million parameter wins." — 一句话概括本期最反直觉的事实,提醒创始人重新算参数/成本这笔账。
