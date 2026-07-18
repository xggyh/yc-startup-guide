# 全文转录 · 为什么只靠 Scaling 造不出 AGI:François Chollet 谈符号程序合成、可验证奖励与创业机会

> ▶ [YouTube](https://www.youtube.com/watch?v=k2ZLQC8P7dc) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/k2ZLQC8P7dc.md) &nbsp;·&nbsp; François Chollet: Why Scaling Alone Isn't Enough for AGI

> 中英对照 · 每段英文原文下附中文翻译

[00:00] **SPEAKER_03:** I think we're probably looking at AGI 2030, around the time that we're going to be releasing like maybe ARC 6 or ARC 7. You're not going to stop AI progress. I think it's too late for that. And so the next question is, okay, like AI progress is here. It's actually going to keep accelerating. How do you make use of it? How do you leverage? How do you ride the wave?

> 我认为我们大概会在 2030 年左右迎来 AGI，差不多就是我们要发布 ARC 6 或 ARC 7 的时候。你无法阻止 AI 的进步，我觉得现在为时已晚。所以接下来的问题是：好吧，AI 的进步已经到来了，而且实际上还会不断加速。你要如何利用它？如何借力？如何驾驭这股浪潮？

[00:22] **SPEAKER_01:** That's the question to ask. Today, we're lucky to be joined by Francois Chollet, founder of the ARC Prize, a global competition to solve the ARC AGI benchmark. His latest project is NDIA, a lab exploring a new paradigm in frontier AI research. Francois is one of the best people in the world to help us understand the current AI moment and where all of this is going. Francois, thank you so much for joining us today and congrats on the launch of ARC AGI V3.

> 这正是我们要问的问题。今天我们很荣幸邀请到了 Francois Chollet，他是 ARC Prize 的创始人——这是一个旨在攻克 ARC AGI 基准测试的全球竞赛。他最新的项目是 NDIA，一个探索前沿 AI 研究新范式的实验室。要理解当下的 AI 时刻以及这一切的走向，Francois 是世界上最合适的人选之一。Francois，非常感谢你今天参加我们的节目，也祝贺你推出 ARC AGI V3。

[00:58] **SPEAKER_03:** Thanks so much for having me. I'm super excited to be here. Super exciting time to talk about AI.

> 非常感谢你们邀请我，我非常兴奋能来到这里。现在是谈论 AI 的绝佳时刻。

[01:02] **SPEAKER_04:** So Francois, tell us a little bit about NDIA. So what exactly is it and what are you guys trying to achieve?

> Francois，跟我们讲讲 NDIA 吧。它究竟是什么，你们想要达成什么目标？

[01:08] **SPEAKER_03:** Right. So NDIA is this new AGI research lab, and we are trying some very different ideas. And so our goal is basically to build this new branch of machine learning that will be much closer to

> 好的。NDIA 是一个新的 AGI 研究实验室，我们正在尝试一些非常不同的想法。我们的目标基本上是构建一个全新的机器学习分支，它会更加接近……

[01:20] **SPEAKER_01:** optimal, unlike deep learning. All of us right now are sort of taken by what's going on with code. I have sort of this viral moment right now where I got to 40,000 stars this morning. Oh, wow. On G-Stack. So it's like, oh, this is an open source project that now is one of the biggest ones. And I

> ……最优，不像深度学习。我们现在都有点被代码领域正在发生的事情吸引住了。我最近也经历了一个爆红时刻——今天早上我的 star 数达到了四万。哦，哇。就是在 G-Stack 上。所以感觉就是，哦，这个开源项目现在成了最大的项目之一。而且我……

[01:38] **SPEAKER_01:** have more than 100 PRs from contributors to deal with. I guess you're one of the best people to talk to about this because you're actually literally coming up with something that is a totally different pathway.

> ……还有一百多个来自贡献者的 PR 要处理。我想你是最适合聊这个话题的人之一，因为你实际上真的在提出一条完全不同的路径。

[01:51] **SPEAKER_03:** That's right. That's right. So what we're doing at NDIA is we're doing program synthesis research. And when I talk about program synthesis, often people ask me, oh, so are you doing like Cogen? Are you building an alternative? Are you building a new project? Are you building an alternative?

> 没错，没错。我们在 NDIA 做的是程序合成（program synthesis）研究。每当我谈到程序合成时，人们常问我：哦，那你们是在做类似代码生成（Cogen）的东西吗？你们是在构建一个替代方案吗？是在做一个新项目吗？是在构建一个替代品吗？

[02:02] **SPEAKER_03:** I'm actually building an alternative to coding agents. And it's actually not at all what we are doing. We are working at a much, much more, much lower level than that. What we're actually doing is that we are trying to build a new branch of machine learning, an alternative to deep learning itself, rather than like coding agents. Coding agents are like this very, very high level, last layer piece of the stack. And we're actually trying to rebuild the whole stack

> 是不是在构建编程智能体（coding agents）的替代品？其实完全不是我们在做的事情。我们工作的层次要比那低得多得多。我们真正在做的，是试图构建一个新的机器学习分支，一个针对深度学习本身的替代方案，而不是编程智能体那样的东西。编程智能体是整个技术栈中非常非常高层、最顶端的那一层。而我们实际上是想在……

[02:26] **SPEAKER_03:** on top of different foundations. So we're building a new learning substrate that's very, very different from parametric learning, deep learning. So if you go back to the problem of machine learning, you have some input data, some target data, and you're trying to find a function that will map the inputs to the targets and that will hopefully generalized to new inputs. And if you're doing deep learning, what you're doing is that you have this parametric curve that serves as your function, as your model, and you're trying to fit the parameters of the curve gradient descent. And this is basically basically what we are doing, except we are replacing the parametric curve with a symbolic model that is meant to be as small as possible. It's like the simplest possible model to

> ……不同的地基之上重建整个技术栈。所以我们在构建一种全新的学习基底（learning substrate），它与参数化学习、深度学习非常非常不同。回到机器学习的基本问题：你有一些输入数据、一些目标数据，你想找到一个函数，把输入映射到目标，并且希望它能泛化到新的输入。如果你做的是深度学习，那你就是用一条参数化曲线来充当你的函数、你的模型，然后用梯度下降去拟合这条曲线的参数。我们做的基本上也是这件事，只不过我们把参数化曲线替换成了一个尽可能小的符号模型（symbolic model）。它是能够……

[03:15] **SPEAKER_03:** explain the data to model what's going on. And of course, if you're doing that, you cannot apply gradient descent anymore. So we are building something that we call symbolic descent, which is like the symbolic space equivalent of gradient descent. The idea is to build this new machine learning engine that's giving you extremely concise, symbolic models of the data you're feeding into it, and then we're going to make it scale. And so everything you're doing with machine learning today, with parametric curves, we should be able to do it with symbolic models in the future, in a way that will be much, much closer to optimality. Much closer to optimality in the

> ……解释数据、刻画背后规律的最简单可能的模型。当然，如果你这么做，就没法再用梯度下降了。所以我们在构建一种我们称之为"符号下降"（symbolic descent）的东西，它相当于符号空间里对应梯度下降的方法。我们的想法是打造这个新的机器学习引擎，它能针对你喂进去的数据给出极其简洁的符号模型，然后我们要让它规模化。这样，今天你用参数化曲线做的一切机器学习任务，未来我们都应该能用符号模型来做，而且方式会更加、更加接近最优。更接近最优的意思是……

[03:56] **SPEAKER_03:** sense that you're going to need much much much less data to obtain the models. The models are going to run much more efficiently at inference time because they're going to be so small. And because they're so small, they will also generalize much better and compose much better. You know, the minimum description length principle that the model of the data that is most likely to generalize is the shortest. And I think you cannot find a model like this. If you're doing parametric

> ……你需要的数据会少得多得多。这些模型在推理时运行效率会高得多，因为它们非常小。而且因为它们这么小，它们的泛化能力也会好得多，组合能力也强得多。你知道最小描述长度原则（minimum description length principle）——最有可能泛化的数据模型是最短的那个。而我认为，如果你做的是参数化学习，你根本找不到这样的模型。

[04:20] **SPEAKER_03:** learning, you need to need to try symbolic learning.

> 如果你想找到这样的模型，就需要尝试符号学习。

[04:23] **SPEAKER_01:** That's fascinating.

> 太引人入胜了。

[04:24] **SPEAKER_02:** So the rest of the industry is just pouring more and more billions of dollars down in the air with a more complex and expensive approach to computing, but also with the bigger one. So we're in a the fiscal crisis, so how do you see how to work in the future about

> 所以业界其余的人只是把越来越多的数十亿美元砸向一种更复杂、更昂贵的计算方法，而且是更大规模的那种。我们正处在一种（投入的）财政压力之中，那么你怎么看待未来该如何在……

[04:38] **SPEAKER_03:** this new approach that was set years ago. Can you help make the case for why you think that it's the right thing to explore alternate approaches instead of just to keep putting more money into the current approach? I mean, everybody is, is, you know, building onto the LLM stack these days, which makes sense because, you know, the returns aren't there, like it's actually working. have everybody working on the same thing. Like I personally don't think that machine learning or AI in 50 years is still going to be built on this stack.

> ……这种多年前就确立的新方法上开展工作。你能不能帮我们论证一下，为什么你认为探索替代方法是对的，而不是一味往当前这条路径里砸更多的钱？我是说，如今每个人都在往 LLM 技术栈上添砖加瓦，这也合理，因为它确实有回报、确实管用，所以大家都在做同一件事。但我个人并不认为五十年后的机器学习或 AI 还会建立在这个技术栈之上。

[05:07] **SPEAKER_03:** I think this is a stack that is very nice. Maybe it even gets us to AGI, but it's not as efficient as it should be. I think it's inevitable that the world of AI will trend over time towards optimality. And so I'm trying to sort of like leapfrog directly to optimality, like to build the foundations of optimal AI today, but in general, you know, our vision is very ambitious and I'm not saying that we're going to be successful. Like we have maybe a 10 or 15% chance of success, but that is enough that it's worth trying, right?

> 我认为这个技术栈很不错，也许它甚至能把我们带到 AGI，但它并没有它本该有的那么高效。我认为 AI 世界随着时间推移必然会朝着最优的方向发展。所以我试图直接跨越式地奔向最优，就是在今天就打下最优 AI 的地基。但总的来说，我们的愿景非常宏大，我并不是说我们一定会成功。我们成功的概率可能只有百分之十到十五，但这已经足以值得一试了，对吧？

[05:42] **SPEAKER_03:** And I think in general, like among listeners, if you have a big idea and it has very low chance of success, but if it works, it's going to be big and no one else is going to be working on it, right? It's not something popular. It's not something... If you don't... If you don't do it, no one else will do it.

> 而且我觉得，一般来说，对于听众们，如果你有一个大想法，它成功的概率很低，但一旦成功就会是件大事，而且没有别人在做这件事，对吧？它不是热门的东西，不是那种……如果你不做……如果你不做，就没有别人会去做。

[05:58] **SPEAKER_03:** And this is basically our situation. If you're in this situation, then you should try a chance. You know, you should go and work on it.

> 这基本上就是我们的处境。如果你处在这种境地，那你就应该去博一把。你知道，你就应该去动手做。

[06:04] **SPEAKER_02:** I mean, that's almost like the mission statement of Y Combinator, the thing that you just said.

> 我是说，你刚说的这番话几乎就是 Y Combinator 的使命宣言。

[06:09] **SPEAKER_03:** Yeah. The reason it's important is that again, if we don't do it, no one else will do it. Right? So it's worth trying. Even if we don't succeed, it's worth trying.

> 是的。它之所以重要，还是那句话：如果我们不做，就没有别人会做，对吧？所以值得一试。即使我们没成功，也值得一试。

[06:15] **SPEAKER_04:** Has the success, very specifically of the coding agents, I guess, built on top of the LLM stack, like has their success surprised you at all and in particular, like say over the last six months or so?

> 那么具体来说，建立在 LLM 技术栈之上的编程智能体的成功——它们的成功有没有让你感到意外，尤其是在过去大约半年里？

[06:26] **SPEAKER_03:** Yeah, absolutely. I think it has surprised many people. It definitely did surprise me. If you look at why everything is starting to work so well with coding agents, it's really because code provides you with a verifiable reward signal. And I think right now we're in this situation where any problem where the solutions you propose can be formally verified and you can actually trust the reward signal, it's not just some guess made by a model, any domain like this can be fully automated with current technology, with the LLM-based stack.

> 是的，绝对意外。我想它让很多人都感到意外，它确实也让我意外。如果你去看为什么编程智能体的一切都开始运转得这么好，那真的是因为代码为你提供了一个可验证的奖励信号。我认为我们现在的处境是：任何一个问题，只要你提出的解可以被形式化地验证，你能真正信任那个奖励信号，而不只是模型的某种猜测——任何这样的领域，都可以用当前的技术、用基于 LLM 的技术栈实现完全自动化。

[06:56] **SPEAKER_03:** And code is sort of like the first domain to fall, but there will be many others in the future. I think mathematics is also primed to see a revolution in the next few years for the same reasons, again, because the domain just gives you verifiable rewards.

> 代码算是第一个被攻克的领域，但未来还会有很多其他领域。我认为数学在接下来几年里也已经蓄势待发、即将迎来一场革命，原因同样是这个领域天然就能给你可验证的奖励。

[07:11] **SPEAKER_00:** I guess the challenge for a formally verified domain is you have to somehow take a domain and make it verifiable, which is the trick. I mean, code is very natural. You could test, there's bugs, compiles, et cetera, and mathematics as well, where there are all the theorems and proofs work out, I guess because we're nebulous when you go a couple of degrees off where there are fields that are not naturally formally verified and you need to come with a, again, with some sort of a function to come up with that reward that makes it verifiable with very fuzzy things, like let's say English language and composing the perfect essay, how do you make that formally verifiable?

> 我想，对于一个可形式化验证的领域来说，挑战在于你得设法把某个领域变得可验证，这才是关键所在。我是说，代码非常自然——你可以测试，有 bug，能编译，等等；数学也一样，所有定理和证明都能推导验证。我猜当你稍微偏离一点，就会进入那些天然不可形式化验证的领域，你需要再次拿出某种函数来构造出那个奖励，从而让那些非常模糊的东西变得可验证。比如说英语语言、写出一篇完美的文章，你要怎么让它变得可形式化验证呢？

[07:55] **SPEAKER_03:** Yeah, yeah, absolutely. I mean, writing essays is the typical example of a domain that's not verifiable. And so what you're going to see is that progress of reasoning models and based LLMs on this type of domain is going to be very slow because the stack we're using, like the LLM stack, is very, very reliant on its trained data. It's basically just operationalizing the trained data. And for writing essays, the trained data is coming from human experts, like annotating answers.

> 是的，是的，完全正确。我是说，写文章正是一个不可验证领域的典型例子。所以你会看到，推理模型和基础 LLM 在这类领域上的进展会非常缓慢，因为我们用的这个技术栈，也就是 LLM 技术栈，非常非常依赖它的训练数据，基本上就是把训练数据加以运用而已。而对于写文章来说，训练数据来自人类专家，比如标注答案。

[08:26] **SPEAKER_03:** And that's costly. So you're going to see this very, very slow progress. Maybe, maybe it's even going to stall. But for any, any verifiable domain, like tech code, for instance, which was the big unlock, is when people started creating this code-based training environment for post-training, where the reward signal, the verification signal is provided by things like unit tests and so on. And so that means that the model was not just working from human-provided annotations.

> 而这代价高昂。所以你会看到这种非常非常缓慢的进展，甚至可能会停滞。但对于任何可验证的领域，比如说代码——这是那个重大的突破口——真正的解锁发生在人们开始为后训练创建这种基于代码的训练环境，其中奖励信号、验证信号由单元测试之类的东西提供。这意味着模型不再只是依赖人类提供的标注来工作。

[08:55] **SPEAKER_03:** It was actually trained. It was actually trying some things, verifying the answer, and generating a lot, lot more trained data in the process, a much denser coverage of the problem space, and not just coverage in terms of, like, is the answer right or wrong, but also starting to build models of the execution traces, right, so that the models could start incorporating an execution model. Very much the way that human programmers, you know, when they look at code, they're sort of like executing the code in their mind. They keep track of the value of variables and so on. It's also what the models are trying to do now, and this is why it's working so well.

> 它实际上是被训练出来的。它实际上会尝试一些做法，验证答案，并在这个过程中生成大量、大量更多的训练数据，对问题空间形成密集得多的覆盖——而且不只是"答案对还是错"这种覆盖，它还开始构建执行轨迹（execution traces）的模型，对吧，这样模型就能开始纳入一个执行模型。这非常像人类程序员——你知道，当他们看代码时，他们某种程度上是在脑子里执行代码，追踪变量的值等等。这也正是现在的模型试图做的事，这就是它效果这么好的原因。

[09:32] **SPEAKER_03:** And it's possible because you're working with this very formal, fully verifiable environment. You cannot do that with SSS. You cannot do that with, you know, LAW or many other problems.

> 而这之所以可能，是因为你处理的是这种非常形式化、完全可验证的环境。你没法在（写作之类的）任务上这么做，你没法在法律或许多其他问题上这么做。

[09:41] **SPEAKER_00:** I think I really like how you define intelligence and how to measure it, which brings to the question of also sharing, having you share the history of ArcGIS.

> 我很喜欢你对智能的定义以及如何度量它，这也引出了另一个问题——想请你分享一下 ARC（AGI 基准）的历史。

[09:52] **SPEAKER_03:** Yeah. So my, my definition of general intelligence. You know, many people around the industry these days, they say AGI is going to be a system that can automate most economically, economically valuable tasks. And to me, that definition is it's about automation. It's not about intelligence.

> 好的。说说我对通用智能的定义。你知道，如今业界很多人说 AGI 会是一个能自动化大多数具有经济价值任务的系统。但在我看来，那个定义讲的是自动化，而不是智能。

[10:11] **SPEAKER_03:** It's not about general intelligence. So my definition is AGI is basically going to be a system that can approach any new problem, any new task, any new domain, and make sense of it, like model it, become competent, add it, uh, with the same degree of efficiency as a human could. So meaning it's going to need basically the same amount of training data, uh, and training computes as, as a human would, which is, which is very little, like humans are really, really, uh, data efficient. So general intelligence is human level skill acquisition efficiency on the, on the same scope of tasks that, uh, humans could potentially, uh, learn to do.

> 它讲的不是通用智能。所以我的定义是：AGI 基本上会是这样一个系统——它能面对任何新问题、任何新任务、任何新领域，理解它、给它建模、在其中变得胜任，而且效率与人类相当。也就是说，它所需的训练数据量和训练算力，基本上和人类差不多，也就是非常少——人类真的非常、非常地数据高效。所以通用智能就是：在人类有可能学会去做的同一范围的任务上，达到人类水平的技能习得效率。

[10:52] **SPEAKER_02:** Do you think it's possible that we will accomplish the first definition? Of AGI, the automate most economically useful work before we accomplish your definition? Absolutely.

> 你觉得有没有可能，我们会先实现第一种 AGI 定义——自动化大多数具有经济价值的工作——然后才实现你的定义？绝对有可能。

[11:01] **SPEAKER_03:** I think that's, that's a trajectory that we're on right now. And I think it's already true that in principle, current technology can fully automate at human level or beyond any domain where you have, uh, very favorable rewards. Right. And code, code being the first one. And I think figuring out AGI, figuring out like human level, uh, you know, learning efficiency over arbitrary tasks, that's probably going to take.

> 我认为这正是我们当下所处的轨迹。而且我认为，原则上，当前的技术已经可以在任何拥有非常有利（可验证）奖励的领域里，达到人类水平甚至超越人类水平地实现完全自动化——代码就是第一个这样的领域。而要搞定 AGI，也就是在任意任务上达到人类水平的学习效率，这大概需要……

[11:26] **SPEAKER_03:** Uh, a different sort of technology, different, a different mindset, different approach.

> ……一种不同的技术、不同的思维方式、不同的方法。

[11:29] **SPEAKER_02:** Do you think that LLMs can be bent to have the same sample efficiency as humans? Or do you think it's like fundamentally just impossible and we need a new approach? And that's, that's the thing that you're hoping, hoping to solve.

> 你觉得能不能把 LLM 改造得拥有和人类一样的样本效率？还是说你认为这从根本上就不可能，我们需要一种全新的方法——而那正是你希望去解决的东西？

[11:41] **SPEAKER_03:** With enough compute, everything starts looking like everything else, every like computer grad equalizer, every approach starts looking the same. And I think it's possible in principle to build something that looks a lot like AGI on top of the LLM stack. Uh, but it's not going to be LLMs per se, it's going to be this new layer, perhaps, you know, it's going to be even a few layers above, not just one layer above, but a few layers above. Uh, but it, you, you can build it on top of, uh, LLMs because LLMs are kind of computer, right? Uh, I do believe, however, this would be the wrong thing to do because it would be very inefficient.

> 有了足够的算力，一切看起来都开始变得像其他一切——算力就像一个大均衡器，每种方法看起来都变得一样。我认为原则上是有可能在 LLM 技术栈之上构建出很像 AGI 的东西的。但它本身不会是 LLM，而会是这个新的层，也许，你知道，甚至会是往上好几层，不只是一层，而是好几层。你可以把它建在 LLM 之上，因为 LLM 某种程度上就是一台计算机，对吧？不过，我确实认为这么做是错误的，因为它会非常低效。

[12:16] **SPEAKER_03:** I think AI, AI research will have to trend towards not just efficiency, but in fact, optimality over time. And for this reason, future AI. In a few decades, uh, it's not going to be this, uh, harness on top of, uh, reasoning model on top of a basal LLM, uh, it's going to be much, much lower than that.

> 我认为随着时间推移，AI 研究不仅要朝着高效，实际上还要朝着最优发展。正因如此，几十年后的未来 AI，不会是"基础 LLM 之上叠一个推理模型、再套一层脚手架（harness）"这种东西，它会比那低得多、底层得多。

[12:35] **SPEAKER_02:** To Diana's question. Do you want to talk about how you actually designed ArcAGI and why it's a good barometer of that?

> 回到 Diana 的问题。你愿意谈谈你实际上是怎么设计 ARC AGI 的，以及为什么它是一个很好的晴雨表吗？

[12:40] **SPEAKER_03:** I mean, I, I, you know, I've been doing deep learning for a very, very long time and initially my, my, my tech, my mindset was that deep learning was going to be able to do everything.

> 我是说，你知道，我做深度学习已经很久很久了，而最初我的想法、我的心态是：深度学习将能做到一切。

[12:50] **SPEAKER_00:** You were the creative at Keras before even all the other frameworks became very popular.

> 早在其他所有框架变得非常流行之前，你就是 Keras 的创造者了。

[12:55] **SPEAKER_03:** That's right. That's right. I was, uh, trained deep learning model, uh, uh, for natural language processing, in fact, in, uh, 2014. And, uh, from that work, uh, you know, I actually started, uh, developing this open source library, which I released, uh, in fact, uh, exactly 11 years ago, uh, March, March, 2015. Uh, so it was Keras and, and then it got popular and then I ended up, uh, sort of like doing less of the research that I, that I had started Keras for and, uh, more of working on the framework.

> 没错，没错。事实上，早在 2014 年，我就在训练用于自然语言处理的深度学习模型。正是从那项工作中，我开始开发这个开源库，实际上我在整整 11 年前发布了它，也就是 2015 年 3 月。那就是 Keras。后来它火了，于是我最终变成了——较少做我当初创建 Keras 时想做的那些研究，而更多地在维护这个框架本身。

[13:25] **SPEAKER_03:** Itself just because it has really, really good product market fit. And so my, my tech, you know, around that time, around like 2015, 2016 was that deep learning was extremely general, that you could do everything with deep learning that you didn't need in anything else. It was sharing complete. So, uh, my tech was basically a deep learning was differentiable programming. Uh, so anything you would do with software, you could, in principle, train a deep learning model on the right inputs and outputs to do the same thing.

> ……仅仅因为它有非常非常好的产品市场契合度。所以在那段时间，大概 2015、2016 年，我的观点是：深度学习极其通用，你用深度学习就能做一切事情，不需要别的东西，它是"图灵完备"的。所以我的观点基本上是：深度学习就是可微分编程（differentiable programming）。也就是说，任何你用软件能做的事，原则上你都可以在正确的输入和输出上训练一个深度学习模型来做同样的事。

[13:53] **SPEAKER_03:** And, uh, in, uh, 2016. I was doing, uh, research at Google Brain on trying to train deep learning models to help with, uh, reasoning problems and in particular, uh, uh, first order logic problems, uh, uh, theorem proving and so on. And I started finding that you could not really get gradient descent to encode, uh, uh, sort of like reasoning style algorithms. It was not because the models could not represent these algorithms. It was.

> 然后，在 2016 年，我在 Google Brain 做研究，试图训练深度学习模型来帮助解决推理问题，特别是一阶逻辑问题、定理证明之类的。我开始发现，你其实没法让梯度下降去编码那种推理式的算法。这并不是因为模型无法表示这些算法，而是……

[14:25] **SPEAKER_03:** Because gradient descent could not find them. Right. So the problem was that, it wasn't about deep learning, not being trained complete or anything like that. Like that was not the problem. The problem was gradient descent, right?

> ……因为梯度下降找不到它们，对吧。所以问题在于——问题不是深度学习不够"图灵完备"之类的，那不是问题所在。问题在于梯度下降，对吧？

[14:37] **SPEAKER_03:** Gradient descent would not find generalizable programs. It would instead, uh, end up doing, uh, over fit pattern matching, right. Uh, over, over sequences of, uh, uh, input tokens.

> 梯度下降找不到能泛化的程序。它最终会去做的，是过拟合式的模式匹配，对吧——在输入 token 的序列之上做过拟合。

[14:47] **SPEAKER_01:** Which I guess people could argue, like, that's what's happening.

> 我想有人可能会说，这正是现在正在发生的事情。

[14:50] **SPEAKER_03:** I mean, it's, it's useful to see what's happening today in a, in a, in a slightly. It's. It's a. It's a slightly higher, higher level version of that.

> 我是说，把今天正在发生的事看作那个（过拟合模式匹配）的一个稍微更高层的版本，是有帮助的。

[14:57] **SPEAKER_00:** It's with a lot of data. So it doesn't feel like overfitting because the data has a lot more distribution. Yeah.

> 是用了大量数据。所以它感觉不像过拟合，因为数据覆盖了大得多的分布。是的。

[15:01] **SPEAKER_03:** With a lot more data. And also, I think models today, uh, they're a lot more compressive after data, which is why, why they, they generalize better.

> 用了多得多的数据。而且我认为，今天的模型对数据的压缩性强得多，这就是为什么它们泛化得更好。

[15:08] **SPEAKER_01:** All models are wrong, but some models are useful. And then I guess what I'm hearing is like your method might find the right model.

> "所有模型都是错的，但有些模型是有用的。"那么我想我听到的意思是：你的方法也许能找到那个正确的模型。

[15:16] **SPEAKER_03:** That's right. That's, uh, that's, uh, where, where the, uh, idea came from. And that was like, you know, at the time back in 2016, 2017, I was like, okay, we are going to need a, a benchmark to capture these ideas. Uh, we're going to need a program synthesis benchmark. And, uh, my, my mental model for that was ImageNet.

> 没错。这个想法正是从那里来的。当时，大概在 2016、2017 年，我就想：好吧，我们需要一个基准测试来刻画这些想法，我们需要一个程序合成的基准。而我为此参照的心智模型就是 ImageNet。

[15:36] **SPEAKER_03:** I was like, oh, I'm going to make the ImageNet of reasoning. So I started brainstorming a few ideas around like 20s, 2017. I explored many different things. Uh, I tried working with, uh, in particular cellular automata, like, uh, uh, a setup where you show a model, uh, cellular automata outputs, and it must recreate the program that generated them, like that sort of thing. Uh, and eventually I settled on the, uh, ArcGIS format, uh, around like early 2018.

> 我想，哦，我要做出推理领域的 ImageNet。所以大概从 2017 年起我开始头脑风暴一些想法，尝试了很多不同的东西。我特别尝试过用元胞自动机（cellular automata）来做——就是那种给模型看元胞自动机的输出、让它重建出生成这些输出的程序的设置，诸如此类。最终，大概在 2018 年初，我确定采用了 ARC 这种格式。

[16:04] **SPEAKER_03:** You know, I was doing this on the side. It was a side project. Like my main project was, uh, developing Keras at Google. I wasn't moving very, very fast, uh, on that. Uh, so summer 2018, uh, I wrote the Arc task editor, and then I started just making lots of tasks by hand.

> 你知道，我这是在业余时间做的，是个副业项目。我的主项目是在 Google 开发 Keras。在这件事上我进展不是很快很快。所以在 2018 年夏天，我写了 ARC 任务编辑器，然后就开始手工制作大量任务。

[16:21] **SPEAKER_03:** And about one year later, I had made 1000 tasks. And so. I wrote up, uh, the paper that was explaining what this was about, what the big idea was, like intelligence as a, as a skill acquisition efficiency. And, and I published, uh, all of that in, uh, in 2019.

> 大约一年后，我做出了 1000 个任务。于是我写了那篇论文，解释这件事是关于什么的、核心思想是什么——也就是把智能看作技能习得效率。我在 2019 年把这一切都发表了。

[16:36] **SPEAKER_00:** In parallel, GP3 2020 was coming out and starting to show signs until the chat GPT moment around 2022, end of the year. And the industry took off with that. And this was one of the benchmark that was really performing really badly. And it was very obscure. I don't think many people.

> 与此同时，GPT-3 在 2020 年问世，开始显现苗头，直到 2022 年年底左右的 ChatGPT 时刻，整个行业随之爆发。而（ARC）是当时表现真的非常糟糕的基准之一，而且它非常冷门。我觉得没有多少人……

[16:54] **SPEAKER_00:** Knew about it. It was mostly niche research communities that maybe read your paper.

> ……知道它。知道它的大多是小众的研究社区，也许他们读过你的论文。

[17:00] **SPEAKER_03:** Yeah. People who worked on programs, this is new, but it's, uh, but a lot of people who worked on, on deep learning, on scaling up LLM stadium, really care for it. And part of the reason why is because LLMs did not work well or at all on the benchmark for a benchmark to capture the attention that the research community needs to start working a little, right? Uh, if it's too hard, people are going to, are just going to dismiss it.

> 是的。做程序合成的人（觉得它新鲜），但很多做深度学习、做 LLM 规模化扩展的人也很在意它。部分原因在于，LLM 在这个基准上表现不好、甚至完全不行——而一个基准要抓住研究社区的注意力，需要（模型）能取得一点点进展，对吧？如果太难，人们就会干脆无视它。

[17:24] **SPEAKER_01:** You're just ahead of your time, clearly, because we're not on arc AGI one anymore. And then two is reaching saturation and then three is out now. Yes.

> 显然你只是走在了时代前面，因为我们已经不再停留在 ARC AGI 一代了。二代正在接近饱和，而三代现在也已经推出了。是的。

[17:36] **SPEAKER_00:** And I think the cool thing about arc AGI, it has been a very good barometer for the industry of the big changes that happen because V1 was not working at all for a long time until 2025. When reasoning models came.

> 我觉得 ARC AGI 很酷的一点是，它一直是业界重大变革的一个很好的晴雨表，因为 V1 在很长一段时间里完全不管用，直到 2025 年推理模型出现。

[17:55] **SPEAKER_03:** Yeah, absolutely. If you look at, uh, performance on arc V1 first and then V2, uh, so basal LLMs, uh, were scoring extremely low on V1, like sub 10%, basically. And I mean, it was true of, uh, the original lag GPT-3, uh, actually scoring zero, but that's even true of the latest basal LLMs today, you know, as of, as of March. Without reasoning. Without reasoning.

> 是的，完全正确。如果你先看 ARC V1、再看 V2 上的表现——基础 LLM 在 V1 上的得分极低，基本上不到 10%。我是说，这对最初的 GPT-3 是成立的，它实际上得了零分；但即便对今天最新的基础 LLM 也一样，你知道，截至今年三月。在不用推理的情况下。不用推理。

[18:19] **SPEAKER_03:** Without reasoning. Yeah. So the base models. So performance of, uh, of basal LLMs on. On the V1 stayed very, very low, even though in the meantime, you know, we had scaled up these models by 50,000 X, right?

> 不用推理，是的。所以基础模型——基础 LLM 在 V1 上的表现一直非常非常低，尽管与此同时，你知道，我们已经把这些模型扩大了五万倍，对吧？

[18:32] **SPEAKER_03:** So it was really telling you that, you know, more scale, scaling up pre-training alone was not going to crack the benchmark. This was not enough to demonstrate that the model had fluid intelligence. And then, uh, the moment, uh, models starting performing well on arc one was with the first reasoning models, in particular, uh, the, the OpenAI 01. And then all three, uh, models, which by the way, they were demonstrated by OpenAI on arc, because it was the one unsaturated reasoning benchmark that was really showing that this model was different, like that new capabilities that we had not seen before. And so with reasoning models, you start seeing this sudden, like step function change, uh, on, on arc one.

> 所以它真的在告诉你：单靠更大的规模、单靠扩大预训练，是攻不下这个基准的。这不足以证明模型具备流体智能（fluid intelligence）。而模型开始在 ARC 一代上表现良好的那一刻，是随着第一批推理模型出现的，特别是 OpenAI 的 o1，然后是 o3 模型——顺便说一句，OpenAI 正是在 ARC 上展示了这些模型，因为它是那个尚未饱和的推理基准，真正显示出这个模型与众不同，展现出我们此前从未见过的新能力。所以随着推理模型的出现，你开始在 ARC 一代上看到这种突然的、阶跃函数式的变化。

[19:14] **SPEAKER_03:** And so arc one was really the benchmark that signaled that at this moment in time, something was happening.

> 所以 ARC 一代真的是那个发出信号的基准——它标志着在那个时刻，某件事正在发生。

[19:20] **SPEAKER_00:** Something big.

> 某件大事。

[19:21] **SPEAKER_03:** Yeah. Something big, like new capabilities were. Mm-hmm. Emerging. Like reasoning was new and different, and it was actually not obvious at the time.

> 是的，某件大事，就像新的能力正在……嗯……涌现。推理是新的、不同的东西，而这在当时其实并不是显而易见的。

[19:30] **SPEAKER_03:** Like, you know, I don't know if you remember when, uh, when, uh, uh, O3, uh, Preview was, was announced by OpenAI.

> 就是，你知道，我不知道你还记不记得 OpenAI 发布 o3 预览版的时候。

[19:36] **SPEAKER_00:** That was end of 2024, actually.

> 那其实是 2024 年年底。

[19:37] **SPEAKER_03:** Yeah, December 2024. And like, sure, it was like a, a, a huge step function progress on arc, uh, but it was very expensive. It did not really have, uh, product market fit effectively. But if you looked at, uh, at arc results, you knew that this was big and important. And then we released arc two, which was the same format, but, uh, more difficult, like with more, uh, uh, composition, uh, uh, at the level of the, the, the reasoning chains.

> 对，2024 年 12 月。当然，它在 ARC 上是一次巨大的阶跃式进步，但它非常昂贵，实际上并没有真正的产品市场契合度。但如果你看 ARC 的结果，你就知道这是件大事、很重要。然后我们发布了 ARC 二代，格式相同，但更难——在推理链的层面上有更多的组合（composition）。

[20:05] **SPEAKER_03:** And what happened is that, so the, the earliest reasoning models started very, very low on arc two, and then around the same time as, uh, coding agents started working, you saw this. Just last year. Yeah. So very, very recent, just a few months ago, you saw this, uh, uh, a very, very fast, like, saturation, uh, of arcs. And so again, like arc two signaled that, yes, there was this, uh, this new set of capabilities emerging.

> 结果是，最早的那批推理模型在 ARC 二代上起点非常非常低，然后大约在编程智能体开始奏效的同一时期，你就看到了这个（跃升）。就在去年。是的，所以是非常非常近期的事，就在几个月前，你看到 ARC（二代）非常非常快地趋于饱和。所以同样地，ARC 二代发出了信号：是的，有这么一套新的能力正在涌现。

[20:29] **SPEAKER_03:** So I think the benchmark did a really good job at capturing the advent of reasoning models and then the advent, uh, of agentic coding. Like this, this new pattern where if you have, uh, verifiable rewards, then you can basically fully automate, uh, the domain, which by the way, is true of arc. Like arc does provide a verifiable reward.

> 所以我认为这个基准很好地捕捉到了推理模型的到来，以及随后的智能体式编程（agentic coding）的到来。就是这种新模式：如果你有可验证的奖励，那你基本上就能完全自动化这个领域——顺便说一句，这对 ARC 也成立，ARC 确实提供了可验证的奖励。

[20:48] **SPEAKER_01:** I guess for v2, what, what caused the, so one was clearly reasoning. Two, a benchmark. So right, so you, you, so a benchmark was clearly the, the, uh, process. Uh, you saw this argument of, of, of a programming model.

> 那么对于 V2，是什么导致了（那次突破）——一代显然是推理。二代，一个基准。所以，对，你看到的（推动力）显然是这个过程，你看到了这种编程模型的论点。

[21:01] **SPEAKER_03:** Uh, a benchmark because it's very, very, very high value. It's like a very, very low, I, a very low value. Uh, so, so this graph is showing, uh, uh, of, of a, of a model, because this is, this is a very basic, uh, algorithm. Yeah. Uh, so, uh, and this, this, this is a, this is a case where you, you, you, you use the algorithms to, to, uh, eliminate the behaviors and the factors that you, you, you use.

> 一个基准，因为它价值非常非常高。就像一个非常非常低……一个非常低的（成本）值。所以这张图展示的是一个模型的（表现），因为这是一个非常基础的算法。对。所以这是这样一种情形：你用这些算法去消除掉那些你所用的行为和因素。

[21:23] **SPEAKER_03:** Yeah. like those in the benchmark and then you try to solve them using let's say let's say program induction for instance uh still using your reasoning model then you verify the solution again it's very viable so you can you can trust the answer and then you fine-tune the model on the successful reasoning chains and then you keep repeating like you generate new tasks you solve them you verify the solution you fine-tune the model on the reasoning chains and you can keep doing this millions of times right like you just need to spend more money yeah this is the rl loop that this is happening yeah and the the new paradigm in ai is basically that any domain where this is true where you have uh the ability to join this uh this is a true uh verification signals you you can run this this kind of loop right if you can run this kind of loop you can mine uh you can brute force mine effectively the entire space and get extremely high performance this is basically the the process through which octo was saturated so what it tells you is that it's not so much that the models have higher fluid intelligence uh than than they did with the with the first using models it's just that you have this new paradigm of post-training and this is exactly what led to agency coding so it does matter it is it is valuable it is useful

> 对，比如基准里的那些（任务），然后你试着去解它们，比方说用程序归纳（program induction），依然借助你的推理模型；接着你验证解答——它同样是可验证的，所以你能信任这个答案；然后你在成功的推理链上对模型进行微调；接着不断重复：你生成新任务，解它们，验证解答，在推理链上微调模型，你可以把这个过程重复上百万次，对吧，你只需要花更多的钱。是的，这就是正在发生的强化学习（RL）循环。而 AI 的新范式基本上就是：任何一个满足这个条件的领域——只要你有能力接入真正的验证信号——你就能跑这种循环，对吧。如果你能跑这种循环，你就能高效地暴力挖掘整个空间，取得极高的性能。这基本上就是 ARC（二代）被攻克饱和的过程。所以它告诉你的是：与其说模型比第一批推理模型拥有了更高的流体智能，不如说你有了这种全新的后训练范式，而这正是催生智能体式编程的东西。所以它确实重要，它确实有价值、有用。

[22:36] **SPEAKER_01:** it's not that the models are smarter it's that they're suddenly more useful it is possible to be more useful in particular domains without being smarter yeah clearly because that's means good things for me i'm not getting getting any smarter right now like at you know age 45 but you know i can learn how to do things and that's sort of what's happening with the models as of like late yeah absolutely when it

> 不是模型变聪明了，而是它们突然变得更有用了。在特定领域里，不变聪明也能变得更有用，这是可能的。是的，显然如此——因为这对我来说意味着好事：我现在，你知道，四十五岁了，并没有变得更聪明，但我可以学会怎么做各种事情。这大致就是最近发生在模型身上的事。是的，完全正确。当谈到……

[23:01] **SPEAKER_03:** comes to uh competency there's always a trade-off between intelligence and knowledge if you have more knowledge if you have better training uh you need less intelligence to be competent and that's exactly uh what happened with the the rise of coding agents right the models don't have higher intelligence per se they don't have like a higher uh iq so to speak it's just that they're way better trained and they're way better trained in in two ways so they're not just trying to complete code anymore they're actually trained via trial and error in these uh oil uh post-string environments with you know three word signals and also they're trained uh to embed this uh model of code execution right where they they they learn to keep track of the value of variables uh over an execution cycle and that's what what's leading to this extremely strong product market foods uh virginity coding today and street is completely changing software engineering this happened not too long ago the

> ……胜任力的时候，在智能和知识之间总是存在一种权衡：如果你有更多知识、有更好的训练，你就需要更少的智能才能变得胜任。而这正是编程智能体崛起时发生的事，对吧——模型本身并没有更高的智能，可以说它们没有更高的"智商"，只是它们训练得好得多。而且它们在两方面训练得更好：其一，它们不再只是试图补全代码，而是真正在这些强化学习后训练环境里通过试错来训练，带着（可验证的）奖励信号；其二，它们被训练去内嵌一个代码执行的模型，对吧——它们学会在一个执行周期里追踪变量的值。这就是导致今天智能体式编程拥有极强产品市场契合度、并彻底改变软件工程的原因。这（饱和）发生在不久之前……

[23:59] **SPEAKER_00:** saturation we actually had the founders of poetic that came and spoke about the approach which is really sounds like this new way of uh getting lms to perform is building this agent harness right and the hardness is basically structuring a problem domain into something that can be formally applied and they did that basically for arc v2 which when they released it they were at the top of the benchmark but then the crazy thing is i actually worked with the company in the winter 26 batch not too long ago called confluence lab which actually ended up saturating the v2 results with 97 and i think their task cost was a lot more efficient too and the approach they basically took is similar to this i think they built the harnesses on top of it in order to get lms to to go and build different tasks and program through it which then for me i was like wow is this bad during the batch they only worked on it for a couple of months and they were able to saturate the benchmark that has been around for a long time it's like something special is happening

> 关于饱和——我们其实请来过 Poetic 的创始人，他们讲过这种方法，听起来这种让 LLM 发挥作用的新方式就是构建这个智能体脚手架（agent harness），对吧。而脚手架基本上就是把一个问题领域结构化成某种可以被形式化应用的东西，他们基本上就是为 ARC V2 做了这件事——发布时他们在基准上名列榜首。但接下来疯狂的是，我其实和一家公司合作过，就在不久前的 2026 冬季批次里，叫 Confluence Lab，他们最终以 97% 的成绩把 V2 的结果攻克饱和了，而且我觉得他们的单任务成本也高效得多。他们基本上采取的方法与此类似——我想他们在其上构建了脚手架，好让 LLM 去构建不同的任务并通过它来编程。这让我当时想，哇，这是不是有点吓人：在批次期间，他们只做了短短几个月，就能把一个已经存在很久的基准攻克饱和。感觉有某种特别的事情正在发生。

[25:07] **SPEAKER_03:** yeah yeah there's a lot of progress right now that's driven by custom harnesses around the task and the harness is basically a way for the the human programmer to um input into the model higher level like solution strategies basically i mean to me the fact that you need humans to engineer these harnesses is also a sign that we're short of agi today because if we had agi you know agi would just make its own harness it would not need to be told how to solve a problem it would just figure it out but it is very effective like harnesses i don't think they get us closer to agi in any sense but it's a very valuable area of research because that can lead to task automation

> 是的，是的，如今有很多进展是由围绕任务的定制脚手架驱动的。脚手架基本上是人类程序员向模型输入更高层的解题策略的一种方式。对我来说，你需要人类去工程化这些脚手架，这本身也是一个我们今天尚未达到 AGI 的迹象——因为如果我们有了 AGI，你知道，AGI 会自己造脚手架，它不需要别人告诉它怎么解决一个问题，它自己就会搞明白。但脚手架确实非常有效。我不认为脚手架在任何意义上让我们更接近 AGI，但它是一个非常有价值的研究领域，因为它能带来任务自动化。

[25:50] **SPEAKER_01:** and the last thing that i want to say is that we are now taking applications got a startup in you apply at ycombinator.com apply it's never too early and filling out the app will level up your

> 我最后想说的一件事是：我们现在正在接受申请。如果你有个创业点子，就去 ycombinator.com 申请吧。永远不嫌太早，而填写申请表本身就会让你的（想法）更上一层楼——

[26:01] **SPEAKER_00:** idea okay back to the video can you tell us about then what v3 is going to measure that's uh just

> ——你的想法。好，回到视频。那你能不能告诉我们，刚刚发布的 V3 将要衡量什么？

[26:08] **SPEAKER_03:** got released yeah absolutely so if you look at v1 v2 it was really focusing on your ability to produce like causal models that i was given to you so it was static it was passive and really focused on modeling and v3 is completely different we are trying to measure agentic intelligence so it's interactive it's active like the data is not provided to you you must go get it the idea is that your agent is dropped into a new environment which is kind of like a mini video game and it's not provided any instructions it's not told what to do it's not told what the goal even is or what the controls even are and it must figure out everything on its own via trial and error so we are we are not just measuring you know that the ai's ability to model its environment we're also looking at its exploration efficiency its ability to acquire goals on its own like goal setting and of course its ability to plan through the model of the environment that's created and to execute the plan and so together you know all of these abilities we call that agentic intelligence and we are looking for ai systems that could learn to play these games and you know crack them with the same degree of action efficiency as a human if you look at the human they are dropped into this new environment they try a few things they start understanding how things work uh they can they can solve the environment you know in in a few hundreds to thousands of actions we're trying to look for ai systems that could match uh this efficiency and we're trying to look for ai systems that could match uh this efficiency and we're trying to look for ai systems that could match and by the way we know that all of these test environments in arc 3 are solvable by humans with no prior training because we actually tested them on on regular people yeah at first you just see this screen and you you know you have these keys available but you know what they do and you must figure out everything from scratch and humans are really good at that by the way they're really good at exploring efficiently with making sense of something new and eventually cracking the game and frontier models today they're

> ——刚发布，是的，当然。如果你看 V1、V2，它们真正关注的是你产出因果模型的能力，而数据是给定给你的，所以它是静态的、被动的，真正聚焦于建模。而 V3 完全不同——我们试图衡量智能体式智能（agentic intelligence），所以它是交互式的、主动的：数据不会提供给你，你必须自己去获取。核心思路是：你的智能体被丢进一个新环境，有点像一个迷你电子游戏，它不会得到任何说明，没人告诉它该做什么，甚至不告诉它目标是什么、控制方式是什么，它必须完全靠自己通过试错把一切都搞清楚。所以我们不只是衡量 AI 对环境建模的能力，我们还关注它的探索效率、它自主获取目标的能力（也就是设定目标），当然还有它借助所建立的环境模型进行规划、并执行计划的能力。把所有这些能力放在一起，我们就称之为智能体式智能。我们在寻找这样的 AI 系统——它能学会玩这些游戏，并以与人类相同的行动效率把它们攻克。如果你看人类：他们被丢进这个新环境，尝试几样东西，开始理解事物是怎么运作的，然后能够在几百到几千个动作之内解决这个环境。我们在寻找能匹配这种效率的 AI 系统。顺便说一句，我们知道 ARC 3 里所有这些测试环境都是人类无需任何预先训练就能解决的，因为我们真的在普通人身上测试过。是的，一开始你只看到这个屏幕，你知道你有这些按键可用，但你不知道它们的作用，你必须从零开始把一切搞明白。而人类非常擅长这个，顺便说一句——他们非常擅长高效地探索、理解新事物，并最终攻克游戏。而如今的前沿模型，它们……

[28:20] **SPEAKER_02:** very good at it if the reasoning models cracked v1 and the like reinforcement learning environments cracked v2 do we need a new advance to crack v3 to the to even the best techniques currently like

> ……很擅长这个。如果说推理模型攻克了 V1、强化学习环境之类的攻克了 V2，那我们是不是需要一项新的突破才能攻克 V3？就连当前最好的技术是不是都……

[28:33] **SPEAKER_03:** not work yeah i mean i'm pretty curious to see how frontier labs are going to react to v3 and how they're going to start to target it um it is designed to be more resistant uh to the same kind of targeting strategy as what we saw for v2 in particular like of course you can try to just make more arc three like games and then train your agents uh in them um but the thing is we've uh deliberately tried to create a private set of environments that is significantly different from the public set like you can look at the public set it's not actually giving you that much information about what's in the private set in the private set you will have very different games with very different concepts and also the public set is meant to be substantially easier so your performance in the public set is not actually it's not representative of how well the system within private so for this reason it's going to be harder to target and that makes it a better test of fluid intelligence as opposed to a test of how much effort you put into into cracking it i'm so curious how do you come up with these games they're so creative yeah we set up an entire video game studio right to create them so we got over 250 games uh and you know they're pretty quick to play like uh each game takes you maybe 10 minutes or or a bit less uh uh to play from scratch like upon first contact and we have like 250 plus and uh we set up this uh a very proactive game studio where we had any given week we had multiple games uh in progress we had like this this pipeline uh including you know design implementation uh review human testing and and uh and uh many many iterations in order to make sure that those every player who gets the knowledge is하고 uh takes a question from you know the userна how long has it taken to actually provide that

> ……都不管用？是的，我是说，我挺好奇前沿实验室会如何回应 V3、又会如何开始针对性地攻它。它在设计上更能抵抗我们在 V2 上看到的那种针对性攻关策略。具体来说，当然，你可以试着做更多类似 ARC 3 的游戏，然后在里面训练你的智能体。但问题是，我们刻意打造了一套私有环境集，它与公开集有显著差异——你可以看公开集，但它其实不会给你太多关于私有集里内容的信息。在私有集里，你会遇到非常不同的游戏、非常不同的概念；而且公开集在设计上要容易得多，所以你在公开集上的表现其实并不能代表系统在私有集上的好坏。正因如此，它会更难被针对性攻关，这就使它成为一个更好的流体智能测试，而不是一个"你为攻克它投入了多少工夫"的测试。我太好奇了——你们是怎么想出这些游戏的？它们太有创意了。是的，我们为此专门建立了一整个电子游戏工作室来制作它们。我们做了 250 多个游戏，而且你知道，它们玩起来相当快——每个游戏第一次接触、从零开始玩大概只需要 10 分钟或更少。我们有 250 多个。我们建立了一个非常积极主动的游戏工作室，任何一周里我们都有多个游戏在制作中，我们有一整套流程，包括设计、实现、评审、人类测试，以及许许多多次迭代，以确保每个玩家（都能上手理解）。它需要（时间）——从用户那里得到一个问题、到实际给出反馈，花了多长时间……

[30:26] **SPEAKER_02:** feedback and that type of information um we line have of our colleagues who are in Мы want we limiting the

> ……反馈以及那类信息。（此处语音转录不清）我们希望限制那些（外部知识）……

[30:33] **SPEAKER_03:** on pト making the視野 visto been working top of core knowledge priors like things like just just you know elementary knowledge like basic physics understanding of objects understanding of the notion of agents for instance like an agent in objects with goals and intentions but we are not incorporating any language any like cultural symbols like you know arrows for instance or the color green meaning go and color red meaning start that sort of thing uh there's no external knowledge that's involved uh in these games it's

> ……我们一直在核心知识先验（core knowledge priors）之上来做这件事，也就是那种最基本的知识，比如基础物理、对物体的理解、对"智能体"概念的理解——比如一个带有目标和意图的智能体和物体。但我们没有纳入任何语言、任何文化符号，比如说箭头，或者绿色代表"通行"、红色代表"停止"这类东西。这些游戏里不涉及任何外部知识。它……

[31:17] **SPEAKER_00:** like one of those uh iq tests that are just pattern matching but now it has time series

> ……就像那种只是模式匹配的智商测试，但现在它加上了时间序列。

[31:20] **SPEAKER_03:** yeah uh it's not just time series it's interactive you must create your own path through game space right you must you know in in in an iq test like problem like you know what arc one and two is the data that you must model is provided to you you already have the data you just you just need to find the causal rule to explain it with r3 actually must gather the data and you must do so efficiently like of course you could say well i'm just gonna you know brute force mine uh the space of every possible game state and then i find the solution you cannot do that because if you try to do that you would score extremely low even if you manage to solve the level because you're scored on your efficiency you must match human level efficiency

> 是的，它不只是时间序列，它是交互式的——你必须自己在游戏空间里开辟出一条路径，对吧。你知道，在一个智商测试式的问题里，比如 ARC 一代和二代，你要建模的数据是提供给你的，你已经有了数据，你只需要找到能解释它的因果规则；而在（ARC 3）里，你实际上必须去采集数据，而且必须高效地采集。当然，你可能会说，好吧，我就暴力挖掘所有可能游戏状态的空间，然后找到解。但你没法这么做，因为如果你试图这么做，即使你成功通关了这一关，你的得分也会极低——因为你是按效率被评分的，你必须匹配人类水平的效率。

[32:06] **SPEAKER_01:** it's funny it's like almost a coming full circle this level of agi with games sort of is the match pair to openai writing i mean you know tom brown uh one of the co-founders of anthropic had to write like the harness code to allow like the you know pre-gpt

> 有意思，这几乎像是一种循环回归——用游戏来衡量这个层级的 AGI，某种程度上正好与 OpenAI 当年（用游戏做研究）相呼应。我是说，你知道，Tom Brown——Anthropic 的联合创始人之一——当年不得不去写脚手架代码，好让那个前 GPT 时代的……

[32:24] **SPEAKER_03:** ai at openai to play starcraft yeah yeah opening i worked on uh on uh in particular on the on dota 2 then the openai 5 model which was very good correctly so this was like not just pre-gpt but i also mostly pre-trial transformers because they were working with a stack of lstm uh layers if i recall correctly and even before opening eye uh deep wine worked a lot on video game uh you know solving video games yeah deep isle uh and they were the first to do uh atari games right back in 2013 that you know they were very very early very visionary in that sense to work on on this problem so early with these methods which are still very modern methods so the big difference is that if you look at atari games for instance or even dota you're training on on the same environment as what you use for testing so effectively you're just trying to memorize the best strategies you're trying to at training time explore the full space of possible game states and productionize operationalize uh that knowledge into into into the model and then at inference time you're basically just recalling that knowledge and that's explicitly what you are trying to avoid with arc 3 uh you're not playing games uh that you've seen before you're not playing games that you've been trained on like for millions of files like the opening i5 model for instance was playing a restricted version of dota 2 and it was trained on like tens of thousands of hours of gameplay effectively i think maybe in millions but it's just an insane amount of training data with arc 3 you're being evaluated on games that you think for the very first time and every action you spend exploring is counted towards your efficiency score right so you're really focused on measuring fluid intelligence your ability to efficiently explore efficiently produce a world model of the environment and then use this model to infer goals uh plan towards these goals

> ……OpenAI 的 AI 去玩星际争霸。是的，是的，OpenAI 特别研究过 Dota 2，就是那个 OpenAI Five 模型，它做得非常好。所以这不仅是前 GPT 时代，而且大体上也是在 Transformer 之前——如果我没记错，他们当时用的是一叠 LSTM 层。甚至在 OpenAI 之前，DeepMind 就在电子游戏、也就是解电子游戏上做了大量工作。是的，DeepMind，他们是最早做雅达利（Atari）游戏的，早在 2013 年，你知道，从这个意义上说他们非常非常早、非常有远见，这么早就用这些方法来研究这个问题，而这些方法至今仍是非常现代的方法。所以最大的区别在于：如果你看雅达利游戏、甚至 Dota，你是在与测试时相同的环境上训练的，所以实际上你只是在试图记住最优策略——你试图在训练时探索所有可能游戏状态的整个空间，把那些知识固化、内化进模型里，然后在推理时，你基本上只是在回忆那些知识。而这正是 ARC 3 明确想要避免的：你玩的不是你以前见过的游戏，不是你被训练过的游戏。比如 OpenAI Five 模型玩的是一个受限版本的 Dota 2，而它实际上是在数万小时的对局上训练的——我想也许是数百万小时，反正就是疯狂庞大的训练数据量。而在 ARC 3 里，你是在你第一次见到的游戏上接受评估，你花在探索上的每一个动作都会计入你的效率得分，对吧。所以你真正聚焦于衡量流体智能——你高效探索、高效构建环境世界模型的能力，然后利用这个模型去推断目标、朝这些目标规划……

[34:34] **SPEAKER_01:** and eventually crack the game one of the arguments for um you know endia is that you're able to do all of the intelligent tasks for you know an arc task might be like 0.3 you know cents for an arc task but you know for the same task on a foundation model with llms it's you know a dollar to ten dollars and then there's this other aspect that we've been tracking where it seems like uh more and more intelligence um at least on the llm side uh can be distilled down into smaller and smaller models and so on the one hand like they're scaling up but then they're like distilling smarter and smarter small models i guess your approach might indicate that it's not billions of parameters like the you know endia achieving agi might not be you know sort of inherently a scale thing at all there's a platonic ideal of the endia model that achieves agi yeah do you ever think about it in terms of

> ……并最终攻克游戏。支持 NDIA 的论点之一是，你能够完成所有这些智能任务，而一个 ARC 任务的成本可能只有 0.3 美分左右；但你知道，同样的任务在基于 LLM 的基础模型上要花 1 到 10 美元。还有另一个我们一直在追踪的方面：似乎越来越多的智能，至少在 LLM 这边，可以被蒸馏进越来越小的模型里。所以一方面它们在扩大规模，另一方面它们又在蒸馏出越来越聪明的小模型。我想你的方法也许暗示，它根本不是几十亿参数的事——NDIA 实现 AGI 可能本质上根本不是一个规模的问题，存在一个实现 AGI 的 NDIA 模型的"柏拉图式理想"。是的，你有没有从这个角度想过它——

[35:33] **SPEAKER_03:** like well it would fit on a floppy disk well okay there are two things to separate that's the sort of like fluid intelligence engine i think it's going to be a very very small code base uh in a very small set of models that's fitted with it and it's probably going to be on the order of megabytes right and then you have the knowledge base so to speak uh that's going to be layered below this this fluid intelligence engine like you know fluid intelligence has to draw on some knowledge and that knowledge is going to take up a lot more space so i think it's it's it's important to differentiate the two i do believe that you know when you create a gi retrospectively it will turn out that it's a code base that's less than 10 000 lines of code and that if you had if you had known about it back in the in the 1980s you could have done a gi back then using the computer resources available wow that's a crazy prediction that's i think retrospectively this

> ——比如说，它能装进一张软盘？好，这里有两件事需要分开。一个是那种流体智能引擎，我认为它会是一个非常非常小的代码库，配上一小组与之相配的模型，量级大概是几兆字节（megabytes），对吧。然后是所谓的知识库，它会分层地位于这个流体智能引擎之下——你知道，流体智能必须借助某些知识，而那些知识会占用大得多的空间。所以我认为区分这两者很重要。我确实相信，等到我们创造出 AGI，事后回看会发现它是一个不到一万行代码的代码库；而且如果你早在 1980 年代就知道它，你当时用当时可用的计算资源就能做出 AGI。哇，这是个疯狂的预测。我认为事后回看，这个……

[36:31] **SPEAKER_02:** will turn out my god to be true wow so it was just like hiding under our noses in plain sight for like 40 years it took us like 40 years

> ……天哪，会被证明是真的。哇，所以它就这样明晃晃地藏在我们眼皮底下大约 40 年，我们花了大约 40 年（才找到它）。

[36:38] **SPEAKER_01:** yeah that's right that's right well that second thing sounds like douglas lenat's like psych project or is that the wrong way to think about it it's like there's sort of knowledge about the world yeah and then there's methods like the program what i hear is like the program might be 10 000 lines and then it operates online knowledge base it's very large so the problem

> 是的，没错，没错。那第二件事听起来像 Douglas Lenat 的 Cyc 项目，还是说这样想是错的？就是说，一边是关于世界的知识——是的——另一边是方法，比如那个程序。我听到的意思是：程序可能只有一万行，然后它在一个非常庞大的知识库之上运行。所以问题……

[36:57] **SPEAKER_03:** with psych uh i mean there were many issues with it but one of the big issues is that

> ……在 Cyc 上——我是说它有很多问题，但其中一个大问题是……

[37:02] **SPEAKER_01:** uh there was no learning involved yeah it's just the knowledge like the knowledge wasn't crafted symbolic knowledge and it was probably inaccurate the way you want to be building a gi is that you

> ……它不涉及任何学习。是的，它只是知识——那些知识是人工精心构造的符号知识，而且很可能不准确。而你想要构建 AGI 的方式应该是，你……

[37:13] **SPEAKER_03:** want to be removing humans uh from from the improvement loop as much as possible you don't want a system where every improvement in system capability has to involve a human engineer doing something it's actually the strength of deep learning and foundation models is that you can just scale up the knowledge base like an llm is effectively knowledge base it's a bank of you know uh vector programs that map patterns of input tokens to patterns of output tokens and you can scale up that knowledge base by just adding training data and training compute with no further human involvement i mean of course there's still a little bit of human involvement in making sure the training job completes but it's it's minor you've managed to remove humans from this improvement loop as much as possible and that's also what we want for our system we want a system that's self-improving where the improvements are sounding meaning that every time the system increases capabilities it's also increasing the

> ……想尽可能地把人类从改进循环中移除。你不想要这样一个系统：系统能力的每一次提升都必须有一个人类工程师去做点什么。深度学习和基础模型的强大之处，恰恰在于你可以直接扩大知识库的规模——一个 LLM 实际上就是一个知识库，它是一堆向量化程序（vector programs）的集合，把输入 token 的模式映射到输出 token 的模式；而你可以仅仅通过增加训练数据和训练算力就把这个知识库扩大，无需更多的人类介入。我是说，当然，为了确保训练任务顺利完成，还是有一点点人类介入，但那很微小。你已经尽可能地把人类从这个改进循环中移除了。这也正是我们希望我们的系统具备的——我们想要一个自我改进的系统，其中的改进是复利式的，也就是说，系统每次提升能力时，它也在提升……

[38:13] **SPEAKER_01:** rate at which it increases its capabilities i think this is a pgism it's like i'm sorry the essay is so long uh if i had more time i would make it shorter yeah when you're looking at the heart problem it's

> ……它提升能力的速率。我觉得这有点像那句名言（帕斯卡说的）：抱歉这封信写得这么长，如果我有更多时间，我会把它写得更短。是的，当你面对那个核心难题时……

[38:25] **SPEAKER_03:** actually harder to produce a short elegant concise solution than the message of the engineered

> ……要产出一个简短、优雅、简洁的解，其实比堆砌出一个工程化的（冗长）方案更难。

[38:31] **SPEAKER_01:** solution yeah you can brute force it but you know the more elegant version is very very short and that's kind of like what you said with

> 是的，你可以用暴力方式做出来，但那个更优雅的版本非常非常短。这有点像你说的……

[38:38] **SPEAKER_03:** how this might come about yeah this is literally the shape of the type of ai approach we are creating and i think this is also the shape of science itself like science is fundamentally a symbolic compression process where you're looking at a big mess of observations like you know the position of planets in the sky or something like that and you're compressing that down to a very simple symbolic rule you're saying like yeah like all these new thousands of observations actually just all at this one simple equation that's symbolic compression and to do this by the way you need the model uh to be symbolic like you you could not fit a curve and say well you know that that kills my model that would never be optimal this would never be concise or elegant enough and that's not what science is doing science is not about curve feeling science is about finding the equation finding the most compressive symbolic model of your pile of And that's the process that you are trying to recreate in software form. Like you could say that the NDI approach to program synthesis is that we are building science incarnate, the scientific method in algorithmic form.

> ……这（更优雅的解）可能会怎样产生。是的，这就是我们正在创造的这类 AI 方法的形态。而我认为这也是科学本身的形态——科学从根本上是一个符号压缩（symbolic compression）的过程：你面对一大堆杂乱的观测，比如天空中行星的位置之类的，然后把它压缩成一条非常简单的符号规则。你会说，是的，所有这成千上万个新观测，其实全都符合这一个简单的方程——这就是符号压缩。而顺便说一句，要做到这一点，你需要模型是符号化的：你不能去拟合一条曲线然后说"好吧，这就是我的模型"，那永远不会是最优的，永远不够简洁或优雅。科学做的不是这个——科学不是关于曲线拟合的，科学是关于找到那个方程，找到你那一堆（数据）最具压缩性的符号模型。而这正是你试图以软件形式重建的过程。可以说，NDIA 的程序合成方法就是：我们在构建"科学的化身"，把科学方法以算法的形式实现出来。

[39:51] **SPEAKER_02:** I'm curious if you compare it to biology. Clearly, LLMs don't learn the way that humans do because no baby reads the whole internet. Do you think program synthesis is closer to the way that humans learn? Or do you think that's yet a third branch where even if program synthesis is correct, there will be some yet as undiscovered third way to do it, which is the thing that we do?

> 我很好奇，如果你把它和生物学做对比。显然，LLM 的学习方式和人类不一样，因为没有哪个婴儿会读完整个互联网。你觉得程序合成更接近人类的学习方式吗？还是说那其实是第三种分支——即便程序合成是正确的，也仍然存在某种尚未被发现的第三种做法，才是我们人类真正做的事？

[40:13] **SPEAKER_03:** I think so. I do think humans do some amount of program synthesis. I think the way humans learn and the way the human mind works is very messy. It's not like there's one simple, elegant principle behind it all. It's an implementation of fundamental principles, the fundamental principles of intelligence, which, you know, I think we can.

> 我认为是这样。我确实认为人类会做某种程度的程序合成。我觉得人类学习的方式、人脑运作的方式非常杂乱，并不是说背后有一条简单、优雅的原理统摄一切。它是一些基本原理——智能的基本原理——的一种实现，而我认为，这些原理我们是可以……

[40:35] **SPEAKER_03:** Identify these principles and reimplement intelligence from scratch from first principles in a way that will be much more efficient than the human brain. I think the human brain is messy and it can be a good source of inspiration for AI. But I think it would be counterproductive to just try to, you know, observe it and reimplement it and make it biologically plausible. I think that's counterproductive. It's not what we're trying to do at NDI.

> ……识别出来的，并从第一性原理出发、从零重新实现智能，其方式会比人脑高效得多。我认为人脑是杂乱的，它可以成为 AI 灵感的良好来源。但我觉得，仅仅试图去观察它、复现它、让它在生物学上说得通，会适得其反。我认为那是南辕北辙，那不是我们在 NDIA 想做的事。

[41:01] **SPEAKER_03:** We're really trying to find what are the first principles. What are the first principles of intelligence and what is the system that would best implement them? But yeah, I do believe the human mind does at the highest level something that looks a lot like program synthesis. Like we're currently building causal models of our surroundings. Like we're describing our surroundings in our mind as, you know, a set of objects and agents and relations between objects that are fundamentally symbolic and causal in nature.

> 我们真正在努力寻找的是第一性原理——智能的第一性原理是什么，以及什么样的系统能最好地实现它们？但没错，我确实相信，人脑在最高层面上做的事情，非常像程序合成。就是说，我们时刻都在为周遭环境构建因果模型：我们在脑中把周遭描述成一组物体、一组智能体，以及物体之间的关系，而这些在本质上都是符号化的、因果性的。

[41:32] **SPEAKER_03:** This is exactly the process. That lets us generalize so well and adapt so well to novelty on the fly.

> 正是这个过程，让我们能够如此出色地泛化，如此出色地即时适应新奇事物。

[41:40] **SPEAKER_04:** I'm curious about NDI, the company, as you're building it. We've all here heard of the OpenAI founding story. And something that's always struck with me is just like both Sam and Greg say that it was a little odd in the early days because they didn't actually know what to do. It was like a bunch of people like hanging out in an apartment. I would love to hear kind of what's that been like for NDI?

> 我很好奇 NDIA 这家公司，也就是你正在构建它的过程。我们这里的人都听过 OpenAI 的创立故事。一直让我印象深刻的一点是，Sam 和 Greg 都说早期有点奇怪，因为他们其实不知道该做什么，就像一群人在一间公寓里瞎晃。我很想听听，对 NDIA 来说那是一种怎样的体验？

[42:01] **SPEAKER_04:** Like what did like the day one look like? And just maybe what's the first step? Yeah. Maybe for just people who are interested in starting these alternative approaches who don't have sort of a researchy background, how should they think about that? Yeah.

> 比如说第一天是什么样的？也许第一步是什么？是的。也许对于那些有兴趣去开创这些替代方法、但没有太多研究背景的人来说，他们该如何思考这件事？是的。

[42:11] **SPEAKER_03:** So we started on day one with the symbolic learning vision. Like we basically knew that we wanted to do symbolic program synthesis, that you wanted to create a new approach to machine learning where you replace parametric curves with the shortest possible symbolic models. And then the big question was, okay, so how do we find these models? We started from the base. The base idea, which is still the idea that we're following today, which is that we are going to do deep learning guided program search, that you have a symbolic search space to explore.

> 我们从第一天起就带着符号学习的愿景出发。我们基本上知道我们想做符号程序合成，想创造一种新的机器学习方法，用尽可能短的符号模型来取代参数化曲线。然后最大的问题是：好吧，那我们怎么找到这些模型？我们从最基础的想法出发。这个基础想法——至今我们仍在遵循的想法——就是：我们要做深度学习引导的程序搜索（deep learning guided program search），也就是你有一个符号化的搜索空间去探索。

[42:46] **SPEAKER_03:** And it's big. It's in fact combinatorial. You're not going to make progress if you just use brute force. It's not going to scale. You have to break the combinatorial wall.

> 而这个空间很大，实际上是组合爆炸式的。如果你只用暴力搜索，是没法取得进展的，它无法规模化。你必须打破这堵组合爆炸之墙。

[42:56] **SPEAKER_03:** And the way to do it is to add deep learning guidance. It's actually very similar to the principles that underlies. Something like AlphaGo or AlphaZero. That was our starting point. We also didn't have very clear ideas about how to build it.

> 而做到这一点的方法就是加入深度学习的引导。这其实和支撑 AlphaGo 或 AlphaZero 之类系统的原理非常相似。那就是我们的起点。当时我们对于该如何构建它也并没有非常清晰的想法。

[43:11] **SPEAKER_03:** So we tried many different things. We tried many, many different ideas. And it took us half a year roughly to get to good foundations where we could start building a system that compounds. And I think that's what's really important when doing a lab like this, that you don't want to be in a situation where you're constantly trying something new. It's not reusing.

> 所以我们尝试了很多不同的东西，尝试了非常非常多不同的想法。大约花了半年时间，我们才打下良好的地基，从而能够开始构建一个可以复利累积的系统。我认为这在做这样一个实验室时是真正重要的一点：你不想陷入那种不断尝试新东西的境地，那样是无法复用的。

[43:34] **SPEAKER_03:** Yeah. You don't want to have any learnings, any findings from the previous approaches. You want a compounding stack. You want to build reusable foundations and then the next layer and then the next layer. And of course, you want to be building onto the right foundation.

> 是的。你不希望之前那些方法的经验、发现全都白费（无法沉淀）。你想要一个能复利累积的技术栈。你想构建可复用的地基，然后是上面的下一层、再下一层。当然，你还想把它建立在正确的地基之上。

[43:48] **SPEAKER_03:** So don't commit to the foundation layer too early, but also make sure that at some point you're building this compounding structure. And that's the situation that we're in now.

> 所以不要过早锁定地基层，但也要确保在某个时刻你开始构建这种复利累积的结构。这正是我们现在所处的状态。

[43:59] **SPEAKER_02:** Is Arc 3 the end or will there be an Arc 4, 5, 6? Can you keep making it harder?

> ARC 3 是终点吗，还是说会有 ARC 4、5、6？你们能一直把它做得更难吗？

[44:04] **SPEAKER_03:** Yeah, yeah. I think there will absolutely be Arc 4 and Arc 5. I mean, we're currently planning Arc 5. The point of the Arc AGI benchmark series is not to say that, well, you know, here's this test. If you pass it, this is AGI.

> 是的，是的。我认为绝对会有 ARC 4 和 ARC 5，我们目前正在规划 ARC 5。ARC AGI 系列基准的意义，并不是要说"喏，这里有个测试，只要你通过了，这就是 AGI"。

[44:19] **SPEAKER_03:** Instead, what you're trying to do is we are targeting the residual gap of fair capabilities. Like Frontier is advancing and we're saying, well, if you compare it to human abilities, there's all this. There's all these tasks, all these things, it's not doing well, so we're going to create a benchmark to target that. And so it's a moving target, right? It's not fixed points, it's a moving target.

> 相反，我们想做的是针对（AI 与人类之间）能力上残余的差距。前沿在不断推进，而我们说，好吧，如果拿它和人类的能力相比，还有这么多——还有这么多任务、这么多事情它做得不好，所以我们要创建一个基准来针对那些。所以它是一个移动的靶子，对吧？它不是固定的点，而是一个移动的靶子。

[44:43] **SPEAKER_03:** So there will be Arc 4, which will be in the spirit of Arc 3, but more focused on continual learning and curriculum learning at longer timescales. So you're going to have fewer games, but they're going to have way more levels and the levels are going to be compounding, meaning that for each level, you need to reuse stuff that you've learned before. Yeah. And then there's going to be Arc 5, and I'm actually really, really excited with Arc 5. It's very, very new and different.

> 所以会有 ARC 4，它会延续 ARC 3 的精神，但更聚焦于更长时间尺度上的持续学习（continual learning）和课程学习（curriculum learning）。所以你会有更少的游戏，但每个游戏会有多得多的关卡，而且这些关卡是复利累积的，意思是每一关你都需要复用之前学到的东西。是的。然后会有 ARC 5，我其实真的非常非常期待 ARC 5，它非常非常新颖、非常不同。

[45:10] **SPEAKER_03:** It's all about invention. And I mean, you will see what that means. Eventually, I expect we will run out of things to test. Like as we get closer to AGI, eventually there will be no measurable difference between human capabilities and partial human learning efficiency and Frontier AI. And when that happens, when it becomes effectively impossible to measure, it's going to be a very, very long process.

> 它完全是关于"发明"的。我是说，你到时候就会明白那意味着什么。最终，我预计我们会没有东西可测了。随着我们越来越接近 AGI，最终人类的能力（及人类学习效率）与前沿 AI 之间将不再有可测量的差异。而当那发生时，当它实际上变得无法测量时——这将是一个非常非常漫长的过程。

[45:33] **SPEAKER_03:** So it's going to be a very, very long process. And it's going to be very, very long process. So it's going to be a very, very long process. But it's going to be very, very long process. But it's going to be very, very long process.

> 所以这将是一个非常非常漫长的过程。这将是一个非常非常漫长的过程。（此处语音有重复）

[45:35] **SPEAKER_03:** This is the AGI moment.

> 这就是 AGI 时刻。

[45:36] **SPEAKER_01:** Well, then the machines will take over and then they will create Arc ASI 1. Yes. And then it will continue from there. Yeah. If you had to put a guess, I mean, years, decades, months.

> 那到时候机器就会接管，然后它们会创造出 ARC ASI 1。是的。然后就从那里继续下去。是的。如果非要你猜一下——我是说，是几年、几十年，还是几个月？

[45:50] **SPEAKER_03:** My timeline to AGI, you know, if you just try to extrapolate from the current rate of progress and the amount of investment that's going into not just the LLM stack, but also large numbers of怪. like, uh, side ideas, side bets that might work out like, you know, India, for instance, I think we're probably looking at AGI 2030, early 2030s, uh, most likely. So around the time, uh, the two are going to be releasing like maybe arc six or arc seven, uh, that's probably going to be AGI.

> 我对 AGI 的时间线——你知道，如果你试着从当前的进展速度，以及不只是投入 LLM 技术栈、还投入大量可能奏效的旁支想法、旁注下注（比如 NDIA）的投资规模来外推，我认为我们大概会在 2030 年、2030 年代初迎来 AGI，这是最有可能的。所以差不多就是我们要发布 ARC 6 或 ARC 7 的时候，那时大概就是 AGI 了。

[46:25] **SPEAKER_02:** You guys are doing a different approach to LLMs. Um, do you think there's room for more startups to explore other new approaches and are there any other ones that you think are promising that don't have time to explore yourself?

> 你们在做一种不同于 LLM 的方法。嗯，你觉得还有空间让更多创业公司去探索其他新方法吗？有没有一些你认为有前景、但你自己没时间去探索的方向？

[46:37] **SPEAKER_03:** Yeah, absolutely. I mean, there are many different approaches that you could try. I've said like compute is a great equalizer. I think if you look at the amount of compute and resources that we've thrown at, uh, deep learning and, and gradient descent and, and scaling that up, if you had thrown the same amount of investment into almost anything else, you would also have seen extremely exciting results like genetic algorithms, for instance. Uh, if you try to scale up genetic algorithms, I mean, I'm sure you can do incredible things with that.

> 是的，绝对有。我是说，有很多不同的方法你可以尝试。我说过算力是个了不起的均衡器。我认为，如果你看看我们已经投向深度学习、梯度下降及其规模化扩展的算力和资源之多——要是你把同样规模的投资砸向几乎任何别的东西，你同样会看到极其令人兴奋的结果。比如遗传算法（genetic algorithms），如果你试着去规模化遗传算法，我敢肯定你能用它做出不可思议的事情。

[47:08] **SPEAKER_03:** Um, you could, you could in fact probably do new, new science, uh, because, uh, that's based on search and search is the, is the, is the best fit for, uh, automating the scientific method. Uh, I think so right now there's also like approaches that, uh, build on top of the current stack with their slightly alternative, like, uh, state space models, for instance, uh, there's, uh, the, the XLSCM architecture, like you can basically, you know, current frontier. It's, it's, it's a stack of things and you, you can take any layer in the stack and try to propose an alternative. Like if you propose an alternative architecture, uh, you can be doing, for instance, like, yeah, like more like, uh, recurrent models instead of transformers, uh, for, for the architecture. Uh, you, or you can do even lower level.

> 嗯，你实际上很可能可以做出新的科学，因为遗传算法基于搜索，而搜索最适合用来自动化科学方法。我认为，现在也有一些在当前技术栈之上做略微不同变体的方法，比如状态空间模型（state space models），还有 xLSTM 架构。你知道，当前的前沿本质上是一叠东西堆起来的，你可以取栈中的任意一层，试着提出一个替代方案。比如你提出一个替代架构，你可以做——是的，比如更偏向循环模型（recurrent models）而不是 Transformer 来做架构。或者你可以做更底层的。

[47:51] **SPEAKER_03:** You're going to be like, okay, we're still going to be training, uh, parametric curves, but you're going to get rid of grand descent, right? We're going to use like search. Maybe you're going to do new evolution. Uh, that's, that's lower level and the. The lowest level is, uh, the low, the level where, where we're operating, where we're saying, well, actually, uh, forget about curves, uh, forget about parametric learning, forget about grand descent.

> 你会说，好吧，我们仍然要训练参数化曲线，但你要摆脱梯度下降，对吧？我们改用搜索，也许你会做神经进化（neuroevolution）之类的。那是更底层的。而最底层的，就是我们所处的层级——我们说，好吧，其实，忘掉曲线吧，忘掉参数化学习吧，忘掉梯度下降吧。

[48:13] **SPEAKER_03:** We're just going to do something completely different. Um, and I think if you want to build optimally, either kind of forced to go back to the foundation of the stack, it cannot be like, uh, uh, one, one layer added on top of the pile.

> 我们要做的是完全不同的东西。而我认为，如果你想以最优的方式来构建，你多少被迫要回到整个技术栈的地基层，它不可能只是在那一大堆之上再加的某一层。

[48:28] **SPEAKER_00:** So do you think for aspiring researchers to want to do a new Neo lab with a different approach? Yeah. You should be reading research papers from the seventies or eighties and go deeply in those with approaches that were not as invested nowadays.

> 那你觉得，对于那些有志于用不同方法去做一个新式实验室的研究者来说——是的——他们应该去读七八十年代的研究论文，并深入钻研那些如今没被大量投入的方法吗？

[48:41] **SPEAKER_03:** That is actually a great idea because, uh, earlier in the, in the history of the AI research timeline, people were exploring more things and very different things. You've had this sort of like collapse of everything into one approach. So it's actually kind of a bad idea. Uh, like consider that not too long ago, like about, about 20 years

> 这其实是个绝妙的主意，因为在 AI 研究历史时间线的更早期，人们探索的东西更多、更五花八门。后来出现了这种一切都坍缩收敛到单一方法上的情况。所以（大家扎堆做同一件事）其实是个挺糟糕的主意。想想看，就在不久前，大约二十年前——

[49:03] **SPEAKER_00:** ago, we had the collapse into SVMs too.

> ——我们也经历过一次坍缩到支持向量机（SVM）上的情况。

[49:05] **SPEAKER_03:** Yeah. I mean, it's, it wasn't, I wouldn't describe it as a collapse because there weren't that many people doing SVMs and the AI was a much, much smaller field back then, but there was this, uh, uh, widespread understanding that neural networks were, were a failed approach that neural networks didn't work. And it was a waste of time to, to, to keep trying.

> 是的。我是说，我不会把它形容为坍缩，因为当时做 SVM 的人并没有那么多，而且那时 AI 是一个小得多、小得多的领域。但当时有一种普遍的认知，认为神经网络是一条失败的路线、神经网络行不通，继续尝试是在浪费时间。

[49:25] **SPEAKER_00:** In the nineties, right?

> 那是在九十年代，对吧？

[49:26] **SPEAKER_03:** Yeah. No, even, even in the, in the, in the late 2000s, this was a set of things, uh, basically like when, when I got into, into AI, uh, people are telling me like, Hey, neural networks, don't, don't try that. I was like, yeah, but it, it looks a lot like what the brain is doing. Like I'm, I'm interested in that. If everybody's working on something, you are discarding ideas that will, uh, actually turn out to be very proactive ideas, right?

> 是的。不，甚至到 2000 年代末，情况还是这样。基本上，当我进入 AI 领域时，人们跟我说：嘿，神经网络，别去碰那个。我心想，可是它看起来很像大脑在做的事，我对那个很感兴趣。如果所有人都在做同一件事，你就等于抛弃了一些日后会被证明极富远见的想法，对吧？

[49:50] **SPEAKER_03:** And yeah, like back in the seventies, back in the eighties, people are trying more things and I think Genetic Algorithm is actually a very good example of that. Uh, I think this is an approach that has a tremendous amount of potential. But there's, there's not too many people are looking into scaling it up, uh, deeply.

> 是的，回到七十年代、八十年代，人们尝试的东西更多，我认为遗传算法其实就是一个很好的例子。我认为这是一种潜力巨大的方法，但真正深入去研究如何规模化扩展它的人并不多。

[50:07] **SPEAKER_01:** Are there any characteristics that you would be looking for? I mean, is it as simple as like, if there's a scaling law that could happen, then even if it's a different, or is it, is that too like, you know, thinking by

> 有没有什么你会去寻找的特征？我是说，是不是简单到——如果存在一条能成立的规模化定律（scaling law），那么即便它是不同的（方法也值得做）；还是说这样想太……你知道，太靠类比来思考了？

[50:21] **SPEAKER_03:** analogy, I think you are looking for approaches that scale. Yeah. Uh, I think it's, it's a non-starter. If you're working on something, but the only way to increase the capabilities of the system is to have, uh, human engineers and researchers spend time on it. It will not work because even if the idea is very clever and very elegant and works really well, capabilities are going to be bounded, that can be bounded by human investment, right?

> 靠类比。我认为你要寻找的是能够规模化扩展的方法。是的。我认为，如果你在做某样东西，但提升系统能力的唯一途径是让人类工程师和研究者花时间在上面，那它就没戏。它行不通，因为即便这个想法非常巧妙、非常优雅、效果也很好，它的能力也会被封顶——被人类投入的多少所封顶，对吧？

[50:47] **SPEAKER_03:** You want to be in a setup where the system can improve its capabilities with no human in the loop, with no human.

> 你想处在这样一种格局里：系统可以在没有人类参与其中的情况下提升自己的能力，无需人类。

[50:53] **SPEAKER_01:** So you would say like, don't just do it the way we did it like 10 years ago. Do it with the idea that recursive self-improvement is baked in at the beginning. Yeah.

> 所以你会说，别只是照我们十年前的老办法去做。要一开始就把递归式自我改进（recursive self-improvement）内建进去。是的。

[51:02] **SPEAKER_03:** Not necessarily recursive self-improvement because deep learning for instance is not, is not recursively self-improving, but with the idea of scaling up with no human bottlenecks, you want to remove the human from, from the improvement loop. The great strength of deep learning is that the models got better and better simply by adding, uh, uh, training, training compute and training data. I mean, it's, it's a little bit of caricature because of course, just adding these factors requires a lot of human involvement, but basically that's the idea that you have these things. It is decoupling from, uh, the improvement curve and the amount of human effort that's needed to be injected into the system.

> 不一定非得是递归式自我改进，因为深度学习本身就不是递归自我改进的；而是要带着"在没有人类瓶颈的情况下规模化扩展"的理念——你想把人类从改进循环中移除。深度学习的巨大优势在于，模型仅仅通过增加训练算力和训练数据就变得越来越好。我是说，这有点夸张，因为当然，光是增加这些要素也需要大量人类介入，但基本理念就是：改进曲线与需要注入系统的人类工作量之间实现了解耦。

[51:39] **SPEAKER_02:** Yes. Or human effort that's already happened because the LMS do actually require an enormous amount of human effort. It's just, it was the human effort to build the internet and we'd already built it.

> 是的。或者说是那些已经付出过的人类努力，因为 LLM 其实确实需要巨量的人类努力——只不过那是当年构建互联网所付出的努力，而我们早已把它建好了。

[51:47] **SPEAKER_03:** Yeah. Actually less and less now, uh, that we are doing, uh, training in, uh, interactive verifiable environments, because then you only need a small amount of human effort to create the environment. And from that small amount of effort, you're, you're. You're creating exponentially more training data, but at first I think to sort of like prime the machine, you need this tremendous amount of, uh, of, uh, uh, human generated abstractions and call it in text data. And if you, if you don't start from that, you, you cannot get the system into this loop.

> 是的。实际上，现在（对人类努力的需求）越来越少了，因为我们是在交互式的、可验证的环境里做训练——那样你只需要少量的人类努力来创建环境，而从那一点点努力出发，你就能生成指数级更多的训练数据。但一开始，为了给机器"打底"启动，我想你需要这海量的、由人类生成的抽象，姑且称之为文本数据。如果你不是从那出发，你就没法把系统带入这个（自我强化的）循环。

[52:21] **SPEAKER_01:** Do you have any advice for me, uh, starting a open source project, things to do things not to do in, uh, in the AI space, because I am. Uh. Not sure how I signed up for this in the last 14 days, but I think I have, I don't know, on the order of like 10 to 30,000 people using G stack every day.

> 你对我有没有什么建议——就是启动一个开源项目、在 AI 领域里哪些该做、哪些不该做？因为我……呃……我也不知道自己是怎么在过去这 14 天里卷进这件事的，但我想现在大概有，我说不好，每天有一到三万人在用 G-Stack。

[52:41] **SPEAKER_04:** That's wild. Yeah.

> 那太夸张了。是的。

[52:43] **SPEAKER_01:** And I don't know, like, I have a job, I guess, like, you know, what was it like to start Keras and how did you keep maintaining it? How what's a good maintainer? Like, what did you learn from that? I don't know. This might be a whole hour.

> 而且我也不知道，我毕竟有份正职工作。你知道，创建 Keras 是什么感觉，你又是怎么一直维护它的？怎样才算一个好的维护者？你从中学到了什么？我不知道，这可能能聊上一整个小时。

[52:57] **SPEAKER_01:** Yeah.

> 是的。

[52:57] **SPEAKER_03:** I mean, that's lots of learnings from too many things. I'm growing, growing. Uh, so right now I'm less involved with it. Uh, there's a big team at Google that's working on it and they're doing an amazing job.

> 我是说，从太多事情里学到了太多东西。它一直在成长、成长。现在我参与得少了，Google 有一个庞大的团队在做它，他们做得非常出色。

[53:09] **SPEAKER_01:** So it is possible to not to, you know, to put people together to like, it is possible to start something.

> 所以是有可能的——你知道，把人们聚到一起——是有可能开创一件事情的。

[53:14] **SPEAKER_03:** It is possible to start something that's a relief and, and, and then get more people involved. And at some point it becomes its own thing. And it's just, you know, it used to be your baby, but now it's all, it's all grown up and it's an adult and, and, and going on with its own life. So if you ask me the, the, the factors that remade care successful, um, I mean, first of all is that there was this big focus on, uh, making the, the API simple and intuitive. There was this big focus on usability, and this was inspired by scikit-learn like scikit-learn was sort of like the OG, uh, machine learning library for Python.

> 是有可能开创一件事——这让人松一口气——然后让更多人参与进来。到某个时刻，它就变成了它自己的东西。就是，你知道，它曾经是你的孩子，但现在它已经长大了、成年了，过着自己的生活。所以如果你问我让 Keras 成功的那些因素——嗯，首先是特别注重把 API 做得简单、直观。有一个对可用性（usability）的巨大关注，这是受了 scikit-learn 的启发——scikit-learn 算是 Python 机器学习库里的元老（OG）。

[53:49] **SPEAKER_03:** And what made it successful was that it was so easy to get started with it. So at first I was like, okay, uh, I'm gonna package, uh, all this functionality I've created under really, really simple API is gonna be like the scikit-learn. That was like the big idea. The focus on usability is not just making sure the API is simple. It's also making sure the entire onboarding experience is nice and easy.

> 而让它成功的原因，就在于上手极其容易。所以起初我想，好吧，我要把我做的所有这些功能封装在非常非常简单的 API 之下，做成像 scikit-learn 那样。那就是核心思路。对可用性的关注不仅仅是确保 API 简单，还要确保整个上手过程都愉快而轻松。

[54:12] **SPEAKER_03:** Like the docs should be very informative. You should, you know, the docs should be not just telling you about how to use this thing. They should actually be teaching you about the domain in the first place, because the, the folks who land on your website, they're not gonna be already deep learning experts. They're gonna be people looking to maybe choosing deep learning. And so you, you have to teach them not just how to use the tool, but where the tool is good for, um, and, and the entire field around it.

> 比如文档应该信息量很大。文档不应该只是告诉你怎么用这个东西，它首先应该真正地教你了解这个领域，因为登陆你网站的那些人，他们不会已经是深度学习专家，他们是可能正在考虑选用深度学习的人。所以你不仅要教他们怎么用这个工具，还要教他们这个工具适合做什么，以及围绕它的整个领域。

[54:40] **SPEAKER_03:** And then, uh, you know, you have to put a lot of investment into community building. Um, one thing we, uh, we did a bit, uh, at Google, in fact, you know, Google made it kind of, kind of difficult. And, and I was sad about that is, uh, hire your power users, like hire your fans. This, this is a really, really good idea. Yeah.

> 然后，你知道，你必须在社区建设上投入很多。有一件事我们在 Google 也做过一点——其实 Google 让这件事变得有点困难，我为此感到遗憾——那就是：雇用你的重度用户，雇用你的粉丝。这是一个非常非常好的主意。是的。

[54:58] **SPEAKER_03:** Like find, find the, the most enthusiastic. Yeah. users from your community and, and, and just hire them on your team. Amazing. Yeah.

> 就是找到你社区里最热情的用户——是的——然后就把他们招进你的团队。太棒了。是的。

[55:07] **SPEAKER_03:** And, uh, these, these, these, these are the, always the best people, right?

> 而这些人，往往就是最优秀的人，对吧？

[55:11] **SPEAKER_01:** All right. Time to start gstack.org. Mm-hmm. Uh, put in a bunch of my own money and then hire a bunch of people to work on it.

> 好吧。是时候创办 gstack.org 了。嗯。投入一大笔我自己的钱，然后雇一批人来做它。

[55:17] **SPEAKER_01:** That sounds good. I think you've been a leader and pioneer and we're so lucky to have you sit with us. There are people watching who are at the beginning of their, you know, adulthood, even like their certainly their professional careers. Uh, or actually like people. just around the world they're like trying to understand like what does this mean as intelligence becomes broadly applicable like what would you tell you know if you were 18 right now what would

> 听起来不错。我认为你一直是一位领导者和先驱，我们很幸运能请你和我们坐在一起。观看的人当中，有些正处在他们成年生活的起点，甚至肯定是他们职业生涯的起点。或者其实是世界各地的人们，他们都在努力理解——随着智能变得广泛可用，这意味着什么。如果你现在 18 岁，你会告诉他们什么？你会……

[55:43] **SPEAKER_03:** you tell them yeah i mean there's a lot of people today who are very pessimistic very negative takes but the rise in your capabilities they say oh you know i'm going to be out of a job soon and that's going to be mass unemployment uh yeah it's just going to take over completely and my my take is actually you know the more you know the more expertise you have but things like programming for instance the better you're able to use and leverage these tools for your own benefit and with the right kind of expertise uh all this ai progress is actually empowerment like it's something that you can leverage for yourself i mean that's that's exactly what you did with your project right yeah and yeah more people should have this mindset of trying to learn as much as possible not just about ai uh but about the domain that they want uh to apply ai to right so that they should they should seek to turn this uh this this new development into an opportunity into into a tool they can use for themselves to improve their own lives i think that's that's the right mindset because you know you're not gonna stop uh ai progress i think i think it's too late for that and so the next question is okay like ai progress is here it's actually going to keep accelerating how do you make use of it how do you leverage how do you

> ……会告诉他们什么。是的，我是说，今天有很多人非常悲观，对 AI 能力的崛起持非常负面的看法。他们说，哦，你知道，我很快就要失业了，会出现大规模失业，AI 会彻底接管一切。而我的看法其实是——你懂得越多、拥有越多专业知识（比如编程这样的东西），你就越有能力为自己的利益去使用和借力这些工具。有了正确的专业知识，所有这些 AI 进步其实是一种赋能，是你能为自己所用的东西。我是说，这正是你用你的项目所做的事，对吧？是的。而且，是的，更多人应该有这种心态：尽可能多地去学习，不只是学习 AI，还要学习他们想把 AI 应用于其中的那个领域，对吧。所以他们应该设法把这个新的发展变成一个机会、变成一个他们能为自己所用、改善自己生活的工具。我认为这才是正确的心态，因为你知道，你无法阻止 AI 的进步，我觉得为时已晚了。所以接下来的问题是：好吧，AI 的进步已经到来，而且实际上还会不断加速，你要如何利用它？如何借力？如何……

[57:01] **SPEAKER_01:** ride the wave that's the question to ask i wish we could uh keep going for a couple hours because i'm sure we could francois thank you so much for spending time with us thanks so much for having me

> ……驾驭这股浪潮？这正是我们要问的问题。真希望我们能再聊上几个小时，因为我敢肯定我们聊得下去。Francois，非常感谢你花时间和我们在一起。非常感谢你们的邀请。
