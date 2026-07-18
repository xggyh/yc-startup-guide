# 全文转录 · Dylan Field 谈 Figma 的规模化与设计的未来

> ▶ [YouTube](https://www.youtube.com/watch?v=-7Qz7tSTfUU) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/-7Qz7tSTfUU.md) &nbsp;·&nbsp; Dylan Field: Scaling Figma and the Future of Design

> 中英对照 · 每段英文原文下附中文翻译

[00:00] **SPEAKER_02:** Designers need to be founders. We need to have folks that are designers step into the founder role and start companies. It feels intuitively like we're in the MS-DOS era of AI right now. If you look back 10 years from now, everyone's gonna go, can you believe that we just had this chat box?

> 设计师需要成为创始人。我们需要让身为设计师的人走进创始人的角色,去创办公司。直觉上感觉,我们现在正处于 AI 的 MS-DOS 时代。如果从十年后回望,大家都会说:真不敢相信我们当时竟然只有这么一个聊天框?

[00:20] **SPEAKER_04:** Awesome, well, wanna welcome Dylan. I'm curious what the makeup of the audience is here. How many people have used Figma before? Wow, all right. Awesome.

> 太棒了,我想欢迎 Dylan。我很好奇现场观众的构成。有多少人用过 Figma?哇,好的,太棒了。

[00:32] **SPEAKER_04:** How many people consider themselves to be designers? Okay, all right. Many of us. Yes, our people. And how many are currently founders?

> 有多少人认为自己是设计师?好,不错,我们当中很多人都是。对,都是自己人。那又有多少人现在是创始人呢?

[00:44] **SPEAKER_04:** Awesome. Cool, okay. That's a good mix of people in the audience. So we'll hear the Figma story, then we'll talk about advice around AI and design, and then we'll get some advice on just being a founder from Dylan too, so I'm excited to jump in. Maybe to start, give us kind of a snapshot on where Figma is today, and then we can kind of go back to the beginning days.

> 太棒了。很好,好的。现场观众的构成很不错。我们会先听听 Figma 的故事,然后聊聊关于 AI 和设计的建议,接着也会向 Dylan 请教一些关于如何做创始人的建议,所以我很期待开始。也许先从这里说起:给我们描绘一下 Figma 如今的概况,然后我们再回到最初的日子。

[01:06] **SPEAKER_02:** Yeah, today we are many different places. We're hybrid, 1,700 people now, which is wild. I have to pinch myself on that number. We have eight products now. We just doubled our product lineup at our last config.

> 是的,如今我们身处许多不同的地方。我们是混合办公模式,现在有 1700 人,这太疯狂了。看到这个数字我得掐一下自己确认不是在做梦。我们现在有八款产品。在上一次 Config 大会上,我们的产品线直接翻了一倍。

[01:20] **SPEAKER_02:** So I'm very excited to hear your feedback, if you got any on things like Figma Make, Sites, Draw, Buzz, but it's been a very exciting time. Lots of work we're doing as we explore all the things that we can do to help our audience.

> 所以如果你们对 Figma Make、Sites、Draw、Buzz 这些产品有任何反馈,我都非常期待听到。这是一段非常令人兴奋的时期。我们做了大量工作,去探索一切能帮助我们用户的可能性。

[01:35] **SPEAKER_04:** And now take us back to maybe 19-year-old Dylan, getting started with the kernel of the idea that eventually became Figma, but it wasn't a straight line getting there. Tell us about the early days and kind of how you and Evan got started.

> 现在把我们带回到大约 19 岁的 Dylan 吧,那个最初萌生了后来成为 Figma 的想法内核的时候,但走到今天并不是一条直线。给我们讲讲最早的日子,以及你和 Evan 是怎么起步的。

[01:47] **SPEAKER_02:** Yeah, so in the early days of Figma, well, I guess before it was even Figma, Evan and I were at Brown together. He was my TA, and we were asking ourselves the question of why now? Like what's changing the world? And the two answers that we had, we came up with that we also felt deep conviction in. One was drones and quadcopters.

> 是这样,在 Figma 早期,嗯,应该说在它还没成为 Figma 之前,我和 Evan 都在布朗大学。他是我的助教,我们那时在问自己一个问题:为什么是现在?比如说,什么正在改变世界?我们得出了两个答案,也都对它们抱有深深的信念。一个是无人机和四旋翼飞行器。

[02:10] **SPEAKER_02:** The other one was WebGL. And Evan, after about a month or so said, hey, like not into drones for all sorts of various reasons. That was kind of the one I was pushing for more at the time, also except WebGL, of course. And then I was like, great, WebGL it is. And so WebGL, I think everybody probably here knows, but it's the way you use the GPU in your computer and the browser.

> 另一个是 WebGL。大约一个月后,Evan 说,嘿,出于种种原因我对无人机不感兴趣。那时候无人机其实是我更力推的方向,当然也除了 WebGL。然后我就说,好啊,那就 WebGL 吧。WebGL 嘛,我想在座各位大概都知道,它是让你在浏览器里使用电脑 GPU 的一种方式。

[02:33] **SPEAKER_02:** WebGPU is its successor. And yeah, we started going really deep on like, what are all the things that we can build? And two main paths were games or tools. Pretty fast, we said, okay, not games, let's go tools. And then it was a deep exploration with many twists and turns as we explored all sorts of tools that we could build.

> WebGPU 是它的继任者。是的,我们开始非常深入地思考:我们到底能造出哪些东西?两条主要的路径是游戏或工具。很快我们就说,好,不做游戏,做工具吧。接着就是一场充满曲折的深入探索,我们尝试了各种各样能构建的工具。

[02:55] **SPEAKER_02:** And it took, we really started in earnest August, 2012, whereas we started talking about it more December of 2011. So it took a while to get to the point where we started. And then from there, I would say it was at least June or July of 2013, before we went all in on, okay, let's build Figma as it is today. And even then there was still a bit of a narrowing path to get to the product that exists now.

> 我们真正认真开始是在 2012 年 8 月,而我们更早开始谈论这件事是在 2011 年 12 月。所以从想法到真正起步花了一段时间。而从那之后,我得说至少到了 2013 年六七月,我们才全力投入到「好,我们就做如今这样的 Figma」这件事上。即便到了那时候,通往现在这款产品的道路仍然还有一段逐步收窄的过程。

[03:21] **SPEAKER_04:** And when you first started, were you thinking about this as a startup and a company that you wanted to build, or were you thinking about it more as like a project that you wanted to do with your friend?

> 那么在你们最初起步时,你是把它当作一家想要打造的创业公司来看待,还是更多把它看成一个想和朋友一起做的项目?

[03:29] **SPEAKER_02:** No, it was definitely the hope with startup, and startup that could scale. At the same time, my downside case was, I get to work with Evan, who I considered then, consider now to be a hero. He's like the smartest guy I know. If you have any doubt about the statement, just look up his GitHub. He's an amazing man and an absolute genius.

> 不,那绝对是奔着创业去的希望,而且是一家能够规模化的创业公司。与此同时,我最坏的情况打算是,我能和 Evan 一起工作,他是我那时候、也是现在都视为英雄的人。他是我认识的最聪明的人。如果你对这句话有任何怀疑,去查查他的 GitHub 就知道了。他是个了不起的人,一个绝对的天才。

[03:51] **SPEAKER_02:** And I figured worst case scenario, I spent a few years working with Evan, I learned a lot, and I go back to school, same place I'm at now, can't hurt. Outside case, we go build a cool company. All the problems that we were thinking about working on were very, very interesting to me. And so I didn't really see any risk to the scenario, and also to help that I had the Teal Fellowship. I would've done it without it, but having 100K over two years, I know now inflation, et cetera, probably sounds like less than it was then.

> 我心想,最坏的情况就是,我花几年时间和 Evan 一起工作,学到很多东西,然后回学校,回到我现在所在的地方,没什么损失。而好的情况是,我们打造出一家很酷的公司。我们当时考虑要解决的所有问题对我来说都非常非常有意思。所以我其实没看到这个方案有什么风险,而且还有一点帮助是我拿到了 Thiel 奖学金。就算没有它我也会去做,但两年拿到十万美元——我知道考虑到通胀之类的因素,现在听起来可能没有当时那么多。

[04:22] **SPEAKER_02:** But yeah, I mean, to have actual cash and not have to dig into savings or going to debt, huge deal, not just because of the cash element, but also because it gives you time. If we had stopped six months in and that was our point where we made a call, Figma would not be here today. And so I think if you're a founder already going or you're thinking about founding, you gotta give yourself time somehow. That's really important.

> 但真的,我是说,手里有实实在在的现金,不必动用积蓄或者背上债务,这非常重要,不仅仅是因为钱本身,更因为它给了你时间。如果我们做了六个月就停下来,而那正是我们做决断的时点,那么今天就不会有 Figma。所以我觉得,如果你已经是一名创业者,或者正在考虑创业,你无论如何都得给自己争取时间。这真的很重要。

[04:46] **SPEAKER_04:** Yeah, you spent a couple of years trying to, you know, do all the twists and turns and the thing that eventually became what Figma is today. Yeah. What kept you going in that time? A lot of times, you know, founders will get into this like pivot hell of jumping from idea to idea and motivation, just keeps declining. And how did you keep yourselves motivated during that time and feel like you were on to something and you were on the right track?

> 是的,你花了好几年,经历了这一路的曲折,才做成了最终成为今天 Figma 的东西。那段时间里是什么支撑你坚持下去的?很多时候,创始人会陷入那种「转型地狱」,从一个点子跳到另一个点子,动力不断下滑。在那段时间里,你们是怎么保持动力、让自己相信你们发现了有价值的东西、走在正确道路上的?

[05:08] **SPEAKER_02:** Well, I mean, first of all, just working with Evan was super fun. You know, we're kind of thinking through ideas by building them. It felt every week like we were kind of inventing the future in some way. At some point, I kind of went, memes are gonna go to the moon and I convinced Evan, hey, let's go build a meme generator. And this is, you know, 2012 timeframe and we built a great fucking meme generator.

> 首先,单是和 Evan 一起工作就非常有意思。你知道,我们是通过动手做来把想法想清楚的。每一周都感觉我们在以某种方式发明着未来。有一次我突然觉得,表情包(meme)要一飞冲天了,于是我说服 Evan,嘿,我们去做个表情包生成器吧。那大概是 2012 年前后,我们做出了一个他妈的超棒的表情包生成器。

[05:28] **SPEAKER_02:** I think it was, for sure, would have been the best one in the market. And my thesis was right, by the way. Look at the exponential curve of memes since 2012. Yeah, we would have made some money there. At the same time, after a week of that, I think both of us were ready to quit.

> 我觉得,它肯定会是市场上最好的那个。而且顺便说一句,我的判断是对的。看看 2012 年以来表情包那条指数级增长的曲线就知道了。是的,我们本来在那上面能赚点钱。可与此同时,做了一周之后,我觉得我俩都想放弃了。

[05:41] **SPEAKER_02:** I was asking myself, like, why did I drop out of Brown for this? That was probably like a pretty low point at the start. But other than that, there's the constant existential nature of asking yourself, like, what are we doing? What's the big goal here? When you're in that phase of really trying to discover what to work on.

> 我在问自己,我到底为什么为了这个从布朗退学?那大概是起步阶段一个相当低谷的时刻。但除此之外,还有那种持续的、事关存在意义的自我拷问,比如,我们在做什么?这里真正的宏大目标是什么?当你正处在真正努力去发现该做什么的那个阶段时,就是这样。

[05:57] **SPEAKER_02:** But I think if you've got a co-founder, you've got a collaborator, you're not just alone. You know, hopefully your highs and their highs, your lows, their highs cancel out somehow. And you can kind of feed off each other to keep each other going. That really helps.

> 但我觉得,如果你有一位联合创始人,有一个合作者,你就不是孤身一人。你知道,理想情况下,你的高潮和他们的高潮、你的低谷和他们的高潮会以某种方式相互抵消。你们能彼此汲取能量,互相支撑着走下去。这真的很有帮助。

[06:10] **SPEAKER_04:** That's cool. Once you kind of came up with the idea for Figma, how did you get your first users?

> 太酷了。等你们大致想出 Figma 这个点子之后,你们是怎么获得第一批用户的?

[06:15] **SPEAKER_02:** Yeah, really the first users of Figma, a lot of it was cold emailing and people in network. So folks that I'd either interned with, for example, I interned at Flipboard, LinkedIn, O'Reilly Media. And from that, there were people I could reach out to. They could tell me others to talk with. But also I just looked online, like who are the designers that I think could be really helpful to us.

> 是的,Figma 真正最早的那批用户,很大一部分来自陌生开发邮件和人脉网络。比如那些曾经和我一起实习过的人——我在 Flipboard、LinkedIn、O'Reilly Media 都实习过。通过这些经历,就有一些人是我可以联系的。他们又能告诉我还可以去找谁聊。此外我也就在网上找,看哪些设计师是我认为可能对我们非常有帮助的。

[06:38] **SPEAKER_02:** And I respect their work. You know, if they answer my email and they let me buy them a coffee, like it'll just be like a personal moment for me cause they're my hero. And a lot of them replied. Like it's kind of wild that people reply to cold emails, but they do. And so, yeah, I went there and then it turns out designers give great feedback.

> 而且我很尊重他们的作品。你知道,如果他们回复了我的邮件,愿意让我请他们喝杯咖啡,那对我来说就是一个很个人化的时刻,因为他们是我心目中的英雄。他们中很多人都回复了。你知道,人们会回复陌生邮件其实挺不可思议的,但他们真的会回。所以是的,我就这么去做了,结果发现设计师们能给出很棒的反馈。

[06:57] **SPEAKER_02:** So it wasn't just like meeting them and them saying, yeah, your product sucks. They'd be like, here's exactly why it's not great. And here's what you can do better. Here's what it would take for me to use this. And the more that I engaged and we worked through that, the better the product got, I'd follow up with them.

> 所以不只是见了面然后他们说,对,你的产品很烂。他们会说,这就是它不好的确切原因。这是你可以改进的地方。这是要我用它需要满足的条件。而我越是投入其中、和他们一起把这些问题梳理清楚,产品就变得越好,然后我会再去跟进他们。

[07:14] **SPEAKER_02:** And eventually they started converting, some of them. Took a while before a lot of them converted. Later on, we kind of went on tour. I met, at this point we had venture investment, the venture firms that invested in us, they invested in other companies too. I had them make introductions to the companies, you know, for an entire summer, I basically met with, I don't know, five, six, seven companies a week at least, sitting down with them, sometimes several a day, saying, hey, here's a demo.

> 最终他们开始转化了,其中一部分人。很多人过了好一阵子才转化。后来,我们算是搞了一场巡回。那时我们已经有了风险投资,投资我们的那些风投机构也投了其他公司。我让他们把我引荐给那些公司,你知道,整整一个夏天,我基本上每周至少见五、六、七家公司,坐下来跟他们聊,有时一天见好几家,说,嘿,这是个演示。

[07:43] **SPEAKER_02:** Will you use it? If not, why not? And very low conversion rate. I think like in that entire summer, maybe two of them went in for it and actually started using Figma. One was Notion.

> 你会用它吗?如果不用,为什么?转化率非常低。我觉得整个那个夏天,大概只有两家真的接受了,并真正开始用起 Figma。一家是 Notion。

[07:57] **SPEAKER_02:** The other was the company that became Coda, then called Krypton. And it was kind of interesting, they're both, you know, these cloud-based document tools with very similar philosophies to us, but you know, you then launch it and people start using it more. There's a lot of folks out there that resonate with the message. So it was a slow arc over time, but the constant was feedback, getting feedback to the team, making sure we understood what problems we needed to solve.

> 另一家是后来成为 Coda 的公司,当时叫 Krypton。挺有意思的,它们俩都是那种基于云的文档工具,理念和我们非常相似。但你知道,随后你把产品发布出去,用的人就多了起来。外面有很多人对这个理念产生了共鸣。所以这是一条随时间缓慢上升的弧线,但不变的是反馈——把反馈带回团队,确保我们理解自己需要解决哪些问题。

[08:22] **SPEAKER_04:** That's interesting because, you know, everyone tells you to launch early. And the reason to launch early is to get that feedback. And from the outside, it looks like you took a long time to launch, and from the outside, it looks like you took a long time to launch, and from the outside, it looks like you took a long time to launch, and from the outside, it looks like you took a long time to launch, but behind the scenes, you were actually talking to tons of users and potential customers and getting feedback constantly. Like, how did you think about when was the right time to actually launch the product?

> 这很有意思,因为你知道,所有人都告诉你要尽早发布。而尽早发布的原因就是为了拿到反馈。从外部看,似乎你们用了很长时间才发布,但在幕后,你其实一直在和大量用户和潜在客户交谈、不断获取反馈。那么,你是怎么判断真正发布产品的合适时机的?

[08:42] **SPEAKER_02:** First of all, I definitely echo the point of launch as soon as you can. If you take anything away from this, it's don't do what I did, you know, get your product out faster and charge money faster for the product to see if you actually can make money. Unless you have some genius galaxy brain consumer thing you're doing, in which case, figure it out yourself. I don't know what to tell you. I think that the feedback is essential, and you should launch as quickly as you can.

> 首先,我绝对赞同尽早发布这个观点。如果你只能从这场谈话里带走一点东西,那就是别学我,你知道,要更快把产品推出去,更快开始为产品收费,看看你到底能不能赚到钱。除非你在做某种天才级、脑洞爆炸的消费级产品,那样的话,你就自己去琢磨吧,我也不知道该给你什么建议。我认为反馈是必不可少的,你应该尽可能快地发布。

[09:07] **SPEAKER_02:** For me, the feedback was very clear. It's not ready. And that made it so that we didn't feel comfortable launching yet. But looking back, we did have the capital. I should have scaled the team faster so we could move faster and get it out quicker.

> 对我来说,反馈非常明确:它还没准备好。这让我们当时觉得还不适合发布。但回头看,我们其实是有资金的。我本该更快地扩张团队,好让我们跑得更快、更早把产品推出去。

[09:22] **SPEAKER_02:** That was something that I now, looking back, have learned. And when a team at Figma comes to me with an epic roadmap that they think is perfection, the first question I always ask is, how do we slim that down? How do we make it more bite-sized and test this earlier with our users? So it's absolutely the case that I try to push people internally towards a one-month or three-month cadence at most. You know, if someone comes to me with a nine-month, a 12-month, two-year cadence, it's like, what the fuck are you doing, man?

> 这是我如今回头看学到的一课。现在当 Figma 的某个团队拿着一份他们认为堪称完美、宏大无比的路线图来找我时,我总是问的第一个问题是:我们怎么把它精简下来?怎么把它拆得更小、更早地拿去让用户测试?所以我确实会在内部推动大家把节奏控制在最多一个月或三个月。你知道,如果有人拿着一个九个月、十二个月、两年的节奏来找我,那就是,老兄,你他妈到底在干嘛?

[09:54] **SPEAKER_04:** Yeah, that's such an important point, especially for small teams, which is a lot of times people are like, well, I have all this stuff I have to build, so I need to go higher up. I need to hire a bunch of people to be able to do it. But it seems like usually the right answer is like, how can you scope it down and do fewer things really well? It sounds like, is that part of your culture as you're building things?

> 是的,这是个非常重要的观点,尤其对小团队而言。很多时候人们会想,我有这么多东西必须做,所以我得往上招人,我得雇一大帮人才能把它做出来。但看起来通常正确的答案是:你怎么把范围缩小、把更少的事情真正做好?听起来这是你们在做东西时文化的一部分,对吗?

[10:10] **SPEAKER_02:** Yeah, constraints can actually really help, but I also think the startup equation, or maybe not equation, but the cycle that you're always in is something along the lines of, if you're the leader of a startup, you need to be identifying what you're doing the most of, figuring out how to get someone else to help you do that, or maybe in the future it's AI, who knows? But then from there, okay, how do you go find that person? And if you don't have enough resources, how do you get the resources? Right, that's the cycle that you're always in. It just turns out that actually having constraints, it breeds creativity, it breeds interesting ways to solve problems.

> 是的,约束其实真的能帮上大忙。但我也认为,创业的那个「方程式」,或者说不算方程式,而是你始终身处其中的那个循环,大致是这样的:如果你是一家创业公司的领导者,你需要识别出自己做得最多的是什么,弄清楚怎么找别人来帮你分担,或者未来也许是 AI,谁知道呢?然后从这里出发,好,你怎么去找到那个人?如果你资源不够,你又怎么去获取资源?对吧,这就是你始终身处的循环。事实证明,拥有约束反而能孕育创造力,孕育出有趣的解决问题的方式。

[10:46] **SPEAKER_02:** And so, yeah, I think they're useful.

> 所以,是的,我觉得约束是有用的。

[10:48] **SPEAKER_04:** What was the inflection point? I don't know. Was it shortly after you launched? Was it years later? Was it a few weeks ago when you actually believed this was gonna be a huge company?

> 拐点是什么时候?我不知道。是发布后不久吗?是好几年之后吗?还是几周前你才真正相信这会成为一家巨大的公司?

[10:57] **SPEAKER_02:** Oh man, I think the point at which I started to believe that actually this might be real was way later than our users did. People were telling me, this is amazing. I'm really excited. Here's my 12-page doc on all the things that I want you to do for Figma. I should have known then, even though our product was really bad, that there was something there.

> 天哪,我觉得我开始相信这事儿也许是真的,那个时间点比我们的用户要晚得多。当时有人对我说,这太棒了,我真的很激动,这是我写的一份十二页文档,列出了我希望你们为 Figma 做的所有事情。我那时就该意识到,即便我们的产品真的很糟,那里面确实有点门道。

[11:20] **SPEAKER_02:** But in reality, it took until Microsoft told us, hey, this is spreading like wildfire, and we're asking ourselves, should we shut it down? Or, you know, should we keep going? And the reason we're asking ourselves that is because you're not charging us. Maybe you should actually charge for the product. That was the moment that I was like, oh, I think something might be working.

> 但实际上,一直等到微软告诉我们,嘿,这东西正像野火一样蔓延,我们在问自己,是该把它关掉,还是,你知道,继续用下去?而我们之所以这么问自己,是因为你们没有向我们收费。也许你们真的该为这个产品收费了。就是那一刻,我才想,哦,我觉得某些东西也许真的开始起作用了。

[11:40] **SPEAKER_02:** We should probably charge people. And that was like five years in. So yeah, don't do that. And also listen for when people are pulling the product out of you. Like I think everyone talks about product market fit, but product market pull is really important.

> 我们大概应该开始收费了。而那已经是入行五年之后的事了。所以是的,别学我这样。同时也要留心什么时候人们在主动把产品从你手里「拽」出来。我觉得每个人都在谈产品市场契合度(product market fit),但产品市场拉力(product market pull)其实非常重要。

[11:57] **SPEAKER_02:** And you'll see signs of it when people are highly engaged, when they are obsessive about what you're doing, when they see the future of the vision that you're planting, that is a sign that you should really double down in whatever way you can. And so many people interpret it instead as, oh man, if only we had all these things that they're asking for, then we might have product market fit. Guess we got to grind for a long time and who knows if it'll work. The right mindset is, oh my God, they actually care enough to give us this feedback? This is huge.

> 你会看到它的迹象:当人们高度投入,当他们对你在做的东西痴迷不已,当他们看到你所播下的那个愿景的未来时,这就是一个信号,说明你真的应该用尽一切办法加倍投入。而太多人反而把它解读成:唉,要是我们把他们要求的这些东西全都有了,也许就能实现产品市场契合了。看来我们得埋头苦干很久,谁知道会不会成呢。正确的心态应该是:天哪,他们竟然在乎到愿意给我们这样的反馈?这可太了不起了。

[12:30] **SPEAKER_02:** And I think that people misinterpret that too much.

> 我觉得人们太经常误读这一点了。

[12:33] **SPEAKER_04:** It seems that even your feedback seeking early on in the early days, I think a lot of people are nervous to do that because they don't want to hear that it's not good enough. And they don't want to hear the thing that they poured so much time and energy into is not good yet and I would not use it and I would not pay you for it. And so you want to just hide from that. How did you shift your perspective to actually want to seek that?

> 看起来,即便是你早期那样去寻求反馈,我觉得很多人都会紧张,不敢那么做,因为他们不想听到「这还不够好」。他们不想听到自己倾注了大量时间和精力的东西还不行、我不会用它、我不会为它付钱。于是你就想干脆逃避这件事。你是怎么转变自己的视角,变得真心想去主动寻求反馈的?

[12:55] **SPEAKER_02:** I think maybe it's just like childhood for me. When I was growing up, I was a child actor, not like a child actor that got into anything really cool that you know about, like commercials and some TV and stuff. But as part of that, you audition constantly and basically you constantly get rejected. For me, that was not a big deal. Like I was used to rejection and I had fun with the process of it.

> 我觉得对我来说也许就跟童年经历有关。我小时候是个童星,不是那种参演过什么你们知道的很酷的东西的童星,就是拍拍广告、上过一点电视之类的。但作为其中一部分,你要不停地去试镜,基本上就是不停地被拒绝。对我来说,这没什么大不了的。我习惯了被拒绝,而且我从这个过程里找到了乐趣。

[13:21] **SPEAKER_02:** So yeah, I think for me, it's just maybe a different mental equation than others. But yeah, if you're not there yet, seek rejection. It's got interesting data in it. Don't you want to know the data?

> 所以是的,我觉得对我而言,也许只是心理上的算法跟别人不太一样。但真的,如果你还没到那个境界,去主动寻求拒绝吧。里面藏着有意思的数据。难道你不想知道这些数据吗?

[13:31] **SPEAKER_04:** Switchgears talked about design for a little bit. It's been a really great month for design, it feels like. It's been pretty wild. Yeah, I mean, we've had some popular redesigns from Airbnb and Netflix. We've had Apple's new Liquid Glass UI, which seems to be somewhat controversial.

> 换个话题,我们来聊一会儿设计。感觉这是设计领域非常精彩的一个月。相当疯狂。是的,我是说,我们看到了 Airbnb 和 Netflix 广受关注的重新设计。还有苹果新的 Liquid Glass 界面,这个似乎有点争议。

[13:48] **SPEAKER_04:** I'm sure there are opinions out here. At least there's opinions on X or Twitter or whatever. You guys had some incredible launches at Config recently. And, you know, at YC, we have kind of a call for more design founders. And then maybe the most surprising and impressive thing was OpenAI acquiring Johnny Ive and his company for more than $6 billion, which is pretty crazy.

> 我敢肯定现场就有各种看法。至少在 X、Twitter 或别的什么平台上是有很多看法的。你们最近在 Config 大会上有一些非常惊艳的发布。而且你知道,在 YC,我们某种程度上在号召更多设计师创始人。然后也许最令人意外、最令人印象深刻的一件事,是 OpenAI 以超过 60 亿美元收购了 Jony Ive 和他的公司,这相当疯狂。

[14:10] **SPEAKER_04:** So I'm curious, like, why now? Like, what is happening in this moment where it seems like design is really a part of the conversation in a lot of the tech world?

> 所以我很好奇,为什么是现在?此刻究竟发生了什么,使得设计似乎真正成为了科技界许多讨论的一部分?

[14:21] **SPEAKER_02:** Yeah, I mean, first of all, I think that in some ways it's new, in some ways it's not new. Design has, I think, been growing in importance, essentially, over the past decade. At Figma, we see it up close every day. More designers being hired. Design going from, you know, lipstick on a pig, make it pretty at the end of the process, to let's deeply think about how it works every step along the way.

> 是的,我是说,首先,我觉得在某些方面这是新鲜事,在某些方面又不新鲜。在我看来,设计的重要性基本上在过去十年里一直在上升。在 Figma,我们每天都近距离目睹这一点:越来越多的设计师被招聘。设计从「给猪涂口红」——也就是在流程末尾把东西弄漂亮——转变为「让我们在每一步都深入思考它是如何运作的」。

[14:45] **SPEAKER_02:** That's been a mindset shift that's been ongoing. But now I think in this age of AI, if you really believe that development gets easier and it's more simple to create software, it's faster to create software, then, like, what is your differentiator? It's design, it's craft, it's attention to detail, it's point of view. What we're seeing is recognition of that. I mean, Airbnb, they literally said, our differentiator is design.

> 这是一场一直在进行中的思维转变。但如今在这个 AI 时代,我觉得,如果你真的相信开发变得更容易了、创造软件变得更简单了、创造软件变得更快了,那么,你的差异化优势是什么?是设计,是匠心,是对细节的关注,是观点主张。我们现在看到的就是对这一点的认可。我是说,Airbnb 就直接说了,我们的差异化优势就是设计。

[15:12] **SPEAKER_02:** I think Brian said that. I believe that, you know, there's lots of takes on open AI and this more than $6 billion transaction. Some people are like, this is the stupidest thing in the world. Other people are hailing it as, like, absolute genius. I guess my mindset is, like, my mental model is there are some people out there who, when they do something you don't understand, it's easy to go into an attack mode and just dismiss it.

> 我记得是 Brian 说的。我认为,你知道,关于 OpenAI 和这笔超过 60 亿美元的交易有很多种看法。有些人觉得,这是世界上最蠢的事情。另一些人则把它奉为绝对的天才之举。我想我的心态、我的思维模型是这样的:世上有些人,当他们做出某件你不理解的事情时,你很容易进入攻击模式,直接否定它。

[15:42] **SPEAKER_02:** But over enough time, sometimes you see patterns and you're like, okay, I've consistently not understood what this person's saying over the course of, like, years. And, you know, years later, I go back to it and I'm like, oh, what I said in response to, what they did was just wrong. And then you kind of do this mental flip of, okay, assume that there's something to learn from whatever they're doing. Assume you're missing something. And I think that I look it up, something like open AI, and some part of it I understand.

> 但时间足够长之后,有时你会看到某种规律,然后你会想,好吧,在长达数年的时间里,我一直都没能理解这个人说的话。而你知道,若干年后,我回头再看,才发现,哦,我当时对他们所做之事的回应完全是错的。于是你就完成了这样一次心理上的翻转:好,假设无论他们在做什么,里面都有值得学习的东西。假设是你自己遗漏了些什么。我觉得,拿 OpenAI 这样的事情来看,其中有一部分我是理解的。

[16:16] **SPEAKER_02:** Design is differentiator. Some parts I don't understand. Like, that's a really big transaction. But Sam is one of those people that, you know, he's right about a lot of stuff. So I would encourage you, if you just dismissed it outright, ask yourself what you might be missing.

> 设计是差异化优势。有些部分我不理解,比如,那真的是一笔非常大的交易。但 Sam 是那种人,你知道,他在很多事情上都判断正确。所以我想鼓励你,如果你直接就把它一口否定了,那不妨问问自己,你可能遗漏了什么。

[16:32] **SPEAKER_04:** And you guys launched some really cool AI-focused products at your conference, Config, about a month ago, which has been really cool to see the reception there. Really positive from a lot of your users and the design community. I'm curious if you can share more about those and your motivation for building some of those.

> 你们大约一个月前在你们的大会 Config 上发布了一些非常酷、以 AI 为核心的产品,看到那里的反响真的很棒。你们很多用户和设计社区的反馈都非常积极。我很好奇你能不能多分享一些关于这些产品的情况,以及你们打造其中一些产品的动机。

[16:49] **SPEAKER_02:** If you look historically at the products we've launched for Figma, the pattern is we notice behavior happening in Figma design. We take it out of Figma design and make it its own product. And therefore, Figma design is able to be what Figma design wants to be, a product design tool. And, you know, whether it's FigJam or whiteboarding brainstorming tool, the first new product we launched, that we can make a dedicated space for, make it be everything it needs to be. Or it's slides where we saw, okay, 5% of files created in Figma design are slides.

> 如果你回顾我们为 Figma 发布过的历代产品,会发现一个规律:我们注意到某种行为正在 Figma Design 里发生。我们把它从 Figma Design 中抽离出来,做成一个独立的产品。这样一来,Figma Design 就能成为它本该成为的样子——一款产品设计工具。你知道,无论是 FigJam,我们发布的第一款新产品,那个白板头脑风暴工具,我们都可以为它开辟一个专属空间,让它成为它需要成为的一切。又比如幻灯片,我们看到,好,Figma Design 里创建的文件有 5% 是幻灯片。

[17:19] **SPEAKER_02:** So great, pull that out, make a slide tool, because there's all this stuff you need for slides that if you put it in Figma design, now you've got a complicated UI and one plus one is not equal to three. Or equal to like 1.5. A lot of the things you saw launch at Configure in that category. So draw, for example, which is a way to do more vector tasks, we made a separate mode for so that users can go deeper.

> 那太好了,把它抽出来,做一款幻灯片工具,因为做幻灯片需要一堆专门的东西,如果你把它们全塞进 Figma Design,你就得到了一个复杂的界面,一加一不等于三,反而只等于一点五左右。你在 Config 上看到发布的很多东西都属于这一类。比如 Draw,它是一种更专注于矢量任务的方式,我们为它做了一个单独的模式,好让用户能钻研得更深。

[17:44] **SPEAKER_02:** Because again, if you believe that craft is differentiator, more people want to be more expressive. How do we enable our customers and designers everywhere to do that on the Figma platform? Buzz, same thing. You have all these people that want to create mass exports and figure out ways to create production graphics. So if you've got a brand team and they've created templates, how do you make it so that you're able to then empower a marketing team to go use those templates and do mass creation of assets?

> 因为再说一遍,如果你相信匠心是差异化优势,更多人会想要更有表现力。我们怎样才能让世界各地的客户和设计师在 Figma 平台上做到这一点?Buzz 也是同样的道理。有很多人想要批量导出、想方设法制作可投产的图形素材。所以,如果你有一个品牌团队,他们创建了模板,那你怎么做到能进而赋能一个营销团队,让他们去使用这些模板、批量生成素材?

[18:13] **SPEAKER_02:** That's like a core workflow we see all the time, but we didn't want to make Figma design more complicated or dumb it down, and so instead you make a new surface. Sites, we see people designing websites all the time in Figma design, but then they have to go somewhere else to actually build the site and get it out there. So how do we get that so that they can actually ship it? And then Make, we're so excited about Make. This is a tool that lets you go from prompt to app, and it's already changed a lot of how we do work at Figma in terms of quickly prototyping and being able to get to the point where you throw ideas away faster.

> 这是我们一直看到的一种核心工作流,但我们不想让 Figma Design 变得更复杂,也不想把它做得过于简陋,于是你就为它开辟一个新的界面(surface)。Sites 也是,我们一直看到人们在 Figma Design 里设计网站,但接着他们不得不去别的地方才能真正把网站搭建出来、发布上线。那我们怎么让他们能够真正把它交付出去?再然后就是 Make,我们对 Make 太兴奋了。这是一款让你从提示词直接生成应用的工具,它已经在很大程度上改变了我们在 Figma 的工作方式——快速做原型,并且能够更快地把想法丢弃掉。

[18:47] **SPEAKER_02:** And with Figma Make, there's so much more that we want to explore and are really excited to explore there. So yeah, stay tuned on that one.

> 而围绕 Figma Make,还有太多我们想去探索、也非常兴奋要去探索的东西。所以,是的,请对它保持关注。

[18:54] **SPEAKER_04:** Cool. Yeah, I mean, you just touched on it there, but it feels like a lot of the line between design, design, and development is getting blurred. And there used to be very distinct phases in a product development process or parts of an iterative cycle. And now it feels like they're almost being combined into one. How do you think about that with the tools that you're making?

> 很酷。是的,你刚才其实已经提到了这一点,但感觉设计与开发之间的很多界线正在变得模糊。过去在产品开发流程中曾经有非常清晰的阶段划分,或者说迭代循环中不同的环节。而现在感觉它们几乎被合并成了一个。你在打造这些工具时是怎么看待这一点的?

[19:12] **SPEAKER_04:** And I'm also curious maybe how that process has changed, like how your own development process has changed within Figma.

> 我还很好奇,也许这个流程本身是怎么改变的,比如你们 Figma 内部自己的开发流程是怎么改变的。

[19:18] **SPEAKER_02:** I'll start with Figma. I think that for us, it's all about speed of iteration, speed of testing ideas. And tools like Make really help with that. It helps to have ways to rapidly prototype and to figure out what's going to work and what's not going to work and make that as low cost as possible. And then there's tools I can't talk about and things we're developing that have been pretty instrumental to how our development process is changing.

> 我先从 Figma 说起。我觉得对我们来说,一切都关乎迭代速度、测试想法的速度。而像 Make 这样的工具在这方面真的很有帮助。有办法快速做原型、弄清楚什么行得通、什么行不通,并把这个过程的成本压到尽可能低,这非常有用。此外还有一些我现在不能谈的工具,以及我们正在开发的一些东西,它们对我们开发流程的转变起到了相当关键的作用。

[19:45] **SPEAKER_02:** So yeah, can't wait to talk about you with them, but not today, sadly. Yeah, when you go back to just the way that design and development are blurring more, I think there's a lot of stuff going on there. I think product is also blurring. I think there's a lot of stuff going on with design and development and potentially even parts of research. All of this is becoming less distinct and it's all kind of coming together more.

> 所以是的,我等不及要跟你们聊这些了,但很遗憾,不是今天。是的,回到设计和开发越来越模糊这件事本身,我觉得这里面发生了很多事情。我觉得产品这个环节也在变模糊。我觉得设计、开发,乃至可能包括研究的一部分,都发生着许多变化。所有这些之间的界限都变得不那么分明,一切都在更多地融合到一起。

[20:08] **SPEAKER_02:** I think this is happening before AI, but it's happening even more with AI. There's something about AI that empowers generalist behavior. I will say that I think that the models today are better at the earlier phases of development than they are at like late stage codebases. So if you have an established codebase, I think you're going to get less out of, uh, AI development tools as they currently exist than if you're at the very start. So I think that everything's better suited for prototyping and sort of like zero to one than it is from one to a hundred, uh, at this current moment.

> 我觉得这在 AI 出现之前就已经在发生了,但有了 AI 之后它发生得更厉害。AI 身上有某种东西,能够赋能「通才式」的行为。我要说,我觉得如今的模型在开发的早期阶段表现得比在那种后期成熟代码库上更好。所以如果你有一个已经成型的代码库,我觉得就现有的 AI 开发工具而言,你从中能获得的收益会比你在最起步阶段时更少。所以我认为,就当下这个时刻而言,一切都更适合做原型、做所谓的从零到一,而不是从一到一百。

[20:41] **SPEAKER_02:** But you know, in a week this could change.

> 但你知道,一周之内这一切都可能改变。

[20:44] **SPEAKER_04:** Yeah, it changes so fast. Yes. Um, I mean, related to that, how do you expect user interfaces to change, uh, over the next couple of years? And it feels like chat has kind of become a lot of the dominant, uh, interface paradigm, but I don't know, it feels like there's got to be something better that, you know, that comes along, right?

> 是的,它变得太快了。是的。嗯,我是说,与此相关,你预计用户界面在接下来这几年会怎么变化?感觉聊天在很大程度上已经成了主导的界面范式,但我不知道,感觉总该有某种更好的东西会出现吧,对吧?

[21:00] **SPEAKER_02:** Yeah, I think that it feels intuitively like we're in the MS-DOS era, uh, of AI right now. And that, you know, if you look back 10 years from now, everyone's going to go, can you believe that we just had this chat box? And yet I think the problem of how do you show users all the things that are possible to do with these models is a very hard challenge. And, um, there's something about the experiments that have worked there that's very interesting. So for example, look at mid journey, you know, they started off in discord where you can rapidly see all the other things that people are doing.

> 是的,直觉上感觉我们现在正处于 AI 的 MS-DOS 时代。而你知道,如果从十年后回望,大家都会说,真不敢相信我们当时竟然只有这么一个聊天框?然而我觉得,如何向用户展示这些模型能做的所有事情,是一个非常困难的挑战。而且,那些在这方面取得成功的实验里有某种很有意思的东西。比如说,看看 Midjourney,你知道,他们一开始是在 Discord 上做的,在那里你可以迅速看到其他所有人都在做什么。

[21:36] **SPEAKER_02:** And that was in many ways, a way to show people what's possible or even Meta's new AI app. Uh, there's been a lot of press cycle and whatnot about the public aspect of people sharing accidentally things that are quite private. But the flip side of that is you actually learn what you can do. And so I think that's been underexplored, uh, in the media. So I think that there's this problem that people have not solved of like, how do you expose capabilities of these models?

> 这在很多方面是一种向人们展示什么是可能的方式,甚至 Meta 新的 AI 应用也是如此。呃,关于人们不小心把相当私密的东西公开分享出去这个公共层面的问题,有过很多轮媒体报道之类的。但它的另一面是,你其实能借此了解到你能做些什么。所以我觉得这一面在媒体上被探讨得不够。因此我认为存在这样一个人们尚未解决的问题:你要如何把这些模型的能力展现出来?

[22:04] **SPEAKER_02:** And there's so much that needs to be developed and work through there. Uh, yeah, I think there's a lot to come on top of that. Everything will be more contextual, uh, AI as you blend it in to different applications. That's a really interesting layer to think about. And on top of that, we're going to have so many new surfaces as well.

> 这里面还有太多东西有待开发、有待梳理清楚。呃,是的,我觉得在此之上还有很多东西即将到来。当你把 AI 融入到不同的应用中时,一切都会更具情境性(contextual)。这是一个非常有意思、值得思考的层面。而在此之上,我们还会拥有非常多新的界面载体(surface)。

[22:24] **SPEAKER_02:** The surfaces that will exist are not going to be just like your phone and your laptop. And your tablet and the thing, you know, it's going to be glasses. Uh, we're going to see much more, um, in terms of, uh, different types of displays that exist throughout your life. So the surfaces are going to multiply, AI will have context, all of it will be a layer you have to intersperse. And that is a really interesting challenge for design of how do you reconcile all that, keep it consistent and actually be able to navigate that whole broad spectrum that people expect you to show up on.

> 未来会存在的载体不会只是你的手机、你的笔记本电脑、你的平板电脑之类的东西,你知道,还会有眼镜。呃,我们会看到多得多的、贯穿你生活方方面面的各种不同类型的显示设备。所以载体会成倍增加,AI 会具备情境,所有这些都会成为你不得不穿插进去的一层。而这对设计来说是一个非常有意思的挑战:你要如何把这一切协调起来,保持一致性,并真正能够驾驭人们期望你出现的整个广阔谱系。

[22:59] **SPEAKER_03:** YC's next batch is now taking applications. Got a startup in you? Apply at YCombinator.com slash apply. It's never too early and filling out the app will level up your idea.

> YC 的下一期正在接受申请。你心里有个创业的念头吗?到 YCombinator.com/apply 提交申请吧。永远都不算太早,而且填写申请表本身就会让你的想法更上一层楼。

[23:11] **SPEAKER_03:** Okay, back to the video.

> 好,我们回到视频。

[23:13] **SPEAKER_04:** How many of you, um, consider yourselves to be researchers or have done research work? Yeah, it's a lot of people in this audience here. And I know you've done this internally, you know, at Figma and building your own models. Um, what is the role of design? Um, in, in research and the research work that you've done, um, and you know, what are some of the design decisions that go into actually like making them better and making them work really well?

> 你们当中有多少人认为自己是研究人员,或者做过研究工作?是的,现场观众里有很多人。而且我知道你们在内部也做过这件事,你知道,在 Figma 内部构建你们自己的模型。嗯,设计在研究中扮演什么角色?在你们做过的研究工作中,嗯,你知道,为了真正让它们变得更好、让它们运作得非常出色,其中涉及哪些设计决策?

[23:38] **SPEAKER_02:** I mean, I think that a lot of researchers, uh, are sort of trained in an academic environment and come at problems as abstractions and try to think very generally. And I think if in some research, like if you're doing pure math, like keep going, that is definitely the way to approach it. If you're doing more research that's applied, uh, for example, in AI, I, I really do think that thinking like a designer can be helpful and working with designers can be helpful too. We found, for example, that embedding designers into our research teams, because obviously we're doing a lot of work on how do we make better AI tools for designers, uh, is been critical because researchers need that intuition of how designers think and without actually having that close collaboration, it really doesn't work. Now you might say in response, well, yeah, that's nice, but you're building for designers.

> 我是说,我觉得很多研究人员是在学术环境里训练出来的,把问题当作抽象来对待,并试图非常一般化地去思考。我认为,在某些研究中,比如如果你在做纯数学,那就继续这么做,那绝对是正确的方式。但如果你做的是更偏应用的研究,呃,比如在 AI 领域,我是真心认为,像设计师那样思考会有帮助,和设计师合作也会有帮助。举个例子,我们发现把设计师嵌入到我们的研究团队里非常关键——因为很显然我们在大量研究如何为设计师打造更好的 AI 工具——因为研究人员需要那种关于设计师如何思考的直觉,而如果没有真正的紧密协作,这真的行不通。现在你也许会回应说,嗯,是啊,这挺好的,但你们本来就是在为设计师做产品。

[24:35] **SPEAKER_02:** My maybe response back would be, well, uh, it's, it's the case that designers have this mindset of you're building for an audience. Maybe it's a general audience, maybe it's a specific audience, but audience has a problem or a set of problems they're trying to solve. And that sort of thinking, I think is very useful to bring into the research context. And also qualitative research needs to pair with, uh, more deep AI research as well. The more that you can actually surface through qualitative methods, what people are actually trying to do and how they perceive and think the more, uh, you can advance.

> 我可能会这样回应:嗯,呃,事实是,设计师有一种思维方式,就是你在为某个受众做东西。也许是一般大众,也许是特定人群,但受众有一个或一组他们试图解决的问题。我认为把这种思维带入研究情境中非常有用。而且定性研究也需要与更深入的 AI 研究相配合。你越是能通过定性方法真正揭示出人们究竟想做什么、他们如何感知和思考,你就越能取得进展。

[25:13] **SPEAKER_02:** So yeah, I guess my push for anyone who's coming for more of a research background would be go get in the field, go talk to people because you'll learn from it and it'll actually make you go faster. And some of the ways that designers have learned and some of the tools that designers have are likely useful for you.

> 所以是的,我想对任何研究背景更浓的人的建议是:走进现场,去和人们交谈,因为你会从中学到东西,而且这实际上会让你走得更快。设计师所积累的一些方法,以及设计师所拥有的一些工具,很可能对你有用。

[25:30] **SPEAKER_04:** Yeah. It's, it's like that Steve jobs quote that, you know, design isn't just how it looks, it's how it works. And, um, it feels like, you know, when you're building models and doing research, you're trying to make a thing like that is the, how it works, you know, you're trying to define that. And that is the core function of a designer that may not be obvious to how people view them from the outside. It seems.

> 是的。这就像史蒂夫·乔布斯那句话说的,你知道,设计不只是它看起来什么样,而是它如何运作。而且,嗯,感觉,你知道,当你在构建模型、做研究时,你正试图做出那样一种东西——那就是「它如何运作」,你知道,你正试图去定义它。而这正是设计师的核心职能,只是从外部看待他们时,人们可能并不容易察觉到这一点。看起来是这样。

[25:50] **SPEAKER_04:** I'm curious, what'd you think the role of designer looks like over the next decade? It seems like it's shifting a lot and, you know, design and development seems to be, you know, drawing closer together. And there's all this research where design can be involved. How do you think that role changes?

> 我很好奇,你觉得设计师这个角色在未来十年会是什么样子?它似乎正在发生很大的转变,而且你知道,设计和开发似乎正在越走越近。还有各种研究工作,设计都可以参与其中。你觉得这个角色会怎么变化?

[26:03] **SPEAKER_02:** I'm really excited about how this will evolve. I think that designers, uh, will have far more leverage in the future and the value of design will only continue to go up. I mean, your RFP, uh, request for proposal for designer founders, I think embodied this. You said, uh, designers need to be founders. We need to have folks that are designers step into the founder role and start companies.

> 我对它将如何演变感到非常兴奋。我认为设计师在未来会拥有大得多的杠杆效应,设计的价值只会持续上升。我是说,你们那份 RFP,呃,针对设计师创始人的招募倡议,我觉得就体现了这一点。你说,呃,设计师需要成为创始人。我们需要让身为设计师的人走进创始人的角色,去创办公司。

[26:31] **SPEAKER_02:** I know that it's been, uh, looking back, you know, you got Brian Chesky, you got Kari at Linear. We have so many designer founders that you can point to now and say, wow, uh, these folks are really successful and are, are killing it. But I think that the number of designer founders will multiply. I think the number of designers that are leading large areas and sort of GMs will grow as well. And in general.

> 我知道,呃,回头看,你知道,有 Brian Chesky,有 Linear 的 Kari。如今我们能举出这么多设计师创始人,可以指着他们说,哇,呃,这些人真的非常成功,干得非常出色。但我觉得设计师创始人的数量将会成倍增长。我觉得那些领导大块业务、担任类似总经理(GM)角色的设计师数量也会增长。总的来说。

[26:57] **SPEAKER_02:** Yeah. Uh, designers will be looked to as experts inside of companies that in sort of the same way that you might have a writer today who is the expert and like the best writer in the company or the best editor, uh, but everyone has a word processor and can write. You'll have a designer who might be the best at problem solving and thinking through how do I actually craft a solution and explore this idea maze and figure out which direction to go, create a system around it. But I think most everyone in the company. We'll be contributing to that process of design.

> 是的。呃,设计师会在公司内部被视为专家,就有点像今天你公司里可能有一位写作者,他是专家、是公司里最好的写手或最好的编辑,呃,但每个人都有文字处理软件、都能写字。你会有一位设计师,他也许最擅长解决问题、最擅长想清楚「我到底该如何打磨出一个解决方案、探索这座点子迷宫、弄清楚该往哪个方向走、并围绕它构建一套体系」。但我觉得公司里几乎每个人都会为这个设计过程做出贡献。

[27:30] **SPEAKER_02:** And so there'll be a lot of curation involved and a lot of leadership will be needed from designers.

> 因此其中会涉及大量的甄选与策展工作,也会需要设计师发挥大量的领导作用。

[27:35] **SPEAKER_04:** So they don't have to step up. I'm curious. What are some of the most interesting ways you guys are using, uh, AI internally at Figma?

> 所以他们得挺身而出。我很好奇,你们在 Figma 内部使用 AI 的方式中,有哪些是最有意思的?

[27:40] **SPEAKER_02:** Yeah. I mean, can't talk about it all. Like I said, uh, since some of it is like products that we'll be releasing, but maybe one thing I'll say is on the designer embedded in the research side point, uh, it's been fascinating to see just how important it is for designers to. Uh, contribute on evals. So if you think about it, uh, as you're doing, uh, developing a model or you're developing research ideas, you have to have good evals and usually the researchers are the ones building those.

> 是的。我是说,不能全都讲。就像我说的,呃,因为其中有些是我们将要发布的产品,不过也许我能说的一件事,是回到「把设计师嵌入研究一侧」这个点上,呃,看到设计师在评估(evals)上做出贡献究竟有多重要,这一点非常引人入胜。所以你想一下,呃,当你在开发一个模型、或者在打磨研究思路时,你必须要有好的评估基准,而通常构建这些的是研究人员。

[28:11] **SPEAKER_02:** And I think that's kind of just the wrong model for us, at least designers. My point of view is that they should be contributing to evals, product people, they should be contributing to evals. It's not something that you need your engineers and your researchers to do because they probably have. They have less understanding of the end user, less contact with end user than your designers do your product people do. So, uh, as you're designing these models, I think evals become more important too.

> 而我觉得,至少对我们来说,那种模式有点不对——设计师也应该参与。我的观点是,设计师应该为评估做贡献,产品人员也应该为评估做贡献。这并不是那种非得让你的工程师和研究人员来做的事情,因为他们对最终用户的理解可能更少、和最终用户的接触也比你的设计师、你的产品人员更少。所以,呃,当你在设计这些模型时,我觉得评估也变得越来越重要。

[28:35] **SPEAKER_04:** And I guess if you were in your twenties today, um, what are some of the skills or tools that you would focus on becoming great at in this, you know, to be successful in this new AI world?

> 那我想,如果你现在正值二十几岁,嗯,你会专注于把哪些技能或工具练到炉火纯青,以便在这个新的 AI 世界里取得成功?

[28:44] **SPEAKER_02:** The setup of the question is that it's like you should kind of do different things than you did in the past. And that's probably true. But. I would start by saying that I think that the stuff that, you know, folks have done historically in order to get really good at thinking and work through problems with critical thoughts, uh, and learn broadly so they can make mental connections, those are still important.

> 这个问题的前提设定是,你应该去做一些跟过去不太一样的事情。这大概是对的。但是,我想先说,我觉得那些人们历来为了把思考练得非常出色、用批判性思维去梳理解决问题、以及广泛学习以便在头脑中建立联系而做的事情,这些依然重要。

[29:10] **SPEAKER_02:** So I think learning about as many different areas as you're curious about deeply, uh, and trying to experience the world, uh, making sure you're still relating to people like those are pretty core things that you should still do. One thing that I'm worried about is, you know, I, I think, uh, a lot of people in their twenties these days, uh, apparently, according to the stats are dating less. Maybe that's true. Maybe it's not true. Y'all can tell me later.

> 所以我觉得,深入地去了解尽可能多的、你感兴趣的不同领域,呃,并努力去体验这个世界,呃,确保你依然在与人建立联系——这些都是你依然应该去做的相当核心的事情。有一件让我担心的事是,你知道,我觉得,呃,如今很多二十几岁的人,呃,据统计数据显示,似乎约会得更少了。也许这是真的,也许不是真的,你们可以待会儿告诉我。

[29:39] **SPEAKER_02:** Uh, but if you think about the future, it'd be so easy to just go talk to your AI model all day. Maybe that gives you a sense of social connection. Like I would highly advise you don't do that. Uh, I would highly advise that y'all date. Uh.

> 呃,但如果你想想未来,整天只是去跟你的 AI 模型聊天会变得太容易了。也许那会给你一种社交连接的感觉。我强烈建议你别那么做。呃,我强烈建议你们去约会。呃。

[29:54] **SPEAKER_02:** If you're in that cohort, um, and I even go so far as to say, this is less to comment about the products that are in this category of the past, but more about what the future could hold. Um, I, I think AI boyfriends and girlfriends, if developed and allowed to exist, uh, is a societal self-owned. I think it's like actively poisonous to society if, um, this becomes the primary, a primary mode of relationship. There's a lot of things that we need to talk about there and have a pretty broad society level discussion about.

> 如果你属于那个群体,嗯,我甚至要说——这与其说是在评价过去这一类别里已有的产品,不如说更多是在谈论未来可能会怎样。嗯,我觉得 AI 男朋友和女朋友,如果被开发出来并被允许存在,呃,是一种社会层面的自我伤害(self-own)。我觉得,如果这变成主要的、一种主要的关系模式,那它简直是在主动毒害社会。关于这一点有很多事情我们需要讨论,需要在相当广泛的社会层面上展开对话。

[30:24] **SPEAKER_04:** Well, I don't want to leave it on that before we open up to questions, but maybe, um, you know, before, uh, we can open up some questions here as people kind of line up, I'm curious, um, what was the most fun period in the history of building Figma for you?

> 好吧,在我们开放提问之前,我不想就停在这个话题上,但也许,嗯,你知道,在,呃,我们开放现场提问、大家开始排队的时候,我很好奇,嗯,在打造 Figma 的历程中,对你来说最有趣的时期是哪一段?

[30:39] **SPEAKER_02:** Uh, you know, maybe it's like the answer everyone's expecting, but it's true. It's right now. Uh, we have like so many things we can do the most brilliant people around to do them with. I love my team. I love the problem set that we have.

> 呃,你知道,也许这是大家都预料到的答案,但它是真的。就是现在。呃,我们有太多可以做的事情,身边又有最杰出的人才和我们一起去做。我爱我的团队。我热爱我们面对的这一组问题。

[30:53] **SPEAKER_02:** Uh. Um, some companies, they go, uh, forward and they kind of tap out and they don't have any more ideas. Like the number of ideas that we have right now has grown so much. There's so much we can do. And there's so much people are asking of us and it's more about, okay, how do we make sure we do the right things?

> 呃。嗯,有些公司,它们一路,呃,往前走,然后就有点后劲不足、再也没有更多的点子了。而我们现在拥有的点子数量增长了这么多。有太多事情是我们可以去做的。人们对我们提出的诉求也太多了,所以问题更多地在于:好,我们怎么确保自己做的是正确的事情?

[31:10] **SPEAKER_02:** And that's a fascinating and really fun place to be. Cool. Let's open up to some questions.

> 而这是一个引人入胜、真正有趣的处境。很好。我们来开放提问吧。

[31:15] **SPEAKER_01:** I'm a founder, product engineer, software engineer, everything, solo entrepreneur at the same time. Awesome. And recently I have started using Cursor AI to handle business. Awesome. So both coding and design, even like down to pixel level details.

> 我是一名创始人、产品工程师、软件工程师,什么都干,同时也是一个单人创业者。太棒了。最近我开始用 Cursor AI 来处理业务。太棒了。也就是编码和设计两方面都用,甚至细到像素级别的细节。

[31:28] **SPEAKER_01:** So what do you think about Cursor AI? Is this Cursor AI can become your, one of your competitors? And at the same time, uh, I just recently discovered a tool called PenPod or giving like developers more control through open source, uh, self-hosted options. What do you think Figma should, uh, move toward being more open and developer friendly to catch up with the trend of many software engineers become product engineer in the future? And more and more solo entrepreneur using Cursor AI to create product in the future?

> 那么你怎么看 Cursor AI?这个 Cursor AI 会不会成为你们的、你们竞争对手之一?与此同时,呃,我最近发现了一个叫 PenPod 的工具,它通过开源、呃,自托管的选项给开发者更多的控制权。你觉得 Figma 是否应该,呃,朝着更开放、更对开发者友好的方向发展,以跟上未来许多软件工程师转型为产品工程师、以及越来越多单人创业者用 Cursor AI 来打造产品这一趋势?

[31:56] **SPEAKER_01:** Yeah, I think it's a great question.

> 是的,我觉得这是个很好的问题。

[31:58] **SPEAKER_02:** Um, and actually just was, uh, able to run to Michael backstage. That was good to see him. Uh, I think that when it comes to AI generation, you know, if you take a step forward from, okay, I generated something. The next question is, okay, how to make it good. And, you know, there's different ways to do that.

> 嗯,其实我刚才,呃,在后台还遇到了 Michael,很高兴见到他。呃,我觉得,当涉及 AI 生成时,你知道,如果你从「好,我生成了某个东西」再往前迈一步,下一个问题就是,好,怎么把它做好。而你知道,做到这一点有不同的方式。

[32:19] **SPEAKER_02:** Uh, you can be writing code and then going into your browser and cutting code into your browser. And then kind of having that loop, that's a very structural way to think, um, other people prefer to think in a more free form way, uh, with make, we're trying to enable that, uh, in a way that's visual first, rather than code first, you can still get to the code. Um, but I really don't think of cursor as a competitor. Uh, I think of them as someone that we, we still want to start MCP server to explicitly make it so that you can get your designs in a cursor and windsurf and all these other NBS code, you know, all these great tools faster. So.

> 呃,你可以一边写代码,一边切到浏览器里、把代码贴进浏览器,然后形成那样一个循环,这是一种非常结构化的思考方式,嗯,另一些人则偏好以更自由的形式来思考,呃,借助 Make,我们正试图去实现这一点,呃,以一种视觉优先而非代码优先的方式,你仍然可以拿到代码。嗯,但我真的不把 Cursor 看作竞争对手。呃,我把他们看作是这样一个对象:我们依然想推出 MCP 服务器,明确地让你能够更快地把你的设计导入 Cursor、Windsurf 以及所有这些其他的,你知道,VS Code 等等这些很棒的工具里。所以。

[32:52] **SPEAKER_02:** There's a lot of really new workflows that are established. And like I said, if the differentiators design, then your first generation, your one shot is probably not the thing that's going to win. So I'd encourage you to think a little bit further than that in terms of open source, we actually just announced today, uh, the acquisition of a payload, uh, CMS, which is an open source, uh, project. And uh, I'm really excited about what we can do there and how we can support open source more.

> 有很多真正全新的工作流正在被确立起来。就像我说的,如果差异化优势是设计,那么你的第一次生成、你的「一次成型」很可能并不是最终会取胜的那个东西。所以我想鼓励你把眼光放得比那更远一点。关于开源,我们其实今天刚刚宣布,呃,收购了 Payload,呃,一款 CMS,它是一个开源、呃,项目。而,呃,我对我们能在那上面做些什么、以及我们能如何更多地支持开源感到非常兴奋。

[33:18] **SPEAKER_09:** Thank you. Hi Dylan. Um, my name is Charlie Fearborn. Uh. I grew up in San Francisco.

> 谢谢。你好 Dylan。嗯,我叫 Charlie Fearborn。呃。我在旧金山长大。

[33:23] **SPEAKER_09:** Um, and I graduated last year from USC and computer science and game design best major ever. So it was cool to hear about the games roots of Figma.

> 嗯,我去年从南加州大学(USC)毕业,专业是计算机科学和游戏设计,史上最棒的专业。所以听到 Figma 的游戏渊源感觉很酷。

[33:31] **SPEAKER_02:** Yeah, we cut it off early, but Evan is also like really was really deep in game design and it's a hard, hard industry, but it's awesome that you're doing it.

> 是的,我们刚才提前打住了那个话题,但 Evan 其实也曾经非常深入地钻研游戏设计,这是个非常非常艰难的行业,但你在做这件事真的很棒。

[33:40] **SPEAKER_09:** Um, I have kind of a more personal question for you. Um, uh, what is the meaning of life?

> 嗯,我有一个比较私人一点的问题想问你。嗯,呃,生命的意义是什么?

[33:45] **SPEAKER_02:** Um, mean of life. I think, uh, you know, seek out how to explore consciousness. Yeah. More as much as you can, uh, uh, share love with others and make sure that, um, you feel fulfilled and the other people around you, uh, are fulfilled and happy, um, at the end of the day. And I think that, uh, that can be something you do on a micro level in your local community, a macro level at scale.

> 嗯,生命的意义。我觉得,呃,你知道,去探寻如何探索意识。是的,尽你所能地多去探索,呃,呃,与他人分享爱,并确保,嗯,你感到充实满足,而你周围的其他人,呃,归根结底也感到充实、幸福。我觉得,呃,这件事你可以在微观层面上、在你身边的社区里去做,也可以在宏观层面上、大规模地去做。

[34:15] **SPEAKER_02:** Doesn't matter. Uh, as long as you're living true to your internal values, I think that, uh, you're leading a fulfilling life. Yeah.

> 无所谓在哪个层面。呃,只要你活得忠于自己内心的价值观,我觉得,呃,你就在过一种充实的人生。是的。

[34:22] **SPEAKER_08:** Hey Dylan, thank you so much. Um, I was wondering as a designer, are there any specific design principles that you love and use? What do you think a lot of like builders or companies get wrong or like sometimes even completely ignore?

> 嘿 Dylan,非常感谢。嗯,我想问,作为一名设计师,有没有什么你特别喜欢并会使用的具体设计原则?你觉得很多创造者或公司在哪些方面做错了,或者有时甚至完全忽视了什么?

[34:33] **SPEAKER_02:** I think the biggest one that I repeat all the time at Figma, uh, which is not my own, it's, you know, has existed for decades is keep the simple things simple and make the complex things possible. Uh, there's always a wide range of things that you want to be able to enable, but if you try to do all of them. Yeah. Yeah. Yeah.

> 我觉得最大的一条,也是我在 Figma 一直不断重复的,呃,它不是我原创的,你知道,已经存在了几十年,那就是:让简单的事情保持简单,让复杂的事情成为可能。呃,你总会想要支持一大堆各式各样的功能,但如果你试图把它们全都做进去。是的。是的。是的。

[34:53] **SPEAKER_02:** And then there's a, there's a huge, um, burden of of your product not being approachable, uh, and not being obvious or intuitive how to use, you're, you're kind of messing up. So I think you have to figure out how to do both, but you start with making the simple things simple.

> 那就会带来一个巨大的,嗯,负担——你的产品变得不平易近人,呃,让人看不出、也想不明白该怎么用,那你其实就搞砸了。所以我觉得你必须想清楚如何两者兼顾,但你要从「让简单的事情保持简单」开始。

[35:07] **SPEAKER_08:** Thank you.

> 谢谢。

[35:08] **SPEAKER_07:** Uh, I'm Michael, I study HCI and computer science at Columbia. Um, say there's a founder you really respect and you finally landed an enterprise contract and have a decent amount of traction on the project that you've been building with a bunch of friends what would be the most polite way to show them the product and ask them to be an angel investor?

> 呃,我是 Michael,我在哥伦比亚大学学习人机交互(HCI)和计算机科学。嗯,假设有一位你非常尊敬的创始人,而你终于拿下了一份企业合同,你和一群朋友一起做的这个项目也有了相当不错的进展,那么向他们展示产品、并请他们做天使投资人的最礼貌的方式会是什么?

[35:28] **SPEAKER_02:** i would send them a loom over email um so that way you know it's got an acing component since time is sometimes hard to find uh they can watch it um and if you want to really pique their interest mutual connections help uh but like i said earlier cold emails work too expect a cold email okay i'm looking forward to it an honor too hey dylan um i love your shoes first of all but

> 我会通过邮件给他们发一段 Loom 录屏,嗯,这样一来,你知道,它有一种异步(async)的成分,因为时间有时很难挤出来,呃,他们可以自己找时间看。嗯,如果你真想勾起他们的兴趣,共同的人脉会有帮助,呃,但就像我前面说的,陌生邮件也管用。等着收你的陌生邮件哦。好的,我很期待。也很荣幸。嘿 Dylan,嗯,首先我很喜欢你的鞋子,不过——

[35:56] **SPEAKER_10:** uh thank you of course um but you said you noticed behaviors when deciding what to productize and i can very clearly see that i was using slides for classes i'm using figma for slides for class before you guys drop slides made it easier using block layers for social media graphics for my friend and then buzz made that so much easier so i guess my question is how do you watch how people repurpose the tools and what kind of structure do you use for these emerging use cases?

> 呃,当然,谢谢。嗯,但你说过你们在决定把什么产品化时会去留意用户的行为,我自己就能非常清楚地感受到这一点:我以前用幻灯片来做课堂展示,在你们推出 Slides 之前我一直用 Figma 来做课堂幻灯片,Slides 让这件事更轻松了;我用图块图层为我朋友做社交媒体图片,然后 Buzz 又让那件事轻松了太多。所以我想我的问题是,你们是怎么观察人们如何「另作他用」地重新利用这些工具的?针对这些新兴用例,你们采用什么样的机制?

[36:18] **SPEAKER_02:** for these emerging use cases it's always a mix of signals right you have to do everything from like watching support requests to qualitative interviews sitting with people and watching how they work looking at the data and you know actually doing data science analysis on it you know looking at what people are saying on social media and more but it's kind of you digest all those signals and you build some intuition around it and hypotheses you can test so yeah it's kind of art plus science but you have to combine a lot of methods i think awesome thank you

> 针对这些新兴用例,它始终是多种信号的组合,对吧,你得把从观察支持工单,到做定性访谈、坐在用户身边看他们如何工作,到查看数据、你知道,真正对它做数据科学分析,到你知道,关注人们在社交媒体上说什么等等所有这些事情都做一遍。但归根结底是你把所有这些信号消化吸收,围绕它建立起某种直觉,以及一些你可以去验证的假设。所以是的,这算是艺术加科学,但我觉得你必须把很多方法结合起来。太棒了,谢谢。

[36:48] **SPEAKER_10:** you

> (致谢)谢谢你。

[36:48] **SPEAKER_06:** thank you hi uh thanks very much for the talk um so right now you're helping designers in a huge breadth of industries when you just started with the cold emailing etc how did you go about with defining rice ap was it very broad as today or did you start focused on one industry?

> 谢谢你。你好,呃,非常感谢这场分享。嗯,现在你们在帮助横跨极其广泛行业的设计师,而当你最初以陌生邮件之类的方式起步时,你们是怎么去界定理想客户画像(ICP)的?是像今天这样非常宽泛,还是一开始就聚焦于某一个行业?

[37:04] **SPEAKER_02:** no we really started focused on product design and uh for digital products uh where and i think even more narrowly where people cared about design uh if i'm gonna be totally honest rather than like you know the broad world uh it seemed like it'd be an easier sell but yeah i think it required um a lot of sort of slimming down of our ambition to be able to state that clearly you know i started off saying we're gonna do everything and thankfully the team pushed back and so it got us to here with the ambition of later on doing everything but

> 不,我们真的是从聚焦于产品设计起步的,呃,是面向数字产品的,呃,而且我觉得范围甚至更窄——聚焦于那些真正在乎设计的人身上,呃,如果我完全诚实地说,而不是面向,你知道,那种宽泛的大众,呃,这样看起来会更好卖一些。但是的,我觉得为了能把这一点讲清楚,它需要,嗯,把我们的野心大幅精简下来。你知道,我一开始说的是我们要做所有的一切,幸好团队顶了回来,所以才把我们带到了今天这一步——同时怀着日后要做所有事情的野心,不过——

[37:41] **SPEAKER_00:** i'm glad we started more narrowly hi um so my background besides being like a cs major and whatnot i'm also in traditional art cool um where perhaps ai is not necessarily as popular as the moment um so i guess my question is just how is figma navigating like ethical challenges of ai and design and like incorporating ai into the products that you are you have available yeah there's so

> ——我很庆幸我们是从更窄的范围起步的。你好,嗯,我的背景除了是计算机科学专业等等之外,我也涉足传统艺术。很酷。嗯,在传统艺术领域,AI 或许并不像当下这么受欢迎。嗯,所以我想我的问题就是,Figma 是如何应对 AI 与设计的伦理挑战,以及把 AI 融入你们现有产品这件事的?是的,有很——

[38:10] **SPEAKER_02:** many different ethical challenges you could consider you know everything from uh okay you're doing some inference is it heating up the planet uh to the questions of um okay are these models regurgitating something they've seen elsewhere and beyond and so i think you have to be very clear about like what you're trying to solve for but yeah it's a maybe a uh sort of escape answer right now a lot of the work we're doing uh is actually with third-party models and so that's something we have less control over um as we do more things in-house i think these questions are very relevant and things are going to be a little bit more complicated and i think that's something that's that we'll have to wrestle with like the art world has hi dylan uh i'm an hci researcher and

> ——有非常多不同的伦理挑战你可以去考量,你知道,从,呃,好,你在做某种推理,它是不是在给地球升温?呃,到那些问题,嗯,好,这些模型是不是在把它们在别处见过的东西照搬吐出来?等等等等。所以我觉得你必须非常清楚你到底想解决的是什么。但是的,现在这也许算是一个,呃,有点回避性的回答:我们做的很多工作,呃,其实用的是第三方模型,所以那是我们控制力较弱的部分。嗯,随着我们越来越多地在内部自研,我觉得这些问题就会非常相关,情况也会变得更复杂一些,我觉得这是我们将不得不去搏斗、去权衡的东西,就像艺术界一直在面对的那样。你好 Dylan,呃,我是一名 HCI 研究者,而且——

[38:54] **SPEAKER_05:** a design founder and as we've been kind of like thinking about interfaces and how we talk to ai it seems that we tend to anthropomorphize things it tends to be that these are probabilistic and we can't design them explicitly how we did with like previous hardware do you think of ai human interaction as necessarily a tool or how do you kind of like build a mental model around this?

> ——也是一名设计师创始人。当我们一直在思考界面、思考我们如何与 AI 对话时,似乎我们倾向于把事物拟人化,而这些东西往往是概率性的,我们没法像过去对待硬件那样明确地去设计它们。你是把 AI 与人的交互必然地看作一种工具吗,还是说你是怎么围绕这一点建立一套心智模型的?

[39:13] **SPEAKER_02:** model around this i think that there's uh sort of where things are at now where they're going and you have to kind of consider both i think that uh there's an interesting split maybe between people that come from a materialist worldview and by that i don't mean like they're going and buying stuff all the time i mean the world view of materialism is one of uh consciousness arises from matter and then on the opposite side side of the spectrum is like religious mindsets where people go of course that's wrong like there's god god is great everyone has a soul ai doesn't have a soul obviously it's like a computer um and so the those are like fundamentally at odds and uh my prediction is that we'll probably see an increase in people projecting consciousness onto ai whether or not that's the right uh thing that you know you agree with or don't agree with i think that the number of people that will do that will increase um i think it leads to some uh very hard to wrestle with territories and so yeah i've been thinking a lot about that and then in terms of what that means for hci or uh whatever you want to call it uh i i think that that's a very underexplored question and i'm excited to see what you do with it i think we're at time sadly um but i just want to thank everybody for coming and uh wish you all the best of luck with whatever path to pursue

> 围绕这一点建立心智模型——我觉得有,呃,事情当下所处的状态、以及它们将往哪里去,你得把这两者都考虑进去。我觉得,呃,在持有唯物主义世界观的人之间也许存在一种有趣的分野——我说唯物主义,不是指他们成天去买东西(注:materialist 也有「物质主义者」之意),我指的是唯物主义那种世界观,认为意识源自物质;而在光谱的另一端则是宗教式的思维,人们会说,那当然是错的,有上帝啊,上帝是伟大的,每个人都有灵魂,AI 显然没有灵魂,它就是台电脑而已。嗯,所以这两者根本上是相互对立的,而,呃,我的预测是,我们大概会看到越来越多的人把意识投射到 AI 身上。无论那到底对不对、你知道,无论你是否认同,我觉得会这么做的人数都会增加。嗯,我觉得这会引向一些,呃,非常难以拿捏、难以搏斗的领域。所以是的,我一直在大量思考这个问题。至于它对 HCI、或者呃你想怎么称呼它都行,意味着什么,呃,我觉得那是一个非常有待探索的问题,我很期待看到你会在这上面做出什么。很遗憾,我觉得我们时间到了。嗯,但我只想感谢大家的到来,呃,祝愿你们无论选择哪条道路都一切顺利、好运相伴。
