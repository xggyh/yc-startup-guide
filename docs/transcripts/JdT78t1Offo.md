# 全文转录 · Anthropic 联创谈 Claude Code、GPT-3 与 AI 系统设计

> ▶ [YouTube](https://www.youtube.com/watch?v=JdT78t1Offo) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/JdT78t1Offo.md) &nbsp;·&nbsp; Anthropic Co-founder: Building Claude Code, Lessons From GPT-3 & LLM System Design
>
> 🗣️ 说话人分离识别到 **5** 位发言者(标注为 SPEAKER_00 …)。

`[00:00]` **SPEAKER_04:** When we started out we didn't seem like we were gonna be successful at all. OpenAI had a billion dollars and like all of these all of the star power and we had seven co-founders in COVID like trying to build something and we didn't know if we were necessarily gonna make a product or what the products would look like. One thing that's interesting to look at is just that humanity is on track for like the largest infrastructure build out of all time. Tell us about the early

`[00:25]` **SPEAKER_03:** days of Anthropic. So you had a general idea of this sort of like long-term mission that you wanted to do to you know not destroy humanity but like what did you actually work on for the first year? How did that converge on an actual product? Welcome back to another episode of The Light Cone.

`[00:48]` **SPEAKER_01:** Today we've got a real treat co-founder of Anthropic Tom Brown. Excited to be here. So Tom one of the things that a lot of the people watching would love to figure out is you got started in tech at the age of 21. Fresh from MIT. How does someone go from that in 2009 to literally co-founding something as important as Anthropic?

`[01:12]` **SPEAKER_04:** Summer 2009. Linked language. Two of my friends had started that out. I think they had seen one of our other friends Kyle Boat kind of do a YC company and so it was in the water. That's a thing that we could try to do. They started out. I was the first employee. Back then yeah you guys let me join for all the dinners and stuff like that too. I could have instead gone to like a big tech company or something like that and I think probably just as a software engineer I might have learned more software engineering skills but I think by being there with the

`[01:43]` **SPEAKER_04:** other co-founders without anyone telling us what to do basically we like we had to figure out how to live how to like the company would die by default. I think in school there was a lot of like a feeling of more of people would give me tasks and I would do the tasks it's kind of like a dog waiting for like food to be like fed to them in their bowl or something like that and I think it was more like wolves and we have to like hunt our real life food otherwise like where our kids are gonna starve or something like that. I think that that mindset I think has been like the most

`[02:11]` **SPEAKER_04:** valuable mindset that shift that I've had for trying to do like bigger more exciting things.

`[02:17]` **SPEAKER_01:** Yeah big tech just teaches you to work at a big tech company whereas it's much more fun to be a

`[02:24]` **SPEAKER_02:** wolf. Yeah. How did you go from like so working at friend startup to then you started your own one?

`[02:31]` **SPEAKER_04:** We ran the company for a bit I ended up going back to school afterwards and then when I left school I went to this company Mopop. That mobile advertising thing right? Yeah yeah I was like the first engineer there I was like okay I want to be a wolf but like I was really bad at programming also I was like very very struggling as like a like software engineer. I know I want to do more but I don't know how to do it yet and so I think that was kind of like experience getting to scale and then we started our first company and then we started the last company and then we started

`[03:06]` **SPEAKER_04:** another one that we started with a friend of mine who was my smartest friend from college pitched me on let's go and start a YC company. We did at the time solid stage this was before docker existed and so the idea was try to make it easier to do DevOps but docker doesn't exist so it's going to be a more flexible Heroku which basically meant a more complicated like Heroku and so we I remember

`[03:28]` **SPEAKER_01:** we like we interviewed with you guys. I think folks didn't really understand what we were trying to do at the time. I think it's actually sometimes common. Yeah I think we were an outlier there

`[03:35]` **SPEAKER_04:** because we like did our interviews and then we got called back driving back to San Francisco and TLB had written on the board like an angry frowny face and what are you actually going to build and so he like wanted us to explain that. I guess we explained it enough or he was just like these guys still don't know what they're doing but maybe they'll figure it out. Halfway through I kind of felt I still didn't actually understand what we were going to build and how we would attach a mission to it that like I wanted to to work on for my whole life. Yeah and so I left PG actually

`[04:07]` **SPEAKER_04:** introed me to Michael Waxman who was the founder. Yeah so the grouper was a dating app only it was

`[04:15]` **SPEAKER_01:** novel in that you had what three guys and three girls. Yeah this was before AI in a lot of ways so there was like a set of a team of people who would manually link people up right yeah and then they'd meet up at a bar and yeah shenanigans would ensue. Yes

`[04:31]` **SPEAKER_04:** shenanigans people didn't always have a great time, I think you want you on a couple. For me for like why I was excited for it was just I was like an incredibly awkward kidding what I wanted to do was to basically have a thing that lets awkward people like me go out and talk to other people. For me to talk to girls and feel like I was safe doing it with like my friends around and stuff like that. And so I think who are going to be our employees was important. I did a all of our engineering interviews we would take someone the only person who went on more was greg

`[05:05]` **SPEAKER_04:** brockman i think yeah i think he had he had a phase where like every single week he would go and like post on uh slack or hip chat because he moved to new york and he was hanging out the recurse center during this period i think oh i i think he was at stripe maybe maybe for part of it he was at recurse yeah but he also had uh i think just like a phase where he would just at stripe he would just like post in their thing every like i'm going on a grouper who's going for like a whole year so i i ended up being close with greg which which ended up being a connection to the

`[05:35]` **SPEAKER_00:** open air what was the journey like because you started as uh you just graduated from mit cs you were 21 you became first an early employee for all these yc startups then you started your company just a couple years later and what was the path for you to eventually become the co-founder of anthropic it was like a long path but it's pretty impressive how did you get there i mean it sounds

`[05:59]` **SPEAKER_01:** like getting into the business and then you're like oh my god i'm gonna be like oh my god i'm gonna be like oh my god i'm gonna be like oh my god i'm gonna be like oh my god i'm gonna be like oh in touch with greg at that moment some serendipity moment uh and then you were one of the first uh

`[06:05]` **SPEAKER_04:** you know a couple dozen people to join open ai as a result yeah so i left grouper 2014 june 2014 and i joined open ai i think a year later i tried to like build up courage to make the switch to be a to try to learn ai research at the time i was like okay it seems like sometime in our lifetimes we might end up making transformative ai if we do that would be the biggest thing maybe there's some way that i could help out but also i got like a b minus in linear algebra in college and so it seemed like at the time you

`[06:41]` **SPEAKER_04:** needed to be just top superstar in order to try to help out with that at all and so i think i had like a lot of uncertainty about whether i would be able to help and also i'd had some success with startups and so a lot of me was just like rather than trying to retool at this like i could try to

`[06:55]` **SPEAKER_02:** do another startup or something like that i feel like in that period um going to work on ai research which is not seen as like a serious like not like a practically serious thing to do yeah and you're in a world where it's like people try and build companies and these like really practical things like what did your were your friends like oh that's really cool you're gonna work on ai stuff

`[07:12]` **SPEAKER_04:** or was it not really i think my friends were like that sounds that sounds weird and bad kind of like it doesn't really seem like it doesn't seem like like ai safety is i think we should be weird like overpopulation on mars doesn't make any sense and my friends were also just like i don't know if you're going to be good at that tom i think that for that reason i think i didn't try very hard for i like kind of flip-flopped on it for like six months trying to build up courage to

`[07:35]` **SPEAKER_02:** do it and what were you specifically at this point like you're reading research papers like what it

`[07:40]` **SPEAKER_04:** what does it look like yeah so first i was just kind of hanging out i built like an art car for titanic zen and stuff like that oh that was fun yeah yeah yeah so i spent like a whole summer like three months after grouper doing that because honestly i was i was like kind of burned out for grouper where i know startups like the highs are high like the lows are low and we weren't working at the end our business was kind of like you know like we were like you know like we were like we were like we were like we were like we were like we were like we were like we were like

`[08:00]` **SPEAKER_04:** wasn't succeeding our revenue was going down but i my main job still was like recruiting engineers and so i had to like pitch them on the stream that i'd had but i like no longer really sounds like a death march yeah and so i was super burnt out and i was like okay tom like chill out do some yoga

`[08:14]` **SPEAKER_01:** like do some crossfit like build an art car what was the hindsight like you know hindsight's 2020 what's the retrospective on like grouper obviously attracted all these really really smart people the graphs were up and to the right and then it flatlined and maybe started declining what happened

`[08:30]` **SPEAKER_04:** i think that when we started the competition was like okay cupid it was all web-based all web-based the main problem that i think we were solving was the it's hard to like go and put yourself out there and go like talk to someone new and they might just be like i don't want to talk to you you seem weird and so we solved that by just blind matching tinder came out while we were doing grouper and tinder solved that same problem with both people have to show interest before you get matched so there's also no worries about getting rejected and i think

`[09:00]` **SPEAKER_04:** that they just had better that was a better solution to that same problem so good work tinder good work all the swipers i think that that that solved the like mission that we were trying to solve better than we solved it and then yeah like when did you get serious about ai and just how did you approach it three months of like kind of playing and having fun and then i ran out of money also when i had like my personal runway i i ran out and so i was like okay i think that i'm going to need six months of stealth study to have a shot at getting like a good deal of money and you know

`[09:30]` **SPEAKER_04:** a job at that point it was deep mind or Google brain were the two places to do work there or Miri Miri was the third one that I was looking at so I was like if I want to help out with that those are the three places to look at I don't have any of the skills yet I need six months of self-study to feel like I would not be a drag on them and like actually be helping instead can you

`[09:50]` **SPEAKER_00:** maybe explain a bit what was a self-study like because I'm sure there's a lot of software engineers right now in their 20s are looking to a tool to become AI researchers what was what was that six months like even though as you said you had a gotten a B minus in linear algebra just like core might have

`[10:06]` **SPEAKER_04:** been a C plus impressive where you got to yeah yeah it turned out okay first I did a contract actually with twitch and like earned like enough to have that six months of runway so I did like three month contract with twitch and then I made a plan to self-study I don't think it's the right plan now for people to get at least the 2015 what did it look like it was like take a Coursera course on machine learning try to solve some Kaggle projects read linear algebra done right and I had a statistics textbook I

`[10:40]` **SPEAKER_04:** think I had YC alumni credits and so I bought like a GPU and I would like SSH into the GPU to like work through my courses for it and this is right after

`[10:51]` **SPEAKER_00:** yeah it was already after I like snack right it was after Alex night yeah so I

`[10:55]` **SPEAKER_04:** was mostly doing image image classification and stuff that I was trying to learn was like the thing that all the courses

`[11:01]` **SPEAKER_00:** would teach you to do how did you get the open AI job because you were one of the few engineers it was mostly researchers and they had a pretty stacked

`[11:09]` **SPEAKER_04:** team of researchers I messaged Greg as soon as open air was announced and I was like I'd love to help out in some way I got to be minus in my linear algebra but I know some engineering I've done a bit of distributed systems work if you guys need help I'm like happy to mop floors if if you guys need I want to help out however and I think Greg was like yeah I think there's like a paucity of people who he said paucity to it I was like fancy word there there's a paucity of people who know both machine learning

`[11:37]` **SPEAKER_04:** and distributed systems so like yes you should do that I think he introduced me to Peter Abiel also to help me put together like a little course for myself too and then I checked in on with him I think every month or something and then after a couple months he was like oh we actually have a project which is uh we need to put together we want to play a gay like play games can you help uh make Starcraft environment and so I joined to like help them with the Starcraft uh environment so

`[12:04]` **SPEAKER_04:** that that ended up I think getting my foot in the door I I didn't do any machine learning work with

`[12:08]` **SPEAKER_02:** them for the first nine months that I was there basically and what did opening I feel like at this point like had it raised much funding did it have like an office is what would it do you feel

`[12:18]` **SPEAKER_04:** like a startup so it was in the chocolate on top of the dandelion chocolate factory um this is after Greg's apartment that's the after Greg's apart yeah so like right after Greg's apartment in the factory when it kicked off right it was like a billion dollars of committed funding from Elon it

`[12:32]` **SPEAKER_00:** felt like it was like very solid the other interesting milestone for you was when you got to build a lot of the engineering around the training for GPT yeah for GPT3 for and how what was that because you got from GPT2 was in tpus right yep and the big breakthrough in GPT3 was

`[12:53]` **SPEAKER_04:** like use more compute and using GPUs yeah so I ended up working at openai for a year left went to Google brain for a year came back and then GPT3 was 2018 through 2019 was like building up to GPT3 which exactly as you said was like scaling things up I think that like Dario had seen the big trend of scaling laws basically you published a paper for that yeah yeah and that's

`[13:16]` **SPEAKER_00:** like a pretty important paper that now has withstood the test of time and we're living now

`[13:22]` **SPEAKER_04:** the dream of it definitely like seeing that line of reliably you get more intelligence if you spend money was the main thing that was at least for me it was like this is a thing that's like happening happening now because you could look even at the time we weren't spending very much money on the on the training jobs at the time and you could see that there was scaling there and then also Danny Hernandez did a paper at the time that showed how much cheaper algorithmic efficiency was making stuff over time too and like those two things stack together that was like oh wow

`[13:53]` **SPEAKER_04:** we're gonna get a lot more Intelligence over the next few years so it was noteworthy and

`[13:57]` **SPEAKER_01:** surprising

`[13:58]` **SPEAKER_04:** surprising when you saw it yeah and I think the thing that seemed the weirdest to me is like I'm not a physicist but like all these physicists were doing this stuff the like original scaling laws paper just the like very straight line over like 12 orders of magnitude I'm just like 12 orders of magnitude is like just like a stupidly large amount of I've like never seen anything go over 12 orders of magnitude that convinced me to definitely pivot all of my work into scaling

`[14:23]` **SPEAKER_01:** which I hadn't been doing before can I asked a like kind of layperson question I mean is it fair to say that the scaling law might show up in all of these other domains then they're like are there like two five a hundred ten thousand domains where the scaling law could hold that we're just

`[14:40]` **SPEAKER_04:** not investing into yeah so I think in physics scaling laws hold all over the place which I didn't know at the time but within physics like there's a whole field called phenomenology that basically looks at various aspects of the world and then does those types of fits and they they find these like power law distributions all over the all over the place this was like I think the first one that I had ever seen in a um like computer science adjacent thing which I think was like interesting and surprising and

`[15:11]` **SPEAKER_01:** and at the time it was people were mad about it they actually were like you're throwing money at gpus or just like wasting money this is very wasteful yeah that was sort of people yes different people now but still people mad about it yeah yeah I guess yeah the researchers were

`[15:28]` **SPEAKER_04:** mad at that too where it's like it's it's not elegant you're just like brute forcing it the like jester cap like stack more layers like which I think I think like anthropic's slogan I think is like do the stupid thing that works that was a thing where like this was very clearly the very

`[15:42]` **SPEAKER_00:** stupid thing that that works can you uh tell us then how you ended up collecting the last Infinity Stone with the topic yeah with anthropic because there's very few people in the world that basically worked at openai DeepMind and anthropic and you were part of the team that spun off from gpt3 yep and then started anthropic so how was how was that jump there were two teams there that was

`[16:05]` **SPEAKER_04:** the safety org and the scaling org were the two orgs that reported into Dario and daniella I think we had just like worked together extremely well one thing I think that was great both at openai and and at anthropic was just like we had a culture where like everything is on slack 100 percent of things on slack and within that all public channels great communication I think that that group also was the group that took the scaling laws the most seriously where it was like okay like this actually is going to be transformative there's going to be a handoff

`[16:37]` **SPEAKER_04:** where like humanity will hand off control to transformative AI at some point and hopefully like they'll be aligned with us and like that'll be a good transition that goes well but it might not be the stakes are incredibly high and so I think that group was very focused on like how do we ensure that that's taken seriously enough and that like we've built an institution that can handle the weight of that that ended up being the core group that left to join anthropic and I think I think it wasn't clear at all to me that like that was the right thing for the world at the time in

`[17:08]` **SPEAKER_04:** hindsight now it seems like that was a good choice I think what was kind of cool then too is when we started out we didn't seem like we were gonna be successful at all openai had a billion dollars and like all of these all of the star power and we had seven co-founders in covid like trying to build something and we didn't know if we were necessarily going to make a product or what the products would look like and so I think that what was interesting from that too is that all of the initial people who joined were there for the

`[17:37]` **SPEAKER_04:** mission too they all could have worked somewhere else for more prestige more more more money people would have known what they were doing Etc well stayed at opening high exactly yeah that exactly that's been an interesting thing then that I think has been like the key to like letting our culture or like let our org scale we're like 2 000 people now but we still have a thing where it doesn't seem like politics have creeped in and I think a lot of that is like the first hundred people all

`[18:02]` **SPEAKER_04:** were just there for the mission so like if something starts to go wrong they'll like raise their hand and be like it seems like this person might not be acting for the for the mission YC's

`[18:10]` **SPEAKER_01:** next batch is now taking applications got a startup in you apply at ycombinator.com slash apply it's never too early and filling out the app will level up your idea okay back to the video

`[18:23]` **SPEAKER_03:** maybe tell us about the early days of Anthropic so the the seven of you broke off from open AI you had a general idea of this sort of like long-term mission that you wanted to do to you know not destroy humanity but like how did what did you actually work on for the first year how did that

`[18:41]` **SPEAKER_04:** convert on an actual product so first year the main thing that I tried to do was just build the training infrastructure that we needed to train a model and then get the compute that we needed to train the model those were like my two main projects all the other things that you need to do when you're like starting up a company too so like set up a brex account and like I don't know like all of that all of that stuff we started out with seven co-founders within like a few months I think like 25 folks from open AI overall had joined so

`[19:11]` **SPEAKER_04:** we had like a pretty substantial team that like already knew how to work together too and so that helped us get up and running faster and at what point did you launch the first product and when

`[19:20]` **SPEAKER_03:** did things begin to actually start working so

`[19:23]` **SPEAKER_04:** the first product that we launched was after chat GPT we had like a maybe nine months before chat GPT

`[19:30]` **SPEAKER_01:** we had a slackbot version of like Claude one oh yeah we had that in the YC uh yeah I remember like

`[19:39]` **SPEAKER_04:** Tom Blomfield adding all of you guys to it and then I think that at the time though we didn't know whether or not we wanted to launch it as a product we didn't know if doing so would be good for the world at the time I think we hadn't really thought through our theory of impact that much for like how we actually will make stuff work well plus I think actually in hindsight like if we tried to launch it we like wouldn't have had the serving infrastructure to have done it and I think because we weren't sure whether or not we

`[20:06]` **SPEAKER_04:** wanted to we like hesitated for too long on building that infrastructure which I think is

`[20:10]` **SPEAKER_01:** learning for for me I mean at this time chat GPT had not launched yet chat GPT hadn't launched and

`[20:16]` **SPEAKER_00:** so I guess we didn't know that it would be a big deal too this is around the pandemic 2022 this is

`[20:23]` **SPEAKER_04:** when chat GPT launched fall 2022 and then we we launched our API after that and then Claude AI after that also I think it didn't seem like it was working basically until Claude 3 5 and coding I think like really really like through that whole time then until about a year ago it seemed like it wasn't clear that we were going to end up being like a successful company we just saw that in the

`[20:53]` **SPEAKER_00:** terms of what is the preferred model for startups so all of 2023 open AI open AI was the response yeah then things started to turn in 2024 is when uh we saw Claude 3.5 and especially sonnet it was starting to get a market share per se in the YC batches going from single digit to at some point like 20 and to 30 percent and especially for coding yeah became the default choice which was very interesting can you tell us about how that emergent behavior and the spikiness was on that particular skill must be 80 now or 90. yeah for coding even more especially now clock

`[21:29]` **SPEAKER_00:** code what was that was that on purpose or just can happen I think that we invested more in trying to

`[21:36]` **SPEAKER_04:** make the model really good at code because we wanted the model to be good at code was one thing and then I think seeing seeing the reaction of everyone to it was like okay yeah like let's go

`[21:48]` **SPEAKER_03:** much harder on that also and this is before 3.5 sonnet you'd already invested enough in coding to realize that that was really promising and you said I decided to

`[21:57]` **SPEAKER_04:** double down I think this really was like individuals within the org being like we want to do coding uh before three five sonnet and then when we saw three five sonnets really good product market

`[22:05]` **SPEAKER_03:** fit that was good signal to like go go for that and you guys know like the day that you guys launched 3.5 sonnet did you know that you had something really special and this was going to be the turning point for the company or were you as surprised as opening I when they launched chat

`[22:19]` **SPEAKER_04:** gbt and it just like unexpectedly took off yeah I wish that I wish that we had like more foresight on that but no I think I think it was surprising for us to like how how big of a deal it was and then I think three sevens on it also like surprised us by how much it unlocked like agentic coding I think for for each of these things yeah we move quite fast in rolling them out and so we really um often don't know what the results are going to be there I think it's what

`[22:44]` **SPEAKER_00:** made a lot of these coding agent startups work I mean there's a crazy story of replit winning going to 100 million in uh just 10 months right there's cursor of course a story and all built on all these with sonnet I think that all of those

`[23:00]` **SPEAKER_04:** things have been surprising to me and then also just like in my working with Claude too like I think I continue to be surprised by like the type of stuff that it can do and I do think with each one there's like more stuff that kind of unlocks but one of my friends was telling me that she had some code that she uh some code source tool that she wanted to modify but she didn't have the source code for it she had the compiled binary and she's like oh can you can you decompile this like

`[23:23]` **SPEAKER_04:** can you disassemble the assembly and Claude Claude chewed on it for 10 minutes and like made a C version of it and so then she had the thing that you can modify it didn't say and she's like yeah and like if I spent three days on it I probably could have gotten the hex tables and like wrote in a little code but like it did the whole thing made up variable names for them Etc so I do think that like we keep getting surprised by stuff that model has memorized all the hex tables it can think

`[23:47]` **SPEAKER_04:** through try to work through it I think we're going to continue to be surprised by that sort of stuff

`[23:53]` **SPEAKER_03:** I prefer using anthropic models for coding by like a huge margin it's much larger than what you would predict if you just looked at the benchmark results yeah so there seems to be some x factor that makes people really like these models for coding do you know what it is and is it intentional in some way or it just came out of the black box somehow I think that the benchmarks benchmarks are like

`[24:16]` **SPEAKER_04:** easy to game where I think that all the other big Labs I think have teams where they like their whole job with the team is to like make the benchmarks scores good and we don't have such a team and so I think that I think that that is probably the biggest factor you don't teach to the test we don't teach those guys because I I do feel like if you start doing that then like it has weird bad incentives maybe we could like put that team under marketing or something like that and then ignore all the benchmarks but I think that that's

`[24:41]` **SPEAKER_00:** one reasons why there's some train tests mismatch there so the evaluations are more qualitative but

`[24:47]` **SPEAKER_03:** internally we have your internal internal benchmarks yeah but we don't we don't publish them and is it the internal benchmarks that the teams are really focused on improving that's right yeah so we have internal

`[24:57]` **SPEAKER_04:** benchmarks that the team focuses on improving and then we also have a bunch of tasks like I think that accelerating our own Engineers is like a top top priority for us too and so we we do a ton of like dog food in there to make sure that it's helping with our folks too going back to

`[25:12]` **SPEAKER_01:** Golden Gate Claude there's a lot of sort of the interpretability seems like it's a big part of it and then most people would say that you know Claude's personality just feels better yeah and then how do you sort of at once be very quantitative but then also you know build evals

`[25:29]` **SPEAKER_04:** around personality the evals for personality are kind of complicated too for like how do you tell if like Claude has like a good heart or something like that it's like hard to know um but I do think that that's like uh Amanda Askell's team's mandate is I think she describes it as like being like a a good world traveler where like it can like Claude goes and talks with all sorts of people from different backgrounds and like each of the people should come from him come to that being like I I

`[25:53]` **SPEAKER_04:** feel good about like this conversation that I've had interp really I think is like a long-term bet right where it's like right now the models aren't that scary but at some point they're going to be more scary and so I think the hope there is to have some ability to know what's actually going

`[26:07]` **SPEAKER_02:** on under the hood when it becomes more intense then more recently Claude code's been a real success can you talk us through like how did that project get started internally and again was it like a did you like know this time it was going to work or was it a surprise Claude code was um an

`[26:23]` **SPEAKER_04:** example like try to help out our our engineers within anthropic that uh yeah Boris um had like hacked together there's an internal anthropic engineer wanting to build it for themselves for internal for other internal engineers for him and other internal engineers and then um I think yeah I think we definitely didn't know that it would be successful out there and I think I think to some degree like we really had fully just bet on the API before that with the intention being like there's like so many so many startups out there

`[26:53]` **SPEAKER_04:** with so many good ideas who are we to like figure out what the right product is to build on top of this stuff everyone out there is going to build better stuff than us and so put all of our effort into just making the best possible API and I think that this surprised me as like okay like we actually were able to make something that like as a product was like better than the other products out on the market for this agentic use I have like a some theory that like part of that came from like a mind shift of seeing Claude as like the user uh for this thing too for like link that

`[27:23]` **SPEAKER_04:** like trying to build things for teachers were like our users for for grouper it was like single people in New York mostly I guess um for this I think really the like users are the developers but also I think the users is Claude it's like give Claude the right tools that Claude can actually do that effectively help Claude get the right contexts to work effectively this team was like the most focused on Claude as like a user which I think you guys would understand Claude the I think that that's a place where like startup founders though like can can do that too and I

`[27:57]` **SPEAKER_04:** think that that's that's probably a rich vein for people to like make tools that are better for

`[28:02]` **SPEAKER_01:** models as users that's the perfect anthropomorphization of like the LLM itself like the agent is one of the stakeholders one of the users that you would go after and try to like

`[28:13]` **SPEAKER_00:** empower yeah yeah totally which actually makes a lot of sense why you guys actually got mcp to work to do tool calling because a bunch of other labs had tried to do tool calling and they didn't work to do something and the standard that stuck that that really took off was yours yeah I think that

`[28:30]` **SPEAKER_02:** that seems like a similar one too where it's like it's like a model model focused going back to cool code so like success is really exciting it's also scary for like cursor and other companies that have built on top of the API like what's your advice to founders building products like how should they think about building on the API but also worrying about like anthropic or in the

`[28:49]` **SPEAKER_04:** labs building something better than they can build I think I was kind of surprised that Claude code didn't like we we did build a thing that was like uh like the best in the market there too it's not super clear to me what the big advantage was for us for Claude code besides more empathy for Claude

`[29:04]` **SPEAKER_02:** I think that's actually really interesting insight like it seems like the thing that yeah you were building for a specific user that you knew really well that other people wouldn't have thought to build for versus like you had some like intrinsic technology advantage yeah like I think a startup

`[29:18]` **SPEAKER_04:** could could have done that same thing too right yeah I think we're the most like developer focused I think we're the most like API focused lab too so I think we want to make sure that we have the best platform for people to build stuff on because this thing is growing so incredibly quickly like we're not going to be the fastest at figuring out all the ways that we need to empower Claude to do the work that connects Claude to the entire human business that's like human human world is all

`[29:44]` **SPEAKER_04:** designed for humans but like we need to get the models to be able to be productive members of

`[29:48]` **SPEAKER_02:** the economy are there like ideas or areas you would love to see developers building in or like areas you don't you you think are like underappreciated right now yeah Claude code is

`[30:00]` **SPEAKER_04:** like how do you get Claude to be a useful pair programmer kind of um or like junior engineer you've got like a sweet level two or three or something like that that you can work with or like very spiky because also it can do the like weird disassembly stuff that like a super high level suite would struggle with less good at knowing what type of work to do needs kind of a lot of hand holding needs a lot of context from it that's like one very particular subset of work that can be done if you look at like all

`[30:30]` **SPEAKER_04:** the stuff that happens in businesses besides that it's like a very tiny fraction of like all the work that's done in businesses that like a smart person who knows how to code and like use lots of tools but doesn't have that much context yet uh would want to do so I think I think finding ways to coach Claude or uh approach whatever model to like do useful tasks for businesses seems like there's just like a huge

`[30:59]` **SPEAKER_03:** huge space there so Tom a big part of your job is like owning all the compute infrastructure that makes anthropic work can you talk about like what what is the compute infrastructure behind this

`[31:10]` **SPEAKER_04:** giant thing now one thing that's interesting to look at is just that humanity is on track for like the largest infrastructure build out of all time now this is gonna be larger than the Apollo project larger than the Manhattan project it'll be bigger than both of them this year if it keeps on the current trajectory which is like roughly 3x per year increase in spending on AGI compute which is just bonkers yeah like 3x per year is wild I think it's going to keep up on the 3x per year trajectory it's already locked in for that for for next year and then

`[31:43]` **SPEAKER_04:** it's a little bit open for for 2027 I mean anecdotally internal to YC uh we can't get

`[31:50]` **SPEAKER_01:** enough you know credits across all of the top Frontier models yeah we're just I mean everyone's bottleneck literally every you know it's like give me more

`[32:02]` **SPEAKER_04:** intelligence I can't have enough yeah and I know you guys have been looking at more hardware startups also for like more accelerators I think that we will see more accelerators coming online to 2027. that's a good a good space also like data center tech I think is a big one where are

`[32:16]` **SPEAKER_03:** the bottlenecks for you guys now is it like getting enough electricity getting enough gpus getting construction permits

`[32:23]` **SPEAKER_01:** power people are using jet engines to get power that's nuts overall for the build out I think

`[32:29]` **SPEAKER_04:** power is going to be the biggest bottleneck especially power in the U.S like we want to build in the U.S that's one of our biggest policy goals is to like get the U.S to like build more data centers permit more data centers make it easier to build is the answer renewables or is

`[32:44]` **SPEAKER_03:** it uh nuclear I I definitely I feel like yes yes all of those things I wish I wish the nuclear was really alive that uses not just one kind of GPU but the GPU is from three different manufacturers can you talk about that and how how that strategy has played out yeah yeah so we use um gpus tpus

`[33:05]` **SPEAKER_04:** and tranium downside of doing that is that we split our performance engineering teams across all of those platforms which is a ton of extra work the positive thing is it gives us the flexibility to both one like soak up that extra capacity because there there just is more of those all together than just one. And then two is we can use the right chips for the right jobs, where some chips will be better for inference, some chips will be better for training, and we can match the right chips to the right jobs.

`[33:33]` **SPEAKER_04:** So yeah, I think that's kind of the trade off there.

`[33:36]` **SPEAKER_00:** I guess one cool thing is just connecting the dots through your career and how all of this compounded, because you were the one engineer building that change of the architecture from TPUs to GPUs back at OpenAI that got GPT-3 to actually scale. And now you're in charge of that at a much, much bigger scale years later. I don't know if that kind of connected dots for you.

`[33:59]` **SPEAKER_04:** The big move from TPUs to GPUs at OpenAI I think was partly driven just that PyTorch was a better software stack on top of them than TensorFlow on top of TPUs. And I think that that then unlocked fast iteration, where if you have a good reliable software stack, then you can... Experiment quickly, just build a whole system that works. I think that that's the thing that we really strive for now at Anthropic too, is a challenge of having many more platforms is that it's harder to write all the good software.

`[34:29]` **SPEAKER_04:** I think building the muscle of knowing how to build that software well so that all of the people who build on top of that low level can have a great experience with it is the most important thing there.

`[34:38]` **SPEAKER_00:** Do you have advice for a younger Tom version of yourself, who now you've seen and went through this crazy journey? If someone was you back in the 20s living today and they wanted to arrive and join the AI revolution, what would you say to them?

`[34:54]` **SPEAKER_02:** Very specifically, something we hear from a lot of college students at the moment is they don't know if they should stay in college, are there going to be jobs for them? How is the world going to change and what should they do?

`[35:07]` **SPEAKER_04:** Taking more risks I think is wise, and then also trying to work on stuff where your friends would be really excited and impressed. Yeah. If you did it, or a more idealized version of yourself would be really proud of yourself if you succeeded at it, I think is probably the thing that I would try to tell a younger version of myself.

`[35:26]` **SPEAKER_01:** More intrinsic, less extrinsic. Don't chase these other credentials and getting the degree or working at Fang. Those are just irrelevant as of today. Yeah. Exactly. That's all we have time for today. We'll see you guys next time.
