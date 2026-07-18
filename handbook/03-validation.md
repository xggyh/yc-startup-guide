# 第 3 章 · 验证需求与和用户对话 / Validation & Talking to Users

> 有了方向之后,最危险的不是"点子不够好",而是"你以为验证过了,其实只验证了自己的幻想"。这一章讲怎么用真实动作(而非客套话)去检验需求、怎么亲自和用户对话、怎么区分"验证问题"与"过早押注方案",以及怎么读懂早期信号。对 AI Agent 创始人尤其关键:模型让你几天就能做出一个能跑的 demo,构建成本趋近于零,于是"做出来"不再是瓶颈——"确认有人真的需要它、并愿意为它付出代价"才是。越是能快速造东西,越容易骗自己;这一章就是那面镜子。

## 核心原则 / Core Principles

### 只信真实动作,不信客套话 / Behavior over words

人几乎总会对你礼貌,尤其是当面。"听起来不错""我会用的""这很有意思"——这些话的信息量接近于零。真正的验证只看真实动作:他点没点那个链接?注没注册?跑没跑一次真实任务?愿不愿意为它挤出自己的时间或预算?PostHog 早期做"销售辖区管理"产品,15 个销售负责人口头都说要用,发了注册链接后 14 个连点都没点——这是没读《The Mom Test》的经典代价。更进一层:别只听用户"说"的问题,要去现场看他们"做"的事。Meesho 第一版只访谈卖家、从没访谈消费者,做出"比商场差、比电商也差"的两头不讨好产品;Groww 则总结出"多数时候你不会照着客户直接要的去做,而是读弦外之音"。常见误区是把"访谈里收集到的热情"当成需求信号,而热情是最不可靠的信号。

> 🗣️ "send them the link to create an account of the 15, 14 of them didn't even click the link, one clicked the link and then didn't create an account." —— James Hawkins / PostHog(From Pivot Hell To $1.4 Billion Unicorn)
> 译:我们把注册链接发给那 15 个人——14 个连点都没点,1 个点了却没注册。

> 🗣️ "most of the time, like you would not build what customer is directly asking, but you read between the lines." —— Lalit Keshre / Groww
> 译:多数时候你不会照着客户直接要的去做,而是去读他们的弦外之音。

**🤖 对 AI Agent 创始人**:别用"你会用这个 Agent 吗"这种问句做验证——把 demo 塞到他手里,量他有没有真的把一个真实任务交给它、有没有第二天回来再用、有没有把它接进自己的工作流。Agent 尤其容易"演示时惊艳、日常里不用",所以要盯留存和真实调用,而不是访谈里的赞美。

### 早收真钱:付费意愿才是最尖锐的检验 / Charge early — willingness to pay is the sharpest test

早期收费的目的从来不是营收,而是反馈。免费用户会用礼貌敷衍你,付了钱的用户会用愤怒告诉你真相——一个付了大钱还生气的客户,比一个不肯付钱的路人有价值得多。Giga(GigaML)的创始人把这条推到极致:立项的唯一准绳不是点子好坏、也不是市场大小,而是"有没有人愿意为它付真钱";他们做新功能前会先给客户报价、拿到付费承诺再动手。"付费"不必只是钱——如果问题足够重要,人们会用钱或时间来付;两样都不肯付,你多半在解决一个假问题。Groww 的做法是把创业风险刻意收敛到"只剩一个问号"(对他们是变现),其余全部先验证掉。

> 🗣️ "The goal here isn't revenue. It's feedback. And paying customers give sharper feedback than free users ever will." —— Ankit Gupta / How To Get Your First Users
> 译:这里的目标不是营收,而是反馈;而付费客户给出的反馈,永远比免费用户更尖锐。

> 🗣️ "If it's an important enough problem, people would pay. Either with money or with time. ... Otherwise, like, you're just solving a fake problem." —— Varun Vummadi / Giga
> 译:如果问题足够重要,人们就会付费——要么付钱,要么付时间;否则你只是在解决一个假问题。

**🤖 对 AI Agent 创始人**:在动手做下一个 Agent 能力前,先向目标客户报出预估价格、拿到一纸付费承诺(或一个明确的付费试点),把"是否有人愿付真钱"当作唯一的立项门槛。哪怕是很小的金额或一次带 KPI 的付费 pilot,也能把"礼貌的兴趣"和"真实的需求"一刀切开。

