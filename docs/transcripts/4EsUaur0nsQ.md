# 全文转录 · 机器人的 GPT 时刻已到:一份垂直机器人创业 playbook

> ▶ [YouTube](https://www.youtube.com/watch?v=4EsUaur0nsQ) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/4EsUaur0nsQ.md) &nbsp;·&nbsp; The GPT Moment for Robotics Is Here
>
> 🗣️ 说话人分离识别到 **5** 位发言者(标注为 SPEAKER_00 …)。

`[00:00]` **SPEAKER_00:** The equation, I think, for starting a robotic business has changed and will continue to change at an accelerating pace because the upfront cost is not that high anymore.

`[00:12]` **SPEAKER_01:** Everyone's sort of spending a lot of time in the digital world and it feels like now is the time to start thinking about the world of atoms.

`[00:19]` **SPEAKER_04:** You literally just gave people the playbook for how to build a vertical robotics company.

`[00:24]` **SPEAKER_00:** This has really been our mission from the start, is to create that Cambrian explosion.

`[00:30]` **SPEAKER_04:** It still blows my mind. I didn't know if this would exist even in my entire lifetime.

`[00:41]` **SPEAKER_01:** Welcome back to another episode of The Light Cone. Today, we have a very special guest, Quan Vuong. He's one of the co-founders of Physical Intelligence, which we think might be the robotics AI lab that brings about the GPT-1 moment for all of robotics. Quan, thank you for joining us.

`[01:01]` **SPEAKER_00:** Pleasure to be here. Has been a long-time admirer of YC. And our mission, is to build a model that can control any robot to do any task that it's physically capable of and to do so as such a high level of performance that's going to be useful to people in all walks of life. And so, GPT-1 for robotics, what is it? Is the chat GPT moment for robotics real? Our perspective here is that we want to build a model that's really intelligent. We want to build a platform that allows us to externalize that intelligence to the rest of the world

`[01:34]` **SPEAKER_00:** and allow them to use it to build very easily, and we want to build a system that's very, very, very, very, very, very interesting application in all sorts of vertical and robotics. And we think that it's going to be more like a peeling an onion's analogy, where you start from a really strong base model that have all sorts of common sense knowledge and already works to some extent on your robot. You have then a mixed autonomy system, very similar, for example, to a autonomous driving car today.

`[02:03]` **SPEAKER_00:** And then you actually deploy that system to do a real job. That's okay. And then over time, by actually exposing the system to the complexity and the edge case of the real world, that system get incrementally, even just slightly better over time every day. And, you know, one day you wake up and you suddenly have a system that is just fully autonomous and just provide tremendous value.

`[02:24]` **SPEAKER_02:** Might be helpful to give the audience a bit of a mini history lesson on why robotics is so hard. And there's been a lot of breakthroughs in the last two years. And I mean, just to simplify that, the robotics problem is three pillars. Semantics, which I think we got a lot of at Luxon with language models that somehow we ported into robotics. Then you have the planning. And then the last thing is control, which needs to be done in real time and interact with an environment that changes. Walk us through the seminal papers

`[02:56]` **SPEAKER_02:** that a lot of the team of Pi Robotics published that gave you the inkling that the GPT-1 moment is near. And that started in 2024.

`[03:05]` **SPEAKER_00:** Yeah. The dream to build general purpose robots has been a long time dream, I think, in humanity. We're not the first to say that our mission is to build a model that can work on any robot. And we're really fortunate to be in this moment in time in history where we feel that it's possible to kind of walk back a little bit. A few years before, there was, I think, the first is Seikan, which to me was the first demonstration of language model and how we can bring all of the common sense knowledge

`[03:38]` **SPEAKER_00:** in language model into robotics. And therefore, that significantly kind of reduces the need to collect robot-specific data. So, for example, if you have a task of, oh, I want to go to the YC office to record a podcast, you know, what a step I need to take, you can ask a language model, you know, just show me the steps and show me the plan. And that worked incredibly well. And then the way kind of language model infiltrate, if you will, in robotics is to start at the planning level, at the semantic level.

`[04:05]` **SPEAKER_00:** And then, but there's still the control problem, you know, at the end of the day, you still need a mechanism to convert the plan into low-level action that can actually actuate the robot. And that bring us to POM-E, and that bring us to RT-2, which stands for Robotic Transformer 2. And what these two work really show is that if you start from a vision language model that is really powerful, and you kind of use robotic data to adapt this model to speak robot language, if you will, then you see a lot of transfer

`[04:38]` **SPEAKER_00:** from the kind of knowledge that exists in the language model, in the vision language model, down to the low-level action. Like one of my favorite example when we did the RT-2 project was you can have picture of celebrity on the table. You have a picture of Taylor Swift. You have a picture of the Queen of England. And you can ask the robot, you know, pick up the Coke can and move it to Taylor Swift, even though the concept of Taylor Swift is just doesn't exist in the robot data at all in that work.

`[05:07]` **SPEAKER_00:** You can do other examples such as kind of spatial reasoning that doesn't exist in the robot data at all. Like, for example, move the dinosaurs next to the red car. And these are all just completely unseen object in robot data. And so that was RT-2, and that was POM-E. Now, RT-2 and POM-E are single embodiment exercise.

`[05:30]` **SPEAKER_02:** Just for the audience, single embodiment meaning it worked for a very specific robot.

`[05:34]` **SPEAKER_00:** It worked for a very specific robot. In robotics, you can ask the question, how do you scale? Especially how do you scale data collections? And one of the insights that we had back then was, you know, maybe the data from one robot is not that different from another robot's anyway. If you have enough robots in your training data, maybe what the model learned isn't to control one specific robot. What the model learned is something that's more abstract, which is how do I kind of learn a general notion

`[06:01]` **SPEAKER_00:** of what it means to control any particular robotic platform? And therefore, I will be better at controlling any particular platform. And that brings us to what we call open cross embodiment and robotic transformer X.

`[06:16]` **SPEAKER_02:** That was a big paper because it was the first that showed potential scaling laws that apply to robotics because now you could start training all these models across multiple kinds of hardware, not just one, which has never been done in robotics. Ever before. Because from all the research labs, they would all train with a very specific set of sensor actuators and motors, and it was all very finicky with that particular hardware, right?

`[06:41]` **SPEAKER_00:** Yeah. One of the really interesting results from open cross embodiment, and let me provide the context here, is that you can take, let's say, 10 different robot platforms, collect data from them, train a policy, and really optimize the policy to work well on that platform. So let's say, you know, you have that, you have 10 different platforms, 10 different policies, and now if you simply take the data and absorb it into a model that is high capacity enough to really absorb that data and you can compare,

`[07:09]` **SPEAKER_00:** you have these generalists, right, that learn to control how to test the 10 different robots. You can compare it to the specialist that has been optimized to work well on a particular embodiment. How does it compare? And the interesting result from open X is it was 50% better. Wow. And that was really surprising. Wow. And in robotic, it's hard enough to get your model to work on one particular robot platform. And one of the reasons why I say that we're really fortunate to be in this moment in time in robotic

`[07:39]` **SPEAKER_00:** is because open X was really only possible because of the support that we received from the robotic community. It was a huge collaboration across the robotic community. And the reason why that's really important is there is this joke in robotic grad school that, you know, if you want to add two years to your PhD, just work on a new robot platform. You know, by that logic, if you want to have 10 robot platform, that's 20 years.

`[08:06]` **SPEAKER_01:** Why is that? It takes like a year or two to just get the platform up and running to even collect the data.

`[08:12]` **SPEAKER_02:** Yeah. Is it fair to say that the data set that was created from embodiment X is similar to the scale of an impact that ImageNet did for vision because it was huge and it was the first large data set across multiple hardware, huge collaboration,

`[08:28]` **SPEAKER_00:** I still think that ImageNet was more impactful in the vision community. And the reason for that is a few. The first is that ImageNet also allowed for reproducible evaluation. Right. You know, open X as an effort was more about making data available for kind of people to use. And evaluation is a really difficult problems in robotic that open X did not solve. And the second is I think open X is a drop in the bucket at this point in the robotic community. If you measure in the kind of the scale and the volume

`[09:06]` **SPEAKER_00:** and the diversity of data that the community is collecting, I think open X at this point is a drop in the bucket.

`[09:11]` **SPEAKER_01:** I mean, I guess we started talking about sort of GP1, but even GP1, that was sort of this moment where you can prove, Alec Radford figured out that there was a neuron based on a very specific input and output. And then that allowed the scaling laws to sort of take hold. The biggest problem in robotics I've heard is basically actually exactly what we've been talking about. It's like it's the data problem. You know, language you could bootstrap off of like, you know, the sum total of what you could get off the internet,

`[09:41]` **SPEAKER_01:** which is actually quite a lot. Can you give us like a sense for like scale? Is it like petabytes? Like, you know, what do you think is necessary as an input to, you know, the true GPT-1 of robotics?

`[09:55]` **SPEAKER_00:** Yeah. The data scarcity problem in robotics, there's a few ways to look at it. The first way is that it's really two problems in disguise. There is the generation, data generation problem, and there's data capture problem. And the difference is that the data capture is that there might already be lots of robotic data that is being generated, but there's just never been really an incentive to capture it, to make it easy for digestions in training. And that's one of the goals that open X was trying to solve,

`[10:21]` **SPEAKER_00:** which is if you have robotic data, it's a really good idea to capture it and make it possible to train on. The second way to look at it is that robotic is very different from language model. There is not a internet of robotic data that you can use. And so you see these kind of very operationally heavy effort to collect data. And there's the question of, is it going to scale? Well, the way that I look at it is, let's take the US GDP, 24 trillion US dollars. Let's say if we actually solve robotics,

`[10:52]` **SPEAKER_00:** a model that can control any robot to scale, to do any task, napkin math, maybe contribute 10% to US GDP. Well, that's already a massive number. And I think that promise is one of the reasons that warrants the investment into data collections in robotics. And the third way to look at it is we're very focused on cross embodiment. And cross embodiment, there is the data collection aspect of as well, which is to really make sure that your model and your organizations and infrastructure are set up to consume data

`[11:27]` **SPEAKER_00:** from many different sources of robots. And that actually allows you to scale easier. For example, if I were to contrast our approach compared to, let's say a company that have a particular hardware platform that they optimize for and they scale, it's not an approach that have really allowed people to scale because it's just much harder to figure out how do you manufacture like a thousand unit of something for now compared to making sure that you yourself are ready to absorb data from like a thousand different types of robot

`[12:01]` **SPEAKER_00:** that are already in there in the community.

`[12:03]` **SPEAKER_01:** I mean, it's a crazy problem, isn't it? I mean, the hardware itself, even within the same design of embodiment, if there's a hardware run that goes awry or like one of the servos is slightly different, like you see it in the data, right? And then how do you control for that?

`[12:18]` **SPEAKER_00:** Yeah, so I think we were doing kind of like an inventory of robot in the cloud. I mean, we were in the company, we were so shocked to find out there are no robot, no two robot platform that are the same. And if you ask people in the ROI community, sometimes there's debate about multi robot versus single robot. And the argument is that, you know, single robot is simpler to scale. And actually that's not how it plays out in practice. Like how it plays out in practice is even if you have a single robot that you're optimizing for,

`[12:45]` **SPEAKER_00:** over time that platform is going to drift. You know, maybe you want to make hardware change or you have software change. You end up in a situation where it's much harder for you to reuse old data because, you know, in machine learning, if you want to generalize from a distribution, you would like many sample from that distribution. And if you just have one robot platform that have a major change every three months, maybe you have a few data points from that distribution. Whereas if you start from the hypothesis

`[13:12]` **SPEAKER_00:** that if you have many robot platform in your fleet, your model is going to learn something more abstract, which is how do I control a robot, not any particular robot, then the model will be able to ingest data from, you know, a slightly different robot better. And actually, we're starting to see emergent property in this kind of robot large foundation model. That's good news. We're doing. Where you start to see like interesting transfer between different data sources. For example, today it's possible to perform tasks zero-shot.

`[13:44]` **SPEAKER_00:** Zero-shot meaning you don't collect any data. And these are the tasks that last year might have required like hundreds and hundreds of hours.

`[13:50]` **SPEAKER_01:** What are some examples? Yeah. Do we have any videos we can see that like show it?

`[13:54]` **SPEAKER_00:** So, you know, I get some flack when I come back because this is not published result. Hopefully this will come out soon. So, you know, I want to reserve the excitement for that. Fair enough. And I'm kind of like building up the excitement a little bit. So hopefully this will come out soon. All right. These are not simple tasks. These are like actually difficult tasks that just last year required like hundreds of hours of data collections.

`[14:16]` **SPEAKER_01:** You hear on Lightcone first that there's some emergent property that are going to come out of Pi. Can you give us a sense of like the flavor of the tasks?

`[14:24]` **SPEAKER_00:** It's really easy to fool yourself. And so we wanted to test across like field different tasks of different flavor. A task that require precision, task that require reasoning with multiple objects in the scene. It all seems to have this property. That's really nice. So it does seems like that's something that's kind of a more general property that emerge rather than we just, you know, got lucky and suddenly the models start working on one particular task.

`[14:49]` **SPEAKER_04:** Could you help us understand where we are now in terms of like what's working and how well it's working? Like we're not quite at the chat GBT moment yet. Like where are we? And I think you brought some videos that you were going to show us to like help everybody visualize what the current state of the art actually looks like.

`[15:04]` **SPEAKER_00:** I think where we are is I think if you have a task where it's okay for the robot to make a mistake and it's possible for you to set up a mixed autonomy system where you have a person that takes over when the robot make a mistake and provide corrections, it is possible to get to a level of performance where it starts to make sense to think about scaling robot deployment. And the example that I specifically want to highlight here is this blog post that we did with Weave and Ultra. And, you know, it's great that these are both YC company.

`[15:41]` **SPEAKER_00:** I want to provide a little bit of context here first. The context is that PI is a primarily research organization. We want to focus on building the best model, but we also want to not be tunnel vision. We want to make sure that the model that we built actually going to be useful and actually perform tasks that people in society cares about. And one of the really good way for us to do so is to partner really closely with company that want to get robot out there today. And the way that these relationship work

`[16:09]` **SPEAKER_00:** is that we treat each other like we're on the same team, very free flow of information. And we design a system that try to get the best possible performance for the task that these company care about. So let me talk about Weave first. What you're seeing in this video is a system that we built together folding really diverse item of laundry in a real laundromat in the mission. You can see, you know, people walking outside. And why this task is difficult is because there's just infinite possibility

`[16:44]` **SPEAKER_00:** of observation space. Like, you know, clothings are deformable. And no two items of clothing here are the same. And these are also unseen. You know, these are not, like, clothing items that are seen in the training data.

`[16:58]` **SPEAKER_01:** Yeah, I love this team. They are some of the most cracked people out of Apple I've ever met.

`[17:03]` **SPEAKER_04:** Gary was the partner for Weave. Maybe you want to, like, explain, like, what Weave is and what their, like, company is.

`[17:08]` **SPEAKER_01:** Yeah, I mean, they're actually, you know, shipping their first robots into the home. We sort of talked about it as, you know, being able to do household tasks like this. And I think they were very inspired by that. They were inspired by Physical Intelligence's first demos with laundry folding. So it's actually a total trip to hear about it, you know, a year ago. We were talking about them doing it. And then now to see them do it working hand-in-hand with you is really awesome. I think this is a great example of, like,

`[17:37]` **SPEAKER_01:** you know, you need the model smarts, you need the data collection, and then the hardware and the sort of system integration all working together is just hard to nail.

`[17:47]` **SPEAKER_00:** Yeah, and to get back to your question about why robotic is hard, it's really, it is a really hard system problem. Like, you need everything to work well and work well together to get this result. And, like, Weave is such an incredible team for us to work with to get this result. And it actually didn't even take us that long to get this result. It was roughly, well, we set a goal, and maybe it was, like, two weeks afterwards where we got a model that was, got a model and a system that was good enough

`[18:17]` **SPEAKER_00:** at performing this task.

`[18:18]` **SPEAKER_04:** It still, like, blows my mind to see a robot actually folding laundry because I remember until, basically, until ChatGPT, I didn't know if this would exist even in my entire lifetime. Because, like, folding laundry, I mean, it's always been, like, the Turing test for robotics because there's no way to, like, deterministically program a system the way that you did, like, pre-AI to do this because the space is, like, so infinite. And, like, we've shown that it's possible for us to do, like, basically, if everyone can do this,

`[18:43]` **SPEAKER_04:** like, robots will be able to do everything. It's only a matter of, like, improving it from here.

`[18:47]` **SPEAKER_00:** There was a funny story where when we first published Pi Zero, people thought of us as the laundry company. Because the demo was just focused on laundry and actually picking home tasks, especially tasks that has to do with deformable objects, is a very intentional choice on our end. We're not just after the home. We really want to make it broadly applicable. But picking home tasks for us to start with has a few benefits. Like, one, it's relatable. You know, you can see the laundry folding

`[19:17]` **SPEAKER_00:** demo and you can kind of, like, grok how this is going to be useful. And you can get a sense of why it's hard. And the second is that it's really easy to set up to test generalization.

`[19:27]` **SPEAKER_02:** You can talk about Ultra, which is your company, Jared. A demo of it.

`[19:30]` **SPEAKER_00:** Yeah, this is Ultra. The thing that I love about this video is you see it's bright outside. And you see this is 4x speed and it's 100 minutes. If I scroll to the end, the sun has set.

`[19:42]` **SPEAKER_02:** Oh, wow. That was one of the big problems in robotics. Where it would be so sensitive to the environment in lighting and mess up the vision system, the semantics and part of it. Yeah.

`[19:54]` **SPEAKER_00:** And the interesting thing here is that it is possible to get to the level of autonomy that the robot is just performing the task. This is autonomy at scale. Like, this is ready to be scaled.

`[20:08]` **SPEAKER_04:** Quan, because this task is less familiar than laundry folding, do you want to explain what the robot is doing here and what Ultra is, like, doing as a company? Ultra is a company

`[20:17]` **SPEAKER_00:** that want to make it really easy to adapt robot to, you know, new tasks. And right now they're focusing on logistics space, which is really important because there's lots of labor shortage in logistics. And the task that we focus on together here is, you know, if you order an item from Amazon, you sometimes get this soft pouch that item gets shipped from. And the task here is you have a tray of these items here and the robot is supposed to pick one of them. at the time and place it inside this pouch.

`[20:48]` **SPEAKER_00:** The machine would then close it and then pick up the pouch and put it on the left here to be ready for shipping. Now, this is hard because there are many different types of objects that can be in this tray. And the opening here is actually very narrow. So you see this interesting example of the robot kind of nudging the item to go into the pouch. And that's really hard. Like, that requires a very good understanding of the scene and, like, very precise motion to nudge the object into the pouch.

`[21:19]` **SPEAKER_00:** The other thing that's hard about this task is the level of autonomy that's required. Like, this is running for an entire day. There is still human intervention, I want to say, in this, like, full-day operation. But the level of intervention is actually quite minimal.

`[21:39]` **SPEAKER_04:** This is not just, like, some, like, demo station, right? This is actually recorded in an actual e-commerce warehouse where they're actually shipping real products to real customers. This isn't just, like, a lab.

`[21:48]` **SPEAKER_00:** This is packaging real customer, real order for customer to be shipped out in a real warehouse. So this is real operations.

`[21:56]` **SPEAKER_04:** So I think this is really cool because I think when people think about robots, they tend to think of the consumer use cases like Weave because that's, you know, what we're familiar with in our daily life. What I find really interesting is that there's, like, a million applications like this Ultra thing that you wouldn't think of as obviously, like, oh, who packs the, like, soft pouch of things that you get from, like, Amazon? Well, there's some person, like, who does that, and this is, like, a job

`[22:16]` **SPEAKER_04:** that we could not build a robot to do.

`[22:18]` **SPEAKER_00:** The interesting thing about the approach is that you're converting it from a very difficult engineering problem into a operation problem of how do I identify the use case and how do I collect the right data, which is, in some sense, more scalable because you can build the system that allows you to collect data from many different tasks. So, you know, it's not a problem of how do I scale data collection rather than, you know, for every new product, for every new task, how do I design a really difficult engineering system

`[22:46]` **SPEAKER_00:** to solve it?

`[22:47]` **SPEAKER_02:** YC Startup School is back. We're hand-selecting the most promising builders in the world and flying them out to San Francisco for July 25th and 26th to discuss the cutting edge of tech. Apply now for a spot. Okay, back to the video. I think one thing that the audience may not know is that you have a very unique technical insight that, in the past, robotics folks would have kind of gasped and be shocked because robots need to run in real time. A lot of times, all of the compute runs in on-device,

`[23:16]` **SPEAKER_02:** but you guys have done something very different. Can you tell us more about that so that this works in real time with large models and really well? So, the context here is that, you know, we talked to many companies that would like to deploy robots

`[23:27]` **SPEAKER_00:** and one of the first questions we get is, what compute units should we get on the robot? You know, it's expensive, it's going to increase the bomb cost, and they're worried that it's going to go out in fashion very quickly because they don't know what they're going to get. So, you know, I think it's important to think in fashion very quickly because the model changes, the model gets bigger. How do I make sure that the hardware that I'm going to commit to today is going to be viable for a couple of years?

`[23:50]` **SPEAKER_00:** It's a very difficult question. People are often really surprised when I tell them that almost all of the robot evaluation that we run at Pi today, including the really complicated demo that we have shown, making coffee, folding laundry, mobile robots navigating around, the model is actually hosted in the cloud. And, you know, this is not like a cloud as in a server in the office. It's a real-world model to the cloud. The model is hosted in a data center somewhere. And within this high-frequency control loop

`[24:17]` **SPEAKER_00:** that is controlling the robot, the robot is actually querying an API endpoint that hosts the model, sending it images and language command and getting back action that then executed directly on the robot. And this is surprising because of precisely the reason that you mentioned, you know, how do you actually make it work? This is why it's really important for Pi to couple a lot of different applications and systems, hardware, and model development and research very tightly together because it allows us to solve

`[24:48]` **SPEAKER_00:** for this problem. So, for example, one of the insights that we have here is that you can actually bury the inference time within the robot control loop because, you know, if I'm a robot, I have enough action for me to execute for the next 100 milliseconds. There's no reason for me to wait until I finish executing that action to ask my model for a different action. I can do it as fast as inference, essentially. And so, you know, maybe when I only have 50 milliseconds of action worth left, I can ask for the next sets of action

`[25:22]` **SPEAKER_00:** and when the current 50 milliseconds is over, I have something that's ready for me to continue with, you know, my next 100 milliseconds. So that's one of the insight. The other kind of algorithmic improvement, we refer to them as real-time chunking. Desire inference in such a way that you know there's going to be a delay in how long it takes to query the model on the cloud, basically. Like the problem here, if I get a little bit more technical, is an action chunk is a sequence of action that I can execute on the robot.

`[25:56]` **SPEAKER_00:** So, you know, it's not just one action. And if I have an action chunk that I can execute for 100 milliseconds and 50 milliseconds in, I want to predict another action chunk and I'm going to transition to that new action chunk if my current 50 millisecond is over. How do I make sure the two are consistent? Like, you know, how do I make sure that if I'm moving this way, the next action chunk is going to continue to allow me to continue to be smoothly

`[26:20]` **SPEAKER_01:** moving this way?

`[26:21]` **SPEAKER_00:** You can pre-compute. Yeah, you can pre-compute and like that's one of the algorithmic improvement that we made to make inference using model hosted

`[26:29]` **SPEAKER_01:** in the cloud possible. I studied computer engineering, so I'm not really an algorithms person, but when it comes to systems like that, like pipelining, like get me all over that. That's great. That's so interesting.

`[26:40]` **SPEAKER_02:** I mean, this simplifies is a brilliant choice because it simplifies so much of the system for the robots. You don't need all these clunky. I don't know. People have two operating systems that sometimes for robots embedded RTOS and then the regular one and all these complex giant compute and power. And this is what the initial versions of Waymo used to run basically a server on the trunk and you can't afford to do that with general day robotics, which is brilliant

`[27:08]` **SPEAKER_01:** because you don't have to. I mean, you can do things. Some of it obviously has to be some compute there, but a lot of the compute can happen elsewhere. And then is there there must be a video like this, this thing that we're looking at in the top left, like how much of that is sort of like video feedback?

`[27:26]` **SPEAKER_04:** How much of it is like local processed? I mean, is there any compute locally on this robot

`[27:31]` **SPEAKER_00:** or is it just like a dumb like video camera that streams data to the cloud for this? I'm trying to believe that it's just a dumb computer for this specific video. I don't remember, but I'm just 100% confident that we can make this work with a dumb computer on the robot. And one other interesting thing about our collaboration with Weave and Ultra is one, I've never seen

`[27:53]` **SPEAKER_01:** that robot in person.

`[27:54]` **SPEAKER_00:** Oh, wow. Two is I have very little idea about how the robot actually works.

`[28:00]` **SPEAKER_04:** Interesting.

`[28:01]` **SPEAKER_00:** And that's a very intentional choice. I want to stay away from that as far as possible. I also don't know how they collect data. Like I intentionally don't ask them this question to understand whether it's possible for an organization like Pi to parachute into their existing system and to work really closely with them on the thing that actually matters to get the system to work and not have to learn about how they've set up their system because in a way that's like a more

`[28:31]` **SPEAKER_02:** scalable recipe. Yeah, you completely decouple a lot of the hardware control from the semantics and planning which just works. Just brilliant.

`[28:41]` **SPEAKER_00:** Yeah. I mean, I'm really surprised. It works. When we started the company, we thought that real deployment is only going to be in a conversation like five years into the life of the company because the problem is just really hard. And we're two years in and this is the result that we have and real deployment and scaling the number of robots is a really serious consideration today and so the pace of progress has just been very pleasantly much faster than we expected

`[29:12]` **SPEAKER_04:** originally. Often on this podcast we talk about like what all this means for startup founders. I think that might be an interesting question for us to explore here. So if you imagine someone was listening to this podcast, maybe they're like a college student that's studying computer science and they think robots are really cool and they want to do something like this, how should they get started and what are the skills that they need? Do they need to be a mechanical engineer or do they need a robot arm

`[29:37]` **SPEAKER_04:** and camera system and like what? And load pie and you're often running in like a day.

`[29:42]` **SPEAKER_00:** Yeah. Before I actually answer your question, let me provide a few more context. The first is that robotic is traditionally really hard because it's an extremely vertically integrated business. You need to have your own customer relationship, your own hardware, your own autonomy stack, your own safety certification, your own everything. And the barrier to entry is just really high because of that and one of the things that we're trying to change is that we're trying to provide a foundation of physical intelligence

`[30:11]` **SPEAKER_00:** that the community can build on top of that allow them to onboard autonomy onto their robot and their task much quicker than before. So that's the first. We want to provide that kind of seat of intelligence that allow people to move much faster so that they can focus on other problems. The second thing is that I think the recipe for starting a vertical robotic business today is one, have a really good understanding of the existing workflow because the robotic system needs to fit into an existing workflow.

`[30:45]` **SPEAKER_00:** And the second is to be very meticulous about identifying where the opportunity is. If there's a workflow that needs X number of work today, where is the robot when you insert it is going to make the biggest difference. And two is to really be scrappy when it comes to hardware and data collections. You don't need an incredibly expensive robot that is capable of very precise motion today to be able to do this task. And the reason why is this model really reactive and so they can compensate for some of the inaccuracy

`[31:17]` **SPEAKER_00:** in the actual robot movement and to ensure that you have the ability to collect data and to run evaluation, especially evaluation in real deployment. The next step after that is to get a mixed autonomy system that allow you to get to the point where it's break even. Like break even economically. Break even economically because the reason why that's important is because it allows you to then scale the number of robots. Because if you lose money

`[31:43]` **SPEAKER_04:** in every robot, it's very hard to scale.

`[31:45]` **SPEAKER_02:** That has been historically one of the biggest challenges for robotic companies as they go into growth stage. It's just the payback hack period is just doesn't make sense. Yeah, so the equation

`[31:53]` **SPEAKER_00:** I think for starting a robotic business has changed and will continue to change at an accelerating pace because the upfront cost is not that high anymore. And now, you know, what is the upfront cost? The upfront cost is much cheaper hardware, ability to collect data, ability to collect evaluation and ability to kind of like understand the use case to see where they should insert the robot. You know, it's not about having incredibly expensive hardware. It's not about having your own proprietary, I think, autonomy,

`[32:29]` **SPEAKER_00:** classical stack anymore to be able to do that. You have to do this task. And so it allows a company to focus on the component that will actually allow them to differentiate themselves from the rest of the space.

`[32:41]` **SPEAKER_04:** Now that you've sort of unbundled it and you no longer need to build this fully vertically integrated company in order to build a robotics company, are we on the precipice of a Cambrian explosion of vertical robotics companies where there's going to be like a thousand companies like Ultra going after, you know, every like menial job in the economy and like getting a deep understanding of the customer, building a robot without any problem, doing like mixed human machine deployment until it like can run

`[33:06]` **SPEAKER_04:** fully autonomously and building a company in every sector? Is that the future that you see people building on top of Pi? It's funny that you mentioned

`[33:13]` **SPEAKER_00:** Cambrian explosion because when we wrote this blog post, there was that term that was very kind of like hotly debated. We are, I think, academics at Hurt and we want to be kind of very measure when we communicate. But, you know, myself personally, I believe there's going to be a Cambrian explosion of, you know, of robotic company across the entire world and across many, many different verticals just because it's just so much cheaper to build and it doesn't require, you know, someone with 20 years of experience in robotic

`[33:45]` **SPEAKER_00:** to start anymore. You know, it requires someone that is really scrappy that can move really quickly, can do the system integration, can understand customer what they want to start the deployment.

`[33:59]` **SPEAKER_01:** I mean, what's coming up for me is obviously we work with a lot of robotics companies and to meet a lot of founders and it feels like there's this continuum. One is to use an analogy to compete, you know, personal computing. You could argue that industrial robotics today is basically like mainframe for a mini computer level. Like, you know, if you look back in the 70s, huge public companies like Digital Computer that, you know, just did like these sort of very, very expensive deployments but like they were very,

`[34:30]` **SPEAKER_01:** very specialized. And it was all extreme enterprise. Like, you know, the idea of a personal computer was ridiculous, right? You know, it took the Altair and then Apple I and Apple II and then IBM PC XT to like create personal computing. And then like the traditional advice for robotics for many years is like go after like dirty and dangerous. And then, of course, those are sort of the industrial cases. Like, you know, you have these giant Tesla robots in the Gigafactory and things like that. It feels like what you said

`[34:59]` **SPEAKER_01:** around profitability is really, really big. So, you know, does that mean that the people who do the vertical robot Cambrian explosion sort of moment, the people who are sort of first in that, like it sounds like they would be the first to be profitable and not dirty and dangerous. I think this is already

`[35:21]` **SPEAKER_00:** happening today. I think we have the fortune of having lots of visibility into the robotic community because, you know, people would like to talk to us. People would like to learn, you know, what it's like to build a foundation model for robotic and people would like to know how do I get the same level of autonomy? And there are so many companies and businesses that we talk to that would love to put a robot into their space that, you know, it's okay for the robot to make a mistake. And this is needed so much.

`[35:51]` **SPEAKER_00:** I really believe that the recipe that I mentioned earlier of identify where the robot can fit in focus on cheaper hardware, collect data, run evaluation, mix autonomy, break even, scale robots will work across many different verticals. And I'm seeing it play out today and it's just incredibly exciting to see. And this is pretty cool

`[36:11]` **SPEAKER_04:** that you literally just gave people the playbook for how to build a vertical robotics company. Like this is a playbook that could possibly be followed successfully hundreds or thousands of times. And the reason why

`[36:21]` **SPEAKER_00:** I want to mention it is because I do want to see that Cambrian explosions. And so, we want to help enable it. You know, for Pi, if we talk about why Pi is going to fail, it's probably going to be because the problem is just way too hard. You know, maybe it takes 50 more years to solve the robotic problem and, you know, not a couple of years, five, ten. And so, we want to enable the community. We want to accelerate progress and that's why we're very open. We publish our research. We open source Pi 0 and Pi 05.

`[36:53]` **SPEAKER_00:** And people also shock when they ask me, you know, what's the difference between Pi 0 and Pi 05 that you open source versus the model that we use internally, Pi 0 and Pi 05? And the answer was, I actually know. It's the same model. Like, the pre-trained model weights that you're using that we open source is also the pre-trained model weights that our researchers internally use for Pi 0 and Pi 05. And so, we really want to help accelerate progress in the community and to create that Cambrian explosions.

`[37:21]` **SPEAKER_01:** Yeah, that's very inspiring. I mean, I feel like that's everyone's sort of spending a lot of time in the digital world. And it feels like, you know, now is the time to start thinking about, you know, the world of atoms. And this is sort of the perfect mix of actually, like, you know, how do you take electrons and turn it into abundance in the, you know, atoms world? And I think about Dario Amadei's essay, All Watched Over by Machines of Loving Grace. And when you really think about the perfect manifestation of that,

`[37:52]` **SPEAKER_01:** it's not like, you know, perfect agents that look over you and say, you just like in the electronic world. It's, you know, actually something a little bit more akin to what we're seeing here.

`[38:04]` **SPEAKER_00:** Yeah. And this has really been our mission from the start is to create that Cambrian explosion. And, you know, this is why we choose to focus on the model because we believe that is the bottleneck to just really make robot useful across many different tasks in the world. And that's why we also focus on cross embodiment. You know, success for us is not defined as only our model on our robot performing tasks that is useful. The surface area for success is actually much larger, which is our model performing really useful tasks

`[38:37]` **SPEAKER_00:** on somebody else robot out there. Maybe that we don't even know what that robot is like in a way that's useful to the end consumer.

`[38:45]` **SPEAKER_03:** Could we maybe talk a little bit about like the humans behind the robots here? How did the company get started? Like who are the, who are your co-founders? How do you all get together? And what skills do you each bring to such a complex problem?

`[38:58]` **SPEAKER_00:** Sometimes the joke I make here is that the human behind the robots are also robots. Not really. Yeah, so Pi is a very, I would say, untraditional company. We have a like larger than average founding teams. And some of us work really closely together when we were at the robotic team at Google. And the robotics team at Google was I think a really, really great environment for seeing the sign of life and creating the relationship in the community that allow the robot community and like these advances

`[39:29]` **SPEAKER_00:** to flourish. There is Locky, which we met when we were thinking about starting the company and it has just been really instrumental in making sure that we're a good business. And there is Adnan, our hardware lead that came over from Android. And Adnan has a really difficult job because if you want to work on cross embodiment, you remember my joke about how if you want to add two years to your grad school, you have to work on cross embodiment, you have to bring on one more robots. The hardware problem

`[39:59]` **SPEAKER_00:** and the operational problem for us is how do we build, improve and scale a fleet of heterogeneous robot. It's just not one robot platform. And because we built the organization from scratch in the beginning to support that, I think we're able to do it, but it's just a really hard problem because there's just like no two different robots in the fleet. How do you make sure everything runs smoothly? We're really good at divide and conquer, if you ask. How many co-founders

`[40:31]` **SPEAKER_03:** are there in total?

`[40:32]` **SPEAKER_00:** We have Brian, we have Chelsea, Sergey, myself, Lucky and Adnan.

`[40:37]` **SPEAKER_03:** Is it just necessary to have that many co-founders to solve a problem as big as this? Or was it a case like you were already sort of like a unit together, you'd already worked together and you just, whatever you started,

`[40:48]` **SPEAKER_00:** you would all have Yeah, one common question that we have is, you know, why band together? And, you know, the first is that we really enjoy each other company. We spend a lot of time at work and it's, you know, in some sense give meaning to life. And so we really want to enjoy the relationship we have at work. And the second is that, you know, any one of us could have started a company and be successful. But the problem is just so incredibly hard. And the chances of success is just so much higher that we band together

`[41:20]` **SPEAKER_00:** and we can divide and conquer the problems. And, you know, that's the, I think, the main reason why the progress has been much faster than we expected. What were the differences

`[41:30]` **SPEAKER_02:** of you working before in either academia or a big industry, big company like Google as opposed to now in a startup? This is the first time for a lot of you doing a startup, right? Yeah, this is the first time for a lot of us. One of the really surprising thing that we learned when we started the company is that

`[41:46]` **SPEAKER_00:** the infrastructure for a startup is not the same as the infrastructure for a company. You know, the infrastructure for a company is the infrastructure for supporting large-scale general-purpose robot, which is not there. And, you know, this starts from the software itself. How do you collect data? What device do you use to collect data? How do you manage the data? How do you annotate the data? How do you get visibility into the data? How do you run evaluation? How do you build operational process? Like,

`[42:14]` **SPEAKER_00:** there wasn't a company that offered this kind of services, which is very different from software. And we were really surprised to find out. And so, we ended up writing a lot of the software at Pi ourselves. But I think this is another area of incredible opportunity of kind of building services for a robot company. Like, you know, if you can offer remote telehealth, for example, if you can offer data collections, if you can offer annotation service. Because, you know, these are functions that doesn't need

`[42:43]` **SPEAKER_00:** to be repeated from one company to the next. So I think there's lots of opportunity to build kind of support for growing robotic business. So that's one thing, and the second is I think one of the reasons why we have managed to achieve such progress is that there is a really tight loop of collaboration in the entire life cycle of model development. Going from what task do you collect data for? You collect data for the task. How do you do it? What hardware do you use? Once after you collect the data, how do you get visibility?

`[43:19]` **SPEAKER_00:** How do you ensure data quality? How do you then make sure that after you train on that, how do you run evaluation? Evaluation is a really hard problem in robotic because it scales super linearly to model capability. Let's say you have a model that can perform a two-minute task. Running evaluation for that is very different from running evaluation for a task that's 20 minutes. It's not 10 times harder. It's more than 10 times harder. After you run evaluation, how do you can distill the learning from that evaluation

`[43:50]` **SPEAKER_00:** to know how to improve the model further? One of the really side projects I would love to take on is to build an automated robotic research scientist, which is really one of the bottlenecks we have today because this is a really difficult skill set that requires intuition about the entire stack. I would love it if there is a model that can ingest multi-model data such as this and analyze filler modes, understanding is the robot performing this way because of the data that was collected and the way that it was annotated

`[44:25]` **SPEAKER_00:** and the way that we train the model and then suggest ideas and actually try them to figure out if those hypotheses are correct. That's something that I would love to have and would dramatically unlock us. Sometimes I make the joke in the company that we should record all of the meetings and then train a model to basically just make prediction about what is

`[44:44]` **SPEAKER_01:** the next sets of experiments. You could. You totally could. What if it's OpenClaw and Obsidian and Markdown files and a brain.md with ontology that's custom to your use case and what if it's a hundred OpenClaws in the background that you orchestrate? I think there's

`[45:00]` **SPEAKER_00:** two sides to this. The first is that we already see a little bit of a sigh of life where for simple filler modes during evaluation if you can describe the way that the robot fill in text very precisely and very clearly then you know you can ask the language model to make very reasonable recommendation about what the next step is. But the flip side is that this only works for simple cases today and the reason why that's the case is because I think it's pretty fundamental limitation of the model that we have today

`[45:31]` **SPEAKER_00:** which is that they are not at the core model that take action in the world and see the consequences of its own action especially action that changes the physical world. And so I think this kind of very fundamental understanding about how the physical world works is missing from the really large foundation model and I think that's one of the ingredient that's missing to be able to build this automated robot research scientist. What's interesting

`[46:00]` **SPEAKER_01:** about OpenClaw I don't know I mean basically it can go and it can just do things which is interesting and then at that point it's on the research lab to provide like you know CLI MCP endpoints to the things that might control robots or reconfigure rooms or I mean I think Karpathy he's starting to talk a bunch about this where you know if you mix auto research plus what he's been talking about with markdown files like it might just happen in the open like you know there's a sort of sense that you have to make something much

`[46:41]` **SPEAKER_01:** much more complicated to make it work but what if that's just wrong what if we just have markdown files and agents and you know you could make it yourself it's just literally an integration challenge

`[46:54]` **SPEAKER_00:** we have a version of this internally that I use a lot there was a point when I was spending a embarrassingly large amount of money on API queries yeah and you know my team was like

`[47:09]` **SPEAKER_01:** Kwon what are you doing oh I'm that guy

`[47:11]` **SPEAKER_00:** at Y Combinator right now so to give you an example we have a cloud skill that's essentially serving the role of a pre-training on call today so you know we have these pre-training runs that are really large it's very I think a difficult exercise to keep them alive to you know for them to continue to churn just because there's so many things that can go wrong and we have a prototype a pre-training on call that kind of babysit the run and have the permission to take action to remedy error that it see and one of the surprising

`[47:49]` **SPEAKER_00:** outcome of that exercise is that we have 50% improvement in compute usage like just overall compute utilization for that large pre-training run which is huge for us and you know this is just a small simple prototype that I built and I think

`[48:06]` **SPEAKER_01:** like there's a lot more to be done Kwon this is incredible thank you so much for everything thank you for making physical intelligence thank you for showing us these incredible demos and honestly like the thing that gives me the most hope is that you know we have a research lab out there that is focused on giving this to the world you know about to create this Cambrian explosion of robotic startups so someone watching right now will be inspired by this and you know start playing

`[48:40]` **SPEAKER_00:** with your models and they might create a robot that touches billions of people's lives in for the good the cost of building in robotic has decreased and I think will continue to dramatically decrease and it also requires a very different kind of scrappy skill set that young startup like needs we hope to enable really an explosion of many many many different robotic use case and you know

`[49:12]` **SPEAKER_01:** always reach out to us

`[49:13]` **SPEAKER_00:** if you want to collaborate

`[49:14]` **SPEAKER_?:** thanks man thank you thank you
