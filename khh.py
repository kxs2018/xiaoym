"""
花花阅读入口：http://mr138301519.nmyebvvmntj.cloud/user/index.html?mid=EG5EVNLF3

http://u.cocozx.cn/api/user/info
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
3. 如果装不上，①请ssh连接到服务器 ②docker exec -it ql bash (ql是青龙容器的名字，不会就问百度) ③pip install pip -U
4. 再装不上依赖就放弃吧
------------------------------------------------------
提现标准默认是5000
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
txbz = 5000  # 不低于3000，平台的提现标准为3000
"""设置为5000，即为5毛起提"""

qwbotkey = os.getenv('qwbotkey')  # line:61
if not qwbotkey:  # line:63
    print('请仔细阅读脚本开头的注释并配置好qwbotkey')  # line:64
    exit()  # line:65


def ftime():  # line:68
    OO0O0O0OO00O0000O = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # line:69
    return OO0O0O0OO00O0000O  # line:70


def debugger(OO00OOO0OOO00OOO0):  # line:73
    if debug:  # line:74
        print(OO00OOO0OOO00OOO0)  # line:75


def printlog(OOOO00OOOO000OO00):  # line:78
    if printf:  # line:79
        print(OOOO00OOOO000OO00)  # line:80


def send(OO0OO0O00000OO0O0, title='通知', url=None):  # line:83
    if not title or not url:  # line:84
        OO00000OO00O00000 = {"msgtype": "text", "text": {
            "content": f"{title}\n\n{OO0OO0O00000OO0O0}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}", }}  # line:91
    else:  # line:92
        OO00000OO00O00000 = {"msgtype": "news", "news": {"articles": [
            {"title": title, "description": OO0OO0O00000OO0O0, "url": url,
             "picurl": 'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}  # line:105
    OO0000OO0O0OOO000 = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'  # line:106
    OOO00000OO0O0000O = requests.post(OO0000OO0O0OOO000, data=json.dumps(OO00000OO00O00000)).json()  # line:107
    if OOO00000OO0O0000O.get('errcode') != 0:  # line:108
        print('消息发送失败，请检查key和发送格式')  # line:109
        return False  # line:110
    return OOO00000OO0O0000O  # line:111


def getmpinfo(OOOO00O00OO0OO00O):  # line:114
    if not OOOO00O00OO0OO00O or OOOO00O00OO0OO00O == '':  # line:115
        return False  # line:116
    OOOOOO0OO0OOOOOO0 = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}  # line:118
    O000OOOO0OO0OO0OO = requests.get(OOOO00O00OO0OO00O, headers=OOOOOO0OO0OOOOOO0)  # line:119
    OO0O00O00OO00OO0O = etree.HTML(O000OOOO0OO0OO0OO.text)  # line:120
    OO00O0OOO0O000OOO = OO0O00O00OO00OO0O.xpath('//meta[@*="og:title"]/@content')  # line:122
    if OO00O0OOO0O000OOO:  # line:123
        OO00O0OOO0O000OOO = OO00O0OOO0O000OOO[0]  # line:124
    O000OO0O0OO0OO000 = OO0O00O00OO00OO0O.xpath('//meta[@*="og:url"]/@content')  # line:125
    if O000OO0O0OO0OO000:  # line:126
        O000OO0O0OO0OO000 = O000OO0O0OO0OO000[0].encode().decode()  # line:127
    try:  # line:128
        O000O00O0OO0O00OO = re.findall(r'biz=(.*?)&', OOOO00O00OO0OO00O)  # line:129
    except:  # line:130
        O000O00O0OO0O00OO = re.findall(r'biz=(.*?)&', O000OO0O0OO0OO000)  # line:131
    if O000O00O0OO0O00OO:  # line:132
        O000O00O0OO0O00OO = O000O00O0OO0O00OO[0]  # line:133
    else:  # line:134
        return False  # line:135
    O0O000O00OOOOO000 = OO0O00O00OO00OO0O.xpath(
        '//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')  # line:136
    if O0O000O00OOOOO000:  # line:137
        O0O000O00OOOOO000 = O0O000O00OOOOO000[0].strip()  # line:138
    OO0000OOOO000O00O = re.findall(r"user_name.DATA'\) : '(.*?)'", O000OOOO0OO0OO0OO.text) or OO0O00O00OO00OO0O.xpath(
        '//span[@class="profile_meta_value"]/text()')  # line:140
    if OO0000OOOO000O00O:  # line:141
        OO0000OOOO000O00O = OO0000OOOO000O00O[0]  # line:142
    OOO0000O000OO0000 = re.findall(r'createTime = \'(.*)\'', O000OOOO0OO0OO0OO.text)  # line:143
    if OOO0000O000OO0000:  # line:144
        OOO0000O000OO0000 = OOO0000O000OO0000[0][5:]  # line:145
    OOOO00O0OOOOO0OOO = f'{OOO0000O000OO0000} {OO00O0OOO0O000OOO}'  # line:146
    O0OOO00O00O00O0OO = {'biz': O000O00O0OO0O00OO, 'text': OOOO00O0OOOOO0OOO}  # line:147
    return O0OOO00O00O00O0OO  # line:148


class Allinone:  # line:151
    def __init__(OOOOOO00OOOO0O00O, OO0O000000OO0OO0O):  # line:152
        OOOOOO00OOOO0O00O.name = OO0O000000OO0OO0O['name']  # line:153
        OOOOOO00OOOO0O00O.s = requests.session()  # line:154
        OOOOOO00OOOO0O00O.payload = {"un": OO0O000000OO0OO0O['un'], "token": OO0O000000OO0OO0O['token'],
                                     "pageSize": 20}  # line:155
        OOOOOO00OOOO0O00O.s.headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                                       'Content-Type': 'application/json; charset=UTF-8', 'Host': 'u.cocozx.cn',
                                       'Connection': 'keep-alive',
                                       'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",
                                       'Origin': 'http://mr1694971896247.dswxin.cn', }  # line:161
        OOOOOO00OOOO0O00O.headers = OOOOOO00OOOO0O00O.s.headers.copy()  # line:162
        OOOOOO00OOOO0O00O.msg = ''  # line:163

    def get_readhost(OOOOO00000O0O0O00):  # line:165
        OO0OO0000O0000O00 = "http://u.cocozx.cn/api/user/getReadHost"  # line:166
        OOOO0OO0OOO0OOOO0 = OOOOO00000O0O0O00.s.post(OO0OO0000O0000O00,
                                                     json=OOOOO00000O0O0O00.payload).json()  # line:167
        debugger(f'readhome {OOOO0OO0OOO0OOOO0}')  # line:168
        OOOOO00000O0O0O00.readhost = OOOO0OO0OOO0OOOO0.get('result')['host']  # line:169
        OOOOO00000O0O0O00.headers['Origin'] = OOOOO00000O0O0O00.readhost  # line:170
        OOOOO00000O0O0O00.msg += f'邀请链接：{OOOOO00000O0O0O00.readhost}/user/index.html?mid={OOOOO00000O0O0O00.huid}\n'  # line:171
        printlog(
            f"{OOOOO00000O0O0O00.name}:邀请链接：{OOOOO00000O0O0O00.readhost}/user/index.html?mid={OOOOO00000O0O0O00.huid}")  # line:172

    def stataccess(OO0O0OO0O0O000OOO):  # line:174
        O0OOOO0000O0OOOO0 = 'http://u.cocozx.cn/api/user/statAccess'  # line:175
        OO0O0OO0O0O000OOO.s.post(O0OOOO0000O0OOOO0, json=OO0O0OO0O0O000OOO.payload).json()  # line:176

    def get_info(O00OO00O0000O0O0O):  # line:178
        try:  # line:179
            OO0O0O0O0O00O000O = O00OO00O0000O0O0O.s.post("http://u.cocozx.cn/api/user/info",
                                                         json=O00OO00O0000O0O0O.payload).json()  # line:180
            OOO000OOOOO00OOOO = OO0O0O0O0O00O000O.get("result")  # line:181
            debugger(f'get_info {OO0O0O0O0O00O000O}')  # line:182
            OO000OO0000OOO000 = OOO000OOOOO00OOOO.get('us')  # line:183
            if OO000OO0000OOO000 == 2:  # line:184
                O00OO00O0000O0O0O.msg += f'账号：{O00OO00O0000O0O0O.name}已被封\n'  # line:185
                printlog(f'账号：{O00OO00O0000O0O0O.name}已被封')  # line:186
                return False  # line:187
            O00OO00O0000O0O0O.msg += f"""账号:{O00OO00O0000O0O0O.name}，今日阅读次数:{OOO000OOOOO00OOOO["dayCount"]}，当前花儿:{OOO000OOOOO00OOOO["moneyCurrent"]}，累计阅读次数:{OOO000OOOOO00OOOO["doneWx"]}\n"""  # line:188
            printlog(
                f"""账号:{O00OO00O0000O0O0O.name}，今日阅读次数:{OOO000OOOOO00OOOO["dayCount"]}，当前花儿:{OOO000OOOOO00OOOO["moneyCurrent"]}，累计阅读次数:{OOO000OOOOO00OOOO["doneWx"]}""")  # line:190
            O0OOO00O000OO0OO0 = int(OOO000OOOOO00OOOO["moneyCurrent"])  # line:191
            O00OO00O0000O0O0O.huid = OOO000OOOOO00OOOO.get('uid')  # line:192
            return O0OOO00O000OO0OO0  # line:193
        except:  # line:194
            return False  # line:195

    def psmoneyc(OO000O0O00OO00O0O):  # line:197
        O000O0OO0OO0O0OOO = {**OO000O0O00OO00O0O.payload, **{'mid': OO000O0O00OO00O0O.huid}}  # line:198
        try:  # line:199
            O0O0OOO0O000OO0O0 = OO000O0O00OO00O0O.s.post("http://u.cocozx.cn/api/user/psmoneyc",
                                                         json=O000O0OO0OO0O0OOO).json()  # line:200
            OO000O0O00OO00O0O.msg += f"感谢下级送来的{O0O0OOO0O000OO0O0['result']['val']}花儿\n"  # line:201
        except:  # line:202
            pass  # line:203
        return  # line:204

    def get_status(OO0O0OOOO0O000OOO):  # line:206
        O0O0O000O000OOO0O = requests.post("http://u.cocozx.cn/api/user/read", headers=OO0O0OOOO0O000OOO.headers,
                                          json=OO0O0OOOO0O000OOO.payload).json()  # line:207
        debugger(f'getstatus {O0O0O000O000OOO0O}')  # line:208
        OO0O0OOOO0O000OOO.status = O0O0O000O000OOO0O.get("result").get("status")  # line:209
        if OO0O0OOOO0O000OOO.status == 40:  # line:210
            OO0O0OOOO0O000OOO.msg += "文章还没有准备好\n"  # line:211
            printlog(f"{OO0O0OOOO0O000OOO.name}:文章还没有准备好")  # line:212
            return  # line:213
        elif OO0O0OOOO0O000OOO.status == 50:  # line:214
            OO0O0OOOO0O000OOO.msg += "阅读失效\n"  # line:215
            printlog(f"{OO0O0OOOO0O000OOO.name}:阅读失效")  # line:216
            return  # line:217
        elif OO0O0OOOO0O000OOO.status == 60:  # line:218
            OO0O0OOOO0O000OOO.msg += "已经全部阅读完了\n"  # line:219
            printlog(f"{OO0O0OOOO0O000OOO.name}:已经全部阅读完了")  # line:220
            return  # line:221
        elif OO0O0OOOO0O000OOO.status == 70:  # line:222
            OO0O0OOOO0O000OOO.msg += "下一轮还未开启\n"  # line:223
            printlog(f"{OO0O0OOOO0O000OOO.name}:下一轮还未开启")  # line:224
            return  # line:225
        elif OO0O0OOOO0O000OOO.status == 10:  # line:226
            O0OO0O0000O00OO0O = O0O0O000O000OOO0O["result"]["url"]  # line:227
            OO0O0OOOO0O000OOO.msg += '-' * 50 + "\n阅读链接获取成功\n"  # line:228
            printlog(f"{OO0O0OOOO0O000OOO.name}:阅读链接获取成功")  # line:229
            return O0OO0O0000O00OO0O  # line:230

    def submit(OOOO0OOO0000O00O0):  # line:232
        O0O0O0O00000O000O = {**{'type': 1}, **OOOO0OOO0000O00O0.payload}  # line:233
        OO00000O000O0000O = requests.post("http://u.cocozx.cn/api/user/submit?zx=&xz=1",
                                          headers=OOOO0OOO0000O00O0.headers, json=O0O0O0O00000O000O)  # line:234
        OOOO00000OO00O0O0 = OO00000O000O0000O.json().get('result')  # line:235
        debugger('submit ' + OO00000O000O0000O.text)  # line:236
        OOOO0OOO0000O00O0.msg += f'阅读成功,获得花儿{OOOO00000OO00O0O0["val"]}，当前剩余次数:{OOOO00000OO00O0O0["progress"]}\n'  # line:237
        printlog(
            f"{OOOO0OOO0000O00O0.name}:阅读成功,获得花儿{OOOO00000OO00O0O0['val']}，当前剩余次数:{OOOO00000OO00O0O0['progress']}")  # line:238

    def read(OOO00OOOOOOO00O00):  # line:240
        while True:  # line:241
            O00O0O0O0O0O00O0O = OOO00OOOOOOO00O00.get_status()  # line:242
            if not O00O0O0O0O0O00O0O:  # line:243
                if OOO00OOOOOOO00O00.status == 30:  # line:244
                    time.sleep(3)  # line:245
                    continue  # line:246
                break  # line:247
            OO0O0OO00O0000OOO = getmpinfo(O00O0O0O0O0O00O0O)  # line:248
            if not OO0O0OO00O0000OOO:  # line:249
                printlog(f'{OOO00OOOOOOO00O00.name}:获取文章信息失败，程序中止')  # line:250
                return False  # line:251
            OOO00OOOOOOO00O00.msg += '开始阅读 ' + OO0O0OO00O0000OOO['text'] + '\n'  # line:252
            printlog(f'{OOO00OOOOOOO00O00.name}:开始阅读 ' + OO0O0OO00O0000OOO['text'])  # line:253
            OOO0OO00OOO0O0O00 = randint(7, 10)  # line:254
            if OO0O0OO00O0000OOO['biz'] == "Mzg2Mzk3Mjk5NQ==":  # line:255
                OOO00OOOOOOO00O00.msg += '当前正在阅读检测文章\n'  # line:256
                printlog(f'{OOO00OOOOOOO00O00.name}:正在阅读检测文章')  # line:257
                send(f'{OOO00OOOOOOO00O00.name}  花花阅读正在读检测文章', OO0O0OO00O0000OOO['text'],
                     O00O0O0O0O0O00O0O)  # line:258
                time.sleep(60)  # line:259
            printlog(f'{OOO00OOOOOOO00O00.name}：模拟阅读{OOO0OO00OOO0O0O00}秒')  # line:260
            time.sleep(OOO0OO00OOO0O0O00)  # line:261
            OOO00OOOOOOO00O00.submit()  # line:262

    def tixian(OOO00OO0OO0O000OO):  # line:264
        global txe  # line:265
        OOOOO0OOO0000000O = OOO00OO0OO0O000OO.get_info()  # line:266
        if OOOOO0OOO0000000O < txbz:  # line:267
            OOO00OO0OO0O000OO.msg += '你的花儿不多了\n'  # line:268
            printlog(f'{OOO00OO0OO0O000OO.name}你的花儿不多了')  # line:269
            return False  # line:270
        if 10000 <= OOOOO0OOO0000000O < 49999:  # line:271
            txe = 10000  # line:272
        elif 5000 <= OOOOO0OOO0000000O < 10000:  # line:273
            txe = 5000  # line:274
        elif 3000 <= OOOOO0OOO0000000O < 5000:  # line:275
            txe = 3000  # line:276
        elif OOOOO0OOO0000000O >= 50000:  # line:277
            txe = 50000  # line:278
        OOO00OO0OO0O000OO.msg += f"提现金额:{txe}"  # line:279
        printlog(f'{OOO00OO0OO0O000OO.name}提现金额:{txe}')  # line:280
        OOO0O000OOOO0O0OO = {**OOO00OO0OO0O000OO.payload, **{"val": txe}}  # line:281
        try:  # line:282
            O00000O0OO000OO00 = OOO00OO0OO0O000OO.s.post("http://u.cocozx.cn/api/user/wd",
                                                         json=OOO0O000OOOO0O0OO).json()  # line:283
            OOO00OO0OO0O000OO.msg += f"提现结果:{O00000O0OO000OO00.get('msg')}\n"  # line:284
            printlog(f'{OOO00OO0OO0O000OO.name}提现结果：{O00000O0OO000OO00.get("msg")}')  # line:285
        except:  # line:286
            OOO00OO0OO0O000OO.msg += f"自动提现不成功，发送通知手动提现\n"  # line:287
            printlog(f"{OOO00OO0OO0O000OO.name}:自动提现不成功，发送通知手动提现")  # line:288
            send(f'可提现金额 {int(txe) / 10000}元，点击提现',
                 title=f'惜之酱提醒您 {OOO00OO0OO0O000OO.name} 花花阅读可以提现了',
                 url=f'{OOO00OO0OO0O000OO.readhost}/user/index.html?mid=FK73K93DA')  # line:290

    def run(OO0OO000O00OO0000):  # line:292
        if OO0OO000O00OO0000.get_info():  # line:293
            OO0OO000O00OO0000.stataccess()  # line:294
            OO0OO000O00OO0000.get_readhost()  # line:295
            OO0OO000O00OO0000.psmoneyc()  # line:296
            OO0OO000O00OO0000.read()  # line:297
            OO0OO000O00OO0000.tixian()  # line:298
        if not printf:  # line:299
            print(OO0OO000O00OO0000.msg.strip())  # line:300


def yd(O000OO0OOO0000OO0):  # line:303
    while not O000OO0OOO0000OO0.empty():  # line:304
        OO00OO00000OO0O00 = O000OO0OOO0000OO0.get()  # line:305
        try:  # line:306
            OO00OO0O0OOO0OO0O = Allinone(OO00OO00000OO0O00)  # line:307
            OO00OO0O0OOO0OO0O.run()  # line:308
        except Exception as OO0O000OOOOO00O0O:  # line:309
            print(OO0O000OOOOO00O0O)  # line:310


def get_ver():  # line:313
    O000O00OO00OOO000 = 'khh V1.2.1'  # line:314
    O0OO000O0O0OOO0O0 = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}  # line:317
    OOOOO0O000000O0O0 = requests.get(
        'https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',
        headers=O0OO000O0O0OOO0O0).json()  # line:319
    OO0O0000OO0OO0O0O = O000O00OO00OOO000.split(' ')[1]  # line:320
    OOO0O0O0000O0OOOO = OOOOO0O000000O0O0.get('version').get(O000O00OO00OOO000.split(' ')[0])  # line:321
    O0OO000OOO0O0OO0O = f"当前版本 {OO0O0000OO0OO0O0O}，仓库版本 {OOO0O0O0000O0OOOO}"  # line:322
    if OO0O0000OO0OO0O0O < OOO0O0O0000O0OOOO:  # line:323
        O0OO000OOO0O0OO0O += '\n' + '请到https://github.com/kxs2018/xiaoym下载最新版本'  # line:324
    return O0OO000OOO0O0OO0O  # line:325


def main():  # line:328
    print("-" * 50 + f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n' + '-' * 50)  # line:329
    O00O000O0O0O00000 = os.getenv('aiock')  # line:330
    if not O00O000O0O0O00000:  # line:331
        print('请仔细阅读脚本开头的注释并配置好aiock')  # line:332
        exit()  # line:333
    try:  # line:334
        O00O000O0O0O00000 = ast.literal_eval(O00O000O0O0O00000)  # line:335
    except:  # line:336
        pass  # line:337
    OOO00O0000OOO0OO0 = Queue()  # line:338
    O0OO0O000OO0O0OO0 = []  # line:339
    for O0O000O000OO00O00, O00O00OO00O0O0000 in enumerate(O00O000O0O0O00000, start=1):  # line:340
        printlog(
            f'{O00O00OO00O0O0000}\n以上是账号{O0O000O000OO00O00}的ck，请核对是否正确，如不正确，请检查ck填写格式')  # line:341
        OOO00O0000OOO0OO0.put(O00O00OO00O0O0000)  # line:342
    for O0O000O000OO00O00 in range(max_workers):  # line:343
        O000OO0O0O00O00OO = threading.Thread(target=yd, args=(OOO00O0000OOO0OO0,))  # line:344
        O000OO0O0O00O00OO.start()  # line:345
        O0OO0O000OO0O0OO0.append(O000OO0O0O00O00OO)  # line:346
        time.sleep(40)  # line:347
    for OO00O0O000OOOO000 in O0OO0O000OO0O0OO0:  # line:348
        OO00O0O000OOOO000.join()  # line:349


if __name__ == '__main__':  # line:352
    main()  # line:353
