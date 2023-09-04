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
uids:wxpusher的参数，当一个微信关注了一个wxpusher的推送主题后，会在主题的关注列表中显示
打开链接：https://wxpusher.zjiecode.com/admin/main/topics/list点击 用户管理->用户列表 能看到uids，用户uids可以单个推送消息给用户
'''
czgmck = [
    {'name': '账号1', 'ck': 'xxxx'},
    {'name': '账号2', 'ck': 'xxxx'},
]
#########################################################################
'''
mtzck是美添赚的参数配置列表
活动入口,微信打开：http://tg.1693634614.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=113565
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
uids:wxpusher的参数，当一个微信关注了一个wxpusher的推送主题后，会在主题的关注列表中显示
打开链接：https://wxpusher.zjiecode.com/admin/main/topics/list点击 用户管理->用户列表 能看到uids，用户uids可以单个推送消息给用户
'''
mtzck = [
    {'name': '账号1', 'ck': 'share:login:18axxxxxx9c68adc1c1', "uids": 'UID_11ZHxxxxxxxxxxQ'},
    {'name': 'xxx', 'ck': 'xxxx'},
    {'name': 'xxx', 'ck': 'xxxx'},
]
#########################################################################
'''
xyyck是小阅阅的参数配置列表
活动入口,微信打开：https://wi40796.sxcwpe.top:10259/yunonline/v1/auth/0489574c00307cdb933067188854e498?codeurl=wi40796.sxcwpe.top:10259&codeuserid=2&time=1693635112
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
uids:wxpusher的参数，当一个微信关注了一个wxpusher的推送主题后，会在主题的关注列表中显示
打开链接：https://wxpusher.zjiecode.com/admin/main/topics/list点击 用户管理->用户列表 能看到uids，用过uids可以单个推送消息给用户
'''
xyyck = [
    {'name': '账号1', 'ck': 'oZdBp08xxxxxx8KpwY'},
    {'name': 'xxx', 'ck': 'xxxx'},
    {'name': 'xxx', 'ck': 'xxxx'},
]
#########################################################################
'''
aiock是星空、元宝和花花的共用参数配置列表，因为是一个平台，所以参数一样
活动入口,微信打开
星空阅读阅读：http://mr1693793443666.tozkjzl.cn/ox/index.html?mid=QR8YRLQNZ
元宝阅读：http://mr1693635846547.kgtpecv.cn/coin/index.html?mid=5U4W6ZWPT
花花阅读：http://mr1693635317854.stijhqm.cn/user/index.html?mid=FK73K93DA

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
uids:wxpusher的参数，当一个微信关注了一个wxpusher的推送主题后，会在主题的关注列表中显示
打开链接：https://wxpusher.zjiecode.com/admin/main/topics/list点击 用户管理->用户列表 能看到uids，用过uids可以单个推送消息给用户
'''
aiock = [
    {'name': 'xxx', 'un': 'xxx', 'token': 'xxx'},
    {'name': 'xxx', 'un': 'xxx', 'token': 'xxx'},
    {'name': 'xxx', 'un': 'xxx', 'token': 'xxx'},
]
#########################################################################

'''
其他参数
参数解释
printf:日志打印参数，0是不打印调试日志，1是打印调试日志
dictType:标志参数请勿修改
'''
printf = 0
dictType = {
    'czgm': '充值购买过检测',
    'mtzyd': '美添赚过检测',
    'xyyyd': '小阅阅过检测',
    'yb': '元宝过检测',
    'hh': '花花过检测',
    'xk': '星空过检测'
}
# ybtxbz:元宝阅读提现标准，默认3000币时提现
ybtxbz = 3000
# xktxbz:星空阅读提现标准，默认3000币时提现
xktxbz = 3000
# czgmtxbz:充值购买阅读提现标准，默认3000币时提现
czgmtxbz = 3000
# xyytxbz:小阅阅阅读提现标准，默认3000币时提现
xyytxbz = 3000
