# 全文转录 · AI 创业公司的 FDE(前置部署工程师)实战手册

> ▶ [YouTube](https://www.youtube.com/watch?v=Zyw-YA0k3xo) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/Zyw-YA0k3xo.md) &nbsp;·&nbsp; The FDE Playbook for AI Startups with Bob McGrew
>
> 🗣️ 说话人分离识别到 **5** 位发言者(标注为 SPEAKER_00 …)。

`[00:00]` **SPEAKER_04:** With AI agents, there is no incumbent product. And so that I think is why you're seeing the FDE model taking off because there's so much product discovery to do. You want to drive the contract size up. You're doing more and more valuable work for this customer and also for future customers. The FDE model effectively is doing things that don't scale at scale.

`[00:29]` **SPEAKER_02:** Hello and welcome back to another episode of The Light Comb. Gary wasn't feeling great today and couldn't be here, but we're thrilled to be joined by Bob McGrew. Bob was an early engineer at PayPal, an early executive at Palantir, and was recently chief research officer at OpenAI, where he led the development of ChatGPT, GPT-4, and the O1 reasoning model. Now he's exploring the future of AI and has an exciting new role with the US Army that we'll get to in a bit.

`[00:54]` **SPEAKER_03:** Bob, thanks so much for being here. It's great to be here. So Bob, I've been particularly excited to sit down with you to talk about the forward deployed engineer model, because this is a topic that keeps coming up in our lives. It is a really hot topic in Silicon Valley right now, and especially among the AI agent companies that we've talked about on this podcast a lot. You were in the room when it all got started, and so you're exactly the right person to explain it. You were actually telling me a funny story. You were at an AI conference that YC organized a few

`[01:24]` **SPEAKER_03:** months ago, and you expected that all the founders would come up to you to talk to you about, you know, inventing ChatGPT. And instead, what all of these AI startup founders wanted to talk, was the Palantir forward deployed engineer model.

`[01:36]` **SPEAKER_04:** Well, and it's really true. It hasn't just been that one conference. As I've been advising startups this last year, I would say that a lot of them are pretty much exclusively trying to learn how the FD strategy works.

`[01:47]` **SPEAKER_03:** Yeah. So this is an intense topic of fascination, and it's super timely because it's actually become, I think, the dominant way that the AI agent startups are organizing themselves. I was looking earlier today, and if you look at the YC job board, there's over 100 YC startups that are hiring for a job with the title forward deployed engineer, and up from basically zero three years ago. Perhaps before we get really into it, for anybody who doesn't already understand, can you just explain what a forward deployed engineer is and how it's relevant today?

`[02:18]` **SPEAKER_04:** So a forward deployed engineer is someone, typically technical and engineer, who sits at the customer site and fills the gap between what the product does and what the customer needs. And how does this play out in practice? You'll have a product. And you go to a new customer site, you start working with a new customer, and the problem that they want you to solve is not a problem that you've ever solved before, but you believe that it's one that with a little bit of work, maybe a lot of work, you can solve for this particular customer, and you'd

`[02:51]` **SPEAKER_04:** be making a huge impact for them. You'd be delivering an outcome to them that would be extremely valuable for them. So you take the product that you have, and the FD with help from the product team figures out how to deliver that outcome, how to build that use case, how to deliver the piece of software that you've built in a way that actually works for the customer.

`[03:10]` **SPEAKER_03:** To go all the way back to the beginning, you were there at Palantir when this whole model that is now like exploding in Silicon Valley was invented. Can you talk about how it all got started?

`[03:19]` **SPEAKER_04:** The interesting way to think about the beginning of Palantir is that when we got started, the focus of our company was to build software for the intelligence community, specifically software for spies. And so one of the challenges in building software for spies. Is that I don't know any spies, you probably don't know any spies either. And if you happen to find a spy and you go and ask them, so what is it exactly that you do, they're not usually going to tell you. And so we had to take an approach that was sort of very unusual at the time, but effectively, we started by building a demo.

`[03:54]` **SPEAKER_04:** And we took that demo to potential customers in the intelligence community. And, you know, Stefan Cohen very famously did this. He was one of the founders of Palantir, and he showed them the demo and he said, you know, well, what do you what do you think? And they said, well, this is terrible. This isn't related to what we do at all. And he said, oh, well, how would you like it to be different? And then, you know, they would say, oh, well, could you make this change in this change? He's like sitting there writing all of this down.

`[04:19]` **SPEAKER_04:** So far, this story feels very much like you would the standard advice you would give to founders today, right? That you have to go, you have to make something that people want, you have to get out of the building, you have to go talk to customers. I think we were we were doing this back in the in, like, the mid 2000s. And so, you know, there's a little bit of that meme where, like, I spent years mastering this technique and Paul Graham just tweeted it out for everybody. But the thing that changes and that really causes the FD strategy is that what you expect and the standard thing that you expect is that you spend a lot of time early on, you know, doing things that don't scale, going out and visiting customers, getting very close to the customers.

`[04:58]` **SPEAKER_04:** And then you discover product market fit. And once you discover product market fit. You know, if you and this is class, you know, if we read Crossing the Chasm or any of these books, once you discover product market fit, you do something entirely different. So, you know, instead of going, you know, staying deep with the customers, doing as much as you can to really understand the customer, instead, you want to embrace distance from your customer and all you want to focus on is scaling.

`[05:19]` **SPEAKER_04:** How do you sell more? How do you treat all customers exactly the same? And, you know, I think I want to say that if you're in a business where this is working for you, that's great. Don't do the FD strategy. You have been given. An amazing gift. If you have the opportunity to just scale, treat all the customers the same, go ahead and do that. But it didn't work for us. And I think this is where Shamsankar, who's very early employee, you know, now I think the president and CTO of Palantir, he really invented the FD strategy.

`[05:49]` **SPEAKER_04:** And the the basic thing we found was that the customers that we had, the product that they needed was slightly different at every place. And so we moved from. One customer building a product for them. We went to the next customer. We saw they had something was slightly different. And instead of sort of building two products or building the exact right feature for each of them at each site, we built something that was more a platform than a product that had the lot a lot of ability to be customized at each site.

`[06:22]` **SPEAKER_04:** So when you do that, well, OK, you need to bring someone to the site to understand what the users are are doing and build customization. And historically, that's been understood as services. Right. So that's. you want to minimize you don't want to be doing a lot of work per customer in this you know product market fit and what sean realized was that you can actually flip this around and make it valuable so what he realized we needed was for the fdes to act as product discovery so they would go to the site

`[06:50]` **SPEAKER_04:** they would take the product as it was and they would fill the gap between what the product did and what the users needed so you know the fde goes and builds like a gravel road to where the product needs to go and then the role of my team of the the product engineering team was to look at that and basically figure out how that should generalize to the next five customers of the next 10 customers and then turn that you know gravel road into like a paved super highway i feel like

`[07:18]` **SPEAKER_02:** sales is product discovery is a concept that's not new certainly around before palantir but typically the view used to be like you had your sales people that went out and did like the sales and talked to the customers and they came back and reported to the engineers but it seems like a palantir was like the engineers were doing that work was that like a conscious decision or how did that come about especially when you're selling into like the government and defense like you would imagine

`[07:41]` **SPEAKER_02:** the natural inclination is to go hire some like experienced salesperson who's got a history of selling into the government and something like don draper like yeah yeah who wears a suit and

`[07:49]` **SPEAKER_03:** yeah worked in the d.o.d for 20 years and like takes generals out to steak dinners and things like that and that's actually not what you guys did right well i mean there's two angles this one

`[07:57]` **SPEAKER_04:** is uh we talked to a lot of those people early on and they said why the hell would i work with a company when i could work with you know a big five defense prime uh and then even when we talked to people who you know seemed like they might be successful in this role it was just very clear to us that they wouldn't mesh with our culture and they wouldn't actually be successful and when we tried doing something like this it almost never worked and so what we found was very different and and i think the difference between sales-led product discovery and fde-led product discovery

`[08:27]` **SPEAKER_04:** is that sales-led product discovery you're talking to people from the outside and again this is a little bit of a different perspective but it's not as effective as the fde-led product discovery where you're solving these problems from the inside so you know the scope of a of a traditional implementation might be you start with something that's pretty close to what the product does but you want to be solving one of the key problems that leadership has identified if you're not solving one of the top five priorities for the ceo it's probably not going

`[08:56]` **SPEAKER_04:** to work they probably won't have the energy to persist through the much more challenging route getting effectively a new piece of the product built in a way that worked for them then once you've solved that first problem then the fdes can you know identify other key problems in the enterprise sometimes much more valuable problems than the ones that you were first targeting that maybe it's not obvious that palantir could have solved those problems or that your company could solve those problems but once you're there you can see through product insight that you can actually

`[09:31]` **SPEAKER_04:** do this and then you go and solve those problems and so it switches from you know how do i sell the same thing to each customer to how do i land and expand bob can you lay out sort of exactly how the fdu

`[09:45]` **SPEAKER_03:** bottle works at palantir like if you were giving people almost like an an instruction manual like

`[09:49]` **SPEAKER_04:** like here's how we did it yeah so i think a starting point is to think about how the team was structured um and of course there's many different iterations but i think this is this is the the key thing that remains constant is that the key roles are those of what we call the echo team and the delta team the echo team were embedded analysts so they would go to the customer site they would speak to the users they would uh try to figure out what demo or what use case uh really made sense for the users at this site what was the

`[10:21]` **SPEAKER_04:** key problem that could be solved and they would also be the account managers so they would also be the people managing the relationships at the customer site and the delta team uh the deployed engineers were effectively software engineers typically very good at writing code extremely quickly eating a lot of pain as we put it and they would be the ones who sort of took those ideas and brought them into the real world and built a solution a prototype but something that could actually work and then deploy that uh for the customer and all of this would come in a very

`[11:00]` **SPEAKER_04:** short period of time so you know you You go in with an idea for what you're going to work on. You set up a few months in that you're going to have a presentation with leadership to show them your progress. And then if that presentation goes well, then you're going to actually deploy and go organization-wide.

`[11:20]` **SPEAKER_00:** LESLIE KENDRICK- The interesting thing about these two roles is very different kinds of people and profile. How would you even go about finding the right person to be in these roles? Because it's not just a regular engineer that could fit an FDE. They needed to have more of that talking to users. Or the echo team also had to be more technical. It wasn't just an account manager. How did Palantir build this early team?

`[11:43]` **SPEAKER_04:** BRIAN DORSEY- Yeah, so the echo team, a classic profile for someone to join your echo team would be someone from the domain you're working in. So possibly a former army officer or someone who worked deeply in health care. So they have deep domain knowledge. And this is really important. They need to be rebels. LESLIE KENDRICK- Mm. BRIAN DORSEY- Or Sean would probably call them heretics. They need to be someone who understands how things are done right now and recognizes that it's insufficient,

`[12:11]` **SPEAKER_04:** that it doesn't work. Because if their perspective is they come from this world, it's great, then they're never going to be able to figure out the step function change that the new software has to be able to make. Because if you can't make some sort of 3x or 10x change within that organization, then there was no reason, no reason to go through all the effort of doing this. You might as well have sold some sort of very simple piece of software. So that's the key profile for the echoes. And then for your deltas, you want someone

`[12:43]` **SPEAKER_04:** who's really good at prototyping. So the wrong profile for a delta would be someone who's a craftsman, who really loves making sure the abstractions are exactly right, that they're building software that's going to be maintainable for a dozen years, because that's not a role. That's not the job. And what you want is someone who can go in, figure out, write some rough and ready code. Sometimes that code is beautiful if you get the right person, but usually not. Again, that's not the key portion of the job.

`[13:13]` **SPEAKER_04:** But someone who can go actually deliver that outcome in the form of software on a timeline. And then it may be the case that the first version they write has to be thrown away. And maybe they write a complete second version. Maybe someone else writes a second version, depending on that person. But those are the key sets of skills.

`[13:31]` **SPEAKER_00:** CARRIE NORDLUND- It does sound a lot like a founding team.

`[13:34]` **SPEAKER_03:** MARK MANDELMANN, Yes. MARK BLYTH, JR.: It sounds a lot like a founder. Would you hire former startup founders and turn them into these roles? Or did it go mostly the other way? I mean, I think it's no coincidence that Palantir has spun off an incredible number of startups, because this FD training, this is exactly the training to become a startup founder. You're learning all the startup founder skills, right? But did it go in the other direction too? MARK BLYTH, JR.: Back in the day when

`[13:54]` **SPEAKER_04:** we were getting this started, there was not a huge supply of founders for us to pull from. I think maybe that's the opposite. What is it now? But I think you're actually quite right. What you're doing in each of these new environments at each of these customer sites is a little bit like being a startup founder. But you're a startup founder where you have access to some very powerful piece of product leverage that makes your job easier. This is, I think, great training. And like you said, this is why you see so many startups

`[14:23]` **SPEAKER_03:** from Palantir founders. CARRIE NORDLUND- So the common knock that you hear on this from people who don't really know what they're talking about is like, oh, it's just consulting dressed up with fancy, fancy marketing speak. Why is that wrong?

`[14:35]` **SPEAKER_04:** MARK BLYTH, JR.: I think before I say, I don't want to tell you glibly why that's wrong. Because I think there's actually a real risk that it's right. And I think if you go back to 2015 and you talk to people about Palantir, maybe you would hear two things. One, that Palantir is evil. But the second thing you hear is that it's a consulting business that is never going to scale, that it's actually like a bad business. It's not a software business. And we spent a lot of time trying to understand whether that was a correct,

`[15:01]` **SPEAKER_04:** accurate characterization or not. From a business model perspective, one of the key things that you will see, that you should see, is that it may be the case that when you go into, you do a new deployment at a customer, that you're actually losing money early on. The longer you're at the customer, first thing is your product, because of the product discovery, gets better suited to what the customer does. And so you no longer need a large team of people at the customer site figuring out what the customer is doing, paving, writing that code.

`[15:31]` **SPEAKER_04:** The second thing is that you should be earning the right, as Sean would put it, to have access to more important problems at the customer site. And so you should see, basically, that your cost per value of the outcome you're delivering is going down. And so your profit margins start off negative, but then ultimately become positive after some period of time, maybe a year, maybe multiple years, at the customer site. And if you look at it from that perspective, you can see that you're actually delivering real, repeatable,

`[16:01]` **SPEAKER_04:** value.

`[16:02]` **SPEAKER_00:** MELANIE WARRICK- I guess one fascinating piece to make this work and drive the cost down is really the product team. So how does the product team fit in and work with the FDE team?

`[16:13]` **SPEAKER_04:** JASON MAYES- I think on the engineering side, it feels my job as an engineer was actually not so bad, because early on, in the early days of Palantir, we were doing this founder-led discovery, and we were building new products. And later on, at the later days of Palantir, we were still doing that. We were still building new products. So it just felt great, right? But the roles that were really different are the FDE team, but then also the product management team. And so the product that you're building,

`[16:40]` **SPEAKER_04:** instead of being highly verticalized, and this is one flow that millions of people are going to be going through, like if you're building Airbnb, right? Instead, the role of the product team is really to hold the product vision. And so you have to think, when I see this new problem that we're seeing at a customer site, what is it? What is the generalizable version of this that applies to the next 10 customers? Because there's a classic failure mode here, where the FDE implements something for one customer.

`[17:14]` **SPEAKER_04:** And you say, great, well, that's how you should do it. And you bring it directly into the product. And it turns out, if you do that, you're building something that's over-specialized for one customer. And so the part of the magic here is being able to build the kind of product, and with the kind of product people, they can look at that, and sort of guess the correct problem that you're solving, which is always a little bit more general than the problem that the customer is coming in with.

`[17:40]` **SPEAKER_00:** LESLIE KENDRICK MASON- So there was some wisdom to figure out which bucket it fit. Is this just for this vertical, or it could be generalized? So could you give us an example of what that looked like in terms of the products and verticals, and what fit in one bucket versus the other one?

`[17:54]` **SPEAKER_04:** MARK MANDELMAN- Yeah, I mean, probably the most basic example here is sort of the invention of the Palantir ontology itself. And so when we first started talking about working with the US government and specifically working intelligence, should we have a database table for people, and a different database table for money, and a different database table for this? And it's super obvious, I think, at this point, if you go down that route and you try to deploy to multiple people, your database doesn't make any sense.

`[18:22]` **SPEAKER_04:** And so the change here would say, well, we need to pull this up to a higher level of generalization. And instead of thinking about specific types, of objects, we should allow that to be defined per customer by the forward-deployed engineering team. And so that's the sort of origin story of where Palantir famously got its ontology.

`[18:41]` **SPEAKER_03:** MARK BLYTH, JR.: So how does that work today? Is there a base database schema that has common reusable objects, like people and money, that then gets customized per site?

`[18:52]` **SPEAKER_04:** MARK BLYTH, JR.: Well, I mean, the database scheme is extremely general. There's just this notion of objects, properties, media, and links between objects. And here, I'm talking about Palantir's government. And I'm talking about Palantir as a product, which was our first product. But the ontology is what encodes all of the specialized information that's per customer. And that says, oh, well, this is a person. This is a ship. This is a money flow. And again, this is, I think, really the very most

`[19:19]` **SPEAKER_04:** basic example. But if you build something for just one customer, then you're going to be thinking in the description that applies to that customer. But instead of saying, OK, well, for Palantir, for people, we do this, you want to be able to pull it up a level and say, OK, well, there's this common operation that we want to apply to things that have this property, like people have this property, but maybe also ships have this property. But let's be honest, money, payments do not have this property.

`[19:48]` **SPEAKER_04:** And so you have to think at a higher level of abstraction. We didn't hire product managers for a long time. And when it did come time for me to hire product managers, I would interview people who were amazing product managers at other companies. And I would ask them to think at this level of abstraction. They couldn't really think at this level of abstraction. They would say, OK, well, this is the flow. This is what it should look like for this customer. But that was the wrong thing to do here.

`[20:13]` **SPEAKER_04:** And they needed to pop up a level and think at the level of, how does this work in the context of the ontology? How do we change the ontology so that this specialized thing works across customers? And of course, there's many other examples that don't have anything to do with the ontology.

`[20:27]` **SPEAKER_02:** MARK MANDELMANN I mean, did that create any sort of cultural tension at Palantir itself? I think you're describing the FTEs as sort of these heretics. They don't want to generalize. They want to do what's best for the customer and build specialized solutions. But presumably, for your own internal product team, you do actually want to hire the people who can think at some level of abstraction and want to build maintainable code that lasts for a while. Surely, that must have created tension somewhere

`[20:48]` **SPEAKER_02:** where there's an FTE who's like, no, I don't want to use the generalizable ontology. I want to do it this way.

`[20:54]` **SPEAKER_04:** MARK BLYTH Well, I mean, absolutely, there was always a lot of tension. And I would not frame this so much in terms of the skills that different people had. Because it was also very common. I think it's a lot about the environment, what people do in the environment they're placed in. It was also very common for FTEs to work in the field for a long time and then say, hey, I can really fix these products and then come in and do an amazing job on the product side and think at that level of abstraction.

`[21:17]` **SPEAKER_04:** But when you're at the customer site, you are faced with one very specific problem. MARK BLYTH Yeah, maybe the incentives are different. MARK BLYTH Yeah.

`[21:21]` **SPEAKER_02:** MARK BLYTH The classes and skills are different.

`[21:22]` **SPEAKER_04:** MARK BLYTH The incentives are different. And so you're solving one very particular problem. And it makes a lot of sense to just take the simplest approach to solve that problem. And that is, in fact, what the FTE should do. That's what the gravel road looks like. And then the paved road, though, has to go by not just this one customer, but a bunch of other customers that are further down the road. So the paved road often looks a little bit different. But the flip side of this, though, is imagine you said,

`[21:47]` **SPEAKER_04:** well, clearly this FTE approach is just wrong. The FTE is building the wrong thing. What if the product team just thinks really hard about what to build, and then they go build that? They're absolutely going to build the wrong thing. In fact, the way that we would often build features early on is that, first, the FTE team would build something. They'd see something at one customer. We'd bring it back to the product team in Palo Alto. And we'd say, OK, what's the right generalized version?

`[22:10]` **SPEAKER_04:** And those FTEs would participate in those discussions. That was incredibly important. And then we'd identify several other customers. Well, if it worked for this customer, we think it could work for this other customer. So let's bring the FTEs from those customers in as well and help them design. And they can help us design this feature so that when we build something, we know it'll work for the customer that was initially prototyped. And we know it will work for these others. And then, of course, once you've built that context where

`[22:40]` **SPEAKER_04:** everybody can see, here are three different workflows that are subtly different, then suddenly you're not having this argument about, well, we think it should be general, and we think it should be specific. But everybody is solving the same problem. And then I think that really melds the incentives.

`[22:53]` **SPEAKER_03:** MARK MANDELMANIS- Do you feel like it requires a lot of organizational discipline to keep this model from devolving into peer consulting, where the FTE team, which I think is the most important part of the process, is just off building whatever product the customer needs?

`[23:06]` **SPEAKER_04:** JASON MAYES- Yes. You absolutely have to focus on this. And I think one of the other failures, by the way, that's even prior to that and more the easier failure to become a consulting firm, it's where you build the product in the field that the customers are asking for, rather than the one that's actually valuable to them. Because it's often the case that the customer, right? You don't actually, the customer is like a whole organization. You talk to the customer, you talk to maybe the CIO, right?

`[23:33]` **SPEAKER_04:** Or you talk to one sponsor, usually a couple levels down from the CEO, who you only get to see every once in a while. And it's often the case that they would rather just have you solve some problem that's easy for them to have you solve, rather than one that's really impactful

`[23:48]` **SPEAKER_00:** and improves the business. MARK MANDELMANIS- Going back to the opening from Jared, what's going on with all these AI companies really now ramping up and hiring tons of FTEs? What has caused them to really adopt this model, which was not the case for the previous generation of companies with SaaS? What happened?

`[24:07]` **SPEAKER_02:** MARK MANDELMANIS- Especially because I feel like even as Palantir became successful and the FTE model became more known, it was still seen as, well, that's a one-off thing because Palantir is a unique company, and selling to the government is just like a- MARK MANDELMANIS- Government, yeah. Like a really weird thing. MARK MANDELMANIS- Yeah. But you wouldn't, don't try this at home.

`[24:22]` **SPEAKER_?:** MARK MANDELMANIS- Exactly.

`[24:23]` **SPEAKER_01:** Exactly.

`[24:24]` **SPEAKER_02:** Exactly. MARK MANDELMANIS- The mindset, right? Now everyone's sort of, like Diana said, it's become very commonplace. Has that, one, has that surprised you? And then two, why do you think that's happened?

`[24:33]` **SPEAKER_04:** MARK MANDELMANIS- This was absolutely a surprise to me, that my first, second, and third pieces of advice to people who are thinking about trying an FTE strategy is, don't do this at home. If you can avoid it, it's probably bad for you. Probably you're going to end up doing services. And then only if you really try hard not to do it and fail. Then, well, then maybe actually it's a moat for you if it's the only thing that can possibly work in your market. So what's special about this market, right?

`[24:57]` **SPEAKER_04:** Why does the AI agents market work this way? Maybe the starting place is, why did Palantir have to adopt this? The Palantir market is not one coherent market, right? So we were working with national intelligence agencies, with national law enforcement, with the military. All of these organizations had some similar projects, right? But even the difference between a counterproliferation workflow and a counterterrorism workflow, one, you're trying to figure out who's building bombs, and the other one, well, who's building nuclear bombs,

`[25:32]` **SPEAKER_04:** and who's building IEDs. And those are actually quite different in terms of how they work. And so there's this incredible heterogeneity. And the market, you should really think of the market as different segments. Inside each segment, you can build something. And the crossing the chasm story a little bit applies. So you're starting off, nothing seems to work. Suddenly, you find product market fit in the segment. You can deploy the people that are doing this kind of workflow. And then with the next customer, you

`[26:01]` **SPEAKER_04:** find the same people doing a similar workflow. And you can deploy with very little customization. But then there's a natural limit to that. And so now you want to go tackle a different market segment. And you have to develop a new piece of technology. And then that can be referenced in other market segments. And like I'm sort of saying here, a segment is not the same as a customer, necessarily, especially in an enterprise or a very large enterprise like the government, where a customer,

`[26:29]` **SPEAKER_04:** is tens of thousands of users, potentially. In that case, that's where the FD strategy matters. Because it's like you're doing things that don't scale, but you're doing it scalably over and over again for every market segment that you enter. Why do we see this with AI agents? I think the other thing that's unique about Palantir is that we were building a completely new type of product. The product that the users saw, well, they were used to basically, you know, tracking, doing their analysis and tracking people

`[27:01]` **SPEAKER_04:** in a tool that looked like PowerPoint. And they would collaborate by sending these files back and forth with each other. But the product we built was tied, basically said, hey, when you're, you know, drawing out that link diagram, you're not just editing a file. You're actually changing a database. And everybody has the same database. And so while to the user it looked like a small change on top of the work they were doing, to the enterprise, to the organization we were selling to, it was a completely different market category.

`[27:31]` **SPEAKER_04:** And that, I think, is what's happening with AI agents, where, you know, this is a completely new market category. If you are implementing, you know, a standard SaaS product and you're replacing one way of paying bills with a different way of paying bills, everybody understands what that market is. And so, you know, the segmentation, you know, there's not all this little segmentation. There's not a lot of, there's not the same kind of product discovery. You can then, you know, make a product

`[27:57]` **SPEAKER_04:** that's better than the incumbent product. And scale by replacing that product. With AI agents, there is no incumbent product. And so also I would say what it is to build AI agents is actually probably a lot of different things. And we don't know what those are yet. We've got to figure them out. Probably in five years, we'll look back, we'll be like, well, AI agents, there wasn't even a thing at all, right? We were actually doing all these different things. And so that I think is why you're seeing

`[28:24]` **SPEAKER_04:** the FDE model taking off, because there's so much product discovery to do. And you can only do it from inside the enterprise.

`[28:30]` **SPEAKER_02:** Okay, well, how does this relate to some of the classic YC advice, which is do things that don't scale?

`[28:36]` **SPEAKER_04:** Well, that's the advice that you give to an early stage founder. And the FDE model effectively is doing things

`[28:43]` **SPEAKER_01:** that don't scale at scale. YC's next batch is now taking applications. Got a startup in you? Apply at ycombinator.com slash apply. It's never too early, and filling out the app will level up your idea. Okay. Back to the video.

`[28:59]` **SPEAKER_03:** Since you see a lot of people trying to apply the FDE model now to their new startups, including a lot of people who didn't work at Palantir and are sort of doing it like second or third hand, what are ways you see people getting it wrong or misconceptions that you'd like to dispel?

`[29:13]` **SPEAKER_04:** Maybe I will start by saying, as I've advised a few different startups who are doing this, I think the startups, the most successful startups doing the FDE model have people from Palantir running the FDE model. The startups that I've talked to who are switching to the FDE model gained a lot of benefit by bringing on someone from Palantir in one of the core roles. As I said, the engineering team is often fairly similar, but maybe continues to be fun for a long time. But the actual mechanics of how the FDEs work,

`[29:43]` **SPEAKER_04:** how you build these accounts, how you find the outcomes, those are actually quite different from a standard software firm. And so one of the key differences, and something that I think is actually quite difficult for people to understand, is how you choose a problem and then how you price that problem. And fundamentally what you're selling with the FDE model is that you're not selling the installation of software, you're selling an outcome. As Sean would say, you're selling that you have solved a problem.

`[30:17]` **SPEAKER_04:** The next question then is if you've now solved a problem that is delivering some value to the users, how do you price that?

`[30:27]` **SPEAKER_00:** That's a very common question we get from all these AI startups because in the age of SaaS, you would do it based on usage or subscription or seats, and this is completely different as outcomes. How do you even price it? How should all these AI founders price their solution?

`[30:46]` **SPEAKER_04:** Yeah, and I think one of the really important things that is differentiated between the FDE model and your sort of standard SaaS model is that with the FDE model, with a SaaS model and product market, you're going towards very simple repeatable contracts, very simple repeatable pricing that makes sense across all of your customers. And often you're going to be quite comfortable with small contracts because the cost, the marginal cost to deploy is very low. With the FDE model, you're gonna get pushed towards larger and larger contracts.

`[31:17]` **SPEAKER_04:** Like we talked about, you're gonna be growing contracts per customer over time. The contracts, because they're complex, are gonna be more flexible.

`[31:25]` **SPEAKER_00:** I think this is what the AI startups that we work with discover on their own. I have this company called Castle that does AI voice agent for mortgage servicing. So they work with very large banks and the way they actually been able to go live with large banks is exactly that model of ramping up, is the number of successful calls that we're handling, all these mortgage requests. Then they had like stipulations when it goes to scale, it would be this much and that, and they kind of figure it out on their own

`[31:53]` **SPEAKER_00:** and other startups as well, like Happy Robot, that's another YC company as well, doing AI voice agents for logistics. They're working with large companies like DHL, similar thing.

`[32:03]` **SPEAKER_04:** There's an asymmetry here between you, the startup and the business that you're selling to, which is typically when you're selling to a large enterprise, they don't believe they can actually accomplish anything. And that's because oftentimes they've had many large projects that have failed. They also don't believe you can accomplish anything, right? Because they think that you, the startup are just like them. You on the other hand, know that you can actually execute. Yeah. You on the other hand, know that you can actually execute.

`[32:26]` **SPEAKER_04:** You on the other hand, know that you can actually execute. And if you can't, well, you should go into a different line of business anyway, right? And so early on, it makes sense for the startup to just take on all the risk and say, we're going to just believe in our own execution and we're going to take on the risk and you pay us if it works, or you pay us when we're actually able to expand. The one place this can go wrong is that, particularly if you're doing something that needs to be deployed into the enterprise,

`[32:57]` **SPEAKER_04:** on-premise or any piece of it needs to be on-premise rather than in the cloud, you do have to fight the IT team.

`[33:04]` **SPEAKER_00:** Yeah, I've actually seen that too.

`[33:06]` **SPEAKER_04:** Yeah.

`[33:06]` **SPEAKER_00:** With some of these companies.

`[33:07]` **SPEAKER_04:** And more generally, who needs to say yes inside the organization you're deploying into in order for you to succeed? Because those people do not think like startups. They are not aligned with the end user. And so you're going to have to figure out a way past them. And, you know, this is part of, part of why it matters that you're working on one of the CEO's top five problems. Because you need to be able to bring in someone from the top to say, yes, give them authority to operate. Give them, you know, the ability to use,

`[33:41]` **SPEAKER_04:** yes, you use this particular type of database. They need to use a different type of database. They, you know, you have all these very specific organizational things that are meant to apply to your IT staff who are building things in-house, but they don't apply to the startup. Let them do what they want. Let them do what they need to do.

`[33:58]` **SPEAKER_00:** How did Palantir get that executive buy-in? I think this is sort of what's happening with all these AI startups that are taking off and going from zero to seven, eight figures in revenue within a year. They figure out the executive buy-in, but it's all very haphazard, I would say, from all the stories I know of.

`[34:17]` **SPEAKER_04:** That's how it felt early on too. Okay. It's a discipline, it's a skill, you know, you need really amazing leadership on the FD team to be able to have that kind of discipline. And, you know, to share what works, you know, and just get the practice of doing it at one customer. I mean, I think it's not surprising. I think Palantir is extremely good at this now, probably better than any other company. And that's why, you know, the companies I've seen that have done this the best have sort of pulled that

`[34:45]` **SPEAKER_04:** from people who've done it before. But it can be learned. We learned it.

`[34:49]` **SPEAKER_02:** Jared pointed out earlier that the, I think this is the Palantir forward deployed engineer model is not that different to sort of like classic YC advice around doing things that don't scale. We have this concept of like the Collison install, which is essentially we boil it down to, don't wait for people to turn up to your website, like go to them and get them to like install the software.

`[35:07]` **SPEAKER_03:** And like physically go to them, like go to their office and like sit and text to them.

`[35:12]` **SPEAKER_02:** And I feel like it's always been a great starting strategy, but most startups aren't getting big contracts off the bat. So actually the reason they have to stop doing sort of like this sort of manual high touch process is, you just, you know, the process is you just can't get the growth rates to sustain without at some point having a product that scales. And it's kind of like what we were talking about earlier. Like at some point you hopefully, you build a product so good that people can figure out

`[35:36]` **SPEAKER_02:** themselves and then all of your problems are just scaling it. With AI what's different is because these contracts are so big now, you can actually go quite far by doing like the high touch thing. And maybe something you could help us out with actually is like probably a common office hour question I get is like, how far can I keep pushing this? And my advice is largely like, well, like it's okay to be doing custom work per customer. You just want to get less custom per every customer. Maybe you could give like more specific,

`[36:01]` **SPEAKER_02:** like higher resolution advice. Like how do you know if it's okay to like keep adding new customers in this sort of like high touch, like I'm doing lots of custom work way versus, oh no, actually I need to be like abstracting out and building like an actual product here.

`[36:16]` **SPEAKER_04:** Yeah. And I, and I think this, this is actually really encapsulates the key difference between, you know, the, the product market fit strategy and the FD strategy. In the product market fit strategy, you want to be doing less work for every customer. You want to be driving down costs. You want to keep the contract size the same. In the FD strategy, you want to drive the contract size up. So you're doing more and more valuable work for this customer and also for future customers. And because you're doing more valuable work, it's okay.

`[36:43]` **SPEAKER_04:** You can leave the amount of customization you do per customer the same.

`[36:47]` **SPEAKER_02:** So the KPI or the internal metric is like contract size, not necessarily like how much custom work they're doing per customer.

`[36:53]` **SPEAKER_04:** There's two useful things here. So one, the thing that you can measure, yes, contract size. I would even be a little bit more general than that and say the value of the outcome you're delivering, because that's, that's actually the true thing, you know, and do you yet have the muscle in order to be able to monetize that and price that and capture that? Maybe not. But if you're able to deliver more and more valuable outcomes to the customer, then, you know, you're, you're doing something right.

`[37:19]` **SPEAKER_04:** The second piece that we haven't, we didn't talk about yet is the value of the product. And so. The other thing you want to measure is, are you getting more and more product leverage against that outcome? This is all extremely counterintuitive when you're in it. It's very hard if you're an FTE or if you're leading an FTE team, there's a lot of things you have to do that, that seem very counterintuitive. You have to, you know, build for the customer things they're not asking for, but that they actually want.

`[37:46]` **SPEAKER_04:** On the product side, you often think to yourself, how do I make a product that's just really easy for every customer to use? It's very easy. And look, I struggled with this myself quite a bit leading product early on. Like you want to focus on on the user experience and you have to do that. But you also have to remember your other key customer is the FTE. Your product should be, you know, ultimately delivering a good thing to the user after FTE customization, but it should be delivering leverage

`[38:14]` **SPEAKER_04:** to the FTE who's delivering that outcome at the customer site. And that that amount of product leverage should be going up over time.

`[38:22]` **SPEAKER_02:** Like they should be able to use. Your product to deliver more value to the customer without them having to go and like pull in three more engineers in order to do it. That's right.

`[38:30]` **SPEAKER_04:** If you know, the first customer you deploy at takes a lot of work. If you want to then go sell that same outcome to a different customer, then that should be a lot easier at the second customer. And it should get easier still as you go customer by customer. But then if you if you really get it to work, remember that you're building a platform, so you're doing more than just, you know, a stack of vertical use cases on top of each other. If you've correctly abstracted away what the core concept is that you're really building,

`[38:59]` **SPEAKER_04:** then you should also have an easier time. You should have more product leverage even when you're not doing that use case, when you're doing something that's sort of similar. Or you will find that your FTEs, if it's a really if it's really good, you'll find your FTEs can figure out some new way to use that technique you built to solve something completely different.

`[39:16]` **SPEAKER_02:** There's always like an internal market dynamic going on where like if you've built it really well, then the FTE should like choose to use it and you should see demand from the FTE. So it's a really good way to use your sort of like abstracted product versus just like hacking a one off solution themselves.

`[39:29]` **SPEAKER_04:** Yes. Although I will just note, this is a very painful process for everyone involved. I probably can't use the word pain often enough in the FTE. You know, there are many times where I built something I thought it was amazing and I thought it was beautiful. Not not there yet. Right. But it would it really would help the FTEs as soon if they just had the the ability to see it. And I'd be like, please use my product. I'd be like, no, it's just this is way more work. It's like not helpful.

`[39:53]` **SPEAKER_04:** And then people say, let's be honest, most of the time I was probably wrong and I was building the wrong product for them. And, you know, I should see that. But sometimes also I was on the right track. But, you know, I hadn't done enough to make it easy for the FTEs to use. And so, you know, I would send, you know, the developers out into the field to deploy those early solutions and get them over the line, even to the point where the FTEs could use them profitably.

`[40:16]` **SPEAKER_02:** Are the FTEs always right in that case? Or should the founders sometimes be just top down and say, like, actually, I just want you to do that, do it this way?

`[40:24]` **SPEAKER_04:** I mean, the answer is like, yes, to all all of these things. The other thing that comes up over and over again is just how much the right answer here is a matter of judgment. And I think I think going back to this question about product vision, right? Like, what is the right product that generalizes from, you know, this customer to the next three to the next ten? You you very literally do not have the the information needed to answer that when you see that first customer. And so it's just it becomes a judgment call.

`[40:52]` **SPEAKER_00:** So in the context of. How all these FTE companies price very differently based on outcome. How does that fit in with now the culture doing demos? Because there's this this thing and at least in SaaS or I used to get this pushback from my engineers, demo driven product development, it would be sort of looked down upon. But in this case, it's different for FTEs, right?

`[41:14]` **SPEAKER_04:** One of the interesting things that happens there is because you have to go repeatedly show this to new customers, you're forced to give these new demos. But but actually, I think demo driven development works really well. If you have the right kind of product. So, you know, in the early days of Palantir, we actually had one demo. It was a flow where you're, you know, stopping a terrorist plot. And we started this with, you know, just one of our features. And every time we integrated a new feature, we had to think to ourselves,

`[41:39]` **SPEAKER_04:** how do I show that this new feature is actually helpful for the analyst who's going through this demo, who's stopping this plot? You know, when we integrated a histogram, we had to say, well, how do we actually use this? How does that work with the existing? Features that we already had? And we went this, you know, we integrated a map and we had the same question. And if you think about the world from what am I building, then, you know, you're thinking about your capabilities. You might think of each of these features individually

`[42:06]` **SPEAKER_04:** and how to build the best version of these features. But when you're building a demo, you're thinking about it from the customer's perspective. And a really good demo is something where you show it to the customer and you are creating desire in that customer for what you're doing. They have to see what you're doing. And just want to reach out and grab it and bring it into their life. And if you see that, then you know that you've identified a real pain for the customer. And by doing that, that also forces you to develop a better product,

`[42:35]` **SPEAKER_04:** because not only are you thinking, OK, do each of these features make sense in isolation, but how do they work together? If I'm going to be showing this demo over and over again, even just simple things like moving from one feature to another, that part of the path has to be very straightforward. And those are those are all the kinds of product pain points that you would want to have. And that's something that you would often see, but only later after you've actually deployed to the customer.

`[42:59]` **SPEAKER_04:** So what the demo does is it is it changes the locus of what you're thinking about from thinking about what can I build to what is it that the customer wants? And am I am I solving that pain point for the customer?

`[43:11]` **SPEAKER_00:** So it sounds like it's sort of this you have to keep doing the gradient ascent in this very, very highly dimensional, multidimensional space. And you keep changing the variables.

`[43:21]` **SPEAKER_04:** Yeah, yeah, I think. Yeah. Maybe. I think that's a really key point here is that the kind of company you have to build is a learning company. And I think everybody wants to build a learning company. But if you're a company like Google or Meta, it's very easy not to learn because what you're doing right now is working. And if you just keep doing it, the market is growing. You know, everybody wants to do what you're doing. You can you can just sort of keep coasting on the same strategy and it's paying off for you.

`[43:50]` **SPEAKER_04:** My advice to people, if they're thinking about where to join a company, is I tell them to join a company. Not necessarily a small company, right, but a young company, because a young company is still figuring things out. It's still learning. It hasn't succeeded yet. You know, if you're just out of college, you want a young company that is growing really fast and then you'll be you'll see what success looks like. That positions you exactly to be a founder of your own company later. This is why Palantir has birthed so many other startups is because even as a very large company, it is still a company where everybody all the time is learning, focused on learning.

`[44:22]` **SPEAKER_04:** And. You know, always doing that same grinding motion that it is to be a new startup, because, you know, yes, you know, new startups, a lot of pain there, too, right? That is like probably like the canonical part of the YC experience is that it's not coasting. It's working really, really hard on something that you're not quite sure if it's going to succeed.

`[44:42]` **SPEAKER_02:** Obviously, I mean, a monster success for Palantir. They're now a super big company, huge organization. We heard that you're joining another large organization, the U.S. Army Reserve. Maybe you could tell us a bit about that. And are there any lessons from the Palantir experience you're planning to apply there?

`[44:56]` **SPEAKER_04:** Yeah, absolutely. I've recently joined the U.S. Army Reserve as part of Detachment 201. And so, you know, one thing just to get out of the way is to say that what everything I'm talking about here, these are my opinions. These are not the opinions of the U.S. Army, the Defense Department, the U.S. Government. But I think it's this it's been this absolutely intense experience and it's a really interesting story. So we are part of a unit that's advising the Army on technology. And we are not just civilian advisors.

`[45:24]` **SPEAKER_04:** We are actual officers. So, you know, we took the oath. I'm a lieutenant colonel in the U.S. Army.

`[45:31]` **SPEAKER_03:** I heard you went through basic training, too.

`[45:33]` **SPEAKER_04:** I yeah, we went through the direct commissioning course. We've been trained by military academics often at five in the morning because that's the time that works for people on the East Coast and doesn't conflict with our day jobs. We learn from officers. I had to take the Army fitness test, which since I am not very fit, you know, it was something that I had to do. But. Something that I had to train for for nine months, but it really matters because we're not just giving advice on the side.

`[45:59]` **SPEAKER_04:** We have skin in the game. We are actually part of the organization that we're advising and the Army itself. The leadership is very different from what it felt like in the early days of Palantir when we were working them back in 2005 or 2010. General Randy George, the chief of staff of the Army, secretary of the Army Driscoll, they have articulated a plan for the transformation. Of the Army. They know that the Army needs to change from, you know, the kind of from finding the kinds of wars we fought in Iraq and Afghanistan to fighting the kind of wars that are being fought today in Ukraine or what it would look like if we face large scale combat operations in the Pacific.

`[46:37]` **SPEAKER_04:** They know the Army needs to move faster. They know the Army needs to change. And we are a part of that strategy that they're executing as they brought us in. They you know, they have given us they've outlined the priorities for the Army. They've given us each an area in which we're supposed to operate. But they've also given us the freedom to, you know, go around, look for problems, work directly with the officers on the ground to solve those problems, or if need be, to escalate that to leadership and get that fixed.

`[47:03]` **SPEAKER_04:** And so I think one of the things that's that's really interesting about it is, you know, in many ways, it does feel a lot like running the FDA strategy, you know, on the Army. We we get to see, you know, what is that? What are the CEOs? What are the leadership's top five priorities? Can we make progress against those? But also in a world where you see that there's a disconnect. There's a disconnect between what the leadership wants and 20 years of how things have been implemented, and it takes a long time to change that.

`[47:30]` **SPEAKER_04:** And so, you know, we're helping them make that change. I'm really eager to have the opportunity to make a difference.

`[47:36]` **SPEAKER_03:** There's a question that we love to ask people on on this podcast, which is what do you think are the best opportunities for startup founders to work on right now?

`[47:43]` **SPEAKER_04:** Well, you know, I think this really goes back to exactly this question of why is it that agents are pursuing the FDA strategy? And, you know, if you if you zoom out and I put on my research hat for once in this podcast, I think what we've seen is that that capability improvements are actually extremely fast. If you you know, yes, I heard people, you know, after GPT-5, people feel like things are plateauing. But actually, if you look at this time period between April 2024, when the best model, you know, the release of GPT-4.0 and April 2025 and the release of O3, that's an extremely

`[48:21]` **SPEAKER_04:** fast. Rate of progress. And I think that's just going to continue. I think we're going to see capabilities continue to move quickly. But what's what's really shocking, actually, is that the adoption is not anywhere near what you would expect from the speed of these capabilities. What the world is going to look like over the next five years is that the capabilities just race ahead and race ahead and race ahead. And somehow the world feels increasingly banal. You know, you're like you're in your Waymo and you aren't thinking, oh, my God, it's not you know, no one's driving this.

`[48:50]` **SPEAKER_04:** You're like, oh, traffic.

`[48:52]` **SPEAKER_02:** It's really slow. Yeah.

`[48:53]` **SPEAKER_04:** And so, you know, just like with the world of the FDEs where you have, you know, the FDEs filling the gap between this product and what the customers need. I think, you know, this is a time where there's so much availability to fill the gap between what the capabilities can actually do and what the customers are able to adopt. And in the early days of AI, we sat around a table in 2018 and talked about what it looked like when AGI was built. People thought, oh, well. You know, it's going to it's going to maybe maybe over the weekend it's going to come alive and it's going to take over the world.

`[49:28]` **SPEAKER_04:** And, you know, one of the things that I think people missed in that was that, you know, AI needs to be adopted. It's something that doesn't just happen by itself, but you need human ingenuity and exploration and while dealing with a lot of pain in order to make that happen. And so I think there's just a huge amount of opportunity out there looking at. What are the capabilities that are there? But what does it take to make them really genuinely useful to people?

`[49:57]` **SPEAKER_03:** There's an analogy that occurs to me. This might be a little bit forced, but it's almost like open AI is the home product team and the startups are the FDEs out figuring out how to get adoption of of of the like research that open AI is cooking up back at the home office.

`[50:12]` **SPEAKER_04:** I think that's not a bad analogy at all. I think that I think that is that is maybe the underlying truth of what's making this whole FTE strategy exciting. Exactly.

`[50:22]` **SPEAKER_02:** Okay, that's all we have time for here today, Bob. Thanks so much for joining us. That was really, really interesting. We all learned a lot and we'll see you all here next time.
