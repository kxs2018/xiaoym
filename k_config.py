
"""自定义ua"""
ua_list = [] # ['ua1','ua2']微信浏览器ua，至少配置一个，否则部分脚本无法运行，只填手机端的，部分平台不支持电脑端ua

"""企业微信设置"""
qwbotkey=''  # 脚本优先从环境变量获取，没有获取到再从此处获取。

"""wxpusher设置"""
pushconfig = {"appToken":"","topicids":[]} 
"""脚本优先从环境变量获取，没有获取到再从此处获取，"topicids":["123456"],一对一推送无需设置toppicids。"""

"""鱼儿设置"""
yu_config = {
        'max_workers': 5,  # 线程数量设置 设置为5，即最多有5个任务同时进行

        'txbz': 0.5,  # 设置提现标准 单位：元

        'sendable': 1,  # 企业微信推送开关 1开0关

        'pushable': 1,  # wxpusher推送开关 1开0关

        'delay_time': 20,  # 并发延迟设置 设置为20即每隔20秒新增一个号做任务，直到数量达到max_workers

        'blacklist':[], # 提现黑名单设置,黑名单中的账号不自动提现，填入ck中的name,['name1','name2']。

        'yuck':[], 
        # ck设置，优先从环境变量中获取，[{'name':'德华','ck':'抓包的ck值'},{'name':'彦祖','ck':'抓包的ck值','uid':'UID_xxx','zfb_account':'18888888888','zfb_name':'狗蛋'}]
        # name值随意，方便自己辨认即可。uid是wxpusher一对一通知专属设置，其它情况不要填,不使用支付宝提现无需设置zfb_account zfb_name

    }
"""鱼儿设置完毕"""

"""可乐设置"""
kl_config={
    'max_workers': 5,  # 线程数量设置,设置为5，即最多有5个任务同时进行

    'txbz': 8000,  # 设置提现标准,不低于3000，平台3000起提,设置为8000，即为8毛起提

    'sendable': 1,  # 企业微信推送开关,1为开，0为关开启后必须设置qwbotkey才能运行

    'pushable': 1,  # wxpusher推送开关,1为开，0为关,开启后必须设置pushconfig才能运行

    'delay_time': 30,  # 并发延迟设置,设置为30即每隔30秒新增一个号做任务，直到数量达到max_workers

    'blacklist':[], # 提现黑名单设置,黑名单中的账号不自动提现，填入ck中的name,['name1','name2']。

    'klck':[], 
    # ck设置，优先从环境变量中获取，[{'name':'德华','ck':'抓包的ck值'},{'name':'彦祖','ck':'抓包的ck值','uid':'UID_xxx','zfb_account':'18888888888','zfb_name':'狗蛋'}]
    # name值随意，方便自己辨认即可。uid是wxpusher一对一通知专属设置，其它情况不要填。不使用支付宝提现无需设置zfb_account zfb_name（暂未支持支付宝提现）
}
"""可乐设置完毕"""

"""小月月设置"""
xyy_config={
    'debug': 1,  # debug模式开关,1为开,0为关

    'max_workers': 5,  # 线程数量设置,设置为5，即最多有5个任务同时进行

    'txbz': 3000,  # 设置提现标准,不低于3000，平台3000起提,设置为8000，即为8毛起提

    'sendable': 1,  # 企业微信推送开关,1为开，0为关开启后必须设置qwbotkey才能运行

    'pushable': 1,  # wxpusher推送开关,1为开，0为关,开启后必须设置pushconfig才能运行

    'delay_time': 30,  # 并发延迟设置,设置为30即每隔30秒新增一个号做任务，直到数量达到max_workers

    'blacklist':[], # 提现黑名单设置,黑名单中的账号不自动提现，填入ck中的name,['name1','name2']。

    'xyyck':'', 
    # ck设置，优先从环境变量中获取，'德华#抓包的ysmuid值&彦祖#抓包的ysmuid值#UID_xxx&狗蛋#ysmuid##支付宝账号#支付宝姓名'
    # name值随意，方便自己辨认即可。uid是wxpusher一对一通知专属设置，其它情况不要填。
}
"""小月月设置完毕"""