### 亲自访谈,谦逊如人类学家,并选"好读"的对的人 / Interview users yourself — like an anthropologist, and pick readable people

验证不能外包,创始人必须亲自泡在用户里。Legora 三个联创都不是律师,入行第一件事就是访谈 100 位律师——用"约午餐 + 提议按对方小时费付钱"的方式接触(结果没人真收),把外行的天真发问变成产品洞察。方法上要"像一个发现了隐秘文明的人类学家":他们怎么决策?为什么会做出"信任你"这个奇怪选择?Zepto 两个 17 岁创始人被 COVID 关在房里,反而屏蔽掉 VC、博客、行业噪音,只剩"我们和门口那个不下单的邻居"——客户不满意时,你无处可藏。同样重要的是选对访谈对象:PostHog 特意避开"信噪比差"的销售负责人,转去服务工程师、客服这类"说的和做的接近"的人,以此从创业方程里消掉一个变量;YC 合伙人则强调,选对细分市场不如对具体买家做"资格审查"(qualification)——只要这个人被授权拍板、有动机、愿意在产品成型前就用你。别把"技术上要做半年"当成躲进车库、不见客户的借口,用最糙的版本先把自己变成用户、先接触客户。

> 🗣️ "I interviewed 100 lawyers ... I texted them asking if we could have lunch, and I would pay their hourly rate." —— Max Junestrand / Legora
> 译:我访谈了 100 位律师……在 LinkedIn 上发消息约他们吃午饭,并说我按他们的小时费付钱。

> 🗣️ "we were able to just create this insulated environment where there was only us and the customer, and then there was nowhere to hide." —— Adit Palicha / Zepto
> 译:我们造出一个隔绝的环境,里面只有我们和客户——于是无处可藏。

**🤖 对 AI Agent 创始人**:把前 20–50 个目标用户列成一张"访谈搜索清单",亲自约、亲自看他们和 Agent 的真实对话记录,而不是投广告或做大众落地页——找首批用户是搜索问题,不是说服问题。优先选"好读、被授权拍板、有燃眉之急"的人(prosumer、某个具体岗位、渴望用 AI 的机构),哪怕产品还很糙,先住进他们的工作流里学他们真正的卡点。

### 验证的是问题,不是你的第一个方案 / Validate the problem, stay uncommitted to your first solution

这是"验证 vs 过早押注(validation vs committing)"的核心。你应该对**问题**极度刚性、对**方案**极度弹性:锁死一个不变的用户问题当使命,把"用哪种交互、哪种模型、哪种商业模式"都当作可随时替换的方案。Meesho 十一年做到"版本五",从蹭 WhatsApp 到帮人开店、方案全换,但"让全印度人上网买卖"的使命从未变;idea 不行就 3 个月证伪砍掉,而不是耗一两年。PostHog 六个月里平均每 5–6 周试一个想法,好点子是"做出来找到的,不是坐等灵感"。Cursor 则给每个方向设"证据止损线":CAD copilot、加密通讯做了半年、基本零用户就果断砍——选 CAD 的理由不过是"觉得它冷门不竞争"这种"扶手椅 MBA"式推理。判断该不该 pivot 有两个先行信号:一是"你自己已经不再相信它能成",二是"用户到底有多看重它"(去访谈,看是否有两个人对你产品的说法一致);而真要转身,手里最好备**一组**候选点子,而非孤注一掷。

> 🗣️ "be very rigid with your problem and be very flexible with your solution." —— Vidit Aatrey / Meesho
> 译:对你的问题极度刚性,对你的解决方案极度灵活。

> 🗣️ "The actual leading indicator that maybe you should pivot is you just stop believing that what you're working on is going to work out." —— Pete Koomen / YC Office Hours
> 译:真正提示你该 pivot 的先行指标,是你自己已经不再相信手头这件事能成了。

**🤖 对 AI Agent 创始人**:把第一版做成"最小可进化产品"(minimum evolvable product)而非一次性押注——prompt、工具、工作流可插拔,架构预留快速改造空间。把你的 Agent 抽象成"一份可迭代的 policy / markdown + 一个业务 KPI",这样即便方案要换,你验证到的"问题 + KPI 曲线"仍然成立;别爱上你的第一版 Agent,爱上你在解决的那个问题。

### 读懂真信号:怕的是"无所谓",不是被恨 / Read the real signals — indifference is death, love-or-hate is life

