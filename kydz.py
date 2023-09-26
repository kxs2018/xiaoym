# -*- coding: utf-8 -*-
# kydz
# Author: kk
# date：2023/9/27
"""
仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
入口：http://5851278349.buemxve.cn/?jgwq=3340348&goid=itrb
http://5851278349.buemxve.cn/?jgwq=3340348&goid=itrb 抓包这个链接 抓出唯一一个cookie 把7bfe3c8f4d51851的值
或者http://wxr.jjyii.com/user/getinfo?v=3 a_h_n值/后面的字符串 填入ck
建议手动阅读几篇再使用脚本！！！
推送检测文章   将多个账号检测文章推送至将多个账号检测文章推送至目标微信目标微信，手动点击链接完成检测阅读
1.企业微信群机器人
qwbotkey为企业微信webhook机器人后面的 key，填入qwbotkey
参考 https://github.com/kxs2018/yuedu/blob/main/获取企业微信群机器人key.md 获取key，并关注插件！！！
2.wxpusher公众号
参考https://wxpusher.zjiecode.com/docs/#/ 获取apptoken、topicids、uids，填入pushconfig
---------------------------------------------------------------
青龙面板，在配置文件里添加
export qwbotkey="qwbotkey"
export pushconfig="{'appToken': 'AT_pCenRjs', 'uids': ['UID_9MZ','UID_T4xlqWx9x'], 'topicids': [''],}"
export ydzck="[{'name':'xxx','ck':'xxx'},{'name':'xxx','ck':'xxx'}]"
===============================================================
no module named lxml 解决方案
1. 配置文件搜索 PipMirror，如果网址包含douban的，请改为下方的网址
PipMirror="https://pypi.tuna.tsinghua.edu.cn/simple"
2. 依赖管理-python 添加 lxml
3. 如果装不上，①请ssh连接到服务器 ②docker exec -it ql bash (ql是青龙容器的名字，docker ps可查询) ③pip install pip -U
===============================================================
"""
import threading
import ast
import hashlib
import json
import os
import random
import re
import time
from queue import Queue
import requests
import datetime
from lxml import etree
from urllib.parse import unquote, urlparse, parse_qs

"""实时日志开关"""
printf = 1
"""1为开，0为关"""

"""debug模式开关"""
debug = 0
"""1为开，打印调试日志；0为关，不打印"""

"""线程数量设置"""
max_workers = 3
"""设置为5，即最多有5个任务同时进行"""

"""设置提现标准"""
txbz = 5000  # 不低于3000，平台标准为3000
"""设置为8000，即为8毛起提"""

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
if not pushable and not sendable:
    print('企业微信和wxpusher至少配置一个才可运行')
    exit()


def ftime():  # line:84
    O0000O0OO000OO00O = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # line:85
    return O0000O0OO000OO00O  # line:86


def debugger(O000OOO0OO0000O00):  # line:89
    if debug:  # line:90
        print(O000OOO0OO0000O00)  # line:91


def printlog(O0000OO0O00OOO0OO):  # line:94
    if printf:  # line:95
        print(O0000OO0O00OOO0OO)  # line:96


