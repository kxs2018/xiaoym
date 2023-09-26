# -*- coding: utf-8 -*-
# k每天赚
# Author: kk
# date：2023/9/26
"""
每天赚入口：http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552
推送检测文章
1.通过企业微信机器人推送到企业微信群，请务必用微信关注微信插件并配置好机器人key
export qwbotkey="xxxxxxxxx"
参考https://github.com/kxs2018/yuedu/blob/main/获取企业微信群机器人key.md 获取key，并关注插件！！！
2.wxpusher公众号
参考https://wxpusher.zjiecode.com/docs/#/ 获取apptoken、topicids、uids，填入pushconfig
export pushconfig="{'appToken': 'AT_pCenRjs', 'uids': ['UID_9MZ','UID_T4xlqWx9x'], 'topicids': [''],}"

打开活动入口，抓包的任意接口headers中的Authorization参数，填入ck。
单账户填写样式(这里只是样式，不要填这里)
export mtzck="[{'name': 'xxx', 'ck': 'share:login:xxxx'},]"
多账户填写样式，几个账号填几个，不要多填。(这里只是样式，不要填这里)
export mtzck="[{'name': 'xxx', 'ck': 'share:login:xxxx'},{'name': 'xxx', 'ck': 'share:login:xxxx'}]"

参数解释
name:账号名，你可以随便填，用来推送时分辨哪一个账号
ck:账号的ck,抓包的任意接口headers中的Authorization参数，格式为share:login:xxxx
------------------------------------------------------------------------
运行提示 no module named lxml 解决方法
1. 在配置文件找到
## 安装python依赖时指定pip源
PipMirror="https://pypi.tuna.tsinghua.edu.cn/simple"
如果这条链接包含douban的，换成和上面一样的
2. 依赖-python 添加lxml
3. 如果装不上，尝试升级pip：①ssh连接到服务器 ②docker exec -it ql bash ③pip install pip -U
ql是青龙容器的名字，docker ps可查询
"""

import json
import os
import random
import requests
import re
import time
import ast

try:
    from lxml import etree
except:
    print('请仔细阅读脚本上方注释中的“no module named lxml 解决方案”')
    exit()
import datetime
import threading
from queue import Queue

"""实时日志开关"""
printf = 1
"""1为开，0为关"""

"""debug模式开关"""
debug = 1
"""1为开，打印调试日志；0为关，不打印"""

"""线程数量设置"""
max_workers = 5
"""填入数字，设置同时跑任务的数量"""

"""设置提现标准"""
txbz = 1000  # 不低于1000，平台的提现标准为1000
"""设置为1000，即为1元起提"""

"""企业微信推送开关"""
sendable = 1  # 开启后必须设置qwbotkey才能运行
"""1为开，0为关"""
if sendable:
    qwbotkey = os.getenv('qwbotkey')
    if not qwbotkey:
        print('请仔细阅读上方注释并设置好key')
        exit()

"""wxpusher推送开关"""
pushable = 1  # 开启后必须设置pushconfig才能运行
"""1为开，0为关"""
if pushable:
    pushconfig = os.getenv('pushconfig')
    if not pushconfig:
        print('请仔细阅读上方注释并设置好pushconfig')
        exit()
    try:
        pushconfig = ast.literal_eval(pushconfig)
    except:
        pass
    if pushconfig:
        appToken = pushconfig['appToken']
        uids = pushconfig['uids']
        topicids = pushconfig['topicids']


def ftime():  # line:95
    O0O00O0OOOOOO0O00 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # line:96
    return O0O00O0OOOOOO0O00  # line:97


def debugger(OO00OO000000O00O0):  # line:100
    if debug:  # line:101
        print(OO00OO000000O00O0)  # line:102


def printlog(OOOO0OO000OO00O00):  # line:105
    if printf:  # line:106
        print(OOOO0OO000OO00O00)  # line:107


