# 全文转录 · 对话 Claude Code 之父 Boris Cherny:如何为「六个月后的模型」而造

> ▶ [YouTube](https://www.youtube.com/watch?v=PQU9o_5rHC4) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/PQU9o_5rHC4.md) &nbsp;·&nbsp; Inside Claude Code With Its Creator Boris Cherny

> 中英对照 · 每段英文原文下附中文翻译

`[00:00]` **SPEAKER_02:** At Anthropic, the way that we thought about it is we don't build for the model of today. We build for the model six months from now. That's actually like still my advice to founders that are building on LLMs. Just try to think about like, what is that frontier where the model is not very good at today? Because it's going to get good at it.

> 在 Anthropic,我们的思路是不为今天的模型做开发,而是为六个月后的模型做开发。这其实也依然是我给那些基于大语言模型创业的创始人的建议。你只要去想:今天模型还不太擅长的那个前沿在哪里?因为它迟早会变得擅长。

`[00:14]` **SPEAKER_02:** All of quad code has just been written and rewritten and rewritten and rewritten over and over and over. There is no part of quad code that was around six months ago. You try a thing, you give it to users, you talk to users, you learn. And then eventually you might end up at a good idea. Sometimes you don't.

> 整个 Claude Code 都是被一遍又一遍地反复重写出来的。六个月前的 Claude Code 里没有任何一部分还留到现在。你尝试一个东西,把它交给用户,和用户交流,从中学习。然后最终你可能会得到一个好点子。有时候你也得不到。

`[00:26]` **SPEAKER_04:** Are you also in the back of your mind thinking that maybe like in six months, you won't need to prompt that explicitly, but the model will just be good enough to figure out on its own?

> 你心里是不是也在想,也许再过六个月,你就不需要那么明确地去提示了,模型自己就足够聪明,能自行搞定?

`[00:34]` **SPEAKER_02:** Maybe in a month.

> 也许一个月后就能。

`[00:36]` **SPEAKER_00:** No more need for a plan mode in a month?

> 一个月后就不再需要计划模式(plan mode)了?

`[00:38]` **SPEAKER_04:** Oh my God.

> 我的天。

`[00:46]` **SPEAKER_01:** Welcome to another episode of The Light Cone. And today we have an extremely special guest, Boris Cherny, the creator, engineer of quad code. Boris, thanks for joining us. Thanks for having me. Thanks for creating a thing that has taken away my sleep for about three weeks straight.

> 欢迎收看新一期的《The Light Cone》。今天我们请来了一位非常特别的嘉宾——Boris Cherny,Claude Code 的创造者和工程师。Boris,谢谢你来。谢谢你们邀请我。也谢谢你造出了一个让我连续三周睡不着觉的东西。

`[01:03]` **SPEAKER_01:** I am very addicted to quad code and it feels like rocket boosters. Has it felt like this for people like for, you know, months at this point? I think it was like end of November is where a lot of my friends said like something changed.

> 我现在非常沉迷于 Claude Code,那种感觉就像装上了火箭助推器。这种感觉是不是很多人已经持续好几个月了?我记得大概是十一月底,我很多朋友都说,有什么东西变了。

`[01:19]` **SPEAKER_02:** I remember for me, I felt this way when I first created quad code and I didn't yet know if I was onto something. I kind of felt like I was onto something. And then that's when I wasn't sleeping. And that was just like three straight months. This was September 2024.

> 我记得对我来说,是在我刚做出 Claude Code、还不确定自己是不是找到了什么名堂的时候有这种感觉的。我隐约觉得自己抓住了点什么。那时候我就睡不着了,一连三个月都是这样。那是 2024 年 9 月。

`[01:32]` **SPEAKER_02:** Yeah, it was like three straight. I didn't take a single day vacation, worked through the weekends, worked every single night. I was just like, oh my God, this is, I think this is going to be a thing. I don't know if it's useful yet because it couldn't actually code yet.

> 是的,连续三个月。我一天假都没休,周末也在干,每天晚上也在干。我当时就想,天哪,我觉得这东西要成气候了。虽然我还不确定它有没有用,因为那时候它其实还不会写代码。

`[01:45]` **SPEAKER_01:** If you look back on those moments to now, like what would be like the most surprising thing about this moment right now?

> 从那些时刻回望到现在,眼下这个时刻最让你意外的是什么?

`[01:52]` **SPEAKER_02:** It's unbelievable that we're still using a terminal. That was supposed to be the starting point. I didn't think that would be the ending point. And then the second one is that it's even useful because, you know, at the beginning it didn't really write code. It didn't write code.

> 最难以置信的是我们居然还在用终端。终端本该只是起点,我没想到它会成为终点。第二件意外的事是它居然真的有用,因为一开始它其实并不会写代码,它不会写代码。

`[02:02]` **SPEAKER_02:** It didn't write code. It didn't write code. It didn't write code. Even in February when we GA'd it, it wrote maybe like 10% of my code or something like that. I didn't really use it to write code.

> 它不会写代码,不会写代码,不会写代码。哪怕到了二月我们正式发布(GA)的时候,它大概也只写了我大约 10% 的代码。我基本上没用它来写代码。

`[02:08]` **SPEAKER_02:** It wasn't very good at it. I still wrote most of my code by hand. So the fact that it actually like our bets paid off and it got good at the thing that we thought it was going to get good at because it wasn't obvious. At Anthropic, the way that we thought about it is we don't build for the model of today. We build for the model six months from now.

> 它当时不太擅长写代码。我大部分代码还是手写的。所以我们的赌注真的兑现了,它真的在我们预期它会擅长的事情上变得擅长了——这一点当初并不是显而易见的。在 Anthropic,我们的思路是不为今天的模型做开发,而是为六个月后的模型做开发。

`[02:26]` **SPEAKER_02:** And that's actually like still my advice to founders that are building on LLMs is, you know, just try to think about like, what is that frontier? Where the model is not very good at today because it's going to get good at it and you just have to wait.

> 这其实也依然是我给那些基于大语言模型创业的创始人的建议:去想一想那个前沿在哪里,今天模型还不擅长的地方在哪里,因为它迟早会变得擅长,你只需要等待。

`[02:38]` **SPEAKER_04:** Going back, do you remember when you first got the idea? Can you just talk us through that? Like, was there something like a spark or what was even the first version of it in your mind?

> 回到最初,你还记得你第一次有这个想法是什么时候吗?能给我们讲讲那个过程吗?比如有没有某个火花般的瞬间?或者说你脑子里最初的版本是什么样的?

`[02:46]` **SPEAKER_02:** You know, it's funny. It was like, it was so accidental that it just kind of evolved into this. You know, as Anthropic, I think for Ant, the bet has been coding for a long time and the bet has been the path to safe AGI is through coding. And this is, this is. It's kind of always been the idea and the way you get there is you teach the model how to code, then you teach it how to use tools, then you teach it how to use computers.

> 说来有意思,它太偶然了,就这么一点点演变成了现在的样子。对 Anthropic 来说,长期以来押注的就是编程,押注的是通往安全 AGI 的路径要经由编程。这一直是我们的理念,而实现它的方式就是:先教会模型编程,然后教它使用工具,再教它使用电脑。

`[03:11]` **SPEAKER_02:** And you can kind of see that because the first team that I joined at Anthropic, this was the Anthropic Labs team, and it produced three products. It was quad code, MCP and the desktop app. So you can kind of see how these like weave together. The particular product that we built, you know, like no one, no one asked me to build a CLI. We kind of knew maybe it was time to build some kind of coding product.

> 你能看出这一点,因为我在 Anthropic 加入的第一个团队是 Anthropic Labs 团队,它产出了三个产品:Claude Code、MCP 和桌面应用。你能看出它们是如何交织在一起的。至于我们做的这个具体产品——没有人叫我去做一个命令行工具(CLI)。我们只是隐约觉得,也许是时候做某种编程产品了。

`[03:33]` **SPEAKER_02:** Because it seemed like the model was ready, but no one had yet really built a product that harnessed this capability. So like still there's this insane feeling of product overhang. But at the time it was just like even crazier because like no one had built this yet. And so I sort of like hacking around and I was like, OK, we build a coding product. What do I have to do first?

> 因为看起来模型已经准备好了,但还没有人真正做出一个能驾驭这种能力的产品。所以直到现在都有一种"产品严重滞后于能力"的疯狂感。而在当时更夸张,因为根本还没人做过这样的东西。于是我就开始瞎折腾,想着:好,我们要做一个编程产品,那我首先得做什么?

`[03:51]` **SPEAKER_02:** I have to understand how to use the API because I hadn't used the Anthropic API at that point. And so I just built like a little terminal app to use the API. That's all that it did. And it was a little chat app because. Think about the, you know, AI applications at the time.

> 我得先搞懂怎么用这个 API,因为那时候我还没用过 Anthropic 的 API。于是我就做了个小小的终端应用来调用这个 API,它就只干这一件事。它是个小小的聊天应用,因为——想想当时的 AI 应用。

`[04:05]` **SPEAKER_02:** And, you know, for non coders today, most what are most people using is just a chat app. So that's what I built. And, you know, it was in a terminal. I can ask questions. I give answers.

> 对今天不写代码的人来说,大多数人用的其实就是个聊天应用。所以我做的就是那个。它跑在终端里,我可以提问,它给出回答。

`[04:15]` **SPEAKER_02:** Then I think tool use came out. I just want to try out tool use because I don't really understand what this is. I was like, tool use, this is cool. Is this actually useful? Probably not.

> 然后我记得工具调用(tool use)功能出来了。我就想试试工具调用,因为我不太理解这到底是什么。我当时想,工具调用,挺酷的。这真有用吗?大概没用吧。

`[04:22]` **SPEAKER_02:** Let me just try it.

> 那就先试试看吧。

`[04:23]` **SPEAKER_04:** You built it in a terminal just because it was the easiest way to get something up and running. Yes, because I didn't have to build a UI.

> 你在终端里做它,只是因为那是最快能把东西跑起来的方式。是的,因为那样我就不用去做界面了。

`[04:29]` **SPEAKER_02:** OK. It was just me.

> 对。当时就我一个人。

`[04:30]` **SPEAKER_04:** At that point, it was like the IDEs cursor. Windsurf were the things that were really taking off. Were you sort of under any pressure or getting lots of suggestions of, hey, like, we should build this out as a plugin or as a as a fully featured ID itself?

> 那个时候,像 Cursor、Windsurf 这样的 IDE 正在真正火起来。你当时有没有承受什么压力,或者收到很多建议,说"嘿,我们应该把它做成一个插件,或者做成一个功能齐全的 IDE"?

`[04:43]` **SPEAKER_02:** There was no pressure because we didn't even know what we wanted to build. Like the team was just in explore mode. You know, like we didn't we know vaguely we wanted to do something in coding, but it wasn't obvious what no one was high confidence enough. That was like my job to figure out. And so I gave the model the bash tool.

> 没有什么压力,因为我们甚至都不知道自己想做什么。团队还处在探索模式。我们只是模糊地知道想在编程领域做点什么,但具体做什么并不明确,谁也没有足够的信心。而搞清楚这一点正是我的工作。于是我给了模型 bash 工具。

`[04:58]` **SPEAKER_02:** That was the first tool that I gave it just because I think that was literally the example in our docs. I just like took the examples in Python. I just ported it to TypeScript because that's how I wrote it. You know, I didn't know like what the model could do with bash. So I asked it to like read a file.

> 那是我给它的第一个工具,纯粹是因为我记得那正好是我们文档里的示例。我就把 Python 的示例拿过来,移植到 TypeScript,因为我是用 TypeScript 写的。我当时不知道模型拿 bash 能做什么,所以我让它去读一个文件。

`[05:10]` **SPEAKER_02:** It could like cat the files like that was cool. And then I was like, OK, like, what can you actually do? And I asked it, what music am I listening to? You wrote some like Apple script to script my my Mac and look up the music in my music player. Oh, my God.

> 它能用 cat 把文件读出来,挺酷的。然后我想,好,那你到底还能做什么?我就问它:我现在在听什么音乐?它写了一段 AppleScript 来操控我的 Mac,去我的音乐播放器里查我在听的音乐。我的天。

`[05:24]` **SPEAKER_02:** And this was sauna 3.5. And, you know, like, I didn't think the model could do that. And that was my first, I think, ever fueled the AGI moment. Whereas it's like, oh, my God, the model, it just wants to use tools.

> 那时候用的是 Sonnet 3.5。我原本没想到模型能做到这一点。那大概是我第一次感受到那种"感觉到 AGI"的时刻。就像是,天哪,这个模型,它就是想用工具。

`[05:37]` **SPEAKER_02:** That's all it wants.

> 它就想要这个。

`[05:38]` **SPEAKER_00:** That's kind of fascinating. I mean, it's very kind of contrarian that Clockwork works so well in such an elegant, simple form factor. I mean, terminals have been around for a really long time. And that seemed to be like a good design constraint that allowed a lot of interesting developer experiences. It doesn't feel like working.

> 这挺让人着迷的。我是说,Claude Code 能以这么优雅、简单的形态运作得这么好,其实是相当反直觉的。终端已经存在很久很久了。而它似乎恰好是一个很好的设计约束,催生了很多有趣的开发者体验。用起来不像是在工作。

`[05:59]` **SPEAKER_00:** It just feels fun as a developer. I don't think about files. I don't know where everything is. And that came by accident almost.

> 作为开发者,它就是让人觉得好玩。我不用去操心文件,我也不知道每样东西具体在哪。而这几乎是无心插柳得来的。

`[06:07]` **SPEAKER_02:** Yeah, it was an accident. I remember. So after the terminal started to take off internally and honestly, like after building this thing, I think like two days after the first prototype, I started giving it to my team just for dogfooding. Because, you know, like, you know, if you come up with an idea and it seems useful, the first thing you want to do is you want to give it to people to see how they use it. And then I came in the next day.

> 是的,是无心插柳。我记得,这个终端工具在内部开始火起来之后——说实话,做出这东西之后,大概在第一个原型出来两天后,我就开始把它交给我的团队试用(dogfooding)。因为你想,如果你有个点子,而且看起来有用,你最先想做的就是把它交给别人,看他们怎么用。然后第二天我来上班。

`[06:26]` **SPEAKER_02:** And then Robert, who sits across from me, he's another engineer, he just like had quad code on his computer. And he was like using it to code. So I was like, what are you what are you doing? Like, this thing isn't ready. It's just a prototype.

> 然后坐在我对面的 Robert——他是另一位工程师——他电脑上就装着 Claude Code,还在用它写代码。我就说,你在干嘛?这东西还没做好呢,它只是个原型。

`[06:37]` **SPEAKER_02:** But yeah, it was already useful in that form factor. And I remember when we did our launch review to kind of launch quad code externally. This was in December, November or something like that. In 2024, Dario asked and he was like, the usage chart internally, like the DAO chart is like vertical. Are you like forcing engineers to use it?

> 但确实,它以那种形态就已经很有用了。我记得我们做发布评审、准备把 Claude Code 对外发布的时候——那是 2024 年的十二月还是十一月左右——Dario 问,内部的使用曲线,那个日活(DAU)曲线简直是垂直往上的,你是不是在强迫工程师用它?

`[06:56]` **SPEAKER_02:** Like, why are you mandating them? And I was just like, no, no, we didn't. We did. I just like posted about it. And they had just been like telling each other.

> 他问,你为什么要强制他们用?我说,不不,我们没有强制。我们没有。我只是发了个帖子提了一下,然后大家就是口口相传。

`[07:03]` **SPEAKER_02:** About it, honestly, it was it was just accidental. We started with the CLI because it was the cheapest thing and it just kind of stayed there for a bit.

> 说实话,这真的纯属偶然。我们从命令行工具起步,因为那是成本最低的做法,然后它就那样在终端里待了一阵子。

`[07:09]` **SPEAKER_04:** So in that 2024 period, what how are the engineers using it? Were they shipping code with it yet or were they using it in a different way?

> 那么在 2024 年那段时间,工程师们是怎么用它的?他们那时候已经用它交付代码了吗,还是以别的方式在用?

`[07:18]` **SPEAKER_02:** The model is not very good at coding yet. I was using it personally for automating Git. I think at this point I've probably forgotten most of my Git because quad code has just been doing it for so long. But yeah, like automating bash commands, that was a very early use case. I think it was like operating like Kubernetes and kind of things like this.

> 那时候模型还不太擅长写代码。我个人是用它来自动化 Git 操作。到现在我大概已经把大部分 Git 命令都忘了,因为 Claude Code 帮我干这事已经干了太久了。但确实,自动化 bash 命令是一个非常早期的用例。还有像操作 Kubernetes 之类的事情。

`[07:36]` **SPEAKER_02:** People were using it for coding, so there were some early signs of this. I think the first use case was actually writing unit tests because it's a little bit lower risk and the model is still pretty bad at it. But people were kind of figuring it out and they were figuring out how to use this thing. And one thing that we saw is people started writing these markdown files for themselves and then having the model read that markdown file. And this is where QuadMD came from.

> 人们也在用它写代码,所以已经有了一些早期的苗头。我觉得第一个真正的用例其实是写单元测试,因为风险低一些,而且当时模型在这方面还挺糟糕的。但大家在慢慢摸索,琢磨怎么用好这个东西。我们观察到的一件事是,人们开始为自己写这些 markdown 文件,然后让模型去读这个 markdown 文件。CLAUDE.md 就是这么来的。

`[07:59]` **SPEAKER_02:** Probably the single for me biggest principle and product is wait and demand. And. Just every bit of this product is built through wait and demand after their initial CLI. And so QuadMD is an example of that. There's this other general principle that I think is maybe interesting where you can build for the model and then you can build scaffolding around the model in order to improve performance a little bit.

> 对我来说,产品上最大的一条原则大概就是"潜在需求"(latent demand)。在最初的命令行工具之后,这个产品的每一点都是围绕潜在需求构建起来的。CLAUDE.md 就是一个例子。还有另一条我觉得可能很有意思的通用原则:你可以为模型本身做开发,也可以围绕模型搭建脚手架(scaffolding),从而把性能稍微提升一点。

`[08:19]` **SPEAKER_02:** And depending on the domain, you can improve performance maybe 10, 20%, something like that. And then essentially the gain is wiped out with the next model. So either you can build the scaffolding and then get some performance gain and then rebuild it again. Or you just wait for the next model and then you kind of get it for free. The QuadMD and kind of the scaffolding is an example of that.

> 视领域不同,你也许能把性能提升个 10%、20% 左右。然后到了下一代模型,这个提升基本上就被抹平了。所以你要么去搭脚手架、拿到一点性能提升,然后再重搭一遍;要么就干脆等下一代模型,然后差不多白白就得到了这份提升。CLAUDE.md 和这类脚手架就是这样的例子。

`[08:38]` **SPEAKER_02:** And really, I think that's why we stayed in the CLI is because we felt there is no UI we could build that would still be relevant in six months because the model was improving so quickly.

> 说真的,我觉得这就是我们一直留在命令行工具里的原因:我们觉得,以模型进步这么快的速度,我们做不出任何一个六个月后还依然适用的界面。

`[08:48]` **SPEAKER_01:** Earlier we were saying like we should compare CloudMDs, but you said something very profound, which is, you know, yours is actually very short, which is almost like the opposite of what, you know, people might expect. Why is that? What's in your CloudMD?

> 我们刚才还说应该比一比各自的 CLAUDE.md,但你说了一句很深刻的话——你的其实非常短,这几乎和人们预期的相反。这是为什么?你的 CLAUDE.md 里有什么?

`[09:01]` **SPEAKER_02:** Okay. So I checked. I checked this before we came. So my, my QuadMD has two things. One is there, it's just two lines. So the first line is whenever you put up a PR, enable auto merge. So as soon as someone accepts it, it's merged.

> 好。我特意查过了,来之前查过。我的 CLAUDE.md 里只有两件事,就两行。第一行是:每当你提交一个 PR,就开启自动合并。这样只要有人通过它,它就会被合并。

`[09:09]` **SPEAKER_02:** That's just so I can like code and I don't have to kind of go back and forth with CR or whatever. And then the second one is whenever I put up a PR, post it in our internal team stamps channel, just so someone can stamp it and I can get unblocked. And the idea is every other instruction is in our QuadMD.

> 这样我就能一直写代码,而不用在代码评审之类的事情上来回折腾。第二行是:每当我提交一个 PR,就把它发到我们团队内部的审批(stamps)频道,这样就有人能给它盖个章,我就能解除阻塞继续往下走。关键在于,所有其他的指令都放在我们那份共享的 CLAUDE.md 里。

`[09:32]` **SPEAKER_02:** That's checked. It's checked into the code base and it's something our entire team contributes to multiple times a week and very often I'll see someone's PR and they make some like mistake that's totally preventable and I'll just literally tag Claude on the PR. I'll just do like add Claude, you know, like add this to the QuadMD and I'll do this, you know, like many times a week.

> 那份文件被签入到了代码库中,是我们整个团队每周都会多次贡献的东西。我经常会看到某人的 PR 犯了个完全可以避免的错误,我就直接在 PR 上 @Claude,写一句"加上 Claude"、"把这条加到 CLAUDE.md 里",这种事我一周要做很多次。

`[09:51]` **SPEAKER_01:** Do you have to like compact the ClaudeMD? Like I've definitely reached a point where I got the message at the top saying your ClaudeMD is like thousands of tokens now. What do you do when you guys hit that?

> 你们需要给 CLAUDE.md 做"压缩"吗?我肯定遇到过那种情况,顶部弹出提示说你的 CLAUDE.md 现在已经好几千个 token 了。你们遇到这种情况会怎么办?

`[10:01]` **SPEAKER_02:** So our ClaudeMD is actually pretty short. I think it's like a couple of thousand tokens, maybe something like that. If you hit this, my recommendation would be delete your QuadMD and just start fresh. Interesting. I think a lot of people like they try to overengineer this, right?

> 我们的 CLAUDE.md 其实相当短,大概也就几千个 token 吧。如果你遇到那种情况,我的建议是:删掉你的 CLAUDE.md,从头再来。挺有意思的。我觉得很多人会在这上面过度设计,对吧?

`[10:13]` **SPEAKER_02:** And really like the capability changes with every model. And so the thing that you want is do the minimal possible thing in order to get the model on track. And so if you delete your QuadMD and then, you know, the model is getting off track, it does the wrong thing. That's when you kind of add back a little bit at a time. And what you're probably going to find is with every model, you have to add less and less.

> 而且模型的能力每一代都在变。所以你想要的是,用尽可能少的东西把模型引上正轨。所以你删掉 CLAUDE.md,然后如果模型跑偏了、做错了事,你再一点一点地把内容加回去。而你大概会发现,随着每一代模型,你需要加的东西越来越少。

`[10:32]` **SPEAKER_02:** For me, I consider myself a pretty average engineer, to be honest. Like I don't use a lot of fancy tools. Like I don't use like Vim. I use, you know, VS Code because it's simpler.

> 对我自己来说,说实话,我觉得自己是个挺普通的工程师。我不怎么用花哨的工具,比如我不用 Vim。我用的是 VS Code,因为它更简单。

`[10:42]` **SPEAKER_03:** Wait, really? I would have assumed that because you built this in the terminal that you were sort of like a diehard terminal like Vim only person, you know, screw those VS Code people.

> 等等,真的吗?我原本以为,既然你是在终端里做出这东西的,你应该是那种铁杆终端、只用 Vim 的人,鄙视那些用 VS Code 的人。

`[10:52]` **SPEAKER_02:** Well, we have people like that on the team. You know, like Adam Wolf, for example, he's on the team. He's like, you will never take Vim for my cold, dead hands. Yeah. So there's definitely a lot of people like that on the team.

> 我们团队里确实有那样的人。比如 Adam Wolf 就在团队里,他就是那种"除非我死了,否则休想从我手里夺走 Vim"的人。所以团队里肯定有不少这样的人。

`[11:01]` **SPEAKER_02:** And this is one of the things that I learned. Early on is every engineer likes to hold their dev tools differently. They like to use different tools. There's just no one tool that works for everyone. But I think also this is one of the things that makes it possible for quad code to be so good because I kind of think about it as what is the product that I would use that makes sense to me.

> 这也是我很早就学到的一件事:每个工程师都喜欢以不同的方式使用自己的开发工具,喜欢用不同的工具。根本没有一个适合所有人的工具。但我觉得,这恰恰也是 Claude Code 能这么好用的原因之一,因为我大致是从"我自己会用的、对我来说讲得通的产品是什么样"这个角度去想的。

`[11:18]` **SPEAKER_02:** And so to use quad code, you don't have to understand Vim. You don't have to understand Tmux. You don't have to know how to like SSH. You don't have to know all this stuff. You just have to open up the tool and it will guide you.

> 所以要用 Claude Code,你不需要懂 Vim,不需要懂 Tmux,不需要知道怎么用 SSH,不需要懂这一大堆东西。你只要打开这个工具,它就会引导你。

`[11:27]` **SPEAKER_02:** It will do all this stuff.

> 它会把这些事都做了。

`[11:28]` **SPEAKER_01:** How do you decide how verbose you want like sort of the terminal to be? Like sometimes. Sometimes you have to go, you know, control O and check it out. And is it like internal bike shed battles around like longer, shorter? I mean, every user probably has a different opinion.

> 你们是怎么决定终端输出要多详细的?比如有时候你得按 Ctrl+O 去展开看一眼。内部会不会为了"更长还是更短"这种细枝末节吵得不可开交?我是说,每个用户大概都有不同的看法。

`[11:43]` **SPEAKER_01:** Like how do you make those sorts of decisions? What's your opinion? Is it too verbose right now? Oh, I love the verbosity because basically sometimes it just like goes off the deep end and I'm watching. And then I can just read very quickly and it's like, oh, no, no, it's not that.

> 你们是怎么做这类决定的?你自己怎么看?现在是不是太啰嗦了?哦,我很喜欢它啰嗦,因为有时候它会跑偏得离谱,而我正盯着看,然后我可以飞快地读一遍,就想:哦,不不不,不是那样的。

`[11:57]` **SPEAKER_01:** And then I escape and then just stop it. And then it just like stops an entire bug farm like as it's happening. I mean, that's usually when I didn't do plan mode properly.

> 然后我按 Esc 把它停下来。这样就能在一整片 bug 正冒出来的时候把它掐停。当然,那通常是因为我没把计划模式用好。

`[12:05]` **SPEAKER_02:** This is something that we probably change pretty often. I remember early on. This is maybe six months ago. I tried to get rid of bash output just internally just to like summarize it because I was like these giant long bash commands. I don't actually care.

> 这是我们大概会经常改动的东西。我记得很早的时候,大概六个月前吧,我在内部试着把 bash 的输出去掉,改成只做摘要,因为我觉得那些又长又大的 bash 命令输出,我其实并不在乎。

`[12:17]` **SPEAKER_02:** And then I gave it to anthropic employees for a day and everyone just revolted. I want to see my dash because it actually is quite useful for, you know, like for something like git output. Maybe it's not useful. But if you're running, you know, like Kubernetes jobs or something like this, you actually do want to see it. We recently hit.

> 然后我把它给 Anthropic 的员工用了一天,所有人都反抗了。他们说我想看到我的输出,因为它其实很有用。像 git 的输出也许没什么用,但如果你在跑 Kubernetes 任务之类的东西,你确实会想看到它。我们最近做了……

`[12:33]` **SPEAKER_02:** The hid the file reads and file searches. So you'll notice instead of saying, you know, like read food, MD, it'll said, you know, like read one file search, search one pattern. And this is something I think we could not have shipped six months ago because the model just was not ready. You would, you know, it's still read the wrong thing pretty often. As a user, you still have to be there and kind of catch it and debug it.

> ……把文件读取和文件搜索的细节隐藏了起来。所以你会注意到,它不再显示"读取 foo.md",而是显示"读取了 1 个文件"、"搜索了 1 个模式"。这是我觉得我们六个月前根本发布不了的东西,因为那时候模型还没到火候。它当时还经常会读错东西,作为用户你还得守在旁边,及时发现并去排查。

`[12:52]` **SPEAKER_02:** But nowadays, I just noticed it's on the right track almost every time. And because it's using tools so much, it's actually a lot better just to summarize it. But then we shipped it. We dog fooded it for like a month. And then people on GitHub didn't like it.

> 但如今,我注意到它几乎每次都走在正确的轨道上。而且因为它那么频繁地在用工具,把这些只做摘要其实体验好得多。可是我们发布之后——我们内部试用了大概一个月——GitHub 上的人们并不喜欢它。

`[13:05]` **SPEAKER_02:** So there was a big issue where people like, no, like, I want to see the details. And that was a really great feedback. And so we added a new verbose mode. And so that's just like in slash config. You can enable verbose mode.

> 所以有一个热门 issue,大家说"不,我想看到细节"。那是非常好的反馈。于是我们加了一个新的详细模式(verbose mode)。它就在 /config 里,你可以开启详细模式。

`[13:15]` **SPEAKER_02:** And if you want to see all the file outputs, you can continue to do that. And then I put on the issue and people still still didn't like it, which is, again, awesome, because like my favorite thing in the world is just hearing people's feedback and hearing how they actually want to use it. And so we just like iterated more and more and more to get that really good and to make it the thing that people want.

> 如果你想看到所有的文件输出,你可以继续这么做。然后我在那个 issue 里回复,人们还是不满意——这同样很棒,因为我在这世上最喜欢的事就是听到大家的反馈,听他们真正想怎么用它。于是我们就一遍又一遍地迭代,把它打磨得非常好,做成人们真正想要的样子。

`[13:32]` **SPEAKER_01:** I'm amazed. Like how much. I enjoy fixing bugs now. And then all you have to do is have really good logging and then even just say, like, hey, check out that, you know, this particular object messed up in this way. And it like searches the log.

> 我很惊讶,现在我竟然这么享受修 bug。你要做的只是有一套很好的日志,然后甚至只要说一句"嘿,看看这个,某个特定对象以这种方式出错了",它就会去搜日志。

`[13:47]` **SPEAKER_01:** It figures everything out. It can like go into your you can make a production tunnel and look at your production DB for you. It's like this is insane. But fixing is just going to century copy mark down, you know, pretty soon it's just going to be straight MCP. It's like an auto bug fixing like and test making.

> 它把一切都搞明白。它可以进去——你可以打一条生产环境的隧道,让它替你查看你的生产数据库。这简直太疯狂了。而修 bug 现在就是去 Sentry 复制那段 markdown,很快就会直接走 MCP 了。它就像一个自动修 bug、自动写测试的东西。

`[14:03]` **SPEAKER_01:** Sort of what's the new term they call it, like making a startup factory.

> 现在有个新说法叫什么来着,像是打造一个"创业工厂"。

`[14:08]` **SPEAKER_03:** Oh, yeah, right.

> 哦,对,没错。

`[14:09]` **SPEAKER_01:** There's like all these concepts now of rather than having to review the code, you know, I'm I'm old school. So I like the verbosity. I like to say, oh, well, you're doing this, but I want you to do that. Right. But there's a totally different school of thought now that says, like, any time a real human being has to look at code, that's bad.

> 现在有各种各样的理念,主张不再需要人去审阅代码。我是老派的,所以我喜欢那种详细的输出,喜欢说"哦,你在做这个,但我想让你做那个"。可现在有一种截然不同的思想流派认为,只要有真人不得不去看代码,那就是坏事。

`[14:29]` **SPEAKER_02:** Yeah. Yeah.

> 对,对。

`[14:30]` **SPEAKER_01:** Yeah. And it's fascinating.

> 对。这很引人入胜。

`[14:31]` **SPEAKER_02:** I think like Dan Chipper talks about this. A lot as kind of whenever you see the model, make a mistake, try to put in the quad MD, try to put it in like skills or something like this. What's reasonable. But I think there's this meta point that I actually struggle with a lot. And people talk about like agents can do this, agents can do that.

> 我觉得 Dan Shipper 经常谈到这一点:每当你看到模型犯了错,就试着把纠正写进 CLAUDE.md,或者写进 skills 之类的地方。这很合理。但我觉得有一个更上层的问题,我自己其实一直很纠结。人们总说 agent 能做这个、能做那个。

`[14:47]` **SPEAKER_02:** But actually what agents can do, it changes with every single model. And so sometimes there's a new person that joins the team and they actually use quad code more than I would have used it. And I'm just constantly surprised by this. Like, for example, there was a we had like a memory leak and we were trying to debug it. And by the way, like Jared Sumner has just been on this crusade killing all the memory leaks.

> 但实际上,agent 能做什么,每一代模型都在变。所以有时候团队来了个新人,他们用 Claude Code 的方式比我用得还狠。这一点让我不断地感到意外。比如说,我们曾经有个内存泄漏,当时正在排查。顺便一提,Jared Sumner 一直在发起一场"消灭所有内存泄漏"的圣战。

`[15:07]` **SPEAKER_02:** And it's just been amazing. But before Jared was on the team, I had to do this and there was this memory leak. I was trying to debug it. And so I took a heap dump. I opened it in DevTools.

> 效果非常惊人。但在 Jared 加入团队之前,这活儿得我来干。当时有个内存泄漏,我在排查,于是我取了一份堆转储(heap dump),用 DevTools 打开它。

`[15:16]` **SPEAKER_02:** I was looking through the profile. Then I was looking through the code and I was just trying to figure this out. And then another engineer on the team, Chris, he just like asked quad code. He was like, hey, I think there's a memory leak. Can you like this and then like try to figure it out?

> 我在翻那个性能剖析,又在翻代码,想把问题弄清楚。而团队里另一位工程师 Chris,他就直接去问 Claude Code,说"嘿,我觉得有个内存泄漏,你能不能试着搞清楚是怎么回事?"

`[15:28]` **SPEAKER_02:** And quad code like took the heap dump. It wrote a little tool for itself to like analyze the heap dump. And then it found the leak faster than I did. And this is just something I have to constantly relearn because my brain is still stuck somewhere six months ago at times.

> 于是 Claude Code 取了堆转储,给自己写了个小工具去分析这个堆转储,然后它比我更快地找到了泄漏点。这就是我不得不反复重新学习的东西,因为我的脑子有时候还停留在六个月前的某个地方。

`[15:43]` **SPEAKER_00:** So what would be some advice for technical founders to really become maximalists at the latest model release? It sounds like people off of fresh off of school or that don't have any assumptions might be better suited than maybe sometimes engineers who have been working at it for a long time. And how do the. Experts get better.

> 那么对技术型创始人来说,要在每次最新模型发布时都把它用到极致,你有什么建议?听起来那些刚出校门、没有任何成见的人,可能反而比一些干了很久的工程师更合适。那么这些专家该怎么变得更强?

`[16:05]` **SPEAKER_02:** I think for yourself, it's kind of beginner mindset and I don't know, maybe just like humility. Like, I feel like engineers as a discipline, we've learned to have very strong opinions and senior engineers are kind of rewarded for this. In my old job at a big company, when I hired like architects and this kind of a type of engineer, you look for people that have a lot of experience and really strong opinions. But it actually turns out a lot of this stuff just isn't relevant anymore. And a lot of these opinions should change because the model is getting better.

> 我觉得对你自己来说,是要有一种初学者心态,还有,大概就是谦逊吧。我觉得工程师这个行当,我们被训练成要有非常强的主见,而资深工程师往往因此受到奖励。在我以前那家大公司的工作里,当我招架构师这类工程师时,你找的是那些经验丰富、主见极强的人。但事实证明,这里面很多东西已经不再适用了,很多主见都应该改变,因为模型在变得越来越好。

`[16:32]` **SPEAKER_02:** Um. So I think actually the biggest skill is people that can think scientifically and can just think from first principles.

> 所以我觉得,其实最重要的能力是能够科学地思考、能够从第一性原理出发思考的人。

`[16:38]` **SPEAKER_00:** How do you screen for that when you try to hire someone now for for your team?

> 那你现在给团队招人的时候,怎么筛选出具备这种能力的人?

`[16:42]` **SPEAKER_02:** I sometimes ask about what's an example of when you're wrong. It's really good on, you know, some of these like classic behavioral questions, like not even coding questions, I think are quite useful because you can see if people can recognize their mistake in hindsight, if they can claim credit for the mistake and if they learn something from it. And I think a lot of these like very senior people, especially there are some founder types like this. But I think founder. Is in particular actually quite good at it.

> 我有时会问"举一个你犯错的例子"。这类经典的行为面试题——甚至都不是编程题——其实非常有用,因为你能看出这个人事后是否能认识到自己的错误、是否愿意为错误担责、是否从中学到了东西。我觉得很多非常资深的人,尤其是有些创始人类型是这样的。而我觉得创始人在这方面其实特别擅长。

`[17:05]` **SPEAKER_02:** But other people sometimes will never really take they'll never take the blame for a mistake. But I don't know, like for me personally, I'm wrong probably half the time, like half my ideas are bad and you just have to try stuff and, you know, you try a thing, you give it to users, you talk to users, you learn, and then eventually you might end up at a good idea. Sometimes you don't. And this is the skill that I think in the past was very important for founders. But now I think it's very important for every engineer.

> 但有些人有时候永远不会真正为错误承担责任。不过对我个人来说,我大概有一半时候是错的,我一半的点子都很烂。你就是得不断去试,你试一个东西,交给用户,和用户交流,从中学习,然后最终你可能会得到一个好点子,有时候也得不到。我觉得这种能力在过去对创始人非常重要,而现在我认为它对每一个工程师都非常重要。

`[17:32]` **SPEAKER_01:** Do you think. You would ever hire someone based on the cloud code transcript of them working with the agent because we're actually doing that right now. We just added just as a test, like you can upload a transcript of you coding a feature with cloud code or codex or whatever it is. Personally, I think that like it's going to work. I mean, you can figure out how someone thinks, like whether they're looking at the logs or not, like can they correct the agent if it goes off off the rails?

> 你觉得你会不会根据某人和 agent 协作的 Claude Code 会话记录来招人?因为我们现在其实正在这么做。我们刚加了一个测试功能,你可以上传一段你用 Claude Code 或 Codex 之类工具开发某个功能的会话记录。我个人觉得这行得通。我是说,你能看出一个人是怎么思考的,比如他们是否在看日志,agent 跑偏了他们能不能把它纠正回来?

`[18:02]` **SPEAKER_01:** Like. Do they use plan mode, you know, when they use plan mode, do they make sure that there are tests or, you know, all of these different things that, you know, do they think about systems? Do they even understand systems like there's just so much that's sort of embedded in that that I imagine I just want like a spider, a spider web graph, you know, like in those video games like NBA 2K and it's like, oh, this person is really good at shooting or defense. It's like you can imagine a spider web graph of like, you know, someone's cloud code skill level. Yeah.

> 比如,他们用不用计划模式?用计划模式的时候,他们有没有确保写了测试?诸如此类的各种事情——他们会不会从系统的角度去思考?他们是否真的懂系统?这里面隐含的信息太多了,以至于我想要一张蜘蛛网图,就像 NBA 2K 那种游戏里那样,标着"哦,这个人投篮很强"或者"防守很强"。你可以想象出一张描绘某人 Claude Code 技能水平的蜘蛛网图。

`[18:30]` **SPEAKER_01:** What would it, what would the skills be? What would be those? I mean, I think it's like systems testing must be like user behavior. I mean, there's got to be a design part for sure. Like product sense, maybe also just like automating stuff.

> 那这些技能会是什么?会有哪些维度?我觉得像是系统、测试,肯定还有用户行为。肯定还有设计的部分,比如产品直觉,也许还有自动化各种东西的能力。

`[18:42]` **SPEAKER_01:** My favorite thing in CloudMD for me is I have a thing that says for every plan, decide whether it's overengineered, underengineered or perfectly engineered and why.

> 我 CLAUDE.md 里最喜欢的一条是:对每一个计划,判断它是过度工程、工程不足还是恰到好处,并说明原因。

`[18:53]` **SPEAKER_02:** I think this is something that we're trying to figure out, too, because I think when I look at engineers on the team that I think are the most effective, there's essentially two. It's very bimodal. There's one side where it's extreme specialists and so like I named Jared before, like he's a really good example of this and kind of the bun team is a really good example, just hyper specialist. They understand DevTools better than anyone else. They understand JavaScript runtime systems better than anyone else.

> 我觉得这也是我们正在试图搞清楚的事,因为当我看团队里我认为最高效的工程师时,基本上分成两类,呈现出很明显的双峰分布。一端是极端的专才,比如我刚提到的 Jared 就是很好的例子,还有 Bun 团队也是很好的例子,超级专精。他们比任何人都更懂 DevTools,比任何人都更懂 JavaScript 运行时系统。

`[19:16]` **SPEAKER_02:** And then there's the flip side of kind of hyper generalists and that's kind of the rest of the team. And a lot of people, they span like product and info or product and design or, you know, like product and user research, product and business. I really like to see people that just do weird stuff. I think that's one of these things that was kind of a warning sign in the past because it's like, can these people actually build something useful?

> 另一端则是超级通才,团队里其余大部分人是这样的。很多人横跨产品与基础设施、或产品与设计、或产品与用户研究、或产品与商业。我特别喜欢看到那些干各种奇奇怪怪事情的人。我觉得这在过去反倒是个警示信号,因为你会想:这些人真的能造出有用的东西吗?

`[19:38]` **SPEAKER_01:** That's the litmus test.

> 那就是试金石。

`[19:39]` **SPEAKER_02:** Yeah, that's the litmus test. But nowadays, like, for example, an engineer on the team, Daisy, she was on a different team and then she transferred onto our team. And the reason that I wanted her to transfer is she put up a PR for Cloud Code like a couple of weeks after she joined or something, and the PR was to add a new feature to Cloud Code. And then instead of just adding the feature, what she did is first. She put up a PR to give Cloud Code a tool so that it can test an arbitrary tool and verify that that works.

> 对,那就是试金石。但如今,比如团队里有位工程师 Daisy,她原来在另一个团队,后来调到了我们团队。我想让她调过来的原因是,她入职大概两周后就给 Claude Code 提了个 PR,那个 PR 是要给 Claude Code 加一个新功能。但她没有直接加那个功能,她先做的是:提了一个 PR,给 Claude Code 加了一个工具,让它可以测试任意一个工具并验证它能正常工作。

`[20:07]` **SPEAKER_02:** And then she put up that PR and then she had Cloud write its own tool instead of herself implementing it. And I think it's this kind of out of the box thinking that is just so interesting because not a lot of people get it yet. You know, like we use the Cloud Agent SDK to automate pretty much every part of development. It automates code review, security review, it labels all of our issues, it shepherds things to production. It does pretty much everything for us.

> 然后她提了那个 PR,再让 Claude 自己去写它需要的工具,而不是她亲自去实现。我觉得正是这种跳出框框的思维方式非常有意思,因为还没多少人领会到这一点。我们用 Claude Agent SDK 几乎自动化了开发的每一个环节。它自动做代码评审、安全评审,给我们所有的 issue 打标签,把东西一路护送到生产环境。它几乎替我们做了所有事。

`[20:30]` **SPEAKER_02:** But I think extremely important. I mean, internally, I'm seeing a lot of people start to figure this out, but it's actually taken a while to figure out how do you use LMS in this way? How do you use this new kind of automation?

> 但我觉得这极其重要。在内部,我看到很多人开始领悟到这一点,但要弄明白怎么以这种方式使用大语言模型、怎么使用这种新型的自动化,其实花了不少时间。

`[20:39]` **SPEAKER_01:** So it's kind of a new skill. I guess one of the funnier things that I've been having office hours with various founders about is you have like sort of the visionary founder who has like the idea they've like built this like crystal palace of the product that they want to build. They've totally loaded in their brain, you know, who the user is and what they feel and what they're motivated by. And then. Yeah.

> 所以这算是一种新技能。我最近和各路创始人办公时间聊到的一件比较有意思的事是:你有那种有远见的创始人,他们脑子里有想法,已经在脑中搭起了他们想做的那个产品的"水晶宫殿"。他们完完全全把用户是谁、用户的感受、用户被什么驱动全都装进了脑子里。然后……对。

`[21:01]` **SPEAKER_01:** They're sitting in cloud code and they can do like, you know, 50 X work and then, but they have engineers who work for them who like don't have the, you know, crystal memory palace of like the platonic ideal of the product that the founder has and they can only do like five X work. Are you hearing stories like that? There's usually a person who's like the core like designer of a thing and they're just like, you know, trying to blast it out of their brain. What's the nature of like teams like that? You know, it seems.

> 他们坐在 Claude Code 前,能干出 50 倍的活儿。但他们手下的工程师并没有那种关于产品理想原型的"水晶记忆宫殿",只能干出 5 倍的活儿。你有没有听到过这样的故事?通常总有一个人是某个东西的核心设计者,他们就是拼命想把脑子里的东西倾泻出来。这样的团队本质上是怎样的?看起来……

`[21:31]` **SPEAKER_01:** Like that's almost a stable configuration. Like you're going to have the visionary who like now is unleashed, but you know, maybe going back to the top of it, like I'm experiencing this right now. It's like, oh, well, I'm only a solo person and you know, I need to eat and sleep and I have, you know, a whole job and it's like, how am I going to do this?

> 这几乎是一种稳定的配置。你会有一个远见者,现在被彻底释放了。但话说回来,回到最开头,我现在自己正经历这个。就是说,哦,我只是一个人,我得吃饭睡觉,我还有一份全职工作,那我到底要怎么做完这些?

`[21:50]` **SPEAKER_02:** You know, you know, like we just launched quad teams and you know, this is a way to do it, but you can also just build your own way to do it. It's pretty easy. What's the vision for cloud teams? Just cooperation. It's like.

> 你知道,我们刚推出了 Claude Teams,这就是一种解决办法,不过你也完全可以自己搭一套自己的办法,挺简单的。Claude Teams 的愿景是什么?就是协作。它就像是……

`[22:00]` **SPEAKER_02:** There's this whole new field of like agent topologies that people are exploring. Like what are the ways they can configure agents? There's this one sub idea, which is uncorrelated context windows. And the idea is just multiple agents. They have fresh context windows that aren't as actually polluted with each other's context or their own previous context.

> 现在有一整个新领域叫"agent 拓扑",人们正在探索——有哪些方式可以配置这些 agent?其中有个子想法叫"不相关的上下文窗口"。意思就是多个 agent,它们各自有全新的上下文窗口,不会被彼此的上下文、或它们自己之前的上下文所污染。

`[22:16]` **SPEAKER_02:** And if you throw more context at a problem, that's like a form of test and compute. Um, and so you just get more capability that way. And then if you have the right topology on top of it, so the agents can communicate in the right way, they're laid out in the right way, then they can just build bigger stuff. And so. Teams is kind of like one idea.

> 如果你给一个问题投入更多的上下文,那就相当于一种"测试时算力"(test-time compute)。这样你就获得了更强的能力。然后如果你在此之上有合适的拓扑结构,让这些 agent 以正确的方式沟通、以正确的方式排布,它们就能构建更大的东西。所以 Teams 算是其中一个想法。

`[22:32]` **SPEAKER_02:** There's a few more that are coming pretty soon. Um, and the idea is just maybe it can build a little bit more. I think the first kind of big example where it worked is our plugins feature was entirely built by a swarm over, over a weekend. It just ran for like a few days. There wasn't really human intervention and plugins is pretty much in the form that it was when, when it came out.

> 还有更多类似的东西很快就会推出。想法就是,也许它能构建出更多东西。我觉得第一个真正跑通的大例子是,我们的插件(plugins)功能完全是由一个 agent 集群(swarm)在一个周末里构建出来的。它就那样跑了几天,基本没有人为干预,而插件功能如今的形态和它当初做出来时几乎一模一样。

`[22:52]` **SPEAKER_01:** How did you set that up? Like, did you spec out sort of the outcome that you were hoping for and then let it sort of figure out the details? And then. Like, let it run.

> 你们是怎么把它搭起来的?比如,你是不是先把你期望的结果大致规定出来,然后让它自己去搞定细节,再让它跑起来?

`[23:02]` **SPEAKER_02:** Yeah. An engineer on the team just gave, uh, gave quad a spec and, um, told quad to use a Asana board and then quad just put up a bunch of tickets on Asana and then spawned a bunch of agents. And the agent started picking up tasks. The main quad just gave it instructions and they all just figured it out.

> 对。团队里一位工程师就给了 Claude 一份规格说明,并让 Claude 使用一个 Asana 看板,然后 Claude 就在 Asana 上建了一堆任务卡,再派生出一堆 agent。这些 agent 开始领取任务。主 Claude 只是给它们下达指令,然后它们就自己把事情都搞定了。

`[23:19]` **SPEAKER_00:** Like independent, um, agents that didn't have the context of the bigger spec. Right.

> 也就是相互独立的 agent,它们并不掌握那份更大规格说明的上下文,对吧。

`[23:23]` **SPEAKER_02:** Right. If you, if you think about the way that, uh, you know, like how our agents actually started nowadays and, you know, I haven't pulled the data on this. But I would bet the majority of agents are actually prompted by quad today in the form of, uh, sub-agents because like a sub-agent is just like a recursive quad code. That's all it is in the code. And it's just prompted by, we call her mama quad and that's all it is.

> 对。如果你想想现在我们的 agent 实际上是怎么被启动的——我还没拉过这方面的数据,但我敢打赌,今天大多数 agent 其实是由 Claude 以子 agent 的形式发起的,因为子 agent 说白了就是一个递归的 Claude Code,在代码里就是这么回事。它就是被我们称为"Mama Claude(妈妈 Claude)"的那个发起的,仅此而已。

`[23:44]` **SPEAKER_02:** And I, I think probably if you look at most agents, they're launched in this way.

> 我觉得如果你去看大多数 agent,它们大概都是以这种方式启动的。

`[23:47]` **SPEAKER_04:** My cloud insights just told me to do this more for debugging so that I get like, I spent a lot of time on debugging and it would just be better to have like multiple sub-agents spin up and like debug something in parallel. And so then I just like added that. To my Claude MD to just be like, Hey, like next time you try and fix a bug, like have one agent that like looks in the log, like one that looks in the code path.

> 我的 Claude Insights 刚建议我在调试时多这么做,因为我在调试上花了很多时间,而更好的做法是启动多个子 agent,并行地去调试某个问题。于是我就把这条加进了我的 CLAUDE.md,大意是"嘿,下次你修 bug 的时候,派一个 agent 去看日志,另一个去看代码路径"。

`[24:07]` **SPEAKER_01:** That just seems sort of inevitable for weird, scary bugs. I try to, uh, fix bugs in plan mode. And then it seems to use the agents to sort of search everything. Whereas like when you're just trying to do it in line, it's like, okay, I'm going to do like this one task instead of search wide. This is something I do all the time too.

> 对那些古怪吓人的 bug 来说,这似乎是不可避免的。我会试着在计划模式下修 bug,那样它似乎就会调用一批 agent 去把所有东西都搜一遍;而如果你只是就地(inline)去修,它就像是"好,我就做这一件事",而不去大范围搜索。这也是我一直在做的事。

`[24:24]` **SPEAKER_02:** I, I just say if the, if the task seems kind of hard, this kind of research task, I'll calibrate the number of sub-agents I ask it to use. Based on the difficulty of the task. So if it's like really hard, I'll say like use three or maybe five or even 10 sub-agents research in parallel and then see what they come up with. I'm curious. So then why don't you put that in your Claude MD file?

> 我会这么说:如果这个任务看起来比较难,是那种研究型的任务,我会根据任务的难度来调整我让它用的子 agent 数量。如果特别难,我会说用 3 个、或者 5 个、甚至 10 个子 agent 并行研究,然后看看它们得出什么。我很好奇,那你为什么不把这条写进你的 CLAUDE.md 文件里呢?

`[24:42]` **SPEAKER_02:** It's kind of case by case, you know, like quite MD, like what is it? It's just a, it's a shortcut. Like if you find yourself repeating the same thing over and over, you put in the quad MD, but otherwise you don't have to put everything there. You can just prompt quad.

> 因为这要看具体情况。CLAUDE.md 是什么呢?它只是一个快捷方式。如果你发现自己在反复重复同一件事,那你就把它放进 CLAUDE.md;但除此之外,你不必把所有东西都放进去,你直接给 Claude 提示就行了。

`[24:54]` **SPEAKER_04:** Are you also in the back of your mind thinking that maybe like in six months, you won't need to prompt that explicitly like the more. Yeah. Yeah. It'll just be good enough to figure out on its own.

> 你心里是不是也在想,也许再过六个月,你就不需要那么明确地去提示了?对,对。它自己就足够聪明,能自行搞定。

`[25:03]` **SPEAKER_02:** Maybe in a month.

> 也许一个月后就能。

`[25:05]` **SPEAKER_00:** No more need for a plan mode in a month.

> 一个月后就不再需要计划模式了。

`[25:07]` **SPEAKER_02:** Oh my God. I think plan mode probably has a limited lifespan. Interesting.

> 我的天。我觉得计划模式大概也活不了太久了。有意思。

`[25:11]` **SPEAKER_00:** That's some alpha for everyone here. What would the world look like without plan mode? Do you just describe it at the prompt level and it would just do it one shot it?

> 这对在座各位都是有价值的内幕信息。没有计划模式的世界会是什么样?你只要在提示层面描述一下,它就能一次性搞定?

`[25:19]` **SPEAKER_02:** Yeah, we've, uh, we've started experimenting with this cause Claude code can now enter plan mode by itself. I don't know if you've, you guys have seen that.

> 对,我们已经开始在试这个了,因为 Claude Code 现在能自己进入计划模式了。不知道你们有没有注意到这一点。

`[25:25]` **SPEAKER_00:** Yeah.

> 注意到了。

`[25:26]` **SPEAKER_02:** So we're, we're trying to kind of get this experience really good. So it would enter plan. Mode the same point where a human would have wanted to enter it. So I think it's like, I think it's something like this, but actually plan mode. There's no, there's no big secret to it.

> 所以我们正努力把这个体验做到非常好,让它在人类会想要进入计划模式的同一个时机自动进入计划模式。我觉得大概就是这样的方向。不过说实话,计划模式没有什么大秘密。

`[25:38]` **SPEAKER_02:** All it does is it adds one sentence to the prompt. That's like, please don't code. That's all it is. You can, you can actually just say that. Yeah.

> 它所做的只是往提示里加一句话,大意是"请先不要写代码"。就这么简单。你其实自己直接说这句话就行了。对。

`[25:45]` **SPEAKER_00:** So it sounds like a lot of the feature development for Claude code is very much, uh, when we talk about YC, talk to your users and then you come and implemented it. It wasn't the other way that you had this master plan and then implemented all the features.

> 所以听起来,Claude Code 的很多功能开发非常符合我们 YC 常说的那句"去和你的用户交流",然后你回来把它实现出来。而不是反过来,你先有一个宏伟蓝图,再把所有功能实现出来。

`[25:58]` **SPEAKER_02:** Yeah. Yeah. I mean, that, that's all it was like plan mode was we saw. Users that, that were like, Hey, Claude, come up with an idea, plan this out, but don't write any code yet. And there was kind of various versions of this.

> 对,对。计划模式就完全是这样来的。我们看到有用户会说"嘿 Claude,想个点子出来,把这个规划一下,但先别写任何代码"。而且这种做法有各种各样的版本。

`[26:07]` **SPEAKER_02:** Sometimes it was just talking through an idea. Sometimes it was these very sophisticated specs that, that they were asking Claude to write, but the common dimension was do a thing without coding yet. And so literally like this was like Sunday night at 10 PM. I was, I was just like looking at GitHub issues and kind of seeing what people were talking about and looking at our internal Slack feedback channel. And I just wrote this thing in like 30 minutes and then, uh, shipped it that night.

> 有时候只是把一个想法聊清楚,有时候是让 Claude 去写那种非常复杂精细的规格说明,但共同点都是"先做一件事但暂时不写代码"。所以说真的,这就是某个周日晚上 10 点,我在看 GitHub 上的 issue、看看大家在讨论什么,看我们内部 Slack 的反馈频道,然后我大概花了 30 分钟就把这东西写出来了,当晚就发布了。

`[26:29]` **SPEAKER_02:** It went out Monday morning. That was plan mode.

> 它周一早上就上线了。那就是计划模式的由来。

`[26:31]` **SPEAKER_04:** So do you mean that there'll be no need for plan mode to, in the sense of I'm worried that the model is going to do, like, it's going to do like the wrong thing or head off in the wrong direction, but there will still be a need for that. You need to think through the idea and figure out exactly what it is that you want. And you have to do that somewhere.

> 那你的意思是说,从"我担心模型会做错事、会朝错误的方向跑偏"这个意义上讲,以后就不需要计划模式了?但从另一个意义上——你仍然需要把想法想透、搞清楚你到底想要什么——这种需求还是存在的,而且你总得在某个地方去做这件事。

`[26:47]` **SPEAKER_02:** I kind of think about it in terms of like kind of increasing model capabilities. So maybe six months ago, a plan was insufficient. So you get Claude to make a plan. Was he even with plan mode, you still have to kind of sit there and babysit because it can go off track nowadays. What I do is probably 80% of my sessions, I say, I say plan mode has a limited lifespan, but I'm a heavy plan mode user.

> 我大致是从"模型能力不断提升"的角度来看这件事的。也许六个月前,光有一个计划还不够,你让 Claude 做一个计划,但即便在计划模式下,你仍然得守在旁边盯着,因为它会跑偏。而如今,我大概 80% 的会话——虽然我说计划模式活不了太久,但我自己是计划模式的重度用户。

`[27:06]` **SPEAKER_02:** Um, I probably 80% of my sessions, I start in plan mode and Claude will, you know, it'll start, it'll start making a plan. I'll move on to my second terminal tab and then I'll have it make another plan. And then when I run out of tabs, I open the desktop app and then I go to the code tab and then I just start a bunch of tabs there. And they all start in plan mode, probably, you know, like 80% of the time. Once the plan is good.

> 我大概 80% 的会话都是从计划模式开始的,Claude 会开始制定一个计划。然后我切到第二个终端标签页,让它再做一个计划。等我把标签页都用完了,我就打开桌面应用,进到代码标签页,在那里再开一堆标签页。它们大概 80% 的时候都是从计划模式开始的。等计划做好了……

`[27:26]` **SPEAKER_02:** And sometimes it takes a little back and forth. They just get Claude to execute. And. Nowadays, what I find with Opus 4.5, I think it started with 4.6.

> ……有时候需要来回沟通几次,然后就让 Claude 去执行。如今我发现,用 Opus 4.5——我觉得其实从 4.6 开始就……

`[27:34]` **SPEAKER_02:** It got really good. Once the plan is good, it just stays on track and it'll just do the thing exactly right. Almost every time. And so, you know, before you had to babysit after the plan and before the plan, now it's just before the plan. So maybe the next thing is you just won't have to babysit.

> ……变得非常好了。一旦计划做好,它就会一直保持在正轨上,几乎每次都能把事情做得完全正确。所以你看,以前你在计划之后和计划之前都得盯着,现在只需要在计划之前盯着了。所以也许下一步就是,你完全不用再盯着了。

`[27:49]` **SPEAKER_02:** You can just kind of give a prompt and Claude will figure it out.

> 你只要给一个提示,Claude 就会自己把它搞定。

`[27:51]` **SPEAKER_01:** The next step is Claude just speaks to your users directly.

> 再下一步就是 Claude 直接去和你的用户对话。

`[27:56]` **SPEAKER_04:** It just bypasses you entirely. It's funny.

> 它把你整个人都绕过去了。真有意思。

`[27:58]` **SPEAKER_02:** This is actually the current stuff, bro. Our Claude's actually like, they talk to each other. They talk to our users on Slack, at least internally, pretty often. Um, my Claude will like tweet once in a while. No way.

> 这其实已经是眼下正在发生的事了,老兄。我们的 Claude 之间真的会互相对话。它们至少在内部相当频繁地在 Slack 上和我们的用户对话。我的 Claude 偶尔还会发推。不会吧。

`[28:08]` **SPEAKER_02:** Um, but I actually like delete it. It's just like, it's a little like cheesy. Yeah. Like, I don't love the tone. What does it want to tweet about?

> 不过我其实会把它删掉,因为有点太肉麻了。对,我不太喜欢那个语气。它想发什么样的推?

`[28:16]` **SPEAKER_02:** Sometimes it'll just like respond to someone. Cause I always have like cowork running in the background and it's like, it's the cowork Claude that really loves to do that. Cause it likes using a browser. That's funny. A really common pattern is I ask Claude to build something.

> 有时候它就是想回复某个人。因为我总是在后台开着 Cowork,而恰恰是 Cowork 里的那个 Claude 特别爱干这种事,因为它喜欢用浏览器。真有意思。一个很常见的模式是:我让 Claude 去构建某个东西。

`[28:26]` **SPEAKER_02:** It'll look in the code base. Uh, it'll see some engineer. It'll touch something in the Git flame and then it'll message that engineer on Slack. Um, just like asking a clarifying question. And then once it gets the answer back, it'll keep going.

> 它会去代码库里查,通过 git blame 看到某个工程师,发现自己要改动的地方和那个工程师有关,然后它就在 Slack 上给那位工程师发消息,问一个澄清性的问题。等它拿到回答之后,就继续往下做。

`[28:37]` **SPEAKER_00:** What are some tips for founders now on how to build for the future? It sounds like everything is really changing. What are like some principles that will stay on and what will change?

> 现在对创始人来说,关于如何为未来做开发,有哪些建议?听起来一切都在剧烈变化。哪些原则会一直不变,哪些会改变?

`[28:47]` **SPEAKER_02:** So I think some of these are pretty, are pretty basic, but I think they're even more important now than they were before. Um, so one example is latent demand. Like I mentioned it a thousand times for me, it's just like the single biggest idea in product. It's a, it's a thing that no one understands. It's a thing.

> 我觉得其中有些原则相当基础,但我认为它们现在比以前更重要了。举个例子就是潜在需求。我已经提了一千遍了,对我来说它就是产品上最重要的一条理念。它是一个没人真正理解的东西。

`[29:03]` **SPEAKER_02:** I certainly did not understand my first few startups and the idea is like people will only do a thing that they already do. You can't get people to do a new thing. If people are trying to do a thing and you make it easier, that's a good idea. But if, if people are doing a thing and you try to make them do a different thing, they're not going to do that. And so you just have to make the thing that they're trying to do easier.

> 我在最初几家创业公司的时候肯定是不理解它的。它的核心是:人们只会去做他们本来就在做的事。你没法让人们去做一件全新的事。如果人们正在努力做一件事,而你把它变得更容易,那就是个好点子。但如果人们正在做一件事,你却想让他们改去做另一件不同的事,他们是不会去做的。所以你要做的,就是把他们本来就想做的事变得更容易。

`[29:20]` **SPEAKER_02:** And I think Claude is going to get increasingly good at kind of figuring out these kinds of product ideas for you. Just cause it can look at feedback. It can look at debug logs, like kind of figure this out.

> 而且我觉得 Claude 会越来越擅长替你想出这类产品点子,因为它可以查看反馈,可以查看调试日志,自己把这些琢磨清楚。

`[29:28]` **SPEAKER_04:** That's what you mean by a plan mode. It was latent demand that people were already like, and it had their Claude chat window open in a browser and we're like talking to it to figure out like the spec and, and what it should do. And now it's the like plan mode just became that you just do it in Claude code.

> 这就是你说的计划模式的意思。它本来就是一种潜在需求——人们已经在浏览器里开着 Claude 的聊天窗口,跟它聊来聊去,搞清楚规格说明、搞清楚它该做什么。而现在,计划模式就变成了你直接在 Claude Code 里做这件事。

`[29:44]` **SPEAKER_02:** Yeah. Yeah. That's it. Sometimes what I'll do is I'll just walk around the office on, on our floor and I'll just kind of stand behind people. I I'll say like, hi. So it's not great. And then, um, I'll, I'll just see kind of like how they're using quad code.

> 对,对,就是这样。有时候我会在办公室我们那层楼里走一走,站到别人身后。我会打个招呼,说声"嗨"——这样其实不太好——然后我就看看他们是怎么用 Claude Code 的。

`[29:52]` **SPEAKER_02:** Um, and this is also just something I saw a lot. Um, but it also came up in.

> 这也是我经常观察的东西。而且它也出现在……

`[29:59]` **SPEAKER_04:** It seems like you're surprised how far the terminal has gone and how far it's been perished. Like how far do you think it has left to go just given with this world of swore multiple agents, like, do you think there's going to be a new, a need for a different UI on top of it?

> 看起来你自己都很惊讶终端能走这么远、坚持了这么久。那你觉得它还能走多远?在这个由集群、多 agent 构成的世界里,你觉得会不会出现对一种全新的、不同界面的需求,凌驾于它之上?

`[30:17]` **SPEAKER_02:** It's funny. If you asked me this a year ago, I would have said the terminal has like a three month lifespan and then we're going to move on to the next thing. Um, and you can see us experimenting with this, right? Cause Claude code started in a terminal, but now it's in, you know, it's on web. You can like.

> 说来有意思。如果一年前你问我这个,我会说终端大概只有三个月的寿命,然后我们就会转向下一个东西了。你能看到我们一直在做这方面的试验,对吧?因为 Claude Code 从终端起步,但现在它已经在网页上了。你可以……

`[30:29]` **SPEAKER_02:** It's in the desktop app. You know, we've had that for, you know, like three months or six months or something just in the code tab. Um, it's in the iOS and Android apps, just like in the code tab. It's in Slack. It's in GitHub.

> 它在桌面应用里。我们的桌面应用里已经有它三个月还是六个月了,就在代码标签页里。它在 iOS 和 Android 应用里,也在代码标签页里。它在 Slack 里,在 GitHub 里。

`[30:41]` **SPEAKER_02:** There's VS code extensions. There's jet brains extensions. So we're just like, we're always experimenting with different form factors for this thing to figure out what's the next thing. I've been wrong so far about the lifespan of the CLI. So I'm probably not the person to forecast.

> 有 VS Code 扩展,有 JetBrains 扩展。所以我们一直在为它试验各种不同的形态,想搞清楚下一个形态会是什么。到目前为止,我对命令行工具寿命的判断一直是错的,所以我大概不是那个适合做预测的人。

`[30:56]` **SPEAKER_04:** What about like your advice to dev tool founders? Like someone's. Building a dev tool company today. Should they just like be building for engineers and humans, or should they be thinking more about like what Claude is going to think and want and build for sort of like the agent?

> 那你对开发者工具类创始人有什么建议?比如今天有人在做一家开发者工具公司,他们应该只为工程师、为人类去做产品,还是应该更多地去思考 Claude 会怎么想、想要什么,从而为 agent 去做产品?

`[31:11]` **SPEAKER_02:** The way I would frame it is think about the thing that the model wants to do and figure out how do you make that easier? And that's something that we saw, you know, like when I first started hacking on cloud code, I realized like this thing just wants to use tools. It just wants to interact with the world. And how, how do you, how do you enable that? Well, the way you don't do it is you put it in a box and you're like, here's the API.

> 我会这样来表述:去想想模型想做什么,然后琢磨怎么让它做起来更容易。这正是我们观察到的——当我最初开始鼓捣 Claude Code 时,我意识到这东西就是想用工具,就是想和世界互动。那你怎么去成全它?错误的做法是把它关在一个盒子里,对它说"喏,这是 API"。

`[31:33]` **SPEAKER_02:** Here's how you interact with me. And here's how you interact with the world. The way you do it is you see what tools it wants to use. You see what it's trying to do. And you enable that the same way that you do for your users.

> "这是你和我互动的方式,这是你和世界互动的方式。"正确的做法是:你去看它想用什么工具,去看它想做什么,然后像你成全你的用户那样去成全它。

`[31:43]` **SPEAKER_02:** And so like for, if you're building a dev tool startup, I would think about like, what is the problem you want to solve for the user? And then when you use, when you apply the model to solving this problem, what is the thing the model wants to do? And then what is the technical and product solution that serves the weight and demand of both?

> 所以如果你在做一家开发者工具的创业公司,我会思考:你想为用户解决的问题是什么?然后当你用模型去解决这个问题时,模型想做的事情是什么?接着,什么样的技术和产品方案能同时服务于两者的潜在需求?

`[31:56]` **SPEAKER_01:** YC's next batch is now taking applications. It's got a startup in you, apply at YCombinator.com slash apply. It's never too early and filling out the app will level up your idea. Okay.

> YC 的下一批正在接受申请。如果你心里有一家创业公司,就去 YCombinator.com/apply 申请吧。永远都不算太早,而且填写申请本身就会让你的点子更上一层楼。好。

`[32:09]` **SPEAKER_01:** Back to the video.

> 回到正片。

`[32:10]` **SPEAKER_00:** Back in the day, more than 10 years ago, you were a very heavy, heavy user and you wrote a book about TypeScript, right? Before TypeScript was cool. This is when everyone was a deep in JavaScript. This is back in early 2010s, right?

> 想当年,十多年前,你是个非常非常重度的用户,还写了一本关于 TypeScript 的书,对吧?那还是在 TypeScript 火起来之前,那时候大家都还深陷在 JavaScript 里。那是 2010 年代初期,对吧?

`[32:25]` **SPEAKER_02:** Yeah. Something like that.

> 对,差不多是那个时候。

`[32:27]` **SPEAKER_00:** Before TypeScript was a thing because back. Then it's a very weird language. It's not supposed to do a lot of things with being typed in JavaScript and now is the right thing. And it feels like cloud code in the terminal has a lot of parallels with TypeScript at the beginning.

> 那是在 TypeScript 还没成气候之前,因为那时候它是一门非常怪异的语言。给 JavaScript 加类型本不该做那么多事情,可如今它却成了正确的做法。我感觉终端里的 Claude Code 和当初的 TypeScript 有很多相似之处。

`[32:44]` **SPEAKER_02:** TypeScript makes a lot of really weird language decisions. So if you look at the type system, pretty much anything can be a literal type, for example. And this is like, this is super weird because like, even though like Haskell doesn't even do this, it's just like, it's too extreme. Or it has like conditional types, which I don't think any language thought of at all.

> TypeScript 做了很多非常怪异的语言设计决策。比如你看它的类型系统,几乎任何东西都可以是字面量类型(literal type)。这非常怪,因为连 Haskell 都不这么干,这实在太极端了。或者它还有条件类型(conditional types),我觉得根本没有别的语言想到过这个。

`[33:05]` **SPEAKER_00:** It was like very strongly typed.

> 它是那种非常强类型的。

`[33:06]` **SPEAKER_02:** Yeah, it was very strongly typed. And the idea was like when, you know, like when Joe Pamer and Anders and the early team was like building this thing, the way they built it is that we OK, we have these teams with these big untyped JavaScript code bases. We have to get types in there, but we're not going to get engineers to change that the way that they code. You're not going to get JavaScript people to have like, you know, 15 layers of class inheritance like you would a Java programmer. Right.

> 对,它是非常强类型的。它的理念是,当 Joe Pamer、Anders 和早期团队在做这东西的时候,他们的做法是:好,现在有很多团队,手里是庞大的、无类型的 JavaScript 代码库。我们得把类型加进去,但我们不可能让工程师改变他们写代码的方式。你没法让 JavaScript 程序员像 Java 程序员那样搞出 15 层的类继承,对吧。

`[33:28]` **SPEAKER_02:** They're going to write code. Right. The way they're going to write it, they're they're going to use a reflection and they're going to use mutation and they're going to use all these features that traditionally are very, very difficult to type.

> 他们会按自己的方式写代码,他们会用反射,会用可变状态(mutation),会用所有这些传统上非常非常难以加类型的特性。

`[33:36]` **SPEAKER_00:** They're a very unsafe type to any strong functional programmers, really.

> 在任何一个坚定的函数式程序员看来,这些东西的类型都非常不安全,真的。

`[33:40]` **SPEAKER_02:** That's right. That's right. That's right. And so the thing that they did instead of getting people to kind of change the way that they code, they built a type system around this. And it was just it's brilliant because there's all these ideas that no one was thinking about, even in academia, like no one thought of a bunch of these ideas.

> 没错,没错,没错。所以他们没有去让人们改变写代码的方式,而是围绕着这些既有的写法构建了一套类型系统。这实在太天才了,因为里面有很多想法是没人想到过的,甚至在学术界都没人想到过这里面的一大堆想法。

`[33:55]` **SPEAKER_02:** It purely came out of the practice of observing people and seeing how JavaScript programmers. Want to write code. And so, you know, for for cloud code, there are some ideas that are kind of similar in that, you know, like you can use it like a Unix utility. You can pipe into it, you can type out of it in some ways. It is kind of rigorous in this way, but in in almost every other way, it's just the tool that we wanted.

> 它纯粹是从实践中来的,来自观察人们、观察 JavaScript 程序员想怎么写代码。对 Claude Code 来说,也有一些类似的理念,比如你可以把它当作一个 Unix 工具来用,你可以用管道把东西输入进去,某种程度上也能把结果输出出来。在这方面它是有点讲究规范的,但在几乎所有其他方面,它就是我们想要的那个工具。

`[34:15]` **SPEAKER_02:** Like I build a tool for myself and then the team builds the tool for themselves and then for anthropic employees and then for users. And it just ends up being really useful. It's not it's not this like principled and academic thing.

> 就是说,我为自己做一个工具,然后团队为他们自己做这个工具,再为 Anthropic 的员工、为用户做这个工具。到头来它就是非常好用。它不是那种讲究原则、学术化的东西。

`[34:27]` **SPEAKER_00:** Which I think the. The proof is actually in the results now, fast forward more than 15 years later, not many code bases are in Haskell, which is more academic, and there's tons of them now in TypeScript because it's way more practical.

> 我觉得,答案其实就摆在结果里。快进 15 年多以后,用 Haskell(更学术)写的代码库并不多,而如今有海量代码库是用 TypeScript 写的,因为它务实得多。

`[34:41]` **SPEAKER_02:** Right.

> 没错。

`[34:42]` **SPEAKER_00:** Which is interesting.

> 这挺有意思的。

`[34:43]` **SPEAKER_02:** Yeah, it is interesting, right? It's like TypeScript solves the problem.

> 对,确实有意思,对吧?就是说 TypeScript 解决了实际问题。

`[34:45]` **SPEAKER_00:** I guess one thing that's cool, I don't know how many people know, but the terminal is actually one of the most beautiful terminal apps out there and is actually written with React terminal.

> 有一件很酷的事,不知道有多少人知道:这个终端其实是市面上最漂亮的终端应用之一,而且它实际上是用 React(终端版)写的。

`[34:57]` **SPEAKER_02:** And when I first started building it, you know, like I did. I've been in front end engineering for for a while, so and I was also like, you know, I'm sort of like a hybrid, like I do like design and user research and, you know, write code and all the stuff. And we love hiring engineers that are like this, so we just we love generalists. So for me, it's like, OK, I'm building a thing for the terminal. I'm actually kind of a shitty Vim user.

> 我最开始做它的时候——我做前端工程有一阵子了,而且我算是那种复合型的人,我做设计、做用户研究、写代码等等。我们特别喜欢招这样的工程师,我们就是喜欢通才。所以对我来说就是:好,我在给终端做一个东西。而我其实是个挺烂的 Vim 用户。

`[35:17]` **SPEAKER_02:** So like, how do I build a thing for people like me that, you know, are going to be working in a terminal? And I think just the delight is so important. And I feel like at YC, this is something you talk about a lot, right? It's like build a thing that people love. The product is useful, but you don't fall in love with it.

> 所以问题就是:我怎么为像我这样的人——将要在终端里工作的人——做一个东西?我觉得"让人愉悦"这一点太重要了。我觉得在 YC 这也是你们经常谈的,对吧?就是做一个人们会爱上的东西。产品有用,但你不会爱上它。

`[35:31]` **SPEAKER_02:** That's not great. So it kind of has to do both. Designing for the terminal, honestly, has been hard, right? It's like it's like 80 by 100 characters or whatever. You have like 256 covers.

> 那样就不够好。所以它得两者兼顾。说实话,为终端做设计一直很难,对吧?你只有大概 80×100 个字符的空间,你只有 256 种颜色。

`[35:40]` **SPEAKER_02:** You have one font size. You don't have like mouse interactions. There's all the stuff you can't do. And there's all these very hard tradeoffs. So like a little known thing, for example, is you can actually enable mouse interactions in a terminal so you can enable like clicking and stuff.

> 你只有一种字号,你没有鼠标交互,有一大堆事情你做不了,还有一大堆非常艰难的权衡。举个鲜为人知的例子:你其实可以在终端里启用鼠标交互,这样就能实现点击之类的操作。

`[35:53]` **SPEAKER_02:** Oh, how do you do that in cloud code? I've been trying to figure out how to do this. We don't we don't have it in cloud code because we actually prototyped it a few times. And it felt really bad because the tradeoff is you have to virtualize scrolling. And so there's all these weird tradeoffs because like the way terminals work is like there's no DOM, right?

> 哦,那在 Claude Code 里怎么做到这个?我一直想搞清楚怎么弄。我们在 Claude Code 里没有这个功能,因为我们其实做过几次原型,但体验非常糟,因为代价是你得把滚动虚拟化。所以有一堆这样古怪的权衡,因为终端的工作方式是没有 DOM 的,对吧?

`[36:07]` **SPEAKER_02:** It's like there's like anti-escape codes and these kind of weird organically evolved specs since like the 1960s or whatever.

> 它靠的是 ANSI 转义码,以及这类从大概 1960 年代一路有机演化下来的古怪规范。

`[36:14]` **SPEAKER_01:** Yeah, it feels like BBSs. It's like a BBS door game. Yeah, yeah, yeah. Oh, my gosh.

> 是啊,它让人想起 BBS。就像一个 BBS 的门户游戏(door game)。对对对。哦,我的天。

`[36:18]` **SPEAKER_02:** That's like that's like a great compliment. Yeah, yeah, yeah. It should feel like you're discovering.

> 那可真是极大的赞美。对对对。它应该给人一种在探索发现的感觉。

`[36:22]` **SPEAKER_01:** Lord of the Red Dragons. Fantastic. Oh, my God.

> 《红龙之王(Legend of the Red Dragon)》。太棒了。哦,我的天。

`[36:24]` **SPEAKER_02:** Yeah, but we have we've had to just like discover all these kind of UX principles for building the terminal because no one really writes about this stuff. And if you look at the big terminal apps of, you know, like the 80s or 90s or 2000s or whatever, these like add curses and they have all these like windows and things like this. And it just looks kind of like janky by modern standards. It just looks too heavy and complicated. And so we had to like reinvent a lot.

> 对,但我们不得不去自己摸索出这一整套为终端做设计的用户体验原则,因为几乎没人写过这方面的东西。如果你看看那些 80 年代、90 年代、2000 年代的大型终端应用,它们用 ncurses,搞出各种窗口之类的东西,按现代标准看就有点粗糙。它们看起来太笨重、太复杂了。所以我们不得不重新发明了很多东西。

`[36:46]` **SPEAKER_02:** And, you know, for example, something like the terminal spinner, like just like the spinner words, it's gone through probably I want to say like 50, maybe 100 iterations at this point. And probably 80% of those didn't ship. So we tried it. It didn't feel good. Move on to the next one.

> 比如说,像终端里那个加载转圈动画(spinner),连它旁边显示的那些词,到现在为止大概经历了 50 次、也许 100 次迭代。其中大概 80% 都没有发布。我们试了一版,感觉不好,换下一版。

`[37:00]` **SPEAKER_02:** Try it. Didn't feel good. Move on to the next one. And this was like sort of one of the amazing things about Quad Code, right? Is like you can write these prototypes and you can just do like 20 prototypes back to back, see which one you like and then ship that.

> 试一版,感觉不好,换下一版。这正是 Claude Code 了不起的地方之一,对吧?你可以写这些原型,可以一口气连做 20 个原型,看看你喜欢哪个,然后把那个发布出去。

`[37:11]` **SPEAKER_02:** And the whole thing takes maybe a couple of hours. Whereas in the past, what you would have had to do is like weren't to use origami or framer or something like this. You built like maybe three prototypes. It took like two weeks. It just took much, much longer.

> 而整个过程大概只需要几个小时。而在过去,你得用 Origami 或者 Framer 之类的工具,你大概只能做三个原型,却要花上两周,耗时长得多得多。

`[37:22]` **SPEAKER_02:** And so we have this luxury of we have to discover this new thing. We have to build the thing. We don't know what the right endpoint is. But we can. We can iterate there so quickly.

> 所以我们享有一种奢侈:我们必须去发现这个全新的东西,必须去把它造出来,我们不知道正确的终点在哪里,但我们能非常快地迭代着逼近它。

`[37:31]` **SPEAKER_02:** And that's what makes it really easy. And that's what lets us build a product that's like joyous and that people like to use.

> 这就是让一切变得轻松的原因,也正是这让我们能做出一个令人愉悦、人们乐于使用的产品。

`[37:36]` **SPEAKER_03:** Boris, you had other advice for builders. And we kept interrupting you because we have so many questions.

> Boris,你之前还有别的给创造者的建议,而我们一直在打断你,因为我们的问题太多了。

`[37:43]` **SPEAKER_02:** I would say, so OK, so maybe two pieces of advice that are kind of weird because it's like about building for the model. So one is don't build for the model of today. Build for the model of six months from now. This is like sort of weird, right? Because like you can't find PMF if the product doesn't work.

> 我想说,好,大概有两条听起来有点怪的建议,因为它们是关于"为模型做开发"的。第一条是:不要为今天的模型做开发,要为六个月后的模型做开发。这听起来有点怪,对吧?因为如果产品跑不通,你就找不到产品市场契合(PMF)。

`[37:58]` **SPEAKER_02:** But actually, this is the thing. This is what you should do because otherwise what will happen is you spend a bunch of work, you find PMF for the product right now, and then you're just going to get leapfrogged by someone else because they're building for the next model and a new model comes out every few months. Use the model, feel out the boundary of what it can do, and then build for the model that you think will be the model maybe six months from now. I think the second thing is, you know, actually in the quad code area where we sit, we have a framed copy of the Bitter Lesson on the wall. And this is this like Rich Sutton blog post.

> 但事实就是,这才是你应该做的,因为否则会发生的是:你费了一堆功夫,为当下这个模型找到了 PMF,然后你就会被别人反超,因为他们是在为下一代模型做开发,而新模型每隔几个月就会出一个。你要使用模型,摸清它能力的边界,然后为你认为大概六个月后会出现的那个模型做开发。第二条是,其实在我们 Claude Code 团队坐的那片区域,墙上挂着一份裱起来的《苦涩的教训(The Bitter Lesson)》,那是 Rich Sutton 的一篇博客文章。

`[38:27]` **SPEAKER_02:** Everyone should read it if you haven't. And the idea is the more general model will always beat the more specific model. And there's a lot of corollaries to this, but essentially what it boils down to is never bet against the model. And so this is just like a thing to that we always think about where we could build a feature into quad code, we could make it better as a product, and we call this scaffolding. That's all this code that's not the model itself.

> 如果你还没读过,每个人都应该读一读。它的核心思想是:更通用的模型永远会打败更专用的模型。这有很多推论,但归根结底就是:永远不要和模型对赌。所以这是我们一直在思考的事——我们可以给 Claude Code 加一个功能,把它作为产品做得更好,我们把这类东西叫作"脚手架",也就是所有那些不属于模型本身的代码。

`[38:50]` **SPEAKER_02:** But we could also just wait like a couple months and the model can probably just do the thing instead. And there's always the straight off, right? It's like engineering work now. And you can kind of extend the capability a little bit, maybe 10, 20% or whatever in whatever domain on this, like, you know, like the spider chart of what you're trying to extend. Or you can just wait and the next model will do it.

> 但我们其实也可以就等上几个月,而模型很可能自己就能把那件事做了。这里总是存在一个权衡,对吧?一边是现在投入工程去做,你能把某个领域的能力——就是你想扩展的那张蜘蛛网图上的某个维度——稍微扩展一点,也许 10%、20%;另一边是你干脆等着,下一代模型就会把它做了。

`[39:09]` **SPEAKER_02:** So just always think in terms of this trade off. Where do you actually want to invest and assume that whatever the scaffolding is, it's just tech debt?

> 所以要始终从这个权衡的角度去思考:你到底想把力气投在哪里?并且假定不管脚手架是什么,它都只是技术债。

`[39:16]` **SPEAKER_00:** How often do you rewrite the code base of a clock code? Is this every six months with this first physical?

> 你们多久重写一次 Claude Code 的代码库?是不是每隔六个月、随着这种"为下一代模型做开发"的思路来一次?

`[39:23]` **SPEAKER_03:** Is there scaffolding that you've deleted because you don't need it anymore because the model just improved?

> 有没有哪些脚手架是你们因为不再需要了而删掉的,就因为模型进步了?

`[39:26]` **SPEAKER_02:** Oh, so much. Yeah. Like all of quad code. Code has just been written and rewritten and rewritten and rewritten over and over and over. We unshipped tools every couple of weeks.

> 哦,多得很。是的,整个 Claude Code 的代码就是被一遍又一遍反复重写出来的。我们每隔几周就下线一些工具。

`[39:34]` **SPEAKER_02:** We add new tools every couple of weeks. There is no product quad code that was around six months ago. It's just constantly rewritten.

> 我们每隔几周又加一些新工具。六个月前的 Claude Code 里没有任何东西还留到现在,它就是在不断地被重写。

`[39:41]` **SPEAKER_00:** Would you say that most of the code base for our current clock code is only, say, 80% of it is only less than a couple of months old?

> 那你会不会说,当前 Claude Code 代码库的大部分——比如 80%——都只有不到几个月的历史?

`[39:48]` **SPEAKER_02:** Yeah, definitely. It might even be like less than, yeah, maybe like a couple of months. That feels about right.

> 对,肯定的。甚至可能还不到几个月。是的,大概几个月,这个数字感觉差不多。

`[39:53]` **SPEAKER_00:** So it's like the lifecycle of code now. That's another alpha is expecting it to be the shelf life to be just a couple of months.

> 所以这就是如今代码的生命周期。这又是一条内幕信息:要预期代码的保质期只有短短几个月。

`[39:58]` **SPEAKER_01:** Yeah.

> 是啊。

`[39:59]` **SPEAKER_00:** For the best founders.

> 对最优秀的创始人来说。

`[40:00]` **SPEAKER_01:** Do you see Steve Yegi's post about how awesome working at Anthropic is? And I think there's a line in there that says that an Anthropic engineer currently averages 1,000x more productivity than a Google engineer at Google's peak, which is really an insane number, honestly, like 1,000x. Three years ago, we were still talking about 10x engineers. Now we're talking about 1,000x on top of a Google engineer in the prime?

> 你看没看 Steve Yegge 那篇讲在 Anthropic 工作有多棒的帖子?我记得里面有一句话说,一名 Anthropic 工程师目前的生产力平均是巅峰期 Google 工程师的 1000 倍,说实话这真是个疯狂的数字,1000 倍。三年前我们还在谈"10 倍工程师",现在我们谈的是在巅峰期 Google 工程师的基础上再乘以 1000 倍?

`[40:28]` **SPEAKER_02:** Like, this is unbelievable, honestly. Yeah, I mean, internally, if you look at like technical employees, they all use quad code every day. And even non-technical employees, I think like half the sales team uses quad code. They've started switching to co-work because it's a little easier to use. It has like a VM, so it's a little bit safer.

> 说实话,这简直难以置信。是的,在内部,如果你看技术类员工,他们每天都用 Claude Code。甚至非技术类员工——我觉得销售团队大概有一半人在用 Claude Code。他们开始转向 Cowork,因为它更好用一点,它带一个虚拟机,所以更安全一点。

`[40:44]` **SPEAKER_02:** But yeah, we actually we just pulled the stat and I think the team doubled in size last year, but productivity per engineer grew something like 70%. As measured by? Just like the simplest, stupidest measure, pull requests. But we also kind of cross-checked that. I mean, we did a lot against like commits and like the lifetime of commits and things like this.

> 但确实,我们刚拉了个数据,我记得团队去年规模翻了一番,但人均工程师的生产力增长了大概 70%。用什么来衡量的?就用最简单、最粗糙的指标——拉取请求(pull request)数量。不过我们也做了交叉验证,比如对照提交(commit)数、提交的存活周期之类的东西核对了很多。

`[41:02]` **SPEAKER_02:** And since quad code came out, productivity per engineer at Anthropic has grown 150%. Oh, my God. And this is crazy because in my old life, I was responsible for code quality at Meta, and I was responsible for the quality of all of our code bases across every product, across like, you know, Facebook, Instagram, WhatsApp, whatever. And one of the things that the team worked on was improving productivity. And back then, seeing a gain of something like 2% in productivity.

> 而自从 Claude Code 问世以来,Anthropic 的人均工程师生产力增长了 150%。哦,我的天。这太疯狂了,因为在我以前的职业生涯里,我在 Meta 负责代码质量,负责我们所有产品、所有代码库的质量——涵盖 Facebook、Instagram、WhatsApp 等等。而我们团队的工作之一就是提升生产力。那时候,能看到生产力提升个 2% 左右……

`[41:28]` **SPEAKER_02:** I mean, it was a year of work by hundreds of people. And so this like 100%, this is just like unheard of, just completely unheard of.

> ……那可是好几百人干上一整年的成果。所以像这种 100% 的增长,简直闻所未闻,完全是闻所未闻。

`[41:35]` **SPEAKER_01:** What drove you to come over to Anthropic? I mean, basically, as a builder, you could go anywhere. What was the moment that made you say, like, actually, this is the set of people or this is the approach?

> 是什么驱使你加入 Anthropic 的?我是说,作为一个创造者,你基本上想去哪儿都行。是哪个时刻让你觉得"没错,就是这群人"或者"就是这条路子"?

`[41:45]` **SPEAKER_02:** I was living in rural Japan and I was opening up Hacker News every morning and I was reading the news and it was all it just started to be like AI stuff at some point. And I started to use some of these early products. And I remember like the first couple of times that I used it, I was just like, it just took my breath away. That was like very cheesy to say, but that was actually the feeling. Like, it was just like, it was amazing.

> 我当时住在日本乡下,每天早上打开 Hacker News 看新闻,某个时刻起,上面全都开始是 AI 相关的内容了。我开始用一些这类早期产品。我记得头几次用它的时候,我简直是——它让我屏住了呼吸。这么说很肉麻,但那确实就是那种感觉。就是那么惊艳。

`[42:08]` **SPEAKER_02:** Like, as a builder, I've just never kind of felt this feeling like using these very, very early products. That was like in the quad two days or something like that. And so I just started talking to friends at Labs just to kind of see what was going on. And I met Ben Mann, who's one of the founders at Anthropic. And he just immediately won me over.

> 作为一个创造者,我从没体会过用这些非常非常早期的产品时的那种感觉。那大概是在 Claude 2 那个时期。于是我就开始找在各家 Labs(研究实验室)的朋友聊,想看看到底发生了什么。我见到了 Ben Mann,他是 Anthropic 的创始人之一,他一下子就把我打动了。

`[42:30]` **SPEAKER_02:** And as soon as I met kind of the rest of the team at Anth, they just won me over. And I think probably in two ways. So one is it operates as a research lab. So the product was teeny, teeny, tiny. It's really all about building a safe model.

> 而当我见到 Anthropic 团队的其余成员时,他们也立刻把我打动了。我觉得大概有两个方面。第一是,它是以一个研究实验室的方式运作的。所以产品当时小得可怜,一切真的都是围绕着构建一个安全的模型。

`[42:43]` **SPEAKER_02:** That's all that matters. And so this idea of just being very close to the model and being very close to development and being not the most important thing because the product isn't anymore. It's just the model is the thing that's the most important. That really resonated with me. And I've been building product for many years.

> 那才是唯一重要的事。所以这种理念——非常贴近模型、非常贴近开发,而产品不再是最重要的东西,只有模型才是最重要的——这让我深深共鸣。而我做产品已经做了很多年了。

`[43:00]` **SPEAKER_02:** And then the second thing was just how mission driven it is. Like I'm a huge sci-fi reader. My bookshelf is just like filled with sci-fi. And so like I just know how bad this can go. And when I kind of think about what's going to happen this year, you know, it's going to be totally insane.

> 第二件事就是它有多么使命驱动。我是个超级科幻迷,我的书架上塞满了科幻小说。所以我很清楚这件事可能坏到什么地步。而当我想到今年会发生什么时,那将会是彻底疯狂的。

`[43:15]` **SPEAKER_02:** And in the worst case, it can go very, very bad. And so I just wanted to be at a place that really understood that and kind of really internalized that. And at Anth, you know, like if you overhear conversations in the lunchroom or in the hallway, people are talking about AI safety. This is really the thing that everyone cares about more than anything. And so I just wanted to be in a place like that.

> 而在最坏的情况下,它可能变得非常非常糟。所以我只想待在一个真正理解这一点、真正把它内化于心的地方。在 Anthropic,如果你在餐厅或走廊里无意中听到别人的谈话,人们谈论的都是 AI 安全。这真的是每个人最在乎的事,胜过一切。所以我就想待在这样的地方。

`[43:33]` **SPEAKER_02:** I know for me personally, the mission is just so important. What is going to happen this year? Okay. So if you think back like six months ago and kind of what are the predictions that people are making? So Dario predicted that 90% of the code at Anthropic would be written by Quad.

> 对我个人而言,这个使命太重要了。今年会发生什么?好。如果你回想大概六个月前,人们当时都做了哪些预测?Dario 预测过,Anthropic 90% 的代码将由 Claude 编写。

`[43:49]` **SPEAKER_02:** This is true. For me personally, it's been 100% for like since Opus 4.5. I uninstalled it. Okay.

> 这是真的。对我个人来说,自从 Opus 4.5 以来就是 100% 了。我把它卸载了。好吧。

`[43:57]` **SPEAKER_02:** I uninstalled my IDE. I don't edit a single line of code by hand. It's just 100% Quad code and Opus. And, you know, I land, you know, like 20 PRs a day every day. If you look at Anthropic overall, it ranges between like 70% to 90%, you know, depending on the team.

> 我卸载了我的 IDE。我不再手写哪怕一行代码,完全 100% 靠 Claude Code 加 Opus。而且我每天要合入大约 20 个 PR。如果看整个 Anthropic,这个比例大概在 70% 到 90% 之间,视团队而定。

`[44:11]` **SPEAKER_02:** For a lot of teams, it's also like 100%. For a lot of people, it's 100%. And I remember making this prediction back in May when we GA'd Quad code that you wouldn't need an IDE to code anymore. And it was totally crazy to say. I feel like people in the audience gasped.

> 对很多团队来说也是 100%,对很多人来说都是 100%。我记得五月我们正式发布 Claude Code 的时候,我做过一个预测:你以后写代码将不再需要 IDE。当时这么说完全是疯了,我感觉台下的观众都倒吸了一口气。

`[44:26]` **SPEAKER_02:** Because it was such like a silly prediction at the time. But really all it is is like you just like trace the, you know, the exponential. And this is just like so deep in, you know, the DNA at Ant. Because like, you know, three of our founders were coauthors of the scaling laws paper. They saw this very early.

> 因为在当时那是个非常荒唐的预测。但其实它无非就是你顺着那条指数曲线往下画而已。而这一点已经深深刻在 Anthropic 的 DNA 里,因为我们有三位创始人是"扩展定律(scaling laws)"论文的共同作者,他们很早就看到了这一点。

`[44:41]` **SPEAKER_02:** And so this is just like tracing the exponential. This is what's going to happen. And yes, that happened. So continuing to trace the exponential, I think what will happen is coding will be generally solved for everyone. And I think today coding is practically solved, you know, for me.

> 所以这无非就是顺着指数曲线往下推:这就是将要发生的事。而没错,它真的发生了。那么继续顺着这条指数曲线推下去,我认为将要发生的是:编程对每个人来说都会被大体解决。而我觉得今天,编程对我来说实际上已经被解决了。

`[44:54]` **SPEAKER_02:** And I think it'll be the case for everyone. You know, regardless of domain. I think we're going to start to see the title software engineer go away. And I think it's just going to be maybe builder, maybe product manager. Maybe we'll keep the title as kind of a vestigial thing.

> 我觉得这对每个人都会成立,无论在哪个领域。我认为我们会开始看到"软件工程师"这个头衔逐渐消失。取而代之的也许会是"创造者",也许是"产品经理"。也许我们会把这个头衔当作一种残留物保留下来。

`[45:06]` **SPEAKER_02:** But the work that people do, it's not just going to be coding. It's software engineers are also going to be writing specs. They're going to be talking to users. Like this thing that we're starting to see right now on our team where engineers are very much generalists. And every single function on our team codes, like our PM's code, our designer's code, our EM codes, our finance guy codes, like everyone on our team codes.

> 但人们所做的工作,将不仅仅是写代码。软件工程师还会写规格说明,会去和用户交流。就像我们团队现在开始看到的那样,工程师非常通才化。而我们团队里每一个职能的人都写代码:我们的产品经理写代码,设计师写代码,工程经理写代码,我们管财务的那位也写代码,团队里每个人都写代码。

`[45:29]` **SPEAKER_02:** We're going to start to see this everywhere. So this is sort of this is kind of like the lower bound if we just continue the trend. The upper bound, I think, is a lot scarier. And this is something like, you know, we hit ASL 4. And, you know, at Anthropic, we talked about the safety levels.

> 我们会开始在各处都看到这种情形。所以如果我们只是顺着这个趋势推下去,这大致算是下限。而上限,我觉得要吓人得多。那就是,比如说我们达到 ASL 4。在 Anthropic,我们谈论的是这些安全等级。

`[45:44]` **SPEAKER_02:** ASL 3 is where the models are right now. ASL 4 is the model is recursively self-improving. And so if this happens, essentially, we have to meet a bunch of criteria before we can release a model. And so the extreme is that, you know, this happens. Or there's some kind of catastrophic misuse.

> ASL 3 是模型目前所处的等级。ASL 4 是指模型能够递归地自我改进。如果这种情况发生,基本上我们在发布一个模型之前必须满足一系列标准。所以极端情况就是,这种事真的发生了;又或者出现某种灾难性的滥用。

`[45:58]` **SPEAKER_02:** Like people are using the model to design bioviruses, design zero days, stuff like this. And this is something that we're really, really actively working on. So that doesn't happen. I think it's just been, honestly, it's just been like so exciting and humbling. Like seeing how people are using quad code.

> 比如人们用模型去设计生物病毒、设计零日漏洞之类的东西。这是我们正在非常非常积极努力防范的事,好让它不会发生。说实话,我觉得这一切既令人激动又令人谦卑,就像看着人们是如何使用 Claude Code 的。

`[46:13]` **SPEAKER_02:** Like, you know, I just wanted to build a cool thing. And it ended up being really useful. And that was so surprising and so exciting.

> 我当初只是想做一个很酷的东西,而它最后竟然真的这么有用。这既让我意外,又让我激动。

`[46:20]` **SPEAKER_04:** My impression from Twitter or just the outside is basically, everyone went away over the holidays and then like found out about quad code. And it's just been crazy ever since. But is that how it was for you at like internet? Did you, were you having like a nice Christmas break and then came back? You're like, what happened?

> 从推特上、或者从外部来看,我的印象基本上是:大家过假期一散,回来后就发现了 Claude Code,从那以后就一直火得不行。但在内部对你来说也是这样吗?你是不是过了个愉快的圣诞假期,回来一看,心想"发生了什么"?

`[46:36]` **SPEAKER_02:** Well, actually, for all of December, I was traveling around. And I took a coding vacation. So we were kind of traveling around and I was just like coding every day. So that was really nice. And then I also started to use Twitter at the time.

> 其实整个十二月我都在四处旅行。我休了一个"编程假期",一边到处旅行一边每天写代码,那感觉真的很好。而且那时候我也开始用推特了。

`[46:46]` **SPEAKER_02:** Because like I worked on threads back then, way back when. So I've been a threads user for a while. So I just like tried to see kind of like, oh. Other platforms where people are. Yeah, I think for a lot of people, they kind of discover, that was the moment where they discovered Opus 4.5.

> 因为我很久以前做过 Threads,所以我用 Threads 有一阵子了。我就想去看看,哦,人们还在别的什么平台上活跃。我觉得对很多人来说,那正是他们发现 Opus 4.5 的时刻。

`[46:59]` **SPEAKER_02:** I kind of already knew. And internally, quad code's just been on this like exponential tear for many, many months now. So that just like, it became even more steep. That's what we saw. And if you look at quad code now, you know, there was some stuff from Mercury that like 70% of startups are, you know, choosing quad as their model of choice.

> 我算是早就知道了。在内部,Claude Code 已经一路指数级狂飙好几个月了。所以那个时候曲线只是变得更陡了,这就是我们看到的。如果你看现在的 Claude Code——Mercury 有份数据说,大约 70% 的创业公司选择 Claude 作为他们首选的模型。

`[47:18]` **SPEAKER_02:** There were some other stuff from like semi-analysis that 4% of all public commits are made by quad code. From like of all code written everywhere. I saw that. All the companies, you know, use quad code from like the biggest companies to kind of, you know, smallest startups. You know, like it wrote, it plotted the course for perseverance.

> 还有 SemiAnalysis 的另一份数据说,所有公开提交(commit)中有 4% 是由 Claude Code 完成的——是从全世界所写的所有代码里算的。我看到那个了。从最大的公司到最小的创业公司,所有公司都在用 Claude Code。比如它还为"毅力号(Perseverance)"规划了航线。

`[47:34]` **SPEAKER_02:** Like for like the Mars Rover. This is just like, this is the coolest thing for me. And we like, we even printed posters. Because the team was like, wow, this is just like so cool. The NASA chooses to use this thing.

> 就是那个火星车。对我来说这真是最酷的事了。我们甚至还印了海报,因为团队都觉得"哇,这太酷了,NASA 竟然选择用这东西"。

`[47:43]` **SPEAKER_02:** So yeah, it's just like, it's humbling. But it also feels like the very beginning.

> 所以是的,这让人心怀谦卑。但同时又感觉,这才只是一个非常初始的开端。

`[47:47]` **SPEAKER_01:** What's the sort of interaction between quad code and then co-work? Like, you know, was it a fork of? Was it like you had quad code look at the quad code code and say, let's make a new spec for non-technical people that, you know, keeps all the lessons. And then, you know, it sort of went off for a couple of days and did that. What's the genesis of that?

> Claude Code 和 Cowork 之间是什么样的关系?它是从前者派生(fork)出来的吗?还是说你让 Claude Code 去看 Claude Code 自己的代码,然后说"我们来为非技术人群写一份新的规格说明,把所有经验教训都保留下来",接着它就跑了几天把这事做了?它的起源是什么?

`[48:07]` **SPEAKER_01:** And, you know, where do you think that goes?

> 你觉得它会走向何方?

`[48:10]` **SPEAKER_02:** This is going to be like my fifth time using the word weight and demand. Yeah. It was just that, I mean, like we were looking at Twitter and there was like that one guy that was using quad code to like monitor his tomato plants. There was like this other person that was using it to like recover wedding photos off of a corrupted hard drive. There were people that using it for like for finance.

> 这大概是我第五次用"潜在需求"这个词了。对,就是那样。我们当时在看推特,有那么一个人在用 Claude Code 监控他的番茄植株。还有另一个人在用它从一块损坏的硬盘里恢复婚礼照片。还有人拿它来做财务。

`[48:28]` **SPEAKER_02:** When we looked internally at Anthropic, every designer is using it. The entire finance team at this point is using it. The entire data science team is using it not for coding. People are jumping over hoops to install a thing in the terminal so that they can use this. So we knew for a while that we wanted to build something.

> 而当我们看 Anthropic 内部时,每一个设计师都在用它。到这个时候,整个财务团队都在用,整个数据科学团队也都在用,而且不是用来写代码。人们不惜费尽周折去在终端里装这么个东西,就为了能用上它。所以我们早就知道自己想做点什么。

`[48:42]` **SPEAKER_02:** And so we're experimenting with a bunch of different ideas. And the thing that kind of took off was just, you know, a little quad code wrapper in a GUI in the desktop app. That's all it is. It's just quad code. There's no code under the hood.

> 于是我们尝试了一堆不同的想法。而真正火起来的,不过就是桌面应用里一个带图形界面(GUI)的 Claude Code 小外壳,仅此而已。它就是 Claude Code,底层没有别的代码。

`[48:53]` **SPEAKER_02:** It's the same agent. Oh, wow. And Felix and the team, and Felix was an early Electron contributor. He kind of knows that stack really well and he was hacking on various ideas. And they built it in I think something like 10 days.

> 它就是同一个 agent。哦,哇。Felix 和团队——Felix 是早期 Electron 的贡献者,他对那套技术栈非常熟悉——他在鼓捣各种想法。他们大概花了 10 天左右就把它做出来了。

`[49:06]` **SPEAKER_02:** It was just like 100% written by quad code. And it just felt ready to release. There was a lot of stuff that we had to build for non-technical users. So it's a little bit different than a technical audience. It runs in a, all the code runs in a virtual machine.

> 它 100% 是由 Claude Code 编写的,而且一做出来就感觉可以发布了。我们有很多东西是专门为非技术用户构建的,所以它和面向技术用户会有点不一样。它运行在——所有代码都运行在一个虚拟机里。

`[49:21]` **SPEAKER_02:** There's a lot of protections for deletion and things like this. There's a lot of permission prompting and kind of other guardrails for users.

> 有很多针对删除之类操作的保护措施,还有很多权限提示,以及为用户设置的其他各种护栏。

`[49:30]` **SPEAKER_01:** But yeah, it was honestly pretty obvious. Boris, thank you so much for making something that is taking away all my sleep. But in return, it's making me feel creator mode again, sort of founder mode again. It's been an exhilarating three weeks. I can't believe I waited that long since November to actually get into it.

> 但确实,说实话它的思路相当明显。Boris,非常感谢你做出了一个夺走我全部睡眠的东西。但作为回报,它让我重新找回了创造者模式,某种程度上又找回了创始人模式。这是令人振奋的三周。我真不敢相信从十一月起我竟然拖了那么久才真正开始用它。

`[49:48]` **SPEAKER_01:** Thank you so much for being with us. And building what you're building.

> 非常感谢你能来到我们节目,也感谢你正在打造的一切。

`[49:52]` **SPEAKER_02:** Yeah. Thanks for having me. And send bugs.

> 好的,谢谢你们邀请我。还有,记得来提 bug。

`[49:55]` **SPEAKER_01:** Sounds good.

> 没问题。
