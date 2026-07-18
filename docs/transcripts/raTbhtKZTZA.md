# 全文转录 · 开源大模型架构横评:GPT-OSS vs Qwen-3 vs DeepSeek

> ▶ [YouTube](https://www.youtube.com/watch?v=raTbhtKZTZA) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/raTbhtKZTZA.md) &nbsp;·&nbsp; OpenAI vs. Deepseek vs. Qwen: Comparing Open Source LLM Architectures

> 中英对照 · 每段英文原文下附中文翻译

[00:00] OpenAI recently dropped GPT-OSS, its first open weights model since GPT-2 in 2019. It's one of the highest profile open source model launches since DeepSeq R1 made waves back in January. But how does GPT-OSS compare to the other top open source models out there architecturally? Let's find out.

> OpenAI 最近发布了 GPT-OSS,这是它自 2019 年 GPT-2 以来的首个开放权重模型。这是自今年一月 DeepSeek R1 引起轰动以来,业界最受瞩目的开源模型发布之一。但 GPT-OSS 在架构上与其他顶尖开源模型相比究竟如何?让我们一探究竟。

[00:14] GPT-OSS is one of OpenAI's most anticipated recent launches, a large fully open weights model from one of the leading American AI labs. Let's take a closer look at the paper to find out how it was actually engineered and trained. GPT-OSS is a mixture of experts model available in two sizes, 120 billion parameters and 20 billion parameters. Each token activates the top four experts, meaning only a portion of the total parameters are used at any given time. This allows for efficient inference without sacrificing the benefits of a larger model.

> GPT-OSS 是 OpenAI 近期最受期待的发布之一,是这家美国顶尖 AI 实验室推出的一款大型、完全开放权重的模型。让我们仔细研读论文,了解它究竟是如何设计和训练的。GPT-OSS 是一款混合专家(MoE)模型,提供两种规模:1200 亿参数和 200 亿参数。每个 token 会激活排名前四的专家,这意味着任意时刻只使用总参数的一部分。这使得它能够在不牺牲大模型优势的情况下实现高效推理。

[00:50] Trained as a decoder-only transformer, GPT-OSS incorporates plenty of features typical to modern LLMs. This includes grouped query attention, a modified attention mechanism that lets multiple query heads share the same key value pairs to reduce memory use and speed up inference. It also incorporates a number of other features, such as the ability of the RMS norm to support longer contacts.

> GPT-OSS 作为一款仅解码器(decoder-only)的 Transformer 进行训练,融合了许多现代大语言模型的典型特性。其中包括分组查询注意力(grouped query attention),这是一种改进的注意力机制,让多个查询头共享同一组键值对,以减少内存占用并加快推理速度。它还整合了其他一些特性,例如借助 RMS norm 来支持更长的上下文。

[01:06] This includes SWEGLU activations in the feed-forward network layers, which allow for more nuanced transformations than simpler activations like RELU, as well as Rotary Positional Impeddings, or ROPE, which encode token position directly into the attention mechanism to support longer contacts. Finally, the model also makes use of RMS norm with pre-normalization, a normalization method that scales inputs by their root-mean-square for more stable training. One standout capability of the model is its 131,000 token contacts window, which it achieves by applying yarn scaling during pre-training. We'll touch on what this means a little later.

> 这些特性包括前馈网络层中的 SwiGLU 激活函数,相比 ReLU 等更简单的激活函数,它能实现更精细的变换;还有旋转位置编码(Rotary Positional Embeddings,即 RoPE),它将 token 的位置信息直接编码进注意力机制,以支持更长的上下文。最后,该模型还采用了带预归一化的 RMS norm,这是一种通过输入的均方根来缩放输入的归一化方法,可让训练更加稳定。该模型的一大突出能力是它拥有 131,000 个 token 的上下文窗口,这是通过在预训练阶段应用 YARN 缩放实现的。稍后我们会谈到这意味着什么。

[01:40] For GPT-OSS, OpenAI makes use of their open-source O200K Harmony Tokenizer. This byte-parent coding tokenizer has over 200,000 tokens and builds on the O200K tokenizer used in models like GPT-4O.

> 对于 GPT-OSS,OpenAI 使用了他们开源的 O200K Harmony 分词器。这款基于字节对编码(BPE)的分词器拥有超过 20 万个 token,并在 GPT-4o 等模型所使用的 O200K 分词器基础上构建。

[01:54] As for the dataset GPT-OSS was trained on, OpenAI has only disclosed the broad strokes. The model was trained on a text-only corpus in the trillions of tokens with a focus on STEM, coding, and general knowledge. All content was filtered out for safety, but beyond that, there's little else known publicly. Once training was complete, the model was released in a quantized format by default, making it lightweight enough for deployment on modest hardware. This allows it to be run on consumer-grade GPUs, laptops, or other resource-limited hardware.

> 至于 GPT-OSS 训练所用的数据集,OpenAI 只披露了大致情况。该模型是在一个仅含文本、规模达数万亿 token 的语料库上训练的,重点涵盖 STEM、编程和通用知识。所有内容都经过了安全过滤,但除此之外,公开信息几乎寥寥。训练完成后,该模型默认以量化格式发布,使其足够轻量,可以部署在配置一般的硬件上。这使它能够在消费级 GPU、笔记本电脑或其他资源受限的硬件上运行。

[02:20] However, there's no unquantized version available. GPT-OSS also underwent substantial post-training for safety and alignment, shaping its default behavior for more controlled outputs. It's worth noting that some in the open-source community are experimenting with reducing or removing these layers in order to explore the raw model's capabilities.

> 不过,目前并没有提供未量化的版本。GPT-OSS 还经过了大量的后训练(post-training)以实现安全性和对齐,从而塑造其默认行为,使输出更加可控。值得注意的是,开源社区中已有一些人在尝试削弱或移除这些层,以探索原始模型本身的能力。

[02:37] In the broader landscape of open-source AI, GPT-OSS arrives as a fully equipped, long-context model ready for immediate use. As impressive as it is, however, it's just one of several models in a rapidly expanding field of open-source LLMs.

> 在更广阔的开源 AI 版图中,GPT-OSS 是一款功能齐备、支持长上下文、可即刻投入使用的模型。然而,尽管它令人印象深刻,它也只是这个快速扩张的开源大语言模型领域中的多款模型之一。

[02:50] QEM3, the newest family of models developed by Alibaba Cloud, dropped this past April to considerable height, with benchmark scores that rivaled those of leading open-source-based models like DeepSeq v3 or Llama 4. The QEM3 family includes both Dense models, which activate all of their parameters for each query, and Mixture of Expert models, which only activate a small subset of their parameters for each query. The Dense models come in seven different size classes, including a 0.6 billion parameter model, one of the smallest current-generation open-weight models around, while the MOE models come in two different size classes.

> Qwen3 是阿里云开发的最新一代模型家族,于今年四月发布,备受瞩目,其基准测试成绩可与 DeepSeek V3 或 Llama 4 等领先的开源基座模型相媲美。Qwen3 家族既包括稠密(Dense)模型——对每个查询都激活全部参数,也包括混合专家(MoE)模型——对每个查询只激活一小部分参数。稠密模型分为七种不同的规模等级,其中包括一个 6 亿参数的模型,是当前一代开放权重模型中最小的模型之一;而 MoE 模型则分为两种不同的规模等级。

[03:22] Architecturally, QEM3 Dense models are very similar to the QEM2.5 models Alibaba's previous releases. Like QEM2.5 and GPT-OSS, QEM3 incorporates features like group query attention, SuiGlu, Rope, and RMS Norm. QEM3's sparse models share the same fundamental architecture as its Dense models, but add a mixture of experts layer, with 128 total experts, of which 8 are activated per token. All QEM3 models also use the same tokenizer used in previous QEM models, which implements byte-level, byte-parent codings that allow it to handle any text or symbol without special preprocessing, unlike word or character-based tokenizers.

> 在架构上,Qwen3 的稠密模型与阿里此前发布的 Qwen2.5 模型非常相似。与 Qwen2.5 和 GPT-OSS 一样,Qwen3 也融合了分组查询注意力、SwiGLU、RoPE 和 RMS Norm 等特性。Qwen3 的稀疏模型与其稠密模型共享相同的基础架构,但增加了一个混合专家层,共有 128 个专家,每个 token 激活其中的 8 个。所有 Qwen3 模型还使用了与以往 Qwen 模型相同的分词器,它采用字节级的字节对编码,使其无需特殊预处理即可处理任何文本或符号,这一点不同于基于词或字符的分词器。

[03:54] One of the main things that sets QEM3 apart from previous QEM models is the way it controls the scale of the key query and value projections to keep attention scores stable and consistent. The QEM3 models also use the same tokenizer used in previous QEM models, which implements byte-blur, byte-coding, and byte-coding to keep attention scores stable at scale. It replaces QKV bias, a static offset that shifts KQ view projections in previous models, with QKNorm, a normalization step that dynamically rescales that query and key vectors to maintain constant magnitudes. Dataset-wise, QEM3 was trained on 36 trillion pre-training tokens, twice as many as the QEM2.5 models.

> Qwen3 区别于以往 Qwen 模型的一个主要之处,在于它控制键、查询和值投影规模的方式,以保持注意力分数的稳定与一致。Qwen3 模型也使用了与以往 Qwen 模型相同的分词器,它采用字节级编码,以在大规模下保持注意力分数的稳定。它用 QK-Norm 取代了 QKV bias——后者是以往模型中用于偏移 KQ 投影的静态偏置量;QK-Norm 是一个归一化步骤,能动态地重新缩放查询和键向量,以保持其幅值恒定。在数据集方面,Qwen3 是在 36 万亿个预训练 token 上训练的,是 Qwen2.5 模型的两倍。

[04:23] In addition to pulling data from multilingual texts, STEM, encoding sources, and reasoning tasks, QEM3 also uses QEM2.5 models to generate trillions of tokens of value. QEM3's pre-training occurred in three stages. In stage one, the general stage, models were trained on over 30 trillion tokens covering 119 languages at a sequence length of 4096 tokens. In stage two, the reasoning stage, models were trained on an additional 5 trillion higher-quality tokens featuring more STEM, reasoning, and coding problems. And in stage three, which the QEM team calls the long context stage, context length was extended to over 32,000 tokens, using a bunch of clever algorithmic optimizations. Including ABF, a technique to adjust rope so positional signals remain accurate over much longer sequences, yarn to further scale for longer inputs, and dual-chunk attention to process sequences efficiently. Together, all of these optimizations allow the model to reason over much longer inputs at inference.

> 除了从多语言文本、STEM、编程来源和推理任务中获取数据外,Qwen3 还利用 Qwen2.5 模型生成了数万亿 token 的有价值数据。Qwen3 的预训练分三个阶段进行。第一阶段是通用阶段,模型在超过 30 万亿个 token 上训练,涵盖 119 种语言,序列长度为 4096 个 token。第二阶段是推理阶段,模型又在额外 5 万亿个更高质量的 token 上训练,这些数据包含更多 STEM、推理和编程问题。第三阶段被 Qwen 团队称为长上下文阶段,上下文长度被扩展到超过 32,000 个 token,并运用了一系列巧妙的算法优化。这些优化包括 ABF——一种调整 RoPE 的技术,使位置信号在更长序列上仍保持准确;YARN——用于进一步扩展到更长的输入;以及双块注意力(dual-chunk attention)——用于高效处理序列。所有这些优化共同作用,使模型在推理时能够处理长得多的输入。

[05:17] Finally, QEM3 uses a four-step post-training pipeline with two goals, giving users more control over how much reasoning to use for a given query, and letting them efficiently distill larger model capabilities into smaller models. The first step in the post-training pipeline is a long-term process. This is a long, chain-of-thought, cold-start stage, which involves feeding a model a curated dataset of challenging reasoning problems from math, logic, and STEM with verifiable reference answers, and then filtering outputs to ensure quality.

> 最后,Qwen3 采用了一套四步的后训练流程,有两个目标:让用户能更好地控制对某个查询使用多少推理,以及让开发者高效地将大模型的能力蒸馏到小模型中。后训练流程的第一步是一个较长的过程。这是一个长链式思维(chain-of-thought)冷启动阶段,做法是向模型输入一个精心整理的数据集,内含来自数学、逻辑和 STEM、且带有可验证参考答案的高难度推理问题,然后对输出进行过滤以确保质量。

[05:43] This is followed by a reasoning RL stage using GRPO, an RL algorithm originally developed by deep-seek researchers, on roughly 4,000 query-verifier pairs to strengthen complex problem-solving. Personally, I think it's fascinating that it only takes 4,000 pairs to get great results.

> 接下来是一个推理强化学习(RL)阶段,使用 GRPO——一种最初由 DeepSeek 研究人员开发的强化学习算法——在大约 4,000 个"查询-验证器"对上进行训练,以增强复杂问题的求解能力。就我个人而言,我觉得非常有意思的是,仅需 4,000 对数据就能取得出色的效果。

[05:58] The third step in the post-training pipeline, thinking-mode fusion. Is a key QEM3 innovation that integrates reasoning and non-reasoning into a single model, letting users switch modes without changing models. Essentially, what developers did in this step was fine-tune the model on a mix of thinking data, which includes intermediate reasoning steps, and non-thinking data, which omits them, and then build a chat interface to let users toggle modes.

> 后训练流程的第三步是思维模式融合(thinking-mode fusion)。这是 Qwen3 的一项关键创新,它将推理和非推理整合到同一个模型中,让用户无需切换模型即可切换模式。本质上,开发者在这一步所做的,是用混合数据对模型进行微调——既有包含中间推理步骤的"思考"数据,也有省略这些步骤的"非思考"数据——然后构建一个聊天界面,让用户可以切换模式。

[06:19] Though this was unique to QEM when the model first launched, GPT-5 now features a similar toggle. The final step, general RL, broadens capabilities in instruction following, formatting, preference alignment, tool use, and specialized scenarios. QEM3's developers then use strong-to-weak distillation, which allows for the training of smaller models from larger ones.

> 虽然在该模型刚发布时,这还是 Qwen 独有的功能,但如今 GPT-5 也具备了类似的切换开关。最后一步是通用强化学习,它拓展了模型在指令遵循、格式化、偏好对齐、工具使用和专门场景方面的能力。Qwen3 的开发者随后采用强到弱的蒸馏方法,从而能够用大模型来训练小模型。

[06:38] All in all, QEM3's performance is very impressive, especially given its relatively small size. But just months earlier, a different model had already raised the stakes in open-source. Released in December of last year, deep-seek's V3 model was one of the most ambitious open-source LLMs to come out of a major lab in recent years. A chatbot developed in China. It's called deep-seek.

> 总的来说,Qwen3 的表现非常令人印象深刻,尤其考虑到它相对较小的规模。但就在几个月前,另一款模型已经提高了开源领域的门槛。去年十二月发布的 DeepSeek V3 模型,是近年来出自主流实验室的最具雄心的开源大语言模型之一。这是一款在中国开发的聊天机器人,名叫 DeepSeek。

[06:57] Deep-seek is such a fundamental change to the economics of what's going on. At 671 billion parameters, it's a massive, general-purpose-based model, designed for efficiency as much as capability, laying the groundwork for the reasoning-focused R1 model that would follow.

> DeepSeek 从根本上改变了整个领域的经济格局。它拥有 6710 亿参数,是一款庞大的通用基座模型,其设计在追求能力的同时也同样注重效率,为随后专注推理的 R1 模型奠定了基础。

[07:16] We're not going to get into a ton of detail about V3's architecture or training pipeline here, because we put out a comprehensive deep dive into it back in February. But high-level, the thing to know about V3 is that it's a mixture of experts' model, with several hardware and algorithmic optimizations. It's relatively an 8-bit, rather than 16 or 32-bit, a huge unlock for cutting training costs.

> 这里我们不会深入探讨 V3 的架构或训练流程的大量细节,因为我们早在二月份就已经发布了一期对它的全面深度解析。但从宏观来看,关于 V3 需要知道的是,它是一款混合专家模型,采用了多项硬件和算法上的优化。它相对采用了 8 位精度,而非 16 位或 32 位,这对削减训练成本是一个巨大的突破。

[07:36] And just recently, deep-seek pushed V3 even further with an updated version. The newly released V3.1 builds directly on the original V3-based checkpoint, extending it with a two-phase long-context training approach and adding a hybrid thinking mode that lets the same model switch between reasoning-heavy and lightweight inference. It also improves tool use and agent performance, thanks to a more advanced post-training. In practice, this means V3.1 keeps the same core R1 model. The V3.1 model is the same as the V3.2 model, but the V3.1 model is different. The V3.1 model is the same as the V3.2 model. The V3.1 model is the same as the V3.2 model. It uses the same core architecture as V3, but delivers stronger reasoning, smarter tool use, and greater performance.

> 而就在最近,DeepSeek 又通过一个更新版本将 V3 进一步向前推进。新发布的 V3.1 直接在最初的 V3 基座检查点上构建,通过一种两阶段的长上下文训练方法对其进行扩展,并加入了混合思维模式,让同一个模型能够在重推理和轻量推理之间切换。得益于更先进的后训练,它还改进了工具使用和智能体(agent)性能。在实践中,这意味着 V3.1 保留了相同的核心 R1 模型。V3.1 模型与 V3.2 模型相同,但 V3.1 模型有所不同。V3.1 模型与 V3.2 模型相同。V3.1 模型与 V3.2 模型相同。它使用与 V3 相同的核心架构,但提供了更强的推理能力、更智能的工具使用和更出色的性能。

[08:07] One thing that sets V3 apart is that it uses different attention mechanisms than GPT-OSS and QEM3. In modern LLMs, a lot of the compute and memory is tied up in the kv-cache. So V3 makes use of MLA, which compresses keys and values into a smaller latent space before caching them, then decompresses them during inference. Although MLA is a bit more complex to implement, the previous deep-seek V2 paper found it delivers greater memory savings, and better modeling performance than GQA, especially in huge long context models like this one. And that's just one of several areas where DeepSeq V3 takes a different path.

> V3 的一个独特之处在于,它采用了与 GPT-OSS 和 Qwen3 不同的注意力机制。在现代大语言模型中,大量的算力和内存都被 KV 缓存所占用。因此 V3 采用了 MLA,它在缓存键和值之前先将其压缩到一个更小的潜在空间中,然后在推理时再解压缩。虽然 MLA 的实现要稍微复杂一些,但此前的 DeepSeek V2 论文发现,相比 GQA,它能带来更大的内存节省和更好的建模性能,尤其是在像这样庞大的长上下文模型中。而这只是 DeepSeek V3 走出不同路径的若干方面之一。

[08:39] With all that in mind, let's take a step back. From V3 to Qen to GPT-OSS, how should we think about, at a high level, the differences between these models? One big difference is size. The Qen3 model family is the only one of the three to offer both dense and mixture of expert variants, with dense models from 0.6 billion to 32 billion parameters and a mixture of experts lineup that includes a 30 billion parameter model and a 235 billion parameter model. Notably, Qen's mixture of experts base models match the dense models' performance with only a fifth as many active parameters.

> 记住这一切之后,让我们退一步来看。从 V3 到 Qwen 再到 GPT-OSS,我们在宏观层面上应该如何看待这些模型之间的差异?一个重大差异是规模。Qwen3 模型家族是这三者中唯一同时提供稠密和混合专家两种变体的,其稠密模型从 6 亿到 320 亿参数不等,而混合专家系列则包括一个 300 亿参数的模型和一个 2350 亿参数的模型。值得注意的是,Qwen 的混合专家基座模型仅用五分之一的激活参数,就达到了与稠密模型相当的性能。

[09:08] On the other hand, DeepSeq V3 only comes in a mixture of experts architecture with 671 billion parameters, of which 37 billion are activated for a given token prediction, so considerably larger than even the biggest Qen3 model. GPT-OSS sits in the middle. It offers two MOE models, one with 117 billion parameters, of which 5.1 billion are activated for a given token, and a smaller one with 21 billion parameters, of which 3.6 billion are activated for a given token.

> 另一方面,DeepSeek V3 只提供混合专家架构,拥有 6710 亿参数,其中 370 亿在单次 token 预测中被激活,因此即便与最大的 Qwen3 模型相比也要大得多。GPT-OSS 则处于中间位置。它提供两款 MoE 模型,一款拥有 1170 亿参数,其中 51 亿在单次 token 中被激活;另一款较小,拥有 210 亿参数,其中 36 亿在单次 token 中被激活。

[09:33] One of the most interesting technical differences lies in how each model extends its context length. YARN, short for Yet Another Rope Extension, is a technique for stretching the model's rotary positional embeddings so that it can handle far longer sequences than it was originally trained on. Normally, rope starts to break down when you feed it more tokens than its base frequency was set for. But YARN tweaks that frequency so the same embedding space covers much more ground.

> 最有意思的技术差异之一,在于每款模型如何扩展其上下文长度。YARN 是 "Yet Another Rope Extension"(又一种 RoPE 扩展)的缩写,是一种拉伸模型旋转位置编码的技术,使其能够处理远超最初训练长度的序列。通常情况下,当你输入的 token 数量超过 RoPE 基频所设定的范围时,RoPE 就会开始失效。但 YARN 会调整这一频率,使同样的编码空间能覆盖大得多的范围。

[09:55] What's interesting is how the three models here use it differently. GPT-OSS applies YARN right from pre-training, so its weights have learned to work natively with 131,000 token contexts. DeepSeq takes a staged approach, fine-tuning after pre-training to first reach 32,000 tokens, then further training to achieve 128,000. Quen also fine-tunes to 32,000, but skips that additional retraining step. Instead, at inference time, they apply YARN scaling again, increasing the rope base frequency by a factor of four to reach 128,000 tokens without extra retraining.

> 有意思的是,这里的三款模型对它的运用方式各不相同。GPT-OSS 从预训练阶段就直接应用 YARN,因此它的权重从一开始就学会了原生地处理 131,000 个 token 的上下文。DeepSeek 采取分阶段的方法,在预训练之后进行微调,先达到 32,000 个 token,再进一步训练达到 128,000 个。Qwen 同样微调到 32,000 个 token,但跳过了那个额外的再训练步骤。取而代之的是,在推理时它们再次应用 YARN 缩放,将 RoPE 基频提高四倍,从而无需额外再训练即可达到 128,000 个 token。

[10:27] In other words, GPT-OSS is born with long-context ability. DeepSeq is trained into it step by step, and Quen pushes the limits of what a 32,000-train model can do without more long-context training.

> 换句话说,GPT-OSS 天生就具备长上下文能力。DeepSeek 是一步步训练获得这种能力的,而 Qwen 则在不进行更多长上下文训练的情况下,挖掘一个以 32,000 上下文训练出来的模型所能达到的极限。

[10:38] Personally, I think one of the most interesting things about these papers and the state of the art in deep learning more generally is that a lot of these read as empirical findings. Each lab describes a combination of tools that works well for them, but almost no one gives a first-principles justification of why one tool is better than the other. For instance, why MLA is better than GQA, full stop. This is much different from domains like math or theoretical physics, which are all about providing first-principles explanations that derive results from axioms or laws.

> 就我个人而言,我认为这些论文以及更广义上深度学习的前沿现状中,最有意思的一点是,其中很多内容读起来都像是经验性的发现。每家实验室都描述了一套对他们行之有效的工具组合,但几乎没有人从第一性原理出发,论证为什么某种工具优于另一种。比如,为什么 MLA 就是比 GQA 更好,如此而已。这与数学或理论物理等领域截然不同,那些领域的核心是提供从公理或定律出发推导出结论的第一性原理解释。

[11:03] Also, it's interesting that even though most of these models have similar top-line benchmark statistics and use broadly the same tools, like attention mechanisms, activation functions, positional embeddings, and so on, they achieve these similar results using often very different techniques. This is quite surprising. You'd expect that very different training methods would lead to very different results.

> 另外,有意思的是,尽管这些模型大多数在头部基准指标上表现相近,并且大体上使用相同的工具——如注意力机制、激活函数、位置编码等等——但它们往往是用非常不同的技术取得这些相近结果的。这相当出人意料。你会以为差异如此之大的训练方法应该会导致差异很大的结果。

[11:22] Also, all of the major models heavily use reinforcement learning as part of the post-training and reasoning portions of their model training efforts. And it's fascinating and pretty surprising how some of these RL efforts require very little amounts of data, just 4,000 data pairs in the case of QUINN.

> 此外,所有主流模型都在其模型训练工作的后训练和推理环节中大量使用了强化学习。而令人着迷、也相当出人意料的是,其中一些强化学习工作所需的数据量非常之少——就 Qwen 而言,仅需 4,000 对数据。

[11:35] Another point here is that it's very opaque what the differences in datasets are between the labs. It's clear from the papers that there's an enormous amount of work happening behind the scenes in dataset engineering. This work is probably a significant aspect of the moat that makes these companies comfortable releasing their models. It's very difficult to replicate what they're releasing.

> 这里还有一点是,各家实验室之间数据集的差异非常不透明。从论文中可以清楚地看出,在数据集工程方面,幕后有大量的工作在进行。这些工作很可能是构成护城河的一个重要方面,正是它让这些公司敢于放心地发布自己的模型。要复制他们所发布的东西是非常困难的。

[11:51] So the big takeaway when reading these papers is you shouldn't focus too much on just the benchmark performance or top-line stats like context size. Instead, look at the specific methods that these labs are using to achieve those results. There are tons of high-performing open-source models that we didn't discuss in this video, like Kimmy K2 or Google Gemma 3. But when you peek under the hood of many of these, you'll find nuanced differences that I find really interesting.

> 因此,阅读这些论文时的一个重要收获是,你不应过于关注单纯的基准表现或诸如上下文规模之类的头部指标。相反,要去看这些实验室为取得那些结果所采用的具体方法。还有大量高性能的开源模型我们在本视频中没有讨论,比如 Kimi K2 或谷歌的 Gemma 3。但当你深入探究其中许多模型的内部时,你会发现一些细微的差异,我觉得这些差异真的很有意思。

[12:13] I hope this gives you a framework for how to understand the latest open-source releases and gives you a toolkit to start tinkering with them yourself. Thanks for watching. See you in the next episode.

> 我希望这能为你提供一个理解最新开源模型发布的框架,并给你一套工具,让你能够自己动手去尝试和摆弄它们。感谢观看。我们下期节目再见。
