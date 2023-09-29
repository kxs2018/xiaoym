# -*- coding: utf-8 -*-
# 元宝阅读多线程单文件版
# Author: kk
# date：2023/9/18 20:45
"""
元宝阅读入口：http://mr139508131.cwejqylmo.cloud/coin/index.html?mid=CS5T87Q98
http://u.cocozx.cn/api/ox/info
抓包 info接口的请求体中的un和token参数

注意：脚本变量使用的单引号、双引号、逗号都是英文状态的
注意：脚本变量使用的单引号、双引号、逗号都是英文状态的
注意：脚本变量使用的单引号、双引号、逗号都是英文状态的
------------------------------------------------------
内置推送企业微信群机器人
参考 https://github.com/kxs2018/yuedu/blob/main/获取企业微信群机器人key.md 获取key，并关注插件！！！

青龙配置文件
export aiock="[{'un': 'xxxx', 'token': 'xxxxx','name':'彦祖'},{'un': 'xxxx', 'token': 'xxxxx','name':'彦祖'},{'un': 'xxxx', 'token': 'xxxxx','name':'彦祖'},]"

export qwbotkey="abcdefg"
------------------------------------------------------
no module named lxml 解决方案
1. 配置文件搜索 PipMirror，如果网址包含douban的，请改为下方的网址
PipMirror="https://pypi.tuna.tsinghua.edu.cn/simple"
2. 依赖管理-python 添加 lxml
3. 如果装不上，①请ssh连接到服务器 ②docker exec -it ql bash (ql是青龙容器的名字，不会问百度) ③pip install pip -U
4. 再装不上依赖就放弃吧
------------------------------------------------------
提现标准默认是3000
达到标准自动提现
"""
import json
from random import randint
import os
import time
import requests
import ast
import re

try:
    from lxml import etree
except:
    print('请仔细阅读脚本上方注释中的“no module named lxml 解决方案”')
    exit()
import datetime
import threading
from queue import Queue

"""实时打印日志开关"""
printf = 1
"""1为开，0为关"""

"""debug模式开关"""
debug = 0
"""1为开，打印调试日志；0为关，不打印"""

"""线程数量设置"""
max_workers = 3
"""设置为3，即最多有3个任务同时进行"""

"""设置提现标准"""
txbz = 10000  # 不低于3000，平台的提现标准为3000
"""设置为10000，即为1元起提"""

qwbotkey = os.getenv('qwbotkey')  # line:65
if not qwbotkey:  # line:66
    print('请仔细阅读脚本开头的注释并配置好qwbotkey')  # line:67
    exit()  # line:68


def ftime():  # line:71
    OOO0OO000O00OO0OO = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # line:72
    return OOO0OO000O00OO0OO  # line:73


def printlog(O0OO000O00O0O0OO0):  # line:76
    if printf:  # line:77
        print(O0OO000O00O0O0OO0)  # line:78


def debugger(O00O00O00O00O0000):  # line:81
    if debug:  # line:82
        print(O00O00O00O00O0000)  # line:83


