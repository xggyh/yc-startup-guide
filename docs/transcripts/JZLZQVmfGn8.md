# 全文转录 · Transformer 简史:改变 AI 的那次发现

> ▶ [YouTube](https://www.youtube.com/watch?v=JZLZQVmfGn8) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/JZLZQVmfGn8.md) &nbsp;·&nbsp; Transformers Explained: The Discovery That Changed AI Forever

> 中英对照 · 每段英文原文下附中文翻译

[00:00] Nearly every state-of-the-art AI system, whether it's ChatGPT, Cloud, Gemini, or Grok, is built on the same underlying model architecture, the transformer. But where did the transformer architecture come from, and what can its development teach us about the way breakthroughs in AI happen? Let's dive in. A transformer is a neural network that uses self-attention to take input data, like text or images, model the relationships between that data, and finally generate outputs, like meaningful text responses, translations, or classifications.

> 几乎每一个最先进的 AI 系统,无论是 ChatGPT、Cloud、Gemini 还是 Grok,都建立在同一种底层模型架构之上,那就是 Transformer。但 Transformer 架构究竟从何而来?它的发展又能告诉我们 AI 突破是如何发生的?让我们深入探讨。Transformer 是一种神经网络,它利用自注意力机制接收输入数据(比如文本或图像),对这些数据之间的关系进行建模,最终生成输出,比如有意义的文本回复、翻译或分类结果。

[00:35] Many people know that the original transformer architecture was introduced in a now-famous 2017 paper from Google called, Attention is All You Need. But what you might not know about are the breakthroughs that made this overnight success possible. There are three key developments that we'll discuss today. Long short-term memory, seek-to-seek with attention, and then finally, transformers. Let's start with long short-term memory networks, or LSTMs.

> 很多人都知道,最初的 Transformer 架构是在 2017 年 Google 那篇如今非常著名的论文《Attention is All You Need》中被提出的。但你可能不知道的是那些让这个"一夜成名"成为可能的突破。今天我们会讨论三项关键进展:长短期记忆网络、带注意力机制的序列到序列模型,以及最后的 Transformer。让我们从长短期记忆网络(即 LSTM)开始。

[00:57] One of the core challenges motivating early AI research was to get neural networks to understand sequences. Natural language is inherently sequential, and that's what we're going to talk about today. So let's get started. The meaning of a word depends on what comes before it or after it, and understanding an entire sentence requires maintaining context across many words. Early architectures, like feed-forward neural networks, processed each input in isolation, and so they weren't capable of understanding context, or they required looking at inputs of a fixed length.

> 推动早期 AI 研究的核心挑战之一,就是让神经网络理解序列。自然语言本质上是有顺序的,这正是我们今天要讨论的内容。那么让我们开始吧。一个词的含义取决于它前面和后面的内容,而理解一整句话则需要在许多词之间保持上下文。早期的架构,比如前馈神经网络,是孤立地处理每一个输入的,因此它们无法理解上下文,或者只能处理固定长度的输入。

[01:22] So researchers developed recurrent neural networks, or RNNs, as a solution to this. In simple terms, an RNN iterates over the inputs in order, one at a time, and consumes the previous outputs as additional input at each step. So if an input is of length n, there are n feed-forward pass steps. And as a result, during the backwards pass, the gradient with respect to the early inputs is the result of n matrix multiplications.

> 于是研究人员开发了循环神经网络(即 RNN)来解决这个问题。简单来说,RNN 会按顺序逐个遍历输入,并在每一步把上一步的输出作为额外输入。所以如果一个输入长度为 n,就会有 n 个前向传播步骤。因此在反向传播时,相对于早期输入的梯度是 n 次矩阵乘法的结果。

[01:44] Now in practice, this meant that we often faced a problem called vanishing gradients. The early inputs in a sequence had less and less influence on the network's output as the sequence grew longer, because it went through these multiple matrix multiplications. Gradients, which are the signals used to adjust weights during training, would fade to near zero as they were passed backwards.

> 而在实践中,这意味着我们经常会遇到一个叫做"梯度消失"的问题。随着序列变长,序列中较早的输入对网络输出的影响越来越小,因为它要经过这么多次矩阵乘法。梯度——也就是训练过程中用来调整权重的信号——在反向传递时会衰减到接近于零。

[02:05] In the 1990s, Hockreiter and Schmidhuber proposed a solution to this. It was called the Long Short Term Memory Network, or LSTMs. LSTMs were a type of RNN that attempted to fix the vanishing gradient problem by introducing gates, which could learn what information to keep, update, or forget. This made it possible to learn long-range dependencies, something vanilla RNNs struggled with. But LSTMs were too expensive to train at scale in the 90s, and so progress stalled.

> 在 20 世纪 90 年代,Hochreiter 和 Schmidhuber 提出了一个解决方案,叫做长短期记忆网络(即 LSTM)。LSTM 是一种 RNN,它试图通过引入"门"来修复梯度消失问题,这些门能够学习哪些信息应该保留、更新或遗忘。这使得学习长距离依赖成为可能,而这正是普通 RNN 难以做到的。但在 90 年代,LSTM 大规模训练的成本太高,因此进展陷入了停滞。

[02:34] Now you fast-forward to the early 2010s, and GPU acceleration, and you can see that the LSTMs were more expensive to train at scale in the 90s, and so progress stalled. Now you fast-forward to the early 2010s, and GPU acceleration, better optimization techniques, and new large-scale datasets brought LSTMs back into the spotlight. Suddenly, this relatively old architecture was viable again, and it began to dominate natural language processing. LSTMs were quickly adopted for everything from speech recognition to language modeling.

> 快进到 2010 年代初,随着 GPU 加速、更好的优化技术以及新的大规模数据集的出现,LSTM 重新回到了聚光灯下。突然之间,这个相对老旧的架构又变得可行了,并开始主导自然语言处理。从语音识别到语言建模,LSTM 很快被广泛采用。

[02:53] In these years, NLP and computer vision were actually somewhat separate worlds. RNNs and LSTMs in particular were preeminent in language tasks, while convolutional neural networks, or CNNs, were winning in vision. But the basic question motivating both NLP and computer vision was the same. How do you model sequences? How do you let those models capture a structure that spans time or space? LSTMs were a huge step forward, but they still had limitations. The most fundamental was something called the fixed-length bottleneck.

> 在那些年里,NLP 和计算机视觉其实是两个相对独立的世界。RNN,尤其是 LSTM,在语言任务中占据主导地位,而卷积神经网络(即 CNN)则在视觉领域大放异彩。但驱动 NLP 和计算机视觉的基本问题是相同的:如何对序列建模?如何让这些模型捕捉跨越时间或空间的结构?LSTM 是一次巨大的进步,但它仍然存在局限,其中最根本的一个被称为"定长瓶颈"。

[03:17] Here's how most early LSTM systems worked. For sequence-to-sequence tasks like translation, you would take the input sentence, feed it into an encoder LSTM, and boil the input down to a single fixed-size vector. Then, a decoder LSTM would take that vector and try to construct the target sentence word-by-word. Then, a decoder LSTM would take that vector and try to construct the target sentence word-by-word. This yielded impressive results on the benchmarks of that era. But in practice, that single vector was still unable to accurately capture the meaning of long or complex sentences.

> 大多数早期的 LSTM 系统是这样工作的。对于像翻译这样的序列到序列任务,你会把输入句子送入一个编码器 LSTM,把输入压缩成一个固定大小的向量。然后,一个解码器 LSTM 会拿着这个向量,尝试逐词构建出目标句子。这在那个时代的基准测试上取得了令人印象深刻的成果。但在实践中,那个单一的向量仍然无法准确捕捉长句或复杂句子的含义。

[03:43] Also, there wasn't a great way to encode the concept of order into a fixed-size vector. This was very important in translation tasks. For example, in English, we put adjectives before nouns, and in Spanish, we often place adjectives after nouns. You'd see this in performance. These models worked okay on short inputs, but they quickly fell apart as sequences got longer. And truthfully, this was more than a performance issue.

> 此外,也没有很好的办法把"顺序"这个概念编码进一个固定大小的向量里。这在翻译任务中非常重要。例如,在英语中我们把形容词放在名词前面,而在西班牙语中我们常常把形容词放在名词后面。你能从性能表现上看到这一点。这些模型在短输入上表现还行,但随着序列变长,它们很快就崩溃了。而说实话,这不仅仅是一个性能问题。

[04:04] It pointed to a deeper architectural problem. Allowing the decoder to only see one static summary of the input was a fundamental limitation. Why not give it access to all the intermediate information that the encoder saw? This sort of insight is what gave rise to the next big leap. In 2014, a paper introduced what would become the new standard for sequence translation. Sequence-to-sequence, or seek-to-seek, models with attention.

> 它指向了一个更深层的架构问题。只让解码器看到输入的一个静态摘要,是一个根本性的局限。为什么不让它访问编码器看到的所有中间信息呢?正是这种洞见催生了下一次重大飞跃。2014 年,一篇论文提出了后来成为序列翻译新标准的东西:带注意力机制的序列到序列(seq2seq)模型。

[04:29] Like before, the core idea was to train two neural networks jointly. An encoder, which reads the input sequence and builds a representation of it, and a decoder, which generates the output sequence one step at a time. Both models were LSTMs, and crucially, they were trained together end-to-end. But there was a key insight that enabled this performance jump. Attention.

> 和之前一样,其核心思想是联合训练两个神经网络。一个编码器,负责读取输入序列并构建它的表示;一个解码器,负责一步一步地生成输出序列。这两个模型都是 LSTM,而关键在于,它们是端到端一起训练的。但真正促成这次性能飞跃的,是一个关键洞见:注意力。

[04:48] Even though seek-to-seek used a fixed-length vector, researchers realized that if you could let the decoder look back or attend to the encoder's hidden states, you could let the model learn how to align parts of the input to parts of the output. Banadao, Chou, and Bengio showed that these models could significantly outperform traditional rule-based systems and the existing seek-to-seek models on tasks like machine translation. That was a big deal. These models were evaluated on translation benchmarks and showed near state-of-the-art performance, beating even the best statistical systems of the time.

> 尽管 seq2seq 使用的是定长向量,但研究人员意识到,如果你能让解码器"回看"或"注意"编码器的隐藏状态,你就能让模型学会如何把输入的各个部分与输出的各个部分对齐。Bahdanau、Cho 和 Bengio 证明,这些模型在机器翻译等任务上能够显著超越传统的基于规则的系统以及现有的 seq2seq 模型。这是件大事。这些模型在翻译基准上接受评测,展现出接近最先进水平的性能,甚至击败了当时最好的统计系统。

[05:16] It was a sign that neural models could compete head-to-head with the mature, production-grade systems of old. And for many people, this was the first moment they began to see these models in practice. This was real, usable NLP. For example, Google Translate adopted a neural seek-to-seek architecture around this time. And you may remember this as the era in which Google Translate started to finally work well.

> 这标志着神经网络模型可以与那些成熟的、生产级的老系统正面较量。对许多人来说,这是他们第一次在实际应用中见到这类模型。这是真正可用的 NLP。例如,Google 翻译大约在这个时期采用了神经 seq2seq 架构。你可能记得,正是在那个时代,Google 翻译终于开始真正好用了。

[05:38] This insight, learning to align and translate at the same time, was transformative. And it wouldn't just stay in NLP. One of the original seek-to-seek authors, Yashua Bengio, soon applied similar alignment-based architectures to computer vision. This was the first sign that these sequence models might be useful beyond language. But even when augmented with attention, RNNs were still constrained by their sequential architecture. Processing tokens one at a time made it challenging to run computations in parallel across time steps.

> 这个洞见——同时学习对齐与翻译——是革命性的。而且它不会只停留在 NLP 领域。最初 seq2seq 论文的作者之一 Yoshua Bengio 很快就把类似的基于对齐的架构应用到了计算机视觉上。这是这类序列模型可能超越语言领域大有用武之地的第一个迹象。但即便加入了注意力机制,RNN 仍然受制于它们的顺序架构。一次只处理一个 token,使得跨时间步并行计算变得困难。

[06:00] So runtime-scanned NLP models would scale linearly with sequence length. This made training models on large data sets, the kinds we knew would be necessary to achieve broadly useful AI, intractably slow. In an attempt to speed up RNNs, researchers developed techniques like factorizing LSTM matrices into smaller matrix products or conditionally activating only parts of a network that were relevant to a query. But the fundamental linear runtime constraint remained.

> 因此这些模型的运行时间会随着序列长度线性增长。这使得在大规模数据集上训练模型——我们知道要实现广泛有用的 AI 就必须依赖这种数据集——变得慢到难以承受。为了给 RNN 提速,研究人员开发了一些技术,比如把 LSTM 矩阵分解成更小的矩阵乘积,或者只有条件地激活网络中与某个查询相关的部分。但那个根本性的线性运行时约束依然存在。

[06:24] Then came the big breakthrough in 2017, when a team of researchers at Google published a paper called Attention is All You Need, which proposed a new machine translation architecture that they called a transformer. Transformers scrapped recurrence entirely, instead relying solely on an attention mechanism to generate outputs. We won't get fully into the technical weeds of transformers here. For that, check out Andrej Karpathy's fantastic explainer.

> 接着,2017 年迎来了重大突破:Google 的一个研究团队发表了一篇名为《Attention is All You Need》的论文,提出了一种新的机器翻译架构,他们称之为 Transformer。Transformer 彻底抛弃了循环结构,转而完全依靠注意力机制来生成输出。我们在这里不会深入 Transformer 的所有技术细节。想了解这些,可以去看 Andrej Karpathy 那份精彩的讲解。

[06:47] But at a high level, transformers use a modified version of the encoder-decoder architecture originally proposed in seek2seek. Instead of compressing inputs into a single vector embedding, transformers kept separate embeddings for each input token and updated these through self-attention, a mechanism that updated token representations based on a learned weighted dot product over the embeddings of all other tokens in the sequence. Because each token in this architecture could attend to all others simultaneously, transformers could process an entire sequence in parallel, making them dramatically faster than RNNs. Remarkably, they were also much more accurate on machine translation benchmarks.

> 但从宏观上看,Transformer 使用的是 seq2seq 最初提出的编码器-解码器架构的一个改良版本。Transformer 不再把输入压缩成单一的向量嵌入,而是为每个输入 token 保留各自独立的嵌入,并通过自注意力来更新它们——这种机制会基于对序列中所有其他 token 嵌入的一个可学习的加权点积,来更新每个 token 的表示。由于在这种架构中每个 token 都能同时关注到所有其他 token,Transformer 可以并行处理整个序列,这使得它们比 RNN 快得多。值得注意的是,它们在机器翻译基准上也准确得多。

[07:25] Over the next few years, researchers started to experiment with different variations of the transformer architecture. The architecture described in the original Google paper featured an encoder and decoder that could be used to process an entire sequence of tokens simultaneously. Each had self-attention and cross-attention between the two. This resembled the original seek2seek architectures but without the recurrence. The next several years saw a lot of innovation in the transformer architecture itself.

> 在接下来的几年里,研究人员开始尝试 Transformer 架构的各种变体。Google 原始论文中描述的架构包含一个编码器和一个解码器,可以同时处理整个 token 序列。每一部分都有自注意力,两者之间还有交叉注意力。这与最初的 seq2seq 架构相似,但去掉了循环结构。接下来的几年里,Transformer 架构本身出现了大量创新。

[07:40] For example, a series of models called BERT focused on using only the encoder to do masked language modeling. In parallel, efforts to use only the decoder for autoregressive modeling gave rise to OpenAI's GPT series of models. At a high level, we can describe both of these model series as subsets of the original attention-is-all-you-can-need transformer model. It quickly became clear that these models could scale to large numbers of parameters.

> 例如,一系列被称为 BERT 的模型专注于只用编码器来做掩码语言建模。与此同时,只用解码器来做自回归建模的努力则催生了 OpenAI 的 GPT 系列模型。从宏观上看,我们可以把这两大系列模型都描述为最初那个"Attention is All You Need"Transformer 模型的子集。人们很快就发现,这些模型可以扩展到参数量非常庞大的规模。

[08:06] Ultimately, one model type, the generative pre-trained transformer model, or GPT, would be scaled up to create the LLMs that we regularly use today in products like ChatGPT or Claude. But not that long ago, it wasn't obvious that there might be one model to rule them all. In fact, people were training variants of model architectures for every task, one for machine translation, another for named entity recognition, and so on, each with a shared backbone but slight differences in the final model layer.

> 最终,有一种模型类型——生成式预训练 Transformer 模型(即 GPT)——被不断放大,进而造就了我们如今在 ChatGPT 或 Claude 等产品中经常使用的大语言模型。但就在不久之前,"可能存在一个统治一切的模型"这件事还并不显而易见。事实上,当时人们是在为每个任务分别训练架构的不同变体:一个用于机器翻译,另一个用于命名实体识别,如此等等,每个模型共享同一个主干,但在最后的模型层上略有不同。

[08:32] These models were intelligent in that their accuracy was high, but they were largely single task models. Also, at this point, there wasn't really a concept of prompting the models because there was no chat interface. Instead, people interacted with the models through domain-specific inputs. It was only as the labs started to experiment with training autoregressive models on much larger datasets that they began to look and feel more like generally intelligent systems.

> 这些模型很"聪明",因为它们的准确率很高,但它们在很大程度上只是单任务模型。而且在这个阶段,还谈不上"给模型下提示词"这个概念,因为当时并没有聊天界面。相反,人们是通过特定领域的输入来与模型交互的。只有当各个实验室开始尝试在大得多的数据集上训练自回归模型时,这些模型才开始看起来、用起来更像是具备通用智能的系统。

[08:55] Hopefully, this history helped contextualize some of what it took to get these models to a place of being able to scale them. In the next video, we'll talk about some of the architectural and engineering innovations it took to actually get them to their current performance levels. Thanks for watching!

> 希望这段历史能帮助你理解,把这些模型带到可以规模化的阶段,背后经历了怎样的过程。在下一个视频中,我们会谈谈为了真正把它们提升到如今的性能水平所需要的一些架构与工程创新。感谢观看!
