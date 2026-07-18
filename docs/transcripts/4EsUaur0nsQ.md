# 全文转录 · 机器人的 GPT 时刻已到:一份垂直机器人创业 playbook

> ▶ [YouTube](https://www.youtube.com/watch?v=4EsUaur0nsQ) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/4EsUaur0nsQ.md) &nbsp;·&nbsp; The GPT Moment for Robotics Is Here

> 中英对照 · 每段英文原文下附中文翻译

`[00:00]` **SPEAKER_00:** The equation, I think, for starting a robotic business has changed and will continue to change at an accelerating pace because the upfront cost is not that high anymore.

> 我认为,创办一家机器人公司的公式已经改变,而且会以加速的态势持续改变,因为如今的前期成本已经没有那么高了。

`[00:12]` **SPEAKER_01:** Everyone's sort of spending a lot of time in the digital world and it feels like now is the time to start thinking about the world of atoms.

> 大家现在都花了很多时间在数字世界里,而感觉现在正是开始思考"原子世界"的时候了。

`[00:19]` **SPEAKER_04:** You literally just gave people the playbook for how to build a vertical robotics company.

> 你刚刚简直是把如何打造一家垂直机器人公司的操作手册直接交给了大家。

`[00:24]` **SPEAKER_00:** This has really been our mission from the start, is to create that Cambrian explosion.

> 这从一开始就是我们的使命——去催生那样一场"寒武纪大爆发"。

`[00:30]` **SPEAKER_04:** It still blows my mind. I didn't know if this would exist even in my entire lifetime.

> 这依然让我震撼不已。我原本都不确定这种东西在我有生之年是否会出现。

`[00:41]` **SPEAKER_01:** Welcome back to another episode of The Light Cone. Today, we have a very special guest, Quan Vuong. He's one of the co-founders of Physical Intelligence, which we think might be the robotics AI lab that brings about the GPT-1 moment for all of robotics. Quan, thank you for joining us.

> 欢迎回到《The Light Cone》的又一期节目。今天我们请到了一位非常特别的嘉宾,Quan Vuong。他是 Physical Intelligence 的联合创始人之一,我们认为这家公司可能会成为为整个机器人领域带来"GPT-1 时刻"的机器人 AI 实验室。Quan,谢谢你来参加节目。

`[01:01]` **SPEAKER_00:** Pleasure to be here. Has been a long-time admirer of YC. And our mission, is to build a model that can control any robot to do any task that it's physically capable of and to do so as such a high level of performance that's going to be useful to people in all walks of life. And so, GPT-1 for robotics, what is it? Is the chat GPT moment for robotics real?

> 很高兴来到这里,我一直以来都很仰慕 YC。我们的使命,是打造一个模型,能够控制任何机器人去完成它在物理上能够胜任的任何任务,并且要以极高的性能水平去完成,使之对各行各业的人都有用。那么,机器人领域的"GPT-1"是什么?机器人的 ChatGPT 时刻真的会到来吗?

`[01:22]` **SPEAKER_00:** Our perspective here is that we want to build a model that's really intelligent. We want to build a platform that allows us to externalize that intelligence to the rest of the world and allow them to use it to build very easily, and we want to build a system that's very, very, very, very, very, very interesting application in all sorts of vertical and robotics. And we think that it's going to be more like a peeling an onion's analogy, where you start from a really strong base model that have all sorts of common sense knowledge and already works to some extent on your robot. You have then a mixed autonomy system, very similar, for example, to a autonomous driving car today. And then you actually deploy that system to do a real job.

> 我们的看法是,我们要打造一个真正智能的模型。我们要打造一个平台,让我们能把这种智能外化给世界上的其他人,让他们能非常轻松地基于它去构建。我们要打造一个系统,能在各种垂直领域和机器人上催生非常非常有趣的应用。我们认为这更像是"剥洋葱"的比喻:你先从一个非常强大的基座模型出发,它已经具备各种常识性知识,并且在你的机器人上已经在一定程度上能用了;然后你有一个"混合自主"系统,很类似于今天的自动驾驶汽车;接着你真正把这个系统部署出去,让它去做一份真正的工作。

`[02:06]` **SPEAKER_00:** That's okay. And then over time, by actually exposing the system to the complexity and the edge case of the real world, that system get incrementally, even just slightly better over time every day. And, you know, one day you wake up and you suddenly have a system that is just fully autonomous and just provide tremendous value.

> 这没关系。随着时间推移,通过真正把系统暴露在现实世界的复杂性和各种边缘情况之下,这个系统会一点一点地、哪怕每天只是稍微地变好。然后有一天你醒来,突然发现你手里有了一个完全自主、能带来巨大价值的系统。

`[02:24]` **SPEAKER_02:** Might be helpful to give the audience a bit of a mini history lesson on why robotics is so hard. And there's been a lot of breakthroughs in the last two years. And I mean, just to simplify that, the robotics problem is three pillars. Semantics, which I think we got a lot of at Luxon with language models that somehow we ported into robotics. Then you have the planning.

> 或许可以给观众上一堂小小的历史课,讲讲为什么机器人这么难。过去两年里出现了很多突破。简化来说,机器人问题有三大支柱:一是语义,我认为我们借助语言模型在这方面收获颇丰,并想办法把它移植到了机器人领域;接着是规划。

`[02:48]` **SPEAKER_02:** And then the last thing is control, which needs to be done in real time and interact with an environment that changes. Walk us through the seminal papers that a lot of the team of Pi Robotics published that gave you the inkling that the GPT-1 moment is near. And that started in 2024.

> 最后一件事是控制,它必须实时完成,并且要与一个不断变化的环境交互。请带我们梳理一下,Pi Robotics 团队里很多人发表的那些开创性论文——正是它们让你隐约感到 GPT-1 时刻已近在眼前。而这一切始于 2024 年。

`[03:05]` **SPEAKER_00:** Yeah. The dream to build general purpose robots has been a long time dream, I think, in humanity. We're not the first to say that our mission is to build a model that can work on any robot. And we're really fortunate to be in this moment in time in history where we feel that it's possible to kind of walk back a little bit. A few years before, there was, I think, the first is Seikan, which to me was the first demonstration of language model and how we can bring all of the common sense knowledge in language model into robotics.

> 是的。我认为,打造通用机器人一直是人类长久以来的梦想。说"我们的使命是打造一个能在任何机器人上工作的模型",我们并不是第一个。我们非常幸运,能身处历史上这样一个时刻,让我们觉得这是有可能实现的。往回倒几年,我想最早的是 SayCan,对我来说,它是首次展示了语言模型、以及我们如何能把语言模型中所有的常识性知识带入机器人领域。

`[03:40]` **SPEAKER_00:** And therefore, that significantly kind of reduces the need to collect robot-specific data. So, for example, if you have a task of, oh, I want to go to the YC office to record a podcast, you know, what a step I need to take, you can ask a language model, you know, just show me the steps and show me the plan. And that worked incredibly well. And then the way kind of language model infiltrate, if you will, in robotics is to start at the planning level, at the semantic level. And then, but there's still the control problem, you know, at the end of the day, you still need a mechanism to convert the plan into low-level action that can actually actuate the robot.

> 因此,这大大减少了收集机器人专用数据的需求。比如说,如果你有一个任务:"哦,我想去 YC 办公室录播客,我需要采取哪些步骤",你可以问语言模型:"给我列出步骤,给我一个计划。"这一招效果好得惊人。语言模型渗透进机器人领域的方式,可以说是从规划层面、从语义层面开始的。但接下来仍然有控制问题——归根结底,你仍然需要一种机制,把计划转化为真正能驱动机器人的底层动作。

`[04:14]` **SPEAKER_00:** And that bring us to POM-E, and that bring us to RT-2, which stands for Robotic Transformer 2. And what these two work really show is that if you start from a vision language model that is really powerful, and you kind of use robotic data to adapt this model to speak robot language, if you will, then you see a lot of transfer from the kind of knowledge that exists in the language model, in the vision language model, down to the low-level action. Like one of my favorite example when we did the RT-2 project was you can have picture of celebrity on the table. You have a picture of Taylor Swift. You have a picture of the Queen of England.

> 这就把我们带到了 PaLM-E,以及 RT-2——即 Robotic Transformer 2(机器人 Transformer 2)。这两项工作真正表明的是:如果你从一个非常强大的视觉语言模型出发,再用机器人数据去让这个模型学会"说机器人的语言",你就会看到大量知识从语言模型、从视觉语言模型中迁移下来,直达底层动作。我做 RT-2 项目时最喜欢的一个例子就是:桌子上可以放名人的照片,一张是 Taylor Swift 的照片,一张是英国女王的照片。

`[04:56]` **SPEAKER_00:** And you can ask the robot, you know, pick up the Coke can and move it to Taylor Swift, even though the concept of Taylor Swift is just doesn't exist in the robot data at all in that work. You can do other examples such as kind of spatial reasoning that doesn't exist in the robot data at all. Like, for example, move the dinosaurs next to the red car. And these are all just completely unseen object in robot data. And so that was RT-2, and that was POM-E.

> 你可以让机器人"拿起可乐罐,把它移到 Taylor Swift 那边",尽管在那项工作里,机器人数据中根本就不存在"Taylor Swift"这个概念。你还可以做其他例子,比如某种在机器人数据中根本不存在的空间推理。例如,"把恐龙移到红色汽车旁边"。而这些都是机器人数据里完全没见过的物体。这就是 RT-2,也是 PaLM-E。

`[05:25]` **SPEAKER_00:** Now, RT-2 and POM-E are single embodiment exercise.

> 那么,RT-2 和 PaLM-E 都是"单一形态(single embodiment)"的实践。

`[05:30]` **SPEAKER_02:** Just for the audience, single embodiment meaning it worked for a very specific robot.

> 为观众解释一下,"单一形态"意思是它只对某一种非常特定的机器人有效。

`[05:34]` **SPEAKER_00:** It worked for a very specific robot. In robotics, you can ask the question, how do you scale? Especially how do you scale data collections? And one of the insights that we had back then was, you know, maybe the data from one robot is not that different from another robot's anyway. If you have enough robots in your training data, maybe what the model learned isn't to control one specific robot.

> 它只对某一种非常特定的机器人有效。在机器人领域,你可以提出这样的问题:如何规模化?尤其是如何规模化地收集数据?我们当时的一个洞见是:也许一个机器人的数据和另一个机器人的数据本来就没那么不同。如果你的训练数据里有足够多的机器人,也许模型学到的并不是去控制某一台特定的机器人。

`[05:56]` **SPEAKER_00:** What the model learned is something that's more abstract, which is how do I kind of learn a general notion of what it means to control any particular robotic platform? And therefore, I will be better at controlling any particular platform. And that brings us to what we call open cross embodiment and robotic transformer X.

> 模型学到的是某种更抽象的东西,也就是:我如何习得一个关于"控制任意某个机器人平台意味着什么"的通用概念?因而,我会更擅长控制任意某个特定平台。这就把我们带到了我们所说的 Open Cross-Embodiment(开放跨形态)和 Robotic Transformer X(机器人 Transformer X)。

`[06:16]` **SPEAKER_02:** That was a big paper because it was the first that showed potential scaling laws that apply to robotics because now you could start training all these models across multiple kinds of hardware, not just one, which has never been done in robotics. Ever before. Because from all the research labs, they would all train with a very specific set of sensor actuators and motors, and it was all very finicky with that particular hardware, right?

> 那是一篇重量级论文,因为它第一次展示了可能适用于机器人的缩放定律(scaling laws)——因为现在你可以开始跨多种硬件、而不只是一种硬件来训练所有这些模型,这在机器人领域此前从未有人做到过。因为过去所有研究实验室都只用一套非常特定的传感器、执行器和电机来训练,而且和那一特定硬件配合起来都非常挑剔、难搞,对吧?

`[06:41]` **SPEAKER_00:** Yeah. One of the really interesting results from open cross embodiment, and let me provide the context here, is that you can take, let's say, 10 different robot platforms, collect data from them, train a policy, and really optimize the policy to work well on that platform. So let's say, you know, you have that, you have 10 different platforms, 10 different policies, and now if you simply take the data and absorb it into a model that is high capacity enough to really absorb that data and you can compare, you have these generalists, right, that learn to control how to test the 10 different robots. You can compare it to the specialist that has been optimized to work well on a particular embodiment. How does it compare?

> 是的。Open Cross-Embodiment 有一个非常有意思的结果,让我先交代一下背景:你可以拿,比如说,10 个不同的机器人平台,从它们身上收集数据,训练一个策略,并把这个策略真正优化到在那个平台上运行良好。假设你有了这个,你有 10 个不同平台、10 个不同策略;现在如果你只是把数据拿来,吸收进一个容量足够大、能真正吃下这些数据的模型里,你就可以做对比——你有了这些"通才",对吧,它们学会了控制这 10 种不同的机器人。你可以把它和那些被优化到只在某一特定形态上表现良好的"专才"作对比。结果如何呢?

`[07:20]` **SPEAKER_00:** And the interesting result from open X is it was 50% better. Wow. And that was really surprising. Wow. And in robotic, it's hard enough to get your model to work on one particular robot platform.

> Open X 有意思的结果是:它好了 50%。哇。这真的很出人意料。哇。而在机器人领域,光是让你的模型在某一个特定机器人平台上跑起来,就已经够难的了。

`[07:34]` **SPEAKER_00:** And one of the reasons why I say that we're really fortunate to be in this moment in time in robotic is because open X was really only possible because of the support that we received from the robotic community. It was a huge collaboration across the robotic community. And the reason why that's really important is there is this joke in robotic grad school that, you know, if you want to add two years to your PhD, just work on a new robot platform. You know, by that logic, if you want to have 10 robot platform, that's 20 years.

> 我之所以说我们非常幸运能身处机器人领域的这个时刻,原因之一就是:Open X 之所以能实现,完全得益于我们从机器人社区获得的支持。这是一次横跨整个机器人社区的大规模协作。它之所以如此重要,是因为机器人研究生圈子里有个笑话:如果你想给自己的博士生涯再加两年,那就去搞一个新的机器人平台。照这个逻辑,你要想搞 10 个机器人平台,那就是 20 年。

`[08:06]` **SPEAKER_01:** Why is that? It takes like a year or two to just get the platform up and running to even collect the data.

> 为什么会这样?难道光是把一个平台搭起来、跑起来,乃至开始收集数据,就得花上一两年?

`[08:12]` **SPEAKER_02:** Yeah. Is it fair to say that the data set that was created from embodiment X is similar to the scale of an impact that ImageNet did for vision because it was huge and it was the first large data set across multiple hardware, huge collaboration,

> 是的。可以这么说吗:Embodiment X 所创建的数据集,其影响的量级堪比 ImageNet 之于视觉领域?因为它规模巨大,是第一个横跨多种硬件的大型数据集,而且是一次大规模协作。

`[08:28]` **SPEAKER_00:** I still think that ImageNet was more impactful in the vision community. And the reason for that is a few. The first is that ImageNet also allowed for reproducible evaluation. Right. You know, open X as an effort was more about making data available for kind of people to use.

> 我还是认为 ImageNet 对视觉社区的影响更大。原因有几点。第一,ImageNet 还使可复现的评测成为可能。对吧。而 Open X 这项工作更多的是把数据开放出来,供大家使用。

`[08:48]` **SPEAKER_00:** And evaluation is a really difficult problems in robotic that open X did not solve. And the second is I think open X is a drop in the bucket at this point in the robotic community. If you measure in the kind of the scale and the volume and the diversity of data that the community is collecting, I think open X at this point is a drop in the bucket.

> 而评测在机器人领域是一个非常棘手的问题,Open X 并没有解决它。第二点是,我认为在机器人社区,Open X 到现在只能算九牛一毛。如果你以社区正在收集的数据的规模、体量和多样性来衡量,我觉得 Open X 到现在只是沧海一粟。

`[09:11]` **SPEAKER_01:** I mean, I guess we started talking about sort of GP1, but even GP1, that was sort of this moment where you can prove, Alec Radford figured out that there was a neuron based on a very specific input and output. And then that allowed the scaling laws to sort of take hold. The biggest problem in robotics I've heard is basically actually exactly what we've been talking about. It's like it's the data problem. You know, language you could bootstrap off of like, you know, the sum total of what you could get off the internet, which is actually quite a lot.

> 我是说,我们刚才开始聊到了类似 GPT-1 的东西,但即便是 GPT-1,那也是这样一个时刻:你能证明——Alec Radford 发现,基于某个非常特定的输入和输出,存在这样一个神经元。然后这就让缩放定律得以成立、站稳脚跟。我听说机器人领域最大的问题,其实基本上正是我们一直在谈的这个——就是数据问题。你知道,语言你可以借助互联网上能获取到的全部内容来启动,而那其实相当庞大。

`[09:42]` **SPEAKER_01:** Can you give us like a sense for like scale? Is it like petabytes? Like, you know, what do you think is necessary as an input to, you know, the true GPT-1 of robotics?

> 你能给我们一点关于规模的概念吗?是 PB(拍字节)级别吗?你觉得,要作为真正的"机器人 GPT-1"的输入,需要多少数据?

`[09:55]` **SPEAKER_00:** Yeah. The data scarcity problem in robotics, there's a few ways to look at it. The first way is that it's really two problems in disguise. There is the generation, data generation problem, and there's data capture problem. And the difference is that the data capture is that there might already be lots of robotic data that is being generated, but there's just never been really an incentive to capture it, to make it easy for digestions in training.

> 是的。机器人领域的数据稀缺问题,可以从几个角度看。第一个角度是:它其实是伪装成一个问题的两个问题。一个是"生成"——数据生成问题;另一个是数据捕获问题。区别在于,数据捕获是指:也许已经有大量机器人数据正在被生成,只是从来没有真正的动机去把它捕获下来、整理成便于训练时消化的形式。

`[10:18]` **SPEAKER_00:** And that's one of the goals that open X was trying to solve, which is if you have robotic data, it's a really good idea to capture it and make it possible to train on. The second way to look at it is that robotic is very different from language model. There is not a internet of robotic data that you can use. And so you see these kind of very operationally heavy effort to collect data. And there's the question of, is it going to scale?

> 这正是 Open X 想要解决的目标之一:如果你有机器人数据,那么把它捕获下来、使之可用于训练,是个非常好的主意。第二个角度是:机器人和语言模型非常不同。并不存在一个"机器人数据的互联网"供你使用。所以你会看到这类在运营上非常繁重的数据收集工作。于是就有了这样一个问题:它能规模化吗?

`[10:44]` **SPEAKER_00:** Well, the way that I look at it is, let's take the US GDP, 24 trillion US dollars. Let's say if we actually solve robotics, a model that can control any robot to scale, to do any task, napkin math, maybe contribute 10% to US GDP. Well, that's already a massive number. And I think that promise is one of the reasons that warrants the investment into data collections in robotics. And the third way to look at it is we're very focused on cross embodiment.

> 我的看法是这样:拿美国 GDP 来说,24 万亿美元。假设我们真的把机器人问题解决了——一个能规模化地控制任何机器人、去完成任何任务的模型——粗略估算,也许能为美国 GDP 贡献 10%。那已经是一个庞大的数字了。我认为,正是这个前景,构成了值得对机器人领域的数据收集进行投资的理由之一。第三个角度是:我们非常专注于跨形态。

`[11:17]` **SPEAKER_00:** And cross embodiment, there is the data collection aspect of as well, which is to really make sure that your model and your organizations and infrastructure are set up to consume data from many different sources of robots. And that actually allows you to scale easier. For example, if I were to contrast our approach compared to, let's say a company that have a particular hardware platform that they optimize for and they scale, it's not an approach that have really allowed people to scale because it's just much harder to figure out how do you manufacture like a thousand unit of something for now compared to making sure that you yourself are ready to absorb data from like a thousand different types of robot that are already in there in the community.

> 而跨形态也有其数据收集的一面,即真正确保你的模型、你的组织和基础设施都被搭建得能够消化来自许多不同来源机器人的数据。这实际上让你更容易规模化。举例来说,如果把我们的做法和一家专注优化并规模化某一特定硬件平台的公司相比——那种做法其实并没有真正让人们得以规模化,因为搞清楚"如何现在就制造出比如一千台某种东西",要比"确保你自己已经准备好吸收来自社区里已有的一千种不同类型机器人的数据"难得多。

`[12:03]` **SPEAKER_01:** I mean, it's a crazy problem, isn't it? I mean, the hardware itself, even within the same design of embodiment, if there's a hardware run that goes awry or like one of the servos is slightly different, like you see it in the data, right? And then how do you control for that?

> 我是说,这是个疯狂的问题,不是吗?我是说,硬件本身,即便在同一种形态设计之内,如果某一批硬件出了岔子,或者某个舵机稍微不一样,你在数据里就能看出来,对吧?那你要怎么控制这种变量?

`[12:18]` **SPEAKER_00:** Yeah, so I think we were doing kind of like an inventory of robot in the cloud. I mean, we were in the company, we were so shocked to find out there are no robot, no two robot platform that are the same. And if you ask people in the ROI community, sometimes there's debate about multi robot versus single robot. And the argument is that, you know, single robot is simpler to scale. And actually that's not how it plays out in practice.

> 是的,我想我们当时是在做类似"云端机器人清点"的事情。我是说,在公司里,我们震惊地发现:没有两台机器人平台是完全一样的。如果你去问机器人社区里的人,有时会有关于"多机器人 vs 单机器人"的争论。一种论点是:单机器人更容易规模化。但实际上在实践中根本不是这样。

`[12:40]` **SPEAKER_00:** Like how it plays out in practice is even if you have a single robot that you're optimizing for, over time that platform is going to drift. You know, maybe you want to make hardware change or you have software change. You end up in a situation where it's much harder for you to reuse old data because, you know, in machine learning, if you want to generalize from a distribution, you would like many sample from that distribution. And if you just have one robot platform that have a major change every three months, maybe you have a few data points from that distribution. Whereas if you start from the hypothesis that if you have many robot platform in your fleet, your model is going to learn something more abstract, which is how do I control a robot, not any particular robot, then the model will be able to ingest data from, you know, a slightly different robot better.

> 实际情况是这样的:即便你只针对一台机器人做优化,随着时间推移,那个平台也会"漂移"。你也许想做硬件改动,或者有软件改动。你最终会陷入这样一种境地:你很难复用旧数据。因为在机器学习里,如果你想从某个分布中泛化,你会希望从那个分布里有很多样本。而如果你只有一个机器人平台、每三个月来一次大改动,那你从那个分布里也许只有寥寥几个数据点。反过来,如果你从这样一个假设出发:如果你的机队里有许多机器人平台,那么你的模型会学到某种更抽象的东西——即"我如何控制一台机器人",而不是控制某一台特定的机器人——那么这个模型就能更好地吸收来自稍有不同的机器人的数据。

`[13:26]` **SPEAKER_00:** And actually, we're starting to see emergent property in this kind of robot large foundation model. That's good news. We're doing. Where you start to see like interesting transfer between different data sources. For example, today it's possible to perform tasks zero-shot.

> 而实际上,我们已经开始在这类机器人大型基座模型中看到涌现特性了。这是好消息。我们正在做这件事。你开始看到不同数据源之间有趣的迁移。比如,如今可以做到零样本(zero-shot)地执行任务。

`[13:44]` **SPEAKER_00:** Zero-shot meaning you don't collect any data. And these are the tasks that last year might have required like hundreds and hundreds of hours.

> 零样本的意思是,你根本不收集任何数据。而这些任务,放在去年可能需要成百上千个小时(的数据)才能做到。

`[13:50]` **SPEAKER_01:** What are some examples? Yeah. Do we have any videos we can see that like show it?

> 能举些例子吗?是的。我们有没有可以看的视频来展示一下?

`[13:54]` **SPEAKER_00:** So, you know, I get some flack when I come back because this is not published result. Hopefully this will come out soon. So, you know, I want to reserve the excitement for that. Fair enough. And I'm kind of like building up the excitement a little bit.

> 你知道,我回去后会挨点批评,因为这还不是已发表的结果。希望它很快就会公布。所以,我想把这份激动留到那时候。有道理。我这也算是在稍微给大家吊吊胃口。

`[14:06]` **SPEAKER_00:** So hopefully this will come out soon. All right. These are not simple tasks. These are like actually difficult tasks that just last year required like hundreds of hours of data collections.

> 所以希望它很快就会公布。好的。这些可不是简单任务。这些是实实在在的高难度任务,而就在去年,它们还需要几百个小时的数据收集才能完成。

`[14:16]` **SPEAKER_01:** You hear on Lightcone first that there's some emergent property that are going to come out of Pi. Can you give us a sense of like the flavor of the tasks?

> 你们在《Lightcone》上第一时间听到——Pi 会有一些涌现特性即将问世。你能给我们描述一下这些任务大致是什么类型的吗?

`[14:24]` **SPEAKER_00:** It's really easy to fool yourself. And so we wanted to test across like field different tasks of different flavor. A task that require precision, task that require reasoning with multiple objects in the scene. It all seems to have this property. That's really nice.

> 人是很容易自欺欺人的。所以我们想在多种不同类型的任务上进行测试:需要精度的任务、需要对场景中多个物体进行推理的任务。它们似乎全都具备这种特性。这真的很棒。

`[14:39]` **SPEAKER_00:** So it does seems like that's something that's kind of a more general property that emerge rather than we just, you know, got lucky and suddenly the models start working on one particular task.

> 所以看起来这确实是某种更具普遍性的、涌现出来的特性,而不是我们只是碰巧走运,模型突然在某一个特定任务上能用了。

`[14:49]` **SPEAKER_04:** Could you help us understand where we are now in terms of like what's working and how well it's working? Like we're not quite at the chat GBT moment yet. Like where are we? And I think you brought some videos that you were going to show us to like help everybody visualize what the current state of the art actually looks like.

> 你能帮我们弄清楚我们现在处于什么阶段吗——就是什么东西是能用的、能用到什么程度?我们还没完全到 ChatGPT 时刻。那我们到哪儿了?我想你带了一些视频要给我们看,好帮大家直观地想象一下当前最先进的水平究竟是什么样子。

`[15:04]` **SPEAKER_00:** I think where we are is I think if you have a task where it's okay for the robot to make a mistake and it's possible for you to set up a mixed autonomy system where you have a person that takes over when the robot make a mistake and provide corrections, it is possible to get to a level of performance where it starts to make sense to think about scaling robot deployment. And the example that I specifically want to highlight here is this blog post that we did with Weave and Ultra. And, you know, it's great that these are both YC company. I want to provide a little bit of context here first. The context is that PI is a primarily research organization.

> 我认为我们所处的阶段是这样:如果你有一个任务,允许机器人犯错,并且你有可能搭建一个混合自主系统——在机器人犯错时由人接管并提供纠正——那么就有可能达到这样一种性能水平,让"规模化部署机器人"开始变得说得通。我想在这里特别强调的例子,是我们与 Weave 和 Ultra 合作发的那篇博客。而且,这两家都是 YC 公司,这很棒。我想先交代一点背景。背景是:Pi 主要是一家研究机构。

`[15:48]` **SPEAKER_00:** We want to focus on building the best model, but we also want to not be tunnel vision. We want to make sure that the model that we built actually going to be useful and actually perform tasks that people in society cares about. And one of the really good way for us to do so is to partner really closely with company that want to get robot out there today. And the way that these relationship work is that we treat each other like we're on the same team, very free flow of information. And we design a system that try to get the best possible performance for the task that these company care about.

> 我们想专注于打造最好的模型,但我们也不想变得目光狭隘。我们想确保我们打造的模型真正有用,真正能完成社会上人们所关心的任务。而实现这一点的一个非常好的方式,就是与那些今天就想把机器人推向现实的公司紧密合作。这种合作关系的运作方式是:我们把彼此当作同一支团队,信息高度自由流通。我们设计一个系统,力求在这些公司所关心的任务上取得尽可能最好的性能。

`[16:24]` **SPEAKER_00:** So let me talk about Weave first. What you're seeing in this video is a system that we built together folding really diverse item of laundry in a real laundromat in the mission. You can see, you know, people walking outside. And why this task is difficult is because there's just infinite possibility of observation space. Like, you know, clothings are deformable.

> 那我先讲 Weave。你在这段视频里看到的,是我们一起打造的一个系统,它正在旧金山 Mission 区一家真实的自助洗衣店里叠各种各样的衣物。你能看到,外面有人走过。这个任务之所以难,是因为观测空间的可能性是无穷的。你知道,衣物是可形变的。

`[16:49]` **SPEAKER_00:** And no two items of clothing here are the same. And these are also unseen. You know, these are not, like, clothing items that are seen in the training data.

> 而且这里没有两件衣物是一样的。这些也都是"没见过的"。它们并不是训练数据里出现过的那些衣物。

`[16:58]` **SPEAKER_01:** Yeah, I love this team. They are some of the most cracked people out of Apple I've ever met.

> 是的,我很喜欢这支团队。他们是我见过的从 Apple 出来的人里最顶尖厉害的一批。

`[17:03]` **SPEAKER_04:** Gary was the partner for Weave. Maybe you want to, like, explain, like, what Weave is and what their, like, company is.

> Weave 的对接合伙人是 Gary。也许你可以解释一下 Weave 是什么、他们公司是做什么的。

`[17:08]` **SPEAKER_01:** Yeah, I mean, they're actually, you know, shipping their first robots into the home. We sort of talked about it as, you know, being able to do household tasks like this. And I think they were very inspired by that. They were inspired by Physical Intelligence's first demos with laundry folding. So it's actually a total trip to hear about it, you know, a year ago.

> 是的,我是说,他们其实正在把他们的第一批机器人送进家庭。我们把它描述为能够完成像这样的家务任务。我觉得他们深受启发。他们受到了 Physical Intelligence 最初那些叠衣服演示的启发。所以一年前听到这件事,真的相当奇妙。

`[17:29]` **SPEAKER_01:** We were talking about them doing it. And then now to see them do it working hand-in-hand with you is really awesome. I think this is a great example of, like, you know, you need the model smarts, you need the data collection, and then the hardware and the sort of system integration all working together is just hard to nail.

> 我们当时还在谈论他们要去做这件事。而如今看到他们与你们携手把它做出来,真的太棒了。我觉得这是一个绝佳的例子:你需要模型的智能,需要数据收集,然后还有硬件以及那种系统集成,所有这些协同运作起来,是非常难以做到位的。

`[17:47]` **SPEAKER_00:** Yeah, and to get back to your question about why robotic is hard, it's really, it is a really hard system problem. Like, you need everything to work well and work well together to get this result. And, like, Weave is such an incredible team for us to work with to get this result. And it actually didn't even take us that long to get this result. It was roughly, well, we set a goal, and maybe it was, like, two weeks afterwards where we got a model that was, got a model and a system that was good enough at performing this task.

> 是的,回到你关于"为什么机器人这么难"的问题——它真的是一个非常难的系统性问题。你需要每一环都运作良好、并且良好地协同运作,才能得到这样的结果。而 Weave 是一支极其出色的团队,能和他们合作拿到这个结果太好了。而实际上,我们拿到这个结果并没有花那么久。大约是这样:我们设定了一个目标,大概两周之后,我们就得到了一个模型——一个模型和一个系统——它已经足够擅长完成这项任务了。

`[18:18]` **SPEAKER_04:** It still, like, blows my mind to see a robot actually folding laundry because I remember until, basically, until ChatGPT, I didn't know if this would exist even in my entire lifetime. Because, like, folding laundry, I mean, it's always been, like, the Turing test for robotics because there's no way to, like, deterministically program a system the way that you did, like, pre-AI to do this because the space is, like, so infinite. And, like, we've shown that it's possible for us to do, like, basically, if everyone can do this, like, robots will be able to do everything. It's only a matter of, like, improving it from here.

> 看到机器人真的在叠衣服,这依然让我震撼不已。因为我记得,基本上直到 ChatGPT 出现之前,我都不确定这种东西在我有生之年是否会出现。因为叠衣服,我是说,它一直是机器人领域的"图灵测试",因为你没办法像 AI 出现之前那样,用确定性的方式去编程一个系统来做这件事,因为其空间实在太无穷了。而我们已经证明了这是我们能做到的——基本上,如果人人都能做到这一点,那机器人将能做任何事。剩下的只是从这里开始不断改进的问题。

`[18:47]` **SPEAKER_00:** There was a funny story where when we first published Pi Zero, people thought of us as the laundry company. Because the demo was just focused on laundry and actually picking home tasks, especially tasks that has to do with deformable objects, is a very intentional choice on our end. We're not just after the home. We really want to make it broadly applicable. But picking home tasks for us to start with has a few benefits.

> 有个好玩的故事:我们第一次发布 Pi Zero 时,人们把我们当成了"洗衣公司"。因为演示只聚焦于洗衣。而实际上,选择家务任务、尤其是与可形变物体有关的任务,是我们这边一个非常有意的选择。我们并不只是盯着家庭场景,我们真正想要的是让它具有广泛适用性。但选择从家务任务入手,对我们来说有几个好处。

`[19:13]` **SPEAKER_00:** Like, one, it's relatable. You know, you can see the laundry folding demo and you can kind of, like, grok how this is going to be useful. And you can get a sense of why it's hard. And the second is that it's really easy to set up to test generalization.

> 比如,第一,它有共鸣感。你看到叠衣服的演示,就能大致领会它将会多么有用。而且你能感受到它为什么难。第二,它很容易搭建起来去测试泛化能力。

`[19:27]` **SPEAKER_02:** You can talk about Ultra, which is your company, Jared. A demo of it.

> 你可以讲讲 Ultra,那是你的公司,Jared。给我们看个它的演示。

`[19:30]` **SPEAKER_00:** Yeah, this is Ultra. The thing that I love about this video is you see it's bright outside. And you see this is 4x speed and it's 100 minutes. If I scroll to the end, the sun has set.

> 好的,这是 Ultra。我喜欢这段视频的一点是:你看,外面还很亮。你看这是 4 倍速播放,总时长 100 分钟。如果我拖到结尾,太阳已经落山了。

`[19:42]` **SPEAKER_02:** Oh, wow. That was one of the big problems in robotics. Where it would be so sensitive to the environment in lighting and mess up the vision system, the semantics and part of it. Yeah.

> 哦,哇。这曾是机器人领域的一大难题——它对环境光照极其敏感,会把视觉系统、语义等等都搞乱。是的。

`[19:54]` **SPEAKER_00:** And the interesting thing here is that it is possible to get to the level of autonomy that the robot is just performing the task. This is autonomy at scale. Like, this is ready to be scaled.

> 而这里有意思的地方在于:有可能达到这样一种自主水平——机器人就这么把任务干着。这是可规模化的自主。这已经准备好被规模化了。

`[20:08]` **SPEAKER_04:** Quan, because this task is less familiar than laundry folding, do you want to explain what the robot is doing here and what Ultra is, like, doing as a company? Ultra is a company

> Quan,因为这个任务不像叠衣服那么为人熟知,你想不想解释一下机器人在这里做什么、以及 Ultra 作为一家公司是做什么的?Ultra 是一家公司——

`[20:17]` **SPEAKER_00:** that want to make it really easy to adapt robot to, you know, new tasks. And right now they're focusing on logistics space, which is really important because there's lots of labor shortage in logistics. And the task that we focus on together here is, you know, if you order an item from Amazon, you sometimes get this soft pouch that item gets shipped from. And the task here is you have a tray of these items here and the robot is supposed to pick one of them. at the time and place it inside this pouch.

> ——它想让"让机器人适配新任务"变得非常容易。目前他们专注于物流领域,这非常重要,因为物流行业有大量劳动力短缺。我们在这里共同聚焦的任务是:如果你在亚马逊上订购一件商品,有时你会收到一个软质包装袋,商品就是装在里面寄出的。这里的任务是:你有一托盘这样的商品,机器人要每次拿起其中一件,放进这个袋子里。

`[20:48]` **SPEAKER_00:** The machine would then close it and then pick up the pouch and put it on the left here to be ready for shipping. Now, this is hard because there are many different types of objects that can be in this tray. And the opening here is actually very narrow. So you see this interesting example of the robot kind of nudging the item to go into the pouch. And that's really hard.

> 然后机器会把袋子封上,再拿起袋子放到左边这里,准备发货。这件事之所以难,是因为托盘里可能有许多不同类型的物品。而这里的开口其实非常窄。所以你看到这个有意思的例子:机器人像是在轻推商品,让它塞进袋子。这真的很难。

`[21:11]` **SPEAKER_00:** Like, that requires a very good understanding of the scene and, like, very precise motion to nudge the object into the pouch. The other thing that's hard about this task is the level of autonomy that's required. Like, this is running for an entire day. There is still human intervention, I want to say, in this, like, full-day operation. But the level of intervention is actually quite minimal.

> 这需要对场景有非常好的理解,以及非常精确的动作,才能把物品轻推进袋子里。这个任务另一个难点在于所要求的自主程度。这可是运行了一整天。我要说明,在这样一整天的运行中,仍然有人工干预。但干预的程度其实相当小。

`[21:39]` **SPEAKER_04:** This is not just, like, some, like, demo station, right? This is actually recorded in an actual e-commerce warehouse where they're actually shipping real products to real customers. This isn't just, like, a lab.

> 这不只是什么演示台,对吧?这实际上是在一个真实的电商仓库里录制的,他们真的在把真实的商品发给真实的客户。这可不只是实验室。

`[21:48]` **SPEAKER_00:** This is packaging real customer, real order for customer to be shipped out in a real warehouse. So this is real operations.

> 这是在为真实客户、真实订单打包,在一个真实的仓库里发货出去。所以这是真实的运营。

`[21:56]` **SPEAKER_04:** So I think this is really cool because I think when people think about robots, they tend to think of the consumer use cases like Weave because that's, you know, what we're familiar with in our daily life. What I find really interesting is that there's, like, a million applications like this Ultra thing that you wouldn't think of as obviously, like, oh, who packs the, like, soft pouch of things that you get from, like, Amazon? Well, there's some person, like, who does that, and this is, like, a job that we could not build a robot to do.

> 我觉得这真的很酷,因为我认为当人们想到机器人时,往往会想到像 Weave 那样的消费级用例,因为那是我们日常生活中熟悉的东西。而我觉得真正有意思的是:还有成千上万像 Ultra 这样的应用,是你不会显而易见想到的——比如,谁来打包你从亚马逊收到的那种软袋商品?嗯,总有个人在做这件事,而这曾是一份我们造不出机器人来干的工作。

`[22:18]` **SPEAKER_00:** The interesting thing about the approach is that you're converting it from a very difficult engineering problem into a operation problem of how do I identify the use case and how do I collect the right data, which is, in some sense, more scalable because you can build the system that allows you to collect data from many different tasks. So, you know, it's not a problem of how do I scale data collection rather than, you know, for every new product, for every new task, how do I design a really difficult engineering system to solve it?

> 这种方法有意思的地方在于:你把它从一个非常困难的工程问题,转化成了一个运营问题——即"我如何识别用例、如何收集正确的数据"。从某种意义上说,这更可规模化,因为你可以搭建一个能让你从许多不同任务中收集数据的系统。所以,问题变成了"我如何规模化地收集数据",而不是"对每一款新产品、每一项新任务,我如何设计一套极其困难的工程系统去解决它"。

`[22:47]` **SPEAKER_02:** YC Startup School is back. We're hand-selecting the most promising builders in the world and flying them out to San Francisco for July 25th and 26th to discuss the cutting edge of tech. Apply now for a spot. Okay, back to the video. I think one thing that the audience may not know is that you have a very unique technical insight that, in the past, robotics folks would have kind of gasped and be shocked because robots need to run in real time.

> YC Startup School 回归了。我们正在从全世界精挑细选最有潜力的开发者,把他们请到旧金山,在 7 月 25 日和 26 日一起探讨科技前沿。现在就申请一个名额吧。好,回到视频。我想有一件事观众可能不知道:你们有一个非常独特的技术洞见——放在过去,机器人圈的人听了会倒吸一口凉气、大为震惊,因为机器人需要实时运行。

`[23:13]` **SPEAKER_02:** A lot of times, all of the compute runs in on-device, but you guys have done something very different. Can you tell us more about that so that this works in real time with large models and really well? So, the context here is that, you know, we talked to many companies that would like to deploy robots

> 很多时候,所有的计算都跑在设备端本地,但你们做了非常不同的事情。你能多讲讲吗——好让这套东西能在使用大模型的情况下实时、且非常良好地运行?

`[23:27]` **SPEAKER_00:** and one of the first questions we get is, what compute units should we get on the robot? You know, it's expensive, it's going to increase the bomb cost, and they're worried that it's going to go out in fashion very quickly because they don't know what they're going to get. So, you know, I think it's important to think in fashion very quickly because the model changes, the model gets bigger. How do I make sure that the hardware that I'm going to commit to today is going to be viable for a couple of years? It's a very difficult question.

> 背景是这样:我们和许多想部署机器人的公司交流过,我们最先被问到的问题之一就是——"我们应该在机器人上配什么算力单元?"你知道,它很贵,会推高物料清单(BOM)成本,而且他们担心它很快就会过时,因为他们不知道该选什么。所以我觉得重要的是要意识到它会很快过时,因为模型在变、模型在变大。我怎么才能确保今天决定投入的硬件在未来几年里仍然可用?这是一个非常难的问题。

`[23:51]` **SPEAKER_00:** People are often really surprised when I tell them that almost all of the robot evaluation that we run at Pi today, including the really complicated demo that we have shown, making coffee, folding laundry, mobile robots navigating around, the model is actually hosted in the cloud. And, you know, this is not like a cloud as in a server in the office. It's a real-world model to the cloud. The model is hosted in a data center somewhere. And within this high-frequency control loop that is controlling the robot, the robot is actually querying an API endpoint that hosts the model, sending it images and language command and getting back action that then executed directly on the robot.

> 当我告诉人们:我们今天在 Pi 运行的几乎所有机器人评测——包括我们展示过的那些非常复杂的演示,煮咖啡、叠衣服、移动机器人四处导航——其模型实际上是托管在云端的,人们常常大为惊讶。而且,这可不是那种"办公室里放台服务器"意义上的云。这是把真实世界里的模型放到云端。模型托管在某处的数据中心里。而在这个控制机器人的高频控制回路中,机器人实际上是在查询一个托管着模型的 API 端点,把图像和语言指令发过去,再取回动作,然后直接在机器人上执行。

`[24:27]` **SPEAKER_00:** And this is surprising because of precisely the reason that you mentioned, you know, how do you actually make it work? This is why it's really important for Pi to couple a lot of different applications and systems, hardware, and model development and research very tightly together because it allows us to solve for this problem. So, for example, one of the insights that we have here is that you can actually bury the inference time within the robot control loop because, you know, if I'm a robot, I have enough action for me to execute for the next 100 milliseconds. There's no reason for me to wait until I finish executing that action to ask my model for a different action. I can do it as fast as inference, essentially.

> 而这之所以令人惊讶,恰恰是因为你提到的那个原因:你到底是怎么让它跑起来的?这正是为什么对 Pi 来说,把许多不同的应用、系统、硬件、以及模型研发与研究非常紧密地耦合在一起如此重要——因为这让我们能解决这个问题。举例来说,我们这里的一个洞见是:你其实可以把推理时间"埋"在机器人的控制回路里。因为,假如我是一个机器人,我手上已经有足够多的动作可供接下来 100 毫秒执行了,那我没有理由要等到执行完那批动作后,才去向模型索要下一批动作。本质上,我可以在推理速度所允许的范围内尽快去做这件事。

`[25:13]` **SPEAKER_00:** And so, you know, maybe when I only have 50 milliseconds of action worth left, I can ask for the next sets of action and when the current 50 milliseconds is over, I have something that's ready for me to continue with, you know, my next 100 milliseconds. So that's one of the insight. The other kind of algorithmic improvement, we refer to them as real-time chunking. Desire inference in such a way that you know there's going to be a delay in how long it takes to query the model on the cloud, basically. Like the problem here, if I get a little bit more technical, is an action chunk is a sequence of action that I can execute on the robot.

> 于是,也许当我只剩下 50 毫秒的动作可执行时,我就可以去请求下一批动作;等当前这 50 毫秒结束时,我就已经有准备好的东西,可以继续我接下来的 100 毫秒。这是其中一个洞见。另一类算法上的改进,我们称之为"实时分块(real-time chunking)"。基本思路是,以某种方式设计推理,使之考虑到"在云端查询模型会有延迟"这一事实。如果我讲得再技术一点,这里的问题是:一个动作块(action chunk)是我可以在机器人上执行的一串动作序列。

`[25:56]` **SPEAKER_00:** So, you know, it's not just one action. And if I have an action chunk that I can execute for 100 milliseconds and 50 milliseconds in, I want to predict another action chunk and I'm going to transition to that new action chunk if my current 50 millisecond is over. How do I make sure the two are consistent? Like, you know, how do I make sure that if I'm moving this way, the next action chunk is going to continue to allow me to continue to be smoothly

> 所以,它不只是单个动作。假如我有一个可以执行 100 毫秒的动作块,而在进行到第 50 毫秒时,我想预测另一个动作块,并且在当前这 50 毫秒结束时切换到那个新动作块。我怎么确保这两者是一致的?就是说,我怎么确保如果我正朝这个方向运动,下一个动作块会让我继续平滑地——

`[26:20]` **SPEAKER_01:** moving this way?

> ——朝这个方向运动下去?

`[26:21]` **SPEAKER_00:** You can pre-compute. Yeah, you can pre-compute and like that's one of the algorithmic improvement that we made to make inference using model hosted

> 你可以预先计算。是的,你可以预先计算,这正是我们所做的算法改进之一,使得用云端托管的模型进行推理成为可能。

`[26:29]` **SPEAKER_01:** in the cloud possible. I studied computer engineering, so I'm not really an algorithms person, but when it comes to systems like that, like pipelining, like get me all over that. That's great. That's so interesting.

> 我学的是计算机工程,所以我其实不算是搞算法的人,但一说到那类系统性的东西,比如流水线(pipelining),我就来劲了。这太棒了。太有意思了。

`[26:40]` **SPEAKER_02:** I mean, this simplifies is a brilliant choice because it simplifies so much of the system for the robots. You don't need all these clunky. I don't know. People have two operating systems that sometimes for robots embedded RTOS and then the regular one and all these complex giant compute and power. And this is what the initial versions of Waymo used to run basically a server on the trunk and you can't afford to do that with general day robotics, which is brilliant

> 我是说,这种简化是个绝妙的选择,因为它为机器人大大简化了系统。你不需要所有那些笨重的东西。我不确定——有时人们给机器人配两套操作系统,一套是嵌入式 RTOS,另一套是常规的,还有所有这些复杂庞大的算力和功耗。这正是 Waymo 早期版本的做法——基本上是在后备箱里放一台服务器,而在日常通用机器人上你根本负担不起这么干,所以这个思路很妙。

`[27:08]` **SPEAKER_01:** because you don't have to. I mean, you can do things. Some of it obviously has to be some compute there, but a lot of the compute can happen elsewhere. And then is there there must be a video like this, this thing that we're looking at in the top left, like how much of that is sort of like video feedback?

> 因为你不必这么做。我是说,有些事情你可以做,显然本地必须有一些算力,但大量的计算可以放在别处。那么,一定有个视频画面——我们看的左上角这个东西,那里面有多少算是视频回传?

`[27:26]` **SPEAKER_04:** How much of it is like local processed? I mean, is there any compute locally on this robot

> 有多少是本地处理的?我是说,这个机器人本地有没有任何算力,

`[27:31]` **SPEAKER_00:** or is it just like a dumb like video camera that streams data to the cloud for this? I'm trying to believe that it's just a dumb computer for this specific video. I don't remember, but I'm just 100% confident that we can make this work with a dumb computer on the robot. And one other interesting thing about our collaboration with Weave and Ultra is one, I've never seen

> 还是说它就只是个"笨"摄像头,把数据流传到云端?就这个具体视频而言,我倾向于相信它就只是一台"笨"电脑。我不太记得了,但我百分之百确信,我们能用机器人上一台"笨"电脑就把这件事做成。而关于我们与 Weave 和 Ultra 的合作,还有一件有意思的事:第一,我从没见过——

`[27:53]` **SPEAKER_01:** that robot in person.

> ——那台机器人的实物。

`[27:54]` **SPEAKER_00:** Oh, wow. Two is I have very little idea about how the robot actually works.

> 哦,哇。第二,我对那台机器人实际是怎么运作的知之甚少。

`[28:00]` **SPEAKER_04:** Interesting.

> 有意思。

`[28:01]` **SPEAKER_00:** And that's a very intentional choice. I want to stay away from that as far as possible. I also don't know how they collect data. Like I intentionally don't ask them this question to understand whether it's possible for an organization like Pi to parachute into their existing system and to work really closely with them on the thing that actually matters to get the system to work and not have to learn about how they've set up their system because in a way that's like a more

> 而这是一个非常有意的选择。我想尽可能远离那部分。我也不知道他们是怎么收集数据的。我故意不去问他们这个问题,为的是弄清楚:像 Pi 这样的机构,是否有可能"空降"进他们既有的系统,和他们在真正关键、真正决定系统能否跑通的事情上紧密合作,而不必去了解他们是怎么搭建自己系统的。因为某种程度上,这是一种更可规模化的配方。

`[28:31]` **SPEAKER_02:** scalable recipe. Yeah, you completely decouple a lot of the hardware control from the semantics and planning which just works. Just brilliant.

> 对,你把大量的硬件控制与语义和规划彻底解耦,而它就是能跑通。真是绝妙。

`[28:41]` **SPEAKER_00:** Yeah. I mean, I'm really surprised. It works. When we started the company, we thought that real deployment is only going to be in a conversation like five years into the life of the company because the problem is just really hard. And we're two years in and this is the result that we have and real deployment and scaling the number of robots is a really serious consideration today and so the pace of progress has just been very pleasantly much faster than we expected

> 是的。我是说,我真的很惊讶,它居然行得通。我们创办公司时,以为"真实部署"要等到公司成立大约五年之后才谈得上,因为这个问题实在太难了。而如今我们才走过两年,就已经有了这样的成果,真实部署以及规模化增加机器人数量在今天已经是一个很严肃的考量。所以进展的节奏出乎意料地、令人欣喜地比我们原先预期的快得多。

`[29:12]` **SPEAKER_04:** originally. Often on this podcast we talk about like what all this means for startup founders. I think that might be an interesting question for us to explore here. So if you imagine someone was listening to this podcast, maybe they're like a college student that's studying computer science and they think robots are really cool and they want to do something like this, how should they get started and what are the skills that they need? Do they need to be a mechanical engineer or do they need a robot arm and camera system and like what?

> 在这个播客里,我们经常聊这一切对创业者意味着什么。我觉得这在这里是个值得探讨的有趣问题。所以设想有人正在听这个播客,也许是个学计算机科学的大学生,他们觉得机器人真的很酷,想做点像这样的事情,那他们应该如何起步、需要哪些技能?他们需要成为机械工程师吗?还是需要一台机械臂加一套摄像头系统,或者需要什么?

`[29:39]` **SPEAKER_04:** And load pie and you're often running in like a day.

> 然后装上 Pi,大概一天就能上手运行起来?

`[29:42]` **SPEAKER_00:** Yeah. Before I actually answer your question, let me provide a few more context. The first is that robotic is traditionally really hard because it's an extremely vertically integrated business. You need to have your own customer relationship, your own hardware, your own autonomy stack, your own safety certification, your own everything. And the barrier to entry is just really high because of that and one of the things that we're trying to change is that we're trying to provide a foundation of physical intelligence that the community can build on top of that allow them to onboard autonomy onto their robot and their task much quicker than before.

> 好。在我真正回答你的问题之前,让我再补充一点背景。第一点是,机器人传统上非常难,因为它是一门极度垂直整合的生意。你需要有自己的客户关系、自己的硬件、自己的自主(算法)栈、自己的安全认证、自己的一切。正因如此,准入门槛真的非常高。我们正试图改变的事情之一,就是提供一个"物理智能"的基础,让社区可以在它之上构建,从而让他们把自主能力搭载到自己的机器人和任务上,比以前快得多。

`[30:20]` **SPEAKER_00:** So that's the first. We want to provide that kind of seat of intelligence that allow people to move much faster so that they can focus on other problems. The second thing is that I think the recipe for starting a vertical robotic business today is one, have a really good understanding of the existing workflow because the robotic system needs to fit into an existing workflow. And the second is to be very meticulous about identifying where the opportunity is. If there's a workflow that needs X number of work today, where is the robot when you insert it is going to make the biggest difference.

> 这是第一点。我们想提供那样一个"智能的底座",让人们能行动得快得多,从而能专注于其他问题。第二点是,我认为如今创办一家垂直机器人公司的配方是:第一,对现有工作流程有非常好的理解,因为机器人系统需要嵌入既有的工作流程之中。第二,非常细致地识别机会所在。如果有一个工作流程今天需要 X 份工作量,那么你把机器人插进去,放在哪里才会产生最大的差别。

`[31:00]` **SPEAKER_00:** And two is to really be scrappy when it comes to hardware and data collections. You don't need an incredibly expensive robot that is capable of very precise motion today to be able to do this task. And the reason why is this model really reactive and so they can compensate for some of the inaccuracy in the actual robot movement and to ensure that you have the ability to collect data and to run evaluation, especially evaluation in real deployment. The next step after that is to get a mixed autonomy system that allow you to get to the point where it's break even. Like break even economically.

> 第二点是,在硬件和数据收集上要真正做到精打细算、因陋就简。如今你并不需要一台极其昂贵、能做非常精确动作的机器人才能完成这项任务。原因在于,这个模型很有"反应性",所以它们能补偿实际机器人运动中的一些不精确之处。同时要确保你具备收集数据和运行评测的能力,尤其是在真实部署中的评测。再往下的一步,是搭建一个混合自主系统,让你能够走到收支平衡的那个点。也就是经济上的收支平衡。

`[31:36]` **SPEAKER_00:** Break even economically because the reason why that's important is because it allows you to then scale the number of robots. Because if you lose money

> 经济上的收支平衡,之所以重要,是因为它随后能让你规模化地增加机器人的数量。因为如果你在每一台机器人上都亏钱——

`[31:43]` **SPEAKER_04:** in every robot, it's very hard to scale.

> ——那就很难规模化。

`[31:45]` **SPEAKER_02:** That has been historically one of the biggest challenges for robotic companies as they go into growth stage. It's just the payback hack period is just doesn't make sense. Yeah, so the equation

> 从历史上看,这一直是机器人公司在进入成长阶段时最大的挑战之一。就是那个回本周期根本说不通。是的,所以这个公式——

`[31:53]` **SPEAKER_00:** I think for starting a robotic business has changed and will continue to change at an accelerating pace because the upfront cost is not that high anymore. And now, you know, what is the upfront cost? The upfront cost is much cheaper hardware, ability to collect data, ability to collect evaluation and ability to kind of like understand the use case to see where they should insert the robot. You know, it's not about having incredibly expensive hardware. It's not about having your own proprietary, I think, autonomy, classical stack anymore to be able to do that.

> ——我认为,创办一家机器人公司的公式已经改变,而且会以加速的态势持续改变,因为如今的前期成本已经没有那么高了。那么现在,前期成本是什么?前期成本是便宜得多的硬件、收集数据的能力、收集评测的能力,以及理解用例、判断该把机器人插入何处的能力。你知道,它不再是关于要拥有极其昂贵的硬件,也不再是关于要拥有自己专有的、传统的自主算法栈才能做到这些。

`[32:32]` **SPEAKER_00:** You have to do this task. And so it allows a company to focus on the component that will actually allow them to differentiate themselves from the rest of the space.

> 你要去完成这项任务。因此,它让一家公司能够专注于那些真正能让自己在这个领域中脱颖而出、与众不同的部分。

`[32:41]` **SPEAKER_04:** Now that you've sort of unbundled it and you no longer need to build this fully vertically integrated company in order to build a robotics company, are we on the precipice of a Cambrian explosion of vertical robotics companies where there's going to be like a thousand companies like Ultra going after, you know, every like menial job in the economy and like getting a deep understanding of the customer, building a robot without any problem, doing like mixed human machine deployment until it like can run fully autonomously and building a company in every sector? Is that the future that you see people building on top of Pi? It's funny that you mentioned

> 既然你们某种程度上把它"解绑"了,创办一家机器人公司不再需要打造一家完全垂直整合的公司,那我们是否正处在一场垂直机器人公司"寒武纪大爆发"的悬崖边上——会有比如一千家像 Ultra 这样的公司,去攻占经济中每一份琐碎的体力工作,深入理解客户,毫无障碍地造出机器人,做人机混合部署,直到它能完全自主运行,并在每一个行业里都建起一家公司?这就是你所看到的、人们将在 Pi 之上构建的未来吗?

`[33:13]` **SPEAKER_00:** Cambrian explosion because when we wrote this blog post, there was that term that was very kind of like hotly debated. We are, I think, academics at Hurt and we want to be kind of very measure when we communicate. But, you know, myself personally, I believe there's going to be a Cambrian explosion of, you know, of robotic company across the entire world and across many, many different verticals just because it's just so much cheaper to build and it doesn't require, you know, someone with 20 years of experience in robotic to start anymore. You know, it requires someone that is really scrappy that can move really quickly, can do the system integration, can understand customer what they want to start the deployment.

> 你提到"寒武纪大爆发"很有意思,因为我们写这篇博客时,这个词曾引起相当激烈的争论。我想我们骨子里是学者,交流时希望非常有分寸。但就我个人而言,我相信将会出现一场"寒武纪大爆发"——遍及全世界、横跨许许多多不同垂直领域的机器人公司大爆发,原因很简单:构建的成本已经便宜太多了,而且它不再需要一个有 20 年机器人经验的人才能起步。它需要的是一个真正能精打细算、能快速行动、能做系统集成、能理解客户需求的人,来开始部署。

`[33:59]` **SPEAKER_01:** I mean, what's coming up for me is obviously we work with a lot of robotics companies and to meet a lot of founders and it feels like there's this continuum. One is to use an analogy to compete, you know, personal computing. You could argue that industrial robotics today is basically like mainframe for a mini computer level. Like, you know, if you look back in the 70s, huge public companies like Digital Computer that, you know, just did like these sort of very, very expensive deployments but like they were very, very specialized. And it was all extreme enterprise.

> 我是说,我脑海里浮现的是——显然我们和很多机器人公司合作,也见过很多创始人,感觉存在这样一个连续谱。打个比方,类比个人计算的发展。你可以说,今天的工业机器人基本上相当于"大型机"到"小型机"的水平。你回看 70 年代,像 Digital(数字设备公司)这样的大型上市公司,做的就是那种非常非常昂贵的部署,但它们高度专门化。而且全都是极端的企业级市场。

`[34:33]` **SPEAKER_01:** Like, you know, the idea of a personal computer was ridiculous, right? You know, it took the Altair and then Apple I and Apple II and then IBM PC XT to like create personal computing. And then like the traditional advice for robotics for many years is like go after like dirty and dangerous. And then, of course, those are sort of the industrial cases. Like, you know, you have these giant Tesla robots in the Gigafactory and things like that.

> 你知道,当时"个人电脑"这个想法简直荒唐,对吧?正是靠 Altair,然后 Apple I、Apple II,再到 IBM PC XT,才创造出了个人计算。而多年来对机器人的传统建议是:去做那些"脏活和危险活(dirty and dangerous)"。当然,那些属于工业场景。比如你在超级工厂(Gigafactory)里看到的那些巨大的特斯拉机器人之类。

`[34:58]` **SPEAKER_01:** It feels like what you said around profitability is really, really big. So, you know, does that mean that the people who do the vertical robot Cambrian explosion sort of moment, the people who are sort of first in that, like it sounds like they would be the first to be profitable and not dirty and dangerous. I think this is already

> 感觉你刚才关于盈利能力所说的那点,真的非常非常重要。所以,这是否意味着:那些赶上垂直机器人"寒武纪大爆发"时刻的人、那些率先入场的人,听起来会是最先实现盈利的一批,而且做的并不是"脏活和危险活"?

`[35:21]` **SPEAKER_00:** happening today. I think we have the fortune of having lots of visibility into the robotic community because, you know, people would like to talk to us. People would like to learn, you know, what it's like to build a foundation model for robotic and people would like to know how do I get the same level of autonomy? And there are so many companies and businesses that we talk to that would love to put a robot into their space that, you know, it's okay for the robot to make a mistake. And this is needed so much.

> 我觉得这今天已经在发生了。我认为我们很幸运,能对机器人社区有大量的了解,因为人们愿意和我们交流。人们想了解为机器人打造基座模型是什么感受,也想知道"我该如何获得同样水平的自主能力"。我们接触到的许许多多公司和企业,都非常想在他们的场景里放一台机器人——一台"允许犯错"的机器人。而这样的需求实在太旺盛了。

`[35:51]` **SPEAKER_00:** I really believe that the recipe that I mentioned earlier of identify where the robot can fit in focus on cheaper hardware, collect data, run evaluation, mix autonomy, break even, scale robots will work across many different verticals. And I'm seeing it play out today and it's just incredibly exciting to see. And this is pretty cool

> 我真心相信,我前面提到的那套配方——识别机器人能嵌入之处、专注于更便宜的硬件、收集数据、运行评测、混合自主、实现收支平衡、规模化增加机器人——将会在许多不同垂直领域奏效。而我今天正看着它一幕幕上演,这实在令人激动不已。

`[36:11]` **SPEAKER_04:** that you literally just gave people the playbook for how to build a vertical robotics company. Like this is a playbook that could possibly be followed successfully hundreds or thousands of times. And the reason why

> 这真的很酷——你刚刚简直是把如何打造一家垂直机器人公司的操作手册直接交给了大家。这是一份可能被成功照搬成百上千次的操作手册。

`[36:21]` **SPEAKER_00:** I want to mention it is because I do want to see that Cambrian explosions. And so, we want to help enable it. You know, for Pi, if we talk about why Pi is going to fail, it's probably going to be because the problem is just way too hard. You know, maybe it takes 50 more years to solve the robotic problem and, you know, not a couple of years, five, ten. And so, we want to enable the community.

> 我之所以想提这套配方,是因为我真的想看到那样一场"寒武纪大爆发"。所以我们想帮忙促成它。对 Pi 来说,如果我们谈"Pi 为什么会失败",那很可能是因为这个问题实在太难了。也许要再花 50 年才能解决机器人问题,而不是短短几年、五年、十年。所以,我们想赋能整个社区。

`[36:46]` **SPEAKER_00:** We want to accelerate progress and that's why we're very open. We publish our research. We open source Pi 0 and Pi 05. And people also shock when they ask me, you know, what's the difference between Pi 0 and Pi 05 that you open source versus the model that we use internally, Pi 0 and Pi 05? And the answer was, I actually know.

> 我们想加速进步,这正是为什么我们非常开放。我们发表我们的研究。我们把 Pi 0 和 Pi 0.5 开源。人们问我"你们开源的 Pi 0 和 Pi 0.5,跟你们内部使用的 Pi 0 和 Pi 0.5 有什么区别"时,也大为惊讶。而答案是——我其实知道。

`[37:05]` **SPEAKER_00:** It's the same model. Like, the pre-trained model weights that you're using that we open source is also the pre-trained model weights that our researchers internally use for Pi 0 and Pi 05. And so, we really want to help accelerate progress in the community and to create that Cambrian explosions.

> 它就是同一个模型。你所使用的、我们开源出来的预训练模型权重,也正是我们内部研究人员用于 Pi 0 和 Pi 0.5 的那份预训练模型权重。所以,我们是真心想帮助加速社区的进步,并催生那样一场"寒武纪大爆发"。

`[37:21]` **SPEAKER_01:** Yeah, that's very inspiring. I mean, I feel like that's everyone's sort of spending a lot of time in the digital world. And it feels like, you know, now is the time to start thinking about, you know, the world of atoms. And this is sort of the perfect mix of actually, like, you know, how do you take electrons and turn it into abundance in the, you know, atoms world? And I think about Dario Amadei's essay, All Watched Over by Machines of Loving Grace.

> 是的,这非常鼓舞人心。我是说,我感觉大家现在都花了很多时间在数字世界里。而感觉现在正是开始思考"原子世界"的时候了。而这某种程度上是一种完美的融合——即,你如何把电子转化为原子世界里的丰盈富足?我想到了 Dario Amodei 的那篇文章《被慈爱恩典的机器所照看(All Watched Over by Machines of Loving Grace)》。

`[37:49]` **SPEAKER_01:** And when you really think about the perfect manifestation of that, it's not like, you know, perfect agents that look over you and say, you just like in the electronic world. It's, you know, actually something a little bit more akin to what we're seeing here.

> 而当你真正去思考那愿景的完美体现时,它并不是那种在电子世界里照看你、对你说话的完美智能体。它其实更接近于我们在这里所看到的这类东西。

`[38:04]` **SPEAKER_00:** Yeah. And this has really been our mission from the start is to create that Cambrian explosion. And, you know, this is why we choose to focus on the model because we believe that is the bottleneck to just really make robot useful across many different tasks in the world. And that's why we also focus on cross embodiment. You know, success for us is not defined as only our model on our robot performing tasks that is useful.

> 是的。而这从一开始就是我们的使命——去催生那样一场"寒武纪大爆发"。这正是为什么我们选择专注于模型,因为我们相信那才是"真正让机器人在世界上各种不同任务中变得有用"的瓶颈所在。这也是为什么我们同样专注于跨形态。对我们而言,成功的定义并不仅仅是"我们的模型在我们的机器人上完成有用的任务"。

`[38:30]` **SPEAKER_00:** The surface area for success is actually much larger, which is our model performing really useful tasks on somebody else robot out there. Maybe that we don't even know what that robot is like in a way that's useful to the end consumer.

> 成功的"表面积"其实要大得多,那就是:我们的模型在别人的机器人上完成真正有用的任务——也许是一台我们甚至都不知道长什么样的机器人,以一种对终端消费者有用的方式。

`[38:45]` **SPEAKER_03:** Could we maybe talk a little bit about like the humans behind the robots here? How did the company get started? Like who are the, who are your co-founders? How do you all get together? And what skills do you each bring to such a complex problem?

> 我们能不能稍微聊聊机器人背后的那些人?公司是怎么起步的?你的联合创始人都是谁?你们是怎么走到一起的?面对这样一个复杂的问题,你们各自带来了哪些技能?

`[38:58]` **SPEAKER_00:** Sometimes the joke I make here is that the human behind the robots are also robots. Not really. Yeah, so Pi is a very, I would say, untraditional company. We have a like larger than average founding teams. And some of us work really closely together when we were at the robotic team at Google.

> 我有时开的玩笑是:机器人背后的人其实也是机器人。当然不是真的。好,Pi 是一家我会说非常"非传统"的公司。我们有一支比一般规模更大的创始团队。我们中的一些人在 Google 的机器人团队时就已经紧密合作过了。

`[39:17]` **SPEAKER_00:** And the robotics team at Google was I think a really, really great environment for seeing the sign of life and creating the relationship in the community that allow the robot community and like these advances to flourish. There is Locky, which we met when we were thinking about starting the company and it has just been really instrumental in making sure that we're a good business. And there is Adnan, our hardware lead that came over from Android. And Adnan has a really difficult job because if you want to work on cross embodiment, you remember my joke about how if you want to add two years to your grad school, you have to work on cross embodiment, you have to bring on one more robots. The hardware problem and the operational problem for us is how do we build, improve and scale a fleet of heterogeneous robot.

> 而 Google 的机器人团队,我觉得是一个非常非常好的环境,让我们看到了"生命的迹象",也在社区里建立起了让机器人社区和这些进展得以蓬勃发展的关系。有 Lachy(Locky),我们在考虑创办公司时认识了他,他在确保我们是一门好生意这件事上发挥了极为关键的作用。还有 Adnan,我们的硬件负责人,是从 Android 团队过来的。Adnan 的活儿非常难,因为你要想搞跨形态——你还记得我那个玩笑吧,想给研究生生涯再加两年,就去搞跨形态,你得再多带一台机器人。对我们来说,硬件问题和运营问题是:我们如何构建、改进并规模化一支异构机器人的机队。

`[40:07]` **SPEAKER_00:** It's just not one robot platform. And because we built the organization from scratch in the beginning to support that, I think we're able to do it, but it's just a really hard problem because there's just like no two different robots in the fleet. How do you make sure everything runs smoothly? We're really good at divide and conquer, if you ask. How many co-founders

> 它绝不是单一的机器人平台。正因为我们一开始就从零搭建了组织来支撑这一点,我觉得我们才做得到,但这仍是个非常难的问题,因为机队里就没有两台一样的机器人。你如何确保一切顺畅运转?如果你问的话,我们非常擅长"分而治之"。

`[40:31]` **SPEAKER_03:** are there in total?

> 总共有多少位联合创始人?

`[40:32]` **SPEAKER_00:** We have Brian, we have Chelsea, Sergey, myself, Lucky and Adnan.

> 我们有 Brian、Chelsea、Sergey、我本人、Lachy(Lucky)和 Adnan。

`[40:37]` **SPEAKER_03:** Is it just necessary to have that many co-founders to solve a problem as big as this? Or was it a case like you were already sort of like a unit together, you'd already worked together and you just, whatever you started,

> 要解决这么大的一个问题,是否必须有这么多位联合创始人?还是说情况是这样:你们本来就已经像一个整体、一支队伍了,你们此前已经合作过,不管开始做什么,你们都会一起——

`[40:48]` **SPEAKER_00:** you would all have Yeah, one common question that we have is, you know, why band together? And, you know, the first is that we really enjoy each other company. We spend a lot of time at work and it's, you know, in some sense give meaning to life. And so we really want to enjoy the relationship we have at work. And the second is that, you know, any one of us could have started a company and be successful.

> 是的,我们常被问到的一个问题是:为什么要抱团在一起?第一,我们真的很享受彼此的陪伴。我们在工作上花很多时间,某种意义上,它赋予了生活以意义。所以我们真心希望能享受我们在工作中建立的关系。第二,我们中的任何一个人,其实都可以自己去创办一家公司并取得成功。

`[41:12]` **SPEAKER_00:** But the problem is just so incredibly hard. And the chances of success is just so much higher that we band together and we can divide and conquer the problems. And, you know, that's the, I think, the main reason why the progress has been much faster than we expected. What were the differences

> 但这个问题实在难得离谱。而如果我们抱团、能够分而治之地攻克这些问题,成功的几率就会高得多。我想,这正是进展比我们预期快得多的主要原因。

`[41:30]` **SPEAKER_02:** of you working before in either academia or a big industry, big company like Google as opposed to now in a startup? This is the first time for a lot of you doing a startup, right? Yeah, this is the first time for a lot of us. One of the really surprising thing that we learned when we started the company is that

> 相比你以前在学术界、或在像 Google 这样的大公司、大产业里工作,如今身处一家创业公司,有哪些不同?你们中很多人这是第一次创业,对吧?

`[41:46]` **SPEAKER_00:** the infrastructure for a startup is not the same as the infrastructure for a company. You know, the infrastructure for a company is the infrastructure for supporting large-scale general-purpose robot, which is not there. And, you know, this starts from the software itself. How do you collect data? What device do you use to collect data?

> 是的,对我们很多人来说这是第一次。我们创办公司时学到的一件非常出人意料的事情是:创业公司所需的基础设施,和成熟公司所需的基础设施并不一样。你知道,那种(支撑大规模通用机器人的)基础设施根本就不存在。而这要从软件本身说起。你如何收集数据?你用什么设备来收集数据?

`[42:05]` **SPEAKER_00:** How do you manage the data? How do you annotate the data? How do you get visibility into the data? How do you run evaluation? How do you build operational process?

> 你如何管理数据?你如何标注数据?你如何获得对数据的可见性(洞察)?你如何运行评测?你如何构建运营流程?

`[42:13]` **SPEAKER_00:** Like, there wasn't a company that offered this kind of services, which is very different from software. And we were really surprised to find out. And so, we ended up writing a lot of the software at Pi ourselves. But I think this is another area of incredible opportunity of kind of building services for a robot company. Like, you know, if you can offer remote telehealth, for example, if you can offer data collections, if you can offer annotation service.

> 就是说,当时并没有一家公司提供这类服务,这和软件领域非常不同。我们惊讶地发现了这一点。于是我们最终在 Pi 自己写了大量软件。但我认为,这是另一个蕴含巨大机会的领域——为机器人公司构建各种服务。比如,你能提供远程(遥操作)运维、你能提供数据收集、你能提供标注服务。

`[42:40]` **SPEAKER_00:** Because, you know, these are functions that doesn't need to be repeated from one company to the next. So I think there's lots of opportunity to build kind of support for growing robotic business. So that's one thing, and the second is I think one of the reasons why we have managed to achieve such progress is that there is a really tight loop of collaboration in the entire life cycle of model development. Going from what task do you collect data for? You collect data for the task.

> 因为这些是不需要从一家公司到另一家公司重复造轮子的功能。所以我认为,为成长中的机器人企业构建配套支持,存在大量机会。这是其一。其二,我认为我们之所以能取得如此进展,原因之一是在整个模型研发生命周期中存在一个非常紧密的协作闭环。从"你为哪个任务收集数据"开始?你为该任务收集数据。

`[43:13]` **SPEAKER_00:** How do you do it? What hardware do you use? Once after you collect the data, how do you get visibility? How do you ensure data quality? How do you then make sure that after you train on that, how do you run evaluation?

> 你怎么做?你用什么硬件?一旦收集完数据,你如何获得可见性(洞察)?你如何确保数据质量?然后你如何确保——在用这些数据训练之后——你如何运行评测?

`[43:26]` **SPEAKER_00:** Evaluation is a really hard problem in robotic because it scales super linearly to model capability. Let's say you have a model that can perform a two-minute task. Running evaluation for that is very different from running evaluation for a task that's 20 minutes. It's not 10 times harder. It's more than 10 times harder.

> 评测在机器人领域是一个非常难的问题,因为它相对于模型能力是"超线性"增长的。假设你有一个能完成两分钟任务的模型,为它运行评测,和为一个 20 分钟的任务运行评测,是非常不同的。它不是难 10 倍,而是难上不止 10 倍。

`[43:44]` **SPEAKER_00:** After you run evaluation, how do you can distill the learning from that evaluation to know how to improve the model further? One of the really side projects I would love to take on is to build an automated robotic research scientist, which is really one of the bottlenecks we have today because this is a really difficult skill set that requires intuition about the entire stack. I would love it if there is a model that can ingest multi-model data such as this and analyze filler modes, understanding is the robot performing this way because of the data that was collected and the way that it was annotated and the way that we train the model and then suggest ideas and actually try them to figure out if those hypotheses are correct. That's something that I would love to have and would dramatically unlock us. Sometimes I make the joke in the company that we should record all of the meetings and then train a model to basically just make prediction about what is

> 运行完评测之后,你如何从那次评测中提炼出经验,从而知道该如何进一步改进模型?我非常想做的一个"副项目",就是打造一个自动化的机器人研究科学家。这其实是我们今天面临的瓶颈之一,因为这是一套非常难的技能组合,需要对整个技术栈都有直觉。如果有一个模型,能够吸收像这样的多模态数据,分析失败模式(failure modes),弄清楚"机器人之所以这样表现,是因为所收集的数据、以及它被标注的方式、以及我们训练模型的方式",然后提出想法、并真的去尝试这些想法,以判断这些假设是否正确——那我会非常想拥有它,它将极大地为我们解锁潜力。我有时在公司开玩笑说,我们应该把所有会议都录下来,然后训练一个模型,让它基本上就来预测——

`[44:44]` **SPEAKER_01:** the next sets of experiments. You could. You totally could. What if it's OpenClaw and Obsidian and Markdown files and a brain.md with ontology that's custom to your use case and what if it's a hundred OpenClaws in the background that you orchestrate?

> ——下一批实验会是什么。你可以的。你完全可以。要是它是 OpenClaw(Claude)加 Obsidian 加 Markdown 文件,再加一个包含为你用例定制本体(ontology)的 brain.md 呢?再要是它是你在后台编排的一百个 OpenClaw 呢?

`[44:59]` **SPEAKER_01:** I think there's

> 我觉得这里有——

`[45:00]` **SPEAKER_00:** two sides to this. The first is that we already see a little bit of a sigh of life where for simple filler modes during evaluation if you can describe the way that the robot fill in text very precisely and very clearly then you know you can ask the language model to make very reasonable recommendation about what the next step is. But the flip side is that this only works for simple cases today and the reason why that's the case is because I think it's pretty fundamental limitation of the model that we have today which is that they are not at the core model that take action in the world and see the consequences of its own action especially action that changes the physical world. And so I think this kind of very fundamental understanding about how the physical world works is missing from the really large foundation model and I think that's one of the ingredient that's missing to be able to build this automated robot research scientist. What's interesting

> ——这有两面。第一面是,我们已经看到了一点"生命的迹象":对于评测中简单的失败模式,如果你能非常精确、非常清晰地描述机器人失败的方式,那么你就可以让语言模型对下一步该怎么做给出非常合理的建议。但另一面是,这今天只对简单情形有效。之所以如此,我认为是因为我们今天拥有的模型有一个相当根本的局限:它们的核心并不是"在世界中采取行动、并看到自己行动之后果"的模型,尤其是那些改变物理世界的行动。因此我认为,这种关于"物理世界如何运作"的非常根本的理解,是那些真正大型的基座模型所缺失的。我认为这正是要打造这个自动化机器人研究科学家所缺的原料之一。

`[46:00]` **SPEAKER_01:** about OpenClaw I don't know I mean basically it can go and it can just do things which is interesting and then at that point it's on the research lab to provide like you know CLI MCP endpoints to the things that might control robots or reconfigure rooms or I mean I think Karpathy he's starting to talk a bunch about this where you know if you mix auto research plus what he's been talking about with markdown files like it might just happen in the open like you know there's a sort of sense that you have to make something much much more complicated to make it work but what if that's just wrong what if we just have markdown files and agents and you know you could make it yourself it's just literally an integration challenge

> 关于 OpenClaw 有意思的是,我说不好——我是说,基本上它可以去、然后就直接把事情做了,这很有意思。到那个时候,就轮到研究实验室来提供——比如 CLI、MCP 端点——去连接那些可能控制机器人、或重新布置房间的东西。我是说,我觉得 Karpathy 最近开始大谈这个:如果你把"自动化研究"加上他一直在讲的 markdown 文件那套结合起来,它也许就这么在开放环境里发生了。有一种感觉是,你得把某样东西搞得复杂得多才能让它奏效,但要是这想法就是错的呢?要是我们只需要 markdown 文件和智能体呢?你自己就能造出来,这实实在在只是一个集成的挑战。

`[46:54]` **SPEAKER_00:** we have a version of this internally that I use a lot there was a point when I was spending a embarrassingly large amount of money on API queries yeah and you know my team was like

> 我们内部有一个这样的版本,我经常用。曾有一段时间,我在 API 查询上花了多到令人难堪的一大笔钱。是的,然后我的团队就说——

`[47:09]` **SPEAKER_01:** Kwon what are you doing oh I'm that guy

> ——"Quan,你在干什么啊?"哦,我就是那种人。

`[47:11]` **SPEAKER_00:** at Y Combinator right now so to give you an example we have a cloud skill that's essentially serving the role of a pre-training on call today so you know we have these pre-training runs that are really large it's very I think a difficult exercise to keep them alive to you know for them to continue to churn just because there's so many things that can go wrong and we have a prototype a pre-training on call that kind of babysit the run and have the permission to take action to remedy error that it see and one of the surprising outcome of that exercise is that we have 50% improvement in compute usage like just overall compute utilization for that large pre-training run which is huge for us and you know this is just a small simple prototype that I built and I think

> ——就在此刻,在 Y Combinator 这里。举个例子:我们有一个 Claude 技能(cloud skill),它如今基本上扮演着"预训练值班工程师(pre-training on-call)"的角色。你知道,我们有这些规模非常大的预训练任务,要让它们"活着"、让它们持续运转,我认为是一件非常困难的事,因为可能出错的地方实在太多了。我们做了一个原型——一个预训练值班助手,它会照看这些运行,并且有权限采取行动去修复它所发现的错误。这次尝试一个出人意料的结果是:我们在算力使用上提升了 50%,就是那次大型预训练运行的整体算力利用率,这对我们来说是巨大的。而你知道,这只是我搭的一个简单的小原型,我觉得——

`[48:06]` **SPEAKER_01:** like there's a lot more to be done Kwon this is incredible thank you so much for everything thank you for making physical intelligence thank you for showing us these incredible demos and honestly like the thing that gives me the most hope is that you know we have a research lab out there that is focused on giving this to the world you know about to create this Cambrian explosion of robotic startups so someone watching right now will be inspired by this and you know start playing

> ——还有太多事情可以做了。Quan,这太不可思议了。非常感谢你所做的一切,谢谢你打造了 Physical Intelligence,谢谢你给我们展示了这些令人惊叹的演示。老实说,最让我充满希望的一点是:我们有这样一家研究实验室,专注于把这些成果交给全世界,即将催生这场机器人创业公司的"寒武纪大爆发"。所以此刻正在观看的某个人会受到这番话的启发,开始动手把玩——

`[48:40]` **SPEAKER_00:** with your models and they might create a robot that touches billions of people's lives in for the good the cost of building in robotic has decreased and I think will continue to dramatically decrease and it also requires a very different kind of scrappy skill set that young startup like needs we hope to enable really an explosion of many many many different robotic use case and you know

> ——你们的模型,他们也许会造出一个机器人,以向善的方式触及数十亿人的生活。机器人领域的构建成本已经下降,而且我认为还会继续大幅下降。它也需要一种非常不同的、精打细算、因陋就简的技能组合——正是年轻创业公司所需要的那种。我们希望真正促成许许多多不同机器人用例的大爆发。

`[49:12]` **SPEAKER_01:** always reach out to us

> 随时联系我们。

`[49:13]` **SPEAKER_00:** if you want to collaborate

> 如果你想合作的话。

`[49:14]` **SPEAKER_?:** thanks man thank you thank you

> 谢谢你,老兄,谢谢,谢谢。
