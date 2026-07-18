# 全文转录 · 六个月折腾折出一家 $100M ARR 公司:Emergent 的打法

> ▶ [YouTube](https://www.youtube.com/watch?v=yyXCQHX55N4) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/yyXCQHX55N4.md) &nbsp;·&nbsp; Emergent: How Six Months of Tinkering Led To A $100M ARR Company

> 中英对照 · 每段英文原文下附中文翻译

[00:00] **SPEAKER_00:** If you look at the last 30 years, most of the economic gain in the world has come from software companies. If you remove all the software companies from NASDAQ and S&P, you'll see it's been just a flat line. And we started thinking, okay, what if we can bring this power to almost everybody in the world? Welcome.

> 如果你看过去 30 年,世界上大部分的经济增长都来自软件公司。如果你把纳斯达克和标普里所有的软件公司拿掉,你会发现指数几乎是一条平线。于是我们开始思考:如果我们能把这种能力带给世界上几乎每一个人,会怎么样?欢迎。

[00:20] **SPEAKER_01:** Super excited to be here. What a crowd. So, Mukund, maybe not everybody knows what a merchant is and also what a big deal it is. For those who don't know, a merchant is one of the fastest AI growing, is the fastest growing AI companies in the world. And really, I would say one of the first truly AI native companies in India to get to real scale.

> 非常高兴来到这里。这么多人。Mukund,也许不是每个人都知道 Emergent 是什么,以及它有多了不起。对于不了解的人,Emergent 是世界上增长最快的 AI 公司之一,可以说是增长最快的 AI 公司。而且我要说,它是印度最早真正做到规模化的 AI 原生公司之一。

[00:42] **SPEAKER_00:** Right, right.

> 对,对。

[00:43] **SPEAKER_01:** And so you're going to get to hear from, I really see you as like a pioneer of a next generation of startups coming out of India. And you're going to get to hear how he's done it. To start with, maybe you can just tell everybody what a merchant is.

> 所以你们将会听到他的分享,我真的把你看作是从印度走出来的下一代创业公司的先驱。你们将会听到他是怎么做到的。首先,也许你可以先告诉大家 Emergent 是什么。

[00:56] **SPEAKER_00:** Yeah, so, I mean, thanks for inviting me. I'm super excited. I can't imagine like so many people coming to the school and the whole energy in India about the whole YC trip has been amazing. I was at IT Delhi a couple days back, same energy. So, super excited to be here.

> 好的,首先谢谢邀请我。我非常兴奋。我没想到会有这么多人来到这里,而印度对整个 YC 之行所展现出的那种能量真是太棒了。几天前我在德里理工学院(IIT Delhi),也是同样的能量。所以能来到这里我非常兴奋。

[01:14] **SPEAKER_00:** Immersion is a platform that allows anybody without any programming knowledge to be able to build software that you can actually ship, that your users can use, that you can monetize. Essentially, we're riding on this whole wave of coding becoming easier with AI. And when we started our journey, we actually started off as a research lab building coding agents, became world number one on Sweetbench, which is the benchmark for all of the coding agent. It was just a four people team, which actually got us there. And then we started thinking about like, hey, what would happen in the world if we can democratize coding for everybody?

> Emergent 是一个平台,它让任何没有编程知识的人都能构建出真正可以上线发布、可以让用户使用、可以变现的软件。本质上,我们乘着 AI 让编程变得更容易的这股大浪潮。我们的旅程一开始其实是一个研究实验室,做编程智能体(coding agents),在 SWE-bench 上做到了世界第一,而 SWE-bench 是所有编程智能体的基准测试。当时只有一个四人团队,就是这个团队把我们带到了那里。然后我们开始思考:嘿,如果我们能让编程对每个人都普及化,世界会变成什么样?

[01:46] **SPEAKER_00:** And me being a programmer, Madhav was my co-founder, was my twin brother. Both of us have been programming since age 12 and super, super passionate about programming. And one of the things that we realized that, if you look at like last 30 years, like most of the economic gain in the world has come from software companies. If you remove all the software companies from, you know, Nasdaq and S&P, you'll see it's been just a flat line. And besides thinking, OK, what if we can bring this power to almost everybody in the world?

> 我本身是程序员,我的联合创始人 Madhav 是我的双胞胎兄弟。我们俩从 12 岁起就开始编程,对编程非常非常热爱。我们意识到的一件事是:如果你看过去 30 年,世界上大部分经济增长都来自软件公司。如果你把纳斯达克和标普里所有的软件公司拿掉,你会发现就是一条平线。于是我们开始思考:如果我们能把这种能力带给世界上几乎每一个人,会怎么样?

[02:14] **SPEAKER_00:** Like there are a billion people with so many ideas, so many ideas just die because you do not have an access to sort of bring them to life. And that was the mission that we started with. Today, we have more than eight and a half million people who are using the platform, more than 10 million people. More than 10 million apps have been built. We recently crossed $100 million in annualized run rate.

> 有十亿人拥有那么多的想法,而那么多想法就这样夭折了,因为你没有途径把它们变成现实。这就是我们出发时的使命。今天,我们已经有超过八百五十万人在使用这个平台,超过一千万人。已经有超过一千万个应用被构建出来。我们最近突破了一亿美元的年化收入(annualized run rate)。

[02:34] **SPEAKER_00:** Today, one of the fastest growing startups in the world. And the reason is that we are able to allow people to actually really ship what they dream. And it's as easy as just chatting with your agent. And we take care of everything from hosting, deployment, maintenance of the product, and truly unlocking the power of, you know, bringing an idea to life with just chatting with your agent. How long since you launched the current version of the product?

> 今天,我们是世界上增长最快的创业公司之一。原因在于我们能让人们真正把他们梦想的东西发布出去。而这就像和你的智能体聊天一样简单。我们负责一切——从托管、部署到产品维护,真正释放了那种只需和智能体聊天就能把一个想法变成现实的力量。你们发布当前版本的产品有多久了?

[02:55] **SPEAKER_01:** Yeah, we launched about nine months back. Nine months. OK. So keep in mind, this is basically a nine month old company. Tell us like about the scale that you're operating at just nine months in.

> 是的,我们大约在九个月前发布的。九个月。好的。所以请记住,这基本上是一家成立九个月的公司。给我们讲讲,才九个月你们就在多大的规模上运营了。

[03:07] **SPEAKER_00:** Yeah. So we have close to about eight and a half million users on the platform. And we are well over 100 million in annualized revenue run rate. And again, like I think the latent demand in the market is really, really high. People, there are a lot of people who want to build software and so far have not been able to have the access to these tools.

> 是的。我们平台上有接近八百五十万用户。我们的年化收入运营率(annualized revenue run rate)远超一亿美元。而且我认为市场上潜在的需求真的非常非常高。有很多人想要构建软件,但一直以来都没有机会接触到这些工具。

[03:29] **SPEAKER_00:** And platform like ours truly enables them to ship, you know, an idea that they have had in mind. A lot of our users are actually entrepreneurs who do not have a tech team and have been sort of handicapped by access to technology and now are able to build.

> 而像我们这样的平台真正让他们能够把心中的想法发布出来。我们很多用户其实是创业者,他们没有技术团队,一直以来都因为无法获得技术而受制约,现在终于能够构建了。

[03:43] **SPEAKER_01:** Who are your users and also where are your users?

> 你们的用户是谁,以及你们的用户在哪里?

[03:47] **SPEAKER_00:** Yeah, so we have users all across the globe in 190 countries. When I started, when I actually like just to give a little background, right, when I came to India in 2014, I was before that I was in Google in the U.S. And I've always had this thought that, hey, why is there no Google from India? Why is there no Facebook from India?

> 是的,我们在全球 190 个国家都有用户。我刚开始的时候——先给点背景,2014 年我回到印度,在那之前我在美国的谷歌工作。我一直有个想法:嘿,为什么没有一个从印度走出来的谷歌?为什么没有一个从印度走出来的 Facebook?

[04:05] **SPEAKER_00:** We have so much talent, so much engineering talent. In fact, you look at the top leadership of all of these companies, you know, like Microsoft, Google, you know, there are sort of Indian folks who have sort of gone there. Right. And I've always wondered, why is there no sort of technology first global company from India? Right. And so when I was after Tanzu, when I was thinking about what to do next, like one of the things that I had in the back of my mind was that I truly want to build a global company from India.

> 我们有这么多人才,这么多工程人才。事实上,你看这些公司——微软、谷歌——的最高管理层,都有一些印度人去到了那里。我一直很好奇,为什么没有一个以技术为先、从印度走出来的全球性公司?所以在 Dunzo 之后,当我思考接下来要做什么时,我心里一直有个念头,就是我真的想从印度打造一家全球性公司。

[04:29] **SPEAKER_00:** Like just like Facebook and Google. And today we have people have been using us over 190 countries and most of the like revenue comes from U.S. and Europe. India accounts for about 10 percent of our revenue.

> 就像 Facebook 和谷歌那样。今天我们在超过 190 个国家都有人在使用我们,而大部分收入来自美国和欧洲。印度大约占我们收入的 10%。

[04:42] **SPEAKER_00:** And but yeah, our audience is fully global.

> 是的,我们的用户群完全是全球性的。

[04:45] **SPEAKER_01:** And I'm not sure that people know, but before you started emerging, you started another company that I'm sure they all know called Dunzo, which is like a really big deal. You raised like a half a billion dollars and it was like it's a huge company.

> 我不确定大家是否知道,但在你创办 Emergent 之前,你还创办了另一家公司,我相信大家都知道,叫 Dunzo,那可是相当了不起的。你们融了大约五亿美元,是一家巨大的公司。

[04:59] **SPEAKER_00:** Yeah. Yeah. I'm sure in Bangalore, I think a lot of people would know us. You know, we were pretty popular in Bangalore. We like, you know, at a peak, we were one of the most loved consumer brands in the country.

> 是的,是的。我相信在班加罗尔,很多人都会知道我们。你知道,我们在班加罗尔相当受欢迎。在巅峰时期,我们是全国最受喜爱的消费品牌之一。

[05:11] **SPEAKER_00:** Even today, when people ship something, they say, hey, Dunzo it and almost became a verb in the country. At peak, we were doing about 10 million monthly orders. We were one of the first people to start the trend of quick commerce in the country. The 10 minute delivery trend, you know, it was a pretty different journey. Like I was solving problems with a very operational nature.

> 即便到今天,当人们要寄送东西时,他们会说"嘿,Dunzo 一下",这在印度几乎变成了一个动词。在巅峰时,我们每月大约有一千万单。我们是全国最早开创即时电商(quick commerce)潮流的公司之一,就是那个 10 分钟送达的潮流。那是一段非常不同的旅程。我当时解决的是非常偏运营性质的问题。

[05:29] **SPEAKER_00:** Also, like last mile logistics, you know, how do you sort of set up the Darkstone network? And the lesson that, you know, like I would say was applicable there and is applicable here as well, is we picked up to solve the hard problems. When we started Dunzo, there were about 87 companies which were doing exactly the same thing. Right. Because we had it was very simple.

> 还有最后一公里物流,你知道,怎么去搭建暗店(dark store)网络。我要说的一个教训,在那里适用,在这里也同样适用,那就是:我们选择去解决那些困难的问题。当我们创办 Dunzo 时,大约有 87 家公司在做完全一样的事情。因为这件事很简单。

[05:52] **SPEAKER_00:** You could just WhatsApp us and we would, you know, we were kind of like a concierge on WhatsApp. So it was super easy to get started. But I think the hard part was. Last mile, like how do you sort of really make sure that the end consumer actually gets the product, the product is delivered in the right state. And we chose to sort of do that, you know, we were actually doing deliveries ourselves early on, like I had, you know, a bike and a car and I would just in the night get an order.

> 你只需要在 WhatsApp 上给我们发消息,我们就会——我们有点像 WhatsApp 上的私人管家。所以上手非常容易。但我觉得难的部分是最后一公里,怎么真正确保最终消费者拿到产品,而且产品是以正确的状态送达的。我们选择去做这件事,早期我们其实是自己在做配送,我有一辆摩托车和一辆汽车,晚上一接到订单,

[06:15] **SPEAKER_00:** I would I would jump on a bike myself and go and deliver. And I think our leader is just doing things yourself. And this is one of the YC mantra doing things that don't scale. But it really, really helps you get close to the customer, understand the real pain point, whether there's a value or not. And I think like.

> 我就会亲自跳上摩托车去送货。我觉得我们的心得就是亲力亲为。这也是 YC 的一句箴言——做那些无法规模化的事(doing things that don't scale)。但这真的非常有助于你贴近客户,理解真正的痛点,判断到底有没有价值。我觉得就是,

[06:29] **SPEAKER_00:** Just just, you know, being a customer yourself or doing things for the customer really, really helps.

> 就是自己成为客户,或者亲自为客户做事,这真的非常有帮助。

[06:35] **SPEAKER_01:** Can can we actually go back in time a bit and talk a little bit about your personal background? I learned just a couple of days ago that a merchant is actually not just your second company, but your fifth startup. This guy's actually started five startups. Yeah. Tell us like, yeah, maybe tell us a bit about your early career, where you grew up and went to school, coming to the U.S.

> 我们能不能稍微回到过去,聊聊你的个人背景?我几天前才知道,Emergent 其实不只是你的第二家公司,而是你的第五家创业公司。这家伙其实创办了五家创业公司。是的,给我们讲讲你早期的职业生涯,你在哪里长大、上学,来到美国,

[06:59] **SPEAKER_01:** and just sort of like getting started.

> 以及最初是怎么起步的。

[07:00] **SPEAKER_00:** Yes. I actually grew up in a very, I would say, middle class, upper middle class family. My dad is an engineer and obviously, like, got into engineering college, did my engineering, always had this idea that I want to do something of my own. I actually very early on saw a lot of videos of Steve Jobs and was like really, really inspired. I mean, I saw him launching the first iPhone in 2007, and that was the moment like, you know, I thought, oh, I want to bring something to the world.

> 是的。我其实是在一个我会说是中产、中上层家庭长大的。我父亲是工程师,很自然地,我考进了工程学院,读了工程,一直有个想法,就是我想做点属于自己的东西。我很早就看了很多史蒂夫·乔布斯的视频,深受启发。我看了他 2007 年发布第一代 iPhone,那一刻我就想,哦,我想给世界带来点什么。

[07:31] **SPEAKER_00:** You know, in similar fashion. And in fact, I went to Spain for an internship in 2008, bought an iPhone. I mean, it didn't work in India, but I just bought it because I liked it so much. Just bought it as a souvenir for myself, tried to hack it to make it work. And then 2009 is when I went to U.S. to do my Ph.D.

> 用类似的方式。事实上,2008 年我去西班牙实习,买了一部 iPhone。它在印度用不了,但我就是太喜欢它了所以买了。就当作给自己的一件纪念品,还试着破解它让它能用。然后 2009 年我去美国读博士。

[07:51] **SPEAKER_00:** And then did an internship at Google. I liked it so much. And whatever research I was going to do, Google had actually done that research already two years back. So I thought there was no point. So I dropped out of school.

> 然后我在谷歌实习。我太喜欢了。而且我打算做的研究,谷歌其实两年前就已经做过了。所以我觉得没有意义。于是我从学校退学了。

[08:00] **SPEAKER_00:** I dropped out of the Ph.D. program, joined Google, was in the search ranking team. There was a 50 people team that controlled all of Google search ranking. I was the youngest person in that team.

> 我从博士项目退学,加入了谷歌,进了搜索排序团队。那是一个 50 人的团队,掌管着整个谷歌的搜索排序。我是那个团队里最年轻的人。

[08:09] **SPEAKER_00:** So I got a lot of liberty to sort of, you know, question a lot of things because I was, you know, a young person who could just just challenge the system. And at that time, Google was very anti-machine learning, like they didn't want to like have machine learning in search. And I was a machine learning engineer. So so I got a lot of, you know, leeway in terms of asking a lot of questions, saying, hey, like, why are we not using machine learning here? Eventually, I got to push some of the biggest changes in search ranking when I was there for a couple of years, then got bitten by the startup bug, left that Google, started a company which was trying to build a group education platform where you can actually, you know, bring a group group class together, raise a bunch of money.

> 所以我有很大的自由去质疑很多事情,因为我是个年轻人,可以直接挑战这套系统。当时谷歌非常反对机器学习,他们不想在搜索里用机器学习。而我是个机器学习工程师。所以我有很大的余地去问很多问题,说,嘿,我们为什么不在这里用机器学习?最终,在我待的那几年里,我推动了搜索排序中一些最大的变革。然后我被创业的念头击中了,离开了谷歌,创办了一家公司,试图打造一个团体教育平台,你可以把一群人组成一个班,融了一笔钱。

[08:50] **SPEAKER_00:** Eventually, like we pivoted into a B2B software company and realized that my passion was not that I really wanted to sort of solve education, wanted to build something consumer first. So return the money, shut down that startup, started another company into sort of habit creation. How do you sort of help people form better habits? Same time, got married. My wife didn't want to move to U.S., so I moved back to India and I thought I could do startup from anywhere.

> 最终我们转型成了一家 B2B 软件公司,然后我意识到我的热情并不在此,我真正想解决的是教育,想做一些以消费者为先的东西。所以我把钱退了,关掉了那家创业公司,又创办了另一家做习惯养成的公司——怎么帮助人们养成更好的习惯?与此同时,我结婚了。我妻子不想搬到美国,所以我搬回了印度,我以为在哪里都能创业。

[09:14] **SPEAKER_00:** And I had an engineering team in New York. I was I was working from India, but realized that the hard way, it's really hard to coordinate, you know, without at that time. So gave that up. And one of the things that sort of has stuck with me, like since the beginning has been that. And which is sort of, you know, like over time, I've sort of realized to, you know, like do more of is just trust my intuition more.

> 我在纽约有个工程团队。我在印度远程工作,但我痛苦地意识到,在那个时代协调起来真的很难。所以我放弃了。而有一件事从一开始就一直伴随着我,并且随着时间推移,我逐渐意识到要更多地去做的,就是更多地相信我的直觉。

[09:36] **SPEAKER_00:** And and so even with Danzo, like I started with this personal problem that when I moved to Bangalore, like there were too many things to be done. Like I had a car to be serviced. I had, you know, electricity to be set up, gas, all of those things. And I thought there must be an easier to do this. And I just, you know, signed a WhatsApp group and gave that number to all of my friends saying that, hey, if you need anything, just bring me on this group.

> 所以即便是 Dunzo,我也是从一个个人问题开始的:我搬到班加罗尔时,有太多事情要办。我有车要保养,要接电、接煤气,诸如此类。我想一定有更简单的方法来做这些。于是我建了一个 WhatsApp 群,把那个号码给了我所有的朋友,说,嘿,如果你们需要任何东西,就把我拉进这个群。

[09:57] **SPEAKER_00:** We'll help you get that done. So starting with a personal pain point that, hey, like we wanted to sort of, you know, make life more convenient in urban cities. And I think that has sort of stuck with me throughout, you know, that where I've been able to sort of, you know, solve a personal pain point. Like the feedback loop has been stronger. You relate with the problem more deeply.

> 我们会帮你搞定。所以是从一个个人痛点出发——我们想让城市里的生活更便捷。我觉得这一直伴随着我:在我能够解决一个个人痛点的时候,反馈闭环会更强。你会更深刻地与这个问题产生共鸣。

[10:17] **SPEAKER_00:** You relate to the customer more deeply. And even with the version, same thing happened. Like, you know, me and Maddy, both of us are like idea guys. Like we have like thousands of ideas all the time. And we wanted to sort of, you know, like automate and get more.

> 你会更深刻地与客户产生共鸣。即便是 Emergent,也是同样的情况。我和 Maddy,我们俩都是那种点子很多的人。我们随时都有成千上万的想法。我们想要把它们自动化,并做出更多。

[10:29] **SPEAKER_00:** More of these ideas out in the life. And that's why we sort of started automating programming and got started on the journey.

> 把更多这样的想法带到现实中。这就是我们开始把编程自动化、并踏上这段旅程的原因。

[10:35] **SPEAKER_01:** Dunzo was a huge deal. I mean, you scaled a massive company. Maybe you can remember some of the some of the stats about how big it got. How many? Yeah.

> Dunzo 是件了不起的大事。你把一家庞大的公司做到了很大的规模。也许你还记得一些数据,它到底做到了多大?有多少?是的。

[10:43] **SPEAKER_00:** Yeah. So Dunzo, like we had almost a million riders on the ground and we were doing 10 million monthly orders, almost like 5000 stores overall. So pretty large scale. Yeah.

> 是的。Dunzo,我们在一线大约有近一百万名骑手,每月做一千万单,总共差不多有 5000 家门店。所以规模相当大。是的。

[10:55] **SPEAKER_01:** Do you have like lessons that you took away from that experience? Either? Things you think, you know, you did right in order to scale something so large or maybe even things that you would do differently.

> 你从那段经历中有什么收获或教训吗?无论是你觉得为了把它做到这么大规模而做对的事情,还是你觉得如果重来会做得不一样的事情。

[11:06] **SPEAKER_00:** Yeah, I mean, I think Dunzo, like, even though like, you know, like it is a bittersweet ending, like for us, like the takeaway was, was like for me, was like two to three things. One was like solving the hard problem, right? We actually, as I said, there were like 87 companies doing the same thing. And we really, really cared about the consumer a lot. Like I remember, you know.

> 是的,我觉得 Dunzo,虽然对我们来说是一个苦乐参半的结局,但对我来说,收获大概有两三点。一是解决困难的问题,对吧?正如我说的,当时有大约 87 家公司在做同样的事。而我们真的非常非常在乎消费者。我记得,

[11:29] **SPEAKER_00:** Back then there was no AI. So, so all the chatting had to be manual and every evening there would be a spike in traffic and every single engineer would drop what they were working on, get back on, you know, on the chat screen, talk to our customers. And very early on, we had this, you know, like culture where we really deeply cared about the customer. Like there was a customer who wanted to ship something to a different city and we actually put a driver, one of the riders on a plane to send that packet. So we would go that extra mile for every single customer.

> 那时候还没有 AI。所以所有的对话都得靠人工,每天晚上都会有一波流量高峰,每一个工程师都会放下手头的工作,回到聊天界面,和我们的客户对话。很早的时候,我们就有一种文化,就是非常非常在乎客户。曾经有一位客户想把东西寄到另一个城市,我们真的让一名司机、一名骑手坐飞机去送那个包裹。我们愿意为每一位客户多走这一步。

[11:57] **SPEAKER_00:** And that's how sort of we created this. So we had a genuine love from all the customers. Second thing I think like one of the things that I learned from, like us not being able to sort of scale eventually was I think, like focus is really important. Like I think for us, like Darkstore was really working and working really well. But at that point we were doing like 10 other things, like we were doing a marketplace model.

> 我们就是这样建立起来的。所以我们得到了所有客户发自内心的喜爱。第二点,我从我们最终未能持续扩张这件事中学到的一个教训是:专注真的非常重要。我觉得对我们来说,暗店(dark store)模式真的很成功,做得非常好。但在那个时候,我们同时还在做另外十件事,比如做市场平台(marketplace)模式,

[12:15] **SPEAKER_00:** We were doing pickup and drop. We were doing, you know, like a bunch of those things. So I think like us, like knowing that, Hey, this is working, let's double down on this model, would have really, really helped. But eventually I think, like, I just see this as a series of, you know, like me being a builder. You know, I'm just working.

> 我们做取送服务,做了一大堆那样的事情。所以我觉得,如果我们能意识到"嘿,这个模式行得通,让我们加倍投入这个模式",真的会非常有帮助。但最终,我把这看作一个系列——我是一个创造者。我一直在做事,

[12:29] **SPEAKER_00:** just as a stepping stone to do something bigger yeah okay so you worked on done so for a bunch

> 只是把它当作去做更大事情的垫脚石。是的。好的,所以你做 Dunzo 做了好些年。

[12:34] **SPEAKER_01:** of years you scaled it to this really huge company it must have been a very intense experience running a you know like adam's based business where all kinds of things go wrong every day i'm

> 你把它做成了这么庞大的一家公司,运营一个像这样以运营为核心、每天各种事情都会出岔子的业务,一定是一段非常紧张的经历。

[12:45] **SPEAKER_00:** sure very very very hard like i mean yeah i mean we had a team called watchtower which would watch over every single order and um it was almost like a war room you're in a war room continuously because everything operational things break pretty pretty often yeah and none of that is sort of i borrowed here so the way we sort of run immersion as well is we monitor all the all the all the all the tasks that are that are getting built all the software is getting built and and if some things are breaking we flag that so a lot of the operational rigor i've been able to borrow

> 我确定非常非常非常难。是的,我们有个团队叫"瞭望塔"(Watchtower),会盯着每一个订单。它几乎就像一个作战室,你持续处在作战室里,因为一切都是运营性的,东西经常出问题。而这些经验我都借鉴到了这里。所以我们运营 Emergent 的方式也是一样:我们监控所有正在构建的任务、所有正在构建的软件,如果有东西出问题,我们就标记出来。所以很多运营上的严谨,我都从 Dunzo 借鉴到了 Emergent。

[13:16] **SPEAKER_01:** from um you know dunzo to immersion as well yes so in 2023 you've been doing this for a number of years and you left dunzo um tell us the story of like leaving dunzo and

> 是的。那么在 2023 年,你已经做了好多年,然后离开了 Dunzo。给我们讲讲你离开 Dunzo 的故事,

[13:29] **SPEAKER_00:** then what what emergence like came out of yeah i think 2023 like um at one point we thought like dunzo was too big to fail um and you know we had raised 200 million dollars in a recent round and i actually told my co-founder that hey i think now we are too big to fail uh right and and of course like this so it didn't end that way um so when i got out in september 23 i was actually pretty depressed uh like didn't want to do anything in my life um and for like first six months i was just reflecting on hey what could have we done better luckily like ai was happening at that time so you know like chat gpd was just taking off um gpd4 had just come out uh so i think it was it was a little bit easy for us to sort of building and and sort of building and coding became sort of my escape from from all the you know the noise that was there so i would actually spend like 10 12 hours just sitting on my computer tinkering with um all the things that was coming out the new voice models were coming out you know people were there were new open source models coming out at that point so i actually got this luxury of six months of like just pure tinkering on things that i really liked with no objective in mind um i built this like um an assistant on my mac where it could actually talk to me and i could sort of something very similar to open club but a very early version of that and i was just following you know like whatever was exciting to me at that point and it became very clear to me very early on that like coding as a space is going to be one that that's going to get disrupted very quickly um and i spent a bunch of time in the us with my friends with people at the labs um but i think it was just pure joy of tinkering pure joy of just building something without any pressure um that sort of led us to sort of think of this idea let us to sort of you know um build emergent uh in some way because all the insights that we got while tinkering we were able to apply while we were building the product um and and uh you know that really helped and i think just having this um sense of curiosity and sense of um you know like when you're building things just for the pure joy of it just for the um you know because because you want to solve a problem right i think i think that allows you to go really deep into the problem and bring insights that is

> 以及后来 Emergent 是怎么诞生的。我觉得 2023 年,某个时刻我们以为 Dunzo 大到不会倒(too big to fail)。我们最近一轮刚融了两亿美元,我还真跟我的联合创始人说,嘿,我觉得现在我们大到不会倒了。当然,结局并不是那样。所以 2023 年 9 月我离开的时候,其实相当抑郁,人生中什么都不想做。头六个月我一直在反思:嘿,我们本可以做得更好的地方在哪里?幸运的是,那时候 AI 正在兴起,ChatGPT 刚刚爆发,GPT-4 刚刚出来。所以我觉得对我们来说,重新构建东西相对容易了一点,而构建和编程成了我逃离一切喧嚣的出口。我会花上十到十二个小时坐在电脑前,摆弄各种新出的东西——新的语音模型出来了,那时候也有新的开源模型出来。所以我得到了六个月纯粹摆弄自己真正喜欢的东西、心里没有任何目标的奢侈时光。我在我的 Mac 上做了一个助手,它能真的跟我对话,有点类似 OpenAI 的东西,但是非常早期的版本。我就是跟着任何当下让我兴奋的东西走,很早我就非常清楚地意识到,编程这个领域将会被非常快地颠覆。我在美国花了不少时间,和我的朋友、和那些实验室里的人在一起。但我觉得正是那种纯粹的摆弄之乐、那种毫无压力地构建东西的纯粹快乐,以某种方式引导我们想到了这个点子、让我们打造了 Emergent,因为我们在摆弄过程中获得的所有洞见,都能在构建产品时应用上。这真的很有帮助。我觉得,拥有这种好奇心,当你构建东西纯粹是出于乐趣、纯粹是因为你想解决一个问题时,我觉得这能让你真正深入到问题里去,带来那些

[15:39] **SPEAKER_01:** otherwise very hard to get i i like i kind of love this picture of you you'd like you just have the super intense experience you build one of the top companies in india you're burnt out you're basically just like recuperating yeah and in your spare time because you have some time ben you're just like tinkering with the latest model you're just seeing oh maybe we could get like

> 否则很难获得的洞见。我挺喜欢这幅你的画面:你刚刚经历了一段超级紧张的经历,打造了印度顶尖的公司之一,你精疲力竭,基本上就是在休养。是的,而在你的空闲时间里,因为你有些时间,你就在摆弄最新的模型,你就在看,哦,也许我们能让

[16:02] **SPEAKER_00:** gpt to write some code i don't know yeah i mean it was practically like just you know like um me i mean just going back to like in the old times when i was a kid you know like i would just pick something new and and play with it and it just felt like the same thing that i was just playing with this new technology and and uh the pace at which uh you know models were sort of accelerating it was it was really really fascinating for us to see that and for us to build a lot of deep insight into like how elements are going to progress but for example like when we started most of the companies were building uh co-pilots that was the fashion that was that was what every vc uh wanted to hear we in fact went and pitched to like 10 12 vcs got rejected from most of them uh and this is you know dunzo founder was just at a big company coming out getting rejected from most vcs because we told them hey we're gonna automate software engineering and they thought it was crazy like that you know the ai is not there yet and but we could see we could see the model are capable like you know if you just project it out a little bit um you know that the steps that they are feeling like could be easily trained in the future so that's what we're back um so we we took this very massive view that ai progress is going to be exponential and we will always build in the direction of ai and and that sort of led us to um sort of think from a problem perspective that hey let's automate all of software engineering versus piece by piece uh thinking of that so i i think having that downtime and just that tinkering energy like really really helped uh us find the way yeah i i just want to like pull on a thread

> GPT 写点代码,我也说不好。是的,这实际上就像,回到我小时候那样,我会随手拿起一个新东西玩一玩,感觉就是同一回事,我只是在玩这项新技术。而模型加速的那种速度,对我们来说看着真的非常非常着迷,也让我们对这些"元素"(模型)将如何进步建立起很多深刻的洞见。举个例子,我们起步时,大多数公司都在做 copilot(副驾驶),那是当时的潮流,那是每个 VC 都想听到的。我们其实去找了十来家 VC 做路演,大多数都拒绝了我们。你想,一个 Dunzo 的创始人,刚从一家大公司出来,却被大多数 VC 拒绝,因为我们告诉他们,嘿,我们要把软件工程自动化,而他们觉得这太疯狂了,觉得 AI 还没到那个程度。但我们看得出来,模型是有能力的,只要你稍微往前推演一下,就会知道它们现在做不到的那些步骤在未来很容易就能被训练出来。所以我们是这么想的。我们采取了一个非常宏大的视角:AI 的进步会是指数级的,我们会始终朝着 AI 的方向去构建。这引导我们从问题的角度去思考:嘿,让我们把整个软件工程都自动化,而不是一块一块地去想。所以我觉得,拥有那段停下来的时间和那股摆弄的能量,真的非常非常帮助我们找到了方向。是的,我想顺着这条线再深挖一下,

[17:27] **SPEAKER_01:** from this because i think this is really good general advice for everyone in the room like what is doing we we have a name for this at icon meter we call it living at the edge it's like the models weren't good at writing code yeah and when you like pitch to vcs they were like the models like aren't going to be able to do this and like they weren't quite able to do it yet but you could tell that they were that like if you if you projected it out when you go to the sparks yes right and like that's just where a lot of the best startup ideas come from it's the things that aren't quite possible yet that's maybe a good segue to talk about some of the technical details of a merchant like um if you just go to a merchant maybe you don't want to go to a merchant you don't want to realize the sort of like deep tactical foundations that it's built on can you talk about that yeah so

> 因为我觉得这对在座的每个人都是非常好的通用建议。他在做的这件事,我们在 YC 有个说法,叫"活在边缘"(living at the edge)。就好比模型当时还不擅长写代码,当你向 VC 路演时,他们会说模型做不到这个,而它们那时确实还做不太到,但你能看出来,如果你往前推演,当你走到那个临界点(sparks)时——对——很多最好的创业点子恰恰就来自这里,来自那些现在还不太可能实现的事情。这也许是个很好的过渡,来聊聊 Emergent 的一些技术细节。如果你去用 Emergent,你也许不会意识到它所构建于其上的那种深层的技术根基。你能讲讲这个吗?好的,

[18:07] **SPEAKER_00:** i mean we actually uh you know like when we started our journey like most people were building co-pilots we thought we'll build autonomous agents that could do agents was not even a word then now it's obviously everywhere but like we build this multi-agent orchestrated system where you have uh different agents which will come in different point of time uh and and perform different um action like for example we have an automated testing agent which will test your app we have a design agent that'll design your app um all of this is coordinated you know through a large memory system that we have built which are sort of self-learns every time a new app gets built on emergent like you know our agents actually extract from that what are the learnable aspects and sort of store it in memory so every every new app actually getting built on the immersion makes the platform even better um and a lot of the energy has gone into us into collecting all of the data that we have now we do a lot of rl on top of that uh we do some amount of fine tuning and and but a lot of the things that we have built essentially is all of the infrastructure that we have built uh ourselves so we have built all of the coding agent we have built um all of the infrastructure for example we when we started there was nobody building um deep container technology so we had to invent a lot of the container technology ourselves like for example uh we wanted to preserve state so that you could have multiple parallel agents running on the same same snapshot so we had to invent this snapshotting memory snapshotting all of those things uh and i think one of the things that you as you said like you know living on the edge you actually discover these problems much early on before you know like other others other ecosystem discovers it and oftentimes you'll have to go solve yourself like for example today like we have um multiple different sort of parallel agents that can sort of swarm together and and completed us which we think is going to be like like the future and and what we are observing is that every time a new model comes comes out like for example a new class of model for example opus is a new class of model like you have to actually delete whatever you have learned so far and sort of reimagine the world from the lens of this new model uh so so far like you know in nine months we have already rewritten our system three times um and and just sort of started rethinking that okay what are the new possibilities that's going to open up and what where this model is going to be in six months um and um and one of the things i was telling you before that you know like that like when we started emerging like one of the biggest challenge was actually that models could not do a good json output uh and like there were like at least 20 or 30 yc companies that were solving the exact same problem json parsing right and we took this view that hey like you know like the next model will be able to solve this so let's say we just completely skipped that problem we started building the agent and and sort of you know we're going to end up the journey so i think living on the edge and just trying to imagine what is possible in the next six months is really important as you sort of progress through your startup journey um can you

> 我们其实,当我们起步的时候,大多数人都在做 copilot,而我们想做的是能自主完成任务的自主智能体(autonomous agents),那时候连 "agent" 这个词都还不存在,现在它显然到处都是。我们构建了这个多智能体编排系统,不同的智能体会在不同的时间点介入,执行不同的动作。比如我们有一个自动化测试智能体来测试你的应用,有一个设计智能体来设计你的应用。所有这些都通过我们构建的一个大型记忆系统来协调,这个系统会自我学习——每当有一个新应用在 Emergent 上被构建出来,我们的智能体就会从中提取出哪些是可学习的方面,并把它存进记忆里。所以每一个在 Emergent 上构建出来的新应用,实际上都会让平台变得更好。我们投入了大量精力去收集我们现在拥有的所有数据,在此基础上我们做大量的强化学习(RL),也做一定量的微调(fine-tuning)。但我们构建的很多东西,本质上是我们自己构建的全部基础设施。所以我们构建了整个编程智能体,构建了所有的基础设施。举个例子,我们起步时没有人在做深度容器技术,所以我们不得不自己发明很多容器技术。比如我们想保留状态,这样你就能让多个并行的智能体运行在同一个快照(snapshot)上,所以我们不得不发明这种快照、记忆快照之类的东西。我觉得正如你说的,活在边缘,你其实会比其他人、比整个生态系统更早发现这些问题,而且往往你得自己去解决。比如今天,我们有多个不同的并行智能体,可以像蜂群一样协同起来,替我们完成任务,我们认为这就是未来。我们观察到的是,每次有新模型出来——比如一个新类别的模型,像 Opus 就是一个新类别的模型——你其实得把到目前为止学到的一切都删掉,从这个新模型的视角重新想象这个世界。所以到目前为止,在九个月里,我们已经把系统重写了三次,并且开始重新思考:好,会打开哪些新的可能性?这个模型在六个月后会到什么程度?我之前跟你说过的一件事是,当我们创办 Emergent 时,最大的挑战之一其实是模型无法很好地输出 JSON,当时至少有二三十家 YC 公司在解决完全一样的问题——JSON 解析。而我们的看法是,嘿,下一代模型就能解决这个,所以我们干脆完全跳过了那个问题,直接开始构建智能体,继续我们的旅程。所以我觉得,活在边缘、努力去想象未来六个月里什么会成为可能,在你推进创业旅程的过程中真的非常重要。你能不能

[20:42] **SPEAKER_01:** talk about beating the benchmark is that's a that's like a core core part part of the founding

> 讲讲打破那个基准测试(benchmark)?那是这个创业故事非常核心的一部分。

[20:47] **SPEAKER_00:** story here yeah so um so one of the things that like happened when we went to ic was that uh and this happens with a lot of ic founders that that you know like you you come in with a different idea you sort of you know stumble upon a different idea when we actually went to yc we were building a web app industry back when we were like 10 something like 10 or 11 agents initially right and um and and and when when sort of we were coming coming from india like we do through this on a whiteboard that hey like very soon you'll be able to build build web apps mobile apps um you know through ai and we have this diagram that hey like we'll be able to build web app on by labs on on thing we day one we went to our yc partner told them that hey we want to build a consumer app building company and they said okay this this you know like maybe you should think about enterprise this seems too ambitious um and for the first like it's a three-month program so we're doing for for three months every week we would have a new idea on the board okay idea of the week is you know let's say ai zapier and and we'll spend a week sort of you know building that or tickling with that um and eventually like you know every every week we'll have a new idea we were pivoting like crazy and um and team was getting frustrated hey like you have a new idea every week what are we gonna do uh so almost just to distract them i actually picked this benchmark sweep end which is the hardest benchmark at that time and i told them hey like while i figure out what what are we gonna build let's just attack this benchmark because you know it allows us to solve harder problems and and so almost send them in that direction it took us three months to sort of crack that benchmark became world number one on that benchmark but that's really set us the foundation for emergent where we were able to build world's best coding agent uh all of the innovation that we sort of have in immersion right now whether it's it's paralyzed test time compute um all of the memory agent agent communication all those things we were able to discover when when we were on this benchmark and i think like like even today i think like um attaching yourself to a number which can sort of show you progress is really really good way to sort of you know um attack a goal or go towards uh building a company because that sort of focuses you into right direction it gives you like a really good feedback in terms of what's happening yeah

> 是的。我们去 YC 时发生的一件事——这在很多 YC 创始人身上都会发生——就是你带着一个想法进来,却又偶然撞上了另一个想法。我们真正去 YC 的时候,我们在做一个网页应用,当时大概有十来个、十一个智能体。当我们从印度过来时,我们在白板上推演:嘿,很快你就能通过 AI 构建网页应用、移动应用了。我们画了这个图。第一天我们去见我们的 YC 合伙人,告诉他们,嘿,我们想做一家消费级应用构建公司,他们说,好吧,也许你们应该考虑企业级(enterprise),这个听起来太有野心了。头几周——这是一个三个月的项目——所以头三个月,我们每周都会在白板上有一个新点子。好,本周的点子是,比方说 "AI 版 Zapier",然后我们会花一周去构建它或摆弄它。最终,每一周我们都有一个新点子,我们疯狂地转向(pivot),团队开始沮丧:嘿,你每周都有一个新点子,我们到底要做什么?所以几乎是为了转移他们的注意力,我挑了 SWE-bench 这个当时最难的基准测试,我告诉他们,嘿,在我搞清楚我们到底要做什么之前,咱们就先攻这个基准测试吧,因为它能让我们去解决更难的问题。于是几乎是把他们引到了那个方向。我们花了三个月攻破了那个基准测试,成为该基准测试的世界第一。但这真的为 Emergent 打下了基础,让我们能够构建世界上最好的编程智能体。我们现在在 Emergent 里拥有的所有创新——无论是并行的测试时计算(test time compute),还是所有的记忆、智能体间通信,所有这些东西——都是我们在攻这个基准测试时发现的。我觉得即便到今天,把自己绑定到一个能向你展示进展的数字上,是一个非常好的攻克目标、或者说朝着构建一家公司前进的方式,因为它能把你聚焦到正确的方向上,给你非常好的反馈,让你知道正在发生什么。是的。

[22:41] **SPEAKER_01:** yeah it's super super impressive what you guys did beating beating that benchmark before you even really had a startup idea like for what to do around it um a recurring theme of the talks today has been um this concept of second mover advantage um you know like zepto wasn't the first grocery delivery company and giga wasn't the first ai customer support thing immersion was also not the first ai website builder to launch when you launched immersion there were already a couple of like pretty big players and probably a whole bunch of small ones um much like i guess your story of starting dunzo when they're already 80 80 similar companies what what what gave you the confidence to launch this anyway even though you weren't the first to the market and how have you been able to carve out such a such a big space for yourself

> 是的,你们做的事真的非常非常令人印象深刻——在你们甚至还没真正有一个围绕它的创业点子之前,就打破了那个基准测试。今天这些分享反复出现的一个主题是"后发优势"(second mover advantage)这个概念。比如 Zepto 不是第一家生鲜配送公司,Giga 不是第一家 AI 客服公司,Emergent 也不是第一个上线的 AI 网站构建工具。你们上线 Emergent 时,已经有几家相当大的玩家,可能还有一大堆小的。这有点像你创办 Dunzo 的故事,当时已经有 80 家类似的公司。是什么给了你信心,即便你不是第一个进入市场的,也仍然要把它做出来?你又是如何为自己开辟出这么大一片空间的?

[23:34] **SPEAKER_00:** yeah i mean for us um when we looked at uh the problem space we realized that like most of the other platforms that were out there like they were mostly focused on front end and building demoware right and and that's what like where a lot of these were finding product market fit right but what we realized was that like users are actually going to want to real software to be shipped um and you know the problem is far from salt right like and we saw that the expectation that user have versus you know and i'm sure we have the rich with bigض and doing like big off the... that's like crazy man your order costs were a lot between the top three and zero in terms of you know selling and getting the hardware where to go is, right? the same thing is with Giga as well, right? Like the expectation that user has like, hey, my queries get solved, same expectation our users have that my software should actually work, right? When I'm prompting something. And most of the solution out there, even though they were

> 对我们来说,当我们审视这个问题空间时,我们意识到市面上其他大多数平台主要都专注于前端和做演示品(demoware),而这也是很多这类产品找到产品市场契合(product market fit)的地方。但我们意识到,用户其实是想要真正能上线的软件,而这个问题远未解决。我们看到用户的期望——我相信 Giga 也是同样的道理——用户的期望是"嘿,我的问题要被解决",我们用户的期望同样是"我提示(prompt)出来的软件应该真的能用"。而市面上大多数解决方案,尽管它们

[24:15] **SPEAKER_00:** good at getting started, they were really bad at finishing. You will not get a working software out of that. You will not have a real backend. You will not have a real databases attached. And so we came to this from a very different angle saying that, hey, if you were to automate all of software engineering, how would you approach the problem? We almost built everything

> 擅长起步,但在收尾上做得非常糟糕。你从那里得不到一个能真正运行的软件。你不会有一个真正的后端。你不会有真正接好的数据库。所以我们从一个非常不同的角度切入,说,嘿,如果你要把整个软件工程都自动化,你会怎么来处理这个问题?我们几乎是把一切都

[24:32] **SPEAKER_00:** ground up. And we could see like in practice, when we sort of ran prompts on all the platform and us, like we were massively outperforming everybody else in the market, right? So that allowed us to sort of really, really attack the market in a big way. But I think again, like we came to this from a very sort of consumer insight that consumers are actually going to want real software that is working and not just prototype and demos and nobody in the market was solving that. And there were no good solutions that actually could take you to the finish line.

> 从头构建的。我们能看到,在实践中,当我们在所有平台和我们自己身上运行同样的提示时,我们大幅领先市场上所有其他人。所以这让我们能够真正地、大规模地攻占市场。但我再次觉得,我们是从一个非常消费者洞察的角度切入的:消费者其实想要的是真正能运行的软件,而不只是原型和演示,而市场上没有人在解决这个问题。也没有好的解决方案能真正带你到达终点线。

[24:59] **SPEAKER_00:** And that's why sort of we attacked that. And once we had the product, like we had to think through GTM, how do we market it? We looked at like which companies are growing really fast, what they have done. And sort of almost converted our growth into a max problem saying that, hey, how many social views do we need? How many impression do we need? How many clicks will

> 这就是我们攻这个方向的原因。一旦有了产品,我们就得想清楚市场进入策略(GTM),我们要怎么去营销它?我们看了哪些公司增长得非常快、他们做了什么。我们几乎把增长转化成一个数学问题:嘿,我们需要多少社交媒体的观看量?需要多少曝光量?能得到多少

[25:18] **SPEAKER_00:** we get? How many users will we get? And at that point we knew, okay, like influencer is a good strategy for us to sort of really launch because we knew the product is really good, working really well. We just need to get it in front of as many users as possible. And that's sort of been the growth engine for us.

> 点击?能得到多少用户?在那个时候我们就知道,好,网红营销(influencer)对我们来说是一个很好的启动策略,因为我们知道产品真的很好、运行得非常好。我们只需要把它呈现在尽可能多的用户面前。这基本上就是我们的增长引擎。

[25:32] **SPEAKER_01:** Where is the Emergent team based? And how do you think about building an AI native company that targets a global audience here?

> Emergent 团队在哪里?你又是如何思考在这里打造一家面向全球用户的 AI 原生公司的?

[25:41] **SPEAKER_00:** Yeah, so most of the team is actually in Bangalore. We have 95% of our team in Bangalore, pretty much built out of India completely. We have a very small team in SF. We have recently opened a new office in SF. So small team is there. And by the way, we are hiring.

> 是的,大部分团队其实在班加罗尔。我们 95% 的团队在班加罗尔,几乎完全是在印度打造出来的。我们在旧金山(SF)有一个非常小的团队。我们最近在旧金山开了一个新办公室。所以那里有个小团队。顺便说一句,我们在招聘。

[25:54] **SPEAKER_00:** So if people want to, you know, apply and work at a strong AI native company, please write to me Mukund at emergent.sh. Happy to take a look at that. And I think like one of the things that I've realized, you know, like, and we generally like hire for like learning slope, people who are like really, really passionate about, you know, solving a problem, people who get excited about, you know, solving some of these problems. And what we have seen is that, I think, like, one of the things that separates us right now from this company is that everybody in the company generally enjoys solving and working with AI, right? I think there's this added, of course, the growth is great. And you know,

> 所以如果大家想申请、想在一家强大的 AI 原生公司工作,请给我写邮件,mukund@emergent.sh。我很乐意看一看。我意识到的一件事是,我们一般按"学习斜率"(learning slope)来招人,招那些对解决问题真的非常非常有热情、对解决这些问题感到兴奋的人。我们看到的是,我觉得现在把我们这家公司区别开来的一点是,公司里每个人普遍都享受用 AI 去解决问题、和 AI 一起工作。我觉得这是额外的一层——当然,增长很棒,而且你知道,

[26:25] **SPEAKER_00:** we get to solve these problems. But I think just the, you know, the complexity of the problem and so much that we generally enjoy, like day to day problem solving with AI right now. So that's

> 我们有机会解决这些问题。但我觉得就是这个问题本身的复杂度,以及我们普遍非常享受当下每天用 AI 来解决问题的过程。所以这

[26:37] **SPEAKER_01:** amazing. You've had a chance to build two very different companies. You built Dunzo. And it's sort of like first wave of great Indian startups that are building things like Zepto, a lot of like local, local stuff. And now you're building emergent, which is like the part of this, like second wave of AI, native companies, post chat GPT. I'm curious, first, what are your takeaways

> 太棒了。你有机会打造了两家非常不同的公司。你打造了 Dunzo,它有点属于第一波伟大的印度创业公司,做的是像 Zepto 那样很多本地化的东西。现在你在打造 Emergent,它属于这第二波——ChatGPT 之后的 AI 原生公司。我很好奇,首先,你从打造这两类公司中

[27:02] **SPEAKER_01:** from building those two kinds of companies? And then second, what would your advice be to folks in the audience who are thinking about where to look for startup ideas and what kind of things to build?

> 有什么收获?其次,对于台下那些正在思考去哪里寻找创业点子、该做什么样的东西的人,你会给什么建议?

[27:11] **SPEAKER_00:** Yeah, I mean, I think I mean, my realization after building the two companies is that like, building a company for for India, a local company versus building a global company is actually exactly same effort. You know, it's equally hard to build a company in India versus building global company. And so my advice to a lot of people right now is just think global from day one, because, I mean, it's kind of like a like a prevalent wisdom that actually starting a harder idea is easier, because you can inspire a lot more people to go after a harder problem. Right? And you can sort of, you know, inspire yourself to go after this. So, so I would I would recommend that like

> 是的,我觉得,我打造这两家公司之后的领悟是,为印度打造一家公司、一家本地公司,和打造一家全球公司,其实付出的努力完全一样。在印度打造一家公司,和打造一家全球公司,同样地难。所以我现在给很多人的建议就是,从第一天起就以全球为目标去思考,因为有一种普遍的智慧是:其实做一个更难的点子反而更容易,因为你能激励更多的人去追逐一个更难的问题,你也能激励你自己去追逐它。所以我会建议

[27:46] **SPEAKER_00:** think global from day one, because like now you have to reach the access internet is with everyone. Technology is a big leveling, you know, for everyone, everybody has the same access same technology. And, and you can actually just reach global customer from day zero from from India today. The other thing I would say is that one, I think just following your intuition is really, I mean, you'll get a lot of advice. But I think following as a founder, following your intuition is actually much better, because you don't like you probably have a better sense of general, you know, what your customer wants, what your customer needs.

> 从第一天起就以全球为目标思考,因为现在互联网的接入人人都有。技术是一个巨大的拉平力量,对每个人都是,每个人都拥有同样的接入、同样的技术。今天你其实可以从第零天起就从印度触达全球客户。另一点我想说的是,跟随你的直觉真的很重要。你会得到很多建议,但作为创始人,我觉得跟随你的直觉其实要好得多,因为你很可能对你的客户想要什么、需要什么有更好的整体判断。

[28:21] **SPEAKER_00:** And also, I think, just thinking big and ambitious, I think, whatever you're thinking right now, just 10x that 100x that because I think the next, you know, with AI, I think a lot of things and, and it's not a time to sort of attack the floor, it's the time to attack the ceiling and think really big. And the bigger you think that the I would say the higher probability that you'll get

> 还有,我觉得,要想得大、想得有野心。无论你现在在想什么,把它放大 10 倍、100 倍,因为我觉得接下来,有了 AI,很多事情——现在不是去攻地板的时候,而是去攻天花板、想得非常大的时候。你想得越大,我会说,你成功的概率就越高。

[28:41] **SPEAKER_01:** to success. That's an amazing piece of advice for us to end on. Mukhand, you're an inspiration to us.

> 这是一条非常棒的建议,让我们以此收尾。Mukund,你是我们的灵感来源。

[28:48] **SPEAKER_00:** Thank you so much. Thank you. Thank you so much for having me here. And the energy is electric here. And I'm looking forward to a lot more of Gigas and Immersion coming out of India over the next year or so and looking forward to these people here. Cheers.

> 非常感谢。谢谢。非常感谢邀请我来到这里。这里的能量简直像通了电一样。我期待在接下来的一年左右看到更多像 Giga 和 Emergent 这样的公司从印度走出来,也期待这里的这些人。干杯。
