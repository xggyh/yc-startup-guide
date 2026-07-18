# 全文转录 · 通往 AGI 还缺什么:Demis Hassabis 谈 Agent、深科技创业与下一场科学突破

> ▶ [YouTube](https://www.youtube.com/watch?v=JNyuX1zoOgU) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/JNyuX1zoOgU.md) &nbsp;·&nbsp; Demis Hassabis: Agents, AGI & The Next Big Scientific Breakthrough

> 中英对照 · 每段英文原文下附中文翻译

[00:00] **SPEAKER_02:** Continual learning, long-term reasoning, some aspects of memory, these are still unsolved. I think all of these are going to be required for AGI. Depending on what your AGI timeline is, you know, mine's like 2030 or something like this, then if you start off on a deep tech journey today, you have to just consider AGI appearing in the middle of that journey. It's not bad necessarily, but you have to take that into account. You have to have an active system

> 持续学习、长期推理、记忆的某些方面,这些至今仍未解决。我认为这些都会是实现通用人工智能(AGI)所必需的。取决于你对 AGI 时间线的判断——我个人大概是 2030 年左右——如果你今天踏上一段深科技的征程,就必须考虑到 AGI 会在这段旅程的中途出现。这未必是坏事,但你必须把它纳入考量。你需要一个能主动运作的系统。

[00:27] **SPEAKER_02:** that can actively solve problems for you to get to AGI. So agents are that path and I think we're

> 一个能主动为你解决问题的系统,才能通向 AGI。所以智能体(agents)就是那条路径,而我认为我们才刚刚起步。

[00:33] **SPEAKER_01:** just getting going. Demis Hassabis has had one of the most unusual careers in tech. He was a chess prodigy as a kid, then designed his first hit video game, Theme Park, at 17. He then went back to school, got a PhD in cognitive neuroscience, published foundational work on how memory and imagination work in the brain.

> 才刚刚起步。Demis Hassabis 拥有科技界最不寻常的职业生涯之一。他小时候是国际象棋神童,17 岁就设计出了自己的第一款热门电子游戏《主题公园》(Theme Park)。之后他重返校园,取得了认知神经科学博士学位,发表了关于大脑中记忆与想象如何运作的奠基性研究。

[01:02] **SPEAKER_01:** And then in 2010, co-founded DeepMind with one mission, solve intelligence. And I think they've done it. Since then, his lab has gone on to do things most people thought were decades away. Alpha Go beat a world champion at Go. Alpha Fold cracked protein structure prediction, a 50-year grand

> 然后在 2010 年,他联合创办了 DeepMind,只有一个使命:解决智能问题。而我认为他们做到了。从那以后,他的实验室做出了许多人们以为还要几十年才能实现的成就。AlphaGo 击败了围棋世界冠军;AlphaFold 攻克了蛋白质结构预测——一个长达 50 年的生物学重大难题。

[01:24] **SPEAKER_01:** challenge in biology, and they gave it away for free to every scientist on Earth. That work won him the Nobel Prize in Chemistry. Today, Demis leads Google DeepMind, where he's building Gemini and pushing toward the same goal he set when he was a teenager, artificial general intelligence. Please welcome Demis Hassabis.

> 这是一个 50 年的生物学重大难题,而他们把成果免费提供给了全世界的每一位科学家。这项工作为他赢得了诺贝尔化学奖。如今,Demis 领导着 Google DeepMind,在那里打造 Gemini,并朝着他少年时代就设定的同一个目标——通用人工智能——不断推进。让我们欢迎 Demis Hassabis。

[01:46] **SPEAKER_01:** So you've been thinking about AGI longer than almost anyone. When you look at the current paradigm, large-scale pre-training, RLHF, chain of thought, how much of the final architecture for AGI do you think we already have and what's fundamentally missing right now?

> 你思考 AGI 的时间几乎比任何人都久。当你审视当前的范式——大规模预训练、RLHF(人类反馈强化学习)、思维链——你认为我们已经掌握了通向 AGI 最终架构的多少部分?而当下从根本上还缺什么?

[02:08] **SPEAKER_02:** Well, first of all, thanks, Gary, for that great introduction. And it's great to be here. Thanks for welcoming me here. It's an amazing space, actually. I have to come back here often. Very

> 首先,谢谢你,Gary,这么精彩的介绍。很高兴来到这里,谢谢你们的接待。这个空间真的很棒,我得常来。很有启发。

[02:16] **SPEAKER_02:** inspiring that you will get to work in this space. So the question is, I think the components that you just mentioned, I'm pretty sure will be part of the final architecture for AGI. So I think they've come such a long way now, and we've proven out so many things about what they can do. I can't see a world in which we will sort of realize in a couple of years this was a dead end. That doesn't make sense to me. But there still might

> 能在这样的空间里工作真是令人振奋。回到问题上,我很确定你刚才提到的那些组成部分会成为 AGI 最终架构的一部分。它们如今已经走了这么远,我们也已经验证了它们能做到的许多事情。我无法想象几年后我们会突然发现这是一条死路,那在我看来说不通。但也许仍然……

[02:42] **SPEAKER_02:** be one or two things missing on top of what we already know works. So continual learning, long-term reasoning, some aspects of memory, these are still unsolved, and how to get the systems to be more consistent across the board. I think all of these are going to be required for AGI. Now, it might be that the existing techniques can just scale up.

> ……在我们已知有效的基础之上,还缺一两样东西。持续学习、长期推理、记忆的某些方面,这些仍未解决,还有如何让系统在各方面都更加一致。我认为这些都是实现 AGI 所必需的。当然,也有可能现有的技术只要继续扩展规模就够了。

[03:08] **SPEAKER_02:** I don't think it's more than one or two, if there are out there. And I think my betting is about 50-50, if that's the case. So of course, at DeepMind, at Google DeepMind, we work on both those things.

> 我认为即便还缺东西,也不超过一两样。而我的判断大概是五五开——是否需要新东西。所以当然,在 DeepMind、在 Google DeepMind,我们两条路都在做。

[03:29] **SPEAKER_01:** I guess that's what we mean. Working with a bunch of agentic systems, the wildest thing to me is to what degree it's the same weights over and over. So this idea of continual learning, is so interesting, because right now, we're sort of cobbling it together with duct tape, these dream cycles at night and things like that. It's pretty cool, the dream cycles. And we used

> 我想这正是我们的意思。在与一堆智能体系统打交道时,最让我惊讶的是它们在多大程度上反复用的是同一套权重。所以持续学习这个概念非常有意思,因为现在我们其实是在用胶带东拼西凑——比如夜里的这些"做梦周期"之类的东西。那些做梦周期挺酷的。我们过去……

[03:49] **SPEAKER_02:** to think about this with consolidation with episodic memory. Actually, that's what I studied for my PhD, is how the hippocampus works and integrates new knowledge gracefully into the existing knowledge base. So the brain does that amazingly well. It does it during sleep, especially things like REM sleep.

> ……曾从情景记忆的巩固角度来思考这个问题。事实上,这正是我博士研究的课题:海马体如何运作,如何优雅地把新知识整合进已有的知识体系。大脑在这方面做得非常出色,它是在睡眠期间完成的,尤其是像 REM(快速眼动)睡眠这样的阶段。

[04:08] **SPEAKER_02:** Replaying back episodes that are important so that you can learn from it. In fact, our very first Atari program, DQN, one of the ways it was able to master Atari games was by doing experience replay. So we sort of borrowed that from neuroscience and replayed successful trajectories many times. That's way back in 2013 now, in the dark ages of AI. It was a really

> 大脑会回放那些重要的经历,好让你从中学习。事实上,我们最早的 Atari 程序 DQN,它能掌握 Atari 游戏的方式之一就是"经验回放"。我们算是从神经科学借来了这个思路,把成功的轨迹反复回放许多次。那还是 2013 年的事了,那时还是 AI 的黑暗时代。那真的是……

[04:32] **SPEAKER_02:** important thing. And I agree with you, we're kind of using duct tape right now. So shove it all in the context window. Yeah.

> ……一件非常重要的事。我同意你的说法,我们现在其实是在用胶带凑合——把所有东西一股脑塞进上下文窗口。是啊。

[04:38] **SPEAKER_02:** This seems a bit unsatisfying. And actually, even though we're working on machines, not biological brains, and so potentially you could have millions or tens of millions size context window or memory, and it can be perfect, there's still a cost to looking it up and finding the right thing that's actually relevant for the specific decision you've got to make right now. And that's non-trivial, that cost, even if you can potentially store it all. I think there's actually a lot of room for innovation in areas like memory.

> 这似乎有点不尽如人意。而且实际上,尽管我们做的是机器而非生物大脑,所以理论上你可以拥有数百万甚至数千万规模的上下文窗口或记忆,而且它可以是完美无损的,但要去查找、并找到对你此刻要做的具体决策真正相关的那一条,仍然是有成本的。即便你有可能把一切都存下来,这个成本也不容忽视。我认为在记忆这类领域,其实还有很大的创新空间。

[05:11] **SPEAKER_01:** Yeah. I mean, the wild thing is, it feels like a million token context windows is actually bigger than, I mean, it's plenty big, honestly, you can do so.

> 是啊。让我惊讶的是,感觉一百万 token 的上下文窗口其实已经比……说实话已经够大了,你能做很多事。

[05:19] **SPEAKER_02:** Well, it's plenty big for most things that it should be used for. I mean, if you think about the context windows sort of equivalent to working memory, humans have, we have a few digits. It's like a dozen digits, maybe, average of seven. We've got a million or 10 million context windows, but the problem is, is that we're trying to store everything in that. Things that are not important,

> 对于它应该被用于的大多数场景,它确实已经够大了。你可以把上下文窗口类比为工作记忆——人类的工作记忆只有几位数,大概十来位吧,平均是七位左右。我们现在有一百万甚至一千万的上下文窗口,但问题在于,我们试图把所有东西都存进去,包括那些不重要的东西……

[05:43] **SPEAKER_02:** things that are wrong, it's pretty brute force currently, and that doesn't seem right. And then the problem is if you're now trying to try and process live video, and you're just going to naively record all the tokens, then actually a million tokens isn't that much. It's only like 20 minutes. So actually you need more if you want something that's going to understand what's going on in your life over maybe a month or two.

> ……甚至错误的东西,目前这种做法相当暴力,感觉不太对劲。而且还有个问题:如果你要处理实时视频,又只是简单粗暴地把所有 token 都记录下来,那么一百万 token 其实并不算多,只相当于大约 20 分钟。所以如果你想要一个能理解你生活中一两个月里发生了什么的系统,你实际上需要更多。

[06:07] **SPEAKER_01:** Deep mind. Has historically leaned into reinforcement learning and search, AlphaGo, AlphaZero, and MuZero. How much of that philosophy is actually embedded in how you're building Gemini today? Is RL still underrated?

> DeepMind 历来都很倚重强化学习和搜索——AlphaGo、AlphaZero、MuZero。这种理念在你们今天构建 Gemini 的方式中占了多大比重?强化学习(RL)是否仍被低估了?

[06:23] **SPEAKER_02:** Yeah, I think potentially it is. It sort of goes in ebbs and waves. We've worked on agents since the beginning of DeepMind. In fact, that was what we said we were working on. So all of the Atari

> 是的,我认为它有可能仍被低估。这种东西是有起有落、一波一波的。从 DeepMind 成立之初我们就在做智能体,事实上那正是我们对外宣称在做的事。所以所有那些 Atari……

[06:34] **SPEAKER_02:** work and AlphaGo, most specifically, they're agent systems. So we've been working on that. They're agent systems. And what we meant by that is systems that are able to accomplish goals on their own and make active decisions and make plans. And so of course we were doing it in the

> ……的工作,尤其是 AlphaGo,它们都是智能体系统。所以我们一直在做这件事,它们是智能体系统。我们所说的智能体,指的是那些能够自主完成目标、主动做决策、制定计划的系统。当然,我们当时是在游戏这个领域里做的……

[06:49] **SPEAKER_02:** domain of games to make it tractable and then doing increasingly complex games, things like StarCraft, after AlphaGo, AlphaStar. So we basically did all the games that are out there. And then of course the question is, can you generalize those models to be world models or models of language not just models of simple games or even complex games and that's what the last few years has been about but really you can think of a lot of the things we're doing today all the leading models with thinking modes and chain of thought reasoning as aspects of what was sort of pioneered with AlphaGo coming back now and I actually think there's a lot of work we did back then that is relevant today and we're sort of re-looking at some of those old ideas at scale today in a more general way including things like Monte Carlo research and other other ways of doing augmenting the RL on top of the reinforcement learning we're ready to do today and I think a lot of those ideas both from AlphaGo and AlphaZero are really really relevant to where we are with today's Foundation models and I think a lot of that is what we're going to see of the advances

> ……以便让问题变得可解,然后在 AlphaGo 之后挑战越来越复杂的游戏,比如《星际争霸》,做出了 AlphaStar。所以我们基本上把市面上的游戏都做了个遍。接下来的问题当然是:你能不能把这些模型泛化成世界模型或语言模型,而不只是简单游戏乃至复杂游戏的模型?这就是过去几年我们所做的事情。但其实,你可以把我们今天所做的很多事情——所有带有思考模式和思维链推理的领先模型——看作是当年 AlphaGo 所开创的那些理念如今的回归。我确实认为我们当年做的很多工作在今天仍然相关,如今我们正以一种更通用、更大规模的方式重新审视其中一些旧想法,包括蒙特卡洛搜索,以及在如今的强化学习之上进一步增强 RL 的其他做法。我认为来自 AlphaGo 和 AlphaZero 的很多想法,对于我们今天基础模型所处的阶段都非常非常相关,而这其中很多正是我们即将看到的进展。

[07:58] **SPEAKER_01:** the next few years one question I would have like obviously today you need bigger and bigger models to be smarter and smarter but then Yeah. also seeing distillation working and then smaller models can be like quite a bit faster I think you know you guys have incredible flash models that are yeah like nine like you're finding that they're 95 as good as uh the Frontier and at like one-tenth the price is that right I think that's one of our

> 未来几年的进展。我有一个问题:显然,今天你需要越来越大的模型才能越来越聪明,但同时——是的——我们也看到蒸馏(distillation)在起作用,更小的模型可以快得多。你们有非常出色的 Flash 模型,你们发现它们能达到前沿模型 95% 的水平,而价格只有大约十分之一,是这样吗?

[08:23] **SPEAKER_02:** core strengths is I mean you have to build the biggest models to to to have uh the Frontier capabilities but I think one of our biggest strengths has been uh distilling and packing that power into smaller and smaller models very quickly obviously we we you know we invented the kind of distillation process and and people like Jeff and Oreo and and others and we're still world experts in that and we also have a huge need to uh do it because we've got to serve the biggest probably AI surfaces um there are obviously there's search with AI overviews and AI mode then there's Gemini app and now increasingly every single product at Google has you know Maps and YouTube and so on has some of the best products out there and so that's some aspect of Gemini or Gemini related technology in it and so that's billions of users a dozen more than a dozen billion user products and they have to be served extremely fast extremely efficiently and cheaply and with low latency so that that gives us a really important incentive to to make these flash and even smaller models flashlight models extremely efficient and hopefully that ends up then being really useful for many of the workloads that all of you use for I'm curious

> 我觉得这是我们的核心优势之一。我是说,你必须打造最大的模型才能拥有前沿能力,但我认为我们最大的优势之一,就是能非常快地把那种能力蒸馏、压缩进越来越小的模型里。众所周知,蒸馏这套流程差不多是我们发明的,像 Jeff、Oriol 等人,我们至今仍是这方面的世界级专家。而我们也有巨大的需求去做这件事,因为我们要服务的可能是最大的一批 AI 触点:显然有带 AI 概览和 AI 模式的搜索,有 Gemini 应用,如今 Google 的每一款产品——地图、YouTube 等等,都是市面上最好的产品之一——里面越来越多地含有某种形式的 Gemini 或 Gemini 相关技术。所以这是数十亿用户、十几个乃至更多个拥有十亿级用户的产品,它们必须以极快的速度、极高的效率、极低的成本和极低的延迟来提供服务。这给了我们一个非常重要的动力,去把这些 Flash 乃至更小的 Flash-Lite 模型做到极致高效,而希望这最终对你们大家使用的许多工作负载都非常有用。我很好奇……

[09:36] **SPEAKER_01:** how much smarter these smaller models can actually be like are there limits to the distillation process like could a 50B or 400B model be as smart as like a mythos for today yeah I don't I don't

> ……这些更小的模型到底能变得多聪明。蒸馏这个过程有没有极限?比如一个 50B 或 400B 的模型,能不能达到今天最强大模型那样的聪明程度?

[09:48] **SPEAKER_02:** see any I don't think we've got to any kind of or at least none of us know yet if we've got to any kind of information or limit I mean maybe at some point that will be the case where there's just an information density that can't we can't get beyond but I think for now there's the assumption we make that after one of our uh leading you know Pro models or Frontier models goes out half a year later a year later you'll have them in the the really tiny almost Edge models and you also see some of that goodness in our Gemma models which hopefully you're all enjoying our Gemma 4 models which I think are really amazing power for their sizes so again that uses a lot of this uh these distillation techniques and and the idea of how to make things really efficient in these very small models so I don't really see any limit yet in terms of like some kind of theoretical limit I think we're still pretty far off of that that's

> 我看不到任何极限。我认为我们还没有触及任何——至少我们当中还没有人知道我们是否触及了某种信息上的极限。也许到某个时刻确实会出现这种情况,存在一个我们无法逾越的信息密度上限。但目前我们做的假设是:在我们某个领先的 Pro 模型或前沿模型发布之后,半年、一年后,你就能在那些极小的、几乎属于边缘端的模型里得到它们(的能力)。你在我们的 Gemma 模型里也能看到这种"好东西"——希望大家都在享用我们的 Gemma 4 模型,我觉得就其体量而言性能非常惊人。这同样大量使用了这些蒸馏技术,以及如何让这些极小模型变得非常高效的思路。所以在某种理论极限的意义上,我目前还看不到任何极限,我认为我们离那还相当远。这……

[10:39] **SPEAKER_01:** amazing I mean that is really good yes uh you know one of the weirder things that we're seeing right now is like engineers can do like 500 to a thousand times the amount of work that they were doing like six months ago I guess I mean the people in this room there are people who are doing about like a thousand X the work that like I Steve Yagi talks about this it's like a thousand X the work that a

> ……太棒了,这真的很了不起,是的。你知道,我们现在看到的比较奇特的现象之一是,工程师能完成的工作量大约是六个月前的 500 到 1000 倍。我是说,这个房间里就有人在做着大约一千倍的工作量,Steve Yegge 就谈到过这个,就像是一千倍于……

[11:01] **SPEAKER_02:** Google engineer from the 2000s was doing I think it's very exciting I mean I think the small models have many uses one is obviously cost but the speed can allow you know if you think about coding even or other things you can iterate a lot faster also especially if there's if you're collaborating with the system I think there's a there's a a a lot of need for having fast systems um that maybe are not quite front here like you said like 95 90 but that's plenty good enough and actually you gain back more than the 10 on the the iteration speed so and then the other big thing I think is running these things on the edge again for efficiency reasons but also for privacy and security reasons too if you think about different devices that you might run these systems on that per that you know process very personal information you can also think about robotics as well you know robots in your house I think you're going to want very efficient uh very powerful local models which may be orchestrated you know with some bigger models Frontier models that in the in the cloud but you only get to that in certain circumstances and perhaps you you know you process all of the audio visual feed let's say locally and that stays local I could imagine uh that would be a very good sort

> ……一位 2000 年代的 Google 工程师所做的工作量。我觉得这非常令人兴奋。我认为小模型有很多用途:一个显然是成本,但速度也很关键——想想写代码或其他事情,你可以迭代得快得多,尤其是当你在和系统协作的时候。我认为对快速系统有很大的需求,这些系统也许不完全是前沿水平,像你说的 95%、90%,但那已经足够好了,而且你在迭代速度上赚回的其实不止那 10%。另一件大事,我认为是在边缘端运行这些东西,同样是出于效率考虑,但也出于隐私和安全的考虑。想想你可能在各种设备上运行这些系统,而这些设备处理的是非常私人的信息;也可以想想机器人,比如你家里的机器人——我认为你会想要非常高效、非常强大的本地模型,它们也许会与云端某些更大的前沿模型协同编排,但你只在特定情况下才动用云端。也许你把所有的音视频信号都在本地处理,并且让它留在本地。我可以想象,那会是一种非常好的……

[12:17] **SPEAKER_00:** of end state YC start a school is back we're hand selecting the most promising Builders in the world and flying them out to San Francisco for July 25th and 26th to discuss the cutting Edge of Tech apply now for a spot okay back to the video going back to context and memory

> ……终态。YC 创业学校又回来了。我们正在从全世界亲手挑选最有潜力的创造者,把他们请到旧金山,于 7 月 25 日和 26 日一起探讨科技的最前沿。现在就申请一个名额吧。好,回到视频。回到上下文和记忆这个话题。

[12:36] **SPEAKER_01:** it's currently stateless but you know continue like what would the developer experience even be like for someone who's using a continual learning model like you know any idea like how you'd steer

> 它目前是无状态的,但——持续学习……对一个使用持续学习模型的人来说,开发者体验会是什么样的?你有没有什么想法,比如你会如何去引导它?

[12:46] **SPEAKER_02:** it I think it's really interesting I think that's one of the not having continual learning currently is one of the things holding back agents from doing full uh tasks you know I think they're really useful for aspects of tasks right now and you can patch them together and do some really cool things but they don't adapt well with the context that you're in and I think that's the missing piece from them being really kind of fire and forget and they'll figure it out themselves you know I think they need to be able to learn um about the specific context um that you're gonna put them in so um I think we have to crack that to

> 我觉得这个问题非常有意思。我认为目前缺乏持续学习,正是阻碍智能体去完成完整任务的因素之一。它们现在对于任务的某些环节确实很有用,你可以把它们拼接起来做出一些很酷的事情,但它们不能很好地适应你所处的具体情境。我认为这正是它们要真正做到"一发即忘、自己搞定"所欠缺的那块拼图。它们需要能够学习你即将把它们放入的那个具体情境。所以我认为我们必须攻克这一点,才能……

[13:24] **SPEAKER_01:** get full General Intelligence where are we on reasoning so models can do really impressive chain of thought now but they still fail on things a smart undergrad wouldn't what specifically needs

> ……实现完整的通用智能。推理方面我们进展如何?现在模型能做出非常令人印象深刻的思维链,但它们仍会在一些聪明的本科生都不会犯错的地方出错。具体缺的是什么?

[13:36] **SPEAKER_02:** respect and reasoning there's a lot of uh Innovation left in in think the thinking paradigms I would say again I think we're fairly we're doing fairly simplistic things fairly brute force one could imagine uh I think there's a lot of scope for example in monitoring the chain of thought maybe interjecting midway through a thought process I often get the impression with our systems and and our competitor systems that they're almost overthinking they're almost getting into sort of loops of things like one thing I sometimes like to do is play chess against Gemini and you know it's all the leading Foundation models are pretty poor at games which is quite interesting it's very uh uh cool to kind of look at the thinking Tracers because obviously these are can be a well understood you know I can tell quite quickly if it's going off on a tangent and it's very sort of provable what the what the the thinking is doing whether it's useful or not and so what we see is that you know sometimes it will it will it will consider a move it will realize it's a blunder but it can't find anything better so it kind of goes back to that move and does it anyway so it you know you just shouldn't be seeing that uh happening in a in a very precise reasoning system so there's just sort of huge gaps I think still but it may only be one or two tweaks that are required to fix those kind of gaps just to be clear but I think that's pretty pretty obvious there are there and that's why you get this kind of jagged intelligence you know on the one hand it can solve gold medal problems in IMO which is super hard but on the other hand as we've all seen it can still make basic elementary math errors if you pose the question in a certain way right so or elementary reasoning errors so there's just something to me about the almost an introspection about its own thought process that I

> 推理方面还有很多创新空间。我要再说一遍,我认为在思考范式上,我们做的东西相当简单、相当暴力。可以想象,比如在监控思维链、也许在思考过程进行到一半时加以干预方面,还有很大的余地。我常常有一种印象,不论是我们的系统还是竞争对手的系统,它们几乎是在"想太多",几乎会陷入某种循环。我有时喜欢做的一件事,就是和 Gemini 下国际象棋——所有领先的基础模型在游戏上都相当糟糕,这很有意思。看它的思考轨迹很酷,因为这些东西是可以被清楚理解的:我能很快判断它是不是跑题了,而且思考在做什么、有没有用,是相当可证的。于是我们看到:有时它会考虑某一步棋,意识到那是个大昏招,但又找不到更好的,于是就退回去照样走了那一步。你知道,在一个非常精确的推理系统里,本不该出现这种情况。所以我认为其中确实还存在巨大的缺口,但要澄清的是,修补这类缺口也许只需要一两处调整。不过我认为这些缺口是相当明显存在的,这也正是为什么你会得到这种"参差不齐的智能":一方面它能解出国际数学奥林匹克(IMO)金牌级别的超难题目,另一方面,正如我们都见过的,如果你用某种方式提问,它仍然会犯基本的初等数学错误,或者初等推理错误。所以在我看来,它对自身思考过程的那种近乎内省的能力,是我……

[15:24] **SPEAKER_01:** feel like there's there's something maybe missing there agents are really big some would say they're hyped I personally think they're just getting started it's totally insane what does Deep Minds internal research tell you about where agent capabilities actually are right now versus you know sort of the hype out there I think we are I

> ……觉得那里也许缺了点什么。智能体现在非常火,有人会说被过度炒作了,而我个人认为它们才刚刚起步,简直不可思议。DeepMind 内部的研究告诉你,智能体的能力当下究竟处于什么水平,相较于外界的种种炒作而言?

[15:41] **SPEAKER_02:** agree with you I think we're just at the beginning you have to have an active system uh that can actively solve problems for you to get to AGI that was always clear to us so agents are that path and I think we're just getting going I think all of us are getting used to how do we best work and you're leading the way in a lot of this in your own personal experiments I'm sure many of you are doing that I think how do you incorporate it into your uh workflow in a way that isn't just um sort of a nice to have but actually starting to do fundamental things my impression is at the moment we're all exp you know we're experimenting on lots of things but we're only in the maybe the last couple of months starting to find the really valuable places and the technology is probably only getting good enough for that to be the case right where that it's not a kind of toy um nice demonstration but actually really adding value to your to your um to your time and efficiency I'd often wonder I see a lot of people working on uh like setting off you know dozens of agents for like 40 hours but I'm not sure I've seen the output that yet of that quite justify that level of input going in but I think it will come so I still think we're in the experimentation phase we haven't seen a AAA game that tops the App Store charts that was sort of vibe coded yet right I've seen and I've programmed and I'm sure many we've all done little nice demonstrations and it's like amazing I can do a prototype a theme park in half an hour months back when I was 17. it's kind of mind-blowing and I and I wish I I got this feeling if I spent the whole summer working on it you could make something really incredible but it still needs craft and you know human sort of soul into it and taste I think that's that's something that can that's you have to make sure you still bring that to to whatever it is you're building and I think it still shows like it's not quite there yet because why haven't we seen a kid making a hit right that should be possible given the effort that's gone in so something's still somehow missing maybe it's to do with the process or maybe it's to do with the tools I'm not quite sure you all probably know better than me because I'm sure you're all experimenting on that but I haven't seen the result yet which I would expect once this is really delivering that full value which I think will come in the next six to 12 months some of it is like how much of it will be

> 我同意你的看法,我认为我们才刚刚开始。你必须拥有一个能主动为你解决问题的系统,才能通向 AGI,这一点对我们一直是清楚的。所以智能体就是那条路,我认为我们才刚起步。我觉得我们所有人都在慢慢摸索如何最好地工作,而你在自己的个人实验里在很多方面走在前面,我相信在座许多人也在做这件事。问题是:你如何把它融入你的工作流程,不只是当作一个"锦上添花"的东西,而是真正开始做根本性的事情。我的印象是,目前我们都在对很多东西做实验,但大概只是在最近这一两个月里,才开始找到那些真正有价值的应用点,而技术也可能才刚刚好到足以让这成为可能——即它不再是那种玩具式的、漂亮的演示,而是真正为你的时间和效率增添价值。我常在想:我看到很多人在做那种一口气放出几十个智能体、跑上 40 小时的事情,但我还不太确定我见过那种投入能被其产出所充分证明其价值。不过我认为那一天会到来。所以我仍然认为我们处在实验阶段。我们还没见过哪款登上 App Store 排行榜榜首的 3A 游戏是靠"氛围编程"(vibe coding)做出来的,对吧?我见过、也亲手编过,我相信我们大家都做过一些漂亮的小演示,那种感觉很惊艳——我能在半小时里做出一个像我 17 岁那时的《主题公园》的原型,这有点让人震撼。我常有这种感觉:如果我花上整整一个夏天来做,你能做出真正了不起的东西。但它仍然需要匠心,需要注入某种人的灵魂和品味。我认为这是你必须确保为你所构建的任何东西带入的东西,而这一点也表明它还没完全到位——因为为什么我们还没看到某个孩子做出一个爆款呢?按理说以已经投入的努力来看,这应该是有可能的。所以某种东西仍然莫名地缺失着,也许和流程有关,也许和工具有关,我不太确定。你们大概比我更清楚,因为我相信你们都在实验这些。但我还没看到那个我预期一旦它真正发挥全部价值时应有的成果,而我认为那会在未来六到十二个月内出现。其中一部分问题是:有多少会是……

[17:59] **SPEAKER_01:** autonomous versus I mean I don't think we'd see autonomous first we would actually probably see people in this room operating as a team yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah

> ……自主完成,而不是……我是说,我认为我们不会先看到完全自主的情形,我们实际上更可能先看到这个房间里的人以团队的方式运作。对对对,没错。

[18:06] **SPEAKER_02:** 1000x and then that's what you should see first and then many of you you know they'll be like games companies or you know other types of companies that have built some kind of best-selling app best-selling game using uh these tools that's what you should see first and then more of that will

> ……一千倍(的效率),而这正是你应该先看到的。然后你们当中的许多人——会有一些游戏公司或其他类型的公司,用这些工具打造出某种畅销应用、畅销游戏,这是你应该先看到的。之后会有越来越多这样的东西……

[18:24] **SPEAKER_01:** get automated I mean some of it is like there's a human in there and then the human doesn't want

> ……被自动化。我是说,其中一部分情况是,里面还有个人参与,而那个人不愿意……

[18:28] **SPEAKER_02:** to say that the the agents did it yet I think part of it might be though that um this if we want to discuss like creativity what I often say about that is like if we look at the things we've done like AlphaGo so obviously very famously you'll all know about the move 37 in game two and for me I was waiting for a moment like that to start the science projects like AlphaFold so we started AlphaFold like the day we got back from Seoul which is 10 years ago now I'm going to career after this to celebrate the 10-year anniversary of AlphaGo but it's not enough to come up with move 37 like that's pretty cool very useful um but can it invent go that's what I want a system that can invent go if you give it a high level description you know like a game you can learn the rules of in five minutes but it takes many lifetimes to master it's beautiful aesthetically but you can play it in a few hours in an afternoon so you know maybe you could imagine that would be the high level description I would give and then I'd want the the return the thing I get back is go right and um clearly today systems I think can't do that so the question is why um and I think there's something still missing

> ……承认是智能体做的。不过我认为,其中一部分原因,如果我们要谈创造力的话——我常这样说:看看我们做过的事,比如 AlphaGo,大家都很熟悉、也很著名的就是第二局里的"第 37 手"。对我来说,我一直在等待这样一个时刻,好去启动像 AlphaFold 这样的科学项目。我们几乎是从首尔回来的那天就开始做 AlphaFold 的,那已经是十年前了——今晚之后我要去参加庆祝 AlphaGo 十周年的活动。但是,想出"第 37 手"是不够的,那当然很酷、很有用,但它能不能"发明"围棋呢?这才是我想要的——一个能发明围棋的系统:如果你给它一段高层次的描述,比如"一个规则五分钟就能学会、却要许多辈子才能精通、在美学上很美、你可以在一个下午几个小时里就下上一盘"的游戏,你也许可以想象那就是我会给出的高层次描述,然后我希望它返回给我的东西——就是围棋。显然,我认为今天的系统做不到这一点。所以问题是:为什么?我认为其中仍然缺了点什么。

[19:42] **SPEAKER_01:** there well someone in this room might might make it then the answer would be there's nothing missing

> 那么,这个房间里也许就有人能做到,那答案就会是:什么都不缺。

[19:46] **SPEAKER_02:** it just was the way we were using the systems and that might actually be the answer it might be that our today systems are capable of that with a brilliant enough creative person using it and providing that impetus that's the soul of the project and being able to probably being enough with the tools um so like almost be at one with the tools I could imagine that would be happening if you experimented with the tools all day and all night like probably many of you are doing that and you combine that with proper deep creativity um something you know more incredible could be done

> ……只是我们使用这些系统的方式问题。而这实际上可能正是答案:也许我们今天的系统本就有这个能力,只要有一个足够才华横溢、有创造力的人去使用它,去提供那份推动力——那是项目的灵魂——并且能够与工具足够地融为一体,几乎与工具合而为一。我可以想象,如果你日日夜夜地实验这些工具(你们许多人大概正在这么做),再把它和真正深刻的创造力结合起来,某种更了不起的东西就能被创造出来。

[20:19] **SPEAKER_01:** switching gears to open source I mean or open open and open weights I mean the recent release of Gemma you're making highly capable open and accessible ones that can actually run locally what do you think that means for will AI be something that is in the hands of users instead of primarily in the cloud and does that change who gets to you know build with these

> 换个话题聊聊开源——我是说开放、开放权重。最近你们发布了 Gemma,你们在做能力很强、开放且可获取、能真正在本地运行的模型。你认为这意味着什么?AI 会不会成为掌握在用户手中、而不再主要依托云端的东西?这是否会改变谁能用这些模型去搭建?

[20:41] **SPEAKER_02:** models we're huge proponents of in general of open source and open science and you mentioned Alpha Fold at the beginning you know we put that all out there for free and all of our science work even still today we publish in you know the big journals we wanted to create uh world leading models for their their sizes right and so that's what hopefully we've done with Gemma and we're you know very committed to that path and hopefully you'll experiment and build and enjoy using Gemma I think it's been like 40 million downloads now and uh just in you know two and a half weeks so we're really excited about that and I also think it's important for there to be Western stacks on open source you know obviously a lot of the Chinese models are excellent and and they're currently we're leading in open source and we think Gem is very competitive for its sizes uh in in all those respects and for us I mean there is a question of resources talent and compute like nobody has enough compute to just make two you know uh Frontier models at maximum size right with different attributes so that's pretty difficult but also for what for now what we've we've decided is that our Edge models the things we want to use for Android and glasses and robotics um it's best that they're open models because they're vulnerable anyway on the set once you put them out on the surfaces so they might as well be actually fully open right so we've sort of made a decision to do that uh at the at the kind of we call it Nano size level so that actually works for us uh strategically as well um and you know we hope as many people as possible build on it and of course

> 我们总体上是开源和开放科学的坚定支持者。你一开始提到 AlphaFold,我们把它全部免费公开了,我们所有的科学工作,直到今天都还发表在那些大期刊上。我们想要打造在各自体量上世界领先的模型,而这正是我们希望通过 Gemma 所做到的。我们非常坚定地走这条路,希望你们去实验、去搭建、去享受使用 Gemma。我记得现在已经有大约 4000 万次下载了,而这才不过两周半的时间,所以我们对此非常兴奋。我也认为,开源领域有西方的技术栈很重要。显然,很多中国的模型都很出色,而且它们目前在开源上处于领先,我们认为 Gemma 就其体量而言在所有这些方面都很有竞争力。对我们来说,这里有一个资源、人才和算力的问题——没有人有足够的算力去同时打造两个具有不同特性的、最大规模的前沿模型,那相当困难。此外,就目前而言,我们决定的是:我们的边缘端模型——那些我们想用于 Android、眼镜和机器人的东西——最好是开放模型,因为反正一旦你把它们部署到各种终端上,它们本来就是脆弱的、可被攻破的,那还不如干脆完全开放。所以我们算是做了这样一个决定,在我们称之为 Nano(纳米)尺寸这一级别上这么做,这在战略上对我们也确实说得通。我们希望尽可能多的人在它之上进行构建,当然……

[22:18] **SPEAKER_01:** we'll be building on that too earlier before we came on I got to show you a demo of uh my version of Samantha from her which is yes uh harrowing for me to try to demo something to you and it worked which is amazing Gemini was built multimodal and I spent a lot of time with a bunch of the um depth of the context and the tool use with speech directly to model yeah there's nothing

> ……我们也会在它之上构建。刚才上场之前,我给你看了一个演示,是我做的《她》(Her)里那个 Samantha 的版本——是的,当着你的面演示东西对我来说挺让人心惊胆战的,而它成功了,这很棒。Gemini 从一开始就是多模态构建的,我花了很多时间去研究上下文的深度、以及把语音直接接入模型的工具使用。是的,没有什么……

[22:42] **SPEAKER_02:** like bar none like the best one actually yeah yeah I think I think that's a sort of still a slightly underappreciated aspect of of of the Gemini series is we we started it being multimodal from the start that made it a little bit more difficult actually to begin with because then just focusing on text for example but we believe we're going to gain from that in the long run and I think we're seeing that now for uh things like world model building so stuff like genie that we build on top of Gemini I think it's going to be really important for things like robotics so this is why Gemini robotics which many of you probably played around with I think it's going to be built on multimodal Foundation models the robotics models and we think we have a sort of competitive advantage with with Gemini being so strong at multimodal we're using it increasingly in things like Waymo but also if you imagine devices and assistance that digital assistance that come with you into the real world you know maybe on your phone or glasses or some other device it needs to understand the physical world around you and intuitive physics and and the physical context you're in and that's what our systems are extremely good at and I think you found that's why you've enjoyed using it in your setup we're planning to continue on that and I think we're far and away the strongest models on on those types of uh problems so the cost of inference

> ……毫无疑问地能比得上它——它其实是最好的。是的,我认为这算是 Gemini 系列一个仍然稍被低估的方面:我们从一开始就把它做成多模态的。这在起步阶段其实让事情变得更难了一些,因为相比之下只专注文本会容易得多,但我们相信从长远看会因此获益,而我认为我们现在正看到这一点,比如在世界模型构建方面。像 Genie 这样建立在 Gemini 之上的东西,我认为对机器人等领域会非常重要。这就是为什么 Gemini Robotics——你们许多人大概都玩过——我认为这些机器人模型会建立在多模态基础模型之上。我们认为凭借 Gemini 在多模态上的强大,我们拥有某种竞争优势。我们在 Waymo 等场景中越来越多地使用它。此外,如果你想象那些会跟随你进入现实世界的设备和数字助手——也许在你的手机、眼镜或其他设备上——它需要理解你周围的物理世界、直觉物理,以及你所处的物理情境,而这正是我们的系统极其擅长的。我想你已经发现了,这就是你为什么喜欢在你的方案里使用它。我们计划在这条路上继续走下去,我认为在这类问题上我们是遥遥领先、最强的模型。那么推理成本……

[24:02] **SPEAKER_01:** is uh dropping fast what becomes possible when inference is essentially free and how does that change what your team is actually optimizing for yeah I'm not

> ……正在快速下降。当推理基本免费时,什么会变得可能?这又会如何改变你的团队实际所优化的目标?

[24:11] **SPEAKER_02:** sure inference will ever be essentially free I mean there's sort of Jevon's paradox and other things about like I think we'll just end up using all of us will end up using whatever we can get our hands on and you could imagine uh millions of agents swarms of agents working together on things that's one way to use the inference or you could imagine uh single agents or groups smaller groups thinking for in multiple directions and then ensembling that so we're experimenting with all these things probably many of you are all of that will use up any inference I think that's available I mean one day maybe it can be almost cost zero certainly the energy if we solve Fusion or you know superconductors or you know optimal batteries or some set of those things which I think we will do with material science energy costs will be essentially zero but they'll still be the physical creation of the chips and other things they'll sub there'll be some bottleneck um at least for the next few decades I think and so if that's the case there'll still be rationing on the inference side you'll still have to use it I think efficiently

> 我不确定推理是否真的会变得基本免费。你知道,有杰文斯悖论之类的道理——我认为我们最终都会把能拿到手的一切算力都用光。你可以想象数百万个智能体、成群结队的智能体协同处理事情,这是使用推理的一种方式;你也可以想象单个智能体、或较小的一组,朝多个方向思考,然后集成它们的结果。所以我们在实验所有这些,你们许多人大概也是。所有这些都会把可得的推理算力用光。也许有一天推理可以做到几乎零成本——能源肯定是这样,如果我们解决了核聚变、超导体、最优电池,或者其中的某些组合(我认为我们会靠材料科学做到),那么能源成本将基本为零。但仍然会有芯片等东西的物理制造,总会有某种瓶颈,至少在未来几十年里我认为是这样。既然如此,推理这一侧仍然会有配给,你仍然必须高效地使用它。

[25:17] **SPEAKER_01:** yeah well luckily the smaller models are getting smarter and smarter which is fantastic uh we got a lot of bio and biotech founders in the audience I can see a few alpha 3 took us Beyond proteins to a broad spectrum of biomolecules how close are we to modeling full cellular systems or is that still a fundamentally

> 是啊,幸好更小的模型正变得越来越聪明,这太棒了。观众里有很多生物和生物科技领域的创始人,我能看到几位。AlphaFold 3 把我们从蛋白质带到了更广谱的生物大分子。我们离对完整的细胞系统建模还有多远?还是说那仍然是一个从根本上……

[25:36] **SPEAKER_02:** harder problem in a class of its own well isomorphic Labs which we spun out from from from from Deep Mind after we did Alpha fold two um it's it's which is going amazingly well it's it's it's trying to build out uh not just Alpha fold it's just one piece of the drug Discovery process uh as many you know but we're trying to do the adjacent biochemistry and chemistry to design the right compounds with the right properties and so on we'll have some big announcements for you know very soon to talk about on on that front I think that's going really well eventually you want a whole virtual cell so I've talked about this in many of my science talks about a full working simulation of a cell that you can perturb and then the you know the the outputs of that would be close enough to experimental that it's useful right you could skip out a lot of the the search steps and generate lots of synthetic data to train other models that then would predict things about you know real cells and um I think we're about 10 years away from that so I think there's a lot that we can do to bridge that gap I think we're about 10 years away from that so I think we're about 10 years away from that so I think probably from something like a virtual cell like a full virtual cell you know we're starting out this is we're working on the deep mind side science side on a you know virtual nucleus cell nucleus first because relatively self-contained the trick with all of these things is can you pick a slice of the complexity you know eventually you want to want to model a human body but can you model it down to the right level of detail and what slice can you take out of it that will be self-contained enough you can kind of model and approximate the inputs and outputs into that self-contained system and then just focus on the self-contained system so a nucleus is quite interesting from that perspective then the other issue is just there's not enough data yet so you need data and i talked to various you know top scientists about who work on electron microscopes and other imaging things if we could image a live cell without killing the cell that would be game-changing obviously because then you could convert it into a vision problem which we would know how to solve right but at the moment there are at least i'm not aware of any techniques that can give you a kind of you know nanometer resolution but without destroying but in you know in a live dynamic cell so you can see all the interactions right you can take static images at that resolution obviously really detailed now that's quite exciting but it's not enough to turn it just into just into you know a complex vision problem so that's one way it could be solved so it could be a hardware driven data driven solution or it could be that we build better learned simulators of these dynamical systems so that's that's the more modeling way of solving it you've been looking at all kinds of

> ……更难的、自成一类的问题?我们在做完 AlphaFold 2 之后从 DeepMind 分拆出来的 Isomorphic Labs,进展好得惊人。它试图不仅仅构建 AlphaFold——如你们许多人所知,那只是药物发现流程中的一环——我们还在做与之相邻的生物化学和化学,去设计具有恰当性质的合适化合物等等。我们很快就会在这方面有一些重大公告要谈,我认为进展非常顺利。最终你想要的是一个完整的虚拟细胞。我在许多科学演讲里都谈过这个:一个完整可运行的细胞模拟,你可以对它施加扰动,而它的输出会足够接近实验结果,以至于真的有用——你可以省去大量搜索步骤,并生成大量合成数据来训练其他模型,那些模型进而就能预测真实细胞的一些情况。我认为我们距离那个大约还有十年,所以我认为要弥合那道鸿沟我们还有很多事情可做。要从类似完整虚拟细胞这样的东西出发……我们才刚起步,在 DeepMind 的科学这一侧,我们先做一个虚拟的细胞核,因为它相对自成一体。所有这类事情的诀窍在于:你能否切出复杂性中的一个切片?最终你想给整个人体建模,但你能否把它建到恰当的细节层级?你能从中切出哪一块,使之足够自成一体,让你可以对进出这个封闭系统的输入输出进行建模和近似,然后只专注于这个封闭系统本身?从这个角度看,细胞核相当有意思。另一个问题就是目前数据还不够,所以你需要数据。我和多位做电子显微镜及其他成像技术的顶尖科学家聊过:如果我们能在不杀死细胞的情况下对一个活细胞成像,那显然将会是颠覆性的,因为那样你就能把它转化成一个视觉问题,而视觉问题我们是知道怎么解决的。但目前——至少据我所知——还没有任何技术能在一个活的、动态的细胞中,给你纳米级分辨率却又不破坏它,好让你看到所有的相互作用。你当然可以在那种分辨率下拍静态图像,非常精细,这很令人兴奋,但那还不足以把它变成一个纯粹的复杂视觉问题。所以这是它可能被解决的一条路——它可能是硬件驱动、数据驱动的解决方案;也可能是我们为这些动力学系统构建更好的、学习得到的模拟器,那是更偏建模的解决方式。你一直在关注各种各样的……

[28:19] **SPEAKER_01:** science not just bio there's material science drug discovery climate modeling mathematics if you had to rank which scientific domain will transform the most dramatically the next five years what's in your list well they're all so

> ……科学,不只是生物,还有材料科学、药物发现、气候建模、数学。如果一定要你排个序,未来五年哪个科学领域会发生最剧烈的变革,你的清单上会是什么?

[28:31] **SPEAKER_02:** exciting and that's why i mean that that for me has been my main passion and always the reason why i've worked on ai for my whole career for 30 plus years now is to use ai as the ultimate tool i always thought ai would be the ultimate tool for science and to invite such advanced scientific understanding scientific discovery and things like medicine and just our understanding of the universe around us so actually when you mentioned our original way we used to articulate our mission statement which is still uh the way we think about it is there was two steps to it one was step one was to put a machine in place and then the other one was to put a machine in place and One was solve intelligence, i.e. build AGI, and then step two was use it to solve everything else. We had to change that a bit over time because people were like, do you really mean solve everything else? And we did mean that. And I think people are sort of understanding what that means

> 它们都太令人兴奋了,而这正是原因所在。对我来说,这一直是我的主要热情所在,也一直是我整个职业生涯——如今已有 30 多年——投身 AI 的原因:把 AI 当作终极工具。我一直认为 AI 会成为科学的终极工具,能带来如此先进的科学理解、科学发现,以及医学等领域的进步,乃至我们对周遭宇宙的理解。所以当你提到我们最初表述使命的方式时——那也仍是我们思考问题的方式——它分两步:第一步是"解决智能",也就是构建 AGI;第二步是用它去解决其他一切。随着时间推移我们不得不稍微改了一下措辞,因为人们会说"你们真的是指解决其他一切吗?"而我们确实就是这个意思。我认为如今人们正逐渐理解那意味着什么。

[29:13] **SPEAKER_02:** today. But specifically, I was meaning solve other what I call root node problems in science. So areas of science that would unlock whole new branches or avenues of discovery. And AlphaFold is the prototypical example of what we want to do. So over 3 million researchers around the world,

> 但具体来说,我指的是解决我所谓科学中的"根节点问题"——那些能解锁全新分支或全新发现路径的科学领域。而 AlphaFold 正是我们想做的事情的典型例子。如今全世界有超过 300 万名研究人员……

[29:30] **SPEAKER_02:** pretty much every biology researcher in the world uses AlphaFold now. And I was told by some of my pharma executive friends that almost every drug discovered from now on will have used AlphaFold at some point in the drug discovery process. So that's something we're very proud of. And it's the sort of impact that we hope to have with AI. But I do think it's just the beginning.

> ……几乎全世界每一位生物学研究者现在都在用 AlphaFold。我的一些制药高管朋友告诉我,从今往后几乎每一种被发现的新药,都会在药物发现过程的某个环节用到 AlphaFold。这是我们非常自豪的事情,也正是我们希望用 AI 带来的那种影响。但我确实认为这仅仅是个开始。

[29:53] **SPEAKER_02:** I don't really see any area of science or engineering that this won't be able to help be helpful with. And the ones you mentioned, I think we're almost like an AlphaFold one moment. So we've got very promising results, but it's not quite solved the grand challenge yet in that domain. But I think we're going to have a lot to talk about in the next couple of years on all those areas you mentioned, materials, which I think is very exciting, all the way to mathematics.

> 我几乎看不到有哪个科学或工程领域是它帮不上忙的。而你提到的那些领域,我认为我们差不多正处在一个"AlphaFold 1 时刻":我们已经有了非常有希望的结果,但在那个领域还没有完全攻克那个重大难题。不过我认为在你提到的所有这些领域——从材料(我认为非常令人兴奋)一直到数学——我们在未来几年会有很多可谈的。

[30:17] **SPEAKER_01:** In science, I mean, it feels Promethean. It's like, here is this capability.

> 在科学领域,这感觉很有"普罗米修斯"的意味——就好像,这里有这样一种能力。

[30:23] **SPEAKER_02:** I think so. I mean, of course, along with that, including the parable of Prometheus, we have to also be careful. With how we use that and what we use it for, and also the misuse that can happen with those same tools.

> 我也这么认为。当然,伴随而来的——包括普罗米修斯那个寓言在内——我们也必须谨慎:谨慎对待我们如何使用它、用它来做什么,以及同样这些工具可能被滥用的情形。

[30:36] **SPEAKER_01:** A lot of people in this room are trying to build companies, applying AI to science. For them, what's the difference between a startup that actually advances the frontier in your view versus one that's just wrapping an API around a foundation model and calling it AI for science?

> 这个房间里有很多人正试图创办公司,把 AI 应用于科学。对他们来说,在你看来,一家真正推动前沿的初创公司,与一家只是给基础模型套个 API 外壳、就号称"AI for science"的公司,区别在哪里?

[30:49] **SPEAKER_02:** Well, look, I think that's one of the things I would recommend. I'm trying to think about, and I think you mentioned this to me before, what would I do today myself if I was sitting in your place in Y Combinator, you know, looking at things? One thing you have to do is obviously intercept where the AI tech is going. So that's one hard part of it. But I do think there's huge scope for combining

> 好,我认为这正是我会推荐的事情之一。我在想——你之前也跟我提过这个——如果今天是我坐在你们 Y Combinator 的位置上审视这些机会,我会怎么做?你显然必须做到的一件事,是去"截住"AI 技术未来的走向,这是难点之一。但我确实认为,把它结合起来有巨大的空间……

[31:10] **SPEAKER_02:** where AI is going with some other deep technology area. I just think that that sweet spot is, whether it's materials or medicine or other really hard areas of science, I think that those kinds of interdisciplinary teams, especially if it involves the world of atoms as well, there's not going to be a shortcut to that. Yeah. Yeah.

> ……把 AI 未来的走向与某个别的深科技领域结合起来。我认为那个甜蜜点——无论是材料、医学还是其他真正困难的科学领域——我认为那种跨学科团队,尤其是当它还涉及"原子世界"(实体世界)时,是没有捷径可走的。是的,没错。

[31:29] **SPEAKER_02:** Yeah. Yeah. In the foreseeable future. Those are areas that are pretty safe from just getting swamped by whatever the next update is to the foundation models.

> 是的,在可预见的未来是这样。那些领域相当"安全",不会因为基础模型的下一次更新就被轻易淹没掉。

[31:38] **SPEAKER_02:** So I think if you're looking for things like that, that's one of the more defensible areas, I would say. And I've always loved deep tech, so I'm kind of biased towards deep tech things. I think nothing that's really long lasting and worthwhile is easy. And so I'm always being drawn to deep technologies. Obviously, AI was like that back in 2010 when we started

> 所以我认为,如果你在寻找这类东西,那是较有护城河的领域之一。我一向热爱深科技,所以我对深科技的东西有点偏爱。我认为任何真正持久且值得做的东西都不容易,因此我总是被深科技所吸引。显然,2010 年我们起步时,AI 就是这样一件事……

[32:00] **SPEAKER_02:** out, right? It was thought to just, we know it doesn't work kind of thing is what I was told by investors. And even in academia, it was considered to be a very niche subject that we sort of tried in the 90s and we know it doesn't work. But if you have belief and conviction in your idea why it's different this time or what special combination from your background that you had, ideally you're expert in both those areas, both the machine learning and the other area you're applying it to, or you can create a founding team with that expertise, I think there's huge impact to be made there and huge value to be built there.

> ……对吧?当时投资人对我说的是那种"我们知道它行不通"的态度。甚至在学术界,它也被视为一个非常小众的课题——我们在 90 年代试过了,知道它行不通。但如果你对自己的想法抱有信念和笃定——相信这次为什么会不一样,或者你的背景带来了什么特殊的组合(理想情况下你在两个领域都是专家:既懂机器学习,也懂你要应用它的那个领域;或者你能组建一个具备这种专长的创始团队)——我认为在那里能创造出巨大的影响力,也能构建出巨大的价值。

[32:34] **SPEAKER_01:** That's a really important message. I mean, it's easy to forget. Basically, once you've done it, you've done it. But before you've done it, people are arrayed against you.

> 这是一个非常重要的信息。这一点很容易被忘记:基本上,一旦你做成了,就是做成了;但在你做成之前,所有人都站在你的对立面。

[32:43] **SPEAKER_02:** Oh, sure. I mean, no one believes in it, which is why I think you've also got to work in things that you're genuinely passionate about. For me, I would have worked on AI no matter what happened. I just decided from a very young age, it was the thing that could be the most consequential thing I could think of. It's turned out that way, but it might not. Maybe

> 哦,当然。没有人相信它,这也正是为什么我认为你必须去做你真正充满热情的事情。对我来说,不管发生什么,我都会去做 AI。我从很小的时候就认定,它可能是我所能想到的最具深远影响的事情。结果确实如此,但它本可能不是。也许……

[33:03] **SPEAKER_02:** we would have been 50 years too early. And it was also the most interesting thing I could think of working on. And so I would still be working on AI today, even if we were still in a little garage somewhere and it still wasn't quite working. I would have still been trying to find, maybe I'd have been back in academia or something, but I would have found some way of continuing to work

> ……我们本可能早了 50 年。它同时也是我能想到的最有趣、最值得投身的事情。所以即便我们今天还窝在某个小车库里、它还没完全跑通,我今天也仍然会在做 AI。我仍然会想方设法——也许我会回到学术界之类的,但我总会找到某种方式继续做下去。

[33:23] **SPEAKER_01:** on it. So, I mean, Alphold was like an example of a spike that you pursued and it worked. What makes the scientific domain ripe for an Alphold style breakthrough? And is there a pattern, a certain

> 继续做下去。那么,AlphaFold 算是你追求并且成功了的一个"尖峰"的例子。是什么让一个科学领域成熟到可以出现 AlphaFold 式的突破?有没有一种模式,某种……

[33:34] **SPEAKER_02:** objective function? I should write this up at some point when I have five minutes spare, but the lesson I've learned from all the Alph projects we've done, specifically AlphaGo and Alphold, is I think the techniques we have and the problems I like to look for are great if the situation can be described as massive combinatorial search space. The more massive, the better in some ways, so no brute force or special case algorithm will solve it. And that's true of Go moves and of different configurations of proteins far more than the atoms in the universe, both of those.

> ……某种目标函数?我应该找个有五分钟空闲的时候把这写下来。但我从我们做过的所有 Alpha 系列项目——尤其是 AlphaGo 和 AlphaFold——中学到的经验是:我认为我们所拥有的技术、以及我喜欢去寻找的问题,在这样一种情形下会非常契合:局面可以被描述为一个巨大的组合搜索空间。某种意义上越巨大越好,以至于没有任何暴力搜索或特例算法能解决它。围棋的走法是这样,蛋白质的不同构象也是这样——这两者的可能性都远远超过宇宙中的原子数目。

[34:09] **SPEAKER_02:** And then you have a clear objective function. So you could think of it as minimizing the free energy in the proteins or winning the game of Go. So you need to specify your objective function clearly so you can hill climb. And then enough data and or simulator that can generate you lots of in-distribution synthetic data. If those things are true, then I think

> 然后你要有一个清晰的目标函数。你可以把它理解为最小化蛋白质中的自由能,或者赢下一盘围棋。所以你需要清晰地界定你的目标函数,这样才能做"爬山"式优化。再加上足够的数据,和/或一个能为你生成大量分布内合成数据的模拟器。如果这些条件都成立,那么我认为……

[34:35] **SPEAKER_02:** with today's methods, you can go a long way into tackling and finding the kind of needle in the haystack that you need for the solution that you're trying to look for. And I think of just drug discovery, by the way, in the same way, right? There is a compound out there that would solve this disease if one could find it, if one could only find it, right? And that wouldn't have any side effects and so on. And as long as the laws of physics allow,

> ……用今天的方法,你就能走得很远,去攻克并找到那种"大海捞针"式的、你所寻求解答所需要的东西。顺便说一句,我也是用同样的方式来看待药物发现的:世上存在着某种化合物,只要能找到它、只要有人能找到它,就能治愈这种疾病,而且不会有任何副作用等等。只要物理定律……

[34:58] **SPEAKER_02:** they allow it, then the only question is how do you find it in an efficient way? In an attractible way? Well, I think we showed for the first time actually with AlphaGo, that these systems could find those kinds of needles in the haystack in that case,

> ……允许它存在,那么唯一的问题就是:你如何以高效的、可解的方式把它找出来?我认为我们其实是用 AlphaGo 第一次证明了,这些系统能够在这种情形下找到那样"大海捞针"般的目标……

[35:12] **SPEAKER_01:** you know, the perfect Go move. I guess to get a little meta, I mean, we were talking about humans using these methods to create alpha fold, but then there's a meta level, which is humans using AI to explore the space of possible hypotheses. How close are we to AI systems that can do that? Yeah, yeah. Yeah, absolutely. So that's kind of the main thing,

> ……也就是那步完美的围棋。我想稍微上升到"元"层面:我们刚才谈的是人类用这些方法去创造 AlphaFold,但还有一个更高的层面,就是人类用 AI 去探索可能假设的空间。我们离能做到这一点的 AI 系统还有多远?是的,没错,绝对如此。所以这算是最主要的事情……

[35:27] **SPEAKER_01:** and then at the end of the, you know, sort of the question is, how do you find it in an efficient way? that can do genuine scientific reasoning not just pattern matching on data i think we're close um

> ……归根结底,问题在于:你如何以高效的方式找到它?一个能进行真正科学推理、而不只是对数据做模式匹配的系统。我认为我们已经很接近了。

[35:35] **SPEAKER_02:** we're working on these general systems like that like i think we have this system called co-scientist and we have other algorithms like alpha evolve that can go a little bit beyond what the basic gemini will do and obviously all the frontier labs are experimenting in this way i've yet to seen anything so far and we all tinker with same things you know some math problems that are a little bit harder than imo and so on i haven't seen anything yet um that is a true genuine you know massive discovery that's my personal opinion i think it's coming i think it may be related to uh this earlier this thing we discussed about creativity and and actually going on beyond the bounds of what's known so clearly that's just not pattern matching at that point because there is no pattern to match to and it's a bit more than extrapolation it's some kind of analogical reasoning and i don't think these systems have that or at least we're not using them in the in the right way to do that so the way i often say that in science is can it come up with a hypothesis that's really interesting not just solve one when i say just we're now talking about just like solving the riemann hypothesis or something this would be obviously amazing or one of the millennium prize problems and maybe we're a couple of years out from doing that um but i'd like to solve p equals np that's that's my favorite one but can you but even harder than that would be to come up with a new set of of millennium prize problems that were regarded by top mathematicians to be as you know deep and meaningful and worthy of lifetime of study and effort to solve i think that's another level harder and uh we don't have um you know i still don't think we know how to do that i don't think it's it's magical though i do think these systems will be eventually be able to do that maybe we're missing one or two things and then the way we would test that is you know sometimes call my einstein test which is you know can you train a system with the knowledge of cutoff of 1901 and then will it come up with you know what einstein did in 1905 including special relativity you know his anna's mirabilis can it can it do that right uh and then i think we could run that test maybe maybe we should just run that test and keep seeing if that's possible and once that is then i think we're on the verge of these systems being able to invent something new truly novel so last last

> ……我们正在研究这类通用系统。我们有一个叫 Co-Scientist(联合科学家)的系统,还有像 AlphaEvolve 这样的其他算法,能比基础的 Gemini 稍微多做一点。显然所有前沿实验室都在这个方向上做实验。到目前为止我还没见过任何东西——我们都在鼓捣同样的东西,比如一些比 IMO 稍难一点的数学题之类——我还没见过任何堪称真正、货真价实的重大发现,这是我个人的看法。我认为它会到来。我认为它可能和我们前面讨论过的创造力、以及真正跨越已知边界的能力有关。因为很显然,到那个程度就不再是模式匹配了,因为根本没有可供匹配的模式;它也不止是外推,而是某种类比推理,而我不认为这些系统具备这一点,或者至少我们没有以正确的方式使用它们来做到这一点。所以我在科学语境里常这样说:它能不能提出一个真正有趣的假设,而不只是解出一个假设。当我说"只是"时——我们现在谈的可是像证明黎曼猜想之类的事情,那显然会非常了不起,或者某个千禧年大奖难题,也许我们离做到那一步还有几年;不过我最想解决的是 P 是否等于 NP,那是我最喜欢的一个。但比那更难的,会是提出一组全新的千禧年大奖难题,而且被顶尖数学家们认为同样深刻、有意义、值得倾注一生去研究和攻克。我认为那又难了一个层级,而我们还没有——我仍然认为我们还不知道该怎么做到。不过我不认为这有什么神秘的,我确实相信这些系统最终能够做到,也许我们只是还缺一两样东西。而我们检验的方式,就是我有时说的"爱因斯坦测试":你能不能用知识截止到 1901 年的数据去训练一个系统,然后它会不会提出爱因斯坦在 1905 年——他的"奇迹年"——所做出的成果,包括狭义相对论?它能不能做到?然后我认为我们可以跑这个测试,也许我们真该跑一跑这个测试,不断看看它是否可行。而一旦它能做到,我认为我们就站在了这些系统能够发明出全新的、真正新颖的东西的临界点上。那么最后一个……

[37:53] **SPEAKER_01:** question for the audience if you have a question for the audience if you have a question for the people who are deeply technical in this room who want to work on something you know even close to the scale that what you've created with you know it's one of the largest ai efforts in the world and you've been a pioneer for all these years so for that i think everyone in this room thanks you and the folks at deep mind very very deeply from the bottom of our hearts thank you what's the thing that you know now about building at the frontier that you wish you

> ……问题,是替观众问的。给这个房间里那些深谙技术、想去做一些哪怕只是接近于你所创造的规模的事情的人——你所创造的是世界上最大的 AI 事业之一,而你这么多年来一直是先驱。为此,我想这个房间里的每一个人都发自内心地、非常非常深切地感谢你和 DeepMind 的同事们,谢谢你们。那么:关于在前沿做事,有什么是你现在明白、而当年 25 岁的你希望自己早就知道的?

[38:18] **SPEAKER_02:** known at 25. i think we covered some of it in terms of actually you you work out that like if you look at what people say to me about the welfare crisis it's quite a complex matter it's quite difficult to talk about it and like i agree with each of you if you're working on a particular model we're going to go really deep into the history of this but but i think what you're describing is like going after hard problems and deep problems um it's no more difficult in some ways than than going after a shallower simpler more superficial problem they're just differently difficult there's different things that are hard about each of those things but i think given life's very short and you know you only have so much time and energy you might as well put your life force into something that will really make a a difference if you hadn't done it if you hadn't been there to push it so i would just think of it through that language but actually i'm also a bit concerned about that i think just really important and like the on the right hand

> 25 岁时希望知道的事。我想我们已经谈到了一部分。你会渐渐明白——我认为你所描述的,是去追逐困难而深刻的问题。从某种意义上说,这并不比去追逐一个更浅显、更简单、更表面的问题更难,它们只是难法不同,各有各难的地方。但我认为,鉴于人生非常短暂、你的时间和精力都有限,你不如把你的生命力倾注到某件真正能带来改变的事情上——那种如果不是你去做、不是你在那里推动它就不会发生的事。所以我会用这样的思路去看待它。而我实际上也对此有点在意,我觉得这真的非常重要。

[39:30] **SPEAKER_02:** So I would just think of it through that lens. And then the other thing is, if you are, and we talked about deep tech, and I love interdisciplinary work, and I think that's going to be even more prevalent in the next few years, in combinations of fields and finding the connections between those fields. And it's going to be even easier to do that with AI. And then the only other thing I would say is if, you know, if you have your, depending on what your AGI timeline is, you know, mine's like 2030 or something like this, then if you start off on a deep tech journey today, usually that you're talking about a 10 year journey for true deep tech, in my opinion.

> 所以我会用那样的视角去看待它。另一件事是,我们谈到了深科技,我热爱跨学科的工作,而我认为在未来几年这会变得更加普遍——在各领域的交叉组合中、在寻找这些领域之间联系的过程中。而借助 AI,做这件事会变得更容易。我唯一还想说的另一点是:取决于你对 AGI 时间线的判断——我个人大概是 2030 年左右——如果你今天踏上一段深科技的征程,那么在我看来,真正的深科技通常意味着一段长达 10 年的旅程。

[39:40] **SPEAKER_02:** So then now you have to just consider AGI appearing in the middle of that journey. So what does that mean? It doesn't, it's not bad, necessarily. But you have to take that.

> 那么现在你就必须考虑到,AGI 会在这段旅程的中途出现。这意味着什么?这未必是坏事,但你必须把它……

[40:10] **SPEAKER_02:** Into account, right to will it be able to leverage it? What will the AGI system do with it? And it goes a little bit back to what you said earlier about alpha fold and general AI systems. So one thing I can think see happening is Gemini, Claude, or one of these general systems, making use of alpha fold, like specialized systems as tools, I don't think we're going to have it just in one giant brain, because it will have too much regression. And if I put all the proteins into, you know, Gemini, that wouldn't make sense. We don't need Gemini.

> ……纳入考量:它能否利用 AGI?AGI 系统会拿它来做什么?这有点回到你早先关于 AlphaFold 和通用 AI 系统的话题。我能想到会发生的一件事是:Gemini、Claude 或某个这类通用系统,会把像 AlphaFold 这样的专用系统当作工具来使用。我不认为我们会把一切都塞进一个巨大的大脑里,因为那会带来太多退化。如果我把所有蛋白质都塞进 Gemini,那说不通——我们不需要让 Gemini……

[40:40] **SPEAKER_02:** To do protein folding, going back to your information efficiency, it will definitely affect its language skills or something like that, right in a bad way. So much better, I think, is to have really good general purpose tool usage models that will then maybe they could even train those specific tools, but they would be in a separate system. So I think that's kind of interesting to think through the implications of that. And then what you might build today, also physical things to like, what kinds of factories would you build? What sorts of, you know, finance systems and so on. So I just think you need to really take that seriously. And on the one hand is like, and imagine what that world would look like, and then build something that would be useful if that comes in halfway through.

> ……去做蛋白质折叠——回到你说的信息效率问题,那肯定会以一种糟糕的方式影响它的语言能力之类。所以我认为好得多的做法,是拥有真正出色的通用型、擅长使用工具的模型,它们也许甚至可以去训练那些专用工具,但这些工具会存在于一个独立的系统里。所以我认为,把这件事的种种含义想清楚是挺有意思的。还有你今天可能会构建的东西,包括实体的东西:你会建造什么样的工厂?什么样的金融系统等等。所以我认为你真的需要认真对待这一点。一方面,去想象那个世界会是什么样子,然后去构建一些即便在(旅程)中途 AGI 到来时仍然有用的东西。
