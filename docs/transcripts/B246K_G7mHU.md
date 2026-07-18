# 全文转录 · YC 内部 AI 手册:把公司变成"超级智能组织"

> ▶ [YouTube](https://www.youtube.com/watch?v=B246K_G7mHU) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/B246K_G7mHU.md) &nbsp;·&nbsp; Inside YC's AI Playbook
>
> 🗣️ 说话人分离识别到 **6** 位发言者(标注为 SPEAKER_00 …)。

`[00:00]` **SPEAKER_00:** How do you build super intelligence inside a company?

`[00:02]` **SPEAKER_01:** Part of the key thing is not to just use AI as a co-pilot. This is the thing where you use it as the building layer for everything and you need to start recording all the artifacts.

`[00:14]` **SPEAKER_03:** It's like a shared organizational brain. It's like the closest thing to us being able to like connect our brains.

`[00:19]` **SPEAKER_02:** If you frame this as a way for everyone in an organization to get better at what they do using the like collective skill and instinct of the people they work with, it's incredibly powerful.

`[00:39]` **SPEAKER_00:** Today we have a real treat. We have a special guest, general partner at YC, our partner, Pete Kuhman. He created Optimizely, which was one of the first and one of the best ways to do A-B testing for apps and websites. And since then, he has gone on to create all of our agent infrastructure at YC. So literally, all of our agent infrastructure at YC. So literally, all of our agent infrastructure at YC. All of our harnesses and how we use AI internal to YC. Pete, welcome to The Light Code.

`[01:07]` **SPEAKER_03:** Thanks, Gary. For the last few years since ChatGPT, YC has been funding mainly AI companies. And we've been, we've gone through like many different like versions of advice for them about how to build AI native companies that build like mainly AI products. And we've gone on a crazy journey with them learning all of this. I think a lot of people don't realize that internally YC is actually building and using a lot of the same stuff that we're helping our startups build and use themselves.

`[01:37]` **SPEAKER_03:** And it's been, I think, a very powerful symbiotic relationship for us to actually be adopting these tools and like transforming our own organization, which was started way, way pre-AI into a super AI native organization ourselves. And Pete has really been leading the charge for that. And so I'm really excited about this episode because I've actually been wanting to talk publicly about all the stuff that we've built internally. And this is the first time I've done this. This is the first time that we're doing it.

`[02:02]` **SPEAKER_03:** So Pete, perhaps to start off, you sort of go back to the beginning and like talk about like there was a particular like moment when we really started adopting these AI tools internally. It was really you who got us started down that path. Sure.

`[02:17]` **SPEAKER_02:** Happy to tell the story here. And it's, I like framing it that way because it was a project that I and a few engineers got started about a year ago, maybe a little more, but that has since snowballed into just a whole infrastructure layer that's made it possible for. Yeah. Us to use AI internally at YC in lots of different ways. And that's actually been one of the neatest parts about this is watching the whole engineering team and many partners also just dive in and contribute to this, this infrastructure layer.

`[02:46]` **SPEAKER_02:** We started building our own harness inside of YC or kind of YC specific agents about a year ago. And the original impetus for the project was some of the work that I and a few of the software engineers at YC were doing with our finance team just for a bit, a bit of backstory. So YC has for as long as it's existed, as far as I'm aware, run mostly on our own software in this era, just given us a huge advantage, right? And so with that context, back to this, this moment, maybe a year ago, we were sitting

`[03:21]` **SPEAKER_02:** down with the finance team talking through a set of tools that we were going to build for them, uh, just to help them run through some of their finance workflows, booking journal, and, and I'll say this all the time. interviews, uh, entries, uh, logging, priced rounds, like all the sorts of things that, that make YC run. Really I was seeing kind of two things at once, like on one hand, uh, we, you know, we had this sort of loop going internally right? Where we'd sit down with the finance team, the finance team would describe to.

`[03:54]` **SPEAKER_02:** Our software engineers, how, you know, this complicated financial workflow worked and then software engineers would go and build some purpose built software where there was a deterministic workflow, encapsulating everything that they had been talked about. hold, and then hand it back to the finance team, and so on. And it felt really inefficient. And then at the same time, this was right around the time when agentic tools were really agentic coding tools were really catching hold, right?

`[04:13]` **SPEAKER_02:** And so you had kind of the first generation windsurf and cursor that were well established by this point. I think this right around when cloud code was introduced. I felt like this was giving me superpowers, right? And then kind of watching this sort of old classical way of building software in YC, and then watching how I was doing things on my own machine, it just felt like a bigger and bigger divide between those things. And so the original impetus was, why don't we try to build some tools at YC that we could use to run

`[04:43]` **SPEAKER_02:** agents that would give the finance team control over their own software, right? Like, remove the software engineers from this crazy loop where they have to sort of understand these complicated workflows and give the finance team the tools that they could use to encode their own workflows, not as, you know. Not as Ruby, but as English, with prompts, right?

`[05:03]` **SPEAKER_00:** I mean, what's interesting is, like, we all funded companies maybe even, like, two or three years ago when LLMs were out, but, like, agentic coding wasn't a thing yet. And so the first thing actually was not agentic coding. It was LLMs for writing SQL queries. Yes. So that's what I remember from, like, the first versions of what you built was how, like, good it was and how basically it rhymed with, like, these other failed startups that we had funded. Yes. Like, each of us probably funded one.

`[05:32]` **SPEAKER_00:** At some point, you know, here it was. It was working. And it worked so well that non-technical people, granted very smart people from finance but with no engineering background, could use these tools to ask real questions.

`[05:44]` **SPEAKER_02:** I was really surprised, too, to be honest. And so that we started with this kind of purpose-built thing for finance and then rewrote it to even more of a general agent loop, right? And this is now, you see these all over the place now. But the first kind of magical thing, the magical moment that I had was we had this agent loop. And we had a tool registry, a shared tool registry, for kind of YC-specific tools. And the first tool that really was an unlock for me was, I think, a tool, looking back,

`[06:14]` **SPEAKER_02:** that you actually built, Jared. It gave these agents the ability to run read-only SQL queries against our database. Yes. Right? It was two tools, actually. One was running queries against our database. And the other one was the ability to read our model files.

`[06:29]` **SPEAKER_03:** I remember. I built those tools. And I felt a little bit like I was breaking the rules. Because initially, we started with very limited tools that had very narrowly-scoped domains. And I kept getting frustrated, because they weren't powerful enough to do the things that I wanted. And so I was like, what if we just gave the thing, like, access, complete access to the production database, where we could just, like, trample on anything? And I sort of, like, surreptitiously pushed it out, maybe late at night.

`[06:59]` **SPEAKER_03:** And it worked. And it worked. It worked extremely well, right? Yeah. Perhaps foreshadowing, you know, subsequent things like OpenClaw, where it turns out that, like, the thing that was hampering the world was being worried about security and privacy and all the things that could go wrong. And when you, like, worry a bit less, you're like, oh, my god. These things are unbelievably powerful.

`[07:17]` **SPEAKER_02:** It's another really good example of this weird split between I'm at work, and I'm kind of operating in this really narrow box. And I'm at home using cloud code or whatever, like OpenClaw, or Hermit, and I can do anything, right? And trying to narrow that gap. So why was this so useful, this ability to run SQL queries against our database? It sounds really simple. Well, I think this is where it's important to talk about one of the big advantages that I think YC had coming into this experiment, which is that we run on our own software.

`[07:49]` **SPEAKER_02:** And all of that software sits on one Postgres database that has everything that's important to YC's world in it. You know, every company that we funded, there's a company's table. There's a founder's table, right? There's tables for our financial transactions. There's tables for the notes that I leave in our little internal CRM, right? All of these functions that I think a lot of other companies farm out to third-party SaaS tools, we've built our own. And as a result, we have this database

`[08:18]` **SPEAKER_02:** with every important piece of context that I can now ask questions like, hey, show me all of the investors who invested in a space-related company in the last four batches. Right? It just turns out, when all of that context is in one place, with a little bit of additional information about how the scheme is laid out, an agent can go and ask or answer arbitrary questions about our business.

`[08:41]` **SPEAKER_00:** MARK MANDELBAUM- That was a magic moment, for sure, when I first saw that.

`[08:43]` **SPEAKER_03:** MARK MIRCHANDANI- Yeah. And the cool thing for me is that it didn't just make it easier to answer questions. It dramatically increased the number of questions that we would ask and dramatically increased the scale and complexity of the questions that we would dare to ask. Where, like, in the old days, back when we were using, like, AI tools, to ask a question like that, you know, like, what investors have invested, like, in space-related companies, that would be, like, several hours of writing SQL.

`[09:08]` **SPEAKER_03:** And so, like, unless it was really important, you just wouldn't bother.

`[09:10]` **SPEAKER_02:** MARK MANDELBAUM- It's just another example of the, you know, this instance of Jeevan's paradox that you get when you remove the amount of back and forth between different teams in order to get a thing done, right? If, in order to ask some kind of complex question about YC, I have to go and knock on, you know, the data science team's door and wait for them to get it through, you know, their backlog, I'm just going to ask far fewer questions.

`[09:36]` **SPEAKER_00:** MARK MANDELBAUM- I mean, there are people out there watching this who work in places that still use it. The majority of people live in that world still, and it's 2026, which is a little unfathomable, actually.

`[09:46]` **SPEAKER_02:** MARK MANDELBAUM- There's a long way to go, I think, which is really exciting.

`[09:49]` **SPEAKER_01:** LESLIE KENDRICK- The last one question is, how do companies that live in that old world could get sort of wings to move so quickly? Because the magic for us was, as you said, everything was, the context was in one place. That made it easy.

`[10:03]` **SPEAKER_00:** MARK MANDELBAUM- You know, if you think about data science, historically, one of the first things that the Googlers had to figure out was Bigtable, right? And Bigtable was, you know, instead of schema and joins, you have one Bigtable that can be map-reduced. And so I think that that's happening again, and I would argue that that's happening now with Karpathy-style knowledge LLM wikis with G-Brain. I mean, that's what I'm seeing anyway. Like, you know, obviously, I have an OpenClaw. It has access to lots of systems.

`[10:39]` **SPEAKER_00:** And then I'm normalizing it to my own schema that's relevant to me and the things that I care about. And it is like denormalization. It's you're taking data and you're putting it into a format that is more or less optimized for OpenClaw or Hermes Agent, like that particular type of harness to be able to ask questions. And it needs retrieval. It needs RAG. It needs graph RAG. It needs, you know, hybrid RRF. Like, there's re-ranking in there. Like, you know, all the things that everyone has learned about retrieval is now inside G-Brain.

`[11:08]` **SPEAKER_00:** And then when you give the agents a soul and you give it the data and it knows you and what you care about, like, suddenly these things have insane wings. Like, I just kind of can't believe how it sees around corners. And you might ask a question, and it'll even, you know, sort of interpret what you are what your question was about and, like, give you a thing that, frankly, like, it would take a human who really knows you well to answer. All that's possible now. And so, you know, your question is, like,

`[11:40]` **SPEAKER_00:** all the data is everywhere. My answer from, like, the OpenClaw Hermes experience with G-Brain is, like, yeah, you basically have to take that you're going to denormalize it and you're going to put it in a format that is optimized for agent retrieval and understanding. You could wrap it in an MCP, but for whatever reason, I just, like. intuitively, I'd be worried. Like, it's still sort of, you know, these things are really good at working with MCP and CLI. They're a little even better with CLI.

`[12:06]` **SPEAKER_00:** It seems like you have to denormalize and do the big table thing, but, you know, specifically for the agent.

`[12:12]` **SPEAKER_02:** Looking back over the last year and a half, it feels like we're still kind of in the single-player era of agents, where the harnesses that have gotten really popular, right, CloudCode, Codex, Py, OpenClaw, Hermes, they're all designed to be used by a single human running on a single machine. And it makes a lot of sense, right? Because in that environment, these agents can do just about anything, right? And they make you incredibly powerful. They're a lot of fun to use. I think one of the big problems that I don't think

`[12:46]` **SPEAKER_02:** has been solved well yet by anybody is the multiplayer harness, right? It's enabling that kind of superpower, but on a team or an organizational level, right? And that's, I think. been the interesting thing to explore with the infrastructure that we've built at YC is watching which primitives that we've created that have enabled individuals and teams to use agents. You asked the question about if you're working inside of a kind of a legacy organization, which is like anyone who's more than two years old,

`[13:18]` **SPEAKER_02:** what are the things that you can focus on in order to help enable everybody at your org to use AI to do more? And we talked about kind of this common context layer, right? And so a data warehouse where just as much of your internal important context lives, it just turns out is extremely useful. There are many tools for connecting individual agent harnesses to other MCP tools, other sources of truth. But just like a coding agent inside a model repo just tends to be much more efficient, watching our agents operating on our single database

`[13:57]` **SPEAKER_02:** that has everything in it, in one schema tells me that there's a lot of value at least in getting all of the context into one place. Having an internal tool registry, this is I think the other really important thing that we've built. So in the beginning, like we were talking about, it was just the whole system was really simple. It was like an agent loop and a simple tool registry and a few other pieces, right? Like a model router underneath. The tool registry is where most of the like YC specific stuff lives, right?

`[14:26]` **SPEAKER_02:** Like tool registry is what turns, it turns these agents into something that's useful at work. And we had like 20 tools at the beginning, including this magical ability to query our SQL database. But over time, teams have added more and more tools. Every time we kind of come upon some piece of work at YC that we think could be improved with an agent, we can just add tools. And there's more than 350 today. I just checked, right? Every team is adding their own tools. You know, I can do things like manage my office hours.

`[14:55]` **SPEAKER_02:** Our finance team can, you know, can book journals. We can do internal entries, right? We can help manage the events that we run. There's tools for all of the important work that we do at YC. And now once these all exist in one place, you can make them available to these internal agents that we've built. But you can also make them available to Cloud Code, you know, running on our individual machines. So those things above all, I think, were the important pieces that we built that if I were working in any other organization,

`[15:25]` **SPEAKER_00:** I would focus on building. I mean, honestly, inspired by what you guys, what you did with tools, like this idea of Skillify in OpenClaw. And then actually the most important, the last part of Skillify, Skillify is like this meta skill that I made in OpenClaw where it's like you just do anything in OpenClaw and Hermes. Hermes actually already has Skillify. They call it something that's like, it makes skills automatically. But the most important thing I think is actually like plugging it into the resolver,

`[15:51]` **SPEAKER_00:** which is like your Agents.md with like the list of things that the agents can do. And then like, it links to the, markdown entry point that like lets you use a tool basically and so like this thing keeps coming up in all these different contexts like cloud code has a skill the skill registry in cloud code is actually a resolver our tool registry is actually a resolver and then the weird thing that you have to do on top of that is actually um i have a meta skill called check resolvable that i call all the

`[16:20]` **SPEAKER_00:** time so i'm always like i do something that's new or different in uh in my agent and then after it does it and i like it i say skillify it and then it becomes basically like a tool call or method call and then i run check resolvable which is like you know look at all of the other skills and uh tools that exist and is it you know dry don't don't repeat yourself and is it uh m-e-c-e which is you know i'm embarrassed to say a mckinsey term for um the consultants use it for for uh making really good slide decks mutually exclusive collectively exhaustive that's like

`[16:56]` **SPEAKER_00:** how you're supposed to do slides if you're a mckinsey consultant but it's useful because it's like an additional layer on top of don't repeat yourself dry and like the models just seem to know what those things are and so if you have a dry and m-e-c-e resolver table anywhere it's actually like the optimal resolver like it's bad to have 10 skills that do all the same thing it's good to have one skill or one tool that has parameters that then let you call them so i don't know i think it's like this is like the wildest time to be alive as like an applied computer

`[17:31]` **SPEAKER_00:** scientist because it's like simultaneous like discovery of the same useful applied concepts over and over again and i wonder if like when people are you know developing the first versions of unix or something it's like discovering a stack and a heap it feels like we're right at that moment today like we're just coming up with the new primitives for what i'm doing right now so what an agentic system actually is and you can see it in the parallel sort of development of like we're just trying to do a thing and it might be in cloud code or it might be in our own internal

`[17:59]` **SPEAKER_00:** harness or it might be in open claw might be in hermes like these things just keep coming back

`[18:04]` **SPEAKER_04:** over and over again yc startup school is back we're hand selecting the most promising builders in the world and flying them out to san francisco for july 25th and 26th to discuss the cutting edge of tech and startups apply now for your spot

`[18:20]` **SPEAKER_02:** it's really interesting to look at how some of the other companies that are building this stuff uh have built their infrastructure because you see a lot of these same primitives in in each of them right like there's the agent loops there's tool registries there's skill registries looking at at the way that we're using skills now at yc so if you think of skill as a simple abstraction layer over tools we have a handful of sort of shared skills uh that that we all have access to uh through this through this agent system

`[18:50]` **SPEAKER_02:** and it's been interesting to watch i think you've talked about this for this progression of like in the beginning you were kind of writing your own system prompts and then skills emerged so you started writing your own skills and then you would start uh meta prompting where you uh where you know

`[19:03]` **SPEAKER_00:** you do it again write a skill exactly improve the prompt yes automatically yes seeing us kind of do

`[19:09]` **SPEAKER_02:** the same progression internally where we have a couple skills and now we've gotten to the point where we have these sort of autonomous self-improving loops right uh you know and so

`[19:20]` **SPEAKER_00:** we're able to work in a way where we can take a little bit more practice uh that way you can

`[19:24]` **SPEAKER_02:** maybe move a little bit more fluidly when you're working on a task and make there's a little bit more feedback but it's also easier to put in place a way to just run through it and be like okay this is a good idea and let's just go ahead and do it one more time and then we can just draw some more data and just work with it and we can figure out how we're going to put the

`[19:40]` **SPEAKER_00:** information in that so that way we can actually put in place the especially in the context that really would be useful uh for the training our scenario so in this case we're going to sort of um be more inclusive in the same way that we would in a different way that we would work with potentially um read all the transcripts and then write them back into the internal uh db into the

`[19:58]` **SPEAKER_02:** internal crm on like what we know about people and companies indeed and we there are cool examples of using transcripts actually to make these skills more effective as well one of the shared skills that we have uh is a skill that that partners at yc use to help our companies uh write what we call two sentence descriptions right everybody here has written hundreds of these we should probably

`[20:23]` **SPEAKER_00:** explain what a two sentence description actually sure so a two sentence description is a concise

`[20:29]` **SPEAKER_02:** way of explaining what your company does in natural language that anyone will understand

`[20:33]` **SPEAKER_03:** and why it's interesting sounds easy but it's surprisingly hard for founders to actually

`[20:37]` **SPEAKER_00:** and also no one does it weirdly weirdly like even the most experienced founders like forget because they have perfect context actually interestingly uh i now realize yc itself is uh context engineering uh sort of process in that like people we're frequently teaching people you have perfect context about what's going on in your brain but great communication is replicating that same context in someone else's brain and that's what a two-sentence pitch is like what is it like i don't even know what the heck this is and then second part is like

`[21:10]` **SPEAKER_00:** is it interesting or valuable what you know is it worth my time and so that you know when i when i teach two sentence pitches that's my favorite way to do it do i even know what the heck this is yes because if you don't know what it is you can't even ask a question about it it's like something about computers i guess whatever what what time is lunch again and then the second part is equally important which is like if i've heard that you know there are like 20 companies like there are five other companies in this room that do x

`[21:38]` **SPEAKER_00:** like and then i don't understand like why this is noteworthy like again i'm like thinking about my pastrami sandwich again right so so the two sentence pitch like viscerally

`[21:49]` **SPEAKER_02:** for founders and it's it's a it's a simple kind of atomic thing that every partner at yc has practiced over and over and over again i think tom uh one of one of the partners here wrote a skill that teaches an agent how to uh take some context about a company and can and condense that into a two-sentence description and so that was his sort of handwritten prompt or skill about how that was done and one of the cool things that happened in the last month or two was that a couple of the other partners took a meeting that they had with a group office hours they had

`[22:25]` **SPEAKER_02:** with a bunch of the companies in the spring batch and just went through and had every founder try their hand at a two-cent subscription and kind of gave them feedback and input and so kind of the knowledge that lives in a partner's head about how to do this effectively was exchanged back and forth right and and and now lived in the context of of that meeting transcript and handing the agent and saying given you know what you've learned by reading through this context improve the two-sentence description skill and they got noticeably better after that like this thing is

`[23:00]` **SPEAKER_02:** now better than i am i would i would argue at writing those this is how super intelligence

`[23:04]` **SPEAKER_00:** happens inside organizations i mean this two-sentence pitch thing sounds like something kind of small but uh embedded in it is actually something very powerful i'm sure you guys have heard um jack dorsey talk about what he's doing with block he basically is trying to turn block into a mini agi around helping people in the world make payments to one another right uh and then this is actually the micro mechanism by which he's going to do that right like you can look at the operation of any organization as uh the aggregate of you know i mean the two-sentence

`[23:39]` **SPEAKER_00:** pitch at yc is that's sort of one of like thousands of things that i would argue we do for founders but you know we just walk through a very concrete way where someone wrote a prompt used it used a bunch more other people used it a bunch of artifacts came off of that around literally like the transcript of using it becomes a thing that can be used to meta prompt and improve in an automated fashion on a daily basis the operation of that one skill and then suddenly that one skill you just said it that skill is now better than any

`[24:13]` **SPEAKER_00:** of us individually than bef you know when before we actually had access to that and so this is like a particular like needle pinprick in the fabric of like how any organization does things and then how do you build super intelligence inside a company you do that on everything you do and it's not more complicated than that like you literally just compose everything that you do and any given thing that any given person can do you combine that in aggregate and in this particular process and like you have a super organization it's possible now like every single

`[24:48]` **SPEAKER_00:** person watching this is a super organization it's possible now like every single person watching this can do this at any company at their own company they can do it at their job i mean the interesting thing is that's why you should start a startup because people are going to be trapped in organizations with people running organizations that are very powerful and have all these resources and all this capital that do not believe what we just said because they keep all the contacts locked down right because it's unsafe it's unsafe this is one of those things that we

`[25:13]` **SPEAKER_01:** talk about um how to build that ai native organization right part of the key thing is not to do just use ai as a co-pilot i think that's very 2023 four right this is the the thing where you use it as uh really the the building layer for everything and you need to start recording all the artifacts like people wouldn't have thought of uh meeting recordings and it is one of those reasons why all these uh meeting recorders have been taking off people have been finding them with coaching them on the meetings but it's not just that you could take that and

`[25:46]` **SPEAKER_01:** improve all the output for you that you do like writing emails communication planning you have

`[25:54]` **SPEAKER_05:** the whole context of everything it's funny i remember the dario essay where it's like there's some of the blockers and just the rate of progression of ai are not technical they're just sort of like social cultural things things kind of like a really interesting example two years ago it would have seemed i just remember it felt odd to just like record a meeting or like there was just like people trying to figure out what the like social etiquette around it was and today i just feel like it's almost like default assumed that like most beings are being required

`[26:23]` **SPEAKER_05:** especially if they're on zoom but just in general like everyone started recording things now it's a

`[26:27]` **SPEAKER_02:** little scary but i think if you frame this as a way for everyone in an organization to get better at what they do using the like collective skill and instinct of of the people they work with it's incredibly powerful having a canonical two-sentence description skill is not just a way to like generate a snippet of text for a founder it's a way to help me get better at understanding what makes for effective founder communication right because now i can tap into everything that diana and harge and you two have learned over the many years you've done this job which are now kind

`[27:03]` **SPEAKER_02:** of baked into this skill through the conversations that you've had it's like a shared organizational

`[27:08]` **SPEAKER_03:** brain yes this is very empowering the closest thing to us being able to like connect our brains

`[27:12]` **SPEAKER_02:** right yeah it it totally is right and i can have an agent now come and i can do this sessions with it right i can have it critique my like there there are so many possibilities once you get all of this knowledge into a place where an agent can can work with it uh it's a it's a it's a very empowering thing for every human in the organization there's some subtle interesting

`[27:32]` **SPEAKER_00:** things around here that like you know other people might get wrong that like i feel like we've gotten right i mean one of them is by default the agent conversation is actually um globally viewable by any full-time employee at yc you know we sort of weren't sure about that decision i mean it felt right and it felt like living in the future but it did not come easily i feel like we had a lot of conversations about like well then everyone sees everything is that okay and like you know what is not okay and then i'm

`[28:03]` **SPEAKER_00:** glad we made the choice to keep it open actually because i agree people learned how to use it from

`[28:08]` **SPEAKER_02:** watching how other people used it we used that transparency to solve several problems at the same agent conversation as you mentioned was broadcast internally to a slack channel and anybody could join that slack channel and look and learn right and i remember this is another kind of big unlock one was when you started using it really heavily you were like super creative with with the things you were doing with it and a lot of us watched that it was like oh wow i didn't even you can do that now to use it that way right it allows you to be a little more lenient on

`[28:42]` **SPEAKER_02:** internal security right one of the things we talked about earlier was this trade-off where these agents are at their most powerful when they are given unrestricted access to lots of context which runs counter to the way more most organizations work it turns out that by defaulting to public broadcast for these conversations you kind of institute a bit of a social control on what people can do with it uh that as we learned i think has been like reasonably effective uh inside of this high trust environment at keeping private information private

`[29:15]` **SPEAKER_00:** yeah what's interesting is um it it betrays two traits of uh truly agentic like 1000x super intelligent organizations that i would not have necessarily guessed would exist but are now like must exist if you want to create this type of organization you have to be relatively egalitarian and you also have to be trust by default and then neither of those things uh actually are most organizations in the world if you're the founder of an organization you actually have to have those at the core of what

`[29:43]` **SPEAKER_02:** you're doing and i think like that kind of environment honestly works best at startups right when it's a small group of people that are all aligned and and and

`[29:53]` **SPEAKER_00:** operating in a high trust environment the other thing you have to do is be willing to spend like ten to a hundred thousand dollars a year on tokens but if you're willing to do it and you invest in the skills and you like actually do everything in an open way with your team that way like basically what i realize is it allows you to live in 2028 right like what you spend a hundred thousand or a million dollars a year on now it will be commonplace in the future for the rest of your life

`[30:16]` **SPEAKER_00:** like in in two years right it'll it won't cost a hundred thousand in a year it'll cost ten thousand and the year after that it'll be like a couple hundred bucks right and everyone will do it and we'll call it like this is how companies are now so basically there's a one-time time warp where you can leapfrog every incumbent all fortune 500s all startups that exist by doing

`[30:40]` **SPEAKER_03:** this like I'm imagining in the 90s I wonder if it felt similarly one company started buying computers for their employees yeah they were probably very expensive and probably only certain companies really invested in buying these like expensive flaky computer systems for their employees but like what a superpower to have a computer when your competitors like don't have

`[30:59]` **SPEAKER_01:** computers I think we're technically how I've seen this effect YC has been raising the floor the floor in a sense what I mean by that is that you could have a new employee joining and maybe would have taken them six months to ramp up but with this it's sort of like they automatically get a lot of the context from the company working and they know how the best people on the star players in the organization do things by apprenticeship automatically with AI instead of that because partner

`[31:28]` **SPEAKER_01:** time is expensive or sometimes the best people in an org they're very busy right and you get to kind of run the simulation of what it's like to be like Pete when he does like an awesome job coaching founders on sales or like Gary when he's like talking to founders are giving very specific advice I think it helps all the new new entrants in the organization just be a mini version of

`[31:50]` **SPEAKER_02:** you a lot faster one of the first things that I appreciated about being able to use a coding agent was that all of the dumb questions I was too embarrassed to ask I had no trouble asking asking the agent and it this is kind of that same thing but at an organizational level right you're a brand new employee you're embarrassed to ask you don't want to bug hard with with a question and now you don't have to write you in which on that means a lot more questions get asked and answered and people ramp up much more quickly after

`[32:19]` **SPEAKER_03:** you had built all of this agent infrastructure at YC it inspired you to write this essay horseless carriages that went like pretty viral on the internet maybe you can like explain the ideas behind horseless carriages I think

`[32:31]` **SPEAKER_02:** there's still very relevant now it was a critique of a lot of the the AI software that I saw being built at the time and to be totally honest I think a lot of it

`[32:40]` **SPEAKER_00:** still falls in this still like that yeah it didn't change yes I just saw a lot of

`[32:44]` **SPEAKER_02:** examples people are doing a lot of the research and there's no end to it but it of companies building software and adding AI features by sort of slotting a little bit of AI inside of a lot of software, right? And the example that I used at the time was the kind of email writer that the Gmail team had shipped. But the real idea underneath was just kind of that the potential for AI is to shift control of software from the developer to the user, right? And the simple example I started with was basically that

`[33:16]` **SPEAKER_02:** all of these kind of like AI as a little feature kept a bunch of prompt context about how the AI should do a job locked away and hidden from the user, which was just this classic example of like, well, it's the developer's job to figure out how all of this stuff should work. So the developer should write that and we should protect the user from that kind of complexity.

`[33:37]` **SPEAKER_00:** Safetyism, I hate it.

`[33:38]` **SPEAKER_02:** Right. And it's just, again, going back to this contrast between watching... the way that some of these tools work and what it was like to use a coding agent on my computer that could do anything, right? And feeling like I had superpowers. I think the conclusion that this essay points to is that as we get better at building AI native software, it's going to look a lot more like the agent wrapping software deterministic tools rather than deterministic software wrapping in AI, right? We've done our best to expose that to internal employees

`[34:16]` **SPEAKER_02:** with some of these primitives that we've built. But we have a long way to go.

`[34:21]` **SPEAKER_05:** The chat as the interface, I just feel something... There's like things going around right now about how there's a need to build a new interface for like AI and what does that look like? And I think that just comes from people who haven't like touched and felt it yet. Chat is actually pretty good because like you trust the agent, you increasingly trust the agent to do more of the work and you trust its decisions and you don't actually need to like have too much of a UI. Right. To go in and like review the things it's doing.

`[34:46]` **SPEAKER_00:** It's time for just-in-time software.

`[34:47]` **SPEAKER_05:** Yeah, basically, right? Like, yes, occasionally you want it to present you like maybe like a specific view of something, but...

`[34:54]` **SPEAKER_00:** And it could make the software and build it as a single page JavaScript just purposely built for you at that moment. Yeah. And it could be a skill file that could be like called anytime you want.

`[35:04]` **SPEAKER_01:** I was thinking a lot about this because I used to be in the camp that, oh, perhaps when ChatGPT came out and it was 2023, that perhaps chat was not going to be the UI for all these AI applications. And I've definitely changed my mind. Part of it is like after experiencing all these tools and I think the more I reflect upon it, why chat is probably the better interface is because it's the closest thing to human language and human language and writing is basically the closest thing to expression of thinking.

`[35:32]` **SPEAKER_01:** So chat is the closest stepping stone to clear intelligence.

`[35:36]` **SPEAKER_00:** Yeah.

`[35:37]` **SPEAKER_01:** So you can't just put it in a box. I think it just constrained us too much to have that very specific box. So that's why I thought it's like, okay, all in with chat interfaces. I used to be in the other camp and it's like.

`[35:49]` **SPEAKER_05:** That is multimodal. I know we've talked about like Telegram is not ideal, but I actually really- It's pretty good. Yeah, it's pretty good.

`[35:55]` **SPEAKER_00:** I mean, the voice memos, sometimes when I don't want to type, you just do the voice memo and it feels like I'm talking to me from you.

`[36:01]` **SPEAKER_05:** I can give it text, I can give it voice, I can give it pictures of things, I can give it files. Like it's like pretty good.

`[36:07]` **SPEAKER_00:** Yeah, I just experienced this. So like January, I think the last episode we did, I just talked about this. Like I spent January through February building a half a million lines of code for a Rails app, which was Gary's list. And it was like, you know, I know people make fun of me for like, it was a blog, but it was like, I built the blog in like the first week. Like I spent a month and a half building a full agentic framework that did like my own version of deep research and like fact checking.

`[36:35]` **SPEAKER_00:** But the thing is I built it the way I would have built software in 2013, the last time I wrote code. It was like the web 2.0 version of this. And Cloud Code lets you do that. And what's crazy to connect is like, I'm working like, I don't know, I think I wrote like 40,000 lines of code the last three days just for G-Brain. And G-Brain is basically Gary's list 2.0, but it's totally open source, right? So everything I had to write for agentic retrieval, everything I had to do for voice extraction,

`[37:06]` **SPEAKER_00:** everything I had to do for fact checking, all of that now exists inside G-Brain. And I just gave it to my Gary's list team yesterday as their own OpenClaw instance. And they're flying now, right? Like they were complaining about like, I had made this monolithic writer chat interface and it was like full of bugs because I was like re-implementing things that OpenClaw and Telegram already do. And now they just use OpenClaw, Telegram and my retrieval system with like all the same data that I extracted it out and with our MCP.

`[37:40]` **SPEAKER_00:** And it's working great. Like basically, you know, Gary's list 2.0, the next rewrite, thankfully, is not half a million lines of Rails code that is like insane to actually, you know, it's rigid. It takes a long time. It like takes like 10 times longer, you know, even though it was one 100th the amount of time to do it like by hand, you don't have to do it by hand. Like that half a million lines of code in Rails is easily like 10,000 lines of like TypeScript and like maybe 2000 lines of Markdown.

`[38:11]` **SPEAKER_00:** And all of that is way more dynamic. Like you could just say like, actually, for the second paragraph, I really like including a biography of like the politician we're focusing on. And it's like, I don't have to code that in Rails. I don't even have to write that into a Ruby file that then gets evaled in like, you know, my complex eval infrastructure. Like OpenClaw just knows that and I have an eval skill. My editor-in-chief can just change it on the fly and I didn't touch it. And it's like, this is insane, actually.

`[38:43]` **SPEAKER_00:** This is actually the dawn of just-in-time software, and I can see it right now.

`[38:46]` **SPEAKER_02:** The best AI software that I've used, whether it's inside of YC or tools that others have built, tend to be very small and just add kind of the smallest amount of code ahead of time that you need in order to let the model shine. And you can build an awful lot with that, right? I can write tens of thousands of lines of code, like you're saying. But the ability to start at this extremely simple thing that I need to understand very little in order to use is incredibly powerful, and I think most software in the future is

`[39:23]` **SPEAKER_05:** going to look like that. We were talking about this earlier, but I think that is what OpenCore did really well. There were a few things that you wanted. You wanted some ability to give it a bit of personality. You wanted it to persist and last for a long time and have some concept of memory. It's not perfect. But... That's actually good enough for that use case.

`[39:41]` **SPEAKER_03:** Cloud code, too. Every time Boris comes and speaks at YC, he spoke with Diana earlier this week. One of the things that really stands out is how obsessed he is with simplicity and with just making the product as small as possible.

`[39:55]` **SPEAKER_02:** My favorite example of this is this open-source harness called Pi, which is a project... That's what OpenCore uses as an out-of-the-box coding agent. It's this beautiful piece of software, which is just the smallest possible coding agent. You can use Pi to modify and extend Pi, right? And it's this kind of idea of self-extending and self-referential software. It's really fascinating. And you're right. OpenCore was built on top of that. One of the things I'm very curious to see is how many other pieces of classic software

`[40:25]` **SPEAKER_02:** emerge in this form as this kind of minimal thing that you start with and then use an agent to extend over time. I think more and more... I mean, looking at, honestly, the benefits that we've gotten from having our own customizable software, I suspect that a lot of commercial software will come with this capability out of the box in the future.

`[40:45]` **SPEAKER_00:** There's a really interesting subtle thing that I wanted to talk about around what I learned from your essay, which is AI can either be centralizing or decentralizing. And the Google, Gmail, I can't change the prompt thing is the perfect example of that. We basically have a choice to be made over the next... I don't think it's even that long. I think it's 18 to 24 months. It might take a while. It might take five years, but there are sort of two scenarios. And what comes to mind is literally the 1984 Macintosh commercial by Apple, where it's

`[41:19]` **SPEAKER_00:** like, is 2034 going to be like 1984? And the 1984 case would be, we have centralized control, there are five kings, there's only... One of them maybe wins. They have the most advanced AI. They have end run around all compute and power. They have all the space data centers, because you can't build any terrestrial data centers in America anyway. There's this centralization of control. And not only that, they don't let you run your own prompts. They literally do the Gmail thing, but for your whole computing existence, right?

`[41:55]` **SPEAKER_00:** And this would be as if personal computers never existed and there were only mainframes and mini computers. This is sort of lost to the sands of time, but in the 1960s and 70s, when computers first came out... You couldn't go to the store like you can today. You couldn't go to an Apple store and just buy an iPhone, let alone a Mac. You had to get access to this thing that was worth hundreds of thousands of dollars to millions of dollars.

`[42:22]` **SPEAKER_03:** And the only... And it was tightly locked down by corporate policies, you're right. And the thing that really spurred the computing revolution was when people started having personal computers that they could experiment on.

`[42:33]` **SPEAKER_00:** Yeah. And just like the priesthood, right? There was a small priesthood. There was a small priesthood and an institutional base that controlled capital, literally the means of production. And so this is like a coherent future that we could live in that I don't want to live in. And the alternative to that is actually embedded in the homebrew computer club. It's embedded in the revolution that Steve Jobs and Steve Wozniak gave us when they were in the garage in Mountain View, literally soldering together breadboards and like sold

`[43:03]` **SPEAKER_00:** 500 of these Apple ones. Yeah. So we're at the Apple one moment right now. We are coming up with the primitives. We're learning how do these things work and how do we sell it and how do we package it? But then there's like a lot of choices right now, right? Like most people, the mass, you know, a billion users use ChatGPT and ChatGPT like gives you a little access, but MCP is really locked down. You actually, you know, can't hook things up to your own databases that easily. And, you know, for what?

`[43:35]` **SPEAKER_00:** Safety, like I would argue Claude is like a little bit more open, but not really. Perplexity Computer is probably the best version of it, but it's still like, you know, pretty limited compared to what you could do with OpenClaw and Hermes Agent. And so what does the revolution look like that is like the true personal AI moment? And that's what I hope that we are building with things like G-Brain and, you know, Hermes Agent and OpenClaw. Like the ability to run your own. Software to change your own prompts, to test all of it, to have your own private repo that

`[44:12]` **SPEAKER_00:** like, you know, is only yours to be able to choose which model to use. And maybe it's an open weight model. Like to me, that's sort of the white pill for AI is we could have corporate control, no control of your own prompts and like literally the AI happens to you, you know, you're under the API line or like there's this other alternative where. I want like a billion people to actually control and program for themselves. What are these things? This should be an extension of yourself and what you care about, not what, you know, meta

`[44:47]` **SPEAKER_00:** or alphabet or even opening our anthropic care about.

`[44:51]` **SPEAKER_02:** I always really bristle when I see AI framed as a way to replace people because it just doesn't match the way that I have experienced it in the way that so many of the people around me have experienced it. Not as a replacement. Not for humans, but as a thing that empowers. If you look at, at, at kind of how tech has developed since the era of, of mainframes to PCs, to the internet, which gave everyone like a publishing platform, like it's, it's a story overall above all of individual empowerment.

`[45:19]` **SPEAKER_02:** And I think AI is going to play out the same way. I think it is going to enable us to do more than we could before. I think it's going to eliminate kind of the drudgery style work that like made a lot of my job painful in the past.

`[45:33]` **SPEAKER_00:** To me, it's like. To make choices to do so by default, like a company is not open by default. A company is a command and control by default. Maybe the leadership gets access to these tools, but like the, you know, line level people, the staff people don't right. And like you, we need like a radically different type of organization and we need to actually offer computing in a different way. And these are all choices and the people who are watching are going to be the people who build all these things in society.

`[46:03]` **SPEAKER_00:** So. We better choose well, well, that's all the time we have for today. I mean, I think we covered some pretty heavy stuff, but Pete, thanks for joining us. Thanks. Thank you. Thank you. Thanks for watching guys. We'll see you guys on the next one.
