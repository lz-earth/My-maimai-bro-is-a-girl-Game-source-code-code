# ==============================================================================
# 《一起玩音游的后辈，居然是女生》
# 恋爱游戏脚本
# ==============================================================================

# 初始化定义
init:
    # 角色定义
    define mc = Character('周哲', color="#8B8B83", what_color="#FFFFFF")
    define momo = Character('莫莫', color="#FFB6C1", what_color="#FFFFFF")
    define friend = Character('阿煌', color="#4682B4", what_color="#FFFFFF")
    define narrator = Character(None, what_color="#D3D3D3")

# ==============================================================================
# 占位符图片定义 - 由于美术资源尚未制作，使用纯色占位符
# ==============================================================================

# 背景占位符 (深灰色)
image bg placeholder = Solid("#333333")
image bg arcade_1 = "images/bg/arcade_1.png"
image bg room_evening = Solid("#1A1A2E")
image bg street_day = Solid("#4A6741")
image bg arcade_entrance = Solid("#3D2914")
image bg arcade_maimai = Solid("#1E3A5F")
image bg hospital_room = Solid("#F5F5F5")

# 周哲立绘占位符 (阴暗废宅男 - 深灰绿色)
# 注：按照galgame惯例，主角说话时不显示立绘
# image zhouzhe neutral = Solid("#556B5B")
# image zhouzhe angry = Solid("#8B4513")
# image zhouzhe pain = Solid("#6B5B73")
# image zhouzhe proud = Solid("#2F4F4F")
# image zhouzhe tired = Solid("#4A5568")
# image zhouzhe happy = Solid("#3D5A4C")
# image zhouzhe surprised = Solid("#5D6D7E")
# image zhouzhe determined = Solid("#2C3E50")

# 莫莫立绘 (使用实际图片)
image momo cheerful = "images/character/momo cheerful.png"
# 其他表情占位符 (待添加实际图片)
image momo proud = Solid("#FF69B4")
image momo sad = Solid("#DB7093")
image momo crying = Solid("#FF1493")
image momo surprised = Solid("#FFA07A")
image momo teasing = Solid("#FF9999")
image momo angry = Solid("#FF6B6B")
image momo shy = Solid("#FFB6C1")
image momo happy = Solid("#FF69B4")
image momo sleeping = Solid("#E6E6FA")

# 阿煌立绘占位符 (钢蓝色)
image ahuang = Solid("#4682B4")

# 围观群众占位符
image crowd1 = Solid("#9370DB")
image cosplay_girl = Solid("#FF69B4")

# CG占位符 (紫色系)
image cg placeholder = Solid("#6A5ACD")
image cg score tiamat = Solid("#9932CC")
image cg rating 15750 = Solid("#4169E1")
image cg score 98 = Solid("#9370DB")
image cg song amazing = Solid("#8A2BE2")
image cg purple 14 = Solid("#4B0082")
image cg happy ending = Solid("#FFD700")

# ==============================================================================
# 音效定义
# ==============================================================================
# define sfx impact = "audio/sfx/impact.wav"
# define sfx dislocate = "audio/sfx/dislocate.wav"
# define sfx login = "audio/sfx/login.wav"

# BGM定义
define bgm_beginning = "audio/BGM/BGM_Beginning.mp3"

# ==============================================================================
# 第一章：女人，呵呵！
# ==============================================================================

