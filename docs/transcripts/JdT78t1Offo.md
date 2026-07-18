# 全文转录 · Anthropic 联创谈 Claude Code、GPT-3 与 AI 系统设计

> ▶ [YouTube](https://www.youtube.com/watch?v=JdT78t1Offo) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/JdT78t1Offo.md) &nbsp;·&nbsp; Anthropic Co-founder: Building Claude Code, Lessons From GPT-3 & LLM System Design

> 中英对照 · 每段英文原文下附中文翻译

[00:00] **SPEAKER_04:** When we started out we didn't seem like we were gonna be successful at all. OpenAI had a billion dollars and like all of these all of the star power and we had seven co-founders in COVID like trying to build something and we didn't know if we were necessarily gonna make a product or what the products would look like. One thing that's interesting to look at is just that humanity is on track for like the largest infrastructure build out of all time. Tell us about the early

> 我们刚起步的时候，看起来根本不像会成功。OpenAI 有十亿美元，还有那些明星光环，而我们只有七个联合创始人，在疫情期间试图做点东西，我们甚至不确定自己到底会不会做出一款产品，或者产品会是什么样子。有一件事很有意思，那就是人类正走在历史上规模最大的一次基础设施建设的道路上。跟我们聊聊那段早期的

[00:25] **SPEAKER_03:** days of Anthropic. So you had a general idea of this sort of like long-term mission that you wanted to do to you know not destroy humanity but like what did you actually work on for the first year? How did that converge on an actual product? Welcome back to another episode of The Light Cone.

> Anthropic 的日子吧。所以你们心里有一个大致的长期使命，就是你知道的，别毁灭人类，但你们第一年实际上到底做了什么？那是怎么最终收敛到一款真正的产品上的？欢迎回到新一期的《The Light Cone》。

[00:48] **SPEAKER_01:** Today we've got a real treat co-founder of Anthropic Tom Brown. Excited to be here. So Tom one of the things that a lot of the people watching would love to figure out is you got started in tech at the age of 21. Fresh from MIT. How does someone go from that in 2009 to literally co-founding something as important as Anthropic?

> 今天我们有一位重量级嘉宾——Anthropic 的联合创始人 Tom Brown。很高兴来到这里。Tom，很多观众都很想弄明白的一件事是：你 21 岁进入科技行业，刚从 MIT 毕业。一个人怎么能从 2009 年的那个起点，一路走到真正联合创办 Anthropic 这样重要的公司？

[01:12] **SPEAKER_04:** Summer 2009. Linked language. Two of my friends had started that out. I think they had seen one of our other friends Kyle Boat kind of do a YC company and so it was in the water. That's a thing that we could try to do. They started out. I was the first employee. Back then yeah you guys

> 2009 年夏天，Linked Language。我的两个朋友创办了它。我想他们是看到我们另一个朋友 Kyle Boat 做过一家 YC 公司，所以这种念头已经在空气里弥漫开来了——这是一件我们也可以去尝试的事。他们起步，我是第一个员工。那时候，是的，你们

[01:27] **SPEAKER_04:** let me join for all the dinners and stuff like that too. I could have instead gone to like a big tech company or something like that and I think probably just as a software engineer I might have learned more software engineering skills but I think by being there with the other co-founders without anyone telling us what to do basically we like we had to figure out how to live how to like the company would die by default. I think in school there was a lot of like a feeling of more of people would give me tasks and I would do the tasks it's kind of like a dog waiting for like food to be like fed to them in their bowl or something like that and I think it was more like wolves and we have to like hunt our real life food otherwise like where our kids are gonna starve or something like that. I think that that mindset I think has been like the most valuable mindset that shift that I've had for trying to do like bigger more exciting things.

> 也让我参加所有的晚宴之类的活动。我本来也可以去一家大科技公司之类的地方，我想单纯作为一名软件工程师，我可能会学到更多的软件工程技能，但我觉得，和其他联合创始人待在一起、没有任何人告诉我们该做什么，我们基本上得自己想办法活下去——因为这家公司默认就是会死掉的。我觉得在学校里，更多的是那种别人给我布置任务、我去完成任务的感觉，有点像一条狗等着别人把食物喂到它的碗里；而这里更像是狼，我们得自己去猎取现实中的食物，否则我们的孩子就要挨饿了。我觉得这种心态转变，是我为了去做更大、更激动人心的事情所经历过的、最宝贵的一次心态转变。

[02:17] **SPEAKER_01:** Yeah big tech just teaches you to work at a big tech company whereas it's much more fun to be a

> 是啊，大科技公司只会教你如何在大科技公司里工作，而当一头

[02:24] **SPEAKER_02:** wolf. Yeah. How did you go from like so working at friend startup to then you started your own one?

> 狼要有趣得多。没错。那你是怎么从在朋友的创业公司工作，到后来自己创办公司的？

[02:31] **SPEAKER_04:** We ran the company for a bit I ended up going back to school afterwards and then when I left school I went to this company Mopop. That mobile advertising thing right? Yeah yeah I was like the first engineer there I was like okay I want to be a wolf but like I was really bad at programming also I was like very very struggling as like a like software engineer. I know I want to do more but I don't know how to do it yet and so I think that was kind of like experience getting to scale and then we started our first company and then we started the last company and then we started another one that we started with a friend of mine who was my smartest friend from college pitched me on let's go and start a YC company. We did at the time solid stage this was before docker existed and so the idea was try to make it easier to do DevOps but docker doesn't exist so it's going to be a more flexible Heroku which basically meant a more complicated like Heroku and so we I remember

> 我们把公司经营了一阵子，后来我回学校继续念书，离开学校之后我去了一家叫 Mopop 的公司。就是那个做移动广告的，对吧？对对，我是那里的第一名工程师，我当时想，好，我想当一头狼，但我编程真的很糟糕，作为一名软件工程师我也真的非常非常吃力。我知道我想做更多的事，但我还不知道该怎么做，所以我觉得那算是一段积累规模化经验的经历。然后我们创办了第一家公司，接着又办了上一家公司，然后又办了另一家，那家是和我大学里最聪明的一个朋友一起创办的，他游说我说，走吧，我们去办一家 YC 公司。我们当时做的是 Solid Stage，那还是在 Docker 出现之前，所以我们的想法是让 DevOps 变得更容易，但因为 Docker 还不存在，它就得做成一个更灵活的 Heroku，而这基本上意味着一个更复杂的 Heroku。我记得

[03:28] **SPEAKER_01:** we like we interviewed with you guys. I think folks didn't really understand what we were trying to do at the time. I think it's actually sometimes common. Yeah I think we were an outlier there

> 我们去和你们面试。我觉得当时大家并没有真正理解我们想做什么。我想这其实有时候还挺常见的。是啊，我觉得我们在那方面算是个异类。

[03:35] **SPEAKER_04:** because we like did our interviews and then we got called back driving back to San Francisco and TLB had written on the board like an angry frowny face and what are you actually going to build and so he like wanted us to explain that. I guess we explained it enough or he was just like these guys still don't know what they're doing but maybe they'll figure it out. Halfway through I kind of felt I still didn't actually understand what we were going to build and how we would attach a mission to it that like I wanted to to work on for my whole life. Yeah and so I left PG actually introed me to Michael Waxman who was the founder. Yeah so the grouper was a dating app only it was

> 因为我们面试完之后，在开车回旧金山的路上又被叫了回去，TLB 在白板上画了一个生气的皱眉脸，还写着"你们到底要做什么"，所以他想让我们把这个解释清楚。我猜我们解释得还算够，要么就是他心想"这些家伙还是不知道自己在干嘛，但也许他们能搞明白"。做到一半的时候，我其实还是觉得自己并不真正明白我们要做什么，也不明白怎么给它赋予一个我愿意投入一辈子去做的使命。所以我离开了。PG 后来把我介绍给了创始人 Michael Waxman。对，Grouper 是一款约会应用，只不过它的新颖之处在于

[04:15] **SPEAKER_01:** novel in that you had what three guys and three girls. Yeah this was before AI in a lot of ways so there was like a set of a team of people who would manually link people up right yeah and then they'd meet up at a bar and yeah shenanigans would ensue. Yes

> 你们是三个男生对三个女生。对，在很多方面这都是 AI 出现之前的事，所以有一整个团队的人在手动帮大家配对，对吧，然后他们会在酒吧碰面，接着就各种趣事频出。没错。

[04:31] **SPEAKER_04:** shenanigans people didn't always have a great time, I think you want you on a couple. For me for like why I was excited for it was just I was like an incredibly awkward kidding what I wanted to do was to basically have a thing that lets awkward people like me go out and talk to other people. For me to talk to girls and feel like I was safe doing it with like my friends around and stuff like that. And so I think who are going to be our employees was important. I did a all of our engineering interviews we would take someone the only person who went on more was greg brockman i think yeah i think he had he had a phase where like every single week he would go and like post on uh slack or hip chat because he moved to new york and he was hanging out the recurse center during this period i think oh i i think he was at stripe maybe maybe for part of it he was at recurse yeah but he also had uh i think just like a phase where he would just at stripe he would just like post in their thing every like i'm going on a grouper who's going for like a whole year so i i ended up being close with greg which which ended up being a connection to the

> 各种趣事——大家并不总是玩得开心，我觉得你参加过几次。对我来说，我之所以对它感到兴奋，是因为我是个极其笨拙、不善交际的孩子，我想做的其实就是弄出一个东西，让像我这样笨拙的人也能走出去、和别人交谈。让我能和女生说话，而且因为身边有朋友在，会觉得很安全之类的。所以我觉得我们要招什么样的员工很重要。我做了我们所有的工程面试，我们会带着某个人去参加，唯一比我参加得还多的人我想是 Greg Brockman。对，我记得他有一阵子，几乎每个星期都会在 Slack 或 HipChat 上发帖，因为他搬到了纽约，那段时间他常泡在 Recurse Center。哦，我想他当时也许一部分时间在 Stripe，一部分在 Recurse。对，但他也有那么一阵子，就在 Stripe 那边，每次都会在他们的群里发"我要去参加 Grouper 了，谁一起去"，就这样发了差不多整整一年。所以我最后和 Greg 关系变得很好，这也成了通往

[05:35] **SPEAKER_00:** open air what was the journey like because you started as uh you just graduated from mit cs you were 21 you became first an early employee for all these yc startups then you started your company just a couple years later and what was the path for you to eventually become the co-founder of anthropic it was like a long path but it's pretty impressive how did you get there i mean it sounds

> OpenAI 的一条纽带。这段旅程是什么样的？因为你一开始，刚从 MIT 计算机系毕业，21 岁，先是成了这一堆 YC 创业公司的早期员工，然后没几年又创办了自己的公司，那你最终成为 Anthropic 联合创始人的路径是怎样的？这是一条很长的路，但相当令人佩服，你是怎么走到那一步的？我是说，这听起来

[05:59] **SPEAKER_01:** like getting into the business and then you're like oh my god i'm gonna be like oh my god i'm gonna be like oh my god i'm gonna be like oh my god i'm gonna be like oh my god i'm gonna be like oh in touch with greg at that moment some serendipity moment uh and then you were one of the first uh

> 像是进入了这个圈子，然后你就想"天哪、天哪、天哪"，在那个时刻和 Greg 搭上了线，某种机缘巧合的时刻，然后你就成了最早的

[06:05] **SPEAKER_04:** you know a couple dozen people to join open ai as a result yeah so i left grouper 2014 june 2014 and i joined open ai i think a year later i tried to like build up courage to make the switch to be a to try to learn ai research at the time i was like okay it seems like sometime in our lifetimes we might end up making transformative ai if we do that would be the biggest thing maybe there's some way that i could help out but also i got like a b minus in linear algebra in college and so it seemed like at the time you needed to be just top superstar in order to try to help out with that at all and so i think i had like a lot of uncertainty about whether i would be able to help and also i'd had some success with startups and so a lot of me was just like rather than trying to retool at this like i could try to

> 因此加入 OpenAI 的那几十号人之一。对，我 2014 年 6 月离开了 Grouper，大概一年后加入了 OpenAI。当时我努力鼓起勇气去做出转变，去尝试学习 AI 研究。那时候我想，好吧，看起来在我们有生之年，我们也许最终会做出变革性的 AI，如果真做出来，那将是最大的事情，也许我能以某种方式出一份力。但我大学线性代数只拿了个 B-，所以当时看起来，你得是顶尖的超级明星才有可能在这件事上帮上一点忙，因此我对自己到底能不能帮上忙有很大的不确定性。而且我在创业上已经取得了一些成功，所以我心里有很大一部分在想，与其在这件事上从头改造自己，我不如去

[06:55] **SPEAKER_02:** do another startup or something like that i feel like in that period um going to work on ai research which is not seen as like a serious like not like a practically serious thing to do yeah and you're in a world where it's like people try and build companies and these like really practical things like what did your were your friends like oh that's really cool you're gonna work on ai stuff

> 再做一家创业公司之类的。我觉得在那个时期，去做 AI 研究并不被看作是一件正经的、在现实层面上靠谱的事情。对，而你身处的那个世界里，人们都在努力创办公司、做那些非常务实的东西，那你的朋友们当时是什么反应？他们会说"哇，太酷了，你要去做 AI 的东西"

[07:12] **SPEAKER_04:** or was it not really i think my friends were like that sounds that sounds weird and bad kind of like it doesn't really seem like it doesn't seem like like ai safety is i think we should be weird like overpopulation on mars doesn't make any sense and my friends were also just like i don't know if you're going to be good at that tom i think that for that reason i think i didn't try very hard for i like kind of flip-flopped on it for like six months trying to build up courage to

> 还是并不这样？我觉得我的朋友们的反应是"那听起来又怪又不靠谱"，有点像 AI 安全这件事——我觉得我们应该觉得它很古怪——就像"火星人口过剩"一样毫无意义。而我的朋友们也在想"我不确定你能不能做好这个，Tom"。我觉得正因为如此，我并没有很拼命地去争取，我在这件事上来来回回犹豫了差不多六个月，一直在努力鼓起勇气去

[07:35] **SPEAKER_02:** do it and what were you specifically at this point like you're reading research papers like what it

> 做这件事。那在这个阶段你具体在做什么？是在读研究论文吗？那到底是

[07:40] **SPEAKER_04:** what does it look like yeah so first i was just kind of hanging out i built like an art car for titanic zen and stuff like that oh that was fun yeah yeah yeah so i spent like a whole summer like three months after grouper doing that because honestly i was i was like kind of burned out for grouper where i know startups like the highs are high like the lows are low and we weren't working at the end our business was kind of like you know like we were like you know like we were like we were like we were like we were like we were like we were like we were like we were like wasn't succeeding our revenue was going down but i my main job still was like recruiting engineers and so i had to like pitch them on the stream that i'd had but i like no longer really sounds like a death march yeah and so i was super burnt out and i was like okay tom like chill out do some yoga

> 什么样子的？对，一开始我其实就是在瞎晃悠，我给 Titanic Zen 之类的活动造了一辆艺术车（art car）。哦，那很好玩。对对对，所以离开 Grouper 之后，我花了差不多一整个夏天、三个月去做那个，因为老实说我当时对 Grouper 已经有点心力交瘁了。创业你懂的，高的时候很高，低的时候很低，而到最后我们的业务其实并不顺利，营收在下滑，可我的主要工作仍然是招募工程师，所以我还得向他们兜售我心里那套愿景，但我自己已经不再真正相信它了。听起来就像一场死亡行军。对，所以我彻底累垮了，我就想，好吧 Tom，放松一下，做做瑜伽

[08:14] **SPEAKER_01:** like do some crossfit like build an art car what was the hindsight like you know hindsight's 2020 what's the retrospective on like grouper obviously attracted all these really really smart people the graphs were up and to the right and then it flatlined and maybe started declining what happened

> 做做 CrossFit，造辆艺术车。那事后回过头看是怎么样的？你知道的，事后诸葛亮总是看得清清楚楚，你现在怎么复盘 Grouper？它显然吸引了这么一堆非常非常聪明的人，图表一路向右上方走，然后就走平了，甚至可能开始下滑，到底发生了什么？

[08:30] **SPEAKER_04:** i think that when we started the competition was like okay cupid it was all web-based all web-based the main problem that i think we were solving was the it's hard to like go and put yourself out there and go like talk to someone new and they might just be like i don't want to talk to you you seem weird and so we solved that by just blind matching tinder came out while we were doing grouper and tinder solved that same problem with both people have to show interest before you get matched so there's also no worries about getting rejected and i think that they just had better that was a better solution to that same problem so good work tinder good work all the swipers i think that that that solved the like mission that we were trying to solve better than we solved it and then yeah like when did you get serious about ai and just how did you approach it three months of like kind of playing and having fun and then i ran out of money also when i had like my personal runway i i ran out and so i was like okay i think that i'm going to need six months of stealth study to have a shot at getting like a good deal of money and you know a job at that point it was deep mind or Google brain were the two places to do work there or Miri Miri was the third one that I was looking at so I was like if I want to help out with that those are the three places to look at I don't have any of the skills yet I need six months of self-study to feel like I would not be a drag on them and like actually be helping instead can you

> 我觉得当我们起步的时候，竞争对手是 OkCupid，全都是基于网页的。我觉得我们要解决的主要问题是：走出去、把自己暴露在外、去和一个陌生人搭话是很难的，因为对方可能就直接说"我不想跟你聊，你看起来很怪"。所以我们的解决办法是盲配对。我们做 Grouper 的时候 Tinder 出现了，Tinder 用另一种方式解决了同样的问题——双方都要先表示有兴趣才会匹配上，所以也就不用担心被拒绝。我觉得他们就是有一个更好的方案来解决同一个问题，所以 Tinder 干得漂亮，所有划屏的人干得漂亮。我觉得他们把我们想要解决的那个使命解决得比我们更好。那你是什么时候开始认真对待 AI 的，又是怎么着手的？玩了、乐了三个月，然后我也没钱了，我个人的资金跑道也用完了，于是我就想，好吧，我觉得我需要六个月的埋头学习，才有机会拿到一笔像样的钱，以及一份工作。那时候能做这方面工作的两个地方是 DeepMind 或 Google Brain，我在考虑的第三个是 MIRI。所以我想，如果我要在这件事上帮上忙，那这三个地方就是要去看的，可我现在一点相关技能都没有，我需要六个月的自学，才能觉得自己不会拖他们后腿，而是真的在帮上忙。你能不能

[09:50] **SPEAKER_00:** maybe explain a bit what was a self-study like because I'm sure there's a lot of software engineers right now in their 20s are looking to a tool to become AI researchers what was what was that six months like even though as you said you had a gotten a B minus in linear algebra just like core might have

> 也许稍微解释一下自学是什么样子的？因为我敢肯定现在有很多二十几岁的软件工程师正想找条路成为 AI 研究员。那六个月是什么样的？尽管像你说的，你线性代数只拿了 B-，基础可能……

[10:06] **SPEAKER_04:** been a C plus impressive where you got to yeah yeah it turned out okay first I did a contract actually with twitch and like earned like enough to have that six months of runway so I did like three month contract with twitch and then I made a plan to self-study I don't think it's the right plan now for people to get at least the 2015 what did it look like it was like take a Coursera course on machine learning try to solve some Kaggle projects read linear algebra done right and I had a statistics textbook I think I had YC alumni credits and so I bought like a GPU and I would like SSH into the GPU to like work through my courses for it and this is right after

> 也许其实是 C+。你能走到今天真的很厉害。对对，结果还不错。首先我其实接了个和 Twitch 的合同，赚到的钱足够撑起那六个月的跑道，我给 Twitch 做了差不多三个月的合同，然后制定了一个自学计划。我觉得那对现在的人来说已经不是合适的计划了，不过至少 2015 年是这样。它是什么样的呢？就是上一门 Coursera 的机器学习课，试着做几个 Kaggle 项目，读《Linear Algebra Done Right》，我还有一本统计学教材。我记得我有 YC 校友的额度，所以我买了一块 GPU，我会 SSH 登进那块 GPU，用它来一步步做我的课程作业。这正好是在

[10:51] **SPEAKER_00:** yeah it was already after I like snack right it was after Alex night yeah so I

> 对，那已经是在 AlexNet 之后了，对吧？是在 AlexNet 之后。对，所以我

[10:55] **SPEAKER_04:** was mostly doing image image classification and stuff that I was trying to learn was like the thing that all the courses

> 主要在做图像分类，我当时试图学的东西就是所有课程

[11:01] **SPEAKER_00:** would teach you to do how did you get the open AI job because you were one of the few engineers it was mostly researchers and they had a pretty stacked

> 都会教你去做的那些。那你是怎么拿到 OpenAI 那份工作的？因为你是为数不多的工程师之一，那里大多是研究员，而且他们有一支阵容相当豪华的

[11:09] **SPEAKER_04:** team of researchers I messaged Greg as soon as open air was announced and I was like I'd love to help out in some way I got to be minus in my linear algebra but I know some engineering I've done a bit of distributed systems work if you guys need help I'm like happy to mop floors if if you guys need I want to help out however and I think Greg was like yeah I think there's like a paucity of people who he said paucity to it I was like fancy word there there's a paucity of people who know both machine learning and distributed systems so like yes you should do that I think he introduced me to Peter Abiel also to help me put together like a little course for myself too and then I checked in on with him I think every month or something and then after a couple months he was like oh we actually have a project which is uh we need to put together we want to play a gay like play games can you help uh make Starcraft environment and so I joined to like help them with the Starcraft uh environment so that that ended up I think getting my foot in the door I I didn't do any machine learning work with

> 研究员团队。OpenAI 一宣布成立，我马上就给 Greg 发了消息，我说我很想以某种方式出一份力，我线性代数只有 B-，但我懂一些工程，也做过一点分布式系统的工作，如果你们需要帮忙，我很乐意去拖地板，只要你们需要，我想以任何方式帮上忙。我记得 Greg 说，是啊，我觉得同时懂机器学习和分布式系统的人很匮乏（paucity）——他用了 paucity 这个词，我心想，好高级的词——这样的人很匮乏，所以，对，你应该来做。我记得他还把我介绍给 Peter Abbeel，帮我给自己拼凑出一门小课程。然后我大概每个月都会去和他联系一下，几个月后他说，哦，我们其实有个项目，我们需要搭建，我们想玩游戏，你能不能帮忙做一个星际争霸的环境？于是我就加入进去帮他们做星际争霸的环境，我想这最终让我算是踏进了门。头一段时间我完全没做任何机器学习方面的工作，

[12:08] **SPEAKER_02:** them for the first nine months that I was there basically and what did opening I feel like at this point like had it raised much funding did it have like an office is what would it do you feel

> 基本上我在那里的头九个月都是如此。那这时候的 OpenAI 给人什么感觉？它当时筹到很多资金了吗？有没有一个办公室？它给你的感觉是

[12:18] **SPEAKER_04:** like a startup so it was in the chocolate on top of the dandelion chocolate factory um this is after Greg's apartment that's the after Greg's apart yeah so like right after Greg's apartment in the factory when it kicked off right it was like a billion dollars of committed funding from Elon it

> 像一家创业公司。它当时在 Dandelion 巧克力工厂楼上。嗯，这是在 Greg 的公寓之后。对，就在 Greg 的公寓之后，搬到那个工厂里，它启动的时候，对吧，有来自 Elon 承诺的十亿美元资金，它

[12:32] **SPEAKER_00:** felt like it was like very solid the other interesting milestone for you was when you got to build a lot of the engineering around the training for GPT yeah for GPT3 for and how what was that because you got from GPT2 was in tpus right yep and the big breakthrough in GPT3 was

> 感觉非常稳。你另一个有意思的里程碑是，你后来负责搭建 GPT 训练相关的大量工程工作。对，GPT-3。那是怎么回事？因为你们从 GPT-2 是在 TPU 上跑的，对吧？对。而 GPT-3 的重大突破在于

[12:53] **SPEAKER_04:** like use more compute and using GPUs yeah so I ended up working at openai for a year left went to Google brain for a year came back and then GPT3 was 2018 through 2019 was like building up to GPT3 which exactly as you said was like scaling things up I think that like Dario had seen the big trend of scaling laws basically you published a paper for that yeah yeah and that's

> 使用更多算力，并且用 GPU。对，所以我在 OpenAI 干了一年，离开去 Google Brain 待了一年，然后又回来，GPT-3 是 2018 到 2019 年间在为其铺路，正如你说的，就是把规模做大。我觉得 Dario 已经看到了扩展法则（scaling laws）这个大趋势，基本上你们还就此发表了一篇论文。对对，那

[13:16] **SPEAKER_00:** like a pretty important paper that now has withstood the test of time and we're living now

> 是一篇相当重要的论文，如今已经经受住了时间的考验，而我们现在正活在

[13:22] **SPEAKER_04:** the dream of it definitely like seeing that line of reliably you get more intelligence if you spend money was the main thing that was at least for me it was like this is a thing that's like happening happening now because you could look even at the time we weren't spending very much money on the on the training jobs at the time and you could see that there was scaling there and then also Danny Hernandez did a paper at the time that showed how much cheaper algorithmic efficiency was making stuff over time too and like those two things stack together that was like oh wow we're gonna get a lot more Intelligence over the next few years so it was noteworthy and

> 它所描绘的那个梦想里。看到那条曲线——只要你花钱，就能可靠地得到更多的智能——这至少对我来说是最主要的一点，我当时的感觉是"这是一件正在发生、此刻正在发生的事"。因为哪怕在当时，你也能看出来，我们那时在训练任务上花的钱其实并不多，而你能看到那里确实存在扩展效应。同时 Danny Hernandez 那时也发了一篇论文，展示了算法效率随时间推移让成本变得多么便宜。这两件事叠加在一起，就让人觉得"哇，接下来这几年我们会得到多得多的智能"，所以它很值得注意，也

[13:57] **SPEAKER_01:** surprising

> 令人惊讶。

[13:58] **SPEAKER_04:** surprising when you saw it yeah and I think the thing that seemed the weirdest to me is like I'm not a physicist but like all these physicists were doing this stuff the like original scaling laws paper just the like very straight line over like 12 orders of magnitude I'm just like 12 orders of magnitude is like just like a stupidly large amount of I've like never seen anything go over 12 orders of magnitude that convinced me to definitely pivot all of my work into scaling

> 你看到它时确实很惊讶。对，我觉得对我来说最诡异的一点是，我不是物理学家，但当时都是这些物理学家在做这件事，最初那篇扩展法则的论文里，那条几乎笔直的直线横跨了大约 12 个数量级。我就想，12 个数量级简直是荒谬地大的一个范围，我从没见过任何东西能横跨 12 个数量级。这让我彻底下定决心，把我的全部工作转向扩展（scaling），

[14:23] **SPEAKER_01:** which I hadn't been doing before can I asked a like kind of layperson question I mean is it fair to say that the scaling law might show up in all of these other domains then they're like are there like two five a hundred ten thousand domains where the scaling law could hold that we're just

> 而在那之前我并没有做这个。我能问一个有点外行的问题吗？我是说，能不能这样讲：扩展法则也许会在所有这些别的领域里出现？会不会有两个、五个、一百个、一万个领域里扩展法则也成立，只是我们

[14:40] **SPEAKER_04:** not investing into yeah so I think in physics scaling laws hold all over the place which I didn't know at the time but within physics like there's a whole field called phenomenology that basically looks at various aspects of the world and then does those types of fits and they they find these like power law distributions all over the all over the place this was like I think the first one that I had ever seen in a um like computer science adjacent thing which I think was like interesting and surprising and

> 还没有投入进去而已？对，我觉得在物理学里，扩展法则到处都成立，这一点我当时并不知道。但在物理学中，有一整个叫做"唯象学"（phenomenology）的领域，基本上就是去观察世界的各个方面，然后做这类拟合，他们到处都能发现这种幂律分布。而这大概是我第一次在一个和计算机科学相关的东西里看到它，我觉得这既有趣又令人意外。

[15:11] **SPEAKER_01:** and at the time it was people were mad about it they actually were like you're throwing money at gpus or just like wasting money this is very wasteful yeah that was sort of people yes different people now but still people mad about it yeah yeah I guess yeah the researchers were

> 而且当时人们对此很恼火，他们真的会说"你就是往 GPU 上砸钱，纯粹是在浪费钱，这太浪费了"。对，那算是一部分人。是啊，现在虽然换了一批人，但还是有人对此恼火。对对，我想是的，研究员们也

[15:28] **SPEAKER_04:** mad at that too where it's like it's it's not elegant you're just like brute forcing it the like jester cap like stack more layers like which I think I think like anthropic's slogan I think is like do the stupid thing that works that was a thing where like this was very clearly the very

> 对此很恼火，因为这不优雅，你就是在用蛮力硬砸，就像戴着小丑帽喊"多叠几层"。我觉得 Anthropic 的口号大概就是"去做那件看起来很蠢但管用的事"。而这件事非常明显就是那个非常

[15:42] **SPEAKER_00:** stupid thing that that works can you uh tell us then how you ended up collecting the last Infinity Stone with the topic yeah with anthropic because there's very few people in the world that basically worked at openai DeepMind and anthropic and you were part of the team that spun off from gpt3 yep and then started anthropic so how was how was that jump there were two teams there that was

> 蠢但管用的事。那你能不能给我们讲讲，你最后是怎么集齐最后一颗无限宝石的——就是 Anthropic。因为世界上很少有人基本上先后在 OpenAI、DeepMind 和 Anthropic 都工作过，而你是从 GPT-3 那支团队里分出来的成员之一。对，然后创办了 Anthropic。那这一跳是怎么完成的？那里当时有两支团队，

[16:05] **SPEAKER_04:** the safety org and the scaling org were the two orgs that reported into Dario and daniella I think we had just like worked together extremely well one thing I think that was great both at openai and and at anthropic was just like we had a culture where like everything is on slack 100 percent of things on slack and within that all public channels great communication I think that that group also was the group that took the scaling laws the most seriously where it was like okay like this actually is going to be transformative there's going to be a handoff where like humanity will hand off control to transformative AI at some point and hopefully like they'll be aligned with us and like that'll be a good transition that goes well but it might not be the stakes are incredibly high and so I think that group was very focused on like how do we ensure that that's taken seriously enough and that like we've built an institution that can handle the weight of that that ended up being the core group that left to join anthropic and I think I think it wasn't clear at all to me that like that was the right thing for the world at the time in hindsight now it seems like that was a good choice I think what was kind of cool then too is when we started out we didn't seem like we were gonna be successful at all openai had a billion dollars and like all of these all of the star power and we had seven co-founders in covid like trying to build something and we didn't know if we were necessarily going to make a product or what the products would look like and so I think that what was interesting from that too is that all of the initial people who joined were there for the mission too they all could have worked somewhere else for more prestige more more more money people would have known what they were doing Etc well stayed at opening high exactly yeah that exactly that's been an interesting thing then that I think has been like the key to like letting our culture or like let our org scale we're like 2 000 people now but we still have a thing where it doesn't seem like politics have creeped in and I think a lot of that is like the first hundred people all were just there for the mission so like if something starts to go wrong they'll like raise their hand and be like it seems like this person might not be acting for the for the mission YC's

> 安全团队和扩展团队，是两支向 Dario 和 Daniela 汇报的团队。我觉得我们只是配合得极其默契。我觉得在 OpenAI 和在 Anthropic 都很棒的一点是，我们有一种文化，就是一切都在 Slack 上，百分之百的事情都在 Slack 上，而且所有的公开频道都保持着很好的沟通。我觉得那个群体也是最认真对待扩展法则的群体，他们的想法是：好吧，这真的会带来变革，未来会有一次交接，某个时刻人类会把控制权交给变革性的 AI，但愿它们会与我们的价值观对齐，那将是一次顺利而美好的过渡——但也可能不是，这里的赌注极其之高。所以我觉得那个群体非常专注于：我们如何确保这件事被足够认真地对待，以及我们建立起一个能够承受这份重量的机构。这最终成为了离开去加入 Anthropic 的核心群体。我觉得当时对我来说，这对世界而言是不是正确的选择完全不清楚，可事后看来，现在这似乎是个好选择。我觉得那时还有一件挺酷的事：我们刚起步时，看起来根本不像会成功，OpenAI 有十亿美元和那些明星光环，而我们只有七个联合创始人，在疫情期间试图做点东西，我们甚至不知道自己到底会不会做出一款产品，或者产品会是什么样。所以我觉得从中有意思的一点是，最初加入的所有人也都是为了使命而来，他们本可以去别的地方获得更高的声望、更多更多的钱，别人也会知道他们在做什么，等等。或者留在 OpenAI。没错，正是如此。这后来一直是件很有意思的事，我觉得它是让我们的文化、让我们的组织得以扩张的关键——我们现在差不多有两千人了，但我们仍然保有一种状态，看起来内部政治并没有渗进来。我觉得这在很大程度上是因为最初的一百个人全都是纯粹为了使命而来，所以一旦有什么开始出问题，他们就会举手说"看起来这个人可能不是在为使命行事"。YC 的

[18:10] **SPEAKER_01:** next batch is now taking applications got a startup in you apply at ycombinator.com slash apply it's never too early and filling out the app will level up your idea okay back to the video

> 下一批正在接受申请。你心里有个创业点子吗，去 ycombinator.com/apply 申请吧，永远不嫌早，而且填写申请本身就会让你的想法更上一层楼。好，回到视频。

[18:23] **SPEAKER_03:** maybe tell us about the early days of Anthropic so the the seven of you broke off from open AI you had a general idea of this sort of like long-term mission that you wanted to do to you know not destroy humanity but like how did what did you actually work on for the first year how did that

> 也许给我们讲讲 Anthropic 的早期日子吧。你们七个人从 OpenAI 分了出来，心里有一个大致的长期使命，就是你知道的，别毁灭人类，但你们第一年实际上到底做了什么？那是怎么

[18:41] **SPEAKER_04:** convert on an actual product so first year the main thing that I tried to do was just build the training infrastructure that we needed to train a model and then get the compute that we needed to train the model those were like my two main projects all the other things that you need to do when you're like starting up a company too so like set up a brex account and like I don't know like all of that all of that stuff we started out with seven co-founders within like a few months I think like 25 folks from open AI overall had joined so we had like a pretty substantial team that like already knew how to work together too and so that helped us get up and running faster and at what point did you launch the first product and when

> 最终收敛到一款真正产品上的？第一年我主要试图做的就是搭建训练一个模型所需的训练基础设施，然后拿到训练模型所需要的算力，这算是我的两个主要项目。还有创办一家公司时你需要做的所有其他事情，比如开一个 Brex 账户，还有，我也说不全，反正就是所有那些杂事。我们一开始有七个联合创始人，几个月内，我记得总共大约有 25 个来自 OpenAI 的人加入了，所以我们有一支相当可观、而且已经知道如何协同工作的团队，这帮助我们更快地把公司运转起来。那你们是在什么时候推出第一款产品的？又是什么时候

[19:20] **SPEAKER_03:** did things begin to actually start working so

> 事情开始真正奏效的？

[19:23] **SPEAKER_04:** the first product that we launched was after chat GPT we had like a maybe nine months before chat GPT

> 我们推出的第一款产品是在 ChatGPT 之后。我们大概在 ChatGPT 之前九个月就有了

[19:30] **SPEAKER_01:** we had a slackbot version of like Claude one oh yeah we had that in the YC uh yeah I remember like

> 我们有一个 Slackbot 版本、类似 Claude 一代的东西。哦对，我们在 YC 就有那个了。对，我记得

[19:39] **SPEAKER_04:** Tom Blomfield adding all of you guys to it and then I think that at the time though we didn't know whether or not we wanted to launch it as a product we didn't know if doing so would be good for the world at the time I think we hadn't really thought through our theory of impact that much for like how we actually will make stuff work well plus I think actually in hindsight like if we tried to launch it we like wouldn't have had the serving infrastructure to have done it and I think because we weren't sure whether or not we wanted to we like hesitated for too long on building that infrastructure which I think is

> Tom Blomfield 把你们所有人都加进去了。不过我觉得那时候我们并不知道自己是否想把它作为一款产品发布，我们不确定这样做对世界是不是好事。当时我觉得我们还没有真正把我们的"影响力理论"想透，也就是我们究竟要怎么把事情做好。而且事后看，我觉得就算我们当时想发布它，我们也没有能支撑它的服务基础设施。我觉得正因为我们不确定自己想不想做，我们在搭建那套基础设施上犹豫了太久，我觉得这是一个

[20:10] **SPEAKER_01:** learning for for me I mean at this time chat GPT had not launched yet chat GPT hadn't launched and

> 教训。对我来说……我是说，这时候 ChatGPT 还没发布。ChatGPT 还没发布，

[20:16] **SPEAKER_00:** so I guess we didn't know that it would be a big deal too this is around the pandemic 2022 this is

> 所以我猜我们也不知道它会是件大事。这大概是疫情前后，2022 年，这是

[20:23] **SPEAKER_04:** when chat GPT launched fall 2022 and then we we launched our API after that and then Claude AI after that also I think it didn't seem like it was working basically until Claude 3 5 and coding I think like really really like through that whole time then until about a year ago it seemed like it wasn't clear that we were going to end up being like a successful company we just saw that in the

> ChatGPT 发布的时候，2022 年秋天。然后我们在那之后推出了我们的 API，再之后又推出了 Claude AI。我觉得基本上直到 Claude 3.5 和编程能力出来之前，看起来它都不像是奏效了。我觉得在那整段时间里，直到大约一年前，我们最终能不能成为一家成功的公司都还不明朗。我们只是看到

[20:53] **SPEAKER_00:** terms of what is the preferred model for startups so all of 2023 open AI open AI was the response yeah then things started to turn in 2024 is when uh we saw Claude 3.5 and especially sonnet it was starting to get a market share per se in the YC batches going from single digit to at some point like 20 and to 30 percent and especially for coding yeah became the default choice which was very interesting can you tell us about how that emergent behavior and the spikiness was on that particular skill must be 80 now or 90. yeah for coding even more especially now clock code what was that was that on purpose or just can happen I think that we invested more in trying to

> 就创业公司偏好用哪个模型而言。整个 2023 年，答案都是 OpenAI，OpenAI。对，然后到 2024 年情况开始转变，我们看到了 Claude 3.5、尤其是 Sonnet，它在 YC 各批次里开始拿下市场份额，从个位数一路涨到某个时候的 20%、30%，尤其是在编程上，成了默认选择，这非常有意思。你能不能跟我们讲讲那种涌现出来的行为，以及它在这项特定技能上的"尖峰"特性？现在肯定得有 80% 或 90% 了吧。对，编程上更高，尤其现在有了 Claude Code。那是怎么回事？是有意为之，还是就那么发生了？我觉得我们投入了更多去努力

[21:36] **SPEAKER_04:** make the model really good at code because we wanted the model to be good at code was one thing and then I think seeing seeing the reaction of everyone to it was like okay yeah like let's go

> 把模型的编程能力做得非常强，因为我们希望模型擅长编程，这是其一。然后我觉得，看到大家对它的反应，就让我们觉得"好，那我们就

[21:48] **SPEAKER_03:** much harder on that also and this is before 3.5 sonnet you'd already invested enough in coding to realize that that was really promising and you said I decided to

> 在这方面更加使劲"。而这还是在 3.5 Sonnet 之前，你们就已经在编程上投入得足够多，意识到它真的很有前途，然后你说你们决定

[21:57] **SPEAKER_04:** double down I think this really was like individuals within the org being like we want to do coding uh before three five sonnet and then when we saw three five sonnets really good product market

> 加倍投入。我觉得这真的是组织内部有一些个人在说"我们想做编程"，那是在 3.5 Sonnet 之前，然后当我们看到 3.5 Sonnet 非常好的产品与市场契合度

[22:05] **SPEAKER_03:** fit that was good signal to like go go for that and you guys know like the day that you guys launched 3.5 sonnet did you know that you had something really special and this was going to be the turning point for the company or were you as surprised as opening I when they launched chat

> 那就是一个很好的信号，让我们下定决心去做。那你们知道吗，在你们发布 3.5 Sonnet 的那一天，你们是不是就知道自己手里握着某个非常特别的东西、它将成为公司的转折点，还是说你们跟 OpenAI 发布 ChatGPT 时一样感到意外，

[22:19] **SPEAKER_04:** gbt and it just like unexpectedly took off yeah I wish that I wish that we had like more foresight on that but no I think I think it was surprising for us to like how how big of a deal it was and then I think three sevens on it also like surprised us by how much it unlocked like agentic coding I think for for each of these things yeah we move quite fast in rolling them out and so we really um often don't know what the results are going to be there I think it's what

> 而它就那么出乎意料地火了？对，我真希望我们对此有更多的先见之明，但没有，我觉得它究竟有多重要，对我们来说是很意外的。然后我觉得 3.7 Sonnet 也让我们大吃一惊，它把智能体编程（agentic coding）解锁到了那种程度。我觉得对于每一件这样的事情，我们推出它们的速度都相当快，所以我们其实常常并不知道结果会怎样。我觉得正是这个

[22:44] **SPEAKER_00:** made a lot of these coding agent startups work I mean there's a crazy story of replit winning going to 100 million in uh just 10 months right there's cursor of course a story and all built on all these with sonnet I think that all of those

> 让很多这些编程智能体创业公司得以成功。我是说，有一个疯狂的故事是 Replit 大获全胜，仅仅 10 个月就做到了一亿美元，对吧？当然还有 Cursor 的故事，而它们全都是基于 Sonnet 构建的。我觉得所有那些

[23:00] **SPEAKER_04:** things have been surprising to me and then also just like in my working with Claude too like I think I continue to be surprised by like the type of stuff that it can do and I do think with each one there's like more stuff that kind of unlocks but one of my friends was telling me that she had some code that she uh some code source tool that she wanted to modify but she didn't have the source code for it she had the compiled binary and she's like oh can you can you decompile this like can you disassemble the assembly and Claude Claude chewed on it for 10 minutes and like made a C version of it and so then she had the thing that you can modify it didn't say and she's like yeah and like if I spent three days on it I probably could have gotten the hex tables and like wrote in a little code but like it did the whole thing made up variable names for them Etc so I do think that like we keep getting surprised by stuff that model has memorized all the hex tables it can think through try to work through it I think we're going to continue to be surprised by that sort of stuff

> 事对我来说都很出乎意料。而且就在我自己用 Claude 的过程中，我觉得它能做的那些事也一直让我惊讶，我确实觉得每出一代，就有更多东西被解锁。不过我的一个朋友跟我说，她有一段代码，是一个她想要修改的源代码工具，但她没有它的源代码，她只有编译后的二进制文件，她就说，哦，你能不能反编译这个、能不能把汇编反汇编出来？结果 Claude 琢磨了 10 分钟，就做出了一个 C 语言的版本，于是她就有了那个可以修改的东西。她说，是啊，如果我自己花三天，我大概也能弄出那些十六进制表、再写点代码，但它把整件事都做完了，还给它们编好了变量名，等等。所以我确实觉得，我们不断被这些东西惊到——模型把所有的十六进制表都记下来了，它能一步步推演、试着把它做出来。我觉得我们还会继续被这类东西惊到。

[23:53] **SPEAKER_03:** I prefer using anthropic models for coding by like a huge margin it's much larger than what you would predict if you just looked at the benchmark results yeah so there seems to be some x factor that makes people really like these models for coding do you know what it is and is it intentional in some way or it just came out of the black box somehow I think that the benchmarks benchmarks are like

> 我在编程上更偏爱用 Anthropic 的模型，而且优势非常大，比你只看基准测试结果所能预测的要大得多。所以似乎有某种 X 因素让人们在编程上格外喜欢这些模型，你知道那是什么吗？它在某种程度上是有意为之的，还是就这么从黑箱里冒出来的？我觉得基准测试

[24:16] **SPEAKER_04:** easy to game where I think that all the other big Labs I think have teams where they like their whole job with the team is to like make the benchmarks scores good and we don't have such a team and so I think that I think that that is probably the biggest factor you don't teach to the test we don't teach those guys because I I do feel like if you start doing that then like it has weird bad incentives maybe we could like put that team under marketing or something like that and then ignore all the benchmarks but I think that that's

> 很容易被"刷分"。我觉得所有其他大实验室都有一些团队，这些团队的全部工作就是把基准测试分数做好看，而我们没有这样的团队，所以我觉得这大概就是最大的因素。你们不"应试教学"。我们不搞那一套，因为我确实觉得，一旦你开始那么做，就会产生一些奇怪的、糟糕的激励。也许我们可以把那样一个团队放到市场部之类的地方去，然后无视所有的基准测试。但我觉得那

[24:41] **SPEAKER_00:** one reasons why there's some train tests mismatch there so the evaluations are more qualitative but

> 是造成某种"训练与测试不匹配"的原因之一，所以评估更偏定性，但

[24:47] **SPEAKER_03:** internally we have your internal internal benchmarks yeah but we don't we don't publish them and is it the internal benchmarks that the teams are really focused on improving that's right yeah so we have internal

> 在内部你们有自己内部的基准测试。对，但我们不发布它们。那各团队真正专注去改进的，就是这些内部基准测试吗？没错。对，所以我们有内部的

[24:57] **SPEAKER_04:** benchmarks that the team focuses on improving and then we also have a bunch of tasks like I think that accelerating our own Engineers is like a top top priority for us too and so we we do a ton of like dog food in there to make sure that it's helping with our folks too going back to

> 基准测试，团队专注于改进它们。然后我们还有一堆任务，我觉得加速我们自己工程师的效率也是我们最最优先的事项之一，所以我们在里面做了大量的"吃自家狗粮"，以确保它也在帮到我们自己的人。回到

[25:12] **SPEAKER_01:** Golden Gate Claude there's a lot of sort of the interpretability seems like it's a big part of it and then most people would say that you know Claude's personality just feels better yeah and then how do you sort of at once be very quantitative but then also you know build evals

> Golden Gate Claude（金门大桥 Claude），可解释性似乎在其中占了很大一部分，然后大多数人会说，你知道的，Claude 的个性就是让人感觉更好。对，那你们怎么做到既非常量化，同时又能构建关于

[25:29] **SPEAKER_04:** around personality the evals for personality are kind of complicated too for like how do you tell if like Claude has like a good heart or something like that it's like hard to know um but I do think that that's like uh Amanda Askell's team's mandate is I think she describes it as like being like a a good world traveler where like it can like Claude goes and talks with all sorts of people from different backgrounds and like each of the people should come from him come to that being like I I feel good about like this conversation that I've had interp really I think is like a long-term bet right where it's like right now the models aren't that scary but at some point they're going to be more scary and so I think the hope there is to have some ability to know what's actually going

> 个性的评估？针对个性的评估其实也挺复杂的，比如你怎么判断 Claude 是不是有一颗善良的心之类的，这很难知道。但我确实觉得，这是 Amanda Askell 团队的职责所在，我记得她把它形容为像做一个"优秀的环球旅行者"，就是说 Claude 会去和各种不同背景的人交谈，而每一个人都应该在交谈之后觉得"我对刚才这段对话感觉很好"。可解释性我觉得真的是一个长期的赌注，对吧，就是说现在的模型还没那么可怕，但到某个时候它们会变得更可怕，所以我觉得那里的希望在于，具备某种能力去知道底下究竟

[26:07] **SPEAKER_02:** on under the hood when it becomes more intense then more recently Claude code's been a real success can you talk us through like how did that project get started internally and again was it like a did you like know this time it was going to work or was it a surprise Claude code was um an

> 发生了什么，等到情况变得更加激烈的时候。那再往近说，Claude Code 是一个真正的成功案例，你能不能给我们讲讲这个项目在内部是怎么起步的？还是那个问题：这次你们是知道它会成功，还是又一次惊喜？Claude Code 是一个

[26:23] **SPEAKER_04:** example like try to help out our our engineers within anthropic that uh yeah Boris um had like hacked together there's an internal anthropic engineer wanting to build it for themselves for internal for other internal engineers for him and other internal engineers and then um I think yeah I think we definitely didn't know that it would be successful out there and I think I think to some degree like we really had fully just bet on the API before that with the intention being like there's like so many so many startups out there with so many good ideas who are we to like figure out what the right product is to build on top of this stuff everyone out there is going to build better stuff than us and so put all of our effort into just making the best possible API and I think that this surprised me as like okay like we actually were able to make something that like as a product was like better than the other products out on the market for this agentic use I have like a some theory that like part of that came from like a mind shift of seeing Claude as like the user uh for this thing too for like link that like trying to build things for teachers were like our users for for grouper it was like single people in New York mostly I guess um for this I think really the like users are the developers but also I think the users is Claude it's like give Claude the right tools that Claude can actually do that effectively help Claude get the right contexts to work effectively this team was like the most focused on Claude as like a user which I think you guys would understand Claude the I think that that's a place where like startup founders though like can can do that too and I think that that's that's probably a rich vein for people to like make tools that are better for

> 例子，就是想帮到我们 Anthropic 内部的工程师。对，Boris 把它拼凑（hack）了出来，是一位 Anthropic 内部工程师想为自己、为内部、为其他内部工程师做出来的东西。然后，我觉得，对，我们当时肯定不知道它在外部会成功。我觉得在某种程度上，在那之前我们真的完全押注在 API 上，我们的想法是：外面有那么多那么多的创业公司，有那么多好点子，我们凭什么去弄清楚在这些东西之上该做什么样的正确产品呢？外面的每个人都会做出比我们更好的东西，所以我们把全部精力都投入到做出尽可能最好的 API 上。所以我觉得这件事让我很意外，就是"好吧，我们竟然真能做出一个东西，作为产品，在这种智能体用途上比市场上其他产品都好"。我有一套理论，觉得这部分来自于一种心态转变，就是把 Claude 也看作这个东西的"用户"。就像给老师做产品时，老师是我们的用户；对 Grouper 来说，用户大概主要是纽约的单身人士；而对这个来说，我觉得真正的用户是开发者，但同时我也觉得用户是 Claude——就是给 Claude 合适的工具，让 Claude 能真正有效地完成任务，帮 Claude 拿到合适的上下文以便高效工作。这支团队是最专注于把 Claude 当作用户来对待的，我想你们会理解 Claude 的处境。我觉得这也是创业公司创始人同样可以做到的地方，我觉得这大概是一条富矿，人们可以据此做出对

[28:02] **SPEAKER_01:** models as users that's the perfect anthropomorphization of like the LLM itself like the agent is one of the stakeholders one of the users that you would go after and try to like

> 作为用户的模型更友好的工具。这是对大语言模型本身完美的拟人化，就是说这个智能体是利益相关方之一、是你会去争取并努力去

[28:13] **SPEAKER_00:** empower yeah yeah totally which actually makes a lot of sense why you guys actually got mcp to work to do tool calling because a bunch of other labs had tried to do tool calling and they didn't work to do something and the standard that stuck that that really took off was yours yeah I think that

> 赋能的用户之一。对对，完全正确。这其实也很好地解释了为什么你们真的把 MCP 做成了、让工具调用能用起来。因为好多其他实验室都试过做工具调用，可它们并没有真正做成什么，而最终立住、真正火起来的标准是你们的。对，我觉得

[28:30] **SPEAKER_02:** that seems like a similar one too where it's like it's like a model model focused going back to cool code so like success is really exciting it's also scary for like cursor and other companies that have built on top of the API like what's your advice to founders building products like how should they think about building on the API but also worrying about like anthropic or in the

> 那似乎也是类似的一件事，就是它同样是以模型为中心的。回到 Claude Code，它的成功真的很令人振奋，但对 Cursor 以及其他基于 API 构建的公司来说，也挺可怕的。那你对那些在做产品的创始人有什么建议？他们该怎么看待在 API 之上构建、同时又要担心 Anthropic 或者其他

[28:49] **SPEAKER_04:** labs building something better than they can build I think I was kind of surprised that Claude code didn't like we we did build a thing that was like uh like the best in the market there too it's not super clear to me what the big advantage was for us for Claude code besides more empathy for Claude

> 实验室做出比他们更好的东西？我觉得我其实有点意外，Claude Code……我们确实做出了一个在那个市场里也算是最好的东西，可对我来说，除了对 Claude 有更多的同理心之外，我们在 Claude Code 上到底有什么大的优势并不十分清楚。

[29:04] **SPEAKER_02:** I think that's actually really interesting insight like it seems like the thing that yeah you were building for a specific user that you knew really well that other people wouldn't have thought to build for versus like you had some like intrinsic technology advantage yeah like I think a startup

> 我觉得这其实是一个非常有意思的洞见，看起来关键在于——对，你们是在为一个你们非常了解、而别人不会想到要去为其构建的特定用户做产品，而不是说你们有某种内在的技术优势。对，我觉得一家创业公司

[29:18] **SPEAKER_04:** could could have done that same thing too right yeah I think we're the most like developer focused I think we're the most like API focused lab too so I think we want to make sure that we have the best platform for people to build stuff on because this thing is growing so incredibly quickly like we're not going to be the fastest at figuring out all the ways that we need to empower Claude to do the work that connects Claude to the entire human business that's like human human world is all designed for humans but like we need to get the models to be able to be productive members of

> 本来也完全可以做同样的事，对吧。是的，我觉得我们是最以开发者为中心的，我觉得我们也是最以 API 为中心的实验室，所以我们想确保我们拥有让人们在其之上构建东西的最好平台。因为这个东西增长得实在太快了，我们不可能是弄清楚所有那些方式的最快的人——所有那些我们需要去赋能 Claude、让 Claude 把工作做好、把 Claude 接入整个人类商业世界的方式。人类世界完全是为人类设计的，可我们需要让模型能够成为

[29:48] **SPEAKER_02:** the economy are there like ideas or areas you would love to see developers building in or like areas you don't you you think are like underappreciated right now yeah Claude code is

> 经济中有生产力的一员。那有没有一些你特别希望看到开发者去做的点子或领域，或者你觉得现在被低估了的领域？对，Claude Code 是

[30:00] **SPEAKER_04:** like how do you get Claude to be a useful pair programmer kind of um or like junior engineer you've got like a sweet level two or three or something like that that you can work with or like very spiky because also it can do the like weird disassembly stuff that like a super high level suite would struggle with less good at knowing what type of work to do needs kind of a lot of hand holding needs a lot of context from it that's like one very particular subset of work that can be done if you look at like all the stuff that happens in businesses besides that it's like a very tiny fraction of like all the work that's done in businesses that like a smart person who knows how to code and like use lots of tools but doesn't have that much context yet uh would want to do so I think I think finding ways to coach Claude or uh approach whatever model to like do useful tasks for businesses seems like there's just like a huge

> 关于怎么让 Claude 成为一个有用的结对编程伙伴，或者说一个初级工程师——你手里有个 L2 或 L3 级别、可以合作的对象，或者说它"很尖峰"，因为它也能做那种诡异的反汇编工作，而那是一个超高级别的员工都会觉得吃力的；但它不太擅长判断该做什么类型的工作，需要相当多的手把手引导，需要你给它大量的上下文。这只是可以被完成的工作里非常特定的一小部分。如果你去看企业里发生的所有事情，除此之外，它其实只是企业里所有工作中极其微小的一部分——那种一个懂编程、会用很多工具、但还没有太多上下文的聪明人会想做的工作。所以我觉得，找到办法去"教练"Claude、或者去引导任何模型为企业做有用的任务，看起来那里有一片极其巨大的

[30:59] **SPEAKER_03:** huge space there so Tom a big part of your job is like owning all the compute infrastructure that makes anthropic work can you talk about like what what is the compute infrastructure behind this

> 广阔空间。那 Tom，你工作中很大一部分是负责让 Anthropic 得以运转的全部算力基础设施，你能不能讲讲这个庞然大物背后的算力基础设施

[31:10] **SPEAKER_04:** giant thing now one thing that's interesting to look at is just that humanity is on track for like the largest infrastructure build out of all time now this is gonna be larger than the Apollo project larger than the Manhattan project it'll be bigger than both of them this year if it keeps on the current trajectory which is like roughly 3x per year increase in spending on AGI compute which is just bonkers yeah like 3x per year is wild I think it's going to keep up on the 3x per year trajectory it's already locked in for that for for next year and then it's a little bit open for for 2027 I mean anecdotally internal to YC uh we can't get

> 究竟是什么样的？有一件很有意思的事值得看看，那就是人类正走在历史上规模最大的一次基础设施建设的道路上。这将比阿波罗计划还大，比曼哈顿计划还大，如果按当前的轨迹继续下去，今年它就会比这两者都大——当前的轨迹大约是每年在 AGI 算力上的支出增长三倍，这简直疯狂。对，每年三倍太夸张了。我觉得它会沿着每年三倍的轨迹继续下去，明年的已经锁定了，2027 年则还有点不确定。我是说，就 YC 内部的轶事而言，我们根本弄不到

[31:50] **SPEAKER_01:** enough you know credits across all of the top Frontier models yeah we're just I mean everyone's bottleneck literally every you know it's like give me more

> 足够的、你知道的、那些顶尖前沿模型的额度。对，我们……我是说，每个人的瓶颈，真的每个人，都是"给我更多

[32:02] **SPEAKER_04:** intelligence I can't have enough yeah and I know you guys have been looking at more hardware startups also for like more accelerators I think that we will see more accelerators coming online to 2027. that's a good a good space also like data center tech I think is a big one where are

> 智能，我永远嫌不够"。对，我知道你们也一直在关注更多硬件创业公司，去找更多的加速器。我觉得到 2027 年我们会看到更多加速器上线。那是个不错的领域，数据中心技术我觉得也是一个很大的方向。你们现在的

[32:16] **SPEAKER_03:** the bottlenecks for you guys now is it like getting enough electricity getting enough gpus getting construction permits

> 瓶颈在哪里？是搞到足够的电力、足够的 GPU，还是拿到施工许可？

[32:23] **SPEAKER_01:** power people are using jet engines to get power that's nuts overall for the build out I think

> 电力。有人在用喷气发动机来发电，太疯狂了。就整体的建设而言，我觉得

[32:29] **SPEAKER_04:** power is going to be the biggest bottleneck especially power in the U.S like we want to build in the U.S that's one of our biggest policy goals is to like get the U.S to like build more data centers permit more data centers make it easier to build is the answer renewables or is

> 电力将会是最大的瓶颈，尤其是美国的电力。我们想在美国建设，这是我们最大的政策目标之一，就是推动美国建更多数据中心、给更多数据中心发许可、让建设变得更容易。那答案是可再生能源，还是

[32:44] **SPEAKER_03:** it uh nuclear I I definitely I feel like yes yes all of those things I wish I wish the nuclear was really alive that uses not just one kind of GPU but the GPU is from three different manufacturers can you talk about that and how how that strategy has played out yeah yeah so we use um gpus tpus

> 核能？我，我肯定觉得，是的、是的，所有这些都要，我真希望核能真的能活起来。你们用的不只是一种 GPU，而是来自三家不同制造商的芯片，你能讲讲这个、以及这个策略后来效果如何吗？对对，所以我们用 GPU、TPU

[33:05] **SPEAKER_04:** and tranium downside of doing that is that we split our performance engineering teams across all of those platforms which is a ton of extra work the positive thing is it gives us the flexibility to both one like soak up that extra capacity because there there just is more of those all together than just one. And then two is we can use the right chips for the right jobs, where some chips will be better for inference, some chips will be better for training, and we can match the right chips to the right jobs. So yeah, I think that's kind of the trade off there.

> 和 Trainium。这样做的坏处是，我们的性能工程团队被分散到所有这些平台上，这是大量的额外工作。好处是它给了我们灵活性：一是我们能吸收那些额外的产能，因为把它们全加起来，总量就是比只用一种要多；二是我们可以为合适的任务用合适的芯片——有些芯片更适合推理，有些更适合训练，我们可以把合适的芯片匹配给合适的任务。所以，对，我觉得那里的权衡大概就是这样。

[33:36] **SPEAKER_00:** I guess one cool thing is just connecting the dots through your career and how all of this compounded, because you were the one engineer building that change of the architecture from TPUs to GPUs back at OpenAI that got GPT-3 to actually scale. And now you're in charge of that at a much, much bigger scale years later. I don't know if that kind of connected dots for you.

> 我觉得一件很酷的事，是把你整个职业生涯的点连起来、看看这一切是怎么复利叠加的。因为当年在 OpenAI，你就是那个把架构从 TPU 换到 GPU、从而让 GPT-3 真正得以扩展的工程师。而如今许多年后，你在规模大得多得多的层面上负责同样的事。我不知道这对你来说是不是把点都连起来了。

[33:59] **SPEAKER_04:** The big move from TPUs to GPUs at OpenAI I think was partly driven just that PyTorch was a better software stack on top of them than TensorFlow on top of TPUs. And I think that that then unlocked fast iteration, where if you have a good reliable software stack, then you can... Experiment quickly, just build a whole system that works. I think that that's the thing that we really strive for now at Anthropic too, is a challenge of having many more platforms is that it's harder to write all the good software. I think building the muscle of knowing how to build that software well so that all of the people who build on top of that low level can have a great experience with it is the most important thing there.

> 在 OpenAI 从 TPU 大规模转向 GPU，我觉得部分原因就是 PyTorch 作为跑在它们之上的软件栈，比跑在 TPU 之上的 TensorFlow 更好。我觉得那随后解锁了快速迭代——如果你有一个可靠好用的软件栈，你就能快速做实验，直接搭建出一个完整、能用的系统。我觉得这也正是我们现在在 Anthropic 真正努力追求的东西。拥有多得多的平台带来的一个挑战是，要把所有那些好软件都写出来更难了。我觉得那里最重要的事，是锻炼出一种"知道如何把那套软件写好"的肌肉，好让所有在那个底层之上构建东西的人都能有很好的使用体验。

[34:38] **SPEAKER_00:** Do you have advice for a younger Tom version of yourself, who now you've seen and went through this crazy journey? If someone was you back in the 20s living today and they wanted to arrive and join the AI revolution, what would you say to them?

> 你有没有什么建议要给年轻版本的自己——现在你已经见识并走过了这段疯狂的旅程？如果有个人就是二十几岁时的你、活在今天，想要投身并加入这场 AI 革命，你会对他们说什么？

[34:54] **SPEAKER_02:** Very specifically, something we hear from a lot of college students at the moment is they don't know if they should stay in college, are there going to be jobs for them? How is the world going to change and what should they do?

> 说得非常具体一点，我们眼下从很多大学生那里听到的一个困惑是：他们不知道自己是否该继续读大学，将来还会有他们的工作吗？世界将会怎样改变，他们又该怎么做？

[35:07] **SPEAKER_04:** Taking more risks I think is wise, and then also trying to work on stuff where your friends would be really excited and impressed. Yeah. If you did it, or a more idealized version of yourself would be really proud of yourself if you succeeded at it, I think is probably the thing that I would try to tell a younger version of myself.

> 我觉得多冒一些险是明智的，然后也要努力去做那种——如果你做成了，你的朋友们会真心为之激动和佩服的事。是的。或者说，如果你在那件事上成功了，一个更理想化版本的你会真正为自己感到骄傲。我觉得这大概就是我会试着告诉年轻版本自己的话。

[35:26] **SPEAKER_01:** More intrinsic, less extrinsic. Don't chase these other credentials and getting the degree or working at Fang. Those are just irrelevant as of today. Yeah. Exactly.

> 更多内在驱动，少一点外在驱动。别去追逐那些别的头衔、去拿学位或者进大厂（FAANG）。那些东西到今天已经无关紧要了。对，正是如此。

[35:39] **SPEAKER_01:** That's all we have time for today. We'll see you guys next time.

> 今天我们的时间就到这里了。我们下次再见。
