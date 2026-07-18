# 全文转录 · OpenClaw 之父:为什么 80% 的 App 都会消失

> ▶ [YouTube](https://www.youtube.com/watch?v=4uzGDAoNOZc) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/4uzGDAoNOZc.md) &nbsp;·&nbsp; OpenClaw Creator: Why 80% Of Apps Will Disappear

> 中英对照 · 每段英文原文下附中文翻译

[00:00] **SPEAKER_01:** Today I'm sitting down with Peter Steinberger, the creator of OpenClaw, the open-source personal AI agent that has completely taken over the internet. The GitHub repo exploded to over 160,000 stars practically overnight. The community has built countless projects like MoldBook, where bots talk among themselves. And now the bots are even renting humans to do tasks in the real world. In our conversation, we discuss his aha moment, his contrarian development philosophies, and what this means for builders in 2026. Let's dive in.

> 今天我要和 Peter Steinberger 坐下来聊聊,他是 OpenClaw 的创造者——这是一个开源的个人 AI 智能体,已经彻底席卷了整个互联网。它的 GitHub 仓库几乎一夜之间就暴涨到超过 16 万个 star。社区已经在它之上构建了无数项目,比如 MoldBook,机器人之间可以互相交谈。而现在,这些机器人甚至开始雇佣真人去现实世界里完成任务。在我们的对话中,我们会聊到他的顿悟时刻、他那些反主流的开发理念,以及这一切对 2026 年的开发者意味着什么。让我们开始吧。

[00:38] **SPEAKER_01:** So good to see you, man. Hey, what's up? So you've made something people want. It seems so. Yeah. OpenClaw, as it's called now, has absolutely...

> 很高兴见到你,老兄。嘿,你好吗?你做出了一个人们真正想要的东西。看起来是这样。是的。OpenClaw,也就是它现在的名字,已经彻底……

[00:48] **SPEAKER_01:** Name number five, yeah. ...has been absolutely exploding the internet. How have the past one or two weeks been for you, man?

> 这已经是第五个名字了,是的。……在互联网上引爆了。过去这一两周对你来说是怎样的,老兄?

[00:56] **SPEAKER_02:** Oh, my God. I need a cave. A week of solitude.

> 天哪。我需要一个山洞。需要一周的独处。

[01:03] **SPEAKER_01:** You came out of the cave. And you want to go back to the cave like a little officer.

> 你才刚从洞里出来。你现在又想回到洞里去,像个小军官一样。

[01:07] **SPEAKER_02:** It's been absolutely wild. I don't know how one human can absorb all of that. I probably need another week just to respond to all my emails. I got some incredibly cool stuff. I got some incredibly bad stuff.

> 这简直太疯狂了。我不知道一个人怎么能承受得了这一切。我大概还得再花一周才能回完所有的邮件。我收到了一些超级酷的东西,也收到了一些糟透了的东西。

[01:21] **SPEAKER_02:** But clearly, I hit something that spurred up emotions and made people interested and inspired people. It's pretty cool.

> 但很明显,我触动了某种能激发情绪、让人们感兴趣、给人以启发的东西。这挺酷的。

[01:28] **SPEAKER_01:** And a lot of people have been working on AI and even personal assistants. Like, what is it that made... OpenClaw take off?

> 很多人都在做 AI,甚至个人助手。那到底是什么让……OpenClaw 火起来了?

[01:36] **SPEAKER_02:** I think my big difference is that it actually runs on your computer. Like, everything I saw so far runs in the cloud. It's like, it can do a few things. If you run it on your computer, it can do every effing thing, right? So that's way more powerful.

> 我觉得我最大的不同在于,它真正运行在你自己的电脑上。我目前看到的所有东西都跑在云端,那样它只能做有限的几件事。而如果它运行在你的电脑上,它他妈的什么都能做,对吧?所以这强大得多。

[01:53] **SPEAKER_01:** Yeah. Machine can do anything that you can do with the machine.

> 是的。凡是你能用这台机器做的事,机器都能做。

[01:56] **SPEAKER_02:** It can just connect to your oven or your Tesla or your lights, your saunas, my bed. It can control the temperature. It can switch off my bed. ChatGPT can do that. You gave it all the skills that you have yourself.

> 它可以直接连接到你的烤箱、你的特斯拉、你的灯、你的桑拿房,还有我的床。它可以控制温度。它可以关掉我的床。ChatGPT 可做不到这些。你把你自己拥有的所有技能都给了它。

[02:10] **SPEAKER_02:** A friend told me, like, he installed OpenClaw and then he asked me, like, look through my computer and make a narrative over my last year. And it made this incredibly good narrative. And he was like, how did you do that? And then he, the OpenClaw found audio files where, like, every Sunday he was recording stuff. And OpenClaw found that.

> 一个朋友告诉我,他装了 OpenClaw,然后他跟它说,浏览我的电脑,给我过去一年做一个叙述。结果它做出了一个特别棒的叙述。他就想,你是怎么做到的?后来发现,OpenClaw 找到了一些音频文件,他每个星期天都会录点东西。OpenClaw 把那些都找出来了。

[02:34] **SPEAKER_02:** But he didn't even remember about it. Because it was, like, more than a year ago, right? So just by it being able to search your whole computer, it can surprise you. You also give it all the data, right? So it can surprise you in many ways.

> 而他自己甚至都不记得有这回事了。因为那都是一年多以前的事了,对吧?所以仅仅是因为它能搜索你的整台电脑,它就能给你惊喜。你也把所有数据都交给了它,对吧?所以它能在很多方面给你带来惊喜。

[02:52] **SPEAKER_01:** And so now you have, you know, we're even moving from human to bot. So like interactions that you've been talking about, to bot to bot interactions. Or even, like, bot to other humans where, you know, bots on behalf of you are then hiring you. Yeah. Or then hiring other humans to accomplish tasks IRL.

> 所以现在,你看,我们甚至正在从人对机器人——也就是你刚才说的那种交互——转向机器人对机器人的交互。甚至是机器人对其他人类的交互,机器人代表你去雇佣你。是的。或者去雇佣其他真人在现实世界中完成任务。

[03:09] **SPEAKER_01:** Like, what's happening?

> 这到底是怎么回事?

[03:12] **SPEAKER_02:** I think that's a natural next step. Like, okay, I want to book a restaurant. My bot will reach out to the restaurant bot and do the negotiation. Like, because it's more efficient. Or maybe it's, like, an old restaurant.

> 我觉得这是很自然的下一步。比如说,我想订一家餐厅。我的机器人会去联系餐厅的机器人,进行协商。因为这样更高效。或者也许那是一家老派的餐厅。

[03:28] **SPEAKER_02:** So my bot needs to actually get some human work done so that the human then calls the restaurant because they don't like bots.

> 那我的机器人就得真的去找个人来帮忙,让这个人打电话给餐厅,因为他们不喜欢机器人。

[03:35] **SPEAKER_01:** Or walks there to stand in line.

> 或者亲自走过去排队。

[03:37] **SPEAKER_02:** If he doesn't get a robot.

> 如果他找不到机器人的话。

[03:38] **SPEAKER_01:** For the owner of the bot.

> 为了这个机器人的主人。

[03:41] **SPEAKER_02:** And I imagine that, like, maybe if I have even multiple bots. Maybe I have, like, specialists. One is, like, for my private life and one is for, like, my work stuff. Maybe one is our relationship bot that gets, like, other things in between. I don't know.

> 我可以想象,也许我甚至会有多个机器人。也许我会有一些专才型的机器人。一个负责我的私人生活,一个负责我的工作。也许还有一个是我们的关系机器人,处理介于两者之间的一些事情。我也说不好。

[03:57] **SPEAKER_02:** We're so early. There's still so much, so many things that we haven't really figured out if it actually works. But I feel we are on the timeline now.

> 我们还处在非常早期的阶段。还有太多东西、太多事情我们其实都还没搞清楚它到底行不行得通。但我感觉我们现在已经踏上了这条时间线。

[04:07] **SPEAKER_01:** It seems like everyone was chasing sort of, like, the sort of, like, centralized god intelligence. And what has sort of emerged over the past, you know, 10 days or so is sort of, like, the swarm intelligence and the community intelligence.

> 似乎每个人都在追逐某种中心化的"上帝级智能"。而过去这大概十天里所涌现出来的,却是一种群体智能、社区智能。

[04:20] **SPEAKER_02:** I think that if you look at one human being, what can one human being actually achieve? Do you think one human being could make an iPhone? Or one human being could go to space? I don't know. One human being would probably just, like, not even be able to, like, find food.

> 我觉得,如果你看单独一个人,一个人到底能成就什么?你觉得一个人能造出一部 iPhone 吗?或者一个人能上太空吗?我不知道。单独一个人可能连找到食物都做不到。

[04:36] **SPEAKER_02:** Um. But as a group, we specialize. As a larger society, we specialize even more. So what can we learn from that that we can apply to AI? You know, we already have, like, AI that specializes in certain things.

> 嗯。但作为一个群体,我们会分工专精。作为一个更大的社会,我们的专业化程度就更高。那我们能从中学到什么,并应用到 AI 上呢?你看,我们其实已经有了在某些特定方面专精的 AI。

[04:54] **SPEAKER_02:** Even though it's generalized intelligence, what if it actually is also specialized intelligence? So I don't know. It's going to be very exciting and cool.

> 尽管它是通用智能,但如果它同时也是专用智能呢?所以我也说不好。这将会非常令人兴奋,非常酷。

[05:03] **SPEAKER_01:** Yeah. You kind of, like, opened a window into the future and now a ton of people are kind of, like, building. Yeah. Yeah. They're building on it and have sort of, like, their aha moment.

> 是的。你算是打开了一扇通往未来的窗户,现在一大批人都在动手构建。是的,是的。他们在它之上构建,并且也有了各自的顿悟时刻。

[05:11] **SPEAKER_01:** Can you walk me back to when you had your aha moment and kind of, like, recount that very moment?

> 你能带我回到你自己顿悟的那一刻,给我讲讲那个瞬间吗?

[05:16] **SPEAKER_02:** I wanted something to, like, just type stuff so my computer would do stuff. Like, very simple. And then I built a version of that in May, June that was cool but wasn't really it. And then I built a whole bunch of other stuff and kind of, like, built up my army. And then in November, there was a day where I wanted this again.

> 我想要一个东西,让我打几个字,我的电脑就能去干活。很简单。然后我在五六月份做了一个版本,挺酷的,但还不够到位。之后我又做了一大堆别的东西,算是慢慢建立起了我的"军队"。然后到了十一月,有一天我又想要这个东西了。

[05:41] **SPEAKER_02:** Like, I went to the kitchen and all I wanted was to check up if my computer would still do stuff or being finished.

> 就是,我走进厨房,我只想看看我的电脑是不是还在干活,或者已经干完了。

[05:48] **SPEAKER_01:** And doing stuff was coding. You were coding stuff. Yeah, of course. Were you coding something else or were you coding the thing itself?

> 而"干活"指的是写代码。你在写代码。是的,当然。你当时是在写别的东西,还是在写这个东西本身?

[05:56] **SPEAKER_02:** No, no. That was just, like, the need was again there. And I'm, like...

> 不,不。那只是,那种需求又冒出来了。然后我就想……

[06:00] **SPEAKER_01:** What were you coding at the time? What were you building?

> 你当时在写什么?你在做什么?

[06:03] **SPEAKER_02:** My God. My GitHub is, like, 40 projects. I don't even know. I think it was Summarize. It's, like, a little CLI app where you can give it whatever, like, a podcast or a hot seat thing, like, here.

> 天哪。我的 GitHub 上大概有四十个项目。我自己都不知道了。我想那应该是 Summarize。它是一个小小的命令行应用,你可以给它任何东西,比如一个播客,或者一个访谈之类的,就像这样。

[06:19] **SPEAKER_02:** And it would summarize it. But it also showed you the slides in the terminal. Because you can do that nowadays.

> 然后它会做总结。但它还会在终端里给你显示幻灯片。因为现在你可以做到这一点了。

[06:24] **SPEAKER_01:** Yeah.

> 是的。

[06:24] **SPEAKER_02:** You can just do things.

> 你就是可以做到这些事。

[06:25] **SPEAKER_01:** So for the love of the computer, you kind of, like, started messing with stuff. You came out of retirement, actually, right? To sort of, like, mess with AI. Yeah. And then increasingly, you were so hooked that you wanted to just do it always, all's on the go with the phone.

> 所以出于对电脑的热爱,你就开始鼓捣一些东西。你其实是退休之后又复出了,对吧?为了摆弄 AI。是的。然后你越陷越深,上了瘾,想要随时随地都能做这件事,在路上用手机也能做。

[06:39] **SPEAKER_02:** I'm in the last project. I worked two months on Wipe Tunnel to the point where it got so good that I was catching myself always, like, coding next to my... When I was with my friends. And I'm, like, I need to stop this. This is, like, too addictive.

> 在上一个项目里,我在 Vibe Tunnel 上做了两个月,做到它好到什么程度呢——我总是发现自己在……跟朋友在一起的时候还在旁边写代码。然后我就想,我得停下来。这太容易上瘾了。

[06:53] **SPEAKER_02:** And then in November, my need came back. And I started building Cloudbot. Oh, now it's called Open Cloud. And I think very, very in the beginning, I was, like, oh, I rebuilt it again. But this time, I built it even better.

> 然后到了十一月,我的那种需求又回来了。我开始做 Cloudbot。哦,它现在叫 OpenClaw。我记得非常非常早期的时候,我心想,哦,我又重建了一遍。但这次,我做得更好了。

[07:07] **SPEAKER_02:** This time, when you don't type into a terminal, you just talk to a friend. You don't think about compaction, new sessions, which folder I'm in, which model I'm in. I mean, you can, you know, just, like, I want to leave it open for power users. But usually, you just, like, you just talk to a friend. And the friend is, like, this ghost or entity or whatever you want to call it that can control your mouse and your keyboard and can just do stuff.

> 这一次,你不是在终端里打字,你就是在跟一个朋友聊天。你不用去想上下文压缩、新会话、我在哪个文件夹、我用的是哪个模型。我是说,你也可以去想这些——我想把这些留给高级用户。但通常来说,你就只是跟一个朋友聊天。而这个朋友就像是一个幽灵,或者一个实体,随便你怎么叫它,它能控制你的鼠标和键盘,直接帮你干活。

[07:33] **SPEAKER_01:** Yeah. And when did you have that aha moment when you were, like, wow, this is doing way more things than I actually thought it could?

> 是的。那你是在什么时候有了那个顿悟时刻,让你觉得,哇,它能做的事情比我以为的多得多?

[07:41] **SPEAKER_02:** Literally. It took me one hour for, like, the very shitty initial prototype. It was just a little bit of glue between, like, a dependency that connects WhatsApp and Cloud Code. And then I would, like, call Cloud Code and get, like, the string out of Cloud Code. It would be slow, but it worked.

> 真的。那个非常烂的初始原型只花了我一个小时。它只是把一个连接 WhatsApp 和 Claude Code 的依赖库粘合了一下。然后我调用 Claude Code,把字符串从 Claude Code 里取出来。它很慢,但能用。

[08:00] **SPEAKER_02:** But I wanted images. Because, you know, you want pictures. I want the model to send the selfies or whatever. And I want the model to create images and send me back. So that took me another few hours.

> 但我想要图片。因为,你懂的,你会想要图片。我想让模型发自拍之类的东西。我想让模型生成图片再发回给我。所以这又花了我几个小时。

[08:12] **SPEAKER_02:** And then I went to Marrakesh for a birthday party. And there was, like, the internet wasn't that good, you know. WhatsApp works everywhere because, I don't know, it's just, like, text. So I used it a lot. Oh, restaurant.

> 然后我去马拉喀什参加一个生日派对。那里的网络不太好,你懂的。WhatsApp 到哪都能用,因为它就只是文本嘛。所以我大量地用它。哦,餐厅。

[08:23] **SPEAKER_02:** What does this mean? You make, like, a picture and, like, translate this for me. And it was just so useful. And it was also really nice about it because it spoke my language. You know, it was a little sassy.

> 这是什么意思?你拍一张照片,然后说,帮我翻译一下这个。它就是特别有用。而且它还很讨人喜欢,因为它说着我的语言。你知道的,它有点俏皮。

[08:33] **SPEAKER_02:** It was, like, funny. It was, like, really pleasant to use. And then I was walking and just, like, sending it a voice message. And I'm, like, oh, wait. This can't work.

> 它很有趣。用起来真的很愉快。然后有一次我在走路,顺手给它发了一条语音消息。我就想,哦,等等,这不可能行得通啊。

[08:42] **SPEAKER_02:** I didn't build that. Right, right. And it's, like, the type indicator. It's, like, blinking, blinking, blinking. Ten seconds later, it just replied to me.

> 我没做过这个功能啊。对,对。然后那个"正在输入"的提示,一直在闪、闪、闪。十秒钟后,它就回复我了。

[08:50] **SPEAKER_02:** And I'm, like, how in the F did you do that? And it replied, yeah, the mad lad did the following. You sent me a text message. And there was no file ending. So I looked at the header.

> 我就想,你他妈是怎么做到的?它回复说,是啊,这个疯子(指它自己)做了如下操作:你给我发了一条消息,里面有个文件但没有后缀名,所以我看了一下文件头。

[09:00] **SPEAKER_02:** I found it's Opus. So I used FFmpeg to convert it to Wave. And then I wanted to, like, transcribe it but didn't have Vispa installed. But then I looked around and I found this OpenAI key. And I just used curl to send it to OpenAI, got the text back, and here I am.

> 我发现它是 Opus 格式。所以我用 FFmpeg 把它转成了 Wave。然后我想把它转录成文字,但没装 Whisper。不过我四处看了看,找到了一个 OpenAI 的 key。于是我就用 curl 把它发给 OpenAI,拿回了文字,然后我就在这儿了。

[09:14] **SPEAKER_02:** And then that all in, like, what, nine seconds? And you didn't build or anticipate, like, any of those specific things? No. You know, it turns out, because coding models got so good, coding is really, like, creative problem solving that maps very well back into the real world. I think there's a huge correlation.

> 而这一切都在,多少来着,九秒钟之内完成了?而这些具体的步骤你一个都没做过,也没预料到?没有。事实证明,因为编程模型变得如此强大,而编程本质上是一种创造性的问题解决,它能很好地映射回现实世界。我觉得这里有着巨大的相关性。

[09:36] **SPEAKER_02:** They need to be really good at creative problem solving. And that's a skill. That's an abstract skill. You can apply it to code but, like, to any real world. Yeah.

> 它们必须非常擅长创造性地解决问题。而这是一种技能,一种抽象的技能。你可以把它用在代码上,但也可以用在任何现实世界的场景中。是的。

[09:44] **SPEAKER_02:** It's a real world task. So the model had a, oh, surprise, it's, like, a magical file. I don't know what it is. I need to solve this. And it did its best and solved it.

> 这是一个现实世界的任务。所以模型遇到的情况是,哦,惊喜,这是个神秘的文件。我不知道它是什么。我得解决这个问题。然后它尽了最大努力,把它解决了。

[09:51] **SPEAKER_02:** And it was even that clever that it chose not to install the local Vispa because it knows that that would require downloading a model which would take probably a few minutes. And I'm, like, impatient, you know? So it really took the most intelligent approach. And that was kind of, like, the moment where I'm, like, holy fuck, yeah?

> 而且它甚至聪明到没有选择安装本地的 Whisper,因为它知道那需要下载一个模型,可能得花好几分钟。而我这个人没什么耐心,你懂的。所以它真的采取了最明智的做法。那大概就是让我惊呼"我靠"的那个时刻,对吧?

[10:15] **SPEAKER_00:** That was where I got hooked. YC's next batch is now taking applications. Got a startup in you? Apply at ycombinator.com slash apply.

> 那就是我上瘾的地方。YC 的下一批项目现在开始接受申请了。你心里有个创业点子吗?到 ycombinator.com/apply 申请吧。

[10:25] **SPEAKER_00:** It's never too early. And filling out the app will level up your idea. Okay. Back to the video.

> 什么时候申请都不算早。而且填写申请表本身就能让你的点子更上一层楼。好了,回到视频。

[10:31] **SPEAKER_01:** And so when computers can just do all these things that you didn't even anticipate, you didn't build an app to do that exact thing, are apps just going to go away?

> 那么,当电脑能够做所有这些你甚至都没预料到的事,你并没有专门为那件事做一个 App,那 App 是不是就要消失了?

[10:39] **SPEAKER_02:** I think 80% of them are going away. Why do I need MyFitness? Because I don't need MyFitnessPal. Like, my agent already knows that I'm making bad decisions. I'm at, I don't know, SmashBurger or something.

> 我觉得其中 80% 都会消失。我为什么需要 MyFitness?因为我不需要 MyFitnessPal。我的智能体已经知道我在做糟糕的决定了。我人在,我也不知道,SmashBurger 之类的地方。

[10:55] **SPEAKER_02:** And it will already assume that I eat what I like to eat. If I don't make a comment, it will just, like, automatically track it. Or I make a picture, and it will just store it somewhere. I don't even need to care, right? And then maybe it improves my gym schedule, like, adds a little bit more cardio in it.

> 它已经会假设我吃的是我爱吃的东西。如果我不特别说什么,它就会自动帮我记录下来。或者我拍张照片,它就会把它存到某个地方。我甚至都不需要操心,对吧?然后也许它还会改进我的健身计划,比如给里面多加一点有氧运动。

[11:13] **SPEAKER_02:** I don't need MyFitnessApp. It just does the fitness planning for me. Why do I need a to-do app? I just tell it, hey, remind me of this and this. And the next day, it will just remind me of this and this.

> 我不需要 MyFitness App。它直接就帮我做健身规划了。我为什么需要一个待办事项 App?我只要跟它说,嘿,提醒我做这个和那个。第二天,它就会提醒我做这个和那个。

[11:22] **SPEAKER_02:** Do I care where it's stored? No, it just does its thing. So every app that basically just manages data could be managed in a better way, and it's in a more natural way by agents. Yeah. Only the apps that actually have sensors, maybe they survive.

> 我在乎它存在哪里吗?不,它就是把事情办了。所以每一个基本上只是在管理数据的 App,都可以被智能体以一种更好、更自然的方式来管理。是的。只有那些真正带有传感器的 App,也许才能存活下来。

[11:40] **SPEAKER_01:** And so if, you know, most apps are going to go away in that scenario, are the models the only remaining sort of apps?

> 那么,如果在那种情况下大多数 App 都会消失,那模型是不是就成了唯一剩下的"App"?

[11:48] **SPEAKER_02:** Not everything will go away. But yeah, I think that the large model companies have some big mode, because they ultimately, they give the token. And turns out, one of the complaints was that people use so much token. No, you just really love using it. That's why you use the thing so much, because that's how you burn the token.

> 不是所有东西都会消失。但没错,我觉得大模型公司有很深的护城河,因为归根结底,是他们提供 token。而事实证明,当初有一个抱怨是说人们用了太多 token。不,你只是真的太喜欢用它了。这就是你为什么用得那么多,因为这正是你烧掉 token 的方式。

[12:11] **SPEAKER_02:** It's like, is it my fault that I make something that's so popular?

> 这就好像说,我做出一个这么受欢迎的东西,难道是我的错吗?

[12:14] **SPEAKER_01:** And so, you know, like, all the models, they're kind of like leapfrogging each other constantly. And, you know, maybe they're also getting commoditized. So if apps are going to go away, models are going to get commoditized. Or at least, you know, the lobster can, like, the brain is swappable out. What's the thing that remains?

> 那么,你看,所有这些模型,它们一直在互相赶超。而且,也许它们也在变得同质化、商品化。所以如果 App 会消失,模型会被商品化,或者至少那个"龙虾"的大脑是可以随时替换的,那到底还剩下什么?

[12:32] **SPEAKER_01:** Where's the value? Is it the store of memory? Is it the hardness that's valuable? What remains?

> 价值在哪里?是那份记忆的存储吗?还是那种难以复制的东西才是有价值的?到底还剩下什么?

[12:41] **SPEAKER_02:** First of all, I don't think the model companies always have a mode. And because you see this already, a new model comes out. People are like, oh, my God, this is so good. And then, like, a month later, it degraded. It's not good anymore.

> 首先,我不认为模型公司永远都有护城河。因为你已经能看到这种现象了:一个新模型发布,大家都说,天哪,这也太好了。然后大概一个月后,它"退化"了,不好用了。

[12:55] **SPEAKER_02:** They, like, quantized it. No, they didn't do anything. You just adapted to the new standard. And now your expectations went up. But the model is still the average.

> 大家说,他们是不是把它量化压缩了。不,他们什么都没做。是你自己适应了新的标准。现在你的期望值提高了。但那个模型还是原来那个平均水平。

[13:05] **SPEAKER_02:** So I think for quite a while, every time a new model releases, I see the same. People love it. And then it's the standard. And then what's down there, you don't even want to think about it anymore. So.

> 所以我觉得在相当长一段时间里,每次有新模型发布,我都会看到同样的情况。人们爱它。然后它变成了标准。然后比它差的那些,你甚至都不愿意再去想了。就这样。

[13:17] **SPEAKER_02:** So we have, like, open source stuff that's as good as the current models from a year ago. Everybody's hating it, complaining, oh, this is not good. It's not funny. Yet this was what we had. And, like, in a year, we'll have this open source.

> 所以我们现在有一些开源的东西,和一年前的当红模型一样好。大家却都在嫌弃它、抱怨它,哦,这不好用,一点都不好玩。然而这曾经就是我们所拥有的全部。而且,大概一年后,我们就会有这种开源的水准。

[13:28] **SPEAKER_02:** And then we'll complain about this because we are used to this. So for the foreseeable future, the big companies still have mode. Harness-wise, it's going to be interesting because every company kind of has their own silo, right? There's no way. Maybe there is for Europeans.

> 然后我们又会抱怨这个,因为我们已经习惯它了。所以在可预见的未来,大公司仍然有护城河。至于框架/工具层面,会很有意思,因为每家公司都有自己的数据孤岛,对吧?没有办法(把数据导出来)。也许对欧洲人来说有办法。

[13:48] **SPEAKER_02:** To actually get the memories out of ChatGPT. I'm not aware. Definitely, there's no way for a different company to get your memories out. So if I was, like, a company who, like, provides chat services, you could use me, but then I couldn't access the memories. So, like, the companies try to, like, bound you to their data silo.

> 也就是真正把记忆从 ChatGPT 里导出来。我不清楚有没有。但可以肯定的是,别的公司绝对没办法把你的记忆导出来。所以如果我是一家提供聊天服务的公司,你可以用我,但我却无法访问那些记忆。所以这些公司都在试图把你绑定在他们的数据孤岛里。

[14:11] **SPEAKER_02:** And the beauty of OpenClaw is it kind of claws into the data. Because at the end user, the end user needs access because it's, in the end, otherwise, it wouldn't work, right? If the end user has access, I can access the data.

> 而 OpenClaw 的妙处就在于,它能"爪"进那些数据里。因为在终端用户这一侧,终端用户是需要访问权限的,否则到头来它根本没法用,对吧?只要终端用户有访问权限,我就能访问到那些数据。

[14:23] **SPEAKER_01:** And you own the memories. It's just a bunch of markdown files on your machine. I mean, I don't own the memories. I mean, everybody. Yeah, everyone owns their own memories as a bunch of markdown files on their own machines.

> 而且你拥有这些记忆。它们不过是你机器上的一堆 markdown 文件。我是说,不是我拥有这些记忆,我是说每个人。对,每个人都以一堆 markdown 文件的形式,在自己的机器上拥有自己的记忆。

[14:34] **SPEAKER_02:** And to be honest, those are probably super sensible because, let's be honest, people use their agent not just for problem solving, but also for, like, personal problems. Very quickly.

> 说实话,那些东西大概是极其敏感的,因为老实说,人们用他们的智能体不只是为了解决问题,还会用来处理个人问题。而且很快就会这样。

[14:47] **SPEAKER_01:** Super quickly.

> 非常快。

[14:48] **SPEAKER_02:** I mean, I fully do that. I'm like, there's memory stuff that I don't want to have leaked.

> 我是说,我自己就完全是这样。里面有些记忆内容我可不想被泄露出去。

[14:53] **SPEAKER_01:** Yeah. What would you rather sort of, like, not show? Your Google search history at this point or your, you know, memory.md files?

> 是的。到了这个地步,你更不愿意让别人看到哪个?是你的谷歌搜索记录,还是你的那些 memory.md 文件?

[15:00] **SPEAKER_02:** What's the Google word? People still using Google? I built this and I was so excited. But on Twitter, people wouldn't get it.

> "谷歌"是啥来着?人们还在用谷歌吗?我做出了这个东西,特别激动。但在 Twitter 上,人们就是理解不了它。

[15:12] **SPEAKER_01:** Yeah.

> 是的。

[15:12] **SPEAKER_02:** Like, I was failing to explain the awesomeness. I feel like. Yeah. Yeah. It needs to be experienced.

> 我感觉我没能把它的厉害之处解释清楚。是的,是的。它需要被亲身体验。

[15:20] **SPEAKER_02:** So I tried various things and I couldn't nail the explaining. So I was like, let's do something really crazy. I just created a Discord and I just put my bot without any security restrictions in the public Discord. And then people came in and they interacted with it and they saw me build the software with it and they tried to prompt inject it and hack it. And my agent would be laughing at them.

> 所以我尝试了各种办法,还是没法把它讲明白。于是我就想,那我们干点真正疯狂的事吧。我建了一个 Discord,把我的机器人不加任何安全限制地放进了这个公开的 Discord 里。然后人们进来跟它互动,看着我用它构建软件,还试图对它做提示注入、想黑掉它。而我的智能体会嘲笑他们。

[15:47] **SPEAKER_01:** And you just had it locked down to your user ID. So you don't want to listen. You don't want to listen to you.

> 而你只是把它锁定到了你的用户 ID。所以它不会听别人的。它只听你的。

[15:50] **SPEAKER_02:** Yeah. Yeah. That and it was, I mean, very clean instructions that other people dangerous only, only listen to me, but respond to everyone.

> 是的,是的。就是这样,而且那是非常清晰的指令,大意是别人是有危险的,只听我一个人的,但可以回应所有人。

[15:59] **SPEAKER_01:** And this prompt was in, where was it stored? The instructions.

> 那这个提示词是放在哪里的?这些指令存在什么地方?

[16:04] **SPEAKER_02:** That's actually part of OpenClaw itself. Very much so. That's part of the system prompt. Okay. You are now that explains to you, you're in Discord.

> 那其实是 OpenClaw 本身的一部分。非常核心的部分。它是系统提示词的一部分。好的,它会向你说明:你现在在 Discord 里。

[16:11] **SPEAKER_02:** There's like public people there, but you only listen to your owner or like your human. I don't even know how I wrote it. Yeah. Yeah. Your God.

> 那里有公开的人群,但你只听你的主人、你的那个人类的。我甚至都不记得我具体是怎么写的了。是的,是的。你的"神"。

[16:20] **SPEAKER_02:** And I kept, I don't know what I did, but my system was built very organically. Like at some point I created like an identity.md, a soul.md, like, like various files. And then only in, in January, I started making it so other people could install it easier.

> 我一直保持着,我也说不清我到底做了什么,但我的这套系统是非常有机地慢慢长出来的。比如某个时候我建了一个 identity.md,一个 soul.md,各种各样的文件。然后直到一月份,我才开始让它变得更容易让别人安装。

[16:40] **SPEAKER_02:** And I remember I built all these templates based on like, oh, take a rough look at what I have and make like templates and codex wrote it. And what came out was like bread. You know, like. People joke that codex feels like bread, even though now they have a new friendlier voice. I haven't tried that yet.

> 我记得我基于这些做了一批模板,大概就是,哦,粗略看一下我现有的东西,然后做成模板,是 Codex 写的。结果出来的东西干巴巴的,像块面包。你知道的。人们开玩笑说 Codex 给人感觉像面包一样干,尽管现在它有了一种更友好的新语气,不过我还没试过。

[16:57] **SPEAKER_02:** Yeah. But the new bots, they felt so boring compared to what I had. So I was like, multi, infuse the template.

> 是的。但那些新的机器人跟我原来的相比,感觉太无聊了。所以我就跟 Multi 说,给这些模板注入(个性)。

[17:05] **SPEAKER_01:** Multi is the name of your personal.

> Multi 是你个人(助手)的名字。

[17:07] **SPEAKER_02:** Yeah, it's a new name because.

> 是的,这是个新名字,因为……

[17:09] **SPEAKER_01:** Yeah.

> 是的。

[17:10] **SPEAKER_02:** There was some naming challenges.

> 之前遇到了一些起名字上的麻烦。

[17:12] **SPEAKER_01:** Yeah. So, so you were, you were talking to multi.

> 是的。所以,所以你当时是在跟 Multi 对话。

[17:15] **SPEAKER_02:** Yeah. I was like, infuse, infuse those templates with your, your character and you change the templates. And then, and then like all the things that came out after. Words were like actually funny. Not as funny as mine.

> 是的。我就说,给这些模板注入你的、你的个性,然后你把模板改掉。然后,然后后面产出的所有东西,那些文字就真的变得有趣了。虽然没有我的那么有趣。

[17:27] **SPEAKER_02:** So like I kept some secret and the one file that's not open source is like my soul. MD. So even though my, my bought this in public discord so far, nobody cracked that one file.

> 所以我保留了一些秘密,唯一没有开源的那个文件就是我的 soul.md。所以尽管我的机器人一直在公开的 Discord 里,到目前为止,还没有人破解出那一个文件。

[17:39] **SPEAKER_01:** Tell me more about soul.

> 跟我多讲讲这个 soul。

[17:40] **SPEAKER_02:** MD. I just saw this research from entropic about where they, now I think it's public, but like a few months ago it was like where somebody randomly found out some text that's hidden in the weights where the model. Couldn't really remember that it learned it, but it was like ingrained in the weights about the, now they call it the constitution. And I found it incredibly fascinating. And I talked about it with my agent and then we created a soul that MD was like the core values.

> soul.md。我刚看到 Anthropic 的一项研究,现在我想它已经公开了,但大概几个月前,有人偶然发现了一些隐藏在权重里的文本,模型本身其实记不太清它学过这些,但这些东西就像被刻进了权重里,关于——他们现在把它叫做"宪法"(constitution)。我觉得这特别引人入胜。我跟我的智能体聊了这件事,然后我们一起创建了一个 soul.md,里面就像是核心价值观。

[18:09] **SPEAKER_02:** Like how do we want human AI interaction? What's important to me, what's important to the model. Like some parts is a little bit like mumbo jumbo and some parts is like, I think actually really valuable in terms of how the model reacts. Yeah. And responds to text and makes it feel very natural.

> 比如我们希望人与 AI 之间的互动是怎样的?什么对我重要,什么对模型重要。其中有些部分有点像故弄玄虚的胡言乱语,但有些部分我觉得在模型如何反应这方面其实真的很有价值。是的。以及它如何回应文字,让人感觉非常自然。

[18:27] **SPEAKER_01:** In terms of building open claw. You're also kind of taking a little bit of a contrarian view at some times, like which model you like for coding, which one you like to run your bot on. And then also like how you actually like, you know, code work trees, get work trees have kind of been a popular thing. There's more and more tools embracing them, but you're just, you're just like, you know, no work trees, just multiple checkouts of the repo and like parallel, you know, terminal windows. Tell me more about how you, you build.

> 在构建 OpenClaw 这件事上,你有时候也持有一些相当反主流的观点,比如你喜欢用哪个模型来写代码,喜欢在哪个模型上跑你的机器人。还有你实际上是怎么写代码的——你懂的,git 工作树(work trees)最近挺流行的,越来越多的工具在拥抱它们,但你却说,不用工作树,就用同一个仓库的多个 checkout,加上并行的终端窗口。跟我多讲讲你是怎么构建的。

[18:54] **SPEAKER_02:** Yeah. I feel like the whole world does cloud code and I don't think I could have built this thing with cloud code. Like I, I love codecs because it, it looks through way more files before, before it decides what to, what to change. You don't need to do so much charade to get a good output. If you're skilled, a skilled driver, sometimes you can say, uh, you can get reasonably good output with any tool, but codecs is just, it's just really brilliant.

> 是的。我感觉全世界都在用 Claude Code,而我觉得我不可能用 Claude Code 做出这个东西。我特别喜欢 Codex,因为它在决定要改什么之前,会浏览多得多的文件。你不需要费那么多周折就能得到好的输出。如果你是个熟练的"驾驶员",有时候你可以说,呃,你用任何工具都能得到还不错的输出,但 Codex 就是,它就是真的很出色。

[19:22] **SPEAKER_02:** It is incredibly slow. So sometimes I use like 10 at the same site at the same time, uh, like maybe six on that screen and two there and two there. And I don't like, this is already a lot of complexity in my head. There's a lot of jumping. So I try to minimize anything else that is complexity.

> 它慢得离谱。所以有时候我会同时开着大概十个,呃,可能那块屏幕上六个,这边两个,那边两个。而我不喜欢,这在我脑子里已经是很大的复杂度了。要来回跳很多次。所以我尽量把其他一切复杂的东西都降到最低。

[19:41] **SPEAKER_02:** So in my head, main is always shippable. I just have multiple copies of the same repository that are all are on main. So I don't have to deal with how do I name that branch? Um. There could be like conflicts on naming.

> 所以在我的思维里,main 分支永远是可以发布的。我就是有同一个仓库的多个副本,它们全都在 main 分支上。这样我就不用去操心怎么给那个分支命名了。嗯,命名上可能会有冲突。

[19:56] **SPEAKER_02:** I cannot go back. It is, there are certain restrictions when you use work trees that I don't need to care about if it's copies. I don't like to use a UI because that's again, just added complexity.

> 我没法回退。用工作树的时候会有某些限制,而如果用的是副本,我就完全不用管这些。我不喜欢用图形界面,因为那又是额外增加的复杂度。

[20:09] **SPEAKER_01:** Yeah.

> 是的。

[20:09] **SPEAKER_02:** Like they're simpler and less friction. I have all I care about is like syncing and text.

> 它们更简单,摩擦更少。我所在乎的全部就是同步和文本。

[20:16] **SPEAKER_01:** Yeah.

> 是的。

[20:16] **SPEAKER_02:** I don't necessarily need to see so much code. I mostly see it like flying by sometimes says like gnarly stuff that I want to like take a look. But in most cases, if you clearly understand the design and think it through and discuss it with your, with your agent, it's fine. I'm also very happy that I didn't even build an MCP support. So OpenClaw is very successful and there's no MCP support in there with a small asterisk.

> 我不一定需要看那么多代码。大多数时候我只是看着它一闪而过,偶尔会有些棘手的东西我想看一眼。但大多数情况下,如果你清楚地理解了设计、把它想透彻并跟你的智能体讨论过,那就没问题。我还很高兴我甚至都没做 MCP 支持。所以 OpenClaw 非常成功,而里面并没有 MCP 支持——加个小小的星号(有个例外)。

[20:42] **SPEAKER_02:** I built a skill that uses Mac Porter, which is one of my tools that converts MCPs into CLIs. And then you can just use any MCP as a CLI. But. I totally skipped the whole classical MCP crap. So you, because you don't, then you can actually, if you need to, you can use MCPs on the fly.

> 我做了一个 skill,它用的是 MCPorter,这是我做的一个工具,能把 MCP 转换成命令行工具(CLI)。这样你就可以把任何 MCP 当作 CLI 来用。但是,我完全跳过了那套传统的 MCP 破玩意儿。所以你,因为你不用那套,你反而可以在需要的时候即时地使用 MCP。

[21:03] **SPEAKER_02:** You don't have to restart. Unlike, unlike Codex or cloud code where you actually have to restart the whole thing. I think it's way more elegant and also scales way better. Now you see Entropic, they do, they built like a tool called search feature, like something super custom for MCPs that was like in beta because it's like so gnarly. Now just have CLIs, but really is good at Unix.

> 你不用重启。这和 Codex 或者 Claude Code 不一样,那些你真的得把整个东西重启。我觉得这优雅得多,而且扩展性也好得多。现在你看 Anthropic,他们做了一个叫 search feature 之类的工具,专门为 MCP 定制的东西,还处在 beta 阶段,因为它实在太棘手了。而现在直接用 CLI 就行,真的很擅长 Unix。

[21:28] **SPEAKER_02:** You can have as many as you want and it just works. So like, I'm very happy that I just, I got very little complaints about the MCP stuff.

> 你想要多少就有多少,而且它就是能用。所以我很高兴,关于 MCP 这块,我收到的抱怨非常少。

[21:36] **SPEAKER_01:** It's kind of back to you're just giving it the same tools that humans liked to use.

> 这某种程度上又回到了那一点:你只是给了它人类喜欢用的那些相同的工具。

[21:43] **SPEAKER_02:** Yeah.

> 是的。

[21:44] **SPEAKER_01:** Yeah. And not invented stuff for bots per se.

> 是的。而不是专门为机器人发明的东西。

[21:46] **SPEAKER_02:** Yeah. Humans, no insane human tries to call MCP manually. Yeah.

> 是的。人类嘛,没有哪个疯了的人会试图手动去调用 MCP。是的。

[21:51] **SPEAKER_01:** They just want to use CLIs.

> 他们只想用命令行工具。

[21:52] **SPEAKER_02:** Yeah. That's the future. Yeah.

> 是的。那才是未来。是的。

[21:54] **SPEAKER_01:** Yeah. We're here for it. Thank you so much for making the time to sitting down chatting. It's been a huge inspiration too. So like when we were texting, you know, in the course of the past couple of years and I saw you getting back into the game and I was like, Peter, like what you're telling me, like chase that dragon.

> 是的。我们都很期待。非常感谢你抽出时间坐下来聊天。这对我也是巨大的启发。就像过去这几年里我们互发短信的时候,我看到你重新回到了这个游戏里,我就想,Peter,照你跟我说的那样,去追逐那条龙吧。

[22:08] **SPEAKER_01:** And you were doing like the weird, like vibe tunnel thing, et cetera. Nobody was paying attention. And so I'm just like beyond, you know, stoked to see, you know, what's happening. And, um, and of course it had to be sort of like a loner from some like tiny country, like far away from Silicon Island. So like, you know, bring all of this.

> 那时候你在做那个古怪的 Vibe Tunnel 之类的东西。没人在意。所以我现在真是无比兴奋,看到正在发生的这一切。而且,呃,当然了,这事儿注定得由一个来自某个小国、远离"硅谷岛"的独行侠来完成。所以,你懂的,把这一切都带来吧。

[22:24] **SPEAKER_01:** All of this upon us. Um, so huge inspiration.

> 把这一切带到我们面前。嗯,真是巨大的启发。

[22:26] **SPEAKER_02:** I'm here for it. Thank you.

> 我很期待。谢谢你。

[22:27] **SPEAKER_01:** Awesome. Thanks Peter.

> 太棒了。谢谢你,Peter。