def send(O00OO000O00000OOO, title='通知', url=None):  # line:110
    if not url:  # line:111
        O0OO00OOO0O00000O = {"msgtype": "text", "text": {
            "content": f"{title}\n\n{O00OO000O00000OOO}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}", }}  # line:118
    else:  # line:119
        O0OO00OOO0O00000O = {"msgtype": "news", "news": {"articles": [
            {"title": title, "description": O00OO000O00000OOO, "url": url,
             "picurl": 'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}  # line:124
    O0OO00000O0000OOO = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'  # line:125
    O0OOO0O0O0OO0O0O0 = requests.post(O0OO00000O0000OOO, data=json.dumps(O0OO00OOO0O00000O)).json()  # line:126
    if O0OOO0O0O0OO0O0O0.get('errcode') != 0:  # line:127
        print('消息发送失败，请检查key和发送格式')  # line:128
        return False  # line:129
    return O0OOO0O0O0OO0O0O0  # line:130


def push(O00000O0OO0O000OO, O00OO0O0OOO0O0OOO, url='', uid=None):  # line:133
    if uid:  # line:134
        uids.append(uid)  # line:135
    O000OO00O0OOOO00O = "<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace(
        'msg', O00000O0OO0O000OO).replace('url', url)  # line:137
    O000O0000OOOOOO0O = {"appToken": appToken, "content": O000OO00O0OOOO00O, "summary": O00OO0O0OOO0O0OOO,
                         "contentType": 3, "topicIds": topicids, "uids": uids, "url": url,
                         "verifyPay": False}  # line:147
    O0OO0OOOOOO00OOO0 = 'http://wxpusher.zjiecode.com/api/send/message'  # line:148
    OOO0000OOOOOOOOO0 = requests.post(url=O0OO0OOOOOO00OOO0, json=O000O0000OOOOOO0O).json()  # line:149
    if OOO0000OOOOOOOOO0.get('code') != 1000:  # line:150
        print(OOO0000OOOOOOOOO0.get('msg'), OOO0000OOOOOOOOO0)  # line:151
    return OOO0000OOOOOOOOO0  # line:152


def getmpinfo(O0O00OOOOO0OOOOOO):  # line:155
    if not O0O00OOOOO0OOOOOO or O0O00OOOOO0OOOOOO == '':  # line:156
        return False  # line:157
    OOOO0OOOOOO0OO0O0 = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}  # line:159
    OOOOO0O00OO00O00O = requests.get(O0O00OOOOO0OOOOOO, headers=OOOO0OOOOOO0OO0O0)  # line:160
    OOO0O0O000O00OO0O = etree.HTML(OOOOO0O00OO00O00O.text)  # line:161
    OOO00OO0OO000O0OO = OOO0O0O000O00OO0O.xpath('//meta[@*="og:title"]/@content')  # line:162
    if OOO00OO0OO000O0OO:  # line:163
        OOO00OO0OO000O0OO = OOO00OO0OO000O0OO[0]  # line:164
    OO0OOOOOO00OO00O0 = OOO0O0O000O00OO0O.xpath('//meta[@*="og:url"]/@content')  # line:165
    if OO0OOOOOO00OO00O0:  # line:166
        OO0OOOOOO00OO00O0 = OO0OOOOOO00OO00O0[0].encode().decode()  # line:167
    OO000O00O000OOOO0 = re.findall(r'biz=(.*?)&', O0O00OOOOO0OOOOOO) or re.findall(r'biz=(.*?)&',
                                                                                   OO0OOOOOO00OO00O0)  # line:168
    if OO000O00O000OOOO0:  # line:169
        OO000O00O000OOOO0 = OO000O00O000OOOO0[0]  # line:170
    OO0000O00OO00OO0O = OOO0O0O000O00OO0O.xpath(
        '//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')  # line:171
    if OO0000O00OO00OO0O:  # line:172
        OO0000O00OO00OO0O = OO0000O00OO00OO0O[0].strip()  # line:173
    OO00000OOO000OO0O = re.findall(r"user_name.DATA'\) : '(.*?)'", OOOOO0O00OO00O00O.text) or OOO0O0O000O00OO0O.xpath(
        '//span[@class="profile_meta_value"]/text()')  # line:175
    if OO00000OOO000OO0O:  # line:176
        OO00000OOO000OO0O = OO00000OOO000OO0O[0]  # line:177
    O0OOO00OO0O000OOO = re.findall(r'createTime = \'(.*)\'', OOOOO0O00OO00O00O.text)  # line:178
    if O0OOO00OO0O000OOO:  # line:179
        O0OOO00OO0O000OOO = O0OOO00OO0O000OOO[0][5:]  # line:180
    O0OOO0O00O0O00OO0 = f'{O0OOO00OO0O000OOO}|{OOO00OO0OO000O0OO}|{OO000O00O000OOOO0}|{OO0000O00OO00OO0O}|{OO00000OOO000OO0O}'  # line:181
    OOOOOO0OO00OOOOO0 = {'biz': OO000O00O000OOOO0, 'text': O0OOO0O00O0O00OO0}  # line:182
    return OOOOOO0OO00OOOOO0  # line:183


class MTZYD:  # line:186
    def __init__(OOO0OO0000OO0O0O0, O0000O00OO00OO000):  # line:187
        OOO0OO0000OO0O0O0.name = O0000O00OO00OO000['name']  # line:188
        OOO0OO0000OO0O0O0.s = requests.session()  # line:189
        OOO0OO0000OO0O0O0.s.headers = {'Authorization': O0000O00OO00OO000['ck'],
                                       'User-Agent': 'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
                                       'content-type': 'application/json', 'Accept': '*/*',
                                       'Origin': 'http://61695315208.tt.bendishenghuochwl1.cn',
                                       'Referer': 'http://61695315208.tt.bendishenghuochwl1.cn/',
                                       'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh', }  # line:199
        OOO0OO0000OO0O0O0.msg = ''  # line:200

    def user_info(OO000O0O000O00O0O):  # line:202
        OOOO00000O00OO000 = 'http://api.mengmorwpt1.cn/h5_share/user/info'  # line:203
        O000O0OOO00O0OOOO = OO000O0O000O00O0O.s.post(OOOO00000O00OO000, json={"openid": 0}).json()  # line:204
        debugger(f'userinfo {O000O0OOO00O0OOOO}')  # line:205
        if O000O0OOO00O0OOOO.get('code') == 200:  # line:206
            OO000O0O000O00O0O.nickname = O000O0OOO00O0OOOO.get('data').get('nickname')  # line:207
            OO000O0O000O00O0O.points = O000O0OOO00O0OOOO.get('data').get('points') - O000O0OOO00O0OOOO.get('data').get(
                'withdraw_points')  # line:208
            O000O0OOO00O0OOOO = OO000O0O000O00O0O.s.post('http://api.mengmorwpt1.cn/h5_share/user/sign',
                                                         json={"openid": 0})  # line:209
            debugger(f'签到 {O000O0OOO00O0OOOO.json()}')  # line:210
            O0000O000OOO00O0O = O000O0OOO00O0OOOO.json().get('message')  # line:211
            OO000O0O000O00O0O.msg += f'\n账号：{OO000O0O000O00O0O.nickname},现有积分：{OO000O0O000O00O0O.points}，{O0000O000OOO00O0O}\n' + '-' * 50 + '\n'  # line:212
            printlog(
                f'{OO000O0O000O00O0O.nickname}:现有积分：{OO000O0O000O00O0O.points}，{O0000O000OOO00O0O}')  # line:213
            OOOO00000O00OO000 = 'http://api.mengmorwpt1.cn/h5_share/user/up_profit_ratio'  # line:214
            O0O00000OOOO000OO = {"openid": 0}  # line:215
            try:  # line:216
                O000O0OOO00O0OOOO = OO000O0O000O00O0O.s.post(OOOO00000O00OO000,
                                                             json=O0O00000OOOO000OO).json()  # line:217
                if O000O0OOO00O0OOOO.get('code') == 500:  # line:218
                    raise  # line:219
                OO000O0O000O00O0O.msg += f'代理升级：{O000O0OOO00O0OOOO.get("message")}\n'  # line:220
            except:  # line:221
                OOOO00000O00OO000 = 'http://api.mengmorwpt1.cn/h5_share/user/task_reward'  # line:222
                for OOOO00O0O00OOOO0O in range(0, 8):  # line:223
                    O0O00000OOOO000OO = {"type": OOOO00O0O00OOOO0O, "openid": 0}  # line:224
                    O000O0OOO00O0OOOO = OO000O0O000O00O0O.s.post(OOOO00000O00OO000,
                                                                 json=O0O00000OOOO000OO).json()  # line:225
                    if '积分未满' in O000O0OOO00O0OOOO.get('message'):  # line:226
                        break  # line:227
                    if O000O0OOO00O0OOOO.get('code') != 500:  # line:228
                        OO000O0O000O00O0O.msg += '主页奖励积分：' + O000O0OOO00O0OOOO.get('message') + '\n'  # line:229
                    OOOO00O0O00OOOO0O += 1  # line:230
                    time.sleep(0.5)  # line:231
            return True  # line:232
        else:  # line:233
            OO000O0O000O00O0O.msg += '获取账号信息异常，检查cookie是否失效\n'  # line:234
            printlog(f'{OO000O0O000O00O0O.name}:获取账号信息异常，检查cookie是否失效')  # line:235
            send(f'{OO000O0O000O00O0O.name} 每天赚获取账号信息异常，检查cookie是否失效',
                 '每天赚账号异常通知')  # line:236
            return False  # line:237

    def get_read(OO0O00OO0O00O00O0):  # line:239
        O0OO0OO000OOOO0OO = 'http://api.mengmorwpt1.cn/h5_share/daily/get_read'  # line:240
        O00OOOO0000O000O0 = {"openid": 0}  # line:241
        OOOO0OOOO0000OO0O = 0  # line:242
        while OOOO0OOOO0000OO0O < 10:  # line:243
            OOOO0O000OOOOO00O = OO0O00OO0O00O00O0.s.post(O0OO0OO000OOOO0OO, json=O00OOOO0000O000O0).json()  # line:244
            debugger(f'getread {OOOO0O000OOOOO00O}')  # line:245
            if OOOO0O000OOOOO00O.get('code') == 200:  # line:246
                OO0O00OO0O00O00O0.link = OOOO0O000OOOOO00O.get('data').get('link')  # line:247
                return True  # line:248
            elif '获取失败' in OOOO0O000OOOOO00O.get('message'):  # line:249
                time.sleep(15)  # line:250
                OOOO0OOOO0000OO0O += 1  # line:251
                continue  # line:252
            else:  # line:253
                OO0O00OO0O00O00O0.msg += OOOO0O000OOOOO00O.get('message') + '\n'  # line:254
                printlog(f'{OO0O00OO0O00O00O0.nickname}:{OOOO0O000OOOOO00O.get("message")}')  # line:255
                return False  # line:256

    def gettaskinfo(O0OO0OO00OOO00O0O, OO00OOO0O0O0OO00O):  # line:258
        for OO000O000OOOO00O0 in OO00OOO0O0O0OO00O:  # line:259
            if OO000O000OOOO00O0.get('url'):  # line:260
                return OO000O000OOOO00O0  # line:261

    def dotasks(OO000O00OOOOOOO00):  # line:263
        O00O00O0O000O0O00 = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
            'content-type': 'application/json', 'Origin': 'http://nei594688.594688be.com.byymmmcm3.cn',
            'Referer': 'http://nei594688.594688be.com.byymmmcm3.cn/', 'Accept-Encoding': 'gzip, deflate', }  # line:270
        O00OOO0O0OOOOOO0O = 1  # line:271
        while True:  # line:272
            OO0OOO00OOOOO000O = {"href": OO000O00OOOOOOO00.link}  # line:273
            O0O0O0OO00000O00O = 'https://api.wanjd.cn/wxread/articles/tasks'  # line:274
            OO0O00000O00000O0 = requests.post(O0O0O0OO00000O00O, headers=O00O00O0O000O0O00,
                                              json=OO0OOO00OOOOO000O).json()  # line:275
            OO00OO000O0O000OO = OO0O00000O00000O0.get('data')  # line:276
            debugger(f'tasks {OO00OO000O0O000OO}')  # line:277
            OOO0O0OOO00O0O0O0 = [O0OO0000O0000OOOO['is_read'] for O0OO0000O0000OOOO in OO00OO000O0O000OO]  # line:278
            if 0 not in OOO0O0OOO00O0O0O0:  # line:279
                break  # line:280
            if OO0O00000O00000O0.get('code') != 200:  # line:281
                OO000O00OOOOOOO00.msg += OO0O00000O00000O0.get('message') + '\n'  # line:282
                printlog(f'{OO000O00OOOOOOO00.nickname}:{OO0O00000O00000O0.get("message")}')  # line:283
                break  # line:284
            else:  # line:285
                O0OOOOO0OOO000OO0 = OO000O00OOOOOOO00.gettaskinfo(OO0O00000O00000O0['data'])  # line:286
                if not O0OOOOO0OOO000OO0:  # line:287
                    break  # line:288
                O0000O0O000O0O000 = O0OOOOO0OOO000OO0.get('url')  # line:289
                O0OOO00O00000OO0O = O0OOOOO0OOO000OO0['id']  # line:290
                debugger(O0OOO00O00000OO0O)  # line:291
                OO0OOO00OOOOO000O.update({"id": O0OOO00O00000OO0O})  # line:292
                OO0000OO0OOO00O00 = getmpinfo(O0000O0O000O0O000)  # line:293
                try:  # line:294
                    OO000O00OOOOOOO00.msg += '正在阅读 ' + OO0000OO0OOO00O00['text'] + '\n'  # line:295
                    printlog(f'{OO000O00OOOOOOO00.nickname}:正在阅读{OO0000OO0OOO00O00["text"]}')  # line:296
                except:  # line:297
                    OO000O00OOOOOOO00.msg += '正在阅读 ' + OO0000OO0OOO00O00['biz'] + '\n'  # line:298
                    printlog(f'{OO000O00OOOOOOO00.nickname}:正在阅读 {OO0000OO0OOO00O00["biz"]}')  # line:299
                if len(str(O0OOO00O00000OO0O)) < 5:  # line:300
                    if O00OOO0O0OOOOOO0O == 3:  # line:301
                        if sendable:  # line:302
                            send('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',
                                 f'{OO000O00OOOOOOO00.nickname} 美添赚检测', )  # line:305
                        if pushable:  # line:306
                            push('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',
                                 f'{OO000O00OOOOOOO00.nickname} 美添赚检测', )  # line:309
                        raise Exception  # line:310
                    if sendable:  # line:311
                        send(OO0000OO0OOO00O00.get('text'), f'{OO000O00OOOOOOO00.nickname} 美添赚过检测',
                             O0000O0O000O0O000)  # line:312
                    if pushable:  # line:313
                        push(f'{OO000O00OOOOOOO00.name}\n点击阅读检测文章\n{OO0000OO0OOO00O00["text"]}',
                             f'{OO000O00OOOOOOO00.nickname} 美添赚过检测', O0000O0O000O0O000)  # line:314
                    OO000O00OOOOOOO00.msg += '发送通知，暂停50秒\n'  # line:315
                    printlog(f'{OO000O00OOOOOOO00.nickname}:发送通知，暂停50秒')  # line:316
                    O00OOO0O0OOOOOO0O += 1  # line:317
                    time.sleep(50)  # line:318
                O0OO00OO00OOOO0OO = random.randint(7, 10)  # line:319
                time.sleep(O0OO00OO00OOOO0OO)  # line:320
                O0O0O0OO00000O00O = 'https://api.wanjd.cn/wxread/articles/three_read'  # line:321
                OO0O00000O00000O0 = requests.post(O0O0O0OO00000O00O, headers=O00O00O0O000O0O00,
                                                  json=OO0OOO00OOOOO000O).json()  # line:322
                if OO0O00000O00000O0.get('code') == 200:  # line:323
                    OO000O00OOOOOOO00.msg += '阅读成功' + '\n' + '-' * 50 + '\n'  # line:324
                    printlog(f'{OO000O00OOOOOOO00.nickname}:阅读成功')  # line:325
                if OO0O00000O00000O0.get('code') != 200:  # line:326
                    OO000O00OOOOOOO00.msg += OO0O00000O00000O0.get('message') + '\n' + '-' * 50 + '\n'  # line:327
                    printlog(f'{OO000O00OOOOOOO00.nickname}:{OO0O00000O00000O0.get("message")}')  # line:328
                    break  # line:329
        O0O0O0OO00000O00O = 'https://api.wanjd.cn/wxread/articles/check_success'  # line:330
        OO0OOO00OOOOO000O = {'type': 1, 'href': OO000O00OOOOOOO00.link}  # line:331
        OO0O00000O00000O0 = requests.post(O0O0O0OO00000O00O, headers=O00O00O0O000O0O00,
                                          json=OO0OOO00OOOOO000O).json()  # line:332
        debugger(f'check {OO0O00000O00000O0}')  # line:333
        OO000O00OOOOOOO00.msg += OO0O00000O00000O0.get('message') + '\n'  # line:334
        printlog(f'{OO000O00OOOOOOO00.nickname}:{OO0O00000O00000O0.get("message")}')  # line:335

    def withdraw(OO0O0O0OO0O000OO0):  # line:337
        if OO0O0O0OO0O000OO0.points < txbz:  # line:338
            OO0O0O0OO0O000OO0.msg += f'没有达到你设置的提现标准{txbz}\n'  # line:339
            printlog(f'{OO0O0O0OO0O000OO0.nickname}:没有达到你设置的提现标准{txbz}')  # line:340
            return False  # line:341
        O000OOO000OOOOO00 = 'http://api.mengmorwpt1.cn/h5_share/user/withdraw'  # line:342
        OO00000O0O0O00OO0 = OO0O0O0OO0O000OO0.s.post(O000OOO000OOOOO00).json()  # line:343
        OO0O0O0OO0O000OO0.msg += '提现结果' + OO00000O0O0O00OO0.get('message') + '\n'  # line:344
        printlog(f'{OO0O0O0OO0O000OO0.nickname}:提现结果 {OO00000O0O0O00OO0.get("message")}')  # line:345
        if OO00000O0O0O00OO0.get('code') == 200:  # line:346
            send(f'{OO0O0O0OO0O000OO0.name} 已提现到红包，请在服务通知内及时领取', title='每天赚提现通知')  # line:347

    def run(O0OOOOO00OOO000OO):  # line:349
        O0OOOOO00OOO000OO.msg += '*' * 50 + f'\n账号：{O0OOOOO00OOO000OO.name}开始任务\n'  # line:350
        printlog(f'账号：{O0OOOOO00OOO000OO.name}开始任务')  # line:351
        if not O0OOOOO00OOO000OO.user_info():  # line:352
            return False  # line:353
        if O0OOOOO00OOO000OO.get_read():  # line:354
            O0OOOOO00OOO000OO.dotasks()  # line:355
            O0OOOOO00OOO000OO.user_info()  # line:356
        O0OOOOO00OOO000OO.withdraw()  # line:357
        printlog(f'账号：{O0OOOOO00OOO000OO.name}:任务结束')  # line:358
        if not printf:  # line:359
            print(O0OOOOO00OOO000OO.msg.strip())  # line:360
            print(f'账号：{O0OOOOO00OOO000OO.name}任务结束')  # line:361


def yd(OOOO000O0OO00000O):  # line:364
    while not OOOO000O0OO00000O.empty():  # line:365
        OOOOOOO00O0OO0OO0 = OOOO000O0OO00000O.get()  # line:366
        OOO00OOO00O000OO0 = MTZYD(OOOOOOO00O0OO0OO0)  # line:367
        OOO00OOO00O000OO0.run()  # line:368


def get_ver():  # line:371
    O0OOO00O000O00O0O = 'kmtz V1.5'  # line:372
    OO0000O00000O0000 = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}  # line:375
    OO00OOOOOO000O0OO = requests.get(
        'https://ghproxy.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json',
        headers=OO0000O00000O0000).json()  # line:377
    OO0O0O000OOO00O0O = O0OOO00O000O00O0O.split(' ')[1]  # line:378
    O0O0OOO00O0O0OO00 = OO00OOOOOO000O0OO.get('version').get(O0OOO00O000O00O0O.split(' ')[0])  # line:379
    OO00OOOO0O00OOOO0 = f"当前版本 {OO0O0O000OOO00O0O}，仓库版本 {O0O0OOO00O0O0OO00}"  # line:380
    if OO0O0O000OOO00O0O < O0O0OOO00O0O0OO00:  # line:381
        OO00OOOO0O00OOOO0 += '\n' + '请到https://github.com/kxs2018/xiaoym下载最新版本'  # line:382
    return OO00OOOO0O00OOOO0  # line:383