def send(O0000OO0O000OO00O, title='通知', url=None):  # line:86
    if not title or not url:  # line:87
        O0O000OOOOO0OO0O0 = {"msgtype": "text", "text": {
            "content": f"{title}\n\n{O0000OO0O000OO00O}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}", }}  # line:94
    else:  # line:95
        O0O000OOOOO0OO0O0 = {"msgtype": "news", "news": {"articles": [
            {"title": title, "description": O0000OO0O000OO00O, "url": url,
             "picurl": 'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}  # line:108
    OO000OO00OO00OOO0 = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'  # line:109
    OOO0O0OOO00000000 = requests.post(OO000OO00OO00OOO0, data=json.dumps(O0O000OOOOO0OO0O0)).json()  # line:110
    if OOO0O0OOO00000000.get('errcode') != 0:  # line:111
        print('消息发送失败，请检查key和发送格式')  # line:112
        return False  # line:113
    return OOO0O0OOO00000000  # line:114


def getmpinfo(OOOO00OOO000O0O00):  # line:117
    if not OOOO00OOO000O0O00 or OOOO00OOO000O0O00 == '':  # line:118
        return False  # line:119
    O0OOOOO0O00O00O00 = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}  # line:121
    OO0O0O0O0O0O000O0 = requests.get(OOOO00OOO000O0O00, headers=O0OOOOO0O00O00O00)  # line:122
    OO000O00000000O00 = etree.HTML(OO0O0O0O0O0O000O0.text)  # line:123
    OO0O0O00OO00OO0O0 = OO000O00000000O00.xpath('//meta[@*="og:title"]/@content')  # line:125
    if OO0O0O00OO00OO0O0:  # line:126
        OO0O0O00OO00OO0O0 = OO0O0O00OO00OO0O0[0]  # line:127
    OOO00OOO0000000OO = OO000O00000000O00.xpath('//meta[@*="og:url"]/@content')  # line:128
    if OOO00OOO0000000OO:  # line:129
        OOO00OOO0000000OO = OOO00OOO0000000OO[0].encode().decode()  # line:130
    try:  # line:131
        OOOOOOO0OOOO0OO00 = re.findall(r'biz=(.*?)&', OOOO00OOO000O0O00)  # line:132
    except:  # line:133
        OOOOOOO0OOOO0OO00 = re.findall(r'biz=(.*?)&', OOO00OOO0000000OO)  # line:134
    if OOOOOOO0OOOO0OO00:  # line:135
        OOOOOOO0OOOO0OO00 = OOOOOOO0OOOO0OO00[0]  # line:136
    else:  # line:137
        return False  # line:138
    O0O0OOOOOOO00OO00 = OO000O00000000O00.xpath(
        '//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')  # line:139
    if O0O0OOOOOOO00OO00:  # line:140
        O0O0OOOOOOO00OO00 = O0O0OOOOOOO00OO00[0].strip()  # line:141
    O000O0OO00OOOO00O = re.findall(r"user_name.DATA'\) : '(.*?)'", OO0O0O0O0O0O000O0.text) or OO000O00000000O00.xpath(
        '//span[@class="profile_meta_value"]/text()')  # line:143
    if O000O0OO00OOOO00O:  # line:144
        O000O0OO00OOOO00O = O000O0OO00OOOO00O[0]  # line:145
    O0000OOO0O00OOO00 = re.findall(r'createTime = \'(.*)\'', OO0O0O0O0O0O000O0.text)  # line:146
    if O0000OOO0O00OOO00:  # line:147
        O0000OOO0O00OOO00 = O0000OOO0O00OOO00[0][5:]  # line:148
    OOO0OOOOOOOO00OOO = f'{O0000OOO0O00OOO00}|{OO0O0O00OO00OO0O0}'  # line:149
    OOOO0O00OOO000000 = {'biz': OOOOOOO0OOOO0OO00, 'text': OOO0OOOOOOOO00OOO}  # line:150
    return OOOO0O00OOO000000  # line:151


class Allinone:  # line:154
    def __init__(O00OOO0O00OO00000, O00O00O0000O00O00):  # line:155
        O00OOO0O00OO00000.name = O00O00O0000O00O00['name']  # line:156
        O00OOO0O00OO00000.s = requests.session()  # line:157
        O00OOO0O00OO00000.payload = {"un": O00O00O0000O00O00['un'], "token": O00O00O0000O00O00['token'],
                                     "pageSize": 20}  # line:158
        O00OOO0O00OO00000.s.headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                                       'Content-Type': 'application/json; charset=UTF-8', 'Host': 'u.cocozx.cn',
                                       'Connection': 'keep-alive',
                                       'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",
                                       'Accept-Encoding': 'gzip, deflate'}  # line:164
        O00OOO0O00OO00000.msg = ''  # line:165

    def get_info(OO0O00OO0OOOO0O0O):  # line:167
        O00O0O00OO0000OO0 = 'CS5T87Q98' if OO0O00OO0OOOO0O0O.name == 'AI' else 'DG52AW2N6'  # line:168
        O00O0OO00OO00O0O0 = {**OO0O00OO0OOOO0O0O.payload, **{'code': O00O0O00OO0000OO0}}  # line:169
        try:  # line:170
            OOOOO00O0O00000OO = OO0O00OO0OOOO0O0O.s.post("http://u.cocozx.cn/api/coin/info",
                                                         json=O00O0OO00OO00O0O0).json()  # line:171
            OO000OOO0OO0OO000 = OOOOO00O0O00000OO.get("result")  # line:172
            debugger(f'get_info {OOOOO00O0O00000OO}')  # line:173
            OOO0O0OOO0O0OOO0O = OO000OOO0OO0OO000.get('us')  # line:174
            if OOO0O0OOO0O0OOO0O == 2:  # line:175
                OO0O00OO0OOOO0O0O.msg += f'账号：{OO0O00OO0OOOO0O0O.name}已被封\n'  # line:176
                printlog(f'账号：{OO0O00OO0OOOO0O0O.name}已被封')  # line:177
                return False  # line:178
            OO0O00OO0OOOO0O0O.msg += f"""账号:{OO0O00OO0OOOO0O0O.name}，今日阅读次数:{OO000OOO0OO0OO000["dayCount"]}，当前元宝:{OO000OOO0OO0OO000["moneyCurrent"]}，累计阅读次数:{OO000OOO0OO0OO000["doneWx"]}\n"""  # line:180
            printlog(
                f"""账号:{OO0O00OO0OOOO0O0O.name}，今日阅读次数:{OO000OOO0OO0OO000["dayCount"]}，当前元宝:{OO000OOO0OO0OO000["moneyCurrent"]}，累计阅读次数:{OO000OOO0OO0OO000["doneWx"]}""")  # line:182
            O0OOOO0O0OOO00O00 = int(OO000OOO0OO0OO000["moneyCurrent"])  # line:183
            OO0O00OO0OOOO0O0O.huid = OO000OOO0OO0OO000.get('uid')  # line:184
            return O0OOOO0O0OOO00O00  # line:185
        except:  # line:186
            return False  # line:187

    def get_readhost(OOOOO00O00OOO0O0O):  # line:189
        OO000OOO0O0O000O0 = "http://u.cocozx.cn/api/coin/getReadHost"  # line:190
        OO000OO0OO00O0OOO = OOOOO00O00OOO0O0O.s.post(OO000OOO0O0O000O0,
                                                     json=OOOOO00O00OOO0O0O.payload).json()  # line:191
        debugger(f'readhome {OO000OO0OO00O0OOO}')  # line:192
        OOOOO00O00OOO0O0O.readhost = OO000OO0OO00O0OOO.get('result')['host']  # line:193
        OOOOO00O00OOO0O0O.msg += f'邀请链接：{OOOOO00O00OOO0O0O.readhost}/oz/index.html?mid={OOOOO00O00OOO0O0O.huid}\n'  # line:194
        printlog(
            f"{OOOOO00O00OOO0O0O.name}:邀请链接：{OOOOO00O00OOO0O0O.readhost}/oz/index.html?mid={OOOOO00O00OOO0O0O.huid}")  # line:195

    def get_status(O0O000O00O0OO0O00):  # line:197
        O0OO00OOO00000000 = O0O000O00O0OO0O00.s.post("http://u.cocozx.cn/api/coin/read",
                                                     json=O0O000O00O0OO0O00.payload).json()  # line:198
        debugger(f'getstatus {O0OO00OOO00000000}')  # line:199
        O0O000O00O0OO0O00.status = O0OO00OOO00000000.get("result").get("status")  # line:200
        if O0O000O00O0OO0O00.status == 40:  # line:201
            O0O000O00O0OO0O00.msg += "文章还没有准备好\n"  # line:202
            printlog(f"{O0O000O00O0OO0O00.name}:文章还没有准备好")  # line:203
            return  # line:204
        elif O0O000O00O0OO0O00.status == 50:  # line:205
            O0O000O00O0OO0O00.msg += "阅读失效\n"  # line:206
            printlog(f"{O0O000O00O0OO0O00.name}:阅读失效")  # line:207
            return  # line:208
        elif O0O000O00O0OO0O00.status == 60:  # line:209
            O0O000O00O0OO0O00.msg += "已经全部阅读完了\n"  # line:210
            printlog(f"{O0O000O00O0OO0O00.name}:已经全部阅读完了")  # line:211
            return  # line:212
        elif O0O000O00O0OO0O00.status == 70:  # line:213
            O0O000O00O0OO0O00.msg += "下一轮还未开启\n"  # line:214
            printlog(f"{O0O000O00O0OO0O00.name}:下一轮还未开启")  # line:215
            return  # line:216
        elif O0O000O00O0OO0O00.status == 10:  # line:217
            O0OO0O00O0000O000 = O0OO00OOO00000000["result"]["url"]  # line:218
            O0O000O00O0OO0O00.msg += '-' * 50 + "\n阅读链接获取成功\n"  # line:219
            printlog(f"{O0O000O00O0OO0O00.name}: 阅读链接获取成功")  # line:220
            return O0OO0O00O0000O000  # line:221

    def submit(OOO0OOO000OOO0000):  # line:223
        O0OOO00O000O00000 = {**{'type': 1}, **OOO0OOO000OOO0000.payload}  # line:224
        O00OOOOOOOOOO0OO0 = OOO0OOO000OOO0000.s.post("http://u.cocozx.cn/api/coin/submit?zx=&xz=1",
                                                     json=O0OOO00O000O00000)  # line:225
        OOO0O0OO000O0O0OO = O00OOOOOOOOOO0OO0.json().get('result')  # line:226
        debugger('submit ' + O00OOOOOOOOOO0OO0.text)  # line:227
        OOO0OOO000OOO0000.msg += f"阅读成功,获得元宝{OOO0O0OO000O0O0OO['val']}，当前剩余次数:{OOO0O0OO000O0O0OO['progress']}\n"  # line:228
        printlog(
            f"{OOO0OOO000OOO0000.name}:阅读成功,获得元宝{OOO0O0OO000O0O0OO['val']}，当前剩余次数:{OOO0O0OO000O0O0OO['progress']}")  # line:229

    def read(OO00O0O0O0O0000O0):  # line:231
        while True:  # line:232
            OO000O0OOO0O0OOOO = OO00O0O0O0O0000O0.get_status()  # line:233
            if not OO000O0OOO0O0OOOO:  # line:234
                if OO00O0O0O0O0000O0.status == 30:  # line:235
                    time.sleep(3)  # line:236
                    continue  # line:237
                break  # line:238
            O0OOOOOO0OOO00OO0 = getmpinfo(OO000O0OOO0O0OOOO)  # line:239
            if not O0OOOOOO0OOO00OO0:  # line:240
                printlog(f'{OO00O0O0O0O0000O0.name}:获取文章信息失败，程序中止')  # line:241
                return False  # line:242
            OO00O0O0O0O0000O0.msg += '开始阅读 ' + O0OOOOOO0OOO00OO0['text'] + '\n'  # line:243
            printlog(f'{OO00O0O0O0O0000O0.name}:开始阅读 ' + O0OOOOOO0OOO00OO0['text'])  # line:244
            O0OOOO000OOOOOO00 = randint(7, 10)  # line:245
            if O0OOOOOO0OOO00OO0['biz'] == "Mzg2Mzk3Mjk5NQ==":  # line:246
                OO00O0O0O0O0000O0.msg += '正在阅读检测文章\n'  # line:247
                printlog(f'{OO00O0O0O0O0000O0.name}:正在阅读检测文章')  # line:248
                send(f'{OO00O0O0O0O0000O0.name}  元宝阅读过检测', O0OOOOOO0OOO00OO0['text'],
                     OO000O0OOO0O0OOOO)  # line:249
                time.sleep(60)  # line:250
            printlog(f'模拟阅读{O0OOOO000OOOOOO00}秒')  # line:251
            time.sleep(O0OOOO000OOOOOO00)  # line:252
            OO00O0O0O0O0000O0.submit()  # line:253

    def tixian(OOOOO0O00OOOO000O):  # line:255
        global txe  # line:256
        OOOO0000000O000O0 = OOOOO0O00OOOO000O.get_info()  # line:257
        if OOOO0000000O000O0 < txbz:  # line:258
            OOOOO0O00OOOO000O.msg += '你的元宝已不足\n'  # line:259
            printlog(f'{OOOOO0O00OOOO000O.name}你的元宝已不足')  # line:260
            return False  # line:261
        elif 10000 <= OOOO0000000O000O0 < 49999:  # line:262
            txe = 10000  # line:263
        elif 50000 <= OOOO0000000O000O0 < 100000:  # line:264
            txe = 50000  # line:265
        elif 3000 <= OOOO0000000O000O0 < 10000:  # line:266
            txe = 3000  # line:267
        elif OOOO0000000O000O0 >= 100000:  # line:268
            txe = 100000  # line:269
        OOOOO0O00OOOO000O.msg += f"提现金额:{txe}\n"  # line:270
        printlog(f'{OOOOO0O00OOOO000O.name}提现金额:{txe}')  # line:271
        OO000OOOOOO0O00O0 = "http://u.cocozx.cn/api/coin/wdmoney"  # line:272
        O0O0O0OOO0OOO0O00 = {**OOOOO0O00OOOO000O.payload, **{"val": txe}}  # line:273
        try:  # line:274
            O0000O0OOO0O0O0OO = OOOOO0O00OOOO000O.s.post(OO000OOOOOO0O00O0, json=O0O0O0OOO0OOO0O00).json()  # line:275
            OOOOO0O00OOOO000O.msg += f'提现结果：{O0000O0OOO0O0O0OO.get("msg")}\n'  # line:276
            printlog(f'{OOOOO0O00OOOO000O.name}提现结果：{O0000O0OOO0O0O0OO.get("msg")}')  # line:277
        except:  # line:278
            OOOOO0O00OOOO000O.msg += f"自动提现不成功，发送通知手动提现\n"  # line:279
            printlog(f"{OOOOO0O00OOOO000O.name}:自动提现不成功，发送通知手动提现")  # line:280
            send(f'可提现金额 {int(txe) / 10000}元，点击提现',
                 title=f'惜之酱提醒您 {OOOOO0O00OOOO000O.name} 元宝阅读可以提现了',
                 url=f'{OOOOO0O00OOOO000O.readhost}/coin/index.html?mid=CS5T87Q98')  # line:282

    def run(O00OOOO00OOO00OO0):  # line:284
        if O00OOOO00OOO00OO0.get_info():  # line:285
            O00OOOO00OOO00OO0.get_readhost()  # line:286
            O00OOOO00OOO00OO0.read()  # line:287
            O00OOOO00OOO00OO0.tixian()  # line:288
        if not printf:  # line:289
            print(O00OOOO00OOO00OO0.msg.strip())  # line:290


def yd(O0OOO0OOO0O000O00):  # line:293
    while not O0OOO0OOO0O000O00.empty():  # line:294
        O0O0O0O0O000O00OO = O0OOO0OOO0O000O00.get()  # line:295
        O00OOO00OO00000O0 = Allinone(O0O0O0O0O000O00OO)  # line:296
        O00OOO00OO00000O0.run()  # line:297


def get_ver():  # line:300
    OOOOO0O0O00O0000O = 'kyb V1.2.1'  # line:301
    O0000O0OO0O0O00OO = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}  # line:304
    OO00O0O0O0000O000 = requests.get(
        'https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',
        headers=O0000O0OO0O0O00OO).json()  # line:306
    O0O0O0OO0OOOO0OOO = OOOOO0O0O00O0000O.split(' ')[1]  # line:307
    O00O0OOO000OO0OO0 = OO00O0O0O0000O000.get('version').get(OOOOO0O0O00O0000O.split(' ')[0])  # line:308
    O00OOOO0OOO0OOO00 = f"当前版本 {O0O0O0OO0OOOO0OOO}，仓库版本 {O00O0OOO000OO0OO0}"  # line:309
    if O0O0O0OO0OOOO0OOO < O00O0OOO000OO0OO0:  # line:310
        O00OOOO0OOO0OOO00 += '\n' + '请到https://github.com/kxs2018/xiaoym下载最新版本'  # line:311
    return O00OOOO0OOO0OOO00  # line:312


def main():  # line:315
    print("-" * 50 + f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n' + '-' * 50)  # line:316
    OOO00OOOOOOO00OOO = os.getenv('aiock')  # line:317
    if not OOO00OOOOOOO00OOO:  # line:318
        print('请仔细阅读脚本开头的注释并配置好aiock')  # line:319
        exit()  # line:320
    try:  # line:321
        OOO00OOOOOOO00OOO = ast.literal_eval(OOO00OOOOOOO00OOO)  # line:322
    except:  # line:323
        pass  # line:324
    O0O00O0O0OOO0OOO0 = Queue()  # line:325
    OOOO0000OOO0OO000 = []  # line:326
    for OOO0O00O0O00O0000, OOO00OO0OOO00OO0O in enumerate(OOO00OOOOOOO00OOO, start=1):  # line:327
        printlog(
            f'{OOO00OO0OOO00OO0O}\n以上是账号{OOO0O00O0O00O0000}的ck，请核对是否正确，如不正确，请检查ck填写格式')  # line:328
        O0O00O0O0OOO0OOO0.put(OOO00OO0OOO00OO0O)  # line:329
    for OOO0O00O0O00O0000 in range(max_workers):  # line:330
        OOOOOOO0OO00OOOOO = threading.Thread(target=yd, args=(O0O00O0O0OOO0OOO0,))  # line:331
        OOOOOOO0OO00OOOOO.start()  # line:332
        OOOO0000OOO0OO000.append(OOOOOOO0OO00OOOOO)  # line:333
        time.sleep(30)  # line:334
    for O0O0000O0OOO00O0O in OOOO0000OOO0OO000:  # line:335
        O0O0000O0OOO00O0O.join()  # line:336


if __name__ == '__main__':  # line:339
    main()  # line:340