早期最致命的反馈不是"我恨它",而是"无所谓"。Groww 的产品验收标准是:每上线一个功能,应该同时收到"太棒了我爱死了"和"太糟糕了我恨它"两类反馈——两者都 OK,唯独"不爱不恨"说明产品不值得存在。同样,规模不等于 PMF:Meesho 曾有几十万商家在用却不肯付费、都是浅层用户,真正的 PMF 藏在一小撮"每天用 15–20 次、一边骂缺功能一边离不开"的 power users 身上;真 PMF 的样子是"连续 10 个月零营销、每月翻倍、极高留存"。Zepto 用"客户是从你手里抢产品,而不是你硬往他喉咙里塞"来描述这种手感;Legora 则说 PMF 像"有无限的需求、一断服务客户就来电话"。关键是:在你亲眼见到之前,你永远不知道 PMF 长什么样——所以别用注册量、demo 好评这类虚荣指标自欺,要盯重度使用频次、留存、自然口碑和主动付费。

> 🗣️ "some people should say, Oh, this is just awesome. I love it. Or they should say, this is terrible. I hate it. Right? Both of these are okay. If it is don't care, that is the problem." —— Lalit Keshre / Groww
> 译:有人该说"太棒了我爱死了",有人该说"太糟糕了我恨它"——这两种都没问题;真正的问题是"无所谓"。

> 🗣️ "unless you see product market fit you never know what product market fit is." —— Vidit Aatrey / Meesho
> 译:在你真正见到 PMF 之前,你永远不知道 PMF 是什么。

**🤖 对 AI Agent 创始人**:给每个新能力设一条发布验收线,主动去量"爱它 / 恨它 / 无所谓"的比例,大量落在"无所谓"就砍掉重做。找出把 Agent 当刚需、每天反复调用、一断就抱怨的那撮 power users,把产品死磕到这撮人身上;广泛但浅的"很多人试了一次"不是 PMF。

### 别用观点代替验证 / Don't substitute opinion for validation

创业者最容易犯的错,是把一个漂亮的观点当成已被验证的事实。真正该做的是找到能**证伪**你假设的因果机制,而不是拍脑袋站队。Jordan Fisher(Standard AI / 现于 Anthropic)提醒:"AI 原生新产品 vs 老产品加持分发""团队会不会更小"这类问题往往因垂直领域而异,没有普适答案,你要去找出能验证假设的因果机制。Razorpay 的 Harshil 给了一条极实用的判据:如果"难在卖给客户",那是真问题、该撤;如果只是"难在合规、冷启动、技术",那不是问题,反而是护城河——他们撑住的信念不来自融资热度,而来自"见的每一个客户都说:我有这个问题、没人在解决"。而 YC 合伙人 Gustaf 的观察一针见血:"我有个伟大点子"这种话,通常不会从真正拥有伟大点子的创始人嘴里说出来——因为伟大是被客户验证出来的,不是被自己宣布出来的。

> 🗣️ "Don't just have an opinion. Like, figure out the causal mechanisms that allow you to validate your hypothesis." —— Jordan Fisher / Ask These Questions Before Starting An AI Startup
> 译:别只有一个观点。要去找出那些能让你验证自己假设的因果机制。

> 🗣️ "'I have a great idea' is not something that founders would have great ideas say generally." —— Gustaf Alströmer / YC Office Hours
> 译:"我有个伟大的点子"这种话,通常不会从那些真正拥有伟大点子的创始人嘴里说出来。

**🤖 对 AI Agent 创始人**:把"AI 能做 X 所以用户会要 X"当成待验证的假设,而不是结论。对每个核心押注写下"什么样的真实动作/数据会证明我错",再去主动收集它;当你发现"客户告诉你行,而所有行家都说不行"时(Zepto 正是如此),优先信客户的脚投票。最后记住 YC 口号"build something people want"要往深里理解——不只是人们会随手消费什么,而是他们真正**需要**什么。

## ⚡ 本章行动清单 / Action Checklist

