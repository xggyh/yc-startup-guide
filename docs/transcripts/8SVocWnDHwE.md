# 全文转录 · AI 正在解锁数百万新一代"建造者"

> ▶ [YouTube](https://www.youtube.com/watch?v=8SVocWnDHwE) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/8SVocWnDHwE.md) &nbsp;·&nbsp; AI Is Unlocking Millions Of New Builders
>
> 🗣️ 说话人分离识别到 **6** 位发言者(标注为 SPEAKER_00 …)。

`[00:00]` **SPEAKER_03:** So I think now we are just truly seeing this unlock where people who were like really close to problem domain expert and but have been blocked by you know technology barrier to sort of really express themselves are using emergent to sort of build these things out. There's just so much focus

`[00:13]` **SPEAKER_05:** on AI is going to replace jobs, knowledge work is going away, like what's that going to mean for employment and civil unrest but like no one's really talking about the fact that actually like if you have like some agency of interest you want to start your own business and have autonomy over your life like you are empowering that at scale. Welcome back to another episode of The Light Cone. Unfortunately Gary got called to jury duty and can't be here with us today but we are really excited to be joined by Mukund and Madhav Jha. They're both twin brothers and founders of Emergent

`[00:51]` **SPEAKER_05:** which went through YC in summer 2024. Emergent's a platform that lets anyone build and ship production-ready software using AI agents. You guys are actually one of the fastest growing companies I believe YC's ever funded. I mean the statistics you were telling us were mind-blowing. You have in eight months since launch seven million apps have been built with Emergent. Walk us through this like incredible growth you're seeing actually when did that hit a real inflection point and how did that that feel for you guys? So we both are

`[01:19]` **SPEAKER_03:** twin brothers. We actually you know started programming when we were age 12. Both of us came to US to do our PhDs. I dropped out of the PhD program, joined Google and Maddy went on to was at Zenefits then went on to start the deep learning team at Amazon and we've been meaning to do a startup together for a long time. We've been doing a startup together for a long time. And before this I was running a startup in India called Dunzo which was a hyperlocal quick commerce company. And Dunzo was a big company actually right? Yeah it was it was really big and and we

`[01:46]` **SPEAKER_03:** we are almost a verb in India. So when people ship things they say Dunzo it. And I was managing a really large team of 300 engineers when you know and we have been sort of watching the deep learning field for a while and we knew an inflection point is coming. One of the things that I observed when I was running this large engineering team was that software testing was the biggest bottleneck in the world. And we started looking at you know what we want to build in AI. That was the first idea.

`[02:08]` **SPEAKER_03:** What year was this? This was 23 and yeah and and so when we applied to YC like we applied with this idea of automating software testing. That was the first idea. In fact we went to a lot of VCs with this idea. They thought it was too crazy you know and and now looking back it almost looks funny. And so we applied to YC with this idea and and when we were building this testing agents we realized that if you can solve for verification which is essentially you know you can solve the testing part. You can actually automate all the software engineering. That was

`[02:38]` **SPEAKER_03:** sort of our key insight that like you know verification is the loop which sort of keeps agent running for a longer period of time. And that's when we pivoted to looking at general coding agent as a space. And we started building general coding agent. And this takes us into 2024.

`[02:50]` **SPEAKER_05:** This is 2024. Yeah tell us what the landscape looked like. Like how big was

`[02:55]` **SPEAKER_03:** Lovable at this point and just. I mean nobody had started. Lovable had not started. I think Cursor was just just getting getting getting started and very very early. I think Devon had just come out so so really really early. And and we looked at this benchmark called SweeBench which is essentially a benchmark. Now it's saturated but at that point of time like that was the benchmark where all the coding agents were getting measured on. And we took on this challenge of becoming number one on that benchmark. And like we sort of packed ourselves in a room four of us and said

`[03:22]` **SPEAKER_03:** okay let's just look at this benchmark. How do we crack it? That sort of set the foundation for Emergent. And we built you know SOTA coding agents which became world number one on SweeBench you know in two months of time. And that was the time when we sort of discovered all of the truths about building with LLM building with agents. Your intended use at this point were presumably engineers. Yeah at that point we were like purely just a research company just building coding agents. We were not thinking about a product. There was a time when we sort of invented

`[03:44]` **SPEAKER_03:** the multi-agent system. We invented memory. We invented like how do we do agent to agent communication. How do you scale up test time compute. A lot of those things which like were sort of coming out like we would we would discover something and we'll see three months later something come out in the paper. You know and that sort of set the foundation for for us too. So we were like cloud code before cloud code was a thing. So we were like what are some of the paradigms like multi-agent orchestration. How do you use

`[04:08]` **SPEAKER_03:** like different different routings. A lot of those things we sort of discovered. I definitely want

`[04:11]` **SPEAKER_05:** to come back to that. I'm curious at this point in the story though when did you sort of pivot

`[04:16]` **SPEAKER_03:** into becoming a tool for non-technical users? Yeah so we actually like once we had this coding agent we actually went the enterprise route. That was the common wisdom at that point that hey like go to enterprise build for enterprise. And we spent like two three months trying to you know make our agents work within enterprise. We found that it was too slow and at the same time we were using emergence platform to build internal tools and internal software. And at that point you know

`[04:39]` **SPEAKER_03:** we saw like lovable is growing like crazy. Bolt was growing like crazy. So we thought hey why don't we have this you know really strong coding agent. How do we sort of package it and and and bring it out in the world. And we launched a very like small beta pilot almost in June last year 20 25 and that really took off. And and since then you know like we have been just focused on solving problem for non-consumers. We in fact thought a lot of technical people would use us. But today 80

`[05:04]` **SPEAKER_03:** percent of the users who are on the platform are non-technical users with zero programming knowledge. And they're building like apps that that run real businesses on top of today. So it's

`[05:13]` **SPEAKER_05:** almost. And they're based all around the world right. Like how many countries. Yeah so they're

`[05:16]` **SPEAKER_03:** all global audience 80 percent. 70 80 percent are in US, Europe or 190 countries right now.

`[05:22]` **SPEAKER_05:** Something that we have talked a bunch about at YC internally is just how does first mover advantage versus second mover advantage play out in the AI world. Certainly something that we've talked about a lot is like if we look at some of our company like Legora enter the legal AI space after Harvey. But it's like growing incredibly fast. So there was clearly that it wasn't maybe as big of a moat around being a first mover as you traditionally think there is in software. When you guys made that sort of the pivot or the slight change in direction into non-technical

`[05:53]` **SPEAKER_05:** users at a time when Lovable and Bolt are growing really really quickly. How did you think about

`[05:58]` **SPEAKER_03:** that. There are like two three different different threads I would want to pull. One essentially is that I think the the model every new model generation actually is presenting a new opportunity of looking at the world. Like for example when we started GPT-4 was the first one that we sort of started looking at. And then the biggest problem that everybody was trying to solve was JSON parsing like a structured output format. And we thought okay like the next model is going to solve for it. You know like let's not

`[06:22]` **SPEAKER_03:** spend time on that. And I think with every new model what's happening is that you need to start reimagining the world. For example like Opus is a different class of model right now. It's going to enable extremely long horizon tasks. It's going to enable like multiple agents coordinating together. And so I think like one of the advantages of starting second right is that you can actually one like learn from what is what is not working for the current competition right. And also I think you fundamentally start from a

`[06:48]` **SPEAKER_03:** different starting point right. Like where like your aperture of the world is like very different. Like your imagination is really big right. And I think and when we were starting emergent we realized that like a lot of the users that were going to you know some of these these these apps. They wanted to actually really build an app that works right. And most of these were actually like really really optimized for front-end prototyping at that point. So we started fundamentally reimagining that okay what would world look like if you could actually ship

`[07:14]` **SPEAKER_03:** things to production. And our key insight was that to automate all of software engineering you will have to build a platform that replicates what what best engineering team do. Like code reviews, automated testing, debugging, deployment, security, hosting. So we reimagined the entire platform from ground up saying what would an end-to-end platform look like. And the real user need was actually to build a platform that would be really powerful for the end-to-end prototyping. I think second

`[07:38]` **SPEAKER_03:** thing is like how do you sort of get the distribution because you're coming from behind right. So even if your product is really really strong and fundamentally I think you'll have to enter the market with a really really strong product which is you know head and shoulder above what what what exists in the market today for people to take notice. We're very confident about the product and and so a lot of our focus like in the early days once we sort of launched was on how do we sort of rapidly scale up distribution. We built out a large influencer network and that was

`[08:03]` **SPEAKER_03:** a big part of our program and part of this bunch of influencers to really really spread the word

`[08:07]` **SPEAKER_05:** out and and that sort of you know kick-started the whole thing for us. So to me so building the influencer marketing engine is like it's like tactics to land grab like were you also thinking about just focusing on personas and specific sub types of users you wanted to go after that weren't like either weren't being targeted by level or others or Emergent was a better fit for them.

`[08:27]` **SPEAKER_03:** I mean our our thesis was that like there are a lot of users who would want to build serious And that was our target audience. And a lot of our marketing, a lot of our initial messaging was around that, like, hey, come and ship real software. What we did was a little bit broad-based marketing. But users that were coming to the platform that we would convert were users who actually wanted to ship a real app on the platform.

`[08:52]` **SPEAKER_05:** And was that in the messaging then?

`[08:53]` **SPEAKER_03:** It was in the messaging. Yeah. So we would say, hey, come and build real apps. We would also use the common errors that you would see on other platform, like, hey, don't face this error on the margin.

`[09:04]` **SPEAKER_01:** It seems like a key insight for you. Basically, you went very hardcore in terms of being maximalist in engineering from your experience, having run large engineering teams of 300 engineers, having worked on deep learning teams at Amazon. You really knew how to architect the systems. Can you maybe share a bit how you built it? One of the cons of all these other big products like LevelBolt or Bolt is just that it is difficult to get those into a fully usable. You can get to a product, but you can't get to a fully usable product.

`[09:31]` **SPEAKER_01:** But yours, you went zero to 100% very quickly. And that takes finesse. It's almost like that 20% gets 80% effort, like the Pareto principle. But you did more than that. The last 20% of that engineering to build production was a lot of work. And that's a lot.

`[09:46]` **SPEAKER_02:** Yeah. And I think the last mile that you mentioned is always what people neglect. That, hey, you need to make sure that not only app gets built, it also gets deployed. And this is one of the conscious reasons why we chose to build our own infra on which the agent is running. So we provide like cloud sandboxes. We don't outsource it to some third party sandbox provider, which was also pretty popular at that time. So we built our own Kubernetes tech stack from ground up, the container

`[10:11]` **SPEAKER_02:** tech stack. And one of the insights here is that if you give your agents the same infra during the build time and the same infra during the deploy time, then during this deployment phase, you don't encounter those many problems, right? And the fact that we have our own infra also allows us to give rapid feedback to the agent. So your agent is only as good as the feedback that you provide. So we built this infra and agent co-build it together from day one. And to your point, because we focused on building ship ready apps, which are production ready, which comes with

`[10:44]` **SPEAKER_02:** backend and front end and everything, the tech stack we chose was also pretty unique to us. We have a Python backend server. We have a React front end server. Most people would typically go with a much more node focus, node heavy tech stack. And this server client architecture where you can have background jobs if you want to have background queues. So we knew that users who would use this app, their ambitions are going to go bigger and bigger, right? Hey, I want to run a job which can do this asynchronous video processing, and they're going to prompt it. And we wanted to

`[11:13]` **SPEAKER_02:** support it from day one, right? And so it's the same tech stack on which Emergent is built, is what we expose to our end users, is what we expose to our agents, right? On the agent side, we were very early on the multi-agent architecture. So we knew that you want to be very frugal about your context management. So what you do is, hey, let the main user know that this is what we want to do. And the main agent, the driving agent handle the main routine, but any delegated tasks that you want to

`[11:34]` **SPEAKER_02:** delegate, you delegate to a sub-agent, be it like testing, be it like, hey, I want to do a design search, or I want to do like, you know, integration search. Like how do I integrate this unique API? And along the way, when we were like finding or doing all of this, we were able to figure out, okay, all the trajectories that we are generating, we can kind of aggregate over time and like sort of build in a long-term memory for the agent, which is very unique in the sense that your agent learns not just from

`[12:00]` **SPEAKER_02:** your own session. It learns across the sessions. This is something I would say is one variant of continual learning that people are interested in now. You would have noticed that people are interested in skills, like people create skills and there's a new benchmark called skills bench, which shows agent with skills outperform agent without skills. And interestingly, those skills cannot be generated by agent themselves. If you generate those skills by agents, they don't match up to the performance. So we were able to do it in a way where

`[12:30]` **SPEAKER_02:** the skills get auto, you know, sort of, we are generated based on previous trajectories and we run it through a CI CD process and then add it to the long-term memory. So all of that like compounds for us, right? So if your agent was struggling to do a calendar integration three weeks ago, today, it is no longer struggling thanks to the previous session

`[12:50]` **SPEAKER_01:** where it was able to make it happen. So fascinating. So it learned on its own because I think one of the challenges of all these vibe coding app platforms is at some point, the applications would get so complex that if you build it very simply, you would run out of the context window for all the models, because that seemed to be the bottleneck. And I think you guys architected your way out. So you kind of built a lot of what the state of the art is now,

`[13:14]` **SPEAKER_02:** but way back a year before. Our coding agent is so powerful that we basically internally use it as a replacement for cloud code as developers, right? So we are so proud of that. And, but yet we don't want to expose that sort of, you know, powered tool to our end non-technical users. And so we, even though we have this VS code editor, we kind of hide it, because what we've noticed is that non-technical users, they even get panicked as soon as they see a diff, you know, we had a, like a fairly technical PM in our team and like, he doesn't like, like

`[13:45]` **SPEAKER_02:** JSON, you know, he's like, no, don't show me, you know, I get intimidated. So building that user empathy where you have that user empathy and building that agent empathy, you also have to empathize with your agents. What does, what does agent, what is agent feeling like?

`[13:58]` **SPEAKER_03:** I mean, internally, I have a term called agent experience, right? That we measure that, how, like how, how is agent's experience

`[14:03]` **SPEAKER_05:** on the platform? Actually a really important point. I think people don't realize is you guys actually, you actually started out essentially as sort of Devon cursor in like the actual, like coding agent world for engineers. You just made the choice to package it up for non-technical users. So you're sort of like moving almost in the opposite direction from like a lover board. Like you have like the power, you have all of the actual, like power. You just need to simplify the user experience. Whereas they like sort of have,

`[14:30]` **SPEAKER_05:** they start with the user experience and they're going to have to develop the power over time.

`[14:33]` **SPEAKER_03:** Right. And I think fundamentally it's like, unless you start from, you know, a starting point, which, which sort of solves all of these problems along the line, the whole software development life cycle, it's actually really hard to come from the other side and solve these problems because you'll make some architectural choices, which are very hard to reverse.

`[14:48]` **SPEAKER_05:** Do you have any more, I'm really curious, like any more examples of where sort of, as you were engineering the system, you just trusted in the model. It's like you mentioned JSON parsing, but was there anything else where you're like, let's not invest time in that because like Opus 4.5 will solve it.

`[15:04]` **SPEAKER_03:** I mean, some of them has, has been, for example, you know, like library definition, some of the integrations that we have sort of built, like, you know, we think that, you know, the next sort of models are solving for us. Similarly, like how do you generate unit tests? Some of those things that we actually like would have heavily prompted before. And the other thing that we are very conscious of is that how do we give more and more autonomy to the models as they, the next generations come out. And the more autonomy you're

`[15:28]` **SPEAKER_03:** able to give to the, the models, the, the better they perform, like initially, like our hardness was very strict and, you know, like we would, we would tighten it up. And, and slowly, like what we were observing is that as these models are getting larger and larger, more, more, more efficient, like, you know, like the more control you give to the model, this is making the better the harness gets.

`[15:47]` **SPEAKER_05:** If we extrapolate that out or sort of like really far out, are you worried about where that sort of leaves you as a company versus the mod, like the models themselves and the models get more powerful? Yeah.

`[15:57]` **SPEAKER_03:** I think there is this underlying current right now, right. In the industry that, that, Hey, like is, is you know, like entropic going to eat everybody up. Yeah. I mean, our view is that I think the, the coding aspect is only 20% of the job, right. I think like taking an app to production is like really, really hard. And, and I think what matters is how closely are you working with the user? How, how well do you understand their needs? And I think as the models are going to get more

`[16:19]` **SPEAKER_03:** and more sort of capable, I think the, the human desire is also continuously growing at the same rate. So I think people are going to want to build more complex apps. On the platform. The other thing is that at least with our harness, we're able to extract 20, 30% more on top of these models. And, and essentially like we can use multiple foundation models together to sort of extract more. And I think we'll have to keep continuing, you know, like delivering more and more things to our users. For example, now we're thinking about

`[16:42]` **SPEAKER_03:** like a lot of our users who have built the app now want to help with distribution, now want to help with growth, now want to help with like, how do you sort of, you know, manage users and things like that. And I think for us, the spectrum sort of keeps growing on that side.

`[16:54]` **SPEAKER_05:** I agree with it. I mean, there's, there's another graph that I'm sure, we've shared recently. It's just like the number of software engineering positions available is actually going up. Right. And I feel like at least internally at YC, we're experiencing this. It's like the more powerful the tools get, the more ideas you get, and the more work you want to do. And it just feels like everyone here is working like more hours doing more stuff. And it's just like the rate of like software that you're expected to

`[17:17]` **SPEAKER_02:** ship per week just keeps going up and up and up. It's a hedonistic adaptation to, you know, like, Hey, Oh, this is more powerful and I can do more work. Yeah.

`[17:25]` **SPEAKER_01:** It is really a Javon's paradox. Yeah. At play. And I think there's a lot of concerns as like, Oh, the software engineering jobs will be gone. I don't think that's the case. I mean, based on everything that you're telling us and what we're experiencing.

`[17:37]` **SPEAKER_03:** I mean, I think we are in an expanding market, right? Like we are like letting non-developers not be developers. Right. I think, you know, that market is expanding. We also are internally seeing like the roles sort of combining. So like a PM, a designer engineer, like a single person is doing, you know, like work of all three together. Right. So like we have a PM who's white coding internally things. And recently, like we, um, so we are seeing this internally right now where, um, a lot of the work that was

`[18:02]` **SPEAKER_03:** done by like five, six people team can now be just done by like single engineer or a single PM.

`[18:07]` **SPEAKER_00:** YC's next batch is now taking applications. Got a startup in you? Apply at ycombinator.com slash apply. It's never too early and filling out the app will level up your idea. Okay. Back to the video. Could we see a demo of emergent?

`[18:22]` **SPEAKER_02:** Oh yeah, sure. Yeah. So this is how, what emergent interface looks like. And, uh, I'm gonna like, put a prompt where like, because we were coming for this podcast, we, I thought like, you know, there should be an app which lets you practice, you know, uh, podcast questions, or maybe you are going to a job interview and you wanna practice questions. Right. So you can build a full stack app on, on emergent. You can build a mobile app. Our prompt engine is smart enough that once you give it a prompt, uh, it will figure out that this is talking about a mobile app. So it'll figure out

`[18:46]` **SPEAKER_02:** like, Hey, the, the right agent to use is, is a mobile app builder. Right.

`[18:49]` **SPEAKER_04:** So even though you have like selected the wrong tab, it's just like, uh,

`[18:53]` **SPEAKER_02:** yeah, yeah. The behind the scenes auto. Yeah. I got you. Right. So while, while this is running, let me quickly also, uh, show you a few, uh, user apps. So this is by somebody based out of Illinois. Uh, he's, uh, sort of has a business of audio video set up, uh, that they do like as manually. Right. So basically whatever this kind of like intake form they would have taken through spreadsheet and other calls, they basically build this out without any, uh, coding background knowledge, right? Like, Hey, this is the kind of AV setup I want. Um, so you, you, you go and you

`[19:23]` **SPEAKER_02:** build your room and then you, you get, uh, it's a lead gen sort of a form, but this is a fairly

`[19:27]` **SPEAKER_04:** full stack app. One thing I noticed about that is like the design is really good. Like the icons, like it just like, it looks like a well-designed app. So we have actually spent a lot of time on

`[19:36]` **SPEAKER_03:** design is actually good. Yeah. Like, so earlier there used to be a big trade-off between design and functionality. Like if you were optimizing for design, like your functionality would not be that strong. Uh, and so we had to figure out like, how do we sort of, you know, share the context in a way where design also gets better. There's another sort of person

`[19:52]` **SPEAKER_02:** based out of Norway. He, he sold his previous business to a PE and realized how much lawyers to struggle with spreadsheets and other things. So he built a CRM for lawyers. He, he describes himself as like business developer. I like the word he used. Like I'm a business developer. He doesn't have a programming background. So a lot of CRM related apps, we are seeing small businesses. It's your second monetization avenue. Right. And so like one of the unique things to emergent is that before agent goes off to build things, it asks you for some clarification because

`[20:18]` **SPEAKER_02:** agent wants to make sure that it understood your, your, uh, requirements properly. And, uh, another thing is that non-technical users probably don't know the concept of API key. How do I get an open AI API key? So in this particular case, I can just say, Hey, use emergent LLM key. So you don't have to worry about getting API key from third party.

`[20:35]` **SPEAKER_05:** This feels like a good example of what you were saying. Um, cause this is sort of like the ask user question skill include code, but you just like, I've scrapped that away, but you're just like built into the experience for someone who had no idea about.

`[20:46]` **SPEAKER_02:** Absolutely. I can be very like casual here. I can say, Hey, uh, the, for the first one, use emergent API key, let's assume good defaults and then go, this is the first time I hand off the agent. And like, at this point I can just like close my laptop. We also have a mobile app, so you can like on the go, keep trying to prompt agent. If, if agent requires a additional, uh, thing, once it's done, uh, you see a preview of your app. So here, for example, in this case, I can practice what is my origin story. Uh, I can record, uh, what my origin story

`[21:14]` **SPEAKER_02:** is and I can keep going to, you know, various questions. Uh, eventually this is a podcast preparation app. Yeah. And then you can go ahead and revisit what answers you gave, uh, to your, uh, app. And so what we have noticed is that a lot of personal apps, people use people build mobile apps, but a lot of business apps, they would go and build a web app. Right. So, uh, that's generally the trend we are seeing. The only other thing I wanted to show was, uh, this is, this is an actual Asana clone that our team built, like one of our QA engineers built

`[21:45]` **SPEAKER_02:** internally. And, uh, so this is actual real emergent data.

`[21:49]` **SPEAKER_05:** I'm curious what prompted that? Like, was there some, was there some feature that Asana was lacking or something it wasn't doing that made them say,

`[21:56]` **SPEAKER_02:** Hey, we should just build our own. Yeah. It kind of like started off as a QA, uh, engineer's curiosity. He, he, like his first prompt, I looked at his all jobs. The first prompt was clone Jira. Okay. And then like, he just kept going with that. And, uh, and I think the other thing is we do do things a little bit differently. So for example, we ship like three times a day, morning, evening, night. So we kind of like built it very customized to the way we do things. Like we have a QA of, uh, uh, involvement in, in, in many, many ways. Uh, and definitely like we,

`[22:23]` **SPEAKER_02:** when we were using Asana, it was very, uh, like even though we were using Asana, it was very, uh, like even though we were using Asana, it was very, uh, like even though we were using Asana, it was very, uh, like even though we were using Asana, it was very, uh, like even to customize it, to, to make it to your, uh, work style was not easy. And, and we, we are, we are also saving like, you know, like 3000, $4,000 a month in subscription. Yeah. Yeah. Has anybody actually

`[22:39]` **SPEAKER_04:** edited the code for this or it's just a hundred percent built, built with a merchant?

`[22:42]` **SPEAKER_03:** 100% built with a merchant. And the good thing is that like, if I want to add a feature, I have to just go to that, uh, you know, a project and just add a feature and it just starts

`[22:51]` **SPEAKER_04:** building. It's probably useful for you guys to dog food the platform this way. Cause this is probably, at the edge of the, of the, of the most complex apps people have built with emergent. So it allows you to test what happens when people get to a very complex app like this.

`[23:02]` **SPEAKER_03:** In fact, like a lot of the teams internally are now building, um, you know, apps using emergent internally. So we have like a marketing team built out of complete CRM, completely built on emergent. We are now like, uh, our customer support team is building customer support software, uh, completely built on emergent. And the power is that these are people who are closest to the problem, like who, you know, who understand the problem really well and are able to now build, uh, these apps and the speed at which we are

`[23:25]` **SPEAKER_03:** able to ship, you know, these internal apps is like crazy.

`[23:27]` **SPEAKER_05:** How far down does it go though? I'm curious, like even within the company, do you have people who want that like separate versions of like your internal Asana?

`[23:34]` **SPEAKER_03:** So currently like everybody in the company is using this, this one tool right now. And, and, and it is collaboratively being built collaboratively, right? So like, you know, a PM can give a feature, a QA can give a feature, uh, somebody from our HR team can give a feature

`[23:46]` **SPEAKER_05:** to sort of build that out right now. How do you think this version control, like feature flagging or all this stuff like develops in a world where anyone could just like write a couple of sentences to update the software they're using?

`[23:59]` **SPEAKER_03:** Yeah. So, so there is a testing testing phases deployment phase, right? So we have different versions maintained, uh, right. And, and there is a primary owner of the software, like who actually manages this right now. And, and so it was, it was like, somebody will make a feature request. Uh, somebody will sort of build that out as the agent will build it out. And then like once it's accepted, then it'll go to the release. It's not managed through get though. It's

`[24:20]` **SPEAKER_02:** like your own workflow thing. So you can connect GitHub if you want to, like we internally connect GitHub for our projects. Right. And, uh, like if non-technical developers are outside of emergent, uh, like they actually call GitHub GitHub, right. So they, they have very, uh, like limited knowledge of GitHub. And so they, we, we take care of like versioning on our site, even if they don't connect

`[24:39]` **SPEAKER_01:** GitHub. Talking about how you run your team, the way you hire must be very different. I mean, you're a very lean and small team. How do you hire for engineering? Yeah. So we, we actually from,

`[24:49]` **SPEAKER_03:** from day one have been very conscious of the kind of team that we want to build and essentially like on two things. One is problem solving, like how good are you at problem solving? Uh, and second is ownership. Like we think that people who can like really, really take ownership, uh, you know, like we index on that. And a lot of our early sort of hires were people like, you know, we were really obsessed with like top a hundred IT rankers. So we had this like program going on where like, I told,

`[25:12]` **SPEAKER_03:** you know, our team that, Hey, we must hire like top a hundred IT rankers. Uh, right now I think we have like IT rank one, IT rank 12, uh, all of those people working with us. And a lot of the initials that also came from Danzo. So I, because I was able to build like a really, really good team, we were able to get some, some initial folks from that. The focus that, that we have is, is essentially like one or two people doing work of what a company would be doing. For example, our deployment, which almost mirrors what,

`[25:36]` **SPEAKER_03:** what Vercel would look like is done by two people. Like our memory, like where you have like multiple startups solving for memory is just built by one person. So I think like we, like we give way more responsibility to people. And I think people are generally attracted towards harder problems that they want to solve. Where is your team located? So most of the team right now is in Bangalore, uh, in India office. Uh, we have a small office in SF, like three to five people here.

`[25:57]` **SPEAKER_04:** And you guys yourselves, you're kind of like split across both countries. Can you maybe just explain how the setup works?

`[26:04]` **SPEAKER_02:** Yeah. So, I mean, I, I, I live here in SF. I've been in like, uh, you know, Bay area for like last 10 years.

`[26:09]` **SPEAKER_03:** I split half my time in SF, half my time in Bangalore, uh, constantly jet lagged.

`[26:13]` **SPEAKER_05:** I think you guys are probably the most successful AI company. That's what it's obviously came from. Like it's an Indian company, but that's got like significant presence in India. Um, why is that?

`[26:24]` **SPEAKER_03:** I mean, I think it's like when I went back to India, uh, you know, after Google and I always had this thought that why is there no Google or Facebook from India? Right. So like from day zero, I was thinking, you know, even though I started Anzo, it was an India focused company at that time. And when I was starting, uh, the second company, I always thought like, Hey, there has to be, you know, like we have so much talent. We have, you know, a lot of capital available. Everything's available in India. Like why

`[26:45]` **SPEAKER_03:** are people not building truly global tech first companies from India? And that was the ambition that, that we started with. And in my opinion, I think a lot of it is with, you know, like just your ambition. Like if you, if you just dream big, if you're able to sort of really, really, um, think, uh, global from day zero, I think now because internet is sort of fully penetrated people, people can actually get understanding knowledge from everywhere. I think every single country has an opportunity to build for global audience. And if you have that sort of mindset, that ambition,

`[27:11]` **SPEAKER_03:** I think, I think a lot, we'll see a lot more companies coming out of India doing the same.

`[27:15]` **SPEAKER_04:** I'm curious to hear what it's actually like sort of on the ground running this sort of like split country company where team is mostly in India, but the product is overwhelmingly used in the U S and Eastern Europe. It's not a private for the Indian market at all. What is it like running this company? How would it be different if you had built a normal Silicon Valley style company

`[27:37]` **SPEAKER_03:** that was all based here internally? We have like really, really set really high standards, like as a, as a, as a global sort of product, I mean, both in hiring both in like the way we sort of develop product. Uh, and I think our spending sort of time here also, also helps. Like one of the things that we do really religiously is everybody talks to a customer once a week, twice a week. Everyone in the entire, everyone in the company, right. Uh, they talk to a customer, everybody does customer support. So

`[27:59]` **SPEAKER_03:** like we were like a really, really small engineering team, like 12 people team. And one person was always on call for customer support. It was really hard decision for us because you know, you're a really small team. You need to ship really fast and then move like one of your best engineers out to do customer support was really hard. But I think that really, really helped us build the customer empathy from day zero. And I think given that like a lot of our distribution happens online, like, you know, like the teams are able to learn from digital things

`[28:22]` **SPEAKER_03:** and build for it. But I think us building that customer empathy from day zero, like talking to our users, like really, really helped us bridge the gap, uh, you know, uh, in terms of like what our users want, uh, today. And it's funny because like, when we launched my first, like five days, I was just glued to a desk doing customer service, uh, support, uh, only. And most of the customer requests were coming in, in a different language, like, you know, French, German, because a lot of these are global and thanks to AI,

`[28:45]` **SPEAKER_03:** like we were able to understand that reply to that. And I think that, that, that, uh, you know, like is also helping, you know, us bridge the gap there. Yeah.

`[28:51]` **SPEAKER_02:** And we are hiring Kirin as well. So, uh, if anybody, uh, if anybody, uh, if anybody, uh, if anybody's, you know, interested in, uh, you know, joining, uh, in various positions, like we research across the board, like backend engineers, front-end engineers, we are hiring here in SF

`[29:03]` **SPEAKER_05:** and in Bangalore. I'd love to go back to what we were talking about regarding personalized software. And what do you think the implications are for SaaS in general? You know, like I guess the provocative question is, is SaaS dead now? I mean, you guys essentially killed Asana for yourself. Like, is that bad for Asana and other SaaS companies? I mean, I definitely think that

`[29:21]` **SPEAKER_03:** like the current, um, way, uh, the SaaS industry is, uh, you know, uh, uh, uh, uh, uh, uh, uh, uh, SaaS is existing today. It needs to change. Right. I think like, I feel there are two sort of massive headwinds. One is more and more of these SaaS workflows are going to get consumed by an agent, right? Like, so like, um, you know, unless your SaaS company pivots into like an agent first company, uh, you know, I, I think, uh, that's going to be hard to sort of survive. And second headwind is obviously like, you know, like people would want more and more customized software,

`[29:46]` **SPEAKER_03:** like which they can build on emergent, just like we built, um, you know, uh, our own do it, uh, project management tool. And we are seeing a lot of these people, um, you know, building these internal tools, uh, the software on, on platform like ours. And like, I feel the nature of software itself is changing. I think a lot more software will become agentic in nature. Um, a lot of people are building on emergent today, like roughly 20% of them are actually agentic apps. So people are actually embedding our own emergent agent inside those apps to sort of,

`[30:13]` **SPEAKER_03:** uh, you know, power a bunch of the workflows. Do you have some interesting, that sounds really

`[30:16]` **SPEAKER_05:** cool. Any interesting examples of people? Yeah. I mean, I would like the, uh, uh,

`[30:20]` **SPEAKER_03:** app that Maddy was just showing, uh, you know, the, uh, CRM for, uh, lawyers that is an agentic app where, you know, an agent can take a workflow and, and then run through the process. The software itself is now morphing into, you know, agentic, like a lot of, a lot of people would just want to, you know, build agents that can actually just do,

`[30:35]` **SPEAKER_01:** you know, a lot more of the work, uh, on its own. What do you think this goes as, uh, agents, uh, horizon for task gets longer and longer? I mean, one of the, the meter chart is one of the

`[30:45]` **SPEAKER_03:** ones that was very shocking recently. Yeah. I think that's the chart of the year, I would say, right? Like the, the meters, uh, exponential growth and, and like for 4.5 was at like, I think four hours and 4.6 is at 10 hours. Uh, and we are internally sort of now like, you know, experimenting with agent swarms where agents can actually like work, uh, for a much longer horizon and multiple agents can sort of coordinate on a single task. Um, at least those are like pretty, pretty exciting. Um, you know, we'll see, I think, I think by end of the year,

`[31:13]` **SPEAKER_03:** you'll have, you know, agents which are running 24 hours, uh, and like maybe hundreds of agents collaborating on just single task. Um, and that's where, that's where we sort of see the future

`[31:21]` **SPEAKER_02:** going right now. How are you building for that? People's admissions are increasing, right? Like, and so like, we, we want to like give agents more autonomy, right? And so like the, the, the main thing is to make sure that the trajectory doesn't get derailed. So you always want to have like an overseeing agent, right? Like, so it's like, let's say a few agents are collaborating and there is an overseeing agent as well, which is like parallely like monitoring the overall task. Right. So, so we are experimenting with many different

`[31:44]` **SPEAKER_02:** architectures, right? Like something even as simple as like, just, uh, you know, you would have heard of this Ralph Wiggum loop kind of a phenomenon, right? Like, so the idea that, Hey, like just keep poking the agent, Hey, continue until it's done. And all of that is only possible if there is a good verification loop, right? So it comes back to, Hey, are you able to give autonomous verification feedback to the agent? Like was the job done? So a lot of our work internally right now is in fact,

`[32:07]` **SPEAKER_02:** still going on, on building best verifiers there. We are actually, uh, doing some custom fine tuning as well. So, uh, we are very careful about like, not directly competing with the models in the sense that we don't want to like build a Opus 4.5 alternative right away, but we do want to augment it through our custom fine-tune. So, uh, we are very careful about like, not directly competing with the models in the sense that we don't want to like build a Opus 4.5 alternative right away, but we do want to augment it through our custom fine-tune.

`[32:23]` **SPEAKER_02:** So, uh, we are very careful about like, not directly competing with the models in the sense that we don't want to like build a Opus 4.5 alternative right away, but we do want to augment it through our custom fine-tune. So, uh, we are very careful about like, not directly competing with the models in the sense that we don't want to like build a Opus 4.5 alternative right away, but we do want to augment it through our custom fine-tune. So some of the fun stuff on the research side we are doing is on that side.

`[32:29]` **SPEAKER_05:** How do you think about some movement in the opposite direction? I mean, we talked about sort of like the models themselves maybe getting more powerful and what does that mean for everyone building on top of them, but how about, uh, at least some of the model companies are explicitly trying to build applications and own the application layer themselves. If one of those companies decides like, you know, cloud code for non-technical users is a really valuable application to build, what implications does that have for you? I mean, I think eventually, eventually I think

`[32:55]` **SPEAKER_03:** like, uh, do you understand your customers requirement really, really well? Are you building closer to them? I think, I think all of those fundamentals of like startup building remains the same. And I think, you know, like for us, like as long as we are focused on like really, really understanding our users need really, really best, I think, you know, we'll compete on the process. Do you think, I mean, maybe,

`[33:09]` **SPEAKER_05:** do you think about all the model companies as like the same or are the differences between them?

`[33:14]` **SPEAKER_03:** If you look at the models themselves, right? Like they're very different. Like for example, you know, um, Opus is obviously a workhorse, um, you know, like, um, Codex is really good in back end debugging. Uh, Gemini is really good in front end. So I think all of these models have their own behaviors. And, and, and one of the, like a good thing for us is that we can actually utilize these spikes that model have, like to, to provide the best experience to the user. Um, and I think eventually, like at least my worldview is that most of these models are going to get, get really,

`[33:39]` **SPEAKER_03:** really commoditized, like where all of these models will have similar behaviors. Uh, they'll have, you know, price, you know, price, you know, price, you know, price, you know, price, you know, price, price, competitiveness, um, between them and, and you can already see like, you know, like Opus was like maybe three to six months behind. Right. And, and there's enough optionality for us to sort of really, really build the layer on top where we really meet the user where they are and, and sort of support them in, in sort of their, their journey. Who understands the customer

`[34:00]` **SPEAKER_03:** needs really, really well and, and is able to build for that is going to sort of win the space.

`[34:04]` **SPEAKER_04:** Users have built 7 million apps with Emergent. What are all these apps? Who, who are the users and what surprised you seeing what people do with it? The users who are coming to platform

`[34:13]` **SPEAKER_03:** for us are generally people who want to build a series apps, people who like really, really have a business use case that they want to automate, or they have a business idea that they want to launch. Um, primary users who are coming to us are small, medium business owners. They're running their business today on, on email, WhatsApp spreadsheet, uh, and would have gone to a dev shop to sort of build a custom software, um, to run, automate their business. They're coming to us. And if

`[34:34]` **SPEAKER_03:** you look at the price point that, you know, we are bringing down, it would have costed you like $500,000 to build the software. Now you can build it for $5,000 completely on your own. Um, and, uh, that is the kind of, you know, like unlock that we are sort of bringing to the world right now. Uh, second, for example, this morning I was talking to user Christie, she's based out of Alaska, uh, and she built this, she's a clinical psychologist. Uh, she's also, uh, a sports coach for equestrian, the horse riding, and she wanted to marry these two fields. Like, you know, like

`[35:02]` **SPEAKER_03:** that she has a lot of insights on psychology side. She had a lot of insight on, on a horse riding side. And she said, she looked around everywhere to find an app that does that. And she couldn't find one. She wanted to build one. She, she, she, she, she, she, she, she, she, she, she, she, she, she, she actually went to a dev shop and she went to a dev shop in Nova Scotia and tried to find somebody who can build it. Uh, they were charging her a bomb. So she discovered emergent side

`[35:24]` **SPEAKER_03:** building, uh, out and she, she just launched her app like a couple of weeks back. It's called equally mine on an app store. Uh, and it actually marries, you know, like her insights in psychology and, and, and, uh, into this, this, uh, sports coaching. Um, she has like hundreds of users right now using the platform. I think that is a log that we're trying to build. Like, you know, people who would have been, um, who have had an idea for a long time, people who are like really, really domain expert, very close to a problem, uh, can now go and build, build things up. Um,

`[35:49]` **SPEAKER_03:** we also have like a lot of solopreneurs building platform, like who would have had to go and hire a technical CTO, uh, to, to build these apps. And the success that we are seeing on the platform is like recently somebody pinged me that, Hey, like this company has raised like $4 million, uh, on an ad that was built on emergent. Uh, and I need to get their permission to share more, but yeah. And so I think now we are just truly seeing this unlock where people who were like really close to problem domain expert and, but have been blocked

`[36:16]` **SPEAKER_03:** by, you know, technology barrier to sort of really express themselves are, are, are, you know, like using emergent to sort of build these things out. And also like one thing, uh, these people

`[36:25]` **SPEAKER_02:** tell us that like, uh, it's not just about money, like, Hey, I can give money to the dev shop, but a lot of lot get lost in the translation when you're trying to express your idea to the, through a developer and they say, Hey, I know what I want to build. If I could just say it out my, out loud myself, I would, I would do a better job. And so, uh, the Norwegian, uh, person I was talking about, like, he said that, Hey, in my team, I am the only builder. I don't even bring in anybody else because I know exactly what to build and like others focus on the

`[36:49]` **SPEAKER_02:** business aspects of it. So this like single solopreneur sort of attitude of like, I'm going to do it myself. I have the domain expertise. Nothing is lost in translation. Uh, that kind of agency is what people are looking forward to with these kinds of platforms.

`[37:00]` **SPEAKER_05:** Yeah. I think it's a really important story that doesn't get told enough actually, is like what you're building is really necessary for society. Like there's just so much focus on AI is going to replace jobs. Knowledge work is going away. Like what's that going to mean for employment and civil unrest, but like, no, one's really talking about the fact that actually, like, if you have like some agency of interest and you want to start your own business and have autonomy over your life, like you are empowering that at scale.

`[37:26]` **SPEAKER_04:** It's so cool. The like amount of human creativity that you're unlocking, like who would have thought that the thing that the world needs is an app that marries clinical psychology with horse riding. Um, and in a world of limited software, that app would never have been built, but in a world of unlimited software, you can build that. Yeah. And 7 million other apps that like, nobody would have ever gotten to build before.

`[37:44]` **SPEAKER_03:** Yeah. We're getting to the niche of niches.

`[37:46]` **SPEAKER_04:** Yeah.

`[37:46]` **SPEAKER_05:** I mean, so Pete, this is like just an extension of the trend PG wrote about a while ago. Right. And so like maybe coming out of the second world war, you had sort of like a few big companies and people like built whole careers, hopefully staying at like IBM or whatever for a couple of decades and then retire. Then the startup wave came along and suddenly like the world becomes higher resolution. People like, oh, maybe I should start my own company or at least join a smaller company

`[38:10]` **SPEAKER_05:** and work at my own company. Yeah. At multiple companies or found multiple companies. And like the next extension of that is just everybody like runs their own like business that's at the intersection of like clinical psychology and horse riding, um, and finds an audience and, and life, uh, livelihood that way.

`[38:26]` **SPEAKER_03:** Yeah. I mean, we are excited about so many ideas coming to life. Like we really want to, like reduce this gap between idea and reality and, and, you know, truly enable people to express themselves and, and, and really, really like have this camera and explosion of ideas, like, which is great for YC.

`[38:40]` **SPEAKER_05:** I would argue it doesn't have to be actually like the whole, like, I think it's really interesting. The whole like explosion of being able to start businesses that aren't like venture funded, that aren't trying to raise lots of capital, that it's just like one person like following their passions and like having control over their life. I think it's like, it's really, um, uplifting message.

`[38:58]` **SPEAKER_03:** Right. And I think we're just in the early innings of this right now. Like, I think, I think this explanation is going to grow and, and we'll see larger and larger, you know, projects being built on, uh, emergent. Yes.

`[39:07]` **SPEAKER_05:** Okay. Well, that's all we have time for today. Thank you so much for joining us. It was a really fascinating conversation and congratulations on all the growth and we're excited to see where things go from here.

`[39:18]` **SPEAKER_03:** Thank you. Thank you so much for having us.
