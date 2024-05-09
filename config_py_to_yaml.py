# -*- coding: utf-8 -*-
"""
用来把config.py转换成config.yaml，配置更方便
"""
import k_config as config
import subprocess

try:
    import yaml
except:
    process = subprocess.Popen(['pip', 'install', 'PyYAML'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode == 0:
        print("PyYAML已成功安装")
    else:
        print("安装失败：")
        print(error.decode('utf-8'))
names = dir(config)
names = [name for name in names if not name.startswith(('__', '_')) and not callable(getattr(config, name))]
conf = {}
for name in names:
    conf.update({name: getattr(config, name)})
lt_config = {
    'ltck': ['name=德华;auth=Bxxxx','name=彦祖;auth=Bxxxxx'],
    'max_workers': 3,  # 线程数量设置,设置为5，即最多有5个任务同时进行
    'shuffle': 0,
    'txbz': 1000,

    'sendable': 0,  # 企业微信推送开关,1为开，0为关开启后必须设置qwbotkey才能运行

    'pushable': 0,  # wxpusher推送开关,1为开，0为关,开启后必须设置pushconfig才能运行

    'delay_time': 20,  # 并发延迟设置,设置为30即每隔30秒新增一个号做任务，直到数量达到max_workers

    'blacklist': ['name1', 'name2'],  # 提现黑名单设置,黑名单中的账号不自动提现，填入ck中的name,['name1','name2']。

}
xzb_config = {
    'ltck': ['name=德华;xiaozhuanbang_session=xx','name=彦祖;xiaozhuanbang_session=xxy'],
    'max_workers': 3,  # 线程数量设置,设置为5，即最多有5个任务同时进行
    'shuffle': 0,
    'txbz': 3000,

    'sendable': 0,  # 企业微信推送开关,1为开，0为关开启后必须设置qwbotkey才能运行

    'pushable': 0,  # wxpusher推送开关,1为开，0为关,开启后必须设置pushconfig才能运行

    'delay_time': 30,  # 并发延迟设置,设置为30即每隔30秒新增一个号做任务，直到数量达到max_workers

    'blacklist': ['name1', 'name2'],  # 提现黑名单设置,黑名单中的账号不自动提现，填入ck中的name,['name1','name2']。

}
conf.update({'lt_config': lt_config})
print(conf)
with open('config.yaml', 'w') as fi:
    yaml.safe_dump(conf, fi, allow_unicode=True)
