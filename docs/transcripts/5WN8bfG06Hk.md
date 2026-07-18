# 全文转录 · 从"转型地狱"到 14 亿美元独角兽

> ▶ [YouTube](https://www.youtube.com/watch?v=5WN8bfG06Hk) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/5WN8bfG06Hk.md) &nbsp;·&nbsp; From Pivot Hell To $1.4 Billion Unicorn

> 中英对照 · 每段英文原文下附中文翻译

[00:04] **SPEAKER_01:** I'm here today with James Hawkins, CEO and founder of PostHog from the YC Winter 20 batch. James is here hot off the news of raising a $75 million Series E round of funding at a $1.4 billion valuation, making PostHog the latest YC unicorn. Today, we're going to talk about how PostHog got started, how they pulled off what I think is one of the best YC pivots of the last decade, and how they use attention and humor to compete with not just other tech companies, but with everything out there for attention.

> 我今天请到了 James Hawkins，他是 PostHog 的 CEO 兼创始人，来自 YC 2020 年冬季批次。James 刚刚传来消息，完成了 7500 万美元的 E 轮融资，估值达到 14 亿美元，使 PostHog 成为 YC 最新的独角兽公司。今天我们要聊聊 PostHog 是如何起步的，他们是如何完成我认为是过去十年 YC 最出色的转型之一，以及他们如何利用关注度和幽默感来竞争——不仅仅是和其他科技公司竞争，而是和一切争夺注意力的事物竞争。

[00:33] **SPEAKER_01:** Welcome, James. Thank you for having me.

> 欢迎你，James。谢谢你邀请我。

[00:35] **SPEAKER_00:** James, could you tell us what is PostHog? Explain it to us a little bit. Sure. So with YC, I always feel like this is my homework being marked by the teacher.

> James，你能告诉我们 PostHog 是什么吗？给我们稍微解释一下。当然。跟 YC 打交道时，我总觉得这就像老师在批改我的作业一样。

[00:44] **SPEAKER_00:** We help users to debug their product, to ship features faster through things like feature flags and so on, and we help keep all their customer and product data in one stack.

> 我们帮助用户调试他们的产品，通过功能开关（feature flags）等方式更快地发布功能，同时帮助他们把所有客户和产品数据统一保存在一个技术栈里。

[00:54] **SPEAKER_01:** And tell us a little bit about the state of the company, how big it is. You guys are pretty big these days. Give our viewers a snapshot of what's going on at PostHog. Sure.

> 再跟我们讲讲公司现在的状况，规模有多大。你们现在已经相当大了。给我们的观众描绘一下 PostHog 目前的概况。好的。

[01:04] **SPEAKER_00:** Yeah. So we're about 160 people, we're around 300,000 customers across like a lot of free customers unpaid. We have several thousand paid. We have, I think, 16 or 17 products kind of in production or in development, they're all at different kind of stages.

> 是的。我们现在大约有 160 人，客户约有 30 万，其中很多是免费的、未付费的用户。我们有几千个付费客户。我们大概有 16 或 17 款产品，有的已经上线、有的还在开发中，它们都处于不同的阶段。

[01:21] **SPEAKER_00:** And we've been, I guess like at the moment, the main thing we're doing and the reason kind of why we did a lot of raising this year, we're pushing very hard on getting more products still out of the door. So instead of kind of going upmarket, we're going just across more of kind of the customer data that people are generating, and we're automating a ton of things through AI, which has been a long and arduous process, but we're starting to get to the point where I'm starting to get proud of what we've achieved so far, but I still kind of feel like, oh, we haven't got started yet. There's a lot more to go, which I don't think is a feeling it will ever go, probably. But yeah, it's been a lot of fun and we're just starting to scale up pretty aggressively now.

> 目前我们主要在做的事，也是今年我们大量融资的原因，就是我们非常努力地想推出更多产品。所以我们不是往高端市场走，而是横向覆盖人们生成的更多客户数据，并通过 AI 把大量工作自动化。这是一个漫长而艰辛的过程，但我们开始走到一个阶段，我开始为我们目前取得的成绩感到自豪，不过我仍然有种感觉：哦，我们其实还没真正开始呢。还有很多路要走，我觉得这种感觉大概永远不会消失。但总之，这个过程非常有趣，我们现在才刚开始相当激进地扩张。

[01:57] **SPEAKER_00:** Like we're, I think we started at 70 people this year, and so we're supposed to be about 200-ish by the end of the year or something. We're starting to get properly into kind of scale-up mode at this point.

> 我们今年年初大概是 70 人，预计到年底会达到大约 200 人左右。到这个阶段，我们才真正进入了扩张模式。

[02:05] **SPEAKER_01:** So you've got this team, you've got all these customers, you have all these products that you're developing and improving on, but what was the initial product that PostHog started with? What was that? The first thing that you guys brought to market as PostHog?

> 那么你有这样一支团队，有这么多客户，有这么多正在开发和改进的产品，但 PostHog 最初起步的产品是什么？那是什么？你们作为 PostHog 推向市场的第一款产品是什么？

[02:16] **SPEAKER_00:** Sure. So yeah, the first thing that worked for us, we had a bunch of pivots before, was self-hosted product analytics because we pivoted so many times. Every time we had to set up product analytics over and over again, and we were just getting frustrated having to implement it, I think we found that there was an awful lot of really strong competition. But we felt all the products were built for kind of product managers to force engineers to go implement.

> 当然。第一个真正奏效的东西——在此之前我们经历了很多次转型——是自托管的产品分析工具，因为我们转型太多次了。每次转型我们都得一遍又一遍地搭建产品分析，而我们对不得不去实现它感到很沮丧。我觉得我们发现这个领域竞争其实非常激烈。但我们感觉所有这些产品都是为产品经理设计的，好逼着工程师去实现它。

[02:37] **SPEAKER_00:** But as like reasonably technical, especially my co-founders, a very technical co-founder, was just getting annoyed at like, I can't, I want to write SQL, I want to see the data underneath. I would like to keep this in my infrastructure so I don't lose data due to ad blockers. So we thought, okay, we think there's room for a self-hosted alternative. And we also, we spent some time talking to potential customers, and we found that quite a lot of people had self-built their analytics stack and were maintaining this kind of janky system.

> 但作为相当有技术背景的人，尤其是我的联合创始人——一个非常技术型的联合创始人——他就很恼火：我不能，我想写 SQL，我想看到底层数据。我想把这些数据保留在自己的基础设施里，这样就不会因为广告拦截器而丢失数据。所以我们想，好吧，我们觉得自托管的替代方案是有市场空间的。我们还花了些时间和潜在客户交流，发现相当多的人都自建了分析技术栈，并在维护着这种拼凑起来、不太靠谱的系统。

[03:02] **SPEAKER_00:** Which we felt, if we can productize something like that, because new infrastructure, and we could see this working quite well. So yeah, we started with just open source product analytics on Hacker News. We spent like the last four weeks of the batch desperately trying to get that out of the door. And then we actually pivot, we iterated or say afterwards, and now we're all cloud-based with multi-products.

> 我们觉得，如果我们能把那种东西做成产品——因为是新的基础设施——我们能看出这会运作得相当好。所以，我们就从在 Hacker News 上发布开源产品分析开始。我们在整个批次的最后四周里拼命想把它推出去。后来我们其实又做了调整，之后不断迭代，而现在我们已经全面转向云端，并且有多款产品了。

[03:22] **SPEAKER_00:** But that was the thing that landed for us finally.

> 但那就是最终让我们站稳脚跟的东西。

[03:24] **SPEAKER_01:** I think at Postog, well, there's this meme among founders of pivot hell. Yep. And it's the thing that YC founders talk about a lot. Yeah.

> 我觉得在 PostHog……嗯，创始人之间有个梗叫"转型地狱"。没错。这是 YC 创始人经常谈论的话题。是的。

[03:31] **SPEAKER_01:** You're going from idea to idea to idea, and you're trying to find something that's going to work. And you guys not only came out of pivot hell and have built this awesome company, but what you built was literally forged in the fires of pivot hell. Yep. Right?

> 你从一个想法换到另一个想法，再换到下一个，一直在试图找到能奏效的东西。而你们不仅走出了转型地狱、建立了这家出色的公司，你们打造的东西简直就是在转型地狱的火焰中锻造出来的。没错。对吧？

[03:46] **SPEAKER_01:** Like while doing these pivots, you had this pain that only came because you were doing the pivots and trying to do them at a high level, setting up the analytics over and over again. Tell us a little bit about how you guys actually got to YC and started this journey of pivoting and finding startup ideas that might work.

> 就是说，在做这些转型的过程中，你们体会到了一种痛点，而这种痛点恰恰是因为你们在高水平地不断转型、一遍又一遍地搭建分析工具才产生的。跟我们讲讲你们究竟是怎么进入 YC，并开始这段不断转型、寻找可能奏效的创业点子的旅程的。

[04:02] **SPEAKER_00:** My co-founder quit. We used to work together. And when I heard news that he was leaving, I'd also been thinking about leaving. And that kind of triggered me to go, okay, I want to do my own thing.

> 我的联合创始人辞职了。我们以前是同事。当我听说他要离开的消息时，我自己也一直在考虑离开。那件事有点像触发了我，让我想：好吧，我要去做自己的事情。

[04:14] **SPEAKER_00:** So I made sure to grab him. And instead of getting him to go off and work in another startup or whatever, we thought, hey, let's just do our own thing.

> 所以我一定要把他拉过来。与其让他跑去另一家创业公司之类的地方工作，我们想，嘿，不如我们一起干自己的事吧。

[04:19] **SPEAKER_01:** And when he was leaving, was he leaving to join another company? Was he leaving to start something?

> 他离开的时候，是要去加入另一家公司吗？还是要去创业？

[04:23] **SPEAKER_00:** Yeah. I think he was actually trying to get a job at Facebook at the time. Okay. All right.

> 是的。我想他当时其实是想去 Facebook 找份工作。好的。明白了。

[04:27] **SPEAKER_00:** He was doing an incremental kind of career move. And I'm like, I think I have this idea that we'll probably have a product market fit for in a couple of weeks' time. Of course. Of course.

> 他在做一个循序渐进的职业转变。而我就说，我有个想法，我们大概过几周就能找到产品市场契合点了。当然啦。当然啦。

[04:35] **SPEAKER_00:** They all do. Of course. Yeah. And it's only a hop, skip, and a jump away.

> 大家都这么说。当然了。是啊。感觉离成功只有一步之遥。

[04:39] **SPEAKER_00:** And then we can just... I'd created a list of problems I'd encountered professionally, thinking, okay, I should solve a problem I've had myself.

> 然后我们就可以……我列了一份自己在职业生涯中遇到过的问题清单，心想，好吧，我应该去解决一个我自己亲身经历过的问题。

[04:44] **SPEAKER_00:** And we started going through the list that we thought we wanted to bootstrap initially. So the two of us were just working out of coffee shops. One of the main problems we found was every time we went to see a customer, we'd have to buy another round of coffee. And so we'd often end up getting whatever the coffee equivalent of waste it is, basically.

> 于是我们开始一条条过这份清单，起初我们想靠自筹资金起步。所以我们俩就在咖啡馆里办公。我们发现的一个主要问题是，每次去见客户，我们都得再买一轮咖啡。所以我们经常会喝到——基本上就是咖啡摄入过量的那种状态。

[04:59] **SPEAKER_00:** So eventually, we did this for about six months, and we worked through an average of one idea every five, probably average of about five or six weeks.

> 所以最终，我们这样做了大约六个月，平均每五周……大概平均每五六周就试完一个想法。

[05:08] **SPEAKER_01:** Do you remember what any of those ideas were?

> 你还记得其中任何一个想法是什么吗？

[05:09] **SPEAKER_00:** Yeah. So the initial thing we tried to build was a sales territory management product. So I used to run a sales, I was VP of sales. And I felt that in sales, you're literally wasting over 90% of your time, because deals don't usually win, they don't usually close, they usually just float around and gradually get killed off.

> 记得。我们最初尝试做的是一款销售区域管理产品。我以前是做销售的，当过销售副总裁。我觉得在销售中，你实际上有超过 90% 的时间都被浪费了，因为交易通常谈不成、通常成交不了，往往就是悬在那里，然后慢慢地黄掉。

[05:27] **SPEAKER_00:** And so if we get better at not focusing on deals that are closing, but on the ones that aren't closing, going a bit more ruthless, using statistics to pull them out of people's pipeline and change the territory for the sales team is what I thought might work. And it was just kind of really complicated to build, I think, because I'm much more technical than a traditional sales leader would be. I just think we built something kind of complicated, and I don't think our go to market was right or anything. Yeah, we had this idea, we built it, I think the thing that was important, or the harsh lesson I learned was, my co-founder was building it, I was just trying to get an interesting prospects to buy it from us.

> 所以我当时想，如果我们能更擅长不去关注那些正在成交的交易，而是关注那些成交不了的交易，稍微更冷酷一点，用统计数据把它们从销售人员的管道里剔除出去，并为销售团队调整区域划分，这也许行得通。但我觉得它就是构建起来相当复杂，因为我比传统的销售主管技术性强得多。我觉得我们做出来的东西有点太复杂了，而且我觉得我们的市场推广方式也不太对。是的，我们有这个想法，把它做出来了，但我觉得重要的一点，或者说我学到的惨痛教训是：我的联合创始人在做产品，而我只是在设法让一些有意思的潜在客户从我们这里买单。

[06:01] **SPEAKER_00:** And so I got about 15 sort of series B, C, D sales leaders queued up saying they wanted to use this. Well, they said they wanted to use it. We got the first version done in a couple of weeks, send them the link to create an account of the 15, 14 of them didn't even click the link, one clicked the link and then didn't create an account. And we're like, it was like a first good, we should have read the mum test, we hadn't done any of the user interviews correctly.

> 于是我大概排了 15 位来自 B 轮、C 轮、D 轮公司的销售主管，都说想用这个产品。好吧，他们说想用。我们几周内做出了第一个版本，把创建账户的链接发给他们，结果这 15 个人里有 14 个连链接都没点，有一个点了链接但没有创建账户。我们当时就想，这本该是个不错的开端，我们本应该读读《妈妈测试》（The Mom Test）这本书，我们的用户访谈一个都没做对。

[06:26] **SPEAKER_00:** But also, it made me feel that building for sales. Building for sales people, or sales leaders in particular, I feel the signal to noise ratio is pretty poor, because they're really quite willing to hop on quick calls, and are very, very positive and kind of very friendly people. A little bit later, it kind of dawned on us that we think we'd be better, because we're not very good at product, we're terrible at product initially, because we're kind of bad, we need to deal with people that are what they say is close to what they'll do. And we felt that like natural problem solver people like engineers or customer support people probably would be a better audience for us to work with.

> 但这也让我觉得，为销售人员做产品——尤其是为销售主管做产品——信噪比相当差，因为他们非常愿意随时接个电话，而且非常非常积极、相当友好。稍晚一点，我们才慢慢意识到，我们觉得如果面向那种"说到就能做到"的人会更好，因为我们不太擅长做产品——起初我们做产品很糟糕——正因为我们做得不好，我们需要打交道的人是那种言行比较一致的人。我们觉得像工程师或客户支持人员这样天生就爱解决问题的人，大概会是更适合我们合作的受众。

[06:57] **SPEAKER_00:** Because out of all the many variables you can get wrong, like it might be like, oh, your product's incredible, but you're terrible at explaining what it does, you'll still fail. And we thought that, okay, that one of the variables we can remove from this equation is the person being a little bit easier to read, basically. And so that was a big part of why we wanted to build something DevTool-y later on, was that sort of realization. But yeah, that was the first thing that we worked on.

> 因为在你可能搞砸的众多变量中，比如说，哦，你的产品很棒，但你不擅长解释它是干什么的，你照样会失败。我们想，好吧，我们能从这个等式里去掉的一个变量，就是让打交道的人更容易读懂、更好判断。所以这也是后来我们想做偏开发者工具方向产品的一个重要原因，就是源于这种领悟。总之，那就是我们做的第一个东西。

[07:20] **SPEAKER_01:** And so when you guys did Y Combinator, the product that you had was another pivot, was having developers take surveys about technical data. When they would submit a pull request. And so you'd already done a few products by that point. You came into YC with another one.

> 所以你们进 Y Combinator 时，手上的产品又是一次转型，是让开发者填写关于技术数据的调查问卷——在他们提交拉取请求（pull request）的时候。所以到那时你们已经做了好几款产品了。你们进 YC 时又带着一个新的。

[07:36] **SPEAKER_01:** How did you kind of keep your spirits up? Or how did you track your trajectory? Did you feel you were getting stronger or better or closer to the target as you were going through these pivots?

> 你们是怎么保持士气的？或者说你们怎么追踪自己的进展轨迹？在经历这些转型的过程中，你有没有感觉自己变得更强、更好，或者离目标更近了？

[07:45] **SPEAKER_00:** I would like to think that was true. I'm not sure it was. We didn't reflect on that. We should have asked, like, are we actually getting better each time around?

> 我很想认为是这样。但我不确定真是这样。我们没有反思过这一点。我们本应该问一问：我们真的每一轮都在变得更好吗？

[07:51] **SPEAKER_00:** I think we should run a retrospective, basically. I don't think we actually were getting that much better each time. There are definitely some things that were consistently better. Yeah.

> 我觉得我们本该做个复盘。我并不认为我们每次真的进步了多少。当然肯定有一些方面是一贯做得更好的。是的。

[07:57] **SPEAKER_00:** That's very important to us, though. For example, we went full gas on each idea. We didn't sort of call it in. We would go in person to every single customer that was remotely interested, we would go in person to go meet.

> 不过那对我们来说非常重要。比如说，我们对每个想法都全力以赴。我们不会敷衍了事。只要有一丝一毫感兴趣的客户，我们都会亲自上门去见。

[08:08] **SPEAKER_00:** We started in England, then came to San Francisco to do YC. We'd catch a bunch of trains and buses to get to a customer in some random place. We would put the effort in to go really push it. Because then kind of what happens when we started charging for all of these products, you would find that, oh, I'm not failing this because I don't have a relationship.

> 我们从英国起步，然后来到旧金山做 YC。我们会换乘一堆火车和公交车，去某个偏僻的地方见客户。我们会投入精力去真正推进它。因为后来当我们开始为这些产品收费时，你会发现，哦，我失败并不是因为我和客户没有建立关系。

[08:25] **SPEAKER_00:** I'm kind of friendly with this customer at this point. And they still don't want to buy from us. This is a really good sign. This product isn't solving the problem.

> 到这个时候我和这位客户关系还挺好的。而他们仍然不想从我们这里买。这其实是个很好的信号。说明这个产品并没有真正解决问题。

[08:31] **SPEAKER_00:** This really demonstrates to me it's nice to have. My previous job, we used to sell enterprise software for millions of dollars a year. And I can remember multiple times thinking, I'm having to work kind of as hard to sell a $50 a month SaaS subscription as I was to sell a $100,000 a year plus deal in my last job. I know that I've tried really hard.

> 这真正向我证明了这个产品只是"可有可无"。我上一份工作是卖企业级软件，一年能卖几百万美元。我记得好多次都在想，我卖一个每月 50 美元的 SaaS 订阅所要付出的努力，几乎和我上一份工作卖一个一年 10 万美元以上的单子一样多。我很清楚我已经非常努力了。

[08:51] **SPEAKER_00:** And so I can rule out one of the other variables, I guess, is are you actually trying as hard as you could be? And we were. And that helped us feel confident enough to go, this just isn't working. So yeah, we worked very hard.

> 所以我想我可以排除掉另一个变量，那就是：你是不是真的已经尽了最大努力？而我们确实尽力了。这让我们有足够的信心去判断：这个方向就是行不通。所以，是的，我们非常努力。

[09:00] **SPEAKER_00:** And I can remember it feeling weird. Like on LinkedIn, for example, I would talk about like, hey, this is what we're up to. And it would be like one week it was like some dev tool, the next week it's a CRM thing. But we just didn't care.

> 我记得那种感觉很怪。比如在 LinkedIn 上，我会说，嘿，这就是我们在做的事情。结果这周还是某个开发者工具，下周就变成 CRM 之类的东西了。但我们根本不在乎。

[09:11] **SPEAKER_00:** We just threw ourselves into each problem. There's an aspect of shamelessness that you have to have to just kind of keep up the momentum and keep trying and not get bogged down. I think it's easy to feel kind of lame almost. Like you have friends who are in investment banking or they have these like proper careers and we're doing something.

> 我们只是全身心地投入到每一个问题里。要维持住那股势头、不断尝试、不被困住，你必须得有一种"厚脸皮"的成分。我觉得这很容易让人感觉自己有点逊。比如你有些朋友在投资银行工作，或者有那种体面的职业，而我们在做的这些事情——

[09:26] **SPEAKER_00:** It's kind of kooky, but like that's the bit. I think that is a specific reason why most people don't run companies because that first bit is like all is so existential and all over the place. I think we just have faith that if we just keep making the input we're looking at is like, are we making very regular, real progress? So one of the ideas we'd often at the start of the week be like, okay, by the end of this week, what is the list of things we will feel good if we get them all done?

> 有点古怪，但那正是关键所在。我觉得这正是大多数人不去创办公司的一个具体原因，因为最初那个阶段一切都充满了存亡攸关的焦虑，而且乱七八糟、毫无头绪。我觉得我们只是抱有一种信念：只要我们持续投入，我们关注的指标就是——我们是不是在非常有规律地取得真实的进展？所以我们经常在每周开始时定一个目标：好，到本周末，如果我们能全部完成，会让我们感觉良好的事情清单是什么？

[09:47] **SPEAKER_00:** And it will be something like, okay, we want to do like 10 customer meetings, build these three big features. And we just held ourselves to account on a like very short cadence all the time. So as people, I think we got much stronger at things like product much later on once PostDog had sort of taken off. But I think we were just like very, we just, yeah, put our heart into things, we're very fast.

> 清单大概会是这样的：好，我们要开 10 次客户会议、做出这三个大功能。我们一直以非常短的节奏来对自己问责。所以就个人成长而言，我觉得我们在诸如产品这类能力上变强，是很久以后 PostHog 有点起飞之后的事了。但我觉得我们当时就是非常……我们，是的，全心投入，而且速度非常快。

[10:06] **SPEAKER_00:** That was kind of what we needed, I think, realistically.

> 我觉得，现实地说，那正是我们当时所需要的。

[10:08] **SPEAKER_01:** You guys were working through these pivots, maybe getting better, maybe not, trying to be wholehearted, trying to be consistent, trying to be really committed to the bit, maybe as a comedian would say. When you started with the open source product analytics, what became the final pivot? What signals did you get early on or signs that maybe this is it, maybe we're really onto something? It was a month before YC Demo Day.

> 你们在经历这些转型，也许在进步，也许没有，努力做到全心全意，努力保持一贯，努力真正"入戏到底"——就像喜剧演员会说的那样。当你们开始做开源产品分析——也就是最终那次转型时——你们早期得到了什么信号，或者什么迹象让你觉得，也许就是它了，也许我们真的抓住了什么？那时距离 YC Demo Day 只有一个月。

[10:28] **SPEAKER_01:** Tell us a little bit about how that unfolded.

> 跟我们讲讲那是怎么展开的。

[10:30] **SPEAKER_00:** Yeah, so I think we had a slightly higher level of excitement about this idea ourselves. I think we had had a couple of ideas where in our heart of hearts, we weren't that interested in them. Like we were kind of doing them because we felt like we had to get something to work. Whereas I think this one, we had an office hours here and I can remember, and we're like, well, we're kind of thinking about building this thing that we'll do two, at the time we thought there were two things that were important.

> 是的，我觉得我们自己对这个想法的兴奋程度要稍微高一些。之前有几个想法，在内心深处我们其实并没有那么感兴趣。我们做它们有点像是因为觉得非得让什么东西成功不可。而这一个，我记得我们在这里参加了一次办公室答疑（office hours），我们说，嗯，我们在考虑做这么个东西，它要做两件事——当时我们觉得有两件事很重要。

[10:52] **SPEAKER_00:** We thought we want to capture all user data completely automatically. Like we don't want anyone to have something that doesn't work. Yeah. Yeah.

> 我们想要完全自动地捕获所有用户数据。就是说，我们不希望任何人拿到一个用不起来的东西。是的。是的。

[10:56] **SPEAKER_00:** We wanted to set up event tracking manually. We didn't even realize someone had already built this and that didn't turn out to be particularly important. But then the second thing, we're like, we want to be able to self-host this thing so that it can stay in your infra. And we came out of the office hours going, ah, that's not the right framing.

> 我们原本想手动设置事件追踪。我们甚至没意识到已经有人做过这个了，而且事实证明这一点并不特别重要。但第二件事是，我们想让这个东西可以自托管，这样它就能留在你自己的基础设施里。我们从那次办公室答疑出来时想，啊，那个定位角度不对。

[11:09] **SPEAKER_00:** It's open source product analytics. Then it's not just about it being your infrastructure. It's also just like a whole vibe. I think immediately we were like, we feel very confident.

> 它其实是"开源产品分析"。这样一来，重点就不只是它在你自己的基础设施里，而是它自带的一整种气质、一整种调性。我觉得我们立刻就觉得，我们非常有信心。

[11:16] **SPEAKER_00:** I could see that really landing on Hacker News and my co-founder and I both read it and it just felt like the kind of thing you would see on the front page. So the level of excitement was a little bit higher for us. I do think it's a bad idea though. Sometimes when I see other founders, they're like, I'm waiting for an idea that I'm excited about.

> 我能想象到它在 Hacker News 上会真正引起反响，我和我的联合创始人都在读 Hacker News，这就是那种你会在首页上看到的东西。所以我们的兴奋程度要稍微高一些。不过我确实觉得那是个糟糕的想法。有时候我看到其他创始人，他们会说，我在等一个能让我兴奋的想法。

[11:31] **SPEAKER_00:** But I think the reality is for us, we had to just build a bunch of things to find the thing we're excited about. What we didn't do was sit cross-legged on the top of a mountain waiting for inspiration. So by trying a few things, we started going, this idea just doesn't feel good. But we know that because we have tried it.

> 但我觉得对我们来说，现实是我们必须先做出一堆东西，才能找到那个让我们兴奋的东西。我们没有做的，是盘腿坐在山顶上等待灵感。所以通过尝试几样东西，我们开始意识到，这个想法感觉就是不对劲。但我们之所以知道，正是因为我们真的试过了。

[11:45] **SPEAKER_01:** You had to find something in the middle of what people want and what you're excited about.

> 你必须在"人们想要什么"和"你对什么感到兴奋"这两者的交集中找到一个东西。

[11:49] **SPEAKER_00:** Yeah, exactly. And so I think doing stuff gives you much stronger, I think it's like a Brian Armstrong quote, but doing stuff gives you a much stronger signal and more information. And then I think when we started booking interviews, it was a little bit easier to get people to talk to us.

> 是的，正是如此。所以我觉得动手去做能给你强得多的——我记得这好像是 Brian Armstrong 说过的一句话——动手去做能给你强得多的信号和更多的信息。然后我觉得当我们开始约用户访谈时，让人们愿意跟我们聊也变得容易了一点。

[12:01] **SPEAKER_00:** But the big deal was on Hacker News when it was just on the front page and it wasn't the best ever. At the time, it was pretty good compared to what happened before. It was a good launch. You had a good Hacker News launch.

> 但真正重要的是在 Hacker News 上，当它登上首页的时候——虽然那并不是史上最佳。以当时来说，跟我们之前的经历相比已经相当不错了。那是一次不错的发布。你在 Hacker News 上有过一次成功的发布。

[12:10] **SPEAKER_00:** But if you look at it at like 2023, 2024, 2025 vintage Hacker News launches, it was very mediocre, but it was enough to get an initial audience.

> 但如果你拿它和 2023、2024、2025 年那批 Hacker News 发布相比，它其实很平庸，不过已经足以为我们带来最初的一批受众了。

[12:18] **SPEAKER_01:** I think because I go back to people's old demo day slides a lot of the times when helping batch founders figure out what they should say. So I pull up the post-talk slide every now and then. And I believe according to the slide, and I think it's true, it was the most upvoted DevTool Hacker News post of the year. So pretty good.

> 我觉得，因为我在帮当期批次的创始人琢磨他们该说什么时，经常会翻回去看别人以前的 Demo Day 幻灯片。所以我时不时会调出 PostHog 的那张幻灯片。我记得根据那张幻灯片——我觉得这是真的——它是那一年 Hacker News 上点赞最多的开发者工具帖子。所以相当不错。

[12:35] **SPEAKER_01:** I remember being in the office hour. You probably shared the idea with a bunch of people, but I remember the first time I heard it and it just made a lot of sense. There were a bunch of product analytics companies out there, but no one had really gone all the way to make this truly developer focused by going open source. And so it just sounded like something someone should try.

> 我记得当时在那次办公室答疑上。你大概跟很多人都分享过这个想法，但我记得我第一次听到它时，就觉得它非常有道理。当时市面上已经有一堆做产品分析的公司了，但没有人真正做到极致，通过开源把它做成真正以开发者为中心的产品。所以这听起来就是那种应该有人去尝试的东西。

[12:53] **SPEAKER_01:** And I wasn't that surprised that it hit. And the way it did and was really excited for you guys at the time. So okay, so you had this, you were starting to get some users, you had to go out and raise money for this thing at demo day, and you'd only been working on it for a few weeks at that point. What was that like?

> 所以它火了，我并不太意外。看到它以那样的方式火起来，我当时真为你们感到高兴。那么好，你们有了这个东西，开始有了一些用户，你们得在 Demo Day 上出去为它融资，而那时你们才做了这个产品几周而已。那是种什么感受？

[13:08] **SPEAKER_01:** How do you get your conviction up to go pitch investors about a product that's really only a month old at this point?

> 你怎么建立起足够的信念，去向投资人推介一个此时其实才诞生一个月的产品？

[13:13] **SPEAKER_00:** It was very mixed. At first, we felt really good, we're like, okay, it feels like we're gonna have this done in like two days or three days. Slam dunk. Yeah, I think we're coming in going like, yeah, we've had a really solid launch.

> 感受非常复杂。一开始我们感觉很好，我们想，好，感觉我们两三天就能搞定融资。十拿九稳。是的，我觉得我们进场时的心态是，嗯，我们的发布相当成功。

[13:23] **SPEAKER_00:** I think we were still buzzing a little bit after like, oh, it's such a feeling of kind of relief that suddenly we've got something where I just instantly the day we launched, it went from being a push basis to a pull basis, getting people interested, like something it's just like, we're trying to service all these random problems and feature requests and stuff we can see coming in. And so we went out to raise, I think, very confident, like we thought we'd kind of be pushing quite a big valuation at the time. And I think we felt that we will have this done in just a few days, that the timing was horrible because it was 2020 in March. And the same week, basically, COVID went from being this somewhat niche thing.

> 我觉得我们当时还有点亢奋，那种感觉像是终于松了一口气，因为我们突然有了一样东西——就在我们发布的那天，它立刻从"推着别人来用"转变成了"别人主动来找我们用"，人们对它产生了兴趣，我们忙着去应付这些各式各样的问题、功能请求，以及我们能看到不断涌进来的各种需求。所以我们出去融资时，我觉得非常有信心，当时我们觉得我们大概能争取到相当高的估值。我觉得我们以为几天内就能搞定，但时机糟透了，因为那是 2020 年 3 月。基本上就在同一周，新冠疫情从一件还算小众的事情——

[13:56] **SPEAKER_00:** To changing the world, and everyone just suddenly pulled out. So we kind of went from feeling like, oh, we've got like all the fanciest VC firms in the world are interested in this thing to everyone's pulled out. And we're now doing like, we're trying to get angel checks for 5000 bucks a pop to try and get all the way up to like raising a few million dollars, and this is gonna take a long time. So it was very peaky.

> ——一下子变成了改变整个世界的事，所有人突然都撤了。所以我们从那种感觉——哦，全世界最顶尖的风投公司都对这个东西感兴趣——一下子变成了所有人都撤资。而我们现在只能这样：设法一张一张地拿到每笔 5000 美元的天使支票，一点点凑，一直凑到融资几百万美元，而这要花很长时间。所以那个过程起伏非常大。

[14:17] **SPEAKER_00:** We also had a lot of stress over like, we're in the US still, my wife was at home and pregnant, and I was worried about getting stuck in America. And my co founder left. And because he was also worried about getting stranded over his thing, his visa and stuff. So there's just all this chaos kind of happening.

> 我们当时还有很多压力，比如我们还在美国，我太太怀着孕在家，我担心自己被困在美国。我的联合创始人离开了。因为他也担心因为签证之类的问题被滞留。所以就是各种混乱同时发生。

[14:31] **SPEAKER_00:** We just kept plugging away, basically. I think it was very easy to it would be very easy, I think, to get disheartened. And it was painful. But we just didn't, I guess we just kept going, was the main thing.

> 我们基本上就是一直埋头苦干。我觉得当时很容易——我觉得当时很容易心灰意冷。那段日子很痛苦。但我们就是没有放弃，我想主要就是我们一直坚持了下去。

[14:40] **SPEAKER_00:** And so we were doing angel checks, happily taking 5k off of people until eventually we got a proper term sheet, and that led to another one, and then we got the round done very quickly. And then the market completely picked up. Right. And just a few months later, I ended up doing like a series A like a month after the seed round had closed.

> 所以我们就一直在拿天使支票，乐呵呵地从别人那里收 5000 美元，直到最终我们拿到了一份正式的投资条款清单（term sheet），接着又引来了另一份，然后我们很快就完成了这一轮融资。之后市场完全回暖了。是的。就在几个月后，我在种子轮结束大约一个月后就完成了 A 轮融资。

[15:00] **SPEAKER_00:** But I think the statistics are something like, I think we met 160 different firms in the seed round. I think for like, if I added up the total number of people, number of firms I've met for the series A, B, C, D, and E, for like 20 in total, like 30 in total, is by far the hardest round we had to raise. But also we sucked at, it's not just the market, like we sucked at pitching, we're trying to people please, I think too much. So we would be like, well, they'd be like, what are you gonna do with the money?

> 但我记得数据大概是这样：种子轮我们见了 160 家不同的机构。如果我把 A、B、C、D、E 各轮加起来见过的机构总数，大概总共也就 20 家、30 家。种子轮是我们迄今为止最难融的一轮。但另外，我们自己也很烂——不只是市场的问题，我们推介得也很烂，我们太想讨好别人了。所以场面会是这样，他们问：你们拿到钱打算做什么？

[15:27] **SPEAKER_00:** And it's like, well, you know, we'll like kind of get some revenue, we'll build some features. It's just very vanilla feeling. We had a lot of people rejecting us because they felt we were too early. But the reality was, it's like what we're dealing with, a lot of these investors have never invested at that time and never invested in open source at all, like the vast majority hadn't because it was quite, it was much more unusual then.

> 我们就答，嗯，你知道的，我们会做出一些收入，会做一些功能。感觉非常平淡无奇、毫无亮点。很多人拒绝我们，因为他们觉得我们太早期了。但现实情况是，我们当时打交道的很多投资人，那时压根就没投过开源项目，绝大多数都没投过，因为那时候投开源要罕见得多。

[15:45] **SPEAKER_00:** And I started realizing that I don't even believe that we'd want to spend money across all these areas. Like we actually just want to go all in on the open source project for a while. Again, I think that's very bad advice for something. Yeah.

> 我开始意识到，我自己甚至都不相信我们会想把钱花在所有这些领域上。其实我们只是想在一段时间里全力押注在这个开源项目上。同样，我觉得这作为一条普适建议是很糟糕的。是的。

[15:54] **SPEAKER_00:** Yeah. I mean, it's not something that doesn't have competition that's making lots of revenue. So you have to be very careful with something like that. But we started getting much more opinionated and that's where we started, that eventually landing.

> 是的。我是说，这可不是那种没有竞争、又能带来大量收入的东西。所以对这种事你必须非常小心。但我们开始变得更有主见，也正是从那时起，这一点最终开始奏效。

[16:03] **SPEAKER_00:** So, hey, like you're out of your mind if you think we're going to go big on like hiring a big sales team or trying to go into the enterprise or something, like it's just about building this like nice big inbound kind of community. We think is the, if we can't do that, nothing else will follow and we need to really establish that property. So yeah, we got much punchier. It's funny how that is.

> 所以我们会说，嘿，你要是觉得我们会大手笔招一个庞大的销售团队、或者要进军企业市场之类的，那你就是疯了。我们要做的就是打造一个漂亮而庞大的、以自然流入为主的社区。我们认为如果做不到这一点，其他任何事情都无从谈起，我们必须真正把这个基础建立起来。所以，是的，我们变得强硬有力多了。有意思的是——

[16:18] **SPEAKER_01:** It's almost like investors are pretty agnostic on what the plan is. So long as there's a plan. Yeah. Yeah.

> 这几乎就像是，投资人对于计划具体是什么其实并不太在意。只要你有一个计划就行。是的。是的。

[16:25] **SPEAKER_01:** You've thought about it and you've thought about it and you're ready to go execute on it.

> 你反复思考过它，你已经准备好去执行了。

[16:27] **SPEAKER_00:** I think there's a Mark Benioff quote, which is something like, it's better to be different than right. I think that it's almost equivalent here where I think it's, if you're trying to raise money, it's better to have a plan than it is to necessarily be like somewhat correct, like be either very clearly right or wrong, because you'll learn something from that.

> 我记得 Mark Benioff 有句话，大意是"与众不同胜过正确"。我觉得这里几乎是等价的：如果你在融资，有一个计划要好过一定程度上正确，也就是说，要么明确地对、要么明确地错，因为那样你都能从中学到东西。

[16:44] **SPEAKER_01:** So that round was really hard. You talked to 160 investors, it took months to get the money? Yeah. Okay.

> 所以那一轮真的很艰难。你跟 160 位投资人谈过，花了好几个月才拿到钱？是的。好的。

[16:52] **SPEAKER_01:** Fast forward to this latest round that you guys just raised. Obviously it's five years later. Things are very different. The company's in a very different place.

> 快进到你们刚刚完成的这最新一轮。显然这已经是五年后了。情况大不相同。公司所处的位置也非常不一样了。

[16:57] **SPEAKER_01:** You have revenue and customers. What's it like to raise a $75 million round? How is that relatable to folks that maybe are out there trying to raise the first money for their company? What's that experience like?

> 你们有收入、有客户了。完成一轮 7500 万美元的融资是种什么感觉？这对于那些也许正在为自己公司募集第一笔资金的人来说，有什么可借鉴之处？那是种怎样的体验？

[17:09] **SPEAKER_00:** Yeah. Perversity is easier. We spoke to one investor for this round. We raised from Pete15.

> 是的。说来讽刺，这次反而更容易。这一轮我们只跟一位投资人谈过。我们是从 Pete15（此处指某风投机构）那里融的。

[17:14] **SPEAKER_00:** There's someone called Shalendra that is the main partner, but also Arnav is involved as well. The round before he tried to take part in, we only had just gotten to know him though. So we kind of felt like we wanted to spend a bit of time with him. Yeah.

> 有一位叫 Shalendra 的人是主要合伙人，另外 Arnav 也有参与。上一轮他曾想参与，但那时我们才刚认识他。所以我们当时觉得想跟他多相处一段时间。是的。

[17:24] **SPEAKER_00:** We wanted to spend a bit longer with you before we raised with you basically. We did spend a little bit more time with him because we liked him as a person. They offered to do the next round preemptively and at first we thought it was a bad idea because we just felt we don't know how we would spend this. We haven't spent like the round before the round before almost, but then at the same time what was starting to happen was we were getting increasingly confident on AI.

> 基本上就是，我们想在接受你投资之前跟你多相处一阵子。我们确实跟他多花了点时间，因为我们喜欢他这个人。他们主动提出要提前把下一轮做了，起初我们觉得这不是个好主意，因为我们只是觉得我们不知道该怎么花这笔钱。我们几乎连上上一轮的钱都还没花完，但与此同时，开始发生的情况是，我们对 AI 越来越有信心了。

[17:48] **SPEAKER_00:** What actually happened was I went on vacation and read about some of the motives for why some of the co-founders built OpenAI in the first place and I thought the reasoning was really interesting. It was humans have a brain, it's a physical object. We can therefore build one basically. There's no technical reason we can't build ADI essentially.

> 实际发生的情况是，我去度假时读到了一些资料，讲 OpenAI 的一些联合创始人当初创建它的动机，我觉得那套推理非常有意思。大意是：人类有大脑，它是一个物理实体。因此我们基本上就能造出一个。本质上没有任何技术上的理由说明我们造不出通用人工智能。

[18:07] **SPEAKER_00:** Then I just, and this is nerdy reading, but I started thinking like what are the specific differences between your brain and LMs today and I concluded there's a lot of things that could be built that I don't understand why they don't exist yet. So I therefore think that AI will, I don't think it will flatten out. I think the rate of improvement may vary, but I think over a long timeframe, it will be incredibly important to the world. So I got much more bullish on its importance and then thinking at work, I'm like, okay, I can definitely see a path.

> 然后我就——这属于很技术宅的阅读——但我开始思考，你的大脑和如今的大语言模型之间具体有哪些差异，我得出的结论是，有很多东西是可以被构建出来的，我不明白为什么它们还不存在。所以我因此认为 AI 不会趋于平缓、停滞不前。我觉得改进的速度可能会有波动，但在很长的时间跨度里，它对这个世界将会极其重要。所以我对它的重要性变得看多得多，然后回到工作上思考，我想，好，我完全能看到一条路径。

[18:33] **SPEAKER_00:** I just spent some time reflecting with my go round. I'm like, okay, how could this shake out basically? Should we change our strategy if we both believe this is this important? So at the time we were thinking about building like a CRM, a support platform, all kinds of other customer data oriented products and everything was kind of working, but we felt actually we can do so much more in the realm of product at first.

> 我花了些时间和我的联合创始人一起反思。我想，好，这大概会怎么发展？如果我们俩都相信这件事这么重要，那我们是不是该改变策略？当时我们在考虑做类似 CRM、客服支持平台，以及各种其他以客户数据为核心的产品，而且一切都算是在奏效，但我们觉得其实我们首先在产品这个领域可以做的还多得多。

[18:52] **SPEAKER_00:** We can build kind of product autonomy out. So we want to go deeper within our products that help you understand what to build. So we wanted to work on, like at the moment we're working on a desktop app, for example, that ships pull requests based on your customer data. So we'll look across all your session recordings, all your analytics, all your error tracking, your LM traces, go, hey, these are the issues we can see in your customer base.

> 我们可以构建出某种"产品自主性"。所以我们想在那些帮助你理解该构建什么的产品里做得更深。举例来说，我们目前正在做一个桌面应用，它能根据你的客户数据直接提交拉取请求。我们会通盘查看你所有的会话录制、所有的分析数据、所有的错误追踪、你的大语言模型调用轨迹，然后说，嘿，这些就是我们在你客户群里能看到的问题。

[19:12] **SPEAKER_00:** We've literally fixed them whilst you're asleep. Here are the pull requests. So instead of like, please build me this feature, the flow is pull based. It's like, hey, we've built these features based on what's happening.

> 我们真的趁你睡觉的时候就把它们修好了。这些就是拉取请求。所以流程不再是"请帮我做这个功能"，而是基于"拉取"的模式。就像是，嘿，我们已经根据实际情况做好了这些功能。

[19:23] **SPEAKER_00:** You can just review, close, edit. Yeah. Merge them depending on what you want to speed up development further. And we just were like, hey, let's just go.

> 你只需要审阅、关闭、编辑就行。是的。根据你的需要把它们合并进去，从而进一步加快开发速度。我们当时就想，嘿，那就干吧。

[19:29] **SPEAKER_00:** We want to be able to go all in on this idea. And so we raised to have just like the comfort and the confidence, a lot of it's psychological. Like I don't think we'll manage to spend it, but we want, that's kind of the point. It's like, this means that we can just fully embrace our product strategy and take a bigger and just like increase the size of swing that we're taking.

> 我们想能够全力押注在这个想法上。所以我们融资就是为了那份从容和信心，其中很大一部分是心理层面的。我并不觉得我们会把这笔钱花完，但我们想要它，这恰恰是关键所在。它意味着我们可以完全拥抱我们的产品策略，出更大的一击，把我们挥棒的幅度加大。

[19:47] **SPEAKER_01:** Well, and it sounds like what you're saying is you're able to fully explore the implications of the original idea of post-hoc, which is understand what's happening in your product and what your users are up to. And there's all this stuff downstream of that. Like once you understand it, then you can do these things and take these actions.

> 嗯，听起来你说的是，你们现在能够充分地去探索 PostHog 最初那个想法所蕴含的全部意义，也就是理解你产品里正在发生什么、你的用户在做什么。而这背后有一连串下游的东西。一旦你理解了它，你就能做这些事、采取这些行动。

[20:01] **SPEAKER_00:** Yeah. Cause we started thinking like, okay, it's a bit like if you're trying to, if your customer is like a painting that you're trying to understand, if you have one data type, it's a bit like seeing a painting, but only being able to see the color blue. You're not going to get a nuanced understanding of a customer. Like it looks like they're not using this feature.

> 是的。因为我们开始这样想，好，这有点像——如果你的客户就像一幅你想要读懂的画，而你只有一种数据类型，那就有点像看一幅画却只能看到蓝色。你没法对一位客户获得细致入微的理解。比如看起来他们没在用这个功能。

[20:14] **SPEAKER_00:** We should email them to cross sell them the new feature we've just built. But at the same time, your other data might be telling you something conflicting. Like they're really pissed off in support right now. And this is a terrible time to automatically send them an email or something.

> 我们应该给他们发邮件，向他们交叉销售我们刚做好的新功能。但与此同时，你的另一些数据可能在告诉你一些相互矛盾的信息。比如他们此刻正在客服那边气得不行。而这个时候自动给他们发邮件之类的，是个糟糕透顶的时机。

[20:24] **SPEAKER_00:** So we kind of felt like, and that's what a human would do today is you kind of look across your tools and we thought, oh, we can basically just build something that does this. And so we set off trying to build basically a product manager. That's a physical thing. We can build it.

> 所以我们有点觉得——今天一个人类会做的就是把各种工具通盘看一遍——于是我们想，哦，我们基本上可以做一个能干这件事的东西。所以我们出发去做的，基本上就是一个产品经理。那是个实体存在的东西。我们能造出来。

[20:36] **SPEAKER_00:** Yeah. We don't want to build something that has like, that we can't conceive of. We want to build something that exists, but just like a better version. And we're like, well, there's a human product manager, has product market fit, like companies buy those.

> 是的。我们不想去做那种我们连想都想象不出来的东西。我们想做的是一个已经存在、但只是更好版本的东西。我们想，嗯，人类产品经理是有产品市场契合度的，公司都会"购买"这个岗位。

[20:45] **SPEAKER_00:** That is sort of where the idea came from. And so instead of just building, cause normally our strategy had been, what are the products have product market fit that have customer data. We will build all of them. It's more convenient.

> 这个想法大致就是这么来的。所以我们不再只是——因为通常我们的策略一直是：哪些涉及客户数据的产品是有产品市场契合度的，我们就把它们全都做出来，这样更方便。

[20:53] **SPEAKER_00:** I'm just like, well, also like you could consider the team members and thinking about sales has product market fit and companies, so does support, so does engineering. So can we build those things now? Because it's now possible. And I think it's going to be correct that that works, but we will see.

> 我就想，嗯，其实你还可以把团队成员也考虑进来——想一想，销售这个岗位是有产品市场契合度的，公司会为之付费，客服也是，工程也是。那我们现在能把这些东西造出来吗？因为现在有可能实现了。我觉得这最终会被证明是行得通的，但我们拭目以待。

[21:06] **SPEAKER_01:** All right. All right. You mentioned to me before we started talking today that you're, this is like unexpectedly, maybe you're having more fun than at any other point in the company so far. And that is a little counterintuitive to people.

> 好的。好的。我们今天开始录之前你跟我提到，出乎意料地，也许你现在比公司创立以来的任何时候都更享受、更快乐。这对很多人来说有点反直觉。

[21:19] **SPEAKER_01:** A lot of founders say, oh, the early days are the most fun and they kind of look back nostalgically.

> 很多创始人会说，哦，早期的日子最有意思，然后带着怀旧之情回望那段时光。

[21:24] **SPEAKER_00:** Why do you think you're having more fun now than ever before? The work feels much more leveraged now, which is quite entertaining. I think before you're so much of our focus was trying to get attention from people because you have no attention by default. It's the world is very noisy.

> 你觉得为什么你现在比以往任何时候都更享受？现在的工作感觉杠杆效应大得多，这挺有意思的。我觉得以前我们太多的精力都花在试图从人们那里获取关注上，因为默认情况下你根本没有任何关注度。这个世界非常嘈杂。

[21:38] **SPEAKER_00:** And so I'm just like sending emails and LinkedIn messages into the ether basically. And it just feels like I'm doing awful stuff that has no impact. Obviously when you do have like a tiny little spark, it then needs to be fire. Whereas now it feels like we're playing computer game.

> 所以我基本上就是把邮件和 LinkedIn 消息发进虚空里。感觉就像在做一些糟糕透顶、毫无效果的事情。显然，当你真的燃起了一点小小的火花，接下来它需要变成一团火。而现在，感觉就像我们在玩电脑游戏。

[21:50] **SPEAKER_00:** We've just unlocked like rocket launchers or something. Okay. And so it's like, oh, we can like go absolutely nuclear on this particular idea and like really fully build it out in a way that would be very hard to, we're like lucky enough to be able to build this because it involves having to have like 15 or 16 products and also a bunch of AI stuff. And we need to be able to like have the time to build this because like there's been remarkable work at like Intercom where they built Finn.

> 我们刚刚解锁了类似火箭发射器之类的东西。好的。所以感觉就是，哦，我们可以在这个特定的想法上火力全开、彻底把它做出来，而这种做法本来是非常难以实现的——我们很幸运能够构建这个，因为它需要拥有大约 15 或 16 款产品，外加一堆 AI 相关的东西。而我们需要能有时间来构建它，因为像 Intercom 就做出过很了不起的成果，他们做了 Finn。

[22:14] **SPEAKER_00:** And what we're trying to do is analogous to that, I think, but it's not making post-doc work with kind of what a couple of products is trying to make it work across like 16 of them. We're going much deeper than we've ever been, but it's enabled us to make a bet like that. Like I think similarly, if we were starting from scratch, trying to build what we're now trying to build would be probably impossible. I think like SpaceX or something is a much more grandiose idea.

> 我觉得我们想做的事情和那个类似，但不是让 PostHog 在两三款产品上跑通，而是要让它在大约 16 款产品上跑通。我们做得比以往任何时候都要深，但正是这一点让我们有能力下这样一个赌注。我觉得同样地，如果我们是从零开始，想要构建我们现在试图构建的东西，大概是不可能的。我觉得像 SpaceX 之类的是一个宏大得多的想法。

[22:37] **SPEAKER_00:** Like on day one, it's not building like the transportation from ours. It's like day one's like we need to build actually relatively unambitious satellite launching business. I think we've been, we've sort of done quite a lot of the homework that means we're able to now do these, take the bigger test basically.

> 比如第一天，他们并不是去建造星际运输系统。第一天更像是：我们其实需要先建立一个相对而言不那么雄心勃勃的卫星发射业务。我觉得我们已经把相当多的功课都做好了，这意味着我们现在有能力去做这些事、去接受更大的考验。

[22:51] **SPEAKER_01:** Yeah. I think that's one of the products post-hoc would need to have to be as grandiose as ambitious as SpaceX. Yeah. It's an interesting comparison.

> 是的。我觉得那是 PostHog 想要像 SpaceX 那样宏大、那样有野心所需要的产品之一。是的。这个类比很有意思。

[23:00] **SPEAKER_01:** You know, you mentioned like having fun, getting this work out there. Like I know building in public is something that you're keen on. What does that look like as a CEO is getting this attention, getting that spark and putting it out there and trying to start a fire. How do you think about that and doing it in the open where people can see what you're up to and hear about it and follow along?

> 你知道，你提到享受其中、把这些成果推出去。我知道"公开构建"（building in public）是你很热衷的事情。作为 CEO，去获取这份关注、去点燃那个火花、把它推出去并试图燎原，这个过程是什么样子的？你是怎么看待这件事的，以及怎么在公开的场合去做——让人们能看到你在做什么、听说它、并一路追随？

[23:18] **SPEAKER_00:** Trust was the original reason for it. Like we just felt that even if you're offering, like as most of our users don't trust us, like we just felt that even if you're offering, like as most of our users don't trust us, like we just felt that even if we're offering, like as most of our users don't trust us, we don't pay anything. Like when you're the open-source project, no one paid, but it still takes up, there is a cost. Like it's trust in terms of what are they doing with my data and also just time with setting this tool up.

> 信任是我们这么做最初的原因。我们只是觉得，即便你提供的东西……因为我们大多数用户并不信任我们……我们只是觉得，哪怕东西是免费的、用户不用付任何钱——就像当你是一个开源项目时，没有人付费，但它仍然是有成本的、有代价的。这里的代价是信任，涉及"他们拿我的数据在做什么"，也包括搭建这个工具所花的时间。

[23:31] **SPEAKER_00:** I think especially as software is getting more, like as it's getting quicker to build, there's more software appearing. It's getting just more and more competitive. I think it's become a step change, more competitive with AI. And so we felt that, okay, the fundamental thing we have to achieve in marketing is we need to highlight how we're different because it's in a busy industry.

> 我觉得尤其是随着软件变得越来越……随着构建软件的速度越来越快，出现的软件越来越多。竞争变得越来越激烈。我觉得有了 AI 之后，竞争激烈程度发生了阶跃式的变化。所以我们觉得，好，我们在市场营销上必须实现的根本一点，就是要突出我们与众不同之处，因为这是一个非常拥挤的行业。

[23:46] **SPEAKER_00:** And then we need to build trust with users and like the foundation of trust we felt was transparency. Instead of just having like a one-pager landing page, we're going to like really fully explain everything we can about who we are, what we're trying to do. I think that gave us the trust we needed. And we thought about kind of, I looked through other Hacker News launches and just sort of summarize like, okay, these are all the pieces of critique I can see.

> 然后我们需要和用户建立信任，而我们觉得信任的基础是透明。我们不搞那种只有一页的落地页，而是要尽我们所能，把我们是谁、我们想做什么，全都真正彻底地讲清楚。我觉得那给了我们所需要的信任。我们还思考了——我把其他 Hacker News 发布帖都翻了一遍，做了个总结：好，这些就是我能看到的各种批评。

[24:07] **SPEAKER_00:** And so we're going to make sure we have transparent answers to these types of, the questions would be things like, they don't have a clear business model. I don't think this is sustainable. For example, there's like this sort of inherent suspicion of ideas. And we thought, okay, let's just like think through these types of questions that we know that our audience developed.

> 所以我们要确保对这些类型的问题都有透明的回答，这些问题会是诸如：他们没有清晰的商业模式；我觉得这不可持续。举例来说，人们对新想法有一种天生的怀疑。我们就想，好，我们干脆把这些我们知道我们的受众——开发者——会有的问题都想清楚。

[24:21] **SPEAKER_00:** Developers would have. And we'll just address them on the website. So we like, you know, we didn't have a pay product. We said, hey, this is how we think the pay product is going to work in future.

> ——开发者会有的这些问题，我们就直接在网站上一一回应。所以，你知道，当时我们还没有付费产品，我们就说，嘿，我们认为未来付费产品会是这样运作的。

[24:27] **SPEAKER_01:** And that was from like day zero. You put some of those things in.

> 而且那是从第零天就开始的。你们把其中一些内容就放进去了。

[24:30] **SPEAKER_00:** Yeah. Like before we launched Hacker News. I think the other thing we realized from a content and like a marketing perspective was I think experts writing about things is more compelling often than non-experts. And if you look at like the front page of Hacker News, there'll be like incredibly technically savvy people talking about very complicated topics quite often.

> 是的。在我们发布到 Hacker News 之前就放进去了。我觉得从内容和营销的角度，我们意识到的另一件事是：专家来写东西，往往比非专家更有说服力。如果你看看 Hacker News 的首页，经常会有技术极其精通的人在讨论非常复杂的话题。

[24:45] **SPEAKER_00:** And I thought, oh man, I'm like, I'm not clever enough to get there, but I need to figure out a way to get us visible in Hacker News. This is like the, probably the most popular place for our audience. And I thought, well, I am the thing I'm actually an expert in is our business. And so I can write about what we're learning and doing.

> 我就想，哦天哪，我没那么聪明，达不到那个水平，但我需要想办法让我们在 Hacker News 上被看到。这大概是我们受众最活跃的地方。然后我想，嗯，我真正称得上专家的东西，就是我们自己的业务。所以我可以写我们正在学到的和正在做的东西。

[24:59] **SPEAKER_00:** And so I feel like a really natural topic. So we, like we wrote a blog post also during the Vicey Badge, like shortly after the launch of what it's like moving San Francisco students. I remember that post. Yeah.

> 所以我觉得这是个非常自然的话题。于是我们——我们在 YC 批次期间还写了一篇博客文章，就在发布后不久，讲的是搬到旧金山当"学生"是种什么体验。我记得那篇文章。是的。

[25:08] **SPEAKER_00:** Again, that was also viral, but I think I built a lot of trust because it humanized us underneath. So I was like, put photos in of like, we climbed up like Twin Peaks, for example, in the night at night. I think people realize like, oh, there are human beings, you know, in the same way that someone might be really aggressive online. But as soon as you meet them in person, they're really aggressive.

> 那篇同样也火了，但我觉得它建立了很多信任，因为它在深层次上让我们显得有人情味。所以我就往里放照片，比如我们爬上双子峰（Twin Peaks），是在夜里爬的。我觉得人们会意识到，哦，原来他们是活生生的人，就好比有人在网上可能很咄咄逼人，但你一旦当面见到他们……（本该是变得随和，此处口误）。

[25:20] **SPEAKER_00:** And they're much more chill. Yeah. It's the same sort of feeling. And we're trying to make that clear.

> 而实际上他们随和多了。是的。就是那种感觉。我们就是想把这一点表达清楚。

[25:24] **SPEAKER_00:** Like with all our products today, you can see like the literal engineers that we have every single team member on the team pages. You can see all the, so you can look at like product analytics. You can see the handful of engineers building it. You can click their bio and read about like their pet cat, for example, so that you're like, oh, there are people building this.

> 比如如今我们所有的产品，你都能看到真真切切正在做它的工程师——每一个团队成员都列在团队页面上。你能看到所有的……所以你可以去看产品分析这块，你能看到正在做它的那几位工程师。你可以点开他们的个人简介，读到比如他们养的宠物猫，这样你就会想，哦，原来是有活生生的人在做这个东西。

[25:38] **SPEAKER_00:** The humanization I think is really important to stand out basically.

> 我觉得这种"人性化"对于脱颖而出基本上是非常重要的。

[25:40] **SPEAKER_01:** Yeah. It lets people know someone's at home. You go visit this house, there'll be someone there and you'll have a neat interaction. I actually, I think about your, your moving to San Francisco post quite often over the years since.

> 是的。它让人们知道"家里有人"。你去拜访这栋房子，里面会有人在，你会有一次愉快的互动。其实这些年来，我经常想起你那篇搬到旧金山的文章。

[25:50] **SPEAKER_01:** Because if you look at it, there's nothing that remarkable in the post, but you got it on Hacker News. People read it. They talked about it. It was discussed.

> 因为如果你去看它，那篇文章里其实没有什么特别了不起的内容，但你把它送上了 Hacker News。人们读了它。人们谈论它。它被拿出来讨论。

[26:00] **SPEAKER_01:** And I think you're right. It's because you just showed some of your humanity behind this product that people could use. And everyone's looking for ways to relate to folks like themselves. I remember when I read that, I thought, wow, they can, they can, you know, climb up Twin Peaks and write about it and get developers to want to check it out.

> 我觉得你说得对。正是因为你在这个人们可以使用的产品背后，展现出了一些你们身上的人性。而每个人都在寻找方式去和跟自己相似的人产生共鸣。我记得我读到那篇时想，哇，他们能够——你知道——爬上双子峰、把它写出来，还能让开发者产生想去看看这个产品的兴趣。

[26:16] **SPEAKER_01:** They've got, you know, this is going to go somewhere. Building in public. It's one of the ways that you guys have really connected with developers. I think another aspect of that though is, is humor and bringing a sense of like merriment, amusement, and maybe even a little chaos to how the post hog message gets across.

> 他们有这个本事，你知道，这个东西会有前途的。公开构建。这是你们真正与开发者建立联结的方式之一。但我觉得其中的另一个方面是幽默，是在传递 PostHog 信息的方式中带入一种欢乐、有趣、甚至可能有一点点混乱的感觉。

[26:34] **SPEAKER_01:** One of the manifestations of that was present all over San Francisco this last year with the crazy billboards that you guys put up. In my opinion, like there's billboards all over the city. When people move to San Francisco, they're shocked by all the tech ads everywhere on all the billboards. But I don't think I've seen anyone do quite what you guys did with your marketing.

> 这一点的一个体现，就是去年遍布整个旧金山的、你们投放的那些疯狂的广告牌。在我看来，整个城市到处都是广告牌。当人们搬到旧金山时，会被广告牌上无处不在的科技广告震惊到。但我觉得我还没见过有谁在营销上做到你们那样。

[26:53] **SPEAKER_01:** And so I thought it'd be really fun to just take a look at some of these together and get your take on what's going on here. So I guess this first one is about session replay ostensibly, but it's a also like an ad for tomato sauce and it's promoting the sweet taste of understanding. Where did you guys come up with this and what made you think to compare tomato sauce to session replay?

> 所以我觉得我们一起来看看其中一些广告，听听你对这些广告在搞什么名堂的说法，会很有意思。我想这第一张表面上是关于会话回放（session replay）的，但它同时又像是一则番茄酱广告，宣传的是"理解的甜美滋味"。你们是怎么想出这个的？是什么让你想到把番茄酱和会话回放做类比？

[27:14] **SPEAKER_00:** For example? There are a few things. I think kind of by design. We wanted it to.

> 举例来说？有几个原因。我觉得这在某种程度上是刻意为之的。我们就想让它——

[27:18] **SPEAKER_00:** Yeah. I think it's going to be different. So kind of our grand theory of billboards was how interesting your brand is. If your brand's normally here, everyone's a bit more interesting on billboards.

> 是的。我觉得它会与众不同。我们关于广告牌的一套宏大理论，是关于你的品牌有多有趣。如果你的品牌平时在这个位置，那么在广告牌上，每个品牌都会显得稍微更有趣一点。

[27:26] **SPEAKER_00:** Like if you just look at companies seem to come out of their shell a bit more on billboards than they do on their websites. Why do you think that is? I think they're trying to stand out basically. But I think it's a bit like, yeah, this is going to sound harsh, but I think it's a bit like watching like a first grader play football where they're going to dabble.

> 就是说，如果你观察一下，公司在广告牌上似乎比在自己网站上更放得开一些。你觉得那是为什么？我觉得基本上就是他们想脱颖而出。但我觉得这有点像——是的，这话听起来可能有点刻薄——但我觉得有点像看一个一年级小孩踢足球，他们会瞎折腾一下。

[27:41] **SPEAKER_00:** But like they're starting from basically being a first grader where it's like, well, we're already pretty weird online. So our billboards need to be bizarre. Like they need to be like totally out there. Yeah.

> 但他们基本上是从一年级小孩的水平起步的，而对我们来说是，嗯，我们在网上本来就已经相当古怪了。所以我们的广告牌需要更加离奇。它们需要彻底地天马行空、出人意料。是的。

[27:49] **SPEAKER_00:** They need to be out there. So we should like lean harder into this, which we think will work because the whole point is like it has to stand out in the environment and we need people to, we won't be able to talk about and see it. And we're not trying to get conversion. Like it's, you're unlikely to decide to install like our SDK whilst you're driving your car down the freeway.

> 它们需要够出格。所以我们应该在这方面更加发力，我们觉得这行得通，因为关键就在于它必须在环境中脱颖而出，我们需要人们去谈论它、注意到它。而我们并不是想获得转化。就是说，你不太可能在开车沿着高速公路行驶时决定去安装我们的 SDK。

[28:05] **SPEAKER_00:** Instead of trying to please everyone, we're not going to care about conversion. We are just going to try and raise awareness. And then the other thing I think that had struck us was from actually doing a bunch of social stuff where like, oh, I can like spend the time to write a useful post based on something we're learning. And that will work.

> 与其去讨好所有人，我们干脆不去在乎转化率。我们要做的只是提高知名度。然后我觉得另一件让我们印象深刻的事，来自我们实际做的很多社交媒体内容——就是，哦，我可以花时间写一篇有用的帖子，基于我们正在学到的东西。那是有效果的。

[28:19] **SPEAKER_00:** And it's going to do me well to get some, like if it's helpful, people will share it. But somewhat depressingly, if we write, like if I just write something I think is funny, it can sometimes go a thousand times further in terms of reach. So if I'm just trying to raise awareness, it has to be funny. And that's actually the primary thing we want to get across.

> 这会给我带来好处，如果它有用，人们就会转发它。但有点令人沮丧的是，如果我们写——如果我只是写点我觉得好笑的东西，它的传播范围有时能远上一千倍。所以如果我的目的只是提高知名度，那它就必须搞笑。而这其实正是我们最想传达的东西。

[28:36] **SPEAKER_00:** And so, yeah, we just really wanted to like crank as far as we could over on the like weirdness, slightly funny scale. It is a real skill. I think we've been trying very hard to, I think a lot of corporates or whatever do like corporate try hard. And it's very hard to not come up because you're obviously trying hard.

> 所以，是的，我们就是很想在"古怪、略带搞笑"这个刻度上尽可能地拉满。这是一门真本事。我觉得我们一直非常努力地去——我觉得很多大公司之类的会有那种"企业式的用力过猛"。而要做到不显得"你明显在硬凹"是非常难的。

[28:52] **SPEAKER_00:** Your stuff is almost a parody of corporate try hard. You've transcended corporate try hard. It's a very, like on Hacker News, for example, people talk about like on Hacker News, it's like trial by fire, basically, where there's unbelievable level of criticism. Our marketing channel in Slack is like that too, where people are like, your joke is just not funny.

> 你们的东西几乎是对"企业式用力过猛"的一种戏仿。你们已经超越了"企业式用力过猛"。这就很——比如在 Hacker News 上，人们说 Hacker News 基本上就是"火刑般的考验"，那里的批评严苛到令人难以置信。我们在 Slack 里的营销频道也是这样，大家会说，你这个笑话就是不好笑。

[29:08] **SPEAKER_00:** It has to be better. You look like you're trying. So we have a very heavy feedback culture in marketing.

> 得再好一点。你看起来太用力了。所以我们在营销团队里有一种非常浓厚的反馈文化。

[29:14] **SPEAKER_01:** Let's talk about that. So before a post-hoc tweet or billboard gets out into the wild, what is the incubation?

> 我们来聊聊这个。那么在一条 PostHog 的推文或一块广告牌真正投放出去之前，它的"孵化"过程是怎样的？

[29:22] **SPEAKER_00:** Yeah, it's a very small number of people will be involved, like probably like three or four. And it is a very high trust, direct place. And so we're really trying to get something that we think is genuinely, it might be sarcastic, but something that's genuinely funny to get onto a billboard or just something that would make us laugh or that we would want, we are kind of doing them for ourselves. Like, is it something I think would be quite funny to see?

> 是的，参与的人非常少，大概也就三四个人。而且那是一个高度信任、非常直接坦率的环境。所以我们真的是在努力做出一些我们认为是真正——它可能带点讽刺，但必须是真正好笑的东西，才能上广告牌，或者只是能让我们自己发笑、我们自己想要的东西，我们某种程度上是为自己做这些的。比如：这是不是我觉得看到会挺好笑的东西？

[29:45] **SPEAKER_00:** Yeah. It's sort of the bar. It feels like you're competing against B2B software because there's all these AI billboards that are quite similar to each other. But I think the reality is if you want people to pay attention, it's like, no, you're competing with what they're listening to on the radio or what they're doing on the phone or whatever else.

> 是的。这算是一条基准线。感觉上你好像在和 B2B 软件竞争，因为现在有一大堆彼此相当雷同的 AI 广告牌。但我觉得现实是，如果你想让人们真正留意，那不对，你是在和他们正在收音机里听的东西、或者在手机上做的事情、或者其他任何事情竞争。

[30:00] **SPEAKER_00:** And so the bar is so many times higher. And so it needs to be at least in that realm. It's not just about doing a slightly better, incrementally better job than other software companies. And which is impossible.

> 所以这条基准线要高出好多倍。所以它至少得达到那个层次。这不只是比其他软件公司做得稍微好一点、渐进地好一点那么简单。而那样（渐进地更好）是不可能奏效的。

[30:12] **SPEAKER_00:** I mean, no one near as interesting as Mr. Beast or something. The mentality is like, oh, I wish we need to be playing that game at least a bit more. We felt that we would make fun of adverts in general.

> 我是说，没有人能有 Mr. Beast 之类的人那么有意思。那种心态就是，哦，我希望我们至少能多玩玩那种玩法。我们觉得我们可以拿广告这件事本身来开玩笑。

[30:23] **SPEAKER_00:** And so we thought like, okay, we'll do like a very like Americana style ad, but we'll make it like it's like a 1950s thing, but for like AI software or whatever.

> 所以我们想，好，我们来做一个非常有美式复古风（Americana）的广告，但把它做成像是 1950 年代的那种东西，只不过卖的是 AI 软件之类的。

[30:31] **SPEAKER_01:** Right. So it tastes better than spaghetti. And you're done up here like the host of a 1950s food show talking about your B2B SaaS product. Okay.

> 对。所以广告词是"它比意大利面更美味"。而你打扮成 1950 年代美食节目主持人的样子，在那儿讲你的 B2B SaaS 产品。好的。

[30:44] **SPEAKER_01:** What about the 1950s Americana? Like what was the appeal there?

> 那 1950 年代的美式复古风呢？它的吸引力在哪里？

[30:47] **SPEAKER_00:** Yeah. I think if you sort of say like, what's the most stereotypical kind of billboard ad you could imagine? I think you sort of would imagine you would go back to like...

> 是的。我觉得如果你要问，你能想象到的最典型、最刻板印象的广告牌广告是什么样的？我觉得你大概会想象自己回到……

[30:53] **SPEAKER_00:** What's the origin of billboards? That's almost when you would look at them from a positive perspective. I think of like, oh, like back in the day ads were kind of cool. They're like funnier, better thought out.

> 广告牌的起源是什么？那几乎是你会从正面角度去看待广告牌的时代。我会想，哦，从前的广告还挺酷的。它们更幽默、更用心构思。

[31:00] **SPEAKER_00:** Whereas now they've just got a bit...

> 而现在它们变得有点……

[31:01] **SPEAKER_01:** Death to humans.

> "人类灭亡"（那种冷冰冰、令人生畏的调调）。

[31:02] **SPEAKER_00:** Yeah. Yeah. Or it's just like big words on a billboard with like no design element to it at all. And we thought like, actually, let's try to make something that's kind of a little bit like warm feeling and pretty stupid.

> 是的。是的。或者就只是广告牌上一堆大字，完全没有任何设计元素。我们就想，其实，我们来试着做点感觉有点温暖、又相当傻气的东西吧。

[31:11] **SPEAKER_00:** Like I was wearing like a frilly frock.

> 比如我穿着一件带荷叶边的连衣裙。

[31:13] **SPEAKER_01:** Yeah. And then you put yourself in all the ads.

> 是的。然后你把自己放进了所有的广告里。

[31:15] **SPEAKER_00:** Okay. So I was like, will anyone even realize this is me or will they think they've got some like random middle-aged guy to turn up these ads? Either case is probably fine. Yeah.

> 好的。所以我当时想，会有人认出这是我吗，还是他们会以为是随便找了个中年大叔来拍这些广告？无论哪种情况大概都无所谓。是的。

[31:24] **SPEAKER_00:** We did a lot with hedgehog. We did do some with hedgehogs as well. Yes. But we felt again, it's just not quite as edgy.

> 我们用刺猬（PostHog 的吉祥物）做了很多。我们也确实做了一些用刺猬的广告。是的。但我们还是觉得，那没那么有锋芒、没那么大胆。

[31:30] **SPEAKER_00:** It's hard to make it not feel like too professionally done almost where it's like kind of kooky to have like a very average person on the ads or whatever, instead of like something that we clearly put tons of time into.

> 很难让它不显得太"专业精致"——那种在广告上放一个非常普通的人反而有点古怪好玩的感觉，而不是那种明显投入了大量时间精心制作的东西。

[31:40] **SPEAKER_01:** Too hard on yourself, James. I mean, I agree. Look. It's great.

> 你对自己太苛刻了，James。我是说，我同意。你看。它很棒。

[31:45] **SPEAKER_01:** My wife gives me so much grief. I get so excited every time I see a post-hoc ad around the city and my wife was like, is those the spaghetti guys again? But it lets people know that someone's home, that there's actual people behind this and that they really care a lot. Even things down the details and the typography, like it sends a message.

> 我太太老是拿这事打趣我。我每次在城里看到 PostHog 的广告都特别兴奋，我太太就会说，又是那帮意大利面的家伙？但它让人们知道"家里有人"，知道这背后有真真切切的人，而且他们非常在乎。哪怕是细节和排版这些东西，都在传递一个信息。

[32:01] **SPEAKER_01:** We are going to make a product that's also this well thought out and it's also trying to get you what you need to the same level.

> 我们要做的产品同样是经过这般深思熟虑的，同样在以这样的用心程度努力满足你所需要的东西。

[32:06] **SPEAKER_00:** Yeah. I think there's just like a level of signaling that you know what you're doing to pull off an ad like this. Because it. Yeah.

> 是的。我觉得，能做成这样一则广告，本身就传递出一种信号，表明你很清楚自己在做什么。因为它。是的。

[32:14] **SPEAKER_00:** It does show a level of savviness. Like the website is similar in thought process of like, we're trying to demonstrate to someone who isn't yet using our product that, oh no, they kind of get technology or they like kind of just get me as a person a little bit better than like the faceless corporation.

> 它确实展现出一定程度的精明老练。就像网站背后的思路也类似：我们在努力向那些还没用我们产品的人证明，哦，这些人是懂技术的，或者说他们比那种毫无面孔的大公司稍微更懂我这个人一点。

[32:28] **SPEAKER_01:** Let's talk about your website. I think you've got the best website of like any B2B company, maybe in the YC portfolio. I don't know. I get in trouble for saying that, but it's incredible.

> 我们来聊聊你们的网站。我觉得你们的网站是所有 B2B 公司里最好的，也许是整个 YC 投资组合里最好的。我说不好。我这么说会惹麻烦，但它真的太棒了。

[32:37] **SPEAKER_01:** Your website's awesome. What was the genesis of going in that direction? Because it wasn't always like that. You mentioned a little bit ago that early on you guys had a lot of back content, a lot of lore on PostHog early on, but the website itself was still pretty typical static website with some information for a SaaS company.

> 你们的网站太赞了。走上这个方向的缘起是什么？因为它并非一直如此。你刚才提到，早期你们有很多幕后内容、很多关于 PostHog 的"传说故事"，但网站本身仍然是一个相当典型的 SaaS 公司静态网站，带一些信息而已。

[32:55] **SPEAKER_01:** But now it's this whole experience simulating, you know, using a computer in PostHog land. Where did this come from?

> 但现在它成了一整套体验，模拟的是，你懂的，在"PostHog 之境"里使用一台电脑。这是从哪儿来的灵感？

[33:03] **SPEAKER_00:** I think a few things. I think we kind of, since like 2021-ish, the website's our sales team. Like there isn't a single customer that won't go through the website before they buy the product. And especially because of the nature of our audience, we're very self-serve.

> 我觉得有几个原因。我觉得，大概从 2021 年左右起，网站就是我们的销售团队。就是说，没有哪一位客户在购买产品之前不会先浏览网站。尤其因为我们受众的特性，我们非常"自助服务"。

[33:13] **SPEAKER_00:** And so I'm like, well, we should invest in this. Like it's the, we don't have to hire a sales team. It turns out in the first few years, or we had, but it was tiny, kind of like two people. And so, well, I think we can therefore justify spending like a ridiculous amount of effort on the website.

> 所以我就想，嗯，我们应该在这上面投入。就是说，我们不必雇一个销售团队。事实证明在头几年里……或者说我们是有销售的，但非常小，大概就两个人。所以，我觉得因此我们有理由在网站上投入多得离谱的精力。

[33:27] **SPEAKER_00:** The cost isn't that high, but like we can put, it's kind of the energy really, because I think this will make us stand out. So I think a lot of people quickly, 80, 20, something you can extremely quickly get to a polished website now. Like in a day you can have a polished website. So everyone just does that and they're like, cool, I'm done now, this is 80, 20, then move on.

> 成本其实没那么高，但我们可以投入——真正投入的是精力，因为我觉得这会让我们脱颖而出。我觉得很多人很快就用"八二法则"（80/20）——现在你可以极快地做出一个精致的网站。差不多一天就能有一个精致的网站。所以每个人都这么干，然后想，好，我搞定了，这就是八二了，接着往下做别的。

[33:40] **SPEAKER_00:** And I'm like, well. 80, 20 is like, because we're in a busy industry is about standing out. And so there's no point doing 80, 20. Like there's, it's just a missed shot.

> 而我想，嗯，八二法则——因为我们身处一个拥挤的行业，关键在于脱颖而出。所以做到八二是没有意义的。那只是白白错失的一击。

[33:48] **SPEAKER_00:** It's like, actually all of the return from the website has come from like the last percent of effort where it's like, no, we're going to go like so insanely far past what is normal that it is remarkable, which means that people will talk about it. Because when we talk to users early on, it turned out all of them are coming to us for people were showing up because they'd heard about us online or someone who recommended us. And then we said, why did they recommend you? And it was all the tools in one, low pricing.

> 实际上，网站带来的所有回报都来自最后那一个百分点的努力——就是那种"不，我们要远远超出常规、超出到疯狂离谱的地步，以至于它令人惊叹"的努力，这意味着人们会去谈论它。因为我们早期和用户交流时发现，他们之所以来找我们，都是因为在网上听说了我们，或者有人推荐了我们。然后我们问，他们为什么推荐你们？答案就是：所有工具集于一体、价格低廉。

[34:11] **SPEAKER_00:** Super brand and very technical support people. And we have literally just done those things. But it's like, okay, we can't just keep doing them as it is. We should be trying to crank the dial up further.

> 超强的品牌，以及非常懂技术的支持人员。而我们做的就是这些实实在在的事情。但我们想，好，我们不能就这么维持原样地一直做下去。我们应该努力把旋钮再往上拧。

[34:20] **SPEAKER_00:** So it's like, instead of building like three products, we should build like 300 products. How could that work? Or on the brand side, it's like, okay, post was kind of weird. It's like, it needs to be weirder still.

> 所以就是说，与其做三款产品，我们应该做三百款产品。那要怎么才能实现？或者在品牌这一侧，就是，好，PostHog 本来就有点古怪，那它需要变得更古怪才行。

[34:30] **SPEAKER_00:** Like it needs to be so weird that it polarizes. Every day we'll get a whole bunch of people talk about that website and we monitor all our brand mentions online. And it's going to be like either, this is literally the best thing I have ever seen. And we also get, this website is atrocious.

> 它需要古怪到能让人两极分化。每天都会有一大群人在谈论那个网站，我们会监测所有关于我们品牌的线上提及。评价要么是：这简直是我见过的最棒的东西。我们也会收到：这个网站糟透了。

[34:44] **SPEAKER_00:** But we feel like we're polarizing it largely in favor of our audience more. Like I'm sure there are some people who are like, what? But we're happy to push so hard in the direction we think is something cool for our audience that the people that aren't really our focus, we don't care if they disproportionately hate it basically. And then partly the other thing that was happening was it didn't just come from like a pure aesthetic perspective.

> 但我们觉得，我们制造的这种两极分化在很大程度上更偏向于讨好我们的受众。我确定肯定有些人会想，这是什么鬼？但我们乐于朝着我们认为对我们受众来说很酷的方向使劲推，以至于那些本来就不是我们目标受众的人，就算他们格外讨厌它，我们基本上也不在乎。另外还有部分原因是，这并不仅仅出于纯粹的审美考量。

[35:04] **SPEAKER_00:** We genuinely were trying to work out how do we build a website that fully documents and prices for like 15 or 16 products. But we also have a whole load of other things we've built that we think are useful. So for example, we have a cool developer jobs board. It's like a jobs board where the filters, instead of being just like location or pay range or something are like, what kind of laptop do I get?

> 我们是真的在琢磨，怎么才能做出一个网站，能为大约 15 或 16 款产品完整地提供文档和定价。但我们还做了一大堆其他我们认为有用的东西。比如说，我们有一个很酷的开发者招聘板。它是那种招聘板，但它的筛选条件不只是地点、薪资范围之类的，而是像：我能拿到什么样的笔记本电脑？

[35:22] **SPEAKER_00:** Is the majority of the company developers? There's stuff that an engineer actually would be interested in. There's something there to think about. Yeah.

> 公司里大部分人是开发者吗？这些是工程师真正会感兴趣的东西。那里有值得琢磨的内容。是的。

[35:27] **SPEAKER_00:** Yeah. And we built this as like kind of fun project, but we're like, well, this is useful to our audience. So we have that in there. We have like a handbook that's quite popular for people to read and learn from.

> 是的。我们把这个当作一个好玩的项目来做，但我们想，嗯，这对我们的受众有用。所以我们把它放进去了。我们还有一本很受欢迎的手册，供人们阅读和学习。

[35:34] **SPEAKER_00:** Like you can learn how everything works. Like how much we pay people. Like when we let people go, like everything is there. And so that's like another thing.

> 你可以了解到一切是怎么运作的。比如我们付给员工多少钱。比如我们什么时候会解雇员工，一切都在那里。所以那又是另外一样东西。

[35:40] **SPEAKER_00:** We have a newsletter with like more than a hundred thousand subscribers that's also in there. And so it just felt like the form of a website of just like a thing, lots of pages you scroll through. It felt like we're doing something more multi, much more multidimensional than that. That was the two things.

> 我们有一份订阅人数超过十万的电子简报，那也在里面。所以就感觉，那种"一个东西加很多可以滚动浏览的页面"的网站形式，感觉我们在做的东西比那要多维得多、丰富得多。就是这两方面。

[35:54] **SPEAKER_00:** It wasn't purely aesthetic. It was also from an experience, but we actually thought it would be better reflect what we're doing. Like PostDog is quite a complicated company. Like, and again, it's tempting to be like, okay, we should just have like a single landing page with like one button you click and nothing, no other information.

> 它并不纯粹是审美考量。它也是出于体验，但我们其实认为这样能更好地反映我们正在做的事情。PostHog 是一家相当复杂的公司。而且，同样地，人们很容易想，好，我们干脆只做一个落地页，上面有一个可以点的按钮，别的什么信息都没有。

[36:06] **SPEAKER_00:** That's not what our audience wants.

> 那不是我们的受众想要的。

[36:08] **SPEAKER_01:** You're kind of just like spitting in the eyes. It's kind of like the idea of a funnel. It's almost like instead of a funnel that you're trying to push people through, you're just giving them a great piece of cheese to dig into and enjoy and savor.

> 你有点像是在——这有点像"漏斗"的概念。这几乎就像是，你没有去搞一个试图把人们硬推过去的漏斗，而是直接给他们一块上好的奶酪，让他们尽情挖掘、享用、细细品味。

[36:19] **SPEAKER_00:** Well, we were wondering what would happen to the conversion rate and we were like, we kind of knew this is going to tank the conversion rate. It's going to get, we're like, this is getting much more traffic and the conversion rate is getting worse. And I was like, well, like if we ongoingly have way more traffic and there's worse conversion rate, if I could like double our traffic and half our conversion rate, I would take that. And so we launched it kind of knowing that's probably what would happen.

> 嗯，我们当时很好奇转化率会怎样，我们其实心里有数，知道这会让转化率暴跌。我们想，这带来了多得多的流量，而转化率在变差。我当时想，嗯，如果我们能持续获得多得多的流量、同时转化率变差，假如我能让流量翻倍、转化率减半，我也愿意接受这个交易。所以我们发布它的时候，大致就知道很可能会是这个结果。

[36:37] **SPEAKER_00:** But we did also think like, we think this is interesting enough that people will actually switch on for once online rather than just like sort of like trying to rush to get to the button. And like, we also thought like, I mean, if a developer can't work out how to click get started when there's already like three of them on the page, like that marginal person who maybe would have not converted, like, I don't know, it just felt like you're playing like a weird game, trying to appeal to that user. And so we think like of the marginal user, this will impress enough that they will convert despite the fact the conversion experience is very unusual. And so yeah, the conversion rate did, it didn't actually tank.

> 但我们也确实想到，我们觉得这个东西足够有意思，会让人们上网时破天荒地真正"用起心来"，而不是那种急着冲去点按钮。而且我们还想，我是说，如果一个开发者在页面上已经有三个"开始使用"按钮的情况下，还搞不清楚该怎么点，那么那种边缘用户——本来可能就不会转化的人——我说不好，那感觉就像你在玩一个很怪的游戏，去迎合那种用户。所以我们觉得，对于边缘用户来说，尽管这个转化体验非常不寻常，但这个网站会足够打动他们，让他们最终转化。所以是的，转化率确实……其实并没有暴跌。

[37:08] **SPEAKER_00:** It was like maybe 10%. Ish off the top of my head that we're gonna do a post on it was worse. We did like one experiment to change the flow slightly, now the traffic is much higher, the conversion rate is significantly higher too. And so it's performing better from a conversion perspective, even though it's like wildly complicated.

> 凭我印象大概是差了 10% 左右，我们打算就此写一篇文章——它当时是变差了。我们做了一个实验，稍微改了一下流程，现在流量高多了，转化率也显著更高了。所以从转化的角度看，它表现得更好了，尽管它复杂得离谱。

[37:22] **SPEAKER_01:** My favorite part of the website, you have this unhinged merch shop that has some some deep cuts in it. And my favorite of the deep cuts is visitors can buy a signed photo of James and Tim, the founders of posthog and it's sold out. Someone actually came and bought I think we sold one. In fact, yeah.

> 我最喜欢网站的一个部分，是你们那个疯疯癫癫的周边商店，里面有一些"深藏款"（不为人知的冷门好货）。而我最喜欢的深藏款是：访客可以买一张 James 和 Tim（PostHog 创始人）的签名照，而且它已经售罄了。真的有人来买了——我想我们卖出去了一张。事实上，是的。

[37:39] **SPEAKER_00:** I love the yacht rock aesthetic of the photo, by the way. Yeah, we've had quite a few boating offsites. This is supposed to represent Tim alignment, but I've think about it on the way here. And I actually think I think the reason that feels funny is you go like this is represent Tim and I being aligned and close together, but this is what aligned would be close, but something else.

> 顺便说一句，我很喜欢那张照片那种"游艇摇滚"（yacht rock）的美学风格。是的，我们搞过好几次船上团建。这张照片本意是代表我和 Tim 的"一致对齐"，但我来这儿的路上想了想。我其实觉得，它之所以显得好笑，是因为你会想，这代表 Tim 和我步调一致、亲密无间，但"对齐"应该是那种亲近，而这张照片却是别的意思（暗示照片显得暧昧亲密）。

[37:59] **SPEAKER_00:** Yeah.

> 是的。

[38:00] **SPEAKER_01:** All right. Well, thank you so much for spending time with us today and talking us through all this. I know we have so many folks out there that follow. You.

> 好的。非常感谢你今天抽时间和我们在一起，并给我们一一讲解了这一切。我知道外面有很多人在关注你。

[38:09] **SPEAKER_01:** The videos that we put out there looking for ways to break through. And I think your point about like you have to be remarkable is obvious, but overlooked so much today. And so thank you for sharing some of the ways that you guys have figured out how to try to stand out and be remarkable. And congratulations again on this latest round that you guys just raised.

> ——关注我们发布的这些视频，寻找突破的方法。我觉得你说的那一点——你必须做到卓尔不群、令人瞩目——显而易见，但如今被太多人忽视了。所以谢谢你分享了你们摸索出来的一些方法，讲述如何努力脱颖而出、做到与众不同、令人难忘。再次祝贺你们刚刚完成的这最新一轮融资。

[38:26] **SPEAKER_01:** We're so happy for you guys. Excited here at YC.

> 我们真为你们感到高兴。在 YC 这边我们都很激动。

[38:28] **SPEAKER_00:** Yeah, thank you. Yeah, it was monumentally important to us to go through the program. So if you're listening, like go apply to YC.

> 是的，谢谢。是的，参加这个项目对我们来说意义极其重大。所以如果你正在收听，去申请 YC 吧。

[38:35] **SPEAKER_01:** All right. Thanks for joining us today.

> 好的。谢谢你今天来参加我们的节目。
