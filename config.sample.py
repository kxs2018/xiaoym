# -*- coding: utf-8 -*-
# config
# Author: kk
# date：2023/9/4 11:24
"""
这个文件是总配置文件，请仔细读配置说明
"""
'''
公共推送参数
参数解释
重要！重要！重要！如果没有脚本不会运行
qwbotkey是企业微信机器人webhookkey
获取方法：https://github.com/kxs2018/yuedu/blob/main/getqwboykey.md
'''
qwbotkey = ''
#########################################################################
'''
czgmck是充值购买的参数配置列表
活动入口,微信打开：http://2502567.pkab.tz6pstg20fnm.cloud/?p=2502567
打开活动入口，抓包的任意接口cookies中的gfsessionid参数,填入ck。
单账户填写样式。(这里只是样式，不要填这里)
czgmck = [
    {'name': 'xxx', 'ck': 'xxxx'},
]
多账户填写样式，几个账号填几个，不要多填。(这里只是样式，不要填这里)
czgmck = [
    {'name': 'xxx', 'ck': 'xxxx'},
    {'name': 'xxx', 'ck': 'xxxx'},
    {'name': 'xxx', 'ck': 'xxxx'},
]
参数解释
name:账号名，你可以随便填，用来推送时分辨哪一个账号
ck:账号的ck,抓包的任意接口cookies中的gfsessionid值
'''
czgmck = [
    {'name': '账号1', 'ck': 'xxxx'},
    {'name': '账号2', 'ck': 'xxxx'},
]
#########################################################################
'''
mtzck是美添赚的参数配置列表
活动入口,微信打开：http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552
打开活动入口，抓包的任意接口headers中的Authorization参数，填入ck。
单账户填写样式(这里只是样式，不要填这里)
mtzck = [
    {'name': 'xxx', 'ck': 'xxxx'},
]
多账户填写样式，几个账号填几个，不要多填。(这里只是样式，不要填这里)
mtzck = [
    {'name': 'xxx', 'ck': 'xxxx'},
    {'name': 'xxx', 'ck': 'xxxx'},
    {'name': 'xxx', 'ck': 'xxxx'},
]
参数解释
name:账号名，你可以随便填，用来推送时分辨哪一个账号
ck:账号的ck,抓包的任意接口headers中的Authorization参数
'''
mtzck = [
    {'name': '账号1', 'ck': 'share:login:18axxxxxx9c68adc1c1', "uids": 'UID_11ZHxxxxxxxxxxQ'},
    {'name': 'xxx', 'ck': 'xxxx'},
    {'name': 'xxx', 'ck': 'xxxx'},
]
#########################################################################
'''
xyyck是小阅阅的参数配置列表
活动入口,微信打开：https://wi56108.ejzik.top:10267/yunonline/v1/auth/0489574c00307cdb933067188854e498?codeurl=wi56108.ejzik.top:10267&codeuserid=2&time=1694865029
打开活动入口，抓包的任意接口cookies中的ysm_uid参数,填入ck。
单账户填写样式(这里只是样式，不要填这里)
xyyck = [
    {'name': 'xxx', 'ck': 'xxxx'},
]
多账户填写样式，几个账号填几个，不要多填。(这里只是样式，不要填这里)
xyyck = [
    {'name': 'xxx', 'ck': 'xxxx'},
    {'name': 'xxx', 'ck': 'xxxx'},
    {'name': 'xxx', 'ck': 'xxxx'},
]
参数解释
name:账号名，你可以随便填，用来推送时分辨哪一个账号
ck:账号的ck,抓包的任意接口headers中的Authorization参数
'''
xyyck = [
    {'name': '账号1', 'ck': 'oZdBp08xxxxxx8KpwY'},
    {'name': 'xxx', 'ck': 'xxxx'},
    {'name': 'xxx', 'ck': 'xxxx'},
]
#########################################################################
'''
aiock是星空、元宝、智慧和花花的共用参数配置列表，因为是一个平台，所以参数一样
活动入口,微信打开
星空阅读阅读：http://mr1693793443666.tozkjzl.cn/ox/index.html?mid=QR8YRLQNZ
元宝阅读：http://mr134905063.znooqoqzk.cloud/coin/index.html?mid=CS5T87Q98
花花阅读：http://mr1693635317854.stijhqm.cn/user/index.html?mid=FK73K93DA
智慧阅读：http://mr1694397085936.qmpcsxu.cn/oz/index.html?mid=2K4E46TVL

打开活动入口，抓包的http://u.cocozx.cn/api/ox/info接口的请求体中的un和token参数
单账户填写样式(这里只是样式，不要填这里)

aiock = [
    {'name': 'xxx', 'un': 'xxx', 'token': 'xxx',"uids": 'xxx'},
    {'name': 'xxx', 'un': 'xxx', 'token': 'xxx',"uids": 'xxx'},
    {'name': 'xxx', 'un': 'xxx', 'token': 'xxx',"uids": 'xxx'},
]
参数解释
name:账号名，你可以随便填，用来推送时分辨哪一个账号
ck:账号的ck,抓包的任意接口headers中的Authorization参数
'''
aiock = [
    {'name': 'xxx', 'un': 'xxx', 'token': 'xxx'},
    {'name': 'xxx', 'un': 'xxx', 'token': 'xxx'},
    {'name': 'xxx', 'un': 'xxx', 'token': 'xxx'},
]
#########################################################################
'''
rrbck是人人帮阅读的参数配置列表
活动入口,微信打开：http://ebb.maisucaiya.cloud/user/index.html?mid=1694991329391673344
打开活动入口，抓包的任意接口cookies中的un、token、uid参数,填入ck。
单账户填写样式(这里只是样式，不要填这里)
rrbck = [
    {'un': '', 'token': '', 'uid': ''},
]
多账户填写样式，几个账号填几个，不要多填。(这里只是样式，不要填这里)
rrbck = [
    {'un': '', 'token': '', 'uid': ''},
    {'un': '', 'token': '', 'uid': ''},
    {'un': '', 'token': '', 'uid': ''},
]
'''

rrbck = [
    {'un': '', 'token': '', 'uid': ''},
    {'un': '', 'token': '', 'uid': ''},
    {'un': '', 'token': '', 'uid': ''},
    {'un': '', 'token': '', 'uid': ''},
    {'un': '', 'token': '', 'uid': ''},
]
#########################################################################


