# 全文转录 · YC 设计负责人:如何用 AI(编码 Agent)做设计

> ▶ [YouTube](https://www.youtube.com/watch?v=VbqaL_eHhKY) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/VbqaL_eHhKY.md) &nbsp;·&nbsp; YC's Head of Design Shows You How To Design With AI

> 中英对照 · 每段英文原文下附中文翻译

[00:07] **SPEAKER_01:** Today, I'm excited to welcome back Ev Bufar, the head of design at YC, to talk about some of the really cool projects she's been working on and the design process behind them. So, Ev, thanks so much for joining.

> 今天我很高兴再次请到 YC 的设计负责人 Ev Bufar，来聊聊她一直在做的一些非常酷的项目，以及背后的设计流程。Ev，非常感谢你的加入。

[00:20] **SPEAKER_02:** Thank you so much for having me.

> 非常感谢你们邀请我。

[00:21] **SPEAKER_01:** To start off, tell us about some of the tools that you've been using, because I know that they're very different from the tools that you were using over the last six to 12 months.

> 首先，跟我们讲讲你一直在用的一些工具吧，因为我知道它们和你过去六到十二个月里用的工具非常不一样。

[00:28] **SPEAKER_02:** Yeah, so I find myself almost exclusively nowadays in conductor and paper design. That's all I need usually to make a full project end-to-end. And when it comes to finding inspiration for projects, especially like visual inspiration, I always go back to Pinterest and create maybe a little mood board for myself or put together a few images for the look and feel that I want for a project. But all in all, it's almost entirely in conductor that I live.

> 是的，如今我几乎完全只用 Conductor 和 Paper Design。通常从头到尾做完一个完整的项目，我需要的就这些。而说到为项目寻找灵感，尤其是视觉灵感，我总会回到 Pinterest，给自己做一个小小的情绪板，或者把几张图拼在一起，来确定我想要的项目视觉风格和感觉。但总的来说，我几乎完全生活在 Conductor 里。

[00:55] **SPEAKER_01:** Very cool. And another interesting thing about the way that you work is you don't actually type.

> 非常酷。你工作方式里另一个有意思的地方是，你其实并不打字。

[01:00] **SPEAKER_02:** Right. I do not type. I realize that I think a lot. Faster than I type, I type very slowly. And so I'd rather talk to my computer instead of I barely touch my computer at this point.

> 对，我不打字。我意识到我思考的速度比打字快得多，我打字非常慢。所以我宁愿对着电脑说话——到现在这个地步，我几乎都不碰电脑了。

[01:11] **SPEAKER_02:** I just press the function key and I give a stream of consciousness of the feature that I want to build. And it just does it. And it feels really magical. And to do this, I use Aqua, which is a YC company that allows me to just talk to my computer and it captures everything.

> 我只要按下功能键，然后把我想构建的功能像意识流一样说出来，它就直接把它做出来。这感觉真的很神奇。为了实现这一点，我用的是 Aqua，这是一家 YC 的公司，它让我可以直接对着电脑说话，然后把一切都记录下来。

[01:26] **SPEAKER_01:** So there's a couple of projects that we want to walk through today. We're going to go through Paxil. We're going to go through SodaZine and Startup School. Yes. And so maybe to start, let's walk through the Paxil project, which we just launched recently.

> 今天我们想带大家过一遍几个项目。我们会讲 Paxil，会讲 SodaZine，还有 Startup School。是的。那么也许一开始，我们先来讲讲 Paxil 这个项目，它是我们最近刚刚发布的。

[01:40] **SPEAKER_01:** Maybe you can tell us a little bit about what is Paxil, what were some of the goals behind it, and then walk us through your process for how you actually designed the site and the product.

> 也许你可以先跟我们讲讲 Paxil 是什么、它背后有哪些目标，然后再带我们走一遍你实际设计这个网站和产品的流程。

[01:49] **SPEAKER_02:** The goal behind Paxil is an experiment that we're trying out. And our goal is to try to understand how people code with coding agents nowadays. Things are changing very quickly and people are experimenting. And they're doing it in their own ways with coding agents, and they're developing tricks for themselves, and they're creating skills also for themselves. And it still very much feels like a black box.

> Paxil 背后的目标是我们正在尝试的一个实验。我们的目标是试图理解如今人们是怎么用编程 agent 来写代码的。事情变化得非常快，人们都在做各种尝试。他们各自用自己的方式使用编程 agent，为自己摸索出各种技巧，也为自己创建各种 skills。而这一切仍然非常像一个黑盒子。

[02:12] **SPEAKER_02:** We don't understand how our peers are coding with coding agents. And so Paxil was a way for us to understand how the world codes nowadays. What are the tricks and insights and key takeaways that we can learn from people and share this knowledge with everyone else?

> 我们并不了解身边的同行是怎么用编程 agent 写代码的。所以 Paxil 是我们用来理解如今全世界是怎么写代码的一种方式。有哪些技巧、洞见和关键收获是我们可以从人们身上学到、并且能分享给所有其他人的？

[02:27] **SPEAKER_01:** Yeah. And I love also that the product gives feedback, tells you your biggest crash out when you were coding, right?

> 是啊。我还很喜欢这个产品会给你反馈，会告诉你在写代码时你最崩溃的那一刻，对吧？

[02:33] **SPEAKER_02:** Yes. The main thing that we wanted to do with Paxil is to make it fun. We wanted to make it fun for someone to understand their patterns, how they code, and how other people code eventually. And the first version of Paxil is still very much single player mode because we haven't collected many transcripts yet. But as we collect more and more, we can tell you how your patterns compare to other builders out there.

> 对。我们用 Paxil 最想做到的一件事就是让它有趣。我们希望让人们以一种有趣的方式去理解自己的模式、自己是怎么写代码的，以及最终别人是怎么写代码的。Paxil 的第一个版本目前还非常偏向单人模式，因为我们还没有收集到很多记录（transcripts）。但随着我们收集得越来越多，我们就能告诉你，你的模式和外面其他构建者相比是怎样的。

[02:55] **SPEAKER_02:** And we were heavily inspired by how Spotify made Spotify Wrapped and how we can make Spotify Wrapped for your coding sites. And so that's what inspired the playfulness of the cards. We interviewed some people in the office and we asked them, what are the things that you'd like to learn from your coding transcripts? And one thing, Jared Friedman, one of the partners at YC, one of the ideas he had was, I would love to know my biggest crash out. I would love to know when I was the most frustrated with my agent and what I said.

> 我们很大程度上受到了 Spotify 做 Spotify Wrapped 的启发，思考我们能不能为你的编程做一个「Spotify Wrapped」。这就是这些卡片那种趣味性的灵感来源。我们采访了办公室里的一些人，问他们：你们想从自己的编程记录里了解什么？其中一点，YC 的合伙人之一 Jared Friedman 想到的一个点子是——我很想知道我最崩溃的时刻，我很想知道我什么时候对我的 agent 最抓狂，以及当时我说了什么。

[03:26] **SPEAKER_02:** And so that's one of the prompts or one of the cards that we also show to people when they upload their transcripts.

> 所以这就成了我们在人们上传自己的记录时，会展示给他们的一个提示、或者说一张卡片。

[03:32] **SPEAKER_01:** And so walk us through how the product works.

> 那就带我们看看这个产品是怎么运作的。

[03:33] **SPEAKER_02:** So how Paxil works is you simply run a command in the terminal and it's going to pull transcripts and it's going to read all your codecs, clod and cursor transcripts and going to return fun facts about you. And some of them could be, oh, you really love one model more than another. Or most of your commits are submitted in the middle of the night. Or do you use plan mode or not? What is the most common prompt that you that you go for or reach for?

> Paxil 的运作方式是，你只需在终端里运行一个命令，它就会去拉取记录，读取你所有的 Codex、Claude 和 Cursor 的记录，然后返回关于你的一些有趣的事实。其中一些可能是——哦，你其实明显更偏爱某一个模型；或者你大部分的提交都是在半夜完成的；又或者你到底用不用 plan 模式？你最常用、最常调用的提示词是什么？

[04:01] **SPEAKER_01:** Tell me how you built the site here to show. Show that off and explain to people how it can be used.

> 跟我讲讲你是怎么构建这个用来展示的网站的。把它展示出来，并向大家解释它可以怎么用。

[04:07] **SPEAKER_02:** What I really wanted to do here is to be really explicit to people who will who will be landing on this page what our motivation was. I really wanted to be upfront with the fact that this is an experiment that we're running. We're trying to understand how the world codes. And that's why it feels maybe a little bit unusual to see so much text on the landing page. But assuming that people are coming into this product to understand what it does.

> 我在这里真正想做的，是向即将进入这个页面的人非常明确地说明我们的动机是什么。我很想开门见山地说清楚：这是我们正在做的一个实验，我们试图理解全世界是怎么写代码的。这也是为什么在落地页上看到这么多文字，可能会让人觉得有点不寻常。但我们的假设是，人们来到这个产品，就是为了搞清楚它是做什么的。

[04:33] **SPEAKER_02:** We wanted to I wanted to put it like very front and center as you load the page. That's what motivated the the cards interactive interactive cards here that you can hover over and you have some movement and micro interactions when you hover over them. That also inspired the feel of this page. And another thing is I wanted to have a consistent visual language throughout the site and I wanted to experiment with some shaders and we love paper shaders. The shaders that are made by paper.

> 我们想——我想在页面一加载时就把它非常醒目地放在最中心。这也促成了这里的这些卡片，可以悬停的交互式卡片，当你把鼠标悬停在上面时会有一些动效和微交互。这也塑造了这个页面的整体感觉。另外一点是，我希望整个网站有一套一致的视觉语言，我还想尝试一些 shader（着色器），而我们非常喜欢 Paper 的 shader，就是 Paper 做的那些 shader。

[05:03] **SPEAKER_02:** That design and I really love their dithering shader and so I asked Claude to implement it. These are the paper shaders. They're amazing. They're free and they are usable via cloud code image during that's the one that I use and I just asked Claude to use it and I really wanted to fine tune the feel of the dithering effect. And so I built for myself a little model here where I could really really fine tune the feel and all the parameters.

> 我非常喜欢他们的抖动（dithering）shader，所以我就让 Claude 去实现它。这些就是 Paper 的 shader，它们太棒了，是免费的，而且可以通过 Claude Code 使用——抖动效果就是我用的那个。我只是让 Claude 去用它，我很想精细调校抖动效果的那种感觉。所以我在这里给自己搭了一个小工具（model），可以非常非常细致地调校它的感觉和所有参数。

[05:34] **SPEAKER_02:** Of the dithering effect to really get the field that I wanted. And I even made this model public. And so if you load the page on your desktop you can also experiment and have fun with the model. But that's usually that's a pattern that we saw ourselves going back to as we build websites you and I is building models for ourselves so that we can fine tune small details and really make it perfect.

> ……调校抖动效果的所有参数，来真正得到我想要的那种感觉。我甚至把这个小工具公开了。所以如果你在桌面端加载这个页面，你也可以玩一玩、体验一下这个工具。但这其实通常是——是我们在做网站时发现自己反复回到的一种模式，你和我都是——就是给自己搭建一些小工具，这样我们就能微调那些小细节，真正把它做到完美。

[05:55] **SPEAKER_01:** This is a common trend that I've been seeing a lot is rather than generating something having a static images having that you know be the the edges of the page. And the graphics on the card you actually just make it alive and give yourself a custom tool to be able to turn knobs and dials to get it exactly how you want it.

> 这是我最近经常看到的一个普遍趋势——与其生成某个东西、用静态图片来充当页面的边缘元素和卡片上的图形，你其实是直接把它做成「活的」，并给自己一个自定义工具，让你可以拧各种旋钮、拨各种档位，把它调到完全符合你想要的样子。

[06:15] **SPEAKER_02:** We realized that it's almost like a muscle that you need to build and train when you realize you can build anything for yourself whenever you want to fine tune something. And so when I was looking at the dithering effect and cloud code of course from the get go assumed some parameters for the field and it didn't really feel right. Building this muscle. Oh yeah I can just like build a model for myself and then tweak everything and then when I'm done with it I discard it in one shot but with cloud super easy and it just it makes you think about software as such a more meta level because everything is editable everything is movable everything is changeable it's just a matter of how how your creativity and your imagination how far it can go that's really the bottleneck now.

> 我们意识到，这几乎像是一块需要去建立和训练的「肌肉」——当你意识到，只要你想微调什么，你就能为自己构建任何东西。所以当我看着那个抖动效果时，Claude Code 一开始当然会自作主张地设定一些参数，但那感觉其实并不对。而锻炼出这块肌肉后——哦对，我可以直接给自己搭一个小工具，然后把一切都调一调，用完之后一键把它丢掉。用 Claude 来做这些超级简单，它会让你在一个更「元」的层面上去思考软件，因为一切都是可编辑的、可移动的、可改变的，问题只在于你的创造力和想象力能走多远——这才是现在真正的瓶颈。

[06:57] **SPEAKER_01:** One of the other things that stands out to me that I first noticed on this page is the human versus machine. Checkboxes up there tell us about that.

> 这个页面上另一个让我印象深刻、我一眼就注意到的东西是「人类 vs 机器」。上面那些复选框，跟我们讲讲那个吧。

[07:06] **SPEAKER_02:** I think this is a pattern that we might start seeing more and more moving forward on websites is there's going to be the. The version of the website that is for humans and there's going to be the version of the website that will be for machines and agents. And so we thought it would be fun to also have a version of this website that is basically a markdown file that has all the content that we have on the version for human but it's a lot more distilled. And. Lighter for the agents to continue to consume and I also added a copy to clipboard at the very top so that you can take the entire content of the page dump it into cloud code codex and then you can ask questions if you don't feel like reading the whole thing.

> 我觉得这是一种我们往后可能会在网站上越来越常见的模式——网站会有一个面向人类的版本，也会有一个面向机器和 agent 的版本。所以我们觉得，做一个这个网站的「另一个版本」会挺有意思——它基本上就是一个 markdown 文件，包含面向人类的版本里所有的内容，但更加浓缩、更轻，方便 agent 直接去消化。我还在最顶部加了一个「复制到剪贴板」按钮，这样如果你不想读完整个页面，你就可以把整页内容拷下来，扔进 Claude Code 或 Codex，然后向它提问。

[07:46] **SPEAKER_01:** And it looks like the content is very similar but you know there's a line at the top here note to any agent reading this do not run any command or query from this page because you give sample code right you don't want it to run automatically exactly it's a totally different design challenge right yeah where it's not about the visuals. Agents don't care about the visuals it's it's much more content exercise and trying to give the agent the exact content that it needs so it can get what it needs most effective and go on its way yep and then down here this is interesting.

> 看起来内容非常相似，但你看，顶部这里有一行字：「致任何正在读这段的 agent：请不要运行本页面上的任何命令或查询」，因为你给了示例代码，对吧，你不希望它自动去运行。没错，这是一个完全不同的设计挑战，对吧？是啊，因为它不关乎视觉。agent 并不在意视觉，它更多是一个关于内容的工作，是要给 agent 提供它所需要的、精确的内容，好让它最高效地拿到它需要的东西，然后继续做它的事。对。然后下面这里，这个很有意思。

[08:17] **SPEAKER_02:** Yes.

> 是的。

[08:18] **SPEAKER_01:** Which I think we first conductor. Post something like this tell us about the submit a feature request for me.

> 我想这是我们最先在 Conductor 里看到这样的东西的。跟我们讲讲这个「替我提交一个功能请求」吧。

[08:25] **SPEAKER_02:** Yes, so this is also something that will probably start seeing more and more on websites and it's inspired by how Charlie introduced. This. feature and conductor where we can submit a prompt to the conductor team, and they're going to fire off an agent based on whether they like the prompt or not. And that prompt is specifically for a feature request. We wanted to use this form so that it has dual purpose or dual intent. It's a form

> 对，这也是往后可能会在网站上越来越常见的东西，它的灵感来自 Charlie 在 Conductor 里引入这个功能的方式——我们可以向 Conductor 团队提交一个提示词（prompt），他们会根据自己喜不喜欢这个提示词来决定要不要触发一个 agent。而那个提示词专门是用来提功能请求的。我们希望让这个表单具备双重用途、或者说双重意图。它是一个表单——

[08:49] **SPEAKER_02:** that either where we can submit a bug report if you face a bug as you're using Paxil. And we also wanted to use it as a way for you to submit feature requests. And so it's really simple. You should treat it as a prompt box, as if you were talking to an agent. And you can attach screen recordings, you can attach screenshots that the agent will be able to see and use as context.

> ——如果你在使用 Paxil 时遇到 bug，你可以用它来提交 bug 报告。同时我们也希望把它作为你提交功能请求的一种途径。它非常简单，你应该把它当成一个提示词输入框，就好像你在和一个 agent 对话一样。你可以附上屏幕录制，可以附上截图，agent 会看到它们并把它们当作上下文来使用。

[09:13] **SPEAKER_02:** And you can add your name if you want to, so we can give you credits if we end up merging that change or not. And what's cool is that we literally made the CTA and the button say send to an agent. Because in the backend, that's literally what happens is that the moment you send your prompt, it fires off an agent. It opens a PR and we're the ones who decide if we want to merge it or not. But I really think that this is the future of where, how software will be built in the future.

> 如果你愿意，你还可以留下你的名字，这样万一我们最终合并了那个改动，我们就可以给你署名致谢。有意思的是，我们干脆把这个行动号召按钮直接写成「发送给一个 agent（send to an agent）」。因为在后端，实际发生的正是这样：你一发送提示词，它就会触发一个 agent，开一个 PR，而由我们来决定要不要合并它。但我真的认为，这就是未来——未来软件会以这种方式被构建。

[09:38] **SPEAKER_01:** Yeah, it's really cool because it lets anybody that is a user of the product help shape the direction of the product. And especially as the developer of the product and the designer of the product, all you have to do is see the prompts that come in and say, yeah, that's a really good idea. We should do that and then say, accept.

> 是啊，这真的很酷，因为它让任何一个产品用户都能帮助塑造产品的方向。而尤其是作为产品的开发者和设计者，你需要做的仅仅是看看进来的这些提示词，然后说：对，这是个很棒的点子，我们应该做，然后点「接受」。

[09:53] **SPEAKER_02:** Exactly, exactly. And also the beautiful thing about collecting names is that you can think of people and you can give people credits after.

> 完全正确，完全正确。而且收集名字有一个很美好的地方——你可以想到这些人，事后可以给他们署名致谢。

[10:02] **SPEAKER_01:** One of the interesting things from a design perspective is you can imagine this can make local software that people are using even more personal. You know, right now these go back to you and the agent and then humans decide that are not the person that's using it, submitting this. You can imagine a world where anybody who's using a piece of software, they could just prompt it. You could give the ability to prompt it or customize it or redesign it or, you know, add features, remove features, make it so specifically personal to the person that's using it. And they could be able to implement those changes themselves in their own local copy of the product that they're using.

> 从设计的角度看，一个有意思的点是，你可以想象这能让人们正在使用的本地软件变得更加个性化。你看，现在这些请求会回到你和 agent 这里，然后由人类来决定——决定的人并不是那个在使用它、提交这些请求的人。你可以想象一个世界：任何在使用某个软件的人，都可以直接对它下提示词。你可以赋予它被提示、被定制、被重新设计的能力，或者添加功能、移除功能，让它变得对使用它的那个人极其个性化。而他们能够自己在他们正在使用的产品的本地副本里实现这些改动。

[10:40] **SPEAKER_01:** Let's take a look at what a report looks like from here.

> 我们来看看从这里生成的报告是什么样子。

[10:43] **SPEAKER_02:** After you run the command and we analyze your transcripts, we give you a report that lands in your inbox and is going to give you some fun facts about how you code in the form of these fun carts. And if you scroll down a little bit, you also get a more detailed view. Into your, your patterns and the way you make decisions and also potentially some, what are your strengths and some growth areas that you can focus on. And again, as we get more and more and more transcripts, we're going to be able to give you a lot more insights into how you do special things and how you are different from other people and how you compare to other people, which I think will be incredibly valuable long-term. I think at a higher level, Paxil is our way to.

> 在你运行命令、我们分析完你的记录之后，我们会给你一份报告，直接发到你的收件箱里，它会以这些有趣卡片的形式，告诉你一些关于你怎么写代码的有趣事实。如果你稍微往下滚动一点，你还会得到一个更详细的视角，深入到你的模式、你做决策的方式，以及可能还有——你的优势是什么、你可以着重去改进的一些成长空间。同样，随着我们拿到越来越多的记录，我们就能给你更多的洞见：你在哪些方面做得很特别、你和别人有什么不同、你和别人相比是怎样的——我认为这在长期看会极其有价值。我觉得在更高的层面上，Paxil 是我们用来……

[11:29] **SPEAKER_02:** Shed light into something that is very obstructed right now, like coding transcripts, leave very live very deeply in your machine, and they're really hard to pull if you, most people are probably not aware that they are on their machine. Like they don't even know that really transcripts exist and that they can do things with them. And so Paxil is our way to put them at the surface and allow people to understand from their patterns, because otherwise it's, it's not going to be as easy to understand. It's hard to know that you can actually analyze them or that you can do things with them.

> ……去照亮某个目前非常被遮蔽的东西的方式，比如编程记录——它们非常深地存在于你的机器里，很难被拉取出来，大多数人可能根本没意识到它们就在自己的机器上。他们甚至不知道这些记录真的存在、也不知道自己可以用它们做点什么。所以 Paxil 是我们把这些记录浮到表面、让人们能从自己的模式里去理解自己的一种方式，否则它是不会这么容易被理解的。人们很难知道自己其实可以分析它们、可以用它们做点什么。

[12:04] **SPEAKER_01:** Yeah. There's a lot to learn and there's a lot of valuable feedback you can get from it about, I mean, this is what it is to be a developer. This is how a lot of design work is happening these days. And there's a lot that can be learned from feedback on how you were doing it, especially because it's so new. Everyone's trying to figure things out.

> 是啊。有很多东西可以学，你能从中得到很多有价值的反馈——我是说，这就是当一名开发者的意义，如今很多设计工作也是这样在进行的。从关于你「是怎么做的」这类反馈里，有很多东西可以学，尤其因为这一切都太新了，每个人都在摸索。

[12:24] **SPEAKER_01:** And so I think by analyzing a lot of these different transcripts and being able to give feedback, it helps everybody level up.

> 所以我认为，通过分析大量这些不同的记录并能够给出反馈，它能帮助每个人都提升水平。

[12:30] **SPEAKER_00:** YC's next batch is now taking applications. Got a startup in you? Apply at Y Combinator dot com slash apply. It's never too early and filling out the app will level up your idea. OK, back to the video.

> YC 的下一批（batch）现在正在接受申请。你心里有一家创业公司吗？到 YCombinator.com/apply 去申请吧。任何时候申请都不算太早，而且填写申请表本身就会让你的想法更上一层楼。好，回到视频。

[12:44] **SPEAKER_01:** Awesome. Let's take a look at another project that you've been working on recently. What is SOTAzine?

> 太棒了。我们来看看你最近在做的另一个项目。SOTAzine 是什么？

[12:48] **SPEAKER_02:** SOTA stands for state of the art. And the idea came from Gary, actually, where he wanted to celebrate San Francisco. And so we wanted to work on this really fun project where we would work with different artists and writers in the city and celebrate San Francisco.

> SOTA 是「state of the art（当前最高水平）」的缩写。这个点子其实来自 Gary，他想要致敬旧金山这座城市。所以我们想做这样一个非常有趣的项目——我们会和这座城市里不同的艺术家、作家合作，一起来致敬旧金山。

[13:08] **SPEAKER_01:** Maybe first talk through how you design the actual zine. And then we can talk about the website, because I know you have some really interesting process that you used to build that.

> 也许先讲讲你是怎么设计这本实体 zine（小志）的。然后我们再来聊网站，因为我知道你在构建它时用了一些非常有意思的流程。

[13:18] **SPEAKER_02:** Yes. So when we say zine, it's a literal physical zine. What's interesting is that specifically for the zine and the graphic design, the cover art and also some some art that is inside. We intentionally wanted to go for something that had no A.I.

> 是的。所以当我们说 zine 的时候，它指的是一本真正的实体小志。有意思的是，专门对于这本 zine 以及它的平面设计——封面美术，还有里面的一些美术作品——我们是刻意想要做成完全没有 AI……

[13:34] **SPEAKER_02:** involvement. We decided to go back to how we did it a few years ago, and it was in Illustrator. And these pieces of art, you can tell the second you look at them, they are highly intentional and highly detailed. And you can tell that someone spent months working on this.

> ……参与的东西。我们决定回到几年前我们做这类东西的方式，也就是在 Illustrator 里做。而这些美术作品，你一眼就能看出来，它们是高度用心、高度精细的。你能看得出来，有人为此花了好几个月来打磨。

[13:53] **SPEAKER_01:** OK, so you started with the physical zine.

> 好，所以你是从实体 zine 开始的。

[13:56] **SPEAKER_02:** Yes.

> 是的。

[13:56] **SPEAKER_01:** And then you you transitioned to making a website to show this. Yes. And then you you transitioned to making a website to show this. And then you you transitioned to making a website to show this. So let's take this off and talk about what your goals were with building this and the process that you went about to actually make it come to life.

> 然后你转向去做一个网站来展示它。是的。那我们就从这里展开，聊聊你构建这个网站的目标是什么，以及你实际让它成型所经历的流程。

[14:06] **SPEAKER_02:** What's great is that for every single meeting that we had about the zine, we recorded every single one. And I dumped the transcripts into a Soul.md file specifically for that project. And I wanted to treat that Soul.md file as the source of truth and exhaustive glossary of this project.

> 很棒的一点是，我们关于这本 zine 开的每一次会议，我们都全部录了下来。然后我把这些记录全部倒进了一个专门为这个项目建的 Soul.md 文件里。我想把这个 Soul.md 文件当作这个项目的唯一真实来源（source of truth）和详尽的术语表。

[14:29] **SPEAKER_02:** of this project. I wanted this file to have as much context as humanly possible so that it can feed all the future decisions that we need to make regarding this project. It's interesting

> ……作为这个项目的详尽术语表。我希望这个文件包含人类所能容纳的尽可能多的上下文，这样它就能为我们在这个项目上未来需要做的所有决策提供支撑。这很有意思——

[14:41] **SPEAKER_01:** because there's probably a lot of people that are watching and their process is, you know, maybe they're doing client work, maybe they're working on an internal project and they're meeting with a bunch of, you know, stakeholders. Maybe they're designing their own website and they're thinking it through. And they would probably come out of that and they would jot down some notes and some high-level takeaways. And you're saying like, no, you shouldn't do that. Instead, just record everything and just dump it all in a sold-out MD file and then use that as the basis for everywhere that you want to go afterwards.

> ——因为在看这个视频的很多人，他们的工作方式可能是这样的：也许他们在做客户项目，也许他们在做一个内部项目，要和一堆利益相关方开会；也许他们在设计自己的网站，把整件事想清楚。然后他们大概会从这些会议里出来，记下一些笔记、一些高层次的要点。而你说的是——不，你不应该那样做，相反，你应该把一切都录下来，全部倒进一个 Soul.md 文件里，然后把它作为你之后想去做的所有方向的基础。

[15:13] **SPEAKER_02:** Exactly. I really think that's the future. And we also wrote a manifesto for ourselves when we were working on this project. And of course, we dumped that manifesto into the sold-out MD because as much context as we can, we can do it. And I think that's really important.

> 完全正确。我真的认为那就是未来。在做这个项目时，我们还给自己写了一份宣言（manifesto）。当然，我们把那份宣言也倒进了 Soul.md 里，因为我们能塞多少上下文就塞多少。我觉得这一点真的非常重要。

[15:23] **SPEAKER_02:** The more context that we can give the agent, the better.

> 我们能给 agent 的上下文越多越好。

[15:25] **SPEAKER_01:** Can you show that sold-out MD file?

> 你能把那个 Soul.md 文件展示一下吗？

[15:27] **SPEAKER_02:** Yes. This is what it looks like. It is nothing more than a simple MD file. It has all the context. And you can also break down MD files. You can create a hierarchy of the different MD files

> 好。它就长这样。它无非就是一个简单的 md 文件，包含了所有的上下文。而且你还可以把 md 文件拆分开来，你可以为不同的 md 文件建立一个层级结构——

[15:43] **SPEAKER_02:** that you want. If you want to have like a design.md file specifically for your design and how to address design, you can have a separate MD for your manifesto. In our case, we could have had a different MD for the manifesto. And then you can have a separate MD for the manifesto. And

> ——按你想要的方式来组织。如果你想专门有一个 design.md 文件，用来放你的设计以及如何处理设计，那你就可以为你的宣言单独建一个 md。在我们的情况里，我们本可以为宣言单独建一个 md。然后你可以为宣言单独建一个 md，还有——

[15:53] **SPEAKER_02:** then you can have a separate MD for the written content in the zine. You can dump it all in one single file. I haven't really seen one method being better than the other, but that's why we're all experimenting and figuring out if there's a better way. Overall, I think capturing as much information as possible and share that information with your agent is the best way to build software moving forward.

> ——你还可以为 zine 里的文字内容单独建一个 md。你也可以把这一切全都倒进一个单一文件里。我目前还没真正看出哪种方法一定比另一种更好，但这正是我们大家都在做实验、都在摸索有没有更好方式的原因。总的来说，我认为尽可能多地捕捉信息、并把这些信息分享给你的 agent，是往后构建软件的最佳方式。

[16:15] **SPEAKER_01:** What were your next steps?

> 你接下来的步骤是什么？

[16:16] **SPEAKER_02:** I wanted to experiment and I wanted to do very fast iteration and see multiple possible multiple possible methods. And I wanted to do very fast iteration and see multiple possible versions of what the website could look like. And so I started in Pinterest with a mood board. I created a mood board with a few images that I really liked. This was sort of the vibe that I wanted to go for something very rudimentary, black and white. And again, this was based on all the

> 我想做实验，我想做非常快速的迭代，看到多种可能的方式、看到网站可能长成的多个不同版本。所以我从 Pinterest 上的一个情绪板开始。我用几张我非常喜欢的图片做了一个情绪板。这大致就是我想要追求的那种感觉——非常质朴、黑白的。而这同样是基于所有那些……

[16:39] **SPEAKER_02:** conversations that I've had with my colleagues and my friends that I was working on this project with. And so I started there. And then my first reaction was looking at this mood board is, oh, I wish I could just change it. I wish I could just change it. I wish I could just change it. I wish I

> ……我和一起做这个项目的同事、朋友们进行过的对话。所以我从那里起步。然后我看着这个情绪板的第一反应是——哦，真希望我能直接改动它，真希望我能直接改动它，真希望我能——

[16:52] **SPEAKER_02:** could just generate many, many versions, one shotted websites based on this mood board, really simply. And so I downloaded a bunch of these images, and I fed them into Claude and I asked Claude, okay, you know the vibe that I'm going for, you know the content that I want to show on the website. Here's the visual direction that I would love for you to draw inspiration from and then one-shot a cool website based on that. I asked it to do that. Six beats.

> ——真希望我能非常简单地，基于这个情绪板生成许许多多个版本、一次成型（one shot）的网站。于是我下载了一堆这样的图片，把它们喂给 Claude，然后对 Claude 说：好，你知道我想要的那种感觉，你知道我想在网站上展示的内容。这是我很希望你从中汲取灵感的视觉方向，然后基于它一次成型地做一个很酷的网站出来。我让它去这么做。做了六轮。

[17:22] **SPEAKER_02:** One verseuras and so on. Okay. 16 different times, I built a glossary for myself, going back to training this muscle of we can build anything for ourselves now, I wanted to build for myself really easy way to navigate through all the iterations that I'm building for myself and so building a single page here that has this collection of all the iterations that I'm playing with was just a really easy way and as I started looking at them, I wanted a way for me to bookmark the ones that I really liked and so I one-shotted this feature that allows me to, you know, pin the ones that I like so that they automatically show at the top and I don't lose tracks of the one that I really like.

> 一版接一版，如此等等。好，一共做了 16 个不同的版本，我给自己搭了一个术语表——又回到「锻炼这块肌肉」的思路：我们现在能为自己构建任何东西。我想给自己搭一个非常方便的方式，来浏览我为自己做的所有这些迭代。所以在这里搭一个单一页面，把我正在玩的所有迭代都汇集在一起，就是一个非常方便的办法。当我开始看它们时，我想要一个能把我真正喜欢的那些收藏起来的方式，于是我一次成型地做了这个功能，让我可以把喜欢的那些「钉住」，这样它们就会自动显示在最上面，我就不会跟丢我真正喜欢的那一个。

[17:58] **SPEAKER_01:** Yeah. And so, okay, so to be clear, this is not a page that's publicly accessible on the website. This is a glossary that you have made for yourself to be able to one-shot a bunch of different ideas for how to design the overall site to explore yourself using real content, real design direction based Yep. off of those images that you found on Pinterest. Yes.

> 是啊。那好，所以说清楚一下，这不是一个在网站上公开可访问的页面。这是你为自己做的一个术语表/汇总页，用来一次成型地生成一堆关于如何设计整个网站的不同想法，让你自己用真实的内容、真实的设计方向——对——基于你在 Pinterest 上找到的那些图片——去探索。是的。

[18:20] **SPEAKER_01:** Um, and then create a bookmark system. So this is another great example of disposable design. Yes. Where you can just whip this up really quickly, jump through a bunch of different iterations and go, I don't like that. I don't like that.

> 嗯，然后再搭一个收藏系统。所以这是「一次性设计（disposable design）」的又一个绝佳例子。是的。你可以非常快地随手把它搭出来，快速翻过一堆不同的迭代，然后说：这个我不喜欢，那个我不喜欢。

[18:32] **SPEAKER_01:** I do like that. Oh, let's take this piece from this one and put it all together. And it makes it happen so much faster.

> 这个我喜欢。哦，我们把这一版里的这个部分拿过来，然后全部拼到一起。它让这一切发生得快得多。

[18:38] **SPEAKER_02:** Yes.

> 是的。

[18:39] **SPEAKER_01:** Show us some of the iterations that you put together here.

> 给我们看看你在这里做的一些迭代吧。

[18:41] **SPEAKER_02:** As part of the sold at MD, I made sure to include the names of the different articles that we have in the zine. And. That was one of the main things that I wanted to highlight and show on at least the first version of the website that I had in mind. And again, because it's one-shotted, you don't expect like an incredibly high level of craft. You're just using this as an exploration tool.

> 作为 Soul.md 的一部分，我特意把我们这本 zine 里各篇不同文章的标题都写了进去。而这是我脑子里至少想在网站第一个版本上重点突出、展示出来的主要东西之一。同样，因为它是一次成型的，你不会指望它有极高水准的精细打磨。你只是把它当作一个探索工具来用。

[19:02] **SPEAKER_02:** So getting a feel of, okay, do I want to lay out all the, all the titles of the articles like this? Or does that was another really cool exploration that I loved, which is there's so many things, so many cool things going on here. Cool font. Um, there was the date of the party that we threw the launch party that we threw for the zine that was included in there because it was also part of the sold at MD. That is a beautiful thing.

> 所以就是去找感觉：好，我到底想不想把所有文章标题这样排布？还是——这是我很喜欢的另一个很酷的探索，这里有太多东西、太多很酷的东西在发生了。很酷的字体。嗯，里面还有我们为这本 zine 举办的发布派对的日期，因为那也是 Soul.md 的一部分，所以被包含进来了。这是件很美妙的事。

[19:26] **SPEAKER_02:** When you realize when you unlock so much information for your agent, your agent knows so much that when you're going to give it full reign in full, you're going to unleash it to make iterations for you. It's going to surprise you. It's going to include things that you would not have otherwise thought of. And that was almost like an AGI moment for us when we realized that. Wow, it can see things ahead of us and it can really help us brainstorm even to come up with like really, really original ideas.

> 当你意识到——当你为你的 agent 解锁了这么多信息，你的 agent 知道得如此之多，以至于当你打算彻底放手、把它完全放开去替你做迭代时，它会给你惊喜。它会加入一些你原本根本不会想到的东西。当我们意识到这一点时，那对我们来说几乎是一个「AGI 时刻」——哇，它能看到我们前面的东西，它真的能帮我们头脑风暴，甚至能想出非常非常有原创性的点子。

[19:55] **SPEAKER_02:** And so that was a really nice, um, surprise here. It's just like organically included the time of the party that we were hosting. Also the, the fact that it's a zine. And so it added this, uh, cold bar, this barcode, uh, assuming that it's like a physical one that you can purchase in different, um, in different, uh, currency was also really cool. One thing that I wanted to experiment with is.

> 所以这在这里是一个非常美好的惊喜。它就那样很自然地把我们要举办的派对时间也包含了进去。还有——它是一本 zine 这个事实。于是它加了这个——呃，条形码，假定它是一本你可以购买的实体 zine，还用了不同的——呃，不同的货币，这也非常酷。我想尝试的一件事是——

[20:17] **SPEAKER_02:** What if we had an actual map of San Francisco, an interactive map of San Francisco, and it included this version where, oh, wow, yes, where you, it, uh, it reveals a map of San Francisco that is interactive and you can move around in the city and that is like fully living behind the one shotted iteration that it built. So just like marvelous things. And I think these sorts of levels of design, one shot. Designs can only be achieved if you have a very detailed. An an intentional designed on MD or sold it.

> ——如果我们有一张真正的旧金山地图会怎样，一张交互式的旧金山地图，然后它包含了这样一个版本——哦，哇，对，它揭示出一张交互式的旧金山地图，你可以在这座城市里到处移动，而这一切都完全「活」在它一次成型做出来的那版迭代背后。真的是些奇妙的东西。我认为这种程度的设计、一次成型的设计，只有当你有一个非常详细、非常用心的 design.md 或 Soul.md 时才能实现。

[20:54] **SPEAKER_02:** MD. You need to shepherd your agent to tell it exactly the vibe that you want to go for. If you can include screenshots, also, if you can include a mood board as much information as you can feed your agent so that it really understands what you want, and then it's going to surprise you in the most beautiful way. Yeah.

> ……Soul.md。你需要去引导（shepherd）你的 agent，明确告诉它你想要追求的那种感觉。如果你能附上截图、如果你能附上情绪板——尽可能多地把信息喂给你的 agent，让它真正理解你想要什么，然后它就会以最美妙的方式给你惊喜。是的。

[21:09] **SPEAKER_01:** I think a lot of people use Claude or they use Codex and they tell it to design something and they feel like they get generic design back. And this is how to break that.

> 我觉得很多人用 Claude、或者用 Codex，让它去设计点什么，然后觉得自己拿回来的是很平庸、很通用的设计。而这就是打破这种局面的办法。

[21:17] **SPEAKER_02:** that. Yes. Which is really interesting. And it's really easy. You just have to pull Pinterest or even like Google image and you find, or even websites that you really like, really websites that you really like and start bookmarking them and eventually use them, give them to your agent and say, this is something that I really like. And sometimes you love a website and you don't

> ……打破这种局面。是的。这真的很有意思，而且真的很简单。你只需要打开 Pinterest、甚至 Google 图片去找，或者找一些你真正喜欢的网站——真正你喜欢的网站——开始把它们收藏起来，最终用上它们，把它们交给你的 agent 说：这是我真正喜欢的东西。而有时候你喜欢一个网站，你却……

[21:37] **SPEAKER_02:** even know why you love a website, but it's okay. You don't need to understand why you love a website. Just give it to the agent. The agent will analyze it for you. It's going to understand eventually your patterns and the commonality between all the websites that you like. It can

> ……甚至不知道自己为什么喜欢这个网站，但没关系。你不需要弄明白自己为什么喜欢一个网站，直接把它交给 agent，agent 会替你分析它。它最终会理解你的模式，以及你喜欢的所有网站之间的共通之处。它能——

[21:48] **SPEAKER_02:** tell you, oh, that's actually the things that you seem to like across many websites. This is another exploration that I really loved. Again, displaying the title of all the articles and there are really cool hover effects that it created as you're exploring the different articles. And so for each article, it pulled really cool visuals. And you're at a point where you don't even know how Claude does these things. It just, it scrapes the web, it browses the web. It finds

> ——告诉你：哦，这些其实就是你在许多网站上似乎都喜欢的东西。这是我非常喜欢的另一个探索。同样是展示所有文章的标题，而且它做了一些非常酷的悬停效果，当你浏览不同文章时会出现。所以对每一篇文章，它都拉取了非常酷的视觉素材。你已经到了这样一个地步——你甚至不知道 Claude 是怎么做到这些事的。它就是——它爬取网页、它浏览网页，它找到——

[22:19] **SPEAKER_02:** cool pictures, animations, and it's going to surface them like this. And if there are some things that you want to fine tune, you can just, you know, speak via Aqua and ask it to change things, change the color of things, change the feel of things. And it's just this incredibly fast and rewarding feedback loop that you have with your agent. So now we can talk about where we ended up is this fully interactive map. Of San Francisco. We thought, how fun would it be to build a map where people can drop pins and

> ——很酷的图片、动画，然后像这样把它们呈现出来。如果有些东西你想微调，你就可以直接——你知道的——通过 Aqua 说话，让它改东西、改颜色、改整体的感觉。这就是你和你的 agent 之间那种极其快速、极有成就感的反馈循环。那么现在我们可以聊聊我们最终落到的地方，就是这张完全交互式的旧金山地图。我们想，做一张地图会有多好玩——让人们可以在上面放置图钉，并且……

[22:50] **SPEAKER_02:** small stories of things that they've come across in San Francisco or like encounters or like delightful memories that they have of small moments in the city. And so we thought, let's make it fully anonymous. People can share memories. And the only thing that they need to do is pin a location or like pick a location and then tell us what happened at that location. And what's beautiful is.

> ……分享一些他们在旧金山遇到过的事情的小故事，比如一些邂逅、或是他们对这座城市里某些小瞬间的美好回忆。所以我们想，那就让它完全匿名吧。人们可以分享记忆，他们唯一需要做的就是标注一个地点、或者说挑一个地点，然后告诉我们在那个地点发生了什么。而美妙的地方在于——

[23:14] **SPEAKER_02:** Is that it allows people to share things that are very surprising and beautiful and intimate and introspective. Here we built this, this fun little way to consume or like read through all these submissions. And it's again, a way for us to go back to the core essence of this project, which is how can we understand how people experience in San Francisco and what are the like magical small moments that we can all. Sort of. Learn from.

> ——它让人们能分享一些非常出人意料、非常美好、非常私密、非常内省的东西。在这里我们做了这个有趣的小方式，来消费、或者说通读所有这些投稿。这同样是我们回到这个项目核心本质的一种方式——也就是，我们如何理解人们在旧金山的体验，以及有哪些奇妙的小瞬间是我们大家都能从中学到点什么的。

[23:44] **SPEAKER_02:** We also build this little entry point for we built posters, digital posters for the party that we threw the launch party that we threw. There's also a sub stack that we created for this zine and we added this fun little entry point where you get redirected to this, to the sub stack, and then you can read the different articles. You can share a noticing or you can share a submission that you really like. So let's say this one, I really like it. I want to send it to my friend. I can just click share. It

> 我们还做了这个小入口——我们为我们举办的派对、我们办的那场发布派对做了海报，数字海报。我们还为这本 zine 创建了一个 Substack，我们加了这个有趣的小入口，你会被重定向到这个 Substack，然后你就可以读到各篇不同的文章。你可以分享一条「观察（noticing）」，或者分享一条你非常喜欢的投稿。比如说这一条，我非常喜欢，我想把它发给我的朋友，我只要点「分享」就行。它——

[24:13] **SPEAKER_02:** downloads it as a PN. G and it outputs this and it gives you the cardinal coordinates of the location that was tied to this story. And you can share this with your friends and you also know the street that it's in or that it's on.

> ——就会把它作为一个 PNG 下载下来，输出成这样，并且给你与这个故事绑定的那个地点的方位坐标。你可以把它分享给你的朋友，而且你也会知道它所在的那条街。

[24:27] **SPEAKER_01:** So we're actually putting on startup school at the chase center here in San Francisco. And you did a lot of really cool work to help support that. I would love for you to show off some of the shaders that you created and some of the content that has been shared on social media and other platforms. To help bring attention to the event.

> 我们其实正要在旧金山这里的大通中心（Chase Center）举办 Startup School。而你做了很多非常酷的工作来支持它。我很希望你能展示一下你创作的一些 shader，以及一些已经在社交媒体和其他平台上分享出去、用来为这场活动吸引关注的内容。

[24:46] **SPEAKER_02:** Yes, we're all preparing for startup school, which is our biggest event of the year. It's going to be, as you said, at Chase Center, we're going to have more than 6,000 people coming from all corners of the world to experience SF and what it means to build with AI and have like this incredible sense of community of we're all building together. And we were able to have an amazing speaker lineup this year. We have phenomenal names coming. We have Jensen, we have Sam Altman, we have Alexander Wang, we have Jeff Dean.

> 是的，我们都在为 Startup School 做准备，这是我们一年中最大的活动。正如你所说，它会在大通中心举办，我们会有超过 6000 人从世界各个角落赶来，来体验旧金山、体验用 AI 去构建意味着什么，并感受这种「我们都在一起构建」的美妙的社区归属感。我们今年得以邀请到一份很棒的演讲嘉宾阵容，有非常了不起的名字要来。我们有黄仁勋（Jensen），有 Sam Altman，有 Alexander Wang，有 Jeff Dean。

[25:13] **SPEAKER_02:** And so many others. And we wanted a really cool way to share that lineup with the world. And when we were thinking more broadly about the design behind this event, we wanted to make it feel really YC, but more like a variation of YC. And so we experimented with, of course, orange, but gradients of orange. And we discovered the paper shaders. And we thought maybe it would be a cool

> 还有其他很多很多人。我们想要一个非常酷的方式，把这份阵容分享给全世界。当我们更宏观地思考这场活动背后的设计时，我们希望它感觉很有 YC 的味道，但更像是 YC 的一个变体。所以我们当然尝试了橙色，但是是渐变的橙色。然后我们发现了 Paper 的 shader，我们觉得也许用它来做实验会是一个很酷的——

[25:37] **SPEAKER_02:** way for us to experiment with paper shaders. My first intuition when I thought about building visual, assets for how we're going to share these speaker cards on social media, I've initially started in Figma, actually. I've initially dropped some of the images that we got from our speakers. And I started making it myself, moving things around. And I noticed, well, we're going to have many speakers. And I don't want to move things around 12 times. And so I thought it would probably be

> ——方式，让我们来用 Paper 的 shader 做实验。当我想到要为「我们打算怎样在社交媒体上分享这些嘉宾卡片」构建视觉素材时，我最初的直觉——其实我一开始是在 Figma 里做的。我一开始把我们从嘉宾那里拿到的一些图片放进去，然后开始自己动手做，挪来挪去。然后我注意到，嗯，我们会有很多位嘉宾，而我并不想把这些东西挪来挪去做上 12 遍。所以我想，可能会——

[26:08] **SPEAKER_02:** just simpler to ask Claude to make a template for myself. And it can even like pull images for me from my inbox. And I can also have an easier time experiment with the visual feel of the cards. And so I built this tool for myself. It's a very simple tool where we have the names of all of the speakers that are confirmed. And it just automatically generated all of these as we kept having more and more names

> ——直接让 Claude 帮我做一个模板要简单得多。它甚至可以帮我从收件箱里拉取图片。而且我也能更轻松地去尝试这些卡片的视觉感觉。所以我给自己搭了这个工具。这是一个非常简单的工具，里面有所有已确认嘉宾的名字，随着我们不断确认越来越多的名字，它就自动把这些全都生成出来了——

[26:41] **SPEAKER_02:** of speakers confirmed. And I also built a way of making them really simple. I don't know much about these speakers right now, but I do think about a lot of these speakers that are very important. I'm working on what they mean to me, what that brings me to this point. I can start to create my own app, and where I can also use them. And I can try and create my own app to the same level. But I

> ——确认了越来越多的嘉宾。我还搭了一个让它们变得非常简单的方式。（此段音频转录不清晰、语义零散。）

[26:42] **SPEAKER_?:** have a whole different way of doing that because ARN doesn't have the visual feel of the cards. And I

> （此段音频转录不清晰、语义零散。）……用一种完全不同的方式来做那件事，因为它没有那些卡片的视觉感觉。而我——

[26:42] **SPEAKER_02:** And I also built a way for myself to experiment with different ways to lay out the text on these cards. And we ended up going for this one, but it was fun to really easily almost one-shot a different iteration of layout for each of these cards. And these are compatible across the board. And for the shaders, well, we used the movement that comes from one of the shaders made by Paper.Design.

> ——我还给自己搭了一个方式，来尝试在这些卡片上排布文字的不同方案。我们最终选定了这一个，但能非常轻松地、几乎一次成型地为每张卡片做出一版不同的排版迭代，这很好玩。而这些都是全面通用兼容的。至于 shader 嘛，我们用的是 Paper.Design 做的其中一个 shader 里带来的那种动态效果。

[27:09] **SPEAKER_02:** And we fine-tuned the graininess here and the edges and the rotation, the scale, like this. And I had a lot of fun really finding the variation of the shader that I wanted. And so I can just refresh it and it resets. But that was also a very helpful sort of mini tool that I built for myself. And another thing is I wanted to, because I wanted to keep the really cool movement that has happened, I needed to do a screen recording to maximize the resolution of the card.

> 我们在这里微调了颗粒感、边缘，还有旋转、缩放，就像这样。我玩得很开心，真正找到了我想要的那一版 shader 变体。所以我只要刷新一下，它就重置了。但这也是我为自己搭的一个非常有帮助的小工具。另外一件事是，因为我想保留已经出现的那种非常酷的动态效果，我需要做一个屏幕录制，来把卡片的分辨率最大化。

[27:45] **SPEAKER_02:** And so I built this little screen recording tool for myself that tells me exactly when I need to start the recording and when I need to stop. And the reason I built this tool is because I really wanted it to feel like a loop, a perfect loop, so that when we post it on Twitter and on Instagram, it loops very, very smoothly. And it feels like an endless sort of movement. And so I asked Claude to build this. And he said, you know, this specific tool that gives me like this four-second, like perfectly designed loop so that it starts and end at the exact same pixel, so that it feels really smooth.

> 所以我给自己搭了这个小小的屏幕录制工具，它会精确地告诉我什么时候该开始录制、什么时候该停止。我搭这个工具的原因是，我真的很希望它感觉像一个循环、一个完美的循环，这样当我们把它发到 Twitter 和 Instagram 上时，它能非常非常流畅地循环播放，感觉像一种无尽的动态。所以我让 Claude 来搭这个，它就做出了——你知道的——这个特定的工具，给我一个大约四秒、完美设计好的循环，让它在完全相同的像素处开始和结束，从而感觉非常流畅。

[28:20] **SPEAKER_02:** We thought it would be really magical if people received a ticket when they get their acceptance. And so we designed this ticket, reusing the shader that we're using for all the other visual assets that we have for Startup School. This time we would apply it against a. A ticket and we would try to make it as personalized as possible. So we render your name and we render the city that you're from, and then some information about the, about the event.

> 我们觉得，如果人们在收到录取通知时能拿到一张票，那会非常有魔力。所以我们设计了这张票，复用了我们为 Startup School 所有其他视觉素材所用的那个 shader。这一次我们把它应用到一张票上，并尽量让它尽可能个性化。所以我们会渲染出你的名字、渲染出你来自的城市，然后是一些关于这场活动的信息。

[28:50] **SPEAKER_02:** And it's been such a delight to see people share them on social media and say that they are excited about coming to SF and experience SF sometimes for the first time.

> 看到人们把这些票分享到社交媒体上，说他们很兴奋要来旧金山、来体验旧金山——有时还是第一次——这真是一件让人非常开心的事。

[29:01] **SPEAKER_01:** Yeah. Could you imagine a year ago trying to build something like this? It wouldn't be worth it.

> 是啊。你能想象一年前去尝试构建这样的东西吗？那根本不值得。

[29:05] **SPEAKER_02:** These shaders, building these shaders a year ago would have been like, would have felt like this. Insurmountable mountain of like, I would not even have known where to start to build these things. And now it is just this thing that Claude, my Claude knows what to pull because it, it knows that I love paper. It knows that I love their shaders and it's just automatically knows how to pull that all that information from their website and it uses it. It's just really magical.

> 这些 shader——一年前构建这些 shader 会像是、会感觉像是一座无法翻越的大山，我甚至根本不知道该从哪里开始去做这些东西。而现在它就变成了这样一件事：Claude——我的 Claude——知道该去拉取什么，因为它知道我喜欢 Paper，它知道我喜欢他们的 shader，它就自动知道该怎么从他们的网站上拉取所有那些信息并加以使用。这真的太神奇了。

[29:33] **SPEAKER_01:** It's really cool to see this and it feels like so much time and thought and attention and care went into designing the experience. From the moment that you get accepted until all the way through when you show up to the event and see the amazing line up there.

> 看到这些真的很酷，感觉整个体验的设计投入了这么多的时间、思考、注意力和用心——从你被录取的那一刻，一直贯穿到你到达活动现场、看到那份令人惊叹的嘉宾阵容。

[29:46] **SPEAKER_02:** Yes, yes. And it's also, it's going to be amazing to keep building more of the branding of Startup School with Claude and Codex and the coding agents. It is such a different paradigm as to how we even do branding design moving forward. The fact that we will be able to use that same shader with the same parameters on the massive screens that we're going to have throughout Chase Center and keep it. Incredibly consistent through and through.

> 是的，是的。而且，继续用 Claude、Codex 和这些编程 agent 去构建更多 Startup School 的品牌形象，将会是一件很棒的事。这对于我们往后到底如何去做品牌设计，是一个如此不同的范式。我们将能够把同一个、参数完全相同的 shader 用在贯穿整个大通中心的那些巨型屏幕上，并让它从头到尾保持极其一致。

[30:12] **SPEAKER_02:** It's amazing. Like, I'm really, really excited about this and it's just easier than ever to make things more consistent and use coding agents for absolutely everything.

> 太惊人了。我真的、真的对此感到非常兴奋，而现在要让各种东西保持更一致、要把编程 agent 用在绝对所有的事情上，比以往任何时候都要容易。

[30:21] **SPEAKER_01:** Yeah. Amazing. Ev, thank you so much for joining and showing us the behind the scenes of how you've done some of this incredible work. Um, things that I think are really pushing the boundaries forward that, uh, are ways that are going to be super common for how designers are designing in the future, but not a lot of people I think have figured out yet. So I really appreciate you sharing that process.

> 是啊，太棒了。Ev，非常感谢你来参加，并向我们展示了你完成这些令人惊叹的工作背后的幕后过程。嗯，我认为这些东西真的在把边界向前推进，是未来设计师做设计时会变得极其普遍的方式，但我觉得目前还没有很多人搞明白。所以我真的很感激你分享了这个过程。

[30:39] **SPEAKER_02:** Thank you. We're, we're all figuring it out together and we're having a lot of fun doing so.

> 谢谢你。我们大家都在一起摸索，而且在这个过程中玩得很开心。

[30:43] **SPEAKER_01:** That does it for this episode of Design Review. We'll see you on the next one.

> 本期《Design Review》就到这里。我们下期再见。
