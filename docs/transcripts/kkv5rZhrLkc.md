# 全文转录 · 十亿分之一:用「分步走」战略把硬科技做成 40 亿美元公司

> ▶ [YouTube](https://www.youtube.com/watch?v=kkv5rZhrLkc) &nbsp;·&nbsp; ← [返回精读 One-page](../notes/kkv5rZhrLkc.md) &nbsp;·&nbsp; BillionToOne Is Solving One of Biotech's Hardest Problems
>
> 🗣️ 说话人分离识别到 **3** 位发言者(标注为 SPEAKER_00 …)。

`[00:00]` **SPEAKER_02:** One in 11 babies born in America this year will be screened by a genetic test that didn't exist a decade ago. Can you articulate like the needle in the haystack problem that you have to solve?

`[00:12]` **SPEAKER_00:** There are 3 billion base pairs in the human genome, and a lot of the human diseases that we are detecting from mom's blood, sickle cell disease, cystic fibrosis, et cetera, it's usually only one base pair that's different, so you're looking for one base pair that's different out of billions, and that's where the Billion to One name came from.

`[00:28]` **SPEAKER_02:** The prenatal test from Billion to One is already one of the most widely used genetic tests, but that's just step one. They're also working towards solving one of the most elusive problems in medicine.

`[00:39]` **SPEAKER_01:** We are maybe less than a year away from launching our, you know, ultra-sensitive MRD test, minimal residual disease test for stage one to cancer patients.

`[00:50]` **SPEAKER_02:** And that same technology could one day be used for early stage detection so that the cancer can be caught before it ever reaches stage one.

`[00:58]` **SPEAKER_01:** Once we are there, I think technically we would have solved the, you know, holy grail of cancer detection.

`[01:05]` **SPEAKER_02:** Billion to One was built by two PhD students who started with half a lab bench and $300,000. So how did they pull it off? And what will it take to make a blood test that detects cancer early?

`[01:16]` **SPEAKER_00:** This is the story of Billion to One.

`[01:26]` **SPEAKER_02:** I met Ogezan and David way back in 2017 when they applied to YC. They've come a long way since then. I recently visited them at their lab in Union Square. I'm so excited to get to sit down with you guys today. To start with, why don't you tell everybody what Billion to One does?

`[01:45]` **SPEAKER_01:** Billion to One is a next generation molecular diagnostics company. We detect DNA in blood samples. This is important because all of our different tissues shed this DNA into the bloodstream. This includes fetus, a developing baby in mother's womb. It releases DNA into the bloodstream. And cancer as well. You know, as cancer is mutating and growing, it releases its DNA into the bloodstream. By detecting this DNA, we can develop diagnostics that have been impossible even a decade ago.

`[02:20]` **SPEAKER_02:** And all their hard work is paying off. Late last year, they took the company public at a valuation over $4 billion. Can you guys give us a sense of the scale that you guys are operating at here?

`[02:31]` **SPEAKER_01:** We are processing more than 600,000 samples. That's a lot. That's a lot. We are processing more than 600,000 tests a year. And in terms of the overall market share, we are close to 20% market share there.

`[02:43]` **SPEAKER_02:** Remarkably, the core idea behind Billion to One is the same as when they applied to YC back in 2017. They were convinced it should be possible to create a prenatal genetic test that works by sequencing fragments of fetal DNA that naturally exist in the mother's blood, and that this would someday be universally adopted. This was a radical idea at the time. Before Billion to One. I mean, it was a very ambitious idea. So we were pleased this set of studies came out. Because this was the first step to kind of an innovation to be able to develop a more

`[03:07]` **SPEAKER_02:** sophisticated method of genetic testing. There's a lot of innovation today. But I'm not sure if Billion to One is the right number to go for. Now, Billion to One is a very, very interesting method, because it's a production of DNA. And it's the process where the DNA is used, and the DNA is used for genetic tests. And in fact, they're used for a whole bunch of things. For example, we understood that most genetic abnormalities could only be detected via amnio-synthesis. An invasive procedure that is only used in high-risk pregnancies.

`[03:16]` **SPEAKER_01:** How is the key insight that enabled you guys to do this when no one else was able to do it before? that is coming from the fetus and the tumor is both very dilute and rare, right? So you might only have a few molecules among billions of other molecules. So every molecular diagnostics approach here requires, in the lab, using a process called PCR to amplify this DNA billions of fold. The problem is that this DNA amplification process can add tremendous noise, so that the small signal that you have can be lost.

`[03:50]` **SPEAKER_01:** So what we have done is to add a synthetic DNA into the patient sample that we get before any amplification happens. These synthetic DNA allow us to know how much amplification happened at different genomic locations. You know, what are the errors that are being introduced by the amplification process? So then we can remove those errors from the sequencing data, the data that we get at the end, so that we know what was in the sample to begin with. That converts a difficult biology problem

`[04:27]` **SPEAKER_01:** to almost a simple mathematical problem.

`[04:31]` **SPEAKER_02:** Let's break that down even further. Every tissue in your body sheds tiny fragments of DNA into your bloodstream. Hidden inside that mix can be a fragment from a fetal condition or a sign of cancer, but detecting it is a needle in a haystack problem. Traditional genetic tests amplify everything, including background noise, which means they can't find the needle. Billion to One has a clever trick. Before amplifying, they add known synthetic DNA molecules to the sample. Because they know exactly what they added,

`[05:03]` **SPEAKER_02:** they can see how much distortion the amplification introduced and subtract the noise using machine learning. The result is that they can spot things no other test can pick up. I want to go back to the first couple of years of the company and talk about how you went from PhD students who had a cool idea to an actual commercial test that was live and processing samples from real patients. Tell us about how you did it and how you did it so fast. Because you guys did it in two years, which is like one of the fastest

`[05:29]` **SPEAKER_02:** I've ever heard of a company doing this.

`[05:31]` **SPEAKER_00:** Ozan and I, we had met actually when we were undergrads, and then we went our kind of separate ways for our PhD studies in biology-related fields. Ozan was studying at Stanford. I was at Rice University. He basically called me up one day and he was like, hey, like, you know, I'm thinking of something. Like, you know, I'm thinking of starting a company.

`[05:47]` **SPEAKER_01:** Initially, we were looking into the cell-free DNA, which is essentially the DNA in blood, to see, you know, what conditions we can detect. And we were approaching this problem from first principles, and we were able to determine that, you know, if we could reduce the noise, we would be able to detect, you know, conditions like sickle cell disease, cystic fibrosis, you know, thalassemias, directly from a maternal blood sample. And given that, you know, sickle cell and beta thalassemia are the most common genetic disorders in the world,

`[06:21]` **SPEAKER_01:** you know, we thought that, you know, we would be able to, you know, create something that would help millions of patients. I think the question almost becomes like, why didn't someone else do this before? Why were you two the first to do that? I think sequencing developed pretty recently, right? This essentially requires this kind of inter-disciplinary approach where people who are analyzing the data and seeing kind of all the... ways in which the data can be biased, also understand the chemistry of how that data

`[06:52]` **SPEAKER_01:** is generated. People who understand chemistry tend to be not the kind of data scientists and bioinformaticians that analyze the data. We were able to, I think, bridge that gap. Billion to one is prenatal genetic testing for every expecting mother.

`[07:09]` **SPEAKER_02:** When they applied to YC, this was all just an idea. But within six months, they developed the actual test and proven its accuracy on test

`[07:17]` **SPEAKER_00:** samples. Our first lab space was very much not anything like the operation we have today. It was actually in a shared facility. We didn't even have an entire kind of lab bench to ourselves. We were sharing it with another one of our friends who was also doing a startup. It was a struggle even to get very common kind of chemical suppliers to allow us to buy things from them because they'd be like, well, do you have a bank account? Like if we send you something. And we invite you to buy something.

`[07:42]` **SPEAKER_00:** And we invite you to buy something. And we invite you to buy something.

`[07:43]` **SPEAKER_01:** The first fundraising that we have done after the fellowship was one of the most difficult things that I have done. The first $300,000 that I've raised was really, really difficult. It took six months and it was $10,000 at the time. So we were very paranoid about essentially the resources that we are able to get. It launched in June. Only person that is using the test, you know, two months later is this one physician and and who's sending like maybe one or two tests per week.

`[08:15]` **SPEAKER_02:** Wow. So two months after launch, you know, you've been working on this thing for two years. You've done incredible R&D. You've gotten approval. You finally launched the thing two months after launch. You still only have like basically one user.

`[08:24]` **SPEAKER_01:** Yes, that is correct. That was really nerve wracking.

`[08:29]` **SPEAKER_02:** Okay. So you call this emergency meeting.

`[08:30]` **SPEAKER_01:** And yeah, I told our VP of sales, I was like, look, in five months, you hired only one rep. Obviously, that is not working. I need you to hire in the next three weeks, five additional sales reps. I need them to be trained over the weekend. And I need them to be in the field on that Monday. When we talk with patients, we can convince them. When we talk with physicians, we can convince them, but we are not getting in front of them. But patients are getting in front of, you know, physicians.

`[09:03]` **SPEAKER_01:** So can we get, you know, marketing leads and essentially convince these patients to convince their doctors- To their doctors, yeah. To convince their doctors- To use this test. It worked to the extent that we were getting about one in five kits back. Our current director of inside sales, he was on the phone essentially with like each patient for 30, 45 minutes, you know, teaching the patient about our tests. You know, this is what the physician would say. This is how it is different. And that was, I think, what we needed to convince,

`[09:35]` **SPEAKER_01:** you know, one or two good sales team members to actually join us. Because they really only want to join a company if there's traction.

`[09:43]` **SPEAKER_02:** Once they cracked the sales problem, they began scaling up and eventually built this state-of-the-art lab in 2022. During our visit, we got a behind-the-scenes tour of how it all comes together in the lab.

`[09:57]` **SPEAKER_01:** This is the start of the processing. When we receive test samples, you know, we need to log them into a laboratory information management system and track the sample through the five to seven-day process that it would go through. We want to make sure that we're getting the results. We want to make sure that when you are processing thousands of samples a day, that the identity of the sample is preserved. Are those actual raw blood samples, like straight from patient over there? Yes, those are actual blood samples

`[10:25]` **SPEAKER_01:** straight from the patients. And really the amazing thing here is that this actually became the bottleneck of all of our processes. So we had to incorporate AI and computer vision to accelerate this. And then we did a complete redesign of the entire project, incorporating computer vision and AI, which was our project called Accessioning in 60 Seconds.

`[10:48]` **SPEAKER_02:** So each file takes a human 60 seconds to handle.

`[10:52]` **SPEAKER_01:** Yes. Once the information is entered into the information system, first step is actually centrifuging them, so spinning them really fast, so that the blood plasma and blood cells are separated. This cell-free DNA that we talked about is in this upper layer of plasma. We programmed these layers of DNA, we programmed these liquid-handling robots, which has an optics that can see that layer and only remove the plasma. So this is our reagent manufacturing lab where we create our own proprietary QCTs,

`[11:26]` **SPEAKER_01:** quantitative counting templates, that we add to every sample to measure the biases so that we can remove them at the end. We believe that we can expand into close to 2 million tests per year, just using this facility. That would be around, essentially, every one in three babies that would be tested with our test.

`[11:50]` **SPEAKER_02:** So I know this is standard for you, but the first time I heard that this was how it was actually done, it seemed like black magic to me, because you actually combine all the fluids into like one droplet, and then you sequence somehow 1,000 patient samples all mixed together. Yes. And then you use some computational magic to figure out which one was which.

`[12:08]` **SPEAKER_01:** Yes. So essentially, it's kind of like you are marking, marking each of their sequences with a specific sequence that belongs to that sample before you combine them. So when you look at the data, every time you see that barcode, you know that that sequence belongs to this patient.

`[12:23]` **SPEAKER_02:** So here's the end of the line, right? Like, this is the last step in the sample processing. After this, it's all computational.

`[12:29]` **SPEAKER_01:** Yes. After this, it is all computational. You know, we have laboratory directors. We have genetic counselors. Sometimes genetics is complicated. So we would sometimes even spend 20 people just discussing one sample to be able to report it well. At the same time, you know, vast majority of samples are in happy path. You know, essentially, we know what the results should be. So those get analyzed and go out automatically.

`[12:56]` **SPEAKER_02:** Today, Billion to One is not just a prenatal genetic test. The same core technology for detecting free-floating DNA also works for detecting cancer via a blood test, known as a liquid biopsy. They launched an early version of this cancer test, commercially, in 2023, proving their ability to execute in two markets simultaneously.

`[13:16]` **SPEAKER_01:** One year into the company, it is actually laid out that, you know, we would start at prenatal genetics, then go into late-stage cancers, and then go into early-stage cancers in this way.

`[13:26]` **SPEAKER_02:** And you're on step two of that right now. Yes.

`[13:28]` **SPEAKER_01:** OK. That was step two. OK. And, you know, we realized that, you know, fundamentally, there is nothing different about, you know, cell-free fetal DNA and cell-free tumor DNA. And the same technology can be added. You can apply to both of them. And that is why I think it was very important to actually select the right problem, the right minimal viable product to work on. Because if we started, I think, on the oncology side, it would have been far more difficult to achieve that initial successful commercialization that

`[13:58]` **SPEAKER_01:** gave us more resources to be able to build, you know, new tests and improve the existing tests.

`[14:04]` **SPEAKER_02:** I'm curious if you guys could share patient stories that sort of illustrate, like, what the impact of all the science means for real people.

`[14:11]` **SPEAKER_00:** So one patient case study that really stands out to me comes from our cancer products. So this was a fairly young, in their 40s, individual with metastatic colorectal cancer. And they had really kind of run out of treatment options. They were about to go into hospice. And you're not kind of shooting for a cure anymore at that point. We ended up testing this person using our Northstar Select Test. We had identified that this person was eligible for a therapy called immunotherapy based on identifying microsatellite instability in the tumor DNA

`[14:44]` **SPEAKER_00:** that was in that patient's bloodstream. And this was a little bit like a last-ditch effort, because they had already done the tumor testing. And there's no kind of indication from the tumor test that this type of therapy would work. But because of how the tumor had mis-sized into many different locations, probably what happened was the exact location of the biopsy was done, just didn't happen to have that alteration, but the other places in the cancer sites did. So this person went on to immunotherapy.

`[15:09]` **SPEAKER_00:** And it did really remarkably well. Sometimes doctors describe the patient response as the cancer melting away. So the patient's doing very well. And to this day, the doctor is really impressed with our results and now starting to actually send us blood tests from pretty much all of his cancer patients.

`[15:25]` **SPEAKER_02:** MARK MIRCHANDANI- Wow. You guys are actively hiring. Can you talk about some of the other unique or interesting aspects of the Billing to One team?

`[15:32]` **SPEAKER_00:** DR. CHRISTOPHER BOUCHARDT- One of the ways we actually rehire scientists is we say, we're not looking to build an interdisciplinary team here. We're actually looking for interdisciplinary people.

`[15:40]` **SPEAKER_01:** MARK MIRCHANDANI- We have found that having that iterative cycle within one scientist actually accelerates the work that they do by an order of magnitude. We actually have very small research teams. It is essentially principal investigators, like a scientist who is interdisciplinary, who has a small team of two or three research associates. And they all directly report to David and me. And they own end-to-end development of an entire product. And they can do that because, again, their iteration cycle

`[16:15]` **SPEAKER_01:** is so fast, and they are not blocked by any bureaucracy because they report to us. So we can essentially unblock them. And every week, we spend a lot of our time with those R&D scientists because it almost creates this interesting structure where we have many startups within the larger company. Each one owns a product that makes it better and better. I want to end by talking about the future.

`[16:41]` **SPEAKER_02:** So as early as 2018, you guys had kind of this three-step plan for the companies, like prenatal testing, late-stage cancer, and then early-stage cancer. It actually just occurred to me, is this similar to the Tesla super secret plan, the three-step plan to go from like the Roadster to the like, huddle three? Have you guys ever thought about that analogy?

`[16:59]` **SPEAKER_01:** It has similarities. I think maybe the primary difference here is that being in health care, we needed to make, like, every test that we build accessible and affordable to everyone. But from the perspective of going into larger and larger markets, you know, it is very much the same approach that we have taken here.

`[17:20]` **SPEAKER_02:** You began with the least capital-intensive product. You got that live and commercial. Then you took the resources from that and were able to launch a more expensive, more difficult product in a larger market. And that's where you guys are at now. This is like, you're in, like, step two, which is late-stage cancer. Can you talk about what's step three?

`[17:38]` **SPEAKER_01:** Step two? Step three is essentially using the same technology for patients who are diagnosed with stage one, two cancers. And then, you know, they undergo what is considered, you know, curative intense surgery. The problem is that in about 20% of these patients, actually, there is a microscopic residue remaining. And they cannot be detected by scans. With our technology, we believe that we can detect this microscopic level of remnant tumor DNA. There is actually a step even four. If you can detect a microscopic level of DNA

`[18:19]` **SPEAKER_01:** and be able to say that that is actually cancer, that is the same really technical problem as being able to detect those in healthy patients or, you know, general population. So that is the kind of eventual goal of cancer screening. If we can, you know, screen it. If we can screen everyone once a year and be able to conclusively say that, you know, this small group of people have early-stage cancer, that would be amazing because, you know, those tumors can often be removed before, you know,

`[18:52]` **SPEAKER_01:** it spreads before it becomes too late.

`[18:54]` **SPEAKER_02:** This is one of these, like, holy grail scientific achievements that the industry has been chasing.

`[18:59]` **SPEAKER_01:** Why has no one else been able to do it before? Being resource limited is sometimes very helpful, right? If you wanted to solve, early detection from the very beginning without having this step-by-step approach, you would have to raise more than a billion dollars, you know, without generating a single dollar of revenue. And as first-time founders, we knew that, you know, we could never do that. I would be very proud of what we, you know, what we achieve, even if we just solved the biggest prenatal problems.

`[19:31]` **SPEAKER_01:** But the great thing about our technology is that it does allow us to have this, you know, step-by-step, approach to being able to get to a place where we can solve a problem for, you know, millions of cancer patients and, you know, potentially make the biggest dent in cancer that, you know, really has happened in the last hundred years. We have a saying that, you know, pressure is a privilege. People who are coming here because they want to take on a challenge, you know, changing healthcare is difficult.

`[20:03]` **SPEAKER_01:** Trying to change healthcare, you know, while also, you know, growing this fast, you know, while being profitable is even more difficult. So we make it very clear to, you know, everyone that, you know, it is probably going to be, you know, one of the most difficult things that you are ever going to do if you join our company, but you are going to be extremely proud of what you are going to achieve here. And now that, you know, we have gone public, these employees, they could easily retire,

`[20:31]` **SPEAKER_01:** but they are not retiring, right? And I think that shows that, you know, they are really here because of the growth and because of the challenge and because, you know, they love what they do.
