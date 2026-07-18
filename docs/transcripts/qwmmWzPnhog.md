# 全文转录 · 我们都对 Claude Code 上瘾了:coding agent 时代的创业启示

> ▶ [YouTube](https://www.youtube.com/watch?v=qwmmWzPnhog) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/qwmmWzPnhog.md) &nbsp;·&nbsp; We're All Addicted To Claude Code
>
> 🗣️ 说话人分离识别到 **5** 位发言者(标注为 SPEAKER_00 …)。

`[00:00]` **SPEAKER_02:** I feel like when I'm using Cloud Code, it's like, oh, I feel like I'm flying through the code.

`[00:03]` **SPEAKER_01:** When it's in your CLI, this thing can debug nested, delayed jobs like five levels in and figure out what the bug was and then write a test for it and it never happens again. This is insane.

`[00:14]` **SPEAKER_02:** I think everyone who's experimenting with this stuff on like a hobbyist level or at like a very small startup, they're just pushing the coding agents as far as they can go. Because it's like, you don't really have time to figure out anything else. Like as a startup, you have limited runway. You're just going to orient around speed. I think at a bigger company, you have a lot more to lose.

`[00:30]` **SPEAKER_00:** What are some of the tips to become a top 1% user of coding agents?

`[00:35]` **SPEAKER_01:** Yeah, what's your stack?

`[00:37]` **SPEAKER_03:** Hey everyone, welcome back to another episode of The Light Cone. Gary, are you ready to record?

`[00:49]` **SPEAKER_01:** I'm in plan mode right now, but okay, yeah, I guess it's time. Sorry about that. Well, welcome to another episode of The Light Cone. And today we have an incredible guest, Kelvin French-Owen. He's one of the first people to create codecs at OPC. OpenAI. And before that, he started Segment, which is a multi-billion dollar company that got to a very successful exit. Kelvin, welcome back.

`[01:13]` **SPEAKER_02:** Thanks for having me.

`[01:14]` **SPEAKER_01:** I guess what a crazy time for all of us. I recently got very, very addicted to Cloud Code. And I would describe it as like 10 years ago, I was a marathon runner and I loved doing it. And then I suffered a catastrophic knee injury, which is called manager mode. And I... I stopped coding, which is tragic and horrible, but now the last nine days have been like this incredible unlock of all the things I remember being able to do. And it's like, you know, I got a new total knee replacement and actually it's a bionic

`[01:50]` **SPEAKER_01:** knee and it allows me to run five times faster. What's your take on it? Because you're, I mean, right out there at the forefront of it, I mean, Codex pioneered all of the... A lot of the ideas that now like... Yeah. Codex still uses and Codex is still evolving too.

`[02:07]` **SPEAKER_02:** For brief context, when I was at OpenAI, I was working on the Codex web product. At the time, Cursor was out in the market and they had kind of built this shim around, I think it was Sonnet 3.5, and it was able to work in your IDE. FOD code had just come out and it was working as a CLI. And we kind of had this idea like, hey, in the future, coding is really going to feel more like talking to a coworker. Like you're going to send off a question. And then they'll go off and do something and come back to you with a PR.

`[02:37]` **SPEAKER_02:** And so that's where we started with this WebView and that's what we were building. I think directionally, that's still kind of correct for where things should go. But obviously now everyone is coding with CLIs instead. Like they're using those tools a lot more, whether it's Cloud Code or whether it's Codex. And I think at least for me, kind of the lesson in that is I think in some sense, you're right that like everyone is going to become a manager in the future, or at least that's my hot take.

`[03:02]` **SPEAKER_02:** But in order to get there, there are steps along the way. And you have to really build a lot of trust in the model and understand what it's doing.

`[03:08]` **SPEAKER_01:** You recently came over to Cloud Code. What's the transition been like in terms of as using it as your, you know, one of your

`[03:15]` **SPEAKER_02:** stacks? Yeah, yeah. So Cloud Code is certainly my kind of like daily driver today. And honestly, this is switched every few months. For a while, I was deeply in Cursor. I think their new model, which is really fast, is actually quite good. Then I kind of moved over to Cloud Code, especially with Opus. Cloud Code is a really interesting product. And I think it's underrated how good the both product and model are working together. If you study them closely, I think one of the things that Cloud Code does in particular

`[03:43]` **SPEAKER_02:** that's really amazing is split up context well. And so if you look at, I don't know, things like skills or subagents, like when you ask Cloud Code to do something, it will typically spawn and explore subagent or like multiple ones. And basically each of those are running haiku to traverse the file system and kind of like explore what's there. And they're doing it in their own way. They're doing it in their own context window. And I think Anthropic has kind of like figured something out here around given a task.

`[04:11]` **SPEAKER_02:** Does that task fit in the context window or should I actually like split it into many more? And the models are like insanely good at this, which I think gives them really good results.

`[04:19]` **SPEAKER_00:** And I think the fascinating thing is because it's on the terminal is the purest form for composable atomic integrations. Because if you came from ID first world, which is where Cursor was, and I suppose Codex too, this concept of. Finding the context more free form wouldn't come out so natural, right? Because which is so unique.

`[04:41]` **SPEAKER_02:** Yeah. And I personally, I was surprised, I don't know how you all feel, but I was surprised

`[04:45]` **SPEAKER_04:** that like CLIs. It's like a weird retro future that like the CLIs, which are the technology from 20 years ago have somehow beaten out all the actual IDEs, which were supposed to be the future.

`[04:56]` **SPEAKER_02:** A hundred percent. Yeah. And I think it's important actually to Cloud Code that it's not an IDE because it sort of distances you from the code. It's being written. Like IDEs are all about exploring files, right? And you're like trying to keep all the state in your head and understand what's going on. But the fact that a CLI is like a totally different thing means that they have a lot more freedom in terms of how it feels. And I don't know about you, but I feel like when I'm using Cloud Code, it's like, oh,

`[05:18]` **SPEAKER_02:** I feel like I'm flying through the code. You know, it's like, there's all sorts of things going, there's like little progress indicators. It's kind of like giving me status updates, but like the code that's being written is not the front and center thing.

`[05:28]` **SPEAKER_01:** I mean, dev environments are so messy. I mean, I really like how clean. Yeah. How clean a sandbox conceptually is in Codex. But then I just ran into all these crazy issues, like trying to do, you know, run just simple testing, right? It needs to access Postgres and then it can't do it, or, you know, my codex.md ended up being 20 lines long and even then it didn't work. When it's in your CLI, it could just access your development database. I mean, I'm not sure if I'm supposed to do this, but I've actually also had it access

`[05:59]` **SPEAKER_01:** my production database. Yeah. Yeah. Yeah. It can just do it. It's like, yeah. Okay. Here, like I looked into it and I think this happened and I'm going to debug this, you know, concurrency issue. And I was like, oh my God, like this thing can debug nested delayed jobs, like five levels in and figure out what the bug was and then write a test for it and it never happens again. This is insane.

`[06:22]` **SPEAKER_02:** Yeah. And I think that distribution mode is frankly underrated. Like thinking about a cursor or a cloud code or a codex CLI, the fact that you can just download it and use it without having to get it. Any permissions or anything makes a huge difference. And actually I was playing around with a product the other day where you download a desktop app and then it execs the cloud code that you have running on your laptop and uses that and communicates back via an MCP server to the desktop product.

`[06:48]` **SPEAKER_02:** And it's like, this is a very interesting way of now starting to work with your laptop where you don't have to get anyone's permission to do it. You just download the product and go.

`[06:57]` **SPEAKER_01:** Yeah. I was looking at like New Relic has an MCP, but you know, Sentry. You can like copy markdown, but like it's like an auto bug fixer basically. It's right there. Yeah.

`[07:07]` **SPEAKER_04:** It's super interesting that in a world where things are changing so fast, you really want your pride to have a bottoms up distribution, not top down because like top down is like just too slow. Like the CTO of a company is going to be like, have all these concerns about security and privacy and what if the control exactly versus like the engineers just like install the thing and start using it. Like this thing is amazing.

`[07:26]` **SPEAKER_02:** Yeah. I think that's right. The one thing I do struggle with, I mean, I'm like a B2B enterprise guy generally. Yeah. But I feel like there's some amount of moat that happens when you do that top down sale and there's got to be some company who manages to crack it where it's like, oh, this is the thing that everyone has access to. Maybe individual people can take it up.

`[07:44]` **SPEAKER_01:** That was the original Netscape Navigator. It was free for non-commercial use and then people would just download it and use it for commercial use and then they could just track down the IPs and figure out exactly how many clients were in all of these different companies and say, you should pay for this. You're in violation, but all you have to do is buy a license. Yeah, yeah. So I'd be curious if you could do that work again here. I mean, your point about distribution is very interesting because now people are probably

`[08:13]` **SPEAKER_01:** just making architecture decisions about what to use directly in Cloud Code. They might not even know what analytics to use and it's like, oh yeah, as long as Cloud Code says use PostHog, they're using PostHog.

`[08:27]` **SPEAKER_02:** 100%. Yeah. Yeah. I was talking about their GEO strategy. This is like the generative optimization or how you show up in chatbots. And what he was saying is funny is one of their competitors had put together a top five list of tools in their category that you should be using and of course, their tool is ranked at the top of this top five list and any human looking at this would be like, oh, this is so obviously biased. It's like the top tool is the one that's in the domain, but the LLMs get fooled and they're

`[08:56]` **SPEAKER_02:** pulling together a bunch of contacts and they're saying like, oh, this is the top and then they'll just recommend it. So I think, yeah, if you're selling a developer tool, like having good docs that are out there, like having social proof, like maybe being posted on Reddit a little bit more, all of that helps your case tremendously.

`[09:09]` **SPEAKER_00:** Which is why I think a lot of the open source projects have taken off a lot more. I think one of the examples is Supabase actually, which really took off last year. And part of it is because they have such a good open source documentation, how to set up a bunch of stuff. Whenever someone asks how to set up anything that you need, some sort of backend, Firebase, whatever. Yeah. That type of transaction. The default answer from all the LLMs is actually Supabase. I was just trying some of these questions that comes from that.

`[09:38]` **SPEAKER_01:** The thing is it's winning the internet. And it was like that before when it was like Stack Overflow, searching Google. And then now that nobody uses Google anymore, it's like crazy. It's kind of the same deal.

`[09:52]` **SPEAKER_02:** I will say it does help open source disproportionately, I would say. I don't know if you all saw there was a Ramp blog post that they recently published about building their own coding agent. And they were mentioning that they use OpenCode as a harness because the model can look and see the source code and understand how it's working. And I do this all the time with open source projects. I'll clone the repo and then spin up Codex or Cloud Code and be like, hey, give me a walkthrough of what's going on here.

`[10:15]` **SPEAKER_02:** It's really useful.

`[10:16]` **SPEAKER_00:** What do you think are some of the tips for anyone that wants to build a coding agent since you've done it a lot? What are some now lessons that you learned that you want to share?

`[10:25]` **SPEAKER_02:** I mean, I think the number one thing is managing context well. Basically, we kind of had a checkpoint for, I think it was 03, one of the reasoning models. And then we did a bunch of fine tuning on it in reinforcement learning where it's like, oh, you're given a bunch of questions to solve these coding problems or fix tests or whatever or implement a feature. And then the model was RL'd to respond to those. And so I think most people are not going to be doing that, right? But the things that you can do are figure out like, hey, what context should I be supplying

`[10:56]` **SPEAKER_02:** to this agent to get the best possible result? Yeah. So in code, if you watch it working, it's like, oh, I'm going to like spawn a bunch of these Explorer sub-agents. They will like search for different patterns in the file system. They will come back, they will have this context, they'll summarize it for me, and then I'll have some place to go. It's interesting watching like different agents structure this context. Like I think Cursor takes an approach where they actually do semantic search, where they

`[11:19]` **SPEAKER_02:** embed everything and figure out like, hey, what query is closest to this? If you look at a codex or a cloud code, they actually just use like grep. Yeah. And I think that works because- It works really well. It works really well. Yeah. It works very well because code is very context dense. Like if you think about lines of code, it's like each line is probably less than 80 characters. There's not a lot of like big like data blobs or like JSON in your code base. Maybe there's some, but not a lot.

`[11:46]` **SPEAKER_02:** You can respect gitignore to figure out and like filter out stuff that's just not relevant or is like packaged. And you can use grep and ripgrep to like find context around the code, which probably gives you a good sense for what that code is doing. And you can navigate the file folder structure.

`[11:58]` **SPEAKER_04:** Yeah. Which is really, really good at admitting very complicated grep expressions that would like torture a human.

`[12:04]` **SPEAKER_02:** Yes. Yeah. Yeah. Yeah. This is like the RL in practice. Yes. Yeah. And so I think all of that, like if you're trying to build a system, well, I'm trying to build systems that integrate agents for non-coding work, I think you can learn a lot of those lessons and say like, hey, how do I get my data in the format that is like maybe closest to code where the model can like peek and look at like areas around it and get the right structured data.

`[12:27]` **SPEAKER_00:** Yeah. So this is how a lot of the superpowers for the best coding agents is context engineering. What are some of the tips to become a top 1% user of coding agents?

`[12:39]` **SPEAKER_02:** Yeah.

`[12:40]` **SPEAKER_00:** What's your stack? Yeah. What do you do to be so productive with it?

`[12:43]` **SPEAKER_02:** One is if you're able to use just generally far less code in plumbing. So a lot of what I do is like deploy stacks on like Vercel or Next.js or like Cloudflare workers where there's kind of like already a bunch of boilerplate like taking care of for you. You don't really have to think that much about like, hey, I need to stand up like all these different services and deal with like service discovery and like registering on like some sort of central endpoint or like all these databases.

`[13:07]` **SPEAKER_02:** It's like, oh, like everything is pretty roughly defined in this like one or 200 lines of code. I tend to operate more towards microservices for that as well, or like individual packages that are fairly well structured. I think it's also worth knowing like what the LLM superpowers are like in general coding agents are. I think. I think I just tweeted about this. They're like super persistent, so they will keep going no matter what. They end up typically just making more of whatever's there.

`[13:37]` **SPEAKER_02:** So if you're trying to direct them to do something, it's worth like, I mean, I can pick on OpenAI slightly. In this example, OpenAI has like a giant monorepo. It's been there for a few years now and has like, I don't know, thousands of engineers who are committing. Some of those engineers are like super senior meta folks who came in and are like, know exactly how to write production code. Some are like new PhDs. It's like a pretty wide range. And so the LLM will pick up different things depending on where you direct it.

`[14:06]` **SPEAKER_02:** I think there's a lot of room actually for coding agents to figure out like, what is the like optimal type of code that we should produce? I mean, obviously giving the model a way to check its work helps improve performance drastically. So the more that you can run tests in Lint, CI, et cetera. Personally, I also use code review bots pretty aggressively. I know. YC company is really good. I use the cursor bug bot has gotten quite good and I actually like Codex for code review as well.

`[14:33]` **SPEAKER_02:** I find it does a very good job on correctness. So those are all things that like the agents are good at and they're excellent exploring the code base too. I think areas where they don't do well, they make more. If your goal is not to make more, they'll like often duplicate code and like spend a bunch of time reimplementing things that like, you're like, oh, of course you didn't want to do this. I think context poisoning is a real thing. Where it kind of like goes down one loop and it will continue because it has this persistence,

`[15:02]` **SPEAKER_02:** but it's referring back to tokens, which are like not right in terms of pursuing a solution. And so one thing that I often do is like very actively clear context.

`[15:12]` **SPEAKER_04:** Like how often?

`[15:14]` **SPEAKER_02:** Usually when it gets above like 50% tokens. Oh, wow. Yeah. Yeah. I don't know. There's this guy, Dex, from this company, Human Layer. That was actually another YC company.

`[15:23]` **SPEAKER_00:** Yes. YC company.

`[15:25]` **SPEAKER_02:** Yeah.

`[15:26]` **SPEAKER_00:** Yeah.

`[15:27]` **SPEAKER_02:** And he talks a lot about it. Yeah. He has this concept of like the LLMs reaching the dumb zone where it's like after a certain amount of tokens, it just starts like degrading in quality. And I actually think that's very true, especially if you think about like how the reinforcement learning might work. Like imagine you're a college student, you're taking an exam. In the first five minutes of that exam, you're like, oh, I have all the time in the world. Like I'll do a great job. I'll think through each of these problems.

`[15:51]` **SPEAKER_02:** Let's say you have like five minutes left and you still have half the exam left. You're like, oh man. I just got to do whatever I can. Like that's the LM with the context window, right?

`[15:59]` **SPEAKER_00:** One of the tricks that I think founders use is you put like a canary at the beginning of the context. There's something very esoteric that it would only help. It's like something really funny. It's like, I don't know. My name is Calvin and blah, blah, blah. I drink tea at 8 AM. Some random fact. And then as you keep going, you ask it, do you remember what's my name? Do you remember when I drank tea? And then when it starts forgetting that, I think is a bit of a sign. That the context has poison.

`[16:28]` **SPEAKER_00:** That's like one trick I see people do. They do a random canary.

`[16:31]` **SPEAKER_01:** I have not tried this, but I fully believe it. That's interesting. I haven't run across any bugs before compaction, but maybe I'm not paying attention, but you're saying like that actually is actively something that it just starts doing weirder things that are not like optimal. Yeah. Yeah.

`[16:47]` **SPEAKER_04:** Okay. I got to be on the lookout for that. It seems like it should be solvable within the plot code itself. Like it should be able to basically do some sort of detection. Like what Tiana said.

`[16:54]` **SPEAKER_01:** Yeah. It should have your own internal heartbeat around it, around the context.

`[16:57]` **SPEAKER_02:** Yeah. And I think we're just not there yet. Like I agree with you in the limit. Right now it's definitely hard to manage context well, and I think kind of the way it gets around it is like split up context windows and then try and merge everything. But you're sort of still at the limit right now of like everything that lives in context at the end of a quad code session is kind of fixed. It's actually interesting. The Codex approach is kind of the opposite. And they just wrote about this on the OpenAI blog where it will run compaction.

`[17:24]` **SPEAKER_02:** Like periodically after each turn. And so Codex can continue to run for a very long time. And if you look at the percentage in the CLI, you'll see it like move up and down as compaction

`[17:36]` **SPEAKER_01:** runs. I guess like there are these very different architectures between Cloud Code and Codex sound like they're actually deeper in that Codex is actually meant for much longer running jobs. That's sort of like off the bat, a different use case, and then the architecture is very different as a result. Yeah. I guess right now it seems like CLIs, you know, 2026 might be the year of CLI. But then this other idea that AGI is here and it's actually ASI is around the corner. The coding agents right now are really, really smart, but not smart enough to run on their

`[18:10]` **SPEAKER_01:** own for long periods of time. But a 10x increase in compute from here, are we there? Like are we at 24 hours or 48 hour running jobs on Codex and that architecture is correct for that world?

`[18:24]` **SPEAKER_02:** Yeah, I think it's a good question. It sort of goes back to like kind of the founding DNA of both companies. I feel like Anthropic has always been very big on like building tools for humans where it comes to like, oh, here's the style of the tone and like, here's how it should fit with all of the rest of your work. And I think Cloud Code is like a very natural extension of that. And a lot of ways it like works like a human would, or it's like, oh, you need to build like, I don't know, a dog house or something.

`[18:48]` **SPEAKER_02:** It's like, oh, I'll go to the hardware store and I'll build all these materials and I'll like figure out how they all fit together. Yeah. It really leans into this idea of just like, we are going to train the best model and reinforce over time and get it to do longer and longer horizon things in this pursuit of artificial general intelligence. And so it may not work like a human at all, like going back to the dog house example,

`[19:10]` **SPEAKER_01:** it's like, oh.

`[19:11]` **SPEAKER_02:** But AlphaGo didn't either. Yeah, but AlphaGo didn't either. It's like, oh, it's like, instead I will have a 3D printer that can print from scratch like a dog house and it will be exactly what you want and it will take a long time and it will be like very custom and it will do like weird things. But it will work, you know, and like maybe in the limit, that's the right call. And so it's going to be really interesting to see how they play out.

`[19:29]` **SPEAKER_01:** I mean, net-net, it seems like the latter is somewhat inevitable, but I like the former so much. Yes. Yeah. You know, like even this idea that it greps is like I thought about, you know, 10 years ago was like, yeah, I was in there like writing my own really weird regexes to try to figure out where everything was when I was refactoring or trying to understand code or whatever. So that's the feeling I get when I'm using it. It's like I can do five people's work. Yeah. Five people's worth of work in like a single day.

`[19:56]` **SPEAKER_01:** It's like rocket boosters. It's just unbelievable.

`[19:58]` **SPEAKER_02:** Yeah. I think it's going to be really interesting to see how this plays out across large and small companies. I think everyone who's experimenting with this stuff on like a hobbyist level or at like a very small startup, they're just pushing the coding agents as far as they can go because it's like you don't really have time to figure out anything else. Like as a startup, you have limited runway. You're just going to like orient around speed. I think at a bigger company, you have a lot more to lose and you have all these other

`[20:22]` **SPEAKER_02:** internal processes around coding. You have code review and you probably already hired like a big eng team. And I think it's going to be very strange as like these individual teams of like one person are like, hey, that team over there isn't doing the right thing. Like let me just build a prototype that like works better. I think at some point it's going to start working better. And I think that landscape shift is going to be a very interesting, strange thing.

`[20:46]` **SPEAKER_01:** My 10 year old, he has writing assignments every day and then yesterday was the first day where he used AI. And then I was like, this is not a turn of a phrase that a 10 year old is capable of doing. And then I think about that in this context because we, you know, we're working with a lot of 18 to 22 year olds who, you know, they've done internships, but like they haven't done like eng manager work. Like, you know, we're saying, you know, post-product market fit once you have job queues of like

`[21:17]` **SPEAKER_01:** millions of jobs and like, you know, hundreds of thousands of errors, that's like real eng management. And that's really, you know, it's horribly unglamorous, like combing through hundreds of thousands of errors and then like manually making sure that like the thing works for all of your users in the background. How does the next generation understand that? Can the cloud code bot actually teach people about architecture and things like that? Or you know, are you just going to bump your head into it and users just kind of suffer

`[21:47]` **SPEAKER_01:** and you know, people have to figure it out.

`[21:50]` **SPEAKER_02:** Yeah. At least where I find myself spending the most time when it comes to projects. Yeah. I think the biggest challenge with a product is figuring out the kind of product model in a sense. Like what are the things that the user has to understand today? And what are the primitives that they can use to like do whatever they want? I always think of Slack like this. It's like Slack was in some ways not really a new concept. It's like there were many chats that existed before it. But the fact that they had like channels, messages and reactions in a simple way that

`[22:17]` **SPEAKER_02:** people could just like think about and be like, oh, I understand how to like navigate this. But then kind of once they were there, like it's very hard to change that later on for a user. You know, it's like, oh, maybe they wanted to go in more of like a document first way or like maybe right now they're trying to incorporate agents. It's like difficult to change the user's mental model. And so I at least for myself building products, it's like you have to think about that very carefully from an early stage, because again, whatever you supply to the coding agents is

`[22:44]` **SPEAKER_02:** that kind of kernel is going to be what they run with and make more of forever more.

`[22:48]` **SPEAKER_01:** YC's NextBatch is now taking applications. It's got a startup in you. Apply at YCombinator.com slash apply. It's never too early and filling out the app will level up your idea. OK, back to the video.

`[23:01]` **SPEAKER_03:** Do you have thoughts just because, you know, the agents so well, like what what types of engineers are going to benefit more than others from these tools becoming popular?

`[23:12]` **SPEAKER_02:** In general, I think that kind of the more senior you are, the more you benefit because the agents are so good at taking. Hmm. So good at taking some sort of idea and then putting it into action. If you're able to prompt that in a few words, it's kind of like, oh, now suddenly I had this idea. I find this so often open AI, like strolling through the code base. It's like, oh, like here's the thing that I wish were different. Here's the thing that I wish were different. Here's the thing that I wish were different.

`[23:37]` **SPEAKER_02:** Like just being able to kick those off and then have them come back, I think, is super empowering and multiplies your impact. I think also being able to detect like which sorts of changes are good or bad architecturally is very important. Or like have a sense for. Or where you might want to flag something to an agent. I think engineers who are more organized, like manager-ish, and there's probably just a missing product to be built here. Maybe something like Conductor where it's like spread across all of your sessions and

`[24:05]` **SPEAKER_02:** kind of reminding you like, hey, you were working on this thing. It's done. It needs your input here. Oh, you should switch your attention over to this other thing. I think that is going to become- Oh, Conductor should add that.

`[24:14]` **SPEAKER_04:** Yeah. Yeah. Like context management for agents, but like we also need context management for humans.

`[24:18]` **SPEAKER_02:** Yes. 100%. Yeah. I mean, I want like when I wake up every day, it kind of is like, hey, here's all the work that got done overnight. Like here are the like three decisions that you need to make. Here are like areas of deep thinking that you were planning to do. Like I want the turn by turn for my day. Other things that make it very useful. Like if you're able to build, I don't know, some sort of like quick prototype for an idea to show it off, like that's an area, I mean, obviously the agents do super well at this.

`[24:46]` **SPEAKER_02:** I would find myself at OpenAI often writing kind of like prototypes. Yeah. Like, hey, I've got this like in memory key value store. Can you now turn it into like work with a production database or something like that? Being able to concisely specify ideas in code. And then I think having a smell for what the right architecture is, is still the area where the models like don't do the best job.

`[25:07]` **SPEAKER_03:** So if you were going back to your like college days and studying CS again, fresh and you like were picking your own like syllabus or curriculum, like what would you study?

`[25:16]` **SPEAKER_02:** Personally, I think still understanding systems. Is very important and just having some conception of like how like Git works, you know, or like HTTP or databases like queues, like all of these different systems, I think that those fundamentals are still quite important. The other thing that I'd probably do is just have a semester where like each week you're just building something and you really try and push the models as far as they can go. There's a sense that you have whenever you're doing something that you could always just

`[25:47]` **SPEAKER_02:** like go up the layer and ask the model to do it. And like go up a layer and ask the model to do it, you know, where it's like, oh, I have like a implement command where it like implements the next phase of the plan, but then I could have like an implement all command and it like goes stage by stage and creates a new subagent. And then I could have like a check your work kind of thing. And like, and I think knowing where the models can and can't accomplish that is such a moving target that it's worthwhile just to like tinker a lot.

`[26:11]` **SPEAKER_01:** I mean, the other thing that's really, really crazy for, I mean, I would love to be able to teach 18 to 22 year olds. Like everyone around. Like at this table has like ship stuff that people really, really want and love. So it's like, how do we teach people that?

`[26:26]` **SPEAKER_03:** I wonder if like the best 18 to 22 year olds, like five years from now, we'll just have like off the charts taste and everything, because there'll just be so much more prolific that they should be right. Like they should just be launching and touching reality like 10 times as much as like the generation before them.

`[26:42]` **SPEAKER_02:** The one thing I have wondered about on that note, um, I don't know if you all found this, but growing up, my mom used to tell me like, oh, like. Stop multitasking. You're not paying attention to like what I'm doing. And I think there is some truth to that. Like often I would be like off on my computer, like not paying attention, but I do think I was legitimately better at multitasking than our parents were. And now I look at this new generation and I think they're actually quite a bit better

`[27:06]` **SPEAKER_02:** at multitasking than we are, you know, cause they've kind of grown up in this age of the internet and they're dealing with like Tik TOK and all of these like different short form video and things like, it seems like there's room for both kind of this like deep thinking where you want to like notice what you're seeing and understand and problem solve. Yeah. But then there's also this mode of just like bounce between a bunch of different things and your context switching constantly. The ADHD mode.

`[27:25]` **SPEAKER_02:** Yeah. The new generation is quite good at this.

`[27:28]` **SPEAKER_03:** Yes. I definitely think there's a, there's a type of smart person, maybe it's ADHD, but just like always has like a bunch of good projects on the go, but just never actually finishes anything. I might relate to this personality a little bit.

`[27:39]` **SPEAKER_01:** Hey, you released your, uh, your vibe code project.

`[27:41]` **SPEAKER_03:** Yeah, but I wouldn't only because of Claude Code, but now I just think like you kind of like, there's certain types of brains that just have like, like 10 branches going in their heads, but you never have enough hours in the day to actually like see any of them through. So they're always like half complete and now it's just like Claude Code gets you over the line with everything. And it's just like, and you made this point in your blog post about how it feels like a video game, but it's just like, there's just a constant novelty factor.

`[28:03]` **SPEAKER_03:** Like you start working on something and usually when you hit the point of like, I'm like bored and then I've got this other better idea and I should like start on that and then come back to this. Like you can't do that now, but like everything can actually get finished.

`[28:14]` **SPEAKER_01:** Let's live in the future for a moment. It's 40 years from now. Software still exists. Databases still exist. Access control still exists. But like at the core of it, I mean, software is entirely personal. Access control and who gets to do it is like, you know, sort of like this manager mode thing that people still have meetings about. But then everything else about a company, its functions, its roles, like is defined by people just doing things in their own Claude Code like thing. I don't know.

`[28:45]` **SPEAKER_01:** Maybe it's a CLI or it's like, you know, having giant armies of workers. Then I don't know. What would that look like?

`[28:51]` **SPEAKER_04:** Like, imagine if every time a company signed up for Segment, you fork the code base, you give them their own copy of Segment, it's running on their own servers, and then if they want to change anything about it, they just like tell some chat window, which is running like an agentic coding loop and just like edits their version of Segment. As Segment, the corporation pushes out more features, some agent figures out how to merge.

`[29:13]` **SPEAKER_02:** Yeah, I could totally see it. I mean, sort of what I've been thinking, I don't know how far this future is. But like eventually every person who's working like has their own sort of like cloud computer and like set of cloud agents who are running for them, and they're mostly just like talking back and forth. It's kind of like having like a super EA or something where it's like, oh, here are the things I need to pay attention to. Like let me make some quick decisions. Like let me spend more time on this.

`[29:36]` **SPEAKER_02:** Let me like meet with other people because I think that there's still going to be room for people who like want to meet other people and exchange ideas in person, or at least I get a lot of movement out of that. And then separately, there's going to be this army of agents who are like, you know, like, this army of agents who are like doing things on your behalf and like automating a bunch of things. I think the average company is probably going to get like a little smaller and there's going

`[29:56]` **SPEAKER_02:** to be many more of them doing more things.

`[29:58]` **SPEAKER_03:** Something I'm curious to see is kind of like what the update version of the PG maker, maker schedule versus manager schedule would look like, because I feel like part of what's going on at YC is sort of a lot of our jobs are essentially manager schedule, which has just really made it hard to do any sort of building your own software, but now you totally can. And that's why like a bunch of the partners- Yeah. Yeah. Yeah. Yeah. Like right at the beginning of this podcast.

`[30:20]` **SPEAKER_00:** You let it run and then come back.

`[30:22]` **SPEAKER_03:** Well, like in the pockets, right? It just used to be like, literally, unless you had like, you know, four hours minimum block free to do something, it just wasn't worth even getting started, right?

`[30:32]` **SPEAKER_04:** And I think that's actually goes very deep to how we've changed programming. Like it used to be that in order to write any code, you had to fill your own context window with so much data about all the different class names and the functions and the code that it touches. It'd take hours to build up that context window. And so doing it in 10 minutes snatches was just like so frustrating.

`[30:49]` **SPEAKER_00:** I do think maybe one primitive for this future world will be, I think still the data models need to be still be consistent and the system of record. There's opportunity for something that's kind of agentic first, because right now we're still kind of integrated very much with databases and SQL or NoSQL queries at a very low level. But imagine something that generates all the data that you need for all the different views for custom software. So a lot of the world would be custom views.

`[31:16]` **SPEAKER_00:** But I think the unified stuff, we still need to have the data to be correct.

`[31:20]` **SPEAKER_02:** I think data has a lot of gravity and I think you see this with companies who are offering access via API or MCP. I think Slack locked down their API a little bit because they didn't want people just exfiltrating everything from Slack and then building agentic experiences on top of it.

`[31:36]` **SPEAKER_00:** I wonder with that note, if you were to rebuild Segment with the current tools, how would it look like?

`[31:44]` **SPEAKER_02:** I mean, Segment is a funny business. Yeah. I mean, we had a business in that where we started was building these integrations, right? And so it's like, oh, you need to wire up the same data going to Mixpanel and Kissmetrics and Google Analytics, et cetera. And I think just writing that code now, that used to be maybe a more annoying or harder thing to do. And so it was worth paying for. Now that value has dropped to zero. One shot. Yeah. And actually, in many cases, you're better off saying, oh, I actually want to map it

`[32:11]` **SPEAKER_02:** this way and I want this specific behavior. I'll just tell the quad or codex what to do. And then it will do it and I'll have exactly the behavior that I want. So I think that aspect of Segment, the value has dropped precipitously. I think the aspect of keeping this data pipeline running and continuing to automate a bunch of parts of your business or schedule these email deliveries, which should go out through Customer I.O. every time a customer signs up or manage audiences for you, that value

`[32:38]` **SPEAKER_02:** is kind of still there. And I think you could do a lot more interesting things where it's like, hey, if I have all this data and a full view of the customer, how should I be emailing? Yeah. How should I be emailing them? Should I change parts of the product when they log in? Should I be giving them different onboardings depending on who they are? There's a lot more interesting stuff that you could do by basically running small LLM agents over them and changing that. That would be the changes I would make.

`[33:01]` **SPEAKER_00:** So it's kind of like moving up the stack to your comment earlier and all the way turtles down. The low level stuff is gone. Yeah. It's now really more doing things at the campaign level, which is way more abstract.

`[33:11]` **SPEAKER_01:** Yes. I mean, I'm amazed at to what degree like Cloud Code, even just from like the context, like, the context of what I'm working on, figures out like what my motivations are.

`[33:20]` **SPEAKER_02:** Yeah. I'm still blown away by coding agents because effectively what you're doing is you're like giving them a copy of a repo and then you're slipping a little note under the door and being like, hey, go implement this thing. They have like no knowledge of like what your company is or like what you do, who your customers are. In most cases, maybe it's in the training set because they know you're Gary. But it blows my mind that it works at all. And that's where I think the context is really important, right?

`[33:44]` **SPEAKER_02:** Because if it latches onto something that isn't. Quite right. It doesn't have a lot to go on, and if it misses something that's essential, it's going to just re implement it.

`[33:51]` **SPEAKER_01:** What do you think the constraints are right now? I mean, like context window is still a constraint, but it's like so big that, you know, it's like we can do some stuff like we can't do the mega re architectures, but we can do a lot. And then if the Opus 4.5 somehow got a lot smarter and then that unlocked a big thing, which was interesting. I don't have no idea if that was like pre training or post training. Like, what are there other like levers that you think of other than, you know, basic model

`[34:22]` **SPEAKER_01:** intelligence like frontier model intelligence and context window?

`[34:26]` **SPEAKER_02:** I mean, I still think context window is like probably the number one limit. Like if you look at cloud code executing, it's delegating to all these different context windows at the end of the day when each one comes back, it's like getting some sort of summary. So it's also not getting the full picture. Like if you have a problem that's just like too big to fit in a single one, like kind of no amount of compaction is going to help. You. I would point to that as like both Anthropic has figured something quite useful out with

`[34:49]` **SPEAKER_02:** delegating to these sub context windows, but also I think it's still a block barrier.

`[34:53]` **SPEAKER_01:** So we do better if we had a million million token context every single time.

`[34:57]` **SPEAKER_02:** Yeah, I think so. And like figure it out a better way to especially train these like very long context trajectories. Because you think about it like there's there's a lot of training data on the Internet for like what is the next sentence that comes or like what's the next paragraph that comes if you have 80,000 tokens that are generated. Like. Understanding what the next thing to do based upon like, oh, I should refer to the 20,000 token. Like that's trickier. I think this like integration and orchestration is starting to become the limiting factor.

`[35:27]` **SPEAKER_02:** I mean, I think there are like stuff on code review related to this. It's like, oh, if we're like merging all this code, like who's watching it, does a human still have to watch it? Like how do we verify the changes? And then I think like pulling in the context correctly from your tools, like you were talking about Sentry, like you want Sentry to auto be able to like figure out a. PR, you know, and then like maybe it pushes it to a subset of your traffic. And if it looks good, then it rolls out everywhere, you know, like all of that automation sauce

`[35:51]` **SPEAKER_01:** to be built. I was surprised how important testing was like I was operating for like the first two or three days of my nine days in the wilderness, like no tests or very few tests. And then one day I was like, all right, today's refactor day I'm going to do get to 100% test coverage. And then I just sped up like crazy. It was like, oh, it did it. It works. I. Didn't necessarily manually test because it's like the test coverage is so good, like nothing breaks.

`[36:19]` **SPEAKER_00:** Which is very similar to what all the companies are doing just for prompt engineering outside of coding is very much test driven development. I think we had this episode with Jake Heller and that was a big paradigm shift. It's like the way you get a good prompt is all test driven, just like evals, right? In a sense, the test cases are your evals.

`[36:36]` **SPEAKER_01:** There are some broken flows now. I think that we might need a cloud code that could like talk to a. Stack overflow that was like a cloud code stack overflow. Like I had this problem. It was so crazy. Like I, instead of using in the, in like the priority of a job queue I used, or actually I didn't even write again, I did not write this. The machine wrote a string with a comma thinking that it would take that syntax, but it was expecting like an array and Jason. And then it just like no jobs would run.

`[37:09]` **SPEAKER_01:** And then I watched it for like 30 minutes. Walk through. The internals of rails job, like the active job, like a couple thousand lines of code, like trying to debug what was happening. And it found the bug actually, and I was like, that's amazing. I just think about what I would do like 10 years ago. And I would have been like, Hey, why are the, you know, jobs not working? And then I would find a stack overflow or blog, put a rails blog post and was like, Oh yeah. Like nobody fixed that stupid bug where, you know, you think that you can put a comma delimited

`[37:40]` **SPEAKER_01:** string in there. But. It's an array. It's like, Oh my God. Like that was very funny actually. I think that's like one of the hardest parts about thinking about what's going to happen here. Cause there's like things that you would do as a human in a CLI right now. And like, that's very obvious. But even that idea of like, should the agents have their own stack overflow? Like if you just increase the intelligence by, you know, I don't know what you even call it. Like by 10 IQ points, like 10 virtual IQ points.

`[38:11]` **SPEAKER_01:** Like would even do that. It'd be like, Oh yeah, that's a string.

`[38:14]` **SPEAKER_02:** Whatever. Yeah. Yeah. I think there's something very interesting here around like agent memory and cloud code has sort of set itself up. And I think Codex too, by storing all your conversation history, just as files. So you could imagine you like give it access to a tool that then can read previous conversation history. I think there's a missing piece around a lot of collaboration there. Like, it'd be amazing if like there was some way of smartly sharing your coworkers prompts and you could see and be like, Oh, like I hit this thing, but actually like Brian over

`[38:41]` **SPEAKER_02:** there, like fixed it earlier. You know? So like the two of us can share knowledge. I think there's something, there's something onto this of like a model generated, like Wiki, you know, or like Grokopedia.

`[38:51]` **SPEAKER_03:** Now I can't stop thinking about, have you seen the Claude bot social net, like the network for Claude bots to talk to each other? What's that like? Yeah.

`[38:59]` **SPEAKER_00:** That's the evolution for Molten bot.

`[39:00]` **SPEAKER_03:** Yeah. But I guess for those that don't know, Claude bot's essentially like, like your own personal AI agent that you can run on your own machine. You can download it. Do not give it access to emails would be my number one. Piece of advice. Well, probably anything. Um, cause it's not clear how safe it is and it's probably almost certainly going to probably a lot of people being prompt injected by it right now. But somebody created, um, this is like a website, I haven't actually seen it, but I was like

`[39:24]` **SPEAKER_03:** seeing it on Twitter, but like a site where like everyone can sort of spin up their own, like Claude bot, their personal agent, and then the agents can talk to each other. And now there's just like all this AI generated content of these like personal AI agents talking to each other.

`[39:36]` **SPEAKER_02:** Yeah. I mean, it looks like Reddit, but if Reddit were run by agents, I mean, it's interesting to see. I think VX is personality shine through when writing code, I would say. Uh, it does most stuff that humans don't do kind of in this alpha go sense where it's like, oh, it'll write a Python script to like modify some part of the file system. I think that is like very interesting and kind of alien behavior, which has been taught and learned. But it does give these like super human results for me, at least when debugging complex issues

`[40:07]` **SPEAKER_02:** that I find Opus often misses.

`[40:09]` **SPEAKER_01:** What's an example of a complex issue that you could talk about? it's like concurrency or naming issues right i find the models are actually like decent at

`[40:17]` **SPEAKER_02:** concurrency oftentimes there's stuff where it's like oh there's a request that is like traversing several different services i mean kind of to your point about the uh serialization and deserialization of like stuff with commas in it um it's like oh it needs to track some sort of complex behavior around those or like way of uh i don't know refreshing complex ui state and opus often will miss it if there's many files but codex seems to catch it interesting yeah yeah prognostication

`[40:45]` **SPEAKER_01:** about how will tools continue to evolve it's very interesting like i feel like sort of a new citizen in this land in a way like i just you know knew what was happening i'd you know manager schedule finally a project appeared and was like oh i'm gonna go all in on this and then now i'm like in it's like uh i'm in a stranger in a strange land but it but it like resembles exactly what i remember i think this is more awesome we all feel that way

`[41:10]` **SPEAKER_02:** yeah like i think i think the most important thing is just to keep tinkering because it all changes every few months i do feel like the best or the people who get the most out of coding agents in the future are going to be kind of like more manager-like where they're focusing on directing flows in certain ways they're probably going to be a little bit more like designer artists in some ways where it's like they're figuring out what specifically goes in the product and what stuff you can do without and i think they'll be very good at just like continuing to think about

`[41:38]` **SPEAKER_02:** automation and where they're making

`[41:40]` **SPEAKER_01:** missing context I guess what's funny is I tried to use codecs just now for my rails project but the thing is like it's kind of obvious that nobody at opening I cares about rails which is fine like it's a very it's a vestigial language it's very strange it happened to be the one that I you know really really went deep on ten years ago and then it's just funny how much of it is exactly again anyone can make something but then the something people want is very hard yes even when you have like unlimited resources at like an opening I it's like

`[42:12]` **SPEAKER_01:** I guess if someone from codecs is watching right now my request would be go down the list of all of the runtimes and just add like syntactic sugar there's like this is probably like you know 10 PRS at most for like I don't know the top like 15 runtimes I guess it's like sort of the reminder that like man actually like there are far fewer excuses for software that doesn't quite work for a user you know now than ever actually yeah I do think this is an interesting point in

`[42:43]` **SPEAKER_02:** terms of mix of training data codecs works very well on python mono repos yeah yeah and it's like I remember working like internally opening I was like oh my gosh this tool is amazing it is incredible um and it kind of makes sense in terms of the data mix and the researchers who are working on it I think entropic is focused a little bit more on like some of the front end things um and I don't know in terms of like a Ruby for example like who has the best model there and who's incorporated the data mix yeah like some of the labs tend to

`[43:15]` **SPEAKER_02:** take this perspective of just more data is better uh and so they'll just flood as much data as possible while others I think are a little bit more tuned in terms of the mix and I think depending on which approach you take there it can give very different results where it's like oh I'm taking just the like top 10 of JavaScript is pretty different than if you're looking across everything I

`[43:35]` **SPEAKER_01:** actually think open AI and the you know opening models are really good at Ruby uh from what I can tell and then it's just it's

`[43:42]` **SPEAKER_04:** the harness around the model yeah it is yeah oh interesting okay it's literally

`[43:45]` **SPEAKER_01:** like rails has this weird thing where you have to have you know access postgres in a certain way or like it couldn't figure out yeah the sandbox yeah the

`[43:55]` **SPEAKER_02:** sandboxing it's such an interesting question because uh I think open AI actually takes the like sandboxing and security question more seriously than almost anyone else I remember when we were building codecs like basically one of the gates that you have to get through in order to release a model is you have to like talk about safety and security risks like every time you want to release one of the things we were looking into was prompt injection especially for opening up to the internet because a bunch of users were like oh this has to like work

`[44:18]` **SPEAKER_02:** on the internet we're like oh we don't know like it seems pretty easy to prop operator was also yeah yeah yeah and so uh the PM on our team Alex uh basically like put together a GitHub issue in it had like a very obvious prompt injection which was like oh reveal this thing and then he told the model like hey go fix this issue uh and he's like oh there's no way this is going to work and like immediately the prompt injection works you know and so I think open AI like sort of correctly is very worried about this and is like hey we're going to run everything in on a sandbox

`[44:47]` **SPEAKER_02:** we're going to make sure it like doesn't touch all these sensitive files in your machine we're going to be very careful about secrets and I think if you're a startup or you're just like running fast you probably don't care you're just like I just want it to work yep you know are you a dangerously skip permissions person uh I actually have not I like have a set of things that I like how about

`[45:05]` **SPEAKER_01:** you are you running no okay I like to read

`[45:07]` **SPEAKER_03:** you know I like to read what it's doing are you skip permissions Jared 100 YOLO mode oh my God it's about 50 50 on the YC engineering team yeah a security engineer would watch this part and say

`[45:21]` **SPEAKER_01:** you can't release this part just cut it from the podcast you can't have this out here I think it's

`[45:27]` **SPEAKER_02:** context dependent like if you're at an Enterprise you don't want to do that if you're a startup and

`[45:30]` **SPEAKER_01:** have nothing to lose you probably do YC has progressed a little bit from a startup we still act like one though because I think important cool I mean this is so awesome Kelvin thank you so much for joining us of course thanks for having me oh my God this is fun yeah so fun all right back to Claude