label start:
    # 黑场过渡
    scene black with fade


    play music bgm_beginning fadein 5.0
    # ===== 场景1：QQ群聊 =====
    scene bg arcade_1 with fade

    # 播放BGM
    mc "......"

    mc "作为一个舞萌老玩家，我一直坚定地认为，女性玩家和男性玩家是两个完全不同的群体。"

    mc "女生啊，都是穿着可爱的cos服、选术力口小歌、成天和男朋友腻歪在一起的生物。"

    mc "在她们眼里，舞萌只有'术力口'和'流行动漫'两个分类。"

    mc "其他的歌里面，不管是潘多拉还是茄子，都入不了她们的法眼。"

    mc "如果你执意选取那些难听的曲目，和她们拼机的时候，可是会被她们用白眼鄙视的....."

    mc "所以说，我一直坚持一个原则：只要对面是女生，就绝对不会和她们拼机！最好是有多远就躲多远，千万别让她们来折磨我！"

    mc "我并不是轻视女生的实力和能力，但是这一点不容辩驳：唯有男人，才懂得舞萌的浪漫。唯有男人，才有与我拼机的资格！"

    show ahuang at right

    friend "......"

    friend "所以啊，你到现在还是个单身狗。"

    mc "......"

    friend "成天只知道打真超檄代的歌，还是那种难听的要死的怪歌，谁稀罕和你拼机啊？"

    friend "（继续说话）"

    narrator "周哲默然无语。"

    narrator "他知道，自己对歌曲的选择确实有些另类。"

    narrator "大部分玩家都喜欢打高难度的曲目，追逐极致的技术。"

    narrator "但是，周哲不同。"

    narrator "他喜欢早期歌曲，尽管它们可能不那么流行，但对他来说，这样的歌才是他真正喜欢的。"

    friend "别说是妹子了，就算是我一大老爷们，都不愿意陪你一起打。"

    narrator "这句话像是一把锐利的刀子，直刺进了周哲的心脏。（++周哲受到暴击伤害）"

    mc "......"

    narrator "好吧，他承认了。"

    narrator "没有人愿意陪他拼机。"

    narrator "因为，他喜欢的是真超檄的歌。"

    narrator "没有人愿意陪他打真超檄的怪歌……"

    narrator "（继续加）"

    hide ahuang

    narrator "其实，周哲也想过做出些改变，但是每次都是以失败告终。"

    narrator "原因很简单，大歌他全都打不来。"

    narrator "什么白潘，白茄，白皇帝，他全都打不来！"

    mc "啊，为什么我这么菜！"

    narrator "气愤的关闭了群聊，周哲坐回沙发上，思索片刻，痛苦的捂住脸。"

    # ===== 场景切换：周哲房间 =====
    scene bg room_evening with fade

    # play music bgm_home fadein 1.0

    narrator "阿煌说得一点没错。"

    narrator "作为一个入坑三年的玩家，他目前15800的rating，在如今实力越来越夸张的舞萌圈内，已经完全不够看了。"

    narrator "和他同期的人，个个都是辉将雪将，甚至还有天赋型选手已经拿到了神牌，实力强的可怕。"

    narrator "只有他，还停留在15800的水平。"

    mc "......"

    narrator "现实是残酷的，他的成绩却远远不及预期。"

    narrator "三年以来，他疯狂地练习，不断挑战高难度的曲目，但rating却始终停滞不前。"

    mc "唉……"

    narrator "被后来者超越的感觉，真的是糟糕透顶，但他已经习惯了。"

    narrator "只是......"

    mc "真的很羡慕啊，我什么时候也能变得像他们一样这么强......"

    narrator "他沉默了片刻，然后深吸一口气，收起了手机。"

    narrator "他站起身来，走到窗边，眺望着远方的天空。"

    narrator "夕阳的余晖洒在他的脸上，给了他一丝温暖的感觉。"

    mc "......"

    narrator "忽然间，手机传来了消息提示的声音。"

    # ===== QQ消息提示 =====
    show screen qq_notification

    pause 1.0

    hide screen qq_notification

    narrator "【QQ】莫莫：【图片】"

    narrator "这种时候，莫莫怎么会发消息呢？"

    narrator "有些不祥的预感啊。"

    narrator "莫莫是他的后辈，一个舞萌玩家，平时最喜欢给他发的就是成绩图了。"

    narrator "这不会.....是成绩图吧？"

    narrator "周哲颤颤巍巍的低下了头，小心的打开了聊天窗口，瞥见了一张熟悉的歌曲成绩图。"

    # ===== 显示成绩图CG =====
    show cg score tiamat at center with dissolve

    pause 2.0

    hide cg score tiamat with dissolve

    narrator "提亚马特，100.15%%"

    show momo cheerful at right with dissolve

    momo "前辈前辈～看到了吗？我把提亚玛特鸟了！嘿嘿～"

    momo "前辈是不是没我高啊？要不要我来教你呀～"

    hide momo cheerful

    narrator "即使隔着屏幕，他都能想象得出莫莫那副得意的小表情了。"

    mc "……"

    mc "？"

    mc "好气啊！！！"

    narrator "自己历经千辛万苦，每天练习，却怎么都打不好的提亚玛特，竟然被年轻的小学弟秒掉了？！"

    narrator "而且这语气是什么意思？是想让自己腼着脸向他请教吗？"

    narrator "门都没有！"

    narrator "不过，即使生气，该有的礼貌还是要有的。"

    narrator "愣了好久，周哲终于从嘴角扯出一丝僵硬的微笑。"

    mc "谢谢，我不需要。"

    narrator "他努力控制自己的情绪，强迫自己保持镇定。"

    show momo sad at right

    momo "qaq前辈你真的不需要我教教吗？"

    mc "嗯，真的不需要。"

    narrator "周哲强忍着拉黑的冲动，咬牙切齿的打下了这几个字。"

    show momo cheerful at right

    momo "好叭，那我继续去打舞萌啦~~(′ω`ゝ)"

    mc "……"

    mc "等一下。"

    hide momo cheerful
    show momo surprised at right

    narrator "虽然心中万般的不爽，周哲还是忍不住好奇问道。"

    mc "我很想知道，你是怎么做到的？"

    mc "要是没记错的话，你一个月前才把提打到99啊。"

    hide momo surprised
    show momo cheerful 

    momo "emmmm~"

    momo "怎么说呢......感觉这首歌很爽，就拿出来练了一下......"

    momo "结果呢，莫名其妙就鸟了。"

    mc "……"

    narrator "'莫名其妙'就鸟了。"

    mc "……"

    narrator "这个理由，真是太无敌了！"

    narrator "自己即使使出了浑身解数，依旧无法鸟掉的歌，却被莫莫轻轻松松地解决了。"

    narrator "好好好，全世界都欺负我是吧，欺负我是个体力白痴是吧。"

    narrator "飞升人别太嚣张了！"

    narrator "他越想，越觉得心里发堵，好像被什么东西卡住了一样。"

    narrator "不爽啊，真的很不爽啊！被入坑仅仅一年时间的学弟轻松超越了啊！"

    narrator "不只是莫莫，你们一个个的，全都飞升了，就留我一个人是吧！"

    narrator "受够了，我受够了！我要报复社会！"

    narrator "喜欢拼机是吧，喜欢开大的是吧！"

    narrator "是时候让你们回想起来，被真超檄支配的恐惧了！"

    mc "一块钱，脑浆，如龙，启动！！！"

    narrator "想着，周哲愤然起身，一把拿起手套和大水，直接向着机厅冲过去了！"

    # ===== 第一章结束 =====
    scene black with fade

    centered "{size=+5}—— 第一章 完 ——{/size}"

    pause 1.0

    jump chapter2

