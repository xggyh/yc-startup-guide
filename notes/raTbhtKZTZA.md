# 开源大模型架构横评:GPT-OSS vs Qwen-3 vs DeepSeek / OpenAI vs. Deepseek vs. Qwen: Comparing Open Source LLM Architectures

> **来源**: [OpenAI vs. Deepseek vs. Qwen: Comparing Open Source LLM Architectures](https://www.youtube.com/watch?v=raTbhtKZTZA) · Y Combinator · 2025-08-29 · 时长 12:31
> **讲者**: Ankit Gupta(YC,单人讲解 / SPEAKER_00)
> **一句话定位**: 拆解 GPT-OSS、Qwen-3、DeepSeek V3 三大顶级开源权重模型的架构与训练差异,帮 AI Agent 创始人搞清"选哪个底座、看什么指标、护城河在哪",避免只盯 benchmark 选型。

## 🎯 TL;DR(中文核心要点)
- 三家旗舰开源模型都是 **MoE(混合专家)**,真正决定推理成本的是"激活参数量"而非总参数:GPT-OSS 117B 只激活 5.1B、20B 只激活 3.6B;DeepSeek V3 671B 激活 37B;Qwen-3 235B MoE 用五分之一激活量就能追平同门 dense 模型。
- 它们用的"零件"高度趋同(GQA 注意力、SwiGLU、RoPE、RMSNorm),**却用很不一样的具体做法得到相近的 benchmark 成绩**——所以选型不能只看跑分和上下文长度这类 top-line 数字。
- **长上下文有三条路线**:GPT-OSS 预训练期就用 YARN,"天生"支持 131K;DeepSeek 分阶段微调 32K→128K;Qwen-3 只微调到 32K,推理时再用 YARN 把 RoPE 基频放大 4 倍冲到 128K。路线不同,部署时的稳定性/成本假设也不同。
- **强化学习(RL)可以极度省数据**:Qwen-3 的推理 RL 只用了约 4000 对 query-verifier 就拿到很好的效果——对想做垂直 agent 微调的团队是重要信号,数据"质"往往比"量"关键。
- DeepSeek V3 走的是 **MLA(多头潜在注意力)**,把 KV 压到低维潜空间再缓存,长上下文下比 GQA 更省显存、建模效果也更好——如果你的 agent 是超长上下文场景,注意力机制的选择直接影响 KV cache 成本。
- **真正的护城河是数据工程(dataset engineering)**,而不是公开的架构。各家论文都只披露训练数据的"大方向",这种不可复现性正是它们敢开源权重的底气。
- GPT-OSS 默认以**量化格式**发布(可跑在消费级 GPU/笔记本),但**没有非量化版本**;并做了大量安全对齐后训练,社区正在尝试剥离对齐层探索"原始能力"。
- 讲者反复强调的元方法论:这些论文更像**经验发现(empirical findings)**,几乎没人给"为什么 A 比 B 好"的第一性原理解释——读论文/选模型要看"具体方法",而非结论性跑分。

## 🧭 适合谁 / 什么时候看
- 正在为 AI Agent 产品**选开源底座**、纠结 GPT-OSS / Qwen-3 / DeepSeek 的工程师型创始人。
- 需要判断**自建/微调 vs 直接用**、关心推理成本(激活参数、KV cache、量化、长上下文)的技术决策者。
- 想建立一套"读大模型论文的框架"、不想被 benchmark 和"131K 上下文"这类营销数字带偏的人。
- 注意:这是一期偏**架构科普**的短片,不是创业方法论;适合补技术地图,不适合找融资/GTM 建议。

## 📝 分段精读

### 1. 开场与横评框架 / OpenAI OSS Launch & Comparing Architectures `[00:00–01:46]`
**要点(中文)**: GPT-OSS 是 OpenAI 自 2019 年 GPT-2 以来首个开源权重模型,也是继今年 1 月 DeepSeek R1 之后最受关注的开源发布。核心问题不是"谁跑分高",而是"在架构上它们到底有什么不同"。整期视频以此为主线,横向对比三家旗舰开源模型的设计取舍。
> 🗣️ "OpenAI recently dropped GPT-OSS, its first open weights model since GPT-2 in 2019. It's one of the highest profile open source model launches since DeepSeq R1 made waves back in January. But how does GPT-OSS compare to the other top open source models out there architecturally?" —— Ankit Gupta
> 译:"OpenAI 最近发布了 GPT-OSS——这是它自 2019 年 GPT-2 以来的首个开源权重模型,也是继今年 1 月 DeepSeek R1 引发轰动后,关注度最高的开源发布之一。但从架构上看,GPT-OSS 跟其他顶级开源模型相比究竟如何?"

### 2. GPT-OSS:MoE + 量化默认发布 / GPT OSS Overview & Under The Hood `[01:46–03:25]`
**要点(中文)**: GPT-OSS 是解码器-only 的 MoE,分 120B 和 20B 两档,每个 token 只激活 top-4 专家,做到"大模型收益、小推理成本"。用满现代 LLM 标配:GQA、SwiGLU、RoPE、带 pre-norm 的 RMSNorm;上下文 131K 是在**预训练阶段**就用 YARN 训出来的。它默认以量化格式发布,能跑在消费级 GPU/笔记本,但没有非量化版;并做了大量安全对齐后训练。
> 🗣️ "Each token activates the top four experts, meaning only a portion of the total parameters are used at any given time. This allows for efficient inference without sacrificing the benefits of a larger model." —— Ankit Gupta
> 译:"每个 token 只激活排名前四的专家,意味着任意时刻只用到总参数的一部分。这让你既能高效推理,又不牺牲大模型带来的收益。"
> 🗣️ "Once training was complete, the model was released in a quantized format by default, making it lightweight enough for deployment on modest hardware... However, there's no unquantized version available." —— Ankit Gupta
> 译:"训练完成后,模型默认以量化格式发布,轻到可以部署在普通硬件上……不过,并没有提供非量化版本。"

### 3. Qwen-3:全尺寸家族与三阶段训练 / Qwen-3 Architecture & Training `[03:25–05:12]`
**要点(中文)**: Qwen-3 是三者里唯一同时提供 dense(0.6B–32B 七档)和 MoE(30B、235B)的家族,0.6B 是当代最小的开源权重模型之一。架构与前代相近(GQA/SwiGLU/RoPE/RMSNorm),但用 **QK-Norm** 取代 QKV-bias 来动态归一化 Q/K 向量、稳住注意力分数。数据上用 36T tokens(是 Qwen-2.5 的两倍),分三阶段:通用(30T+、119 种语言)→ 推理(+5T 高质量 STEM/推理/代码)→ 长上下文(扩到 32K+,配合 ABF、YARN、dual-chunk attention)。
> 🗣️ "Qen3 was trained on 36 trillion pre-training tokens, twice as many as the Qen2.5 models." —— Ankit Gupta
> 译:"Qwen-3 用了 36 万亿的预训练 token,是 Qwen-2.5 的两倍。"

### 4. Qwen-3 后训练:思维模式融合与省数据的 RL / Qwen-3 Post-Training & RL `[05:12–06:52]`
**要点(中文)**: Qwen-3 用四步后训练,目标是"让用户控制思考量"+"把大模型能力蒸馏进小模型":长思维链冷启动 → 用 GRPO(DeepSeek 提出的 RL 算法)做推理 RL → **思维模式融合**(推理/非推理合进一个模型,用户可切换,GPT-5 后来也有类似开关)→ 通用 RL(指令遵循、格式、工具调用等)。最惊人的信号是:推理 RL 只用约 4000 对数据就能出好结果。
> 🗣️ "Personally, I think it's fascinating that it only takes 4,000 pairs to get great results." —— Ankit Gupta
> 译:"就我个人而言,只用 4000 对数据就能拿到很好的效果,这一点非常令人着迷。"

### 5. DeepSeek V3 / V3.1 与 MLA 注意力 / DeepSeek V3, V3.1 & MLA `[06:52–09:39]`
**要点(中文)**: DeepSeek V3 是 671B 的纯 MoE(激活 37B),用 FP8 训练大幅降本,为后续 R1 打底。V3.1 在同一 checkpoint 上加了两阶段长上下文训练和"混合思考模式"(一个模型切换重推理/轻推理),并强化了工具调用与 agent 能力。关键区别在注意力:V3 用 **MLA**——把 K/V 压进更小的潜空间再缓存、推理时解压;实现更复杂,但在超长上下文下比 GQA 更省显存、建模更好。
> 🗣️ "So V3 makes use of MLA, which compresses keys and values into a smaller latent space before caching them, then decompresses them during inference... it delivers greater memory savings, and better modeling performance than GQA, especially in huge long context models like this one." —— Ankit Gupta
> 译:"V3 采用 MLA:在缓存前把 key/value 压缩到更小的潜空间,推理时再解压……相比 GQA,它带来更大的显存节省和更好的建模效果,尤其是在这种超大、超长上下文的模型上。"

### 6. 尺寸对比与三种长上下文策略 / Comparing Sizes & Long-Context Strategies `[09:39–11:25]`
**要点(中文)**: 尺寸上 GPT-OSS 居中,Qwen 的 MoE 用五分之一激活量就能追平 dense。长上下文是最有意思的技术分野:GPT-OSS 预训练就带 YARN,"天生"native 支持 131K;DeepSeek 分阶段微调一步步做到 128K;Qwen 只微调到 32K,推理时把 RoPE 基频×4 冲到 128K、省掉额外长上下文训练。三条路线对应不同的部署成本与外推稳定性假设。
> 🗣️ "GPT-OSS is born with long-context ability. DeepSeq is trained into it step by step, and Quen pushes the limits of what a 32,000-train model can do without more long-context training." —— Ankit Gupta
> 译:"GPT-OSS 是'天生'就具备长上下文能力;DeepSeek 是一步步训练出来的;而 Qwen 则是在不做更多长上下文训练的前提下,把一个 32K 训练的模型的极限往外压。"
> 🗣️ "Qen's mixture of experts base models match the dense models' performance with only a fifth as many active parameters." —— Ankit Gupta
> 译:"Qwen 的 MoE 基座模型,只用五分之一的激活参数,就能匹配 dense 模型的性能。"

### 7. 方法论反思与总结:护城河是数据工程 / Reflections & Takeaways `[11:25–12:31]`
**要点(中文)**: 讲者的元观察:这些论文更像"经验发现",各家给出一套好用的工具组合,却几乎没人从第一性原理解释"为什么 MLA 好过 GQA";相同的零件、很不同的做法,却得到相近成绩,这本身很反直觉。RL 又极度省数据。而各家数据集差异非常不透明——**海量的数据工程才是真正难以复现的护城河**。给读者的落地建议:别只盯 benchmark 和上下文长度,去看各家用的"具体方法"。
> 🗣️ "This work is probably a significant aspect of the moat that makes these companies comfortable releasing their models. It's very difficult to replicate what they're releasing." —— Ankit Gupta
> 译:"这些(数据)工作很可能是护城河的重要组成部分,正是它让这些公司敢于放心开源自己的模型——因为别人极难复现他们放出来的东西。"
> 🗣️ "The big takeaway when reading these papers is you shouldn't focus too much on just the benchmark performance or top-line stats like context size. Instead, look at the specific methods that these labs are using to achieve those results." —— Ankit Gupta
> 译:"读这些论文最大的收获应该是:别太纠结跑分或上下文长度这类表面数字,而要去看这些实验室是用什么具体方法达成这些结果的。"
> 🗣️ "A lot of these read as empirical findings. Each lab describes a combination of tools that works well for them, but almost no one gives a first-principles justification of why one tool is better than the other." —— Ankit Gupta
> 译:"这些论文很多读起来像是经验性发现:每家实验室都描述了一套对他们有效的工具组合,却几乎没人从第一性原理去论证为什么某个工具就比另一个好。"

## 🚀 给 AI Agent 创始人的行动项
- [ ] **按"激活参数量"而非总参数估算推理成本**:选底座时把 GPT-OSS(激活 5.1B/3.6B)、Qwen-3 MoE(1/5 激活)、DeepSeek V3(激活 37B)按 tokens/s 与显存实测一遍,别被总参数吓退或迷惑。
- [ ] **长上下文按业务实测,而非信 131K 标称**:分别用 GPT-OSS(原生 YARN)、DeepSeek(分阶段)、Qwen(推理期 YARN×4)在你 agent 的真实长上下文任务上跑外推质量,记录长文召回/幻觉退化点。
- [ ] **超长上下文场景优先评估 MLA 类模型**:若 agent 需要长期记忆/大 KV cache,把 DeepSeek(MLA)与 GQA 系模型做显存与延迟对比,MLA 的 KV 压缩可能直接决定单机能承载的并发。
- [ ] **微调走"少而精"的 RL 路线**:参考 Qwen-3 用约 4000 对 query-verifier 的做法,先构建高质量、可验证(verifier)的小数据集做 GRPO/RL,而不是先堆量;把数据工程当作核心投入。
- [ ] **优先落地量化部署**:GPT-OSS 默认量化可跑消费级 GPU,把"能否在便宜硬件上跑通 agent 主循环"作为选型硬指标,压低单位推理成本。
- [ ] **选型评审看方法不看榜**:内部选型文档强制列出"这个模型用了哪些具体方法(注意力/长上下文/后训练)",禁止仅凭 benchmark 分数拍板。

## 🔑 关键术语 / 概念
- **MoE(Mixture of Experts,混合专家)** — 每个 token 只激活一部分"专家"参数;总参数大但激活参数小,兼顾能力与推理效率。GPT-OSS 每 token 激活 top-4 专家。
- **激活参数 vs 总参数(active vs total parameters)** — 决定实际推理算力/显存的是激活参数;如 V3 是 671B 总、37B 激活。
- **GQA(Grouped Query Attention,分组查询注意力)** — 多个 query 头共享同一组 K/V,降低显存、加速推理,是三家的通用注意力。
- **MLA(Multi-head Latent Attention,多头潜在注意力)** — DeepSeek 的做法,把 K/V 压到低维潜空间再缓存、推理时解压;长上下文下比 GQA 更省显存、建模更好。
- **YARN(Yet Another RoPE eN-extension)** — 通过调整 RoPE 基频扩展上下文外推能力;可用于预训练(GPT-OSS)、分阶段微调(DeepSeek)或推理期直接放大(Qwen ×4)。
- **RoPE / RMSNorm / SwiGLU** — 现代 LLM 标配:旋转位置编码、均方根归一化(带 pre-norm)、门控前馈激活;三家几乎都用。
- **QK-Norm** — Qwen-3 用它取代 QKV-bias,动态归一化 Q/K 向量,稳住注意力分数。
- **思维模式融合(Thinking-Mode Fusion)** — 把"推理/非推理"合进同一模型、用户可切换的后训练技巧;GPT-5 后来也有类似开关。
- **GRPO** — DeepSeek 提出的 RL 算法,Qwen-3 用约 4000 对数据做推理 RL。
- **数据工程护城河(dataset engineering moat)** — 各家最不透明、最难复现的部分,是它们敢开源权重的底气所在。

## 🔖 高价值金句时间戳
- `[05:54]` "Personally, I think it's fascinating that it only takes 4,000 pairs to get great results." — RL 极度省数据:垂直 agent 微调该先做"高质量小数据",而非堆量。
- `[08:16]` "V3 makes use of MLA, which compresses keys and values into a smaller latent space before caching them." — 超长上下文 agent 选型时,注意力机制直接决定 KV cache 显存成本。
- `[09:06]` "Qen's mixture of experts base models match the dense models' performance with only a fifth as many active parameters." — 用激活参数量而非总参数来估推理成本。
- `[10:28]` "GPT-OSS is born with long-context ability. DeepSeq is trained into it step by step, and Quen pushes the limits..." — 长上下文三条路线不同,别只信 131K 标称,要按业务实测外推质量。
- `[11:44]` "This work is probably a significant aspect of the moat that makes these companies comfortable releasing their models." — 真正的护城河是数据工程,不是公开的架构。
- `[11:51]` "You shouldn't focus too much on just the benchmark performance or top-line stats like context size. Instead, look at the specific methods." — 选型看方法不看榜的元原则。
