# 全文转录 · 为什么只靠 Scaling 造不出 AGI:François Chollet 谈符号程序合成、可验证奖励与创业机会

> ▶ [YouTube](https://www.youtube.com/watch?v=k2ZLQC8P7dc) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/k2ZLQC8P7dc.md) &nbsp;·&nbsp; François Chollet: Why Scaling Alone Isn't Enough for AGI
>
> 🗣️ 说话人分离识别到 **5** 位发言者(标注为 SPEAKER_00 …)。

`[00:00]` **SPEAKER_03:** I think we're probably looking at AGI 2030, around the time that we're going to be releasing like maybe ARC 6 or ARC 7. You're not going to stop AI progress. I think it's too late for that. And so the next question is, okay, like AI progress is here. It's actually going to keep accelerating. How do you make use of it? How do you leverage? How do you ride the wave?

`[00:22]` **SPEAKER_01:** That's the question to ask. Today, we're lucky to be joined by Francois Chollet, founder of the ARC Prize, a global competition to solve the ARC AGI benchmark. His latest project is NDIA, a lab exploring a new paradigm in frontier AI research. Francois is one of the best people in the world to help us understand the current AI moment and where all of this is going. Francois, thank you so much for joining us today and congrats on the launch of ARC AGI V3.

`[00:58]` **SPEAKER_03:** Thanks so much for having me. I'm super excited to be here. Super exciting time to talk about AI.

`[01:02]` **SPEAKER_04:** So Francois, tell us a little bit about NDIA. So what exactly is it and what are you guys trying to achieve?

`[01:08]` **SPEAKER_03:** Right. So NDIA is this new AGI research lab, and we are trying some very different ideas. And so our goal is basically to build this new branch of machine learning that will be much closer to

`[01:20]` **SPEAKER_01:** optimal, unlike deep learning. All of us right now are sort of taken by what's going on with code. I have sort of this viral moment right now where I got to 40,000 stars this morning. Oh, wow. On G-Stack. So it's like, oh, this is an open source project that now is one of the biggest ones. And I have more than 100 PRs from contributors to deal with. I guess you're one of the best people to talk to about this because you're actually literally coming up with something that is a totally different pathway.

`[01:51]` **SPEAKER_03:** That's right. That's right. So what we're doing at NDIA is we're doing program synthesis research. And when I talk about program synthesis, often people ask me, oh, so are you doing like Cogen? Are you building an alternative? Are you building a new project? Are you building an alternative? I'm actually building an alternative to coding agents. And it's actually not at all what we are doing. We are working at a much, much more, much lower level than that. What we're actually doing is that

`[02:11]` **SPEAKER_03:** we are trying to build a new branch of machine learning, an alternative to deep learning itself, rather than like coding agents. Coding agents are like this very, very high level, last layer piece of the stack. And we're actually trying to rebuild the whole stack on top of different foundations. So we're building a new learning substrate that's very, very different from parametric learning, deep learning. So if you go back to the problem of machine learning, you have some input data, some target data, and you're trying

`[02:42]` **SPEAKER_03:** to find a function that will map the inputs to the targets and that will hopefully generalized to new inputs. And if you're doing deep learning, what you're doing is that you have this parametric curve that serves as your function, as your model, and you're trying to fit the parameters of the curve gradient descent. And this is basically basically what we are doing, except we are replacing the parametric curve with a symbolic model that is meant to be as small as possible. It's like the simplest possible model to

`[03:15]` **SPEAKER_03:** explain the data to model what's going on. And of course, if you're doing that, you cannot apply gradient descent anymore. So we are building something that we call symbolic descent, which is like the symbolic space equivalent of gradient descent. The idea is to build this new machine learning engine that's giving you extremely concise, symbolic models of the data you're feeding into it, and then we're going to make it scale. And so everything you're doing with machine learning today,

`[03:44]` **SPEAKER_03:** with parametric curves, we should be able to do it with symbolic models in the future, in a way that will be much, much closer to optimality. Much closer to optimality in the sense that you're going to need much much much less data to obtain the models. The models are going to run much more efficiently at inference time because they're going to be so small. And because they're so small, they will also generalize much better and compose much better. You know, the minimum description length principle that the model of the data that

`[04:14]` **SPEAKER_03:** is most likely to generalize is the shortest. And I think you cannot find a model like this. If you're doing parametric learning, you need to need to try symbolic learning.

`[04:23]` **SPEAKER_01:** That's fascinating.

`[04:24]` **SPEAKER_02:** So the rest of the industry is just pouring more and more billions of dollars down in the air with a more complex and expensive approach to computing, but also with the bigger one. So we're in a the fiscal crisis, so how do you see how to work in the future about

`[04:38]` **SPEAKER_03:** this new approach that was set years ago. Can you help make the case for why you think that it's the right thing to explore alternate approaches instead of just to keep putting more money into the current approach? I mean, everybody is, is, you know, building onto the LLM stack these days, which makes sense because, you know, the returns aren't there, like it's actually working. have everybody working on the same thing. Like I personally don't think that machine learning or AI in 50 years is

`[05:05]` **SPEAKER_03:** still going to be built on this stack. I think this is a stack that is very nice. Maybe it even gets us to AGI, but it's not as efficient as it should be. I think it's inevitable that the world of AI will trend over time towards optimality. And so I'm trying to sort of like leapfrog directly to optimality, like to build the foundations of optimal AI today, but in general, you know, our vision is very ambitious and I'm not saying that we're going to be successful. Like we have maybe a 10 or 15% chance of success, but that is

`[05:39]` **SPEAKER_03:** enough that it's worth trying, right? And I think in general, like among listeners, if you have a big idea and it has very low chance of success, but if it works, it's going to be big and no one else is going to be working on it, right? It's not something popular. It's not something... If you don't... If you don't do it, no one else will do it. And this is basically our situation. If you're in this situation, then you should try a chance. You know, you should go and work on it.

`[06:04]` **SPEAKER_02:** I mean, that's almost like the mission statement of Y Combinator, the thing that you just said.

`[06:09]` **SPEAKER_03:** Yeah. The reason it's important is that again, if we don't do it, no one else will do it. Right? So it's worth trying. Even if we don't succeed, it's worth trying.

`[06:15]` **SPEAKER_04:** Has the success, very specifically of the coding agents, I guess, built on top of the LLM stack, like has their success surprised you at all and in particular, like say over the last six months or so?

`[06:26]` **SPEAKER_03:** Yeah, absolutely. I think it has surprised many people. It definitely did surprise me. If you look at why everything is starting to work so well with coding agents, it's really because code provides you with a verifiable reward signal. And I think right now we're in this situation where any problem where the solutions you propose can be formally verified and you can actually trust the reward signal, it's not just some guess made by a model, any domain like this can be fully automated with current technology, with the LLM-based stack.

`[06:56]` **SPEAKER_03:** And code is sort of like the first domain to fall, but there will be many others in the future. I think mathematics is also primed to see a revolution in the next few years for the same reasons, again, because the domain just gives you verifiable rewards.

`[07:11]` **SPEAKER_00:** I guess the challenge for a formally verified domain is you have to somehow take a domain and make it verifiable, which is the trick. I mean, code is very natural. You could test, there's bugs, compiles, et cetera, and mathematics as well, where there are all the theorems and proofs work out, I guess because we're nebulous when you go a couple of degrees off where there are fields that are not naturally formally verified and you need to come with a, again, with some sort of a function to come up

`[07:43]` **SPEAKER_00:** with that reward that makes it verifiable with very fuzzy things, like let's say English language and composing the perfect essay, how do you make that formally verifiable?

`[07:55]` **SPEAKER_03:** Yeah, yeah, absolutely. I mean, writing essays is the typical example of a domain that's not verifiable. And so what you're going to see is that progress of reasoning models and based LLMs on this type of domain is going to be very slow because the stack we're using, like the LLM stack, is very, very reliant on its trained data. It's basically just operationalizing the trained data. And for writing essays, the trained data is coming from human experts, like annotating answers. And that's costly.

`[08:27]` **SPEAKER_03:** So you're going to see this very, very slow progress. Maybe, maybe it's even going to stall. But for any, any verifiable domain, like tech code, for instance, which was the big unlock, is when people started creating this code-based training environment for post-training, where the reward signal, the verification signal is provided by things like unit tests and so on. And so that means that the model was not just working from human-provided annotations. It was actually trained. It was actually trying some things, verifying the answer, and generating a lot, lot more trained data in the process, a much denser coverage of the problem space, and not just coverage in terms of, like, is the answer right or wrong, but also starting to build models of the execution traces, right, so that the models could start incorporating an execution model.

`[09:20]` **SPEAKER_03:** Very much the way that human programmers, you know, when they look at code, they're sort of like executing the code in their mind. They keep track of the value of variables and so on. It's also what the models are trying to do now, and this is why it's working so well. And it's possible because you're working with this very formal, fully verifiable environment. You cannot do that with SSS. You cannot do that with, you know, LAW or many other problems.

`[09:41]` **SPEAKER_00:** I think I really like how you define intelligence and how to measure it, which brings to the question of also sharing, having you share the history of ArcGIS.

`[09:52]` **SPEAKER_03:** Yeah. So my, my definition of general intelligence. You know, many people around the industry these days, they say AGI is going to be a system that can automate most economically, economically valuable tasks. And to me, that definition is it's about automation. It's not about intelligence. It's not about general intelligence. So my definition is AGI is basically going to be a system that can approach any new problem, any new task, any new domain, and make sense of it, like model it, become competent,

`[10:26]` **SPEAKER_03:** add it, uh, with the same degree of efficiency as a human could. So meaning it's going to need basically the same amount of training data, uh, and training computes as, as a human would, which is, which is very little, like humans are really, really, uh, data efficient. So general intelligence is human level skill acquisition efficiency on the, on the same scope of tasks that, uh, humans could potentially, uh, learn to do.

`[10:52]` **SPEAKER_02:** Do you think it's possible that we will accomplish the first definition? Of AGI, the automate most economically useful work before we accomplish your definition? Absolutely.

`[11:01]` **SPEAKER_03:** I think that's, that's a trajectory that we're on right now. And I think it's already true that in principle, current technology can fully automate at human level or beyond any domain where you have, uh, very favorable rewards. Right. And code, code being the first one. And I think figuring out AGI, figuring out like human level, uh, you know, learning efficiency over arbitrary tasks, that's probably going to take. Uh, a different sort of technology, different, a different mindset, different approach.

`[11:29]` **SPEAKER_02:** Do you think that LLMs can be bent to have the same sample efficiency as humans? Or do you think it's like fundamentally just impossible and we need a new approach? And that's, that's the thing that you're hoping, hoping to solve.

`[11:41]` **SPEAKER_03:** With enough compute, everything starts looking like everything else, every like computer grad equalizer, every approach starts looking the same. And I think it's possible in principle to build something that looks a lot like AGI on top of the LLM stack. Uh, but it's not going to be LLMs per se, it's going to be this new layer, perhaps, you know, it's going to be even a few layers above, not just one layer above, but a few layers above. Uh, but it, you, you can build it on top of, uh, LLMs because LLMs are kind of computer, right?

`[12:10]` **SPEAKER_03:** Uh, I do believe, however, this would be the wrong thing to do because it would be very inefficient. I think AI, AI research will have to trend towards not just efficiency, but in fact, optimality over time. And for this reason, future AI. In a few decades, uh, it's not going to be this, uh, harness on top of, uh, reasoning model on top of a basal LLM, uh, it's going to be much, much lower than that.

`[12:35]` **SPEAKER_02:** To Diana's question. Do you want to talk about how you actually designed ArcAGI and why it's a good barometer of that?

`[12:40]` **SPEAKER_03:** I mean, I, I, you know, I've been doing deep learning for a very, very long time and initially my, my, my tech, my mindset was that deep learning was going to be able to do everything.

`[12:50]` **SPEAKER_00:** You were the creative at Keras before even all the other frameworks became very popular.

`[12:55]` **SPEAKER_03:** That's right. That's right. I was, uh, trained deep learning model, uh, uh, for natural language processing, in fact, in, uh, 2014. And, uh, from that work, uh, you know, I actually started, uh, developing this open source library, which I released, uh, in fact, uh, exactly 11 years ago, uh, March, March, 2015. Uh, so it was Keras and, and then it got popular and then I ended up, uh, sort of like doing less of the research that I, that I had started Keras for and, uh, more of working on the framework.

`[13:25]` **SPEAKER_03:** Itself just because it has really, really good product market fit. And so my, my tech, you know, around that time, around like 2015, 2016 was that deep learning was extremely general, that you could do everything with deep learning that you didn't need in anything else. It was sharing complete. So, uh, my tech was basically a deep learning was differentiable programming. Uh, so anything you would do with software, you could, in principle, train a deep learning model on the right inputs and outputs to do the same thing.

`[13:53]` **SPEAKER_03:** And, uh, in, uh, 2016. I was doing, uh, research at Google Brain on trying to train deep learning models to help with, uh, reasoning problems and in particular, uh, uh, first order logic problems, uh, uh, theorem proving and so on. And I started finding that you could not really get gradient descent to encode, uh, uh, sort of like reasoning style algorithms. It was not because the models could not represent these algorithms. It was. Because gradient descent could not find them. Right.

`[14:29]` **SPEAKER_03:** So the problem was that, it wasn't about deep learning, not being trained complete or anything like that. Like that was not the problem. The problem was gradient descent, right? Gradient descent would not find generalizable programs. It would instead, uh, end up doing, uh, over fit pattern matching, right. Uh, over, over sequences of, uh, uh, input tokens.

`[14:47]` **SPEAKER_01:** Which I guess people could argue, like, that's what's happening.

`[14:50]` **SPEAKER_03:** I mean, it's, it's useful to see what's happening today in a, in a, in a slightly. It's. It's a. It's a slightly higher, higher level version of that.

`[14:57]` **SPEAKER_00:** It's with a lot of data. So it doesn't feel like overfitting because the data has a lot more distribution. Yeah.

`[15:01]` **SPEAKER_03:** With a lot more data. And also, I think models today, uh, they're a lot more compressive after data, which is why, why they, they generalize better.

`[15:08]` **SPEAKER_01:** All models are wrong, but some models are useful. And then I guess what I'm hearing is like your method might find the right model.

`[15:16]` **SPEAKER_03:** That's right. That's, uh, that's, uh, where, where the, uh, idea came from. And that was like, you know, at the time back in 2016, 2017, I was like, okay, we are going to need a, a benchmark to capture these ideas. Uh, we're going to need a program synthesis benchmark. And, uh, my, my mental model for that was ImageNet. I was like, oh, I'm going to make the ImageNet of reasoning. So I started brainstorming a few ideas around like 20s, 2017. I explored many different things. Uh, I tried working with, uh, in particular cellular automata, like, uh, uh, a setup where you show a model, uh, cellular automata outputs, and it must recreate

`[15:55]` **SPEAKER_03:** the program that generated them, like that sort of thing. Uh, and eventually I settled on the, uh, ArcGIS format, uh, around like early 2018. You know, I was doing this on the side. It was a side project. Like my main project was, uh, developing Keras at Google. I wasn't moving very, very fast, uh, on that. Uh, so summer 2018, uh, I wrote the Arc task editor, and then I started just making lots of tasks by hand. And about one year later, I had made 1000 tasks. And so. I wrote up, uh, the paper that was explaining what this was about, what the big idea was, like intelligence as a, as a skill acquisition efficiency.

`[16:33]` **SPEAKER_03:** And, and I published, uh, all of that in, uh, in 2019.

`[16:36]` **SPEAKER_00:** In parallel, GP3 2020 was coming out and starting to show signs until the chat GPT moment around 2022, end of the year. And the industry took off with that. And this was one of the benchmark that was really performing really badly. And it was very obscure. I don't think many people. Knew about it. It was mostly niche research communities that maybe read your paper.

`[17:00]` **SPEAKER_03:** Yeah. People who worked on programs, this is new, but it's, uh, but a lot of people who worked on, on deep learning, on scaling up LLM stadium, really care for it. And part of the reason why is because LLMs did not work well or at all on the benchmark for a benchmark to capture the attention that the research community needs to start working a little, right? Uh, if it's too hard, people are going to, are just going to dismiss it.

`[17:24]` **SPEAKER_01:** You're just ahead of your time, clearly, because we're not on arc AGI one anymore. And then two is reaching saturation and then three is out now. Yes.

`[17:36]` **SPEAKER_00:** And I think the cool thing about arc AGI, it has been a very good barometer for the industry of the big changes that happen because V1 was not working at all for a long time until 2025. When reasoning models came.

`[17:55]` **SPEAKER_03:** Yeah, absolutely. If you look at, uh, performance on arc V1 first and then V2, uh, so basal LLMs, uh, were scoring extremely low on V1, like sub 10%, basically. And I mean, it was true of, uh, the original lag GPT-3, uh, actually scoring zero, but that's even true of the latest basal LLMs today, you know, as of, as of March. Without reasoning. Without reasoning. Without reasoning. Yeah. So the base models. So performance of, uh, of basal LLMs on. On the V1 stayed very, very low, even though in the meantime, you know, we had scaled up these models by 50,000 X, right?

`[18:32]` **SPEAKER_03:** So it was really telling you that, you know, more scale, scaling up pre-training alone was not going to crack the benchmark. This was not enough to demonstrate that the model had fluid intelligence. And then, uh, the moment, uh, models starting performing well on arc one was with the first reasoning models, in particular, uh, the, the OpenAI 01. And then all three, uh, models, which by the way, they were demonstrated by OpenAI on arc, because it was the one unsaturated reasoning benchmark that was really showing that this model was different, like that new capabilities that we had not seen before.

`[19:07]` **SPEAKER_03:** And so with reasoning models, you start seeing this sudden, like step function change, uh, on, on arc one. And so arc one was really the benchmark that signaled that at this moment in time, something was happening.

`[19:20]` **SPEAKER_00:** Something big.

`[19:21]` **SPEAKER_03:** Yeah. Something big, like new capabilities were. Mm-hmm. Emerging. Like reasoning was new and different, and it was actually not obvious at the time. Like, you know, I don't know if you remember when, uh, when, uh, uh, O3, uh, Preview was, was announced by OpenAI.

`[19:36]` **SPEAKER_00:** That was end of 2024, actually.

`[19:37]` **SPEAKER_03:** Yeah, December 2024. And like, sure, it was like a, a, a huge step function progress on arc, uh, but it was very expensive. It did not really have, uh, product market fit effectively. But if you looked at, uh, at arc results, you knew that this was big and important. And then we released arc two, which was the same format, but, uh, more difficult, like with more, uh, uh, composition, uh, uh, at the level of the, the, the reasoning chains. And what happened is that, so the, the earliest reasoning models started very, very low on arc two, and then around the same time as, uh, coding agents started working, you saw this.

`[20:15]` **SPEAKER_03:** Just last year. Yeah. So very, very recent, just a few months ago, you saw this, uh, uh, a very, very fast, like, saturation, uh, of arcs. And so again, like arc two signaled that, yes, there was this, uh, this new set of capabilities emerging. So I think the benchmark did a really good job at capturing the advent of reasoning models and then the advent, uh, of agentic coding. Like this, this new pattern where if you have, uh, verifiable rewards, then you can basically fully automate, uh, the domain, which by the way, is true of arc.

`[20:45]` **SPEAKER_03:** Like arc does provide a verifiable reward.

`[20:48]` **SPEAKER_01:** I guess for v2, what, what caused the, so one was clearly reasoning. Two, a benchmark. So right, so you, you, so a benchmark was clearly the, the, uh, process. Uh, you saw this argument of, of, of a programming model.

`[21:01]` **SPEAKER_03:** Uh, a benchmark because it's very, very, very high value. It's like a very, very low, I, a very low value. Uh, so, so this graph is showing, uh, uh, of, of a, of a model, because this is, this is a very basic, uh, algorithm. Yeah. Uh, so, uh, and this, this, this is a, this is a case where you, you, you, you use the algorithms to, to, uh, eliminate the behaviors and the factors that you, you, you use. Yeah. like those in the benchmark and then you try to solve them using let's say let's say program

`[21:28]` **SPEAKER_03:** induction for instance uh still using your reasoning model then you verify the solution again it's very viable so you can you can trust the answer and then you fine-tune the model on the successful reasoning chains and then you keep repeating like you generate new tasks you solve them you verify the solution you fine-tune the model on the reasoning chains and you can keep doing this millions of times right like you just need to spend more money yeah this is the rl loop that this is happening yeah and the the new paradigm in ai is basically that any domain

`[22:00]` **SPEAKER_03:** where this is true where you have uh the ability to join this uh this is a true uh verification signals you you can run this this kind of loop right if you can run this kind of loop you can mine uh you can brute force mine effectively the entire space and get extremely high performance this is basically the the process through which octo was saturated so what it tells you is that it's not so much that the models have higher fluid intelligence uh than than they did with the with the first using models it's just that you have this new paradigm of post-training

`[22:30]` **SPEAKER_03:** and this is exactly what led to agency coding so it does matter it is it is valuable it is useful

`[22:36]` **SPEAKER_01:** it's not that the models are smarter it's that they're suddenly more useful it is possible to be more useful in particular domains without being smarter yeah clearly because that's means good things for me i'm not getting getting any smarter right now like at you know age 45 but you know i can learn how to do things and that's sort of what's happening with the models as of like late yeah absolutely when it

`[23:01]` **SPEAKER_03:** comes to uh competency there's always a trade-off between intelligence and knowledge if you have more knowledge if you have better training uh you need less intelligence to be competent and that's exactly uh what happened with the the rise of coding agents right the models don't have higher intelligence per se they don't have like a higher uh iq so to speak it's just that they're way better trained and they're way better trained in in two ways so they're not just trying to complete code

`[23:30]` **SPEAKER_03:** anymore they're actually trained via trial and error in these uh oil uh post-string environments with you know three word signals and also they're trained uh to embed this uh model of code execution right where they they they learn to keep track of the value of variables uh over an execution cycle and that's what what's leading to this extremely strong product market foods uh virginity coding today and street is completely changing software engineering this happened not too long ago the

`[23:59]` **SPEAKER_00:** saturation we actually had the founders of poetic that came and spoke about the approach which is really sounds like this new way of uh getting lms to perform is building this agent harness right and the hardness is basically structuring a problem domain into something that can be formally applied and they did that basically for arc v2 which when they released it they were at the top of the benchmark but then the crazy thing is i actually worked with the company in the winter 26 batch not too long ago called confluence lab which actually ended up saturating the v2 results with

`[24:37]` **SPEAKER_00:** 97 and i think their task cost was a lot more efficient too and the approach they basically took is similar to this i think they built the harnesses on top of it in order to get lms to to go and build different tasks and program through it which then for me i was like wow is this bad during the batch they only worked on it for a couple of months and they were able to saturate the benchmark that has been around for a long time it's like something special is happening

`[25:07]` **SPEAKER_03:** yeah yeah there's a lot of progress right now that's driven by custom harnesses around the task and the harness is basically a way for the the human programmer to um input into the model higher level like solution strategies basically i mean to me the fact that you need humans to engineer these harnesses is also a sign that we're short of agi today because if we had agi you know agi would just make its own harness it would not need to be told how to solve a problem it would just figure it out but it is very effective like harnesses i don't think they get us closer to agi

`[25:42]` **SPEAKER_03:** in any sense but it's a very valuable area of research because that can lead to task automation

`[25:50]` **SPEAKER_01:** and the last thing that i want to say is that we are now taking applications got a startup in you apply at ycombinator.com apply it's never too early and filling out the app will level up your

`[26:01]` **SPEAKER_00:** idea okay back to the video can you tell us about then what v3 is going to measure that's uh just

`[26:08]` **SPEAKER_03:** got released yeah absolutely so if you look at v1 v2 it was really focusing on your ability to produce like causal models that i was given to you so it was static it was passive and really focused on modeling and v3 is completely different we are trying to measure agentic intelligence so it's interactive it's active like the data is not provided to you you must go get it the idea is that your agent is dropped into a new environment which is kind of like a mini video game and it's not provided

`[26:46]` **SPEAKER_03:** any instructions it's not told what to do it's not told what the goal even is or what the controls even are and it must figure out everything on its own via trial and error so we are we are not just measuring you know that the ai's ability to model its environment we're also looking at its exploration efficiency its ability to acquire goals on its own like goal setting and of course its ability to plan through the model of the environment that's created and to execute the plan and so together you know all of these abilities we call that agentic intelligence and we are

`[27:26]` **SPEAKER_03:** looking for ai systems that could learn to play these games and you know crack them with the same degree of action efficiency as a human if you look at the human they are dropped into this new environment they try a few things they start understanding how things work uh they can they can solve the environment you know in in a few hundreds to thousands of actions we're trying to look for ai systems that could match uh this efficiency and we're trying to look for ai systems that could match uh this efficiency and we're trying to look for ai systems that could match

`[27:50]` **SPEAKER_03:** and by the way we know that all of these test environments in arc 3 are solvable by humans with no prior training because we actually tested them on on regular people yeah at first you just see this screen and you you know you have these keys available but you know what they do and you must figure out everything from scratch and humans are really good at that by the way they're really good at exploring efficiently with making sense of something new and eventually cracking the game and frontier models today they're

`[28:20]` **SPEAKER_02:** very good at it if the reasoning models cracked v1 and the like reinforcement learning environments cracked v2 do we need a new advance to crack v3 to the to even the best techniques currently like

`[28:33]` **SPEAKER_03:** not work yeah i mean i'm pretty curious to see how frontier labs are going to react to v3 and how they're going to start to target it um it is designed to be more resistant uh to the same kind of targeting strategy as what we saw for v2 in particular like of course you can try to just make more arc three like games and then train your agents uh in them um but the thing is we've uh deliberately tried to create a private set of environments that is significantly different from the public set like you can look at the public set it's not actually giving you

`[29:09]` **SPEAKER_03:** that much information about what's in the private set in the private set you will have very different games with very different concepts and also the public set is meant to be substantially easier so your performance in the public set is not actually it's not representative of how well the system within private so for this reason it's going to be harder to target and that makes it a better test of fluid intelligence as opposed to a test of how much effort you put into into cracking it i'm so curious how do you come up

`[29:36]` **SPEAKER_03:** with these games they're so creative yeah we set up an entire video game studio right to create them so we got over 250 games uh and you know they're pretty quick to play like uh each game takes you maybe 10 minutes or or a bit less uh uh to play from scratch like upon first contact and we have like 250 plus and uh we set up this uh a very proactive game studio where we had any given week we had multiple games uh in progress we had like this this pipeline uh including you know design

`[30:09]` **SPEAKER_03:** implementation uh review human testing and and uh and uh many many iterations in order to make sure that those every player who gets the knowledge is하고 uh takes a question from you know the userна how long has it taken to actually provide that

`[30:26]` **SPEAKER_02:** feedback and that type of information um we line have of our colleagues who are in Мы want we limiting the

`[30:33]` **SPEAKER_03:** on pト making the視野 visto been working top of core knowledge priors like things like just just you know elementary knowledge like basic physics understanding of objects understanding of the notion of agents for instance like an agent in objects with goals and intentions but we are not incorporating any language any like cultural symbols like you know arrows for instance or the color green meaning go and color red meaning start that sort of thing uh there's no external knowledge that's involved uh in these games it's

`[31:17]` **SPEAKER_00:** like one of those uh iq tests that are just pattern matching but now it has time series

`[31:20]` **SPEAKER_03:** yeah uh it's not just time series it's interactive you must create your own path through game space right you must you know in in in an iq test like problem like you know what arc one and two is the data that you must model is provided to you you already have the data you just you just need to find the causal rule to explain it with r3 actually must gather the data and you must do so efficiently like of course you could say well i'm just gonna you know brute force mine uh the space of every possible game state and then i find the solution you

`[31:56]` **SPEAKER_03:** cannot do that because if you try to do that you would score extremely low even if you manage to solve the level because you're scored on your efficiency you must match human level efficiency

`[32:06]` **SPEAKER_01:** it's funny it's like almost a coming full circle this level of agi with games sort of is the match pair to openai writing i mean you know tom brown uh one of the co-founders of anthropic had to write like the harness code to allow like the you know pre-gpt

`[32:24]` **SPEAKER_03:** ai at openai to play starcraft yeah yeah opening i worked on uh on uh in particular on the on dota 2 then the openai 5 model which was very good correctly so this was like not just pre-gpt but i also mostly pre-trial transformers because they were working with a stack of lstm uh layers if i recall correctly and even before opening eye uh deep wine worked a lot on video game uh you know solving video games yeah deep isle uh and they were the first to do uh atari games right back in 2013 that you

`[33:00]` **SPEAKER_03:** know they were very very early very visionary in that sense to work on on this problem so early with these methods which are still very modern methods so the big difference is that if you look at atari games for instance or even dota you're training on on the same environment as what you use for testing so effectively you're just trying to memorize the best strategies you're trying to at training time explore the full space of possible game states and productionize operationalize uh that knowledge into into into the model and then at inference time you're

`[33:39]` **SPEAKER_03:** basically just recalling that knowledge and that's explicitly what you are trying to avoid with arc 3 uh you're not playing games uh that you've seen before you're not playing games that you've been trained on like for millions of files like the opening i5 model for instance was playing a restricted version of dota 2 and it was trained on like tens of thousands of hours of gameplay effectively i think maybe in millions but it's just an insane amount of training data with arc 3 you're being evaluated on games that you think for the very first time and every action you spend

`[34:14]` **SPEAKER_03:** exploring is counted towards your efficiency score right so you're really focused on measuring fluid intelligence your ability to efficiently explore efficiently produce a world model of the environment and then use this model to infer goals uh plan towards these goals

`[34:34]` **SPEAKER_01:** and eventually crack the game one of the arguments for um you know endia is that you're able to do all of the intelligent tasks for you know an arc task might be like 0.3 you know cents for an arc task but you know for the same task on a foundation model with llms it's you know a dollar to ten dollars and then there's this other aspect that we've been tracking where it seems like uh more and more intelligence um at least on the llm side uh can be distilled down into smaller and smaller models and so on the

`[35:08]` **SPEAKER_01:** one hand like they're scaling up but then they're like distilling smarter and smarter small models i guess your approach might indicate that it's not billions of parameters like the you know endia achieving agi might not be you know sort of inherently a scale thing at all there's a platonic ideal of the endia model that achieves agi yeah do you ever think about it in terms of

`[35:33]` **SPEAKER_03:** like well it would fit on a floppy disk well okay there are two things to separate that's the sort of like fluid intelligence engine i think it's going to be a very very small code base uh in a very small set of models that's fitted with it and it's probably going to be on the order of megabytes right and then you have the knowledge base so to speak uh that's going to be layered below this this fluid intelligence engine like you know fluid intelligence has to draw on some knowledge and that knowledge is going to take up a lot more space so i think it's it's it's

`[36:08]` **SPEAKER_03:** important to differentiate the two i do believe that you know when you create a gi retrospectively it will turn out that it's a code base that's less than 10 000 lines of code and that if you had if you had known about it back in the in the 1980s you could have done a gi back then using the computer resources available wow that's a crazy prediction that's i think retrospectively this

`[36:31]` **SPEAKER_02:** will turn out my god to be true wow so it was just like hiding under our noses in plain sight for like 40 years it took us like 40 years

`[36:38]` **SPEAKER_01:** yeah that's right that's right well that second thing sounds like douglas lenat's like psych project or is that the wrong way to think about it it's like there's sort of knowledge about the world yeah and then there's methods like the program what i hear is like the program might be 10 000 lines and then it operates online knowledge base it's very large so the problem

`[36:57]` **SPEAKER_03:** with psych uh i mean there were many issues with it but one of the big issues is that

`[37:02]` **SPEAKER_01:** uh there was no learning involved yeah it's just the knowledge like the knowledge wasn't crafted symbolic knowledge and it was probably inaccurate the way you want to be building a gi is that you

`[37:13]` **SPEAKER_03:** want to be removing humans uh from from the improvement loop as much as possible you don't want a system where every improvement in system capability has to involve a human engineer doing something it's actually the strength of deep learning and foundation models is that you can just scale up the knowledge base like an llm is effectively knowledge base it's a bank of you know uh vector programs that map patterns of input tokens to patterns of output tokens and you can scale up that knowledge base by just adding training data and training compute with no

`[37:49]` **SPEAKER_03:** further human involvement i mean of course there's still a little bit of human involvement in making sure the training job completes but it's it's minor you've managed to remove humans from this improvement loop as much as possible and that's also what we want for our system we want a system that's self-improving where the improvements are sounding meaning that every time the system increases capabilities it's also increasing the

`[38:13]` **SPEAKER_01:** rate at which it increases its capabilities i think this is a pgism it's like i'm sorry the essay is so long uh if i had more time i would make it shorter yeah when you're looking at the heart problem it's

`[38:25]` **SPEAKER_03:** actually harder to produce a short elegant concise solution than the message of the engineered

`[38:31]` **SPEAKER_01:** solution yeah you can brute force it but you know the more elegant version is very very short and that's kind of like what you said with

`[38:38]` **SPEAKER_03:** how this might come about yeah this is literally the shape of the type of ai approach we are creating and i think this is also the shape of science itself like science is fundamentally a symbolic compression process where you're looking at a big mess of observations like you know the position of planets in the sky or something like that and you're compressing that down to a very simple symbolic rule you're saying like yeah like all these new thousands of observations actually just all at this one simple equation that's symbolic compression and to do this by the way

`[39:17]` **SPEAKER_03:** you need the model uh to be symbolic like you you could not fit a curve and say well you know that that kills my model that would never be optimal this would never be concise or elegant enough and that's not what science is doing science is not about curve feeling science is about finding the equation finding the most compressive symbolic model of your pile of And that's the process that you are trying to recreate in software form. Like you could say that the NDI approach to program synthesis is that we are building

`[39:46]` **SPEAKER_03:** science incarnate, the scientific method in algorithmic form.

`[39:51]` **SPEAKER_02:** I'm curious if you compare it to biology. Clearly, LLMs don't learn the way that humans do because no baby reads the whole internet. Do you think program synthesis is closer to the way that humans learn? Or do you think that's yet a third branch where even if program synthesis is correct, there will be some yet as undiscovered third way to do it, which is the thing that we do?

`[40:13]` **SPEAKER_03:** I think so. I do think humans do some amount of program synthesis. I think the way humans learn and the way the human mind works is very messy. It's not like there's one simple, elegant principle behind it all. It's an implementation of fundamental principles, the fundamental principles of intelligence, which, you know, I think we can. Identify these principles and reimplement intelligence from scratch from first principles in a way that will be much more efficient than the human brain.

`[40:45]` **SPEAKER_03:** I think the human brain is messy and it can be a good source of inspiration for AI. But I think it would be counterproductive to just try to, you know, observe it and reimplement it and make it biologically plausible. I think that's counterproductive. It's not what we're trying to do at NDI. We're really trying to find what are the first principles. What are the first principles of intelligence and what is the system that would best implement them? But yeah, I do believe the human mind does at the highest level something that looks a lot like program synthesis.

`[41:16]` **SPEAKER_03:** Like we're currently building causal models of our surroundings. Like we're describing our surroundings in our mind as, you know, a set of objects and agents and relations between objects that are fundamentally symbolic and causal in nature. This is exactly the process. That lets us generalize so well and adapt so well to novelty on the fly.

`[41:40]` **SPEAKER_04:** I'm curious about NDI, the company, as you're building it. We've all here heard of the OpenAI founding story. And something that's always struck with me is just like both Sam and Greg say that it was a little odd in the early days because they didn't actually know what to do. It was like a bunch of people like hanging out in an apartment. I would love to hear kind of what's that been like for NDI? Like what did like the day one look like? And just maybe what's the first step? Yeah. Maybe for just people who are interested in starting these alternative approaches who don't have sort of a researchy background, how should they think about that?

`[42:11]` **SPEAKER_04:** Yeah.

`[42:11]` **SPEAKER_03:** So we started on day one with the symbolic learning vision. Like we basically knew that we wanted to do symbolic program synthesis, that you wanted to create a new approach to machine learning where you replace parametric curves with the shortest possible symbolic models. And then the big question was, okay, so how do we find these models? We started from the base. The base idea, which is still the idea that we're following today, which is that we are going to do deep learning guided program search, that you have a symbolic search space to explore.

`[42:46]` **SPEAKER_03:** And it's big. It's in fact combinatorial. You're not going to make progress if you just use brute force. It's not going to scale. You have to break the combinatorial wall. And the way to do it is to add deep learning guidance. It's actually very similar to the principles that underlies. Something like AlphaGo or AlphaZero. That was our starting point. We also didn't have very clear ideas about how to build it. So we tried many different things. We tried many, many different ideas. And it took us half a year roughly to get to good foundations where we could start building a system that compounds.

`[43:25]` **SPEAKER_03:** And I think that's what's really important when doing a lab like this, that you don't want to be in a situation where you're constantly trying something new. It's not reusing. Yeah. You don't want to have any learnings, any findings from the previous approaches. You want a compounding stack. You want to build reusable foundations and then the next layer and then the next layer. And of course, you want to be building onto the right foundation. So don't commit to the foundation layer too early, but also make sure that at some point you're building this compounding structure.

`[43:56]` **SPEAKER_03:** And that's the situation that we're in now.

`[43:59]` **SPEAKER_02:** Is Arc 3 the end or will there be an Arc 4, 5, 6? Can you keep making it harder?

`[44:04]` **SPEAKER_03:** Yeah, yeah. I think there will absolutely be Arc 4 and Arc 5. I mean, we're currently planning Arc 5. The point of the Arc AGI benchmark series is not to say that, well, you know, here's this test. If you pass it, this is AGI. Instead, what you're trying to do is we are targeting the residual gap of fair capabilities. Like Frontier is advancing and we're saying, well, if you compare it to human abilities, there's all this. There's all these tasks, all these things, it's not doing well, so we're going to create a benchmark to target that.

`[44:39]` **SPEAKER_03:** And so it's a moving target, right? It's not fixed points, it's a moving target. So there will be Arc 4, which will be in the spirit of Arc 3, but more focused on continual learning and curriculum learning at longer timescales. So you're going to have fewer games, but they're going to have way more levels and the levels are going to be compounding, meaning that for each level, you need to reuse stuff that you've learned before. Yeah. And then there's going to be Arc 5, and I'm actually really, really excited with Arc 5.

`[45:08]` **SPEAKER_03:** It's very, very new and different. It's all about invention. And I mean, you will see what that means. Eventually, I expect we will run out of things to test. Like as we get closer to AGI, eventually there will be no measurable difference between human capabilities and partial human learning efficiency and Frontier AI. And when that happens, when it becomes effectively impossible to measure, it's going to be a very, very long process. So it's going to be a very, very long process. And it's going to be very, very long process.

`[45:34]` **SPEAKER_03:** So it's going to be a very, very long process. But it's going to be very, very long process. But it's going to be very, very long process. This is the AGI moment.

`[45:36]` **SPEAKER_01:** Well, then the machines will take over and then they will create Arc ASI 1. Yes. And then it will continue from there. Yeah. If you had to put a guess, I mean, years, decades, months.

`[45:50]` **SPEAKER_03:** My timeline to AGI, you know, if you just try to extrapolate from the current rate of progress and the amount of investment that's going into not just the LLM stack, but also large numbers of怪. like, uh, side ideas, side bets that might work out like, you know, India, for instance, I think we're probably looking at AGI 2030, early 2030s, uh, most likely. So around the time, uh, the two are going to be releasing like maybe arc six or arc seven, uh, that's probably going to be AGI.

`[46:25]` **SPEAKER_02:** You guys are doing a different approach to LLMs. Um, do you think there's room for more startups to explore other new approaches and are there any other ones that you think are promising that don't have time to explore yourself?

`[46:37]` **SPEAKER_03:** Yeah, absolutely. I mean, there are many different approaches that you could try. I've said like compute is a great equalizer. I think if you look at the amount of compute and resources that we've thrown at, uh, deep learning and, and gradient descent and, and scaling that up, if you had thrown the same amount of investment into almost anything else, you would also have seen extremely exciting results like genetic algorithms, for instance. Uh, if you try to scale up genetic algorithms, I mean, I'm sure you can do incredible

`[47:07]` **SPEAKER_03:** things with that. Um, you could, you could in fact probably do new, new science, uh, because, uh, that's based on search and search is the, is the, is the best fit for, uh, automating the scientific method. Uh, I think so right now there's also like approaches that, uh, build on top of the current stack with their slightly alternative, like, uh, state space models, for instance, uh, there's, uh, the, the XLSCM architecture, like you can basically, you know, current frontier. It's, it's, it's a stack of things and you, you can take any layer in the stack

`[47:38]` **SPEAKER_03:** and try to propose an alternative. Like if you propose an alternative architecture, uh, you can be doing, for instance, like, yeah, like more like, uh, recurrent models instead of transformers, uh, for, for the architecture. Uh, you, or you can do even lower level. You're going to be like, okay, we're still going to be training, uh, parametric curves, but you're going to get rid of grand descent, right? We're going to use like search. Maybe you're going to do new evolution. Uh, that's, that's lower level and the.

`[48:03]` **SPEAKER_03:** The lowest level is, uh, the low, the level where, where we're operating, where we're saying, well, actually, uh, forget about curves, uh, forget about parametric learning, forget about grand descent. We're just going to do something completely different. Um, and I think if you want to build optimally, either kind of forced to go back to the foundation of the stack, it cannot be like, uh, uh, one, one layer added on top of the pile.

`[48:28]` **SPEAKER_00:** So do you think for aspiring researchers to want to do a new Neo lab with a different approach? Yeah. You should be reading research papers from the seventies or eighties and go deeply in those with approaches that were not as invested nowadays.

`[48:41]` **SPEAKER_03:** That is actually a great idea because, uh, earlier in the, in the history of the AI research timeline, people were exploring more things and very different things. You've had this sort of like collapse of everything into one approach. So it's actually kind of a bad idea. Uh, like consider that not too long ago, like about, about 20 years

`[49:03]` **SPEAKER_00:** ago, we had the collapse into SVMs too.

`[49:05]` **SPEAKER_03:** Yeah. I mean, it's, it wasn't, I wouldn't describe it as a collapse because there weren't that many people doing SVMs and the AI was a much, much smaller field back then, but there was this, uh, uh, widespread understanding that neural networks were, were a failed approach that neural networks didn't work. And it was a waste of time to, to, to keep trying.

`[49:25]` **SPEAKER_00:** In the nineties, right?

`[49:26]` **SPEAKER_03:** Yeah. No, even, even in the, in the, in the late 2000s, this was a set of things, uh, basically like when, when I got into, into AI, uh, people are telling me like, Hey, neural networks, don't, don't try that. I was like, yeah, but it, it looks a lot like what the brain is doing. Like I'm, I'm interested in that. If everybody's working on something, you are discarding ideas that will, uh, actually turn out to be very proactive ideas, right? And yeah, like back in the seventies, back in the eighties, people are trying

`[49:53]` **SPEAKER_03:** more things and I think Genetic Algorithm is actually a very good example of that. Uh, I think this is an approach that has a tremendous amount of potential. But there's, there's not too many people are looking into scaling it up, uh, deeply.

`[50:07]` **SPEAKER_01:** Are there any characteristics that you would be looking for? I mean, is it as simple as like, if there's a scaling law that could happen, then even if it's a different, or is it, is that too like, you know, thinking by

`[50:21]` **SPEAKER_03:** analogy, I think you are looking for approaches that scale. Yeah. Uh, I think it's, it's a non-starter. If you're working on something, but the only way to increase the capabilities of the system is to have, uh, human engineers and researchers spend time on it. It will not work because even if the idea is very clever and very elegant and works really well, capabilities are going to be bounded, that can be bounded by human investment, right? You want to be in a setup where the system can improve its capabilities with no human

`[50:52]` **SPEAKER_03:** in the loop, with no human.

`[50:53]` **SPEAKER_01:** So you would say like, don't just do it the way we did it like 10 years ago. Do it with the idea that recursive self-improvement is baked in at the beginning. Yeah.

`[51:02]` **SPEAKER_03:** Not necessarily recursive self-improvement because deep learning for instance is not, is not recursively self-improving, but with the idea of scaling up with no human bottlenecks, you want to remove the human from, from the improvement loop. The great strength of deep learning is that the models got better and better simply by adding, uh, uh, training, training compute and training data. I mean, it's, it's a little bit of caricature because of course, just adding these factors requires a lot of human involvement, but basically that's the idea that you have these

`[51:32]` **SPEAKER_03:** things. It is decoupling from, uh, the improvement curve and the amount of human effort that's needed to be injected into the system.

`[51:39]` **SPEAKER_02:** Yes. Or human effort that's already happened because the LMS do actually require an enormous amount of human effort. It's just, it was the human effort to build the internet and we'd already built it.

`[51:47]` **SPEAKER_03:** Yeah. Actually less and less now, uh, that we are doing, uh, training in, uh, interactive verifiable environments, because then you only need a small amount of human effort to create the environment. And from that small amount of effort, you're, you're. You're creating exponentially more training data, but at first I think to sort of like prime the machine, you need this tremendous amount of, uh, of, uh, uh, human generated abstractions and call it in text data. And if you, if you don't start from that, you, you cannot get the system into this loop.

`[52:21]` **SPEAKER_01:** Do you have any advice for me, uh, starting a open source project, things to do things not to do in, uh, in the AI space, because I am. Uh. Not sure how I signed up for this in the last 14 days, but I think I have, I don't know, on the order of like 10 to 30,000 people using G stack every day.

`[52:41]` **SPEAKER_04:** That's wild. Yeah.

`[52:43]` **SPEAKER_01:** And I don't know, like, I have a job, I guess, like, you know, what was it like to start Keras and how did you keep maintaining it? How what's a good maintainer? Like, what did you learn from that? I don't know. This might be a whole hour. Yeah.

`[52:57]` **SPEAKER_03:** I mean, that's lots of learnings from too many things. I'm growing, growing. Uh, so right now I'm less involved with it. Uh, there's a big team at Google that's working on it and they're doing an amazing job.

`[53:09]` **SPEAKER_01:** So it is possible to not to, you know, to put people together to like, it is possible to start something.

`[53:14]` **SPEAKER_03:** It is possible to start something that's a relief and, and, and then get more people involved. And at some point it becomes its own thing. And it's just, you know, it used to be your baby, but now it's all, it's all grown up and it's an adult and, and, and going on with its own life. So if you ask me the, the, the factors that remade care successful, um, I mean, first of all is that there was this big focus on, uh, making the, the API simple and intuitive. There was this big focus on usability, and this was inspired by scikit-learn like scikit-learn

`[53:45]` **SPEAKER_03:** was sort of like the OG, uh, machine learning library for Python. And what made it successful was that it was so easy to get started with it. So at first I was like, okay, uh, I'm gonna package, uh, all this functionality I've created under really, really simple API is gonna be like the scikit-learn. That was like the big idea. The focus on usability is not just making sure the API is simple. It's also making sure the entire onboarding experience is nice and easy. Like the docs should be very informative.

`[54:14]` **SPEAKER_03:** You should, you know, the docs should be not just telling you about how to use this thing. They should actually be teaching you about the domain in the first place, because the, the folks who land on your website, they're not gonna be already deep learning experts. They're gonna be people looking to maybe choosing deep learning. And so you, you have to teach them not just how to use the tool, but where the tool is good for, um, and, and the entire field around it. And then, uh, you know, you have to put a lot of investment into community building.

`[54:45]` **SPEAKER_03:** Um, one thing we, uh, we did a bit, uh, at Google, in fact, you know, Google made it kind of, kind of difficult. And, and I was sad about that is, uh, hire your power users, like hire your fans. This, this is a really, really good idea. Yeah. Like find, find the, the most enthusiastic. Yeah. users from your community and, and, and just hire them on your team. Amazing. Yeah. And, uh, these, these, these, these are the, always the best people, right?

`[55:11]` **SPEAKER_01:** All right. Time to start gstack.org. Mm-hmm. Uh, put in a bunch of my own money and then hire a bunch of people to work on it. That sounds good. I think you've been a leader and pioneer and we're so lucky to have you sit with us. There are people watching who are at the beginning of their, you know, adulthood, even like their certainly their professional careers. Uh, or actually like people. just around the world they're like trying to understand like what does this mean as intelligence

`[55:36]` **SPEAKER_01:** becomes broadly applicable like what would you tell you know if you were 18 right now what would

`[55:43]` **SPEAKER_03:** you tell them yeah i mean there's a lot of people today who are very pessimistic very negative takes but the rise in your capabilities they say oh you know i'm going to be out of a job soon and that's going to be mass unemployment uh yeah it's just going to take over completely and my my take is actually you know the more you know the more expertise you have but things like programming for instance the better you're able to use and leverage these tools for your own benefit and with the right kind of expertise uh all this ai progress is actually empowerment like it's

`[56:20]` **SPEAKER_03:** something that you can leverage for yourself i mean that's that's exactly what you did with your project right yeah and yeah more people should have this mindset of trying to learn as much as possible not just about ai uh but about the domain that they want uh to apply ai to right so that they should they should seek to turn this uh this this new development into an opportunity into into a tool they can use for themselves to improve their own lives i think that's that's the right mindset because you know you're not gonna stop uh ai

`[56:51]` **SPEAKER_03:** progress i think i think it's too late for that and so the next question is okay like ai progress is here it's actually going to keep accelerating how do you make use of it how do you leverage how do you

`[57:01]` **SPEAKER_01:** ride the wave that's the question to ask i wish we could uh keep going for a couple hours because i'm sure we could francois thank you so much for spending time with us thanks so much for having me
