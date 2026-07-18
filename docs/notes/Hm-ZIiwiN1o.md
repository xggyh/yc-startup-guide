# 十亿美元级的冷门点子:如何做"反共识且正确"的押注 / Billion-Dollar Unpopular Startup Ideas

📄 **[点此查看全文转录 / Full transcript »](../transcripts/Hm-ZIiwiN1o.md)**

> **来源**: [Billion-Dollar Unpopular Startup Ideas](https://www.youtube.com/watch?v=Hm-ZIiwiN1o) · Y Combinator · 2025-10-17 · 时长 37:43
> **讲者**: YC 播客 The Light Cone 四人组——Garry Tan(SPEAKER_00)、Harj Taggar(SPEAKER_03)、Jared Friedman(SPEAKER_02)、Diana Hu(SPEAKER_01)
> **一句话定位**: 当 AI 垂直赛道从"遍地绿地"变成"处处红海",这期从 Uber/Coinbase/DoorDash/Flock Safety 等案例拆解"如何找到别人不信、你却相信的秘密",教 AI Agent 创始人用第一性原理而非热点做反共识押注,避免成为"第 3 到 98 名"陪跑的死尸。

## 🎯 TL;DR(中文核心要点)
- **AI 的"淘金窗口期"正在关闭**:每次技术平台(互联网、智能手机、AI)出现后约有两年"明显点子被一抢而空"的红利期;如今模型已很久没有 step-function 式跃进、垂直赛道每个都挤了多家公司,靠"随便挑个垂直做 workflow 自动化"已经不够,必须有**独特洞见**。
- **非共识 ≠ 智力上说不清,而是"体感上危险、吓人"**:真正值钱的点子会让你觉得"我可能赌上十年一无所获";这种恐惧本身就是别人不敢进、因而没有竞争的信号。
- **很多伟大点子藏在"灰色地带"**:Uber/Lyft(当年近乎违法)、Coinbase(监管模糊)、甚至 OpenAI(未经许可爬全网)都在法律不清晰的边缘。关键不是去做违法的事,而是找到**"写在某次技术剧变之前、已不符合现实的旧法律"**,然后有胆量去试——终端用户获益足够大时,法律会被改。
- **警惕"已成共识的 playbook",它们可能正是该反着做的地方**:DoorDash 当年反的是"full-stack startup"教条(只做配送、不自建厨房);如今该被质疑的默认剧本可能是 **forward-deployed engineer(FDE)**——Bob McGrew 这位发明者本人都认为它被过度滥用。
- **codegen 正把企业切换成本压到接近零**:过去把客户老数据 schema 迁到你这里要 6 周定制脚本、整单落地要 12–18 个月;现在好 demo + 一套 codegen 转换工具能把 time-to-value 从一年压到不到一个月——这是复杂企业级 AI 创业的重大利好。
- **把 FDE 本身产品化是一个反共识机会**:GigaML 用"AI forward-deployed engineer"替代人肉 FDE,人做要几周,AI 做只要几分钟——本质是"客户输入 spec、你即时交付产品",是"抽象层层叠加"的新形态。
- **别用 VC 的三条军规否掉自己**:Flock Safety 当年集齐 VC 三宗"不投"(硬件、市场只有 5000 万美元/年、在亚特兰大)——如今估值 75 亿美元,解决全美 10% 的报案犯罪。TAM 只是参考指标,不该用来划掉点子;规则越多,越容易把大钱说没。
- **只做"热"的东西 = 主动选择做衍生、明显、有一堆竞争对手的点子**。真正改变世界的是创始人;把注意力放回"人类真正迫切需要什么",商业模式、分发、增长都能后面再补出来。

## 🧭 适合谁 / 什么时候看
- 正在 AI 垂直赛道里**纠结"赛道已经很挤、还有没有机会"**、想找差异化洞见的 AI Agent 创始人。
- 手里有个**"看起来奇怪 / 别人都说是 tar pit"却有客户在拉你**的点子,需要判断该不该 all in 的人。
- 做**复杂企业级落地(数据迁移、FDE、替换 NetSuite 这类大软件)**、想理解 codegen 如何改变竞争格局的团队。
- 容易被 X、TechCrunch、朋友聚会上的"共识"影响判断,需要**校准自己"什么是真的"信息源**的创始人。

## 📝 分段精读

### 1. 开场:AI 竞争回来了 / Intro `[00:00–02:00]`
**要点(中文)**: Garry 用 Peter Thiel 的"竞争属于失败者"开场,指出他们观察 YC 众多 AI 创业公司发现——AI 领域的竞争正在回归。问题不再是"有没有机会",而是"如何用第一性原理、通过反共识且正确来对抗竞争"。这期整集就是在回答:如何发现一个你相信、别人还不信的秘密。
> 🗣️ "If you only want to work on things that are hot, you're going to find yourself working on derivative ideas that end up being obvious, that end up having 5, 10, 100 competitors." —— Garry Tan
> 译:如果你只想做当下火的东西,你会发现自己在做衍生的点子,最终它们都很明显、都有 5 个、10 个、100 个竞争对手。
> 🗣️ "Nine out of 10 people might tell you you're stupid or crazy, but then one out of 10 people might be exactly the person who believes what you believe." —— Garry Tan
> 译:十个人里九个会说你蠢或疯,但那第十个,可能恰好就是和你相信同一件事的人。

### 2. AI 垂直赛道正变得越来越拥挤 / AI Verticals Are Becoming More Crowded `[02:00–06:22]`
**要点(中文)**: Harj 复盘:一年多前"给创业者找点子/pivot"空前容易,原因有二——一是 AI 太新、垂直遍地绿地还没被挑过;二是模型每隔几个月就有 step-function 式跃进,不断把点子空间撑大。但现在氛围变了:每个垂直(保险、银行)都已有多家创业公司,而且很久没有一次能"洗牌"的模型跃进,所以"你到底有什么独特洞见"变得空前重要。Jared 补充"两年淘金窗口"规律:互联网、智能手机每次出现,都有约两年明显点子被一抢而空,之后就得想"接下来是什么"。
> 🗣️ "It's becoming more important to think about what's your actual unique insight that is going to enable you to find a good idea?" —— Harj Taggar
> 译:"你究竟有什么独特洞见,能让你找到一个好点子",这件事正变得越来越重要。
> 🗣️ "Each time there's a roughly two-year window where it was really easy. There was essentially a modern day gold rush... everybody rushed in, launched all the obvious ideas." —— Jared Friedman
> 译:每一次都有大约两年的窗口期特别容易,本质上就是一场现代淘金热……所有人涌进来,把所有明显的点子都做了。

### 3. 那些非共识的赢家:Uber、DoorDash、Lyft / Non-Obvious Successes `[06:22–09:50]`
**要点(中文)**: iPhone 出来时有上百万篇文章讨论"能做什么公司",但没人猜到 Uber 会是结果;真正的大赢家(Uber、DoorDash、Instacart)当年都极其非共识。DoorDash 尤其典型:它进的是超级红海(外卖、免配送早就有,Postmates、Grubhub、Seamless 都是巨头,连 YC 的 OrderAhead 都更领先),却仍胜出。Garry 又讲 Lyft 前身 Zimride 的故事:从"周末拼车去 Tahoe"的低频撮合,转向"人人有智能手机、可每天用的短途拼车",第一次让人看到"手机驱动的移动劳动力"这一形态。
> 🗣️ "When the iPhone came out there was like a million articles... I don't think a single person thought that like uber would be the consequence." —— Jared Friedman
> 译:iPhone 刚出来时有上百万篇文章……我不认为有任何一个人想到过,Uber 会是最终的结果。

### 4. 终端用户能倒逼法律改变:灰色地带的机会 / End Users Can Get Regulations Changed `[09:50–18:05]`
**要点(中文)**: 很多顶级点子处在"法律不清晰的灰色地带"。Lyft 创始人上线前一周极度担心"会不会坐牢",仍掷骰子上了——正是这种恐惧挡住了别人。Coinbase 是另一种反共识:2010–2012 年圈子里主流是"F the state"的 cypherpunk,Brian Armstrong 却反着做——主动去和银行合作、走 KYC/AML、拥抱监管,当时市场对此"愤怒到极点",因为这些合规反而让产品变难用;但他赌的是"普通人早晚会想交易加密货币"。四人反复强调**分界线**:不是叫你去做违法的事(那明确是净坏),而是从第一性原理想"人和市场需要什么",并去找那些"写在智能手机之前、已经不符合现实的旧法律"。Garry 举当下正在争取的 open banking / Plaid 数据权作为"用户获益 → 法律终将改"的现实例子。
> 🗣️ "A lot of great startup ideas are sort of in this gray area of like the law is not totally clear... even open AI is like that... they crawled the entire web without permission." —— Jared Friedman
> 译:很多伟大的创业点子都处在这种法律不完全清晰的灰色地带……连 OpenAI 都是这样,他们未经许可爬取了整个互联网。
> 🗣️ "Don't go out and do things that the law explicitly says you cannot do, but finding laws that were written in a time before some big tech shift that changes everything and just don't reflect reality can be really valuable." —— Harj Taggar
> 译:不要去做法律明文禁止的事;但找到那些"写在某次颠覆一切的技术剧变之前、已完全不符合现实的法律",可能极有价值。
> 🗣️ "The through line is not that you should do illegal things... it's that you should think about from first principles what are the things that markets and people need." —— Garry Tan
> 译:贯穿始终的主线不是"你该去做违法的事",而是你该从第一性原理去想:市场和人们到底需要什么。

### 5. 如何找反共识点子:去反那些已成默认的 playbook / Finding Contrarian Ideas `[18:05–25:10]`
**要点(中文)**: 一个可操作的框架——**列出过去一两年已成"共识 playbook"的东西,问哪些可能是错的、该反着做**。历史范例:DoorDash 反的是 2014 年前后盛行的"full-stack startup"教条(SpoonRocket、Sprig 都自建 ghost kitchen),它偏只做 app + marketplace 的"轻"配送,事后证明是对的。落到 AI:①"compound startup"(Parker Conrad / Rippling 带火)实践极难,但对某些 AI 公司反而可行——YC 的 Campfire 就直接做整套 AI-native 财务软件去正面刚 NetSuite,而非只做 point solution,正在拿下大客户。②Garry 指出 codegen 把企业切换成本压到接近零,是"轻装打复杂企业级"的利好。③最该被反的默认剧本可能是 **forward-deployed engineer**:Palantir 发明它时极其反共识,如今已成默认打法且效果惊人,但连发明者 Bob McGrew 都认为它被过度滥用、应只用于极特殊场景。④GigaML 正是"反 FDE"的例子:用 AI FDE 替代人肉 FDE——本质已经不是 FDE,而是"客户输入 spec、即时交付产品"。
> 🗣️ "Doordash's contrarian bet was actually [to] say we're just going to do delivery... we're not going to try to be a full stack startup, which was obviously the right bet in hindsight." —— Harj Taggar
> 译:DoorDash 的反共识押注,其实就是说"我们就只做配送……我们不去当 full-stack 创业公司"——事后看这显然是对的。
> 🗣️ "With codegen increasingly you can actually bring the switching cost closer to zero... time to value in like less than a month when it used to take a year." —— Garry Tan
> 译:随着 codegen 越来越强,你其实能把切换成本压到接近零……过去要一年的 time-to-value,现在可以压到不足一个月。
> 🗣️ "The AI FDE can do it in minutes... it's not really an FDE at all really, it's actually just like product." —— Harj Taggar
> 译:AI 版 FDE 几分钟就能搞定……它其实根本不算 FDE 了,本质上就是产品本身。

### 6. Flock Safety:向地方政府卖、别被 VC 军规否掉 / Flock Safety & Selling to Local Governments `[25:10–33:40]`
**要点(中文)**: Garry 亲历:一次整条街的车被专业团伙洗劫、警察因"没车牌"无能为力,让他一秒理解了 Flock Safety 的价值(树莓派 + 摄像头 + 太阳能板 + 边缘计算车牌识别,卖给社区/邻里协会)。这个项目当年集齐 VC 三宗"不投":是硬件、TAM 算下来最多 5000–6000 万美元/年、创始人在亚特兰大——近乎"不可融资"。但 Garry 强调:**TAM 只是参考指标,创始人和投资人都不该拿它当划掉点子的理由**(引 Brian Singerman:投资规则越多,越容易把大钱说没)。真正的破局不是靠 VC 反馈,而是从增长目标倒推——邻里协会不够,于是硬啃"卖给警局/市政府"这条看似不可能的路,成了增长主引擎;再叠加"犯罪被侦破 → 上晚间新闻 → 隔壁镇警长看到就要"的病毒式传播。如今估值 75 亿美元,解决全美 10% 的报案犯罪。这些打法无法从博客、X 或 ChatGPT 学到,只能亲自去试、去和人聊。
> 🗣️ "Flock safety today solves 10 percent of all reported crime in the united states." —— Garry Tan / Jared Friedman
> 译:如今 Flock Safety 侦破了全美所有报案犯罪中的 10%。
> 🗣️ "Just really razor focused on your customer and the actual need, like it just became so obvious." —— Garry Tan
> 译:只要真正把注意力像剃刀一样锋利地聚焦在客户和真实需求上,答案就会变得无比明显。
> 🗣️ "The more rules you have about investing, the more ways you can basically talk yourself out of making a lot of money." —— Garry Tan(转述 Brian Singerman)
> 译:你给投资定的规则越多,你能把自己劝退、错失大钱的方式就越多。

### 7. 科幻创始人:去做"不可能"的大点子 / The Sci-Fi Founder & "Impossible" Big Ideas `[33:40–36:42]`
**要点(中文)**: Diana 提出另一类反共识——"科幻创始人",专挑那些大多数人因为"太他妈难"而不敢碰、甚至需要重新发现科学与物理边界的点子。OpenAI 是典型:Sam 从 YC 出来时根本没人确定 AI 会成,早期只是研究者做魔方求解、打 Dota 的"支线任务";发布时舆论以负面为主,学术界的 AI 权威嘲讽"一群二三十岁、还没发过论文的人凭什么造 AGI"。Garry 指出:学术界为"多发论文"这个错误指标做 paperclip 优化,而真正的顶级 builder 优化的是"客户和用户的结果"。SpaceX 同理——Elon 是第 5 个搞火箭的亿万富翁,可复用火箭被斥为"亵渎",每炸一次就是一波负面新闻。共同点:创始人得在九成人说你蠢/疯的情况下,长期坚持己见。
> 🗣️ "One category is sort of the sci-fi founder... really going after ideas that most people are scared to build because they're just so freaking hard." —— Diana Hu
> 译:有一类是"科幻创始人"……专门去做那些大多数人因为"实在太难了"而不敢碰的点子。
> 🗣️ "The thing that really great builders optimize for is like outcomes for customers and users." —— Garry Tan
> 译:真正顶尖的构建者所优化的,是客户和用户的结果(而不是论文数量这种错误指标)。

### 8. 收尾:校准你的"什么是真的"信息源 / Outro `[36:42–37:43]`
**要点(中文)**: 反共识之所以能"变对",是因为它能像磁铁一样,把世界上少数和你相信同一件事的人吸引过来。Garry 的临别叮嘱:认真审视"你如何知道世界上什么是真的、正确的"——来自用户、来自你亲身经历、来自你直接对话的人的信息,是可验证的、可作为现实基底;而在 X 上刷帖、听名人(甚至包括他们自己)说的,都只是 N=1。唯一重要的,是你在意的、和你共享价值观的那群人。
> 🗣️ "Nine out of 10 people might tell you you're stupid or crazy, but then one out of 10 people might be exactly the person who believes what you believe. And then you're contrarian and you become right." —— Garry Tan
> 译:十个人里九个会说你蠢或疯,但那第十个可能正是和你相信同一件事的人——于是你既反共识,又变得正确。

## 🚀 给 AI Agent 创始人的行动项
- [ ] **列一张"AI 创业共识 playbook"清单**(如:纯 FDE 打法、只做 point-solution 的垂直 Agent、"wrapper 会被大模型碾死"、compound startup 太难做),逐条问"如果这条在特定场景下是错的,反着做会怎样"。
- [ ] **优先押注 codegen 带来的"切换成本→0"套利**:选一个替换成本极高的存量系统(NetSuite / 老 CRM / 定制 schema),把 demo 打磨到极致 + 建一套自动数据/schema 迁移的 codegen 工具,目标把 time-to-value 从一年压到一个月内。
- [ ] **考虑把 FDE 本身产品化**:如果你的 Agent 现在靠人肉 forward-deploy 配置,评估能否用 codegen 造一个"AI FDE",让客户输入 spec 即时得到可用产品,把交付从"数周"降到"数分钟"。
- [ ] **用第一性原理而非 TAM 筛点子**:先确认"人类是否迫切需要、且只有现在(AI 能干活)才可能",再谈市场规模;别用"市场太小/是硬件/地点不对"这类 VC 军规提前否掉自己。
- [ ] **主动去找"体感危险"的灰色地带**:识别那些"写在智能手机/AI 之前、已不符现实的旧法规或旧禁忌",在合法边界内验证用户获益是否足够大到能倒逼规则改变——但绝不做法律明文禁止的事。
- [ ] **校准你的信息源**:把决策依据从"X/TechCrunch/朋友说这是 tar pit"切换到"付费客户、亲身经历、你直接对话的人";当客户在"把产品从你手里拽走"(pull)时,优先相信这个信号。
- [ ] **从增长目标倒推 go-to-market**,而不是从当前渠道顺推:如果现有客户群撑不起增长目标(如只卖邻里协会),尽早去啃那条"看似不可能但更大"的渠道(如市政府 / 大企业)。

## 🔑 关键术语 / 概念
- **Contrarian and right(反共识且正确)** — 既要与主流看法相反,又要最终被证明是对的;只反不对是找死,只对不反则没有超额回报。
- **Two-year window / gold rush(两年淘金窗口)** — 每次新技术平台出现后约两年内,明显点子被一抢而空,之后须转向非共识。
- **Full-stack startup** — 2014 年前后流行的"光做软件不够、要自建全链条(自建厨房等)"教条;DoorDash 反之而胜。
- **Compound startup(复合型创业)** — Parker Conrad / Rippling 带火的"一次做一整套多产品模块"打法;实践极难,但对部分 AI 公司(如 Campfire)反而可行。
- **Forward-deployed engineer(FDE,前置部署工程师)** — Palantir 发明、模糊咨询与软件边界的打法:工程师驻场把客户的 schema/业务逻辑转成你的系统;如今已成 AI 企业级默认剧本,也因此成了"最值得反"的对象。
- **codegen 驱动的切换成本归零** — 用代码生成自动完成数据/schema 迁移,把过去数周至数月的定制迁移压到数分钟至数周,大幅降低企业换供应商的阻力。
- **Regulatory capture(监管俘获)** — 在位巨头借"为消费者安全"之名,用监管/服务条款阻止用户流向低费率新供应商,以此当护城河(如银行对抗 open banking / Plaid)。
- **Sci-fi founder(科幻创始人)** — 专挑"因为太难而没人敢做、甚至需重新逼近科学/物理边界"的大点子(OpenAI、SpaceX)。
- **Paperclip optimizing the wrong metric** — 为错误指标做极端优化(如学术界为"发论文"优化);真正的 builder 应优化"客户/用户的结果"。

## 🔖 高价值金句时间戳
- `[00:00]` "Run out and try to find things that humans really desperately want and need, and then you'll figure out the rest." — 先盯死人类的迫切需求,商业模式/分发/增长都能后补。
- `[02:37]` "It's becoming more important to think about what's your actual unique insight." — 绿地红利消退后,独特洞见取代"随便挑垂直"成为胜负手。
- `[10:02]` "Even open AI is like that... they crawled the entire web without permission." — 顶级点子常在灰色地带;边界是"用户是否真正获益",而非"是否舒适"。
- `[15:16]` "Finding laws that were written in a time before some big tech shift... don't reflect reality can be really valuable." — 反共识的合法路径:攻击"过时旧法律",而非做违法事。
- `[21:20]` "You can actually bring the switching cost closer to zero." — codegen 让复杂企业级替换从一年变一个月,是当下最实的 AI 创业红利。
- `[27:20]` "How can a startup that has a dozen people kill netsuite? This is the timeline world." — 小团队 + AI 正在把"不可能替换的巨型软件"变成可攻目标。
- `[29:38]` "Flock safety today solves 10 percent of all reported crime in the united states." — 集齐 VC 三宗"不投"的项目,最终成了 75 亿美元、影响全美的公司。
- `[36:26]` "Nine out of 10 people might tell you you're stupid or crazy... And then you're contrarian and you become right." — 反共识变对的机制:吸引那第十个和你同频的人。