# ==============================================================================
# 第二章：莫莫
# ==============================================================================

label chapter2:
    scene black with fade

    centered "{size=+10}第二章{/size}"
    centered "{size=+5}莫莫{/size}"

    scene black with fade

    # ===== 场景：前往机厅的路上 =====
    scene bg street_day with fade

    # play music bgm_arcade fadein 1.0

    narrator "出门右拐，扫一辆共享自行车，在约莫十分钟的车程后，周哲抵达了终点。"

    narrator "这里，就是他最常来的地方。"

    narrator "世界最高城，长龙广场！"

    narrator "作为一个合格的舞萌吃，周哲闭着眼睛，仅凭直觉便跑到了熟悉的地方。"

    narrator "大风再起游乐汇，舞萌吃们永远的家！"

    # ===== 场景：机厅门口 =====
    scene bg arcade_entrance with fade

    narrator "今天是周末，再加上这个点本来人就很多，让游戏厅显得异常热闹。"

    mc "人还是很多啊。"

    narrator "即使大风再起有四台舞萌，在十几个人面前依然显得少了点。"

    narrator "每台机子前都有人在打歌，后面的板凳上也有好多人排队等机位。"

    mc "嗯……"

    narrator "周哲微微皱眉。"

    narrator "他并不喜欢人太多的地方，因为人一多鱼龙混杂，还总会有一群叽叽喳喳的小女生。"

    narrator "对，就是那种拼机只会开术力口的小女生！"

    narrator "忽然间，周哲停住了脚步。"

    # ===== 场景：发现莫莫 =====
    scene bg arcade_maimai with fade

    # play music bgm_comedy fadein 1.0

    narrator "他转过头看着左数第三个机台，看见了自己想找的人。"

    narrator "莫莫正站在那儿选歌。"

    # ===== 莫莫登场CG =====
    show momo cheerful at right with dissolve

    narrator "他今天穿着白色t恤，搭配黑色短裤，洁白的双腿暴露在空气中。"

    narrator "头发相对男生来说显得有点长，随意的披肩散落身后，闪烁着点点光芒，甚是好看。"

    narrator "脸上挂着清纯的笑容，两只小虎牙露在外面。"

    narrator "整张精致的脸庞被光芒所照耀，显得很活泼。"

    narrator "虽然人比较小只，但他站姿笔挺，背脊也挺直。整体形象，非常阳光，让人感到亲切。"

    narrator "{size=-2}眼光帅气小少年莫莫，闪亮登场！{/size}"

    narrator "周哲忍不住对比了一下自己的样子。"

    narrator "相较于莫莫，自己就完全是另外一副模样。"

    narrator "作为一个阴暗的宅男，他天生自带着阴郁的气质，好像被世界压得喘不过气来。"

    narrator "脸色苍白如纸，像刚从坟墓里爬出来一样，唇色发紫，没有一丝生气。"

    narrator "身体瘦得像个纸片人，骨头都要掉下来似的，身上的肌肉恐怕已经放弃了工作。"

    narrator "这个可怜的家伙，一点活力都没有，就像个死气沉沉的僵尸一样。"

    narrator "周哲也很清楚这一点，但没有丝毫想要改正的想法，平时除了吃喝拉撒睡，他几乎把自己关在屋内，连房门也不出。"

    narrator "要不是因为打舞萌能偶尔锻炼一下身体，他恐怕早就因为健康问题，猝死在屋里了。"

    narrator "这就是周哲，一个典型的废宅男！"

    narrator "此刻，他满脸阴沉，缓缓朝莫莫靠近！"

    mc "呵~莫莫，总算找到你了，桀桀桀。"

    narrator "冷酷一笑，缓缓的接近着自己的小学弟。"

    show momo surprised at right with dissolve

    narrator "莫莫正专注的选歌呢，忽然听见耳旁传来了怪叫声，被吓了一跳。"

    narrator "一转头，发现一个怪人朝着自己咧嘴坏笑。"

    momo "（奇怪，怎么看上去像个死人？）"

    momo "（再仔细一看，哦，原来是前辈啊。）"

    momo "（前辈正不怀好意的看着自己呢。）"

    hide momo surprised
    show momo cheerful at right with dissolve

    narrator "莫莫的心跳加速了几分，他不知道周哲究竟想做什么。"

    narrator "但每次面对前辈时，莫莫就好像有用不完的活力一样！"

    narrator "他兴奋的一把抱住了周哲。"

    momo "前辈～我们一起玩吧！"

    # ===== 撞击事件 =====
    show momo cheerful at right

    narrator "和迎面走来的周哲撞了满怀。"

    # play sound sfx_impact

    narrator "【咔擦】"

    narrator "这是骨头断裂的声音。"

    narrator "本就脆弱的骨头，碰上热情小学弟的熊抱，直接断成两截了。"

    mc "疼死了！"

    mc "啊，好痛！轻一点啊！你...你快给我撒手！"

    narrator "他双手捂着肋骨，痛苦不堪。"

    show momo surprised at right with dissolve

    momo "哦~对、对不起！"

    hide momo surprised
    show momo sad at right with dissolve

    narrator "莫莫急忙收回双手，尴尬的道歉。"

    narrator "周哲咬着牙，嘴里喘着粗气，一瘸一拐的走到一边坐下。"

    momo "对不起，前辈。"

    mc "你还好意思道歉！疼死我了！"

    narrator "周哲捂着胸口，满额头的冷汗。"

    narrator "他深深吸了口气，试图让自己的身体恢复正常，坐在一旁喘息了片刻，才感觉胸口的疼痛稍微缓解了一些。"

    momo "呃，前辈，您没事吧？"

    mc "托你的福，还死不了。"

    hide momo sad
    show momo cheerful at right with dissolve

    narrator "周哲摆着一副臭脸。"

    momo "噢，好吧。"

    hide momo cheerful

    narrator "莫莫乖巧的应了一声，灰溜溜的回去打歌了。"

    narrator "周哲又躺倒在座椅上休息了一会儿，才感觉恢复的差不多了。"

    mc "诶，真的得加强体质训练了。要，要不然，迟早会被这家伙给撞成残疾人。"

    narrator "看着一蹦一跳，一脸期待的莫莫，周哲心中涌现出一阵无力感。"

    narrator "这家伙，真是进步飞快啊。"

    narrator "今天鸟了提亚玛特，明天呢？"

    narrator "明天会不会把茄子鸟了？"

    narrator "再想想，一周后会不会把紫潘也鸟了？"

    narrator "......"

    narrator "不，不能再想了。"

    narrator "再想下去的话，他怕是明年就舞神了！"

    narrator "到那时候，自己就一辈子都追不上他了吧？"

    narrator "虽然不愿意承认，但周哲能感觉到，自己的小学弟，实力马上就要超过自己了。"

    narrator "唉，老了~"

    narrator "现在的他，也就只能靠真超檄代歌维持一下脸面了。"

    narrator "而且他心里清楚，自己之所以会打这些歌，都是这几年来慢慢练出来的。"

    narrator "要知道，光是真代的歌，他就打了足足2500pc，消耗在上面的时间可想而知，非常多。"

    narrator "2500pc的话，即使他奶奶来了都能打的贼高吧？"

    narrator "......"

    # ===== 莫莫邀请拼机 =====
    show momo cheerful at right with dissolve

    momo "前辈～前辈～我们一起拼机吧！"

    narrator "没过多久，莫莫兴奋的跑了过来。"

    mc "行吧。"

    narrator "周哲叹了口气，无奈的答应了莫莫。"

    show momo proud at right with dissolve

    momo "耶！！"

    hide momo proud

    narrator "莫莫兴奋的得跳了起来，然后拉着周哲走到滴蜡熊面前。"

    momo "我先上啦！"

    hide momo proud

    narrator "打开手机，打开【舞萌/中二】，点开二维码！"

    narrator "舞萌dx，启动！"

    # ===== 显示Rating CG =====
    show cg rating 15750 at center with dissolve

    pause 2.0

    hide cg rating 15750 with dissolve

    narrator "'157.......50吗？'"

    narrator "看着屏幕上rating，周哲愣了一下。"

    narrator "上周还只有15700，没想到一周就加了50分。"

    mc "真厉害......"

    show momo cheerful at right with dissolve

    momo "前辈？"

    mc "啊？哦，没事没事，我走神了！"

    hide momo cheerful

    narrator "周哲手忙脚乱的点开了二维码，在倒计时结束前登陆了账号。"

    # play sound sfx_login

    narrator "滴滴——"

    narrator "'欢迎回来！'"

    narrator "随着滴蜡熊的语音响起，他们正式开始了游戏。"

    narrator "这时，周哲才想起自己此次出勤的目的。"

    narrator "教训一下眼前这个小子，让他知道自己的厉害！"

    narrator "很幼稚的想法，但却很符合自己此刻的处境。"

    narrator "该收拾收拾这家伙，瞧瞧自己真正的技术了！"

    narrator "周哲深呼吸了一下，按捺下内心的躁动，然后露出了冷酷的微笑。"

    narrator "接下来，就让你见识一下，来自真代的慢慢恶意......"

    mc "一块钱！"

    # ===== 第二章结束 =====
    scene black with fade

    centered "{size=+5}—— 第二章 完 ——{/size}"

    pause 1.0

    jump chapter3

