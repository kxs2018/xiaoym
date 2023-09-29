"""
智慧阅读入口：http://mr1694397085936.qmpcsxu.cn/oz/index.html?mid=QX5E9WLGS

http://u.cocozx.cn/api/ox/info
抓包 info接口的请求体中的un和token参数

注意：脚本变量使用的单引号、双引号、逗号都是英文状态的
注意：脚本变量使用的单引号、双引号、逗号都是英文状态的
注意：脚本变量使用的单引号、双引号、逗号都是英文状态的
------------------------------------------------------
内置推送企业微信群机器人
参考 https://github.com/kxs2018/yuedu/blob/main/获取企业微信群机器人key.md 获取key，并关注插件！！！

青龙配置文件
export aiock='''[{"un": "xxxx", "token": "xxxxx","name":"彦祖"}]'''
export qwbotkey="abcdefg"
------------------------------------------------------
no module named lxml 解决方案
1. 配置文件搜索 PipMirror，如果网址包含douban的，请改为下方的网址
PipMirror="https://pypi.tuna.tsinghua.edu.cn/simple"
2. 依赖管理-python 添加 lxml
3. 如果装不上，①请ssh连接到服务器 ②docker exec -it ql bash (ql是青龙容器的名字，docker ps可查看) ③pip install pip -U
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

qwbotkey = os.getenv('qwbotkey')  # line:62
if not qwbotkey:  # line:63
    print('请仔细阅读脚本开头的注释并配置好qwbotkey')  # line:64
    exit()  # line:65


def ftime():  # line:68
    O00000000O0OOO0O0 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # line:69
    return O00000000O0OOO0O0  # line:70


def debugger(OO00000OO000O0OOO):  # line:73
    if debug:  # line:74
        print(OO00000OO000O0OOO)  # line:75


def printlog(O0OOO00OOOO0OOOOO):  # line:78
    if printf:  # line:79
        print(O0OOO00OOOO0OOOOO)  # line:80


def send(OO0O0OOO000OOO0OO, title='通知', url=None):  # line:83
    if not title or not url:  # line:84
        O0O0O00O00OO0OOO0 = {"msgtype": "text", "text": {
            "content": f"{title}\n\n{OO0O0OOO000OOO0OO}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}", }}  # line:91
    else:  # line:92
        O0O0O00O00OO0OOO0 = {"msgtype": "news", "news": {"articles": [
            {"title": title, "description": OO0O0OOO000OOO0OO, "url": url,
             "picurl": 'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}  # line:105
    OOO000O00000OOOOO = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'  # line:106
    O0OO0O0O00OO0O000 = requests.post(OOO000O00000OOOOO, data=json.dumps(O0O0O00O00OO0OOO0)).json()  # line:107
    if O0OO0O0O00OO0O000.get('errcode') != 0:  # line:108
        print('消息发送失败，请检查key和发送格式')  # line:109
        return False  # line:110
    return O0OO0O0O00OO0O000  # line:111


def getmpinfo(O0O000OOOOO00OOO0):  # line:114
    if not O0O000OOOOO00OOO0 or O0O000OOOOO00OOO0 == '':  # line:115
        return False  # line:116
    O0OO00O00O000OOOO = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}  # line:118
    OOO00O0OOO0OO0O00 = requests.get(O0O000OOOOO00OOO0, headers=O0OO00O00O000OOOO)  # line:119
    OOO0OO0O0OOOO00OO = etree.HTML(OOO00O0OOO0OO0O00.text)  # line:120
    OOOO0O000000OOOO0 = OOO0OO0O0OOOO00OO.xpath('//meta[@*="og:title"]/@content')  # line:122
    if OOOO0O000000OOOO0:  # line:123
        OOOO0O000000OOOO0 = OOOO0O000000OOOO0[0]  # line:124
    O0OOO0O00O000O00O = OOO0OO0O0OOOO00OO.xpath('//meta[@*="og:url"]/@content')  # line:125
    if O0OOO0O00O000O00O:  # line:126
        O0OOO0O00O000O00O = O0OOO0O00O000O00O[0].encode().decode()  # line:127
    try:  # line:128
        O0O0OO0OO00000O0O = re.findall(r'biz=(.*?)&', O0O000OOOOO00OOO0)  # line:129
    except:  # line:130
        O0O0OO0OO00000O0O = re.findall(r'biz=(.*?)&', O0OOO0O00O000O00O)  # line:131
    if O0O0OO0OO00000O0O:  # line:132
        O0O0OO0OO00000O0O = O0O0OO0OO00000O0O[0]  # line:133
    else:  # line:134
        return False  # line:135
    OO0O00O0000000OOO = OOO0OO0O0OOOO00OO.xpath(
        '//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')  # line:136
    if OO0O00O0000000OOO:  # line:137
        OO0O00O0000000OOO = OO0O00O0000000OOO[0].strip()  # line:138
    O0000O000O00O00OO = re.findall(r"user_name.DATA'\) : '(.*?)'", OOO00O0OOO0OO0O00.text) or OOO0OO0O0OOOO00OO.xpath(
        '//span[@class="profile_meta_value"]/text()')  # line:140
    if O0000O000O00O00OO:  # line:141
        O0000O000O00O00OO = O0000O000O00O00OO[0]  # line:142
    O000OOOOOO0OO00OO = re.findall(r'createTime = \'(.*)\'', OOO00O0OOO0OO0O00.text)  # line:143
    if O000OOOOOO0OO00OO:  # line:144
        O000OOOOOO0OO00OO = O000OOOOOO0OO00OO[0][5:]  # line:145
    OOO00O00000000OO0 = f'{O000OOOOOO0OO00OO} {OOOO0O000000OOOO0}'  # line:146
    O0OOO0000OOOO0OO0 = {'biz': O0O0OO0OO00000O0O, 'text': OOO00O00000000OO0}  # line:147
    return O0OOO0000OOOO0OO0  # line:148


class Allinone:  # line:151
    def __init__(O0O000O0000OOO000, OO000O0OOOO00OOO0):  # line:152
        O0O000O0000OOO000.name = OO000O0OOOO00OOO0['name']  # line:153
        O0O000O0000OOO000.s = requests.session()  # line:154
        O0O000O0000OOO000.payload = {"un": OO000O0OOOO00OOO0['un'], "token": OO000O0OOOO00OOO0['token'],
                                     "pageSize": 20}  # line:155
        O0O000O0000OOO000.s.headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                                       'Content-Type': 'application/json; charset=UTF-8', 'Host': 'u.cocozx.cn',
                                       'Connection': 'keep-alive', 'Origin': 'http://mr1694957965536.qwydu.com',
                                       'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",
                                       'Accept-Encoding': 'gzip, deflate'}  # line:162
        O0O000O0000OOO000.headers = O0O000O0000OOO000.s.headers.copy()  # line:163
        O0O000O0000OOO000.msg = ''  # line:164

    def get_readhost(O0O00OOOO00OOOOOO):  # line:166
        O0000OOO0OOO0OOOO = "http://u.cocozx.cn/api/oz/getReadHost"  # line:167
        O0OOOOO0OO0O000O0 = O0O00OOOO00OOOOOO.s.post(O0000OOO0OOO0OOOO,
                                                     json=O0O00OOOO00OOOOOO.payload).json()  # line:168
        debugger(f'readhome {O0OOOOO0OO0O000O0}')  # line:169
        O0O00OOOO00OOOOOO.readhost = O0OOOOO0OO0O000O0.get('result')['host']  # line:170
        O0O00OOOO00OOOOOO.headers['Origin'] = O0O00OOOO00OOOOOO.readhost  # line:171
        O0O00OOOO00OOOOOO.msg += f'邀请链接：{O0O00OOOO00OOOOOO.readhost}/oz/index.html?mid={O0O00OOOO00OOOOOO.huid}\n'  # line:172
        printlog(
            f"{O0O00OOOO00OOOOOO.name}:邀请链接：{O0O00OOOO00OOOOOO.readhost}/oz/index.html?mid={O0O00OOOO00OOOOOO.huid}")  # line:173

    def get_info(OO0OOO00OOOOOO000):  # line:175
        OO00O000OOOOO00O0 = 'QX5E9WLGS' if OO0OOO00OOOOOO000.name == 'AI' else '4G7QUZY8Y'  # line:176
        O0O0O0000O00OO00O = {**OO0OOO00OOOOOO000.payload, **{'code': OO00O000OOOOO00O0}}  # line:177
        try:  # line:178
            OO00000O0OOOOO0O0 = OO0OOO00OOOOOO000.s.post("http://u.cocozx.cn/api/oz/info",
                                                         json=O0O0O0000O00OO00O).json()  # line:179
            OO00O0O0000O00000 = OO00000O0OOOOO0O0.get("result")  # line:180
            debugger(f'get_info {OO00000O0OOOOO0O0}')  # line:181
            OO0O00O00000OO000 = OO00O0O0000O00000.get('us')  # line:182
            if OO0O00O00000OO000 == 2:  # line:183
                OO0OOO00OOOOOO000.msg += f'账号：{OO0OOO00OOOOOO000.name}已被封\n'  # line:184
                printlog(f'账号：{OO0OOO00OOOOOO000.name}已被封')  # line:185
                return False  # line:186
            OO0OOO00OOOOOO000.msg += f"""账号:{OO0OOO00OOOOOO000.name}，今日阅读次数:{OO00O0O0000O00000["dayCount"]}，当前智慧:{OO00O0O0000O00000["moneyCurrent"]}，累计阅读次数:{OO00O0O0000O00000["doneWx"]}\n"""  # line:187
            printlog(
                f"""账号:{OO0OOO00OOOOOO000.name}，今日阅读次数:{OO00O0O0000O00000["dayCount"]}，当前智慧:{OO00O0O0000O00000["moneyCurrent"]}，累计阅读次数:{OO00O0O0000O00000["doneWx"]}""")  # line:189
            OO00OO0O0OOOO00OO = int(OO00O0O0000O00000["moneyCurrent"])  # line:190
            OO0OOO00OOOOOO000.huid = OO00O0O0000O00000.get('uid')  # line:191
            return OO00OO0O0OOOO00OO  # line:192
        except:  # line:193
            return False  # line:194

    def get_status(OOO0OOO00OOO0O000):  # line:196
        O000000O000OO00O0 = requests.post("http://u.cocozx.cn/api/oz/read", headers=OOO0OOO00OOO0O000.headers,
                                          json=OOO0OOO00OOO0O000.payload).json()  # line:197
        debugger(f'getstatus {O000000O000OO00O0}')  # line:198
        OOO0OOO00OOO0O000.status = O000000O000OO00O0.get("result").get("status")  # line:199
        if OOO0OOO00OOO0O000.status == 40:  # line:200
            OOO0OOO00OOO0O000.msg += "文章还没有准备好\n"  # line:201
            printlog(f"{OOO0OOO00OOO0O000.name}:文章还没有准备好")  # line:202
            return  # line:203
        elif OOO0OOO00OOO0O000.status == 50:  # line:204
            OOO0OOO00OOO0O000.msg += "阅读失效\n"  # line:205
            printlog(f"{OOO0OOO00OOO0O000.name}:阅读失效")  # line:206
            return  # line:207
        elif OOO0OOO00OOO0O000.status == 60:  # line:208
            OOO0OOO00OOO0O000.msg += "已经全部阅读完了\n"  # line:209
            printlog(f"{OOO0OOO00OOO0O000.name}:已经全部阅读完了")  # line:210
            return  # line:211
        elif OOO0OOO00OOO0O000.status == 70:  # line:212
            OOO0OOO00OOO0O000.msg += "下一轮还未开启\n"  # line:213
            printlog(f"{OOO0OOO00OOO0O000.name}:下一轮还未开启")  # line:214
            return  # line:215
        elif OOO0OOO00OOO0O000.status == 10:  # line:216
            O00O000O0O00000OO = O000000O000OO00O0["result"]["url"]  # line:217
            OOO0OOO00OOO0O000.msg += '-' * 50 + "\n阅读链接获取成功\n"  # line:218
            printlog(f"{OOO0OOO00OOO0O000.name}:阅读链接获取成功")  # line:219
            return O00O000O0O00000OO  # line:220

    def submit(OOO00OO0000O00OOO):  # line:222
        OOO0O000OOOOO0000 = {**{'type': 1}, **OOO00OO0000O00OOO.payload}  # line:223
        O0OO00OO0000000OO = requests.post("http://u.cocozx.cn/api/oz/submit?zx=&xz=1",
                                          headers=OOO00OO0000O00OOO.headers, json=OOO0O000OOOOO0000)  # line:224
        OOO0OOO000OO00OOO = O0OO00OO0000000OO.json().get('result')  # line:225
        debugger('submit ' + O0OO00OO0000000OO.text)  # line:226
        OOO00OO0000O00OOO.msg += f"阅读成功,获得智慧{OOO0OOO000OO00OOO['val']}，当前剩余次数:{OOO0OOO000OO00OOO['progress']}\n"  # line:227
        printlog(
            f"{OOO00OO0000O00OOO.name}:阅读成功,获得智慧{OOO0OOO000OO00OOO['val']}，当前剩余次数:{OOO0OOO000OO00OOO['progress']}")  # line:228

    def read(O0000O000OO0O0000):  # line:230
        O00000O0O000O00O0 = 1  # line:231
        while True:  # line:232
            O00000O0O00O000OO = O0000O000OO0O0000.get_status()  # line:233
            if not O00000O0O00O000OO:  # line:234
                if O0000O000OO0O0000.status == 30:  # line:235
                    time.sleep(3)  # line:236
                    continue  # line:237
                break  # line:238
            OO0O0O0000OO00O00 = getmpinfo(O00000O0O00O000OO)  # line:239
            O0000O000OO0O0000.msg += '开始阅读 ' + OO0O0O0000OO00O00['text'] + '\n'  # line:240
            printlog(f'{O0000O000OO0O0000.name}:开始阅读 ' + OO0O0O0000OO00O00['text'])  # line:241
            OOOO00OO00O00OOO0 = randint(7, 10)  # line:242
            if OO0O0O0000OO00O00['biz'] == "Mzg2Mzk3Mjk5NQ==":  # line:243
                O0000O000OO0O0000.msg += '当前正在阅读检测文章\n'  # line:244
                printlog(f'{O0000O000OO0O0000.name}:正在阅读检测文章')  # line:245
                send(f'{O0000O000OO0O0000.name}  智慧阅读正在读检测文章', OO0O0O0000OO00O00['text'],
                     O00000O0O00O000OO)  # line:246
                time.sleep(60)  # line:247
            printlog(f'{O0000O000OO0O0000.name}：模拟阅读{OOOO00OO00O00OOO0}秒')  # line:248
            time.sleep(OOOO00OO00O00OOO0)  # line:249
            O0000O000OO0O0000.submit()  # line:250

    def tixian(O0O00O00000000OOO):  # line:252
        global txe  # line:253
        OO0O0OO0OO0OOO0OO = O0O00O00000000OOO.get_info()  # line:254
        if OO0O0OO0OO0OOO0OO < txbz:  # line:255
            O0O00O00000000OOO.msg += '你的智慧不多了\n'  # line:256
            printlog(f'{O0O00O00000000OOO.name}你的智慧不多了')  # line:257
            return False  # line:258
        elif 10000 <= OO0O0OO0OO0OOO0OO < 49999:  # line:259
            txe = 10000  # line:260
        elif 50000 <= OO0O0OO0OO0OOO0OO < 100000:  # line:261
            txe = 50000  # line:262
        elif 3000 <= OO0O0OO0OO0OOO0OO < 10000:  # line:263
            txe = 3000  # line:264
        elif OO0O0OO0OO0OOO0OO >= 100000:  # line:265
            txe = 100000  # line:266
        O0O00O00000000OOO.msg += f"提现金额:{txe}\n"  # line:267
        printlog(f'{O0O00O00000000OOO.name}提现金额:{txe}')  # line:268
        O0O00O000OO0O00OO = {**O0O00O00000000OOO.payload, **{"val": txe}}  # line:269
        try:  # line:270
            O00OO0OO00OOOOO0O = O0O00O00000000OOO.s.post("http://u.cocozx.cn/api/oz/wdmoney",
                                                         json=O0O00O000OO0O00OO).json()  # line:271
            O0O00O00000000OOO.msg += f'提现结果：{O00OO0OO00OOOOO0O.get("msg")}\n'  # line:272
            printlog(f'{O0O00O00000000OOO.name}提现结果：{O00OO0OO00OOOOO0O.get("msg")}')  # line:273
        except:  # line:274
            O0O00O00000000OOO.msg += f"自动提现不成功，发送通知手动提现\n"  # line:275
            printlog(f"{O0O00O00000000OOO.name}:自动提现不成功，发送通知手动提现")  # line:276
            send(f'可提现金额 {int(txe) / 10000}元，点击提现',
                 title=f'惜之酱提醒您 {O0O00O00000000OOO.name} 智慧阅读可以提现了',
                 url=f'{O0O00O00000000OOO.readhost}/oz/index.html?mid=QX5E9WLGS')  # line:278

    def run(O0O0OOOO00O000OOO):  # line:280
        O0O0OOOO00O000OOO.msg += '*' * 50 + '\n'  # line:281
        if O0O0OOOO00O000OOO.get_info():  # line:282
            O0O0OOOO00O000OOO.get_readhost()  # line:283
            O0O0OOOO00O000OOO.read()  # line:284
            O0O0OOOO00O000OOO.tixian()  # line:285
        if not printf:  # line:286
            print(O0O0OOOO00O000OOO.msg.strip())  # line:287


def yd(OOO0O0OO0OOOO0000):  # line:290
    while not OOO0O0OO0OOOO0000.empty():  # line:291
        O0OO0O00O000OOO0O = OOO0O0OO0OOOO0000.get()  # line:292
        OOOO0OOOOO00OO0OO = Allinone(O0OO0O00O000OOO0O)  # line:293
        OOOO0OOOOO00OO0OO.run()  # line:294


def get_ver():  # line:297
    O0O000OO0OOOOOO0O = 'kzh V1.2.1'  # line:298
    O0O000OOO0O00OOOO = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}  # line:301
    OOOO000OO00OO000O = requests.get(
        'https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',
        headers=O0O000OOO0O00OOOO).json()  # line:303
    O000000OOOO0O0OO0 = O0O000OO0OOOOOO0O.split(' ')[1]  # line:304
    O0OOO0OO00OO00OO0 = OOOO000OO00OO000O.get('version').get(O0O000OO0OOOOOO0O.split(' ')[0])  # line:305
    OOO0O0OO0OOO0O000 = f"当前版本 {O000000OOOO0O0OO0}，仓库版本 {O0OOO0OO00OO00OO0}"  # line:306
    if O000000OOOO0O0OO0 < O0OOO0OO00OO00OO0:  # line:307
        OOO0O0OO0OOO0O000 += '\n' + '请到https://github.com/kxs2018/xiaoym下载最新版本'  # line:308
    return OOO0O0OO0OOO0O000  # line:309


def main():  # line:312
    print("-" * 50 + f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n' + '-' * 50)  # line:313
    O0OO00O00O0000OOO = os.getenv('aiock')  # line:314
    if not O0OO00O00O0000OOO:  # line:315
        print('请仔细阅读脚本开头的注释并配置好aiock')  # line:316
        exit()  # line:317
    try:  # line:318
        O0OO00O00O0000OOO = ast.literal_eval(O0OO00O00O0000OOO)  # line:319
    except:  # line:320
        pass  # line:321
    O0O00O00OOO0OO0OO = Queue()  # line:322
    OOO0OOOO00O0OO0O0 = []  # line:323
    for O0000O0000O0OO00O, OOOOO00000O0O00OO in enumerate(O0OO00O00O0000OOO, start=1):  # line:324
        printlog(f'{OOOOO00000O0O00OO}\n以上是账号{O0000O0000O0OO00O}的ck，如不正确，请检查ck填写格式')  # line:325
        O0O00O00OOO0OO0OO.put(OOOOO00000O0O00OO)  # line:326
    for O0000O0000O0OO00O in range(max_workers):  # line:327
        O00000O0O00O0OOO0 = threading.Thread(target=yd, args=(O0O00O00OOO0OO0OO,))  # line:328
        O00000O0O00O0OOO0.start()  # line:329
        OOO0OOOO00O0OO0O0.append(O00000O0O00O0OOO0)  # line:330
        time.sleep(40)  # line:331
    for OOO00OO0O0O0OOO00 in OOO0OOOO00O0OO0O0:  # line:332
        OOO00OO0O0O0OOO00.join()  # line:333


if __name__ == '__main__':  # line:336
    main()  # line:337