def send(O000O0OO00OO0OO00, title='通知', url=None):  # line:99
    if not url:  # line:100
        O00O00OOO0O0O00OO = {"msgtype": "text", "text": {
            "content": f"{title}\n\n{O000O0OO00OO0OO00}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}", }}  # line:107
    else:  # line:108
        O00O00OOO0O0O00OO = {"msgtype": "news", "news": {"articles": [
            {"title": title, "description": O000O0OO00OO0OO00, "url": url,
             "picurl": 'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}  # line:113
    O000OO00O00OO0O00 = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'  # line:114
    O00OOO0O0000OOOO0 = requests.post(O000OO00O00OO0O00, data=json.dumps(O00O00OOO0O0O00OO)).json()  # line:115
    if O00OOO0O0000OOOO0.get('errcode') != 0:  # line:116
        print('消息发送失败，请检查key和发送格式')  # line:117
        return False  # line:118
    return O00OOO0O0000OOOO0  # line:119


def push(OO0O00OO0000O0OO0, O000OO00O0O000O0O, O0O00OOOO0OO00000, uid=None):  # line:122
    if uid:  # line:123
        uids.append(uid)  # line:124
    O0OO00000OOO0O000 = "<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace(
        'msg', OO0O00OO0000O0OO0).replace('url', O0O00OOOO0OO00000)  # line:126
    O0O0O00OOOO00O0OO = {"appToken": appToken, "content": O0OO00000OOO0O000, "summary": O000OO00O0O000O0O,
                         "contentType": 3, "topicIds": topicids, "uids": uids, "url": O0O00OOOO0OO00000,
                         "verifyPay": False}  # line:136
    OOO0000O00OO00OO0 = 'http://wxpusher.zjiecode.com/api/send/message'  # line:137
    O00OOOO00O0OOOO00 = requests.post(url=OOO0000O00OO00OO0, json=O0O0O00OOOO00O0OO).json()  # line:138
    if O00OOOO00O0OOOO00.get('code') != 1000:  # line:139
        print(O00OOOO00O0OOOO00.get('msg'), O00OOOO00O0OOOO00)  # line:140
    return O00OOOO00O0OOOO00  # line:141


def getmpinfo(OO00O0O00OO0OOOOO):  # line:144
    if not OO00O0O00OO0OOOOO or OO00O0O00OO0OOOOO == '':  # line:145
        return False  # line:146
    OOOOOO0OO0O0OO000 = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}  # line:148
    O0O0O00O000O000OO = requests.get(OO00O0O00OO0OOOOO, headers=OOOOOO0OO0O0OO000)  # line:149
    O0OO00O0OOO0O0000 = etree.HTML(O0O0O00O000O000OO.text)  # line:150
    O0OOOO0OOOO0OOO00 = O0OO00O0OOO0O0000.xpath('//meta[@*="og:title"]/@content')  # line:151
    if O0OOOO0OOOO0OOO00:  # line:152
        O0OOOO0OOOO0OOO00 = O0OOOO0OOOO0OOO00[0]  # line:153
    OOOOOOOOO0O00O0O0 = O0OO00O0OOO0O0000.xpath('//meta[@*="og:url"]/@content')  # line:154
    if OOOOOOOOO0O00O0O0:  # line:155
        OOOOOOOOO0O00O0O0 = OOOOOOOOO0O00O0O0[0].encode().decode()  # line:156
    try:  # line:157
        O00OOO00000OO00OO = re.findall(r'biz=(.*?)&', OO00O0O00OO0OOOOO)  # line:158
    except:  # line:159
        O00OOO00000OO00OO = re.findall(r'biz=(.*?)&', OOOOOOOOO0O00O0O0)  # line:160
    if O00OOO00000OO00OO:  # line:161
        O00OOO00000OO00OO = O00OOO00000OO00OO[0]  # line:162
    else:  # line:163
        return False  # line:164
    OOO0O0O0O0O000000 = O0OO00O0OOO0O0000.xpath(
        '//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')  # line:165
    if OOO0O0O0O0O000000:  # line:166
        OOO0O0O0O0O000000 = OOO0O0O0O0O000000[0].strip()  # line:167
    O0O0O00OO0O00O00O = re.findall(r"user_name.DATA'\) : '(.*?)'", O0O0O00O000O000OO.text) or O0OO00O0OOO0O0000.xpath(
        '//span[@class="profile_meta_value"]/text()')  # line:169
    if O0O0O00OO0O00O00O:  # line:170
        O0O0O00OO0O00O00O = O0O0O00OO0O00O00O[0]  # line:171
    O0OO000O0000OOO00 = re.findall(r'createTime = \'(.*)\'', O0O0O00O000O000OO.text)  # line:172
    if O0OO000O0000OOO00:  # line:173
        O0OO000O0000OOO00 = O0OO000O0000OOO00[0][5:]  # line:174
    OOOOO0O0OO000OOOO = f'{O0OO000O0000OOO00}|{O0OOOO0OOOO0OOO00}|{O00OOO00000OO00OO}|{OOO0O0O0O0O000000}|{O0O0O00OO0O00O00O}'  # line:175
    O0O0O00O00OO00OO0 = {'biz': O00OOO00000OO00OO, 'text': OOOOO0O0OO000OOOO}  # line:176
    return O0O0O00O00OO00OO0  # line:177


class YDZ:  # line:180
    def __init__(OOO0OOO0O00O0OO00, O00OOO00O0OO00O0O):  # line:181
        OOO0OOO0O00O0OO00.name = O00OOO00O0OO00O0O.get('name')  # line:182
        OOO0OOO0O00O0OO00.s = requests.session()  # line:183
        OOO0OOO0O00O0OO00.ck = O00OOO00O0OO00O0O.get('ck')  # line:184
        OOO0OOO0O00O0OO00.msg = ''  # line:185
        OOO0OOO0O00O0OO00.s.headers = {'Proxy-Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1',
                                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8431 Flue',
                                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                       'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                                       'a_h_n': f'http%3A%2F%2F5851535337.udqyeba.cn%2F%3Fjgwq%3D3340348%26goid%3Ditrb/{OOO0OOO0O00O0OO00.ck}',
                                       'cookie': f'7bfe3c8f4d51851={OOO0OOO0O00O0OO00.ck}'}  # line:192

    def init(O0OO0O0OO0OO000OO):  # line:194
        try:  # line:195
            OO00O0OO0OO0OO0OO = 'http://5851599460.udqyeba.cn/?jgwq=3340348&goid=itrb'  # line:196
            OOOO0OOO00OO00OO0 = O0OO0O0OO0OO000OO.s.get(OO00O0OO0OO0OO0OO).text  # line:197
            OOOO0OOO00OO00OO0 = re.sub('\s', '', OOOO0OOO00OO00OO0)  # line:199
            O0OO0O0OO0OO000OO.nickname = re.findall(r'nname=\'(.*?)\',', OOOO0OOO00OO00OO0)[0]  # line:200
            OO0000O000OOOO000 = re.findall(r'uid=\'(\d+)\'', OOOO0OOO00OO00OO0)[0]  # line:201
            O0O00OO0OO00OOOO0 = f'http://58515{random.randint(10000, 99999)}.udqyeba.cn/?jgwq={OO0000O000OOOO000}&goid=itrb/{O0OO0O0OO0OO000OO.ck}'  # line:202
            O0OO0O0OO0OO000OO.s.headers.update({'a_h_n': O0O00OO0OO00OOOO0})  # line:203
            return True  # line:204
        except:  # line:205
            printlog(f'{O0OO0O0OO0OO000OO.name} 账号信息获取错误，请检查ck有效性')  # line:206
            O0OO0O0OO0OO000OO.msg += '账号信息获取错误，请检查ck有效性\n'  # line:207
            return False  # line:208

    def getinfo(OO00O0O0OOO00O0OO):  # line:210
        OOO0O000O0OO00OOO = 'http://wxr.jjyii.com/user/getinfo?v=3'  # line:211
        O00OOOOOOO000OOO0 = OO00O0O0OOO00O0OO.s.get(OOO0O000O0OO00OOO).json()  # line:212
        debugger(f'getinfo2 {O00OOOOOOO000OOO0}')  # line:213
        O0OOO00O0O00OO00O = O00OOOOOOO000OOO0.get('data')  # line:214
        OO00O0O0OOO00O0OO.count = O0OOO00O0O00OO00O.get('count')  # line:215
        OO00O0O0OOO00O0OO.gold = O0OOO00O0O00OO00O.get('balance')  # line:216
        O0OO00OO00O0OO00O = O0OOO00O0O00OO00O.get('hm')  # line:217
        O0OO0OO00O0O0OOOO = O0OOO00O0O00OO00O.get('hs')  # line:218
        printlog(
            f'账号:{OO00O0O0OOO00O0OO.nickname},当前金币{OO00O0O0OOO00O0OO.gold}，今日已读{OO00O0O0OOO00O0OO.count}')  # line:219
        OO00O0O0OOO00O0OO.msg += f'账号:{OO00O0O0OOO00O0OO.nickname},当前金币{OO00O0O0OOO00O0OO.gold}，今日已读{OO00O0O0OOO00O0OO.count}\n'  # line:220
        if O0OO00OO00O0OO00O != 0 or O0OO0OO00O0O0OOOO != 0:  # line:221
            printlog(f'{OO00O0O0OOO00O0OO.nickname} 本轮次已结束，{O0OO00OO00O0OO00O}分钟后可继续任务')  # line:222
            OO00O0O0OOO00O0OO.msg += '本轮次已结束，{hm}分钟后可继续任务\n'  # line:223
            return False  # line:224
        return True  # line:225

    def read(O0OO00O0OO0OOOOOO):  # line:227
        O000OOOOO0OOOOO00 = 'http://wxr.jjyii.com/r/get?v=10'  # line:228
        OO0OOOOO0OO00000O = {'o': f'http://58517{random.randint(10000, 99999)}.ulzqwjf.cn/?a=gt', 'goid': 'itrb',
                             '_v': '3890', 't': 'quick'}  # line:230
        OO00OOOOO0000OO0O = 0  # line:231
        OOOO0OO0O0O0O0O0O = 0  # line:232
        while OO00OOOOO0000OO0O < 30 and OOOO0OO0O0O0O0O0O < 5:  # line:233
            if not O0OO00O0OO0OOOOOO.getinfo():  # line:234
                break  # line:235
            O00OOOO0OO000O000 = O0OO00O0OO0OOOOOO.s.post(O000OOOOO0OOOOO00, data=OO0OOOOO0OO00000O).json()  # line:236
            debugger(f'read {O00OOOO0OO000O000}')  # line:237
            O00O000O0O0O00000 = O00OOOO0OO000O000.get('data').get('url')  # line:238
            if not O00O000O0O0O00000:  # line:239
                printlog(f'{O0OO00O0OO0OOOOOO.nickname} 没有获取到阅读链接，正在重试')  # line:240
                O0OO00O0OO0OOOOOO.msg += '没有获取到阅读链接，正在重试\n'  # line:241
                time.sleep(5)  # line:242
                OOOO0OO0O0O0O0O0O += 1  # line:243
                continue  # line:244
            O0O0000000OO000O0 = getmpinfo(O00O000O0O0O00000)  # line:245
            try:  # line:246
                printlog(f'{O0OO00O0OO0OOOOOO.nickname} 正在阅读 {O0O0000000OO000O0["text"]}')  # line:247
                O0OO00O0OO0OOOOOO.msg += f'正在阅读 {O0O0000000OO000O0["text"]}\n'  # line:248
            except:  # line:249
                printlog(f'{O0OO00O0OO0OOOOOO.nickname} 正在阅读 {O0O0000000OO000O0["biz"]}')  # line:250
                O0OO00O0OO0OOOOOO.msg += f'正在阅读 {O0O0000000OO000O0["biz"]}\n'  # line:251
            if 'chksm=' in O00O000O0O0O00000:  # line:252
                printlog(f'{O0OO00O0OO0OOOOOO.nickname} 正在阅读检测文章，发送通知，暂停60秒')  # line:253
                O0OO00O0OO0OOOOOO.msg += '正在阅读检测文章，发送通知，暂停60秒\n'  # line:254
                if sendable:  # line:255
                    send(f'{O0OO00O0OO0OOOOOO.nickname}\n点击阅读检测文章', f'{O0OO00O0OO0OOOOOO.name} 阅读赚过检测',
                         O00O000O0O0O00000)  # line:256
                if pushable:  # line:257
                    push(f'{O0OO00O0OO0OOOOOO.nickname}\n点击阅读检测文章\n{O0O0000000OO000O0["text"]}',
                         f'{O0OO00O0OO0OOOOOO.name} 阅读赚过检测', O00O000O0O0O00000)  # line:258
                time.sleep(60)  # line:259
            O0O0OO00OO0O00OO0 = random.randint(7, 10)  # line:260
            O0OO00O0OO0OOOOOO.msg += '模拟阅读{t}秒\n'  # line:261
            time.sleep(O0O0OO00OO0O00OO0)  # line:262
            O0O0O0O000OOOO000 = 'http://wxr.jjyii.com/r/ck'  # line:263
            OOOO0OOO000O000OO = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                                 'Origin': 'http://5851780833.ebrmrwy.cn',
                                 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', }  # line:266
            O0OO00O0OO0OOOOOO.s.headers.update(OOOO0OOO000O000OO)  # line:267
            O00OOOO0OO000O000 = O0OO00O0OO0OOOOOO.s.post(O0O0O0O000OOOO000, data={'t': 'quick'}).json()  # line:268
            debugger(f'check {O00OOOO0OO000O000}')  # line:269
            OO0OOOO0OOOOOOOO0 = O00OOOO0OO000O000.get('data').get('gold')  # line:270
            if OO0OOOO0OOOOOOOO0:  # line:271
                printlog(f'{O0OO00O0OO0OOOOOO.nickname} 阅读成功，获得金币{OO0OOOO0OOOOOOOO0}')  # line:272
                O0OO00O0OO0OOOOOO.msg += f'阅读成功，获得金币{OO0OOOO0OOOOOOOO0}\n'  # line:273
            OO00OOOOO0000OO0O += 1  # line:274

    def cash(OO00O000O00O0O0O0):  # line:276
        if OO00O000O00O0O0O0.gold < txbz:  # line:277
            printlog(f'{OO00O000O00O0O0O0.nickname} 你的金币不多了')  # line:278
            OO00O000O00O0O0O0.msg += '你的金币不多了\n'  # line:279
            return False  # line:280
        O00OOOO00OOOO0OO0 = int(OO00O000O00O0O0O0.gold / 1000) * 1000  # line:281
        printlog(f'{OO00O000O00O0O0O0.nickname} 本次提现：{O00OOOO00OOOO0OO0}')  # line:282
        OO00O000O00O0O0O0.msg += f'本次提现：{O00OOOO00OOOO0OO0}\n'  # line:283
        OOOOO000OO0000O00 = 'http://wxr.jjyii.com/mine/cash'  # line:284
        O00OO0OOO00OO00O0 = OO00O000O00O0O0O0.s.post(OOOOO000OO0000O00)  # line:285
        if O00OO0OOO00OO00O0.json().get('code') == 1:  # line:286
            printlog(f'{OO00O000O00O0O0O0.nickname} 提现成功')  # line:287
            OO00O000O00O0O0O0.msg += '提现成功\n'  # line:288
        else:  # line:289
            debugger(O00OO0OOO00OO00O0.text)  # line:290
            printlog(f'{OO00O000O00O0O0O0.nickname} 提现失败')  # line:291
            OO00O000O00O0O0O0.msg += '提现失败\n'  # line:292

    def run(OOOOO000O0O0OOOO0):  # line:294
        if OOOOO000O0O0OOOO0.init():  # line:295
            OOOOO000O0O0OOOO0.read()  # line:296
        OOOOO000O0O0OOOO0.cash()  # line:297
        if not printf:  # line:298
            print(OOOOO000O0O0OOOO0.msg)  # line:299


def yd(O00000O0OOOO0O0O0):  # line:302
    while not O00000O0OOOO0O0O0.empty():  # line:303
        O00000O00O0OO0O00 = O00000O0OOOO0O0O0.get()  # line:304
        OOO00OO00OOO0OOO0 = YDZ(O00000O00O0OO0O00)  # line:305
        OOO00OO00OOO0OOO0.run()  # line:306


def get_ver():  # line:309
    O000O00O0O0000OO0 = 'kydz V0.1.5'  # line:310
    O000OOO0O00O0O0OO = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}  # line:313
    O0O000O0OOO000OO0 = requests.get(
        'https://ghproxy.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json',
        headers=O000OOO0O00O0O0OO).json()  # line:315
    O0O0OO0OO0O00OOO0 = O000O00O0O0000OO0.split(' ')[1]  # line:316
    OO0OO0O0OO000000O = O0O000O0OOO000OO0.get('version').get(O000O00O0O0000OO0.split(' ')[0])  # line:317
    O00O00OO00O00OO0O = f"当前版本 {O0O0OO0OO0O00OOO0}，仓库版本 {OO0OO0O0OO000000O}"  # line:318
    if O0O0OO0OO0O00OOO0 < OO0OO0O0OO000000O:  # line:319
        O00O00OO00O00OO0O += '\n' + '请到https://github.com/kxs2018/xiaoym下载最新版本'  # line:320
    return O00O00OO00O00OO0O  # line:321


def main():  # line:324
    print("-" * 50 + f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n' + '-' * 50)  # line:325
    O0OOO0OOOOO0OOO0O = os.getenv('ydzck')  # line:326
    if not O0OOO0OOOOO0OOO0O:  # line:327
        print('仔细阅读脚本上方注释，配置好ydzck')  # line:328
        return False  # line:329
    try:  # line:330
        O0OOO0OOOOO0OOO0O = ast.literal_eval(O0OOO0OOOOO0OOO0O)  # line:331
    except:  # line:332
        pass  # line:333
    O0000O0O0O0O0000O = []  # line:334
    OOO0OO00OOOO0O00O = Queue()  # line:335
    for OO0OO0OOOOOO0OOOO, O00OOO00O0000O00O in enumerate(O0OOO0OOOOO0OOO0O):  # line:336
        printlog(
            f'{O00OOO00O0000O00O}\n以上是账号{OO0OO0OOOOOO0OOOO}的ck，请核对是否正确，如不正确，请检查ck填写格式')  # line:337
        OOO0OO00OOOO0O00O.put(O00OOO00O0000O00O)  # line:338
    for OO0OO0OOOOOO0OOOO in range(max_workers):  # line:339
        OOOOO0O00O0O0OOOO = threading.Thread(target=yd, args=(OOO0OO00OOOO0O00O,))  # line:340
        OOOOO0O00O0O0OOOO.start()  # line:341
        O0000O0O0O0O0000O.append(OOOOO0O00O0O0OOOO)  # line:342
        time.sleep(30)  # line:343
    for O0OO000000O000000 in O0000O0O0O0O0000O:  # line:344
        O0OO000000O000000.join()  # line:345


if __name__ == '__main__':  # line:348
    main()  # line:349