# ==============================================================================
# 第三章：前辈，你欺负人！
# ==============================================================================

label chapter3:
    scene black with fade

    centered "{size=+10}第三章{/size}"
    centered "{size=+5}前辈，你欺负人！{/size}"

    scene black with fade

    # ===== 场景：拼机开始 =====
    scene bg arcade_maimai with fade

    # play music bgm_tension fadein 1.0

    show momo cheerful at right

    narrator "周哲一上来就选择了一块钱。"

    narrator "如果有人看到，一定会以为他是被气急了而导致头脑发热，才会做出如此愚蠢的事情。"

    narrator "然而事实却并非如此。"

    narrator "对周哲来说，玩真代的歌就像吃饭和睡觉一样简单。"

    narrator "没有什么特别复杂的配置，甚至连邪道都懒得用。"

    narrator "只需要记住最恶心的部分，然后反复多练就行了，根本不会感到有压力。"

    mc "啊啊啊啊啊啊啊啊！一块钱！！！！！"

    narrator "屏幕亮起时，那刺耳的声音立刻钻进了耳朵。"

    narrator "然而，周哲却淡定无比地抬起手，随着节奏轻轻拍击了几下按键。"

    narrator "伴随着他的手掌落下，一个个音符都被他准确地击中了。"

    narrator "不知何时，周哲周围已经聚集了一圈人。"

    narrator "所有人都目瞪口呆地看着周哲，脸上露出惊骇的表情。"

    # ===== 围观群众反应 =====
    show crowd1 at center with dissolve

    narrator "我去！有人开一块钱！"

    narrator "一声高昂的叫喊响起，围观的舞萌吃们瞬间陷入了死寂。"

    narrator "我靠！！这……这家伙也太恐怖了吧？！"

    narrator "居然开一块钱，是不是精神出问题了！"

    narrator "你才是精神出问题了好吧，不看看人家头顶上的牌子！"

    narrator "那是什么？真舞舞啊！蠢货！"

    hide crowd1 with dissolve

    narrator "短暂的沉默之后，一阵阵惊讶的呼声响彻全场。"

    narrator "而周哲，依旧保持着淡定。"

    narrator "他在意的不是围观的舞萌吃的看法。"

    narrator "他在意的，是自己的成绩！"

    narrator "视线，始终盯着屏幕。"

    narrator "现在的每一秒钟，都是对他的巨大挑战！"

    narrator "因为，他想要完美驾驭这首歌！"

    narrator "是的，没有错......他的目标是，ap！"

    mc "真神！我来啦！"

    narrator "周哲嘴角扬起一抹笑容，眼神变得坚毅无比。"

    narrator "紧接着，猛然抬起手臂，甩出了一道帅气的弧线！"

    # ===== 手臂脱臼 =====
    # play sound sfx_dislocate

    narrator "【咔擦】"

    narrator "是骨头断裂的声音。"

    mc "诶哟！"

    narrator "一声痛苦的呻吟从周哲口中传出，他的额头瞬间冒汗，表情痛楚到扭曲。"

    mc "好疼！"

    mc "不行不行，用力过猛了，手臂要断掉了！"

    narrator "而在他身旁，一众舞萌吃更是惊讶地捂住了嘴，仿佛被吓到了似的。"

    narrator "他们万万没有想到，这家伙竟然在扫键的时候，把胳膊给弄脱臼了！"

    narrator "大家都汗流浃背了！"

    narrator "好可怕，把手都打断了欸！"

    # ===== 女生围观反应 =====
    show cosplay_girl at center with dissolve

    narrator "一个穿着cos服的女生悄悄说道。"

    narrator "果然舞萌就是一个高危游戏啊！娜娜，我们还是去打术力口吧！"

    hide cosplay_girl with dissolve

    narrator "在她边上，那个叫娜娜的女生深以为然的点了点头。"

    narrator "嗯嗯，我也这么觉得的。"

    narrator "听到两位女生的话语，其余人都赞同的点头，显然是被刚才那一幕吓到了。"

    narrator "原来，打真代歌会把手臂打断掉！"

    narrator "真是太吓人了！"

    narrator "舞萌吃纷纷如鸟兽散开，回去继续打歌了，看都不敢再看一眼。"

    narrator "只留着周哲抱着胳膊坐在椅子上，一个人在风中凌乱。"

    mc "好...难受。"

    mc "他感觉自己快哭出来了，怎么办！"

    mc "这尼玛不仅仅没拿到分数，甚至还把一条胳膊弄断了！"

    mc "真的太倒霉了！"

    mc "周哲欲哭无泪。"

    mc "早知道，应该拿小歌先热身的。"

    narrator "他咬牙切齿，强忍剧痛，慢吞吞的站起来。"

    narrator "肯定是莫莫这家伙，前面撞了我一下，把骨头弄错位了。"

    narrator "喃喃低语的说着，心里已经将莫莫骂了千百遍。"

    mc "唉......"

    narrator "他叹息一声，摇了摇头，强撑着痛意，缓缓的站起了身。"

    narrator "虽然左臂很疼，但总算是勉强能够支撑住，只要休息一会儿就没事了。"

    # ===== 莫莫的反应 =====
    show momo sad at right

    narrator "一首歌的时间马上就结束了。"

    momo "啊啊啊！！！打的好烂啊！"

    narrator "突然，莫莫绝望的声音从周哲身旁传来。"

    narrator "周哲眉毛一跳，顿时抬头望去。"

    narrator "只见，莫莫正抱着脑袋蹲在地上，一副生无可恋的样子。"

    narrator "小拳头狠狠锤着地板，脸上写满了委屈，仿佛受到了天大的伤害一般。"

    hide momo sad

    narrator "怎么回事？"

    narrator "周哲看了眼莫莫的成绩。"

    # ===== 显示莫莫成绩CG =====
    show cg score 98 at center with dissolve

    narrator "果不其然，只有98.3504%%，S+！"

    hide cg score 98 with dissolve

    narrator "呵呵。"

    narrator "周哲心中冷笑。"

    narrator "没错，这就是他想要的效果。"

    narrator "既然要教训小学弟，就不能手下留情！"

    show momo angry at right

    momo "前辈！你这是故意欺负人！"

    mc "哦？哪里欺负人了？"

    momo "我明明想和前辈一起拼机的，结果前辈你居然开一块钱欺负我！"

    mc "莫莫，你怎么能这么认为呢？我只是想让你体验一下真代歌的乐趣。"

    show momo angry at right

    momo "哼，前辈这是在狡辩！你肯定是欺负人！"

    momo "让我想想，前辈为什么要这么做呢？"

    momo "哦~我知道了！一定我长得太帅了！前辈害怕被我抢了风头，所以才想方设法打败我，对不对！"

    momo "略略略，前辈真是超~~幼稚的！"

    momo "你就是嫉妒我比你帅，才故意找我麻烦的！"

    mc "......"

    show momo teasing at right

    momo "一副一语道破天机的神秘表情。"

    mc "咳咳...你想多了。"

    narrator "闻言，周哲尴尬地摸了摸鼻子。"

    narrator "虽然理由不完全对，但不得不说，确实有这种成分在。"

    narrator "他确实想教训一下小学弟，不过也没有其他目的了。"

    show momo sad at right

    narrator "但莫莫却误解了周哲的意思。"

    narrator "他一脸幽怨的表情，一双水灵灵的大眼睛充斥着失望的光芒。"

    momo "前辈，你真的变坏了！我再也不喜欢你了！"

    mc "……"

    narrator "这话怎么听起来怪怪的呢..."

    mc "喂喂喂，什么叫'再也不喜欢你了'？你不会是男同吧？"

    show momo surprised at right

    momo "啊？没有没有，前辈你肯定听错了。"

    hide momo surprised
    show momo angry at right

    narrator "莫莫急忙摆了摆手，脸颊绯红。"

    momo "喂，不要岔开话题！我告诉你，我是绝对不会向恶势力妥协的！"

    momo "如果前辈你再要开怪歌的话，小心了，我可是会报仇的！"

    mc "……"

    narrator "这小子要做什么？"

    narrator "只见，莫莫切换了选歌的排序，然后按照等级从高向低排列。"

    narrator "很快，他就锁定了14的等级，找到了那个东西。"

    narrator "周哲看着这首歌，顿时双腿发软，眼前一黑。"

    mc "提......提亚玛特！"

    # ===== 第三章结束 =====
    scene black with fade

    centered "{size=+5}—— 第三章 完 ——{/size}"

    pause 1.0

    jump chapter4

