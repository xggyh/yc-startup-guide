# 全文转录 · Tokenmaxxing:顶尖构建者如何用 AI 干 400 个工程师的活

> ▶ [YouTube](https://www.youtube.com/watch?v=57lDpTwiW6g) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/57lDpTwiW6g.md) &nbsp;·&nbsp; Tokenmaxxing: How Top Builders Use AI To Do The Work Of 400 Engineers

> 中英对照 · 每段英文原文下附中文翻译

[00:00] **SPEAKER_00:** i think that's like the defining question like will you have control over your own tools or will your tools have control over you using open claw these days is like driving a ferrari and it's like exhilarating it's insane like you get to do things like it figures things out you would never think a machine could figure out and it does it so quickly but then it's also like a ferrari and that you better be a mechanic like it's a ferrari that will break down on the side of the road you know when you most need it and you need to get out with your wrench and pop the hood and like fix it you know you're gonna have to fix it yourself and so this is a very exciting time in uh computer science and technology welcome back to a special episode of the light cone in

> 我觉得这是那个决定性的问题:到底是你掌控你自己的工具,还是你的工具掌控你。如今使用 OpenClaw 就像开法拉利,让人兴奋,简直疯狂,你能做到那些事,它能想出你根本不会认为一台机器能想出来的解法,而且做得飞快。但它同样也像法拉利,你最好懂点机械,因为这是一辆会在半路抛锚的法拉利——偏偏在你最需要它的时候,你得拿着扳手下车、掀开引擎盖、自己把它修好,你得靠自己修。所以现在是计算机科学和技术领域一个非常激动人心的时刻。欢迎回到 The Light Cone 的一期特别节目。

[00:50] **SPEAKER_03:** this episode we're going to talk about how gary tann got back to building if you follow us on twitter you'll know that after a multi-year hiatus to become an investor gary tann is back to being a builder and in the last couple months he shipped hundreds of thousands of lines of code and built popular open source projects that have gone from nothing to more than a hundred thousand stars on github and he did all of this while having a very demanding job running yc full time a lot of people on the internet don't even think that this is possible and are somewhat like in disbelief but it actually happened we know because we were here to see the whole thing and so today we're going to

> 这一期我们要聊聊 Gary Tan 是如何重新回到"构建者"角色的。如果你在 Twitter 上关注我们,就会知道,在多年暂停编码、转做投资人之后,Gary Tan 又回来当建设者了。过去几个月里,他写了数十万行代码,做出了几个热门开源项目,从零起步到在 GitHub 上拿下超过十万颗星。而他做到这一切的同时,还全职经营着 YC 这份极其繁重的工作。网上很多人甚至认为这根本不可能,颇有些难以置信,但它确实发生了。我们知道,因为我们全程亲眼见证。所以今天我们要来聊聊。

[01:26] **SPEAKER_00:** talk about how he did it well i'm relatively uh shocked myself i'm amazed as well it was 13 years of not coding and then suddenly boom i'm doing about 400x the amount of work that i was that year the last time i was even sort of like two-thirds of the time writing code maybe to start things

> 聊聊他是怎么做到的。其实我自己也相当震惊,也很惊叹。整整 13 年没写代码,然后突然砰的一下,我做的工作量大约是当年的 400 倍——上一次我大概还有三分之二的时间是在写代码。也许先从这里说起。

[01:44] **SPEAKER_03:** off how will we go back to the project that started it all off which was gary's list oh yeah and just like talk about a few months ago how you powered up claude code and like started

> 我们不如回到那个引发这一切的项目,也就是 Gary's List。对,聊聊几个月前你是怎么把 Claude Code 用起来、重新开始编码的。

[01:53] **SPEAKER_02:** to get back to coding yeah it was right after one of the lycan episodes right oh yeah definitely

> 重新回到编码。对,那正好是在某一期 Light Cone 节目之后,对吧?对,没错。

[01:56] **SPEAKER_00:** i realized that i wanted to bring together all the people who believed what i'd be able to do and i believed particularly for california and so i started a 501 c4 and now it's a c3 and a pack which is sort of what a lot of political groups do it's a very common way to bring people together you know everyone focuses on the money but we're trying to bring together smart people you know what i learned in the years of working in san francisco politics is that bringing together people is so powerful and uh that's what a mass social movement is and i said okay well why don't i just make a website where we start doing that and it would just start with um why don't i start writing about the issues that i'm worried about it's like i want children in school you know people watching this from all around the world might find it very very strange like i find it strange that uh it was not possible and still very very hard for a seventh grader or eighth grader in middle school in san francisco public schools to be able to take algebra and that was you know a math education thing like you know if i didn't get to do that when i was in public schools in the east bay of the bay area there's no way i would have studied engineering at stanford i never would have written code i never would have been able to do any of these things so it was close to my heart and i realized like hey it's time to write code and i ended up building posterous my first yc startup from 2008. what was positive for people who don't remember it yeah posterous was dead simple blogs by email it grew to be a top 200 website on the internet and then twitter ended up buying it for about 20 million dollars so that was sort of like my first bag really i actually built it again uh as post haven when twitter um you know bought it for the amazing people that we had hired and they shut down the startup it would have cost a couple million dollars to buy it back from twitter and at the time i had no money in the world so the next best thing was why don't i write it again and then in january of this year i ended up writing it a third time um only you know the first time it took about you know four million dollars and you know six or seven people and about a year and a half and then the second time it you know took about i don't know a hundred grand and two people me and my co-founder brett gibson who now runs initialized um and maybe like three months or so and then in this case it took about two hundred dollars which was my cloud code max account and probably five days full featured blog platform does everything you want and then on top of that like full rag full um agentic retrieval like be able to you know sort of go out and read all of the internet like every tweet i've ever done recursive crawl deep research of any topic the algebra thing is just one of a whole lot of different issues that we really really care about and to be able to go ingest the internet you know see all the arguments for and against and then to craft incredibly detailed um reports on the back end about um what are all the quotables like i think people who are big followers of the light cone might remember one of our first episodes about agentic uh systems with jake heller actually so jake created case text and he described exactly what i ended up building for basically journalistic uh long form articles about any you know sort of issue or uh you know piece of news that was happening and so you know anyone can go to gary's list.org today and you know we do about two or three relatively you know researched all fully sourced um articles about what's going on in california and san francisco and la and like how do we build a

> 我意识到,我想把所有相信我能做成某件事的人聚到一起,尤其是为加州这件事。于是我成立了一个 501(c)(4),现在又有了一个 (c)(3) 和一个 PAC(政治行动委员会),很多政治团体都是这么做的,这是把人聚在一起的常见方式。大家都盯着钱,但我们真正想聚的是聪明人。我在旧金山政治圈工作那些年学到的是,把人聚在一起非常有力量,这正是大规模社会运动的本质。我就想,那我干脆做个网站,从这里开始。起步很简单——我先把我担忧的那些议题写出来。比如我希望孩子们能在学校学到东西。全世界看这期节目的人可能会觉得很怪,我自己也觉得怪:在旧金山公立学校,一个七年级或八年级的初中生想学代数,过去做不到,现在也依然非常难。这是数学教育的问题。要是我当年在湾区东湾的公立学校没能学到代数,我绝不可能去斯坦福读工程,绝不会写代码,也绝不可能做成这些事。所以这件事对我而言意义重大。我意识到,是时候写代码了,最后我做出了 Posterous——我 2008 年的第一家 YC 创业公司。对于不记得的人,Posterous 是极其简单的"用邮件发博客"的平台,后来成长为全互联网排名前 200 的网站,最终 Twitter 以大约两千万美元把它收购了,那算是我人生的第一桶金。后来 Twitter 是为了我们招到的那批优秀员工才收购,并关掉了这家创业公司,我又把它重写了一遍,做成了 Post Haven。要从 Twitter 手里把它买回来得花几百万美元,而我当时身无分文,所以退而求其次:我干脆再写一遍。然后今年一月,我把它写了第三遍。只不过,第一次大约花了四百万美元、六七个人、一年半时间;第二次大概花了十万美元、两个人——我和联合创始人 Brett Gibson(他现在经营 Initialized)——差不多三个月;而这一次,只花了大约两百美元,也就是我的 Claude Code Max 账号,大概五天时间,就做出了一个功能齐全、你想要什么都有的博客平台。而且在此之上,还有完整的 RAG、完整的智能体式检索,能够跑出去读遍整个互联网——比如读我发过的每一条推文,递归爬取、对任何主题做深度研究。代数只是我们真正非常在意的一大堆议题之一。它能吞下整个互联网,看到正反两方的所有论点,然后在后端撰写极其详尽的报告,把所有值得引用的观点整理出来。经常看 Light Cone 的人可能记得我们最早几期里有一期讲智能体系统,嘉宾其实是 Jake Heller。Jake 做了 Casetext,他描述的东西正是我最终做出来的——本质上是针对任何议题或正在发生的新闻,写出新闻式的长篇文章。所以今天任何人都可以去 garyslist.org,我们每天大约发两三篇经过相当程度调研、全部标注来源的文章,讲加州、旧金山和洛杉矶正在发生的事,以及我们该如何建设一个更好的政府。

[05:49] **SPEAKER_02:** better government this is the thing i feel like people missed about gary's little don't fully get is that it's like the classic thing we've been talking about here which is like software was you build software to let people use it so it's like you build a blogging platform and people blog so maybe like they'd start their own sub stacks eventually or they write articles but gary's list is both blogging platform but it actually does the work of a high quality investigative journalist it's not just something that a journalist uses to publish their articles

> 一个更好的政府。我觉得人们对 Gary's List 有一点没完全领会,那就是我们一直在这里讲的那个经典观念:软件,过去是你做出软件让别人来用。比如你做一个博客平台,人们来写博客,最终也许他们会开自己的 Substack、写文章。但 Gary's List 既是一个博客平台,同时它本身还在做一位高质量调查记者的工作。它不只是记者用来发表文章的工具而已。

[06:17] **SPEAKER_00:** yeah i mean basically the for the equivalent of like five or ten dollars of opus calls i mean i would estimate that it does the work of like you know a real human being that would have to like go painstaking through dozens of articles read entire books about certain subjects annotate them I mean going back to the case text example like the thing that Jake taught me was that you need to think about what a human would do with the context given like what would it retrieve like does it go to the library what kind of book would it look for what does it search on for search you know on the web I mean the great thing now is like you don't have to just do that like you can get perplexities API and you can do deep research there you have X as API you can do deep research there you know groks API if you need to like do research on X using the grok API is actually very very good and you can just grab all of the context this is sort of going back to the philosophy of boil the ocean which is one of my essays it's like particularly when building agentic software now you don't have to settle for what we did when we were here foreign writing the code like and that goes for research as well what if you absolutely boiled the ocean like what is you know the total completionist like if you were a human this would take you about a month to do this research you can just you know zap the rocks harder uh you know it you pay more money and you might be token Maxing but you should token Max like basically if there is incremental work that makes something more complete more awesome more you know in the case of um this type of writing like we wanted to be more representative of reality like you know we don't just settle for one source when we can get 20 sources and we can cross-reference them we can figure out like well these 13 sources Say This and the seven sources disagree with that and then you know you want to feed all of that context into like your core prompt and then you can basically make a better decision than what you would just you know a human being clicking a link reading a headline and Knight basically making a better decision than what you would just you know a human being clicking a link reading a headline that's part of a, clicking on a link, reading a headline, and that's all you understand. And I think if you token max, that's actually the coolest thing you can do now. And it's not just in generating articles. It's clearly in writing code, right? I think now it's going to permeate every part of society. Every thing that we would call knowledge work could be token maxed. And

> 对,基本上,花相当于五到十美元的 Opus 调用,我估计它能完成一个真人才能做的工作量——那个人得费力翻遍几十篇文章、读完关于某些主题的整本书、还要做批注。回到 Casetext 的例子,Jake 教我的是:你要去想,一个人拿到给定的上下文会怎么做——他会去检索什么?会不会去图书馆?会找什么样的书?会在网上搜什么?现在最棒的是,你不必只靠自己去做这些——你可以用 Perplexity 的 API 在那里做深度研究,可以用 X 的 API 做深度研究,如果你需要在 X 上做调研,用 Grok 的 API 其实非常好,你可以把所有上下文都抓过来。这其实又回到了"把整片海洋煮沸"(boil the ocean)的理念,那是我写过的一篇文章。尤其是现在做智能体软件,你不必再将就于我们当年手写代码时那种妥协,做调研也一样。如果你彻底把海洋煮沸会怎样?那种极致的完整主义——如果换成一个人来做这项调研大约要花一个月,而你现在只需要把石头"电"得更狠一点,也就是多花点钱,你可能是在"token 拉满",但你就该 token 拉满。基本上,只要有能让成果更完整、更出色的增量工作值得做,就去做。就这类写作而言,我们想更真实地反映现实,所以当我们能拿到 20 个来源并交叉比对时,就不会只将就一个来源。我们能弄清楚:这 13 个来源这么说,而那 7 个来源不同意。然后你把所有这些上下文都喂进你的核心提示词,这样你做出的判断,就比一个人点开一个链接、只读个标题所能做出的判断要好得多。我觉得如果你把 token 拉满,这其实是现在你能做的最酷的事。而且不只是在生成文章上,写代码显然也是如此。我觉得现在它将渗透到社会的方方面面。任何我们称之为知识工作的东西,都可以 token 拉满。

[08:45] **SPEAKER_00:** I don't think that it means that we're going to get rid of people. I think it means that people need to still supply the agency. I need this. I'm the one who's sitting here caring about algebra. I want kids like me who couldn't afford private school. San Francisco

> 我不认为这意味着我们要淘汰人。我认为这意味着人仍然需要提供"主观能动性"。是我需要这个,是我坐在这里在乎代数这件事,是我希望那些像我一样上不起私立学校的孩子能有机会。旧金山——

[09:01] **SPEAKER_00:** is the one city in the world that has the highest rate of private school attendance, probably in the entire country, actually. And that's not okay. You shouldn't have to be rich to have a good education. And I don't know why that's controversial. And so for me, it's like this mass sort of shift in technology was happening. And then I had a need and a want and a desire. And

> ——是全世界私立学校入学率最高的城市,实际上可能是全美最高。这不对。你不应该必须有钱才能获得良好教育。我不明白这为什么会有争议。所以对我来说,当时正好赶上技术的这场大规模变革,而我又有一个需要、一个渴望、一个愿望。

[09:28] **SPEAKER_00:** it was a burning desire. It hurts me and pains me to think about 10, 12, 13-year-old kids who don't know algebra and could have. But some bureaucrat or some virtue signaling person in power says, actually, I don't want that kid who wants to learn algebra to learn it.

> 那是一种炽热的渴望。一想到那些十岁、十二岁、十三岁本可以学会代数却没能学的孩子,我就心痛难受。可某个官僚、某个手握权力、只想着表演道德姿态的人却说:其实,我不想让那个想学代数的孩子学到它。

[09:47] **SPEAKER_01:** So I think in this process of basically solving your own pain and need from the young Gary and building Gary's list, you sort of discover a lot of patterns on token maxing and this new way of building that led you

> 所以我想,在这个为年少时的 Gary 解决自身痛点和需求、构建 Gary's List 的过程中,你逐渐发现了很多关于"token 拉满"和这种全新构建方式的模式,而这些又把你引向了——

[10:04] **SPEAKER_00:** to the next project, which was GStack. I actually did not plan to make GStack. All I did was I realized that I was doing the same things over and over again. And then I got sick of typing the same things over and over again. And then I got sick of typing the same things over and over again. And then I got sick of typing the same things over and over again.

> ——下一个项目,也就是 GStack。其实我并没有计划要做 GStack。我做的只是意识到自己在反反复复做同样的事情,然后我实在厌倦了一遍又一遍地敲同样的东西。

[10:19] **SPEAKER_00:** So I went into my Apple Notes. I typed in all the things that I found myself writing over and over again into Cloud Code. And it was pretty simple stuff. It's like, here's the plan review. One of the things I started doing is I really love asking Claude to make ASCII art diagrams. One of the

> 于是我打开了我的 Apple Notes,把那些我发现自己在 Claude Code 里反复输入的内容都记了下来。都是些相当简单的东西,比如"这是方案评审"。我开始做的一件事是,我特别喜欢让 Claude 画 ASCII 字符图。

[10:38] **SPEAKER_00:** things I discovered is sometimes Claude would just get confused and like write bugs or not be complete. But once I started saying, actually, before you start your work, make an ASCII diagram of all the data flows, all the inputs and outputs. What are the user flows? What are the error messages? And you can see this. It's like data flow, state machines, dependency graphs, processing

> 我发现的一件事是,有时候 Claude 会犯迷糊,写出 bug 或者做得不完整。但一旦我开始要求它"在动手之前,先画一张 ASCII 图,把所有数据流、所有输入输出都画出来。用户流程是什么?错误信息有哪些?"——你就能看到这些内容,像是数据流、状态机、依赖图、处理流水线——

[10:59] **SPEAKER_00:** pipelines, decision trees. Once it did that, it loaded all of the context in and then it just did the work more completely. Like it boiled the ocean better. And it broke down into a bunch of different sections. Like here's architecture review, code quality, test. I mean, one of the

> ——处理流水线、决策树。一旦它画完这些,就把所有上下文都加载进来了,然后它把工作做得更完整,也就是把整片海洋煮得更彻底。它还会拆分成好几个不同的部分,比如"这是架构评审、代码质量、测试"。

[11:14] **SPEAKER_00:** things I learned building Gary's list was that when I was writing the code myself, I would always do the minimum amount of testing because it's just like not very fun. I knew I needed to have it, but I'm here to write, you know, fun new code. I did not like to write tests. And then honestly, like I hit all the things that everyone else hits when they start vibe coding, which is like, this is slop. It's not working that well. Like it works fine for the 80% case, but if any users

> 我做 Gary's List 学到的一件事是,当我自己写代码时,我总是只做最少量的测试,因为写测试实在没什么乐趣。我知道必须得有测试,但我来这儿是为了写好玩的新代码,我不喜欢写测试。然后说实话,我撞上了所有人开始"氛围编程"(vibe coding)时都会撞上的问题:这就是一堆糊弄出来的垃圾,跑得不怎么样。它在 80% 的情况下没问题,但只要有真实用户去碰它——

[11:41] **SPEAKER_00:** actually touch it, it starts falling over. And then that's when I realized, Oh, I can get to a hundred percent test coverage. I've since learned that a hundred percent is probably too much. Like hitting 80 to 90% is usually the best practice at this point. But yeah, this, this is basically the first version of plan dash eng dash review. I know everyone knows the office

> ——它就开始崩。就在那时我意识到:哦,我可以做到百分之百的测试覆盖率。后来我才明白,百分之百大概太多了,达到 80% 到 90% 通常才是当下的最佳实践。但总之,这基本上就是 plan-eng-review 的第一个版本。我知道大家都知道那个"办公时间"(office hours)技能。

[12:01] **SPEAKER_00:** hour skill, which is, you know, what people can use. And I still use when I'm trying to make a brand new product or a brand new feature, it simulates what, what we do when we're working with a company. It's like, how do you know that people want this? You know, who's it for? What does it do? And what's the.

> ——那个技能是大家都能用的。当我要做一个全新产品或全新功能时我仍然会用它,它模拟的是我们和一家公司合作时会做的事:你怎么知道人们想要这个?它是给谁用的?它做什么?还有它的——

[12:19] **SPEAKER_00:** Impact. Right. But this is like the proto skill. Like this is, I didn't even know skills existed and I posted this and it went viral. Like, you know, 200,000 people saw that. And then I made

> ——影响是什么。对吧。但这算是"原型技能"。那时我甚至都不知道有"技能"(skills)这个东西存在,我把它发了出去,结果爆火,大概有二十万人看到了。然后我又做了——

[12:29] **SPEAKER_00:** another version of it. That was a much more ex expansive version. I called it the mega plan. And then I ended up renaming it to the CEO plan. We've probably talked about meta prompting before I used meta prompting here. I took the other review plan that we had. And then I said, okay, well, let's do

> ——另一个版本,一个内容丰富得多的版本,我叫它"mega plan(超级方案)",后来又把它改名叫"CEO plan"。我们之前大概聊过"元提示"(meta prompting),我这里就用了元提示。我拿来我们已有的那个评审方案,然后说,好,我们来做——

[12:48] **SPEAKER_00:** a version of this. But like, imagine Brian Chesky sitting with you, right? Like Brian Chesky has this great line about what is a 10 star experience. So, and you know, the point of it is everyone thinks about hotels in terms of like three, this is a two, three star experience is a four star experience. And he like goes, you know, through the list, like five stars. It's like everyone, you know,

> ——一个升级版。但你想象一下 Brian Chesky 坐在你旁边,对吧?Brian Chesky 有一句很棒的话,讲什么是"十星级体验"。它的要点是,大家想到酒店时都是用三星、这是二星、这是三星、这是四星来衡量的。他会顺着这个清单往下讲,到五星——大家都知道五星意味着什么。

[13:09] **SPEAKER_00:** yeah, cool. Like, he's like, what's a six star and what's a seven star and what's an eight star. And like, he goes all through that entire list. And, um, that's one of my favorite, like product design exercises to go through, like as a mental exercise. And then the cool thing is like, you can do that every single time now. And so that's what this is. You know, this prompt basically tries to

> 对,很酷。他接着问:六星是什么样?七星是什么样?八星是什么样?他把整个清单都走了一遍。这是我最喜欢的产品设计思维练习之一。而现在最酷的是,你每一次都能做这个练习。这就是这个东西的作用——这个提示词基本上是在试图——

[13:29] **SPEAKER_00:** figure out what is the platonic ideal of, uh, what this is. These are sort of like the three, the two things that are pretty awesome. One is, uh, what is the 10 X check? What is more ambitious and delivers 10 X more value, uh, for only two X, the effort. Right. And so for whatever reason, coming

> ——弄清楚它的"柏拉图式理想形态"是什么样。里面有两三样特别棒的东西。其一是"10 倍检验":有什么更有野心、能带来 10 倍价值、却只需要 2 倍投入的做法?对吧。不知为何,从潜空间里出来——

[13:48] **SPEAKER_00:** out of latent space, it's helpful. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

> ——从潜空间里出来的东西,很有帮助。对,对,对。

[13:49] **SPEAKER_00:** Right. Right. Yeah. Yeah. Yeah. Yeah. So first off, it helps the model like really visualize. Like, so plan

> 对,对。所以首先,它能帮助模型真正地把东西"可视化"出来。就像这个 plan——

[13:54] **SPEAKER_00:** SEO skill . I actually really enjoy because I'm an ADHD CA CEO. And I love, um, potential, like pure potential. And so this is like the one, like, I can't believe this is just literally two little sentences, but like this unlocks an incredible amount. And so that's how G G stack started actually not, as you know, I didn't want it to be anything other than like, well, I just need to make, I'm skills.

> ——这个 CEO 技能,我其实非常喜欢,因为我是个有 ADHD 的 CEO,我热爱潜力,纯粹的潜力。所以这就是那个——我简直不敢相信,它其实就只有两小句话,却能解锁出惊人的东西。这其实就是 GStack 的起源。如你所知,我一开始并不想让它成为别的什么,我只是需要做一些技能而已。

[14:17] **SPEAKER_00:** And I had heard that people were So let's do that. like skill repos but then the third thing i did was i started um using these two skills so much that um my conductor instance was getting very backed up so this is how i use conductor uh this is actually my real setup like okay so this is your like daily workflow this is how you've been

> 我听说有人在做"技能仓库",那我们也来做这个吧。但我做的第三件事是,我开始大量使用这两个技能,以至于我的 Conductor 实例严重堆积。这就是我使用 Conductor 的方式,这其实就是我真实的配置。——好,所以这就是你的日常工作流,你就是这样一直——

[14:37] **SPEAKER_03:** shipping hundreds of thousands of lines of code a month it's all it's all in here yeah that's right

> ——每个月发布数十万行代码的,全都在这里。对,没错。

[14:41] **SPEAKER_00:** so i dropped like 13 prs in the last 48 hours and then you know i you just queue them up like anytime i come up with a new idea i come in and uh here it is you know i love using the ceo skill i love using the eng skill to like really make it super well tested i did that all in plan mode and then i'd click approve here and then you know claude would go and do all the stuff and then i did that so much that i ended up having like 15 different features that were all queued up waiting for me to manually test it like it passed it you know it passed end-to-end testing it passed it to me and then i did that and then i did that and then i did that and then i did that and then it passed uh integration it passed unit tests but like at the end of the day i still need to you know for gary's list it's like pop open the rail server and like you know load that user and like make it into that configuration for that particular user and like manually just make sure it works and i got sick of doing that and i was trying to use um claude in code mcp and it was very very slow two to three seconds for every turn it was like this is not usable for qa but i had heard about it and i was like oh my god this is not usable for qa and i was like oh my god this is not usable for qa and i was like oh my god this is not usable for qa and i heard that microsoft had heard that microsoft had heard that microsoft had released playwright which is sort of um an released playwright which is sort of um an released playwright which is sort of um an alternative testing framework in retrospect alternative testing framework in retrospect alternative testing framework in retrospect it's like actually there was like agent uh it's like actually there was like agent uh it's like actually there was like agent uh they're like agent harness and like all they're like agent harness and like all they're like agent harness and like all these other like tools that i could have these other like tools that i could have these other like tools that i could have used but the upside and downside of cloud used but the upside and downside of cloud used but the upside and downside of cloud code is it's so easy to just start something that i just popped open like i literally went in here and this is probably what i did it's like i'm so sick of using claude claude in in chrome mcp it's too slow let's go ahead and wrap microsoft's playwright can we do that and then i just pressed enter and then you know one of the things that emerged with gstack is that like this is how i create new features now of course you know what it's going to do now is like hey dude you already did that which is hilarious you know i have bug fixes right next to giant features and then um the way gstack works there's a ceo there's a designer there's actually a developer experience person in there there's a number of design tools uh and then plan eng is the last one and then i actually usually run slash codex and i recently added a slash claude in codex so one of the cool things that i actually learned from uh yc alums i came to an event and brain totally frazzled but you know went to one of our batch events and we're just you know shooting the about what's going on with claude code versus codex and at the time i was a total claude code only guy and uh i realized oh a lot of people actually prefer codex why is that and i discovered that claude code is ideal for the adhd ceo but once in a while there's a you know claude code will just bs a bunch of stuff like claude models are very very good but like they are not the smartest it turns out and so a lot of people you know explain to me that if you have a problem that's much crazier you need the 200 iq nearly non-verbal cto so you can just call in a friend and then that's what like slash codex is it's a gstack skill that takes whatever plan it your plan is or if you're out of plan mode and you already implemented it'll take your repo and it'll run codex in a command line prompt with the prompt that says find all the problems and all the bugs and it reports it back to cloud code and then you and claude code can work through those feet that feedback and then i have since added if you use codex as your main coding agent you can actually go and type slash claude and have claude come and be the ceo briefly if you want as well the cool thing about g-stack is when i run it through this program like i always i do i start with office hours ceo review like i do design if there's ui if um i know a developer needs to use it which is like practically all of ng brain stuff i run the developer review and then i do end review and then codex once that plan is done i've worked through all of the issues the g-stack relies very heavily on ask user question so because you know and that's that to me is like really important that's where the human you know vibe coder operator agentic engineer needs to supply their understanding of what's going on what are we building there's not really a substitute to that it would surprise me very much because it's you know it's a lot of work and it's a lot of work to do all of that but but i do think it's a good example of how someone really truly did manage to make a thing that could just make software without the human in the loop like that you know it's controversial take i think but um i never want to be entirely out of the loop i just want the machine to do the stuff that i don't want to do and so you know basically qa is a good examples and you know i mean that's hilarious coming back to the demo it's like i type something into the modern version of gstack and it's HP daemon with 70 commands as a CLI, and then QA is just browse, but in the prompt for QA, it says, look in your context, what did we do on this branch? If there's UI or any mutation of data, go and use the browser to test that thing, which is cool. It's like having a black box browser. It blew my mind when it first worked. It's like mini AGI is already here.

> 所以过去 48 小时里我提交了大概 13 个 PR。你就把它们排进队列,任何时候我一有新点子,就进来,喏,就在这儿。我喜欢用 CEO 技能,喜欢用 Eng 技能把东西测得非常扎实。我全都在 plan 模式下完成,然后在这里点"批准",Claude 就会去把所有事都做完。我这么干得太频繁,以至于最后攒了大概 15 个不同的功能全排在队列里,等着我手动测试——它已经通过了端到端测试、通过了集成测试、通过了单元测试,然后交到我手里。但归根结底,对 Gary's List 我还是得启动 Rails 服务器,加载那个用户,把它配置成那个特定用户的状态,然后手动确认它能正常工作。我做腻了这个。我本来想用 Claude 的 Chrome MCP,但它非常非常慢,每一轮要两三秒,根本没法用来做 QA。我听说微软发布了 Playwright,某种意义上是一个替代的测试框架。事后看,其实还有各种 agent harness 以及其他一堆我本可以用的工具,但 Claude Code 的好处和坏处都在于:开始做点什么太容易了。我就直接打开它,大概就是这么干的:我烦透了用 Claude 的 Chrome MCP,太慢了,我们干脆把微软的 Playwright 包一层,能做到吗?然后我就按了回车。GStack 里冒出来的一点是,这就是我现在创建新功能的方式。当然,它现在会做的事是:"哥们,你已经做过这个了"——这挺搞笑的。我把 bug 修复和庞大的功能并排放在一起。GStack 的运作方式是:里面有一个 CEO、一个设计师,其实还有一个开发者体验角色,有一堆设计工具,然后 plan-eng 是最后一个。之后我通常会运行 /codex,最近还加了在 Codex 里的 /claude。我从 YC 校友那里学到一件很酷的事:有一次我大脑一团糟地去参加了我们的一个批次活动,大家就聊 Claude Code 对比 Codex 的近况。当时我是彻头彻尾只用 Claude Code 的人,然后我发现,哦,很多人其实更偏爱 Codex,这是为什么?我搞明白了:Claude Code 对有 ADHD 的 CEO 来说是理想工具,但偶尔 Claude Code 会一本正经地胡扯一堆——Claude 的模型非常非常好,但事实证明它们并不是最聪明的。很多人跟我解释,如果你遇到一个更疯狂的难题,你需要那个 200 智商、近乎不善言辞的 CTO,你可以把这位"朋友"叫进来,这就是 /codex 的作用。它是一个 GStack 技能,会拿走你手头的方案(或者如果你已经不在 plan 模式、已经实现了,就拿走你的代码库),在命令行里用一句"找出所有问题和所有 bug"的提示运行 Codex,然后把结果反馈回 Claude Code,你和 Claude Code 就能一起处理这些反馈。后来我还加了:如果你把 Codex 作为主编码智能体,你也可以输入 /claude,让 Claude 短暂地过来当一下 CEO。GStack 很酷的一点是,当我用这套流程跑时,我总是从"办公时间 CEO 评审"开始;如果有 UI 就做设计;如果我知道开发者需要用它——差不多所有 G-Brain 的东西都是这样——我就跑开发者评审;然后做最终评审;等方案做完、我把所有问题都处理完后,再跑 Codex。GStack 非常依赖"向用户提问"(ask user question),这对我来说真的很重要,因为那正是人——氛围编程者、操作者、智能体工程师——需要提供他对当下情况、对我们到底在构建什么的理解的地方,这没什么能真正替代。如果有人真做出一个完全不需要人在环中就能造软件的东西,我会非常惊讶,因为那要做的工作太多了。不过我确实觉得那会是个很好的例子,证明有人真的成功做出了那样的东西——虽然我觉得这是个有争议的观点。但我永远不想完全脱离环路,我只想让机器去做那些我不想做的事,所以 QA 就是个好例子。回到演示,这挺搞笑的:我在现代版的 GStack 里输个东西,它是一个带 70 条命令的 CLI 守护进程,而 QA 就只是"浏览"。但在 QA 的提示里写着:查看你的上下文,我们在这个分支上做了什么?如果有 UI 或任何数据变更,就去用浏览器测试那个东西,这很酷,就像有一个黑盒浏览器。第一次跑通时把我震住了,简直像迷你版 AGI 已经来了。

[20:00] **SPEAKER_00:** I realize this is not true AGI. True AGI would be like, I'm not even here, and actually, that's fine. In this respect, as a builder, selfishly, I hope that we never have to stop. I hope that the machines never figure it out, because that would be really cool. Then humans are really important, and engineers who know how to do this, who have taste in design and product feedback, and the real customer in mind, we basically have wings for as long as we do.

> 我知道这并不是真正的 AGI。真正的 AGI 会是那种连我都不在场也照样行得通的状态,而且说实话那也没关系。就这一点而言,作为一个建设者,我私心里希望我们永远不必停下。我希望机器永远搞不定这最后一步,因为那样才真的很酷。那样的话,人就非常重要,而懂得怎么做这件事、对设计和产品反馈有品味、心里装着真实客户的工程师,基本上只要我们在做,就等于长了翅膀。

[20:32] **SPEAKER_01:** YC Startup School is back. We're hand-selecting the most promising builders in the world and flying them out to San Francisco for July 25th and 26th to discuss the cutting edge of tech. Apply now for a spot. Okay, back to the video. I think you crystallize a lot of these thinking in this post on X about thin hardness and fat skills, which actually encompasses all of this philosophy on how to token max.

> YC Startup School 回归了。我们从全世界精挑细选最有潜力的建设者,把他们请到旧金山,在 7 月 25、26 两日一起探讨技术的最前沿。现在就申请名额吧。好,回到节目。我觉得你在 X 上那篇讲"薄 harness、厚 skills"(thin harness and fat skills)的帖子里,把很多这方面的思考都提炼了出来,它其实概括了这一整套关于如何 token 拉满的理念。

[20:59] **SPEAKER_00:** Yeah. I mean, some of it came out of being trolled on the internet. Yeah. Some of it came out of being trolled on the internet, relentlessly, about Markdown. I'm just peddling a set of Markdown.

> 对。其中一部分是被网上的人喷出来的。对,有一部分是因为被人在网上就 Markdown 这件事没完没了地嘲讽——说我不过是在兜售一堆 Markdown。

[21:08] **SPEAKER_00:** I guess my lived experience at this point is that Markdown is actually code. It's just compiled in a different way, but you can get the computer to do really astonishing things. Even this, it's like, could we have imagined that I would be talking to something that has replaced Visual Studio for ... I don't use Visual Studio at all. There's no reason to.

> 我想,到现在我的亲身体会是:Markdown 其实就是代码,只是以另一种方式被"编译",但你能让计算机做出真正令人惊叹的事。就连这个也是——我们当初能想象到吗,我会在跟一个已经取代了 Visual Studio 的东西对话?我现在根本不用 Visual Studio 了,没有理由用。

[21:30] **SPEAKER_00:** Yeah. I mean, I'm an agent and my agent can do this, right? The name actually came from our partner, Pete Kuhman. We have had to build an internal agent, and we call that the harness over and over again. And then at some point, using Cloud Code all day, we realized, why should we rewrite a version of that over and over again?

> 对。我是说,我是个智能体,而我的智能体能做到这些,对吧?这个名字其实来自我们的合伙人 Pete Kuhman。我们不得不构建一个内部智能体,一次又一次地把那个东西叫作"harness(骨架/驱动壳)"。然后在某个时刻,整天用着 Claude Code,我们意识到:我们干嘛要一遍又一遍重写它的某个版本?

[21:52] **SPEAKER_00:** We should just use the things that are really awesome as harnesses. Like a harness is the core loop that takes the user input, gives it to the LLM, runs what the LLM does, it can do tool calls and things like that. Why would we build that? What we should be spending all our time doing is thinking about what Markdown should there be. And the way to think about Markdown is if you were an event planner and throwing a wedding and you were trying to write down a checklist of how to throw a wedding again, what would you write in plain English to teach the next person who had to do it what to do?

> 我们应该直接拿那些真正出色的东西来当 harness。所谓 harness,就是那个核心循环:接收用户输入,交给大模型,运行大模型产出的动作,它可以做工具调用之类的事情。我们为什么要自己造这个?我们真正该把全部时间花在上面的,是思考应该有哪些 Markdown。而思考 Markdown 的方式是:假如你是个活动策划,要办一场婚礼,你想写一份"如何再办一场婚礼"的清单,你会用平实的英语写下什么,来教会下一个接手的人该怎么做?

[22:27] **SPEAKER_00:** All of that should be in the Markdown. Whereas all the things that should be deterministic or is a real action, like a wedding planner might have to call 20 venues, but you wouldn't use Markdown for that. You would make a call to Twilio, for instance. All of the difficulty in agentic engineering today is when people try to do things that should be in Markdown in code, and it fails because code is brittle, it doesn't understand special cases. Code literally doesn't understand what you want or who you are.

> 所有这类东西都应该放进 Markdown 里。而所有那些本该是确定性的、或属于真实动作的事——比如婚礼策划可能得给 20 个场地打电话——你就不会用 Markdown 来做,你会去调用 Twilio 之类的接口。如今智能体工程里所有的难点,都出在人们试图用代码去做那些本该放进 Markdown 的事,结果失败了,因为代码是脆的,它不理解特殊情况。代码从字面上就不理解你想要什么、你是谁。

[23:06] **SPEAKER_00:** It is like executing deterministic zeros and ones in a Turing complete loop. It doesn't know. But then now we have LLMs that have latent space, and they know who you are, and it knows what your motivations are, and it can handle generic cases. And then a lot of the magic right now as an engineer is figuring out who you are. Figuring out, okay, how much of it is over here in LLM land, and how much of it is over there in code land?

> 它不过是在一个图灵完备的循环里执行确定性的 0 和 1,它并不"懂"。但现在我们有了拥有潜空间的大模型,它们知道你是谁,知道你的动机是什么,能处理各种一般化的情况。而现在作为工程师,很大一部分的魔法就在于弄清楚"你是谁",弄清楚:好,这件事有多少属于大模型的领域,又有多少属于代码的领域?

[23:38] **SPEAKER_00:** And then if you combine that with the other thing I learned, which is get to 80 to 90% tests. If it's not tested, and you're just throwing users in there, it's slop. 10x worse than human written code, because you just have no idea what's going to happen. And so that's one of the things that people have to do. It's like, all right.

> 然后再把这个和我学到的另一件事结合起来,那就是把测试覆盖率做到 80% 到 90%。如果没有测试,你就直接把用户扔进去,那就是一堆糊弄的垃圾,比人写的代码还糟 10 倍,因为你完全不知道会发生什么。所以这是人们必须要做的事情之一。好吧,就是这样。

[23:59] **SPEAKER_00:** Not only do you need to figure out what's going on in latent space and deterministic space, you also have to make sure that it's individually tested, and then the integration is tested. And then going back to Boil the Ocean, the machine doesn't care. It'll just do it. It's amazing. Just zap the rocks more, and you can get to 90% test coverage.

> 你不仅要弄清楚潜空间和确定性空间里各自发生着什么,还要确保每一部分都被单独测试过,然后集成也被测试过。再回到"把海洋煮沸":机器不在乎,它就是会去做,太神奇了。你只要多"电"几下那些石头,就能把测试覆盖率做到 90%。

[24:17] **SPEAKER_00:** And then you can have a system that is not quite perfect. OpenClaw right now, there are lots of failure cases, but it's 95% there. I feel like using OpenClaw these days is like driving a Ferrari, and it's exhilarating. It's insane. You get to do things.

> 然后你就能拥有一个虽不完美、但相当可用的系统。OpenClaw 现在还有很多失败的情况,但已经做到九成五了。我觉得如今用 OpenClaw 就像开法拉利,让人兴奋,简直疯狂,你能做到很多事。

[24:37] **SPEAKER_00:** It figures things out you would never think a machine could figure out, and it does it so quickly. But then it's also like a Ferrari in that you better be a mechanic. It's a Ferrari that will break down on the side of the road when you most need it, and you need to get out with your wrench and pop the hood and fix it. You're going to have to fix it yourself. And so this is a very exciting time.

> 它能想出你根本不会认为一台机器能想出来的解法,而且做得飞快。但它同样也像法拉利,你最好懂点机械。这是一辆会在半路抛锚的法拉利——偏偏在你最需要它的时候,你得拿着扳手下车、掀开引擎盖把它修好。你得靠自己修。所以现在是一个非常激动人心的时刻。

[24:57] **SPEAKER_00:** Yeah. It's a very exciting time in computer science and technology, because it's like, this is Homebrew Computer Club, the moment when the Apple One came out. The Apple One created by Steve Jobs and Steve Wozniak was a breadboard inside literally a wooden case hammered together with nails and duct tape. And if you wanted a personal computer, that's what you had to do, and that's where we're at right now. Yeah.

> 对。这是计算机科学和技术领域一个非常激动人心的时刻,因为这就像"家酿计算机俱乐部"(Homebrew Computer Club),就像 Apple One 刚问世的那一刻。乔布斯和沃兹尼亚克造的 Apple One,不过是一块面包板,装在一个用钉子和胶带敲敲打打钉在一起的木盒子里。当年你要一台个人电脑,就得这么折腾——而我们现在正处在同样的阶段。对。

[25:27] **SPEAKER_00:** It's really smart, technical, and people who had to study computer science have to spend two or three hours and maybe $500 or $1,000 in both tokens and cloud to actually get something like that running. But once you get it, we're sort of in the kit car Ferrari phase. Then you can drive, and you can go anywhere, and you want to shout to the hills like, hey, I got a Ferrari.

> 得是很聪明、很懂技术、专门学过计算机科学的人,花上两三个小时、也许再花五百到一千美元的 token 和云资源,才能真正把这样的东西跑起来。但一旦你搞定了,我们就有点像处在"组装式法拉利套件车"的阶段。然后你就能开着它,想去哪就去哪,你会想冲着山头大喊:嘿,我有一辆法拉利!

[25:51] **SPEAKER_02:** Even the part about fixing it yourself, I feel people ... It's just one of those things, until you've pushed through, you just don't quite get. If I really zoom out, it's almost like things have moved so quickly. If you think way back, just having Stack Overflow as a website that you could consult when you got stuck on a programming problem felt amazing. And then it's like a chat GPT launches, like, oh, now I've got this interactive thing that's way better than Stack Overflow.

> 就连"自己动手修"这一点,我觉得人们……这是那种没有亲自熬过来就体会不到的事情。如果我真的把视角拉远,几乎会觉得一切变化得太快了。往回想,当年只要有 Stack Overflow 这么个网站,在你被某个编程问题卡住时能去查一查,就已经感觉很棒了。然后 ChatGPT 一发布,哦,现在我有了一个远比 Stack Overflow 好用的交互式工具。

[26:14] **SPEAKER_02:** But you're still sort of doing the same thing. You're asking questions, and you're copy and pasting code, and you're running the code and seeing what happens, and copy and pasting it back. And then with cloud code, you sort of push through, and you realize that you don't need to do the copy and pasting anymore. It just actually executes and runs the code. And even with Open Cloud, I found out when I set it up, yeah, it's annoying because it can effectively brick itself, and it does a bunch of annoying things.

> 但你其实还是在做同样的事:你提问,你复制粘贴代码,你运行代码看结果,再复制粘贴回去。然后有了 Claude Code,你算是熬过了一关,你意识到不再需要复制粘贴了,它真的会自己执行并运行代码。就连 OpenClaw,我配好之后发现,是的,它挺烦人,因为它实际上会把自己搞"变砖",还会做一堆恼人的事。

[26:35] **SPEAKER_02:** But if you actually have cloud code- It'll fix it. Yeah. If I just have cloud code running, it will just fix it. It's clearly not the way things will be long-term, but there's this mentality shift of it doesn't actually matter if it's brittle and requires fixing, because you can actually just have another agent sat there fixing it all the time.

> 但只要你手上有 Claude Code——它会去修好。对。只要我让 Claude Code 一直跑着,它就会自动把问题修好。这显然不是长期该有的样子,但这里有一个心态上的转变:它是不是脆、是不是需要修,其实并不重要,因为你完全可以让另一个智能体一直守在那儿,随时把它修好。

[26:53] **SPEAKER_00:** Yeah. I feel like this evolution ... I was completely clueless. I was clod-code-pilled, and still am, but probably only 50% or 60% of my time building product or agentic engineering is in cloud code now, at some point, basically, Open Cloud. Wow.

> 对。我觉得这种演进……我当时完全一无所知。我曾经是 Claude Code 的死忠(现在也还是),但如今我用来做产品或做智能体工程的时间,大概只有 50% 或 60% 是在 Claude Code 里,某个时刻起,基本上转到了 OpenClaw。哇。

[27:11] **SPEAKER_00:** Almost half of it is through Open Cloud now. Yeah. Which is very interesting. I mean, then again, I'm also spending most of my time working on G-Brain itself. So G-Brain came about because, obviously, we had Peter on the show, and then I finally got around to it.

> 现在差不多有一半是通过 OpenClaw 做的。对,这很有意思。不过话说回来,我大部分时间也都在做 G-Brain 本身。G-Brain 的出现,显然是因为我们请 Peter 上过节目,然后我终于腾出手来做了这件事。

[27:25] **SPEAKER_00:** It was like one weekend. I said, I got to check this out. What's going on with Open Cloud? Let's get it going. This was about the time Karpathy wrote his next post about knowledge LLM wikis.

> 就是一个周末的事。我说,我得来看看这个。OpenClaw 到底怎么回事?让我们把它跑起来。那大概正好是 Karpathy 写下他那篇关于"知识型 LLM 维基"的帖子的时候。

[27:37] **SPEAKER_00:** And so I was like, okay, well, I have a repo full of markdown. I should put all of my context into that markdown. And then at some point, I realized, oh, shoot, it's just using grep. And grep is not that good. It's wasting context.

> 于是我想,好,我有一个塞满 Markdown 的代码库,我应该把我所有的上下文都放进那些 Markdown 里。然后在某个时刻我意识到,糟糕,它只是在用 grep,而 grep 没那么好用,它在浪费上下文。

[27:52] **SPEAKER_00:** It's loading a lot more into context than it needs to. And then I sort of fell into a rabbit hole. I just went into Conductor, clicked Quick Start, and then I had G-Stack built into Conductor already. And basically, this was how I started. It was actually much more interesting than that.

> 它往上下文里加载的东西远比实际需要的多。然后我就一头栽进了这个"兔子洞"。我打开 Conductor,点了"快速开始",而 GStack 那时已经内建进了 Conductor。基本上我就是这么开始的。其实过程比这还有意思得多。

[28:09] **SPEAKER_00:** So I didn't start off from nothing. One of the things I've learned as you write a larger and larger corpus of code is you have it loaded in your brain. You're like, oh, well, in order to build an agentic newsroom for Gears of War, I'm going to have to do this. I'm going to have to do this. I'm going to have to do this.

> 所以我并不是从零开始的。随着你写下越来越庞大的代码量,我学到的一件事是,你会把它装进自己的脑子里。你会想:哦,好吧,要为 Gary's List 搭一个智能体式的新闻编辑室,我得做这个,得做这个,还得做这个。

[28:21] **SPEAKER_00:** I'm going to have to do this. I'm going to have to do this. I'm going to have to do this. I'm going to have to do this. I'm going to have to do this.

> 我得做这个,得做这个,还得做这个。

[28:23] **SPEAKER_00:** I'm going to have to do this. I'm going to have to do this. But when you're in Gary's list, I actually had to learn about vector embedding and hybrid RRF and chunking. When you're in there trying to make it work, you're just very applied. It's like, I have an output that I want.

> 我得做这个,得做这个。但当你在做 Gary's List 时,我其实不得不去学向量嵌入、混合 RRF(倒数排名融合)和分块(chunking)。当你身处其中、努力想让它跑通时,你的状态是非常"实战导向"的:我有一个想要的输出结果。

[28:38] **SPEAKER_00:** I want the article to look like this. It needs to be of this quality. It needs to have these citations. You start building up your tests and integration tests, and you end up with a product that's battle-tested from the output that you want. And so I sort of put two and two together and I, you know, and this is something that, you know, anyone can do, actually, it's like this, this is why I think we're entering the golden age of open source, I could just open, you know, this project and conductor.

> 我要文章长成这个样子,要达到这样的质量,要包含这些引用出处。你开始搭建你的测试和集成测试,最终从你想要的输出反推,得到一个经受过实战检验的产品。于是我把这些前后串了起来。而这件事其实任何人都能做,这也是为什么我觉得我们正在进入开源的黄金时代——我可以直接在 Conductor 里打开这个项目。

[29:07] **SPEAKER_00:** And then the first thing I write is like, you know, go look at, you know, tilde slash git slash Gary's list. Like look at how we do chunking, embedding, you know, hybrid RF rag, like all of this, and then just like extract it. And then I want to use Postgres with PG vector. And like, I want a, you know, full rag system for my open claw. And then sort of like one thing led to another, it's like, then I have, you know, 10 windows and G brain, and I'm just like, add it.

> 然后我写下的第一件事大概是:去看看 ~/git/garyslist,看看我们是怎么做分块、嵌入、混合 RRF 检索这一整套的,然后把它抽取出来。接着我说我想用带 pgvector 的 Postgres,我想给我的 OpenClaw 搭一套完整的 RAG 系统。然后就是一件事牵出另一件事,接着我就开了 10 个窗口在 G-Brain 里,不停地"加上这个"。

[29:38] **SPEAKER_00:** What's cool about open claw. I mean, maybe this is a good example. This is actually my open claw, I did go ahead and ask it's how you know, how did I actually get into it? January 23. Also, all your email, I had a tweet that was like cloud code this week.

> OpenClaw 酷的地方是——也许这是个好例子。这其实就是我的 OpenClaw,我确实去问了它:我到底是怎么开始上手的?一月二十三日。还有你所有的邮件。我这周发过一条讲 Claude Code 的推文。

[29:51] **SPEAKER_00:** Because I wake in my 25 year old self, the one that checked Red Bulls and stayed up till dawn coding. We're so back. The builder identity resurfaces, you know, I'm basically back to, you know, sleeping four hours and, you know, coding 20 hours a day, you know, this is also when I started getting myself into trouble, like talking about lines of code, I still believe this,

> 因为我唤醒了 25 岁的那个自己——那个灌红牛、熬到天亮写代码的自己。我们彻底回来了。那个"建设者"的身份重新浮现,我基本上又回到了每天睡四小时、写 20 小时代码的状态。也正是从这时起,我开始给自己惹麻烦,比如谈论代码行数——我到现在仍然相信这一点。

[30:11] **SPEAKER_03:** by the way, this might be like a good quick aside to talk about like this, this idea of like, lines of code being important measure has been like controversial on the internet, there's obviously the counter argument, like, oh, lines of code doesn't like measure developer productivity, but what doesn't right? But do you think but it also does? So it also kind of does, right?

> 顺便说一句,这也许是个不错的小插曲,可以聊聊"代码行数是重要衡量指标"这个观点。它在网上一直很有争议。当然有反方论点,说"代码行数并不能衡量开发者的生产力"——可又有什么能衡量呢,对吧?但你觉得,它是不是其实也确实能衡量一部分?所以它也算某种程度上有效,对吧?

[30:31] **SPEAKER_00:** Yeah, like it does. It's clearly and you know, what's interesting is you can actually, there's well published Git repos out there that you can run to strip away and like standardize what is actual logical lines of code. And so I actually did go ahead and do that. You know, and I got into trouble for saying like, oh, I'm coding it like 100x. The rate that I was in 2013.

> 对,它确实能。这很明显。有意思的是,其实网上有一些成熟公开的 Git 仓库工具,你可以跑一跑,把注释、空行之类剥掉,标准化出真正的"逻辑代码行数"。我确实去这么做了。之前我说"我写代码的速度大概是我 2013 年时的 100 倍",结果为这话惹了麻烦。

[30:54] **SPEAKER_00:** And then after I did the logical lines of code stripped down, actually went up, it actually went up. So it turns out that I was actually doing 400x the amount of code, but you know, obviously, I wasn't writing it, I was directing, you know, 15 agents at a time to do so. And then by the numbers, like, it was not that it did like knock down my lines of code from cloud code a little bit. But the surprising thing to me was that I was actually doing 400x. It was that it knocked down the amount of lines of code that I was writing in 2013, by like 70%.

> 结果我做完"逻辑代码行数"的剥离统计后,这个数字反而上去了,真的上去了。原来我实际产出的代码量是当年的 400 倍——当然,显然不是我亲手写的,我是在同时指挥大约 15 个智能体去写。按数字来看,Claude Code 确实把我亲手写的行数削减了一点点。但让我惊讶的是,我实际产出竟然是 400 倍——它把我 2013 年亲手写代码的那个行数基数,削掉了大约 70%。

[31:27] **SPEAKER_00:** And so I think that that's sort of the mismatch here, like people get very upset because it's easy to like pad the lines of code if you're a human writing code, whereas like, unless you direct cloud code to literally like pad the lines of code, it doesn't necessarily do that, like, it'll maybe build the wrong thing. Like you might not steer it very well. It might not do the right thing. But like, it's not trying to optimize for lines of code the way a human working a job would, right? Which is, you know, that's just life.

> 所以我觉得这里存在一种错配。人们之所以很反感,是因为如果是人在写代码,很容易"注水"、故意堆行数;而除非你明确指挥 Claude Code 去注水凑行数,否则它不一定会这么做——它也许会造出错的东西,你可能没把它引导好,它可能做得不对。但它并不会像一个上班的人那样,刻意去优化代码行数这个指标,对吧?而人会,这就是现实。

[32:00] **SPEAKER_00:** And then I guess the really surprising thing is if you look at the literature about software engineering going back to like 2000, 1990, I mean, it's pretty clear that the average number of lines of code that a professional software engineer that's like tested and production ready, it's not like 100 lines of code. It's like 30. It's like 50. It's like 30. Like a day.

> 然后我想,真正令人惊讶的是,如果你去翻软件工程的文献,一直回溯到 2000 年、1990 年,会很清楚地看到:一个专业软件工程师平均写出的、经过测试且可用于生产的代码,并不是每天 100 行,而是大约 30 行、50 行、30 行——每天。

[32:23] **SPEAKER_00:** Yeah, a day. Right? Like for me, it was like 14. But I was like part time. I don't know.

> 对,每天。对吧?对我来说大概是每天 14 行,不过我那时算是兼职,说不好。

[32:28] **SPEAKER_00:** It's so that's where the 400x actually came from. You know, the other thing I know is like, I should have said that instead of just trolling people more on the line of code. If I trolled you on the internet, I'm very sorry for that. Like there, you know, there is a deeper understanding of this. And I did end up releasing a blog post about it that explains this quite a bit more.

> 所以那个 400 倍就是这么算出来的。我知道的另一件事是,我当初就该把这些解释清楚,而不是在代码行数这事上继续挑逗大家。如果我在网上呛过你,我非常抱歉。这背后其实有更深一层的理解。我最后确实发了一篇博客文章,把这件事解释得详细多了。

[32:47] **SPEAKER_00:** I mean, and I think it's not a little bit significant. It's very significant for people who are technical, because it actually raises the bar on like what you're capable of doing. Like all the people who are attacking me about lines of code, they particularly are the people who are most likely to get wings if you like let it rip and token max. This is sort of like the classic problem. It's like if you have taste, and you understand technology, you are particularly the people who should would benefit the most from getting this.

> 我觉得这件事的意义不只是"有一点点重要"。对懂技术的人来说,它非常重要,因为它实实在在地抬高了你所能做到的上限。那些在代码行数上攻击我的人,恰恰是最有可能因为"放开手脚、token 拉满"而长出翅膀的人。这算是个经典的悖论:如果你有品味、又懂技术,你恰恰就是最该、也最能从掌握这套方法中受益的人。

[33:18] **SPEAKER_00:** All someone has to do is. You know, believe. Right. Yeah. So stop fighting.

> 一个人要做的,只是——你懂的,去相信。对吧。所以别再抗拒了。

[33:23] **SPEAKER_00:** Just open cloud code and try it. You know,

> 直接打开 Claude Code,试一试。你懂的。

[33:25] **SPEAKER_02:** I think another thing that's potentially going on is just like, the experience is very dramatically depending on like the models and the harnesses. Like certainly something I've noticed is any sort of like, semi complicated programming tasks I try and do through my open core agent just like kind of fails. Like it's exactly the same model. And so like Opus 4.7.

> 我觉得另一件可能在起作用的事是:体验会因为模型和 harness 的不同而天差地别。我确实注意到,任何稍微有点复杂的编程任务,只要我试着用我那个开源核心的智能体去做,就基本会失败。而它用的其实是完全相同的模型,比如 Opus 4.7。

[33:49] **SPEAKER_02:** As Claude code, but it just like, like anything above like a simple script, I just find like it's not like that great at so I'll go back into like Claude code. And then it was sort of a moment for me where I realized, oh, like, this is how it used to feel like this is how like, even six months ago, used to feel like, oh, like you try and like these things. Yeah, these things aren't quite there yet. And then Claude code with like, Opus 4.5 was like, oh, like, it's actually magic here.

> ——和 Claude Code 用的是同一个模型,但只要超出简单脚本的范畴,我就发现它没那么擅长,于是我又退回去用 Claude Code。那对我来说是个顿悟时刻,我意识到:哦,原来以前就是这种感觉,甚至半年前也是这种感觉——你去试这些东西,嗯,它们还没到位。而 Claude Code 配上 Opus 4.5,则是那种"哦,这里简直是魔法"的感觉。

[34:15] **SPEAKER_02:** It's about to recur.

> 这一幕即将重演。

[34:17] **SPEAKER_00:** Like right now, people sort of are feeling like. Like open claw or Hermes is like, not quite there, or it's like a lot of work. And then I guarantee you, like, this time next year, like, everyone's going to be saying what you heard here first, which is like, every single person on the planet will have their own personal AI, we could either live in a world where we have our own AI, where we have our own data, our own integrations, like we see what's happening, we write our own prompts, and we have control over what we see. Okay. Or it's corporate controlled.

> 就像现在,人们的感觉是 OpenClaw 或 Hermes 还没完全到位,或者说要花很多功夫。但我向你保证,明年这个时候,所有人都会开始说你在这里最先听到的这句话:地球上每一个人都会拥有自己的私人 AI。我们要么活在一个我们拥有自己的 AI、自己的数据、自己的集成、能看清正在发生什么、自己写提示词、掌控自己所看到内容的世界;要么就是被企业控制的世界。

[34:51] **SPEAKER_00:** It's something, you know, you go to a host, it's kind of like your Facebook feed. And like, you don't know what the, you know, who wrote that algorithm? And who does it benefit? And like, what business model is behind it? Like nobody knows.

> 那会是这样一种东西:你去访问某个托管方,有点像你的 Facebook 信息流,而你并不知道那个算法是谁写的、它让谁获益、背后是什么商业模式——没人知道。

[35:03] **SPEAKER_00:** The most powerful idea that like, was a gift was the personal computer revolution. And we're about to go through exactly that same shift with personal AI. And it's going to be a choice like, you know, people are going to have to figure out, am I willing to write my own prompts? And, you know, I think I wish Pete Kuman were here, like, that's one of the things we learned from him, too. It's like, unless you have your own prompts, and you can write it for yourself, like you are, you know, below the API line for some PM or developer that is not you, who like will not understand you will not understand your needs will not understand what you uniquely care about.

> 那个作为馈赠、最有力量的观念,就是个人电脑革命。而我们即将在"个人 AI"上经历一模一样的转变。这将是一个选择:人们得想清楚,我是否愿意自己写提示词?我真希望 Pete Kuhman 在场,因为这也是我们从他那里学到的一点:除非你拥有自己的提示词、能为自己写它,否则你就处在"API 线以下",受制于某个不是你的产品经理或开发者——那个人不懂你,不懂你的需求,不懂你独一无二在乎的东西。

[35:43] **SPEAKER_00:** And I think that's like, the defining question, like, will you have control over your own? Will you have control over your own tools? Or will your tools, your tools have control over you?

> 我觉得这就是那个决定性的问题:你能掌控你自己的……你能掌控你自己的工具吗?还是说,是你的工具在掌控你?

[35:52] **SPEAKER_01:** And I think this is the one of the disconnects that the public has, I think, is a lot of these capabilities, you have to be on the latest and greatest models. And it's actually quite expensive to use them and burn all the tokens for now. It's coming down. But I think maybe people are just trying like Sonnet or the free model or having the basic cloud probe subscription only. Yeah.

> 我觉得这也是大众存在的一个认知落差:这里很多能力,你得用上最新、最强的模型才行。而目前用它们、把 token 大量烧掉其实相当贵——成本在下降,但我想很多人可能只是在试用 Sonnet、或免费模型,或者只订了最基础的 Claude 订阅。对。

[36:19] **SPEAKER_01:** And I think part of this, maybe we have to address that this new way of really getting all this almost ASI AGI moment for for building is you have to be burning lots of tokens, the whole token maxing paradigm.

> 我觉得这里有一部分,也许我们得点明:要真正获得这种近乎 ASI/AGI 级别的构建体验,这种新方式的前提就是你得烧掉大量 token——也就是整套"token 拉满"的范式。

[36:32] **SPEAKER_02:** It actually reminds me of rent, San Francisco rent, like one of the things that I feel like we always have to do with YC founders is that it's like a general thing is like, oh, like, I don't want to move to San Francisco, because it's like, so expensive to live there. But it's like, it's so expensive to not live. Yeah. Right. Like early on in a YC badge, like I'm used to like a founder being like, like this, like this apartment is like $1,000 a month in rent, like seems ridiculous, like, should I like pay it or not?

> 这其实让我想起房租,旧金山的房租。我觉得我们和 YC 创始人打交道时,总要处理的一件普遍的事就是:哦,我不想搬到旧金山,因为在那儿生活太贵了。但事实是,不住在那里的代价更贵。对。比如在 YC 批次早期,我常遇到创始人说,这套公寓月租 1000 美元,简直离谱,我到底该不该付?

[37:00] **SPEAKER_02:** It's like, no, you should absolutely pay and if anything, you should pay more to not just be in San Francisco, but being like the dog patch and just like being like neighborhoods where you create the serendipity like token maxing is going to be one of those things for founders that we sort of have to teach them where it's not immediately obvious that you shouldn't, this is actually like rent, like this is one of the things where you should like, spend as much as you can. As much as you can to like, get the like, most utility out of it versus treating it like the office desk or something like sure, you can economize on that or you don't need like a super expensive like couch, but like, when it comes to like actually using the models and your token spend, you should probably be like pushing pretty hard on that.

> 而答案是:不,你绝对应该付,甚至更应该多花点,不只是为了待在旧金山,而是待在像 Dogpatch 这样的社区、那些能创造机缘巧合的街区。"token 拉满"对创始人来说也会是这样一件事,是我们某种程度上得去教他们的——它并不一目了然地"该做",但它其实就跟房租一样,是那种你应该尽可能多花的事情,尽你所能地花,以榨取出最大的效用。而不是把它当成办公桌之类的东西——那些当然可以省,你也不需要一张超贵的沙发,但一旦涉及到真正使用模型、涉及到你的 token 花销,你大概就应该在这上面用力推、狠狠投入。

[37:37] **SPEAKER_00:** Yeah, one of the key maxims for YC is, you know, how do you find good startup ideas, live in the future and build what's missing, right? And so this is a profound version of that, where all you have to do is. Is commit your brain to look at, you know, spending $500 in a single day on tokens and say actually, like, you know, as long as I'm building something that's actually of great value to me, you know, and I'm building the right thing, I'm going to do that.

> 对,YC 的一条核心格言是:怎么找到好的创业点子?活在未来里,把缺失的东西造出来,对吧?而这就是这句话的一个更深刻的版本——你要做的,只是让自己的头脑接受这样一件事:一天在 token 上花掉 500 美元,然后说,其实只要我在构建对我真正有巨大价值的东西、只要我在构建对的东西,我就会这么花。

[38:06] **SPEAKER_03:** Yeah, I have a weird question. Do you think that in some ways, the fact that you tried to build all of this while also being the CEO of Y Combinator actually helped you because like, your time is so scarce, you have to like. Try to figure out how to write hundreds of thousands of lines of code, which is like spare minutes in between meetings, unlike a full time software engineer that could, you know, just take the time to like open the website and like click around it, like test it like those minutes were like, insanely scarce for you as you were constantly pushing yourself to figure out how to like automate everything.

> 对,我有个奇怪的问题。你觉不觉得,从某种意义上讲,你是在同时担任 Y Combinator CEO 的情况下试图构建这一切,反而帮到了你?因为你的时间极度稀缺,你不得不想办法在会议之间那点零碎的几分钟里写出数十万行代码——不像一个全职软件工程师可以从容地打开网站、到处点点、测一测。对你来说那些零碎的分钟稀缺到疯狂,于是你不断逼自己去琢磨如何把一切都自动化。

[38:37] **SPEAKER_00:** Yeah, I envy time billionaires, you know, sometimes look at I mean, I'm looking at my kids and it's like, these kids are time billionaires right now, you know, you could just like do that, you know, you run across people at startup schools. All the time. And it's like, you're a time billionaire right now, like, this is incredible, like, you could just do anything you'd like learn about anything. This is so great. So yeah, I'm, you know, personally, like, I think my philosophy is I am in a crazy rush in my brain, I'm like, probably live 10 billion lifetimes live in this body right now.

> 对,我很羡慕"时间亿万富翁"。我有时看着我的孩子,心想,这些孩子现在就是时间亿万富翁,你可以尽情去做任何事。你在 Startup School 上会不断遇到这样的人,你会觉得:你现在就是个时间亿万富翁,这太不可思议了,你可以做任何你想做的事、学任何你想学的东西,这太棒了。所以就我个人而言,我的信条是:我脑子里处在一种疯狂的赶时间状态,我大概想在这具身体里、此时此刻,活出一百亿次人生。

[39:04] **SPEAKER_00:** And I need every single moment to count. And then if you can token max, it's like, I mean, you can buy millions of years of consciousness of machine consciousness. Now I can be a time billionaire. It's not, you know, my own time. It's the time of a machine, like doing work for me, and like the human entities that I care about working on the causes that I care about, right, I care about YC, I care about builders being able to build even in a lot of our internal meetings.

> 我需要每一个瞬间都有价值。而如果你能 token 拉满,就好比你能买下数百万年的意识——机器的意识。这样我就能成为时间亿万富翁了。那不是我自己的时间,而是机器的时间,替我干活,以及我所在意的那些人的时间,投入到我所在意的事业上。对吧,我在意 YC,我在意让建设者们能够去创造——甚至在我们很多内部会议上也是如此。

[39:36] **SPEAKER_00:** Last year, remember, in our offsites, we would talk about like, how do we teach the next generation how to use these tools. And so, you know, I'd like to, I wish that I could say, like, that was all a part of the grand plan. And that's how it started. It's not like, but you know, subconsciously, I actually think it was like, I think subconsciously from doing like cone and like talking about this stuff, like sitting side by side with Boris journey, right here was a very powerful moment for me, because I realized, like, he's he started saying things that like, I could do myself. It's like he said, our team doesn't write a single line of code.

> 记得去年,在我们的团建务虚会上,我们会讨论:怎么教下一代使用这些工具。我真希望能说这一切都是宏大计划的一部分、当初就是这么开始的,但并不是。不过下意识里,我确实觉得——大概是因为做 Light Cone、聊这些东西,就在这里和 Boris 并肩而坐,对我而言是一个非常有力量的时刻,因为我意识到,他开始说的那些事,是我自己也能做到的。比如他说,我们团队一行代码都不写。

[40:12] **SPEAKER_00:** I'm like, Oh, actually, like, I can do that. And like the people who are watching right now, it's like, you and I are not. Yeah. We're all different. Right?

> 我心想,哦,其实,我也能做到这个。而正在看节目的各位——你和我并非……对,我们各不相同,对吧?

[40:19] **SPEAKER_00:** We're the same. Like, we started in the same place. I don't think of myself as like, you know, in the sky yet, even though people seem to talk like I am, you know, like, I'm just a person trying to do a thing. And if I sit next to Boris, I'm like, you know, this guy is one of the best engineers I've ever met. But also, like, if I just open a prompt, we have the same prompt, we have the same MacBook Pro.

> 但我们又是一样的,我们都是从同一个起点出发的。我并不觉得自己已经"高高在上",尽管人们说起我时似乎是那么讲的。我只是一个想把某件事做成的普通人。当我坐在 Boris 旁边时,我会想,这家伙是我见过最优秀的工程师之一。但同时,只要我打开一个提示框——我们用的是同样的提示、同样的 MacBook Pro。

[40:41] **SPEAKER_00:** And, you know, there's nothing that stands between like me or you or any of us from, like, drawing on millions of years, potentially, of like tokens to like serve humanity.

> 而在我、你、或我们任何人,与那可能长达数百万年的 token 之间,已经没有任何东西横亘其中,阻挡我们去调用它、去服务人类。

[40:55] **SPEAKER_01:** Well, Gary, I think that was a beautiful quote that should be retweetable.

> 嗯,Gary,我觉得那是一句很美的话,值得被转发。

[41:00] **SPEAKER_00:** It says, Got to get it on the X right away.

> 它是这么说的——得赶紧把它发到 X 上去。

[41:03] **SPEAKER_01:** You could have infinite time by borrowing the time from the machines.

> 通过向机器借时间,你可以拥有无限的时间。

[41:06] **SPEAKER_03:** Yeah, what a time to be alive. That's a beautiful thought to end on. Thanks Gary for showing us the future. Thanks, guys.

> 对,活在这样的时代真是太好了。用这个美好的想法收尾再合适不过。谢谢 Gary 为我们展示了未来。谢谢大家。

[41:13] **SPEAKER_02:** All right. Thanks for watching. And we'll see you on the next episode of the LiteCone.

> 好了。感谢观看。我们下一期 Light Cone 再见。
