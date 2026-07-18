# 全文转录 · 点阵图:真正看清用户在做什么

> ▶ [YouTube](https://www.youtube.com/watch?v=e5-6rEwzxLs) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/e5-6rEwzxLs.md) &nbsp;·&nbsp; Dot Plots: How to Actually See What Your Users Are Doing

> 中英对照 · 每段英文原文下附中文翻译

[00:08] **SPEAKER_01:** One of the biggest mistakes I see founders make is relying on aggregate user metrics instead of understanding how any individual users use their product. In my last video, I talked about cohort retention curves and how you can use those to separate groups of users and track what they do over time throughout using your product. And I think that's the best tool that you've got to figure out if people keep using your product. But what you don't know is how are they using your product?

> 我看到创始人犯的最大错误之一,就是依赖聚合的用户指标,而不去理解具体某个用户是如何使用他们产品的。在我上一个视频里,我讲过分组留存曲线(cohort retention curves),以及如何用它把用户分成不同的群体,追踪他们在使用产品的过程中随时间的行为变化。我认为这是判断人们是否会持续使用你产品的最佳工具。但你不知道的是:他们到底是怎么使用你的产品的?

[00:35] **SPEAKER_01:** How are they interacting? What features are they using? What's the frequency of use? What's the pacing of how they use the product?

> 他们是如何与产品互动的?他们在用哪些功能?使用频率是多少?他们使用产品的节奏又是怎样的?

[00:41] **SPEAKER_01:** And most founders just like ignore this. But I think it's the most important signal to figure out if you've built something that people want. So you want to be able to look at what individual users are doing. But that's a lot, right?

> 而大多数创始人基本上都忽略了这一点。但我认为,这是判断你是否做出了人们真正想要的东西的最重要信号。所以你需要能够观察每个用户具体在做什么。但这信息量很大,对吧?

[00:52] **SPEAKER_01:** If you even have like 10 or 20 users, it's pretty challenging to just tail the logs and watch every event that every user is doing. So with aggregate data, the graphs that we're all used to talking about, things like DAUs or MAUs, these long...

> 哪怕你只有10个或20个用户,想要单纯地盯着日志、观察每个用户的每一个行为事件,也是相当困难的。所以人们才会用聚合数据,也就是我们都习惯谈论的那些图表,比如日活(DAU)、月活(MAU)这些……

[01:08] **SPEAKER_01:** You can't lump all of your users together and you can't really get a sense of what any individual user is doing. And if you have any amount of growth, those graphs tend to be going up and to the right, even if users aren't actually enjoying using your product. So today I want to tell you about a tool that we came to in my startup that allows you to understand what's going on with individual users while also giving you a big picture view of how your entire product is performing. And we call it the dot plot.

> 你不能把所有用户一股脑地混在一起,那样你就无法真正了解任何一个具体用户在做什么。而且只要你有一点点增长,那些图表往往就会一路向右上方攀升,哪怕用户其实并不喜欢用你的产品。所以今天我想给你介绍一个我们在创业公司里摸索出来的工具,它能让你既了解每个用户身上发生了什么,又能给你一个关于整个产品表现的全局视角。我们把它叫做点阵图(dot plot)。

[01:37] **SPEAKER_01:** So let me show you what a dot plot looks like. Based on the name, you can figure out it probably involves dots. What you basically do is just make a two-dimensional grid, like a spreadsheet, where there are a bunch of columns and a bunch of rows. Each row represents one individual user.

> 那么让我给你展示一下点阵图长什么样。从这个名字你就能猜到,它大概跟"点"有关。你要做的基本上就是画一个二维网格,像电子表格一样,有一堆列和一堆行。每一行代表一个具体的用户。

[01:52] **SPEAKER_01:** If I'm one of the users, I'll write my name here, Dave. I'm one of the users. And every other user of your product gets their own row. And then every column represents a time period.

> 如果我是其中一个用户,我就在这里写上我的名字,Dave。我是其中一个用户。你产品的其他每一个用户也都各自占一行。然后每一列代表一个时间段。

[02:05] **SPEAKER_01:** I think days are usually the right thing to use for your product, but it probably depends a bit on the nature of your product. But it probably depends a bit on the nature of your product. But it probably depends a bit on the nature of your product. So let's just draw in the days.

> 我认为对大多数产品来说,用"天"作为单位通常是合适的,不过这可能也取决于你产品的具体性质。这可能取决于你产品的性质。这取决于你产品的性质。那我们就先把这些天数画上去。

[02:13] **SPEAKER_01:** I'll just do Monday, Tuesday, Wednesday, Thursday, Friday. And you can make this as big or as small as you want. For the sake of this example, I'll just do like a week or two of days, just to show you what's going on here. And then the idea, it's called a dot plot, is you put some dots in each of the cells.

> 我就画周一、周二、周三、周四、周五。你可以把这个网格做得任意大或任意小。为了举例方便,我就画一两周的天数,给你演示一下这里的原理。然后核心思路——它之所以叫点阵图——就是你要在每个格子里放一些点。

[02:32] **SPEAKER_01:** You want to pick an event that your user does in the process of using your product that you think represents value in the product. It's sharing a photo if you're building a photo app, or listening to a song if you're building a music app, or processing an invoice if you're building a B2B invoice processing product. And you can just put a dot for each day that each user uses the product. Let's say we're Spotify and we're building a music streaming app, and we wanna see how our users are using it.

> 你要挑选一个用户在使用你产品的过程中会做的、你认为能代表产品价值的行为事件。如果你在做照片应用,那就是分享照片;如果你在做音乐应用,那就是听一首歌;如果你在做一个B2B的发票处理产品,那就是处理一张发票。然后你就可以在每个用户使用产品的每一天上打一个点。比如说我们是Spotify,在做一个音乐流媒体应用,我们想看看用户是怎么用它的。

[02:59] **SPEAKER_01:** Let's pick the event that we're gonna chart here being listen to a song. So anytime a user listened to a song during a day, we're gonna put a dot. So for me, let's say I listened to Spotify song on Monday and Tuesday and not on Wednesday, but Thursday and Friday again, and then maybe again on Monday and Wednesday. Another thing you can do to make a record of the first day that a user used the product, the day that they onboarded, you can put another symbol, like let's say on a user's first day, we'll just draw a little ring around the dot like that, just to give us a little bit more signal.

> 我们就把要在这里标记的事件定为"听一首歌"。所以只要用户在某一天听了一首歌,我们就打一个点。以我为例,假设我在周一和周二听了Spotify的歌,周三没听,周四和周五又听了,然后可能下一个周一和周三又听了。你还可以做的另一件事是记录用户第一次使用产品的那天,也就是他们完成注册引导的那天,你可以用另一个符号来标记。比如说,在用户使用的第一天,我们就在那个点周围画一个小圈,像这样,给我们多一点信息。

[03:34] **SPEAKER_01:** And what you'll eventually start seeing is a pretty high density visualization of individual users and their usage over time. What's really cool about this is it lets you figure out patterns that you probably would not have seen with your human brain, just looking at aggregate charts or looking at individual user logs. Okay, so let's look at this example I've just drawn. For our Spotify app, what do we see?

> 你最终会看到的,是一个关于单个用户及其使用行为随时间变化的、信息密度相当高的可视化图。它真正妙的地方在于,它能让你发现一些用你的人脑本来根本看不出来的模式——无论你是只看聚合图表,还是只看单个用户的日志,都发现不了这些模式。好,那我们来看看我刚画的这个例子。对于我们的Spotify应用,我们看到了什么?

[04:05] **SPEAKER_01:** What patterns have emerged now that we can see individual users and their own behavior? Well, one thing I see is it seems like there's a set of people who use the product on weekdays, right? We've got myself, we've got user number three here, user four used it on a Monday, user six used it during the week. And there's a couple of users who seem to kind of only use it on the weekends.

> 现在我们能看到单个用户及其各自的行为了,那浮现出了哪些模式呢?嗯,我注意到的一点是:似乎有一批人是在工作日使用这个产品的,对吧?有我自己,有这里的三号用户,四号用户在周一用过,六号用户在工作日里用过。而还有几个用户似乎基本上只在周末使用。

[04:26] **SPEAKER_01:** That's an interesting observation that might help me redesign my product in a different way or target different users, maybe understand which users are the most valuable ones to me. Do I want the weekday workday? Do I want the worktime listeners? Or do I want the weekend users?

> 这是一个很有意思的观察,它可能会帮助我以不同的方式重新设计产品,或者去瞄准不同的用户群,也许还能让我明白哪些用户对我来说是最有价值的。我想要的是工作日、上班时段的用户吗?我想要的是在工作时间听歌的人吗?还是说我想要的是周末用户?

[04:40] **SPEAKER_01:** We would have no idea about this if we didn't have a dot plot visualization like this. Another thing I can see is a measure of retention. Like, do we see a lot of users like user four that try the app on one day and then never come back? If we see that on a bunch of our rows, we have an idea of a potential problem that we've got in our onboarding or other things.

> 如果没有这样一张点阵图可视化,我们对这些情况会一无所知。我还能看到的另一件事是留存情况的度量。比如说,我们是不是看到很多像四号用户那样的人,只在某一天试了一下这个应用,然后就再也没回来过?如果我们在很多行上都看到这种情况,我们就能意识到我们的引导流程或者其他环节可能存在一个潜在的问题。

[05:01] **SPEAKER_01:** As you get more sophisticated with dot plots, you can make them as intricate as you want. At Bump, we had different symbols that we would put into these cells. So we knew whether you shared your contact information using Bump or if you shared a photo, and it gives you a lot more granularity. And you can kind of go as deep as you want on this.

> 当你把点阵图用得越来越熟练之后,你可以把它做得任意复杂。在Bump的时候,我们会往这些格子里放不同的符号。这样我们就知道你是用Bump分享了联系方式,还是分享了一张照片,这能给你带来更细的粒度。你可以在这方面想钻多深就钻多深。

[05:17] **SPEAKER_01:** This idea of dot plots might be familiar to some of you. You've probably seen it at the top of GitHub pages. This is basically what a GitHub graph looks like. They've just wrapped the days around per week.

> 点阵图这个概念你们中的一些人可能会觉得眼熟。你八成在GitHub页面的顶部见过它。这基本上就是GitHub那张图的样子。他们只不过是把天数按每周折行排列了而已。

[05:28] **SPEAKER_01:** Another thing you can do is, instead of just tracking user actions, you can track user state. So was this user using an iPhone or an Android phone? Were they on the web? Was this user coming from the United States or a different country?

> 你还可以做的另一件事是:除了追踪用户的行为,你还可以追踪用户的状态。比如,这个用户用的是iPhone还是安卓手机?他们是在网页端吗?这个用户是来自美国还是别的国家?

[05:44] **SPEAKER_01:** Sometimes you have demographic information about your users. Is this a user that makes a lot of money? Or is this a college kid that you just got on Reddit or something? You can encode those states with other symbols or shading the cells different colors.

> 有时候你会掌握用户的一些人口统计信息。这是一个收入很高的用户吗?还是一个你刚从Reddit之类的地方拉来的大学生?你可以用别的符号来编码这些状态,或者把格子涂成不同的颜色。

[06:00] **SPEAKER_01:** You can write things over here. So like I might say, this is a iOS user, and this is an iOS user. But these ones are Androids. And another thing you can do then is sort your rows based on whatever attributes you want to sort them by.

> 你可以在这边写上一些标注。比如我可能会写,这是一个iOS用户,这也是一个iOS用户。但这几个是安卓用户。接下来你还可以做的一件事,就是根据你想要的任何属性,对这些行进行排序。

[06:15] **SPEAKER_01:** So you might say, I only want to look at iOS users first, or I only want to look at users whose first time using the app was this Monday. So let's resort so we only see people that have rings around their first day. What you find when you look at this in aggregate, you can then kind of zoom out and see an entire page of these, is your brain will start to notice these patterns in a way that you would never have figured out on your own a priori. This is actually an idea that I remember hearing about 10 years ago from Max Levchin, one of the founders of PayPal.

> 所以你可能会说,我只想先看iOS用户,或者我只想看第一次使用应用是在这个周一的用户。那我们就重新排序,让我们只看到那些第一天带有圆圈标记的人。当你把这些放在一起整体来看的时候——你可以缩小视野,看到满满一页这样的图——你会发现,你的大脑会开始以一种你事先靠自己绝对想不到的方式,注意到这些模式。这其实是一个我记得大约10年前从Max Levchin那里听来的想法,他是PayPal的创始人之一。

[06:47] **SPEAKER_01:** They had a big fraud problem at PayPal when they first launched, but they didn't know the patterns to look for. So what they did instead is build a visualization, a graph of all the transactions that were happening on PayPal. And they just had humans sit and stare at screens of these drawings and graphs. And while the graph was there, while the humans didn't know what exactly was going on, they were able to look at the screen and say, that thing happening there, that's different and probably fraud.

> PayPal刚上线的时候有一个很严重的欺诈问题,但他们不知道该去找什么样的模式。于是他们改而做了一个可视化,把PayPal上所有正在发生的交易画成一张图。然后他们就让人坐在那里盯着这些图画和图表的屏幕看。虽然图就摆在那儿、虽然那些人并不确切知道到底发生了什么,但他们能够看着屏幕说:那边发生的那个东西,不太一样,很可能是欺诈。

[07:15] **SPEAKER_01:** And then they would go and dig into that. It's kind of the same idea with dot plots. You can look at these charts and figure out, huh, there's something going on with users. I see this pattern emerging.

> 然后他们就会去深入调查那部分。点阵图的思路其实是一样的。你可以看着这些图表,发现:咦,用户这边有点什么名堂。我看到有个模式冒出来了。

[07:27] **SPEAKER_01:** And then you can go dig into it a lot deeper. So to illustrate the point I was talking about where dot plots give you a lot more granularity about what's going on with the users, let's draw the DAU graph for these users. So what you would have seen had you only been looking at your DAU graph. I'll just draw it on top of here to illustrate.

> 然后你就可以去做更深入的挖掘。为了说明我前面讲的那个观点——点阵图能让你以更细的粒度了解用户身上发生了什么——我们来给这些用户画一张日活(DAU)图。也就是说,如果你只盯着日活图看,你会看到的东西。我就直接在这上面画出来给你演示一下。

[07:46] **SPEAKER_01:** So again, like imagine each of these days is the same day above.

> 那么再说一遍,你就想象下面这些天,每一天都对应上面的同一天。

[07:51] **SPEAKER_00:** The DAU graph here looks like this. On day one, it's two. On day two, it's three. On day three, it's two, two, two, two, two.

> 这里的日活图看起来是这样的。第一天,是2。第二天,是3。第三天,是2、2、2、2、2。

[08:09] **SPEAKER_00:** One, zero.

> 1,0。

[08:15] **SPEAKER_01:** So if you were just looking at DAUs, this is the graph you would see. And it really doesn't tell you all that much. It basically tells you, yeah, we're not growing. We have some users.

> 所以如果你只看日活,这就是你会看到的图。它其实并没有告诉你太多东西。它基本上只告诉你:嗯,我们没有增长。我们有一些用户。

[08:27] **SPEAKER_01:** Instead, looking at the dot plot, we have a much richer understanding of our users. We know something about their behavior, maybe something about their lives. We probably have inferred from this that these people that use it during the week, probably they're doing it at the office or in some other place where they can find it. They're doing it in a place where they can listen to music every single day of the work week.

> 相比之下,看点阵图我们就能对用户有丰富得多的理解。我们了解到了一些关于他们行为的信息,也许还有一些关于他们生活的信息。我们大概能从中推断出,这些在工作日使用它的人,很可能是在办公室或者其他能用到它的地方使用的。他们是在一个能让他们在整个工作周的每一天都听音乐的地方使用的。

[08:44] **SPEAKER_01:** And again, you can go a lot deeper on this. And if you change the dots to be different symbols, for example, in our Spotify example, we could choose to represent different features of the product. Let's say if a user uses search in Spotify, we'll put a little S next to it. Or if they use maybe a playlist, they join a public playlist, let's say, we could put a P there.

> 再说一次,你可以在这方面挖得深得多。如果你把这些点换成不同的符号,比如在我们的Spotify例子里,我们就可以选择用它们来代表产品的不同功能。比方说,如果一个用户用了Spotify里的搜索功能,我们就在旁边放一个小小的S。或者如果他们用了歌单,比如加入了一个公开歌单,我们就可以在那里放一个P。

[09:09] **SPEAKER_01:** And you might start to see patterns where specific features maybe drive behaviors in the product that you actually want. Let's just say for the sake of argument that we see this one user here that joined a public playlist. They then have a string of many, many consecutive days of using the product. We could then infer like, oh, maybe the playlist feature is really causal to having people be really active in our product.

> 然后你可能就会开始看到一些模式,某些特定的功能也许会驱动出你真正想要的那种产品内行为。为了便于讨论,我们就假设我们看到这里的这个用户加入了一个公开歌单。之后他们就连续很多很多天一直在使用产品。那我们就可以推断:哦,也许歌单这个功能对于让人们在我们产品里保持高度活跃是真正起因果作用的。

[09:33] **SPEAKER_01:** This is the sort of stuff that you can learn with dot plots. So what's really great for most founders, you have a very small number of users at the beginning. And so you can literally look at every single user of your product on every single day they've ever used it. And it all fits on one screen on your monitor.

> 这就是你能通过点阵图学到的那类东西。所以对大多数创始人来说真正美妙的一点是,你在一开始只有非常少的用户。因此你可以真真切切地看到你产品的每一个用户在他们用过的每一天里的情况。而且这一切都能塞进你显示器的一屏之内。

[09:51] **SPEAKER_01:** That's really great. But it actually does scale to when you have thousands or millions or billions of users. This is a tool that we used at Google Photos when we had well more than a billion users. And the idea is you can just choose to sample your users and represent them on a dot plot however you want.

> 这非常棒。但实际上,当你有成千上万、数百万甚至数十亿用户的时候,它同样能扩展适用。这是我们在Google Photos用户远超十亿的时候还在用的一个工具。它的思路就是,你可以选择对你的用户进行抽样,然后按你想要的任何方式把他们呈现在一张点阵图上。

[10:09] **SPEAKER_01:** So we would have days where we print out, dozens of these pieces of paper with dot plots on them for different samples of our user base. I would print out a piece of paper and hand one of our team members like, here's the iOS users in France. I want you to understand what they're doing. And I would hand another piece of paper to somebody else and say, these are the users on web in the United States who make more than $80,000 a year.

> 所以我们会有那样的日子,打印出几十张这种印着点阵图的纸,分别对应我们用户群里的不同抽样。我会打印出一张纸,递给我们团队的某个成员,说:这是法国的iOS用户,我想让你搞清楚他们在做什么。然后我会把另一张纸递给别人,说:这些是美国网页端、年收入超过8万美元的用户。

[10:29] **SPEAKER_01:** Let's see what they're up to. And we would have days where we just sit in the office and look at these dot plots and try to draw conclusions about what's going on with our users. So you might be thinking to yourself, this is cool, Dave, but we're a B2B product. And we just sell seats to businesses and they pay for it.

> 我们来看看他们在忙些什么。我们会有那样的日子,就坐在办公室里看着这些点阵图,试图对我们用户身上发生的事情得出一些结论。那么你可能会心里想:这挺酷的,Dave,但我们是个B2B产品。我们只是把席位(seats)卖给企业,他们付钱就行了。

[10:45] **SPEAKER_01:** And so I, that's all that matters, right? Turns out that dot plots could be really useful to you too. Let me give you a specific example. I worked with a company in the most recent YC batch that had a very name brand customer that signed up and bought their product.

> 所以对我来说,重要的就只有这个,对吧?但事实证明,点阵图对你来说其实也可能非常有用。让我给你举一个具体的例子。我在最近这一批YC里跟一家公司合作过,他们有一个非常知名的品牌客户注册并购买了他们的产品。

[10:59] **SPEAKER_01:** I think it was like a $80,000 a year contract. They onboarded the company. The company said they wanted 10 seats and later the company churned. Let me show you what they could have figured out had they been using dot plots.

> 我记得那是一份大约每年8万美元的合同。他们完成了这家公司的入驻引导。这家客户公司说他们想要10个席位,而后来这家公司流失了(churned)。让我给你展示一下,如果他们当时用了点阵图,他们本可以发现什么。

[11:13] **SPEAKER_01:** So this is what it actually looked like. The company bought 10 seats, but only three seats ever activated. Only three of those people ever tried the product. And if you look at their usage, they weren't getting a lot of value from it.

> 实际情况是这样的。这家公司买了10个席位,但从头到尾只有3个席位被激活过。那些人里只有3个真正试用过产品。而如果你看他们的使用情况,他们并没有从中获得多少价值。

[11:25] **SPEAKER_01:** Nobody used it more than two days per week. And it looks like pretty sporadic usage. And it turns out what happened is the company was in the States. The champion had gotten excited about this product and bought it.

> 没有人每周使用超过两天。而且看上去使用得相当零散。事实证明,后来发生的情况是:这家公司在美国。那位内部推动者(champion)对这个产品很兴奋,于是买了它。

[11:39] **SPEAKER_01:** champion left the company. And as soon as the champion left, a new person came in and they said, why are we using this software? We're going to churn. And so they opted out of a renewal clause at the last moment. The company could have known that this contract was in jeopardy by looking at

> 后来这位推动者离开了公司。而他一走,一个新人接手进来,就说:我们为什么要用这个软件?我们要停掉。于是他们在最后一刻选择退出了续约条款。这家做产品的公司本来是可以知道这份合同岌岌可危的,只要他们看一看……

[11:53] **SPEAKER_01:** the dot plot. So there's a few ways you can misuse dot plots. The number one thing is to just chart the wrong event. A lot of founders might want to populate their dot plot with the easiest way to populate it so it feels good and you see a lot of dots. Maybe you'll pick like open the app or

> ……点阵图就行了。那么,使用点阵图也有几种会用错的方式。头号错误就是选错了要标记的事件。很多创始人可能会想用最容易填满点阵图的方式去填它,好让自己感觉良好、看到密密麻麻一堆点。也许你会选择比如"打开应用",或者……

[12:09] **SPEAKER_01:** signed into the product. Those are pretty bad events to choose because they don't really measure whether the user is getting real value. So I suggest you pick something that actually represents value being created for the user. Listen to a song, shared a photo, something like that. That's

> ……"登录了产品"。这些都是相当糟糕的事件选择,因为它们并不能真正衡量用户是否获得了真实的价值。所以我建议你挑选一个真正代表着为用户创造了价值的东西。听一首歌、分享一张照片,诸如此类的。那才是……

[12:24] **SPEAKER_01:** a real event. The other mistake you can make is picking a time period that's too wide. Sometimes founders want to make it look better and they pick weeks, like week one, week two, week three, it's way harder to figure out what's actually going on unless you look at it at the day or maybe even like subday granularity. So I would go so far as to say until you have hundreds of users, the dot plot could be your only dashboard. What's great about dot plots is they're just a logs

> ……一个真实的事件。你可能会犯的另一个错误是选了一个太宽的时间段。有时候创始人想让它看起来更漂亮,于是他们用"周"作单位,比如第一周、第二周、第三周,而这样就更难看清到底发生了什么,除非你以"天"、甚至以"日内(subday)"这样的粒度去看它。所以我甚至敢说,在你拥有几百个用户之前,点阵图可以是你唯一的仪表盘。点阵图的妙处在于,它们只不过是一个日志……

[12:51] **SPEAKER_01:** visualization tool. There's no fancy computations happening here. You basically just need to parse your logs and put them into a 2D grid. This is a thing that modern AI coding tools can whip up in 10 minutes. These are best used

> ……可视化工具而已。这里面没有什么花哨的计算。你基本上只需要解析你的日志,然后把它们放进一个二维网格里。这是现代AI编程工具10分钟就能鼓捣出来的东西。它们最好是与……

[13:04] **SPEAKER_01:** in conjunction with cohort retention curves. Cohort retention curves teach you in aggregate whether groups of users that you acquire stick with you over time. That's very important. You should definitely be measuring that. But the dot plot shows you how those users are actually using

> ……分组留存曲线结合起来使用。分组留存曲线从聚合的层面告诉你,你所获取的一批批用户是否会随时间的推移持续留在你这里。这非常重要,你绝对应该去衡量它。但点阵图向你展示的是,这些用户实际上是如何使用……

[13:19] **SPEAKER_01:** your product and they give you the color to go ask the right questions of your users, to go build the right features, to fix things that are broken in your product that you would never learn by looking at aggregate metrics. So cohort retention curves and dot plots are, in my experience, two of the most important tools that you've got to understand your users. Good luck.

> ……你产品的,它们能给你提供那些鲜活的细节,让你去向用户提出正确的问题、去构建正确的功能、去修复你产品中那些出了问题的地方——而这些都是你光看聚合指标永远学不到的。所以,以我的经验来看,分组留存曲线和点阵图,是你理解用户所拥有的两个最重要的工具。祝你好运。
