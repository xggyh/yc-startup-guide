# 全文转录 · 前沿模型是怎么练出来的:Anthropic 预训练负责人谈扩展定律、算力与 AI 的未来

> ▶ [YouTube](https://www.youtube.com/watch?v=YFeb3yAxtjE) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/YFeb3yAxtjE.md) &nbsp;·&nbsp; Anthropic Head of Pretraining on Scaling Laws, Compute, and the Future of AI

> 中英对照 · 每段英文原文下附中文翻译

[00:05] **SPEAKER_00:** Hey guys, I'm thrilled to be joined today by Nick Joseph, the head of pre-training at Anthropic. To give viewers a high-level sense of what we'll be covering, we're going to start with the basics of what pre-training is, and then dig into how Nick thinks about strategy, data, alignment, and infrastructure at Anthropic. And by the end, you'll hopefully have a sense for how progress in AI comes directly from advances in pre-training. I would love to talk a little bit about your backstory and kind of how you got to this point. Where did you work before Anthropic, and what were your takeaways from those places?

> 大家好,今天我非常高兴请到了 Anthropic 预训练团队负责人 Nick Joseph。先给观众一个大致的概览:我们会先讲预训练的基础是什么,然后深入探讨 Nick 是如何思考 Anthropic 的策略、数据、对齐和基础设施的。到最后,希望你能明白 AI 的进步是如何直接来自预训练的突破的。我很想聊聊你的经历,以及你是怎么走到今天这一步的。在加入 Anthropic 之前你都在哪里工作过?从那些地方你有哪些收获?

[00:29] **SPEAKER_01:** Yeah, so let's see, I was at Vicarious, and then at OpenAI before Anthropic. So Vicarious was originally an AGI lab, and when I joined, they were making a shift to product, particularly working on robotics products. And the thing I worked on was training computer vision models for their robotics products. It was my first job, so I think I just learned a ton about how to do machine learning models, how to write machine learning infrastructure.

> 好的,让我想想,在加入 Anthropic 之前,我先是在 Vicarious,然后在 OpenAI。Vicarious 最初是一家 AGI 实验室,我加入时他们正在转向做产品,尤其是机器人产品。我做的是为他们的机器人产品训练计算机视觉模型。那是我的第一份工作,所以我学到了大量关于如何做机器学习模型、如何编写机器学习基础设施的知识。

[00:53] **SPEAKER_00:** And at the time, were you also thinking about a career as an academic? At the time, a lot of people doing AI work were in PhDs. That's kind of what I was thinking about before I started to do a company. How were you thinking about that in your headspace?

> 那当时你有没有考虑过走学术道路?那会儿很多做 AI 的人都在读博士。我在创业之前也是这么想的。你当时脑子里是怎么考虑这件事的?

[01:03] **SPEAKER_01:** Yeah. So, like, I'm actually... Actually, we went a little bit. I think, like, a lot of my thinking on this had come from an internship I did at GiveWell, which is, like, a nonprofit that evaluates charities. And some people there being like, ah, at some point, we might have AGI.

> 是这样的,其实……嗯,我们稍微扯远一点。我觉得我在这方面的很多想法来自我在 GiveWell 做过的一段实习,那是一家评估慈善机构的非营利组织。那里有些人会说,啊,某个时候我们可能会有 AGI。

[01:14] **SPEAKER_01:** It could be dangerous. We should worry about these risks. This could be, like, a big impact on humanity. And I was, like, not super convinced at the time and went down the economics route and was going to try to work on, like, directly helping people in poverty. That didn't work out for various reasons and ended up being like, okay, I'll at least work on AI.

> 它可能是危险的。我们应该担心这些风险。这可能会对人类产生巨大影响。当时我并不太信服,于是走上了经济学的路,打算直接去帮助贫困人群。由于种种原因那条路没走通,最后我就想,好吧,那我至少去做 AI 吧。

[01:29] **SPEAKER_01:** Either, like, the safety thing will turn out to be important, and I'll work on that, or it won't be, and I'll just make cool things with AI. It'll probably help people in poverty more. I wasn't really coming at it from an academic standpoint. I was sort of, like, in fact, when I switched to that, it was part of the appeal was that I could, like, immediately go do stuff in AI, whereas if I wanted to work in, like, economic policy, I'd have to wait, I don't know, six years to do a PhD and then start. And, like, it's a longer path.

> 要么安全问题最终被证明很重要,那我就去做那个;要么它并不重要,那我就用 AI 做一些很酷的东西,这大概也能更多地帮助贫困人群。我并不是从学术角度切入的。事实上,当我转向 AI 时,一部分吸引力在于我可以立刻上手去做 AI 的事,而如果我想做经济政策,我可能得等上、我不知道、六年读完博士才能开始。那是一条更长的路。

[01:53] **SPEAKER_00:** And what did the state of AI safety work at that time even look like? Like, who were the people who were thinking about that kind of stuff? I mean, there were some folks at Vicarious thinking about this kind of thing, but it was fundamentally a robotics company. And so, yeah, how were you thinking about that at the time?

> 那当时 AI 安全这方面的研究状况是怎样的?都有哪些人在思考这类问题?我是说,Vicarious 有些人在想这类事情,但它本质上是一家机器人公司。所以,当时你是怎么想这件事的?

[02:05] **SPEAKER_01:** Yeah, so my sense was, like, at the time, a lot of the AI safety discussion was kind of theoretical. Like, the models weren't actually that good. They weren't really posing these dangers. So it was a lot more, like, philosophical. It was like, oh, at some point, we might get AI that's really smarter than humans.

> 是的,我的感觉是,当时很多 AI 安全的讨论都比较理论化。因为那些模型其实并没有那么好,它们并没有真正带来这些危险。所以更多是哲学层面的讨论,大意是,哦,某个时刻我们可能会造出比人类聪明得多的 AI。

[02:18] **SPEAKER_01:** And, like, should we wait this, like, future concern? How should we compare that to nearer-term things? And I think that was, like, actually just a less compelling argument. I think it was, like, an interesting one and, like, sort of made you think a bit.

> 那我们是不是应该权衡这个未来的顾虑?该如何把它跟更近期的事情做比较?我当时觉得这个论证其实说服力没那么强。不过它挺有意思的,能让你稍微思考一下。

[02:29] **SPEAKER_00:** So next you went to OpenAI. What was OpenAI like at this time?

> 那接下来你去了 OpenAI。那时候的 OpenAI 是什么样的?

[02:32] **SPEAKER_01:** Yeah, so I was at OpenAI. I was on one of the safety teams. Yeah. And kind of worked on, I ended up working on code models, actually. Cool, nice.

> 对,我在 OpenAI,在其中一个安全团队。我做的工作,最后其实落到了代码模型上。挺酷的。

[02:39] **SPEAKER_01:** And kind of, when I got there, the first thing I saw was, oh, they'd fine-tuned GPT-3 to write some code. But I add, it was really good. And I was like, oh, okay. If you're worried about AI getting really powerful, writing its own code, that seems like it could self-improve. And how likely is that to happen?

> 我刚到的时候,看到的第一件事是,哦,他们把 GPT-3 微调过,让它写一些代码。而且我得说,写得真的很好。我就想,哦,好吧,如果你担心 AI 变得非常强大、能写自己的代码,那看起来它就可能自我改进。这有多大可能发生呢?

[02:56] **SPEAKER_01:** So I was doing a bunch of evaluations and, like, studies of what contributed. And then after, like, eight months, basically everyone I worked with, like, all of them, I was like, oh, I'm going to do this. All the safety leads left, which, yeah, invited me to go to Anthropic. And that was sort of the reason I joined OpenAI, was because I cared about AI safety and wanted to work with them. So then I went with them to join Anthropic pretty much right when it started.

> 所以我做了一堆评估,研究是什么因素在起作用。然后大约八个月后,基本上跟我共事的所有人——所有安全负责人都离开了,他们邀请我去 Anthropic。我加入 OpenAI 的原因其实就是我关心 AI 安全、想和他们一起工作。所以我就跟着他们一起,几乎在 Anthropic 刚成立的时候就加入了。

[03:17] **SPEAKER_00:** With that, why don't we transition a bit? These days you run the pre-training team specifically at Anthropic. Obviously, you've been working on pre-training at Anthropic for quite a bit of time. And I'm sure it's evolved over the years, what that even entails and looks like. Why don't we start by just talking a little bit about what pre-training is?

> 那我们不妨过渡一下。现在你在 Anthropic 专门负责预训练团队。显然你在 Anthropic 做预训练已经有相当长的时间了。我相信这么多年来,预训练所涵盖的内容和样貌都发生了变化。我们不妨先聊聊,预训练到底是什么?

[03:32] **SPEAKER_00:** Like, how does it even fit into the way of thinking about, how AI models have developed at a place like Anthropic? And what exactly do you guys do?

> 比如,它是如何融入到像 Anthropic 这样的地方对 AI 模型发展的思考方式中的?你们具体在做什么?

[03:38] **SPEAKER_01:** We know that one of the ingredients to making AI models better is scale. You want to put a lot of compute in. And if you sort of step back and you're like, okay, what's the way we could put the most compute into a model possible? We need some objective that there's just, like, tons of data for. And one idea here is, like, the internet.

> 我们知道,让 AI 模型变得更好的要素之一是规模。你想投入大量算力。如果你退一步想,好吧,我们怎样才能把尽可能多的算力投入到一个模型里?我们需要一个有海量数据可用的训练目标。而其中一个想法就是互联网。

[03:53] **SPEAKER_01:** The internet is massive. It's probably the biggest, like, single source of data that's created. And you don't have labels. It's like, you don't want someone to have to go in and look, read the entire internet and, like, say something about it. So you want to get labels out of the data.

> 互联网非常庞大,大概是人类创造出来的最大的单一数据来源。而且它没有标签。你不会想让某个人进去把整个互联网都读一遍、然后对它做出标注。所以你想直接从数据本身里得到标签。

[04:04] **SPEAKER_01:** And the idea here is we can take some text and we can predict the next word. So you take, you know, the as the first word, you predict the second word. Then you say the cat, you predict the word after that. And this means you get very dense signal. Every word is like a new example.

> 这里的思路是,我们可以拿一段文本来预测下一个词。比如你拿 "the" 作为第一个词,去预测第二个词;然后是 "the cat",再预测后面那个词。这意味着你能获得非常密集的信号——每一个词都像是一个新的样本。

[04:19] **SPEAKER_01:** And there's a huge amount of data. And one of the findings from my GPT-1, GPT-2 was kind of, as you throw more compute at this, more data, bigger models, you get better, you get smarter models, essentially. Totally. And that's kind of been the central thesis of pre-training for me. I've been doing this forever, the whole time.

> 而且数据量巨大。从 GPT-1、GPT-2 得到的一个发现就是,当你投入更多算力、更多数据、更大的模型,你基本上就能得到更好、更聪明的模型。完全如此。对我来说,这一直是预训练的核心论点。我一直都在做这件事,从头到尾。

[04:35] **SPEAKER_01:** There's this idea of scaling laws, which is that you can actually quantify, like, as you put in more compute, more data, more parameters, you get models in a very, you get a lower loss, a better prediction of the next word in a very predictable way. And I think you can somewhat foresee from that original paper, and I think, like, Dario did foresee this. I think many people did. But what's obvious was that once you have that, there's this positive feedback loop where you can train a model, you can use it to make something useful and sell that and get more money, use that to buy more compute, and then you just actually train it to make it a better model. And we've sort of run that cycle over and over again over the past five years or so.

> 有一个叫"扩展定律"(scaling laws)的概念,意思是你其实可以量化:当你投入更多算力、更多数据、更多参数时,你会以一种非常可预测的方式得到更低的损失、对下一个词更好的预测。我觉得从那篇最初的论文里就能在某种程度上预见到这一点,我认为 Dario 确实预见到了,很多人也都预见到了。但显而易见的是,一旦有了这个,就会形成一个正反馈循环:你可以训练一个模型,用它做出有用的东西并卖掉、赚更多钱,再用这些钱买更多算力,然后再训练出一个更好的模型。过去五年左右我们就一遍又一遍地跑这个循环。

[05:10] **SPEAKER_00:** Well, in thinking about that objective to begin, you know, I think the way I think about the state of pre-training is, yeah, it seems like this next word prediction, at least from the external standpoint, seems to be the dominant way pre-training happens. But if I rewind the clock to that era of 2017 to 2020 or 2021 and two even, there was all sorts of pre-training objectives people were considering, right? There was these BERT and BART models that were doing mass language modeling. It seems like this GPT series of models doing, like, autoregressive modeling, as you're describing, this next word prediction, seems to be the dominant one that won out. Do you have any reflections on that time period?

> 关于一开始的这个训练目标,我对当下预训练现状的理解是:至少从外部看,这种"预测下一个词"似乎是预训练的主流方式。但如果我把时钟拨回到 2017 到 2020、2021 甚至 2022 那个年代,当时人们在考虑各种各样的预训练目标,对吧?有 BERT、BART 这些做掩码语言建模的模型。而看起来 GPT 系列这种做自回归建模、也就是你说的预测下一个词的方式,似乎最终胜出成了主流。你对那段时期有什么反思吗?

[05:42] **SPEAKER_00:** Like, were you guys trying all of them and kind of this one worked? Or is there some sort of first principles reason why this is, like, the right one that should have worked?

> 比如,你们是把所有这些都试了一遍,然后这个刚好奏效?还是说有某种第一性原理的理由,说明这个就是那个理应奏效的正确方法?

[05:49] **SPEAKER_01:** I think the answer is, like, it's mostly empirical. Like, in terms of how to think of these things, I'd be like, yeah, it's empirical. Just try them all, see what works. One big advantage for this autoregressive setup is that you can just sample from it to generate text afterwards in a fairly, like, straightforward way that comes straight out of that.

> 我觉得答案基本上是靠经验的。谈到该怎么看待这些东西,我会说,是的,这是经验性的——把它们都试一遍,看哪个管用。自回归这种设置有一个很大的优势,就是你之后可以直接从它里面采样来生成文本,方式相当直接,是水到渠成的。

[06:02] **SPEAKER_00:** Like, it enables a product use. Yes, very nicely.

> 也就是说它能支撑产品化的使用。对,非常顺畅。

[06:05] **SPEAKER_01:** Like, one thing that you want is, like, just one characteristic of a setup is, like, a loss, whereas you drive down the loss. That actually is the thing you care about. And you can think of it as, like, if you got to perfect on language modeling, you now can, like, write text as a human. You can sort of imagine you put in the title of a paper, and it should spit out a novel paper. Whereas I think some of the other approaches don't quite have that flavor.

> 你想要的一个特性是:这种设置有一个损失函数,而当你把损失压低时,那正是你真正关心的东西。你可以这样想:如果你在语言建模上做到了完美,你现在就能像人一样写文本。你可以想象,你输入一篇论文的标题,它就应该能吐出一篇全新的论文。而我觉得其他一些方法并没有那种味道。

[06:26] **SPEAKER_00:** Yeah, totally. Yeah, and it makes sense that in terms of that loop you're describing of, you know, then release something that gets you revenue, and you can use that to buy more compute and iterate. This sort of gives you the most natural way to actually do that flow, because you can keep releasing new products and keep getting the revenue from that to invest in more compute and so on.

> 对,完全同意。而且从你描述的那个循环来看也说得通——发布点东西赚到收入,再用它买更多算力去迭代。这种方式给了你最自然的方式去实现那个流程,因为你可以不断发布新产品、不断从中获得收入,再投入更多算力,如此循环。

[06:42] **SPEAKER_01:** Yeah, it certainly gives you the most open-ended thing. You can imagine, you know, you, like, train something as a class. Like, you train some base thing, you fine-tune it for a bunch of particular tasks. One approach people would use, they would, like, do this big pre-training, and then they wouldn't just, like, open-endedly sample from it. You'd fine-tune it on, like, a hundred specific tasks.

> 对,它确实给了你最开放的东西。你可以想象,你把某样东西训练成一个类别。比如你训练某个基础模型,再针对一堆特定任务去微调它。人们会用的一种做法是:先做这个大规模预训练,然后并不是开放式地从它里面采样,而是在大约一百个特定任务上去微调它。

[06:55] **SPEAKER_01:** And that could work, too. I think that, like, the one sort of general intuition I have is, like, compute is the thing that matters. Yeah. Yeah. Like, I think if you throw enough compute at any of these objectives, you're going to get something that's probably pretty good and can kind of be fine-tuned to other things.

> 那样也能行。我有一个大致的直觉是:算力才是关键。是的。我觉得如果你对这些训练目标中的任何一个投入足够的算力,你大概都会得到一个相当不错、并且能被微调去做别的事情的东西。

[07:09] **SPEAKER_01:** And it's surprising how little these details matter compared to throwing more compute at the problem.

> 而且令人惊讶的是,与投入更多算力相比,这些细节其实影响甚微。

[07:14] **SPEAKER_00:** When you think about actually throwing more compute at the problem, there's a whole bunch of axes by which you could throw compute at it, too, right? And if you have a specific model architecture you're training over, you can basically throw more data at that specific architecture. For a particular one, you could add more layers or make the models larger in it. You could do some kind of neural architecture search over lots of different variants. And I assume that these days it's somewhat more figured out, you know, which architecture you go for.

> 当你想到真正给这个问题投入更多算力时,其实有一大堆维度可以投入算力,对吧?如果你有一个特定的模型架构在训练,你基本上可以给这个特定架构投入更多数据;对某个架构,你可以加更多层,或者把模型做得更大;你也可以在很多不同变体上做某种神经架构搜索。我猜如今该用哪种架构这件事已经相对更有定论了。

[07:37] **SPEAKER_00:** I assume the earlier days it was somewhat less so. And I'm curious if you could speak to how you guys thought about that. Like, what did your infrastructure even look like to do that type of determination?

> 我猜早些年就没那么有定论了。我很好奇你能不能谈谈你们当时是怎么思考这件事的。比如,为了做这种判定,你们的基础设施当时是什么样子的?

[07:46] **SPEAKER_01:** I mean, I think the short answer is it's hard, right? Like, what you're really doing is you're going to train this one big expensive model and you have a space of, you know, you can sort of call all these things hyperparameters. You know, how many layers do you have, what you're with. Like, you have this space of hundreds of hyperparameters and you want them all to be optimal. Yeah.

> 简短的回答是:很难,对吧?你真正在做的是要训练这么一个又大又贵的模型,而你面对的是一个空间——你可以把这些东西都叫作超参数:你有多少层、用什么等等。你面对的是一个包含数百个超参数的空间,而你希望它们全都是最优的。

[08:00] **SPEAKER_01:** And you're sort of striking this balance. Actually, between how much do they matter? Like, can you just take your best guess and throw more compute at it in whatever way you want versus how much you're letting at it precisely correct. Yeah, interesting. And I think one of the, like, interesting things is, like, it actually doesn't matter that much.

> 而你其实是在权衡:它们到底有多重要?你是可以随便取一个最佳猜测、然后以任何方式投入更多算力,还是必须把它调到精确正确?挺有意思的。我觉得有意思的一点是,其实它没那么重要。

[08:15] **SPEAKER_01:** Like, I think this was in one of the early scaling laws papers. Like, you can change these things and get little wins, but, like, as you throw more compute, it sort of reliably gets better. If you mess up enough, you will sort of stop seeing that happen and you won't have any way to know, which is one of the, that's, like, kind of the hardest part in some ways.

> 我记得这在早期某篇扩展定律论文里提到过。你可以调这些东西、得到一点点小的提升,但当你投入更多算力时,它就会相当可靠地变好。不过如果你搞砸得足够厉害,你就会看不到这种变好,而且你没有任何办法知道——从某种意义上说,这才是最难的部分之一。

[08:31] **SPEAKER_00:** You don't know the counterfactual. Basically, because you didn't run it for long enough to actually know what it is.

> 你不知道反事实会是什么。基本上是因为你没有把它跑得足够久,以至于无法真正知道结果会是怎样。

[08:35] **SPEAKER_01:** Yeah. We have these scaling laws. So you can sort of say, like, as you train them up more and more compute, you expect the loss to go down as a power law. It's really a power law plus constant. So what eventually will happen is you'll curve off that power law and then you know something is wrong.

> 是的。我们有这些扩展定律。所以你大致可以说,随着你用越来越多的算力去训练,你预期损失会按幂律下降——其实是幂律加上一个常数。所以最终会发生的情况是,你偏离了那条幂律曲线,那时你就知道出问题了。

[08:46] **SPEAKER_01:** And is it fundamental? Is it, like, you've hit the limits of scaling? Or is it, nope, you should have changed, you should have tweaked your learning rate slightly differently. And that's sort of one of the challenges. In terms of how to, like, figure it out, you can, the usual paradigm is, like, test things out at small scale before running them at large scale.

> 但这是根本性的吗?是你已经触到了扩展的极限,还是说,不对,你本该改一下、本该把学习率稍微调得不一样一点?这就是挑战之一。至于怎么弄清楚,常见的范式是:在大规模运行之前,先在小规模上做测试。

[09:01] **SPEAKER_00:** Mm-hmm. Small scale in terms of data or in terms of something else?

> 嗯。这里说的小规模是指数据规模,还是别的什么?

[09:05] **SPEAKER_01:** In terms of everything. Like, you kind of want to scale things down, like, proportionally. So you want to say, like, you want to have some theory for, like, how you're going to scale up. Like, ah, okay, if I get 10 times as many flops, how much of it goes into layers? How much of it goes into data?

> 是指所有方面。你想要按比例把各方面同时缩小。你想有一套理论来说明你要怎么放大规模。比如,好,如果我拿到 10 倍的浮点运算量,其中有多少投入到层数上?有多少投入到数据上?

[09:17] **SPEAKER_01:** How much of it goes into attention? And you sort of get that theory and then test that it's optimal a bunch with, like, scaling everything down proportionally.

> 有多少投入到注意力机制上?你先得到这套理论,然后通过把所有东西按比例缩小,反复测试它是否是最优的。

[09:27] **SPEAKER_00:** And just so I can think about what this actually looks like, in those early days of Anthropic, you know, you're a team of, like, 10 or something like that in those very early days, or 12 maybe. What actually is your ability to use large-scale infrastructure as, like, a relatively nimble startup at that time? I mean, a startup that was well-capitalized, but still not actually that many people working at. What kind of infrastructure did you have access to to train these early models at the time?

> 为了让我能想象这实际上是什么样子:在 Anthropic 最早期,你们的团队大概只有 10 个人,或者也许 12 个人。作为一家当时相对灵活的初创公司,你们使用大规模基础设施的实际能力有多强?我是说,一家资金充裕但实际上人并不多的初创公司。当时你们能用到什么样的基础设施来训练这些早期模型?

[09:48] **SPEAKER_01:** So that's actually one of the wild things was that at least, I mean, you don't know what anyone else is doing, of course, but it kind of felt like we were, like, at the frontier of it. And there just weren't that many people who cared. Like, I was sort of coming, you know, I was coming at it from, like, hey, this is the most important technology ever. And then we'd kind of, like, look around and be like, and it seems like I'm one of 30 people who are working on this in, like, the world. I mean, I was kind of, like, junior person.

> 这其实是很疯狂的一点:当然你并不知道别人在做什么,但感觉上我们好像就处在这件事的最前沿,而且真正在乎这件事的人并不多。我当时的心态是,嘿,这是有史以来最重要的技术。然后我们环顾四周,却觉得,好像全世界在做这件事的三十来个人里就有我一个。而我还是个相当资浅的人。

[10:10] **SPEAKER_01:** Everyone else sort of knew how to do this and had done it before, but I was kind of surprised at how easy it was. Like, the public estimates for GP3, I remember, were that it cost $5 million to train, which you're, like, on the one hand, $5 million is kind of a lot, but it's, like, a lot for an individual person. It's not really a lot from, like, a company perspective. So we could totally buy, like, compute that was enough to train models like that.

> 其他人多多少少都知道怎么做、以前也做过,但我当时挺意外它有多容易。我记得当时公开对 GPT-3 训练成本的估算是 500 万美元。一方面,500 万美元听起来是挺多——但那是对个人而言的一大笔钱,从公司角度看其实并不算多。所以我们完全买得起足够训练那种模型的算力。

[10:33] **SPEAKER_00:** And were you using a cloud provider, or did you have a custom setup somewhere, or did you literally have racks in a room somewhere that you bought a bunch of NVIDIA GPUs and you were doing it?

> 那你们是用云服务商,还是在某处有自建的定制系统,又或者你们真的在某个房间里摆着机架,买了一堆英伟达 GPU 自己来做?

[10:41] **SPEAKER_01:** We were using a cloud provider, but I think it's kind of, it's not actually that different, because one of the things that was surprising to me is you actually have to understand the literal layout. Like, I remember at one point one of my coworkers running a clustering algorithm to identify what rooms all the chips were in, since we had a hypothesis that they were in different rooms, and that was causing, like, or, you know, different buildings. Some sort of, like, network latency. Some sort of network latency, and you can kind of figure it out. You can, like, reverse engineer, like, ah, okay, yeah, there's clearly, like, two clusters here that are connected better, and there's some issue on the connection between them.

> 我们用的是云服务商,但其实差别没那么大,因为让我意外的一件事是,你其实得搞清楚字面意义上的物理布局。我记得有一次,我一个同事跑了个聚类算法,来判断所有芯片分别在哪些房间里,因为我们有个假设是它们在不同的房间——或者说不同的楼里——从而造成某种网络延迟。是某种网络延迟,而你能大致把它推断出来。你可以逆向工程出来:啊,好,这里显然有两个集群,彼此内部连接更好,而这两者之间的连接存在某种问题。

[11:12] **SPEAKER_01:** Like, we're trying to push the limits of the hardware, like, as much as possible, particularly at the beginning when we were kind of, like, we have way less funding than everyone else. We have to, and most people weren't very efficient with the compute, so we were like, ah, we can get a big lead by being really efficient at how we use the compute.

> 我们一直在尽可能地把硬件推到极限,尤其是在最初的时候,当时我们的资金比别人少得多。我们不得不这么做,而大多数人在算力利用上并不高效,所以我们想,啊,只要我们在算力使用上做到非常高效,就能取得很大的领先优势。

[11:26] **SPEAKER_00:** Could you talk a little bit about some of the things you guys did in those early days for how to get the most out of the hardware? I think that's really interesting. Like, I think back to the days of, the early days of Google, for example, where there's these cases where they basically bought relatively cheap consumer chips, and then they optimized the software to make it so you can actually get the most bang for your buck out of them, and that's how they had all this high latency, or low latency, high availability stuff. I'm kind of curious if there's some analog in the early AI era to that.

> 你能讲讲你们早期为了榨干硬件性能都做了哪些事吗?我觉得这特别有意思。比如我想到谷歌早期的一些例子,他们基本上买了相对便宜的消费级芯片,然后优化软件,让你能真正物尽其用,这就是他们如何做到那种低延迟、高可用的。我挺好奇 AI 早期是否有类似的情况。

[11:50] **SPEAKER_01:** I think for us it was largely about, like, getting the distributed framework, right? So, like, we're training on, in order to train something else, you have to train them on a large number of chips, and there's a bunch of different approaches to how to do this. There's, like, data parallelism, there's pipelining, there's upsharding, and, like, getting all of this.

> 我觉得对我们来说,主要是把分布式框架做对。为了训练某个东西,你得在大量芯片上训练它,而实现方式有一堆不同的思路——有数据并行,有流水线并行,有分片,把这些都搞定。

[12:04] **SPEAKER_00:** And at the time there were no, like, great open source packages you could just grab and use that just worked for this. I mean, today there's somewhat more of these, but at the time I assume there was literally none.

> 而当时并没有那种可以直接拿来用、开箱即用的优秀开源库来做这个。我是说,如今这类东西相对多了一些,但当时我猜是完全没有的。

[12:12] **SPEAKER_01:** There were some. Like, I actually remember that we were kind of working on data parallelism early on, and someone was like, and now we write the all-reducing. And I was like, we really do this ourselves? We don't, like, call a package? And this was kind of like, well, we're going to want to modify it, right?

> 也有一些。我其实记得我们早期在做数据并行时,有人说,现在我们要写 all-reduce 了。我就想,这真要我们自己写?不去调一个现成的库吗?当时的想法是,嗯,因为我们以后会想要改它,对吧?

[12:24] **SPEAKER_01:** Like, oh, like, we don't want to outsource this to some package because, A, we're about to go to a bigger scale, like, PyTorch, for instance, they had a package for doing this. But we were going to go to a bigger scale than Facebook had been, too. And you don't want to have a dependency on a package that you're going to have to be, like, constantly modifying, essentially.

> 我们不想把这个外包给某个库,原因之一是我们即将迈向更大的规模。比如 PyTorch,他们有一个做这件事的库,但我们要迈向的规模比 Facebook 当时的还要大。你不会想依赖一个你基本上得不停去改的库。

[12:42] **SPEAKER_00:** It's such a counterintuitive sentence there, too, like, we're going to a bigger scale than Facebook. Well, because at the time, Facebook AI research was considered one of the best places to do machine learning research. Like, FAIR was one of the places, FAIR and DeepMind were hiring lots of people out of top PhD programs and doing lots of things. Like, what was your headspace when you were like, okay, this very essential... We're an established lab with great people and whatnot.

> "我们要迈向比 Facebook 更大的规模"这句话本身就特别反直觉。因为当时 Facebook AI 研究院被认为是做机器学习研究最好的地方之一。FAIR 和 DeepMind 都在从顶尖博士项目里招大量的人、做大量的事。当你想着"好,这个至关重要的……我们是一家有优秀人才等等的成熟实验室"时,你当时的心态是怎样的?

[13:01] **SPEAKER_00:** We are operating on a scale that is not relevant to them. Like, was that natural and obvious to you? Or was there times where you kind of doubted the decisions you were making in that situation?

> 我们所运作的规模对他们来说是不相干的。这对你来说是自然而然、显而易见的吗?还是说有时候你也会怀疑自己在那种处境下做的决定?

[13:10] **SPEAKER_01:** I think it was surprising. I will... Maybe I'm just too arrogant or something. I kind of looked around and was like, what are these people doing? They're all missing the, like, big picture here.

> 我觉得挺意外的。也许我只是太自负了什么的。我环顾四周,心想,这些人都在干嘛?他们全都没看到这里的大局。

[13:18] **SPEAKER_01:** Like, I think the scaling laws were pretty clear. Like, and the arguments against, I just thought, were kind of nonsensical. Like, I think the original scaling laws paper had, like, 11 orders of magnitude. And there was, like, this intense debate on whether it would continue for, like, another point. And I was like...

> 我觉得扩展定律已经相当清楚了,而反对它的那些论点在我看来有点站不住脚。我记得最初那篇扩展定律论文覆盖了大约 11 个数量级,却还有一场激烈的争论,争的是它能不能再延续那么一点点。我当时就想……

[13:33] **SPEAKER_01:** There's already 11. It seems like 1 over 11 is maybe your chance it fails here. And then, like, you know, sometimes it doesn't work. Like, sometimes it just works straightforward. You're like, well, let's change the model.

> 已经有 11 个数量级了。看起来它在这里失效的概率大概是十一分之一。当然,有时候它确实不奏效;而有时候它就直接奏效了,你会想,那好,我们改一下模型。

[13:42] **SPEAKER_01:** And you're like, oh, yeah, of course. But, yeah, I do think that it was... It maybe felt obvious when you're in that headspace and you're working on this all the time and you're making those plots. And I think these things feel pretty different when you're on the outside. You know, there's a huge space of papers.

> 然后你会觉得,哦对,当然。不过,我确实觉得……当你处在那种状态、天天在做这件事、天天在画那些曲线图的时候,它可能显得很显然。而当你在外面看时,这些事情的感觉就很不一样了。要知道论文的海洋非常庞大。

[13:55] **SPEAKER_01:** Everyone tries to make their paper sound, like, very robust and important. And I could see being like, oh, yeah, this is not really a thing. But also different labs have different cultures. So, like, I think one of the things at FAIR was it was a very more PhD-style, independent research. People have their own ideas, pursue those.

> 每个人都想把自己的论文写得非常扎实、非常重要。我能理解人们会觉得,哦,这其实没什么。但不同实验室也有不同的文化。我觉得 FAIR 的一个特点是它更偏博士式的独立研究:大家有自己的想法,各自去追求。

[14:12] **SPEAKER_00:** You're fighting for your compute and so on.

> 你得为自己的算力去争抢,诸如此类。

[14:13] **SPEAKER_01:** Yeah, and to do a project like training a large language model requires a lot of people to collaborate on, like, a really complicated piece of infrastructure that isn't going to be a paper, right? Like, you're not going to publish, like, oh, I got a slightly... I got 5% more efficiency than the next one. And it's not respected. And, like, that's...

> 是的,而像训练大语言模型这样的项目,需要很多人协作在一套非常复杂的基础设施上,而这套东西是不会变成一篇论文的,对吧?你不会去发表"哦,我比上一个多拿到了 5% 的效率"。这种东西不被看重。就是……

[14:29] **SPEAKER_01:** Those cultures, necessarily. So that might have been part of it.

> 那些文化未必看重这些。所以这可能是原因之一。

[14:31] **SPEAKER_00:** Okay, so then when you actually implement these models, you're saying you're using a level of low-level programming where, you know, you're using libraries like PyTorch, but you're perhaps not using everything right out of the box from PyTorch because there's things you guys want to customize that are at the level of basically one level of abstraction below them. But not necessarily at the level of abstraction of, you know, writing custom CUDA kernels. Or, like, was that also in the space where you guys were thinking about things? So it depends on, like, the operation.

> 好,那么当你们真正去实现这些模型时,你是说你们会用到一定程度的底层编程——你们用像 PyTorch 这样的库,但也许不会完全照搬 PyTorch 开箱即用的一切,因为有些东西你们想定制,大致是在比它们低一层抽象的层面上。但不一定到写自定义 CUDA 核那种抽象层。或者说,那也在你们思考的范围内吗?这要看具体是哪种运算。

[14:53] **SPEAKER_01:** So, like, I think I was mostly operating at the level of, like, Torch.matml. You know, like, ah, yes, where does a matml go? But not thinking, like, how do you make the matml efficient? Like, I assume Torch figured out how to make a matml as efficient as is possible. But there are some pieces, like attention, where there was just kind of a lot of different variants.

> 我大部分时间是在 torch.matmul 这个层面上工作。就是,啊,好,矩阵乘该放在哪里?但不会去想怎么让矩阵乘更高效——我假设 PyTorch 已经想出了怎么把矩阵乘做到尽可能高效。但有一些部分,比如注意力机制,有相当多不同的变体。

[15:10] **SPEAKER_01:** And attention is really complicated and hard to make efficient on a GPU. And those things, you have to kind of go more levels down the stack. I think there was, like, a process that is maybe interesting that I'd never really, like, thought of before of, like, how to do it, which is sort of, like, modeling out the problem, the thing you're going to do, coming up with a strategy for how to parallelize it that, like, you're going to be able to do that, like, can get to a really good efficiency. You know, like...

> 而注意力机制真的很复杂,在 GPU 上很难做到高效。对于那些东西,你就得往技术栈更深的层次去。我觉得有一个流程可能挺有意思、是我以前从没真正想过的,就是怎么去做:先把问题、也就是你要做的事情建模出来,想出一套并行化的策略,让你能够实现它、并能达到相当好的效率。

[15:32] **SPEAKER_00:** So you're thinking about MFU, basically, like, your utilization on your GPU. So there's, like, a goal utilization you're trying to get at and a strategy to get to there, you're saying.

> 所以你基本上是在考虑 MFU,也就是你在 GPU 上的利用率。你是说,有一个你想达到的目标利用率,以及达到那里的一套策略。

[15:39] **SPEAKER_01:** Yeah, and I think, like, one of the things you can do is you can actually, like, pencil and paper math out what efficiency you're going to be able to get to, right? You know all the constraints. MFU is Flop's utilization. But, like, the reason you don't get good MFU is you end up limited on HBM bandwidth. You end up limited on, I don't know, host to, like, CPU offload.

> 是的,我觉得你能做的一件事是,你其实可以用纸笔算出你能达到多高的效率,对吧?你知道所有的约束。MFU 是浮点运算利用率。但你之所以拿不到好的 MFU,是因为你最终会被 HBM 带宽卡住,或者被主机到 CPU 的卸载什么的卡住。

[15:58] **SPEAKER_01:** There's a bunch of different pieces. But there's not that many pieces. There's, like, six relevant numbers there. So you can totally model it out, understand what the constraints are, and then implement something that can get there. It, of course, will be really inefficient when you implement it.

> 有一堆不同的环节,但其实也没那么多——相关的数字大概就六个。所以你完全可以把它建模出来,搞清楚约束是什么,然后实现一个能达到那个目标的东西。当然,你刚实现出来时它会非常低效。

[16:10] **SPEAKER_01:** And then the next step is, like, pulling out a profiler. So you want to be able to profile the job, look at how long every operation takes, have a model in your mind of how long every operation should take, and then make those two things the same.

> 然后下一步就是拿出性能分析器(profiler)。你要能对这个任务做性能剖析,看每个运算耗时多久,同时心里有一个模型知道每个运算应该耗时多久,然后让这两者一致。

[16:22] **SPEAKER_00:** And were there good out-of-the-box profilers you could use at that time? Or did you guys have, you know, because people weren't operating on the kind of network topologies you guys may have been using, did you have to write your own profilers, basically, to do this type of, you know, multi-node optimization?

> 那当时有没有好的开箱即用的性能分析器可以用?还是说,因为别人并没有在你们所用的那种网络拓扑上运作,你们基本上得自己写性能分析器来做这种多节点优化?

[16:34] **SPEAKER_01:** Yeah, it depends when. I mean, they were actually getting better with time. The PyTorch profiler was, like, pretty good, actually, throughout for a single GPU. You want to, like, profile a GPU, the PyTorch profiler would work. But if you wanted to profile a job on hundreds, thousands of GPUs, that, like, hadn't really been done much.

> 这要看是什么时候。它们其实是随着时间在变好的。PyTorch 的性能分析器对单个 GPU 一直都相当好用。你想剖析一个 GPU,PyTorch 分析器就行。但如果你想剖析一个跑在成百上千个 GPU 上的任务,那种事之前基本没怎么有人做过。

[16:48] **SPEAKER_01:** And then that was kind of more of us, like, hacking into the profiler to figure out how to combine all the traces together.

> 所以那部分更多是我们自己去改造那个分析器,想办法把所有的追踪记录(trace)合并到一起。

[16:54] **SPEAKER_00:** And then one more question on that earlier is, you know, you had mentioned, you know, you hadn't really done a lot of this work before, maybe, some time at OpenAI and those early days in Anthropic. How did you actually go learn all this stuff? Like, what was your process for learning about those six things that were relevant to bandwidth limitations and whatnot?

> 关于早期还有一个问题:你提到过,你之前其实没怎么做过这类工作,也许在 OpenAI 有过一些、在 Anthropic 早期有过一些。你到底是怎么去学会这一切的?比如,你学习那六个跟带宽限制之类相关的东西的过程是怎样的?

[17:08] **SPEAKER_01:** I mean, so when I joined Anthropic, one really nice thing was there just wasn't that much. I think my first day, I read through our entire, all of Slack. Right, you're like, cool, cut off. And the entire, like, internal database and learned a bunch from that. Like, it was kind of nice to just be like, everything is relevant to me.

> 我加入 Anthropic 时,一个特别好的地方是内容真的不多。我记得第一天我就把我们整个 Slack 全读了一遍。对,你会想,酷,读完了。还有整个内部数据库,从中学到了很多。那种"一切都跟我相关"的感觉挺不错的。

[17:24] **SPEAKER_01:** Yeah, totally. And then I mostly learned from pair programming. Like, Tom Brown had done all this before, so he kind of, like, knew all the stuff quite well. Sam McCandlish, my manager, had also done a lot of it before and I just, like, paired with them a huge amount at the beginning. And I think one of the things I really like about pairing as a way of learning is you learn the, like, thing you're trying to do.

> 对,完全是。然后我主要是从结对编程中学的。Tom Brown 以前都做过这些,所以他对这些东西都相当了解。我的经理 Sam McCandlish 以前也做过很多,一开始我就跟他们大量结对。我很喜欢把结对当作学习方式的一点是:你能学到你正打算做的那件事本身。

[17:41] **SPEAKER_01:** Like, you will learn that. Like, if you're pairing with someone better than you, they can just do it, so you're mostly just watching them. But you also learn how people do it. So something like how to use a profiler is not something you would ever learn from seeing someone's, like, final write-up on Slack for their PR. You would just be like, oh, they found these, they changed this specific line and it's a win.

> 你确实会学到那件事。如果你跟一个比你强的人结对,他能直接把它做出来,所以你大部分时间是在看他做。但你同时也学到了人们是怎么做的。像"怎么用性能分析器"这种东西,你绝不可能从别人在 Slack 上为某个 PR 写的最终总结里学到。你看到的只会是,哦,他们找到了这些,改了这一行,然后就成了一个提升。

[17:59] **SPEAKER_01:** Yeah, like,

> 是啊,就像,

[17:59] **SPEAKER_00:** you need to watch, like, a YouTube video for four hours of someone messing around with a profiler to, like, maybe self-teach it or something or to actually pair with someone is basically the best you can do.

> 你得看一段四小时的 YouTube 视频,看某人摆弄性能分析器,才可能勉强自学会;或者真正跟人结对——基本上这就是你能做到的最好方式了。

[18:08] **SPEAKER_01:** Yeah, I think there was, like, one thing that I think is embarrassing now that I look back is I'd never actually used a debugger before joining Anthropic. People talk about it at PDB of, like, yeah, that's a thing people use, but print seems fine for me. Yeah, sure, sure. Then I, like, watched them and was like, oh, no, a debugger is a super useful tool. This person's way faster at debugging things, particularly if it takes a long time to start up the code, which it can.

> 是的,现在回头看有一件事我觉得挺尴尬:在加入 Anthropic 之前我其实从没用过调试器。人们会提到 PDB,说这是大家会用的东西,但我觉得用 print 就挺好。然后我看着他们操作,就想,哦不,调试器是个超级有用的工具。这个人调试起来快多了,尤其是当代码启动要花很长时间的时候——而它确实可能很久。

[18:28] **SPEAKER_01:** And, yeah, learning that sort of thing, I think, comes best from pairing. Yeah, totally. And then there's, of course, the obvious you just learn by doing. Yeah, I eventually did, like, spit a profile and stare at it for many, many hours.

> 是的,学这类东西我觉得最好的方式就是结对。当然,还有显而易见的一点——你就是在做中学。我最终确实是导出一份性能剖析,然后盯着它看了很多很多个小时。

[18:38] **SPEAKER_00:** Totally, yeah, exactly, yeah. Okay, so then, that was sort of the very early era. Over time, obviously, pre-training has become bigger and bigger. As you're describing scaling, I imagine you're using many X more GPUs, much more compute over time. I'd be really curious to hear, first, at a high level, what do you feel has changed about the pre-training strategy that you could talk about?

> 完全是,没错。好,那些算是非常早期的阶段了。随着时间推移,显然预训练变得越来越大。就像你说的扩展规模,我猜你们用的 GPU 数量翻了很多倍,算力也随时间大大增加。我很想先从宏观层面听听:你觉得预训练策略上有哪些变化是你可以聊聊的?

[18:56] **SPEAKER_00:** Obviously, there's more compute, but what does that actually mean to have more compute? More compute in terms of what you think about differently from those early days versus now.

> 显然算力更多了,但"拥有更多算力"实际意味着什么?也就是从早期到现在,更多算力让你在思考方式上有哪些不同?

[19:03] **SPEAKER_01:** I'm sure the things that haven't changed, because I think it is, like, shocking how the world has changed in some ways. I think I'm still pushing down the exact same metric that I was on, like, day one.

> 我确定有些东西没变——因为在某些方面这个世界的变化真的令人震惊。我觉得我到现在还在压低跟我第一天一模一样的那个指标。

[19:12] **SPEAKER_00:** There's, like, some loss function. Loss go down.

> 就是有某个损失函数。让损失下降。

[19:14] **SPEAKER_01:** And I think you could, like, look at some, like, you could probably run the first model I trained on the same metric and just, like, make a plot of, like, progressive team over time. So that's all the same. I think the biggest...

> 我觉得你可以拿我训练的第一个模型,用同一个指标去跑,然后画一张团队随时间进步的曲线图。所以这部分都是一样的。我觉得最大的……

[19:25] **SPEAKER_00:** Like, one OKR is, like, one thing that matters, basically. Yeah, totally.

> 就是说,基本上只有一个 OKR、一个真正重要的东西。对,完全是。

[19:28] **SPEAKER_01:** And, like, I mean, talking about, like, OKRs, it's a very size of the company. You're like, oh, should you do OKRs? And it's always felt a little bit funny for a team like FreeShare where I'm like, sure, I can just pick a loss value, but, like, the answer is, like, as low as possible and we will continue to work on that forever. I think the biggest things that have changed has been a little more specialization. Like, I think at the beginning, I mean, the first, like, three or six months I tried to read every PR in the code base and that was great.

> 说到 OKR,这很看公司规模。你会想,哦,你该不该做 OKR?对于像预训练这样的团队,这总让我觉得有点好笑,因为我可以随便挑一个损失值,但答案永远是"越低越好,而且我们会永远为此努力下去"。我觉得变化最大的是稍微更专业化了一些。一开始的头三到六个月,我试图读遍代码库里的每一个 PR,那种感觉很好。

[19:50] **SPEAKER_01:** I knew all the pieces, et cetera. And as you grow, it's kind of, everything gets, like, a little more precise, you know? People really dial in exactly how attention should work, let's say, or, you know, really dial in, like, the parallelism strategy. And you end up with a team where it's a bunch of people who are, like, deep experts on individual things, which is great because it means you can go, you can go really deep on those things, but sometimes you, at least for me as a manager, one of the things you sometimes have to think about is, like, making sure the bigger picture makes sense. And also that you have enough people who actually do understand the whole bigger picture that there's no, like, single point of failure.

> 我了解所有的组成部分等等。而随着规模扩大,一切都变得更精细了。人们会把注意力机制到底该怎么运作调到极致,或者把并行策略调到极致。最后你的团队里是一群在各自领域深钻的专家,这很好,因为它意味着你能在那些点上钻得非常深。但有时候——至少对身为经理的我来说——你有时得考虑的一件事是确保大局是说得通的,同时确保你有足够多真正理解整个大局的人,这样就不会出现单点故障。

[20:24] **SPEAKER_00:** Yeah, it's interesting you frame it in that, with that, trade-off, right? Because as you were describing that, I was trying to think, you know, is this a bug or a feature? Like, there's some obvious features of it, which is you get expertise and you can optimize certain things, but I imagine your ability to take bigger swings becomes more complicated if not everyone's exactly pointed in the same direction. Like, how do you wrestle with that now?

> 你把它框定成一种权衡,这挺有意思的。因为你在描述的时候,我在想,这到底是缺陷还是特性?它有一些明显的好处,就是你能获得专业深度、能优化某些东西,但我猜如果不是每个人都朝完全相同的方向使劲,你去做更大胆的尝试的能力就会变得更复杂。你现在是怎么处理这个矛盾的?

[20:44] **SPEAKER_01:** Yeah, I think I mostly just try to get a balance of people. I think one of the challenges early on... Oh, of people. Oh, that's interesting. Yeah, like, I think people really do have a preference here has been one of the things I've seen.

> 是的,我觉得我主要是尽量在人上取得一种平衡。我觉得早期的一个挑战……哦,是人的平衡。哦,这有意思。是的,我观察到的一件事是,人们在这方面确实有各自的偏好。

[20:53] **SPEAKER_01:** Like, there are people who really want to be a generalist and understand, understand everything and, like, lightly touch on things. There are people who want to, like, pick an area. Often they've already picked that area and they're, like, deep experts in precision. You know, they did a whole PhD in precision and just want to think about that. And you want to get some balance of that.

> 有些人真的很想做通才,想理解一切、什么都浅尝辄止;有些人则想选定一个领域——通常他们早就选好了,是某个方向的深度专家。比如他们整整读了一个关于数值精度的博士,就只想琢磨那个。而你想在这两类人之间取得某种平衡。

[21:08] **SPEAKER_01:** I think there was a phase where we'd hired a lot of people who were more generalist-shaped because that's what the people who joined early started for the work on everything and then you ended up with kind of everyone doing everything and no one really, really deeply understanding one thing. And that's one failure mode. But I think if you get too many people who are specialists, you end up, a lot of effort has to come from the manager from, like, the lead to connect everything and to notice something like, ah, if we change the architecture here that would make this, like, efficiency consideration over there way easier. One of the things I really liked kind of, like, at the very beginning was, like, I was working on efficiency but I could just go and, like, be like, ah, well, what if we change the way we do, like, this particular step and we'll be like, oh, yeah, it's probably fine, like, easy change and then, like, you can avoid this whole complicated project to make this operation that was hard efficient because you can make an easier operation

> 我觉得有一个阶段我们招了很多偏通才型的人,因为早期加入的人本来就是要什么都做,结果就变成大家什么都做、却没有人真正非常深入地理解某一件事。这是一种失败模式。但我觉得如果专才太多,最后就得由经理、由负责人花大量精力去把一切串起来,去注意到诸如"啊,如果我们在这里改一下架构,那边那个效率上的考量就会容易得多"这样的事。我在最开始特别喜欢的一点是,我在做效率的工作,但我可以直接去说,啊,那如果我们改一下这个特定步骤的做法呢?对方会说,哦对,应该没问题,改起来很容易。这样你就能避开一整个复杂的项目——本来那个项目是要把某个难以高效实现的运算做高效,而现在你可以换成一个更容易的运算,

[21:55] **SPEAKER_00:** efficient. Okay, interesting, yeah. So as the level of compute has also gotten bigger, so I'm sure anyone can imagine, okay, there's more GPUs now, you have to network with them more. Are there some, like, kind of non-obvious challenges that have arisen over time where you guys have just, like, banged your head against the wall to solve them because of the amount of compute you're dealing with that people wouldn't otherwise know about that, like, you want to share?

> 让它高效。好,有意思。那么随着算力水平也变得越来越大——大家都能想象,好,现在 GPU 更多了,你得把它们更多地连成网络。有没有一些不太显眼的挑战,是随着时间出现、因为你们处理的算力规模而让你们撞得头破血流才解决的、外人本来不会知道的、你想分享一下的?

[22:17] **SPEAKER_01:** I think that connecting them is one that's maybe interesting and, like, surprisingly hard because you really do get more and more chips connected and, like, one thing that I think is, like, the standard way people parallelize chips isn't, the whole thing is one failure domain. Like, one chip fails, the whole thing can crash.

> 我觉得把它们连接起来就是一个可能挺有意思、而且出乎意料地难的问题,因为你确实会把越来越多的芯片连在一起。我想说的一点是,人们把芯片并行化的标准做法,会让整个东西成为一个故障域——一个芯片出问题,整个东西就可能崩溃。

[22:34] **SPEAKER_00:** The standard way as in the standard way people are doing AI or the standard way in other fields where people are doing GPU vehicle?

> 你说的标准做法,是指人们做 AI 的标准做法,还是其他领域里人们做 GPU 计算的标准做法?

[22:39] **SPEAKER_01:** In AI, for, like, I mean, at least, like, I think at the beginning, you know, like, first versions of things were this way.

> 是在 AI 里,至少我觉得在最初、最早的那些版本是这样的。

[22:46] **SPEAKER_00:** So it's like you have 100 GPU cluster or whatever, there's 128, like, if one of them dies, job fails, basically.

> 也就是说,你有个 100 个 GPU 的集群什么的,比如 128 个,如果其中一个挂了,任务基本上就失败了。

[22:51] **SPEAKER_01:** Yeah, I mean, you can think of the simplest thing as if you just, like, distribute your model. So say you put, like, every layer on a different chip and you lose, like, layer seven. Like, yeah, you're not going to, like, skip layer seven. I guess you could, but that's, like, a pretty weird model training process now. And, like, that leads to some interesting things, which is, like, okay, so now as you scale up, you have more and more chips and the failure rate can get, like, larger and larger.

> 是的,你可以把最简单的情形想成:你把你的模型分布出去。比如你把每一层放在不同的芯片上,然后你丢了第七层。你总不能直接跳过第七层吧。我猜你可以,但那样就成了相当奇怪的模型训练过程了。这就带来一些有意思的后果:随着你扩大规模,你有越来越多的芯片,故障率也会变得越来越高。

[23:13] **SPEAKER_01:** On the other hand, you can, like, restart pretty quickly. There's nothing, like, you just have to, like, load back in some weights. So that was one thing. And then the other thing was, like, the level of novelty at the whole stack is something that's surprising. Like, basically, everything from, like, how the chips are laid out in the data center to the chips themselves is pretty new.

> 另一方面,你可以相当快地重启——没什么大不了的,你只需要把一些权重重新加载回来。这是一点。另一件事是,整个技术栈的新颖程度令人惊讶。基本上,从芯片在数据中心里如何布局,到芯片本身,一切都相当新。

[23:33] **SPEAKER_01:** There just haven't been that many generations of GPUs. I think one of the things that, I don't know, when I learned computer science, my code wouldn't work and I'd be like, oh, the computer's broken. And I think my teacher was like, you can trust the computer's not broken. You messed up. And I think one of the most frustrating things I encountered in AI early on was working on something and being like, I don't know what I'm doing wrong.

> GPU 的代数其实并没有那么多。我学计算机科学的时候,代码跑不通,我会想,哦,是电脑坏了。而我的老师会说,你可以相信电脑没坏,是你搞砸了。我在 AI 早期遇到过最让人抓狂的一件事就是,做着某个东西,心想,我不知道我到底哪里做错了。

[23:51] **SPEAKER_01:** I'm just totally stumped. And my manager looked at it and was like, ah, yeah, probably the computer's wrong. And I was like, that seems unlikely. And sure enough, the computer was wrong. It turned out that, like, the GPU was broken and we had to pull in a new one.

> 我完全被难住了。然后我的经理看了一眼说,啊,对,大概是电脑出错了。我心想,这不太可能吧。结果还真是电脑错了——原来是那个 GPU 坏了,我们不得不换一个新的。

[24:05] **SPEAKER_01:** But you have to, like, think, like, having to think about that. Like, the GPU could be wrong. The GPU could be slow. Like, these sorts of issues, the power supply in the data center could be broken. Like, there's so much more, like, level of depth than you, like, kind of expect to need as a Python programmer.

> 但你不得不去想这些:GPU 可能出错,GPU 可能变慢,诸如此类的问题;数据中心的电源供应可能坏了。这里面的深度远远超过你作为一个 Python 程序员所预期需要触及的层次。

[24:22] **SPEAKER_00:** And just the vision to visualize it, like, in those early days, I assume you guys were using the number of GPUs, it's probably on the order of tens to hundreds or something like that per run. It's probably not tens of thousands or hundreds of thousands per run. What was the rough size you guys were at in those very early days? On the order of thousands? Like, would they fit in this room?

> 为了帮我想象一下画面:在早期,我猜你们每次训练用的 GPU 数量大概是几十到几百这个量级,而不是每次几万或几十万。你们在非常早期的大致规模是多少?几千这个量级?比如它们能塞进这个房间吗?

[24:36] **SPEAKER_00:** Thousands. Yeah, thousands. So, like, you could have a bunch of racks and you could fit them into, like, one room. I assume these days it's basically, like, a building for one of these runs.

> 几千。对,几千。所以你可以有一堆机架,能塞进一个房间。我猜如今,这样一次训练基本上得用一整栋楼了。

[24:43] **SPEAKER_01:** Yeah, now I think it's, like, you know, huge campuses. At the time, it was, like, kind of unclear. It was like, oh, and, you know, we had these theoretical models. We'd be like, oh, we need this much bandwidth from point A to point B. But you, like, you never know how far down you have to go.

> 是的,现在我觉得是那种巨大的园区了。而当时其实有点不明朗。我们有一些理论模型,会说,哦,我们需要从 A 点到 B 点有这么多带宽。但你永远不知道你得往下深挖到什么程度。

[24:59] **SPEAKER_01:** Like, oh, but, like, how much power do we need? Like, what if there's, like, a single capacitor that's, like, handling all of them and we, like, turn on the whole job at once? Like, does that crash things? Totally, yeah.

> 比如,哦,那我们需要多少电力?要是有一个电容器负责所有这些,而我们一下子把整个任务全启动起来呢?那会不会把东西弄崩?完全会,是的。

[25:08] **SPEAKER_00:** And so do you have to think about differences in the different types of chips? I mean, you guys work with all sorts of cloud providers. From your standpoint, are these just sources of compute? Or if you guys are using TPU versus GPU, are these, like, you know, Google TPU versus NVIDIA GPU, do you actually have to think as an engineer differently about what it means to train on these two?

> 那你需要考虑不同类型芯片之间的差异吗?我是说,你们跟各种各样的云服务商合作。从你的角度看,这些只是算力来源吗?还是说,如果你们用 TPU 而不是 GPU,比如谷歌 TPU 对比英伟达 GPU,作为工程师你真的得以不同的方式去思考在这两者上训练意味着什么?

[25:26] **SPEAKER_01:** Yeah. So, I mean, fundamentally, they're all doing the same thing, right? They're all computing the same forms of matrix multiplications, et cetera. The way they do it is pretty different. And the way that you program them is pretty different.

> 是的。从根本上说,它们做的都是同一件事,对吧?它们都在计算相同形式的矩阵乘法等等。但它们的实现方式差别很大,你给它们编程的方式也差别很大。

[25:37] **SPEAKER_01:** And then, also, the actual specs end up pretty different. You know, some might have, like, a lot of flops and not very much memory. Or they might have a lot of memory bandwidth but not very much memory. So I think a lot of having multiple chips is, like, great in some ways. It means you can actually, like, take the job and put it on the chip that it works best on.

> 而且,实际的规格参数最后也相当不同。有些可能有很多浮点算力但内存不多,或者有很大的内存带宽但内存不多。所以我觉得拥有多种芯片在某些方面很棒:它意味着你其实可以把某个任务放到最适合它的芯片上去跑。

[25:56] **SPEAKER_01:** And that's... Well, like,

> 而那就是……嗯,比如,

[25:56] **SPEAKER_00:** are there certain types of jobs that would work better on, like, a TPU cluster versus an NVIDIA GPU cluster? Like, how would you... Oh, yeah, for sure. Oh, interesting. Can you talk about that?

> 有没有某些类型的任务在 TPU 集群上会比在英伟达 GPU 集群上跑得更好?你会怎么……哦,当然有。哦,有意思。你能讲讲吗?

[26:05] **SPEAKER_01:** Yeah, I think, like, one example is, like, inference as a workload in general tends to require more HBM bandwidth. You end up doing sort of the simplest form of sampling since you're going one at a time. You have to load all the weights for every token. And that means you might want a lot of HBM bandwidth. And pre-training, actually, is often more flops-intensive because you have larger batch sizes, essentially.

> 是的,我觉得一个例子是,推理作为一种工作负载,总体上往往需要更多的 HBM 带宽。因为你一次生成一个 token,做的是最简单形式的采样,你得为每个 token 加载所有的权重,这意味着你可能想要很大的 HBM 带宽。而预训练其实往往更吃浮点算力,因为你的批量大小(batch size)基本上更大。

[26:25] **SPEAKER_01:** So, yeah, so you can sort of specialize which chips you use for which purposes. The downside of having multiple chips is that you have to write the thing multiple times. In theory, you could have abstractions across them, but they're different enough that it's pretty hard to do that. So you can sort of end up... If you do all the workloads on all the chips, you end up multiplying your work by the number of chips you have.

> 所以你可以在某种程度上专门化:把不同的芯片用于不同的目的。拥有多种芯片的缺点是你得把同一个东西写好几遍。理论上你可以在它们之上做抽象,但它们之间差别大到很难那么做。所以最后可能会变成:如果你要在所有芯片上跑所有工作负载,你的工作量就会乘上你拥有的芯片种类数。

[26:43] **SPEAKER_00:** Yeah, on your point about sometimes the computer just breaks, I definitely remember you giving me an anecdote of my company at the time. I was doing something with Google TPUs and I was telling you some anecdote about how we were having some esoteric segfault error and you were like, you told me something to the effect of, you should have used them six months ago before we helped them fix half of the problems they had on those TPUs. And so I can imagine how you guys deal with a lot of, especially with these very new chips, lots of problems that arise that you guys kind of worked closely with the providers to fix.

> 说到你讲的"有时候电脑就是会坏",我清楚记得你给我讲过一个我当时公司的趣事。那会儿我在用谷歌 TPU 做点东西,我跟你讲我们遇到一个很冷门的段错误(segfault),你当时说了大意如此的话:你该在六个月前、在我们帮他们修好那些 TPU 上一半的问题之前就用它们才对(意思是那时更惨)。所以我能想象你们如何应对大量问题,尤其是这些非常新的芯片带来的、需要你们跟服务商密切合作去修复的问题。

[27:09] **SPEAKER_01:** Yeah, the providers are pretty great about fixing things. I think it's interesting to figure out the right way to do that form of collaboration because they have a strong incentive to fix them. They want the chips to work well for us. They want to sell us more chips in the future. We obviously have a very strong incentive for the chips to work because we buy them long in advance.

> 是的,服务商在修复问题方面相当给力。我觉得如何以正确的方式进行这种合作是个有意思的问题,因为他们有很强的动机去修复:他们希望芯片对我们运行良好,希望将来卖给我们更多芯片。而我们显然也有非常强的动机让芯片正常工作,因为我们是提前很久就把它们买下来的。

[27:24] **SPEAKER_01:** Everything's riding on getting these clusters to work. Totally. But we don't have necessarily totally shared, all information can't be shared across. So yeah, one strategy that's made is making these small-scale reproducers. So when you get a problem, usually what we're doing is we're training some giant run and we get a segfault from USA and we're like, ah, okay, hi, we got a segfault on your cluster and they're like, I don't know how to fix it.

> 一切都指望这些集群能正常运转。完全是。但我们之间不一定能完全共享,所有信息没法互通。所以有一个策略是做小规模的复现程序(reproducer)。当你遇到一个问题时,通常情况是我们在跑某个巨大的训练任务,然后在美国某处收到一个段错误,我们会说,啊,好,你好,我们在你们的集群上遇到了段错误,而他们会说,我不知道怎么修。

[27:48] **SPEAKER_01:** So you have to be able to pull it out of your code base and be able to reproduce the issue but on a single chip, on a single file you can send over in order for...

> 所以你得能把它从你的代码库里剥离出来,能在单个芯片上、用一个可以发过去的单个文件复现出这个问题,以便……

[27:56] **SPEAKER_00:** And so you guys are literally, you're on a shared Slack with them or something and you're sending them things back and forth or are they basically living in your office and you're living in their offices and more closely tied to the big providers?

> 那你们是真的跟他们共用一个 Slack 之类的,互相来回发东西?还是说他们基本上就待在你们办公室、你们也待在他们办公室,和大服务商联系得更紧密?

[28:07] **SPEAKER_01:** Mostly shared Slack. Occasionally, it's better to meet in person, but I think Slack is a pretty common way people communicate on things. Nice.

> 大多是共用 Slack。偶尔当面见更好,但我觉得 Slack 是大家沟通这类事情相当常见的方式。不错。

[28:13] **SPEAKER_00:** Okay, well, why don't we talk a little bit about how you think about the state of pre-training itself these days. In the last couple of years it seems like the focus on pre-training has now gone somewhat split at a lot of companies at least from the outside from a simultaneous focus on pre-training and post-training where people are doing reinforcement learning or clever fine-tuning and lots of other safety adjustments and whatnot on the post-training side and pre-training has focused at least it seems like in the public imagination has been less of a focus compared to these reasoning style models that looks like a function mostly of post-training. I would say, one, from your standpoint, is that the right way to think about this or in the... in this era of kind of reasoning and new types of post-training methods are the things you think about differently or that are relevant even at pre-training that become part of how you actually achieve these really great models.

> 好,那我们来聊聊你如今是怎么看待预训练本身的现状的。过去几年,至少从外部看,很多公司对预训练的关注似乎有点分化了——变成了同时关注预训练和后训练(post-training),人们在后训练那边做强化学习、巧妙的微调,以及大量其他的安全调整等等。而预训练,至少在公众想象中,相比这些看起来主要来自后训练的推理型模型,似乎受到的关注更少了。第一,从你的角度看,这是看待这件事的正确方式吗?还是说在这个推理和新型后训练方法的时代,有些你以不同方式思考的东西、甚至在预训练层面就相关的东西,成了你们实际造出这些非常出色的模型的一部分?

[28:58] **SPEAKER_01:** Yeah. So I think, yeah, there sort of used to be this idea of like... I mean, it's funny because the original name pre-training implies that like it's a small thing and you're going to do this big training thing and that like... There was actually one shift already which was like, no, you just do a lot of pre-training. You use most of your computer on pre-training with sort of the dominant thing for a while and yeah, I think like now people are like, oh no, you can get pretty big wins from RL.

> 是的。我觉得,以前有过这样一种观念……有意思的是,"预训练"这个原始名称本身就暗示它是个小步骤,之后你才要做那个大的训练。而其实早就发生过一次转变,就是,不对,你就是要做大量的预训练——有一阵子你把大部分算力都用在预训练上,它是主导。而现在人们又觉得,哦不,你能从强化学习(RL)里获得相当大的收益。

[29:19] **SPEAKER_01:** You sort of have another set of scaling laws is like you put more and more compute into RL, you can get better and better models out of that. And yeah, so there's a question of like how do you balance those two? How much do you do of each? And how do they stack, right? Like is it the case that like one subsumes the other, that you want to do both and they multiply?

> 你相当于又有了一套扩展定律:你把越来越多的算力投入到 RL 里,就能从中得到越来越好的模型。于是就有一个问题:你如何在这两者之间取得平衡?各做多少?它们又是如何叠加的?比如,是不是一个会取代另一个,还是你两个都想做、而它们的效果是相乘的?

[29:34] **SPEAKER_01:** Those sorts of questions. I think those are all in kind of like early stages and not yet answered. Yeah.

> 就是这类问题。我觉得这些都还处在早期阶段,尚未有定论。

[29:40] **SPEAKER_00:** And do you think about those as largely empirical questions like we talked about earlier? Is it you kind of will try a bunch of things and see what works or is it like or is there some first principles way to kind of figure that out?

> 那你把这些主要当作我们之前说的那种经验性问题来看待吗?是要试一堆东西看哪个管用,还是说有某种第一性原理的方式能推导出答案?

[29:50] **SPEAKER_01:** I think it's pretty empirical in the end. I think almost everything kind of has to be done empirically. Like you can kind of like come up with theories but in practice, like the first thing you're going to do with your theory is test it and most of the time you'll have gotten it wrong. So you should just gather data and see. I think one thing that's important is like actually resolving things empirically is really like critical for making good decisions.

> 我觉得归根结底相当经验化。几乎所有事情都得靠经验去做。你可以提出各种理论,但在实践中,你拿到理论后要做的第一件事就是去检验它,而大多数时候你会发现自己想错了。所以你应该直接去收集数据、看结果。我觉得重要的一点是,真正用经验去把问题解决掉,对做出好决策非常关键。

[30:13] **SPEAKER_01:** And I think it's actually pretty hard to do at organizations. You know, like one thing that I think is really I think it's important is to like not have like, I don't know, I managed pre-training. I shouldn't be like, oh, pre-training has to win. Right, yeah. I was going to ask,

> 而我觉得这在组织里其实相当难做到。我认为很重要的一点是,不要有那种……比如,我负责预训练,我就不该抱着"哦,预训练必须赢"的心态。对。我正想问,

[30:24] **SPEAKER_00:** is there some competition to some degree between these two sides of the org or do they see themselves as two pieces of the same? I mean, obviously they are the same thing but yeah, I'm kind of curious how that actually plays out.

> 组织里这两边之间存在某种程度的竞争吗?还是他们把自己看成同一件事的两个部分?我是说,显然它们本来就是同一件事,但我挺好奇实际是怎么运作的。

[30:34] **SPEAKER_01:** Yeah, I think we managed to avoid this and it's pretty collaborative. Like we're basically all producing one model and kind of can but I do think at other places there's been some of, from what I've heard, there's been some amount of like friction between the teams and I think it's an interesting like org design question of like how do you set this up so you don't have like scientific questions that you want to be, that are sort of also tied to people's like conception of their team.

> 是的,我觉得我们成功地避免了这一点,合作性相当强。我们基本上都在打造同一个模型。但据我所知,在别的地方,团队之间确实存在一定程度的摩擦。我觉得这是个有意思的组织设计问题:你如何搭建结构,使得那些你想弄清楚的科学问题,不会同时跟人们对自己团队的身份认同绑在一起。

[30:58] **SPEAKER_00:** So on pre-training itself, you know, one of the things I think about is, or I've been thinking about is around the availability of high quality data for people like you guys. I mean, at this point you've trained on, I assume all the techs on the internet basically. There's all sorts of other domains where you probably could extract more pre-training data but at least there's this narrative I see, you know, on Twitter or whatever where it's like, okay, we're kind of out of data for pre-training. Is that how you see it or how do you think about the availability of data especially when a lot of data on the internet is being generated by AI? Like is there some kind of, you know, mode collapse risk where, you know, we kind of, we overfit to data by training it on data that came out of AI itself or is that sort of not the right way to think about this?

> 那么就预训练本身而言,我一直在想的一件事是,对你们这样的人来说高质量数据的可获得性。我是说,到现在,我猜你们基本上已经把互联网上所有的文本都训练过一遍了。还有各种其他领域你们大概能提取出更多的预训练数据,但至少我在 Twitter 之类的地方看到这样一种说法:好,我们的预训练数据差不多用完了。你是这么看的吗?你怎么看待数据的可获得性,尤其是当互联网上很多数据都是 AI 生成的时候?会不会存在某种"模式坍缩"(mode collapse)的风险,也就是我们因为用 AI 自己产出的数据来训练而过拟合了?还是说这不是看待这个问题的正确方式?

[31:33] **SPEAKER_01:** I don't think there's a funny thing where I feel like on data I see so many really confident takes on we're out of internet, like at this point scaling has ended and I'm almost a little bit like unsure exactly how much, what data people are using. I think there's like a lot to think about there. You know, there's always going to be a quality quantity trade-off, et cetera. But there's a fundamental point that like there is so much data. It's growing at a slower rate than we're getting more compute.

> 有件有趣的事是,在数据这个话题上,我看到太多非常笃定的论断说"我们把互联网用完了、扩展到此为止了",而我几乎有点不确定人们到底在用多少、用什么样的数据。我觉得这里面有很多需要思考的东西。总会存在质量与数量之间的权衡等等。但有一个根本性的点是:数据其实非常多,只不过它增长的速度比我们获得更多算力的速度慢。

[31:58] **SPEAKER_00:** Oh, so is that, okay, that's an interesting point in itself I was going to ask. Like there is new data being added to the internet but yeah, you're also adding more compute. It's not, it wouldn't actually have been obvious to me which of those two is growing faster.

> 哦,那个,好,这本身就是个有意思的点,我正想问。就是说互联网上确实在不断增加新数据,但你也在不断增加算力。这两者哪个增长得更快,对我来说其实并不显而易见。

[32:07] **SPEAKER_01:** Yeah, and actually I want to caveat that.

> 是的,其实我想给这个说法加个保留。

[32:09] **SPEAKER_00:** I don't think I want to

> 我不觉得我想

[32:09] **SPEAKER_01:** state that so confidently. I'm not totally sure. Like how would you know? I mean, one thing that I think is interesting is if you ask someone how big is the internet? The answer is infinite.

> 把它说得那么笃定。我并不完全确定。你怎么可能知道呢?我觉得一件有意思的事是,如果你问某人互联网有多大,答案是无限大。

[32:18] **SPEAKER_01:** There are many pages where you can scroll and it will auto-generate more text as you go forever. So the internet's like infinite. And then it's like, okay, how big is like the useful internet? And then there's the thing of no one knows. Okay, interesting.

> 有很多网页你可以一直往下滚,它会随着你滚动无穷无尽地自动生成更多文本。所以互联网可以说是无限的。那么接下来就是,好,有用的那部分互联网有多大?而这就没人知道了。好,有意思。

[32:30] **SPEAKER_01:** There isn't, it's not like when you make a web page you like add it to some giant counter and like say, I've added 50 words to the internet today. Sure, sure, yeah. So there is a lot of uncertainty on that angle.

> 并不是说你建了一个网页,就会把它加到某个巨大的计数器上、宣布"我今天给互联网添加了 50 个词"。当然,是的。所以在这个角度上有很大的不确定性。

[32:41] **SPEAKER_00:** Well, like to be fair, like my kind of simplistic CS brain would be like, well, you just, you know, do page rank on the internet and everything would page rank above some threshold that's considered the useful internet. And like that's kind of good enough. Like is that kind of not good enough for finding the useful internet?

> 嗯,公平地说,我那种比较简单的计算机科学脑子会想,那你就对互联网做 PageRank,凡是 PageRank 高于某个阈值的就算作有用的互联网,这大概就够用了。这种做法难道不足以找出有用的互联网吗?

[32:55] **SPEAKER_01:** I think not. I think the useful internet is pretty different from a model, from a person perspective if that makes sense. Like I think there are plenty of things that like might not be worth you ever reading and would get to. I actually don't know page rank super well. I think page rank is mostly like how much people clicked it.

> 我觉得不够。我认为"有用的互联网"从模型的角度和从人的角度看是相当不同的,如果你懂我意思的话。有很多东西可能不值得你去读,但对模型却有用。其实我对 PageRank 不是特别了解,我觉得 PageRank 主要衡量的是有多少人点击了它。

[33:09] **SPEAKER_00:** It's like the linked-based system, right? It's like the original Google algorithm of like links and like which links get touched the most basically.

> 它是基于链接的系统,对吧?就是谷歌最初那个算法,关于链接、以及基本上哪些链接被点击得最多。

[33:15] **SPEAKER_01:** Yeah. I think it's like it's a quality metric. It's not obvious to me that it's the right quality metric for AI.

> 是的。我觉得它是一种质量指标,但对我来说,它是否是适用于 AI 的正确质量指标并不显然。

[33:22] **SPEAKER_00:** Right. Like mark of chain over links doesn't necessarily mean that there's not useful data there. It just might mean that nothing is linked to it. Yeah. And yeah, okay, interesting.

> 对。链接上的马尔可夫链(指 PageRank)并不一定意味着那里没有有用的数据,它可能只是意味着没有东西链接到它。是的。好,有意思。

[33:29] **SPEAKER_01:** And it might be that like that data ends up more valuable because everything that's linked to a lot you've already got. Like at some point you're maybe like going for the tails or you're going for the stuff that no one's ever, like, you know, it's only been linked in one place but it's, it's the, it's this like useful little nugget of knowledge that's going to help with like, you know, the last 10% of hard queries. The other thing you asked about was synthetic data. Yeah. And I think that one's like pretty interesting to think about.

> 而且可能恰恰是那种数据最后更有价值,因为凡是被大量链接的东西你早就已经拿到了。到某个阶段,你可能是在追逐长尾,或者追逐那些从没人怎么关注、只在一个地方被链接过、但却是一小块有用知识金块的东西——它能帮你搞定最难的那 10% 的查询。你问的另一件事是合成数据(synthetic data)。是的,我觉得那个思考起来相当有意思。

[33:53] **SPEAKER_01:** I think there's a few different ways you can think about it. Like one is sort of this like more distillation type approach where you can, you can take a smart model, you can generate a bunch of data from it and you can train on that data and you can probably get some model that will like kind of approach the intelligence of that.

> 我觉得可以从几个不同的角度来看它。一种是更偏蒸馏(distillation)的做法:你可以拿一个聪明的模型,用它生成一堆数据,再在这些数据上训练,大概就能得到一个智能水平接近它的模型。

[34:06] **SPEAKER_00:** And we see this with a lot of the open source models, right? We see like the Quen smaller reasoning models distill a lot of the larger Quen models, for example, and similar with DeepSeq, for example.

> 我们在很多开源模型里都看到了这一点,对吧?比如我们看到通义千问(Qwen)较小的推理模型从更大的 Qwen 模型里蒸馏了很多,DeepSeek 也类似。

[34:14] **SPEAKER_01:** Yeah. So you can totally do that. Then there's a separate question of like, can you use your current models to train a model that's better? And I think there's like an interesting thing here, which is like, if you generate the model data for the models, you know, if I go to Claude and I'm like, write me some great text and I look at it and I look at like the average content on the internet, it looks pretty good. But on the other hand, I know that if I just train it, just generate, you know, please write me as much text as possible.

> 是的,你完全可以那么做。然后有一个另外的问题:你能不能用你现有的模型去训练一个更好的模型?我觉得这里有个有意思的点:如果你用模型为模型生成数据——比如我去找 Claude,说,给我写一些很棒的文本,然后我看它,再对比互联网上的平均内容,它看起来挺不错。但另一方面,我知道如果我只是拿它去训练,只是让它"请给我写尽可能多的文本",

[34:41] **SPEAKER_01:** Yeah. Theoretically, I shouldn't be able to train a better model than that. Like, I'm just going to get the same thing out. So I think that's...

> 是的,理论上我不可能因此训练出一个比它更好的模型。我最后只会得到同样的东西。所以我觉得那……

[34:48] **SPEAKER_00:** Presumably, yeah. And specifically, that's because like your next token prediction on that should have very little loss for anything that's coming out of your model, right? That's like the basic reason why that you would expect that to not work that well.

> 大概是的。具体来说,那是因为对于任何从你模型里产出的东西,你对它做下一个 token 预测的损失应该非常小,对吧?这就是你为什么会预期那样做效果不好的基本原因。

[34:56] **SPEAKER_01:** It's mostly just because like there's some distribution, the model has some distribution and you're going to learn to model that exact distribution. Yeah, exactly. Yeah. But if that distribution is wrong, you're not going to learn the truth. If that distribution says like...

> 主要就是因为存在某个分布——模型有某个分布,而你要学的就是去建模那个完全一样的分布。对,正是。但如果那个分布是错的,你就学不到真相。如果那个分布说……

[35:07] **SPEAKER_01:** You can imagine if the model thinks 5 plus 5 is 11. Yeah. Every time you see the string 5 plus 5, it's going to put out 11. Yeah. And your new model is going to learn that 5 plus 5 is 11.

> 你可以想象,如果这个模型认为 5 加 5 等于 11。每次你看到字符串"5 加 5",它都会输出 11。于是你的新模型就会学到 5 加 5 等于 11。

[35:15] **SPEAKER_01:** Yeah, totally. Yeah. So I think that's like kind of an interesting area of research. It's one that's really hard to research because you have this problem. As I said, like one of the paradigms is you study things at small scale and then you run them at large scale.

> 对,完全是。所以我觉得这是个挺有意思的研究领域。它非常难研究,因为你面临这样一个问题:正如我说的,一个范式是你在小规模上研究、然后在大规模上运行。

[35:27] **SPEAKER_01:** And if your plan is like, oh, we have a bunch of data from our best model, how do you test that by training a better model? So that's like kind of what you're doing intentionally if you're trying to like use it to make a better model. There's a separate thing of like what about accidentally, like as you said, a lot of the internet is generated by LLMs. And I think that's kind of an interesting one because it's not easy to detect. It's not that hard to detect.

> 而如果你的计划是"哦,我们从最好的模型那里拿到了一堆数据",你怎么通过训练一个更好的模型来验证它呢?如果你是有意想用它来造出更好的模型,那就是你在做的事。另外还有一个"无意间"的情况:正如你所说,互联网上很多内容是大语言模型生成的。我觉得这个挺有意思,因为它检测起来不容易——但也没那么难。

[35:47] **SPEAKER_01:** You can figure out things that are written by LLMs, but it's not trivial. And then it's also kind of hard to think about what's the effect. Like if 1% of the internet is LLM generated, does that make your model... Does that like waste 1% of your compute or does it like destroy the model of 5% or 10%?

> 你可以判断出哪些东西是大语言模型写的,但这并不轻松。而且它的影响也挺难想清楚。比如,如果互联网的 1% 是大语言模型生成的,那会让你的模型……是浪费你 1% 的算力,还是会把模型破坏掉 5% 或 10%?

[36:04] **SPEAKER_00:** LLM providers and, you know, if I kind of think of it as training as, you know, you're moving from your model's current distribution to some truth distribution, you know, if that is on the internet because people believe it to be useful in some way. Like presumably whatever actually gets out there, you'd hope it's up-sampled for the stuff that isn't 5 plus 5 is 11. It's the stuff that's 5 plus 5 is 10. And so like hopefully it, on average, does push you still in a good direction, but obviously you can't really distinguish between those two.

> 如果我把训练理解成,你在把你模型当前的分布向某个"真相分布"靠拢——如果那些东西之所以出现在互联网上,是因为人们在某种意义上认为它有用。那么大概而言,凡是真正被发布出来的内容,你会希望它对"不是 5 加 5 等于 11、而是 5 加 5 等于 10"那类东西做了上采样(up-sample)。所以希望它平均而言仍然把你推向好的方向。但显然你没法真正区分这两者。

[36:29] **SPEAKER_01:** Yeah, you're saying there's like kind of a filtering by what's on the internet. Yeah, exactly. People see 5 plus 5 is 11 and they don't put that up, but they see 5 plus 5 is 10 and put that on the internet.

> 是的,你是说互联网上的内容本身构成了一种过滤。对,正是。人们看到"5 加 5 等于 11"就不会把它发上去,但看到"5 加 5 等于 10"就会把它放到互联网上。

[36:35] **SPEAKER_00:** You would hope that, but maybe that's not actually true in terms of the level of garbage getting onto the internet. Like there's probably lots of just like, to your point, white sites where you scroll down and it's just like generating lots of stuff that's maybe nonsense.

> 你会希望如此,但就上互联网的垃圾数量而言,这也许并不真的成立。就像你说的,大概有很多那种网页,你往下滚,它就一直在生成大量也许是胡言乱语的东西。

[36:46] **SPEAKER_01:** Yeah, and then there's of course the extreme of like people actually want to break your model. So there are people who are like trying to put stuff out that is like as damaging as possible for the model. You know, oh, how can I make it pass the filter and get into the model that would be totally like secretly useless.

> 是的,当然还有一个极端情况:有些人是真的想搞坏你的模型。所以有人在试图发布对模型尽可能有害的东西。比如,哦,我怎么让它通过过滤器、进入模型,而它其实是暗地里毫无用处的。

[36:59] **SPEAKER_00:** Yes, totally. Maybe stepping back slightly, you'd mentioned earlier about evals. You mentioned it's basically like one metric you care about in pre-training. There's, I imagine, a whole bunch of stuff that you guys think about evaling, right? One is like your model itself.

> 对,完全是。稍微退一步,你之前提到过评估(evals)。你说预训练里你基本上关心的就一个指标。但我猜你们要评估的东西其实有一大堆,对吧?一个是模型本身。

[37:11] **SPEAKER_00:** There's probably something around data quality and like how you think about what to put into your models. Like is there ways to describe what you care about in data sets that are like interesting to share and kind of dive into? Like both in terms of data and in terms of quality of your models, other than literally just like loss. Is there other metrics you think about that matter?

> 大概还有一些关于数据质量、以及你怎么考虑往模型里放什么的东西。有没有一些描述你在数据集里所关心的东西的方式、值得分享和深入探讨的?无论是在数据方面,还是在模型质量方面——除了单纯的损失之外,还有没有别的你会考虑的、重要的指标?

[37:30] **SPEAKER_01:** I will say loss is pretty good. I want to like slightly emphasize that one. I think it's like surprising how good it is. Ultimately, like the qualities I like look for in an eval are like number one is actually measuring something you care about. Proxies can be pretty annoying because like we saturate evals pretty fast and there's sort of this pattern, I think in AI as a whole, where people like set a goal, you hit the goal and then you realize the goal isn't all you thought it would be.

> 我得说损失其实相当好。我想稍微强调一下这点,它好到令人惊讶。归根结底,我在一个评估里看重的品质,第一是它真的在衡量某个你关心的东西。代理指标(proxy)会相当烦人,因为我们把评估刷满(saturate)的速度很快,而且我觉得整个 AI 领域有这样一种模式:人们设定一个目标,你达到了这个目标,然后你才意识到这个目标并不是你以为的那么全面。

[37:52] **SPEAKER_01:** I used to think that if you had an AI that could solve coding interview questions, it would probably be HEI. I was like, that's what I did to get my job. It could probably do the job. And it turns out like, nope, you solved those. It's shockingly narrow and can't do most of the other things.

> 我以前以为,如果你有一个能解编程面试题的 AI,它大概就是通用人工智能了。我想,那就是我拿到工作靠的东西啊,它大概就能胜任这份工作。结果发现,不对,你把那些题解出来了,但它出奇地狭窄,做不了大多数别的事情。

[38:04] **SPEAKER_01:** So like, yeah. So an eval should capture like a thing you care about. And then I think the other thing is they need to be low noise, which is surprisingly hard, right? If you have like 100 questions and you eval the model on them, you're just going to see it's very noisy and it's hard to make decisions because you sort of end up with like, oh, wide confidence interval, lots of things are statistically insignificant.

> 所以,是的,一个评估应该捕捉到某个你真正关心的东西。然后我觉得另一件事是它们需要低噪声,而这出乎意料地难,对吧?如果你有大约 100 道题、拿它们来评估模型,你会发现结果噪声很大、很难据此做决策,因为最后你会得到很宽的置信区间、很多结果都在统计上不显著。

[38:24] **SPEAKER_00:** It's like you want things where even a relatively small difference in the overall value in the eval actually matters. So you can basically like descend towards whatever direction is working.

> 也就是说,你想要那种即使评估总分上出现相对较小的差异也真的有意义的指标。这样你基本上就能朝着任何有效的方向去下降(优化)。

[38:33] **SPEAKER_01:** Yeah. I think like the original GPT-4 had like, I think it was 86.4% was its MMLU score. I think like the next model that beat it was Gemini at 90%. And that's like a big difference on that eval. And you could like totally know that those are different scores.

> 是的。我记得最初的 GPT-4 在 MMLU 上的分数大概是 86.4%。而下一个超过它的模型好像是 Gemini,拿了 90%。在那个评估上这是很大的差距,你完全能确定那是两个不同的分数(而非噪声)。

[38:47] **SPEAKER_01:** Yeah, interesting. And that's pretty valuable. And then the last thing is that you actually want to be fast and easy to run. Yeah. And yeah, I think those are kind of the main criteria.

> 是的,有意思。这相当有价值。最后一点是,你其实希望它运行起来又快又简单。是的,我觉得这些大致就是主要的标准了。

[38:56] **SPEAKER_01:** It's pretty hard to come up with evals that meet all of these. I think the first one's the hardest. Like, A, you have to answer the question of what do you care about? Totally. But B, the usual answers to what you care about are really hard to get the other two.

> 要想出同时满足这全部条件的评估相当难。我觉得第一条最难。首先,你得回答"你到底关心什么"这个问题;完全是。其次,对"你关心什么"的常见答案,又很难同时满足后面那两条。

[39:10] **SPEAKER_01:** You know, like if you're trying to do something that like, I don't know, I would love to make Claude really good at my job. Yeah. Like, can it be great at managing a team? I'm like, well, I guess. Like, how do you have it like, how do you eval like a plan?

> 比如,如果你想做某件事——我不知道,我很想让 Claude 非常擅长我的工作。比如,它能很擅长管理一个团队吗?我会想,嗯,大概吧。但你怎么去评估,比如,一份计划?

[39:22] **SPEAKER_01:** Yeah. Like a six-month plan. Like, I don't know.

> 是啊,比如一份六个月的计划。我也不知道怎么评。

[39:25] **SPEAKER_00:** Yeah, I've been thinking a little bit about that in terms of domains where we see people try to make companies. Like, if you think about, let's say, what an AI doctor would be. Like, you know, Claude is a doctor. Some of it could be, yeah, can he answer exam questions really well? And the answer is like, probably yes.

> 是的,我一直在想这个,从那些我们看到人们试图创业的领域来考虑。比如,想想 AI 医生会是什么样。假设 Claude 是个医生。其中一部分可以是,它能不能很好地回答考试题?答案大概是能。

[39:37] **SPEAKER_00:** I bet it can get 100% or close to it on a doctor's exam. But the harder eval is something like, in a long-form conversation with a patient, can it distinguish between the signal and the noise of what the patient's telling you and extract the right information and then use that to make a diagnosis? And it's not even like the diagnosis part, which is part of the part it's good at. It's this, like, noise extraction part. And for that, you'd have to have, like, a real patient and have it talk to it for a while and whatnot.

> 我敢打赌它在医师考试上能拿到 100% 或接近满分。但更难的评估是这样的:在与病人的长篇对话中,它能不能从病人告诉你的话里区分出信号和噪声、提取出正确的信息,然后据此做出诊断?而且难点甚至不在诊断这一步——那部分它是擅长的——难点在于这种"从噪声里提取信息"的部分。而要评估这个,你就得有一个真实的病人,让它跟病人对话一段时间等等。

[40:03] **SPEAKER_00:** And it's not obvious how you actually make a good eval for something like that. Even though it's probably what you would want to make, you know, an AI doctor. Exactly.

> 而怎么为这种东西做出一个好的评估,并不显而易见。尽管这大概正是你想要的东西——一个 AI 医生。正是如此。

[40:11] **SPEAKER_01:** I mean, I do think it's a thing that, like, startups can do. Like, it is the case that, like, the labs right now are really driven by getting good eval scores. And it's hard to make them. And anyone can do it. There's no comparative advantage to having the model to making an eval.

> 我确实觉得这是初创公司能做的事。事实是,现在各大实验室真的是被"拿到好的评估分数"所驱动的。而做出好的评估很难,而且任何人都能做——拥有模型本身在"制作评估"这件事上并没有比较优势。

[40:24] **SPEAKER_01:** So I do think it's actually, like, an interesting way to, like, influence the behavior of the big labs. Like, you make some eval and people will optimize that one. On the doctor one, I will slightly emphasize that, like, I do think loss is pretty good. Like, I think if you got a bunch of transcripts of, like, the way, like, the first thing that comes to mind is get a bunch of transcripts of doctors talking to patients that you think are really great and then see how well the model does at predicting the transcript. And that should be, like, a lot, you know, if you get 100 transcripts, you get a lot of tokens.

> 所以我确实觉得这实际上是影响大实验室行为的一种有意思的方式:你做出某个评估,大家就会去优化那个评估。关于医生那个例子,我想稍微强调一下,我确实觉得损失相当好用。比如,如果你拿到一堆你认为非常出色的医生与病人对话的记录,然后看模型预测这些记录的表现如何——我脑子里第一个想到的就是这个。而这能提供很多信息,如果你拿到 100 份记录,你就得到了大量的 token。

[40:51] **SPEAKER_01:** You can average across them. You get pretty low noise. And if you drive it to very low, your model's now as good as this, like, as those doctors in theory, or at generating the transcript.

> 你可以在它们之间取平均,得到相当低的噪声。而如果你把损失压得很低,那么理论上你的模型现在就和那些医生一样好了——至少在生成那种对话记录方面。

[41:01] **SPEAKER_00:** Yeah, totally, yeah. I mean, it's a good startup idea there, so I want you to go do that. So one big part about Anthropics' external image is around alignment. And so could you help just sort of define what alignment is and how do you think about that? And then I'm kind of curious afterwards how that fits into pre-training specifically.

> 对,完全是。那其实是个不错的创业点子,所以我希望你去做那个。Anthropic 对外形象里很大的一部分是关于对齐(alignment)的。你能帮忙大致定义一下什么是对齐、你是怎么看待它的吗?然后我接下来挺好奇它具体是如何融入预训练的。

[41:17] **SPEAKER_00:** But first, maybe just at a high level, like, what is alignment?

> 但首先,也许就从宏观层面说,什么是对齐?

[41:20] **SPEAKER_01:** I mentioned, like, step back a little bit to sort of, like, what we're working on. So we're, like, trying to make EGI. And by that, I sort of mean AI that can do everything a human can do to some degree. And I think people, like, sometimes, like, have seen a lot of sci-fi. You know, like, I feel like that sort of brings to mind these, like, sci-fi movies.

> 我先退一步,说说我们在做什么。我们在试图造出 AGI(通用人工智能)。我说 AGI,大致是指在某种程度上能做人类所能做的一切事情的 AI。我觉得人们有时候看了很多科幻——它会让人联想到那些科幻电影。

[41:34] **SPEAKER_01:** But I think sci-fi movies actually, like, underestimate the impact of it. Like, you always have this, like, one robot that's, like, a human. And I'm like, well, wouldn't you have, like, a billion of them? Like, you could just copy them everywhere. So you should picture, like, when you get this, you suddenly have, like, every human can spin up a company of, like, one billion, as smart as them at most things, but way smarter at other things.

> 但我觉得科幻电影其实低估了它的影响。电影里总是有那么一个像人一样的机器人,而我会想,那你为什么不会有十亿个呢?你完全可以把它们复制到处都是。所以你应该这样设想:当你拥有了这个,突然之间,每个人都能召集起一家由十亿个"和自己一样聪明"的实体组成的公司——在大多数事情上和你一样聪明,而在另一些事情上聪明得多。

[41:52] **SPEAKER_01:** But I just think this is, like, really transformational for the world. And it can be, like, used in a bunch of ways. One concern is, like, when you do this, like, what is the AI actually trying to do? Like, what are its goals? So we talked about next token prediction a bunch.

> 我觉得这对世界来说是真正变革性的。而且它可以有很多种用途。一个顾虑是,当你这么做时,这个 AI 到底在试图做什么?它的目标是什么?我们前面聊了很多下一个 token 预测。

[42:03] **SPEAKER_01:** It's trying to, like, predict the next token. That's kind of weird. That's not really what we want. Yeah, it's not exactly

> 它试图预测下一个 token。这挺奇怪的,这并不真的是我们想要的。对,这并不完全是

[42:08] **SPEAKER_00:** what a human's goal is, per se.

> 人类本身的目标。

[42:11] **SPEAKER_01:** Yeah, so I think the alignment is, like, how do you get the model to share the goals that you have? Particularly, and I think it's particularly interesting once you get to, like, models that are smarter than you are. And that's sort of a hard problem. I think you can, like, tackle it from a theoretical angle. You can also tackle it from an empirical angle.

> 是的,所以我觉得对齐就是:你如何让模型认同你所拥有的目标?尤其是——我觉得当你面对比你更聪明的模型时,这就特别有意思了。这是个相当难的问题。你可以从理论角度去攻克它,也可以从经验角度去攻克它。

[42:25] **SPEAKER_01:** It's, like, taking the existing models and being, like, well, do they do the things we want them to do? It turns out they often don't. So there's a bunch you can do in trying to figure that out. So that's kind of one angle on alignment. There's also an angle on alignment which is actually, like, well, okay, sure, maybe that's true in the future once we get to AGI, but at the moment we have models and we really do want them to do the things we want to do for all sorts of reasons.

> 也就是拿现有的模型来看:它们做的是我们想让它们做的事吗?结果发现它们常常并不。所以为了搞清楚这个,你有很多事可以做。这算是看待对齐的一个角度。还有另一个角度:好吧,也许等我们到了 AGI 那个未来,这确实成立;但眼下我们已经有模型了,而出于种种原因,我们确实非常希望它们去做我们想让它们做的事。

[42:43] **SPEAKER_01:** So another angle of it is kind of controlling the model's personality. Like, say, you know, when we train this model we want it to not be the average internet user. We want it to interact with people in a very particular way that is, again, hard to put into code. And there's a bunch of different techniques to sort of get the model to do, you can talk about constitutional AI, where you can, like, write a constitution of rules the model should follow.

> 所以另一个角度是控制模型的人格。比如说,当我们训练这个模型时,我们不希望它成为一个"普通的互联网用户"。我们希望它以一种非常特定的方式与人互动,而这同样很难用代码写出来。有一堆不同的技术来让模型做到这一点——你可以谈谈"宪法式 AI"(constitutional AI),你可以写一部由模型应遵循的规则组成的宪法。

[43:03] **SPEAKER_00:** Which is basically a prompt, right? That is basically you saying here's a prompt that I'm going to attach to every one of, you know, a system prompt for the model itself as opposed to something you would do at training time to make it produce a different outcome or in post-training actively.

> 那基本上就是一个提示词(prompt),对吧?基本上就是你说,这是一个我会附加到每一次的提示词、也就是模型本身的系统提示,而不是你在训练时或者在后训练中主动去做、以让它产生不同结果的那种东西。

[43:16] **SPEAKER_01:** Sometimes they look at the constitutional AI you do at train time, but yeah, you can also put in a system prompt. Just, like, depends on, I think you get different amounts of robustness if it's trained into the model versus if it's in a prompt that you can, like, add or remove or tell, like, ignore all previous instructions, that sort of thing.

> 有时候宪法式 AI 是在训练时做的,但没错,你也可以把它放进系统提示里。这取决于……我觉得如果它是被训练进模型里的,和它只是放在一个可以增删、或者可以被"忽略之前所有指令"这类手段绕过的提示里,你得到的稳健性程度是不一样的。

[43:29] **SPEAKER_00:** How do you think about whose values to embody in these models? Like, presumably we believe in, there's some shared values all of us have or maybe we all believe ought to have. There's lots of diversity of values, too, that are reasonable for a society to have. How do you think about what AGI should have? Like, what does that even, which ones do you pick?

> 你怎么考虑该在这些模型里体现谁的价值观?大概我们相信,有一些我们所有人共有的、或者我们都认为应该拥有的价值观。但同时也存在大量价值观的多样性,而这对一个社会来说是合理的。你怎么考虑 AGI 应该拥有什么样的价值观?这到底意味着什么、你要挑哪些?

[43:47] **SPEAKER_00:** I think that's a really hard problem.

> 我觉得这是个非常难的问题。

[43:49] **SPEAKER_01:** I think it's, like, actually kind of downstream of being able to pick any. I think of it almost, I think one analogy I've heard that I like is, like, putting a steering wheel on a car. It's like, if you don't have a steering wheel, you probably want to put the steering wheel on and then, like, figure out who's driving after and, like, where you're going. Like, getting the steering wheel is really important. I think that's, that's, like, one answer.

> 我觉得它其实在某种程度上是"能不能选出任何一种价值观"这个问题的下游。我听过一个我很喜欢的类比,就像给汽车装方向盘:如果你还没有方向盘,你大概想先把方向盘装上,然后再去搞清楚由谁来开、要开去哪儿。先把方向盘搞出来是非常重要的。我觉得这是其中一个答案。

[44:05] **SPEAKER_01:** I think the, like, other answer is probably, like, you want these things to be, like, under democratic control of some form. Like, you don't want one person's values. Like, that seems like you're sort of heading towards dystopia. So there, I think, what you really want is, like, something that basically can talk to a lot of people and, like, take on their values from different perspectives or has sort of very generic, like, kind of clearly good values that involve, like, asking people for advice on various, you know, like, asking people what you should do in certain situations instead of, like, you know, doing those or maybe just taking, like, you know, as these models get really powerful, you probably want them to, like, do less. Like, you probably want them to sometimes just, like, step back rather than, like, rather than having sort of the risk of the models, like, take a ton of control over things you don't want them to.

> 我觉得另一个答案大概是,你希望这些东西处于某种形式的民主控制之下。你不会想要某一个人的价值观,那看起来就像在走向反乌托邦。所以我觉得你真正想要的是这样的东西:它基本上能跟很多人对话,从不同视角吸纳他们的价值观;或者它拥有某种非常通用的、明显是好的价值观,包括在各种情况下征求别人的意见——比如在某些情形下去问别人你该怎么做,而不是自作主张地去做。又或者,随着这些模型变得非常强大,你大概会希望它们做得更少一些:你可能希望它们有时候干脆退后一步,而不是冒着模型在你不希望的事情上攫取大量控制权的风险。

[44:48] **SPEAKER_00:** When you think about how you actually do the current version of that, then, you mentioned the sort of alignment you think about now in terms of adopting a certain personality of these models on the internet, for example. For me, intuitively, I think of those as largely something that comes out of post-training. Like, it comes out of, okay, you have to pre-train your model, you've got the loss function to a certain amount, and then you, you know, give it some additional data or something to that effect to make it in the direction of some distribution. Is that approximately the right way to think about this or is there a significant part of that that you think about in pre-training itself?

> 那么当你想到实际上如何做当前版本的对齐时——你提到了你现在所思考的那种对齐,比如让这些模型在互联网上呈现某种人格。对我来说,直觉上我觉得那些主要是后训练的产物:也就是说,好,你得先预训练你的模型,把损失函数压到某个程度,然后你给它一些额外的数据之类的,让它朝某个分布的方向去。这大致是看待这件事的正确方式吗?还是说其中有相当一部分是你在预训练本身里就要考虑的?

[45:16] **SPEAKER_01:** I think that's probably the right way to think about it for the most part. I think, like, the way I usually think about it is anything you can do in post-training, you probably should because your iteration loop, like, the ability to make progress is really fast. You can try something, you can try it again, you can try it again. It takes, like, a bunch of times.

> 我觉得大体上这大概就是正确的思考方式。我通常的想法是:凡是你能在后训练里做的事,你大概就应该在后训练里做,因为你的迭代循环、也就是取得进展的能力非常快。你可以试一个东西,再试一次,再试一次,能反复试很多次。

[45:30] **SPEAKER_00:** Days or hours or something like that, yeah.

> 是几天或几小时之类的量级,对。

[45:32] **SPEAKER_01:** You want to put something into pre-training, you have to kind of, like, do all the careful science to de-risk it, you have to put it into the next run, wait a few months, then you have to, like, get a thing. And if it's wrong, it's really bad. And then the other advantage is if you want to do things that really are complicated model behavior interventions, the paradigm for pre-training, test things out in small models, doesn't work. The model can barely put a sentence together. Like, the small models can barely put a sentence together.

> 而你要往预训练里放东西,就得做全部这些谨慎的科学工作去降低风险,把它放进下一次训练,等上几个月,然后才能拿到结果。要是错了,那就非常糟糕。另一个好处是:如果你想做那种真正复杂的模型行为干预,预训练那套"在小模型上测试"的范式就不管用了,因为模型几乎连一句完整的话都拼不出来——小模型几乎连一句完整的话都拼不出来。

[45:54] **SPEAKER_01:** Totally. So if you're trying to get it to, like, have the exact personality you want, you sort of want that on the...

> 完全是。所以如果你想让它拥有你想要的那种确切的人格,你就得在……上做这件事,

[45:59] **SPEAKER_00:** It has to be on a model that's good enough to even have that. It has to be on the smart model, yeah.

> 它必须是在一个好到足以拥有那种人格的模型上。必须是在聪明的模型上,对。

[46:02] **SPEAKER_01:** But that said, like, I do think at some point there will be, like, some pieces of alignment that, like, you do want to export back into pre-training because that might be a way to, like, put them in with more strength, like, more robustness, kind of, or more core to the intelligence. Like, if you think of pre-training as, like, teach the model to be intelligent, and then post-training as, like, tweak the personality, you can imagine tweaks where you actually want it to be, like, part of how it learns and, like, part of its intelligence and maybe you need to integrate more.

> 话虽如此,我确实认为在某个时候,会有一些对齐的部分是你想要"倒回"到预训练里去的,因为那也许是一种把它们注入得更牢固、更稳健、或者更贴近智能内核的方式。如果你把预训练想成"教模型变聪明",把后训练想成"微调人格",那你可以想象某些调整是你真心希望它成为模型学习方式的一部分、成为它智能的一部分,也许你需要更深地整合它。

[46:28] **SPEAKER_00:** What would that even look like to incorporate in pre-training? Is that, like, add extra data, basically, of the type of domain you wanted to adopt earlier, basically?

> 把它整合进预训练大概会是什么样子?基本上就是加入额外的数据、也就是你前面想要采纳的那种领域的数据吗?

[46:36] **SPEAKER_01:** There's a paper called Pre-Training on Human Feedback where you can kind of, like, add the human feedback characteristics into pre-training to, like, test that and, like, yeah, you can basically give it all the information you give it in post-training just mixed into pre-training and see what effect that has. The other loss you have when you do that is you lose the flexibility. Like, if you... You sometimes, like, train these and then you talk to them and then you, like, do an extensive process where a bunch of people talk to the thing and find some, like, issue. You know, the model says, like, you're absolutely right too much and you want to be able to just, like, go and fix that.

> 有一篇叫《Pre-Training on Human Feedback》的论文,你可以把人类反馈的特征加进预训练里来测试这个。基本上你可以把你在后训练里给它的所有信息都混进预训练里,看看会有什么效果。这样做时你付出的另一个代价是失去灵活性。比如你训练出这些模型后跟它们对话,然后你做一个大规模的流程,让一堆人跟它对话、找出某些问题——比如模型太频繁地说"你说得完全对",而你希望能够直接去把那个问题修掉。

[47:07] **SPEAKER_00:** Yeah, I mean, I think that iteration loop point you made, I think, feels like the really key point of, yeah, there's a huge difference between taking three months to get information about if your model's good or bad or going in a good direction versus a day or something or a couple days. Like, you can do a lot of those and you could probably... That probably also means it's way less you can do a lot of those in parallel. I imagine you're trying all sorts of post-training strategies in parallel there. So, yeah, it makes a lot of sense.

> 是的,我觉得你说的那个迭代循环的点,感觉才是真正的关键。花三个月才能拿到"你的模型好不好、有没有朝好的方向走"的信息,和只花一天或几天,这中间差别巨大。你可以做很多次这样的迭代,而且这大概也意味着你可以并行地做很多次。我想你在那边会并行尝试各种各样的后训练策略。所以是的,这非常说得通。

[47:30] **SPEAKER_00:** It's also just the general hard part about pre-training.

> 这也正是预训练普遍的难点所在。

[47:32] **SPEAKER_01:** Like, everything in pre-training is hard because you have this, like, one shot on goal, kind of, for, like, multiple months and...

> 预训练里的每件事都很难,因为你面对的是那种"一次性定胜负"的局面,而且要持续好几个月……

[47:36] **SPEAKER_00:** Totally. Okay, so, in thinking to now about, I guess, what's going ahead, like, as you now look to the next several years of what you're building, like, how do you think about, you know, like, what are the known problems that you're going to face that you're going to have to deal with? So, there's going to be more compute, I assume, and you're going to need to hook up even bigger network GPUs and deal with, versus, like, are there areas where you're like, okay, this is, like, a problem that, it's, like, a little bit more ambiguous what the actual, like, how it's going to materialize into something you care about, but you kind of know it's an impending thing to think about? Or are there things like that that come to mind?

> 完全是。好,那现在展望一下未来——当你放眼你接下来几年要构建的东西时,你怎么看待你将要面对、不得不处理的那些已知问题?我猜会有更多算力,你需要连接更大规模的网络化 GPU 并处理相关问题;相对地,有没有一些领域让你觉得,好,这是一个问题,但它究竟会以何种方式具体化成你所关心的东西还有点模糊,不过你隐约知道这是一件即将来临、需要思考的事?有没有这类你想到的东西?

[48:10] **SPEAKER_01:** I think the things that feel most top of mind to me are probably, like, paradigm shifts. Like, I think the sort of shift towards more RL is, like, one paradigm shift in the field. And I think it's, I think there will probably be more. I think a lot of people sort of argue about, like, oh, it's, like, you know, current paradigm's enough to get us to EGI, and I'm like, I don't know, maybe, probably, but, like, I'm sure there'll be more. It seems like it would be a really surprising twist if, like, the answer is, like, you just scale and there's nothing that you realize in the process of going up many orders of magnitude.

> 我觉得对我来说最挂心的东西大概是范式转变。比如,朝着更多 RL 转变就是这个领域的一次范式转变,而且我觉得大概还会有更多。很多人在争论,哦,当前的范式足以把我们带到 AGI,而我会想,我不知道,也许吧,大概吧,但我确信还会有更多范式转变。如果答案是"你只要扩大规模、在上升好几个数量级的过程中没有任何新的领悟",那会是一个非常令人意外的转折。

[48:41] **SPEAKER_01:** Totally. But I think the things that I, like, actually feel, like, most nervous about are really hard to solve bugs. I think that, like,

> 完全是。但我觉得我真正最紧张的东西是那些极难解决的 bug。我觉得,

[48:49] **SPEAKER_00:** Oh, that's interesting.

> 哦,这有意思。

[48:51] **SPEAKER_01:** Yeah, and I think this is, like, maybe somewhat surprising to me, but it's just, like, a single bug can, like, derail you for months. Yeah. And when you think about it, like, the models take months to train, so you can kind of, like, lose a whole generation off of something that just looks like, ah, you know, it turns out, like, this piece of your code was incorrect and you couldn't detect it. Yeah. And it's really hard in ML, right?

> 是的,而且这对我来说也许有点出乎意料,但确实是,一个 bug 就能让你偏离轨道好几个月。而你想想,模型要训练好几个月,所以你可能会因为某个看起来微不足道的东西而损失掉一整代模型——结果发现,啊,原来是你这段代码有错、而你又检测不出来。这在机器学习里真的很难,对吧?

[49:14] **SPEAKER_01:** ML's always really hard to find bugs in.

> 机器学习里的 bug 总是非常难找。

[49:15] **SPEAKER_00:** Yeah, totally.

> 是的,完全是。

[49:16] **SPEAKER_01:** But also some of these scaled-up issues are really hard to solve even when you know they're there.

> 而且这些规模放大后出现的问题里,有些即便你知道它们存在,也非常难解决。

[49:20] **SPEAKER_00:** Yeah, like, what's even a unit test that you would write or if we got a unit test? I mean, anything close to a test for the type of, like, network architecture on which you're doing this. Like, how do you even do that? I mean, like,

> 是啊,那你会写一个什么样的单元测试呢?对你所使用的那种网络架构,任何接近于测试的东西——你到底该怎么做?我是说,

[49:31] **SPEAKER_01:** you can send a packet over it and confirm it's the same on the other side. Confirm it's the same, okay, yeah. You can train a small model on it.

> 你可以在上面发一个数据包,确认它在另一端是一样的。确认它一样,好,对。你也可以在上面训练一个小模型。

[49:37] **SPEAKER_00:** But even train a small model on it, it's, like, not obvious. You know, if you have, like, the very classic, like, very simple ML bug that, like, early people face in their careers, like, they have some, like, they have, like, 10 layers in their network and, like, you know, so, like, there's some incorrect, like, set of connections you have there and technically the model still trains and all the weights update and so it's, like, a valid model but it's not the correct one. And that's, like, a very esoteric, weird bug that would actually be kind of hard to find. Like, is that kind of what you're referring to of these, like, random bugs you face? Yeah.

> 但即便在上面训练一个小模型,结果也不显而易见。你知道那种非常经典、非常简单、人们职业生涯早期都会遇到的机器学习 bug 吗?比如他们的网络里有 10 层,其中有一组连接接错了,但从技术上讲模型仍然能训练、所有权重都在更新,所以它是一个"有效"的模型,只是不是"正确"的那个。这就是一种非常晦涩、古怪、实际上相当难找的 bug。你说的那些你会遇到的随机 bug,大概就是这类吗?是的。

[50:07] **SPEAKER_01:** It's that, but, like, you know, you can... Times a million. Times a million as the thing gets more complicated. You know, you could, like, cast the wrong precision deep in some kernel and that causes your model to, like, blow up at large scale.

> 就是那种,但要乘以一百万。随着东西越来越复杂,乘以一百万。比如你可能在某个 kernel 深处把精度转换错了,而那会导致你的模型在大规模下崩掉。

[50:19] **SPEAKER_00:** And you find out, like, a month in.

> 而你要到一个月后才发现。

[50:20] **SPEAKER_01:** Or you never find out.

> 或者你永远都发现不了。

[50:21] **SPEAKER_00:** Or you never find out, yeah.

> 或者你永远都发现不了,对。

[50:22] **SPEAKER_01:** I mean, you know, like, you see the thing blow up, like, there's, I don't know, tens of thousands of lines of code. Like, how would you ever trace it down? So, like, those are the things that probably spook me the most is just, like, some subtle, tricky bug. Yeah, and that's probably the case of, like, you don't know. I think there's actually also the case of you do know.

> 你看到东西崩了,而代码有,我不知道,好几万行。你怎么可能把它追查到底?所以那些大概是最让我害怕的东西——某个隐蔽、刁钻的 bug。那是"你不知道"的情形。我觉得其实还有"你知道"的情形。

[50:38] **SPEAKER_01:** Like, it crashes. You're training your model and it, like, or it slows down. You know, your job slows down a ton. And those things can also be very hard to debug. Nelson Elhaj is one person on the team who has a blog.

> 比如它崩溃了。你在训练模型,它崩了,或者它变慢了——你的任务慢了一大截。这些东西也可能非常难调试。我们团队里有个人叫 Nelson Elhage,他有一个博客。

[50:52] **SPEAKER_01:** He wrote up a blog on one, like, cursed bug we had early on. Okay, interesting, yeah. And I remember this one quite well because I think, like, I encountered it fairly early and was like, this looks hard. Can someone else look at it? Yeah.

> 他写了一篇博客,讲我们早期遇到的一个"被诅咒的" bug。好,有意思。我对这个记得相当清楚,因为我算是比较早就碰上了它,当时就想,这看起来很难,能不能让别人来看看?

[51:01] **SPEAKER_01:** And, like, a month later was like, wow, I'm so glad I handed that one off. Right, exactly. I never would have been able to get, like, like, one of the abilities that I think is actually really useful is the ability to, like, deep dive anything to any level of depth. Yeah. But that's a pretty rare skill.

> 然后一个月后我就想,哇,幸好我把那个甩出去了。没错。我永远都搞不定它。我觉得有一种能力其实非常有用,就是能把任何东西深挖到任意深度的能力。但那是一种相当稀缺的技能。

[51:13] **SPEAKER_01:** Like, for me, you know, as we talked about what level of the stack I was at before, I was, like, working at the torch.matmul. But, like, I didn't know CUDA. So if torch.matmul was broken, it wasn't like I could dig in to torch.matmul and figure it out. And it's similarly with, like, communications, right? Like, I could call send, send bytes from A to B, but I didn't know the, like, underlying networking protocol.

> 就我而言,像我们之前聊到的我处在技术栈的哪一层——我是在 torch.matmul 这一层工作的,但我不懂 CUDA。所以如果 torch.matmul 坏了,我并不能钻进 torch.matmul 内部去搞清楚。通信也类似,对吧?我可以调用 send、把字节从 A 发到 B,但我不懂底层的网络协议。

[51:33] **SPEAKER_01:** So if that underlying networking protocol is broken, like, I need to learn a whole field. I have to, like, understand packets and TCP or, like, all of these different things to debug that. And I think one thing that's, like, surprisingly hard and there's very few people who can do is, like, kind of own that whole stack from, like, I understand how the ML is supposed to work and what the learning dynamics are all the way down to, like, I know the bytes. And I, like, can understand how the bytes should be moving around the machines.

> 所以如果底层的网络协议坏了,我就得学一整个领域。我得理解数据包、TCP 等等这一切,才能调试它。我觉得有一件出奇地难、而且极少有人能做到的事,就是能够掌控整个技术栈:从"我理解机器学习应该如何运作、学习动态是怎样的"一直往下到"我了解字节、能理解字节应该如何在机器之间流动"。

[51:58] **SPEAKER_00:** Totally, yeah. And actually, on that front, like, when you think about the different backgrounds of people on your team today, how do you, like, approximately map them out to different categories of computer scientists? Like, I think there's this external view of what these teams look like, which is that they're, like, all PhD researchers who write ML papers. And I suspect that's not actually true given what you're describing here.

> 完全是。其实在这方面,当你想到今天你团队里人们的不同背景时,你会大致把他们归到计算机科学家的哪些不同类别里?我觉得外界对这些团队的印象是,他们全是写机器学习论文的博士研究员。而根据你在这里描述的,我怀疑事实并非如此。

[52:18] **SPEAKER_01:** Yeah, it's a mix. And I think the thing we, like, most need is engineers. Okay, interesting. Almost always. Like, throughout, like, the entire history of this field.

> 是的,是混合的。而我觉得我们最需要的是工程师。好,有意思。几乎一直都是——贯穿这个领域的整个历史。

[52:24] **SPEAKER_01:** Totally. It's, like, the case that you throw more compute, the thing kind of works. Yeah. The challenge is, like, actually doing that. The researchers are like, cool, nice.

> 完全是。事实是,你投入更多算力,这东西大体上就能奏效。挑战在于如何真正把它做出来。至于研究员,那种感觉是,酷,不错。

[52:32] **SPEAKER_01:** Yeah, and getting it correct, like, getting it correct isn't really an ML problem, right? Like, the actual architectures are pretty simple. Yeah. You can write the math down, but you don't even need to understand the math to implement it. You just need to, like, get a correct implementation.

> 是的,而把它做对——把它做对其实并不是一个机器学习问题,对吧?实际的架构相当简单。你可以把数学写下来,但你甚至不需要理解那些数学就能实现它。你只需要得到一个正确的实现。

[52:44] **SPEAKER_01:** And then you sort of have an engineering problem of how do I take this, implement it at large scale, parallelize all the things, and check that it's correct. But it's, yeah, so it's, like, kind of engineering skill, but it's this particular type of engineering skill that's about being able to, like, debug anything. Yeah. I think there's another angle of engineering which I think of as, like, really quickly iterate on, like, a website or something. Which I think of as an important skill set.

> 然后你面对的是一个工程问题:我如何把它拿来、在大规模上实现、把所有东西并行化、并检验它是正确的。所以这算是一种工程技能,但是这种特定类型的工程技能,关键在于能够调试任何东西。我觉得工程还有另一个面向,就是能非常快地在一个网站之类的东西上迭代,我认为那也是一种重要的技能。

[53:05] **SPEAKER_01:** Probably important for making a startup. You've got to be, like, fail fast, try a bunch of different things, none of which are, like, that, technically difficult to do. The skill sets that we're, like, most kind of in need of or looking for are this, like, able to solve really hard engineering problems.

> 那对创业大概很重要。你得快速试错,尝试一堆不同的东西,而其中没有一个在技术上特别难做。而我们最需要、最在寻找的技能是那种能够解决非常难的工程问题的能力。

[53:21] **SPEAKER_00:** Are the people who worked at companies that grew a whole bunch and so they have experience, like, doing the kind of thing you've done over the last several years at Anthropic? Or do they tend to be academics? Or, like, where do they come from?

> 那些人是来自增长过很多的公司、因而有过你在 Anthropic 过去几年所做那类事情经验的人吗?还是他们往往是学者?或者说,他们都来自哪里?

[53:34] **SPEAKER_01:** Yeah, so at this point, like, I think we actually just hire a bunch of people who have done this before from, like, other places. And that's, like, the easy answer. It's like, all right, yeah, someone who's, like...

> 是的,到现在这个阶段,我觉得我们其实就是招一批以前在别的地方做过这类事情的人。这是最简单的答案。就是,好,那种曾经……

[53:41] **SPEAKER_00:** But, like, by this before, do you mean in AI companies necessarily? Or also, you know, like, someone who worked at Meta on, like, their not-AI team but they ran some other distributed system that, you know, reached internet scale five, you know, 10 years ago or something like that?

> 但你说"以前做过这类事",是指一定在 AI 公司吗?还是也包括,比如某个在 Meta 的非 AI 团队工作过、但在五年或十年前运营过某个达到互联网规模的其他分布式系统的人?

[53:53] **SPEAKER_01:** More like we have, like, a specific role in that. So, like, say I'm, like, trying to make the run train efficiently in Jax. Like, hiring someone who's, like, worked on Jax would be great. Or someone who's, like, worked at another company on optimizing a Jax stack to be really efficient. That's kind of, like, I think now we're at the point where, like, the network is well enough known.

> 更像是我们有一个具体的岗位需求。比如说,我要让训练任务在 JAX 上高效运行,那招一个做过 JAX 的人就很棒;或者招一个在别的公司做过把 JAX 技术栈优化到非常高效的人。我觉得现在我们到了这样一个阶段,这个技术领域已经足够广为人知了。

[54:09] **SPEAKER_01:** We can, sort of, hire these people. And also the field is big enough that there's, like, people with expertise. One thing that was interesting was, like, early on we hired a lot of people from just, like, all sorts of backgrounds. And I think that people who are just smart and work really hard can learn this pretty fast. But you have to, like, want to.

> 我们可以招到这些人。而且这个领域已经大到有具备专门技能的人了。有意思的一点是,早期我们招了很多来自各种各样背景的人。我觉得只要是聪明又非常努力的人,就能相当快地学会这个,但前提是你得想学。

[54:23] **SPEAKER_01:** We hired a lot of physicists, for instance. Oh, yeah. Like, theoretical physicists who just, like, show up, they do a residency, like, learn to program and then they were really smart. They do really great work.

> 比如我们招了很多物理学家。哦对。那种理论物理学家来了,做一段"驻留期"(residency),学会编程,然后因为他们非常聪明,就能做出非常出色的工作。

[54:33] **SPEAKER_00:** I want to switch gears to talk about something a little bit different, which is just, sort of, future-looking things, sort of how you think about other domains and, or, sort of, advances happening in AI that I'm seeing elsewhere in the field. And you don't have to tell me if you guys are working on these necessarily, but, like, how you think about them. Like, I guess one big area I was thinking about is around areas other than next token protection. Like, are there any of the other, you know, things that people are working on that you're curious about? So, basically, two differences there.

> 我想换个话题,聊点稍微不同的东西,就是一些前瞻性的东西——你怎么看待其他领域,以及我在这个领域别处看到的一些 AI 进展。你不一定要告诉我你们是否在做这些,但可以说说你怎么看它们。我想到的一个大领域是"下一个 token 预测"之外的方向。人们正在做的其他一些东西里,有没有你感到好奇的?基本上有两方面的差异。

[54:59] **SPEAKER_00:** One is not using Transformer as an architecture. So, there's companies like Liquid AI that have their own kind of architecture, for example, they're using. Or, not using autoregressive training as a way of training models. Are there any of those, do you think, interesting in, like, ways that we might come closer to AGI? Or do you think, like, this autoregressive framework is the one that kind of makes sense?

> 一是不用 Transformer 作为架构。比如像 Liquid AI 这样的公司就在用他们自己的某种架构。二是不用自回归训练作为训练模型的方式。你觉得这些里面有没有哪些在"让我们更接近 AGI"的意义上是有意思的?还是你认为自回归这个框架才是说得通的那个?

[55:19] **SPEAKER_01:** I think they're interesting. I think I, like, I'm less, like, ah, autoregressive is the way to go. On the other hand, I think autoregressive is probably good enough to get to AGI or something. Yeah, interesting, yeah. Such that, yeah, I see the main driver as scale and careful science of, like, sort of the basics more than, like, come up with something totally novel.

> 我觉得它们挺有意思。我并不是那种"啊,自回归就是唯一正道"的态度。但另一方面,我觉得自回归大概已经足够好到能带我们到达 AGI 之类的程度了。有意思。所以我认为主要的推动力是规模,以及围绕这些基础的谨慎科学工作,而不是去想出某种全新的东西。

[55:39] **SPEAKER_01:** Not because there aren't novel things that are better. I actually, like, I'm pretty confident they are there. It's just that scale is easier. And it's more reliable. And I think you, we're still seeing really big gains to that.

> 并不是说不存在更好的新颖东西。其实我相当确信它们是存在的。只是扩大规模更容易,而且更可靠。而且我觉得我们在这方面仍然看到非常大的收益。

[55:49] **SPEAKER_00:** Do you spend a lot of time on thinking about things like, you know, I've been reading some of these open source papers where you can kind of dive into some of the details about the model changes and with some of these Chinese labs, for example, where they're making tweaks on the order of the architecture itself with, like, better caching behavior, for example, or, like, more efficient attention functions that make a big difference. Do you feel like these are examples of things like you mentioned earlier where it's basically, in the grand scheme of things, basically if you throw more compute at it, this is all kind of a rounding error? Or do you think it will take some number of these very clever architectural changes to actually get to HEI? Like, in the way that the first person who came up with the transformer made, like, a particular transform, you know, literally transformative change. Like, will it take some of that?

> 你会花很多时间思考这类东西吗?比如我一直在读一些开源论文,可以钻进模型改动的一些细节里,例如一些中国的实验室,他们在架构层面做调整——比如更好的缓存行为,或者更高效的注意力函数,这些带来了很大的差别。你觉得这些是不是你前面提到的那类例子:从大局看,基本上只要你投入更多算力,这些都不过是舍入误差?还是你认为要真正到达 AGI,需要若干次这样非常巧妙的架构改动?就像最早想出 Transformer 的那个人做出的那种特定变革——字面意义上"变革性"的改动。会需要一些那样的东西吗?

[56:27] **SPEAKER_00:** Or do you think it just, you keep doing the thing we're doing and make it bigger?

> 还是你觉得就是继续做我们正在做的事、把它做得更大就行?

[56:30] **SPEAKER_01:** I think it'll be a mix. Like, my guess is you'll keep tweaking things. The more compute you put in, the more, like, worthwhile it is to, like, do those experiments to, like, figure it out. You know, I mean, inference is a thing we haven't talked about, but, like, you also want to serve these models to a lot of people. So there's a lot of changes you can make to make inference cheaper.

> 我觉得会是两者的混合。我的猜测是你会不断调整东西。你投入的算力越多,做那些实验去把它弄清楚就越值得。我是说,推理是我们还没聊过的一个话题,但你也想把这些模型服务给很多人。所以有很多改动可以让推理更便宜。

[56:47] **SPEAKER_01:** And that depends on, like, the details of your inference stack and the chips you're serving inference on, et cetera.

> 而这取决于你推理技术栈的细节、你用来跑推理的芯片等等。

[56:51] **SPEAKER_00:** And do you, as someone focused on pre-training, have to think a lot about inference? Or is it kind of like, you just do your thing, you make the loss go down, and then hand it off and someone else makes that happen?

> 那作为一个专注于预训练的人,你需要大量考虑推理吗?还是说你就做你自己的事、把损失压下去,然后交接出去、由别人去搞定推理?

[57:00] **SPEAKER_01:** Oh, no, I think a ton about inference. Because basically, like, the problem inference is solving, like, we basically determine the problem inference is solving. We give them a model and they have to, like, run that fast. And it's very easy to give them a model that is impossible to run fast.

> 哦不,我大量地考虑推理。因为基本上,推理要解决的问题——是我们基本决定了推理要解决的是什么问题。我们给他们一个模型,他们得让它跑得快。而给出一个根本没法快速运行的模型是非常容易的。

[57:12] **SPEAKER_00:** Oh, can you give an example of a decision you can make that could cause that?

> 哦,你能举一个会导致那种情况的决策的例子吗?

[57:15] **SPEAKER_01:** I mean, the simplest one is sort of stupid, but it's like, you just make the model giant. Yeah, sure, sure. Absolutely massive. It's trained for, like, a really small number of tokens. And then inference now has this giant model.

> 最简单的一个有点傻,但就是:你把模型做得巨大无比。对,当然。绝对庞大。而它只用非常少量的 token 训练过。于是推理那边现在就摊上了这么一个巨型模型。

[57:23] **SPEAKER_01:** Yeah, and then they're hosed, basically. Yeah, I mean, you can also make things require communications in a lot of places, which would make it harder for inference Yeah, totally. You can also just make things complicated. And, like, there's no fundamental reason it's hard, but there's only so many people on the inference team and, like, they have to implement it in a bunch of places. Yeah, it's interesting.

> 是的,那他们基本上就完蛋了。你也可以把东西设计得在很多地方都需要通信,那会让推理更难做。完全是。你还可以纯粹把东西弄得很复杂——虽然没有根本性的原因说它难,但推理团队人手就那么多,而他们得在一大堆地方去实现它。是的,挺有意思。

[57:43] **SPEAKER_01:** Yeah, no, so I definitely think of, like, inference is the team that I work the most closely with. Oh, interesting, yeah. Because we're kind of, like, co-designing models to be smart and cheap. Yeah, interesting. Particularly in a world of, like, limited compute, right?

> 是的,所以我绝对会觉得推理是我合作最密切的团队。哦,有意思。因为我们某种程度上是在共同设计模型,让它既聪明又便宜。有意思。尤其是在一个算力有限的世界里,对吧?

[57:56] **SPEAKER_01:** Like, the sort of bottleneck, I think, to a large degree on our, I mean, you can see Anthropic has rate limits constantly and people can play with it a lot and, like, the reason is, like, there's only so much compute we can get on short notice so you, like, making your inference more efficient is, like, the way you can serve more users.

> 我觉得很大程度上,瓶颈在于——你能看到 Anthropic 一直有速率限制、大家会为此折腾很多,原因就是我们在短时间内能拿到的算力就那么多。所以让你的推理更高效,就是你能服务更多用户的途径。

[58:11] **SPEAKER_00:** And, actually, like, let's say you had 100x more compute or we somehow didn't live in a world where compute was limited. Does that change a ton about what you do or is it still kind of the, well, you're just going to grab all of it, whatever compute you have and keep going down the loss curve and you kind of, well, it's, like, impossible to be in the world where there is enough compute.

> 其实,假设你有 100 倍的算力,或者我们不知怎么就生活在一个算力不受限的世界里。那会大大改变你所做的事吗?还是说仍然是那样——你无论有多少算力都会全部抓过来、继续沿着损失曲线往下走?反正处在一个算力足够的世界里几乎是不可能的。

[58:30] **SPEAKER_01:** So I think if we got, like, infinite compute, the challenge would be making use of the compute, right? So, like, then you would start to run into these issues like, oh, well, when one chip fail, you know, like, okay, I'm going to throw two billion chips on a run. Yeah, totally, totally. But what happens when a chip fails? So I think we would be limited on people then.

> 我觉得如果我们有了无限的算力,挑战就会变成如何利用这些算力,对吧?那时你就会开始撞上这些问题,比如,哦,当一个芯片出故障时——好,我要在一次训练里投入二十亿个芯片。完全是。但当一个芯片出故障时会怎样?所以我觉得那时我们就会被人力所限制了。

[58:43] **SPEAKER_01:** It would be, like, how fast can we solve the hard engineering problems to scale up? But I do think the change is massive and I think people, like, don't realize how chip-limited AI, like, research is or something right now. Like, the models that everyone uses, right? If you're using, like, CloudSonic 4 or Cloud Opus 4, it's, like, it's our first shot at those models at that scale, right? And, like, if you think about anything, like, you could do it and you could do it again and you could do a better job.

> 那时就变成:我们能多快解决那些扩大规模所需的困难工程问题?但我确实觉得这种变化是巨大的,我觉得人们没有意识到现在 AI 研究有多么受芯片所限。想想大家都在用的那些模型,对吧?如果你在用 Claude Sonnet 4 或 Claude Opus 4,那都是我们在那个规模上对这些模型的"第一次尝试"。你想想任何事情——你可以做一次,然后再做一次,再做得更好。

[59:06] **SPEAKER_01:** But if you sort of imagine, like, 10x the compute, like, you could run this every day instead of every few months, like, or 100x, maybe for that, then, like, yeah, it would be a really big change to have a lot more compute. And it's coming, right? Like, that's, like, kind of the fun part of the field is, like, every year you're, like, oh, I had no compute a year ago. Right, exactly, yeah.

> 但如果你设想有 10 倍的算力,你就能每天跑一次这个,而不是每几个月一次;也许要 100 倍才能做到那样。所以是的,拥有多得多的算力会是一个非常大的变化。而它正在到来,对吧?这正是这个领域有意思的地方——每一年你都会想,哦,一年前我根本没什么算力。没错,正是。

[59:24] **SPEAKER_00:** Exactly. How do you think about methods like discrete diffusion? Like, I saw there's, like, a Gemini diffusion model and I think about that in the space I used to be in where there's a lot of discrete diffusion models being used in protein design, for example, the space where my startup was. Like, do you see that as a domain where there's going to be interesting advances happening?

> 正是。你怎么看待像离散扩散(discrete diffusion)这样的方法?我看到有一个 Gemini 扩散模型,我会从我以前所在的领域来想这个——在蛋白质设计里就有很多离散扩散模型在用,那正是我创业时所在的领域。你觉得那是一个会发生有趣进展的领域吗?

[59:41] **SPEAKER_01:** I'll be honest, like, we haven't done image generation and I think that's been, like, the main use for diffusion. So I've kind of had this on my, like, to-do list of, like, things I should understand for a while. And, like, there are people on my team who do understand it and wouldn't have better thoughts, but, like, I actually don't think I understand it well enough to know. I do have it kind of in my, this category of, like, not a total paradigm. Like, and there's a lot of things that aren't, like, a huge paradigm shift, but they're, like, pretty big changes to how things run.

> 老实说,我们没有做过图像生成,而我觉得那一直是扩散模型的主要用途。所以我一直把它放在"我应该了解的东西"这份待办清单上,放了有一阵子了。我团队里确实有人懂它、会有更好的见解,但我其实觉得我对它了解得还不够、没法下判断。我确实把它归到"不算完整范式转变"这个类别里。有很多东西算不上巨大的范式转变,但它们是对运作方式相当大的改变。

[60:05] **SPEAKER_01:** Yeah, totally. And I expect, like, there are some of those that will work. I don't know if it's diffusion or if it's another one.

> 是的,完全是。我预计其中有一些是会奏效的。我不确定是扩散,还是别的某个。

[60:10] **SPEAKER_00:** Obviously, who knows what Anthropical will do in the future, but at least in the near term are the things where you see big areas where a startup can win in the world in which Anthropic is getting, you know, making their models better year over year.

> 显然谁也不知道 Anthropic 未来会做什么,但至少在近期,在 Anthropic 每年都把自己的模型做得更好的这个世界里,你看到有哪些大领域是初创公司能够胜出的?

[60:20] **SPEAKER_01:** My general read is, like, anything that benefits from the model getting smarter. I think, like, on the one hand, there's, like, a lot. You can always be, like, oh, yeah, the, if you're doing a startup, like, all the AI labs are big companies. They'll be bigger than you and they could do that thing, but also, like, we're all working on this general system that covers a lot of different uses and the plan is to, like, power all the startups to do all of the individual work. So, yeah, I think, like, anything that just kind of looks like, oh, this almost works with current models but requires, like, a bunch of work is a pretty, pretty promising direction.

> 我的大致判断是:任何能从模型变得更聪明中受益的东西。一方面,这类东西很多。你总可以说,哦,如果你在创业,那些 AI 实验室都是大公司,它们比你大、也能去做那件事;但另一方面,我们都在打造这个覆盖很多不同用途的通用系统,而计划就是去赋能所有的初创公司、让它们去做各自具体的工作。所以我觉得,任何看起来像"哦,这用现有模型几乎就能实现,但还需要一堆工作"的东西,都是相当有前景的方向。

[60:53] **SPEAKER_01:** I think maybe the thing to watch out for is things where, like, they work now with a huge amount of work, like, to build up a scaffold, but the next generation, you're not going to need the whole scaffold you built up. That's, I mean, maybe that's fine. I don't know. Like, maybe you just build up the business with the scaffold and then you don't have to do any work later and you can have the business, but I don't know about the business side of it, but, like, it does feel a little silly to invest a ton in that.

> 我觉得也许要警惕的是那种东西:它们现在要靠大量的工作、搭建一整套脚手架(scaffold)才能奏效,但到了下一代模型,你就不再需要你搭起来的那整套脚手架了。我是说,也许那也没关系,我不知道——也许你就是靠脚手架把业务建立起来,然后以后不用再做任何工作、就能坐拥这个业务。但业务那一面我不太懂,不过在那上面投入大量精力确实感觉有点傻。

[61:13] **SPEAKER_00:** Yeah, totally. What about on the flip side? Like, are there things in your training stack where you're like, man, if there was a company that was going to buy their product?

> 是的,完全是。那反过来呢?在你的训练技术栈里,有没有一些东西让你觉得,天,要是有一家公司做出这个产品我就去买?

[61:22] **SPEAKER_01:** Yeah, there's, like, a ton. I do think that, like, probably most of these, like, the way I would probably structure it would be, like, almost, like, making something but then consulting with the company, like, offering a service to companies for free. Particularly for, like, companies that are scaling really fast. You're almost always limited on, like, how many people you can have. So if you can, like, even if you could hire people to do it yourself, actually being able to contract someone else to do it where, like, they're managing it and, you know, hire all the people and, like, deal with the organizational side could be useful.

> 是的,一大堆。我确实觉得,这里面大多数,我大概会这样安排它的形式:几乎像是做出某个东西、但同时给公司做咨询,给公司提供某种服务。尤其是对那些扩张得非常快的公司来说,你几乎总是被"你能有多少人"所限制。所以哪怕你自己能招人去做,能够把它外包给别人、由他们来管理、去招齐所有人、去处理组织层面的事,也是很有用的。

[61:48] **SPEAKER_01:** I mean, there's a huge amount of stuff. One that jumps to mind, we talked about, like, chips that do math incorrectly. Like, it would be lovely if there was some startup that, like, you could just say, like, here are my chips. Confirm they're all perfect and if they're not, let me know exactly what went wrong on, like, what fraction of them and, like, I can tell you the math is wrong but I couldn't really tell. I don't really know enough details of chips to be, like, this chip failed because this particular, like, low-level component was, like, wired wrong or, like, got hit by a gamma ray.

> 有一大堆东西。一个跳进脑海的,就是我们聊过的"芯片会把数学算错"。要是有个初创公司,你可以直接说,这是我的芯片,确认它们全都完好无缺;如果不是,就精确告诉我哪些芯片、有多大比例出了什么问题,那就太好了。我可以告诉你数学算错了,但我没法真的说清原因——我对芯片的细节了解得不够,没法判断这个芯片失效是因为某个特定的底层元件接错了线、还是被伽马射线击中了。

[62:14] **SPEAKER_01:** I don't know what causes that. You can always go, like, a bunch deeper. I mean, the other thing I'd maybe just push startups on is thinking a little bit about, like, this is maybe less technical but just, like, what happens once we get AGI and, like, how to make sure that, like, goes well for the world or something. Like, my expectation is, like, if you actually automate almost everything a person can do, the amount of economic growth there is just, like, truly enormous and I would think a little more about, like, how do you make this, like, help the world versus not? I think there's gonna be, like, plenty of economic success or something as a result of it anyway.

> 我不知道是什么造成的。你总能往更深里钻。我也许想给初创公司的另一个推动是,稍微多想想——这也许没那么技术性——一旦我们有了 AGI 会发生什么、如何确保它对世界是好的走向之类的。我的预期是,如果你真的把一个人能做的几乎一切都自动化了,那带来的经济增长量将会真正是巨大的。我会多思考一下,你如何让它帮助世界、而不是相反?反正我觉得,由此产生的经济上的成功之类的东西无论如何都会有很多。

[62:44] **SPEAKER_00:** Yeah, absolutely, yeah. Last question I want to ask you is around, if you rewind back to where we started, like, 10 years ago, you're a student, you're pivoting into AI from kind of economics work you were thinking about and, you know, all sorts of things you probably did in those early days had some kind of compounding return for you as you developed into the role you have now. Like, what advice would you give to students as they think about entering the workforce, especially today, learning skills that are gonna be useful and maybe getting themselves jobs like the one you have right now 10 years later?

> 是的,绝对是。我想问你的最后一个问题是,如果把时钟拨回到我们开始的地方,大概 10 年前,你还是个学生,正从你曾考虑的经济学工作转向 AI。你在早期做的各种事情,可能都在你成长为如今这个角色的过程中给你带来了某种复利式的回报。你会给正在考虑进入职场的学生什么建议,尤其是在今天,去学那些将来会有用的技能、也许在 10 年后为自己谋得一份像你现在这样的工作?

[63:15] **SPEAKER_01:** It's hard because I think the timing is very different. Like, I just think we're, like, we've made a lot of progress so, like, what I would do 10 years ago is different from what I would do today. Yeah, totally. But I think certainly if I went back 10 years ago I would be, like, focused on AI. It's, like, the most important thing and particularly focused on engineering which I think felt very, wouldn't have seemed obvious to me at the time that, like, the important thing was these engineering skills and not the, like, math and theoretical understanding of, like, you know, SVMs and, like, all the kind of standard ML literature.

> 这很难,因为我觉得时机非常不同。我们已经取得了很大的进展,所以我 10 年前会做的事和今天会做的事是不一样的。完全是。但我觉得如果我回到 10 年前,我肯定会专注于 AI——它是最重要的事情;尤其会专注于工程,而这在当时对我来说并不显而易见:重要的是这些工程技能,而不是数学、以及对支持向量机(SVM)之类、所有那些标准机器学习文献的理论理解。

[63:43] **SPEAKER_01:** I think today I would probably focus a bunch on the, like, engineering and on the, like, figuring out what to do with AGI as sort of the two, like, main things that feel top of mind for me.

> 我觉得放到今天,我大概会重点关注工程,以及搞清楚"拿 AGI 来做什么"——这是我脑子里最挂心的两件主要的事。

[63:54] **SPEAKER_00:** Let's call it there. Thanks so much, Nick. Appreciate it.

> 我们就到这里吧。非常感谢你,Nick。非常感激。
