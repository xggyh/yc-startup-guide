# 25 岁、零法律背景,如何做成 6.75 亿美元法律 AI 公司(Legora 复盘) / How This 25-Year-Old Built A $675M Legal AI Startup (With No Legal Experience)

📄 **[点此查看全文转录 / Full transcript »](../transcripts/pHuXCzM2ntU.md)**

> **来源**: [How This 25-Year-Old Built A $675M Legal AI Startup (With No Legal Experience)](https://www.youtube.com/watch?v=pHuXCzM2ntU) · Y Combinator · 2025-08-26 · 时长 45:26
> **讲者**: Gustaf Alströmer(YC 合伙人,主持)· Max Junestrand(Legora 联合创始人兼 CEO,YC W24)
> **一句话定位**: 以 Legora 为样本,拆解一个 AI Agent 团队在最保守的垂直行业(法律)里,如何在零行业背景下切入、向 AI 怀疑者销售、把 agent 做成"可交付的生产力",并在模型飞速迭代中建立护城河——对做垂直 AI Agent 创业的人,这是一份可照抄的实战手册。

## 🎯 TL;DR(中文核心要点)
- **入行不靠背景,靠"访谈 100 个用户 + 极度谦逊"**:Max 创业前没做过律师,靠 LinkedIn 约了 100 位律师吃饭(提出按小时费付钱,结果没人收),把"外行的天真发问"变成产品优势。
- **产品形态 = 把 agent 塞进用户已有工作流**:两条腿——Web 端(chat → 能调用内部/外部工具的 agent → tabular review 网格)+ Word 插件("律师版 Cursor"),而不是造一个新 App 让用户搬家。
- **真正的技术难点不是 prompt,而是规模化**:tabular review 要"同时并行跑 10 万条 query 不出错、每条都带正确引用",靠大量 chunking / RAG / 处理法律文档的交叉引用与定义。
- **向保守行业销售:自上而下,先造样板间**:法律行业无法 bottom-up(采购要过 procurement + IT + 安全审查),打法是"先把一个 partner 团队变成明星,别人看了自己要跟进"。
- **销售话术核心是对齐利益:"你赢我们才赢"**:低差异化的法律工作一旦被人用 AI 打破均衡,客户会迅速倒戈,律所被迫且被激励去采纳——这不是价格竞赛,而是把省下的时间转去做高价值咨询。
- **模型策略:永远可热插拔 + 分类路由**:Azure/AWS/GPT/Claude/Gemini/Mistral 可互换,简单 query 走小模型、复杂 query 走大模型控制毛利——"不需要用火箭筒的时候别用,拿水枪就行"。
- **团队打法:优先招"前创始人"**:头几号员工招做过创业的人(哪怕创业失败),要的是 agency、主人翁精神和"能同时跑多条产品线"的能力;公司本质是"公司里套着多个公司"。
- **给垂直 AI 创始人的两条铁律**:① 别被单一模型供应商锁死、别去和 AI 实验室正面竞争;② 要么找模型够不到的窄品类,要么用别人没想到的方式创造性地用模型(如 AI scribing/写符合律师笔法的条款)。

## 🧭 适合谁 / 什么时候看
- 正在做/想做**垂直行业 AI Agent**的创始人,尤其是要卖给保守、监管重、决策链长的行业(法律/金融/保险/医疗/合规)。
- 没有目标行业背景,纠结"我不懂这行能不能做"的技术创始人——本片给出明确的"能,而且天真是优势"的方法论。
- 已经有 demo、正卡在"怎么从 10 人扩到 100 人 / 怎么向企业客户销售 / 怎么在模型迭代中不被淘汰"阶段的团队。
- 想理解 **MCP、模型热插拔、agent 工具编排** 在真实企业级产品里落地形态的工程 leader。

## 📝 分段精读

### 1. 起源:从 BERT 到 GPT-3.5 的解锁 / Origin: From BERT to the GPT Unlock `[00:34–04:09]`
**要点(中文)**: 法律科技早就存在,但长期是"一堆各自为战的点状工具"(模板、翻译、检索),因为旧模型处理不了非结构化的法律文本。触发点是一位联创的律师朋友"整个夏天四个月只在给大所做判例摘要"——GPT-3.5 一放给开发者,他们立刻做 POC(第一个产品是"解释股票期权合同的阅读器"),很快转向"覆盖全流程、每个法律人都想用的端到端系统"。做欧洲市场的第一关是合规:数据全部欧洲托管、不用于训练、不留存、豁免人工审查,先把这些"坑"跳过去才谈得上产品。

> 🗣️ "generative AI came into the game and just kind of threw up everything off the table and then when it landed you very clearly saw how you could solve a lot for a lot of these use cases with the same underlying tech" —— Max Junestrand
> 译:生成式 AI 一进场,直接把桌上所有东西掀翻;等尘埃落定,你会非常清楚地看到,原来这么多用例可以用同一套底层技术来解决。

> 🗣️ "one of the co-founders friend who was a lawyer spent four months during a summer just summarizing court cases for a big law firm" —— Max Junestrand
> 译:一位联创的律师朋友,整整一个夏天四个月,就干一件事——给一家大律所做判例摘要。(这就是最初点燃公司的观察)

### 2. Aha 时刻、产品形态与 $80M / The Aha Moment, Product & $80M `[04:10–09:38]`
**要点(中文)**: Aha 时刻发生在把 Legora 部署进北欧最大律所 Mannheimer Swartling——那位曾公开说"AI 更多是 artificial 而非 intelligent"的管理合伙人,当场输入一个法律检索 query(后端用 RAG 接了瑞典立法),系统完美作答,他"眼睛里就有了那个瞬间"。真正的产品爆点是 **tabular review**:把上百份文件做成网格,每份文档一行、每个 query 一列,交叉运行——"这一百份雇佣合同里都有 IP 条款吗?" 系统哗哗地 yes/yes/no/yes 并逐条链接到出处。产品分两块:Web 端(简单 chat 已进化成能调用内外部工具、跑多步 workflow 的 agent)+ Word 插件("律师版 Cursor",受限于只能占右侧一栏,像做移动端一样螺蛳壳里做道场)。此时刚完成 **$80M B 轮**(Iconiq、General Catalyst 领投,YC/Benchmark/Redpoint 跟投)。

> 🗣️ "You realize like, holy shit, this is transformational. It's taking tasks which used to be days or hours and it's turning them into minutes." —— Max Junestrand `[05:58]`
> 译:你会意识到:我靠,这是颠覆性的。它把过去要花几天或几小时的活,变成了几分钟。

> 🗣️ "you could phrase it as Cursor for lawyers ... how do we bring generative AI into the existing work environment of a legal professional" —— Max Junestrand `[08:28]`
> 译:你可以把它形容成"律师版 Cursor"……核心是怎么把生成式 AI 塞进法律人已有的工作环境里(而不是让他们搬到一个新地方)。

> 🗣️ "The big innovation there does not really come from how do you prompt and work with a model, but it's how do you make this run at scale? How do you run 100,000 queries in parallel at the same time and make sure nothing breaks, all the citations are correct?" —— Max Junestrand
> 译:真正的创新不在于怎么写 prompt、怎么调模型,而在于怎么把它跑到规模化——怎么同时并行跑 10 万条 query,还保证一条都不出错、所有引用都正确。

### 3. AI 把"天"变成"分钟",以及向 AI 怀疑者销售 / Transforming Legal Work & Selling to Skeptics `[09:39–17:14]`
**要点(中文)**: 旧 ML 只能识别"长得一样"的条款,LLM 能理解"意思相同但写法不同"的 change-of-control 条款,于是 redlining(按 playbook 对合同做红线批注)、跨上千份判例的 deep research、把尽调从"进物理数据室拿笔标"变成近乎商品化的能力,全部成立。销售层面,YC 过去投的法律软件公司最难的就是卖给律所;Max 在面试时就"逆势"断言"这次不一样,相信我们"。他的核心逻辑:**法律工作低差异化,一旦有人用新方式打破均衡,客户会迅速倒戈**,律所因此被迫且被激励采纳——而且这不是价格战,省下尽调时间就能腾出手做高价值的并购咨询。产品把这套沉淀成 **playbooks**(一组规则 + 示例语言 + 回退方案,按 play 键逐条跑合同),而且外溢到法务之外:Legora 自己每个销售在发 NDA 前都用它谈判,一家北欧大银行从法务→合规→风控→销售一路铺开,还顺带统一了全公司标准。

> 🗣️ "the way that we approached the problem was always with this idea of we win if you win so let's align our incentives" —— Max Junestrand
> 译:我们处理这个问题的方式始终是"你赢,我们才赢",所以让我们把双方的利益对齐。

> 🗣️ "when he goes into the battlefield having legora is like having another piece of armor" —— Max Junestrand(转述一位西班牙合伙人在庭审中实时用 Legora 查对方证据) `[15:32]`
> 译:当他走上战场,带着 Legora 就像多了一件铠甲。(那位律师在对方律师发言时实时查询,一发现漏洞就能立刻打断)

> 🗣️ "clients are also not really that excited to pay for very simple contract review when they know that AI can do 99% of it" —— Max Junestrand
> 译:客户也不太乐意再为很简单的合同审查付大钱,因为他们知道 AI 能干掉其中 99%。

### 4. 没有行业背景怎么入行:访谈 100 位律师 / No Expertise Needed: Interviewing 100 Lawyers `[17:15–20:19]`
**要点(中文)**: 三个联创都不是律师。方法是**极度谦逊 + 高频反馈**:上来先访谈 100 位律师——LinkedIn 上发消息约午餐、提出按对方小时费付钱(其实付不起,而没有一个人真收)。Max 把"我是那种别人愿意帮的人"称为被严重低估的技能:对人无所畏惧地主动,同时真诚地感激对方的帮助。给想做物流/保险/金融软件的创始人的建议不是"你不需要懂行",而是"去学":吃饭时疯狂提问、也回馈对方一些点子和认可,让对方产生"想给你出主意"的参与感。外行的"为什么非得这样、其实可以那样"的天真,在一个正剧变的行业里反而是资产。

> 🗣️ "the first thing I did was I interviewed 100 lawyers. I had this good hack on LinkedIn. I texted them asking if we could have lunch, and I would pay their hourly rate." —— Max Junestrand `[18:48]`
> 译:我做的第一件事就是访谈 100 位律师。我在 LinkedIn 上有个小妙招:发消息约他们吃午饭,并说我按他们的小时费付钱。

> 🗣️ "One of the attributes that have been very helpful in my career has been that I'm somebody people want to help. I think that's a very underrated skill." —— Max Junestrand `[19:10]`
> 译:我职业生涯里非常受用的一个特质是:我是那种别人愿意去帮的人。我觉得这是一项被严重低估的技能。

### 5. 硬刚巨头 + 技术栈与模型策略 / Competing with Incumbents & Model Strategy `[20:20–24:45]`
**要点(中文)**: 法律科技里有一批靠并购做大的老牌巨头,根基深、有数据壁垒,但极不受终端用户待见。AI 改变了出货速度、也造出了一个新品类,老 suite 里的点状工具正快速变得无关紧要。Legora 的杀手锏是**速度**:30 个工程师的出货能力碾压对手上千人的团队,100 人的公司迭代速度高于百倍体量的公司。壁垒(lock-in)在瓦解:买方不再签五年长约,只签一到两年,因为世界变得太快——而且他们现在挑供应商,看的不只是当下技术,更是**你的变化速率(rate of change)**,要的是能把他们从 A 带到 B 的长期伙伴。技术栈:一开始押 Azure(和客户同栈)只能用 GPT,现在 AWS/Claude/Gemini/GPT/Mistral 可互换,核心工程目标是"随时热插拔模型 + 模型一变强产品就自动变好",并用分类模型做 query 路由控制毛利。

> 🗣️ "our ability to out-ship or out-deliver these teams of thousands of engineers with just 30 is insane" —— Max Junestrand `[21:23]`
> 译:我们用 30 个人,就能在出货/交付上压过那些上千工程师的团队,这简直离谱。

> 🗣️ "how do we build everything in such a way where we can hot swap the models whenever we want, and also build it in such a way that the models become better, everything improves?" —— Max Junestrand `[24:19]`
> 译:我们怎么把一切都搭成"随时可以热插拔模型"、并且"模型一变好、整个产品就跟着变好"的样子?

> 🗣️ "sometimes you don't need a bazooka when you just need a water gun" —— Max Junestrand `[24:40]`
> 译:有时候你根本不需要火箭筒,一把水枪就够了。(简单 query 走小模型、复杂 query 走大模型)

### 6. 谁买单 & 保守行业销售打法 / Who Buys & Cracking Conservative Sales `[24:46–27:50]`
**要点(中文)**: 律所结构:合伙人组掌权,大所常有 innovation 部门(强势时自己做采购和创新议程),但他们不是真正的用户;而 M&A/争议/仲裁组里的一线律师背着计费指标、极其惜时,倾向于沿用熟悉方式,所以 innovation 团队的使命就是把用例推给各业务组做 upskill。中型所往往没有 innovation 部门,得靠合伙人拍板,而"让整个合伙人群体都买账"极难。销售解法:**要么说服所有人,要么从小切入**——先和一个 partner 及其团队合作、把他们捧成明星,其他人看了就会主动要用,然后再横向扩张。关键是**自上而下、先攻资深人**;bottom-up 在这行走不通,因为软件不是个人采购,必须过 procurement、IT、以及一大堆安全与数据隐私审查。

> 🗣️ "You have to convince everybody or you start smaller. You say, let's work with this partner and their team and make them rock stars. And then everybody else looks at them saying, what's that guy doing? That looks awesome. We also want in." —— Max Junestrand
> 译:你要么说服所有人,要么从更小处切入:先和某个合伙人和他的团队合作,把他们变成明星;然后其他人一看——那家伙在干嘛?太酷了,我们也要用。

> 🗣️ "It's impossible to do a bottom-up motion in our industry because you don't procure software individually. You take it through procurement and you take it through IT." —— Max Junestrand `[27:30]`
> 译:在我们这行,自下而上的打法根本行不通,因为软件不是个人采购的——它要走采购流程、走 IT。

### 7. 从电竞到超速扩张:招"前创始人"与"just do things" / eSports to Hypergrowth: Hiring Ex-Founders `[27:51–36:42]`
**要点(中文)**: Max 18 岁在"打职业 Dota 2"和"上大学"之间,用"最好情形推演"选了大学(赢下 The International 拿 1000 万美元之后"人生就停了");靠钻招生漏洞在 COVID 期间同时读工程和商科两所大学。做过电竞博彩统计模型、待过 Norrsken、麦肯锡短暂实习、在 Depict 只待了一周。增长打法:产品靠一场 demo 就能让律所下单——"这说明你做对了",于是"要在所有地方一次性全做"。但融资后第一次董事会,他宣布**未来四五个月先不销售**,专注可靠性/可扩展性,因为"法律人第一次登录是你唯一的机会,搞砸了他们不会回来";打磨到能"一天稳定 onboard 一千名律师"后才 let it rip,六个月从 25 人干到 100 人(平均每周招 2 人)。团队核心心法:**头几号员工优先招前创始人**(PG 的建议:创业过的人在人才市场上更抢手),要的是 agency 和对多产品线的主人翁精神——公司本质是"公司里套着多个公司";扩张新 hub 时always 派斯德哥尔摩最好的人去搭建,因为文化就是你招的人。面试常问"你在职责之外为公司做过什么",筛的是发现并解决问题、主动担责的人;扁平组织要的是用 AI 做 10 倍活的通才。

> 🗣️ "when law firms start to buy things after one demo, you're doing something right" —— Max Junestrand `[31:08]`
> 译:当律所看完一场 demo 就开始下单,说明你做对了什么。

> 🗣️ "I remember the look on some of our board members' faces when I basically said, we're not going to sell for the next four to five months ... the first experience of a legal professional logging in is the one chance you have. If you mess that up, they're not coming back." —— Max Junestrand `[31:55]`
> 译:我还记得董事会成员听我说"接下来四五个月我们不做销售"时的表情……法律人第一次登录就是你唯一的机会,搞砸了,他们不会再回来。

> 🗣️ "the first people you want to hire all former founders ... it's also like the way that we built the company because we're effectively running multiple companies within the company" —— Gustaf & Max `[34:08]`
> 译:你想招的头几个人全是前创始人……这也是我们搭公司的方式,因为我们本质上是在"一家公司里同时跑好几家公司"。

> 🗣️ "what have you done outside of your role for the company ... here I'm looking for creativity, ability to spot problems and solve them, and to take responsibility for more things than just the stuff that you're doing" —— Max Junestrand `[35:38]`
> 译:"你在职责之外为公司做过什么?"——我在这里找的是创造力、发现并解决问题的能力,以及愿意为分外之事担责。

### 8. 律师的未来、AI 实验室的角色与 PMF 的手感 / Future of Law, AI Labs & What PMF Feels Like `[36:43–39:35]`
**要点(中文)**: 5–10 年后律师会越来越多地"审阅工作而非亲自做工作"——管理客户预期、指挥并监督 AI agents、把关质量与交付;之所以卖给律师而非法律服务的终端使用者,是因为"总需要一个真正懂行的人"来交付最终产品。对 AI 实验室的判断:它们正从"模型提供商"变成"平台公司"(Google 把 Gemini 塞进 Workspace、Anthropic 猛推 MCP 做统一入口);对 Legora 这类公司,"模型实验室出的东西是预期内的,你在上面加的才是锦上添花"。PMF 的手感被形容为一种被市场"拖拽/无限需求"往前拉的感觉——产品已从"实验性 AI"变成客户交付核心工作的依赖,一断就立刻来电话。

> 🗣️ "you're more and more entering a workspace of reviewing work than actually doing it ... you are managing the expectations from your clients and the work from your AI agents" —— Max Junestrand `[36:54]`
> 译:你会越来越进入一种"审阅工作而非亲自做工作"的状态……你在管理客户的预期,也在管理你的 AI agents 交出来的活。

> 🗣️ "it literally feels like we have infinite demand ... it's moved from being in this experimental AI bucket into we are reliant on this for core work" —— Max Junestrand `[38:45]`
> 译:那感觉简直就像我们有无限的需求……它已经从"实验性 AI"这一档,变成了"客户的核心工作离不开它"。

### 9. 留守斯德哥尔摩、品类领导与给垂直 AI 创始人的建议 / Staying in Stockholm, Category Leadership & Advice for Vertical AI Founders `[39:36–45:26]`
**要点(中文)**: 没听 YC "搬去旧金山"的常规建议,而是留在斯德哥尔摩:先在本土市场长大,去美国既更卷、也会逼你做得更窄;他们反其道横向做强,发现"在芬兰/丹麦/挪威也是最强",再扩到西班牙/法国/德国/伦敦,最后才进美国——那时新市场进入的"算法"已成型,自己也从小池塘小鱼长成大池塘里的鲨鱼。做品类领导者不只是做软件,而是做大所转型的战略伙伴,因为"软件与服务的界线正在模糊"。给垂直 AI 创始人的收尾铁律:**别被单一供应商锁死、别和 AI 实验室正面竞争**;把东西建成"船",潮水一涨(模型变强)一切自动变好;起步阶段承认自己没能力超过那些公司,**要么找模型够不到的窄品类,要么用别人没想到的方式创造性地用模型**(如 AI scribing——要嵌大量定制 prompt 让它用对医学/法律术语,写出律师会写的条款,而不是模型吐出的"最可能答案")。

> 🗣️ "we had also then grown from this small fish in a small pond to crocodile or a shark in the bigger pond" —— Max Junestrand `[40:30]`
> 译:那时我们已经从小池塘里的小鱼,长成了大池塘里的鳄鱼——或者说鲨鱼。

> 🗣️ "don't get locked in with a provider and don't compete with the AI labs. The AI labs ship ... you want to be really clear and honest to yourself where you're adding value and where you're adding long-term moat" —— Max Junestrand `[42:12]`
> 译:别被某个供应商锁死,也别和 AI 实验室正面竞争——实验室的出货能力很强……你要对自己非常清醒诚实:你到底在哪里创造价值、在哪里建立长期护城河。

> 🗣️ "how do we build things as boats so that when the tide rises just everything gets better" —— Max Junestrand `[42:29]`
> 译:我们怎么把东西造成"船",这样潮水一涨(模型一变强),一切就自动变好。

> 🗣️ "you can't have to find a narrow category to do it where you know the [labs] won't get to, or ... finding out a way to leverage the models very creatively in a way that others haven't done it" —— Gustaf & Max `[42:39]`
> 译:你得找到一个模型(实验室)够不到的窄品类,要么就找到一种别人没用过的、极具创造性的方式去用模型。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **上来先做 100 场用户访谈**:用"约午餐 + 提议按小时费付钱"的方式接触目标行业从业者,把外行的"为什么非得这样"当成产品洞察来源,而不是遮羞的短板。
- [ ] **把 agent 嵌进用户已有工作流**,而不是造新 App 让他们搬家(参考"Word 插件 = 律师版 Cursor"):先想清楚你的"Word"是什么。
- [ ] **把工程重心从 prompt 转到规模化与可靠性**:并行海量 query、逐条可追溯引用、处理长文档的 chunking/RAG/交叉引用;并把"第一次使用体验"当成唯一机会去打磨,达标前甚至可以暂停销售。
- [ ] **架构上做到模型热插拔 + 分类路由**:多云多模型可互换,简单请求走小模型、复杂请求走大模型控毛利,并确保"模型一升级,产品自动变好"。
- [ ] **对保守/企业客户走自上而下**:先把一个团队做成"样板明星间"再横向扩,别指望 bottom-up;提前准备好过 procurement、IT、安全与数据隐私审查(欧洲还要数据本地托管/不留存/不训练)。
- [ ] **销售话术围绕"你赢我们才赢 + 变化速率"**:向客户证明不采纳会被打破均衡、且你是能把他们从 A 带到 B 的长期伙伴,而非卖一次性工具。
- [ ] **头几号员工优先招"前创始人"**,面试问"你在职责之外做过什么",按 agency/主人翁精神/能跑多产品线来筛;扩新地点派最好的老员工去带文化。
- [ ] **护城河建在"模型够不到的窄品类 + 创造性用法"上**:别和 AI 实验室正面刚,把产品造成"随潮水上涨的船",默认模型会持续变强。

## 🔑 关键术语 / 概念
- **Tabular review(表格化审阅)** — Legora 的核心创新:把 N 份文件 × M 个 query 做成网格并行运行,每格结果都带回原文引用;难点在规模化(同时跑 10 万 query 不出错)而非 prompt。
- **Playbooks(规则手册)** — 一组"批准/否决"规则 + 示例语言 + 回退方案(fallback 1/2);打开合同按"play"逐条跑并自动红线批注,可外溢到销售谈 NDA、统一全公司标准。
- **Redlining(红线批注)** — 依据 precedent 或 playbook 对合同逐条改动/标注,旧 ML 做不到,LLM 让它成为可能。
- **MCP(Model Context Protocol)** — Max 重仓的方向,用来规模化 agent 的工具调用,让不同业务组按自身 workflow 定制;他视 Anthropic 推 MCP 为"打造应用统一入口"的平台化动作。
- **Classification / model routing(分类路由)** — 用分类模型判断 query 复杂度,简单走小模型、复杂走大模型,控制毛利("别用火箭筒当水枪")。
- **Rate of change(变化速率)** — 保守买方选供应商时越来越看的不是当下功能,而是你迭代进化的速度,即能否把他们持续从 A 带到 B。
- **"Build things as boats"(把产品造成船)** — 把产品架构成"潮水(模型能力)上涨则一切自动变好"的形态,避免和 AI 实验室正面竞争。
- **Software–service blur(软件与服务界线模糊)** — 越深入法律软件栈,越发现品类领导者不只是卖软件,而是充当大所转型的战略伙伴。

## 🔖 高价值金句时间戳
- `[04:20]` "that AI was more artificial than intelligent" — 曾经的怀疑者(北欧最大所管理合伙人)后来正是被 Legora 现场演示打动的人:保守客户会转向,只要你给出足够强的 aha。
- `[05:58]` "holy shit, this is transformational. It's taking tasks which used to be days or hours and it's turning them into minutes." — 垂直 AI 的价值主张要能用"天→分钟"这种量级来陈述。
- `[18:48]` "I interviewed 100 lawyers ... I would pay their hourly rate." — 零背景入行的第一动作:用诚意换 100 场深度用户访谈。
- `[21:23]` "our ability to out-ship ... teams of thousands of engineers with just 30 is insane" — 小团队对巨头的唯一且致命的武器是出货速度。
- `[24:40]` "sometimes you don't need a bazooka when you just need a water gun" — 模型路由的通俗版:按需分配算力/模型,毛利才活得下来。
- `[38:45]` "it literally feels like we have infinite demand" — PMF 的真实手感:被市场拖着走、一断服务就来电话。
- `[42:12]` "don't get locked in with a provider and don't compete with the AI labs" — 给垂直 AI 创始人的第一铁律,反复值得抄在墙上。
- `[42:29]` "how do we build things as boats so that when the tide rises just everything gets better" — 把"模型会一直变强"变成顺风而非威胁的架构哲学。
