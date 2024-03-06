

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

"""自定义ua"""
ua_list = [] # ['ua1','ua2']微信浏览器ua，至少配置一个，否则部分脚本无法运行，只填手机端的，部分平台不支持电脑端ua

"""企业微信设置"""
qwbotkey=''  # 脚本优先从环境变量获取，没有获取到再从此处获取。已实装脚本：钢镚、每天赚

"""wxpusher设置"""
pushconfig = {"appToken":"","topicids":[]} 
"""脚本优先从环境变量获取，没有获取到再从此处获取，"topicids":["123456"],一对一推送无需设置toppicids"""

