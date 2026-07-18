# 全文转录 · AI 到底有多聪明?用 ARC-AGI 重新定义"智能"

> ▶ [YouTube](https://www.youtube.com/watch?v=pBlIgs6w7Ss) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/pBlIgs6w7Ss.md) &nbsp;·&nbsp; How Intelligent Is AI, Really?

> 中英对照 · 每段英文原文下附中文翻译

[00:11] **SPEAKER_00:** I'm excited today to welcome Greg Kamrad, who is the president of the ArcPrize.

> 今天我很高兴邀请到 Greg Kamrad,他是 ArcPrize 的主席。

[00:16] **SPEAKER_01:** That's right.

> 没错。

[00:17] **SPEAKER_00:** Thanks for coming here at NeurIPS 2025 in beautiful San Diego.

> 感谢你来到美丽的圣地亚哥参加 NeurIPS 2025。

[00:21] **SPEAKER_01:** Thank you, Diana.

> 谢谢你,Diana。

[00:21] **SPEAKER_00:** So what does the ArcPrize Foundation do?

> 那么 ArcPrize 基金会是做什么的呢?

[00:25] **SPEAKER_01:** Yes. So the ArcPrize Foundation is a nonprofit, but it's a little bit of a different nonprofit because we are very tech forward. And so our mission is to pull forward open progress towards systems that can generalize just like humans.

> 好的。ArcPrize 基金会是一家非营利组织,但它有点不太一样,因为我们非常注重技术前沿。我们的使命是推动开放性的进展,朝着能够像人类一样进行泛化的系统前进。

[00:38] **SPEAKER_00:** So according to Francois Chollet, he defines intelligence as the ability to learn new things a lot more efficiently. What does that mean for founders as they look at all these benchmarks for all these model releases that are chasing MMLU numbers?

> 根据 Francois Chollet 的定义,智能是更高效地学习新事物的能力。对于那些看着一堆模型发布、追逐 MMLU 分数的各种基准测试的创业者来说,这意味着什么?

[01:08] **SPEAKER_01:** Yes, absolutely. Well, so one of the cool things about ArcPrize is we have a very opinionated definition of intelligence, and this came from Francois Chollet's paper in 2019 on the measure of intelligence. And in there, you would normally think that intelligence would be

> 是的,当然。ArcPrize 一个很酷的地方在于,我们对智能有一个非常鲜明的定义,这源自 Francois Chollet 在 2019 年关于智能度量的论文。在那篇论文里,你通常会以为智能应该是……

[01:08] **SPEAKER_?:** a very specific definition of intelligence. And in there, you would normally think that intelligence would be a very specific definition of intelligence.

> ……一个非常具体的智能定义。在那篇论文里,你通常会以为智能应该是一个非常具体的智能定义。

[01:08] **SPEAKER_01:** How much can you score in the SAT test or how hard of math problems can you do? And he actually proposed an alternative theory, which is the foundation for what ArcPrize does. And he actually defined intelligence as your ability to learn new things. So we already know that AI is really good at chess.

> 你在 SAT 考试里能考多少分,或者你能解多难的数学题?而他实际上提出了另一种理论,这正是 ArcPrize 所做工作的基础。他把智能定义为你学习新事物的能力。我们已经知道 AI 在国际象棋上非常厉害。

[01:25] **SPEAKER_01:** It's superhuman. We know that AI is really good at Go. It's superhuman. We know that it's really good at self-driving.

> 它是超人类水平的。我们知道 AI 在围棋上也非常厉害,同样是超人类水平的。我们也知道它在自动驾驶上很在行。

[01:29] **SPEAKER_01:** But getting those same systems to learn something else, a different skill, that is actually the hard part. And so Francois, alongside that, proposed his definition of intelligence. He says, well, I don't just have a definition. I also have a benchmark or a test that tests whether or not you can learn new things.

> 但要让同样的这些系统去学习别的东西、一种不同的技能,那才是真正困难的部分。因此,Francois 在提出智能定义的同时也说:我不只是有一个定义,我还有一个基准测试,用来检验你能不能学会新东西。

[01:48] **SPEAKER_01:** Because generally, people are going to learn new things over a long horizon, a couple hours, a couple days, or maybe over a lifetime. But he proposed a test called the Arc AGI, or at the time, it was just called the Arc Benchmark. And in it, he tests your ability to learn new things. So what's really cool is that not only humans can take this test, but also machines can take this test too.

> 因为一般来说,人们学习新事物是在一个较长的时间跨度里进行的——几个小时、几天,或者可能是一生。他提出了一个叫 Arc AGI 的测试,当时只是叫 Arc 基准。在这个测试里,他检验的是你学习新事物的能力。真正酷的地方在于,不仅人类可以做这个测试,机器也可以做这个测试。

[02:08] **SPEAKER_01:** So whereas other benchmarks, they might try to do what I call PhD++ problems harder and harder. So we had MMLU, we had an MMLU+, and now we have humanities last exam. Those are going superhuman, right? Arc benchmarks, normal people can do these.

> 相比之下,其他基准测试可能在做我所说的"博士++"级别的题目,越来越难。我们有过 MMLU,有过 MMLU+,现在又有"人类最后的考试"(Humanity's Last Exam)。这些都在走向超人类水平,对吧?而 Arc 基准,普通人就能做出来。

[02:22] **SPEAKER_01:** And so we actually test all of our benchmarks to make sure that normal people can do them.

> 所以我们其实会对所有基准进行测试,以确保普通人都能完成它们。

[02:25] **SPEAKER_00:** And just a bit of context for the audience, this particular prize was famously one that a lot of LLMs with just pre-training before RL came in. Yeah. In the picture before 2024, all these large models, language models were doing terribly, right?

> 给观众补充一点背景,这个奖项有一个著名之处:在强化学习(RL)出现之前,很多只经过预训练的大语言模型——是的——在 2024 年之前的那个阶段,所有这些大型语言模型表现得都很糟糕,对吧?

[02:44] **SPEAKER_01:** Yes, absolutely, doing terribly. And, you know, it's kind of weird, but nowadays it's hard to come up with problems to stump AI. You know, back in 2012 with ImageNet, all you needed to do was just show people an image of a cat and you could stump the computer. But when Francois Chollet came out with his benchmark in 2019, fast forward all the way to 2024, I think at the time it was GPT-4, the base model, no reasoning, I think it was getting 4%, 4 or 5%.

> 是的,绝对如此,表现得非常糟糕。你知道,这有点奇怪,但如今很难想出能难倒 AI 的问题了。回到 2012 年的 ImageNet,你只需要给人看一张猫的图片就能难倒计算机。但当 Francois Chollet 在 2019 年推出他的基准后,一路快进到 2024 年——我记得当时是 GPT-4,那个基础模型,没有推理能力——我记得它大概只得了 4%,4% 到 5% 左右。

[03:10] **SPEAKER_01:** So clearly show it, hey, humans can do this, but base models are not doing anything. And what's really cool actually is right at 01, I remember testing 01 and 01 preview, right when that first came out, I think performance jumped up to 21%. So you look at that and after five years, it was only 4%. And then in such a short time, it goes to 21.

> 所以这清楚地表明:嘿,人类能做到,但基础模型根本做不了什么。而真正酷的是,恰好在 o1 出现的时候——我记得我在 o1 和 o1-preview 刚发布时就测试过——性能一下子跳到了 21%。你看,五年过去了才 4%,然后在这么短的时间里就涨到了 21。

[03:27] **SPEAKER_01:** That tells you something really interesting is going on. So actually we used Arc to identify that reasoning paradigm was huge. That was actually transformational for what was contributing towards AI at the time.

> 这告诉你有一些非常有意思的事情正在发生。所以我们实际上用 Arc 识别出了"推理范式"是一件大事。在当时,它对推动 AI 发展是具有变革性意义的。

[03:37] **SPEAKER_00:** So much so that now all the big labs, XAI, OpenAI are actually now using ArcAGI as part of their model releases and the numbers that they're hitting. So it's become the standard now.

> 以至于现在所有大实验室,xAI、OpenAI,实际上都把 ArcAGI 作为他们模型发布及所达成分数的一部分。所以它现在已经成了标准。

[03:50] **SPEAKER_01:** Yeah. Well, I tell you what, we're excited that the community is recognizing that ArcAGI can tell you something. That's what we're excited about. And when public labs or frontier labs like to use us in terms of reporting their performance, it's really awesome that they too say, yes, we just came out with this frontier model.

> 是的。我跟你说,我们很兴奋看到社区认可 ArcAGI 能说明一些问题。这正是我们感到振奋的地方。当那些公开的实验室或前沿实验室愿意用我们来报告他们的性能时,他们也说"是的,我们刚推出了这个前沿模型",这真的很棒。

[04:06] **SPEAKER_01:** This is how we choose to measure our performance. And so in the past 12 months, you're right. We've had OpenAI, we've had XAI with Grok4, we've had Gemini with Gemini 3 Pro and DeepThink, and then just recently Anthropic with Opus 4.5.

> "这就是我们选择衡量自身性能的方式。"所以在过去的 12 个月里,你说得对,我们有 OpenAI,有 xAI 的 Grok 4,有 Gemini 的 Gemini 3 Pro 和 DeepThink,然后就是最近 Anthropic 的 Opus 4.5。

[04:17] **SPEAKER_00:** That's cool. So what's going well with all these releases?

> 太酷了。那么在所有这些发布中,有哪些进展是顺利的?

[04:20] **SPEAKER_01:** So it's going really well that they're adopting it. However, we're mindful of vanity metrics that come from there too. So just because they use us doesn't necessarily mean that our mission is done or our job is done or what we're trying to do here. Because again, if we go back to the mission of ArcPrize, it's to pull forward OpenAGI progress.

> 他们采用我们的基准,这一点进展得非常好。不过,我们也警惕由此而来的"虚荣指标"。所以仅仅因为他们用了我们,并不一定意味着我们的使命完成了、我们的工作完成了,或者我们想做的事情达成了。因为再说一次,如果回到 ArcPrize 的使命,那就是推动开放的 AGI 进展。

[04:37] **SPEAKER_01:** So we want to inspire researchers, small teams, individual researchers. And having big labs give an endorsement more or less is really good for that mission, but it's also secondary to the overall mission.

> 所以我们想要激励研究者、小团队、个体研究者。让大实验室或多或少地给予背书,对这个使命是很有好处的,但相对于整体使命而言,它也是次要的。

[04:49] **SPEAKER_00:** So now that you've seen also lots of teams trying to ship AI products, what are most common false positives that you observe? Things that feel like progress, but aren't quite progress because it's easy to perhaps just hit a benchmark somewhere and call it done.

> 那么,既然你也见过很多团队尝试推出 AI 产品,你观察到的最常见的"假阳性"是什么?那些感觉像是进步、但其实算不上真正进步的东西——因为也许只要在某个基准上刷出分数,就宣称大功告成了。

[05:06] **SPEAKER_01:** Sure.

> 当然。

[05:07] **SPEAKER_00:** It doesn't quite work.

> 但实际上并不真的奏效。

[05:08] **SPEAKER_01:** Yeah. So when I answer that question, I put on my almost researcher hat, because there's two hats that are very prominent within AI right now. There's economically valuable, like, you know, we're going to go monetize this product hat. And then there's going to be the, call it, romantic pursuit of general intelligence hat.

> 是的。回答这个问题时,我几乎要戴上我的研究者帽子,因为如今在 AI 领域有两顶非常突出的帽子。一顶是"经济价值"的帽子——你知道的,就是"我们要把这个产品变现";另一顶则可以称为"对通用智能的浪漫追求"的帽子。

[05:25] **SPEAKER_01:** And I'm wearing the latter hat. So one thing that stands out to me is, of course, is everybody talks about it, but all the RL environments. And there's been famous AI researchers that have said, hey, as long as we can make an RL environment, we can score well on this benchmark. Whatever this domain or whatever it may be.

> 而我戴的是后一顶帽子。所以有一件事让我印象深刻——当然,人人都在谈论它——那就是所有那些强化学习环境。有一些著名的 AI 研究者说过:嘿,只要我们能做出一个 RL 环境,我们就能在这个基准上拿到好成绩,无论是哪个领域、无论它是什么。

[05:39] **SPEAKER_01:** To me, that's kind of like whack-a-mole. You know, you're not going to be able to make RL environments for every single thing you're going to end up wanting to do. And core to RKGI is novelty and novel problems that end up coming in the future, which is one of the reasons why we have a hidden test set, by the way. So I think while that's cool and why you're going to get short-term gains from it, I would rather see investment into systems that are actually generalizing and you don't need the environment for it.

> 对我来说,这有点像打地鼠。你知道,你不可能为你最终想做的每一件事都造出一个 RL 环境。而 ArcAGI 的核心就是新颖性,以及未来会出现的新问题——顺便说一句,这也是我们要设置一个隐藏测试集的原因之一。所以我认为,虽然这很酷、也能让你获得短期收益,但我更希望看到大家投入到那些真正能够泛化、且不需要专门环境的系统上。

[06:00] **SPEAKER_01:** Because if you see, or if you compare it to humans, humans don't need the environment to go and train on that.

> 因为如果你观察,或者把它和人类相比,人类并不需要那样的环境去专门训练。

[06:05] **SPEAKER_00:** Perhaps walk us through a bit of the human environment. Yeah. So you talked about the history of a RKGI version, so it was RKGI 1, 2, and 3 is coming up soon. Yes.

> 也许你可以带我们了解一下"人类环境"这方面。是的。你刚才谈到了 ArcAGI 各个版本的历史,所以有 ArcAGI 1、2,而 3 很快就要来了。是的。

[06:14] **SPEAKER_00:** Which is a whole new thing with game-like environments and interactive. So walk us through the history and then tell us what 3 is all about.

> 那是一个全新的东西,带有类游戏的环境和交互性。所以请带我们回顾一下历史,然后告诉我们第 3 版到底是关于什么的。

[06:21] **SPEAKER_01:** Yes, absolutely. So RKGI 1 came out in 2019, that was Francois Chollet proposed it. I think he made all 800 tasks himself within it, which is a huge feat in and of itself. And that came with this paper on the measure of intelligence.

> 好的,当然。ArcAGI 1 是 2019 年推出的,由 Francois Chollet 提出。我记得里面全部 800 个任务都是他自己做的,这本身就是一项巨大的壮举。它是随那篇关于智能度量的论文一起发布的。

[06:34] **SPEAKER_01:** Now in 2025, just this year. Earlier in March of this year, we came with RKGI 2. And so think of that as a deeper version or an upgraded version of RKGI 1. Now what's interesting is those two are both static benchmarks, or call it metastatic benchmarks.

> 到了 2025 年,也就是今年。今年早些时候的三月,我们推出了 ArcAGI 2。你可以把它看作是 ArcAGI 1 的一个更深入或升级的版本。有意思的是,这两个都是静态基准,或者叫准静态基准。

[06:50] **SPEAKER_01:** We're coming out with RKGI 3 next year. And the big difference with RKGI 3 is it's going to be interactive. So if you think about reality and the world that we all live in, we are constantly making an action, getting feedback, and kind of going back and forth with our environment. And it is in my belief that future AGIs are going to be interactive.

> 我们明年将推出 ArcAGI 3。ArcAGI 3 最大的不同在于它将是交互式的。想想现实,想想我们所有人生活的这个世界,我们不断地做出一个动作、得到反馈,然后与我们的环境来回互动。我坚信未来的 AGI 将是交互式的。

[07:06] **SPEAKER_01:** Future AGI will be declared with an interactive benchmark because that is really what reality is. And so V3 is going to be about 150 video game environments. Now we say video game because that's an easy way to communicate it, but really it's an environment where you give an action and then you get some response. Now the really cool part and one thing that jazzes me up about V3 the most is we're not going to give any instructions to the test taker on how to complete the environment.

> 未来的 AGI 将通过一个交互式基准来宣告,因为那才是现实的真正样子。因此 V3 将包含大约 150 个电子游戏环境。我们说"电子游戏"是因为这样便于沟通,但其实它是一种环境:你给出一个动作,然后得到某种响应。而真正酷、也是 V3 最让我兴奋的一点是,我们不会给测试者任何关于如何完成这个环境的说明。

[07:35] **SPEAKER_01:** So there's no English, there's no words. There's no symbols or anything like that. And in order to beat the benchmark, you need to go in, you need to take a few actions and see how your environment responds and try to figure out what the ultimate goal is in the first place.

> 所以没有英文,没有文字,没有符号之类的任何东西。为了通过这个基准,你需要进去,采取一些动作,看看环境如何响应,并首先设法弄清楚最终目标究竟是什么。

[07:47] **SPEAKER_00:** I tried a bunch of those games. They were actually fun.

> 我玩了其中一堆游戏。它们其实挺好玩的。

[07:49] **SPEAKER_01:** Yeah, they're cool. And much like ARK 1 and ARK 2, we're testing humans on every single V3 game. So we will recruit members of the general public. So accountants, Uber drivers, you know, that type of thing.

> 是的,它们很酷。而且和 Arc 1、Arc 2 很像,我们会让人类去测试每一个 V3 游戏。我们会招募普通公众,比如会计、Uber 司机,你知道的,就是这类人。

[08:01] **SPEAKER_01:** We'll put 10 people in front of each game and if each game does not pass a minimum solvability threshold by regular humans. Then we're going to exclude it. Now again, I just have to emphasize, but that's in contrast to other benchmarks where you try to go harder and harder and harder questions. But the fact that ARK 3 will be out there and regular people can do it, but AI cannot do it, tells you, well, there's something missing still.

> 我们会让 10 个人来玩每一个游戏,如果某个游戏没有达到普通人可解的最低阈值,我们就会把它排除掉。再次强调一下,这与其他那些一味追求越来越难题目的基准形成鲜明对比。但 Arc 3 摆在那里,普通人能做出来而 AI 做不出来,这个事实告诉你:嗯,还有某种东西是缺失的。

[08:24] **SPEAKER_01:** There's something clearly missing that we need new ideas for research on.

> 显然还缺少某种东西,我们需要新的研究思路来解决它。

[08:28] **SPEAKER_00:** So there's this big theme in terms of measuring intelligence with human capabilities. So there's this growing idea. Yeah. That accuracy is not the only metric that matters to models, but also the time and amount of data that it takes to acquire new skills, which is what this whole spirit of AGI is.

> 那么,在用人类能力来衡量智能这个方面有一个大主题。有一个越来越盛行的观点——是的——那就是准确率并不是衡量模型的唯一指标,还有获取新技能所需的时间和数据量,而这正是整个 AGI 精神的所在。

[08:49] **SPEAKER_00:** So I guess the question is how close are we to evaluating models in human time?

> 所以我想问题是:我们距离用"人类时间"来评估模型还有多近?

[08:55] **SPEAKER_01:** Yes. So with regards to human time, we actually see time as a little bit arbitrary because if you throw more compute at something, you're going to reduce the time no matter what. So it's almost just a decision on how much compute you need. Yeah.

> 是的。关于"人类时间",我们其实觉得时间有点武断,因为如果你对某件事投入更多算力,无论如何都会缩短时间。所以这几乎只是一个"你需要多少算力"的决定。是的。

[09:06] **SPEAKER_01:** You can do whatever you want, which is how much time it's going to take, which tells you that wall clock may not be the important part for what we have intelligence here. But there's two other factors that go into the equation of intelligence. Number one is going to be the amount of training data that you need, which is exactly what you said. And then number two is actually the amount of energy that you need in order to execute upon that intelligence.

> 你可以随心所欲地决定它会花多少时间,这说明"墙上时钟"(实际耗时)可能并不是我们这里所谈智能的重要部分。但还有另外两个因素进入了智能的方程式。第一个是你所需的训练数据量,这正是你刚才说的。第二个其实是你为了执行这种智能所需的能量。

[09:25] **SPEAKER_01:** And the reason why those are so fascinating is because we have benchmarks for humans on both of those. So we know how many data points a human needs in order to execute a task, and we know how much energy the human needs. We know how much energy the human brain consumes to execute a task. So with ArcAGI 3, the way that we're actually going to be measuring efficiency, not just by accuracy, I told you they're video games, and they're turn-based video games.

> 而这两点之所以如此引人入胜,是因为我们对人类在这两方面都有基准数据。所以我们知道一个人执行一项任务需要多少数据点,也知道这个人需要多少能量。我们知道人脑执行一项任务消耗多少能量。因此在 ArcAGI 3 中,我们衡量效率的方式不只是看准确率——我告诉过你它们是电子游戏,而且是回合制的电子游戏。

[09:47] **SPEAKER_01:** And so you might click up, left, right, down, or something like that. And we're going to count the number of actions that it takes a human to beat the game, and we're going to compare that to the number of actions that it takes an AI to beat the game. So back in the old Atari days, in 2016, when they were making a run at video games then, they would use brute force solutions, and they would need millions and billions of frames of video game, and they would need millions of actions to basically spam and brute force the space. We're not going to let you do that on Arc 3.

> 所以你可能会点上、左、右、下之类的方向。我们会统计一个人类通关一个游戏所需的动作数,然后把它和 AI 通关同一个游戏所需的动作数进行比较。回到过去的 Atari 时代,2016 年他们当时挑战电子游戏,会使用暴力破解的方法,需要数百万乃至数十亿帧的游戏画面,需要上百万次动作来基本靠刷、靠暴力去穷举这个空间。在 Arc 3 上我们不会允许你那样做。

[10:16] **SPEAKER_01:** And so we're basically going to normalize AI performance to the average human performance that we see.

> 所以我们基本上会把 AI 的表现,归一化到我们观察到的人类平均表现上。

[10:22] **SPEAKER_00:** That's very cool. Yes. My last question. Yes.

> 那非常酷。是的。我的最后一个问题。请讲。

[10:26] **SPEAKER_00:** Let's wave a magic wand. And then there's a super amazing team that suddenly tomorrow launches a model that scores 100%. Yeah. It's called Arc AGI Benchmarks.

> 让我们挥动一根魔法棒。假设有一个超级了不起的团队,明天突然发布了一个能拿 100 分的模型。是的。就在那个叫 Arc AGI 的基准上。

[10:40] **SPEAKER_00:** What should the world update about the priors of what AGI is? Yeah. How would the world change?

> 世界应该如何更新关于"AGI 是什么"的先验认知?是的。世界会如何改变?

[10:45] **SPEAKER_01:** Well, it's funny you ask that. The what AGI is question is such a deep topic that we can go much deeper on. So from the beginning, Francois has always said that the thing that solves Arc AGI is necessary for AGI. It's not sufficient.

> 嗯,你问这个很有意思。"AGI 是什么"这个问题是一个非常深刻的话题,我们可以深入探讨得多。从一开始,Francois 就一直说,能够解决 Arc AGI 的东西对于 AGI 是必要的,但不是充分的。

[10:59] **SPEAKER_01:** So what that means is the thing that solves Arc AGI 1 and 2 will not be AGI, but it will be an authoritative source of generalization. Now our claim for V3 is that no, the thing that beats it won't be AGI. However, it will be the most authoritative evidence that we have to date about a system that can generalize. If a team were to come out and beat it tomorrow, we would of course want to analyze that system, figure out where still are the failure points that come from that.

> 这意味着,能够解决 Arc AGI 1 和 2 的东西并不会是 AGI,但它会是泛化能力的一个权威来源。而对于 V3,我们的主张是:不,击败它的东西也不会是 AGI,然而它将是我们迄今为止关于"一个能够泛化的系统"所拥有的最权威的证据。如果有个团队明天站出来击败了它,我们当然会想去分析那个系统,弄清楚它仍然存在哪些失败点。

[11:27] **SPEAKER_01:** And like any good benchmark creator, we want to continue to guide the world towards what we believe to be proper AGI. But ultimately, our prize, we want to put ourselves in a position. When we can fully understand and be ready to declare when we do actually have AGI. So if that team were to do it tomorrow, we would want to have a conversation with them.

> 而且像任何优秀的基准创建者一样,我们希望继续引导世界走向我们所认为的真正的 AGI。但归根结底,我们的这个奖项,是想让我们自己处在一个位置上——当我们能够充分理解、并准备好在我们真正拥有 AGI 时予以宣告的位置。所以如果那个团队明天真做到了,我们会想和他们好好谈一谈。

[11:43] **SPEAKER_01:** I'll put it that way.

> 我就这么说吧。

[11:44] **SPEAKER_00:** That's a good way to wrap. Thank you so much for coming and chatting with us, Greg.

> 这是个很好的收尾方式。非常感谢你前来与我们交流,Greg。

[11:46] **SPEAKER_01:** Thank you, Diana.

> 谢谢你,Diana。
