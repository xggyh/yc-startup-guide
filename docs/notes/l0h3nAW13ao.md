# 从想法到 6.5 亿美元退出:AI 创业的实战心法 / From Idea to $650M Exit: Lessons in Building AI Startups

📄 **[点此查看全文转录 / Full transcript »](../transcripts/l0h3nAW13ao.md)**

> **来源**: [From Idea to $650M Exit: Lessons in Building AI Startups](https://www.youtube.com/watch?v=l0h3nAW13ao) · Y Combinator · 2025-10-28 · 时长 39:25
> **讲者**: Jake Heller(Casetext 联合创始人兼 CEO,AI 法律助手 CoCounsel;2023 年被 Thomson Reuters 以 6.5 亿美元现金收购;录制于 2025-06-17 AI Startup School)
> **一句话定位**: 一位真正把 AI 应用做到大额退出的创始人,系统讲清"选什么想法 → 如何造出可靠(而非只是 demo)的 AI 产品 → 如何定价与卖出去"三件事;对要做 AI Agent 创业、正卡在"demo 很酷但不敢上生产"的工程师尤其对症。

## 🎯 TL;DR(中文核心要点)
- **选想法有了捷径:看"人们正花钱雇别人做什么"**。以前要靠 "make something people want" 反复试错,现在直接盯着别人已经付费购买的人工任务(客服、保险理赔、律师、私教、行政助理),那就是被验证过的需求。
- **三类机会:辅助(assist)/ 替代(replace)/ 做以前不可能的事(the unthinkable)**。第三类是全新增量——比如让上千个 Gemini 实例读完一家律所几亿份文档,这在人力时代根本不敢想。
- **TAM 涨了 10–1000 倍**:过去按"座位数 × 每月 20 美元"算市场;现在天花板是"这些岗位的全部薪资总和",一个专业岗位客户可能愿意每月付 5000–20000 美元。
- **造产品的方法极其朴素却几乎没人做**:先像卧底一样搞清"这个行业的专家到底怎么干活",把任务拆成步骤;每一步要么是一个 prompt,要么就是老老实实的 Python 代码(能用确定性代码就别用 prompt,token 又慢又贵);确定性流程做成 workflow,依情况而变的才做成 agentic。
- **真正的护城河是 evals,不是模型**。demo 能做到 60–70% 准确、能骗到 VC 和试点合同,但生产环境会崩。把任务设计成可客观打分(true/false、0–7 分),用 PromptFoo 之类框架,从十几个测试做到 100 个甚至 1000 个,盯着单个 prompt "不眠不休磨两周",能从 60% 提到 97%。
- **产品质量 > 营销**。他做了 10 年,产品平庸时招再牛的销售也只是"OK";产品真正惊艳后,口碑和媒体自己找上门,老销售变成"接单员"。别信"营销比产品重要"的 VC。
- **按价值定价,同时问客户想怎么付**。别再卖 20 美元/月的 SaaS,而要卖"每份合同 500 美元"的服务;但客户可能宁愿要可预测的按座位年费(如 6000 美元/座)也不要按用量——直接问他们。
- **警惕"试点收入(PRR)"幻觉,并投入交付**。很多号称 10M ARR 的公司其实是不会转化的试点收入,一场"大灭绝"在酝酿;产品不只是屏幕上的像素,还包括培训、客户成功、"前线部署工程师(forward-deployed engineers)"贴身让客户真正用起来。

## 🧭 适合谁 / 什么时候看
- 你是 AI/Agent 工程师,能做出很酷的 demo,但不知道怎么把它变成客户敢在真实业务里依赖的可靠产品。
- 你还在纠结做哪个方向、担心"只是个套壳(GPT wrapper)"、担心竞争对手。
- 你要给 AI 产品定价、做 B 端销售,想知道怎么跨过大企业的"信任鸿沟"、避免试点收入陷阱。
- 想听一个真实的大额退出案例复盘(而非泛泛而谈的方法论),39 分钟含 Q&A,信息密度高。

## 📝 分段精读

### 1. 开场:6.5 亿退出与三大主题 / How We Built a $650M AI Company `[00:00–01:00]`
**要点(中文)**: Jake 自我介绍:程序员出身,做过律师,2013 年创办 Casetext。因长期深耕 NLP/LLM,2022 年夏就拿到 GPT-4 早期访问——当时公司已有 2000 万美元营收、约 100 人,却"停下手里一切"去 all-in 造了 CoCounsel(第一个、他认为至今最好的律师 AI 助手),两年后被 Thomson Reuters 以 6.5 亿美元现金收购。全篇围绕三个大问题:选什么想法、怎么造、怎么卖(最后这点最常被忽视)。
> 🗣️ "We were like $20 million in revenue. We were doing great. I had like 100 people, and we stopped everything that we were doing and said, we're going to build something totally new... based on this new technology." —— Jake Heller
> 译:我们当时约有 2000 万美元营收,发展得很好,大概 100 号人;但我们停下了手上正在做的一切,说:我们要基于这项新技术,做一个全新的东西。

### 2. AI 时代如何选想法:盯住"别人花钱雇人做的事" / Picking the Right Idea in the AI Era `[01:00–04:45]`
**要点(中文)**: YC 的老话是 "make something people want",难点在于"猜不准人们想要什么"。Jake 说这事现在简单多了:人们想要什么?看他们现在正付钱请别人做什么——客服、保险理赔、律师助理,或生活中的私教、行政助理。这些都是被真金白银验证过的需求。选好领域后,能用 LLM 解决就用 LLM,物理世界的活儿留给机器人。核心心法:不要凭空想需求,去"逆向"已经存在的付费人工任务。
> 🗣️ "the problem of choosing what people want just got a lot easier because now you have to look what are people paying other people to do" —— Jake Heller
> 译:选"人们想要什么"这个难题变简单多了,因为你现在只要去看:人们正花钱请别人做什么。

### 3. 三类机会 + 千倍市场 + 更美好的未来 / Three Types: Assist, Replace, or Do the Unthinkable `[04:45–09:25]`
**要点(中文)**: 三类切入点:(1)**辅助**——帮专业人士更快完成任务(CoCounsel 帮律师读文档、做研究、改合同);(2)**替代**——干脆变成一家"由 AI 驱动的律所/会计所";(3)**做以前不可能的事**——律所有上亿份文档,人力时代根本不敢逐份阅读归类,如今可让上千个模型实例全读一遍,"以前不可想,现在可想了"。更重要的是 TAM 逻辑变了:过去 = 座位数 × 每月 20 美元;现在 = 这些岗位的全部薪资总和,一个客户可能付每月 5000–20000 美元,市场放大 10–100–1000 倍。他强调这不 dystopian 而是美好的:既解锁我们今天想象不到的未来(类比"点灯人"这种被淘汰的旧职业),也把过去只有富人才买得起的服务(如法律,85% 低收入者用不起)民主化。
> 🗣️ "the actual amount of money that we already know people and companies are willing to spend is the combined salaries of all the people they're currently paying to do the job and that number is like a thousand x bigger" —— Jake Heller
> 译:我们已经确知人和公司愿意花的钱,是他们现在雇人做这件事所付的全部薪资总和——这个数字大约要大上一千倍。
> 🗣️ "the previously unthinkable is now thinkable" —— Jake Heller
> 译:以前不可想的事,现在可想了。
> 🗣️ "everybody should get the world's best financial assistant everyone in the world should get the best executive or personal assistant" —— Jake Heller
> 译:每个人都应拥有全世界最好的理财助理,每个人都应拥有最好的行政或私人助理。

### 4. 如何造出可靠(而非只是 demo)的 AI 产品 / How to Build Reliable AI Products `[09:25–16:30]`
**要点(中文)**: 方法听起来平淡无奇,但几乎没人真做。第一步:搞清"这个行业的专家到底怎么干活",要极其具体、亲身或访谈得来,别拍脑袋(Jake 自己是律师,公司 30–40% 员工含程序员都是律师);不然就去当"卧底"或找一个懂行的联合创始人。第二步:问"最好的人如果有无限时间、无限资源(比如上千个能并行的 AI)会怎么做",然后倒推出具体步骤(他们两年半前就照此做出了法律版 deep research:澄清问题→做研究计划→执行几十次检索→逐条精读筛选→记笔记→成文→末尾自检引用)。第三步:落到代码——大多数步骤会变成一个或多个 prompt(因为它们本需人类级智能);但**能用确定性代码/数学计算搞定就别用 prompt,token 又慢又贵**。第四步:确定性、每次都走同样步骤的,做成简单 **workflow**(纯 Python 函数串起来,"不需要什么 LangChain");依情况而变的才做成更难保证质量的 **agentic**。
> 🗣️ "how would the best person in that field do this if they have like unlimited time and unlimited resources like a thousand ais that can all work... simultaneously" —— Jake Heller
> 译:如果这个领域最厉害的人拥有无限时间、无限资源(比如上千个能同时工作的 AI),他会怎么做这件事?
> 🗣️ "if you can get away with it not being a prompt, if it's like deterministic or it's like a math calculation or something like that, that's better. Prompts are slow and expensive." —— Jake Heller
> 译:如果某一步能不用 prompt(比如是确定性的、或是个数学计算),那更好。prompt 又慢又贵。
> 🗣️ "you don't need to have, frankly, like fucking Lang chain or whatever. Just Python code." —— Jake Heller
> 译:说白了你根本不需要什么 LangChain 之类的东西,普通 Python 代码就行。

### 5. Evals 才是真正的护城河 / The Importance of Evals and Testing `[16:30–24:20]`
**要点(中文)**: 造出来不难,难在"做对"。demo 能到 60–70% 准确、足以拿融资、签下前几个试点,但生产环境会崩,所有兴奋随之瓦解——因为 LLM 像人一样会"没喝咖啡就出错"。解法核心是 evals,而这恰恰是大多数人不做的。做法:从领域专家定义"什么叫做得好"(整体任务与每个子任务都要);尽量把答案设计成可客观打分(true/false、0–7 分),用 PromptFoo 之类开源框架跑;从十几个测试做起,做到 50、100,留 holdout set 防止过拟合。关键是韧性——愿意"不眠不休磨两周单个 prompt",多数人 60% 就放弃、61% 又一批放弃,但坚持下去能到 97%,剩下 3% 是可解释的判断题。上线 beta 后,客户投诉、"客户会用你的 app 干最蠢的事"都变成新测试;换新模型继续跑,单词的增删有时就能提升 1%,在法律/金融/医疗这类领域意义重大。只要做到"搞懂专家怎么干 + 每步都 eval"这两件事,就已胜过市面上 90% 的产品。
> 🗣️ "the biggest qualification for success here is whether you or whoever is working on the prompts in your company is willing to spend two weeks sleeplessly working on a single prompt to try to pass these evals" —— Jake Heller
> 译:这里最大的成功资格,就是你(或你公司里写 prompt 的人)是否愿意为通过这些 eval,不眠不休地在单个 prompt 上磨两周。
> 🗣️ "if you spend like solid two weeks prompting and adding more evals... you're gonna get to something that passes like 97% of the time and the 3% is kind of explainable" —— Jake Heller
> 译:如果你实打实地花两周,不断改 prompt、加 eval……你会做出能通过 97% 的东西,而剩下 3% 是可解释的。
> 🗣️ "most people never eval, and they never take the time to figure out how professionals really do the job" —— Jake Heller
> 译:大多数人从不做 eval,也从不花时间去搞清专业人士真正是怎么干活的。

### 6. 产品质量胜过营销;如何定价与建立信任 / Product Beats Hype; Pricing & Trust `[24:20–29:30]`
**要点(中文)**: 反主流观点:很多 VC 和董事会说"营销和销售最重要,产品没那么重要",Jake 直言"bullshit"。他做了 10 年,产品平庸时换了几任很牛的销售也只是"OK";产品真正惊艳后,口碑与媒体自己找上门(免费营销),老销售变成"接单员"。当然仍要让世界知道你(树倒在无人的林子里没意义)。定价三条:(1)**你卖的可能不再是传统软件**,按价值定价——别人 1000 美元/份的合同审查,你可做全套服务收 500 美元/份,而不是 20 美元/月;(2)但**问客户想怎么付**——他们发现客户宁愿要可预测的 6000 美元/座年费,也不要更便宜的按用量;(3)跨过**信任鸿沟**:大公司想试 AI 但不敢,可用"头对头对比"建立信任——"留着你的律所/会计,同时并行用我们的,直接比速度、比质量、比结果差异"。
> 🗣️ "the most important thing you could do for marketing and sales is to build a fucking amazing product and then making sure the world knows about it somehow" —— Jake Heller
> 译:你为营销和销售能做的最重要的事,就是造出一个惊艳到爆的产品,然后想办法让世界知道它。
> 🗣️ "$20 per month versus $500 per contract. We're talking about extreme step ups in price. Price it according to the value you're selling it." —— Jake Heller
> 译:每月 20 美元 对 每份合同 500 美元——这是价格的极端跃升。要按你所卖的价值来定价。
> 🗣️ "Some really smart companies are doing head-to-head comparisons. Keep your law firm. And then use our thing side-by-side and then compare." —— Jake Heller
> 译:一些很聪明的公司在做头对头对比:留着你的律所,同时并行用我们的东西,然后比较。

### 7. 交付才算完:警惕试点收入,产品不只是像素 / Product Isn't Just Pixels `[29:30–33:00]`
**要点(中文)**: 卖出去不等于成交结束,试点开始更不等于。他作为天使投资人看到很多号称 10M ARR 的公司,扒开一看是付了半年高价的试点,大量根本不会转化——他戏称这是 "PRR(pilot recurring revenue)",一场"大灭绝"在酝酿,即使报表数字很漂亮也危险。创始人的重要工作是让每个用户真正理解并用起来:认真培训、有意识地推进上线、精心 onboarding,必要时派人贴身坐在客户旁边——即 Satya 当天提到的"前线部署工程师(forward-deployed engineers)"。核心信念:产品不只是屏幕上的像素,还包括客户支持、客户成功、创始人的人际互动和培训,投入这些的公司会击败只有"最好像素"的对手。
> 🗣️ "instead of ARR, it's like PRR, like pilot recurring revenue... A big part of your job as a founder... is making sure that everybody who uses the product really understands it." —— Jake Heller
> 译:那不是 ARR,更像 PRR——试点循环收入……而你作为创始人很重要的一部分工作,是确保每个使用产品的人真正理解它。
> 🗣️ "your product isn't just the pixels on the screen... It's the human interactions with your support, customer success with the founder. It's training. It's everything around it." —— Jake Heller
> 译:你的产品不只是屏幕上的像素……它还是与你的客服、客户成功、创始人之间的人际互动,是培训,是围绕它的一切。

### 8. 创始人真正该聚焦什么 & Q&A / What Founders Should Focus On & Q&A `[33:00–39:25]`
**要点(中文)**: 被问及不同阶段的重心,Jake 半开玩笑地反复回答:种子轮、A 轮、B 轮、C 轮——每一轮都该"聚焦做出能拿到 PMF 的好产品"。他坦承自己犯过错:把 HR、财务、融资、企业文化当成"目的本身"去追,而非服务于"做出有 PMF 的产品"这个唯一目的。Q&A 要点:(1)**别管竞争对手**——市场以万亿计,没有单一赢家;等你真开始造,会惊讶对手做得多烂;(2)**选市场**看"哪些岗位已经被外包(尤其到别国)"——愿意外包的就是 AI 好目标,而 Pixar 讲故事这种"身份认同"部分别碰;(3)**新增量任务(如读几十万份文档)怎么定价**——先从价值出发,能帮客户省 1 亿或原本要花 500 万,就谈拿其中 10–20%;(4)**如何不沦为套壳**——最快的答案:"直接造,一造你就知道它有多难",做完你会拥有别人造不出的东西,因为你花了两年只干这一件事。
> 🗣️ "at the seed stage, focus on making a great product that gets product market fit. And then at the series A stage, focus on making a great product that gets product market fit." —— Jake Heller
> 译:种子轮,聚焦做出能拿到产品市场契合的好产品;到了 A 轮,还是聚焦做出能拿到产品市场契合的好产品。
> 🗣️ "Just build it, and as soon as you build it, you'll see how fucking hard it was... you're gonna find that you built something that nobody else can build because you spent, like, two years just doing nothing but that" —— Jake Heller
> 译:直接造就是了,一造你就会发现它有多难……你会发现自己做出了别人造不出的东西,因为你花了整整两年只做这一件事。
> 🗣️ "what are the kinds of roles that people are currently outsourcing, say, to another country? If it's something that they're willing to do that for, then that's probably a pretty good target for what AI could take over." —— Jake Heller
> 译:人们现在把哪些岗位外包(比如外包到别的国家)?如果他们愿意这样外包,那这大概就是 AI 可以接管的好目标。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **用"付费人工任务"清单选方向**:列出目标行业里人们正花钱雇人做的具体任务,标注类别(辅助/替代/做不可能之事)与"薪资总和 TAM",挑一个又大、又已被外包、你能拿到内部信息的切入。
- [ ] **先做"专家工作流田野调查"**:亲自当卧底或深访 5–10 位从业专家,把"最好的人怎么做这件事"拆成明确步骤,写下来,别拍脑袋。
- [ ] **按"prompt vs 代码"给每一步分类**:能确定性/数学计算解决的用 Python,只有需要人类级智能的才做成 prompt;确定性全流程做成 workflow,依情况而变的才上 agentic。
- [ ] **第一天就搭 eval 流水线**:把关键判断设计成可客观打分(true/false、0–7),用 PromptFoo 之类框架,从十几个测试起步做到 100+,留 holdout,把"磨一个 prompt 两周从 60% 到 97%"当成核心工作而非杂活。
- [ ] **把客户投诉与"蠢用法"变成回归测试**:上线 beta 明确告知"尚未完美",系统性收集真实失败样例并加进 eval;新模型一发布就用你的 eval 集重跑对比。
- [ ] **按价值定价 + 直接问付费偏好**:设计"每单/每任务/每座位"等高于 SaaS 的定价,并当面问客户想怎么付;用"头对头对比/试点研究"跨越信任鸿沟。
- [ ] **区分 ARR 与 PRR 并投资交付**:盯紧试点→付费的真实转化率,配置 onboarding、培训与"前线部署工程师",确保客户真的用起来而不只是签了试点。

## 🔑 关键术语 / 概念
- **Assist / Replace / Do the Unthinkable(辅助 / 替代 / 做以前不可能的事)** — 三类 AI 创业切入点;第三类是人力时代因成本不可行、如今 AI 让其成为可能的全新增量任务。
- **TAM = combined salaries(以薪资总和为天花板的市场)** — 不再按"座位 × 月费"估算,而按"目标岗位全部薪资总和"估算,可比传统 SaaS 大 10–1000 倍。
- **Workflow vs. Agentic(固定工作流 vs 智能体)** — 每次都走同样步骤的确定性任务做成简单 workflow(纯代码串联);随情况而变的才做成更难保证质量的 agentic。
- **Evals(评估集)** — 为整体任务与每个子任务定义"什么叫做得好",尽量设计成可客观打分,用框架自动化跑;是把 demo 变成生产级产品的关键护城河。
- **PromptFoo** — 讲者偏好的开源命令行 eval 框架,可对同一组测试快速比较不同 prompt/模型的表现。
- **Holdout set(留出集)** — 写 prompt 时不看的一批测试,用于检验是否只是对 eval 过拟合。
- **PRR(Pilot Recurring Revenue,试点循环收入)** — 讲者造词,讽刺很多 AI 公司把不会转化的试点收入包装成 ARR,面临"大灭绝"风险。
- **Forward-deployed engineer(前线部署工程师)** — 贴身坐在客户旁、不惜代价让产品在客户处真正跑通的工程师角色;当天由 Satya 提及。
- **GPT wrapper(套壳)** — 常见质疑;讲者回应:真正造出来会发现数据集成、校验、prompt 微调、选模型等无数细节,构成难以复制的壁垒。

## 🔖 高价值金句时间戳
- `[04:08]` "now you have to look what are people paying other people to do" — 一句话给出 AI 时代的选题方法论:逆向已被付费验证的人工任务。
- `[06:27]` "that number is like a thousand x bigger" — 为什么 AI 应用的市场比传统 SaaS 大几个数量级:天花板从月费变成薪资总和。
- `[13:39]` "if you can get away with it not being a prompt... that's better. Prompts are slow and expensive." — 反"什么都塞给 LLM"的工程纪律:能用确定性代码就别用 prompt。
- `[15:23]` "The hard part, frankly, isn't building it. The hard part is getting it right." — 点破 AI 产品的真痛点:从 demo 到可靠是两回事。
- `[20:11]` "willing to spend two weeks sleeplessly working on a single prompt to try to pass these evals" — 定义了做出可靠 AI 的核心资格:对单个 prompt 的极致韧性。
- `[25:16]` "the most important thing you could do for marketing and sales is to build a fucking amazing product" — 反 VC 主流叙事:产品质量远比早期投资人说的更重要。
- `[28:45]` "there's going to be a mass extinction event as a lot of pilot revenue" — 给高 ARR 数字泼冷水:警惕不会转化的试点收入(PRR)。
- `[39:14]` "you built something that nobody else can build because you spent, like, two years just doing nothing but that" — 破"套壳"焦虑:壁垒来自两年深耕堆出的无数细节。