# ==============================================================================
# 第四章：噗噗~前辈体力杂鱼~
# ==============================================================================

label chapter4:
    scene black with fade

    centered "{size=+10}第四章{/size}"
    centered "{size=+5}噗噗~前辈体力杂鱼~{/size}"

    scene black with fade

    # ===== 场景：选歌开始 =====
    scene bg arcade_maimai with fade

    # play music bgm_tension fadein 1.0

    show momo proud at right

    narrator "周哲险些昏死过去。"

    narrator "显然，提亚玛特带给他的心理阴影，已经很难用言语形容了。"

    narrator "这首歌简直可以称得上是周哲如梦魇般恐惧的歌，几乎是每次打到这首歌，他都会被累死。"

    narrator "他是真的怕了。"

    mc "莫莫你别冲动！"

    show momo cheerful at right

    momo "没有哦，我只是吓吓前辈。"

    narrator "周哲心中松了口气。"

    momo "我准备了一首更大的歌，绝对不会让前辈失望的。"

    mc "......"

    narrator "你丫是魔鬼吗！"

    mc "不行不行，我今晚已经很累了，明天再打吧。"

    show momo sad at right

    momo "唉，没想到前辈竟然这么弱。"

    momo "才打一把就累了？我还期待着跟前辈再玩几把呢。"

    mc "……"

    narrator "你大爷啊！老子什么时候说要和你玩了！"

    show momo cheerful at right

    momo "既然这样，那就算了吧。"

    momo "我也知道，前辈今天应该挺累的，不能为难前辈。"

    momo "那就勉为其难，和前辈打首小歌啦......"

    narrator "说着，莫莫将手伸向了右边的按键。"

    mc "等、等等！"

    momo "怎么了，前辈？"

    mc "呃……我想知道你为什么要把手放在右边？"

    mc "要是想选小歌的话，应该点左边的按钮啊？"

    momo "左边的按钮？"

    mc "是啊，按一下左边的按钮，把等级切换到13+......不不不，最好是13，把等级调的越小越好。"

    mc "你把手放在右边上，是会把等级调到14+的啊！"

    momo "嗯？"

    show momo cheerful at right

    momo "莫莫似懂非懂的点了点头，乖巧的把手收回去，放在了左边的按键上。"

    narrator "周哲见状，终于松了口气。"

    narrator "接着，他就看到了莫莫手指落下的位置——"

    # ===== 选歌CG =====
    show cg song amazing at center with dissolve

    narrator "AMAZING MIGHTYYYY ，expert 13难度。"

    hide cg song amazing with dissolve

    mc "诶哟，不错。"

    mc "确实是挺轻松的歌。"

    narrator "然而，莫莫接下来的操作并没有让他轻松多少。"

    # ===== 莫莫的骚操作 =====
    show momo teasing at right

    narrator "因为他居然点了一下自己的3号键，把难度切换成了紫14+！！！"

    narrator "他给周哲开了红AM，然后自己去打紫的了！"

    mc "卧槽！！！"

    narrator "周哲顿时泪流满面，他已经完全忘记了自己之前说的话，只想大叫一声。"

    narrator "给他开红的，自己却打紫的，这是瞧不起人吗！"

    narrator "这tmd哪里是什么'体谅前辈'，这分明就是变相的嘲讽啊！"

    narrator "嘲讽他是个菜逼！"

    narrator "周哲深吸了一口气，压抑着心底的愤怒，努力维持微笑。"

    narrator "他告诉自己，忍耐！"

    narrator "一定要冷静！"

    narrator "一定要克制住自己！"

    narrator "他现在可是个受伤的残疾人士！"

    narrator "就算被变相嘲讽了，也不应该失去理智。"

    narrator "他必须要保持作为老舞萌玩家的优雅！"

    narrator "这种小鬼，根本不值得生气，更何况他还是自己的后辈。"

    narrator "嗯，就是酱紫。"

    narrator "周哲努力控制自己的情绪，努力让自己恢复冷静。"

    narrator "但是他看到莫莫的动作后，险些没控制住骂出声来。"

    show momo cheerful at right

    narrator "莫莫居然测过身来，继续点了一下周哲的6号键，把他的难度从13切换到了9！！！"

    narrator "从红AM，变成了黄AM！"

    mc "你确定这样做真的好吗？"

    momo "为什么不好呢，前辈不是觉得13太难了吗？"

    momo "要不还是打9级歌休息一下吧！"

    mc "难你麻痹！"

    mc "老子收13的时候，你还在那里打黄谱呢！"

    narrator "周哲快崩溃了。"

    narrator "他发誓自从自己打舞萌以来，遇到的奇葩简直数不胜数，可像莫莫这么奇葩的，还真的是第一次碰见！"

    narrator "他甚至怀疑，莫莫是为了故意整他才入坑舞萌的？"

    mc "莫莫啊，你是不是对舞萌有什么误解？"

    show momo surprised at right

    momo "误解？"

    mc "是啊，你瞧瞧，这么大一个机厅，哪有像你这么玩的。"

    momo "嗯？"

    mc "我是问你，你平时怎么玩舞萌的？"

    show momo cheerful at right

    momo "很简单啊，只要看准时机，全部拍到就行啦!"

    mc "(?д?)b"

    mc "你大爷啊！！！"

    narrator "这孩子是不是脑子有问题？"

    narrator "他突然有了一丝悔意，如果早知道莫莫是这样的抽象，他就不应该把拉莫莫进舞萌坑的。"

    narrator "年轻的小伙子，就应该玩玩王者荣耀这种游戏。"

    narrator "或者，玩个原神什么的也可以嘛。"

    narrator "干嘛要打舞萌啊！"

    narrator "可惜，他已经没有选择了。"

    narrator "因为歌曲的选择，不是他说了算，而是莫莫说了算了。"

    # ===== 周哲的反击 =====

    mc "莫莫，别太瞧不起人了！"

    narrator "如今的他，已经被愤怒冲昏了头脑，丧失了理智。"

    narrator "于是乎……"

    narrator "他把手放到了六号键上。"

    narrator "然后，连点两次，把难度从黄谱，提升到了紫谱！"

    narrator "直接挑战最困难的等级，14+！"

    narrator "樱代最难曲目，紫AM！"

    # ===== 紫14+ CG =====
    show cg purple 14 at center with dissolve

    narrator "切，打紫谱就打紫谱，谁怕谁呢！"

    narrator "反正自己的rating已经达到15800了，努力一下，打个99没问题吧！"

    narrator "主要是，这家伙真的太欠收拾了！"

    narrator "不给他一些颜色看看，还真不知道谁是前辈呢！"

    hide cg purple 14 with dissolve

    narrator "周哲的眼中闪过了一丝阴狠，然后他毫不犹豫的按下了开始。"

    show momo surprised at right

    momo "等等，前辈！先别打！"

    narrator "莫莫见状吓了一跳，连忙阻止周哲。"

    momo "前辈，您的伤还没好啊！万一再受伤了就糟糕了！"

    mc "怕个毛线！我的身体结实着呢！"

    show momo sad at right

    momo "前辈，我错了！我刚才只是跟你闹着玩呢！你不要当真啊！"

    mc "少罗嗦，我就想打14+，你别多管闲事！"

    momo "不要啊，前辈。"

    momo "你会累死的！真的会累死的！"

    mc "少废话，不就是打14+吗，累个锤子？"

    momo "不不不，14+是真的会累死人的啊！前辈，求求你不要打了！"

    mc "闭嘴！"

    hide momo sad

    narrator "周哲没有再理睬他，而是专注于自己的机台。"

    # ===== 开始挑战 =====

    narrator "很快，乐曲开始了。"

    narrator "周哲的眼神坚定而决绝。他全神贯注地迎接着AM的挑战，指尖舞动的瞬间，一个个音符被精准的敲击。"

    narrator "随着乐曲的进行，难度逐渐提升，节奏变得更加快速而复杂。"

    narrator "周哲的手指开始有些发疼，但他并没有放弃的意思。他想要证明自己的能力，也想向莫莫证明他的能力。"

    narrator "然而，随着时间的推移，他感觉身体有些不对劲了。"

    mc "好......累，卧槽。"

    narrator "眼皮变得沉重，眼前的画面开始模糊起来。"

    narrator "尽管他努力地保持着意识，但身体的疲惫和过度消耗渐渐占据了上风。"

    mc "不是吧，我连个14+都打不动吗？"

    narrator "手指开始发颤，呼吸变得急促而不规律，这是身体开始发出警告了。"

    narrator "剧烈的疲劳和持续的高强度活动让他的肌肉酸痛不已，他的双手仿佛沉重的铁块，视线开始模糊起来。"

    mc "好难受......"

    narrator "他的手指逐渐变得僵硬，无法再像之前那样灵活地击打按键。"

    narrator "他的呼吸变得急促而不规律，汗水从额头上滴落下来。"

    narrator "他感到一阵晕眩，但他强迫自己集中精神，不让眼前的模糊影响他的判断。"

    narrator "\"我不能放弃，不能输给那个家伙。\"周哲心中坚定地告诉自己。"

    narrator "在那一刻，他的决心和毅力超越了疲劳和痛苦。"

    narrator "但下一刻，手却无论如何也抬不起来了。"

    mc "不......不行......好累......"

    narrator "眼睛越来越迷茫，周哲的意识彻底陷入黑暗中。"

    narrator "他的身体缓慢地倒在了机台上，脸上露出安详的笑容，仿佛已经完成了自己的使命。"

    narrator "年轻人就是好，倒头就睡。"

    show momo crying at right

    momo "喂...前辈，前辈你醒醒啊，前辈！你没事吧！"

    momo "呜呜呜，前辈你千万不能死啊，前辈！"

    narrator "意识消失的前一刻，周哲隐约听到莫莫的哭声，他勉强睁开眼睛，然后看到了一张梨花带雨的俏丽脸庞。"

    mc "哈哈，莫莫，你可是男孩子，怎么能随便哭啊......"

    narrator "周哲想着，他的身体不受控制地向后仰倒。"

    narrator "只来得及发出一声闷哼，便彻底晕死在了地上。"

    show momo crying at right

    momo "前辈！！！！！！"

    # ===== 结局场景 =====
    scene black with fade

    centered "{size=+5}—— 第四章 完 ——{/size}"

    pause 1.0

    # ===== 尾声 =====
    scene black with fade

    centered "{size=+10}未完待续{/size}"
    centered "{size=+5}敬请期待后续章节{/size}"

    pause 2.0

    return

# ==============================================================================
# 屏幕定义
# ==============================================================================

screen qq_notification:
    text "{size=+5}【QQ消息】莫莫发来一张图片{/size}" align (0.5, 0.1)
    text "{size=-2}点击继续...{/size}" align (0.5, 0.9)