# 全文转录 · AI 创业公司的 FDE(前置部署工程师)实战手册

> ▶ [YouTube](https://www.youtube.com/watch?v=Zyw-YA0k3xo) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/Zyw-YA0k3xo.md) &nbsp;·&nbsp; The FDE Playbook for AI Startups with Bob McGrew

> 中英对照 · 每段英文原文下附中文翻译

[00:00] **SPEAKER_04:** With AI agents, there is no incumbent product. And so that I think is why you're seeing the FDE model taking off because there's so much product discovery to do. You want to drive the contract size up. You're doing more and more valuable work for this customer and also for future customers. The FDE model effectively is doing things that don't scale at scale.

> 在AI智能体领域,并不存在既有的现成产品。我想这就是为什么你会看到FDE(前沿部署工程师)模式正在兴起——因为有太多的产品探索工作要做。你希望把合同金额做大。你在为这个客户、也在为未来的客户做越来越有价值的工作。FDE模式本质上就是在规模化地去做那些原本无法规模化的事情。

[00:29] **SPEAKER_02:** Hello and welcome back to another episode of The Light Comb. Gary wasn't feeling great today and couldn't be here, but we're thrilled to be joined by Bob McGrew. Bob was an early engineer at PayPal, an early executive at Palantir, and was recently chief research officer at OpenAI, where he led the development of ChatGPT, GPT-4, and the O1 reasoning model. Now he's exploring the future of AI and has an exciting new role with the US Army that we'll get to in a bit.

> 大家好,欢迎回到《The Light Comb》的又一期节目。Gary今天身体不太舒服没能到场,但我们非常高兴请到了Bob McGrew。Bob曾是PayPal的早期工程师、Palantir的早期高管,最近还担任OpenAI的首席研究官,在那里主导了ChatGPT、GPT-4以及o1推理模型的研发。如今他正在探索AI的未来,还在美国陆军担任一个令人兴奋的新职务,这个我们稍后会聊到。

[00:54] **SPEAKER_03:** Bob, thanks so much for being here. It's great to be here. So Bob, I've been particularly excited to sit down with you to talk about the forward deployed engineer model, because this is a topic that keeps coming up in our lives. It is a really hot topic in Silicon Valley right now, and especially among the AI agent companies that we've talked about on this podcast a lot. You were in the room when it all got started, and so you're exactly the right person to explain it.

> Bob,非常感谢你能来。很高兴来到这里。Bob,我一直特别期待能和你坐下来聊聊前沿部署工程师(FDE)模式,因为这个话题在我们的生活中不断出现。它现在是硅谷一个非常热门的话题,尤其是在我们这档播客里经常谈到的那些AI智能体公司当中。这一切开始时你就在现场,所以你正是解释这件事最合适的人。

[01:17] **SPEAKER_03:** You were actually telling me a funny story. You were at an AI conference that YC organized a few months ago, and you expected that all the founders would come up to you to talk to you about, you know, inventing ChatGPT. And instead, what all of these AI startup founders wanted to talk, was the Palantir forward deployed engineer model.

> 你其实还跟我讲过一个有趣的故事。几个月前你参加了一场YC组织的AI大会,你本以为所有创始人都会跑来跟你聊发明ChatGPT的事。结果这些AI初创公司创始人真正想聊的,却是Palantir的前沿部署工程师模式。

[01:36] **SPEAKER_04:** Well, and it's really true. It hasn't just been that one conference. As I've been advising startups this last year, I would say that a lot of them are pretty much exclusively trying to learn how the FD strategy works.

> 确实是这样。而且不只是那一场大会。在过去这一年里我为初创公司做顾问,我得说,他们中很多人几乎专门就是想弄明白FDE策略是怎么运作的。

[01:47] **SPEAKER_03:** Yeah. So this is an intense topic of fascination, and it's super timely because it's actually become, I think, the dominant way that the AI agent startups are organizing themselves. I was looking earlier today, and if you look at the YC job board, there's over 100 YC startups that are hiring for a job with the title forward deployed engineer, and up from basically zero three years ago. Perhaps before we get really into it, for anybody who doesn't already understand, can you just explain what a forward deployed engineer is and how it's relevant today?

> 是的。所以这是一个让人极其着迷的话题,而且非常应景,因为我认为它实际上已经成为AI智能体初创公司组织自身的主流方式。我今天早些时候查了一下,如果你看YC的招聘板,有超过100家YC初创公司在招聘职位名称为"前沿部署工程师"的岗位,而三年前这个数字基本为零。也许在我们深入之前,对于还不了解的人,你能不能先解释一下什么是前沿部署工程师,以及它为什么在今天如此重要?

[02:18] **SPEAKER_04:** So a forward deployed engineer is someone, typically technical and engineer, who sits at the customer site and fills the gap between what the product does and what the customer needs. And how does this play out in practice? You'll have a product. And you go to a new customer site, you start working with a new customer, and the problem that they want you to solve is not a problem that you've ever solved before, but you believe that it's one that with a little bit of work, maybe a lot of work, you can solve for this particular customer, and you'd be making a huge impact for them. You'd be delivering an outcome to them that would be extremely valuable for them.

> 前沿部署工程师是这样一个人,通常是技术人员、工程师,他常驻在客户现场,填补产品所能做的和客户所需要的之间的差距。这在实践中是怎么展开的呢?你有一个产品。你去到一个新客户现场,开始和新客户合作,而他们希望你解决的问题,是一个你从没解决过的问题,但你相信只要花点功夫、也许要花很多功夫,你就能为这个特定客户把它解决掉,并且你会为他们创造巨大的影响力。你会为他们交付一个对他们极其有价值的成果。

[02:56] **SPEAKER_04:** So you take the product that you have, and the FD with help from the product team figures out how to deliver that outcome, how to build that use case, how to deliver the piece of software that you've built in a way that actually works for the customer.

> 于是你拿着你手上现有的产品,FDE在产品团队的帮助下,想办法交付那个成果、构建那个用例、以一种真正对客户有效的方式交付你所构建的这块软件。

[03:10] **SPEAKER_03:** To go all the way back to the beginning, you were there at Palantir when this whole model that is now like exploding in Silicon Valley was invented. Can you talk about how it all got started?

> 我们把时间拉回到最开始。当这套如今在硅谷爆发的模式被发明出来时,你就在Palantir。你能讲讲这一切是怎么开始的吗?

[03:19] **SPEAKER_04:** The interesting way to think about the beginning of Palantir is that when we got started, the focus of our company was to build software for the intelligence community, specifically software for spies. And so one of the challenges in building software for spies. Is that I don't know any spies, you probably don't know any spies either. And if you happen to find a spy and you go and ask them, so what is it exactly that you do, they're not usually going to tell you. And so we had to take an approach that was sort of very unusual at the time, but effectively, we started by building a demo.

> 看待Palantir起点的一个有趣角度是:我们刚起步时,公司的重心是为情报界打造软件,具体来说是为间谍打造软件。而为间谍做软件的挑战之一在于:我不认识任何间谍,你大概也不认识任何间谍。而且就算你碰巧找到一个间谍,你去问他"你到底是做什么的",他通常也不会告诉你。所以我们不得不采取一种在当时相当不寻常的做法,基本上,我们从做一个demo开始。

[03:54] **SPEAKER_04:** And we took that demo to potential customers in the intelligence community. And, you know, Stefan Cohen very famously did this. He was one of the founders of Palantir, and he showed them the demo and he said, you know, well, what do you what do you think? And they said, well, this is terrible. This isn't related to what we do at all.

> 然后我们把那个demo拿给情报界的潜在客户看。你知道,Stefan Cohen就非常著名地这么做过。他是Palantir的创始人之一,他把demo展示给他们,然后说,你觉得怎么样?他们说,这太糟糕了。这跟我们做的事情完全没关系。

[04:11] **SPEAKER_04:** And he said, oh, well, how would you like it to be different? And then, you know, they would say, oh, well, could you make this change in this change? He's like sitting there writing all of this down. So far, this story feels very much like you would the standard advice you would give to founders today, right? That you have to go, you have to make something that people want, you have to get out of the building, you have to go talk to customers.

> 他就说,哦,那你希望它怎么改呢?然后他们会说,哦,你能不能改这个、改那个。他就坐在那儿把这些全都记下来。到目前为止,这个故事听起来非常像你今天会给创始人的标准建议,对吧?你必须去做人们想要的东西,你必须走出办公室,你必须去和客户交流。

[04:32] **SPEAKER_04:** I think we were we were doing this back in the in, like, the mid 2000s. And so, you know, there's a little bit of that meme where, like, I spent years mastering this technique and Paul Graham just tweeted it out for everybody. But the thing that changes and that really causes the FD strategy is that what you expect and the standard thing that you expect is that you spend a lot of time early on, you know, doing things that don't scale, going out and visiting customers, getting very close to the customers. And then you discover product market fit. And once you discover product market fit.

> 我想我们在做这件事的时候大概是2000年代中期。所以你知道,有那么点像那个梗:我花了好几年才掌握的技巧,Paul Graham一条推特就发给所有人了。但真正带来变化、真正催生FDE策略的地方在于:你所预期的、以及标准情况下你会预期的是,你在早期花大量时间去做那些无法规模化的事,出去拜访客户、和客户走得非常近。然后你发现了产品市场契合。而一旦你发现了产品市场契合。

[05:02] **SPEAKER_04:** You know, if you and this is class, you know, if we read Crossing the Chasm or any of these books, once you discover product market fit, you do something entirely different. So, you know, instead of going, you know, staying deep with the customers, doing as much as you can to really understand the customer, instead, you want to embrace distance from your customer and all you want to focus on is scaling. How do you sell more? How do you treat all customers exactly the same? And, you know, I think I want to say that if you're in a business where this is working for you, that's great.

> 你知道,这是经典套路,如果我们读过《跨越鸿沟》或任何这类书,一旦你发现了产品市场契合,你就会去做完全不同的事情。所以,你不再是深入扎在客户那里、尽可能去真正理解客户,相反,你要去拥抱和客户之间的距离,而你唯一想专注的就是规模化。你怎么卖得更多?你怎么让所有客户都被一视同仁地对待?我想说的是,如果你所在的业务里这套做法对你有效,那太好了。

[05:29] **SPEAKER_04:** Don't do the FD strategy. You have been given. An amazing gift. If you have the opportunity to just scale, treat all the customers the same, go ahead and do that. But it didn't work for us.

> 那就别搞FDE策略。你已经被赐予了一份了不起的礼物。如果你有机会就这样规模化、对所有客户一视同仁,那就尽管去这么做。但这对我们不管用。

[05:40] **SPEAKER_04:** And I think this is where Shamsankar, who's very early employee, you know, now I think the president and CTO of Palantir, he really invented the FD strategy. And the the basic thing we found was that the customers that we had, the product that they needed was slightly different at every place. And so we moved from. One customer building a product for them. We went to the next customer.

> 我想这就到了Shyam Sankar登场的地方,他是很早期的员工,现在我想是Palantir的总裁兼CTO,他真正发明了FDE策略。我们发现的基本情况是,对我们已有的客户来说,他们需要的产品在每个地方都略有不同。所以我们从一个客户、为他们构建一个产品,然后去到下一个客户。

[06:06] **SPEAKER_04:** We saw they had something was slightly different. And instead of sort of building two products or building the exact right feature for each of them at each site, we built something that was more a platform than a product that had the lot a lot of ability to be customized at each site. So when you do that, well, OK, you need to bring someone to the site to understand what the users are are doing and build customization. And historically, that's been understood as services. Right.

> 我们看到他们那里有些东西略有不同。我们没有去构建两个产品、或为每个现场构建恰好正确的功能,而是构建了一个更像平台而非产品的东西,它拥有在每个现场进行大量定制的能力。当你这么做时,好吧,你需要派一个人到现场去理解用户在做什么并构建定制。而历史上,这一直被理解为"服务",对吧。

[06:32] **SPEAKER_04:** So that's. you want to minimize you don't want to be doing a lot of work per customer in this you know product market fit and what sean realized was that you can actually flip this around and make it valuable so what he realized we needed was for the fdes to act as product discovery so they would go to the site they would take the product as it was and they would fill the gap between what the product did and what the users needed so you know the fde goes and builds like a gravel road to where the product needs to go and then the role of my team of the the product engineering team was to look at that and basically figure out how that should generalize to the next five customers of the next 10 customers and then turn that you know gravel road into like a paved super highway i feel like

> 所以那正是……你想要尽量减少……在产品市场契合的语境下你不想为每个客户做大量工作。而Sean意识到的是,你其实可以把这件事反过来,让它变得有价值。他意识到我们需要的是让FDE去充当产品探索的角色。所以他们会去到现场,拿着当时现状的产品,去填补产品所做的和用户所需之间的差距。你知道,FDE去修出一条通往产品需要到达之处的"碎石路",然后我团队、也就是产品工程团队的角色,是去审视那条路,基本上弄清楚它应该如何推广到下五个客户、下十个客户,然后把那条"碎石路"变成一条铺好的超级高速公路。我觉得……

[07:18] **SPEAKER_02:** sales is product discovery is a concept that's not new certainly around before palantir but typically the view used to be like you had your sales people that went out and did like the sales and talked to the customers and they came back and reported to the engineers but it seems like a palantir was like the engineers were doing that work was that like a conscious decision or how did that come about especially when you're selling into like the government and defense like you would imagine the natural inclination is to go hire some like experienced salesperson who's got a history of selling into the government and something like don draper like yeah yeah who wears a suit and

> 销售即产品探索,这个概念并不新鲜,在Palantir之前肯定就有了。但过去典型的看法是,你有你的销售人员,他们出去做销售、和客户交流,然后回来向工程师汇报。但看起来Palantir的做法是,工程师自己在做这项工作。这是一个有意识的决定吗?或者说这是怎么发生的?尤其是当你向政府和国防部门销售时,你会想象,自然的倾向应该是去雇一个有向政府销售历史的、经验丰富的销售,某种像Don Draper那样的——对对——穿着西装的人。

[07:49] **SPEAKER_03:** yeah worked in the d.o.d for 20 years and like takes generals out to steak dinners and things like that and that's actually not what you guys did right well i mean there's two angles this one

> 是啊,在国防部干了20年、带着将军们去吃牛排大餐之类的,而你们实际上并没有这么做,对吧?嗯,这里有两个角度。

[07:57] **SPEAKER_04:** is uh we talked to a lot of those people early on and they said why the hell would i work with a company when i could work with you know a big five defense prime uh and then even when we talked to people who you know seemed like they might be successful in this role it was just very clear to us that they wouldn't mesh with our culture and they wouldn't actually be successful and when we tried doing something like this it almost never worked and so what we found was very different and and i think the difference between sales-led product discovery and fde-led product discovery is that sales-led product discovery you're talking to people from the outside and again this is a little bit of a different perspective but it's not as effective as the fde-led product discovery where you're solving these problems from the inside so you know the scope of a of a traditional implementation might be you start with something that's pretty close to what the product does but you want to be solving one of the key problems that leadership has identified if you're not solving one of the top five priorities for the ceo it's probably not going to work they probably won't have the energy to persist through the much more challenging route getting effectively a new piece of the product built in a way that worked for them then once you've solved that first problem then the fdes can you know identify other key problems in the enterprise sometimes much more valuable problems than the ones that you were first targeting that maybe it's not obvious that palantir could have solved those problems or that your company could solve those problems but once you're there you can see through product insight that you can actually do this and then you go and solve those problems and so it switches from you know how do i sell the same thing to each customer to how do i land and expand bob can you lay out sort of exactly how the fdu

> 第一个是,我们早期跟很多那样的人聊过,他们说,我凭什么要跟你们公司合作,我明明可以跟一家五大国防承包商合作?而且就算我们跟那些看起来可能在这个角色上会成功的人聊,我们也非常清楚,他们跟我们的文化合不来,他们其实不会成功。而当我们尝试做这类事情时,几乎从来没成功过。所以我们发现的情况非常不同。我认为销售主导的产品探索和FDE主导的产品探索之间的区别在于,销售主导的产品探索,你是从外部和人交谈——再说一次,这是个稍微不同的视角——但它不如FDE主导的产品探索那么有效,后者是你从内部去解决这些问题。所以你知道,一次传统实施的范围,可能一开始是从跟产品现有能力相当接近的东西起步,但你想要解决的是领导层已经识别出的关键问题之一。如果你解决的不是CEO的前五大优先事项之一,那大概率行不通,他们大概不会有精力去挺过那条更具挑战性的路径——也就是以一种真正对他们有效的方式,基本上把产品的一块新东西构建出来。然后一旦你解决了第一个问题,FDE就能识别出企业里的其他关键问题,有时是比你最初瞄准的更有价值的问题,也许并不显而易见Palantir能解决那些问题、或者你的公司能解决那些问题,但一旦你在现场,你就能通过产品洞察看到你其实做得到,然后你就去解决那些问题。于是它就从"我怎么把同样的东西卖给每个客户"转变为"我怎么落地并扩展"。Bob,你能不能大致讲一下FDE……

[09:45] **SPEAKER_03:** bottle works at palantir like if you were giving people almost like an an instruction manual like

> ……模式在Palantir具体是怎么运作的,就像你要给人一本操作手册那样……

[09:49] **SPEAKER_04:** like here's how we did it yeah so i think a starting point is to think about how the team was structured um and of course there's many different iterations but i think this is this is the the key thing that remains constant is that the key roles are those of what we call the echo team and the delta team the echo team were embedded analysts so they would go to the customer site they would speak to the users they would uh try to figure out what demo or what use case uh really made sense for the users at this site what was the key problem that could be solved and they would also be the account managers so they would also be the people managing the relationships at the customer site and the delta team uh the deployed engineers were effectively software engineers typically very good at writing code extremely quickly eating a lot of pain as we put it and they would be the ones who sort of took those ideas and brought them into the real world and built a solution a prototype but something that could actually work and then deploy that uh for the customer and all of this would come in a very short period of time so you know you You go in with an idea for what you're going to work on. You set up a few months in that you're going to have a presentation with leadership to show them your progress. And then if that presentation goes well, then you're going to actually deploy and go organization-wide.

> ……就是"我们当时是这么做的"。好的。我想一个起点是思考团队是如何组织的。当然经历了很多不同的迭代,但我认为始终保持不变的关键是,核心角色是我们所称的Echo团队和Delta团队。Echo团队是嵌入式分析师,他们会去客户现场,和用户交谈,试图弄清楚在这个现场对用户来说什么样的demo或什么用例真正说得通,能被解决的关键问题是什么;他们同时也是客户经理,所以他们也是在客户现场管理关系的人。而Delta团队,也就是部署工程师,本质上是软件工程师,通常极其擅长非常快速地写代码、按我们的说法"吞下大量的痛苦",他们是负责把那些想法拿过来、带进现实世界、构建出一个解决方案、一个原型、但是能真正跑起来的东西,然后为客户部署它。而所有这些都会在非常短的时间内完成。所以你带着一个要做什么的想法进去。你设定几个月后要和领导层做一次汇报,向他们展示进展。然后如果那次汇报顺利,你就会真正部署,推广到整个组织。

[11:20] **SPEAKER_00:** LESLIE KENDRICK- The interesting thing about these two roles is very different kinds of people and profile. How would you even go about finding the right person to be in these roles? Because it's not just a regular engineer that could fit an FDE. They needed to have more of that talking to users. Or the echo team also had to be more technical.

> 这两个角色有意思的地方在于是非常不同类型的人和特质。你会怎么去找到适合这两个角色的合适人选?因为FDE并不是一个普通工程师就能胜任的。他们得更多地具备和用户交谈的能力。或者说Echo团队也得更懂技术。

[11:38] **SPEAKER_00:** It wasn't just an account manager. How did Palantir build this early team?

> 它不只是一个客户经理。Palantir当初是怎么组建这支早期团队的?

[11:43] **SPEAKER_04:** BRIAN DORSEY- Yeah, so the echo team, a classic profile for someone to join your echo team would be someone from the domain you're working in. So possibly a former army officer or someone who worked deeply in health care. So they have deep domain knowledge. And this is really important. They need to be rebels.

> 是的,所以Echo团队,一个加入你Echo团队的经典画像,会是来自你所在领域的人。所以可能是一名前陆军军官,或者一个在医疗行业深耕过的人。这样他们就有深厚的领域知识。而这一点真的很重要:他们需要是叛逆者。

[12:02] **SPEAKER_04:** LESLIE KENDRICK- Mm. BRIAN DORSEY- Or Sean would probably call them heretics. They need to be someone who understands how things are done right now and recognizes that it's insufficient, that it doesn't work. Because if their perspective is they come from this world, it's great, then they're never going to be able to figure out the step function change that the new software has to be able to make. Because if you can't make some sort of 3x or 10x change within that organization, then there was no reason, no reason to go through all the effort of doing this.

> 嗯。或者Sean大概会称他们为"异端"。他们需要是那种理解现在事情是怎么做的、并且认识到现状不够好、行不通的人。因为如果他们的视角是"我来自这个世界,现状挺好的",那他们就永远无法想清楚新软件必须要能带来的那种阶跃式变革。因为如果你没法在那个组织里带来某种3倍或10倍的改变,那就根本没有理由去经历这一切的努力。

[12:34] **SPEAKER_04:** You might as well have sold some sort of very simple piece of software. So that's the key profile for the echoes. And then for your deltas, you want someone who's really good at prototyping. So the wrong profile for a delta would be someone who's a craftsman, who really loves making sure the abstractions are exactly right, that they're building software that's going to be maintainable for a dozen years, because that's not a role. That's not the job.

> 你还不如去卖某种非常简单的软件算了。所以这就是Echo角色的关键画像。然后对于你的Delta,你想要一个真正擅长做原型的人。所以Delta的错误画像会是一个工匠型的人,他真的很在意确保抽象恰到好处、在意自己构建的软件能维护十几年,因为那不是这个角色。那不是这份工作。

[13:03] **SPEAKER_04:** And what you want is someone who can go in, figure out, write some rough and ready code. Sometimes that code is beautiful if you get the right person, but usually not. Again, that's not the key portion of the job. But someone who can go actually deliver that outcome in the form of software on a timeline. And then it may be the case that the first version they write has to be thrown away.

> 你想要的是那种能进去、弄明白、写出一些粗糙但能用的代码的人。有时候如果你找对了人,那些代码是很漂亮的,但通常不是。再说一次,那不是这份工作的关键部分。而是要一个能在规定时限内,以软件的形式真正交付那个成果的人。然后有可能他们写的第一版必须被扔掉。

[13:24] **SPEAKER_04:** And maybe they write a complete second version. Maybe someone else writes a second version, depending on that person. But those are the key sets of skills.

> 也许他们会写出一个完整的第二版。也许由别人写第二版,取决于那个人。但这些就是关键的技能组合。

[13:31] **SPEAKER_00:** CARRIE NORDLUND- It does sound a lot like a founding team.

> 这听起来确实很像一个创始团队。

[13:34] **SPEAKER_03:** MARK MANDELMANN, Yes. MARK BLYTH, JR.: It sounds a lot like a founder. Would you hire former startup founders and turn them into these roles? Or did it go mostly the other way?

> 是的。听起来很像一个创始人。你会招募前初创公司创始人并把他们转成这些角色吗?还是说主要是反过来?

[13:42] **SPEAKER_03:** I mean, I think it's no coincidence that Palantir has spun off an incredible number of startups, because this FD training, this is exactly the training to become a startup founder. You're learning all the startup founder skills, right? But did it go in the other direction too? MARK BLYTH, JR.: Back in the day when

> 我的意思是,Palantir孵化出数量惊人的初创公司,这绝非偶然,因为这套FDE训练,正是成为初创公司创始人的训练。你在学习所有创始人技能,对吧?但反过来的方向也发生过吗?在我们刚起步的那个年代……

[13:54] **SPEAKER_04:** we were getting this started, there was not a huge supply of founders for us to pull from. I think maybe that's the opposite. What is it now? But I think you're actually quite right. What you're doing in each of these new environments at each of these customer sites is a little bit like being a startup founder.

> ……当时并没有大量可供我们招募的创始人。我想也许现在正好相反。现在是什么情况呢?但我认为你其实说得很对。你在每一个这样的新环境里、每一个客户现场所做的事情,有点像在当一个初创公司创始人。

[14:13] **SPEAKER_04:** But you're a startup founder where you have access to some very powerful piece of product leverage that makes your job easier. This is, I think, great training. And like you said, this is why you see so many startups

> 但你是一个手上握有某种非常强大的产品杠杆的创始人,这让你的工作更轻松。我认为这是很好的训练。而且就像你说的,这就是为什么你会看到这么多出自Palantir的初创公司……

[14:23] **SPEAKER_03:** from Palantir founders. CARRIE NORDLUND- So the common knock that you hear on this from people who don't really know what they're talking about is like, oh, it's just consulting dressed up with fancy, fancy marketing speak. Why is that wrong?

> ……由Palantir人创立的公司。所以那些其实并不真懂行的人对这件事常见的一种质疑是,哦,这不就是包装了花哨营销话术的咨询嘛。为什么这种说法是错的?

[14:35] **SPEAKER_04:** MARK BLYTH, JR.: I think before I say, I don't want to tell you glibly why that's wrong. Because I think there's actually a real risk that it's right. And I think if you go back to 2015 and you talk to people about Palantir, maybe you would hear two things. One, that Palantir is evil.

> 我想在我说之前,我不想轻率地告诉你为什么它是错的。因为我认为其实真的存在一种风险——它可能是对的。我认为如果你回到2015年,和人们谈起Palantir,也许你会听到两件事。第一,Palantir是邪恶的。

[14:49] **SPEAKER_04:** But the second thing you hear is that it's a consulting business that is never going to scale, that it's actually like a bad business. It's not a software business. And we spent a lot of time trying to understand whether that was a correct, accurate characterization or not. From a business model perspective, one of the key things that you will see, that you should see, is that it may be the case that when you go into, you do a new deployment at a customer, that you're actually losing money early on. The longer you're at the customer, first thing is your product, because of the product discovery, gets better suited to what the customer does.

> 但你听到的第二件事是,它是一个永远无法规模化的咨询业务,它其实是个糟糕的生意。它不是一个软件生意。我们花了大量时间试图搞清楚那种说法是否准确、是否是对的刻画。从商业模式的角度看,你会看到、也应该看到的一件关键事情是:有可能当你进入、在一个客户那里做新部署时,你早期其实是在亏钱的。你在客户那里待得越久,第一件事是,由于产品探索,你的产品会越来越贴合客户所做的事。

[15:23] **SPEAKER_04:** And so you no longer need a large team of people at the customer site figuring out what the customer is doing, paving, writing that code. The second thing is that you should be earning the right, as Sean would put it, to have access to more important problems at the customer site. And so you should see, basically, that your cost per value of the outcome you're delivering is going down. And so your profit margins start off negative, but then ultimately become positive after some period of time, maybe a year, maybe multiple years, at the customer site. And if you look at it from that perspective, you can see that you're actually delivering real, repeatable, value.

> 于是你就不再需要在客户现场放一大队人去弄清楚客户在做什么、去铺路、去写那些代码。第二件事是,用Sean的话说,你应该在"赢得"访问客户现场更重要问题的权利。所以你应该会看到,基本上,你交付成果所对应的"单位价值成本"在下降。于是你的利润率一开始是负的,但最终在某段时间之后——也许一年、也许好几年——在那个客户现场变为正的。如果你从这个角度看,你就能看到你其实是在交付真实的、可复制的价值。

[16:02] **SPEAKER_00:** MELANIE WARRICK- I guess one fascinating piece to make this work and drive the cost down is really the product team. So how does the product team fit in and work with the FDE team?

> 我猜让这套模式跑起来、把成本压下来的一个引人入胜的环节,真正的关键其实是产品团队。那么产品团队是怎么融入进来、怎么和FDE团队协作的?

[16:13] **SPEAKER_04:** JASON MAYES- I think on the engineering side, it feels my job as an engineer was actually not so bad, because early on, in the early days of Palantir, we were doing this founder-led discovery, and we were building new products. And later on, at the later days of Palantir, we were still doing that. We were still building new products. So it just felt great, right? But the roles that were really different are the FDE team, but then also the product management team.

> 我想在工程这一侧,感觉上我作为工程师的工作其实还不赖。因为在Palantir早期,我们在做这种创始人主导的探索,我们在构建新产品。而到了Palantir后期,我们仍在做这件事。我们仍在构建新产品。所以感觉就是很棒,对吧?但真正不同的角色是FDE团队,以及产品管理团队。

[16:37] **SPEAKER_04:** And so the product that you're building, instead of being highly verticalized, and this is one flow that millions of people are going to be going through, like if you're building Airbnb, right? Instead, the role of the product team is really to hold the product vision. And so you have to think, when I see this new problem that we're seeing at a customer site, what is it? What is the generalizable version of this that applies to the next 10 customers? Because there's a classic failure mode here, where the FDE implements something for one customer.

> 所以你构建的这个产品,不是高度垂直化的——比如说,如果你在做Airbnb,那是数百万人都会走一遍的同一个流程。相反,产品团队的角色其实是要守住产品愿景。所以你得思考,当我在某个客户现场看到这个新问题时,它是什么?能推广到接下来10个客户的、可泛化的版本是什么?因为这里有一个经典的失败模式:FDE为一个客户实现了某个东西。

[17:14] **SPEAKER_04:** And you say, great, well, that's how you should do it. And you bring it directly into the product. And it turns out, if you do that, you're building something that's over-specialized for one customer. And so the part of the magic here is being able to build the kind of product, and with the kind of product people, they can look at that, and sort of guess the correct problem that you're solving, which is always a little bit more general than the problem that the customer is coming in with.

> 然后你说,太好了,那就该这么做。你就把它直接搬进产品里。结果发现,如果你那么做,你构建出来的东西对那一个客户是过度专门化的。所以这里魔法的一部分在于,要能构建那种类型的产品、并且有那种类型的产品人,他们能看着那个东西,大致猜出你真正要解决的正确问题——它总是比客户来时带着的问题要更一般化一点。

[17:40] **SPEAKER_00:** LESLIE KENDRICK MASON- So there was some wisdom to figure out which bucket it fit. Is this just for this vertical, or it could be generalized? So could you give us an example of what that looked like in terms of the products and verticals, and what fit in one bucket versus the other one?

> 所以这里需要某种智慧去判断它归入哪个桶。这只是针对这个垂直领域,还是能被泛化?那你能不能给我们举个例子,说明在产品和垂直领域方面这看起来是什么样的,以及什么归入这个桶、什么归入那个桶?

[17:54] **SPEAKER_04:** MARK MANDELMAN- Yeah, I mean, probably the most basic example here is sort of the invention of the Palantir ontology itself. And so when we first started talking about working with the US government and specifically working intelligence, should we have a database table for people, and a different database table for money, and a different database table for this? And it's super obvious, I think, at this point, if you go down that route and you try to deploy to multiple people, your database doesn't make any sense. And so the change here would say, well, we need to pull this up to a higher level of generalization. And instead of thinking about specific types, of objects, we should allow that to be defined per customer by the forward-deployed engineering team.

> 是的,这里最基础的例子大概就是Palantir本体论(ontology)本身的发明。所以当我们最初开始谈论和美国政府合作、特别是从事情报工作时,我们是不是应该有一张"人"的数据库表、一张不同的"钱"的数据库表、再来一张不同的"这个"的表?我想到现在这一点已经超级明显了:如果你走那条路,然后试图部署给多个客户,你的数据库就毫无意义了。所以这里的改变会说,好吧,我们需要把它上提到一个更高的泛化层级。我们不该去思考具体的对象类型,而应该允许它由前沿部署工程团队按客户来定义。

[18:38] **SPEAKER_04:** And so that's the sort of origin story of where Palantir famously got its ontology.

> 这就是Palantir著名的本体论的起源故事。

[18:41] **SPEAKER_03:** MARK BLYTH, JR.: So how does that work today? Is there a base database schema that has common reusable objects, like people and money, that then gets customized per site?

> 那今天这是怎么运作的呢?是不是有一个基础的数据库schema,包含像"人"和"钱"这样的通用可复用对象,然后再按现场定制?

[18:52] **SPEAKER_04:** MARK BLYTH, JR.: Well, I mean, the database scheme is extremely general. There's just this notion of objects, properties, media, and links between objects. And here, I'm talking about Palantir's government. And I'm talking about Palantir as a product, which was our first product.

> 嗯,数据库schema是极其通用的。就只有对象、属性、媒体、以及对象之间的链接这样的概念。而这里我说的是Palantir Government。我说的是Palantir这个产品,它是我们的第一个产品。

[19:05] **SPEAKER_04:** But the ontology is what encodes all of the specialized information that's per customer. And that says, oh, well, this is a person. This is a ship. This is a money flow. And again, this is, I think, really the very most basic example.

> 但本体论才是编码所有按客户定制的专门信息的地方。它说,哦,这是一个人。这是一艘船。这是一笔资金流。再说一次,我认为这真的是最最基础的例子。

[19:20] **SPEAKER_04:** But if you build something for just one customer, then you're going to be thinking in the description that applies to that customer. But instead of saying, OK, well, for Palantir, for people, we do this, you want to be able to pull it up a level and say, OK, well, there's this common operation that we want to apply to things that have this property, like people have this property, but maybe also ships have this property. But let's be honest, money, payments do not have this property. And so you have to think at a higher level of abstraction. We didn't hire product managers for a long time.

> 但如果你只为一个客户构建东西,那你就会用适用于那个客户的描述去思考。但你不该说"好,对Palantir来说、对人来说,我们这么做",而是要能把它上提一个层级,说,好,有这么一个通用操作,我们想应用到具有某个属性的事物上,比如人有这个属性,但也许船也有这个属性,不过说实话,钱、支付并不具备这个属性。所以你必须在更高的抽象层级上思考。我们很长一段时间都没招产品经理。

[19:53] **SPEAKER_04:** And when it did come time for me to hire product managers, I would interview people who were amazing product managers at other companies. And I would ask them to think at this level of abstraction. They couldn't really think at this level of abstraction. They would say, OK, well, this is the flow. This is what it should look like for this customer.

> 而等到我确实需要招产品经理的时候,我会面试那些在其他公司做得非常出色的产品经理。我会请他们在这个抽象层级上思考。他们其实没法在这个抽象层级上思考。他们会说,好,这是流程。这是它对这个客户应该长什么样。

[20:11] **SPEAKER_04:** But that was the wrong thing to do here. And they needed to pop up a level and think at the level of, how does this work in the context of the ontology? How do we change the ontology so that this specialized thing works across customers? And of course, there's many other examples that don't have anything to do with the ontology.

> 但那在这里是错误的做法。他们需要往上跳一个层级,在这个层面上思考:这在本体论的语境下是怎么运作的?我们要怎么改变本体论,才能让这个专门化的东西跨客户都成立?当然,还有很多其他和本体论毫无关系的例子。

[20:27] **SPEAKER_02:** MARK MANDELMANN I mean, did that create any sort of cultural tension at Palantir itself? I think you're describing the FTEs as sort of these heretics. They don't want to generalize. They want to do what's best for the customer and build specialized solutions. But presumably, for your own internal product team, you do actually want to hire the people who can think at some level of abstraction and want to build maintainable code that lasts for a while.

> 我是说,这在Palantir内部有没有制造出某种文化上的张力?你把FDE描述成某种"异端"。他们不想泛化。他们想做对客户最好的事、构建专门化的解决方案。但想必对于你自己的内部产品团队,你其实是想招那些能在某种抽象层级上思考、想构建能维持一段时间的可维护代码的人。

[20:47] **SPEAKER_02:** Surely, that must have created tension somewhere where there's an FTE who's like, no, I don't want to use the generalizable ontology. I want to do it this way.

> 这中间某处肯定制造出了张力吧,会有一个FDE说,不,我不想用那个可泛化的本体论。我就想按我这个方式来。

[20:54] **SPEAKER_04:** MARK BLYTH Well, I mean, absolutely, there was always a lot of tension. And I would not frame this so much in terms of the skills that different people had. Because it was also very common. I think it's a lot about the environment, what people do in the environment they're placed in. It was also very common for FTEs to work in the field for a long time and then say, hey, I can really fix these products and then come in and do an amazing job on the product side and think at that level of abstraction.

> 嗯,当然,一直都有很多张力。但我不会太多从不同人所拥有的技能这个角度去框定它。因为还有一个很常见的情况——我认为很大程度上取决于环境,取决于人们在所处环境里会做什么。同样很常见的是,FDE在一线现场工作很长时间,然后说,嘿,我真的能把这些产品修好,然后进来在产品这一侧做得非常出色、在那个抽象层级上思考。

[21:17] **SPEAKER_04:** But when you're at the customer site, you are faced with one very specific problem. MARK BLYTH Yeah, maybe the incentives are different. MARK BLYTH Yeah.

> 但当你在客户现场时,你面对的是一个非常具体的问题。是啊,也许激励机制是不同的。是的。

[21:21] **SPEAKER_02:** MARK BLYTH The classes and skills are different.

> 那种类别和技能是不同的。

[21:22] **SPEAKER_04:** MARK BLYTH The incentives are different. And so you're solving one very particular problem. And it makes a lot of sense to just take the simplest approach to solve that problem. And that is, in fact, what the FTE should do. That's what the gravel road looks like.

> 激励机制是不同的。所以你在解决一个非常特定的问题。而采取最简单的方式来解决那个问题是很合理的。事实上,那正是FDE应该做的。那就是"碎石路"的样子。

[21:35] **SPEAKER_04:** And then the paved road, though, has to go by not just this one customer, but a bunch of other customers that are further down the road. So the paved road often looks a little bit different. But the flip side of this, though, is imagine you said, well, clearly this FTE approach is just wrong. The FTE is building the wrong thing. What if the product team just thinks really hard about what to build, and then they go build that?

> 而铺好的路,则不仅要经过这一个客户,还要经过一堆在这条路更远处的其他客户。所以铺好的路往往看起来会有点不一样。但这件事的另一面是,想象你说,显然这套FDE做法就是错的。FDE在构建错误的东西。要是产品团队就使劲想清楚该构建什么,然后就去把它构建出来呢?

[21:55] **SPEAKER_04:** They're absolutely going to build the wrong thing. In fact, the way that we would often build features early on is that, first, the FTE team would build something. They'd see something at one customer. We'd bring it back to the product team in Palo Alto. And we'd say, OK, what's the right generalized version?

> 他们绝对会构建出错误的东西。事实上,我们早期经常构建功能的方式是,首先FDE团队构建某个东西。他们在某个客户那里看到某样东西。我们把它带回帕洛阿尔托的产品团队。然后我们说,好,正确的泛化版本是什么?

[22:10] **SPEAKER_04:** And those FTEs would participate in those discussions. That was incredibly important. And then we'd identify several other customers. Well, if it worked for this customer, we think it could work for this other customer. So let's bring the FTEs from those customers in as well and help them design.

> 而那些FDE会参与那些讨论。这一点极其重要。然后我们会识别出另外几个客户。嗯,如果它对这个客户管用,我们认为它可能对另外这个客户也管用。所以让我们把那些客户的FDE也拉进来,帮他们做设计。

[22:26] **SPEAKER_04:** And they can help us design this feature so that when we build something, we know it'll work for the customer that was initially prototyped. And we know it will work for these others. And then, of course, once you've built that context where everybody can see, here are three different workflows that are subtly different, then suddenly you're not having this argument about, well, we think it should be general, and we think it should be specific. But everybody is solving the same problem. And then I think that really melds the incentives.

> 他们能帮我们设计这个功能,这样当我们构建某个东西时,我们知道它对最初做原型的那个客户管用,也知道它对这些其他客户管用。然后,当然,一旦你构建了那个语境、让每个人都能看到"这里有三个略有微妙差异的不同工作流",那么突然之间你就不再是在争论"我们觉得它应该通用、我们觉得它应该专门"。而是每个人都在解决同一个问题。然后我认为那才真正把激励机制融合到了一起。

[22:53] **SPEAKER_03:** MARK MANDELMANIS- Do you feel like it requires a lot of organizational discipline to keep this model from devolving into peer consulting, where the FTE team, which I think is the most important part of the process, is just off building whatever product the customer needs?

> 你是否觉得要防止这套模式退化成纯咨询——也就是FDE团队(我认为它是整个流程中最重要的部分)只是自顾自地去构建客户所需要的任何产品——需要很强的组织纪律?

[23:06] **SPEAKER_04:** JASON MAYES- Yes. You absolutely have to focus on this. And I think one of the other failures, by the way, that's even prior to that and more the easier failure to become a consulting firm, it's where you build the product in the field that the customers are asking for, rather than the one that's actually valuable to them. Because it's often the case that the customer, right? You don't actually, the customer is like a whole organization.

> 是的。你绝对必须专注在这件事上。而且我想顺便说,另一个失败模式,其实还在这之前、也是更容易掉进去的、变成一家咨询公司的失败,是你在一线现场构建的是客户嘴上要求的产品,而不是真正对他们有价值的那个。因为常常是这样,客户,对吧,你其实……客户是一整个组织。

[23:30] **SPEAKER_04:** You talk to the customer, you talk to maybe the CIO, right? Or you talk to one sponsor, usually a couple levels down from the CEO, who you only get to see every once in a while. And it's often the case that they would rather just have you solve some problem that's easy for them to have you solve, rather than one that's really impactful

> 你跟客户交谈,你也许跟CIO谈,对吧?或者你跟一个赞助人谈,通常是CEO往下几层、你只能偶尔见到一次的人。而常常是这样,他们宁愿让你去解决某个对他们来说容易让你去解决的问题,而不是一个真正有影响力、能改善业务的问题。

[23:48] **SPEAKER_00:** and improves the business. MARK MANDELMANIS- Going back to the opening from Jared, what's going on with all these AI companies really now ramping up and hiring tons of FTEs? What has caused them to really adopt this model, which was not the case for the previous generation of companies with SaaS? What happened?

> 回到Jared开头的问题,现在所有这些AI公司真的在大举扩张、招聘大量FDE,这是怎么回事?是什么让他们真正采用了这套模式?而上一代SaaS公司并不是这样的。发生了什么?

[24:07] **SPEAKER_02:** MARK MANDELMANIS- Especially because I feel like even as Palantir became successful and the FTE model became more known, it was still seen as, well, that's a one-off thing because Palantir is a unique company, and selling to the government is just like a- MARK MANDELMANIS- Government, yeah. Like a really weird thing. MARK MANDELMANIS- Yeah. But you wouldn't, don't try this at home.

> 尤其是因为,我觉得即便Palantir变得成功、FDE模式变得更为人所知,它当时仍被视为——好吧,那是个一次性的特例,因为Palantir是一家独特的公司,向政府销售就是一件很——对,政府。很奇怪的事。是的。但你不会……别在家里尝试这个。

[24:22] **SPEAKER_?:** MARK MANDELMANIS- Exactly.

> 没错。

[24:23] **SPEAKER_01:** Exactly.

> 没错。

[24:24] **SPEAKER_02:** Exactly. MARK MANDELMANIS- The mindset, right? Now everyone's sort of, like Diana said, it's become very commonplace. Has that, one, has that surprised you? And then two, why do you think that's happened?

> 没错。是那种心态,对吧?现在大家都有点像,就像Diana说的,它变得非常司空见惯了。这个,第一,这有没有让你感到意外?第二,你认为为什么会发生这种情况?

[24:33] **SPEAKER_04:** MARK MANDELMANIS- This was absolutely a surprise to me, that my first, second, and third pieces of advice to people who are thinking about trying an FTE strategy is, don't do this at home. If you can avoid it, it's probably bad for you. Probably you're going to end up doing services. And then only if you really try hard not to do it and fail. Then, well, then maybe actually it's a moat for you if it's the only thing that can possibly work in your market.

> 这对我来说绝对是个意外,因为我给那些正在考虑尝试FDE策略的人的第一、第二、第三条建议都是:别在家里尝试这个。如果你能避免,那多半对你不好。你多半最终会沦为做服务。然后,只有当你真的努力去不做它却失败了。那么,好吧,那也许它对你反而是一道护城河——如果它是你市场里唯一可能行得通的东西的话。

[24:55] **SPEAKER_04:** So what's special about this market, right? Why does the AI agents market work this way? Maybe the starting place is, why did Palantir have to adopt this? The Palantir market is not one coherent market, right? So we were working with national intelligence agencies, with national law enforcement, with the military.

> 那么这个市场有什么特别之处呢,对吧?为什么AI智能体市场是这样运作的?也许起点是,为什么Palantir当初不得不采用这套?Palantir的市场并不是一个连贯统一的市场,对吧?我们当时是和国家情报机构、国家执法部门、军方合作。

[25:16] **SPEAKER_04:** All of these organizations had some similar projects, right? But even the difference between a counterproliferation workflow and a counterterrorism workflow, one, you're trying to figure out who's building bombs, and the other one, well, who's building nuclear bombs, and who's building IEDs. And those are actually quite different in terms of how they work. And so there's this incredible heterogeneity. And the market, you should really think of the market as different segments.

> 所有这些组织都有一些类似的项目,对吧?但即便是反扩散工作流和反恐工作流之间的差别——一个,你是在试图搞清楚谁在造炸弹,另一个,谁在造核弹、谁在造简易爆炸装置。这两者在如何运作上其实相当不同。所以存在这种惊人的异质性。你真的应该把这个市场看作不同的细分。

[25:42] **SPEAKER_04:** Inside each segment, you can build something. And the crossing the chasm story a little bit applies. So you're starting off, nothing seems to work. Suddenly, you find product market fit in the segment. You can deploy the people that are doing this kind of workflow.

> 在每个细分内部,你可以构建出某个东西。而"跨越鸿沟"的故事在一定程度上适用。所以你一开始,似乎什么都不管用。突然间,你在这个细分里找到了产品市场契合。你就可以部署那些在做这类工作流的人。

[25:59] **SPEAKER_04:** And then with the next customer, you find the same people doing a similar workflow. And you can deploy with very little customization. But then there's a natural limit to that. And so now you want to go tackle a different market segment. And you have to develop a new piece of technology.

> 然后到了下一个客户,你发现同样的人在做类似的工作流。你就可以只做很少的定制就完成部署。但接着这就有个天然的上限。于是现在你想去攻打另一个市场细分。而你必须开发出一项新技术。

[26:15] **SPEAKER_04:** And then that can be referenced in other market segments. And like I'm sort of saying here, a segment is not the same as a customer, necessarily, especially in an enterprise or a very large enterprise like the government, where a customer, is tens of thousands of users, potentially. In that case, that's where the FD strategy matters. Because it's like you're doing things that don't scale, but you're doing it scalably over and over again for every market segment that you enter. Why do we see this with AI agents?

> 然后那项技术又能被其他市场细分所引用。而正如我在这儿大致说的,一个细分并不必然等同于一个客户,尤其是在企业、或者像政府这样非常大的企业里,一个客户可能是成千上万的用户。在那种情况下,那就是FDE策略发挥作用的地方。因为这就好比你在做那些无法规模化的事,但你在以可规模化的方式,为你进入的每一个市场细分一遍又一遍地去做。为什么我们在AI智能体上看到了这种情况?

[26:48] **SPEAKER_04:** I think the other thing that's unique about Palantir is that we were building a completely new type of product. The product that the users saw, well, they were used to basically, you know, tracking, doing their analysis and tracking people in a tool that looked like PowerPoint. And they would collaborate by sending these files back and forth with each other. But the product we built was tied, basically said, hey, when you're, you know, drawing out that link diagram, you're not just editing a file. You're actually changing a database.

> 我认为Palantir还有一个独特之处在于,我们当时在构建一种全新类型的产品。用户看到的那个产品——嗯,他们习惯的基本上是在一个长得像PowerPoint的工具里做分析、追踪人。他们通过互相来回发送这些文件来协作。但我们构建的产品本质上是绑定在一起的,它说,嘿,当你在画那张关系连线图时,你不只是在编辑一个文件。你其实是在改变一个数据库。

[27:18] **SPEAKER_04:** And everybody has the same database. And so while to the user it looked like a small change on top of the work they were doing, to the enterprise, to the organization we were selling to, it was a completely different market category. And that, I think, is what's happening with AI agents, where, you know, this is a completely new market category. If you are implementing, you know, a standard SaaS product and you're replacing one way of paying bills with a different way of paying bills, everybody understands what that market is. And so, you know, the segmentation, you know, there's not all this little segmentation.

> 而且每个人用的是同一个数据库。所以虽然在用户看来这只是他们原有工作之上的一个小改动,但对企业、对我们所销售的那个组织来说,它是一个完全不同的市场品类。而我认为这正是AI智能体正在发生的事情:这是一个全新的市场品类。如果你在实施一个标准的SaaS产品,你只是用一种付账单的方式替换另一种付账单的方式,那每个人都懂那个市场是什么。所以那种细分,并没有这么多琐碎的小细分。

[27:52] **SPEAKER_04:** There's not a lot of, there's not the same kind of product discovery. You can then, you know, make a product that's better than the incumbent product. And scale by replacing that product. With AI agents, there is no incumbent product. And so also I would say what it is to build AI agents is actually probably a lot of different things.

> 没有太多、没有那种同样的产品探索。然后你就可以做出一个比既有产品更好的产品,通过替换那个产品来实现规模化。而在AI智能体这里,根本不存在既有产品。所以我还想说,"构建AI智能体"到底意味着什么,其实很可能是许许多多非常不同的事情。

[28:11] **SPEAKER_04:** And we don't know what those are yet. We've got to figure them out. Probably in five years, we'll look back, we'll be like, well, AI agents, there wasn't even a thing at all, right? We were actually doing all these different things. And so that I think is why you're seeing the FDE model taking off, because there's so much product discovery to do.

> 而我们还不知道那些是什么。我们得去把它们弄清楚。大概五年后,我们回头看会说,嗯,AI智能体,那压根就不是一个东西,对吧?我们其实是在做所有这些不同的事情。所以我认为这就是为什么你会看到FDE模式正在兴起,因为有太多的产品探索要做。

[28:28] **SPEAKER_04:** And you can only do it from inside the enterprise.

> 而你只能从企业内部去做这件事。

[28:30] **SPEAKER_02:** Okay, well, how does this relate to some of the classic YC advice, which is do things that don't scale?

> 好的,那这和一些经典的YC建议——也就是"做那些无法规模化的事"——有什么关系呢?

[28:36] **SPEAKER_04:** Well, that's the advice that you give to an early stage founder. And the FDE model effectively is doing things

> 嗯,那是你给早期阶段创始人的建议。而FDE模式本质上就是在规模化地去做那些无法规模化的事……

[28:43] **SPEAKER_01:** that don't scale at scale. YC's next batch is now taking applications. Got a startup in you? Apply at ycombinator.com slash apply.

> ……规模化地做无法规模化的事。YC的下一批现在正在接受申请。你心里有个创业点子吗?到ycombinator.com/apply申请吧。

[28:53] **SPEAKER_01:** It's never too early, and filling out the app will level up your idea. Okay. Back to the video.

> 永远不嫌太早,而且填写申请会让你的点子更上一层楼。好了,回到视频。

[28:59] **SPEAKER_03:** Since you see a lot of people trying to apply the FDE model now to their new startups, including a lot of people who didn't work at Palantir and are sort of doing it like second or third hand, what are ways you see people getting it wrong or misconceptions that you'd like to dispel?

> 既然你现在看到很多人试图把FDE模式应用到他们的新创业公司上,包括很多没在Palantir工作过、算是二手三手学来的人,你看到人们在哪些方面做错了、或者有哪些你想澄清的误解?

[29:13] **SPEAKER_04:** Maybe I will start by saying, as I've advised a few different startups who are doing this, I think the startups, the most successful startups doing the FDE model have people from Palantir running the FDE model. The startups that I've talked to who are switching to the FDE model gained a lot of benefit by bringing on someone from Palantir in one of the core roles. As I said, the engineering team is often fairly similar, but maybe continues to be fun for a long time. But the actual mechanics of how the FDEs work, how you build these accounts, how you find the outcomes, those are actually quite different from a standard software firm. And so one of the key differences, and something that I think is actually quite difficult for people to understand, is how you choose a problem and then how you price that problem.

> 也许我先说,在我为几家做这件事的不同初创公司做顾问的过程中,我认为最成功地运用FDE模式的那些初创公司,是有Palantir出来的人在运营他们的FDE模式。那些我聊过的、正在切换到FDE模式的初创公司,通过在一个核心角色上引入一个Palantir的人,获得了很大的收益。就像我说的,工程团队往往相当相似,而且可能长时间里都还挺有意思的。但FDE具体如何运作、你如何培育这些客户、如何找到成果,这些其实和标准软件公司相当不同。所以其中一个关键区别、也是我认为人们其实相当难以理解的一点,是你如何选择一个问题、然后如何为那个问题定价。

[30:06] **SPEAKER_04:** And fundamentally what you're selling with the FDE model is that you're not selling the installation of software, you're selling an outcome. As Sean would say, you're selling that you have solved a problem. The next question then is if you've now solved a problem that is delivering some value to the users, how do you price that?

> 从根本上说,你用FDE模式所销售的,不是软件的安装,你销售的是一个成果。用Sean的话说,你销售的是你已经解决了一个问题。那么接下来的问题是,如果你现在已经解决了一个正在为用户带来某种价值的问题,你要怎么给它定价?

[30:27] **SPEAKER_00:** That's a very common question we get from all these AI startups because in the age of SaaS, you would do it based on usage or subscription or seats, and this is completely different as outcomes. How do you even price it? How should all these AI founders price their solution?

> 这是我们从所有这些AI初创公司那里得到的一个非常常见的问题,因为在SaaS时代,你会基于用量、订阅或席位来定价,而这个以成果为准则的方式完全不同。你到底该怎么给它定价?所有这些AI创始人应该如何为他们的解决方案定价?

[30:46] **SPEAKER_04:** Yeah, and I think one of the really important things that is differentiated between the FDE model and your sort of standard SaaS model is that with the FDE model, with a SaaS model and product market, you're going towards very simple repeatable contracts, very simple repeatable pricing that makes sense across all of your customers. And often you're going to be quite comfortable with small contracts because the cost, the marginal cost to deploy is very low. With the FDE model, you're gonna get pushed towards larger and larger contracts. Like we talked about, you're gonna be growing contracts per customer over time. The contracts, because they're complex, are gonna be more flexible.

> 是的,我认为FDE模式和你那种标准SaaS模式之间一个非常重要的差异是,在FDE模式下——用SaaS模式加产品市场契合,你是在朝着非常简单、可复制的合同、非常简单、可复制、对你所有客户都说得通的定价前进。而且你往往会对小额合同相当满意,因为部署的边际成本非常低。而用FDE模式,你会被推向越来越大的合同。就像我们说的,你会随着时间推移把每个客户的合同越做越大。而由于这些合同很复杂,它们会更有弹性。

[31:25] **SPEAKER_00:** I think this is what the AI startups that we work with discover on their own. I have this company called Castle that does AI voice agent for mortgage servicing. So they work with very large banks and the way they actually been able to go live with large banks is exactly that model of ramping up, is the number of successful calls that we're handling, all these mortgage requests. Then they had like stipulations when it goes to scale, it would be this much and that, and they kind of figure it out on their own and other startups as well, like Happy Robot, that's another YC company as well, doing AI voice agents for logistics. They're working with large companies like DHL, similar thing.

> 我认为这正是和我们合作的那些AI初创公司自己发现的。我有一家叫Castle的公司,做面向抵押贷款服务的AI语音智能体。所以他们和非常大的银行合作,而他们之所以能真正在大银行那里上线,正是那种逐步加码的模式——我们处理的成功通话数量、所有这些抵押贷款请求。然后他们设定了一些条款,当规模扩大到某个程度时,费用就会是这么多、那么多,他们基本上是自己摸索出来的,其他初创公司也是,比如Happy Robot,那是另一家YC公司,做面向物流的AI语音智能体。他们和DHL这样的大公司合作,情况类似。

[32:03] **SPEAKER_04:** There's an asymmetry here between you, the startup and the business that you're selling to, which is typically when you're selling to a large enterprise, they don't believe they can actually accomplish anything. And that's because oftentimes they've had many large projects that have failed. They also don't believe you can accomplish anything, right? Because they think that you, the startup are just like them. You on the other hand, know that you can actually execute.

> 这里存在一种不对称,在你(初创公司)和你所销售的企业之间。通常当你向一家大企业销售时,他们并不相信自己真的能完成任何事情。这是因为很多时候他们经历过很多失败的大型项目。他们也不相信你能完成任何事情,对吧?因为他们认为你这个初创公司跟他们没什么两样。而你这一方,却知道你其实能够执行到位。

[32:26] **SPEAKER_04:** Yeah. You on the other hand, know that you can actually execute. You on the other hand, know that you can actually execute. And if you can't, well, you should go into a different line of business anyway, right? And so early on, it makes sense for the startup to just take on all the risk and say, we're going to just believe in our own execution and we're going to take on the risk and you pay us if it works, or you pay us when we're actually able to expand.

> 是的。你这一方,却知道你其实能够执行到位。你这一方,知道你确实能执行。而如果你不能,那你反正也该改行去做别的生意了,对吧?所以早期,对初创公司来说,承担所有风险是合理的,说,我们就相信我们自己的执行力,我们来承担风险,如果成了你就付我们钱、或者当我们真正能够扩展时你再付。

[32:49] **SPEAKER_04:** The one place this can go wrong is that, particularly if you're doing something that needs to be deployed into the enterprise, on-premise or any piece of it needs to be on-premise rather than in the cloud, you do have to fight the IT team.

> 这件事可能出错的一个地方是,尤其当你在做的事情需要部署进企业内部、在本地(on-premise)、或者其中任何一块需要在本地而不是在云上时,你确实得和IT团队斗一斗。

[33:04] **SPEAKER_00:** Yeah, I've actually seen that too.

> 是啊,我其实也见过这种情况。

[33:06] **SPEAKER_04:** Yeah.

> 是的。

[33:06] **SPEAKER_00:** With some of these companies.

> 在其中一些公司身上。

[33:07] **SPEAKER_04:** And more generally, who needs to say yes inside the organization you're deploying into in order for you to succeed? Because those people do not think like startups. They are not aligned with the end user. And so you're going to have to figure out a way past them. And, you know, this is part of, part of why it matters that you're working on one of the CEO's top five problems.

> 更一般地说,在你要部署进去的那个组织内部,得由谁点头你才能成功?因为那些人不像初创公司那样思考。他们和终端用户并不一致。所以你得想办法绕过他们。而这,部分就是为什么"你在做的是CEO前五大问题之一"这件事很重要。

[33:32] **SPEAKER_04:** Because you need to be able to bring in someone from the top to say, yes, give them authority to operate. Give them, you know, the ability to use, yes, you use this particular type of database. They need to use a different type of database. They, you know, you have all these very specific organizational things that are meant to apply to your IT staff who are building things in-house, but they don't apply to the startup. Let them do what they want.

> 因为你需要能够搬来一个高层的人来说,行,给他们操作的授权。给他们、你知道,使用的能力——对,你用这种特定类型的数据库。他们需要用一种不同类型的数据库。他们有各种非常具体的组织规定,那些规定本意是适用于你那些在内部自建东西的IT员工的,但它们不适用于这家初创公司。让他们做他们想做的。

[33:57] **SPEAKER_04:** Let them do what they need to do.

> 让他们做他们需要做的事。

[33:58] **SPEAKER_00:** How did Palantir get that executive buy-in? I think this is sort of what's happening with all these AI startups that are taking off and going from zero to seven, eight figures in revenue within a year. They figure out the executive buy-in, but it's all very haphazard, I would say, from all the stories I know of.

> Palantir当初是怎么拿到那种高管支持的?我认为这正是现在所有这些起飞的AI初创公司身上正在发生的事情——它们在一年之内从零做到七位数、八位数的收入。他们搞定了高管支持,但从我知道的所有故事来看,这一切都非常随机、没有章法。

[34:17] **SPEAKER_04:** That's how it felt early on too. Okay. It's a discipline, it's a skill, you know, you need really amazing leadership on the FD team to be able to have that kind of discipline. And, you know, to share what works, you know, and just get the practice of doing it at one customer. I mean, I think it's not surprising.

> 早期感觉也是这样的。好的。这是一种纪律、一种技能,你知道,你需要FDE团队里真正出色的领导力,才能拥有那种纪律。以及,分享什么管用,并且真正把它在一个客户身上实践一遍、形成惯例。我是说,我认为这并不令人意外。

[34:35] **SPEAKER_04:** I think Palantir is extremely good at this now, probably better than any other company. And that's why, you know, the companies I've seen that have done this the best have sort of pulled that from people who've done it before. But it can be learned. We learned it.

> 我认为Palantir现在极其擅长这一点,大概比任何其他公司都强。而这就是为什么我见过的那些把这件事做得最好的公司,基本上是从做过这件事的人那里把它借鉴过来的。但它是可以学会的。我们就学会了。

[34:49] **SPEAKER_02:** Jared pointed out earlier that the, I think this is the Palantir forward deployed engineer model is not that different to sort of like classic YC advice around doing things that don't scale. We have this concept of like the Collison install, which is essentially we boil it down to, don't wait for people to turn up to your website, like go to them and get them to like install the software.

> Jared早先指出,我认为Palantir的前沿部署工程师模式和围绕"做那些无法规模化的事"的经典YC建议其实没那么不同。我们有一个叫"Collison安装"的概念,本质上我们把它归结为:别等着人们自己找上你的网站,而是去找到他们、让他们把软件装上。

[35:07] **SPEAKER_03:** And like physically go to them, like go to their office and like sit and text to them.

> 而且是亲自去找他们,去他们的办公室,坐下来手把手教他们。

[35:12] **SPEAKER_02:** And I feel like it's always been a great starting strategy, but most startups aren't getting big contracts off the bat. So actually the reason they have to stop doing sort of like this sort of manual high touch process is, you just, you know, the process is you just can't get the growth rates to sustain without at some point having a product that scales. And it's kind of like what we were talking about earlier. Like at some point you hopefully, you build a product so good that people can figure out themselves and then all of your problems are just scaling it. With AI what's different is because these contracts are so big now, you can actually go quite far by doing like the high touch thing.

> 我一直觉得这是一个很好的起步策略,但大多数初创公司一上来是拿不到大合同的。所以他们之所以不得不停止这种手动的、高触达的流程,是因为你——你知道,这套流程就是,不到某个时刻拥有一个能规模化的产品,你就没法维持住那个增长率。这有点像我们前面聊的:到某个时刻,你但愿构建出一个好到人们能自己搞明白的产品,然后你所有的问题就只剩下把它规模化。而在AI这里不同之处在于,因为现在这些合同这么大,你其实可以靠做那种高触达的方式走得相当远。

[35:45] **SPEAKER_02:** And maybe something you could help us out with actually is like probably a common office hour question I get is like, how far can I keep pushing this? And my advice is largely like, well, like it's okay to be doing custom work per customer. You just want to get less custom per every customer. Maybe you could give like more specific, like higher resolution advice. Like how do you know if it's okay to like keep adding new customers in this sort of like high touch, like I'm doing lots of custom work way versus, oh no, actually I need to be like abstracting out and building like an actual product here.

> 而也许你其实可以帮我们解答一下,这大概是我在office hour常被问到的一个问题:我能把这个一直推进到多远?我的建议大体上是,嗯,给每个客户做定制工作是可以的。你只是想让每个客户所需的定制越来越少。也许你能给出更具体、更高分辨率的建议。比如你怎么知道,继续以这种高触达、"我在做大量定制工作"的方式不断加入新客户是可以的,还是说,哦不,其实我需要开始做抽象、在这里构建一个真正的产品了?

[36:16] **SPEAKER_04:** Yeah. And I, and I think this, this is actually really encapsulates the key difference between, you know, the, the product market fit strategy and the FD strategy. In the product market fit strategy, you want to be doing less work for every customer. You want to be driving down costs. You want to keep the contract size the same.

> 是的。我认为这其实很好地概括了产品市场契合策略和FDE策略之间的关键区别。在产品市场契合策略里,你想为每个客户做更少的工作。你想把成本压下来。你想让合同金额保持不变。

[36:31] **SPEAKER_04:** In the FD strategy, you want to drive the contract size up. So you're doing more and more valuable work for this customer and also for future customers. And because you're doing more valuable work, it's okay. You can leave the amount of customization you do per customer the same.

> 而在FDE策略里,你想把合同金额做大。所以你在为这个客户、也在为未来的客户做越来越有价值的工作。而正因为你在做更有价值的工作,所以没关系。你可以让每个客户所需的定制量保持不变。

[36:47] **SPEAKER_02:** So the KPI or the internal metric is like contract size, not necessarily like how much custom work they're doing per customer.

> 所以那个KPI或者说内部指标是合同金额,而不一定是他们为每个客户做了多少定制工作。

[36:53] **SPEAKER_04:** There's two useful things here. So one, the thing that you can measure, yes, contract size. I would even be a little bit more general than that and say the value of the outcome you're delivering, because that's, that's actually the true thing, you know, and do you yet have the muscle in order to be able to monetize that and price that and capture that? Maybe not. But if you're able to deliver more and more valuable outcomes to the customer, then, you know, you're, you're doing something right.

> 这里有两个有用的东西。第一,你能衡量的那个,对,合同金额。我甚至会比这更一般化一点,说是你所交付成果的价值,因为那才是真正的东西,而你是否已经练出了能够将其变现、定价、并捕获它的那块肌肉呢?也许还没有。但如果你能够为客户交付越来越有价值的成果,那么你就是在做对一些事情。

[37:19] **SPEAKER_04:** The second piece that we haven't, we didn't talk about yet is the value of the product. And so. The other thing you want to measure is, are you getting more and more product leverage against that outcome? This is all extremely counterintuitive when you're in it. It's very hard if you're an FTE or if you're leading an FTE team, there's a lot of things you have to do that, that seem very counterintuitive.

> 第二块我们还没聊到的是产品的价值。所以,你要衡量的另一件事是,你是否在针对那个成果获得越来越多的产品杠杆?当你身处其中时,这一切都极其反直觉。如果你是个FDE、或者你在领导一个FDE团队,你要做的很多事情看起来都非常反直觉,那是很难的。

[37:41] **SPEAKER_04:** You have to, you know, build for the customer things they're not asking for, but that they actually want. On the product side, you often think to yourself, how do I make a product that's just really easy for every customer to use? It's very easy. And look, I struggled with this myself quite a bit leading product early on. Like you want to focus on on the user experience and you have to do that.

> 你得为客户构建他们没有开口要、但其实想要的东西。在产品这一侧,你常常会想,我怎么做出一个对每个客户都真的很容易使用的产品?它很容易用。而说实话,我自己早期领导产品时也在这件事上挣扎过不少。你想专注在用户体验上,而你确实必须这么做。

[38:02] **SPEAKER_04:** But you also have to remember your other key customer is the FTE. Your product should be, you know, ultimately delivering a good thing to the user after FTE customization, but it should be delivering leverage to the FTE who's delivering that outcome at the customer site. And that that amount of product leverage should be going up over time.

> 但你也必须记住,你另一个关键客户是FDE。你的产品最终应该是在FDE定制之后为用户交付一个好东西,但它应该是在为那个在客户现场交付成果的FDE输送杠杆。而那份产品杠杆的量,应该随时间推移不断上升。

[38:22] **SPEAKER_02:** Like they should be able to use. Your product to deliver more value to the customer without them having to go and like pull in three more engineers in order to do it. That's right.

> 就是说他们应该能够用你的产品为客户交付更多价值,而不必为此再拉进三个工程师才能做到。没错。

[38:30] **SPEAKER_04:** If you know, the first customer you deploy at takes a lot of work. If you want to then go sell that same outcome to a different customer, then that should be a lot easier at the second customer. And it should get easier still as you go customer by customer. But then if you if you really get it to work, remember that you're building a platform, so you're doing more than just, you know, a stack of vertical use cases on top of each other. If you've correctly abstracted away what the core concept is that you're really building, then you should also have an easier time.

> 要知道,你部署的第一个客户会花很多功夫。如果你接着想把同一个成果卖给另一个客户,那在第二个客户那里就应该容易很多。而且随着你一个客户接一个客户地推进,它应该会越来越容易。但如果你真的把它做成了,记住你在构建的是一个平台,所以你做的不只是把一堆垂直用例一层层叠在一起。如果你正确地把你真正在构建的核心概念抽象出来了,那么你也应该会更轻松。

[39:01] **SPEAKER_04:** You should have more product leverage even when you're not doing that use case, when you're doing something that's sort of similar. Or you will find that your FTEs, if it's a really if it's really good, you'll find your FTEs can figure out some new way to use that technique you built to solve something completely different.

> 即便当你不在做那个用例、而是在做某个有点类似的事情时,你也应该拥有更多的产品杠杆。或者你会发现你的FDE——如果它真的、真的很好——你会发现你的FDE能想出某种全新的方式,用你构建的那项技术去解决一个完全不同的问题。

[39:16] **SPEAKER_02:** There's always like an internal market dynamic going on where like if you've built it really well, then the FTE should like choose to use it and you should see demand from the FTE. So it's a really good way to use your sort of like abstracted product versus just like hacking a one off solution themselves.

> 总有一种内部市场动态在发生:如果你把它构建得真的很好,那么FDE就应该会选择去用它,你应该会看到来自FDE的需求。所以这是一个很好的检验方式,看你那个抽象化的产品(相对于他们自己临时手搓一个一次性解决方案)是不是真的好用。

[39:29] **SPEAKER_04:** Yes. Although I will just note, this is a very painful process for everyone involved. I probably can't use the word pain often enough in the FTE. You know, there are many times where I built something I thought it was amazing and I thought it was beautiful. Not not there yet. Right.

> 是的。不过我得说一句,这对所有相关的人来说都是一个非常痛苦的过程。在FDE这件事上,我用"痛苦"这个词可能都用得不够多。有很多次,我构建了某个东西,我觉得它很了不起、我觉得它很漂亮。还没到那个份上,对吧。

[39:43] **SPEAKER_04:** But it would it really would help the FTEs as soon if they just had the the ability to see it. And I'd be like, please use my product. I'd be like, no, it's just this is way more work. It's like not helpful. And then people say, let's be honest, most of the time I was probably wrong and I was building the wrong product for them.

> 但只要FDE有能力看到它,它其实真的会帮到他们。我就会说,拜托,用我的产品吧。他们会说,不,这反而是更多的工作。这没帮助。然后人们说,说实话,大多数时候大概是我错了,我在为他们构建错误的产品。

[39:57] **SPEAKER_04:** And, you know, I should see that. But sometimes also I was on the right track. But, you know, I hadn't done enough to make it easy for the FTEs to use. And so, you know, I would send, you know, the developers out into the field to deploy those early solutions and get them over the line, even to the point where the FTEs could use them profitably.

> 而我应该看到这一点。但有时候我也走在正确的轨道上。只不过,我还没有做足够多的工作让FDE用起来足够容易。所以我会把开发人员派到一线去部署那些早期的解决方案、把它们做到能跨过那道线,甚至做到FDE能有利可图地使用它们的程度。

[40:16] **SPEAKER_02:** Are the FTEs always right in that case? Or should the founders sometimes be just top down and say, like, actually, I just want you to do that, do it this way?

> 在那种情况下,FDE总是对的吗?还是说创始人有时候就应该自上而下地说,其实,我就想让你去做那个、按这个方式做?

[40:24] **SPEAKER_04:** I mean, the answer is like, yes, to all all of these things. The other thing that comes up over and over again is just how much the right answer here is a matter of judgment. And I think I think going back to this question about product vision, right? Like, what is the right product that generalizes from, you know, this customer to the next three to the next ten? You you very literally do not have the the information needed to answer that when you see that first customer.

> 我是说,答案就是,对所有这些问题都"是"。另一件反复出现的事情,就是这里正确答案在多大程度上是一个判断问题。我想,回到关于产品愿景的这个问题,对吧?比如,从这个客户泛化到下三个、下十个客户的那个正确产品是什么?当你看到第一个客户时,你真的字面意义上不具备回答这个问题所需的信息。

[40:50] **SPEAKER_04:** And so it's just it becomes a judgment call.

> 所以它就变成了一个判断的抉择。

[40:52] **SPEAKER_00:** So in the context of. How all these FTE companies price very differently based on outcome. How does that fit in with now the culture doing demos? Because there's this this thing and at least in SaaS or I used to get this pushback from my engineers, demo driven product development, it would be sort of looked down upon. But in this case, it's different for FTEs, right?

> 那么在所有这些FDE公司基于成果、以非常不同的方式定价的语境下,这跟现在这种做demo的文化是怎么契合的?因为有这么一件事,至少在SaaS里、或者我过去常从我的工程师那里得到这种反对——demo驱动的产品开发,那会被有点看不起。但在这种情况下,对FDE来说是不同的,对吧?

[41:14] **SPEAKER_04:** One of the interesting things that happens there is because you have to go repeatedly show this to new customers, you're forced to give these new demos. But but actually, I think demo driven development works really well. If you have the right kind of product. So, you know, in the early days of Palantir, we actually had one demo. It was a flow where you're, you know, stopping a terrorist plot.

> 那里发生的一件有趣的事情是,因为你得反复把这个东西展示给新客户,你被迫要不断给出这些新的demo。而其实,我认为demo驱动的开发效果非常好。前提是你有正确类型的产品。所以你知道,在Palantir早期,我们实际上只有一个demo。它是一个流程,你在挫败一起恐怖袭击阴谋。

[41:32] **SPEAKER_04:** And we started this with, you know, just one of our features. And every time we integrated a new feature, we had to think to ourselves, how do I show that this new feature is actually helpful for the analyst who's going through this demo, who's stopping this plot? You know, when we integrated a histogram, we had to say, well, how do we actually use this? How does that work with the existing? Features that we already had?

> 而我们是从、你知道,仅仅我们的一个功能开始做起的。而每次我们集成一个新功能,我们都不得不问自己,我怎么展示这个新功能对那个正在走这个demo、正在挫败这起阴谋的分析师是真正有帮助的?你知道,当我们集成一个直方图时,我们不得不说,那我们到底怎么用它?它怎么和我们已有的功能配合?

[41:54] **SPEAKER_04:** And we went this, you know, we integrated a map and we had the same question. And if you think about the world from what am I building, then, you know, you're thinking about your capabilities. You might think of each of these features individually and how to build the best version of these features. But when you're building a demo, you're thinking about it from the customer's perspective. And a really good demo is something where you show it to the customer and you are creating desire in that customer for what you're doing.

> 然后我们又集成了一张地图,我们有同样的问题。如果你从"我在构建什么"来看世界,那么你在想的是你的各项能力。你可能会单独去想这些功能中的每一个、以及怎么把这些功能各自的最佳版本构建出来。但当你在构建一个demo时,你是从客户的视角来思考它。而一个真正好的demo,是那种你展示给客户看、并在那个客户心里为你所做的事情创造出渴望的东西。

[42:22] **SPEAKER_04:** They have to see what you're doing. And just want to reach out and grab it and bring it into their life. And if you see that, then you know that you've identified a real pain for the customer. And by doing that, that also forces you to develop a better product, because not only are you thinking, OK, do each of these features make sense in isolation, but how do they work together? If I'm going to be showing this demo over and over again, even just simple things like moving from one feature to another, that part of the path has to be very straightforward.

> 他们必须看到你在做什么。然后就想伸手把它抓过来、带进他们的生活。如果你看到了这一点,那你就知道你识别出了客户一个真实的痛点。而通过这么做,它也迫使你开发出一个更好的产品,因为你不仅在想,好,这些功能单独看是否都说得通,还在想,它们怎么协同工作?如果我要一遍又一遍地展示这个demo,那么哪怕是很简单的事情,比如从一个功能切换到另一个功能,那段路径也必须非常顺畅。

[42:50] **SPEAKER_04:** And those are those are all the kinds of product pain points that you would want to have. And that's something that you would often see, but only later after you've actually deployed to the customer. So what the demo does is it is it changes the locus of what you're thinking about from thinking about what can I build to what is it that the customer wants? And am I am I solving that pain point for the customer?

> 而那些都是你会想拥有的那类产品痛点。那是你往往会看到、但只有在你真正部署到客户之后才会较晚看到的东西。所以demo所做的,是它把你思考的焦点从"我能构建什么"转移到"客户想要的到底是什么?我是不是在为客户解决那个痛点?"

[43:11] **SPEAKER_00:** So it sounds like it's sort of this you have to keep doing the gradient ascent in this very, very highly dimensional, multidimensional space. And you keep changing the variables.

> 所以听起来这有点像,你必须在这个非常非常高维、多维的空间里不断做梯度上升。你不断改变各个变量。

[43:21] **SPEAKER_04:** Yeah, yeah, I think. Yeah. Maybe. I think that's a really key point here is that the kind of company you have to build is a learning company. And I think everybody wants to build a learning company.

> 是的,是的,我想。是的。也许吧。我认为这里一个真正的关键点是,你必须构建的那种公司是一家会学习的公司。而我认为每个人都想构建一家会学习的公司。

[43:31] **SPEAKER_04:** But if you're a company like Google or Meta, it's very easy not to learn because what you're doing right now is working. And if you just keep doing it, the market is growing. You know, everybody wants to do what you're doing. You can you can just sort of keep coasting on the same strategy and it's paying off for you. My advice to people, if they're thinking about where to join a company, is I tell them to join a company.

> 但如果你是像Google或Meta那样的公司,不学习是很容易的,因为你现在正在做的事情是奏效的。你只要一直这么做下去,市场就在增长。你知道,每个人都想做你在做的事情。你可以就这样一直在同一个策略上滑行,而它一直在给你带来回报。我给人们的建议是,如果他们在考虑加入哪家公司,我会告诉他们加入一家……

[43:53] **SPEAKER_04:** Not necessarily a small company, right, but a young company, because a young company is still figuring things out. It's still learning. It hasn't succeeded yet. You know, if you're just out of college, you want a young company that is growing really fast and then you'll be you'll see what success looks like. That positions you exactly to be a founder of your own company later.

> ……不一定是小公司,而是一家年轻的公司,因为一家年轻的公司还在摸索。它还在学习。它还没成功。你知道,如果你刚从大学毕业,你想要一家增长非常快的年轻公司,那样你就会看到成功是什么样子。那正好把你摆在一个日后能成为你自己公司创始人的位置上。

[44:12] **SPEAKER_04:** This is why Palantir has birthed so many other startups is because even as a very large company, it is still a company where everybody all the time is learning, focused on learning. And. You know, always doing that same grinding motion that it is to be a new startup, because, you know, yes, you know, new startups, a lot of pain there, too, right? That is like probably like the canonical part of the YC experience is that it's not coasting. It's working really, really hard on something that you're not quite sure if it's going to succeed.

> 这就是为什么Palantir孵化出了这么多其他初创公司,因为即便作为一家非常大的公司,它仍然是一家所有人始终都在学习、专注于学习的公司。并且,总是在做当一家新初创公司时的那种同样的、磨人的动作,因为,是的,你知道,新初创公司,那里也有很多痛苦,对吧?那大概就是YC体验的典型部分——它不是滑行。它是在一件你并不完全确定是否会成功的事情上非常非常努力地干活。

[44:42] **SPEAKER_02:** Obviously, I mean, a monster success for Palantir. They're now a super big company, huge organization. We heard that you're joining another large organization, the U.S. Army Reserve.

> 显然,我是说,Palantir是个巨大的成功。他们现在是一家超大的公司、庞大的组织。我们听说你正要加入另一个大组织——美国陆军预备役。

[44:51] **SPEAKER_02:** Maybe you could tell us a bit about that. And are there any lessons from the Palantir experience you're planning to apply there?

> 也许你能跟我们讲讲这个。而且Palantir的经验里有没有什么教训是你打算应用到那里的?

[44:56] **SPEAKER_04:** Yeah, absolutely. I've recently joined the U.S. Army Reserve as part of Detachment 201. And so, you know, one thing just to get out of the way is to say that what everything I'm talking about here, these are my opinions.

> 是的,当然。我最近作为201分遣队的一员加入了美国陆军预备役。所以有一件事得先说清楚,我在这里谈的一切,都是我个人的观点。

[45:07] **SPEAKER_04:** These are not the opinions of the U.S. Army, the Defense Department, the U.S. Government.

> 这些不是美国陆军、国防部、美国政府的观点。

[45:11] **SPEAKER_04:** But I think it's this it's been this absolutely intense experience and it's a really interesting story. So we are part of a unit that's advising the Army on technology. And we are not just civilian advisors. We are actual officers. So, you know, we took the oath.

> 但我认为这是一段绝对紧张、密集的经历,而且是一个非常有意思的故事。所以我们是一个向陆军就技术提供建议的单位的一部分。而我们不只是文职顾问。我们是真正的军官。所以,你知道,我们宣了誓。

[45:29] **SPEAKER_04:** I'm a lieutenant colonel in the U.S. Army.

> 我是美国陆军的一名中校。

[45:31] **SPEAKER_03:** I heard you went through basic training, too.

> 我听说你还经历了新兵训练。

[45:33] **SPEAKER_04:** I yeah, we went through the direct commissioning course. We've been trained by military academics often at five in the morning because that's the time that works for people on the East Coast and doesn't conflict with our day jobs. We learn from officers. I had to take the Army fitness test, which since I am not very fit, you know, it was something that I had to do. But.

> 我,是的,我们走了直接授衔课程。我们由军事学者培训,常常是在早上五点,因为那是东海岸的人合适、又不与我们日常工作冲突的时间。我们向军官学习。我得参加陆军体能测试,由于我不怎么健壮,你知道,那是我不得不去做的一件事。不过。

[45:52] **SPEAKER_04:** Something that I had to train for for nine months, but it really matters because we're not just giving advice on the side. We have skin in the game. We are actually part of the organization that we're advising and the Army itself. The leadership is very different from what it felt like in the early days of Palantir when we were working them back in 2005 or 2010. General Randy George, the chief of staff of the Army, secretary of the Army Driscoll, they have articulated a plan for the transformation.

> 是我得为之训练了九个月的一件事,但它真的很重要,因为我们不只是在旁边给建议。我们是有切身利害的。我们实实在在是我们所建言的那个组织、以及陆军本身的一部分。而领导层跟我们2005年或2010年早期在Palantir跟他们打交道时的感觉非常不同。陆军参谋长Randy George将军、陆军部长Driscoll,他们已经清晰阐述了一个转型计划。

[46:22] **SPEAKER_04:** Of the Army. They know that the Army needs to change from, you know, the kind of from finding the kinds of wars we fought in Iraq and Afghanistan to fighting the kind of wars that are being fought today in Ukraine or what it would look like if we face large scale combat operations in the Pacific. They know the Army needs to move faster. They know the Army needs to change. And we are a part of that strategy that they're executing as they brought us in.

> 关于陆军的转型。他们知道陆军需要从、你知道,从我们在伊拉克和阿富汗打的那类战争,转变为应对今天在乌克兰正在打的那类战争、或者一旦我们在太平洋面临大规模作战行动会是什么样子。他们知道陆军需要走得更快。他们知道陆军需要改变。而我们是他们正在执行的那个战略的一部分,他们就是为此把我们招进来的。

[46:44] **SPEAKER_04:** They you know, they have given us they've outlined the priorities for the Army. They've given us each an area in which we're supposed to operate. But they've also given us the freedom to, you know, go around, look for problems, work directly with the officers on the ground to solve those problems, or if need be, to escalate that to leadership and get that fixed. And so I think one of the things that's that's really interesting about it is, you know, in many ways, it does feel a lot like running the FDA strategy, you know, on the Army. We we get to see, you know, what is that?

> 他们已经给了我们、他们已经勾勒出了陆军的优先事项。他们给了我们每个人一个我们应当在其中开展工作的领域。但他们也给了我们自由,去四处走动、去寻找问题、直接和一线的军官协作解决那些问题,或者在必要时把问题上报给领导层、让它得到解决。所以我认为其中一件真正有意思的事情是,在很多方面,它确实感觉很像在陆军身上运行FDE策略。我们得以看到,那是什么?

[47:13] **SPEAKER_04:** What are the CEOs? What are the leadership's top five priorities? Can we make progress against those? But also in a world where you see that there's a disconnect. There's a disconnect between what the leadership wants and 20 years of how things have been implemented, and it takes a long time to change that.

> CEO们的、领导层的前五大优先事项是什么?我们能不能针对那些取得进展?但同时也是在这样一个世界里:你看到存在一种脱节。领导层想要的东西,和过去20年事情实际是怎么落实执行的之间,存在脱节,而改变那个需要很长时间。

[47:30] **SPEAKER_04:** And so, you know, we're helping them make that change. I'm really eager to have the opportunity to make a difference.

> 所以,你知道,我们在帮他们做出那个改变。我真的很渴望有这个机会去带来一些不同。

[47:36] **SPEAKER_03:** There's a question that we love to ask people on on this podcast, which is what do you think are the best opportunities for startup founders to work on right now?

> 我们这档播客特别喜欢问人们一个问题,那就是:你认为现在对创业创始人来说,最好的、值得去做的机会是什么?

[47:43] **SPEAKER_04:** Well, you know, I think this really goes back to exactly this question of why is it that agents are pursuing the FDA strategy? And, you know, if you if you zoom out and I put on my research hat for once in this podcast, I think what we've seen is that that capability improvements are actually extremely fast. If you you know, yes, I heard people, you know, after GPT-5, people feel like things are plateauing. But actually, if you look at this time period between April 2024, when the best model, you know, the release of GPT-4.0 and April 2025 and the release of O3, that's an extremely fast.

> 嗯,你知道,我认为这真的又回到了这个问题:为什么智能体在追求FDE策略?而且,如果你拉远来看——在这档播客里我难得戴上一次我的研究者帽子——我认为我们所看到的是,能力的提升其实极其快。如果你,是的,我听到人们在GPT-5之后,人们感觉事情在趋于平台期。但其实,如果你看2024年4月——当时最好的模型、GPT-4o的发布——到2025年4月、o3的发布之间的这段时间,那是一个极其快的……

[48:22] **SPEAKER_04:** Rate of progress. And I think that's just going to continue. I think we're going to see capabilities continue to move quickly. But what's what's really shocking, actually, is that the adoption is not anywhere near what you would expect from the speed of these capabilities. What the world is going to look like over the next five years is that the capabilities just race ahead and race ahead and race ahead.

> ……进步速率。而我认为这只会继续下去。我认为我们会看到能力继续快速推进。但真正令人震惊的其实是,采用的速度远远达不到你从这些能力的推进速度所会预期的程度。未来五年世界会是什么样子:能力就是一路狂奔、狂奔、再狂奔。

[48:42] **SPEAKER_04:** And somehow the world feels increasingly banal. You know, you're like you're in your Waymo and you aren't thinking, oh, my God, it's not you know, no one's driving this. You're like, oh, traffic.

> 而不知怎的,这个世界却感觉越来越平淡无奇。你知道,就像你坐在你的Waymo里,你并不会想,我的天,没有、你知道,没人在开这辆车。你想的是,唉,堵车。

[48:52] **SPEAKER_02:** It's really slow. Yeah.

> 真的好慢。是啊。

[48:53] **SPEAKER_04:** And so, you know, just like with the world of the FDEs where you have, you know, the FDEs filling the gap between this product and what the customers need. I think, you know, this is a time where there's so much availability to fill the gap between what the capabilities can actually do and what the customers are able to adopt. And in the early days of AI, we sat around a table in 2018 and talked about what it looked like when AGI was built. People thought, oh, well. You know, it's going to it's going to maybe maybe over the weekend it's going to come alive and it's going to take over the world.

> 所以,你知道,就像FDE的世界里,你有FDE去填补这个产品和客户所需之间的差距一样。我认为,这是一个存在大量机会去填补"能力实际能做到什么"与"客户能够采用什么"之间差距的时代。而在AI早期,我们2018年围坐在一张桌子旁,谈论当AGI被造出来时会是什么样子。人们当时想,哦,嗯。你知道,它会……也许就在某个周末它会活过来、会接管世界。

[49:28] **SPEAKER_04:** And, you know, one of the things that I think people missed in that was that, you know, AI needs to be adopted. It's something that doesn't just happen by itself, but you need human ingenuity and exploration and while dealing with a lot of pain in order to make that happen. And so I think there's just a huge amount of opportunity out there looking at. What are the capabilities that are there? But what does it take to make them really genuinely useful to people?

> 而,你知道,我认为人们当时忽略的一件事是,你知道,AI是需要被采用的。它不是某种会自己凭空发生的东西,你需要人类的巧思、探索、以及在承受大量痛苦的同时,才能让它发生。所以我认为外面存在着巨大的机会,去审视:那里已有的能力是什么?但要让它们对人们真正、实实在在地有用,又需要什么?

[49:57] **SPEAKER_03:** There's an analogy that occurs to me. This might be a little bit forced, but it's almost like open AI is the home product team and the startups are the FDEs out figuring out how to get adoption of of of the like research that open AI is cooking up back at the home office.

> 我想到一个类比。这可能有点牵强,但几乎就像是OpenAI是那个"总部产品团队",而各家初创公司是外派的FDE,在摸索如何把OpenAI在总部炮制出来的那些研究成果推向被采用。

[50:12] **SPEAKER_04:** I think that's not a bad analogy at all. I think that I think that is that is maybe the underlying truth of what's making this whole FTE strategy exciting. Exactly.

> 我认为这个类比一点都不差。我认为那也许正是让整个FDE策略令人兴奋的底层真相。没错。

[50:22] **SPEAKER_02:** Okay, that's all we have time for here today, Bob. Thanks so much for joining us. That was really, really interesting. We all learned a lot and we'll see you all here next time.

> 好的,Bob,今天我们时间就到这里了。非常感谢你参加我们的节目。这真的、真的非常有意思。我们都学到了很多,我们下次再见。
