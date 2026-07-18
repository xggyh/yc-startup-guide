# 全文转录 · AI 到底有多聪明?用 ARC-AGI 重新定义"智能"

> ▶ [YouTube](https://www.youtube.com/watch?v=pBlIgs6w7Ss) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/pBlIgs6w7Ss.md) &nbsp;·&nbsp; How Intelligent Is AI, Really?
>
> 🗣️ 说话人分离识别到 **2** 位发言者(标注为 SPEAKER_00 …)。

`[00:11]` **SPEAKER_00:** I'm excited today to welcome Greg Kamrad, who is the president of the ArcPrize.

`[00:16]` **SPEAKER_01:** That's right.

`[00:17]` **SPEAKER_00:** Thanks for coming here at NeurIPS 2025 in beautiful San Diego.

`[00:21]` **SPEAKER_01:** Thank you, Diana.

`[00:21]` **SPEAKER_00:** So what does the ArcPrize Foundation do?

`[00:25]` **SPEAKER_01:** Yes. So the ArcPrize Foundation is a nonprofit, but it's a little bit of a different nonprofit because we are very tech forward. And so our mission is to pull forward open progress towards systems that can generalize just like humans.

`[00:38]` **SPEAKER_00:** So according to Francois Chollet, he defines intelligence as the ability to learn new things a lot more efficiently. What does that mean for founders as they look at all these benchmarks for all these model releases that are chasing MMLU numbers?

`[00:54]` **SPEAKER_01:** Yes, absolutely. Well, so one of the cool things about ArcPrize is we have a very opinionated definition of intelligence, and this came from Francois Chollet's paper in 2019 on the measure of intelligence. And in there, you would normally think that intelligence would be

`[01:08]` **SPEAKER_?:** a very specific definition of intelligence. And in there, you would normally think that intelligence would be a very specific definition of intelligence.

`[01:08]` **SPEAKER_01:** How much can you score in the SAT test or how hard of math problems can you do? And he actually proposed an alternative theory, which is the foundation for what ArcPrize does. And he actually defined intelligence as your ability to learn new things. So we already know that AI is really good at chess. It's superhuman. We know that AI is really good at Go. It's superhuman. We know that it's really good at self-driving. But getting those same systems to learn something else, a different skill, that is actually the hard part.

`[01:35]` **SPEAKER_01:** And so Francois, alongside that, proposed his definition of intelligence. He says, well, I don't just have a definition. I also have a benchmark or a test that tests whether or not you can learn new things. Because generally, people are going to learn new things over a long horizon, a couple hours, a couple days, or maybe over a lifetime. But he proposed a test called the Arc AGI, or at the time, it was just called the Arc Benchmark. And in it, he tests your ability to learn new things.

`[02:01]` **SPEAKER_01:** So what's really cool is that not only humans can take this test, but also machines can take this test too. So whereas other benchmarks, they might try to do what I call PhD++ problems harder and harder. So we had MMLU, we had an MMLU+, and now we have humanities last exam. Those are going superhuman, right? Arc benchmarks, normal people can do these. And so we actually test all of our benchmarks to make sure that normal people can do them.

`[02:25]` **SPEAKER_00:** And just a bit of context for the audience, this particular prize was famously one that a lot of LLMs with just pre-training before RL came in. Yeah. In the picture before 2024, all these large models, language models were doing terribly, right?

`[02:44]` **SPEAKER_01:** Yes, absolutely, doing terribly. And, you know, it's kind of weird, but nowadays it's hard to come up with problems to stump AI. You know, back in 2012 with ImageNet, all you needed to do was just show people an image of a cat and you could stump the computer. But when Francois Chollet came out with his benchmark in 2019, fast forward all the way to 2024, I think at the time it was GPT-4, the base model, no reasoning, I think it was getting 4%, 4 or 5%. So clearly show it, hey, humans can do this, but base models are not doing anything.

`[03:14]` **SPEAKER_01:** And what's really cool actually is right at 01, I remember testing 01 and 01 preview, right when that first came out, I think performance jumped up to 21%. So you look at that and after five years, it was only 4%. And then in such a short time, it goes to 21. That tells you something really interesting is going on. So actually we used Arc to identify that reasoning paradigm was huge. That was actually transformational for what was contributing towards AI at the time.

`[03:37]` **SPEAKER_00:** So much so that now all the big labs, XAI, OpenAI are actually now using ArcAGI as part of their model releases and the numbers that they're hitting. So it's become the standard now.

`[03:50]` **SPEAKER_01:** Yeah. Well, I tell you what, we're excited that the community is recognizing that ArcAGI can tell you something. That's what we're excited about. And when public labs or frontier labs like to use us in terms of reporting their performance, it's really awesome that they too say, yes, we just came out with this frontier model. This is how we choose to measure our performance. And so in the past 12 months, you're right. We've had OpenAI, we've had XAI with Grok4, we've had Gemini with Gemini 3 Pro and DeepThink,

`[04:14]` **SPEAKER_01:** and then just recently Anthropic with Opus 4.5.

`[04:17]` **SPEAKER_00:** That's cool. So what's going well with all these releases?

`[04:20]` **SPEAKER_01:** So it's going really well that they're adopting it. However, we're mindful of vanity metrics that come from there too. So just because they use us doesn't necessarily mean that our mission is done or our job is done or what we're trying to do here. Because again, if we go back to the mission of ArcPrize, it's to pull forward OpenAGI progress. So we want to inspire researchers, small teams, individual researchers. And having big labs give an endorsement more or less is really good for that mission, but

`[04:47]` **SPEAKER_01:** it's also secondary to the overall mission.

`[04:49]` **SPEAKER_00:** So now that you've seen also lots of teams trying to ship AI products, what are most common false positives that you observe? Things that feel like progress, but aren't quite progress because it's easy to perhaps just hit a benchmark somewhere and call it done.

`[05:06]` **SPEAKER_01:** Sure.

`[05:07]` **SPEAKER_00:** It doesn't quite work.

`[05:08]` **SPEAKER_01:** Yeah. So when I answer that question, I put on my almost researcher hat, because there's two hats that are very prominent within AI right now. There's economically valuable, like, you know, we're going to go monetize this product hat. And then there's going to be the, call it, romantic pursuit of general intelligence hat. And I'm wearing the latter hat. So one thing that stands out to me is, of course, is everybody talks about it, but all the RL environments. And there's been famous AI researchers that have said, hey, as long as we can make an

`[05:34]` **SPEAKER_01:** RL environment, we can score well on this benchmark. Whatever this domain or whatever it may be. To me, that's kind of like whack-a-mole. You know, you're not going to be able to make RL environments for every single thing you're going to end up wanting to do. And core to RKGI is novelty and novel problems that end up coming in the future, which is one of the reasons why we have a hidden test set, by the way. So I think while that's cool and why you're going to get short-term gains from it, I would

`[05:56]` **SPEAKER_01:** rather see investment into systems that are actually generalizing and you don't need the environment for it. Because if you see, or if you compare it to humans, humans don't need the environment to go and train on that.

`[06:05]` **SPEAKER_00:** Perhaps walk us through a bit of the human environment. Yeah. So you talked about the history of a RKGI version, so it was RKGI 1, 2, and 3 is coming up soon. Yes. Which is a whole new thing with game-like environments and interactive. So walk us through the history and then tell us what 3 is all about.

`[06:21]` **SPEAKER_01:** Yes, absolutely. So RKGI 1 came out in 2019, that was Francois Chollet proposed it. I think he made all 800 tasks himself within it, which is a huge feat in and of itself. And that came with this paper on the measure of intelligence. Now in 2025, just this year. Earlier in March of this year, we came with RKGI 2. And so think of that as a deeper version or an upgraded version of RKGI 1. Now what's interesting is those two are both static benchmarks, or call it metastatic benchmarks. We're coming out with RKGI 3 next year.

`[06:52]` **SPEAKER_01:** And the big difference with RKGI 3 is it's going to be interactive. So if you think about reality and the world that we all live in, we are constantly making an action, getting feedback, and kind of going back and forth with our environment. And it is in my belief that future AGIs are going to be interactive. Future AGI will be declared with an interactive benchmark because that is really what reality is. And so V3 is going to be about 150 video game environments. Now we say video game because that's an easy way to communicate it, but really it's an

`[07:20]` **SPEAKER_01:** environment where you give an action and then you get some response. Now the really cool part and one thing that jazzes me up about V3 the most is we're not going to give any instructions to the test taker on how to complete the environment. So there's no English, there's no words. There's no symbols or anything like that. And in order to beat the benchmark, you need to go in, you need to take a few actions and see how your environment responds and try to figure out what the ultimate goal is in

`[07:46]` **SPEAKER_01:** the first place.

`[07:47]` **SPEAKER_00:** I tried a bunch of those games. They were actually fun.

`[07:49]` **SPEAKER_01:** Yeah, they're cool. And much like ARK 1 and ARK 2, we're testing humans on every single V3 game. So we will recruit members of the general public. So accountants, Uber drivers, you know, that type of thing. We'll put 10 people in front of each game and if each game does not pass a minimum solvability threshold by regular humans. Then we're going to exclude it. Now again, I just have to emphasize, but that's in contrast to other benchmarks where you try to go harder and harder and harder questions.

`[08:15]` **SPEAKER_01:** But the fact that ARK 3 will be out there and regular people can do it, but AI cannot do it, tells you, well, there's something missing still. There's something clearly missing that we need new ideas for research on.

`[08:28]` **SPEAKER_00:** So there's this big theme in terms of measuring intelligence with human capabilities. So there's this growing idea. Yeah. That accuracy is not the only metric that matters to models, but also the time and amount of data that it takes to acquire new skills, which is what this whole spirit of AGI is. So I guess the question is how close are we to evaluating models in human time?

`[08:55]` **SPEAKER_01:** Yes. So with regards to human time, we actually see time as a little bit arbitrary because if you throw more compute at something, you're going to reduce the time no matter what. So it's almost just a decision on how much compute you need. Yeah. You can do whatever you want, which is how much time it's going to take, which tells you that wall clock may not be the important part for what we have intelligence here. But there's two other factors that go into the equation of intelligence.

`[09:16]` **SPEAKER_01:** Number one is going to be the amount of training data that you need, which is exactly what you said. And then number two is actually the amount of energy that you need in order to execute upon that intelligence. And the reason why those are so fascinating is because we have benchmarks for humans on both of those. So we know how many data points a human needs in order to execute a task, and we know how much energy the human needs. We know how much energy the human brain consumes to execute a task.

`[09:39]` **SPEAKER_01:** So with ArcAGI 3, the way that we're actually going to be measuring efficiency, not just by accuracy, I told you they're video games, and they're turn-based video games. And so you might click up, left, right, down, or something like that. And we're going to count the number of actions that it takes a human to beat the game, and we're going to compare that to the number of actions that it takes an AI to beat the game. So back in the old Atari days, in 2016, when they were making a run at video games then,

`[10:06]` **SPEAKER_01:** they would use brute force solutions, and they would need millions and billions of frames of video game, and they would need millions of actions to basically spam and brute force the space. We're not going to let you do that on Arc 3. And so we're basically going to normalize AI performance to the average human performance that we see.

`[10:22]` **SPEAKER_00:** That's very cool. Yes. My last question. Yes. Let's wave a magic wand. And then there's a super amazing team that suddenly tomorrow launches a model that scores 100%. Yeah. It's called Arc AGI Benchmarks. What should the world update about the priors of what AGI is? Yeah. How would the world change?

`[10:45]` **SPEAKER_01:** Well, it's funny you ask that. The what AGI is question is such a deep topic that we can go much deeper on. So from the beginning, Francois has always said that the thing that solves Arc AGI is necessary for AGI. It's not sufficient. So what that means is the thing that solves Arc AGI 1 and 2 will not be AGI, but it will be an authoritative source of generalization. Now our claim for V3 is that no, the thing that beats it won't be AGI. However, it will be the most authoritative evidence that we have to date about a system

`[11:18]` **SPEAKER_01:** that can generalize. If a team were to come out and beat it tomorrow, we would of course want to analyze that system, figure out where still are the failure points that come from that. And like any good benchmark creator, we want to continue to guide the world towards what we believe to be proper AGI. But ultimately, our prize, we want to put ourselves in a position. When we can fully understand and be ready to declare when we do actually have AGI. So if that team were to do it tomorrow, we would want to have a conversation with them.

`[11:43]` **SPEAKER_01:** I'll put it that way.

`[11:44]` **SPEAKER_00:** That's a good way to wrap. Thank you so much for coming and chatting with us, Greg.

`[11:46]` **SPEAKER_01:** Thank you, Diana.
