
"""企业微信设置"""
qwbotkey=''  # 脚本优先从环境变量获取，没有获取到再从此处获取。已实装脚本：钢镚、每天赚

"""wxpusher设置"""
pushconfig = {"appToken":"","topicids":[]} 
"""脚本优先从环境变量获取，没有获取到再从此处获取，"topicids":["123456"],一对一推送无需设置toppicids。已实装脚本：钢镚、每天赚"""

"""元宝智慧星空内部互助设置"""
invite_info = {'name':'','code':''}  # 仓库脚本无需理会，收费项目专用
"""鱼儿设置"""
yu_config = {
        'max_workers': 5,  # 线程数量设置 设置为5，即最多有5个任务同时进行

        'txbz': 0.5,  # 设置提现标准 单位：元

        'sendable': 1,  # 企业微信推送开关 1开0关

        'pushable': 1,  # wxpusher推送开关 1开0关

        'delay_time': 20,  # 并发延迟设置 设置为20即每隔20秒新增一个号做任务，直到数量达到max_workers

        'blacklist':[], # 提现黑名单设置,黑名单中的账号不自动提现，填入ck中的name,['name1','name2']。

        'yuck':[], # ck设置，优先从环境变量中获取，[{'name':'德华','ck':'抓包的ck值'},{'name':'彦祖','ck':'抓包的ck值','uid':'UID_xxx'}]name值随意，方便自己辨认即可。uid是wxpusher一对一通知专属设置，其它情况不要填

    }
"""鱼儿设置完毕"""

