# 全文转录 · 递归:AI 的下一条 Scaling Law

> ▶ [YouTube](https://www.youtube.com/watch?v=DGtUUMNYLcc) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/DGtUUMNYLcc.md) &nbsp;·&nbsp; Recursion Is The Next Scaling Law In AI

> 中英对照 · 每段英文原文下附中文翻译

`[00:00]` **SPEAKER_00:** Welcome back to another episode of Decoded. Today, I'm back with YC visiting partner, Francois Chaubard, to talk about one of the most interesting recent trends in AI research, recursion. Specifically, we're going to talk about how we can improve a model's reasoning performance by using recursion at inference time, rather than by just making the model bigger and bigger. There were two papers that made the power of this approach really clear in 2025. One on hierarchical reasoning models, or HRM, and another on tiny recursive models, TRM.

> 欢迎回到新一期的 Decoded。今天我又请来了 YC 的访问合伙人 Francois Chaubard，来聊聊 AI 研究中最有意思的近期趋势之一——递归。具体来说，我们要讨论如何通过在推理阶段使用递归来提升模型的推理表现，而不是单纯地把模型越做越大。2025 年有两篇论文把这种方法的威力展现得非常清楚：一篇关于分层推理模型（HRM），另一篇关于微型递归模型（TRM）。

`[00:28]` **SPEAKER_00:** Francois, thanks for joining us. Can you tell us a little bit about these two models, and what was so interesting about them?

> Francois，谢谢你来参加。你能给我们简单介绍一下这两个模型，以及它们到底有什么让人觉得如此有意思的地方吗？

`[00:42]` **SPEAKER_01:** Sure. I guess to set up a little bit of a foundation, you already did an amazing lecture on RNNs and LLMs in one of the previous videos, so I won't overdo it, but just to give the cliff notes, an RNN is just a model that you recursively call again and again and again on itself, and we were very much in the belief that this was required to get to the point where we could do this. So we went to AGI peak RNN use, which was probably until 2016, with Alex Graves' keynote, which is just fantastic, and all his adaptive compute time work.

> 当然。为了先打个基础——你在之前的一期视频里已经做过一场很棒的关于 RNN 和 LLM 的讲解，所以我不会讲得太多，但简单概括一下：RNN 就是一种你不断地、反复地对它自身进行递归调用的模型。我们当时非常坚信，要达到能做到这一步的水平，就必须靠它。所以我们经历了 RNN 使用的鼎盛时期，大概一直到 2016 年，Alex Graves 的主题演讲——那真是精彩绝伦——以及他所有关于自适应计算时间的工作。

`[01:15]` **SPEAKER_00:** So this is about 10 years ago, people were working on these models. This was in the era of LSTMs and LSTMs with attention.

> 所以这大约是十年前，人们在研究这些模型。那是 LSTM，以及带注意力机制的 LSTM 的时代。

`[01:21]` **SPEAKER_01:** Yeah, and depending which professors you talk to, before attention was invented.

> 是的，而且要看你跟哪位教授聊——那甚至是在注意力机制被发明之前。

`[01:25]` **SPEAKER_00:** Yes, yes, totally.

> 对，对，完全没错。

`[01:28]` **SPEAKER_01:** And I think what really was the limiting step on RNNs in general was this thing called backprop. Backprop is where you have to, you roll out the model, and then to update the weights, you need to approximate the gradient, and you step back, back, back, and you keep rolling out. And as the model gets bigger and bigger, and as you roll out for more and more steps, then you have all these accumulation of errors, and the gradient gets noisier and noisier, and then it just kind of stops to work.

> 我觉得总体上真正限制住 RNN 的，是叫做反向传播的东西。反向传播就是你得把模型展开，然后为了更新权重，你需要近似梯度，你一步步往回走、往回走、往回走，而且不断地展开。随着模型越来越大，展开的步数越来越多，你就会积累起所有这些误差，梯度变得越来越嘈杂，最后就几乎没法用了。

`[01:54]` **SPEAKER_00:** Yeah, so you have these vanishing or exploding gradient problems, and it's because if you have an input with 20 steps, you're multiplying these matrices 20 times, and that causes training.

> 对，所以你会遇到梯度消失或梯度爆炸的问题，原因在于如果你有一个 20 步的输入，你就要把这些矩阵相乘 20 次，而这会影响训练。

`[02:01]` **SPEAKER_01:** And we're talking about doing context length of a million or a billion, and so it's not even just 20, it's like a billion. And even worse, you have to retain the activations at every single step. And so if this were happening in your brain, you would need a million copies of your brain at every single activation so that I can backprop through it. There's tricks around this that you can do, and you can do a gradient checkpointing and things like that to reduce that issue, but then you're just trading off memory for wall clock time and compute.

> 而我们说的是要做到上百万甚至上十亿的上下文长度，所以根本不止 20 步，而是十亿这个量级。更糟的是，你必须保留每一步的激活值。所以如果这发生在你的大脑里，你就需要在每一个激活处都有一百万份大脑的副本，我才能反向传播回去。有一些绕过这个问题的技巧，比如你可以做梯度检查点（gradient checkpointing）之类的来减轻这个问题，但那样你只是在用内存去换实际耗时和算力而已。

`[02:29]` **SPEAKER_00:** Right, so now if you contrast that with LLMs, the ones that people are widely using, these, while at face value they appear to be similar, at training time, they're doing basically this one-shot feedforward process for every input, right? The LLM, the transformer block, can take all of the inputs in parallel. It's not actually iteratively going over them one at a time at train time, so you don't have this needing to store tons of activations problem or this giant vanishing gradients problem with them.

> 对，那么如果你把它和大家广泛使用的 LLM 对比一下，这些模型表面上看起来相似，但在训练时，它们基本上对每个输入做的是一次性的前馈过程，对吧？LLM，也就是 Transformer 模块，可以并行地接收所有输入。它在训练时并不是真的一次一个地迭代处理它们，所以你不会有那种需要存储海量激活值的问题，也不会有那种巨大的梯度消失问题。

`[02:55]` **SPEAKER_01:** Yeah, exactly. Like, it's actually all happening in time in one shot, magically. And that was like the trill or lower triangle trick, that kind of thing. Yeah. And that's what happens, this causal mask that occurs.

> 是的，正是如此。就好像所有事情神奇地一次性、同时发生了。那就是所谓的三角、下三角这类技巧。对，就是这样，就是那个因果掩码（causal mask）在起作用。

`[03:06]` **SPEAKER_01:** And so you actually do all time steps in one shot, and you forward pass a feedforward model on all time steps in one shot, and you backwards in one shot, and it's amazing for train time in terms of like wall clock. It requires a lot of flops, and it still requires a lot of the memory. You still need it there, but you don't have the vanishing gradient issue. And what you actually paid for that you have to give up is this latent reasoning thing and this compression in the time direction. There is no compression in LLMs.

> 于是你实际上一次性完成了所有时间步，你对所有时间步一次性地前向传播一个前馈模型，再一次性地反向传播，从实际耗时的角度来说，这对训练时间来说非常棒。它需要大量的浮点运算，也仍然需要大量的内存，那些你还是得有，但你不会有梯度消失的问题。而你为此付出的、不得不放弃的代价，就是这种潜在推理能力，以及时间方向上的压缩。LLM 里没有压缩。

`[03:35]` **SPEAKER_01:** Every single decode that I do, I still have to retain the entire, you know, Shakespeare novel just to like decode a little bit, and in RNNs, you don't have to do that. It's all compressed in this hidden state that you kind of roll out.

> 我每做一次解码，都还得保留整部——你知道的——莎士比亚小说，就为了解码那么一点点；而在 RNN 里，你不必这样做。所有东西都被压缩进你逐步展开的这个隐藏状态里。

`[03:46]` **SPEAKER_00:** Okay, so let's talk about that in a little bit more detail. Like, you refer to this inherent reasoning ability. You know, many people think about LLMs as doing reasoning, and we're going to talk about that a little bit later, but help me understand where you see the biggest limitations in LLMs reasoning ability. Or is in terms of what the model does in an actual forward pass.

> 好，那我们再详细一点谈谈这个。你提到这种内在的推理能力。要知道，很多人认为 LLM 是在做推理，我们稍后会谈到这一点，但先帮我理解一下：你认为 LLM 推理能力最大的局限在哪里？或者说，就模型在一次实际前向传播中所做的事情而言。

`[04:08]` **SPEAKER_01:** Yeah, and so I guess we go back to chat GPT-2. GPT-2 was this landmark architecture and paper that basically was just get next token, next token, next token, and it kind of worked. And like we just watched val loss go down, perplexity goes down, like the model just is more performant, looks better, starts to make some Shakespeare that actually sounds somewhat plausible. Right. And then we have to get these things to reason.

> 好，那我想我们要回到 ChatGPT-2。GPT-2 是一个里程碑式的架构和论文，基本上就是预测下一个 token、下一个 token、下一个 token，而且它还挺管用。我们就看着验证损失（val loss）往下降、困惑度（perplexity）往下降，模型就是越来越强、越来越好看，开始能写出听起来还挺像那么回事的莎士比亚。对。然后我们就得让这些东西去推理。

`[04:33]` **SPEAKER_01:** And to actually solve some really hard problems. And I've done extensive experiments on this, but like if you take, for example, sort. You have infinite amounts of unsorted lists and you give it sorted lists. You keep feeding it to the model, it should work, right? It's actually impossible for the model to map from unsorted list to sorted list.

> 还要真正去解决一些非常难的问题。我在这方面做过大量实验，但比如说你拿排序来举例。你有无穷多的未排序列表，你给它对应的已排序列表。你不断地把它们喂给模型，它应该学得会，对吧？可实际上，模型根本不可能完成从未排序列表到已排序列表的映射。

`[04:54]` **SPEAKER_01:** If I have a- In a one-shot basically. In a one-shot basis. It's like literally that we know a theoretical lower bound that for comparison sort, you can't do better than n log n. Steps. And if I have a list that's 31 characters or elements long, and my transformer is 30, I run out of steps to do comparisons.

> 如果我有一个——基本上是在一次性（one-shot）的情况下。在一次性的前提下。这就好比我们知道有一个理论下界：对于比较排序，你没法比 n log n 更快——是步数。如果我有一个 31 个字符或元素长的列表，而我的 Transformer 只有 30 层，我就没有足够的步数去做比较了。

`[05:16]` **SPEAKER_01:** It's not possible for me to do all the steps that is needed to be done. In HRM and TRM, they use Sudoku as an incompressible problem. Similarly, and so are mazes, those are incompressible problems. Rolling sum, incompressible problem.

> 我不可能完成所有需要做的步骤。在 HRM 和 TRM 里，他们用数独作为一个不可压缩的问题。类似地，迷宫也是，那些都是不可压缩的问题。滚动求和（rolling sum），也是不可压缩的问题。

`[05:29]` **SPEAKER_00:** So when you mentioned the sorting algorithm, when I think back to my algorithms class from college, the one way you could get faster than n log n in a sorting algorithm is if you had some access to an external memory cache. If you had some tape you could write to, then you can actually do faster than n log n by basically selectively putting things onto this memory. And I suspect that's a key limitation of these LLMs in that because there's no external memory tape in-built into the model, you lose certain performance possibilities in terms of how fast you can go.

> 那么你提到排序算法时，我回想起大学里的算法课，能让排序算法比 n log n 更快的一种办法，是你能访问某种外部内存缓存。如果你有某种可以写入的磁带，那么你实际上就能通过有选择地把东西放到这块内存上，从而做到比 n log n 更快。我猜这就是这些 LLM 的一个关键局限：因为模型内部没有内置的外部内存磁带，你就在能跑多快这方面失去了某些性能上的可能性。

`[05:57]` **SPEAKER_01:** That's right. And so I guess rate of sort would be the most common one, depending on the number of buckets that you have. You can kind of get from n log n to order n. You can't get less than n. You have to touch all the elements.

> 没错。所以我想基数排序（radix sort）会是最常见的例子，取决于你有多少个桶。你大致能从 n log n 降到 O(n)。你没法低于 n，你必须触及所有元素。

`[06:09]` **SPEAKER_01:** Sorry, you have to do that. And if you run out of layers and transformer layers in your neural network, then you ran out of chances to do that.

> 抱歉，你必须那样做。而如果你在神经网络里用完了层数、用完了 Transformer 的层，那你就用完了做这件事的机会。

`[06:20]` **SPEAKER_00:** So this is just like going back to like Alan Turing now and like a Turing machine, right? So what's the analogy there exactly that we should think about in terms of LLMs, I guess, not quite satisfying how you think about a Turing machine?

> 所以这就好像现在回到了 Alan Turing、回到了图灵机，对吧？那么在 LLM 的语境里，我们究竟应该怎么理解这个类比呢？我猜大概是说，LLM 并不完全满足你对图灵机的那种设想？

`[06:30]` **SPEAKER_01:** Yeah. So let's just talk about like chat-GBT2. GBT2. GBT2, the original, like no bells and whistles, it's just a feed-forward model. And so it's just forward passing one step and taking an input, creating a bunch of outputs.

> 对。那我们就说说 ChatGPT-2 吧。GPT-2。最初的 GPT-2，没有任何花哨的东西，它就是一个前馈模型。所以它只是一步前向传播，接收一个输入，产生一堆输出。

`[06:44]` **SPEAKER_01:** In the Sudoku case, if I have 50 different squares, and it's provable that I can only do one given this information, and I have this many layers, then that's all I can do. And the cheat is the chain of thought. And so it's completely true that at test time. They are Turing complete, and you can simulate all Turing computable functions at test time. But how do you get it to learn it?

> 拿数独来说，如果我有 50 个不同的格子，而可以证明根据现有信息我一次只能填一个，而我只有这么多层，那我能做的就到此为止了。而作弊的手段就是思维链（chain of thought）。所以完全正确的一点是：在测试时它们是图灵完备的，你在测试时可以模拟所有图灵可计算的函数。但你怎么让它学会这一点呢？

`[07:10]` **SPEAKER_01:** You need to train it. And that's where, unless you're training it on human-labeled traces, for which there's a lot of problems like the millennial prize problem, we don't have the trace for it. Right.

> 你得训练它。而问题就在这里：除非你用人工标注的推理轨迹（traces）来训练它，可对于像千禧年大奖难题这样的很多问题，我们根本没有对应的轨迹。对。

`[07:21]` **SPEAKER_00:** So we'd love to have the trace for it, just doesn't exist. Totally. Makes sense. Okay. So with that context in mind now, let's talk about these two papers, because I think that sets up a lot of the contrast we're going to draw between these papers.

> 所以我们很想有那个轨迹，只是它根本不存在。完全对。说得通。好。那么有了这个背景之后，我们现在来谈谈这两篇论文，因为我觉得这为我们要在这两篇论文之间做的很多对比铺垫了基础。

`[07:31]` **SPEAKER_00:** Yeah. Yeah. And the models that people are maybe more used to. So let's talk about HRMs first. Walk me through a little bit about how this model works and some of the intuition behind it.

> 对，对。还有那些人们可能更熟悉的模型。那我们先谈谈 HRM。带我大致过一遍这个模型是怎么工作的，以及它背后的一些直觉。

`[07:42]` **SPEAKER_01:** Sure. So this is directly in the lineage of RNNs. There's not that much novel from the RNN standpoint, at least in my opinion. They do have this idea of, inspired by the brain, where I have, there's different parts of the brain that operate at different frequencies.

> 当然。这直接属于 RNN 的谱系。从 RNN 的角度看，至少在我看来，并没有多少新东西。他们确实有一个受大脑启发的想法：大脑的不同部分以不同的频率运作。

`[08:03]` **SPEAKER_01:** So some that operate at a really high frequency, which is then the low level of the hierarchy. Some that operate in a really low frequency, which is the higher level of the hierarchy. And the interplay between those things is really interesting.

> 有些以非常高的频率运作，那就对应层级结构中的低层。有些以非常低的频率运作，那就是层级结构中的高层。而这两者之间的相互作用非常有意思。

`[08:13]` **SPEAKER_00:** So this is like literally in the human brain, there's some bio-inspiration here, which is that you have different waves running at different frequencies at different parts of the brain or something like that.

> 所以这确实是从人脑而来，这里有一些生物学上的启发，也就是说在大脑的不同部位有以不同频率运行的不同波，或者诸如此类的东西。

`[08:22]` **SPEAKER_01:** Yeah. And I guess that's one interpretation of it, of the way that they're talking about classifying these hierarchies of frequencies. Yeah. But the most interesting part, at least for me, is the way that they train the neural network. You take in some X, some input, whether it's a incomplete Sudoku puzzle, a maze, or an art prize challenge, you do TL steps with the lower level module, then you do, to go to H, you do that TH times.

> 对。我想那是对它的一种解释，就是他们谈论如何对这些频率层级进行分类的方式。对。但最有意思的部分，至少对我来说，是他们训练神经网络的方式。你接收某个 X、某个输入，无论是一个未完成的数独谜题、一个迷宫，还是一个 ARC Prize 挑战，你用低层模块做 TL 步，然后为了进到 H，你把那件事做 TH 次。

`[08:59]` **SPEAKER_01:** And then you have N sup outer refinement. Yeah.

> 然后你还有 N_sup 次的外层精炼（outer refinement）。对。

`[09:02]` **SPEAKER_00:** So you basically are like running through the input with a given matrix, with a given transformation repeatedly on it. And you're doing that through two levels of refinement, and then basically running that process several times.

> 所以你基本上就是用一个给定的矩阵、一个给定的变换，反复地在输入上运行。你在两个层级的精炼中这样做，然后基本上把这整个过程再运行好几遍。

`[09:15]` **SPEAKER_01:** Yes. So there's exactly three levels of recursion occurring here. There's the low level, there's the high level, and then there's the outer refinement steps.

> 是的。所以这里恰好发生了三层递归。有低层，有高层，然后还有外层精炼的步骤。

`[09:22]` **SPEAKER_00:** And we're calling it recursion because it's the same weights that are being applied repeatedly. We're not changing the weights in between these steps.

> 我们之所以称之为递归，是因为反复施加的是同一组权重。在这些步骤之间我们并没有改变权重。

`[09:28]` **SPEAKER_01:** Exactly right. You get to recurse on the L net. TL times. You've recursed on the TH and the TL, this looped recursion, TH times, and then you do N sup, you do this whole outer refinement step, N sup times.

> 完全正确。你可以在 L 网络上递归 TL 次。你在 TH 和 TL 上做过这种循环递归，做 TH 次，然后你做 N_sup 次，你把这整个外层精炼步骤做 N_sup 次。

`[09:41]` **SPEAKER_00:** Cool. And so what's the basic intuition for why that works? Like why does that produce an effective paper result, and what even were the results that this paper showed?

> 酷。那么它为什么有效，基本的直觉是什么？也就是说它为什么能产生一个有效的论文结果，而且这篇论文展示的结果究竟是什么？

`[09:50]` **SPEAKER_01:** Yeah. And so, I mean, this got state of the art on ArtPrize 1 and 2, this was only a 27 million parameter model. Okay. Yeah.

> 对。我是说，这个模型在 ARC Prize 1 和 2 上取得了当时的最佳成绩，而它只是一个 2700 万参数的模型。好。对。

`[10:02]` **SPEAKER_00:** And so it's like a thousand inputs or something like that, like puzzles, basically.

> 所以差不多是一千个输入之类的，基本上就是谜题。

`[10:06]` **SPEAKER_01:** Yeah. There's literally a thousand tasks, which is extremely small. There is no pre-training at all. This starts from like literally tabula rasa weights, and it can outperform at that time if we go back. You know, we had O3, if you remember back, way back when, and O3 gets zero, literally zero.

> 对。真的就是一千个任务，这非常之小。完全没有预训练。它字面意义上从一张白纸（tabula rasa）的权重开始，而且在当时——如果我们回到那个时候——它就能超越……你知道的，那时候有 O3，如果你还记得的话，很久以前，而 O3 得零分，字面意义上的零分。

`[10:26]` **SPEAKER_01:** And this got like something like 70% on ArtPrize 1 at least at the time, which was just a huge breakthrough. And so kind of the way you can kind of think this is like variable scoping. And so like if I have like, you know, three nested functions, I guess the first, the lowest level function has like scoped variables, which they'll call ZL, which is the carry that and it's the zero.

> 而这个模型在 ARC Prize 1 上至少在当时拿到了大概 70%，这简直是巨大的突破。你大致可以把这理解成变量作用域（variable scoping）。就好比我有三个嵌套的函数，我想第一个、最底层的函数有它作用域内的变量，他们把它叫做 ZL，就是那个"进位"（carry），而它初始是零。

`[10:48]` **SPEAKER_00:** A latent variable. Latent variable.

> 一个潜变量（latent variable）。潜变量。

`[10:50]` **SPEAKER_01:** And like traditional RNN literature, they would call this the hidden state, the low level hidden state. Yeah. And I get to recurse, recurse, recurse. And then I pass back that ZL back to the outer scoped function, the higher level one. I let that one do one iter.

> 而按照传统的 RNN 文献，他们会把这叫做隐藏状态，低层的隐藏状态。对。然后我可以递归、递归、递归。接着我把那个 ZL 传回给外层作用域的函数，也就是更高层的那个。我让它做一次迭代。

`[11:05]` **SPEAKER_01:** It goes back and calls the lower level again. It does this whole thing in a third outer loop, which is called the outer refinement step.

> 它再回过头去，又调用低层。它把整件事放在第三个外层循环里做，那个循环就叫外层精炼步骤。

`[11:11]` **SPEAKER_00:** But when you describe it like that, it seems like it would have the same back prop through time problem that you would have at RNNs, and I think they came up with a clever trick to basically get around that. So like what was that trick that they figured out?

> 但你这样描述的时候，看起来它应该会有和 RNN 一样的、随时间反向传播（backprop through time）的问题，而我觉得他们想出了一个巧妙的技巧基本上绕开了它。那么他们想出的那个技巧是什么？

`[11:22]` **SPEAKER_01:** And this is really the crux of the paper that like differentiates it, in my opinion, in the literature, is they, instead of doing what Alex Graves did in all of his papers from neural turing machines to adaptive compute time to differential neural computers, is he always back propped through all of the recursion steps. And he was limited by back prop through time, so you could only make the model so big, you have all these issues, vanishing gradients, et cetera, et cetera. And what they do is they kind of have this DEQ method of doing fixes. So it's like deep equilibrium models. Yeah, deep equilibrium learning, where if I take a batch, and this is completely counterintuitive as a computer vision person, because you'd never do this, but it actually does make sense.

> 而这确实是这篇论文的关键所在，在我看来也是它在文献中与众不同的地方：他们没有像 Alex Graves 在他所有论文里做的那样——从神经图灵机到自适应计算时间再到可微神经计算机——他总是穿过所有递归步骤做反向传播。而他受限于随时间反向传播，所以模型只能做到那么大，你会遇到所有这些问题：梯度消失，等等等等。而他们所做的，是采用一种 DEQ 的方法来做修正。也就是深度平衡模型（deep equilibrium models）。对，深度平衡学习，就是如果我取一个批次（batch）——作为一个搞计算机视觉的人，这完全反直觉，因为你绝不会这么做——但它其实是说得通的。

`[12:11]` **SPEAKER_01:** And I'll explain why. If I take a batch of like ImageNet or CIFAR10, and I forward pass through the model, and I get some loss, and I back prop, and I update the weights, I would go get a different batch for the next one. But what they do instead is they actually do that 16 times. Yeah. And so, and as you do that, you actually can see the change in your residuals get less and less and less.

> 我来解释为什么。如果我取一个 ImageNet 或 CIFAR10 的批次，我把它前向传播过模型，得到某个损失，然后反向传播、更新权重，接下来我会去取一个不同的批次。但他们做的却是把那件事做了 16 次。对。而随着你这样做，你实际上能看到残差的变化越来越小、越来越小、越来越小。

`[12:31]` **SPEAKER_01:** And why it actually makes sense is because when, in the RNN case, the ZL and the ZH, which are the carry, the task carry, start out as- Or the hidden states. The hidden states. Start out at zeros. Those are zeros. Then we go through this whole loopy recursion, at least the two loops, the two lower loops, the TL and TH steps.

> 而它之所以其实说得通，是因为在 RNN 的情形里，ZL 和 ZH——也就是那个进位、任务进位——一开始是——或者说是隐藏状态。隐藏状态。一开始是零。它们是零。然后我们经过这一整套循环递归，至少是那两个循环，那两个较低层的循环，TL 和 TH 步。

`[12:52]` **SPEAKER_01:** And then I back prop just through the two models. Just once. And I don't recurse all the way back. I do a stop grad, and I stop right there. And then there's a huge residual, and then I don't reset ZL and ZH.

> 然后我只穿过这两个模型做反向传播。只做一次。我不会一路递归回去。我做一次停止梯度（stop grad），就在那里停住。这时会有一个很大的残差，然后我不重置 ZL 和 ZH。

`[13:06]` **SPEAKER_01:** I do it again at a different point in the carry or hidden variable space. And so one can actually look at it as a different batch every time, even though it's the same exact axis.

> 我在进位空间、或者说隐变量空间的一个不同的点上再做一次。所以人们其实可以把它看成每次都是一个不同的批次，尽管它是完全相同的那个（数据）。

`[13:19]` **SPEAKER_00:** Yeah. Like the way I kind of think about it is like the 16 or whatever that you're recursing over, it's like constructing a mini batch, not from different inputs, but from different memory states basically. It's like across this hidden or carry memory access basically.

> 对。我大致是这么理解的：你递归的那 16 次或不管多少次，就像是在构造一个小批次（mini batch），不是用不同的输入，而是基本上用不同的记忆状态。基本上就是跨越这个隐藏的、或者说进位的记忆访问来构造的。

`[13:38]` **SPEAKER_01:** And that math holds, and it works. It follows DEQ directly in the event that the delta in ZL and the delta in ZH go to zero, which it actually doesn't do. And so we'll get to TRM. But Alexia- Yeah. It basically shows that it's just not the case, and you can't actually apply this math.

> 而那套数学是成立的，也管用。在 ZL 的增量（delta）和 ZH 的增量趋于零的情况下，它就直接遵循 DEQ——可实际上它并不会趋于零。所以我们接下来会讲到 TRM。但 Alexia——对。它基本上表明事实并非如此，你其实没法套用这套数学。

`[13:59]` **SPEAKER_01:** And that's why it's working. That's not sufficient support for why it's working. We actually don't know why it's really working. And she figures out that you actually can back prop through all the way to the deep recursion, which we're going to get into TRM in a second. And that actually improves performance much, much more.

> 而这就是它之所以有效的原因（存疑）。那并不足以解释它为什么有效。我们其实并不知道它到底为什么有效。而她（Alexia）弄明白了，你其实可以一路反向传播到深层递归——我们马上就会讲到 TRM。而那样做实际上把性能提升了非常非常多。

`[14:17]` **SPEAKER_00:** Interesting. OK. So before we get into TRM, yeah, on this paper, I think there's a bunch of different ways people have looked at this, right? In terms of... How they came up with it, and then why this may or may not be working.

> 有意思。好。那么在我们进入 TRM 之前——对，关于这篇论文，我觉得人们从很多不同的角度看待过它，对吧？就……他们是怎么想出来的，以及它为什么可能有效、又或许并不有效。

`[14:28]` **SPEAKER_00:** One, it's a sort of bio-plausibility argument. As you know, I'm usually not super keen on these. I think machine learning tends to have a long history of people starting with bio-plausible arguments and then realizing that there's some variant of them that seems highly bio-implausible that actually works better. I think you have example along those lines right there.

> 第一，它是一种生物学合理性（bio-plausibility）的论证。如你所知，我通常对这类论证不太感冒。我觉得机器学习往往有一段很长的历史：人们从生物学上合理的论证出发，然后意识到它们的某个变体——看起来在生物学上极不合理——反而效果更好。我想你手头就有沿着这个思路的例子。

`[14:45]` **SPEAKER_01:** Yeah. The classic, the first deep learning paper that started this whole craziness is AlexNet. And in AlexNet, there's actually this funny little thing called Local Receptive... Activation, or Depression, or something like that, where once this activation fires, then I have this refractory region or something like that, it actually doesn't work at all. And it didn't work, and you didn't need that, and then VGG came out and said, get rid of all that, just go deeper.

> 对。经典的、开启这整场疯狂的第一篇深度学习论文是 AlexNet。而在 AlexNet 里，其实有一个有趣的小东西，叫做局部感受……激活，或者抑制之类的，就是一旦这个激活被触发，我就有一个不应期区域（refractory region）之类的东西——它其实根本没用。它不管用，你并不需要它，然后 VGG 出来说：把那些统统去掉，直接加深就行。

`[15:10]` **SPEAKER_01:** It's like three by three. And three by three conv. And it actually just outperforms dramatically. And so this is always the case. Maybe you need to do it to get accepted into NeurIPS.

> 就是 3×3。用 3×3 的卷积。而它的表现确实就是大幅领先。所以情况总是如此。也许你需要那么做才能被 NeurIPS 接收。

`[15:18]` **SPEAKER_01:** Yeah, sure. Totally. Totally, yeah. You're definitely the expert here, but what do you consider to be bio-plausible and what's not?

> 对，没错。完全同意。完全同意，对。你在这方面肯定是专家，那你认为什么算是生物学上合理的，什么不算？

`[15:24]` **SPEAKER_00:** I think a lot of machine learning literature has overlapped a lot with people working in neuroscience. I think it is very natural for us to ask questions about how does our brain work, because our brain is like an incredible instrument that does a ton of computing, obviously, and does it in a very shockingly efficient manner, it seems like. And so a lot of machine learning research has, for a long time, sought analog from how we think to understand our brain to work and try to encode that in various machine learning systems. So from the very basic concept of what a neural network is, it's called a neural network because we think it's some basic model for what a neuron is, how certain activation functions work are meant to be inspired by certain biological premises.

> 我觉得很多机器学习文献与研究神经科学的人有大量重叠。我认为我们去追问大脑是如何工作的，是非常自然的，因为显然我们的大脑就像一台不可思议的仪器，做着海量的计算，而且似乎是以一种惊人高效的方式在做。所以很长一段时间以来，很多机器学习研究都从我们理解大脑运作的思考方式中寻找类比，并试图把它编码进各种机器学习系统。所以从神经网络最基本的概念说起——它之所以叫神经网络，是因为我们认为它是对神经元的某种基本建模；某些激活函数如何工作，本意就是要受某些生物学前提的启发。

`[16:03]` **SPEAKER_01:** Do you think that's a misnomer?

> 你觉得那是一种用词不当（误称）吗？

`[16:04]` **SPEAKER_00:** The thing about them is that often we use bio-plausibility to inspire us to come up with ideas, but we end up veering away from the bio-plausible to something adjacent to them that is likely bio-implausible, but that seems to work better.

> 关于它们，问题在于：我们常常用生物学合理性来启发自己想出点子，但最终我们会从生物学上合理的东西偏离出去，转向与之相邻、很可能在生物学上并不合理、但似乎效果更好的东西。

`[16:18]` **SPEAKER_01:** Something that runs better on a GPU. Exactly.

> 某种在 GPU 上跑得更好的东西。正是。

`[16:20]` **SPEAKER_00:** It runs better on a GPU, it's more efficient in some capacity that is relevant to how we actually encode it in a computational system. So I find thinking about bio-plausibility fun and interesting, and it's definitely a great way to inspire us to think about new things. But I tend to not be bounded by bio-plausibility when I think about what machine learning systems we should prioritize working on or think are particularly exciting, other than as an interesting scientific launching point for a deeper exploration. I think the version of this that I find more compelling is actually that original discussion we were having. It was around automata theory, basically, and honestly, just actually like fundamental data structures and algorithms theory, which is that if you're running a complex algorithm, having access to sort of a memory cache is actually very useful for being able to run that algorithm efficiently.

> 它在 GPU 上跑得更好，在某种与我们实际把它编码进计算系统相关的意义上更高效。所以我觉得思考生物学合理性既有趣又好玩，它绝对是启发我们思考新东西的好办法。但在我思考应该优先研究哪些机器学习系统、或者认为哪些特别令人兴奋时，我倾向于不被生物学合理性所束缚——除非把它当作一个有趣的科学起点，用来展开更深入的探索。我觉得这件事更让我信服的版本，其实是我们最初在进行的那场讨论。它基本上是围绕自动机理论（automata theory），说实话，其实就是最基础的数据结构与算法理论：如果你在运行一个复杂算法，能访问某种内存缓存，对于高效运行那个算法其实非常有用。

`[17:05]` **SPEAKER_00:** And I kind of think of this set of hidden states or carry as akin to a Turing machine tape or akin to the radix sort memory bank, where you can basically train a model to use this memory cache. And then you can do this in a more intelligent way in a single forward pass, so that you can get a more efficient time operation that would otherwise require some sort of more complicated reasoning. Yeah.

> 而我大致把这组隐藏状态或进位看成类似于图灵机的磁带，或者类似于基数排序的内存库（memory bank），在那里你基本上可以训练一个模型去使用这个内存缓存。然后你就能在一次前向传播中以更聪明的方式做到这一点，从而得到一个时间上更高效的操作，而这在其他情况下本来会需要某种更复杂的推理。对。

`[17:27]` **SPEAKER_01:** I think that a point I wanted to make earlier is that we did this COT stuff and this tool use thing as ways to get beyond the limitations of GPT-2. And so the way that we get... You can actually... I've done this experiment, you can actually, if you give me infinite amounts of unsorted list and sorted lists... If I can do chain of thought and I can do every single step and teach it to do every single step, then I can actually get it to do sort and become a Turing machine at test time.

> 我想我早些时候想说的一点是：我们搞出思维链（CoT）这套东西，以及工具使用这套东西，是作为超越 GPT-2 局限的手段。所以我们得到的方式是……你其实可以……我做过这个实验，你其实可以——如果你给我无穷多的未排序列表和已排序列表——如果我能做思维链，能把每一个步骤都做出来，并教它去做每一个步骤，那我其实就能让它完成排序，并在测试时变成一台图灵机。

`[18:02]` **SPEAKER_01:** And similarly, an even cheaper one that is much easier to do is you teach it and you say, hey, there's this Python function called sort. Just call the function. Just call the function. And I'm like, that's the easiest thing to do and you don't need back prop at all. And so those are the two hacks.

> 类似地，还有一种更省事、更容易做的办法：你教它，跟它说，嘿，有个叫 sort 的 Python 函数。你就调用这个函数。就调用这个函数。我就想，那是最省事的做法，而且你根本不需要反向传播。所以那就是那两种取巧的办法（hack）。

`[18:17]` **SPEAKER_01:** Now, well, Francois, this is solved. Like, we're done. Right? No. Because I needed to know what sort was.

> 那么，好吧，Francois，这不就解决了嘛。就好像我们搞定了。对吧？不对。因为我需要事先知道 sort 是什么。

`[18:23]` **SPEAKER_01:** What happens if we didn't know what merge sort is?

> 如果我们不知道归并排序（merge sort）是什么，会怎么样呢？

`[18:25]` **SPEAKER_00:** The chain of thought is not going to inherently discover sorting from first principles. It's finding it from our historical knowledge of everything it's trained on.

> 思维链本身不会从第一性原理出发去发现排序。它是从它训练过的所有历史知识里找到排序的。

`[18:32]` **SPEAKER_01:** Yeah. I mean, this is like the... The demos had this whole thing about like the ultimate test is the Einstein test. Like go back to 1911 and then like have it rebuild all the physics up until now. Similarly, let's just pretend that we only had bubble sort.

> 对。我是说，这就像……那些演示里有一整套说法，说终极测试是"爱因斯坦测试"。就好比回到 1911 年，然后让它把直到今天的所有物理学重新建立起来。类似地，我们就假装我们只有冒泡排序（bubble sort）。

`[18:44]` **SPEAKER_01:** We knew other... No other sort system. If you chain of thought it on all the bubble sort input and output. It will only do bubble sort. In fact, it won't even do bubble sort that well.

> 我们知道其他……没有别的排序系统。如果你用所有冒泡排序的输入和输出对它做思维链，它就只会做冒泡排序。事实上，它连冒泡排序都做不太好。

`[18:53]` **SPEAKER_01:** So this is the best situation. And then the tool use, of course, it can only know bubble sort. I want to get to merge sort. How do I discover merge sort?

> 所以这已经是最好的情况了。然后工具使用——当然，它也只能知道冒泡排序。可我想达到归并排序。我该怎么发现归并排序呢？

`[19:01]` **SPEAKER_00:** And I think the interesting thing just to emphasize here, because it may not have been extremely clear is there already exists some type of recursion that people are used to in LLMs, which is chain of thought we mentioned earlier. But that is a recursion that's happening in the token space of the model's outputs. Yeah. And that's inherent to the model itself. And that's sort of the fundamental limitation is that the model can only do a feed forward one shot output.

> 我觉得这里值得强调的一件有意思的事——因为它可能还不是特别清楚——是在 LLM 中已经存在某种人们习以为常的递归，也就是我们前面提到的思维链。但那是一种发生在模型输出的 token 空间里的递归。对。而那是模型本身固有的。而这某种程度上就是根本的局限：模型只能做一次性的前馈输出。

`[19:28]` **SPEAKER_00:** And then we basically just have this hack that if you keep letting it output things, then it can read its outputs and do somewhat intelligent seeming things with it. But it seems to sort of be upper bounded by the data that we feed it that the labs are very hungrily buying right now and not this sort of like inherent underlying recursive reasoning.

> 然后我们基本上就有这么一个取巧的办法：如果你不断让它输出东西，它就能读取自己的输出，并用这些输出做出一些看起来还算聪明的事情。但它似乎在某种程度上被我们喂给它的数据所限定住了——就是各大实验室现在正如饥似渴地购买的那些数据——而不是靠这种内在的、底层的递归推理。

`[19:47]` **SPEAKER_01:** Yeah. So in both cases. In both cases. If you're using hacks to solve this in COT and tool use, you're bounded by the bounds of human knowledge. In the event it's outside the set of human knowledge, then like you're kind of SOL.

> 对。所以在这两种情况下。在这两种情况下。如果你用思维链和工具使用这些取巧的办法来解决它，你就被人类知识的边界所限定。一旦要解决的东西落在人类知识集合之外，那你基本上就没辙了。

`[20:00]` **SPEAKER_01:** And so that's one. The other, you make a great point about discrete versus latent space. Reasoning in a discrete, it can only output the carry in the case of LLMs has to be snapped back to some discrete token space. And in the case of RNNs. Yeah.

> 所以那是其一。另一点——你关于离散空间与潜在空间的对比说得很好。在离散空间里推理——就 LLM 的情形而言，它只能把进位输出出来，而这必须被"吸附"回某个离散的 token 空间。而在 RNN 的情形里。对。

`[20:19]` **SPEAKER_01:** RNNs in general, they remain in this continuous latent space, which is much higher dimensional. If you give me like a tape that's this long and you cut it up into 10 buckets, like versus all the possible values. Right. Exactly. Yeah.

> 总体上，RNN 停留在这个连续的潜在空间里，而它的维度要高得多。如果你给我一条这么长的磁带，你把它切成 10 个桶——相比之下（连续空间）是所有可能的取值。对。正是。对。

`[20:32]` **SPEAKER_01:** It's much more expressive to being continuous space. But we can't train it that way because we actually, you know, because you're inhibited by back drop through time largely. And this is why this paper is so exciting.

> 处在连续空间要富有表达力得多。但我们没法那样去训练它，因为其实——你知道的——因为你在很大程度上被随时间反向传播所束缚。而这正是这篇论文如此令人兴奋的原因。

`[20:40]` **SPEAKER_00:** Okay. So before we then go over to the TRM paper, let's just summarize here. What matters most from the HRM paper that we should take away? Before we transition and contrast it with the TRM paper?

> 好。那么在我们转向 TRM 那篇论文之前，我们先在这里总结一下。从 HRM 这篇论文里，我们最应该带走的、最重要的东西是什么？在我们过渡并把它和 TRM 论文对比之前？

`[20:51]` **SPEAKER_01:** Yeah. I think that the number one piece to take away is this outer refinement loop. The outer refinement loop scales. And there's a great breakdown. Basically the Sapien authors, which huge kudos for this paper because there's so many innovations in this paper, didn't really do like a scaling ablations on every single one of the inputs.

> 对。我觉得第一个要带走的要点就是这个外层精炼循环。外层精炼循环是可扩展的（scales）。而且有一份很棒的拆解分析。基本上，Sapient 的作者们——这篇论文非常值得称赞，因为里面有太多创新——并没有真正针对每一个输入去做扩展性的消融实验。

`[21:17]` **SPEAKER_01:** But this guy, Constantine. Constantine at François Chalet's company, India, actually did. And it's this amazing breakdown that he posted on YouTube that you can go check out. But basically the main takeaway is that the outer refinement loops is the main beneficiary, is the main reason why these things work so well, which Alexia basically takes the, she found I think in parallel and scales up and shows that you can get rid of a lot of all this other stuff.

> 但有个人，Konstantin。在 François Chollet 的公司 Ndea 工作的 Konstantin，确实做了。这是他发在 YouTube 上的一份精彩拆解，你可以去看看。但基本上，主要的结论是：外层精炼循环是主要的受益者，是这些东西之所以效果这么好的主要原因——而 Alexia 基本上就抓住了这一点，我想她大概是独立地也发现了这一点，然后把它放大扩展，并表明你可以把其他所有那些东西都去掉一大堆。

`[21:46]` **SPEAKER_00:** It's a lot of machine learning. The follow on paper is basically delete 75% of the first paper, as we've often done in videos here, and keep the magic basically. So what's the magic then? What's the part that actually matters in terms of what stays in the TRM paper?

> 这很有机器学习的味道。这篇后续论文基本上就是把第一篇论文删掉 75%——就像我们在这里的视频中常做的那样——然后基本上把那个"魔法"留下来。那么魔法是什么呢？就 TRM 论文里保留下来的东西而言，真正重要的那部分是什么？

`[22:01]` **SPEAKER_00:** And let's now contrast the core architectural differences between these two papers.

> 那我们现在就来对比一下这两篇论文在核心架构上的差异。

`[22:05]` **SPEAKER_01:** Yeah. So I think that, I guess if I break it down into two major things, is this outer refinement loop thing is really great and works really well, and that this truncated back prop through time. Yeah. So truncated back prop through time, except I truncate at some time. Some earlier point.

> 对。我想，如果我把它拆成两大点，那就是：这个外层精炼循环非常棒、效果非常好；以及这种截断式的随时间反向传播（truncated backprop through time）。对。所谓截断式随时间反向传播，就是我在某个时刻把它截断。在某个更早的点上。

`[22:22]` **SPEAKER_01:** Earlier point. Yeah. Called T, T back. T equals one is actually completely sufficient. And so truncated back prop through time, T equals one, completely sufficient.

> 更早的点。对。叫做 T，T_back。T 等于 1 其实就完全足够了。所以截断式随时间反向传播，T 等于 1，完全足够。

`[22:31]` **SPEAKER_01:** And that's very counterintuitive.

> 而这非常反直觉。

`[22:33]` **SPEAKER_00:** Which is what HRM found.

> 这正是 HRM 所发现的。

`[22:34]` **SPEAKER_01:** Which is what HRM found. And TRM does a little bit further, rather than going through just one call to the H net and the L net, it actually goes through one full recursion loop. So if I do it 16 times, I just go back. I go back through one time. And that is kind of sufficient.

> 这正是 HRM 所发现的。而 TRM 又更进一步：与其只穿过对 H 网络和 L 网络的一次调用，它实际上穿过一整个递归循环。所以如果我做了 16 次，我就往回走。我往回穿过一次。而那大致就足够了。

`[22:52]` **SPEAKER_01:** And if you do it with this fixed point iteration thing, pseudo fixed point iteration thing, where you keep hitting it with gradient at every single step, it weirdly works. And this batch size across the carry space actually works.

> 而如果你用这种不动点迭代（fixed point iteration）的东西、这种伪不动点迭代的东西来做——就是你在每一步都不断给它施加梯度——它就奇怪地生效了。而这种跨越进位空间的"批量大小"其实是管用的。

`[23:08]` **SPEAKER_00:** So that part is also kept between these two models. It seemed like another thing that changed was having this sort of double layer of higher order thinking. And lower order thinking. It seems like it collapsed it down into just a single one. What's the intuition there?

> 所以那一部分在这两个模型之间也被保留了下来。看起来另一处改动是：原本有这种双层结构——高阶思考和低阶思考。看起来它把这个折叠成了单独一层。这里的直觉是什么？

`[23:23]` **SPEAKER_00:** And how does that actually work in the TRM paper?

> 而在 TRM 论文里，这实际上是怎么运作的？

`[23:25]` **SPEAKER_01:** Yeah, so it's interesting. She actually ablates having two separate networks versus just having one. I guess the more important space is the variable scope. Is that you should have low level features and high level features. But the same network.

> 对，这很有意思。她其实对"用两个独立的网络"和"只用一个网络"做了消融实验。我想更重要的地方在于变量作用域。也就是你应该同时拥有低层特征和高层特征。但用的是同一个网络。

`[23:36]` **SPEAKER_01:** And so the best performance model.

> 所以性能最好的那个模型。

`[23:37]` **SPEAKER_00:** The same network can extract both, basically.

> 基本上，同一个网络就能提取出两者。

`[23:39]` **SPEAKER_01:** Yeah. You weight share between the L net and the H net, and it's just called net. And you do just one transformer layer versus the four like they do in C. Yeah. And then you do one transapient and just whittle it down to one and do more recursion.

> 对。你在 L 网络和 H 网络之间共享权重，它就叫做 net。而且你只用一个 Transformer 层，而不是他们（Sapient 那篇）用的四层。对。然后你把它削减到一层，转而做更多的递归。

`[23:52]` **SPEAKER_01:** But you keep ZL and ZH to be distinct and separate. And she calls it X and Y, which I found very confusing. X, Y, Z. It was just very confusing. And it's just like ZH and ZL is just cleaner.

> 但你让 ZL 和 ZH 保持各自不同、彼此独立。而她把它们叫做 X 和 Y，这让我觉得非常混乱。X、Y、Z。真的很让人糊涂。而用 ZH 和 ZL 就是更清爽。

`[24:04]` **SPEAKER_00:** So if you read the paper, Y is actually like latent space. It's like Z, basically.

> 所以如果你读那篇论文，Y 其实就像是潜在空间。它基本上就相当于 Z。

`[24:08]` **SPEAKER_01:** And it is not a label. Yeah. Okay. Which really threw me through a loop. Whatever, yeah.

> 而它并不是标签（label）。对。好吧。这真的把我搞懵了。算了，对。

`[24:13]` **SPEAKER_01:** But anyway, we'll go through some code here and I'll walk you through it. So I've replaced all of her nodes. Yeah. Yeah. I've used the old term and use the sapient notation, which is much cleaner and more straightforward to me at least.

> 但无论如何，我们这里会过一些代码，我会带你一步步看。所以我把她的所有节点都替换掉了。对，对。我用了旧的术语、用了 Sapient 的记号，至少对我来说那要清爽、直白得多。

`[24:23]` **SPEAKER_00:** Okay, cool. And now before we dive into the code for a sec, like in terms of how these TRMs actually work, it's pretty interesting. Because this recursion advantage now gives you a bunch of advantages over transformers. Rather than having, you know, 500 or a thousand or a million or whatever transformer layers and having tons and tons of parameters, you get compute depth basically without this parameter depth. Right.

> 好，酷。那现在，在我们扎进代码之前先说一下：就这些 TRM 实际如何工作而言，这相当有意思。因为这种递归的优势现在给了你一堆相对于 Transformer 的好处。与其拥有——你知道的——500 层、一千层、一百万层之类的 Transformer 层、拥有海量海量的参数，你基本上是在没有这种参数深度的情况下获得了计算深度。对。

`[24:47]` **SPEAKER_00:** And the optimization process looks like more of like an iterative kind of like expectation maximization algorithm. Do you want to talk about how that worked in the TRM paper? Because I thought that was also pretty interesting.

> 而这个优化过程看起来更像是一种迭代式的、类似期望最大化（expectation maximization）的算法。你想谈谈它在 TRM 论文里是怎么运作的吗？因为我觉得那也相当有意思。

`[24:57]` **SPEAKER_01:** So both of them kind of have the same kind of EME feeling thing, where like we update ZL, condition upon the input X and ZH, the last ZH, ZH t minus one, let's say. And then we keep updating ZL, ZL, ZL, ZL, ZL, and we keep updating it. And then we go holding, we update ZH, condition upon ZL, and actually it's just ZL, it's not even X. And then we just update ZH. And the way to think about ZL and ZH is ZL is like your local scoped variables that are just being overwritten and updating, updating, updating.

> 所以它们两个大致都有同一种"EM 的感觉"的东西：我们更新 ZL，条件是输入 X 和 ZH——上一个 ZH，比方说 ZH_{t-1}。然后我们不断地更新 ZL、ZL、ZL、ZL、ZL，不停地更新它。接着我们再固定住，更新 ZH，条件是 ZL——其实就只是 ZL，甚至连 X 都不用。然后我们就更新 ZH。而理解 ZL 和 ZH 的方式是：ZL 就像是你局部作用域的变量，不断被覆盖，不断更新、更新、更新。

`[25:37]` **SPEAKER_01:** And then ZH, and Azalea makes this point, sorry, Azalea, Alexia makes this point, that is, that is a candidate answer, a proposed answer. A proposed latent answer that is just an embedding space away, one MLP lookup away from the true answer.

> 然后是 ZH——Azalea 提到了这一点，抱歉，Azalea，是 Alexia 提到了这一点——那就是一个候选答案、一个被提议的答案。一个被提议的潜在答案，它距离真正的答案只差一个嵌入空间、差一次 MLP 查表。

`[25:54]` **SPEAKER_00:** So you're kind of like EMing, just to like zoom out a little bit. You're kind of maximizing the probability of the correct, you know, information stored in your memory, conditioned on a given output, and maximizing the right output conditioned on the information stored in your memory, quote unquote, in parallel. And like that optimization algorithm leads to... you ultimately learning a recursive method that stores the right information to this local memory, basically. Yeah.

> 所以你大致是在做 EM——稍微拉远一点看。你大致是在最大化"存储在你记忆里的正确信息"的概率——以给定输出为条件；同时又并行地最大化"正确的输出"——以存储在你记忆里的信息（姑且这么叫）为条件。而这样的优化算法会导致……你最终学到一种递归的方法，它基本上会把正确的信息存进这块局部记忆里。对。

`[26:25]` **SPEAKER_00:** And then outputs the right thing.

> 然后输出正确的东西。

`[26:26]` **SPEAKER_01:** It really, like, if we actually think of Sudoku, it's actually a really natural way to think about what's actually happening under the hood. Where Sudoku is an incomplete puzzle. You can't guess every cell at any one time. You can, actually it's designed where you can only guess one or two cells based on the available information. So it's not, it's an incompressible problem.

> 它真的——如果我们真去想数独，其实这是一种非常自然的方式去理解底层到底在发生什么。数独是一个不完整的谜题。你没法在任何一个时刻就把每个格子都猜出来。其实它的设计就决定了，你基于现有信息一次只能猜出一两个格子。所以它不是……它是一个不可压缩的问题。

`[26:43]` **SPEAKER_01:** You actually can't do it unless you're just randomly guessing and guessing and guessing, which is... it's a very high combinatorial space. And so what the ZL is doing is some type of, let me try this, try that, do some computation, think about little things, and then it proposes, and then we go to condition upon, like, something that it may have found, it sends it to ZH, ZH fills it in, and now we have a little bit more of a filled in Sudoku puzzle.

> 你其实做不到，除非你只是不停地随机猜、猜、猜——那是一个组合空间非常巨大的问题。所以 ZL 所做的，是某种"让我试试这个、试试那个，做点计算，想一些小的东西"，然后它给出一个提议，然后我们以它可能发现的某样东西为条件，它把这个传给 ZH，ZH 把它填进去，于是现在我们就有了一个多填了一点点的数独谜题。

`[27:07]` **SPEAKER_00:** And the training process is training the algorithm to know to do that, right? It's like, it's maximizing that, it's like, oh, this strategy for what you save tends to lead to correctness. Correct outputs.

> 而训练过程就是在训练这个算法，让它懂得去这么做，对吧？就好比，它在最大化那个——就像是，哦，你所保存的东西的这套策略往往会通向正确性。通向正确的输出。

`[27:18]` **SPEAKER_01:** Without chain of thought.

> 而且不用思维链。

`[27:19]` **SPEAKER_00:** Without chain of thought, exactly.

> 不用思维链，正是如此。

`[27:20]` **SPEAKER_01:** That's the most important part. It's like, if we had Sudoku and we knew how to solve Sudoku, because, like, we were just, you know, dumb homo sapiens that didn't know how to solve Sudoku, like, it would just have solved it. And that's why it's cool, because it actually is able to discover things without being teacher forced via chain of thought. Right.

> 那是最重要的部分。就好比，如果我们有数独，而我们本来知道怎么解数独——因为，比如说，我们只是不懂怎么解数独的、笨笨的智人——那它就会（自己）把它解出来。这就是它很酷的地方，因为它其实能够在不通过思维链被"教师强制"（teacher forcing）的情况下发现东西。对。

`[27:37]` **SPEAKER_00:** Interesting, yeah. Should we look at some code? Let's do it. Okay, let's dive in. And I would love to see what these papers or bottles look like just distilled down to their core essence.

> 有意思，对。我们要不要看点代码？来吧。好，我们扎进去。我很想看看这些论文提炼到只剩其核心本质时是什么样子。

`[27:47]` **SPEAKER_00:** I know there's lots of details on how you train them, but kind of the core training algorithm. And it'd be great to contrast the two methods. Yeah.

> 我知道关于怎么训练它们有很多细节，但（我想看）大致的核心训练算法。而且能把这两种方法对比一下就太好了。对。

`[27:53]` **SPEAKER_01:** So, I mean, they're remarkably similar. And so, largely one, and learning one is learning the other. But basically, you start out with some ZH and ZL that are just zeros. You have some input embedding space to go from X raw to X, which is the maze state or whatever it is, initial maze state. And then with no grad, you don't pass any gradients back through this.

> 那么，我是说，它们出奇地相似。所以很大程度上，学会一个就等于学会了另一个。但基本上，你从某个 ZH 和 ZL 开始，它们就是零。你有某个输入嵌入空间，用来从原始的 X（X_raw）变换到 X，也就是迷宫状态或不管它是什么，初始迷宫状态。然后在 no_grad 之下，你不让任何梯度经由这里回传。

`[28:16]` **SPEAKER_01:** You...

> 你……

`[28:17]` **SPEAKER_00:** This is the trick, basically. This is the trick. To not back prop through time.

> 这基本上就是那个技巧。这就是那个技巧。就是不做随时间反向传播。

`[28:20]` **SPEAKER_01:** Yeah. Here are two of the three recursion levels. So, yeah, this is like the... They do this just for simplicity, but I hit ZL, T low times. And then once for modulo, T low, then I hit the ZH and I do it again and again.

> 对。这里是三层递归中的两层。所以，对，这就像是……他们这么做只是为了简洁，但我把 ZL 击打 T_low 次。然后每隔 T_low（取模）一次，我就击打一下 ZH，然后我一遍又一遍地做。

`[28:38]` **SPEAKER_01:** And like you said, I'm updating ZL condition upon ZH and X. Right. And then I update ZH condition upon ZL.

> 而就像你说的，我在更新 ZL，条件是 ZH 和 X。对。然后我更新 ZH，条件是 ZL。

`[28:45]` **SPEAKER_00:** Right. So, this is like the expectation maximization style approach. Exactly.

> 对。所以这就像是期望最大化风格的做法。正是。

`[28:49]` **SPEAKER_01:** Yeah. And then you don't really need this. This is like just for cleanliness to show clearly that there's no gradients occurring above this line.

> 对。然后你其实并不需要这个。这只是为了整洁，好清楚地表明在这条线以上没有发生任何梯度。

`[28:57]` **SPEAKER_00:** Basically freezing the weights past that.

> 基本上就是把那之后的权重冻结住。

`[28:58]` **SPEAKER_01:** Exactly. And then I hit L net and H net one more time.

> 正是。然后我再击打一次 L 网络和 H 网络。

`[29:01]` **SPEAKER_00:** And then... Which is the same thing as up above. So, this is just... Okay. It's literally just the no grad thing running one more time.

> 然后……这和上面那个是同一件事。所以这只是……好。它字面上就是那个 no_grad 的东西再运行一次。

`[29:06]` **SPEAKER_01:** Exactly. Cool. Yeah. And just make it really clear. And then there you go.

> 正是。酷。对。就是把它讲得很清楚。然后就是这样了。

`[29:11]` **SPEAKER_01:** And that's your HRM model. Cool. And they use... That's quite simple. Yeah.

> 那就是你的 HRM 模型了。酷。他们用……这相当简单。对。

`[29:16]` **SPEAKER_01:** It's actually sufficient. If you actually go much higher, Konstantin showed very clearly that it doesn't actually help.

> 它其实就够了。如果你真把（层数/步数）加得高很多，Konstantin 非常清楚地表明那其实并没有帮助。

`[29:22]` **SPEAKER_00:** So, that's two of the three recursions you said. The third happens in the actual train loop.

> 所以，那是你说的三层递归中的两层。第三层发生在实际的训练循环里。

`[29:26]` **SPEAKER_01:** The third is in the train loop and at the test loop. They both have this M test or N supervision, which Alexia calls deep supervision. They call it adder refinement steps. It's just whatever you want to call it, call it NSUP.

> 第三层在训练循环里，也在测试循环里。它们都有这个 M_test，或者叫 N 监督（supervision），Alexia 把它叫做深度监督（deep supervision）。他们（HRM 那篇）把它叫做外层精炼步骤。随便你想怎么叫，就叫它 N_SUP。

`[29:40]` **SPEAKER_00:** And so, you do this NSUP times during training and then during test time, there's a different hyperparameter. So, for how many times it recurses over each model, which is M test, basically. They're actually the same.

> 所以，你在训练时做 N_SUP 次，然后在测试时，有一个不同的超参数。就是它在每个模型上递归多少次，基本上就是 M_test。其实它们是一样的。

`[29:50]` **SPEAKER_01:** Okay. And so, this and this, we can probably just call this the same. Yeah. But it's the same. And if you actually...

> 好。所以，这个和这个，我们大概可以就把它当成一样的。对。但它就是一样的。而如果你真的……

`[29:59]` **SPEAKER_01:** Konstantin does a good job of this. If you actually train on 16 and you test on only one, you get like seven eighths of the performance or almost all the performance. So, it's actually quite interesting. This is just redundant, too much compute, and it doesn't actually help you all that much. So, setting this to one is actually like...

> Konstantin 在这件事上做得很好。如果你实际上用 16 来训练，而在测试时只用 1，你能得到大概八分之七的性能，或者说几乎全部的性能。所以这其实相当有意思。这（更多的测试时递归）只是冗余、太多算力，而它其实并没有帮到你多少。所以把它设为 1 其实就像是……

`[30:21]` **SPEAKER_00:** But presumably for like more complicated problems, having more test time compute is still useful is like the reason you would set it up this way.

> 但想必对于更复杂的问题，拥有更多的测试时算力仍然是有用的，这大概就是你会这样设置它的原因。

`[30:28]` **SPEAKER_01:** Yeah, for sure. And so, we call our HRM, we get some loss, we back prop through just those two little parts here, and then we step, we zero out the gradient, but we do not update ZH and ZL. These are still the same in it, so that's the really important detail there. Right. And then so we go back, we pass in the ZH and the ZL from the previous one, so now this is actually not the same batch.

> 对，当然。所以，我们调用我们的 HRM，得到某个损失，我们只穿过这里这两个小部分做反向传播，然后我们做一步优化（step），把梯度清零，但我们不更新 ZH 和 ZL。它们保持不变，所以那是这里非常重要的一个细节。对。然后我们回过头去，把上一次的 ZH 和 ZL 传进去，所以现在这其实就不是同一个批次了。

`[30:54]` **SPEAKER_01:** Right. Because we have updated ZH and ZL, so it's in a different part of the latent space.

> 对。因为我们已经更新了 ZH 和 ZL，所以它处在潜在空间的一个不同的部分。

`[30:59]` **SPEAKER_00:** Cool. Yeah. And that's the key like mini batch construction through memory space concept. Yeah.

> 酷。对。而那就是那个关键的概念——通过记忆空间来构造小批次。对。

`[31:05]` **SPEAKER_01:** Exactly. Yeah, cool. Exactly. And then at test time, it's simply the three loops. So, there's your outer refinement loop, which turns out like just at train time...

> 正是。对，酷。正是。然后在测试时，就只是那三个循环。所以那里有你的外层精炼循环，结果表明它就像在训练时……

`[31:13]` **SPEAKER_01:** Doesn't matter. Train time recursion was important, but test time recursion was actually not that important, which is kind of counterintuitive. And then the HRM inside that has your two other loops. Makes sense. And that's it.

> 无关紧要。训练时的递归很重要，但测试时的递归其实并没那么重要，这有点反直觉。然后其中的 HRM 里有你另外那两个循环。说得通。就是这样。

`[31:24]` **SPEAKER_01:** So, pretty simple. Okay. Now the TRM. And now for the only two changes, the main two changes here is that they collapse, LNet and HNet into just net. Great.

> 所以，相当简单。好。现在来看 TRM。现在说说仅有的两处改动，这里主要的两处改动是：他们把 L 网络和 H 网络折叠成单独一个 net。很好。

`[31:34]` **SPEAKER_01:** And it's important detail. These are four transformer layers, this is four transformer layers, and this is just one transformer layer. Yeah. Yeah. So, this actually shows that going deeper actually didn't help.

> 而这是个重要的细节。这些是四个 Transformer 层，这个是四个 Transformer 层，而这个就只是一个 Transformer 层。对。对。所以这实际上表明，加深其实并没有帮助。

`[31:44]` **SPEAKER_00:** Yeah. And actually on some tasks, it was just the feed forward net actually worked just as well as the transformer there, right? Yeah.

> 对。而且实际上在某些任务上，只用前馈网络其实就和那里的 Transformer 一样好，对吧？对。

`[31:49]` **SPEAKER_01:** And the MLP. It was like on Sudoku, I think. Yeah. On Sudoku, MLP actually outperformed the attention. It scored zero on the maze, the MLP scored zero on the maze.

> 还有那个 MLP。我想是在数独上。对。在数独上，MLP 其实胜过了注意力机制。它在迷宫上得了零分，那个 MLP 在迷宫上得了零分。

`[31:57]` **SPEAKER_01:** And so, it's not clear, it's not obvious that the transformer is always better. So, there's the weight sharing. And then instead of going back just the one, two, the H, this back propping through just these two, you actually back prop through one latent recursion step, all the way through one latent recursion step. So, let me just walk through this a little bit. So, we have the same thing here.

> 所以，并不清楚、并不显然 Transformer 总是更好。那么，这里有权重共享。然后，与其只往回走那一两步、走到 H、只穿过这两步做反向传播，你实际上是穿过一个潜在递归步骤做反向传播，一路穿过一个完整的潜在递归步骤。那我稍微带你过一下这个。所以，我们这里有相同的东西。

`[32:22]` **SPEAKER_01:** Same starting point, yeah. It's mainly the same thing here. We're doing this six times. And then we go one more time here. And then we do our deep recursion.

> 相同的起点，对。这里主要是相同的东西。我们把这个做六次。然后我们在这里再做一次。然后我们做我们的深层递归。

`[32:32]` **SPEAKER_01:** This is the outer loop, N sub times. And so, again, we have the no grad, we have the detach. And then this is where it's different. So, I am calling this latent recursion after the detach.

> 这是外层循环，做 N_sub 次。所以，再一次，我们有 no_grad，我们有 detach（分离梯度）。然后这就是不同的地方。所以我是在 detach 之后调用这个潜在递归的。

`[32:45]` **SPEAKER_00:** Yeah. So, it's one full recursive loop is happening versus here.

> 对。所以，（在 TRM 里）发生的是一整个完整的递归循环，而不是（HRM）这里（只穿过两步）。

`[32:49]` **SPEAKER_01:** And so, that's the main difference in the optimization, otherwise it's effectively the same. And then it outputs, and then you're good to go. And you train it exactly as the same way before. And then at test time, it's the same thing again. And so, largely the same.

> 所以，那就是优化上的主要差异，除此之外它实际上是一样的。然后它输出，然后你就大功告成了。你完全按照之前一样的方式训练它。然后在测试时，又是同样的东西。所以，大体上是一样的。

`[33:05]` **SPEAKER_00:** Cool. And so, in many ways, it's sort of a simplification, right? You're collapsing certain parts of it. You're simplifying this net arc. You're simplifying the architecture.

> 酷。所以在很多方面，它某种程度上是一种简化，对吧？你把它的某些部分折叠了。你在简化这个 net 架构。你在简化这个架构。

`[33:14]` **SPEAKER_00:** It's slightly more complicated along this back prop through time part because you're actually back propping through more than you did before. But it's like taking a bunch of lessons from the first one and basically simplifying most of it.

> 在随时间反向传播这部分它稍微更复杂了一点，因为你实际上比之前穿过了更多的步骤做反向传播。但它就像是从第一篇里吸取了一堆经验，然后基本上把其中大部分都简化了。

`[33:24]` **SPEAKER_01:** Right. Which is actually why she needs, I think, is why she needs to make the model smaller. And so, it's a 28 million parameter model for HRM. Now she brings it down to a 7 million parameter model and it actually gets from 70% to 87% on ArcPrize 1.

> 对。我觉得这其实就是她为什么需要把模型做得更小的原因。所以，HRM 是一个 2800 万参数的模型。现在她把它降到一个 700 万参数的模型，而它实际上在 ARC Prize 1 上从 70% 提升到了 87%。

`[33:41]` **SPEAKER_01:** And it's actually quite well on ArcPrize 2 as well. And so, yeah. So, she makes the model three, four times smaller. But because it has that recursion, it actually outperforms. And there's this researcher named Melanie Mitchell that writes this book talking about this very phenomenon, which is like it is sufficient, not necessary, to go bigger and get better performance.

> 而且它在 ARC Prize 2 上其实也表现得相当好。所以，对。她把模型做小了三到四倍。但因为它有那种递归，它实际上表现更好。有一位叫 Melanie Mitchell 的研究者写了一本书，谈的正是这个现象，也就是说：把模型做得更大从而获得更好的性能，是充分的，而非必要的。

`[34:08]` **SPEAKER_01:** And it is sufficient and not necessary to add more. Yeah. Yeah. Yeah. Yeah.

> 而增加更多，也是充分而非必要的。对。对。对。对。

`[34:11]` **SPEAKER_01:** Yeah. Yeah. Yeah. And so, you can get a lot more recursion. And so, where I'm really excited is what happens if you do both.

> 对。对。对。所以，你可以获得多得多的递归。所以，我真正感到兴奋的地方是：如果你把两者都做了会怎么样。

`[34:15]` **SPEAKER_01:** Right. And you're still limited by back prop through time. Even Alexia is limited by that last step from a memory perspective for sure. And so, if you can make the model really big and you have lots of recursion and we do something else other than back prop through time, then we can get exact all the benefits of this and all the benefits of the giant LLMs. And then you can get some crazy stuff.

> 对。而你仍然被随时间反向传播所限制。即便是 Alexia，从内存的角度看，肯定也被那最后一步所限制。所以，如果你能把模型做得非常大、又有大量的递归，而我们用某种不同于随时间反向传播的东西来做，那我们就能同时获得这（递归）的全部好处和巨型 LLM 的全部好处。然后你就能得到一些疯狂的东西。

`[34:39]` **SPEAKER_00:** So, now to wrap up. Why don't we talk a little bit about the bigger picture? What does this mean for the field of AI research? How should people think about where these models fit into the current span of research happening, especially given that it seems like a bit of a departure from a lot of the methods that people are used to hearing about and increasingly seeing products that people use?

> 那么，现在来收个尾。我们不妨谈谈更宏观的图景？这对 AI 研究领域意味着什么？人们应该如何看待这些模型在当前正在进行的研究版图中所处的位置——尤其是考虑到，它似乎与人们习惯听到的、并且越来越多地在所用产品中看到的很多方法有点偏离？

`[34:57]` **SPEAKER_01:** Well, I think for one, from the arguments that Schmidhuber makes and that we've talked about today, recursion is important and it's not going away. And clearly the benefit is here of adding recursion into models and you've seen things like the recursion language models out of Google that are pretty powerful and cool. And so that's definitely one piece that's, I don't think, going away anytime soon. The next one is this add a refinement loop, like back t, tb, tt, like t equals one, truncated back wrap through time t equals one. I think that that is a really powerful idea and the fact that that works so well, we have yet to really explore that extremely, really understand what's happening there.

> 嗯，我觉得首先，从 Schmidhuber 提出的、以及我们今天谈到的那些论点来看，递归很重要，而且它不会消失。而把递归加进模型的好处显然就在这里，你已经看到过像 Google 出的递归语言模型（recursion language models）那样的东西，相当强大也很酷。所以那绝对是我认为短期内不会消失的一块。接下来一块是这个外层精炼循环，比如 back_t、T_b、T_t，比如 T 等于 1，截断式随时间反向传播、T 等于 1。我觉得那是一个非常强大的想法，而它效果如此之好这件事，我们还没有真正极其深入地去探索它、真正理解那里到底在发生什么。

`[35:37]` **SPEAKER_01:** And then the third is that idea of like, okay. Okay. We know that recursion works. We have these tiny recursive models that are seven million parameters that can solve what a hundred million, a hundred billion, a trillion parameter model can't solve trained on the entire internet and a seven million parameter wins. Like the right answer is to like take the amazingness here and take the amazingness here, which probably is already in Gemini already or some of these, it might be at least in some part.

> 然后第三点是这么个想法，好吧。好吧。我们知道递归是管用的。我们有这些七百万参数的微型递归模型，它们能解决那些用整个互联网训练的一亿、一千亿、一万亿参数的模型都解不了的问题，而一个七百万参数的模型赢了。那么正确的答案就是把这边（递归）的了不起之处和那边（巨型模型）的了不起之处结合起来——那可能在 Gemini 里已经有了、或者在其中一些模型里，至少可能已经有了一部分。

`[36:08]` **SPEAKER_01:** But when you, when you take. The benefit of both these TRMs and these giant models and you actually slam them together, I think that it's just going to take off and it's going to be really huge.

> 但当你、当你把这些 TRM 和这些巨型模型两者的好处都拿过来，真正把它们硬凑到一起，我觉得它就会一飞冲天，会非常非常巨大。

`[36:18]` **SPEAKER_00:** Yeah. One of the things that's really interesting about these TRMs and HRMs is they're not general purpose models, right? These were task specific models, right? The model trained to do Sudoku cannot do ArcPrize inherently, it has to be trained on the ArcPrize set to do so versus the LLMs that are used on these tasks are general purpose models that maybe get some additional fine tuning data or in context learning data on those tasks. And so I think that's where the interesting overlap might come is if you can make these more general purpose agents that can somehow be general purpose in the way that the sort of next token prediction algorithm has given us and do more complex reasoning to achieve that.

> 对。关于这些 TRM 和 HRM，一个真正有意思的地方是它们不是通用模型，对吧？它们是任务专用的模型，对吧？训练来做数独的模型本质上做不了 ARC Prize，它必须在 ARC Prize 的数据集上训练才能做到；而用在这些任务上的 LLM 是通用模型，可能只是在那些任务上获得了一些额外的微调数据或上下文学习数据。所以我觉得有意思的交汇点可能就在这里：如果你能把这些做成更通用的智能体，让它们能够以某种"下一个 token 预测算法"所赋予我们的方式变得通用，并且做更复杂的推理来实现这一点。

`[36:53]` **SPEAKER_00:** It seems like you can have really efficient architectures to do scale up reasoning.

> 看起来你可以拥有非常高效的架构来扩大推理规模。

`[36:57]` **SPEAKER_01:** Right. And like a lot of the view of what these LLMs are doing is finding really amazing embedding representation spaces, but reasoning inside that, that space is actually not done all that much.

> 对。而对这些 LLM 在做什么的很多看法是：它们在寻找真正了不起的嵌入表示空间，但在那个空间内部进行推理，其实做得并不多。

`[37:08]` **SPEAKER_00:** It's always through the token space.

> 它总是通过 token 空间来进行的。

`[37:10]` **SPEAKER_01:** It's always through the token space. And so like what you can imagine is we found mapping from token space or from vision, from pixels, some really cool latent space where like things are just nicely semantically separated and we can, you know, makes it really easy for downstream tasks to do. But now in that space, use this like tiny reasoning models, use some type of recursion inside that and train those, those, those, that model on that, a little small model on that reasoning space. That's really going to work.

> 它总是通过 token 空间。所以你可以想象的是：我们找到了从 token 空间、或者从视觉、从像素出发的某个非常酷的潜在空间，在那里各种东西都被很好地在语义上分开了，而我们可以——你知道的——让下游任务做起来非常容易。但现在，在那个空间里，用这种微型推理模型，在其中用某种递归，然后在那上面训练那些、那些、那个模型，在那个推理空间上训练一个小小的模型。那真的会管用。

`[37:40]` **SPEAKER_00:** Francois, thanks so much for breaking it all down for us. See you all in the next episode of Decoded. Thank you.

> Francois，非常感谢你为我们把这一切都拆解清楚。我们下一期 Decoded 再见。谢谢。