def main():  # line:386
    print("-" * 50 + f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n' + '-' * 50)  # line:387
    OOO000OO0OO0OO0O0 = os.getenv('mtzck')  # line:388
    if not OOO000OO0OO0OO0O0:  # line:389
        print('请仔细阅读上方注释并配置好key和ck')  # line:390
        exit()  # line:391
    try:  # line:392
        OOO000OO0OO0OO0O0 = ast.literal_eval(OOO000OO0OO0OO0O0)  # line:393
    except:  # line:394
        pass  # line:395
    OOO00OO0O0000O0OO = Queue()  # line:396
    OOO000OOO0OOOOO0O = []  # line:397
    for O0OOO0O0000O00O00, OOOOOOOO0O0OOO000 in enumerate(OOO000OO0OO0OO0O0, start=1):  # line:398
        printlog(f'{OOOOOOOO0O0OOO000}\n以上是账号{O0OOO0O0000O00O00}的ck，如不正确，请检查ck填写格式')  # line:399
        OOO00OO0O0000O0OO.put(OOOOOOOO0O0OOO000)  # line:400
    for O0OOO0O0000O00O00 in range(max_workers):  # line:401
        O0OOOOOOO0O0O0O0O = threading.Thread(target=yd, args=(OOO00OO0O0000O0OO,))  # line:402
        O0OOOOOOO0O0O0O0O.start()  # line:403
        OOO000OOO0OOOOO0O.append(O0OOOOOOO0O0O0O0O)  # line:404
        time.sleep(20)  # line:405
    for OO0O00O0O000OO0O0 in OOO000OOO0OOOOO0O:  # line:406
        OO0O00O0O000OO0O0.join()  # line:407


if __name__ == '__main__':  # line:410
    main()  # line:411
