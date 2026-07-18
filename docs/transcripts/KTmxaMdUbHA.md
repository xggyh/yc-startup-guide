# 全文转录 · AI 正在吞噬物流:Flexport 的自动化实战

> ▶ [YouTube](https://www.youtube.com/watch?v=KTmxaMdUbHA) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/KTmxaMdUbHA.md) &nbsp;·&nbsp; AI Is Eating Logistics

> 中英对照 · 每段英文原文下附中文翻译

[00:00] **SPEAKER_02:** Logistics are a very scale-driven industry, and so the bigger you get, the cheaper you get. Our take is that we can make the price of shipping anything by ocean container shipping between eight and ten percent cheaper over the next few years, and AI is a big part of that. So our AI for that saved us two percent of our ocean freight spend, while improving transit time 20 percent. Usually that's a trade-off. It's like either faster or cheaper, but not both.

> 物流是一个高度依赖规模的行业,所以你规模越大,成本就越低。我们的看法是,在未来几年内,我们能把任何货物的海运集装箱运输价格降低8%到10%,而AI在其中扮演着重要角色。我们为此打造的AI帮我们节省了2%的海运费用,同时把运输时效提升了20%。通常这两者是要权衡取舍的——要么更快,要么更便宜,很难兼得。

[00:25] **SPEAKER_00:** And you're at two billion dollars of your revenue and just getting started. Welcome back to another episode of The Light Cone. We've got a real treat today. We have Ryan Peterson of Flexport with us. He went through YC in 2014, and he is easily one of the most awesome founders I've ever met. Ryan, thanks a lot for joining.

> 而你们的营收已经达到20亿美元,却才刚刚起步。欢迎回到《The Light Cone》的又一期节目。今天我们有一位重量级嘉宾——Flexport的Ryan Peterson。他在2014年参加了YC,毫无疑问是我见过最出色的创始人之一。Ryan,非常感谢你来参加。

[00:51] **SPEAKER_00:** Thank you. To start, Ryan, what is Flexport, and what are some of the things in AI you're actually implementing right now?

> 谢谢。首先,Ryan,能不能介绍一下Flexport是做什么的,以及你们现在实际在AI方面落地了哪些东西?

[00:58] **SPEAKER_02:** So Flexport is a global logistics company built around a modern tech stack, and that means we help companies ship cargo from point A to point B across any mode of transport, so air, ocean, truck, and rail, and get that cargo delivered, hopefully on time and in full at a lower cost, thanks to the tech. What we're doing with AI is, I had to make an exhaustive, we have to extend the length of the podcast to pull that off, but starts with customer user experience. What can we do with their data, getting them better access? How do we load containers in the optimal way? How do we put that container onto the right ship at the lowest cost while maintaining or beating transit time expectations, automating just tons of work that's done in email, or phone, or work that you wouldn't even do because the cost is too high for a human, but actually does create some value that's worth it with AI.

> Flexport是一家围绕现代技术栈打造的全球物流公司,意思是我们帮企业把货物从A点运到B点,涵盖任何运输方式——空运、海运、卡车、铁路,并借助技术把货物尽可能准时、完整、低成本地送达。至于我们用AI做的事情,要详尽讲的话得把播客时长延长才行,但它从客户的使用体验开始。我们能用他们的数据做什么,让他们更好地获取信息?我们如何以最优方式装载集装箱?如何以最低成本把集装箱装上正确的船,同时保持甚至超越运输时效的预期?我们把大量在邮件、电话里完成的工作自动化,还有一些原本因为人工成本太高而根本不会去做、但用AI去做其实能创造值得的价值的工作。

[01:50] **SPEAKER_02:** So most contracts in logistics come in giant Excel files, thousands of rows and a dozen tabs. You can't just feed that to open AI and get a structured JSON file back. It needs intelligence, but writing code and then having AI write the code, you write a parser that ingests it and then have AI that can write those parsers for you learning. It's an endless list and we feel like we don't even know all the

> 物流行业的大多数合同都是巨大的Excel文件,几千行、十几个标签页。你没法直接把它扔给OpenAI就拿回一个结构化的JSON文件。它需要智能,但你可以写代码,再让AI来写代码——你写一个解析器来读取它,然后让AI帮你学着写这些解析器。这是一个无穷无尽的清单,我们感觉自己甚至还不知道它能做的所有

[02:14] **SPEAKER_00:** things that it can do. It's still pretty new. So basically one of the most human intensive things now can be streamlined to the point where actually it might affect GDP in the world.

> 事情。它还很新。所以基本上,曾经最依赖人力的工作之一,现在可以被精简到甚至可能影响全球GDP的程度。

[02:25] **SPEAKER_02:** Our take is that we can make the price of shipping anything by ocean container shipping cheaper by between eight and 10% cheaper over the next few years. And AI is a big, not the only part of that, but a big part of that. As our business model, the way we think about it is as I call it scale economies shared, which is the bigger you get, the cheaper you get. Automation is a form of scale. And the bigger you get or the cheaper you get, the lower your costs, you give that, share that with your customer, which will make them do even more volume with you. There are scale benefits that come, logistics are very scale

> 我们的看法是,未来几年内我们能把任何货物海运集装箱运输的价格降低8%到10%。AI在其中占很大比重——不是唯一的因素,但是很重要的一部分。至于我们的商业模式,我把它称作"共享的规模经济":你规模越大,成本就越低。自动化就是一种规模。你规模越大、成本越低,你就把这部分节省分享给客户,而这会让他们跟你做更大的量。规模带来的好处会不断累积,物流是一个非常依赖规模的

[02:58] **SPEAKER_02:** driven industry. And so the bigger you get, the cheaper you get. Like the Costco model, I love Costco, even though I don't shop there, I just love the business. You keep driving down the price that makes you more attractive, more competitive and just keep going. Yeah.

> 行业。所以你规模越大,成本就越低。就像Costco的模式——我很喜欢Costco,虽然我不在那儿购物,但我就是喜欢这门生意。你不断压低价格,这让你更有吸引力、更有竞争力,然后就这样一直滚下去。对。

[03:12] **SPEAKER_00:** And you're at $2 billion a year revenue and just getting started.

> 而你们年营收已经20亿美元,却才刚刚起步。

[03:15] **SPEAKER_04:** Just getting started. Yes. Something I'm curious about. So from our perspective, we work with all the startups and we've seen AI over the last couple of years go from when ChatGPT launched and then some startups in the back start playing around with it and it's become progressively more serious. I think you're the first person we've had on the show who's running a company at scale that was founded pre AI. What have the last few years been like for you from that perspective, from like ChatGPT

> 刚刚起步。是的。有件事我很好奇。从我们的角度,我们和所有创业公司打交道,这几年我们看着AI一路走来——从ChatGPT发布,然后一些创业者开始拿它捣鼓,再到它变得越来越正经。我觉得你是我们节目里第一位在AI出现之前就创立、如今经营着一家有规模的公司的嘉宾。从这个角度看,过去几年对你来说是什么样的?从ChatGPT

[03:39] **SPEAKER_04:** launch? Like at what point did it start becoming like a thing you were paying more attention to?

> 发布算起?大概在哪个时间点,它开始变成一件你更加关注的事情?

[03:44] **SPEAKER_02:** Like so many other people is on November of 20, was it 2022? It's already been a few years since the ChatGPT launch, been personally obsessed ever since then. It's interesting to watch it take hold at the company and in some cases not take hold and you then saying like, come on guys, we can't be this boomer company. Like everybody needs to be using this. We're trying to drive that sense of paranoia from the top, from me, but many others in the company, maybe even more paranoid than me or more enthusiastic, excited than me as well to say that story that we say of like, well, we're the only large logistics company founded since the web browser. And I know there's a kid in the next YC batch who say, hey, we're the

> 和很多人一样,是在2020年11月……是2022年吧?ChatGPT发布已经好几年了,从那以后我个人就一直着迷于它。看着它在公司里扎根很有意思,有些情况下又扎不下根,于是你就会说,拜托各位,我们不能变成这种老古董公司。每个人都得用起来。我们试图从高层、从我这里推动这种"偏执"的紧迫感,但公司里还有很多其他人,可能比我更偏执、比我更热情兴奋。我们常说的那句话是:我们是自网页浏览器诞生以来唯一成立的大型物流公司。而我知道下一批YC里会有个年轻人说,嘿,我们才是

[04:24] **SPEAKER_02:** only break border founded since ChatGPT November 2022. Like it has got a point. So we have to be leading on this. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

> 自2022年11月ChatGPT问世以来唯一成立的公司。这话是有道理的。所以我们必须在这方面走在前面。对,对,对。

[04:34] **SPEAKER_02:** Yeah. This is true of all incumbents in an industry. They have some real advantages when it comes to AI and benefiting from it. And one is the scale of the data. Two is the domain experience to know, okay, which problems should we be solving? And some of those problems are

> 对。这一点对行业里所有的在位者都成立。在AI以及从中获益方面,他们有一些实实在在的优势。第一是数据的规模。第二是领域经验,知道好,我们该解决哪些问题?而其中有些问题

[04:49] **SPEAKER_02:** small enough that you shouldn't start a whole company around the problem. It's maybe a feature, not a company. But for them, it's great. It's a valuable feature that they could add. And third is distribution. Like when we build or any large company builds a great AI product,

> 小到你不该围绕它去创办一整家公司。它也许是一个功能,而不是一家公司。但对在位者来说这很棒,是他们可以增加的一个有价值的功能。第三是渠道分发。比如当我们、或任何一家大公司做出一个很棒的AI产品时,

[05:04] **SPEAKER_02:** the next day it can be used by thousands of companies. Whereas a startup doing that has to go beg people for their data to train the model and earn their trust to have that data from a security compliance standpoint. And then third, get the customer. So that's the huge advantage that any incumbent will have. And we definitely feel that we have that advantage at our scale.

> 第二天就能被成千上万家公司使用。而一家创业公司要做同样的事,得去求别人给数据来训练模型,还得从安全合规的角度赢得他们的信任才能拿到这些数据,然后第三步才是获得客户。所以这是任何在位者都会拥有的巨大优势。以我们的规模,我们绝对能感受到自己拥有这种优势。

[05:25] **SPEAKER_02:** But the flip side where I think we also have an advantage is that we are still a young company relative to our industry, but young in terms of our tech stack. Like we've built a lot of tech. We build our own tech. Therefore we can implement and integrate AI and just add it wherever we want. Most of our competitors treat technology period as IT, as a service that they pay for. Many cases like desktop app or like Windows remote desktop is very common in our

> 但从另一面看,我认为我们还有一个优势:相对于我们所在的行业,我们仍是一家年轻的公司——就技术栈而言很年轻。我们自己造了很多技术,我们自建技术,因此我们可以在任何想要的地方去实施和集成AI。我们大多数竞争对手把技术完全当成IT,当成一种花钱买来的服务。很多情况下他们用桌面应用,比如Windows远程桌面在我们这个行业里很常见,

[05:50] **SPEAKER_02:** industry. But still it's something they buy and therefore you don't control the code base. If you wanted to add AI to automate something or do something that you're like, it's not really,

> 但那毕竟是他们买来的东西,因此你无法控制代码库。如果你想加入AI来自动化某个环节或做点什么,那其实并不真的可行,

[05:59] **SPEAKER_04:** it's hard. Has there been a specific moment since ChatGPT launched where you started as a company, like taking it more seriously? Because my impression, like the first version was a toy, even within the YC batches, like we sort of see some founders playing around with things, but it wasn't clear that they'd actually be like companies founded on it. So I'm just curious what's like founder running large scale company. You start out, you're like, this is really interesting to me personally. Like, was there some moment where you're like, oh, like we should probably

> 很难。自ChatGPT发布以来,有没有某个具体的时刻,你们作为一家公司开始更认真地对待它?因为在我的印象里,第一个版本像个玩具,即便在YC的各批次里,我们也只是看到一些创始人拿它玩玩,但当时并不清楚真的会有以它为基础创立的公司。所以我很好奇,作为经营大型公司的创始人是什么感受。一开始你觉得,这对我个人来说真有意思。有没有某个时刻你想,哦,我们大概应该

[06:24] **SPEAKER_04:** try and like build something or do something internally with this?

> 试着用它在内部做点什么、建点什么东西?

[06:27] **SPEAKER_02:** Yeah. I think a lot of it has come through in our hackathons, but there could be an interesting metric here is like what percentage of hackathon projects, first of all, used AI, like we're building something with large language models, and which percent of the projects actually you decided to fund and push into like, oh, let's actually make this thing

> 对。我觉得很多是通过我们的黑客松体现出来的,这里有个有意思的指标:首先,有多大比例的黑客松项目用到了AI,也就是用大语言模型来做东西;以及有多大比例的项目你真的决定去投入资金、推进到"我们真的要把这个东西做

[06:43] **SPEAKER_04:** real. It's not just a hack. Is hackathon something you've done for a while? Is that like-

> 出来"的地步。它不只是个临时的小玩意。黑客松是你们做了一段时间的事吗?那算是——

[06:46] **SPEAKER_02:** Yeah. We usually do two a year. Okay. I think now we're like kind of religious about two every year, but one to two a year where, and for us, it's very much a free for all. You can build anything you want.

> 是的。我们通常一年办两次。现在我们几乎是雷打不动地每年办两次,一年一到两次,而对我们来说它非常自由随意。你想做什么都可以。

[06:57] **SPEAKER_02:** If you look now at the last two hackathons we've done, it'd been like 90% LLM based projects. I haven't studied it, but it was just like my feeling in my gut. Whereas probably 18 months ago, there were like four or five. There's probably 50, 60 teams that do a hackathon project each time. In the beginning of Flexport, I was very much of this idea that like, you just get smart people and get out of their way and go execute.

> 如果你看我们最近办的两次黑客松,大概有90%都是基于大语言模型的项目。我没做过统计,只是凭直觉的感受。而大概18个月前,可能只有四五个。每次大概有五六十个团队做黑客松项目。在Flexport创业初期,我非常笃信这样一种理念:你只需招来聪明人,然后别挡他们的路,让他们去执行就行。

[07:24] **SPEAKER_02:** Oh, that sounds like manager mode. Yeah. I had way too much manager mode. I had this idea of like human beings are going to flourish. If only they could be set free. They don't want to be

> 哦,那听起来像是"管理者模式"。对。我当时"管理者模式"太重了。我抱有这样一种想法:只要人被解放,他们就会蓬勃发展。他们不想被

[07:34] **SPEAKER_02:** told what to do by the man. That's why I started a company. I don't want to be told what to do. And I went through my own Chesky moment of founder mode and recognizing, oh, you gotta be way more tops down and directive and tell people what to do and get people aligned and rowing in the right direction. And that's been my evolution the last two years at Flexport. I've

> 被上头指挥着干这干那。这正是我创业的原因——我不想被人指挥。后来我经历了自己的"Chesky时刻",体会到了创始人模式,意识到,哦,你得更加自上而下、更有指令性,告诉大家该做什么,把大家对齐、朝同一个正确方向划船。这就是过去两年我在Flexport的转变。我

[07:50] **SPEAKER_02:** been pretty way more hands-on and hardcore and directing the business. But then as I see these hackathons, I'm like, I never would have come up with that idea in a million years. And I got to let these guys build what they want to build and flourish. And so I'm starting, and I'm going to now come back on myself and say, where's the room in our product roadmap for bottoms-up innovation? Certainly you see it in these hackathons and trying to maybe even start making sure I do the hackathon timing before we do our roadmap exercise every six months or so.

> 变得更亲力亲为、更硬核、更直接地指挥业务。但当我看到这些黑客松时,我心想,这种点子我一万年也想不出来。我得让这些人去做他们想做的东西,让他们尽情发挥。所以我开始反思自己,现在要往回调一调,问:我们的产品路线图里,自下而上的创新有没有空间?你在这些黑客松里显然能看到这种创新,我甚至想开始确保把黑客松安排在每六个月一次的路线图规划之前。

[08:21] **SPEAKER_02:** We should probably do the hackathon right before that so that when you see a great idea, you can budget it instead of after the budget. I mean, there's a noteworthy change here

> 我们大概应该把黑客松安排在那之前,这样当你看到一个好点子时,就能为它编入预算,而不是在预算定完之后。我是说,这里有一个值得注意的变化

[08:28] **SPEAKER_00:** that's happening for you. I mean, I think most companies might throw a hackathon, and then in most hackathons, 90% of the projects are just toys and you never return to them again. Someone gets a nice participation trophy and that's it. But it sounds like the difference right now in the age of LLMs and age of intelligence is that these hackathon things are actually turning into real product lines and features for you.

> 正在你们身上发生。我是说,我觉得大多数公司也许会办黑客松,而在大多数黑客松里,90%的项目只是玩具,你再也不会回头去碰它们。有人拿个漂亮的参与奖,仅此而已。但听起来,如今在大语言模型和智能的时代里,不同之处在于这些黑客松产物真的变成了你们实实在在的产品线和功能。

[08:54] **SPEAKER_02:** Yes. And at the very least into debates in my head of being like, man, I've got to do that. But we're going to crush everybody with just our regular roadmap. Yeah, absolutely. Yeah.

> 是的。而且至少会在我脑子里引发争论,让我觉得,天呐,我一定得做那个。不过光靠我们常规的路线图,我们就会把所有人碾压掉。对,绝对是。对。

[09:04] **SPEAKER_02:** Yeah, absolutely. Absolutely. I had this after the very last, I think our next hackathon's in two weeks, so the last four or six months ago. I remember thinking afterwards, I'm like, you know what, we could just only do that stuff and we'll also win.

> 对,绝对是,绝对是。上一次黑客松之后我就有这种感觉——我想我们下一次黑客松在两周后,所以上一次是在四到六个月前。我记得之后我在想,你知道吗,我们哪怕只做那些东西,也照样能赢。

[09:13] **SPEAKER_00:** Yeah. Maybe win faster? Maybe.

> 对。也许还能赢得更快?也许吧。

[09:16] **SPEAKER_02:** It's highly unlikely that the person at the top now knows best what the best implications are, applications are, that it's just as likely that someone on the front lines closer to the problem is going to go, hey, look, watch, it can do this. You go, oh man, I wouldn't have guessed it could do that.

> 如今坐在最高位的人最清楚最佳的影响、最佳的应用是什么,这种可能性极低;同样有可能的是,某个在一线、更接近问题的人会说,嘿,你看,看好了,它能做到这个。而你会说,哦天呐,我根本猜不到它能做那个。

[09:30] **SPEAKER_04:** You kind of need engineers who are just really into it and have been playing around with it and just understand how to build the products in the first place to come up with the ideas.

> 你多少需要那种真正痴迷于它、一直在拿它捣鼓、本来就懂怎么造产品的工程师,才能想出这些点子。

[09:37] **SPEAKER_02:** Yeah, engineers and engineers being really close to the business is something we've always prided ourselves on, like really being in the weeds. And one of the other things that we've done is create a program for non-engineers to learn AI skills and a kind of formalized program. So your manager has to agree, but you get one day a week for 90 days. It's a 90-day program. One day a week where we teach you kind of a...

> 对,工程师,而且工程师非常贴近业务,这一直是我们引以为傲的地方,就是真正深入到细节里。我们做的另一件事,是为非工程师创建了一个学习AI技能的项目,一个比较正式的项目。你的经理得同意,然后在90天里,你每周有一天。这是一个90天的项目,每周一天,我们会教你一种……

[10:02] **SPEAKER_02:** AI bootcamp, vibe coding, and different ways to apply. And it's a new program, so we're only about six months into this. You'll see how it works out. But people love it, and you are seeing gains. But the promise of the leader who created this and convinced the managers to give up someone for 20% of their time to go into it was, I will return them to you as 10 times more productive than their peers.

> AI集训营、氛围编程(vibe coding),以及各种应用方式。这是个新项目,所以我们才推进大约六个月。以后能看到效果如何。但大家都很喜欢,而且确实看到了收益。创建这个项目、并说服经理们放出员工20%时间去参加的那位负责人,当初的承诺是:我会把他们还给你,而且比他们的同事生产力高出十倍。

[10:24] **SPEAKER_02:** I'm sure we haven't have achieved that or it would show up in the metrics, but that's the idea.

> 我敢肯定我们还没做到那一步,不然就会在指标上体现出来了,但那就是目标所在。

[10:28] **SPEAKER_01:** How are you training all these folks to up-level skill in AI? What are the sorts of things they're learning?

> 你们是怎么培训这么多人来提升AI技能的?他们学的都是些什么东西?

[10:34] **SPEAKER_02:** Certainly, it's Cursor and a set of related products like that. I think we're using something called Streamlit, but probably there's YC Company. I don't know. Maybe we should use Replit or something, but it's similar ideas. You can spin up, build your own little apps, build workflow automation tools to say, okay, because a lot of what Flexport is, we call it freight forwarding.

> 当然,用的是Cursor以及一系列类似的相关产品。我想我们在用一个叫Streamlit的东西,不过大概也有YC公司的产品。我不知道,也许我们该用Replit之类的,但思路类似。你可以快速搭建、做你自己的小应用,做工作流自动化工具,来说,好,因为Flexport大部分业务,我们称之为货运代理。

[10:56] **SPEAKER_02:** I've often joked it should be called freight email forwarding. You're like taking docs and sending it on. So how do you look at a person's... job and there's no one better to look at it than the person doing the job and saying, oh man, I'm doing the same thing over and over again. What if I instead...

> 我常开玩笑说它应该叫"货运邮件转发"。你就是拿着文件再转发出去。所以你怎么去审视一个人的……工作呢?没有谁比正在做这份工作的人更适合来审视它,他会说,天呐,我一遍又一遍地在做同一件事。如果我换个方式……

[11:11] **SPEAKER_02:** it's like if everybody was an engineer, they would... and I've thought about this in the past is saying, hey, what if I took one group of engineers and hire them as engineers as a big bait and switch, and then tell them, actually, you're just moving freight, sorry, and watch them automate their way out of the job. Right. And you sort of say, okay, I never really wanted to do that to an engineer because I feel like I'd just have a revolt of them. Yeah, yeah, yeah, yeah.

> 就好像如果每个人都是工程师,他们就会……我过去还想过这个,就是说,嘿,要是我招一批工程师,以工程师的名义把他们招进来玩一出"挂羊头卖狗肉",然后告诉他们,其实你们就是在搬运货物,抱歉了,然后看着他们把自己的工作自动化掉。对吧。然后你会想,好吧,我从来没真想对工程师这么干,因为我觉得那样只会招来他们的集体反抗。对对对对。

[11:32] **SPEAKER_02:** But... now you're kind of like, well, I could do it to a non-engineer who's already doing that job and turn them into a, you know, a lightweight, low-code engineer. Which is cool.

> 但是……现在你会觉得,我可以对一个本来就在做那份工作的非工程师这么做,把他们变成一个,你懂的,轻量级的、低代码的工程师。这挺酷的。

[11:40] **SPEAKER_01:** Yeah. It's going the other direction where you're taking really all these super domain experts and now they can finally build and they can automate themselves out of it instead of getting the engineer to do it.

> 对。这是反着来的方向:你把所有这些超级领域专家拿过来,现在他们终于能自己动手造东西,能把自己的工作自动化掉,而不用去找工程师来做。

[11:49] **SPEAKER_02:** Yeah. And that program started on our Amsterdam. We have an engineering office in Amsterdam. It started there. I think they did it without me knowing about it for the first six, few months.

> 对。这个项目是从我们阿姆斯特丹那边开始的。我们在阿姆斯特丹有一个工程办公室,项目就是在那里起步的。我想头几个月他们是背着我在搞,我都不知道。

[11:58] **SPEAKER_02:** And then now we're like, oh, this is great. Everybody loves it. So we're starting to bring it global to other offices.

> 然后现在我们觉得,哦,这太棒了,大家都很喜欢。所以我们开始把它推广到全球其他办公室去。

[12:02] **SPEAKER_03:** I wonder if you could share some examples of the AI projects that you have rolled out that have been most impactful over the last couple of years, both customer facing features, but also like any internal operational things that you guys have automated that maybe the customers have no idea about.

> 我想请你分享一些例子,关于过去这几年你们上线的、影响最大的AI项目,既包括面向客户的功能,也包括你们在内部运营中自动化掉的、客户可能压根不知道的那些事情。

[12:17] **SPEAKER_02:** Yeah. The customer facing one, probably the most impactful, like a lot of what you care about from your logistics company is your data. What's going on with my supply chain, the types of data that people are looking at. So the way Flexport works, you place orders to your factories through Flexport. So I'm replenishing my inventory, I'm buying things, I'm placing purchase orders.

> 好。面向客户的这个,可能是影响最大的:你对物流公司在意的很多东西,其实就是你的数据。我的供应链在发生什么,人们查看的那类数据。Flexport的运作方式是,你通过Flexport向你的工厂下订单。所以我在补充库存,我在采购,我在下采购订单。

[12:36] **SPEAKER_02:** So those flow out to the factory. Factory becomes a user. There's a nice network effect there. Once the cargo is ready, they place a booking. And then we execute that, a booking to move the freight, come pick it up on this date and we'll execute it by air, ocean, truck, rail, whatever, and move it across the world for you.

> 于是这些订单流向工厂,工厂就成了用户。这里有一个很好的网络效应。货物一旦准备好,他们就下一个订舱。然后我们来执行这个订舱,去运输货物——在某个日期来提货,我们会通过空运、海运、卡车、铁路等等来执行,替你把货运往世界各地。

[12:55] **SPEAKER_02:** So that's kind of the loop that we're trying to run. So you care a lot about the data for on-time performance, SKU level performance, cost, you care a lot about that. There's customs attributes here that are super important with tariffs and everything's happening. So being able to get that data is one of the core areas that Flexport shines already, historically. With AI, and this did start as a hackathon project, we just built like natural language ability so that you don't need to know SQL, you don't need to build dashboards, you just type your question and it generates those graphs, charts, tables, don't think it does maps yet, but it should.

> 这大致就是我们想要跑起来的闭环。所以你会很在意准时率、SKU级别表现、成本这些数据,你非常在意。这里还有海关方面的属性,在关税以及各种事情都在发生的当下极其重要。所以能够拿到这些数据,是Flexport历来就出彩的核心领域之一。在AI方面——这确实起初是个黑客松项目——我们打造了自然语言的能力,让你不需要懂SQL,不需要搭建仪表盘,你只要输入你的问题,它就生成那些图表、图形、表格,我想它还不会做地图,但它应该能做到。

[13:29] **SPEAKER_02:** And it works. And that has done wonderful. Wonderful. Customers love it. But two is it's about 25% of our account management time is spent helping people generate reports.

> 而且它有效。这做得非常棒,非常棒,客户很喜欢。第二点是,我们大约25%的客户管理时间都花在帮人生成报表上。

[13:41] **SPEAKER_02:** That's another huge metric for us. If we're cheaper, more people will choose us. It's not that we just started using AI with LLMs. We've had a machine learning model for doing planning for, and planning in the sense of logistics means, let's say on a containerized basis, I've got a container, which ship should it go on? You've gotta look at all the contracts with their price.

> 那对我们是另一个很大的指标。如果我们更便宜,就会有更多人选择我们。并不是说我们直到用了大语言模型才开始用AI。我们早就有一个机器学习模型来做规划,而物流意义上的"规划",比如说以集装箱为单位:我有一个集装箱,它该装上哪条船?你得看所有合同以及它们的价格。

[14:04] **SPEAKER_02:** You need the sailing schedules, how long is it gonna take? Which route variability, all around those, both those things. Our AI for that saved us 2% of our ocean freight spend while improving transit time, 20%. Usually that's a trade off. It's either faster or cheaper, but not both.

> 你需要航行班期,要花多长时间?哪条航线,航线的波动性,围绕这些,两方面都要考虑。我们为此打造的AI帮我们省下了2%的海运支出,同时把运输时效提升了20%。通常这两者是要取舍的——要么更快,要么更便宜,不能兼得。

[14:25] **SPEAKER_02:** Huge win there. Customers don't, they care a lot about those metrics. They don't care how we did it.

> 那是一个巨大的胜利。客户不会去管我们怎么做到的,他们非常在意那些指标,但不在乎我们是怎么实现的。

[14:29] **SPEAKER_03:** And for that one, was the unlock parsing a bunch of computers? Yeah. Yeah. unstructured like emails and data that you get from the shipping companies that have this but it's all like in like a big paragraph where like you couldn't just like run a simple query on it

> 那个项目的突破点,是不是解析一堆……对,对,那些非结构化的东西,比如你从船公司拿到的邮件和数据,他们有这些信息,但都是一大段文字,你没法直接对它跑一个简单的查询

[14:40] **SPEAKER_02:** before sort of yeah the way to think about it is um you've got if you just put a container on the cheapest contract you you made uh it's an optimization okay which one's the cheapest but also the fastest you know i'm trading off so that that's one thing that machines are better at uh and then it's the scale of that so on a given week we have about 2 000 containers that get canceled by our customers they place the booking and then they say oh actually the cargo is not ready the factory is late it's just inevitable it's going to happen what software does that humans could never do is go through 10 times a day and taking each one of those containers and say okay i lost this container it's been canceled is there another container that was meant to depart one week from now and i'll grab that and move it forward that's how you get the 20 transit time increase and then the optimization piece of fine is just find the cheapest contract like a solver out you know algorithm to go find the humans can't do that because it has to happen

> 之前是没法的,对。可以这样理解:如果你只是把一个集装箱放到最便宜的合同上,那你做的就是一个优化——好,哪个最便宜,但同时又最快,你懂的,我在做权衡。这是机器更擅长的一件事。然后是它的规模。比如在某一周里,我们大约有2000个集装箱被客户取消——他们下了订舱,然后说,哦其实货还没准备好,工厂延误了,这是不可避免的,总会发生。软件能做而人永远做不到的事,是一天检查十次,拿起这些集装箱里的每一个说,好,我丢了这个集装箱,它被取消了,有没有另一个本来打算一周后才出发的集装箱?我就把它抓过来提前发运。这就是你获得20%运输时效提升的方式。而优化那部分嘛,就是找到最便宜的合同,像用一个求解器、一个算法去找。人做不到这个,因为它必须发生得

[15:28] **SPEAKER_04:** really quickly

> 非常快

[15:29] **SPEAKER_02:** is this happening 10 times a day for every container in the system okay you know it's

> 这是对系统里每一个集装箱一天进行十次,好,你知道这

[15:32] **SPEAKER_04:** just like you wouldn't you maybe you could but you wouldn't you have to like an all-inclusive

> 就是说你不会去做——也许你能做,但你不会,你得算一个全包的

[15:35] **SPEAKER_01:** cost would be crazy if you calculate this first principle sounded like that first version was using classical optimization problems and you had certain data about all these shipments inputs outputs unscheduled what do you think is the delta that you could get with ai now that you could harness all the unstructured data what kind of efficiencies could you get you may be able to

> 成本,如果你从第一性原理去算,那会大得离谱。听起来第一个版本用的是经典的优化问题,你手上有关于所有这些货运的某些数据——输入、输出、未排期的。你觉得现在用AI能获得的增量是多少?既然你能驾驭所有这些非结构化数据,你能获得什么样的效率提升?你也许能

[15:54] **SPEAKER_02:** get a lot more now that you're starting to see tool use because the tool itself is incredibly powerful and i don't think an llm will outperform that but the llm can use that tool and it can do other things outside of that so you can we'll see we haven't started to do that yet so we're actually

> 获得多得多,尤其是现在你开始看到工具调用(tool use),因为那个工具本身就极其强大,我不认为大语言模型会比它表现更好,但大语言模型可以使用那个工具,并且能做那之外的其他事情。所以你可以——我们走着瞧,我们还没开始做这个,所以其实我们

[16:09] **SPEAKER_04:** still using that i can actually email people or call them up and yeah but it could its you assign

> 还在用那个。我其实可以给人发邮件或打电话,对,但它可以——你把

[16:13] **SPEAKER_02:** the llm the same solver problem but it is going to default to use this tool and then it'll also say yes maybe this container i'm not sure if i could move it forward i should ask the customer would be a good idea actually email that hey is it okay if i bring you this container early like the solver's

> 同样的求解问题交给大语言模型,但它会默认去使用这个工具,然后它还会说,是的,也许这个集装箱,我不确定能不能提前发运,我应该问问客户,发封邮件其实是个好主意——嘿,如果我把这个集装箱提前给你,可以吗?就像求解器

[16:28] **SPEAKER_00:** but then basically the agent is the user.

> 但那样一来,基本上智能体(agent)就成了用户。

[16:32] **SPEAKER_02:** MARK MANDELMAN- Yes, instead of right now there's not really a user, there's someone who's approving the plan. And so you could make that person upstream of the solver, choose the solver as one of many tools. So that'd be interesting. We haven't done that yet. And then the other thing is just routine work.

> 是的,而现在其实并没有一个用户,只有一个批准方案的人。所以你可以把那个人放到求解器的上游,让他把求解器作为众多工具之一来选用。那会很有意思。我们还没这么做。另外一件事就是常规工作。

[16:48] **SPEAKER_02:** For example, you've got a lot of email communication with your customer base. So how do you take this? You say, hey, I want to place a booking for a container. Translate that into a booking. LLMs are quite good at that.

> 比如说,你和你的客户群之间有大量的邮件往来。那你怎么处理呢?你说,嘿,我想为一个集装箱下个订舱。把那句话转化成一个订舱单。大语言模型在这方面相当擅长。

[17:03] **SPEAKER_02:** A big use case today is verifying warehouse addresses and other information and getting appointments. I've got to deliver to a warehouse. Quite costly to call the warehouse and be like, do I have the right address? You're not going to do it every time. And then you have a lot of misses where your address data was bad, and your truck got lost, pain in the ass.

> 如今一个很大的应用场景是核实仓库地址和其他信息,以及预约送货时间。我要往一个仓库送货。打电话给仓库问"我这个地址对不对?"是相当费成本的,你不会每次都去做。于是就会出很多岔子——你的地址数据是错的,你的卡车迷了路,烦死人。

[17:22] **SPEAKER_02:** So LLMs, now before we deliver, if we haven't delivered to the site in the last three months, there's an LLM agent. It does email and voice.

> 所以有了大语言模型,现在在我们送货之前,如果我们过去三个月没往那个地点送过货,就会有一个大语言模型智能体介入。它会发邮件、打语音电话。

[17:31] **SPEAKER_03:** MARK MANDELMAN- Interesting. Wow. So if necessary, it'll actually call the warehouse and be like, hey, can you confirm that 2 PM tomorrow is an OK time to deliver this? LLAMAS GORDIUS- Yes. Yes.

> 有意思。哇。所以如果有必要,它真的会打电话给仓库说,嘿,你能确认明天下午2点方便送这批货吗?是的,是的。

[17:40] **SPEAKER_03:** MARK MANDELMAN- Wow. Very cool.

> 哇,太酷了。

[17:41] **SPEAKER_01:** LLAMAS GORDIUS- Which is great, because you're turning this previous communication protocol, which is very much, I suppose, very lossy, to work sort of like the internet, like TCP, fully acknowledge, and you can get guarantees.

> 这很棒,因为你把之前那种通信协议——我想是非常有损耗的——变得有点像互联网,像TCP那样,完全确认,你能得到可靠性保证。

[17:54] **SPEAKER_02:** MARK MANDELMAN- Sometimes it's not replacing work, although I'm very happy to do so. But like, in some cases, the work would have been too expensive, so you just didn't do the work. LLAMAS GORDIUS- To do this phone call. MARK MANDELMAN- And even if a human could do it, it's just not worth it. Another good one is just messages.

> 有时它并不是在取代工作,尽管我很乐意去取代。但在某些情况下,那项工作原本成本太高,所以你干脆就不做了。——去打这通电话。——即便一个人能做,也根本不值当。另一个好例子就是消息。

[18:07] **SPEAKER_02:** So the way we communicate with our customers, some of it's email, but a lot, we try to drive as much as possible through our messaging applications inside the Flexport platform. There's this huge amount of signal in that customer sentiment. If a customer, in AI, we've trained the model to detect unhappy customers in the way that they message us. And then that creates an automatic escalation to the manager of the front line person saying, hey, this person seems upset. There's a lot of emotion in logistics.

> 我们和客户沟通的方式,一部分是邮件,但很大一部分我们尽量通过Flexport平台内部的消息应用来推进。客户情绪里蕴含着大量的信号。在AI方面,我们训练了模型,从客户给我们发消息的方式中识别出不满意的客户。然后这会自动升级上报给一线员工的经理,说,嘿,这个人似乎不太高兴。物流里有很多情绪。

[18:37] **SPEAKER_02:** You know, it's your stuff. Your business is on the line. You need to get it delivered. In fact, we measured, at the beginning of the year, we had automated 20% of the work. It was pretty low scale of automation.

> 你知道,那是你的货,你的生意都押在上面,你必须把它送到。事实上我们测算过,年初的时候,我们把20%的工作自动化了,自动化程度相当低。

[18:48] **SPEAKER_02:** We're going to finish this year at 50%. And we had set a goal for ourselves next year of 80. We thought 80 was actually the upper limit of what could be automated. It's not scientific. But now we feel like, oh, it's probably closer to 90 to 95 current.

> 今年年底我们会达到50%。我们给自己定的明年目标是80%。我们本以为80%实际上就是能被自动化的上限。这不是很科学的判断。但现在我们觉得,哦,当前大概能接近90%到95%。

[19:03] **SPEAKER_02:** And then that'll get way more so as LLMs keep progressing.

> 而随着大语言模型不断进步,这个比例还会高得多。

[19:07] **SPEAKER_03:** How will that affect the total cost of ocean freight? If all the human work gets automated, does stuff actually get materially cheaper?

> 那会如何影响海运的总成本?如果所有人工工作都被自动化了,东西真的会明显变便宜吗?

[19:15] **SPEAKER_02:** Yeah. It's 10% of the end cost that the importer exporter pays for their freight. 10%, if you look at the full P&L, about 10% is the labor cost in the freight forwarding layer of logistics. Wow.

> 会。它占进出口商为货运支付的最终成本的10%。如果你看完整的损益表,大约10%是物流中货运代理这一层的人工成本。哇。

[19:29] **SPEAKER_03:** So when AI is fully rolled out, stuff will actually get 10% cheaper. Well, the freight of moving the stuff, the cost of moving it. The stuff itself depends on what the ratio is. But yeah. But the transportation costs of international freight is actually 10% on it.

> 所以当AI全面铺开后,东西真的会便宜10%。嗯,是搬运东西的运费、搬运它的成本。东西本身能便宜多少取决于比例。不过是的。但国际货运的运输成本确实占其中10%。

[19:45] **SPEAKER_02:** On containerized ocean freight, that's our view, is that we can drop the price of everything by around 8%. And maybe it goes to 9% over the next few years by doing this.

> 在集装箱海运上,我们的观点是,我们能把一切的价格降低大约8%,通过这么做,未来几年也许能达到9%。

[19:55] **SPEAKER_01:** That has some big economic ripples, in terms of, wow. Yeah. Yeah. Yeah. In terms of, if it's becoming cheaper to ship things across the ocean, is it going to create just more trade?

> 那会带来一些巨大的经济连锁反应,哇。对对对。就是说,如果跨洋运输东西变得更便宜,它会不会催生更多的贸易?

[20:03] **SPEAKER_01:** I mean, there's also trade wars, but.

> 我是说,当然还有贸易战,不过。

[20:05] **SPEAKER_02:** Exactly. It's very hard to control for that in the world where tariffs just made everything like 10 times more expensive. But we're doing our part.

> 正是。在一个关税刚把一切都变贵了十倍的世界里,要把这个变量控制住是很难的。但我们在尽自己的一份力。

[20:11] **SPEAKER_00:** I mean, the white pill on AI right now is this hope and sort of possibility that AI rolled out properly across society would increase GDP 7% a year. So this would be maybe a few percent.

> 我是说,眼下关于AI的"白色药丸"(乐观愿景)是这样一种希望和可能性:如果AI在整个社会中得到恰当铺开,能让GDP每年增长7%。所以这块也许能贡献百分之几。

[20:24] **SPEAKER_02:** 7% a year will double you in 10 years is the law of 72. Yeah. Yeah. That is the hope, right? And I think more people should talk about that.

> 每年7%,按"72法则",10年就能翻一番。对,对。那就是希望所在,对吧?我觉得应该有更多人谈论这个。

[20:30] **SPEAKER_02:** And everyone's so worried about automating away the jobs. And I just think that misunderstands the role of companies in society. Like, the role of companies is not to employ people. It's to deliver goods and services. And in fact, whoever employs the least number of people will have the lowest cost and win.

> 每个人都那么担心把工作岗位自动化掉。我认为那是误解了公司在社会中的角色。公司的角色不是雇佣人,而是交付商品和服务。而事实上,谁雇的人最少,谁的成本就最低、谁就赢。

[20:49] **SPEAKER_02:** And that's how they benefit society, is lowering costs and making things more available for us to buy and sell. And there's this idea, well, how are people going to make money if AI is doing all the work? And I think that that very much misunderstands human nature, that we'll just want more things. Like, there's an infinite desire inside the human soul can never be satisfied without God. We need more stuff.

> 而这正是它们造福社会的方式——降低成本,让更多东西可供我们买卖。有一种说法是,那如果AI把所有活都干了,人们要怎么赚钱?我认为那非常误解了人性:我们只会想要更多的东西。人的灵魂深处有一种无穷的欲望,没有上帝就永远无法被满足。我们需要更多东西。

[21:11] **SPEAKER_02:** Like, we've got to have more. We've got to have more.

> 就是说,我们必须拥有更多,我们必须拥有更多。

[21:13] **SPEAKER_00:** And so we're trying to return to the garden.

> 所以我们是在试图回到那座伊甸园。

[21:16] **SPEAKER_02:** We may get a return to some. I think that, actually, the internet first, we haven't quite reconciled this on a spiritual, philosophical level, the emergence of these technologies. And AI would not even believe it. It's not even beginning to, of what it means for us. But there's a period in history called the Axial Age.

> 我们或许能回到某种程度。我觉得,其实先是互联网,我们还没有在精神、哲学的层面上真正消化这些技术的出现所意味着什么。而AI就更别提了——它对我们意味着什么,我们连开始理解都谈不上。但历史上有一段时期叫"轴心时代"。

[21:34] **SPEAKER_02:** It's about 500 years BC. And that's when coins really started to spread. What you had, if you think about it, with coins, is taking transactions between two people and really making them very impersonal. You no longer care who you're doing business with. I don't need to have a ledger.

> 大约是公元前500年。那正是钱币真正开始普及的时候。如果你想想,钱币带来的是把两个人之间的交易变得非常没有人情味。你不再在乎跟谁做生意。我不需要一本账簿。

[21:50] **SPEAKER_02:** Does this guy owe me money? What's my relationship? Do I trust him? Just like, here, take this thing. And it actually led to this breakdown.

> 这家伙欠我钱吗?我们是什么关系?我信任他吗?你只需说,给,拿着这个东西。而这实际上导致了一种崩解。

[21:57] **SPEAKER_02:** And it actually led to this breakdown in societies, because we just stopped being so knowing your neighbor. You used to only do business with your neighbors. Now you could just do business with any old person. The internet kind of does that at scale. What happened in the Axial Age, you had this breakdown of ability, of trust.

> 它实际上导致了社会的一种崩解,因为我们不再那么了解自己的邻里。你过去只跟邻居做生意,现在你可以跟随便什么人做生意。互联网某种程度上把这个规模化了。轴心时代发生的是,你出现了一种能力上的、信任上的崩解。

[22:15] **SPEAKER_02:** And you started to get degeneracy and all kinds of things that start to break down in society. And simultaneously, across the world, you had four major prophets that emerged. Well, prophets of sorts. You had Buddha. You had Lao Tzu, Confucius, and Socrates.

> 于是你开始出现堕落,以及社会中开始瓦解的各种东西。与此同时,在世界各地,涌现出了四位重要的先知——好吧,某种意义上的先知。你有佛陀,有老子、孔子,还有苏格拉底。

[22:30] **SPEAKER_02:** They all lived at the exact same moment in time, right, as coins were taking hold. Fascinating. As like, hey, we need to kind of get our hands around, how do we behave in this new world? So I do think there's an opportunity here. Maybe it could be you, Gary, at YC, to be the next Socrates, yes, Buddha.

> 他们全都生活在完全相同的那个时间点,正当钱币开始扎根的时候。很迷人。就好像在说,嘿,我们得设法搞清楚,在这个新世界里我们该如何行事?所以我确实认为这里有一个机会。也许可以是你,Gary,在YC,去当下一个苏格拉底,对,佛陀。

[22:49] **SPEAKER_00:** I'm in, but I might not be the right person. I mean, I particularly like this idea that the idea that what are humans going to do, is a little bit invalid in that, you know, that's a little bit like going back five, 800 years and saying, like, oh my God, all of us are farmers. And then what are we going to do when modern agriculture comes? And it's like, we figured it out.

> 我愿意,但我可能不是合适的人选。我是说,我特别喜欢这个观点:"人类将来要做什么"这个问题本身有点站不住脚,你知道,这有点像回到五百、八百年前说,天呐,我们所有人都是农民,那等现代农业来了我们要怎么办?结果呢,我们后来还是想明白了。

[23:12] **SPEAKER_02:** Or check the printing press, right? What are the monks going to do? They're transcribing words all day. There's no more jobs for transcription.

> 或者看看印刷机,对吧?那些修道士要怎么办?他们整天在誊抄文字。再也没有誊抄的工作了。

[23:18] **SPEAKER_00:** So there will be implications for society and morality and how people relate to one another. And obviously, like, we're seeing that right now. And we have no idea what that is.

> 所以对社会、道德以及人与人之间的关系都会产生影响。而显然,我们此刻正在目睹这一切,但我们完全不知道那会是什么样。

[23:26] **SPEAKER_02:** So it's early days, but history does kind of repeat. And there's lessons there and figure out, OK, how does this? But the human nature doesn't change much, right? You can't satisfy humans. You're just going to want more stuff.

> 所以现在还很早,但历史确实会重演。里面是有教训的,去弄明白,好,这该怎么办?但人性变化不大,对吧?你满足不了人类,人就是会想要更多东西。

[23:36] **SPEAKER_02:** The more money you have, the more, classically, right? Cliche, like, the more you have, the more you want. That's not going to go away. So if you give people a lot more stuff, it's not like, oh, I'm going to quit working. Most people aren't like that.

> 你钱越多就想要越多,老生常谈了,对吧?俗话说,你拥有得越多,想要的就越多。这一点不会消失。所以如果你给人多得多的东西,人们并不会说,哦,那我要不干活了。大多数人不是那样的。

[23:46] **SPEAKER_02:** I'm going to get a lot of stuff. I'll just quit working. You find out you're miserable. You want to keep producing, keep contributing.

> "我要弄到一大堆东西,然后就不干活了。"结果你会发现自己很痛苦。你会想继续创造,继续贡献。

[23:51] **SPEAKER_00:** MARK MIRCHANDANI- One of the interesting things that has been percolating around the YC community among young founders, like AI researchers that we've been talking to, is this idea that, like, there are going to be humans in the loop. The humans in the loop may well be, some might be, like, government mandated, right? In fintech, there's a lot around, you cannot have an AI algorithm, like, approve loans, for instance. There are, like, requirements from the government in these highly regulated industries to have humans in the loop. And then-

> 在YC社区里、在年轻创始人和我们交流过的AI研究者当中,一直在酝酿的一个有趣观点是:未来会有"人在环路中"(human in the loop)。这些环路中的人,很可能有一部分是政府强制要求的,对吧?在金融科技里,有很多规定,比如你不能让AI算法去批贷款。政府对这些高度监管的行业有要求,必须有人在环路中。然后——

[24:21] **SPEAKER_02:** MARK MIRCHANDANI- Customs brokerage as well. We have to have a human that's approving the transaction before we clear customs.

> 报关也是如此。在我们清关之前,必须有一个人来审批这笔交易。

[24:25] **SPEAKER_00:** MARK MIRCHANDANI- Yeah. Yeah. MARK MIRCHANDANI- And so vibe coding's happening. There's this idea of you enter a prompt, it comes back with a bunch of stuff, and then you just click Accept All Changes without reading any of it, right? Do you think this might happen?

> 对,对。所以氛围编程正在发生。有这样一种情形:你输入一个提示词,它返回一大堆东西,然后你看都不看就点击"接受所有更改",对吧?你觉得这种情况可能发生吗?

[24:39] **SPEAKER_00:** Would this happen at Flexport? Or would this happen more broadly across all businesses? Like, what if businesses are, at the core, like, hyper-intelligent AI that has access to all your systems of record, knows what to do, optimizes constantly? And you have sort of, like, government-mandated liability sinks that are humans in the loop. Ideally, the organizations still actually serve human needs, in which case, like, the decision to use, you know, vendor A or vendor B sometimes boils down to who brought me to the nicest steakhouse last.

> 这会在Flexport发生吗?还是会更普遍地在所有企业中发生?比如说,如果企业的核心就是一个超级智能的AI,它能访问你所有的记录系统,知道该做什么,不断进行优化?然后你有一种像是政府强制的"责任承接者",也就是环路中的人。理想情况下,这些组织仍然真正服务于人的需求,在这种情况下,选用供应商A还是供应商B的决定,有时归结为上次谁请我去了最好的牛排馆。

[25:12] **SPEAKER_00:** So then, like, the model for companies ends up being ASI of some sort, like, some sort of AI process at the core of each company. But then, you know, humans attach to it as either, like, decision makers in, like, you know, accepting or preventing liability and or holding relationships with other relationship holders at other companies.

> 那么,公司的模式最终会变成某种超级人工智能(ASI),每家公司的核心都是某种AI流程。但接着,人会附着在它之上,或者作为决策者——比如接受或规避责任——或者作为维系与其他公司关系持有者之间关系的人。

[25:34] **SPEAKER_02:** Yeah, and presumably, you're still relating with— you're still here to serve humans, you know? Once we get to a world where AI is serving AI, then fair enough, you don't need to learn that much from the record of human history, because there's no more humans involved in the loop. And I don't have a lot to say about that. But as long as there's humans there, there's going to—humans are going to want to relate with other humans and have a relationship. And, like, I think we're pretty, pretty, pretty far from humans preferring to work with AI than to work with other humans.

> 对,而且大概你仍然是在与人打交道——你在这里终归是为了服务人类,对吧?一旦我们进入一个AI服务AI的世界,那好吧,你就不太需要从人类历史的记录中学什么了,因为环路里不再有人参与。对那种情况我没太多可说的。但只要那里还有人,人就会——人会想要与其他人建立联系、维系关系。而且,我觉得离"人类宁愿与AI共事而不愿与其他人共事"还非常非常非常遥远。

[26:04] **SPEAKER_02:** We're seeing where AI is doing more and more work. You know, another good example is a— and just that made me think of with your bank, you know, you have to have an approver. Is that even in our humans and customs brokerage across the industry, we benchmark to make about 2% mistakes and they file the entry with 2%. And we built this sort of, like, AI system. Right. Right. And we built this sort of, like, AI system.

> 我们正看到AI在做越来越多的工作。你知道,另一个好例子是——你刚说到银行让我想起来,你知道,你必须有一个审批人。就是说,在报关这一行,人工在整个行业里的基准差错率大约是2%,他们提交报关单时带着2%的错误率。而我们打造了一种AI系统。对,对。我们打造了一种AI系统。

[26:26] **SPEAKER_02:** spellchecker, the two-digit code for Australia versus Austria, you could easily get that wrong. And the AI will figure out, oh, this thing is not made in Australia, it's made in Austria.

> 一个拼写检查器——澳大利亚(Australia)和奥地利(Austria)的两位代码,你很容易搞错。而AI会推断出来,哦,这东西不是澳大利亚产的,是奥地利产的。

[26:38] **SPEAKER_01:** I guess one question for you, Ryan, is if you were to start Flexport today, how would the company be different?

> Ryan,我想问你一个问题:如果你今天创办Flexport,这家公司会有什么不同?

[26:44] **SPEAKER_02:** Not that different, I hope. The things that Flexport did really well compared to all the other tech companies who have tried and failed in our space, both before we came along and in parallel, is we didn't look at ourselves as a pure technology company. We're willing to pick up the phone and solve problems with humans, drive down to the port. Still, to this day, we've got a new customer who's asking us to do something really weird. We need a crane on the truck to unload this thing.

> 但愿不会太不同。相比那些在我们这个领域尝试过又失败了的其他科技公司——无论是在我们之前还是同期——Flexport真正做得好的地方,是我们不把自己看成一家纯技术公司。我们愿意拿起电话、亲自和人一起解决问题、开车到港口去。直到今天仍是如此,我们有个新客户要求我们做一件很奇怪的事:我们需要卡车上带一台起重机来卸这个东西。

[27:12] **SPEAKER_02:** We don't have that. It's not typical what we do. And I just said, take the customer, and I need you to drive there and follow the truck and make sure this goes well. So I would not change that at all. And I think that's the mistake that a lot of tech companies make.

> 我们没有那个,那不是我们通常做的事。而我就说,把这个客户接下来,我需要你开车过去,跟着卡车,确保这件事顺利完成。所以这一点我完全不会改。我认为这正是很多科技公司会犯的错误。

[27:25] **SPEAKER_02:** And I think that's the mistake people in traditional markets will fail at, because they're like, oh, if there's no API, I can't do it. If my agent is unable to do this task, I guess the task can't be done.

> 我认为这也是传统市场里的人会栽跟头的错误,因为他们会想,哦,如果没有API,我就做不了。如果我的智能体做不了这个任务,那我想这个任务就没法完成了。

[27:36] **SPEAKER_01:** No tool use for cranes.

> 起重机没法用工具调用来搞定。

[27:37] **SPEAKER_02:** Yeah, and it might take you a long time, and you should not try to automate

> 对,而且它可能会花你很长时间,你不该试图去自动化

[27:41] **SPEAKER_04:** that last tail of things. You started and grew Flexport, especially in the first few years, during an era where there's more money coming into it. There's more venture capital each year coming into startups, and you had multiple fundraising rounds. In what ways was that? Was that capital an advantage?

> 那最后一小截长尾的事情。你创办并壮大Flexport,尤其是最初几年,是在一个资金越来越多涌入的时代。每年有越来越多的风险资本流入创业公司,你们经历了多轮融资。那在哪些方面是——那些资本是一种优势吗?

[27:57] **SPEAKER_04:** And I feel like now it's somewhat back there in the AI world now. The rounds are heating up. There's more money flowing in. It just posts the 2022 crash. What's your advice to the founders now who are in these companies that are growing and have options to raise huge funding rounds?

> 我感觉现在在AI世界里,某种程度上又回到了那种状态。融资轮次在升温,更多资金在涌入,刚经历了2022年的崩盘之后。对于那些身处正在成长、并有机会去融巨额资金轮的公司里的创始人,你现在有什么建议?

[28:12] **SPEAKER_04:** How should they think about it?

> 他们该如何看待这件事?

[28:13] **SPEAKER_02:** Every company is super unique, so don't listen to advice on a podcast. Get someone who's paying attention, knows the details of your business, which no one will know better than you. Generally, capital is a beautiful thing, having it in your bank account gives you a lot of advantages. All you really need to care about at the end of the day is price per share. Because if you issue more stock, as long as your price per share goes up, you are richer.

> 每家公司都极其独特,所以别听播客上的建议。去找一个真正在关注、了解你业务细节的人——而没人会比你自己更了解你的业务。总体上,资本是个美好的东西,银行账户里有钱会给你带来很多优势。归根结底,你真正需要在意的只有每股价格。因为如果你增发更多股票,只要你的每股价格上涨,你就更富有。

[28:37] **SPEAKER_02:** Doesn't matter what percent you own until it comes to control. So there's two things that matter. Do you control your company legally or otherwise? Culturally, it also works. But do you really have control over the decisions that are getting made, and do you have a job and price per share?

> 你持股比例是多少并不重要,除非涉及到控制权。所以重要的有两件事。你是否在法律上或其他方式上控制着你的公司?文化上也算。但你是否真的掌控着正在做出的那些决策?你有没有一份工作,还有每股价格?

[28:50] **SPEAKER_02:** And that's all that matters. I still think that's true. That's always how I thought about it. There's been a lot of dilution to our investors, but the price per share went up, and everybody's made better off. I didn't take away anybody's shares, so you're better off.

> 重要的就只有这些。我至今仍认为这是对的,我一直是这么想的。我们对投资人有很多稀释,但每股价格涨了,大家都变得更好了。我没有拿走任何人的股份,所以你是变好了。

[29:01] **SPEAKER_02:** The part that I underappreciated and that I now take very, very seriously is the degree to which money just wants to spend itself. And you will end up making a lot of mistakes where and the biggest mistake is believing, for sure, every company has a lot of problems. And you start to default to like, oh, we'll just use money to solve this problem. And the way that that manifests itself is, oh, I got this thing that we need to do. OK.

> 我以前低估、而现在非常非常认真对待的一点,是钱有多么"想要把自己花出去"。你最终会犯很多错误,而最大的错误是相信——每家公司当然都有很多问题——你开始默认地想,哦,我们用钱来解决这个问题就好。这一点表现出来就是:哦,我有这么件事得做。好。

[29:25] **SPEAKER_02:** Hire someone to do it. And you feel like you just end up very bloated. We had too many people. You start to really slow down. And it's just a super bad cultural approach to problem solving.

> 那就招个人来做。然后你会发现自己变得非常臃肿。我们人太多了。你开始真的慢下来。而这是一种极其糟糕的、以文化解决问题的方式。

[29:35] **SPEAKER_02:** Like, you're going to solve the problems, not the new people that you're going to hire. So I give this advice. Only one founder's ever listened to me, but I tell founders who are friends of mine who raise a large round, and sure, go raise a big round. As long as you're up round, like you're doing good, great. Raise a large round, then do a hiring freeze for 90 days.

> 就是说,解决问题的是你,而不是你将要招的那些新人。所以我会给出这样的建议。只有一位创始人真的听进去了,但我会对那些融了大额轮次的创始人朋友说,当然,去融一大笔钱吧。只要你是溢价轮(up round),说明你做得不错,很好。融一大笔钱,然后做一个90天的招聘冻结。

[29:53] **SPEAKER_02:** The next day. To tell your team culturally, like, no, the money's not going to solve our problems. We're going to solve our problems and keep that. And then, sure, go higher. Because it happened to us over and over again, where you just like headcount, got out of control.

> 就在第二天。为了在文化上告诉你的团队,不,钱不会解决我们的问题,是我们自己来解决我们的问题,并保持这个理念。然后,当然,再去招人。因为这在我们身上一次又一次地发生,人头数就那样失控了。

[30:06] **SPEAKER_02:** All the plans look good. I want to fund all the, we're doing budgeting for next year. And I'm like, god, it's so painful not to add OPEX, add engineers, whatever. But you've got to stay disciplined. And the money will easily make that stop.

> 所有的计划看起来都很好。我想为所有的……我们在做明年的预算。我心想,天呐,不去增加运营开支、不去加工程师什么的,真是太痛苦了。但你必须保持自律。而钱很容易会让这种自律停摆。

[30:21] **SPEAKER_00:** So I'm really psyched to hear about this idea that AI is actually transforming your business in pretty fundamental ways. It's like coming bottom up. What does Flexport look like in 2035?

> 听到AI正以相当根本的方式改造你们的业务,我真的很兴奋。它是自下而上冒出来的。Flexport在2035年会是什么样子?

[30:32] **SPEAKER_02:** What a cool thing about Flexport is the way our vision has evolved. I mentioned we started as a customer broker. We do all end to end, all the way from factory floor to consumer stores. We have an e-commerce business that does fulfillment, retail store distribution, et cetera. So we want to take that globally to where you can really ship anything, anywhere, by any means, any mode, in any quantity, and do it all, be a, by any code, all available via APIs, or voice, or it's just easy to execute transactions at the lowest cost, automate away the cost.

> Flexport一个很酷的地方,是我们愿景演变的方式。我提到过我们是从报关代理起步的。我们做全流程,一路从工厂车间到消费者门店。我们有一块电商业务,做履约、零售门店配送等等。所以我们想把它推向全球,做到你真的能运输任何东西、到任何地方、用任何手段、任何方式、任何数量,并且全部搞定,通过任何——通过API,或语音,或者就是让你以最低成本轻松完成交易,把成本自动化掉。

[31:02] **SPEAKER_02:** And so that brands, companies of all kinds, don't spend time thinking about logistics. Logistics should be this utility that just works. Just like you don't spend time thinking about the electrical grid, you flip the light switch, you get power. You go back to doing your thing, which is making something people want and talking to users. That's what I think companies should do.

> 这样一来,各类品牌和公司就不用花时间去操心物流。物流应该像一种"用了就好"的公用设施。就像你不会花时间去想电网,你按下开关就有电。然后你回去做你自己的事,也就是做出人们想要的东西、去和用户交流。我认为这才是公司该做的事。

[31:20] **SPEAKER_02:** Our customers should be doing that all day. Make great products. Make a great brand to sell those products. And we'll take care of everything in between in the most automated, efficient, reliable ways possible on a global basis. So today, and we have a long ways to go to actually make all that true.

> 我们的客户应该整天做那个:做出优秀的产品,打造一个优秀的品牌来销售这些产品。而中间的一切,我们会在全球范围内以尽可能最自动化、最高效、最可靠的方式来打理。所以就今天而言,要真正把这一切变为现实,我们还有很长的路要走。

[31:37] **SPEAKER_02:** First off, the automation stuff I talked about, making progress, but I got to keep going. And then the global aspect, so we have employee, we shipped cargo to and from 147 countries last year. But we only have employees in 22 countries. And therefore, people on the ground, they can do the work. Yes, we are automating that work.

> 首先,我谈到的自动化那些东西正在推进,但我得继续往前走。然后是全球化这一面,我们有员工——去年我们把货物运往和运出147个国家,但我们只在22个国家有员工。因此,在当地有人才能做那些活。是的,我们正在把那些工作自动化。

[31:56] **SPEAKER_02:** And in fact, it's easier for us to automate our own employees work than it is some third party company that's doing work. Even though they're in our software, it's very hard to automate. We don't know what they're doing. So we want to be in every country by 2035, certainly. In fact, our roadmap has us covering 95% of all container trade with our own people doing all the work in the country in 2028.

> 而且事实上,自动化我们自己员工的工作,比自动化某个替我们干活的第三方公司要容易。即便他们在用我们的软件,也很难自动化,因为我们不知道他们在做什么。所以我们希望到2035年一定要遍布每一个国家。事实上,我们的路线图是到2028年,由我们自己的人在当地完成所有工作,覆盖全部集装箱贸易的95%。

[32:20] **SPEAKER_02:** So by 2035, I think we could realistically say, look, we'll be everywhere that's legal. And that is a big extension of our original vision. And I didn't have all that in mind when I did YC Demo Day. My pitch was like, we'll do customs, and then we'll add some other stuff. But it wasn't like, we will cover the Earth, any two plates on Earth, whatever you want to move, we'll move it.

> 所以到2035年,我觉得我们可以现实地说,看,凡是合法的地方我们都会覆盖。而这是对我们最初愿景的一次巨大延展。我做YC Demo Day的时候脑子里并没有这全部构想。我的路演大意是,我们做报关,然后再加点别的东西。但并不是"我们要覆盖整个地球,地球上任意两个点,你想运什么我们都给你运"。

[32:41] **SPEAKER_02:** Yeah, it's a very ambitious goal. The good thing is, I really genuinely, we're going to win on tech. We're winning. We're going to extend our lead there relative to our peers, our competitors. We're behind them.

> 对,这是一个非常有野心的目标。好消息是,我是真心觉得,我们会在技术上取胜。我们正在赢。相对于同行、竞争对手,我们会扩大在技术上的领先。我们落后于他们(注:此处口误,意指领先)。

[32:53] **SPEAKER_02:** On the global side, that's super fun. If you told 25-year-old me, they're like, oh, Ryan, your job this year is we've got to launch Flexport in Indonesia, Australia, Japan, Philippines, Turkey, and Poland, and France. I'd be like, oh my, really? I get to go to all those places and talk to the locals and stuff? So it's a pretty fun moment in our history, but also really challenging, but fun kind of challenging, yeah.

> 在全球化这一面,那超级有意思。如果你告诉25岁的我,说,哦Ryan,你今年的任务是我们得在印度尼西亚、澳大利亚、日本、菲律宾、土耳其、波兰和法国把Flexport开起来,我会说,天呐,真的吗?我能去所有这些地方跟当地人聊天什么的?所以这是我们历史上一个相当有趣的时刻,同时也真的很有挑战,但是那种有趣的挑战,对。

[33:19] **SPEAKER_00:** No better kind. Ryan, thank you so much for joining us. Man, it's always a pleasure. All right, we'll see you guys next time.

> 没有比这更好的挑战了。Ryan,非常感谢你来参加。老兄,和你聊总是很愉快。好了,我们下次再见。