- [ ] 为每个核心方向写一句"待验证假设 + 证伪条件":什么样的真实动作(点击/注册/付费/留存)出现或不出现,就证明它成立或不成立。
- [ ] 亲自约到并完成至少 20–50 场用户访谈(参考 Legora"约午餐 + 按小时费付钱"的打法),访谈里疯狂提问、绝不推销,像人类学家一样记录他们如何决策。
- [ ] 去现场观察用户今天用什么"土办法"完成任务(像 Meesho 发现 WhatsApp 群),把被将就使用的现有工作流当成你 Agent 的切入点;别只听自述。
- [ ] 从第一天就设法收真钱或拿到带 KPI 的付费 pilot——在动手做下一个功能前先报价、拿承诺;记录"付了钱还生气"的人在气什么。
- [ ] 选"好读、被授权拍板、有燃眉之急"的对的用户群做验证,主动避开信噪比差的买家。
- [ ] 给每个 idea 设"证据止损线 / 3 个月证伪闸门":到线还没有真实动作信号就砍掉,手里备一组候选点子而非孤注一掷。
- [ ] 用"爱它 / 恨它 / 无所谓"三分法给每次发布验收;盯重度使用频次、留存、自然口碑,而不是注册量和 demo 好评。
- [ ] 对问题刚性、对方案弹性:把 Agent 抽象成"可迭代的 policy/markdown + 一个业务 KPI",让方案可换而验证到的问题不变。

## 📚 本章取材视频 / Sources

- [How To Get Your First Users](https://www.youtube.com/watch?v=0kARDVL2nZg) — 提出"最小可进化产品"、"找首批用户是搜索而非说服"、"早收真钱是为反馈"与"像人类学家研究早期用户"(`notes/0kARDVL2nZg.md`)
- [Groww: If Your Customers Don't Love It or Hate It, You've Already Lost](https://www.youtube.com/watch?v=ObBAxL2dFzw) — "无所谓才是失败信号"、"读弦外之音"、"收敛到一个问号"与"自然增长即 PMF"(`notes/ObBAxL2dFzw.md`)
- [Startup Advice: AI GTM, Pivoting & How To Hire](https://www.youtube.com/watch?v=nGLmpKi-jRU) — "学习速度 > TAM"、"资格审查比选细分市场重要"、"pivot 先行信号是你不再相信它"与"别拿'要做半年'当不见客户的借口"(`notes/nGLmpKi-jRU.md`)
- [How This 25-Year-Old Built A $675M Legal AI Startup](https://www.youtube.com/watch?v=pHuXCzM2ntU) — 零行业背景靠"访谈 100 位律师 + 极度谦逊"入行,以及"我是别人愿意帮的人"这项被低估的技能(`notes/pHuXCzM2ntU.md`)
- [From Pivot Hell To $1.4 Billion Unicorn](https://www.youtube.com/watch?v=5WN8bfG06Hk) — "15 人口头要用、14 人连链接都没点"的 The Mom Test 教训、选"好读"的用户、好点子是做出来找到的(`notes/5WN8bfG06Hk.md`)
- [How Meesho Became India's Biggest Shopping App](https://www.youtube.com/watch?v=49L8lVe_PVo) — "只听一侧用户是致命错误"、"蹲点观察真实行为"、"几十万用户 ≠ PMF"、"对问题刚性、对方案弹性"(`notes/49L8lVe_PVo.md`)
- [Ask These Questions Before Starting An AI Startup](https://www.youtube.com/watch?v=DJjZzzPANBY) — "别用观点代替验证,去找能证伪假设的因果机制"、把"想要"升级为"需要"(`notes/DJjZzzPANBY.md`)
- [Why Two IIT Engineers Turned Down $550K Jobs To Build A Startup](https://www.youtube.com/watch?v=2Ap1dnv-GXA) — "关键从来不是点子,而是有没有人愿意付钱"、"先卖后建"、把 Agent 产品化为"markdown + KPI"(`notes/2Ap1dnv-GXA.md`)
- [Michael Truell: Building Cursor At 23](https://www.youtube.com/watch?v=TrXi3naD6Og) — 给想法设"证据止损线"(CAD 半年零用户即砍)、用"信念一致性"选赛道、敢于对吵闹但错方向的用户说不(`notes/TrXi3naD6Og.md`)
- [Zepto: How Two 17-Year-Olds Built India's Largest Seller Of Fruits and Vegetables](https://www.youtube.com/watch?v=YKZCU0ynEbs) — "死磕前 30–100 个用户"、"只有你和客户、无处可藏"、"客户说行而专家说不行时信客户"(`notes/YKZCU0ynEbs.md`)
- [Harshil Mathur: AI Is Compressing Every Moat](https://www.youtube.com/watch?v=X5bABLCuIHA) — "难在客户端是问题、难在别处是护城河"、"信念不是天生的,是客户给的"(`notes/X5bABLCuIHA.md`)
