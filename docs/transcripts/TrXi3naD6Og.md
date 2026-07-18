# 全文转录 · 24 岁做出 Cursor:在 GitHub Copilot 阴影下,靠"信念一致性"押注编程的未来

> ▶ [YouTube](https://www.youtube.com/watch?v=TrXi3naD6Og) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/TrXi3naD6Og.md) &nbsp;·&nbsp; Michael Truell: Building Cursor At 23, Taking On GitHub Copilot & Advice To Engineering Students

> 中英对照 · 每段英文原文下附中文翻译

[00:00] **SPEAKER_02:** We realized we were really inherently excited about the future of coding and I think we took a step back and realized that if we were being really consistent with our beliefs there was going to be an opportunity for all of coding to change in the next five years and for all of software development to flow through models. It felt like no one working on the space at the time was really taking that seriously. It felt like they had great products and they were making them a bit better but they weren't really aiming for a world where you know all of coding as we know it today gets automated and building software ends up looking very very different. Then with that in mind we set out to to work on that. Let's start this talk with sort of the

> 我们意识到自己发自内心地对编程的未来感到兴奋。我想我们退后一步、认真审视后发现,如果我们真的忠于自己的信念,那么在接下来的五年里,整个编程领域将迎来彻底变革的机会,所有的软件开发都将通过模型来完成。当时感觉没有一个在这个领域工作的人真正认真对待这件事。感觉他们有很棒的产品,也在把产品做得更好一些,但他们并没有真正瞄准这样一个世界:今天我们所知的整个编程都将被自动化,而构建软件这件事最终会变得非常非常不一样。带着这个想法,我们开始着手去做这件事。让我们从这个话题开始——

[00:38] **SPEAKER_00:** origin story of your journey as a founder. You kind of have to go way back to middle school when you were reading the essays from PJ right? So early on I think you know I had been interested

> 讲讲你作为创业者的起源故事吧。这大概得追溯到你上初中的时候,那时你在读 PJ(Paul Graham)的文章,对吧?

[00:52] **SPEAKER_02:** in starting a company for a long time. I'd been interested in a bunch of a bunch of other things too. I think actually I originally got into programming being interested in in starting something. It was kind of commercial where the first time that I ever saw code it was over some winter break and my brother and I we wanted to create a hit mobile game. We didn't really know how to do that. We looked on Google. How do you create a game? We heard that you need to download this

> 很早的时候,我想我对创办一家公司就已经有了长久的兴趣。我对很多很多别的事情也感兴趣。其实我最初接触编程,正是因为对创办点什么感兴趣。那还带点商业色彩——我第一次看到代码是在某个寒假,我和我哥哥想做一款爆款手机游戏。我们其实完全不知道该怎么做。我们在谷歌上搜:怎么做游戏?我们听说需要下载一个叫

[01:17] **SPEAKER_02:** application called Xcode. We did that and we were hit with these weird colorful esoteric symbols which were Objective-C which you know is still around but maybe a little bit less popular than it was then for good reasons and stared at this kind of impenetrable wall of Objective-C and my brother promptly ejected. Didn't move on with programming. He now is on a very different career path. He's kind of trying to paint or something like that but I yeah kept going and bought a book on Objective-C and then eventually started working on on mobile games. That was the genesis of me getting into programming

> Xcode 的应用程序。我们下载了它,结果迎面而来的是一堆奇怪、花花绿绿、晦涩难懂的符号,那就是 Objective-C——你知道,它现在还在用,但可能没有当年那么流行了,而且是有充分理由的。我盯着这堵仿佛无法逾越的 Objective-C 高墙,我哥哥立刻就"弹射逃生"了,没有继续走编程这条路。他现在走的是一条非常不同的职业道路,好像在尝试画画之类的。但我呢,坚持了下来,买了一本讲 Objective-C 的书,然后最终开始做手机游戏。这就是我踏入编程的起点。

[01:54] **SPEAKER_02:** and then along the way also yes was a big fan of PJ's essays and Sam's essays too also and a bunch of books and stuff. I was also inspired by his essay books. I was a huge fan of his essays and Sam's essays too also and a bunch of books. a bunch of the folks in YC, and that was definitely a big inspiration, even from the very early stages of high school.

> 一路走来,是的,我也是 PJ(Paul Graham)文章的忠实粉丝,还有 Sam(Sam Altman)的文章,以及一堆书之类的。我也从他的文章、书里受到启发。我非常喜欢他的文章,还有 Sam 的文章,以及一堆书,还有 YC 里的一群人——那绝对是一个巨大的激励来源,甚至从我高中最早期的阶段就开始了。

[02:09] **SPEAKER_00:** I think the wildest thing about Cursor is that right now you're just 24 and build this monster of a company in a really short amount of time. To a lot of people it could seem that it's a bit of out of nowhere, but this was really in the making for more than a decade. You've been working and shipping a lot of different projects, right? And you were working in AI even when you were in high school, right? Tell us a bit about the projects and how you got started with that.

> 我觉得 Cursor 最不可思议的一点是,你现在才 24 岁,却在极短的时间里打造出这样一家庞然大物般的公司。对很多人来说,这好像有点凭空冒出来的感觉,但其实它酝酿了十多年。你一直在做、也发布了很多不同的项目,对吧?而且你甚至在高中时就已经在搞 AI 了,对吧?跟我们讲讲那些项目,以及你是怎么起步的。

[02:36] **SPEAKER_02:** Was lucky enough to find programming early on. Was also lucky enough to be interested in AI early on and have some great collaborators to work on AI projects with. Soon after kind of the foray into mobile games, which also turned into, I wasn't very good at mobile games, so one of the things that I built, and actually one of the things that got most popular, which was kind of the technically easiest thing to build, which was maybe a lesson in startups of the code isn't everything, was this mobile game or this mobile app where you could spoof high scores in things like piano tiles and Flappy Bird and then send them to your friends. And that was kind of the thing that went viral. It wasn't the painstakingly handcrafting the game engine yourself type thing.

> 我很幸运,很早就接触到了编程。我也很幸运,很早就对 AI 产生了兴趣,并且有一些很棒的合作者一起做 AI 项目。在初次涉足手机游戏之后不久——这后来也变成了……其实我做手机游戏做得并不好。所以我做的其中一个东西,也是实际上最火的一个,同时又是技术上最容易做的一个(这也许算创业里的一个教训:代码并不是一切)——那是一个手机游戏或者说手机 App,你可以在《钢琴块》(Piano Tiles)、《Flappy Bird》这类游戏里伪造高分,然后发给你的朋友。那个东西一下子就火了,而不是那种你自己费尽心思手工打造游戏引擎的东西。

[03:15] **SPEAKER_02:** But yeah, no, soon after that, got interested with a friend in the idea of building a robotic dog, where we thought it would be really great to have a robot that you could teach to do things without programming it. Instead, you could give it positive and negative feedback, like you give a dog, so you could give it a treat if it does some, quote, treat if it does something good. You could say bad if it does something bad. And then maybe you could teach it to play fashion, things like that. That idea really animated us.

> 但是,没错,那之后不久,我和一个朋友对做一只机器狗的想法产生了兴趣。我们觉得,能有一个机器人,你不用给它编程就能教它做事,那该多棒。取而代之的是,你可以像对待一只狗那样给它正面和负面的反馈——它做得好,你就给它"奖励"(引用一下,给它个"零食奖励");它做得不好,你就说"坏"。然后也许你可以教它玩接飞盘之类的东西。这个想法真的让我们充满了干劲。

[03:40] **SPEAKER_02:** We had no idea how to build it. And so again, started the place where one would start, which is Google, and kind of went down a lot of rabbit holes and took us into a place of learning about genetic algorithms, and maybe that was gonna be helpful for building this robot dog that we wanted to build. And then we eventually learned about this neural network stuff, because some people were playing with taking genetic algorithms and using them to evolve neural networks at the time with work like NEET. And then eventually it took us to RL, reinforcement learning, which was, even back in 2015, people had been working on it for a long time. In the end, my friend and I, we did eventually build a couple of robots.

> 我们完全不知道该怎么做。于是,还是从大家都会起步的地方开始——谷歌——然后一路钻进了各种"兔子洞",把我们带到了学习遗传算法的领域,也许那对我们想做的机器狗会有帮助。接着我们最终了解到了神经网络这些东西,因为当时有些人在玩把遗传算法用来演化神经网络的做法,比如 NEAT 这样的工作。然后它最终把我们引向了强化学习(RL)——即便是在 2015 年,人们研究它也已经有很长时间了。最后,我和我朋友确实做出了几个机器人。

[04:17] **SPEAKER_02:** We didn't do any sort of substantial work that really lasted, but we did work that was interesting at the time in taking reinforcement learning algorithms and making them more data efficient, making them better at learning from very, very few data points, order of tens of data points, and also from noisy data, data that a human's giving. It wasn't exactly a dog, but we built a couple of robots where one of them was this many-axis robot arm that could kind of swing a paddle and play ping pong, and if you put the right sensor on it and then you gave it the right sort of positive and negative feedback, you could teach it to swing when it sees a ball. And then we had this KiwiDrive robot that we would teach to follow a line. To do that, it was actually kind of this great education in ML, partially because of our dumb naivete, where we didn't really know that there were things like Torch and TensorFlow and kind of other, you know, lots of building blocks we could use from. Maybe we weren't good enough at Googling.

> 我们并没有做出什么真正能长久留存的实质性成果,但在当时,我们做的工作是很有意思的:我们把强化学习算法拿来,让它们的数据利用效率更高,让它们更善于从极少的数据点(大约几十个数据点这个量级)中学习,也能从带噪声的数据、也就是人类给出的数据中学习。它并不完全是一只狗,但我们做了几个机器人,其中一个是多轴机械臂,可以挥动球拍打乒乓球——如果你给它装上合适的传感器,再给它恰当的正负反馈,你就能教它在看到球时挥拍。然后我们还有一个 KiwiDrive 机器人,我们会教它沿着一条线走。做这些事,其实是一次很棒的机器学习教育,一部分原因在于我们那种傻乎乎的天真——我们当时根本不知道有 Torch、TensorFlow 这些东西,也不知道有很多现成的构建模块可以用。也许是我们谷歌搜索的水平还不够。

[05:09] **SPEAKER_00:** So you implemented your own neural network from scratch?

> 所以你是从零开始自己实现了一个神经网络?

[05:12] **SPEAKER_02:** Yeah, so-

> 是的,所以——

[05:13] **SPEAKER_00:** When you were like, I don't know, 16, 17?

> 那时你大概,我也说不准,16、17 岁?

[05:16] **SPEAKER_02:** The constraints of the problem were we were dealing with robots, and so we were dealing with microcontrollers. And so microcontrollers have very little memory, and they couldn't really fit any of the normal standard ML libraries. So as part of our bike-shedding, trying to build a robot dog, we implemented our own tiny neural network library. And I have memories of us not really understanding any of the internals of how these things worked, or not really understanding calculus, but kind of fumbling our way through reimplementing some important ideas from neural networks. You know, I think it taught us a lot.

> 这个问题的约束条件是,我们打交道的是机器人,所以我们打交道的是微控制器。而微控制器的内存非常小,根本装不下任何常规的标准机器学习库。所以,作为我们在做机器狗时那种"钻牛角尖式折腾"的一部分,我们自己实现了一个微型神经网络库。我还记得,我们其实完全不理解这些东西内部是怎么运作的,也不太懂微积分,但我们就是磕磕绊绊地重新实现了神经网络里一些重要的思想。你知道吗,我觉得这教会了我们很多东西。

[05:49] **SPEAKER_02:** I think that there were a lot of gaps in the fundamentals that it took many years to fill in later.

> 我觉得在基础知识上有很多缺口,后来花了好多年才把它们补上。

[05:53] **SPEAKER_00:** Then fast forward to the founding of AnySphere. It's an interesting name. Because Cursor is not what it is. When you guys started, you had just graduated MIT, right? That was back in 2022.

> 那我们快进到 AnySphere 的创立。这是个有意思的名字,因为它并不叫 Cursor。你们起步的时候,你刚从 MIT 毕业,对吧?那是在 2022 年。

[06:09] **SPEAKER_00:** What were the first idea that all four of you started working on back in 2022?

> 2022 年,你们四个人最初着手做的第一个点子是什么?

[06:14] **SPEAKER_02:** Yeah, so the genesis of Cursor was in 2021. My co-founders and I, we had been interested in AI for a long time. Each of us kind of had our own little robot dog moment where one of my co-founders, he worked on trying to build a competitor to Google, actually, using LLMs in 2021 and training his own, and training his own contrastive models. One of my co-founders worked on computer vision in academia. And some of us also worked on recommendation systems at companies like Google.

> 是的,Cursor 的起源其实是在 2021 年。我和我的联合创始人们对 AI 感兴趣已经很久了。我们每个人都有过属于自己的"机器狗时刻"——我的一位联合创始人在 2021 年尝试用大语言模型打造一个谷歌的竞争对手,自己训练模型,训练自己的对比学习(contrastive)模型。我的另一位联合创始人在学术界做计算机视觉。我们当中还有一些人在谷歌这样的公司做过推荐系统。

[06:44] **SPEAKER_02:** But we were really interested in AI. In 2021, we were trying to figure out what we'd do with that interest. Do we go and work on AI in academia? Or do we go join a big existing AI effort? Or do we start our own thing?

> 但我们对 AI 是真的很感兴趣。2021 年,我们在琢磨该拿这份兴趣做点什么。我们是去学术界研究 AI?还是去加入某个已有的大型 AI 项目?又或者是自己创业干点什么?

[06:58] **SPEAKER_02:** There were two moments that really got us excited. One was seeing the first AI product start to come out. GitHub Copilot was really the canonical example for us. The other was seeing work about how it looked like AI was going to predictably get better in the future as you scaled up these models. At the very beginning of 2022, me and my co-founders, we went on like a month-long hackathon, basically.

> 有两个瞬间真正让我们兴奋起来。一个是看到第一批 AI 产品开始出现,GitHub Copilot 对我们来说就是最经典的例子。另一个是看到一些研究表明:随着你把这些模型规模扩大,AI 在未来看起来会可预期地变得越来越好。2022 年一开年,我和我的联合创始人们基本上进行了一场长达一个月的黑客马拉松。

[07:18] **SPEAKER_02:** And we started hacking on ideas related to kind of picking an area of knowledge work and building what it looks like as AI gets more and more mature.

> 我们开始围绕这样一个思路来折腾各种点子:挑选某个知识工作领域,然后去构建随着 AI 越来越成熟、这个领域会变成什么样子。

[07:27] **SPEAKER_00:** You guys have collected a lot of data for that. That's your first idea, right?

> 你们为此收集了大量数据。那就是你们的第一个点子,对吧?

[07:30] **SPEAKER_02:** Yeah. So the first real idea that we worked on for a long time was in mechanical engineering. It was trying to build a copilot for mechanical engineers and trying to train models to kind of predict what you would do in a CAD system like SOLIDWORKS or Fusion 360, which is where mechies model out parts in 3D on a computer. We picked it because we thought it would be boring and sleepy and uncompetitive. And we were kind of doing an armchair MBA thing, even though it was a horrible choice from the get-go because none of us were really mechanical engineers, so science wasn't really ready for that area.

> 是的。我们花了很长时间投入的第一个真正的点子是在机械工程领域。我们想为机械工程师打造一个"副驾驶"(copilot),想训练模型来预测你在 SOLIDWORKS 或 Fusion 360 这类 CAD 系统里会做什么——机械工程师就是在这些系统里用计算机以 3D 方式建模零件的。我们之所以选它,是因为我们觉得这个领域会很无聊、很沉寂、竞争不激烈。我们当时有点在纸上谈兵地做"MBA 式的分析",尽管从一开始这就是个糟糕的选择,因为我们当中没有一个人真的是机械工程师,而且当时的技术水平其实也还没准备好去做这个领域。

[08:00] **SPEAKER_00:** But you guys kept working at it for a number of months, right? And you crawled and got all these CAD files and actually got something working with auto-completion, right? That was like the first version of it working?

> 但你们还是坚持做了好几个月,对吧?你们爬取并拿到了所有这些 CAD 文件,而且真的做出了一个能自动补全的东西,对吧?那算是它第一个能跑起来的版本?

[08:12] **SPEAKER_02:** Yes. A bunch of the work was in data scraping, honestly. It was trying to get all the CAD models on the internet. There are also all these different file formats and trying to convert them all into something that's canonical because CAD is this weird software market where there are all these different systems that are pretty popular and it's very fragmented. There are also Cloud CAD systems that don't have easily exportable files, and they don't want you to scrape their stuff.

> 是的。老实说,很大一部分工作都在于数据爬取,也就是尝试把互联网上所有的 CAD 模型都搞到手。同时还有各种各样不同的文件格式,得把它们全部转换成某种标准化的形式,因为 CAD 是个很怪的软件市场——有一堆各不相同、都还挺流行的系统,非常分散。还有一些云端 CAD 系统,它们的文件不太容易导出,而且它们也不希望你去爬取它们的东西。

[08:34] **SPEAKER_02:** And so there was a bunch of work there. Also, the training infrastructure for doing any kind of modeling work back then was pretty rudimentary. And so there was a lot of work on the infra side there and just a lot of experimenting with models and a lot of experimenting with how you even jerry-rig an extension into these CAD systems because we were building an extension. These applications aren't really extensible at all. There were actually also other projects that we were working on at the time.

> 所以那里有一大堆工作要做。另外,当时做任何建模工作的训练基础设施都相当简陋。所以在基础设施这一侧也有很多工作,还有大量对模型的实验,以及大量关于"你到底怎么才能把一个插件硬塞进这些 CAD 系统里"的实验,因为我们做的是一个插件。而这些应用程序其实根本就不太支持扩展。其实当时我们同时还在做另外一些项目。

[08:56] **SPEAKER_02:** So two of my co-founders, they were working on an extension. It was an end-to-end encrypted messaging system because one of them has a background in security research. And the idea there was apps like Signal and WhatsApp, they encrypt the body of the messages, but they don't hide who's talking to who at what time, which is actually really crucial information if you don't want to trust the messaging app provider. So if a journalist is talking to some informant in the government, just knowing that they're communicating at all is actually a really big piece of information.

> 我的两位联合创始人当时在做一个……(严格说是一个系统)——一个端到端加密的通信系统,因为他们其中一位有安全研究的背景。那个想法是:像 Signal 和 WhatsApp 这样的应用会加密消息的正文,但它们并不隐藏"谁在什么时间和谁通话"这个信息,而如果你不想信任通信应用的提供商,这其实是极其关键的信息。所以,如果一名记者正在和政府里的某个线人交谈,仅仅是知道他们之间存在通信这件事,实际上就是一条非常重大的信息。

[09:27] **SPEAKER_00:** So that was in the middle of 2022. So you guys were working for about a good six months on this idea?

> 那是在 2022 年年中。所以你们在这个点子上大概投入了整整六个月?

[09:34] **SPEAKER_02:** Yes.

> 是的。

[09:34] **SPEAKER_00:** And how many users did you get at that point? So you shipped the product.

> 那到那个时候你们获得了多少用户?你们把产品发布出去了。

[09:39] **SPEAKER_02:** All of these projects were ill-fated, and it had basically no users.

> 所有这些项目都命途多舛,它基本上没有用户。

[09:43] **SPEAKER_00:** At what point did you realize that the idea was not working? It's like, oh, no, we're all working on this. We're trying to do a startup. It's not working. And what was that moment like?

> 你是在哪个时刻意识到这个点子行不通的?就是那种"糟了,我们大家都在做这个,我们在努力搞创业,但它不成"的感觉。那个时刻是什么样的?

[09:55] **SPEAKER_02:** I think it was a bit different for each of the projects. I think for the messaging app, it was a bit different. Yeah. Yeah. The messaging system that two of my co-founders worked on, it was really technically impressive, but it had these bad trade-offs where it wasn't very scalable.

> 我觉得每个项目的情况都有点不一样。对通信 App 来说,情况稍有不同。是的,是的。我那两位联合创始人做的那个通信系统,技术上真的很令人惊艳,但它有一些不好的权衡取舍——它的可扩展性不太好。

[10:07] **SPEAKER_02:** And I think they tried to give it to people, and it didn't really work. And then they tried to sell it B2B, and then it didn't really work. And I think it was after a couple of months of trying to get traction. For the CAD ideas, it was, yeah, many months of trying to get the models to really be useful for end users. And then also reckoning around, are we really interested in these areas, or is there something else that we're inherently much more excited about?

> 我记得他们尝试把它推给用户,但没什么效果。然后他们又尝试做 B2B 销售,还是没什么效果。我想那是在努力争取用户增长几个月之后。而对于那些 CAD 的点子,则是花了好几个月试图让模型真正对终端用户有用。同时也在反思:我们是真的对这些领域感兴趣,还是说有别的什么东西是我们发自内心地更为兴奋的?

[10:29] **SPEAKER_00:** So there was a moment that you decided, OK, these ideas are not working. We have to pivot again.

> 所以有那么一个时刻,你们决定:好吧,这些点子行不通,我们又得转型了。

[10:33] **SPEAKER_02:** Yes.

> 是的。

[10:34] **SPEAKER_00:** You churned through three ideas, three, four, five ideas before landing into code completion?

> 在最终落到代码补全上之前,你们已经折腾过三个点子——三个、四个、五个点子?

[10:42] **SPEAKER_02:** Yeah, I think that we had been inspired by tools like Copilot really, really on. And we had avoided working on AI and coding because we thought it was too competitive. Which is crazy. It was competitive then, still is competitive now.

> 是的,我觉得我们很早很早就受到了像 Copilot 这样的工具的启发。而我们之所以一直回避去做 AI 加编程这件事,是因为我们觉得它竞争太激烈了。这想想也挺疯狂的——它当时竞争激烈,现在仍然竞争激烈。

[10:57] **SPEAKER_00:** Because back in 2022. GitHub Copilot was making already about $100 million in revenue?

> 因为早在 2022 年,GitHub Copilot 就已经在创造大约 1 亿美元的收入了?

[11:02] **SPEAKER_02:** I think potentially more, yeah.

> 我觉得可能还不止,是的。

[11:04] **SPEAKER_00:** And you guys were like, oh, we could still do a better job than GitHub Copilot? Because people thought the game was done.

> 而你们却想,哦,我们仍然能做得比 GitHub Copilot 更好?因为大家都觉得这场仗已经打完了。

[11:08] **SPEAKER_02:** It's like, hey, GitHub did it. Well, I mean, we didn't think we could at the start. And then I think it was the desperation of having worked on ideas for a while and not really being excited about them after a while and them not really working out. And that kind of shapes, I think, what you care about and what you're aiming for. And we realized we were really inherently excited about the future of coding.

> 那感觉就像是:嘿,GitHub 都已经做出来了。嗯,我是说,一开始我们并不觉得自己能做到。然后我想,是那种"做了一阵子点子、过了一段时间对它们并不真正兴奋、而且它们也没真正做成"所带来的绝望感。我觉得这种感觉某种程度上塑造了你在乎什么、你在追求什么。而我们意识到,自己发自内心地对编程的未来感到兴奋。

[11:28] **SPEAKER_02:** I think also. We got to see how some of the other people in the space were working on their products. We got to see how the tech was developing. And I think we took a step back and realized that if we were being really consistent with our beliefs, there was going to be an opportunity for all of coding to change in the next five years and for all of software development to flow through models. And it felt like no one working on the space at the time was really taking that seriously.

> 我想还有一点。我们得以看到这个领域里其他一些人是怎么打磨他们的产品的,得以看到技术是怎么演进的。我觉得我们退后一步、认真审视后意识到,如果我们真的忠于自己的信念,那么在接下来的五年里,整个编程领域将迎来彻底变革的机会,所有的软件开发都将通过模型来完成。而当时感觉,没有一个在这个领域工作的人真正认真对待这件事。

[11:52] **SPEAKER_02:** It felt like they had great products, and they were making them a bit better. But they weren't really aiming for a world where all of coding as we know it today gets automated. And building software ends up looking very, very different. Then with that in mind, we set out to work on that.

> 感觉他们有很棒的产品,也在把产品做得更好一些。但他们并没有真正瞄准这样一个世界:今天我们所知的整个编程都将被自动化,而构建软件这件事最终会变得非常非常不一样。带着这个想法,我们开始着手去做这件事。

[12:06] **SPEAKER_00:** That was a bold move, because you said, OK, we're going to stop working on all these other ideas that we didn't have as much of a background. And you were excited about programming, even though you had this big Goliath in the room with GitHub Copilot. You decided to go, and let's just solve this problem.

> 那是个大胆的举动,因为你们说,好,我们不再做那些我们其实并没有那么多背景积累的点子了。而你对编程充满热情,尽管房间里有 GitHub Copilot 这样一个巨人歌利亚。你们还是决定去做,决定就来解决这个问题。

[12:22] **SPEAKER_02:** It didn't really feel bold or like a move at the time, because it's like a bunch of people sitting around in their living room on laptops. It's not like pivoting some giant company. But yeah, no, we did. And initially, we kind of waded into it where we were thinking, well, maybe we do this very niche tool for basically security reviews, trying to detect future CVEs in your code. Or maybe we build something that's just for this one niche area of software.

> 那在当时其实并不觉得大胆,也不像是什么"重大举动",因为无非就是一群人坐在客厅里、抱着笔记本电脑而已。那可不像是要给某个巨型公司做战略转型。但是,没错,我们确实这么做了。一开始,我们是慢慢试探着进入这个领域的,当时我们在想:嗯,也许我们做一个非常细分的工具,基本上是用于安全审查、尝试在你的代码里检测未来可能出现的 CVE(安全漏洞)。或者也许我们做一个只针对软件某一个细分领域的东西。

[12:48] **SPEAKER_02:** We thought about building for quants and actually prototypes and things just for quantitative researchers. But yeah, in doing that, we were just brimming with ideas for what Cursor could be if it were just about trying to be the best way to code with AI in general. And then I think that we had a ton of conviction about that, and we had a ton of excitement about that. And so at some point, we just decided to go for it.

> 我们还想过为量化交易员做点东西,实际上还做了原型,做了些只面向量化研究员的东西。但是,没错,在做这些的过程中,我们对"如果 Cursor 只是致力于成为用 AI 编程的最佳方式,它能变成什么样子"这件事,脑子里满是各种点子。然后我想,我们对这一点有着极强的信念,也有着极大的兴奋感。所以在某个时刻,我们干脆决定放手一搏。

[13:09] **SPEAKER_00:** And that was end of 2022, right, when you decided to make that move? And how quickly did you ship the first product? And what did the first product look like? And that was around, you shipped it a couple of weeks later. And what was that look like?

> 那是在 2022 年年底,对吧,当你们决定做出这个转变的时候?你们多快就发布了第一个产品?第一个产品是什么样子的?那大概是……你们几周后就把它发布了。那是什么样子的?

[13:21] **SPEAKER_02:** It did take us a little bit of time to ship something publicly. It took us roughly, I think, three months from first. It took us a little bit of time to ship the first line of code to open it up and GA it. Originally, what we did is we built our own editor, quote unquote, from scratch. Oh, my god.

> 我们确实花了一点时间才把东西公开发布出来。我想,从最初大约花了三个月。我们花了一点时间——从写下第一行代码,到把它开放出来并正式发布(GA,General Availability)。最初我们做的是,自己"从零开始"打造了一个编辑器(要打引号)。哦,我的天。

[13:38] **SPEAKER_02:** It was still using a bunch of open source building blocks. There are a lot of great primitives like CodeMirror and the language servers, and there's a lot of open source tech that can help you build an editor. But yeah, no, it was cobbled together from scratch, and there was our own version of remote SSH, our own Copilot integration at the time, because we didn't have anything like autocomplete. You have to build your own PIN system. You have to build all your own language server integrations.

> 它仍然用了一堆开源的构建模块。有很多很棒的基础组件,比如 CodeMirror、各种语言服务器(language server),还有很多开源技术能帮你搭一个编辑器。但是,没错,它就是从零开始东拼西凑起来的,当时里面有我们自己版本的远程 SSH、我们自己的 Copilot 集成,因为我们当时并没有类似自动补全那样的东西。你得自己搭一套(PIN)系统,得自己搭好所有的语言服务器集成。

[13:59] **SPEAKER_02:** It ends up going into something as developed as the code editor market, making something that can actually be competitive there and serve as someone's daily driver. But I think it was four weeks until we built something that we could use as our daily driver. It was maybe four weeks later where we gave it to the first beta testers. And then there was another four weeks, and then we GA'd it. And it was still very, very crude at the time.

> 一旦你要进入像代码编辑器市场这样成熟的领域,想做出一个真正能在那里有竞争力、能成为某人日常主力工具的东西(是很不容易的)。但我想,大约花了四周,我们才做出一个我们自己能当日常主力工具来用的东西。大概又过了四周,我们把它交给了第一批 Beta 测试用户。然后又过了四周,我们就正式发布(GA)了它。而在当时,它仍然非常非常粗糙。

[14:19] **SPEAKER_02:** It didn't feel like a big thing to just open it up to the public.

> 就那样把它向公众开放,当时并不觉得是件多大的事。

[14:22] **SPEAKER_00:** What did you learn in that first version? Because you built a code editor from scratch. You guys haven't done the whole forking yet.

> 你们在第一个版本里学到了什么?因为你们是从零开始做了一个代码编辑器,那时你们还没有做后来那套"fork(分叉现有编辑器)"的事情。

[14:29] **SPEAKER_?:** Yeah.

> 对。

[14:29] **SPEAKER_02:** Yeah. We had the fear of God in us. I mean, people hadn't really liked some of the things we had built for a while. So I think that we were kind of all in on it and very focused. But what did we learn from that?

> 是的。我们心里充满了敬畏与紧迫感(直译:我们心中有对上帝的敬畏之惧)。我是说,有很长一段时间,人们其实并不怎么喜欢我们做出来的一些东西。所以我想,我们算是全力以赴、非常专注地投入其中。那我们从中学到了什么呢?

[14:40] **SPEAKER_02:** I think that we learned the first initial set of AI features, where when we started, I think that there was just one key command. And it pulled up this universal remote in the editor. And then you asked it to do something. And then entirely, the AI would just figure out, oh, what exactly do you want it to do? Do you want something back?

> 我想我们摸索出了最初的第一组 AI 功能。刚开始的时候,我记得就只有一个快捷键命令。按下它,编辑器里就会弹出一个"万能遥控器"式的东西。然后你让它去做点什么,接着完全由 AI 自己去弄明白:哦,你到底想让它做什么?你想要一个返回结果吗?

[14:59] **SPEAKER_02:** That's like a chat response? Or do you want a code suggestion that you can then take? Or do you want it to go search around your code base and answer a question? Or do you want it to go spin for a really long time or a short time? And there wasn't a lot of control.

> 是像一段聊天式的回复那样?还是你想要一个可以直接采纳的代码建议?又或者你想让它在你的代码库里到处搜索、回答一个问题?再或者你想让它运转很长时间,还是很短时间?当时可供用户掌控的东西并不多。

[15:10] **SPEAKER_02:** And I think that we learned, given the tech of the time at the end of 2022, that the form factor has to look a bit different. And so we learned the first early AI features that then became part of the core of Cursor from iterating both for ourselves and also giving it to people. I think another thing we learned was we were very rapidly building a feature-complete version of what we want in a normal code editor, plus then some AI stuff that we thought was great. But then a feature-complete code editor for the world is going to be a way, way, way longer road. We thought that Fiescode had been developed over the course of 12 years, was one of the earliest TypeScript projects, had lots of people on it.

> 我想我们学到的是,鉴于 2022 年底当时的技术水平,产品的形态必须得有所不同。于是,我们通过既给自己用、也把它交给别人用的不断迭代,摸索出了最初那批早期 AI 功能,而这些功能后来成了 Cursor 的核心组成部分。我想我们学到的另一件事是,我们非常快速地做出了一个功能完备的、我们心目中普通代码编辑器该有的版本,再加上一些我们自认为很棒的 AI 东西。但要做出一个面向全世界、真正功能完备的代码编辑器,那将是一条长得多、长得多、长得多的路。我们知道 VS Code 是历经 12 年开发出来的,是最早的一批 TypeScript 项目之一,投入了很多人。

[15:48] **SPEAKER_02:** We thought, oh, yeah, of course, you can kind of spin something up that's just equivalent for the world in a few months. And I think that we learned very rapidly that that wasn't the reality, and our time was going to be best spent just focused on the AI stuff. And so similar to how browsers often base themselves off of Chromium's rendering engine, we then switched to being based off of VS Code.

> 我们当时想,哦,当然啦,你花几个月就能鼓捣出一个功能上和它对全世界而言等价的东西。而我想我们很快就明白,现实并非如此,我们的时间最好还是专注在 AI 这些东西上。于是,就类似于浏览器常常以 Chromium 的渲染引擎为基础那样,我们随后转为基于 VS Code 来构建。

[16:06] **SPEAKER_00:** The other thing is you guys had also implemented your own models too. Back then, you got a lot of inspiration from Codex, right?

> 另一件事是,你们当时其实也自己实现了自己的模型。那时候,你们从 Codex 那里得到了很多灵感,对吧?

[16:15] **SPEAKER_02:** Yes. So when we were setting out to work on our first idea that we really spent a bunch of time on, which was trying to help mechanical engineers be more productive using AI, one of the things when we raised our first round of funding, because we actually kind of needed money from the get-go to do a little bit of model training, because you couldn't bootstrap it with the models that existed off the shelf. They weren't good enough at that task. One of the papers that we would tout around is actually the original Codex paper, because by our calculations, Codex, which was the first, this was the first autocomplete model behind GitHub Copilot, it didn't really cost that much money to train, even though even back then, at kind of the beginning and middle of 2022, people were talking about how expensive AI models were to train. I think it cost, my math might be wrong, but I think it was about $100K in training costs.

> 是的。当我们着手做我们真正花了大量时间的第一个点子——也就是尝试用 AI 帮助机械工程师提高生产力——的时候,有件事是,我们募集了第一轮融资,因为我们其实从一开始就有点需要钱来做一些模型训练,因为你没法用市面上现成的模型把它给"引导起来",那些模型在那个任务上还不够好。我们当时到处拿出来"炫耀"的其中一篇论文,其实就是最初的 Codex 论文,因为按我们的估算,Codex——它是 GitHub Copilot 背后的第一个自动补全模型——训练起来其实并没有花那么多钱,尽管即便在那时候,也就是 2022 年年初到年中,人们都在谈论训练 AI 模型有多么昂贵。我想它花了……我的算术可能不对,但我想训练成本大约是 10 万美元。

[16:58] **SPEAKER_02:** And then, you know, during this foray into mechanical engineering, we had done our own training. And then when we set off on Cursor, I think we were a little bit burned by that. And so we wanted to be as pragmatic as possible, not reinvent the wheel. And so we started by doing none of that. And then over the course of 2023, you know, in dialing in the product, that ended up being a really important product lever, especially as we got to scale and we got a bunch of people using the product.

> 然后,你知道,在我们涉足机械工程这段时间里,我们自己做过训练。而当我们启程去做 Cursor 的时候,我想我们多少被那段经历"烫伤"过。所以我们想尽可能务实,不去重复造轮子。于是一开始,我们完全不碰这些。而在 2023 年这一整年里,你知道,随着我们不断打磨产品,那(自研模型)最终成了一个非常重要的产品杠杆,尤其是当我们规模上去、有一大批人在用这个产品之后。

[17:21] **SPEAKER_02:** And then that also gives you the ability to use product data to make the product better. And so that actually has been a really important muscle to build in the company.

> 而这也让你有能力用产品数据来把产品做得更好。所以,这其实是公司里非常重要的一块要练就的"肌肉"。

[17:28] **SPEAKER_01:** YC's next batch is now taking applications. Got a startup in you? Apply at ycombinator.com slash apply. It's never too early, and filling out the app will level up your idea.

> YC 的下一期正在接受申请。你心里有个创业的念头吗?去 ycombinator.com/apply 申请吧。永远不嫌太早,而且填写申请表本身就会让你的点子更上一层楼。

[17:40] **SPEAKER_01:** Okay, back to the video.

> 好,让我们回到视频。

[17:42] **SPEAKER_00:** What happened then in 2023 was when you were still not sure about whether Cursor was going to be a thing, right? You were still debating with your co-founders whether you should still pivot. It's like, oh, is this idea still going to work? And you're still trying to grow it, right? Because it took a long time.

> 那么 2023 年发生的情况是,你当时其实还不确定 Cursor 到底能不能成,对吧?你还在和你的联合创始人们争论,要不要还是再转型一次。就是那种"哦,这个点子到底行不行"的感觉。而你们仍在努力让它增长,对吧?因为这花了很长时间。

[17:58] **SPEAKER_00:** It took a long time to get to revenue, right?

> 花了很长时间才做出收入,对吧?

[18:01] **SPEAKER_02:** Yeah, I think that over 2023, it was growing. The numbers were kind of small. And I think that also we were working on something where there wasn't always a clear next step. I think that there are probably some markets where you're really well served by going and immediately talking to a bunch of people, listing down their problems really rigorously, or really kind of systematically and exhaustively thinking through each problem, what would kind of be the direct solution, and then prioritizing them and then going from there. But I think that we were and are in a space that's a bit different than that.

> 是的,我想在 2023 年这一整年,它是在增长的,只是数字有点小。而且我觉得,我们做的这件事,并不总有一个清晰的下一步。我认为,在某些市场里,你可能非常适合直接去找一大堆人聊,把他们的问题非常严谨地列出来,或者非常系统、非常彻底地把每一个问题都想清楚,想出直接的解决方案是什么,然后给它们排优先级,再从那里往下走。但我想,我们过去和现在所处的领域,和那种情况有点不一样。

[18:35] **SPEAKER_02:** You know, we're this end user application that doesn't have much of a complexity budget. We are trying to build the best way to code with AI. And so a lot of that is figuring out, you know, given the tools that you have today, what can you actually do? There's a lot of things that you could write down that would be useful if you could build them, but then, you know, figuring out how to build them and all the details, it's not entirely clear how to move forward on that. And so, yeah, there were a lot of times over the course of 2023.

> 你知道,我们是这样一个面向终端用户的应用,它没有多少"复杂度预算"。我们想打造用 AI 编程的最佳方式。所以很大一部分工作在于弄清楚:在你今天所拥有的工具条件下,你实际上能做到什么?有很多东西你可以写下来,它们如果你能做出来会很有用,但接着,你知道,搞清楚怎么把它们做出来、以及所有的细节,该如何往前推进并不完全明朗。所以,是的,2023 年这一整年里有很多这样的时候。

[19:00] **SPEAKER_02:** And then, you know, actually also to add to this, of our early user base, if you just kind of followed the gradient of exactly what they wanted, you would get pulled in slightly different directions than we ended up in. You know, we had a really loud segment of users that didn't know how to code at all. And we talked about, you know, should we focus on those folks? We had a really loud segment of users that wanted us to do things that were very tech stack specific, you know, just building for one technology and making it much less of a horizontal tool. And we resisted doing that too.

> 然后,你知道,其实还要补充一点:对于我们的早期用户群,如果你只是顺着他们究竟想要什么的"梯度"走,你会被拉向和我们最终所处方向略有不同的地方。你知道,我们有一群声音非常大的用户,他们根本完全不会写代码。我们讨论过,你知道,我们该不该专注于服务这批人?我们还有一群声音非常大的用户,他们希望我们去做一些非常绑定特定技术栈的东西,你知道,就是只为某一种技术打造,把它变成一个远没那么"横向通用"的工具。而我们也顶住了压力,没有那么做。

[19:29] **SPEAKER_02:** So there was a lot of early prototyping and kind of wandering the desert in 2023, and then, you know, figuring out things around, you know, where does it make sense to not just build the software, but also build our own models to improve the API models or to replace them in places, like, you know, for instance, with our tab, you know, our next edit prediction, and then how exactly to do that.

> 所以在 2023 年,有大量的早期原型开发,以及某种"在沙漠里游荡摸索"的过程,然后,你知道,去搞清楚一些事情,比如:在哪些地方,我们不仅要构建软件,还值得去构建我们自己的模型,来改进那些 API 模型,或者在某些地方替代它们——比如,你知道,拿我们的 Tab 功能来说,也就是我们的"下一处编辑预测"(next edit prediction),以及到底该怎么去实现它。

[19:49] **SPEAKER_00:** You went from zero to 1 million around 2023, right? And it took a lot to get there, right?

> 你们大约在 2023 年从 0 做到了 100 万,对吧?而走到那一步费了很大功夫,对吧?

[19:56] **SPEAKER_02:** Yeah, it was a bit more than that, but sort of roughly that.

> 是的,比那还多一点,但大致就是那样。

[19:59] **SPEAKER_00:** Yeah. And then 2024 was a crazy year. You guys went from one to 100 million in one year. Tell us about this loss of compounding power, because you kept that growing 10% week over week. How did that happen?

> 是的。然后 2024 年是疯狂的一年,你们在一年之内从 100 万做到了 1 亿。跟我们讲讲这种复利式增长的力量吧,因为你们保持着每周 10% 的增长。这是怎么发生的?

[20:14] **SPEAKER_02:** So the numbers felt small early on, then the compounding kind of kept going. I think that there were a couple of things that really drove our growth. We're in this market where if you make the product better, you kind of see it in the numbers immediately, where, you know, things start to grow more, and so we felt it around, you know, when we first started to make Cursor Codebase aware, when we first started to, you know, be able to predict your next action, when we made that then more accurate, then when we made that faster, then when we made that more ambitious, you know, it could predict sequences of changes, and then when we let the AI model start to take more action within your codebase, and then do that really fast, you know, speeding that up. And so all along the way, you know, we kind of just focused on making the product better. The compounding continued.

> 一开始那些数字让人觉得很小,然后这种复利式增长就一直持续了下去。我认为有几件事真正推动了我们的增长。我们所处的这个市场,是那种如果你把产品做得更好,你几乎会立刻在数据上看到反馈——你知道,各项指标开始增长得更快。所以我们能感受到它,比如,你知道,当我们最初开始让 Cursor 理解整个代码库(codebase-aware)的时候,当我们最初开始能够预测你的下一步操作的时候,然后当我们把这个预测做得更准确的时候,再然后当我们把它做得更快的时候,再当我们把它做得更有"野心"的时候——你知道,它能预测一连串的修改;然后当我们让 AI 模型开始在你的代码库里采取更多操作、并且把这件事做得非常快、加速这个过程的时候。所以一路走来,你知道,我们基本上就是专注于把产品做得更好,复利式增长也就一直延续了下去。

[20:59] **SPEAKER_02:** And I don't think that this is true of all markets, but I think we're in a market where end user preferences matter a lot. And if you make the best thing, people hear about it and talk about it. And that kept going for a long time.

> 我并不认为这对所有市场都成立,但我觉得我们所在的市场里,终端用户的偏好非常重要。如果你做出最好的东西,人们就会听说它、谈论它。而这种情况持续了很长时间。

[21:11] **SPEAKER_00:** I think one of the funny things that a lot of that's happened around that time, we did see a big shift in the YC companies as they were going through the batch. Because we would ask, what kind of tech stack do you use to build your applications? And it was night and day from one batch to the other. I remember in 2023, I think it was maybe single-digit percentage of the batch we used Cursor. Then 2024, it was like 80%.

> 我觉得那段时间发生的一件有趣的事情是,我们确实在正在经历这一期的 YC 公司身上看到了一个巨大的转变。因为我们会问:你们用什么样的技术栈来构建你们的应用?结果从一期到下一期,简直是天壤之别。我记得在 2023 年,我想大概只有个位数百分比的公司在用 Cursor;然后到了 2024 年,大约就有 80% 了。

[21:37] **SPEAKER_00:** It's just like spread, like wildfires, like the best builders were using you.

> 它就那样传播开来,像野火一样,最优秀的那些开发者都在用你们的产品。

[21:40] **SPEAKER_02:** CHRISTIAAN BRINKHOFF- We got onto their Twitter feed, yeah.

> 我们进入了他们的 Twitter 信息流,是的。

[21:42] **SPEAKER_00:** AMANDA SCHADE- It was a Twitter feed. Is that where a lot of adoption, how did all the growth came from?

> 是通过 Twitter 信息流。那是不是很多用户采用的来源?所有这些增长到底是从哪儿来的?

[21:48] **SPEAKER_02:** CHRISTIAAN BRINKHOFF- So the very early stages, when we were first launching the editor, we tried to kind of evangelize it on social networks. And actually, one of my co-founders when kind of the dopamine hit keeping him going in 2022 when we were working on some of these ill-fated ideas, he started posting on the internet and kind of explicitly set out to gain a lot of followers, not by doing kind of normal social media things, but by talking about AI, actually. It was kind of surprising the degree to which someone could actually just read kind of all the papers, think kind of deeply about what was going on at the time, talk about that publicly, and then get recognized by influential people in the space. And so there was like this particular open source model, Flan T5 at the time, that multiple AI efforts that ended up using that model, they found out about kind of the benefits of that model directly from my co-founder, just because he was posting on Twitter and doing that kind of consistently. But he became like sort of niche, very niche, like sort of niche, niche, niche of SF, micro-celebrity.

> 在非常早期的阶段,当我们第一次发布这个编辑器的时候,我们尝试在社交网络上为它做某种"布道"式的推广。而实际上,在 2022 年我们做那些命途多舛的点子时,支撑着我的一位联合创始人坚持下去的那种"多巴胺快感"——他开始在网上发帖,并且相当明确地立志要收获大量粉丝,方法不是去做那些常规的社交媒体操作,而是其实是通过谈论 AI。有一点挺出人意料的:一个人竟然真的能够仅仅通过读遍几乎所有论文、对当时正在发生的事情进行相当深入的思考、把这些公开讲出来,就能得到这个领域里有影响力的人的认可。所以,当时有这么一个特定的开源模型,叫 Flan-T5,有好几个 AI 项目最终用上了这个模型,而他们正是直接从我的联合创始人那里了解到这个模型的好处的,原因无非就是他一直在 Twitter 上发帖、并且很有恒心地这么做。但他变成了那种很小众、非常小众的……那种旧金山圈子里小众、小众、再小众的微型名人。

[22:54] **SPEAKER_02:** He would actually kind of evangelize the product early on. And so we had this kind of very movie magic, demo when we first launched and when we first did a wait list to just get our initial batch of users. I think that that was helpful, getting us kick-started. But then after that, we kind of stepped away from that. And we kind of lived like monks in 2023 and just focused on the product.

> 早期他其实就是这样为产品做布道式推广的。所以当我们第一次发布、第一次开放候补名单(wait list)来获取最初那批用户的时候,我们有过那种非常有"电影魔法"感的演示。我想那对我们很有帮助,让我们启动了起来。但在那之后,我们某种程度上就从那种方式抽身而退了。2023 年我们过得有点像修道士,只专注于打磨产品。

[23:14] **SPEAKER_02:** And it really just spread from word of mouth. I remember there were a couple of times during that year where there were members of the team that would say things like, guys, the product's already good enough. Like, let's put it aside. Let's just focus on growth engineering. And then the next day, we were like, oh, we're going to do this.

> 而它真的就完全是靠口口相传传播开来的。我记得那一年有那么几次,团队里有成员会说这样的话:各位,产品已经够好了,咱们就先把它放一边吧,咱们专注去做增长工程(growth engineering)。然后第二天,我们又想,哦,我们要做这个。

[23:28] **SPEAKER_02:** We're going to do this. We're going to do this. We're going to do this. We're going to do this. And then there would be like a two-month sprint on doing some version of that.

> 我们要做这个,我们要做这个,我们要做这个,我们要做这个。然后就会有大约两个月的冲刺,去把那件事的某个版本做出来。

[23:34] **SPEAKER_02:** And it just never kind of washed away compared to the other stuff that we worked on that year.

> 而相比我们那一年做的其他东西,它(把产品做得更好这件事)始终没有被冲淡、没有被搁置。

[23:38] **SPEAKER_00:** And by that time in 2024, how big was Kirchner? How big was the company at that point?

> 那么到 2024 年那个时候,Cursor 有多大了?公司在那个时点有多大规模?

[23:45] **SPEAKER_02:** It was pretty small in 2023, where my co-founders are fantastic engineers, and there were four of us. And so we could go pretty far without hiring anyone. We also had our own set of missteps in figuring out, like, what are we going to do about the first set of people to hire and how exactly to do that? And so we were both very patient early on and also focused on hiring a lot less than we probably should have early on. I think we ended 2023 at only single digits, people.

> 2023 年时公司还相当小,我的联合创始人们都是了不起的工程师,我们一共四个人。所以在不招任何人的情况下,我们也能走得挺远。在弄清楚"第一批要招什么样的人、以及到底该怎么招"这件事上,我们也犯过自己的一系列失误。所以早期我们既非常有耐心,同时招人的数量也远远少于我们本来大概应该招的。我想我们 2023 年结束时,团队人数还只是个位数。

[24:19] **SPEAKER_02:** Like, we were less than 10 still. Yeah.

> 就是说,我们那时还不到 10 个人。是的。

[24:21] **SPEAKER_00:** Amazing. Now, I guess I'm curious, now shifting gears a little bit about what are your thoughts in terms of how the future is going to look with that?

> 太惊人了。那么,我想我有点好奇,现在稍微换个话题:关于未来会因此变成什么样子,你有什么看法?

[24:29] **SPEAKER_02:** What are your thoughts on coding? We were kind of this maybe middle road bet from the start, where when we set out to work on the company and we were hiring our first people, we would get these weird looks around, why are you? I mean, at the end of 2022, it wasn't really like this, right? Because kind of chat GPT happened, and then the whole world woke up to things in the beginning of 2023. But especially during 2022, when we were working on the CAD stuff and then the early code stuff, people thought working on AI, it was kind of weird to do.

> 你对编程有什么看法?我们从一开始大概算是押注在一条"中间路线"上。当我们着手创办这家公司、并在招募最初几名员工时,我们会收到那种奇怪的目光,人家会想:你们为什么要……?我是说,2022 年底其实还不是这样,对吧?因为 ChatGPT 差不多就是那时候出现的,然后到 2023 年年初,全世界一下子都醒悟过来了。但尤其是在 2022 年那段时间,当我们在做 CAD 相关的东西、以及后来早期的代码相关的东西时,人们觉得去搞 AI 这件事有点怪。

[24:58] **SPEAKER_02:** I was not entirely convinced that it was a good use of time and that there were going to be lots of great applications to fall out of AI. And then even the people who are interested in AI, there was, in our space, a bunch of people that were just focused on optimizing kind of the form factor that exists already and just making those products a little bit better. And then at the same time, in our social circles and professional circles, there's a bunch of people that were thinking, oh, why would you work on anything other than AGI? And all of the work that you're doing right now, in one or two years, circa 2022, is going to go away. And yeah, I think that we've always had this view that there's going to be lots and lots of incredibly valuable things to build over the next couple of decades.

> (当时很多人)并不完全相信这是对时间的一种好的利用,也不相信 AI 会催生出大量了不起的应用。然后,即便是那些对 AI 感兴趣的人——在我们这个领域里,有一批人只专注于优化那种已经存在的产品形态,只是把那些产品做得稍微好一点。与此同时,在我们的社交圈和职业圈里,又有一批人在想,哦,除了 AGI(通用人工智能),你为什么还要去做别的任何东西?你现在正在做的所有这些工作,在一两年内(大约 2022 年时的说法)都会烟消云散。而,是的,我想我们一直抱有这样一种看法:在接下来的几十年里,会有非常非常多极其有价值的东西值得去构建。

[25:43] **SPEAKER_02:** AI is going to be this transformative technology, maybe more so than any technological revolution in recent centuries. But it's going to take a couple of decades, and it's going to be this industry-wide effort where there are all of these independent capabilities that each need to fall out to really get to a place where you can entirely get to the end state of transforming building software on computers or kind of the other areas of knowledge work that might be transformed by AI. And yeah, I think concretely kind of in the near term, we think that for professional engineers, which is the end user we serve, the market that we serve, code is still really important. And there will be this long, messy middle where you will be working with the AI. More and more, it will become like a colleague.

> AI 将会是一项变革性的技术,也许比近几个世纪以来任何一次技术革命都更具变革性。但它将需要几十年的时间,而且它将是一场覆盖整个行业的努力——需要所有这些相互独立的能力各自逐一实现,才能真正走到那个终点状态:彻底改变在计算机上构建软件的方式,或者被 AI 变革的其他知识工作领域。而,是的,我想具体到近期,我们认为对于专业工程师——也就是我们所服务的终端用户、我们所服务的市场——来说,代码仍然非常重要。而且会有一段漫长而混乱的"中间地带",在那里你将与 AI 一起工作。它会越来越像一位同事。

[26:25] **SPEAKER_02:** More and more, it may also become like a very advanced compiler. That can start to hide some of the code for you. You're going to have to read the logic and review it and edit it.

> 越来越多地,它也可能变得像一个非常高级的编译器,可以开始替你把一部分代码隐藏起来。你将不得不去读懂其中的逻辑、审查它、编辑它。

[26:37] **SPEAKER_00:** So what do you think are the skills that are still going to matter? What should everyone still be studying or stop studying?

> 那么你认为哪些技能仍然会重要?大家应该继续学习什么,又该停止学习什么?

[26:42] **SPEAKER_02:** I mean, I think that programming like math is kind of just a good general education. I don't think that that goes away. And I think that there's also lots of practical skills that comes from studying computer science right now. I mean, often when people are kind of entering dynamic industries, the specific stuff that they, Yeah. they study in school isn't super crucial.

> 我是说,我觉得编程就像数学一样,本身就是一种很好的通识教育。我不认为这会消失。而且我觉得,现在学习计算机科学也会带来很多实用技能。我是说,人们在进入那些快速变化的行业时,他们在学校里学的那些具体的东西,往往并没有那么关键。

[27:02] **SPEAKER_02:** It's more the kind of learning that they get along the way. And I don't think that's changed with AI.

> 更重要的是他们在这一路上所获得的那种学习能力。而我不认为这一点因为 AI 而有所改变。

[27:05] **SPEAKER_00:** What advice do you have for the audience if you have like a young Michael Truel? Maybe not just three years ago. If they want to be like you three years ago before they start Cursor, what should they be doing right now?

> 如果观众里有一个年轻版的 Michael Truell(你),你会给他什么建议?也许不只是三年前的你。如果他们想成为三年前、在创办 Cursor 之前的你那样的人,他们现在应该做些什么?

[27:19] **SPEAKER_02:** I think just working on things that you're interested in and doing it with people both that you enjoy being around, but that you respect a ton, and taking that really seriously. Yeah, I think that for a lot of people that are in school, there's so many things that pulls you toward more checking boxes and less focusing on building something up over time and really focusing on something that you're interested in.

> 我觉得就是去做你真正感兴趣的事情,并且和那些既让你乐于相处、又让你无比敬重的人一起去做,而且要非常认真地对待这件事。是的,我觉得对很多还在上学的人来说,有太多东西会把你拉向"多打勾完成任务"的方向,而不是让你专注于日积月累地把某样东西建立起来、真正专注于你所感兴趣的事情。

[27:48] **SPEAKER_00:** All right, let's give it a round of applause to Michael. Thank you so much. Yeah, of course.

> 好,让我们把掌声送给 Michael。非常感谢你。嗯,当然。

[27:54] **SPEAKER_02:** Thank you for having me.

> 谢谢你们邀请我。

[27:55] **SPEAKER_?:** Yeah.

> 好的。
