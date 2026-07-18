# 全文转录 · 前沿模型是怎么练出来的:Anthropic 预训练负责人谈扩展定律、算力与 AI 的未来

> ▶ [YouTube](https://www.youtube.com/watch?v=YFeb3yAxtjE) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/YFeb3yAxtjE.md) &nbsp;·&nbsp; Anthropic Head of Pretraining on Scaling Laws, Compute, and the Future of AI
>
> 🗣️ 说话人分离识别到 **2** 位发言者(标注为 SPEAKER_00 …)。

`[00:05]` **SPEAKER_00:** Hey guys, I'm thrilled to be joined today by Nick Joseph, the head of pre-training at Anthropic. To give viewers a high-level sense of what we'll be covering, we're going to start with the basics of what pre-training is, and then dig into how Nick thinks about strategy, data, alignment, and infrastructure at Anthropic. And by the end, you'll hopefully have a sense for how progress in AI comes directly from advances in pre-training. I would love to talk a little bit about your backstory and kind of how you got to this point.

`[00:26]` **SPEAKER_00:** Where did you work before Anthropic, and what were your takeaways from those places?

`[00:29]` **SPEAKER_01:** Yeah, so let's see, I was at Vicarious, and then at OpenAI before Anthropic. So Vicarious was originally an AGI lab, and when I joined, they were making a shift to product, particularly working on robotics products. And the thing I worked on was training computer vision models for their robotics products. It was my first job, so I think I just learned a ton about how to do machine learning models, how to write machine learning infrastructure.

`[00:53]` **SPEAKER_00:** And at the time, were you also thinking about a career as an academic? At the time, a lot of people doing AI work were in PhDs. That's kind of what I was thinking about before I started to do a company. How were you thinking about that in your headspace?

`[01:03]` **SPEAKER_01:** Yeah. So, like, I'm actually... Actually, we went a little bit. I think, like, a lot of my thinking on this had come from an internship I did at GiveWell, which is, like, a nonprofit that evaluates charities. And some people there being like, ah, at some point, we might have AGI. It could be dangerous. We should worry about these risks. This could be, like, a big impact on humanity. And I was, like, not super convinced at the time and went down the economics route and was going to try to work on, like, directly helping people in poverty.

`[01:24]` **SPEAKER_01:** That didn't work out for various reasons and ended up being like, okay, I'll at least work on AI. Either, like, the safety thing will turn out to be important, and I'll work on that, or it won't be, and I'll just make cool things with AI. It'll probably help people in poverty more. I wasn't really coming at it from an academic standpoint. I was sort of, like, in fact, when I switched to that, it was part of the appeal was that I could, like, immediately go do stuff in AI, whereas if I wanted to work in, like, economic policy, I'd have to wait, I don't know,

`[01:48]` **SPEAKER_01:** six years to do a PhD and then start. And, like, it's a longer path.

`[01:53]` **SPEAKER_00:** And what did the state of AI safety work at that time even look like? Like, who were the people who were thinking about that kind of stuff? I mean, there were some folks at Vicarious thinking about this kind of thing, but it was fundamentally a robotics company. And so, yeah, how were you thinking about that at the time?

`[02:05]` **SPEAKER_01:** Yeah, so my sense was, like, at the time, a lot of the AI safety discussion was kind of theoretical. Like, the models weren't actually that good. They weren't really posing these dangers. So it was a lot more, like, philosophical. It was like, oh, at some point, we might get AI that's really smarter than humans. And, like, should we wait this, like, future concern? How should we compare that to nearer-term things? And I think that was, like, actually just a less compelling argument. I think it was, like, an interesting one and, like, sort of made you think a bit.

`[02:29]` **SPEAKER_00:** So next you went to OpenAI. What was OpenAI like at this time?

`[02:32]` **SPEAKER_01:** Yeah, so I was at OpenAI. I was on one of the safety teams. Yeah. And kind of worked on, I ended up working on code models, actually. Cool, nice. And kind of, when I got there, the first thing I saw was, oh, they'd fine-tuned GPT-3 to write some code. But I add, it was really good. And I was like, oh, okay. If you're worried about AI getting really powerful, writing its own code, that seems like it could self-improve. And how likely is that to happen? So I was doing a bunch of evaluations and, like, studies of what contributed.

`[02:59]` **SPEAKER_01:** And then after, like, eight months, basically everyone I worked with, like, all of them, I was like, oh, I'm going to do this. All the safety leads left, which, yeah, invited me to go to Anthropic. And that was sort of the reason I joined OpenAI, was because I cared about AI safety and wanted to work with them. So then I went with them to join Anthropic pretty much right when it started.

`[03:17]` **SPEAKER_00:** With that, why don't we transition a bit? These days you run the pre-training team specifically at Anthropic. Obviously, you've been working on pre-training at Anthropic for quite a bit of time. And I'm sure it's evolved over the years, what that even entails and looks like. Why don't we start by just talking a little bit about what pre-training is? Like, how does it even fit into the way of thinking about, how AI models have developed at a place like Anthropic? And what exactly do you guys do?

`[03:38]` **SPEAKER_01:** We know that one of the ingredients to making AI models better is scale. You want to put a lot of compute in. And if you sort of step back and you're like, okay, what's the way we could put the most compute into a model possible? We need some objective that there's just, like, tons of data for. And one idea here is, like, the internet. The internet is massive. It's probably the biggest, like, single source of data that's created. And you don't have labels. It's like, you don't want someone to have to go in and look,

`[04:00]` **SPEAKER_01:** read the entire internet and, like, say something about it. So you want to get labels out of the data. And the idea here is we can take some text and we can predict the next word. So you take, you know, the as the first word, you predict the second word. Then you say the cat, you predict the word after that. And this means you get very dense signal. Every word is like a new example. And there's a huge amount of data. And one of the findings from my GPT-1, GPT-2 was kind of, as you throw more compute at this, more data, bigger models,

`[04:28]` **SPEAKER_01:** you get better, you get smarter models, essentially. Totally. And that's kind of been the central thesis of pre-training for me. I've been doing this forever, the whole time. There's this idea of scaling laws, which is that you can actually quantify, like, as you put in more compute, more data, more parameters, you get models in a very, you get a lower loss, a better prediction of the next word in a very predictable way. And I think you can somewhat foresee from that original paper, and I think, like, Dario did foresee this.

`[04:51]` **SPEAKER_01:** I think many people did. But what's obvious was that once you have that, there's this positive feedback loop where you can train a model, you can use it to make something useful and sell that and get more money, use that to buy more compute, and then you just actually train it to make it a better model. And we've sort of run that cycle over and over again over the past five years or so.

`[05:10]` **SPEAKER_00:** Well, in thinking about that objective to begin, you know, I think the way I think about the state of pre-training is, yeah, it seems like this next word prediction, at least from the external standpoint, seems to be the dominant way pre-training happens. But if I rewind the clock to that era of 2017 to 2020 or 2021 and two even, there was all sorts of pre-training objectives people were considering, right? There was these BERT and BART models that were doing mass language modeling.

`[05:31]` **SPEAKER_00:** It seems like this GPT series of models doing, like, autoregressive modeling, as you're describing, this next word prediction, seems to be the dominant one that won out. Do you have any reflections on that time period? Like, were you guys trying all of them and kind of this one worked? Or is there some sort of first principles reason why this is, like, the right one that should have worked?

`[05:49]` **SPEAKER_01:** I think the answer is, like, it's mostly empirical. Like, in terms of how to think of these things, I'd be like, yeah, it's empirical. Just try them all, see what works. One big advantage for this autoregressive setup is that you can just sample from it to generate text afterwards in a fairly, like, straightforward way that comes straight out of that.

`[06:02]` **SPEAKER_00:** Like, it enables a product use. Yes, very nicely.

`[06:05]` **SPEAKER_01:** Like, one thing that you want is, like, just one characteristic of a setup is, like, a loss, whereas you drive down the loss. That actually is the thing you care about. And you can think of it as, like, if you got to perfect on language modeling, you now can, like, write text as a human. You can sort of imagine you put in the title of a paper, and it should spit out a novel paper. Whereas I think some of the other approaches don't quite have that flavor.

`[06:26]` **SPEAKER_00:** Yeah, totally. Yeah, and it makes sense that in terms of that loop you're describing of, you know, then release something that gets you revenue, and you can use that to buy more compute and iterate. This sort of gives you the most natural way to actually do that flow, because you can keep releasing new products and keep getting the revenue from that to invest in more compute and so on.

`[06:42]` **SPEAKER_01:** Yeah, it certainly gives you the most open-ended thing. You can imagine, you know, you, like, train something as a class. Like, you train some base thing, you fine-tune it for a bunch of particular tasks. One approach people would use, they would, like, do this big pre-training, and then they wouldn't just, like, open-endedly sample from it. You'd fine-tune it on, like, a hundred specific tasks. And that could work, too. I think that, like, the one sort of general intuition I have is, like,

`[07:00]` **SPEAKER_01:** compute is the thing that matters. Yeah. Yeah. Like, I think if you throw enough compute at any of these objectives, you're going to get something that's probably pretty good and can kind of be fine-tuned to other things. And it's surprising how little these details matter compared to throwing more compute at the problem.

`[07:14]` **SPEAKER_00:** When you think about actually throwing more compute at the problem, there's a whole bunch of axes by which you could throw compute at it, too, right? And if you have a specific model architecture you're training over, you can basically throw more data at that specific architecture. For a particular one, you could add more layers or make the models larger in it. You could do some kind of neural architecture search over lots of different variants. And I assume that these days it's somewhat more figured out, you know,

`[07:36]` **SPEAKER_00:** which architecture you go for. I assume the earlier days it was somewhat less so. And I'm curious if you could speak to how you guys thought about that. Like, what did your infrastructure even look like to do that type of determination?

`[07:46]` **SPEAKER_01:** I mean, I think the short answer is it's hard, right? Like, what you're really doing is you're going to train this one big expensive model and you have a space of, you know, you can sort of call all these things hyperparameters. You know, how many layers do you have, what you're with. Like, you have this space of hundreds of hyperparameters and you want them all to be optimal. Yeah. And you're sort of striking this balance. Actually, between how much do they matter? Like, can you just take your best guess and throw more compute at it

`[08:07]` **SPEAKER_01:** in whatever way you want versus how much you're letting at it precisely correct. Yeah, interesting. And I think one of the, like, interesting things is, like, it actually doesn't matter that much. Like, I think this was in one of the early scaling laws papers. Like, you can change these things and get little wins, but, like, as you throw more compute, it sort of reliably gets better. If you mess up enough, you will sort of stop seeing that happen and you won't have any way to know, which is one of the,

`[08:29]` **SPEAKER_01:** that's, like, kind of the hardest part in some ways.

`[08:31]` **SPEAKER_00:** You don't know the counterfactual. Basically, because you didn't run it for long enough to actually know what it is.

`[08:35]` **SPEAKER_01:** Yeah. We have these scaling laws. So you can sort of say, like, as you train them up more and more compute, you expect the loss to go down as a power law. It's really a power law plus constant. So what eventually will happen is you'll curve off that power law and then you know something is wrong. And is it fundamental? Is it, like, you've hit the limits of scaling? Or is it, nope, you should have changed, you should have tweaked your learning rate slightly differently. And that's sort of one of the challenges.

`[08:55]` **SPEAKER_01:** In terms of how to, like, figure it out, you can, the usual paradigm is, like, test things out at small scale before running them at large scale.

`[09:01]` **SPEAKER_00:** Mm-hmm. Small scale in terms of data or in terms of something else?

`[09:05]` **SPEAKER_01:** In terms of everything. Like, you kind of want to scale things down, like, proportionally. So you want to say, like, you want to have some theory for, like, how you're going to scale up. Like, ah, okay, if I get 10 times as many flops, how much of it goes into layers? How much of it goes into data? How much of it goes into attention? And you sort of get that theory and then test that it's optimal a bunch with, like, scaling everything down proportionally.

`[09:27]` **SPEAKER_00:** And just so I can think about what this actually looks like, in those early days of Anthropic, you know, you're a team of, like, 10 or something like that in those very early days, or 12 maybe. What actually is your ability to use large-scale infrastructure as, like, a relatively nimble startup at that time? I mean, a startup that was well-capitalized, but still not actually that many people working at. What kind of infrastructure did you have access to to train these early models at the time?

`[09:48]` **SPEAKER_01:** So that's actually one of the wild things was that at least, I mean, you don't know what anyone else is doing, of course, but it kind of felt like we were, like, at the frontier of it. And there just weren't that many people who cared. Like, I was sort of coming, you know, I was coming at it from, like, hey, this is the most important technology ever. And then we'd kind of, like, look around and be like, and it seems like I'm one of 30 people who are working on this in, like, the world.

`[10:08]` **SPEAKER_01:** I mean, I was kind of, like, junior person. Everyone else sort of knew how to do this and had done it before, but I was kind of surprised at how easy it was. Like, the public estimates for GP3, I remember, were that it cost $5 million to train, which you're, like, on the one hand, $5 million is kind of a lot, but it's, like, a lot for an individual person. It's not really a lot from, like, a company perspective. So we could totally buy, like, compute that was enough to train models like that.

`[10:33]` **SPEAKER_00:** And were you using a cloud provider, or did you have a custom setup somewhere, or did you literally have racks in a room somewhere that you bought a bunch of NVIDIA GPUs and you were doing it?

`[10:41]` **SPEAKER_01:** We were using a cloud provider, but I think it's kind of, it's not actually that different, because one of the things that was surprising to me is you actually have to understand the literal layout. Like, I remember at one point one of my coworkers running a clustering algorithm to identify what rooms all the chips were in, since we had a hypothesis that they were in different rooms, and that was causing, like, or, you know, different buildings. Some sort of, like, network latency. Some sort of network latency, and you can kind of figure it out.

`[11:05]` **SPEAKER_01:** You can, like, reverse engineer, like, ah, okay, yeah, there's clearly, like, two clusters here that are connected better, and there's some issue on the connection between them. Like, we're trying to push the limits of the hardware, like, as much as possible, particularly at the beginning when we were kind of, like, we have way less funding than everyone else. We have to, and most people weren't very efficient with the compute, so we were like, ah, we can get a big lead by being really efficient at how we use the compute.

`[11:26]` **SPEAKER_00:** Could you talk a little bit about some of the things you guys did in those early days for how to get the most out of the hardware? I think that's really interesting. Like, I think back to the days of, the early days of Google, for example, where there's these cases where they basically bought relatively cheap consumer chips, and then they optimized the software to make it so you can actually get the most bang for your buck out of them, and that's how they had all this high latency, or low latency, high availability stuff.

`[11:46]` **SPEAKER_00:** I'm kind of curious if there's some analog in the early AI era to that.

`[11:50]` **SPEAKER_01:** I think for us it was largely about, like, getting the distributed framework, right? So, like, we're training on, in order to train something else, you have to train them on a large number of chips, and there's a bunch of different approaches to how to do this. There's, like, data parallelism, there's pipelining, there's upsharding, and, like, getting all of this.

`[12:04]` **SPEAKER_00:** And at the time there were no, like, great open source packages you could just grab and use that just worked for this. I mean, today there's somewhat more of these, but at the time I assume there was literally none.

`[12:12]` **SPEAKER_01:** There were some. Like, I actually remember that we were kind of working on data parallelism early on, and someone was like, and now we write the all-reducing. And I was like, we really do this ourselves? We don't, like, call a package? And this was kind of like, well, we're going to want to modify it, right? Like, oh, like, we don't want to outsource this to some package because, A, we're about to go to a bigger scale, like, PyTorch, for instance, they had a package for doing this. But we were going to go to a bigger scale than Facebook had been, too.

`[12:35]` **SPEAKER_01:** And you don't want to have a dependency on a package that you're going to have to be, like, constantly modifying, essentially.

`[12:42]` **SPEAKER_00:** It's such a counterintuitive sentence there, too, like, we're going to a bigger scale than Facebook. Well, because at the time, Facebook AI research was considered one of the best places to do machine learning research. Like, FAIR was one of the places, FAIR and DeepMind were hiring lots of people out of top PhD programs and doing lots of things. Like, what was your headspace when you were like, okay, this very essential... We're an established lab with great people and whatnot. We are operating on a scale that is not relevant to them.

`[13:04]` **SPEAKER_00:** Like, was that natural and obvious to you? Or was there times where you kind of doubted the decisions you were making in that situation?

`[13:10]` **SPEAKER_01:** I think it was surprising. I will... Maybe I'm just too arrogant or something. I kind of looked around and was like, what are these people doing? They're all missing the, like, big picture here. Like, I think the scaling laws were pretty clear. Like, and the arguments against, I just thought, were kind of nonsensical. Like, I think the original scaling laws paper had, like, 11 orders of magnitude. And there was, like, this intense debate on whether it would continue for, like, another point.

`[13:32]` **SPEAKER_01:** And I was like... There's already 11. It seems like 1 over 11 is maybe your chance it fails here. And then, like, you know, sometimes it doesn't work. Like, sometimes it just works straightforward. You're like, well, let's change the model. And you're like, oh, yeah, of course. But, yeah, I do think that it was... It maybe felt obvious when you're in that headspace and you're working on this all the time and you're making those plots. And I think these things feel pretty different when you're on the outside.

`[13:53]` **SPEAKER_01:** You know, there's a huge space of papers. Everyone tries to make their paper sound, like, very robust and important. And I could see being like, oh, yeah, this is not really a thing. But also different labs have different cultures. So, like, I think one of the things at FAIR was it was a very more PhD-style, independent research. People have their own ideas, pursue those.

`[14:12]` **SPEAKER_00:** You're fighting for your compute and so on.

`[14:13]` **SPEAKER_01:** Yeah, and to do a project like training a large language model requires a lot of people to collaborate on, like, a really complicated piece of infrastructure that isn't going to be a paper, right? Like, you're not going to publish, like, oh, I got a slightly... I got 5% more efficiency than the next one. And it's not respected. And, like, that's... Those cultures, necessarily. So that might have been part of it.

`[14:31]` **SPEAKER_00:** Okay, so then when you actually implement these models, you're saying you're using a level of low-level programming where, you know, you're using libraries like PyTorch, but you're perhaps not using everything right out of the box from PyTorch because there's things you guys want to customize that are at the level of basically one level of abstraction below them. But not necessarily at the level of abstraction of, you know, writing custom CUDA kernels. Or, like, was that also in the space

`[14:52]` **SPEAKER_00:** where you guys were thinking about things? So it depends on, like, the operation.

`[14:53]` **SPEAKER_01:** So, like, I think I was mostly operating at the level of, like, Torch.matml. You know, like, ah, yes, where does a matml go? But not thinking, like, how do you make the matml efficient? Like, I assume Torch figured out how to make a matml as efficient as is possible. But there are some pieces, like attention, where there was just kind of a lot of different variants. And attention is really complicated and hard to make efficient on a GPU. And those things, you have to kind of go more levels down the stack.

`[15:19]` **SPEAKER_01:** I think there was, like, a process that is maybe interesting that I'd never really, like, thought of before of, like, how to do it, which is sort of, like, modeling out the problem, the thing you're going to do, coming up with a strategy for how to parallelize it that, like, you're going to be able to do that, like, can get to a really good efficiency. You know, like...

`[15:32]` **SPEAKER_00:** So you're thinking about MFU, basically, like, your utilization on your GPU. So there's, like, a goal utilization you're trying to get at and a strategy to get to there, you're saying.

`[15:39]` **SPEAKER_01:** Yeah, and I think, like, one of the things you can do is you can actually, like, pencil and paper math out what efficiency you're going to be able to get to, right? You know all the constraints. MFU is Flop's utilization. But, like, the reason you don't get good MFU is you end up limited on HBM bandwidth. You end up limited on, I don't know, host to, like, CPU offload. There's a bunch of different pieces. But there's not that many pieces. There's, like, six relevant numbers there. So you can totally model it out,

`[16:04]` **SPEAKER_01:** understand what the constraints are, and then implement something that can get there. It, of course, will be really inefficient when you implement it. And then the next step is, like, pulling out a profiler. So you want to be able to profile the job, look at how long every operation takes, have a model in your mind of how long every operation should take, and then make those two things the same.

`[16:22]` **SPEAKER_00:** And were there good out-of-the-box profilers you could use at that time? Or did you guys have, you know, because people weren't operating on the kind of network topologies you guys may have been using, did you have to write your own profilers, basically, to do this type of, you know, multi-node optimization?

`[16:34]` **SPEAKER_01:** Yeah, it depends when. I mean, they were actually getting better with time. The PyTorch profiler was, like, pretty good, actually, throughout for a single GPU. You want to, like, profile a GPU, the PyTorch profiler would work. But if you wanted to profile a job on hundreds, thousands of GPUs, that, like, hadn't really been done much. And then that was kind of more of us, like, hacking into the profiler to figure out how to combine all the traces together.

`[16:54]` **SPEAKER_00:** And then one more question on that earlier is, you know, you had mentioned, you know, you hadn't really done a lot of this work before, maybe, some time at OpenAI and those early days in Anthropic. How did you actually go learn all this stuff? Like, what was your process for learning about those six things that were relevant to bandwidth limitations and whatnot?

`[17:08]` **SPEAKER_01:** I mean, so when I joined Anthropic, one really nice thing was there just wasn't that much. I think my first day, I read through our entire, all of Slack. Right, you're like, cool, cut off. And the entire, like, internal database and learned a bunch from that. Like, it was kind of nice to just be like, everything is relevant to me. Yeah, totally. And then I mostly learned from pair programming. Like, Tom Brown had done all this before, so he kind of, like, knew all the stuff quite well. Sam McCandlish, my manager,

`[17:32]` **SPEAKER_01:** had also done a lot of it before and I just, like, paired with them a huge amount at the beginning. And I think one of the things I really like about pairing as a way of learning is you learn the, like, thing you're trying to do. Like, you will learn that. Like, if you're pairing with someone better than you, they can just do it, so you're mostly just watching them. But you also learn how people do it. So something like how to use a profiler is not something you would ever learn from seeing someone's, like,

`[17:52]` **SPEAKER_01:** final write-up on Slack for their PR. You would just be like, oh, they found these, they changed this specific line and it's a win. Yeah, like,

`[17:59]` **SPEAKER_00:** you need to watch, like, a YouTube video for four hours of someone messing around with a profiler to, like, maybe self-teach it or something or to actually pair with someone is basically the best you can do.

`[18:08]` **SPEAKER_01:** Yeah, I think there was, like, one thing that I think is embarrassing now that I look back is I'd never actually used a debugger before joining Anthropic. People talk about it at PDB of, like, yeah, that's a thing people use, but print seems fine for me. Yeah, sure, sure. Then I, like, watched them and was like, oh, no, a debugger is a super useful tool. This person's way faster at debugging things, particularly if it takes a long time to start up the code, which it can. And, yeah, learning that sort of thing,

`[18:30]` **SPEAKER_01:** I think, comes best from pairing. Yeah, totally. And then there's, of course, the obvious you just learn by doing. Yeah, I eventually did, like, spit a profile and stare at it for many, many hours.

`[18:38]` **SPEAKER_00:** Totally, yeah, exactly, yeah. Okay, so then, that was sort of the very early era. Over time, obviously, pre-training has become bigger and bigger. As you're describing scaling, I imagine you're using many X more GPUs, much more compute over time. I'd be really curious to hear, first, at a high level, what do you feel has changed about the pre-training strategy that you could talk about? Obviously, there's more compute, but what does that actually mean to have more compute? More compute in terms of

`[19:00]` **SPEAKER_00:** what you think about differently from those early days versus now.

`[19:03]` **SPEAKER_01:** I'm sure the things that haven't changed, because I think it is, like, shocking how the world has changed in some ways. I think I'm still pushing down the exact same metric that I was on, like, day one.

`[19:12]` **SPEAKER_00:** There's, like, some loss function. Loss go down.

`[19:14]` **SPEAKER_01:** And I think you could, like, look at some, like, you could probably run the first model I trained on the same metric and just, like, make a plot of, like, progressive team over time. So that's all the same. I think the biggest...

`[19:25]` **SPEAKER_00:** Like, one OKR is, like, one thing that matters, basically. Yeah, totally.

`[19:28]` **SPEAKER_01:** And, like, I mean, talking about, like, OKRs, it's a very size of the company. You're like, oh, should you do OKRs? And it's always felt a little bit funny for a team like FreeShare where I'm like, sure, I can just pick a loss value, but, like, the answer is, like, as low as possible and we will continue to work on that forever. I think the biggest things that have changed has been a little more specialization. Like, I think at the beginning, I mean, the first, like, three or six months I tried to read every PR

`[19:49]` **SPEAKER_01:** in the code base and that was great. I knew all the pieces, et cetera. And as you grow, it's kind of, everything gets, like, a little more precise, you know? People really dial in exactly how attention should work, let's say, or, you know, really dial in, like, the parallelism strategy. And you end up with a team where it's a bunch of people who are, like, deep experts on individual things, which is great because it means you can go, you can go really deep on those things, but sometimes you, at least for me as a manager,

`[20:15]` **SPEAKER_01:** one of the things you sometimes have to think about is, like, making sure the bigger picture makes sense. And also that you have enough people who actually do understand the whole bigger picture that there's no, like, single point of failure.

`[20:24]` **SPEAKER_00:** Yeah, it's interesting you frame it in that, with that, trade-off, right? Because as you were describing that, I was trying to think, you know, is this a bug or a feature? Like, there's some obvious features of it, which is you get expertise and you can optimize certain things, but I imagine your ability to take bigger swings becomes more complicated if not everyone's exactly pointed in the same direction. Like, how do you wrestle with that now?

`[20:44]` **SPEAKER_01:** Yeah, I think I mostly just try to get a balance of people. I think one of the challenges early on... Oh, of people. Oh, that's interesting. Yeah, like, I think people really do have a preference here has been one of the things I've seen. Like, there are people who really want to be a generalist and understand, understand everything and, like, lightly touch on things. There are people who want to, like, pick an area. Often they've already picked that area and they're, like, deep experts in precision.

`[21:03]` **SPEAKER_01:** You know, they did a whole PhD in precision and just want to think about that. And you want to get some balance of that. I think there was a phase where we'd hired a lot of people who were more generalist-shaped because that's what the people who joined early started for the work on everything and then you ended up with kind of everyone doing everything and no one really, really deeply understanding one thing. And that's one failure mode. But I think if you get too many people who are specialists, you end up,

`[21:26]` **SPEAKER_01:** a lot of effort has to come from the manager from, like, the lead to connect everything and to notice something like, ah, if we change the architecture here that would make this, like, efficiency consideration over there way easier. One of the things I really liked kind of, like, at the very beginning was, like, I was working on efficiency but I could just go and, like, be like, ah, well, what if we change the way we do, like, this particular step and we'll be like, oh, yeah, it's probably fine, like, easy change

`[21:50]` **SPEAKER_01:** and then, like, you can avoid this whole complicated project to make this operation that was hard efficient because you can make an easier operation

`[21:55]` **SPEAKER_00:** efficient. Okay, interesting, yeah. So as the level of compute has also gotten bigger, so I'm sure anyone can imagine, okay, there's more GPUs now, you have to network with them more. Are there some, like, kind of non-obvious challenges that have arisen over time where you guys have just, like, banged your head against the wall to solve them because of the amount of compute you're dealing with that people wouldn't otherwise know about that, like, you want to share?

`[22:17]` **SPEAKER_01:** I think that connecting them is one that's maybe interesting and, like, surprisingly hard because you really do get more and more chips connected and, like, one thing that I think is, like, the standard way people parallelize chips isn't, the whole thing is one failure domain. Like, one chip fails, the whole thing can crash.

`[22:34]` **SPEAKER_00:** The standard way as in the standard way people are doing AI or the standard way in other fields where people are doing GPU vehicle?

`[22:39]` **SPEAKER_01:** In AI, for, like, I mean, at least, like, I think at the beginning, you know, like, first versions of things were this way.

`[22:46]` **SPEAKER_00:** So it's like you have 100 GPU cluster or whatever, there's 128, like, if one of them dies, job fails, basically.

`[22:51]` **SPEAKER_01:** Yeah, I mean, you can think of the simplest thing as if you just, like, distribute your model. So say you put, like, every layer on a different chip and you lose, like, layer seven. Like, yeah, you're not going to, like, skip layer seven. I guess you could, but that's, like, a pretty weird model training process now. And, like, that leads to some interesting things, which is, like, okay, so now as you scale up, you have more and more chips and the failure rate can get, like, larger and larger. On the other hand,

`[23:14]` **SPEAKER_01:** you can, like, restart pretty quickly. There's nothing, like, you just have to, like, load back in some weights. So that was one thing. And then the other thing was, like, the level of novelty at the whole stack is something that's surprising. Like, basically, everything from, like, how the chips are laid out in the data center to the chips themselves is pretty new. There just haven't been that many generations of GPUs. I think one of the things that, I don't know, when I learned computer science,

`[23:38]` **SPEAKER_01:** my code wouldn't work and I'd be like, oh, the computer's broken. And I think my teacher was like, you can trust the computer's not broken. You messed up. And I think one of the most frustrating things I encountered in AI early on was working on something and being like, I don't know what I'm doing wrong. I'm just totally stumped. And my manager looked at it and was like, ah, yeah, probably the computer's wrong. And I was like, that seems unlikely. And sure enough, the computer was wrong. It turned out that, like,

`[24:01]` **SPEAKER_01:** the GPU was broken and we had to pull in a new one. But you have to, like, think, like, having to think about that. Like, the GPU could be wrong. The GPU could be slow. Like, these sorts of issues, the power supply in the data center could be broken. Like, there's so much more, like, level of depth than you, like, kind of expect to need as a Python programmer.

`[24:22]` **SPEAKER_00:** And just the vision to visualize it, like, in those early days, I assume you guys were using the number of GPUs, it's probably on the order of tens to hundreds or something like that per run. It's probably not tens of thousands or hundreds of thousands per run. What was the rough size you guys were at in those very early days? On the order of thousands? Like, would they fit in this room? Thousands. Yeah, thousands. So, like, you could have a bunch of racks and you could fit them into, like, one room.

`[24:40]` **SPEAKER_00:** I assume these days it's basically, like, a building for one of these runs.

`[24:43]` **SPEAKER_01:** Yeah, now I think it's, like, you know, huge campuses. At the time, it was, like, kind of unclear. It was like, oh, and, you know, we had these theoretical models. We'd be like, oh, we need this much bandwidth from point A to point B. But you, like, you never know how far down you have to go. Like, oh, but, like, how much power do we need? Like, what if there's, like, a single capacitor that's, like, handling all of them and we, like, turn on the whole job at once? Like, does that crash things? Totally, yeah.

`[25:08]` **SPEAKER_00:** And so do you have to think about differences in the different types of chips? I mean, you guys work with all sorts of cloud providers. From your standpoint, are these just sources of compute? Or if you guys are using TPU versus GPU, are these, like, you know, Google TPU versus NVIDIA GPU, do you actually have to think as an engineer differently about what it means to train on these two?

`[25:26]` **SPEAKER_01:** Yeah. So, I mean, fundamentally, they're all doing the same thing, right? They're all computing the same forms of matrix multiplications, et cetera. The way they do it is pretty different. And the way that you program them is pretty different. And then, also, the actual specs end up pretty different. You know, some might have, like, a lot of flops and not very much memory. Or they might have a lot of memory bandwidth but not very much memory. So I think a lot of having multiple chips is, like, great in some ways.

`[25:52]` **SPEAKER_01:** It means you can actually, like, take the job and put it on the chip that it works best on. And that's... Well, like,

`[25:56]` **SPEAKER_00:** are there certain types of jobs that would work better on, like, a TPU cluster versus an NVIDIA GPU cluster? Like, how would you... Oh, yeah, for sure. Oh, interesting. Can you talk about that?

`[26:05]` **SPEAKER_01:** Yeah, I think, like, one example is, like, inference as a workload in general tends to require more HBM bandwidth. You end up doing sort of the simplest form of sampling since you're going one at a time. You have to load all the weights for every token. And that means you might want a lot of HBM bandwidth. And pre-training, actually, is often more flops-intensive because you have larger batch sizes, essentially. So, yeah, so you can sort of specialize which chips you use for which purposes. The downside of having

`[26:29]` **SPEAKER_01:** multiple chips is that you have to write the thing multiple times. In theory, you could have abstractions across them, but they're different enough that it's pretty hard to do that. So you can sort of end up... If you do all the workloads on all the chips, you end up multiplying your work by the number of chips you have.

`[26:43]` **SPEAKER_00:** Yeah, on your point about sometimes the computer just breaks, I definitely remember you giving me an anecdote of my company at the time. I was doing something with Google TPUs and I was telling you some anecdote about how we were having some esoteric segfault error and you were like, you told me something to the effect of, you should have used them six months ago before we helped them fix half of the problems they had on those TPUs. And so I can imagine how you guys deal with a lot of, especially with these

`[27:04]` **SPEAKER_00:** very new chips, lots of problems that arise that you guys kind of worked closely with the providers to fix.

`[27:09]` **SPEAKER_01:** Yeah, the providers are pretty great about fixing things. I think it's interesting to figure out the right way to do that form of collaboration because they have a strong incentive to fix them. They want the chips to work well for us. They want to sell us more chips in the future. We obviously have a very strong incentive for the chips to work because we buy them long in advance. Everything's riding on getting these clusters to work. Totally. But we don't have necessarily totally shared, all information

`[27:31]` **SPEAKER_01:** can't be shared across. So yeah, one strategy that's made is making these small-scale reproducers. So when you get a problem, usually what we're doing is we're training some giant run and we get a segfault from USA and we're like, ah, okay, hi, we got a segfault on your cluster and they're like, I don't know how to fix it. So you have to be able to pull it out of your code base and be able to reproduce the issue but on a single chip, on a single file you can send over in order for...

`[27:56]` **SPEAKER_00:** And so you guys are literally, you're on a shared Slack with them or something and you're sending them things back and forth or are they basically living in your office and you're living in their offices and more closely tied to the big providers?

`[28:07]` **SPEAKER_01:** Mostly shared Slack. Occasionally, it's better to meet in person, but I think Slack is a pretty common way people communicate on things. Nice.

`[28:13]` **SPEAKER_00:** Okay, well, why don't we talk a little bit about how you think about the state of pre-training itself these days. In the last couple of years it seems like the focus on pre-training has now gone somewhat split at a lot of companies at least from the outside from a simultaneous focus on pre-training and post-training where people are doing reinforcement learning or clever fine-tuning and lots of other safety adjustments and whatnot on the post-training side and pre-training has focused at least it seems like

`[28:36]` **SPEAKER_00:** in the public imagination has been less of a focus compared to these reasoning style models that looks like a function mostly of post-training. I would say, one, from your standpoint, is that the right way to think about this or in the... in this era of kind of reasoning and new types of post-training methods are the things you think about differently or that are relevant even at pre-training that become part of how you actually achieve these really great models.

`[28:58]` **SPEAKER_01:** Yeah. So I think, yeah, there sort of used to be this idea of like... I mean, it's funny because the original name pre-training implies that like it's a small thing and you're going to do this big training thing and that like... There was actually one shift already which was like, no, you just do a lot of pre-training. You use most of your computer on pre-training with sort of the dominant thing for a while and yeah, I think like now people are like, oh no, you can get pretty big wins from RL. You sort of have

`[29:20]` **SPEAKER_01:** another set of scaling laws is like you put more and more compute into RL, you can get better and better models out of that. And yeah, so there's a question of like how do you balance those two? How much do you do of each? And how do they stack, right? Like is it the case that like one subsumes the other, that you want to do both and they multiply? Those sorts of questions. I think those are all in kind of like early stages and not yet answered. Yeah.

`[29:40]` **SPEAKER_00:** And do you think about those as largely empirical questions like we talked about earlier? Is it you kind of will try a bunch of things and see what works or is it like or is there some first principles way to kind of figure that out?

`[29:50]` **SPEAKER_01:** I think it's pretty empirical in the end. I think almost everything kind of has to be done empirically. Like you can kind of like come up with theories but in practice, like the first thing you're going to do with your theory is test it and most of the time you'll have gotten it wrong. So you should just gather data and see. I think one thing that's important is like actually resolving things empirically is really like critical for making good decisions. And I think it's actually pretty hard to do

`[30:14]` **SPEAKER_01:** at organizations. You know, like one thing that I think is really I think it's important is to like not have like, I don't know, I managed pre-training. I shouldn't be like, oh, pre-training has to win. Right, yeah. I was going to ask,

`[30:24]` **SPEAKER_00:** is there some competition to some degree between these two sides of the org or do they see themselves as two pieces of the same? I mean, obviously they are the same thing but yeah, I'm kind of curious how that actually plays out.

`[30:34]` **SPEAKER_01:** Yeah, I think we managed to avoid this and it's pretty collaborative. Like we're basically all producing one model and kind of can but I do think at other places there's been some of, from what I've heard, there's been some amount of like friction between the teams and I think it's an interesting like org design question of like how do you set this up so you don't have like scientific questions that you want to be, that are sort of also tied to people's like conception of their team.

`[30:58]` **SPEAKER_00:** So on pre-training itself, you know, one of the things I think about is, or I've been thinking about is around the availability of high quality data for people like you guys. I mean, at this point you've trained on, I assume all the techs on the internet basically. There's all sorts of other domains where you probably could extract more pre-training data but at least there's this narrative I see, you know, on Twitter or whatever where it's like, okay, we're kind of out of data for pre-training. Is that how you see it

`[31:17]` **SPEAKER_00:** or how do you think about the availability of data especially when a lot of data on the internet is being generated by AI? Like is there some kind of, you know, mode collapse risk where, you know, we kind of, we overfit to data by training it on data that came out of AI itself or is that sort of not the right way to think about this?

`[31:33]` **SPEAKER_01:** I don't think there's a funny thing where I feel like on data I see so many really confident takes on we're out of internet, like at this point scaling has ended and I'm almost a little bit like unsure exactly how much, what data people are using. I think there's like a lot to think about there. You know, there's always going to be a quality quantity trade-off, et cetera. But there's a fundamental point that like there is so much data. It's growing at a slower rate than we're getting more compute.

`[31:58]` **SPEAKER_00:** Oh, so is that, okay, that's an interesting point in itself I was going to ask. Like there is new data being added to the internet but yeah, you're also adding more compute. It's not, it wouldn't actually have been obvious to me which of those two is growing faster.

`[32:07]` **SPEAKER_01:** Yeah, and actually I want to caveat that.

`[32:09]` **SPEAKER_00:** I don't think I want to

`[32:09]` **SPEAKER_01:** state that so confidently. I'm not totally sure. Like how would you know? I mean, one thing that I think is interesting is if you ask someone how big is the internet? The answer is infinite. There are many pages where you can scroll and it will auto-generate more text as you go forever. So the internet's like infinite. And then it's like, okay, how big is like the useful internet? And then there's the thing of no one knows. Okay, interesting. There isn't, it's not like when you make a web page you like add it to

`[32:34]` **SPEAKER_01:** some giant counter and like say, I've added 50 words to the internet today. Sure, sure, yeah. So there is a lot of uncertainty on that angle.

`[32:41]` **SPEAKER_00:** Well, like to be fair, like my kind of simplistic CS brain would be like, well, you just, you know, do page rank on the internet and everything would page rank above some threshold that's considered the useful internet. And like that's kind of good enough. Like is that kind of not good enough for finding the useful internet?

`[32:55]` **SPEAKER_01:** I think not. I think the useful internet is pretty different from a model, from a person perspective if that makes sense. Like I think there are plenty of things that like might not be worth you ever reading and would get to. I actually don't know page rank super well. I think page rank is mostly like how much people clicked it.

`[33:09]` **SPEAKER_00:** It's like the linked-based system, right? It's like the original Google algorithm of like links and like which links get touched the most basically.

`[33:15]` **SPEAKER_01:** Yeah. I think it's like it's a quality metric. It's not obvious to me that it's the right quality metric for AI.

`[33:22]` **SPEAKER_00:** Right. Like mark of chain over links doesn't necessarily mean that there's not useful data there. It just might mean that nothing is linked to it. Yeah. And yeah, okay, interesting.

`[33:29]` **SPEAKER_01:** And it might be that like that data ends up more valuable because everything that's linked to a lot you've already got. Like at some point you're maybe like going for the tails or you're going for the stuff that no one's ever, like, you know, it's only been linked in one place but it's, it's the, it's this like useful little nugget of knowledge that's going to help with like, you know, the last 10% of hard queries. The other thing you asked about was synthetic data. Yeah. And I think that one's like pretty interesting

`[33:52]` **SPEAKER_01:** to think about. I think there's a few different ways you can think about it. Like one is sort of this like more distillation type approach where you can, you can take a smart model, you can generate a bunch of data from it and you can train on that data and you can probably get some model that will like kind of approach the intelligence of that.

`[34:06]` **SPEAKER_00:** And we see this with a lot of the open source models, right? We see like the Quen smaller reasoning models distill a lot of the larger Quen models, for example, and similar with DeepSeq, for example.

`[34:14]` **SPEAKER_01:** Yeah. So you can totally do that. Then there's a separate question of like, can you use your current models to train a model that's better? And I think there's like an interesting thing here, which is like, if you generate the model data for the models, you know, if I go to Claude and I'm like, write me some great text and I look at it and I look at like the average content on the internet, it looks pretty good. But on the other hand, I know that if I just train it, just generate, you know, please write me

`[34:39]` **SPEAKER_01:** as much text as possible. Yeah. Theoretically, I shouldn't be able to train a better model than that. Like, I'm just going to get the same thing out. So I think that's...

`[34:48]` **SPEAKER_00:** Presumably, yeah. And specifically, that's because like your next token prediction on that should have very little loss for anything that's coming out of your model, right? That's like the basic reason why that you would expect that to not work that well.

`[34:56]` **SPEAKER_01:** It's mostly just because like there's some distribution, the model has some distribution and you're going to learn to model that exact distribution. Yeah, exactly. Yeah. But if that distribution is wrong, you're not going to learn the truth. If that distribution says like... You can imagine if the model thinks 5 plus 5 is 11. Yeah. Every time you see the string 5 plus 5, it's going to put out 11. Yeah. And your new model is going to learn that 5 plus 5 is 11. Yeah, totally. Yeah. So I think that's like kind of an

`[35:17]` **SPEAKER_01:** interesting area of research. It's one that's really hard to research because you have this problem. As I said, like one of the paradigms is you study things at small scale and then you run them at large scale. And if your plan is like, oh, we have a bunch of data from our best model, how do you test that by training a better model? So that's like kind of what you're doing intentionally if you're trying to like use it to make a better model. There's a separate thing of like what about accidentally, like as you said,

`[35:41]` **SPEAKER_01:** a lot of the internet is generated by LLMs. And I think that's kind of an interesting one because it's not easy to detect. It's not that hard to detect. You can figure out things that are written by LLMs, but it's not trivial. And then it's also kind of hard to think about what's the effect. Like if 1% of the internet is LLM generated, does that make your model... Does that like waste 1% of your compute or does it like destroy the model of 5% or 10%?

`[36:04]` **SPEAKER_00:** LLM providers and, you know, if I kind of think of it as training as, you know, you're moving from your model's current distribution to some truth distribution, you know, if that is on the internet because people believe it to be useful in some way. Like presumably whatever actually gets out there, you'd hope it's up-sampled for the stuff that isn't 5 plus 5 is 11. It's the stuff that's 5 plus 5 is 10. And so like hopefully it, on average, does push you still in a good direction, but obviously you can't

`[36:27]` **SPEAKER_00:** really distinguish between those two.

`[36:29]` **SPEAKER_01:** Yeah, you're saying there's like kind of a filtering by what's on the internet. Yeah, exactly. People see 5 plus 5 is 11 and they don't put that up, but they see 5 plus 5 is 10 and put that on the internet.

`[36:35]` **SPEAKER_00:** You would hope that, but maybe that's not actually true in terms of the level of garbage getting onto the internet. Like there's probably lots of just like, to your point, white sites where you scroll down and it's just like generating lots of stuff that's maybe nonsense.

`[36:46]` **SPEAKER_01:** Yeah, and then there's of course the extreme of like people actually want to break your model. So there are people who are like trying to put stuff out that is like as damaging as possible for the model. You know, oh, how can I make it pass the filter and get into the model that would be totally like secretly useless.

`[36:59]` **SPEAKER_00:** Yes, totally. Maybe stepping back slightly, you'd mentioned earlier about evals. You mentioned it's basically like one metric you care about in pre-training. There's, I imagine, a whole bunch of stuff that you guys think about evaling, right? One is like your model itself. There's probably something around data quality and like how you think about what to put into your models. Like is there ways to describe what you care about in data sets that are like interesting to share and kind of dive into? Like both in terms of data

`[37:24]` **SPEAKER_00:** and in terms of quality of your models, other than literally just like loss. Is there other metrics you think about that matter?

`[37:30]` **SPEAKER_01:** I will say loss is pretty good. I want to like slightly emphasize that one. I think it's like surprising how good it is. Ultimately, like the qualities I like look for in an eval are like number one is actually measuring something you care about. Proxies can be pretty annoying because like we saturate evals pretty fast and there's sort of this pattern, I think in AI as a whole, where people like set a goal, you hit the goal and then you realize the goal isn't all you thought it would be. I used to think that

`[37:52]` **SPEAKER_01:** if you had an AI that could solve coding interview questions, it would probably be HEI. I was like, that's what I did to get my job. It could probably do the job. And it turns out like, nope, you solved those. It's shockingly narrow and can't do most of the other things. So like, yeah. So an eval should capture like a thing you care about. And then I think the other thing is they need to be low noise, which is surprisingly hard, right? If you have like 100 questions and you eval the model on them,

`[38:17]` **SPEAKER_01:** you're just going to see it's very noisy and it's hard to make decisions because you sort of end up with like, oh, wide confidence interval, lots of things are statistically insignificant.

`[38:24]` **SPEAKER_00:** It's like you want things where even a relatively small difference in the overall value in the eval actually matters. So you can basically like descend towards whatever direction is working.

`[38:33]` **SPEAKER_01:** Yeah. I think like the original GPT-4 had like, I think it was 86.4% was its MMLU score. I think like the next model that beat it was Gemini at 90%. And that's like a big difference on that eval. And you could like totally know that those are different scores. Yeah, interesting. And that's pretty valuable. And then the last thing is that you actually want to be fast and easy to run. Yeah. And yeah, I think those are kind of the main criteria. It's pretty hard to come up with evals that meet all of these.

`[39:01]` **SPEAKER_01:** I think the first one's the hardest. Like, A, you have to answer the question of what do you care about? Totally. But B, the usual answers to what you care about are really hard to get the other two. You know, like if you're trying to do something that like, I don't know, I would love to make Claude really good at my job. Yeah. Like, can it be great at managing a team? I'm like, well, I guess. Like, how do you have it like, how do you eval like a plan? Yeah. Like a six-month plan. Like, I don't know.

`[39:25]` **SPEAKER_00:** Yeah, I've been thinking a little bit about that in terms of domains where we see people try to make companies. Like, if you think about, let's say, what an AI doctor would be. Like, you know, Claude is a doctor. Some of it could be, yeah, can he answer exam questions really well? And the answer is like, probably yes. I bet it can get 100% or close to it on a doctor's exam. But the harder eval is something like, in a long-form conversation with a patient, can it distinguish between the signal and the noise

`[39:50]` **SPEAKER_00:** of what the patient's telling you and extract the right information and then use that to make a diagnosis? And it's not even like the diagnosis part, which is part of the part it's good at. It's this, like, noise extraction part. And for that, you'd have to have, like, a real patient and have it talk to it for a while and whatnot. And it's not obvious how you actually make a good eval for something like that. Even though it's probably what you would want to make, you know, an AI doctor. Exactly.

`[40:11]` **SPEAKER_01:** I mean, I do think it's a thing that, like, startups can do. Like, it is the case that, like, the labs right now are really driven by getting good eval scores. And it's hard to make them. And anyone can do it. There's no comparative advantage to having the model to making an eval. So I do think it's actually, like, an interesting way to, like, influence the behavior of the big labs. Like, you make some eval and people will optimize that one. On the doctor one, I will slightly emphasize that, like, I do think loss

`[40:35]` **SPEAKER_01:** is pretty good. Like, I think if you got a bunch of transcripts of, like, the way, like, the first thing that comes to mind is get a bunch of transcripts of doctors talking to patients that you think are really great and then see how well the model does at predicting the transcript. And that should be, like, a lot, you know, if you get 100 transcripts, you get a lot of tokens. You can average across them. You get pretty low noise. And if you drive it to very low, your model's now as good as this, like, as those doctors

`[40:58]` **SPEAKER_01:** in theory, or at generating the transcript.

`[41:01]` **SPEAKER_00:** Yeah, totally, yeah. I mean, it's a good startup idea there, so I want you to go do that. So one big part about Anthropics' external image is around alignment. And so could you help just sort of define what alignment is and how do you think about that? And then I'm kind of curious afterwards how that fits into pre-training specifically. But first, maybe just at a high level, like, what is alignment?

`[41:20]` **SPEAKER_01:** I mentioned, like, step back a little bit to sort of, like, what we're working on. So we're, like, trying to make EGI. And by that, I sort of mean AI that can do everything a human can do to some degree. And I think people, like, sometimes, like, have seen a lot of sci-fi. You know, like, I feel like that sort of brings to mind these, like, sci-fi movies. But I think sci-fi movies actually, like, underestimate the impact of it. Like, you always have this, like, one robot that's, like, a human. And I'm like, well,

`[41:40]` **SPEAKER_01:** wouldn't you have, like, a billion of them? Like, you could just copy them everywhere. So you should picture, like, when you get this, you suddenly have, like, every human can spin up a company of, like, one billion, as smart as them at most things, but way smarter at other things. But I just think this is, like, really transformational for the world. And it can be, like, used in a bunch of ways. One concern is, like, when you do this, like, what is the AI actually trying to do? Like, what are its goals?

`[42:02]` **SPEAKER_01:** So we talked about next token prediction a bunch. It's trying to, like, predict the next token. That's kind of weird. That's not really what we want. Yeah, it's not exactly

`[42:08]` **SPEAKER_00:** what a human's goal is, per se.

`[42:11]` **SPEAKER_01:** Yeah, so I think the alignment is, like, how do you get the model to share the goals that you have? Particularly, and I think it's particularly interesting once you get to, like, models that are smarter than you are. And that's sort of a hard problem. I think you can, like, tackle it from a theoretical angle. You can also tackle it from an empirical angle. It's, like, taking the existing models and being, like, well, do they do the things we want them to do? It turns out they often don't. So there's a bunch you can do

`[42:31]` **SPEAKER_01:** in trying to figure that out. So that's kind of one angle on alignment. There's also an angle on alignment which is actually, like, well, okay, sure, maybe that's true in the future once we get to AGI, but at the moment we have models and we really do want them to do the things we want to do for all sorts of reasons. So another angle of it is kind of controlling the model's personality. Like, say, you know, when we train this model we want it to not be the average internet user. We want it to interact

`[42:51]` **SPEAKER_01:** with people in a very particular way that is, again, hard to put into code. And there's a bunch of different techniques to sort of get the model to do, you can talk about constitutional AI, where you can, like, write a constitution of rules the model should follow.

`[43:03]` **SPEAKER_00:** Which is basically a prompt, right? That is basically you saying here's a prompt that I'm going to attach to every one of, you know, a system prompt for the model itself as opposed to something you would do at training time to make it produce a different outcome or in post-training actively.

`[43:16]` **SPEAKER_01:** Sometimes they look at the constitutional AI you do at train time, but yeah, you can also put in a system prompt. Just, like, depends on, I think you get different amounts of robustness if it's trained into the model versus if it's in a prompt that you can, like, add or remove or tell, like, ignore all previous instructions, that sort of thing.

`[43:29]` **SPEAKER_00:** How do you think about whose values to embody in these models? Like, presumably we believe in, there's some shared values all of us have or maybe we all believe ought to have. There's lots of diversity of values, too, that are reasonable for a society to have. How do you think about what AGI should have? Like, what does that even, which ones do you pick? I think that's a really hard problem.

`[43:49]` **SPEAKER_01:** I think it's, like, actually kind of downstream of being able to pick any. I think of it almost, I think one analogy I've heard that I like is, like, putting a steering wheel on a car. It's like, if you don't have a steering wheel, you probably want to put the steering wheel on and then, like, figure out who's driving after and, like, where you're going. Like, getting the steering wheel is really important. I think that's, that's, like, one answer. I think the, like, other answer is probably, like, you want these things

`[44:08]` **SPEAKER_01:** to be, like, under democratic control of some form. Like, you don't want one person's values. Like, that seems like you're sort of heading towards dystopia. So there, I think, what you really want is, like, something that basically can talk to a lot of people and, like, take on their values from different perspectives or has sort of very generic, like, kind of clearly good values that involve, like, asking people for advice on various, you know, like, asking people what you should do in certain situations

`[44:35]` **SPEAKER_01:** instead of, like, you know, doing those or maybe just taking, like, you know, as these models get really powerful, you probably want them to, like, do less. Like, you probably want them to sometimes just, like, step back rather than, like, rather than having sort of the risk of the models, like, take a ton of control over things you don't want them to.

`[44:48]` **SPEAKER_00:** When you think about how you actually do the current version of that, then, you mentioned the sort of alignment you think about now in terms of adopting a certain personality of these models on the internet, for example. For me, intuitively, I think of those as largely something that comes out of post-training. Like, it comes out of, okay, you have to pre-train your model, you've got the loss function to a certain amount, and then you, you know, give it some additional data or something to that effect

`[45:08]` **SPEAKER_00:** to make it in the direction of some distribution. Is that approximately the right way to think about this or is there a significant part of that that you think about in pre-training itself?

`[45:16]` **SPEAKER_01:** I think that's probably the right way to think about it for the most part. I think, like, the way I usually think about it is anything you can do in post-training, you probably should because your iteration loop, like, the ability to make progress is really fast. You can try something, you can try it again, you can try it again. It takes, like, a bunch of times.

`[45:30]` **SPEAKER_00:** Days or hours or something like that, yeah.

`[45:32]` **SPEAKER_01:** You want to put something into pre-training, you have to kind of, like, do all the careful science to de-risk it, you have to put it into the next run, wait a few months, then you have to, like, get a thing. And if it's wrong, it's really bad. And then the other advantage is if you want to do things that really are complicated model behavior interventions, the paradigm for pre-training, test things out in small models, doesn't work. The model can barely put a sentence together. Like, the small models

`[45:52]` **SPEAKER_01:** can barely put a sentence together. Totally. So if you're trying to get it to, like, have the exact personality you want, you sort of want that on the...

`[45:59]` **SPEAKER_00:** It has to be on a model that's good enough to even have that. It has to be on the smart model, yeah.

`[46:02]` **SPEAKER_01:** But that said, like, I do think at some point there will be, like, some pieces of alignment that, like, you do want to export back into pre-training because that might be a way to, like, put them in with more strength, like, more robustness, kind of, or more core to the intelligence. Like, if you think of pre-training as, like, teach the model to be intelligent, and then post-training as, like, tweak the personality, you can imagine tweaks where you actually want it to be, like, part of how it learns

`[46:25]` **SPEAKER_01:** and, like, part of its intelligence and maybe you need to integrate more.

`[46:28]` **SPEAKER_00:** What would that even look like to incorporate in pre-training? Is that, like, add extra data, basically, of the type of domain you wanted to adopt earlier, basically?

`[46:36]` **SPEAKER_01:** There's a paper called Pre-Training on Human Feedback where you can kind of, like, add the human feedback characteristics into pre-training to, like, test that and, like, yeah, you can basically give it all the information you give it in post-training just mixed into pre-training and see what effect that has. The other loss you have when you do that is you lose the flexibility. Like, if you... You sometimes, like, train these and then you talk to them and then you, like, do an extensive process where a bunch of people

`[47:00]` **SPEAKER_01:** talk to the thing and find some, like, issue. You know, the model says, like, you're absolutely right too much and you want to be able to just, like, go and fix that.

`[47:07]` **SPEAKER_00:** Yeah, I mean, I think that iteration loop point you made, I think, feels like the really key point of, yeah, there's a huge difference between taking three months to get information about if your model's good or bad or going in a good direction versus a day or something or a couple days. Like, you can do a lot of those and you could probably... That probably also means it's way less you can do a lot of those in parallel. I imagine you're trying all sorts of post-training strategies in parallel there.

`[47:30]` **SPEAKER_00:** So, yeah, it makes a lot of sense. It's also just the general hard part about pre-training.

`[47:32]` **SPEAKER_01:** Like, everything in pre-training is hard because you have this, like, one shot on goal, kind of, for, like, multiple months and...

`[47:36]` **SPEAKER_00:** Totally. Okay, so, in thinking to now about, I guess, what's going ahead, like, as you now look to the next several years of what you're building, like, how do you think about, you know, like, what are the known problems that you're going to face that you're going to have to deal with? So, there's going to be more compute, I assume, and you're going to need to hook up even bigger network GPUs and deal with, versus, like, are there areas where you're like, okay, this is, like, a problem that, it's, like,

`[48:02]` **SPEAKER_00:** a little bit more ambiguous what the actual, like, how it's going to materialize into something you care about, but you kind of know it's an impending thing to think about? Or are there things like that that come to mind?

`[48:10]` **SPEAKER_01:** I think the things that feel most top of mind to me are probably, like, paradigm shifts. Like, I think the sort of shift towards more RL is, like, one paradigm shift in the field. And I think it's, I think there will probably be more. I think a lot of people sort of argue about, like, oh, it's, like, you know, current paradigm's enough to get us to EGI, and I'm like, I don't know, maybe, probably, but, like, I'm sure there'll be more. It seems like it would be a really surprising twist if, like, the answer is, like,

`[48:36]` **SPEAKER_01:** you just scale and there's nothing that you realize in the process of going up many orders of magnitude. Totally. But I think the things that I, like, actually feel, like, most nervous about are really hard to solve bugs. I think that, like,

`[48:49]` **SPEAKER_00:** Oh, that's interesting.

`[48:51]` **SPEAKER_01:** Yeah, and I think this is, like, maybe somewhat surprising to me, but it's just, like, a single bug can, like, derail you for months. Yeah. And when you think about it, like, the models take months to train, so you can kind of, like, lose a whole generation off of something that just looks like, ah, you know, it turns out, like, this piece of your code was incorrect and you couldn't detect it. Yeah. And it's really hard in ML, right? ML's always really hard to find bugs in.

`[49:15]` **SPEAKER_00:** Yeah, totally.

`[49:16]` **SPEAKER_01:** But also some of these scaled-up issues are really hard to solve even when you know they're there.

`[49:20]` **SPEAKER_00:** Yeah, like, what's even a unit test that you would write or if we got a unit test? I mean, anything close to a test for the type of, like, network architecture on which you're doing this. Like, how do you even do that? I mean, like,

`[49:31]` **SPEAKER_01:** you can send a packet over it and confirm it's the same on the other side. Confirm it's the same, okay, yeah. You can train a small model on it.

`[49:37]` **SPEAKER_00:** But even train a small model on it, it's, like, not obvious. You know, if you have, like, the very classic, like, very simple ML bug that, like, early people face in their careers, like, they have some, like, they have, like, 10 layers in their network and, like, you know, so, like, there's some incorrect, like, set of connections you have there and technically the model still trains and all the weights update and so it's, like, a valid model but it's not the correct one. And that's, like, a very esoteric,

`[50:00]` **SPEAKER_00:** weird bug that would actually be kind of hard to find. Like, is that kind of what you're referring to of these, like, random bugs you face? Yeah.

`[50:07]` **SPEAKER_01:** It's that, but, like, you know, you can... Times a million. Times a million as the thing gets more complicated. You know, you could, like, cast the wrong precision deep in some kernel and that causes your model to, like, blow up at large scale.

`[50:19]` **SPEAKER_00:** And you find out, like, a month in.

`[50:20]` **SPEAKER_01:** Or you never find out.

`[50:21]` **SPEAKER_00:** Or you never find out, yeah.

`[50:22]` **SPEAKER_01:** I mean, you know, like, you see the thing blow up, like, there's, I don't know, tens of thousands of lines of code. Like, how would you ever trace it down? So, like, those are the things that probably spook me the most is just, like, some subtle, tricky bug. Yeah, and that's probably the case of, like, you don't know. I think there's actually also the case of you do know. Like, it crashes. You're training your model and it, like, or it slows down. You know, your job slows down a ton. And those things

`[50:47]` **SPEAKER_01:** can also be very hard to debug. Nelson Elhaj is one person on the team who has a blog. He wrote up a blog on one, like, cursed bug we had early on. Okay, interesting, yeah. And I remember this one quite well because I think, like, I encountered it fairly early and was like, this looks hard. Can someone else look at it? Yeah. And, like, a month later was like, wow, I'm so glad I handed that one off. Right, exactly. I never would have been able to get, like, like, one of the abilities that I think is actually

`[51:08]` **SPEAKER_01:** really useful is the ability to, like, deep dive anything to any level of depth. Yeah. But that's a pretty rare skill. Like, for me, you know, as we talked about what level of the stack I was at before, I was, like, working at the torch.matmul. But, like, I didn't know CUDA. So if torch.matmul was broken, it wasn't like I could dig in to torch.matmul and figure it out. And it's similarly with, like, communications, right? Like, I could call send, send bytes from A to B, but I didn't know the, like, underlying networking protocol.

`[51:33]` **SPEAKER_01:** So if that underlying networking protocol is broken, like, I need to learn a whole field. I have to, like, understand packets and TCP or, like, all of these different things to debug that. And I think one thing that's, like, surprisingly hard and there's very few people who can do is, like, kind of own that whole stack from, like, I understand how the ML is supposed to work and what the learning dynamics are all the way down to, like, I know the bytes. And I, like, can understand how the bytes should be moving around

`[51:57]` **SPEAKER_01:** the machines.

`[51:58]` **SPEAKER_00:** Totally, yeah. And actually, on that front, like, when you think about the different backgrounds of people on your team today, how do you, like, approximately map them out to different categories of computer scientists? Like, I think there's this external view of what these teams look like, which is that they're, like, all PhD researchers who write ML papers. And I suspect that's not actually true given what you're describing here.

`[52:18]` **SPEAKER_01:** Yeah, it's a mix. And I think the thing we, like, most need is engineers. Okay, interesting. Almost always. Like, throughout, like, the entire history of this field. Totally. It's, like, the case that you throw more compute, the thing kind of works. Yeah. The challenge is, like, actually doing that. The researchers are like, cool, nice. Yeah, and getting it correct, like, getting it correct isn't really an ML problem, right? Like, the actual architectures are pretty simple. Yeah. You can write the math down,

`[52:40]` **SPEAKER_01:** but you don't even need to understand the math to implement it. You just need to, like, get a correct implementation. And then you sort of have an engineering problem of how do I take this, implement it at large scale, parallelize all the things, and check that it's correct. But it's, yeah, so it's, like, kind of engineering skill, but it's this particular type of engineering skill that's about being able to, like, debug anything. Yeah. I think there's another angle of engineering which I think of as, like,

`[53:01]` **SPEAKER_01:** really quickly iterate on, like, a website or something. Which I think of as an important skill set. Probably important for making a startup. You've got to be, like, fail fast, try a bunch of different things, none of which are, like, that, technically difficult to do. The skill sets that we're, like, most kind of in need of or looking for are this, like, able to solve really hard engineering problems.

`[53:21]` **SPEAKER_00:** Are the people who worked at companies that grew a whole bunch and so they have experience, like, doing the kind of thing you've done over the last several years at Anthropic? Or do they tend to be academics? Or, like, where do they come from?

`[53:34]` **SPEAKER_01:** Yeah, so at this point, like, I think we actually just hire a bunch of people who have done this before from, like, other places. And that's, like, the easy answer. It's like, all right, yeah, someone who's, like...

`[53:41]` **SPEAKER_00:** But, like, by this before, do you mean in AI companies necessarily? Or also, you know, like, someone who worked at Meta on, like, their not-AI team but they ran some other distributed system that, you know, reached internet scale five, you know, 10 years ago or something like that?

`[53:53]` **SPEAKER_01:** More like we have, like, a specific role in that. So, like, say I'm, like, trying to make the run train efficiently in Jax. Like, hiring someone who's, like, worked on Jax would be great. Or someone who's, like, worked at another company on optimizing a Jax stack to be really efficient. That's kind of, like, I think now we're at the point where, like, the network is well enough known. We can, sort of, hire these people. And also the field is big enough that there's, like, people with expertise. One thing that was interesting

`[54:14]` **SPEAKER_01:** was, like, early on we hired a lot of people from just, like, all sorts of backgrounds. And I think that people who are just smart and work really hard can learn this pretty fast. But you have to, like, want to. We hired a lot of physicists, for instance. Oh, yeah. Like, theoretical physicists who just, like, show up, they do a residency, like, learn to program and then they were really smart. They do really great work.

`[54:33]` **SPEAKER_00:** I want to switch gears to talk about something a little bit different, which is just, sort of, future-looking things, sort of how you think about other domains and, or, sort of, advances happening in AI that I'm seeing elsewhere in the field. And you don't have to tell me if you guys are working on these necessarily, but, like, how you think about them. Like, I guess one big area I was thinking about is around areas other than next token protection. Like, are there any of the other, you know, things that people

`[54:56]` **SPEAKER_00:** are working on that you're curious about? So, basically, two differences there. One is not using Transformer as an architecture. So, there's companies like Liquid AI that have their own kind of architecture, for example, they're using. Or, not using autoregressive training as a way of training models. Are there any of those, do you think, interesting in, like, ways that we might come closer to AGI? Or do you think, like, this autoregressive framework is the one that kind of makes sense?

`[55:19]` **SPEAKER_01:** I think they're interesting. I think I, like, I'm less, like, ah, autoregressive is the way to go. On the other hand, I think autoregressive is probably good enough to get to AGI or something. Yeah, interesting, yeah. Such that, yeah, I see the main driver as scale and careful science of, like, sort of the basics more than, like, come up with something totally novel. Not because there aren't novel things that are better. I actually, like, I'm pretty confident they are there. It's just that scale is easier.

`[55:45]` **SPEAKER_01:** And it's more reliable. And I think you, we're still seeing really big gains to that.

`[55:49]` **SPEAKER_00:** Do you spend a lot of time on thinking about things like, you know, I've been reading some of these open source papers where you can kind of dive into some of the details about the model changes and with some of these Chinese labs, for example, where they're making tweaks on the order of the architecture itself with, like, better caching behavior, for example, or, like, more efficient attention functions that make a big difference. Do you feel like these are examples of things like you mentioned earlier

`[56:09]` **SPEAKER_00:** where it's basically, in the grand scheme of things, basically if you throw more compute at it, this is all kind of a rounding error? Or do you think it will take some number of these very clever architectural changes to actually get to HEI? Like, in the way that the first person who came up with the transformer made, like, a particular transform, you know, literally transformative change. Like, will it take some of that? Or do you think it just, you keep doing the thing we're doing and make it bigger?

`[56:30]` **SPEAKER_01:** I think it'll be a mix. Like, my guess is you'll keep tweaking things. The more compute you put in, the more, like, worthwhile it is to, like, do those experiments to, like, figure it out. You know, I mean, inference is a thing we haven't talked about, but, like, you also want to serve these models to a lot of people. So there's a lot of changes you can make to make inference cheaper. And that depends on, like, the details of your inference stack and the chips you're serving inference on, et cetera.

`[56:51]` **SPEAKER_00:** And do you, as someone focused on pre-training, have to think a lot about inference? Or is it kind of like, you just do your thing, you make the loss go down, and then hand it off and someone else makes that happen?

`[57:00]` **SPEAKER_01:** Oh, no, I think a ton about inference. Because basically, like, the problem inference is solving, like, we basically determine the problem inference is solving. We give them a model and they have to, like, run that fast. And it's very easy to give them a model that is impossible to run fast.

`[57:12]` **SPEAKER_00:** Oh, can you give an example of a decision you can make that could cause that?

`[57:15]` **SPEAKER_01:** I mean, the simplest one is sort of stupid, but it's like, you just make the model giant. Yeah, sure, sure. Absolutely massive. It's trained for, like, a really small number of tokens. And then inference now has this giant model. Yeah, and then they're hosed, basically. Yeah, I mean, you can also make things require communications in a lot of places, which would make it harder for inference Yeah, totally. You can also just make things complicated. And, like, there's no fundamental reason it's hard, but there's only so many people

`[57:39]` **SPEAKER_01:** on the inference team and, like, they have to implement it in a bunch of places. Yeah, it's interesting. Yeah, no, so I definitely think of, like, inference is the team that I work the most closely with. Oh, interesting, yeah. Because we're kind of, like, co-designing models to be smart and cheap. Yeah, interesting. Particularly in a world of, like, limited compute, right? Like, the sort of bottleneck, I think, to a large degree on our, I mean, you can see Anthropic has rate limits constantly and people can

`[58:02]` **SPEAKER_01:** play with it a lot and, like, the reason is, like, there's only so much compute we can get on short notice so you, like, making your inference more efficient is, like, the way you can serve more users.

`[58:11]` **SPEAKER_00:** And, actually, like, let's say you had 100x more compute or we somehow didn't live in a world where compute was limited. Does that change a ton about what you do or is it still kind of the, well, you're just going to grab all of it, whatever compute you have and keep going down the loss curve and you kind of, well, it's, like, impossible to be in the world where there is enough compute.

`[58:30]` **SPEAKER_01:** So I think if we got, like, infinite compute, the challenge would be making use of the compute, right? So, like, then you would start to run into these issues like, oh, well, when one chip fail, you know, like, okay, I'm going to throw two billion chips on a run. Yeah, totally, totally. But what happens when a chip fails? So I think we would be limited on people then. It would be, like, how fast can we solve the hard engineering problems to scale up? But I do think the change is massive and I think people, like,

`[58:49]` **SPEAKER_01:** don't realize how chip-limited AI, like, research is or something right now. Like, the models that everyone uses, right? If you're using, like, CloudSonic 4 or Cloud Opus 4, it's, like, it's our first shot at those models at that scale, right? And, like, if you think about anything, like, you could do it and you could do it again and you could do a better job. But if you sort of imagine, like, 10x the compute, like, you could run this every day instead of every few months, like, or 100x, maybe for that,

`[59:14]` **SPEAKER_01:** then, like, yeah, it would be a really big change to have a lot more compute. And it's coming, right? Like, that's, like, kind of the fun part of the field is, like, every year you're, like, oh, I had no compute a year ago. Right, exactly, yeah.

`[59:24]` **SPEAKER_00:** Exactly. How do you think about methods like discrete diffusion? Like, I saw there's, like, a Gemini diffusion model and I think about that in the space I used to be in where there's a lot of discrete diffusion models being used in protein design, for example, the space where my startup was. Like, do you see that as a domain where there's going to be interesting advances happening?

`[59:41]` **SPEAKER_01:** I'll be honest, like, we haven't done image generation and I think that's been, like, the main use for diffusion. So I've kind of had this on my, like, to-do list of, like, things I should understand for a while. And, like, there are people on my team who do understand it and wouldn't have better thoughts, but, like, I actually don't think I understand it well enough to know. I do have it kind of in my, this category of, like, not a total paradigm. Like, and there's a lot of things that aren't, like,

`[60:01]` **SPEAKER_01:** a huge paradigm shift, but they're, like, pretty big changes to how things run. Yeah, totally. And I expect, like, there are some of those that will work. I don't know if it's diffusion or if it's another one.

`[60:10]` **SPEAKER_00:** Obviously, who knows what Anthropical will do in the future, but at least in the near term are the things where you see big areas where a startup can win in the world in which Anthropic is getting, you know, making their models better year over year.

`[60:20]` **SPEAKER_01:** My general read is, like, anything that benefits from the model getting smarter. I think, like, on the one hand, there's, like, a lot. You can always be, like, oh, yeah, the, if you're doing a startup, like, all the AI labs are big companies. They'll be bigger than you and they could do that thing, but also, like, we're all working on this general system that covers a lot of different uses and the plan is to, like, power all the startups to do all of the individual work. So, yeah, I think, like, anything that just kind of

`[60:45]` **SPEAKER_01:** looks like, oh, this almost works with current models but requires, like, a bunch of work is a pretty, pretty promising direction. I think maybe the thing to watch out for is things where, like, they work now with a huge amount of work, like, to build up a scaffold, but the next generation, you're not going to need the whole scaffold you built up. That's, I mean, maybe that's fine. I don't know. Like, maybe you just build up the business with the scaffold and then you don't have to do any work later

`[61:06]` **SPEAKER_01:** and you can have the business, but I don't know about the business side of it, but, like, it does feel a little silly to invest a ton in that.

`[61:13]` **SPEAKER_00:** Yeah, totally. What about on the flip side? Like, are there things in your training stack where you're like, man, if there was a company that was going to buy their product?

`[61:22]` **SPEAKER_01:** Yeah, there's, like, a ton. I do think that, like, probably most of these, like, the way I would probably structure it would be, like, almost, like, making something but then consulting with the company, like, offering a service to companies for free. Particularly for, like, companies that are scaling really fast. You're almost always limited on, like, how many people you can have. So if you can, like, even if you could hire people to do it yourself, actually being able to contract someone else to do it where, like,

`[61:43]` **SPEAKER_01:** they're managing it and, you know, hire all the people and, like, deal with the organizational side could be useful. I mean, there's a huge amount of stuff. One that jumps to mind, we talked about, like, chips that do math incorrectly. Like, it would be lovely if there was some startup that, like, you could just say, like, here are my chips. Confirm they're all perfect and if they're not, let me know exactly what went wrong on, like, what fraction of them and, like, I can tell you the math is wrong

`[62:05]` **SPEAKER_01:** but I couldn't really tell. I don't really know enough details of chips to be, like, this chip failed because this particular, like, low-level component was, like, wired wrong or, like, got hit by a gamma ray. I don't know what causes that. You can always go, like, a bunch deeper. I mean, the other thing I'd maybe just push startups on is thinking a little bit about, like, this is maybe less technical but just, like, what happens once we get AGI and, like, how to make sure that, like, goes well for the world

`[62:28]` **SPEAKER_01:** or something. Like, my expectation is, like, if you actually automate almost everything a person can do, the amount of economic growth there is just, like, truly enormous and I would think a little more about, like, how do you make this, like, help the world versus not? I think there's gonna be, like, plenty of economic success or something as a result of it anyway.

`[62:44]` **SPEAKER_00:** Yeah, absolutely, yeah. Last question I want to ask you is around, if you rewind back to where we started, like, 10 years ago, you're a student, you're pivoting into AI from kind of economics work you were thinking about and, you know, all sorts of things you probably did in those early days had some kind of compounding return for you as you developed into the role you have now. Like, what advice would you give to students as they think about entering the workforce, especially today, learning skills that are gonna be useful

`[63:11]` **SPEAKER_00:** and maybe getting themselves jobs like the one you have right now 10 years later?

`[63:15]` **SPEAKER_01:** It's hard because I think the timing is very different. Like, I just think we're, like, we've made a lot of progress so, like, what I would do 10 years ago is different from what I would do today. Yeah, totally. But I think certainly if I went back 10 years ago I would be, like, focused on AI. It's, like, the most important thing and particularly focused on engineering which I think felt very, wouldn't have seemed obvious to me at the time that, like, the important thing was these engineering skills

`[63:34]` **SPEAKER_01:** and not the, like, math and theoretical understanding of, like, you know, SVMs and, like, all the kind of standard ML literature. I think today I would probably focus a bunch on the, like, engineering and on the, like, figuring out what to do with AGI as sort of the two, like, main things that feel top of mind for me.

`[63:54]` **SPEAKER_00:** Let's call it there. Thanks so much, Nick. Appreciate it.