"""猫猫设置"""
mm_config={

    'max_workers': 3,  # 线程数量设置,设置为5，即最多有5个任务同时进行

    'txbz': 0.3,  # 设置提现标准,0.3 5 10 20 共四档，单位元

    'sendable': 1,  # 企业微信推送开关,1为开，0为关开启后必须设置qwbotkey才能运行

    'pushable': 1,  # wxpusher推送开关,1为开，0为关,开启后必须设置pushconfig才能运行

    'delay_time': 30,  # 并发延迟设置,设置为30即每隔30秒新增一个号做任务，直到数量达到max_workers

    'blacklist':[], # 提现黑名单设置,黑名单中的账号不自动提现，填入ck中的name,['name1','name2']。
    
    'mmck':[{'name':'','zfb_account':'','zfb_name':'','ck':'bbus=eyJpdiI6Ixxxxxxx'}], 
    # ck设置，优先从环境变量中获取，[{'name':'xxx','ck':'bbus=xxx'},{'name':'xxx','uid':'UID_xxxxx','ck':'xxx','zfb_account':'11123455','zfb_name':'刘德华'}]
    # name值随意，方便自己辨认即可。ck是抓包数据。uid是wxpusher一对一通知专属设置，其它情况不要填，支付宝提现时需设置支付宝账号姓名
    }
"""猫猫设置完毕"""

"""点点赚设置"""
ddz_config={
    'max_workers': 5,  # 线程数量设置,设置为5，即最多有5个任务同时进行

    'txbz': 8000,  # 设置提现标准,不低于3000，平台3000起提,设置为8000，即为8毛起提

    'sendable': 1,  # 企业微信推送开关,1为开，0为关开启后必须设置qwbotkey才能运行

    'pushable': 1,  # wxpusher推送开关,1为开，0为关,开启后必须设置pushconfig才能运行

    'delay_time': 30,  # 并发延迟设置,设置为30即每隔30秒新增一个号做任务，直到数量达到max_workers

    'whitelist':[], # 提现白名单设置,白名单中的账号自动提现，填入ck中的name,['name1','name2']。

    'zfb_account': '', #支付宝账号
    
    'zfb_name': '', #支付宝名字

    'ddzck':[], # ck设置，优先从环境变量中获取，[{'name':'xxx','ck':'xxx'},{'name':'xxx','ck':'xxx','uid':'UID_xxxxx','zfb_account':'18888888888','zfb_name':'狗蛋'}]name值随意，方便自己辨认即可。抓包cookie所有值，填入ck。uid是wxpusher一对一通知专属设置，其它情况不要填
}
"""点点赚设置完毕"""


"""每天赚设置"""
mtz_config = {
    'debug': 0,  # debug模式开关 1为开，打印调试日志；0为关，不打印

    'max_workers': 2,  # 因为没有服务器验证是否点击链接的机制，建议线程设置为2.线程数量设置 设置为5，即最多有5个任务同时进行

    'txbz': 10000,  # 设置提现标准 不低于3000，平台标准为3000 设置为8000，即为8毛起提

    'sendable': 1,  # 企业微信推送开关 1开0关

    'pushable': 1,  # wxpusher推送开关 1开0关

    'delay_time': 40,  # 并发延迟设置 设置为20即每隔20秒新增一个号做任务，直到数量达到max_workers
    
    'blacklist':[],  # 黑名单中的账号不进行自动提现，填入ck中的name,['name1','name2']，未实名的辅助号专用，可到一定金额再实名提现
    
    'total_num': 19,  # 设置单轮任务最小数量"""设置为18即本轮数量小于18不继续阅读"""

    'mtzv2ck':'', #ck设置，建议填到环境变量或配置文件,多账号用&连接或创建多条变量。name=xxx;ck=share:xxxx&name=xxx;ck=share:xxxx;uid=UID_xxxx，微信和wxpusher群发不用填uid

}

