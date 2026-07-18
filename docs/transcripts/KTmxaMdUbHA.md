# 全文转录 · AI 正在吞噬物流:Flexport 的自动化实战

> ▶ [YouTube](https://www.youtube.com/watch?v=KTmxaMdUbHA) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/KTmxaMdUbHA.md) &nbsp;·&nbsp; AI Is Eating Logistics
>
> 🗣️ 说话人分离识别到 **5** 位发言者(标注为 SPEAKER_00 …)。

`[00:00]` **SPEAKER_02:** Logistics are a very scale-driven industry, and so the bigger you get, the cheaper you get. Our take is that we can make the price of shipping anything by ocean container shipping between eight and ten percent cheaper over the next few years, and AI is a big part of that. So our AI for that saved us two percent of our ocean freight spend, while improving transit time 20 percent. Usually that's a trade-off. It's like either faster or cheaper, but not both.

`[00:25]` **SPEAKER_00:** And you're at two billion dollars of your revenue and just getting started. Welcome back to another episode of The Light Cone. We've got a real treat today. We have Ryan Peterson of Flexport with us. He went through YC in 2014, and he is easily one of the most awesome founders I've ever met. Ryan, thanks a lot for joining. Thank you. To start, Ryan, what is Flexport, and what are some of the things in AI you're actually implementing right now?

`[00:58]` **SPEAKER_02:** So Flexport is a global logistics company built around a modern tech stack, and that means we help companies ship cargo from point A to point B across any mode of transport, so air, ocean, truck, and rail, and get that cargo delivered, hopefully on time and in full at a lower cost, thanks to the tech. What we're doing with AI is, I had to make an exhaustive, we have to extend the length of the podcast to pull that off, but starts with customer user experience. What can we do with their data,

`[01:26]` **SPEAKER_02:** getting them better access? How do we load containers in the optimal way? How do we put that container onto the right ship at the lowest cost while maintaining or beating transit time expectations, automating just tons of work that's done in email, or phone, or work that you wouldn't even do because the cost is too high for a human, but actually does create some value that's worth it with AI. So most contracts in logistics come in giant Excel files, thousands of rows and a dozen tabs. You can't just feed that to open AI and get a structured

`[02:00]` **SPEAKER_02:** JSON file back. It needs intelligence, but writing code and then having AI write the code, you write a parser that ingests it and then have AI that can write those parsers for you learning. It's an endless list and we feel like we don't even know all the

`[02:14]` **SPEAKER_00:** things that it can do. It's still pretty new. So basically one of the most human intensive things now can be streamlined to the point where actually it might affect GDP in the world.

`[02:25]` **SPEAKER_02:** Our take is that we can make the price of shipping anything by ocean container shipping cheaper by between eight and 10% cheaper over the next few years. And AI is a big, not the only part of that, but a big part of that. As our business model, the way we think about it is as I call it scale economies shared, which is the bigger you get, the cheaper you get. Automation is a form of scale. And the bigger you get or the cheaper you get, the lower your costs, you give that, share that with your customer, which will make them

`[02:53]` **SPEAKER_02:** do even more volume with you. There are scale benefits that come, logistics are very scale driven industry. And so the bigger you get, the cheaper you get. Like the Costco model, I love Costco, even though I don't shop there, I just love the business. You keep driving down the price that makes you more attractive, more competitive and just keep going. Yeah.

`[03:12]` **SPEAKER_00:** And you're at $2 billion a year revenue and just getting started.

`[03:15]` **SPEAKER_04:** Just getting started. Yes. Something I'm curious about. So from our perspective, we work with all the startups and we've seen AI over the last couple of years go from when ChatGPT launched and then some startups in the back start playing around with it and it's become progressively more serious. I think you're the first person we've had on the show who's running a company at scale that was founded pre AI. What have the last few years been like for you from that perspective, from like ChatGPT

`[03:39]` **SPEAKER_04:** launch? Like at what point did it start becoming like a thing you were paying more attention to?

`[03:44]` **SPEAKER_02:** Like so many other people is on November of 20, was it 2022? It's already been a few years since the ChatGPT launch, been personally obsessed ever since then. It's interesting to watch it take hold at the company and in some cases not take hold and you then saying like, come on guys, we can't be this boomer company. Like everybody needs to be using this. We're trying to drive that sense of paranoia from the top, from me, but many others in the company, maybe even more paranoid than me or more enthusiastic, excited

`[04:13]` **SPEAKER_02:** than me as well to say that story that we say of like, well, we're the only large logistics company founded since the web browser. And I know there's a kid in the next YC batch who say, hey, we're the only break border founded since ChatGPT November 2022. Like it has got a point. So we have to be leading on this. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. This is true of all incumbents in an industry. They have some real advantages when it comes to AI and benefiting from it. And one is the scale of the data. Two is the domain

`[04:44]` **SPEAKER_02:** experience to know, okay, which problems should we be solving? And some of those problems are small enough that you shouldn't start a whole company around the problem. It's maybe a feature, not a company. But for them, it's great. It's a valuable feature that they could add. And third is distribution. Like when we build or any large company builds a great AI product, the next day it can be used by thousands of companies. Whereas a startup doing that has to go beg people for their data to train the model and earn their trust to have that data from a

`[05:14]` **SPEAKER_02:** security compliance standpoint. And then third, get the customer. So that's the huge advantage that any incumbent will have. And we definitely feel that we have that advantage at our scale. But the flip side where I think we also have an advantage is that we are still a young company relative to our industry, but young in terms of our tech stack. Like we've built a lot of tech. We build our own tech. Therefore we can implement and integrate AI and just add it wherever we want. Most of our competitors treat technology period as IT, as a service that they

`[05:46]` **SPEAKER_02:** pay for. Many cases like desktop app or like Windows remote desktop is very common in our industry. But still it's something they buy and therefore you don't control the code base. If you wanted to add AI to automate something or do something that you're like, it's not really,

`[05:59]` **SPEAKER_04:** it's hard. Has there been a specific moment since ChatGPT launched where you started as a company, like taking it more seriously? Because my impression, like the first version was a toy, even within the YC batches, like we sort of see some founders playing around with things, but it wasn't clear that they'd actually be like companies founded on it. So I'm just curious what's like founder running large scale company. You start out, you're like, this is really interesting to me personally. Like, was there some moment where you're like, oh, like we should probably

`[06:24]` **SPEAKER_04:** try and like build something or do something internally with this?

`[06:27]` **SPEAKER_02:** Yeah. I think a lot of it has come through in our hackathons, but there could be an interesting metric here is like what percentage of hackathon projects, first of all, used AI, like we're building something with large language models, and which percent of the projects actually you decided to fund and push into like, oh, let's actually make this thing

`[06:43]` **SPEAKER_04:** real. It's not just a hack. Is hackathon something you've done for a while? Is that like-

`[06:46]` **SPEAKER_02:** Yeah. We usually do two a year. Okay. I think now we're like kind of religious about two every year, but one to two a year where, and for us, it's very much a free for all. You can build anything you want. If you look now at the last two hackathons we've done, it'd been like 90% LLM based projects. I haven't studied it, but it was just like my feeling in my gut. Whereas probably 18 months ago, there were like four or five. There's probably 50, 60 teams that do a hackathon project each time. In the beginning of Flexport, I was very much of this idea that like, you just

`[07:21]` **SPEAKER_02:** get smart people and get out of their way and go execute. Oh, that sounds like manager mode. Yeah. I had way too much manager mode. I had this idea of like human beings are going to flourish. If only they could be set free. They don't want to be told what to do by the man. That's why I started a company. I don't want to be told what to do. And I went through my own Chesky moment of founder mode and recognizing, oh, you gotta be way more tops down and directive and tell people what to do and get people aligned and

`[07:46]` **SPEAKER_02:** rowing in the right direction. And that's been my evolution the last two years at Flexport. I've been pretty way more hands-on and hardcore and directing the business. But then as I see these hackathons, I'm like, I never would have come up with that idea in a million years. And I got to let these guys build what they want to build and flourish. And so I'm starting, and I'm going to now come back on myself and say, where's the room in our product roadmap for bottoms-up innovation? Certainly you see it in these hackathons and trying to maybe even start

`[08:15]` **SPEAKER_02:** making sure I do the hackathon timing before we do our roadmap exercise every six months or so. We should probably do the hackathon right before that so that when you see a great idea, you can budget it instead of after the budget. I mean, there's a noteworthy change here

`[08:28]` **SPEAKER_00:** that's happening for you. I mean, I think most companies might throw a hackathon, and then in most hackathons, 90% of the projects are just toys and you never return to them again. Someone gets a nice participation trophy and that's it. But it sounds like the difference right now in the age of LLMs and age of intelligence is that these hackathon things are actually turning into real product lines and features for you.

`[08:54]` **SPEAKER_02:** Yes. And at the very least into debates in my head of being like, man, I've got to do that. But we're going to crush everybody with just our regular roadmap. Yeah, absolutely. Yeah. Yeah, absolutely. Absolutely. I had this after the very last, I think our next hackathon's in two weeks, so the last four or six months ago. I remember thinking afterwards, I'm like, you know what, we could just only do that stuff and we'll also win.

`[09:13]` **SPEAKER_00:** Yeah. Maybe win faster? Maybe.

`[09:16]` **SPEAKER_02:** It's highly unlikely that the person at the top now knows best what the best implications are, applications are, that it's just as likely that someone on the front lines closer to the problem is going to go, hey, look, watch, it can do this. You go, oh man, I wouldn't have guessed it could do that.

`[09:30]` **SPEAKER_04:** You kind of need engineers who are just really into it and have been playing around with it and just understand how to build the products in the first place to come up with the ideas.

`[09:37]` **SPEAKER_02:** Yeah, engineers and engineers being really close to the business is something we've always prided ourselves on, like really being in the weeds. And one of the other things that we've done is create a program for non-engineers to learn AI skills and a kind of formalized program. So your manager has to agree, but you get one day a week for 90 days. It's a 90-day program. One day a week where we teach you kind of a... AI bootcamp, vibe coding, and different ways to apply. And it's a new program, so we're only about six months into this.

`[10:08]` **SPEAKER_02:** You'll see how it works out. But people love it, and you are seeing gains. But the promise of the leader who created this and convinced the managers to give up someone for 20% of their time to go into it was, I will return them to you as 10 times more productive than their peers. I'm sure we haven't have achieved that or it would show up in the metrics, but that's the idea.

`[10:28]` **SPEAKER_01:** How are you training all these folks to up-level skill in AI? What are the sorts of things they're learning?

`[10:34]` **SPEAKER_02:** Certainly, it's Cursor and a set of related products like that. I think we're using something called Streamlit, but probably there's YC Company. I don't know. Maybe we should use Replit or something, but it's similar ideas. You can spin up, build your own little apps, build workflow automation tools to say, okay, because a lot of what Flexport is, we call it freight forwarding. I've often joked it should be called freight email forwarding. You're like taking docs and sending it on. So how do you look at a person's...

`[11:02]` **SPEAKER_02:** job and there's no one better to look at it than the person doing the job and saying, oh man, I'm doing the same thing over and over again. What if I instead... it's like if everybody was an engineer, they would... and I've thought about this in the past is saying, hey, what if I took one group of engineers and hire them as engineers as a big bait and switch, and then tell them, actually, you're just moving freight, sorry, and watch them automate their way out of the job. Right. And you sort of say, okay, I never really wanted to do that to an engineer because I feel

`[11:28]` **SPEAKER_02:** like I'd just have a revolt of them. Yeah, yeah, yeah, yeah. But... now you're kind of like, well, I could do it to a non-engineer who's already doing that job and turn them into a, you know, a lightweight, low-code engineer. Which is cool.

`[11:40]` **SPEAKER_01:** Yeah. It's going the other direction where you're taking really all these super domain experts and now they can finally build and they can automate themselves out of it instead of getting the engineer to do it.

`[11:49]` **SPEAKER_02:** Yeah. And that program started on our Amsterdam. We have an engineering office in Amsterdam. It started there. I think they did it without me knowing about it for the first six, few months. And then now we're like, oh, this is great. Everybody loves it. So we're starting to bring it global to other offices.

`[12:02]` **SPEAKER_03:** I wonder if you could share some examples of the AI projects that you have rolled out that have been most impactful over the last couple of years, both customer facing features, but also like any internal operational things that you guys have automated that maybe the customers have no idea about.

`[12:17]` **SPEAKER_02:** Yeah. The customer facing one, probably the most impactful, like a lot of what you care about from your logistics company is your data. What's going on with my supply chain, the types of data that people are looking at. So the way Flexport works, you place orders to your factories through Flexport. So I'm replenishing my inventory, I'm buying things, I'm placing purchase orders. So those flow out to the factory. Factory becomes a user. There's a nice network effect there. Once the cargo is ready, they place a booking.

`[12:44]` **SPEAKER_02:** And then we execute that, a booking to move the freight, come pick it up on this date and we'll execute it by air, ocean, truck, rail, whatever, and move it across the world for you. So that's kind of the loop that we're trying to run. So you care a lot about the data for on-time performance, SKU level performance, cost, you care a lot about that. There's customs attributes here that are super important with tariffs and everything's happening. So being able to get that data is one of the core areas that Flexport shines already, historically.

`[13:14]` **SPEAKER_02:** With AI, and this did start as a hackathon project, we just built like natural language ability so that you don't need to know SQL, you don't need to build dashboards, you just type your question and it generates those graphs, charts, tables, don't think it does maps yet, but it should. And it works. And that has done wonderful. Wonderful. Customers love it. But two is it's about 25% of our account management time is spent helping people generate reports. That's another huge metric for us.

`[13:43]` **SPEAKER_02:** If we're cheaper, more people will choose us. It's not that we just started using AI with LLMs. We've had a machine learning model for doing planning for, and planning in the sense of logistics means, let's say on a containerized basis, I've got a container, which ship should it go on? You've gotta look at all the contracts with their price. You need the sailing schedules, how long is it gonna take? Which route variability, all around those, both those things. Our AI for that saved us 2% of our ocean freight spend while improving transit time, 20%.

`[14:19]` **SPEAKER_02:** Usually that's a trade off. It's either faster or cheaper, but not both. Huge win there. Customers don't, they care a lot about those metrics. They don't care how we did it.

`[14:29]` **SPEAKER_03:** And for that one, was the unlock parsing a bunch of computers? Yeah. Yeah. unstructured like emails and data that you get from the shipping companies that have this but it's all like in like a big paragraph where like you couldn't just like run a simple query on it

`[14:40]` **SPEAKER_02:** before sort of yeah the way to think about it is um you've got if you just put a container on the cheapest contract you you made uh it's an optimization okay which one's the cheapest but also the fastest you know i'm trading off so that that's one thing that machines are better at uh and then it's the scale of that so on a given week we have about 2 000 containers that get canceled by our customers they place the booking and then they say oh actually the cargo is not ready the factory is late it's just inevitable it's going to happen what software does that

`[15:07]` **SPEAKER_02:** humans could never do is go through 10 times a day and taking each one of those containers and say okay i lost this container it's been canceled is there another container that was meant to depart one week from now and i'll grab that and move it forward that's how you get the 20 transit time increase and then the optimization piece of fine is just find the cheapest contract like a solver out you know algorithm to go find the humans can't do that because it has to happen

`[15:28]` **SPEAKER_04:** really quickly

`[15:29]` **SPEAKER_02:** is this happening 10 times a day for every container in the system okay you know it's

`[15:32]` **SPEAKER_04:** just like you wouldn't you maybe you could but you wouldn't you have to like an all-inclusive

`[15:35]` **SPEAKER_01:** cost would be crazy if you calculate this first principle sounded like that first version was using classical optimization problems and you had certain data about all these shipments inputs outputs unscheduled what do you think is the delta that you could get with ai now that you could harness all the unstructured data what kind of efficiencies could you get you may be able to

`[15:54]` **SPEAKER_02:** get a lot more now that you're starting to see tool use because the tool itself is incredibly powerful and i don't think an llm will outperform that but the llm can use that tool and it can do other things outside of that so you can we'll see we haven't started to do that yet so we're actually

`[16:09]` **SPEAKER_04:** still using that i can actually email people or call them up and yeah but it could its you assign

`[16:13]` **SPEAKER_02:** the llm the same solver problem but it is going to default to use this tool and then it'll also say yes maybe this container i'm not sure if i could move it forward i should ask the customer would be a good idea actually email that hey is it okay if i bring you this container early like the solver's

`[16:28]` **SPEAKER_00:** but then basically the agent is the user.

`[16:32]` **SPEAKER_02:** MARK MANDELMAN- Yes, instead of right now there's not really a user, there's someone who's approving the plan. And so you could make that person upstream of the solver, choose the solver as one of many tools. So that'd be interesting. We haven't done that yet. And then the other thing is just routine work. For example, you've got a lot of email communication with your customer base. So how do you take this? You say, hey, I want to place a booking for a container. Translate that into a booking.

`[17:01]` **SPEAKER_02:** LLMs are quite good at that. A big use case today is verifying warehouse addresses and other information and getting appointments. I've got to deliver to a warehouse. Quite costly to call the warehouse and be like, do I have the right address? You're not going to do it every time. And then you have a lot of misses where your address data was bad, and your truck got lost, pain in the ass. So LLMs, now before we deliver, if we haven't delivered to the site in the last three months, there's an LLM agent.

`[17:29]` **SPEAKER_02:** It does email and voice.

`[17:31]` **SPEAKER_03:** MARK MANDELMAN- Interesting. Wow. So if necessary, it'll actually call the warehouse and be like, hey, can you confirm that 2 PM tomorrow is an OK time to deliver this? LLAMAS GORDIUS- Yes. Yes. MARK MANDELMAN- Wow. Very cool.

`[17:41]` **SPEAKER_01:** LLAMAS GORDIUS- Which is great, because you're turning this previous communication protocol, which is very much, I suppose, very lossy, to work sort of like the internet, like TCP, fully acknowledge, and you can get guarantees.

`[17:54]` **SPEAKER_02:** MARK MANDELMAN- Sometimes it's not replacing work, although I'm very happy to do so. But like, in some cases, the work would have been too expensive, so you just didn't do the work. LLAMAS GORDIUS- To do this phone call. MARK MANDELMAN- And even if a human could do it, it's just not worth it. Another good one is just messages. So the way we communicate with our customers, some of it's email, but a lot, we try to drive as much as possible through our messaging applications inside the Flexport platform.

`[18:15]` **SPEAKER_02:** There's this huge amount of signal in that customer sentiment. If a customer, in AI, we've trained the model to detect unhappy customers in the way that they message us. And then that creates an automatic escalation to the manager of the front line person saying, hey, this person seems upset. There's a lot of emotion in logistics. You know, it's your stuff. Your business is on the line. You need to get it delivered. In fact, we measured, at the beginning of the year, we had automated 20% of the work.

`[18:46]` **SPEAKER_02:** It was pretty low scale of automation. We're going to finish this year at 50%. And we had set a goal for ourselves next year of 80. We thought 80 was actually the upper limit of what could be automated. It's not scientific. But now we feel like, oh, it's probably closer to 90 to 95 current. And then that'll get way more so as LLMs keep progressing.

`[19:07]` **SPEAKER_03:** How will that affect the total cost of ocean freight? If all the human work gets automated, does stuff actually get materially cheaper?

`[19:15]` **SPEAKER_02:** Yeah. It's 10% of the end cost that the importer exporter pays for their freight. 10%, if you look at the full P&L, about 10% is the labor cost in the freight forwarding layer of logistics. Wow.

`[19:29]` **SPEAKER_03:** So when AI is fully rolled out, stuff will actually get 10% cheaper. Well, the freight of moving the stuff, the cost of moving it. The stuff itself depends on what the ratio is. But yeah. But the transportation costs of international freight is actually 10% on it.

`[19:45]` **SPEAKER_02:** On containerized ocean freight, that's our view, is that we can drop the price of everything by around 8%. And maybe it goes to 9% over the next few years by doing this.

`[19:55]` **SPEAKER_01:** That has some big economic ripples, in terms of, wow. Yeah. Yeah. Yeah. In terms of, if it's becoming cheaper to ship things across the ocean, is it going to create just more trade? I mean, there's also trade wars, but.

`[20:05]` **SPEAKER_02:** Exactly. It's very hard to control for that in the world where tariffs just made everything like 10 times more expensive. But we're doing our part.

`[20:11]` **SPEAKER_00:** I mean, the white pill on AI right now is this hope and sort of possibility that AI rolled out properly across society would increase GDP 7% a year. So this would be maybe a few percent.

`[20:24]` **SPEAKER_02:** 7% a year will double you in 10 years is the law of 72. Yeah. Yeah. That is the hope, right? And I think more people should talk about that. And everyone's so worried about automating away the jobs. And I just think that misunderstands the role of companies in society. Like, the role of companies is not to employ people. It's to deliver goods and services. And in fact, whoever employs the least number of people will have the lowest cost and win. And that's how they benefit society, is lowering costs

`[20:51]` **SPEAKER_02:** and making things more available for us to buy and sell. And there's this idea, well, how are people going to make money if AI is doing all the work? And I think that that very much misunderstands human nature, that we'll just want more things. Like, there's an infinite desire inside the human soul can never be satisfied without God. We need more stuff. Like, we've got to have more. We've got to have more.

`[21:13]` **SPEAKER_00:** And so we're trying to return to the garden.

`[21:16]` **SPEAKER_02:** We may get a return to some. I think that, actually, the internet first, we haven't quite reconciled this on a spiritual, philosophical level, the emergence of these technologies. And AI would not even believe it. It's not even beginning to, of what it means for us. But there's a period in history called the Axial Age. It's about 500 years BC. And that's when coins really started to spread. What you had, if you think about it, with coins, is taking transactions between two people and really making them very impersonal.

`[21:47]` **SPEAKER_02:** You no longer care who you're doing business with. I don't need to have a ledger. Does this guy owe me money? What's my relationship? Do I trust him? Just like, here, take this thing. And it actually led to this breakdown. And it actually led to this breakdown in societies, because we just stopped being so knowing your neighbor. You used to only do business with your neighbors. Now you could just do business with any old person. The internet kind of does that at scale. What happened in the Axial Age, you

`[22:12]` **SPEAKER_02:** had this breakdown of ability, of trust. And you started to get degeneracy and all kinds of things that start to break down in society. And simultaneously, across the world, you had four major prophets that emerged. Well, prophets of sorts. You had Buddha. You had Lao Tzu, Confucius, and Socrates. They all lived at the exact same moment in time, right, as coins were taking hold. Fascinating. As like, hey, we need to kind of get our hands around, how do we behave in this new world? So I do think there's an opportunity here.

`[22:42]` **SPEAKER_02:** Maybe it could be you, Gary, at YC, to be the next Socrates, yes, Buddha.

`[22:49]` **SPEAKER_00:** I'm in, but I might not be the right person. I mean, I particularly like this idea that the idea that what are humans going to do, is a little bit invalid in that, you know, that's a little bit like going back five, 800 years and saying, like, oh my God, all of us are farmers. And then what are we going to do when modern agriculture comes? And it's like, we figured it out.

`[23:12]` **SPEAKER_02:** Or check the printing press, right? What are the monks going to do? They're transcribing words all day. There's no more jobs for transcription.

`[23:18]` **SPEAKER_00:** So there will be implications for society and morality and how people relate to one another. And obviously, like, we're seeing that right now. And we have no idea what that is.

`[23:26]` **SPEAKER_02:** So it's early days, but history does kind of repeat. And there's lessons there and figure out, OK, how does this? But the human nature doesn't change much, right? You can't satisfy humans. You're just going to want more stuff. The more money you have, the more, classically, right? Cliche, like, the more you have, the more you want. That's not going to go away. So if you give people a lot more stuff, it's not like, oh, I'm going to quit working. Most people aren't like that. I'm going to get a lot of stuff.

`[23:47]` **SPEAKER_02:** I'll just quit working. You find out you're miserable. You want to keep producing, keep contributing.

`[23:51]` **SPEAKER_00:** MARK MIRCHANDANI- One of the interesting things that has been percolating around the YC community among young founders, like AI researchers that we've been talking to, is this idea that, like, there are going to be humans in the loop. The humans in the loop may well be, some might be, like, government mandated, right? In fintech, there's a lot around, you cannot have an AI algorithm, like, approve loans, for instance. There are, like, requirements from the government in these highly regulated industries

`[24:18]` **SPEAKER_00:** to have humans in the loop. And then-

`[24:21]` **SPEAKER_02:** MARK MIRCHANDANI- Customs brokerage as well. We have to have a human that's approving the transaction before we clear customs.

`[24:25]` **SPEAKER_00:** MARK MIRCHANDANI- Yeah. Yeah. MARK MIRCHANDANI- And so vibe coding's happening. There's this idea of you enter a prompt, it comes back with a bunch of stuff, and then you just click Accept All Changes without reading any of it, right? Do you think this might happen? Would this happen at Flexport? Or would this happen more broadly across all businesses? Like, what if businesses are, at the core, like, hyper-intelligent AI that has access to all your systems of record, knows what to do, optimizes constantly?

`[24:56]` **SPEAKER_00:** And you have sort of, like, government-mandated liability sinks that are humans in the loop. Ideally, the organizations still actually serve human needs, in which case, like, the decision to use, you know, vendor A or vendor B sometimes boils down to who brought me to the nicest steakhouse last. So then, like, the model for companies ends up being ASI of some sort, like, some sort of AI process at the core of each company. But then, you know, humans attach to it as either, like, decision makers in, like,

`[25:26]` **SPEAKER_00:** you know, accepting or preventing liability and or holding relationships with other relationship holders at other companies.

`[25:34]` **SPEAKER_02:** Yeah, and presumably, you're still relating with— you're still here to serve humans, you know? Once we get to a world where AI is serving AI, then fair enough, you don't need to learn that much from the record of human history, because there's no more humans involved in the loop. And I don't have a lot to say about that. But as long as there's humans there, there's going to—humans are going to want to relate with other humans and have a relationship. And, like, I think we're pretty, pretty, pretty far

`[25:59]` **SPEAKER_02:** from humans preferring to work with AI than to work with other humans. We're seeing where AI is doing more and more work. You know, another good example is a— and just that made me think of with your bank, you know, you have to have an approver. Is that even in our humans and customs brokerage across the industry, we benchmark to make about 2% mistakes and they file the entry with 2%. And we built this sort of, like, AI system. Right. Right. And we built this sort of, like, AI system. spellchecker, the two-digit code for Australia versus Austria,

`[26:31]` **SPEAKER_02:** you could easily get that wrong. And the AI will figure out, oh, this thing is not made in Australia, it's made in Austria.

`[26:38]` **SPEAKER_01:** I guess one question for you, Ryan, is if you were to start Flexport today, how would the company be different?

`[26:44]` **SPEAKER_02:** Not that different, I hope. The things that Flexport did really well compared to all the other tech companies who have tried and failed in our space, both before we came along and in parallel, is we didn't look at ourselves as a pure technology company. We're willing to pick up the phone and solve problems with humans, drive down to the port. Still, to this day, we've got a new customer who's asking us to do something really weird. We need a crane on the truck to unload this thing. We don't have that.

`[27:13]` **SPEAKER_02:** It's not typical what we do. And I just said, take the customer, and I need you to drive there and follow the truck and make sure this goes well. So I would not change that at all. And I think that's the mistake that a lot of tech companies make. And I think that's the mistake people in traditional markets will fail at, because they're like, oh, if there's no API, I can't do it. If my agent is unable to do this task, I guess the task can't be done.

`[27:36]` **SPEAKER_01:** No tool use for cranes.

`[27:37]` **SPEAKER_02:** Yeah, and it might take you a long time, and you should not try to automate

`[27:41]` **SPEAKER_04:** that last tail of things. You started and grew Flexport, especially in the first few years, during an era where there's more money coming into it. There's more venture capital each year coming into startups, and you had multiple fundraising rounds. In what ways was that? Was that capital an advantage? And I feel like now it's somewhat back there in the AI world now. The rounds are heating up. There's more money flowing in. It just posts the 2022 crash. What's your advice to the founders now

`[28:07]` **SPEAKER_04:** who are in these companies that are growing and have options to raise huge funding rounds? How should they think about it?

`[28:13]` **SPEAKER_02:** Every company is super unique, so don't listen to advice on a podcast. Get someone who's paying attention, knows the details of your business, which no one will know better than you. Generally, capital is a beautiful thing, having it in your bank account gives you a lot of advantages. All you really need to care about at the end of the day is price per share. Because if you issue more stock, as long as your price per share goes up, you are richer. Doesn't matter what percent you own until it comes to control.

`[28:40]` **SPEAKER_02:** So there's two things that matter. Do you control your company legally or otherwise? Culturally, it also works. But do you really have control over the decisions that are getting made, and do you have a job and price per share? And that's all that matters. I still think that's true. That's always how I thought about it. There's been a lot of dilution to our investors, but the price per share went up, and everybody's made better off. I didn't take away anybody's shares, so you're better off.

`[29:01]` **SPEAKER_02:** The part that I underappreciated and that I now take very, very seriously is the degree to which money just wants to spend itself. And you will end up making a lot of mistakes where and the biggest mistake is believing, for sure, every company has a lot of problems. And you start to default to like, oh, we'll just use money to solve this problem. And the way that that manifests itself is, oh, I got this thing that we need to do. OK. Hire someone to do it. And you feel like you just end up very bloated.

`[29:28]` **SPEAKER_02:** We had too many people. You start to really slow down. And it's just a super bad cultural approach to problem solving. Like, you're going to solve the problems, not the new people that you're going to hire. So I give this advice. Only one founder's ever listened to me, but I tell founders who are friends of mine who raise a large round, and sure, go raise a big round. As long as you're up round, like you're doing good, great. Raise a large round, then do a hiring freeze for 90 days. The next day.

`[29:54]` **SPEAKER_02:** To tell your team culturally, like, no, the money's not going to solve our problems. We're going to solve our problems and keep that. And then, sure, go higher. Because it happened to us over and over again, where you just like headcount, got out of control. All the plans look good. I want to fund all the, we're doing budgeting for next year. And I'm like, god, it's so painful not to add OPEX, add engineers, whatever. But you've got to stay disciplined. And the money will easily make that stop.

`[30:21]` **SPEAKER_00:** So I'm really psyched to hear about this idea that AI is actually transforming your business in pretty fundamental ways. It's like coming bottom up. What does Flexport look like in 2035?

`[30:32]` **SPEAKER_02:** What a cool thing about Flexport is the way our vision has evolved. I mentioned we started as a customer broker. We do all end to end, all the way from factory floor to consumer stores. We have an e-commerce business that does fulfillment, retail store distribution, et cetera. So we want to take that globally to where you can really ship anything, anywhere, by any means, any mode, in any quantity, and do it all, be a, by any code, all available via APIs, or voice, or it's just easy to execute transactions at the lowest

`[31:00]` **SPEAKER_02:** cost, automate away the cost. And so that brands, companies of all kinds, don't spend time thinking about logistics. Logistics should be this utility that just works. Just like you don't spend time thinking about the electrical grid, you flip the light switch, you get power. You go back to doing your thing, which is making something people want and talking to users. That's what I think companies should do. Our customers should be doing that all day. Make great products. Make a great brand to sell those products.

`[31:25]` **SPEAKER_02:** And we'll take care of everything in between in the most automated, efficient, reliable ways possible on a global basis. So today, and we have a long ways to go to actually make all that true. First off, the automation stuff I talked about, making progress, but I got to keep going. And then the global aspect, so we have employee, we shipped cargo to and from 147 countries last year. But we only have employees in 22 countries. And therefore, people on the ground, they can do the work. Yes, we are automating that work.

`[31:56]` **SPEAKER_02:** And in fact, it's easier for us to automate our own employees work than it is some third party company that's doing work. Even though they're in our software, it's very hard to automate. We don't know what they're doing. So we want to be in every country by 2035, certainly. In fact, our roadmap has us covering 95% of all container trade with our own people doing all the work in the country in 2028. So by 2035, I think we could realistically say, look, we'll be everywhere that's legal. And that is a big extension of our original vision.

`[32:28]` **SPEAKER_02:** And I didn't have all that in mind when I did YC Demo Day. My pitch was like, we'll do customs, and then we'll add some other stuff. But it wasn't like, we will cover the Earth, any two plates on Earth, whatever you want to move, we'll move it. Yeah, it's a very ambitious goal. The good thing is, I really genuinely, we're going to win on tech. We're winning. We're going to extend our lead there relative to our peers, our competitors. We're behind them. On the global side, that's super fun.

`[32:56]` **SPEAKER_02:** If you told 25-year-old me, they're like, oh, Ryan, your job this year is we've got to launch Flexport in Indonesia, Australia, Japan, Philippines, Turkey, and Poland, and France. I'd be like, oh my, really? I get to go to all those places and talk to the locals and stuff? So it's a pretty fun moment in our history, but also really challenging, but fun kind of challenging, yeah.

`[33:19]` **SPEAKER_00:** No better kind. Ryan, thank you so much for joining us. Man, it's always a pleasure. All right, we'll see you guys next time.
