# -*- coding: utf-8 -*-
# k小阅阅阅读多线程V2
# Author: kk
# date：2023/9/26
"""
new Env('小阅阅');
仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
小阅阅阅读入口：https://fbd.boxunet.top:10265/yunonline/v1/auth/457f9f15cb3fd5116b73961ce5cd26c6?codeurl=fbd.boxunet.top:10265&codeuserid=2&time=1696914349
阅读文章抓出ysmuid 建议手动阅读5篇左右再使用脚本，不然100%黑！！！
===============================================================
推送检测文章   将多个账号检测文章推送至将多个账号检测文章推送至目标微信目标微信，手动点击链接完成检测阅读
1.企业微信机器人 参考 https://github.com/kxs2018/yuedu/blob/main/获取企业微信群机器人key.md 获取key，填入qwbotkey，并关注插件！！！
2.wxpusher公众号  参考https://wxpusher.zjiecode.com/docs/#/ 获取apptoken、topics、uids，填入pushconfig
===============================================================
青龙面板，在配置文件里添加
export qwbotkey="key"
export pushconfig="{'appToken': 'AT_pCenRjs', 'uids': ['UID_9MZ','UID_T4xlqWx9x'], 'topicids': [''],}"
export xyyck="[{'name':'xxx','ysmuid':'xxx'},{'name':'xxx','ysmuid':'xxx'}]"
===============================================================
no module named lxml 解决方案
1. 配置文件搜索 PipMirror，如果网址包含douban的，请改为下方的网址
PipMirror="https://pypi.tuna.tsinghua.edu.cn/simple"
2. 依赖管理-python 添加 lxml
3. 如果装不上，①请ssh连接到服务器 ②docker exec -it ql bash (ql是青龙容器的名字，docker ps可查询) ③pip install pip -U
===============================================================
"""
import datetime
import hashlib
import threading
import ast
import json
import os
import random
import re
from queue import Queue
import requests
import time
from urllib.parse import urlparse, parse_qs

try:
    from lxml import etree
except:
    print('请仔细阅读脚本上方注释中的“no module named lxml 解决方案”')
    exit()

"""实时日志开关"""
printf = 1
"""1为开，0为关"""

"""debug模式开关"""
debug = 0
"""1为开，打印调试日志；0为关，不打印"""

"""线程数量设置"""
max_workers = 5
"""设置为5，即最多有5个任务同时进行"""

"""设置提现标准"""
txbz = 8000  # 不低于3000，平台标准为3000
"""设置为8000，即为8毛起提"""

"""企业微信推送开关"""
sendable = 0
if sendable:
    qwbotkey = os.getenv('qwbotkey')
    if not qwbotkey:
        print('请仔细阅读上方注释并设置好key')
        exit()
"""wxpusher推送开关"""
pushable = 1
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

checklist = ['MzkxNTE3MzQ4MQ==', 'Mzg5MjM0MDEwNw==', 'MzUzODY4NzE2OQ==', 'MzkyMjE3MzYxMg==', 'MzkxNjMwNDIzOA==',
             'Mzg3NzUxMjc5Mg==', 'Mzg4NTcwODE1NA==', 'Mzk0ODIxODE4OQ==', 'Mzg2NjUyMjI1NA==', 'MzIzMDczODg4Mw==',
             'Mzg5ODUyMzYzMQ==', 'MzU0NzI5Mjc4OQ==', 'Mzg5MDgxODAzMg==']  # line:90


def ftime():  # line:93
    O0O0O0OO00O0O0O0O = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # line:94
    return O0O0O0OO00O0O0O0O  # line:95


def debugger(O00O00O00O00000O0):  # line:98
    if debug:  # line:99
        print(O00O00O00O00000O0)  # line:100


def printlog(OO0O0O000OOO00O00):  # line:103
    if printf:  # line:104
        print(OO0O0O000OOO00O00)  # line:105


def send(OOOOO0O000O0O0O0O, title='通知', url=None):  # line:108
    if not url:  # line:109
        O00O0O0OOOOOOO0OO = {"msgtype": "text", "text": {
            "content": f"{title}\n\n{OOOOO0O000O0O0O0O}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}", }}  # line:116
    else:  # line:117
        O00O0O0OOOOOOO0OO = {"msgtype": "news", "news": {"articles": [
            {"title": title, "description": OOOOO0O000O0O0O0O, "url": url,
             "picurl": 'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}  # line:122
    OO0OOO0000OOOO000 = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'  # line:123
    OO0OO0OO00OO00OOO = requests.post(OO0OOO0000OOOO000, data=json.dumps(O00O0O0OOOOOOO0OO)).json()  # line:124
    if OO0OO0OO00OO00OOO.get('errcode') != 0:  # line:125
        print('消息发送失败，请检查key和发送格式')  # line:126
        return False  # line:127
    return OO0OO0OO00OO00OOO  # line:128


def push(O0O0000O00OOO0OOO, O0000OOOO0O0O0O0O, O00O0O0O0O0O0OOOO, uid=None):  # line:131
    if uid:  # line:132
        uids.append(uid)  # line:133
    OO0000OOOOOO0O00O = "<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace(
        'msg', O0O0000O00OOO0OOO).replace('url', O00O0O0O0O0O0OOOO)  # line:135
    OOO00O0OO0OOOOO0O = {"appToken": appToken, "content": OO0000OOOOOO0O00O, "summary": O0000OOOO0O0O0O0O,
                         "contentType": 3, "topicIds": topicids, "uids": uids, "url": O00O0O0O0O0O0OOOO,
                         "verifyPay": False}  # line:145
    O0OOO000OO00O00OO = 'http://wxpusher.zjiecode.com/api/send/message'  # line:146
    O00O0O0O00OOO0000 = requests.post(url=O0OOO000OO00O00OO, json=OOO00O0OO0OOOOO0O).json()  # line:147
    if O00O0O0O00OOO0000.get('code') != 1000:  # line:148
        print(O00O0O0O00OOO0000.get('msg'), O00O0O0O00OOO0000)  # line:149
    return O00O0O0O00OOO0000  # line:150


def getmpinfo(OO0OO0O0000O0OO00):  # line:153
    if not OO0OO0O0000O0OO00 or OO0OO0O0000O0OO00 == '':  # line:154
        return False  # line:155
    O00O0OO00OO0000OO = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}  # line:157
    OO0OO00OO0O0OO0O0 = requests.get(OO0OO0O0000O0OO00, headers=O00O0OO00OO0000OO)  # line:158
    OO0OO0O000O000OO0 = etree.HTML(OO0OO00OO0O0OO0O0.text)  # line:159
    OOO0O0O00O00OO0O0 = OO0OO0O000O000OO0.xpath('//meta[@*="og:title"]/@content')  # line:161
    if OOO0O0O00O00OO0O0:  # line:162
        OOO0O0O00O00OO0O0 = OOO0O0O00O00OO0O0[0]  # line:163
    OO00000O000000OOO = OO0OO0O000O000OO0.xpath('//meta[@*="og:url"]/@content')  # line:164
    if OO00000O000000OOO:  # line:165
        OO00000O000000OOO = OO00000O000000OOO[0].encode().decode()  # line:166
    try:  # line:167
        O0O00O000O00OOO00 = re.findall(r'biz=(.*?)&', OO0OO0O0000O0OO00)  # line:168
    except:  # line:169
        O0O00O000O00OOO00 = re.findall(r'biz=(.*?)&', OO00000O000000OOO)  # line:170
    if O0O00O000O00OOO00:  # line:171
        O0O00O000O00OOO00 = O0O00O000O00OOO00[0]  # line:172
    else:  # line:173
        return False  # line:174
    OO00OO0OO0OO0O000 = OO0OO0O000O000OO0.xpath(
        '//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')  # line:175
    if OO00OO0OO0OO0O000:  # line:176
        OO00OO0OO0OO0O000 = OO00OO0OO0OO0O000[0].strip()  # line:177
    O00OOO0O0O0O00O00 = re.findall(r"user_name.DATA'\) : '(.*?)'", OO0OO00OO0O0OO0O0.text) or OO0OO0O000O000OO0.xpath(
        '//span[@class="profile_meta_value"]/text()')  # line:179
    if O00OOO0O0O0O00O00:  # line:180
        O00OOO0O0O0O00O00 = O00OOO0O0O0O00O00[0]  # line:181
    OO0O0O0OOO0OO0O00 = re.findall(r'createTime = \'(.*)\'', OO0OO00OO0O0OO0O0.text)  # line:182
    if OO0O0O0OOO0OO0O00:  # line:183
        OO0O0O0OOO0OO0O00 = OO0O0O0OOO0OO0O00[0][5:]  # line:184
    OO0O0OO0O0O0OO000 = f'{OO0O0O0OOO0OO0O00}|{OOO0O0O00O00OO0O0}|{O0O00O000O00OOO00}|{OO00OO0OO0OO0O000}|{O00OOO0O0O0O00O00}'  # line:185
    O000OOO0000OOO00O = {'biz': O0O00O000O00OOO00, 'text': OO0O0OO0O0O0OO000}  # line:186
    return O000OOO0000OOO00O  # line:187


def ts():  # line:190
    return str(int(time.time())) + '000'  # line:191


def generate_md5(OO0O0O00OO0000OO0):  # line:194
    O0O0OOOOOO0O000OO = hashlib.md5()  # line:195
    O0O0OOOOOO0O000OO.update(OO0O0O00OO0000OO0.encode('utf-8'))  # line:196
    return O0O0OOOOOO0O000OO.hexdigest()  # line:197


class XYY:  # line:200
    def __init__(OO0O0OOO0O00O0O0O, O00000OO0OOO00OO0):  # line:201
        OO0O0OOO0O00O0O0O.name = O00000OO0OOO00OO0['name']  # line:202
        OO0O0OOO0O00O0O0O.ysm_uid = None  # line:203
        OO0O0OOO0O00O0O0O.ysmuid = O00000OO0OOO00OO0.get('ysmuid')  # line:204
        OO0O0OOO0O00O0O0O.sec = requests.session()  # line:205
        OO0O0OOO0O00O0O0O.sec.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': f'ysmuid={OO0O0OOO0O00O0O0O.ysmuid};', }  # line:210
        OO0O0OOO0O00O0O0O.msg = ''  # line:211

    def init(O0O00O0O000O000O0):  # line:213
        if not O0O00O0O000O000O0.ysmuid:  # line:214
            print('ck没有ysmuid，不能运行本脚本，自动退出')  # line:215
            return False  # line:216
        OOOO0OOOOOOO0O000 = 0  # line:217
        while OOOO0OOOOOOO0O000 < 5:  # line:218
            OO00OOOO00O00O0OO = O0O00O0O000O000O0.sec.get('http://1695722587.sumir.top/').text  # line:219
            O0O00O0O000O000O0.ysm_uid = re.findall(r'unionid="(o.*?)";', OO00OOOO00O00O0OO)  # line:220
            if O0O00O0O000O000O0.ysm_uid:  # line:221
                O0O00O0O000O000O0.ysm_uid = O0O00O0O000O000O0.ysm_uid[0]  # line:222
                OO0OO000OOOOO0000 = re.findall(r'href="(.*?)">提现', OO00OOOO00O00O0OO)  # line:223
                if OO0OO000OOOOO0000:  # line:224
                    OO0OO000OOOOO0000 = OO0OO000OOOOO0000[0]  # line:225
                    O00000000000O0000 = parse_qs(urlparse(OO0OO000OOOOO0000).query)  # line:226
                    O0O00O0O000O000O0.unionid = O00000000000O0000.get('unionid')[0]  # line:227
                    O0O00O0O000O000O0.request_id = O00000000000O0000.get('request_id')[0]  # line:228
                    O0O00O0O000O000O0.netloc = urlparse(OO0OO000OOOOO0000).netloc  # line:229
                else:  # line:230
                    printlog(f'{O0O00O0O000O000O0.name} 获取提现参数失败，本次不提现')  # line:231
                    O0O00O0O000O000O0.msg += f'获取提现参数失败，本次不提现\n'  # line:232
                return True  # line:233
            else:  # line:234
                OOOO0OOOOOOO0O000 += 1  # line:235
                continue  # line:236
        printlog(f'{O0O00O0O000O000O0.name} 获取ysm_uid失败，请检查账号有效性')  # line:237
        O0O00O0O000O000O0.msg += '获取ysm_uid失败，请检查账号有效性\n'  # line:238
        return False  # line:239

    def something(OO0OOOOO0O0O00000):  # line:241
        O0000OO0OO000O0O0 = 'http://1695724331.umis.top/yunonline/v1/sign_info'  # line:242
        O0O0000000OO00O00 = {'time': ts(), 'unionid': OO0OOOOO0O0O00000.ysm_uid}  # line:243
        OO0OOOOO0O0O00000.sec.get(O0000OO0OO000O0O0, params=O0O0000000OO00O00)  # line:244
        O0000OO0OO000O0O0 = 'http://1695724331.umis.top/yunonline/v1/hasWechat'  # line:245
        O0O0000000OO00O00.pop('time')  # line:246
        OO0OOOOO0O0O00000.sec.get(O0000OO0OO000O0O0, params=O0O0000000OO00O00)  # line:247
        O0000OO0OO000O0O0 = 'http://1695724142.umis.top/yunonline/v1/devtouid'  # line:248
        O0O0000000OO00O00.update({'devid': generate_md5(OO0OOOOO0O0O00000.ysm_uid)})  # line:249
        OO0OOOOO0O0O00000.sec.post(O0000OO0OO000O0O0, data=O0O0000000OO00O00)  # line:250

    def user_info(OOOOO0OO0OO0OOO0O):  # line:252
        OOO0OOO0OOO00OO0O = f'http://1695724331.umis.top/yunonline/v1/gold?unionid={OOOOO0OO0OO0OOO0O.ysm_uid}&time={ts()}'  # line:253
        O0OOOO0000O000OOO = OOOOO0OO0OO0OOO0O.sec.get(OOO0OOO0OOO00OO0O).json()  # line:254
        debugger(f'userinfo {O0OOOO0000O000OOO}')  # line:255
        O00OOO00OOOOO0OOO = O0OOOO0000O000OOO.get("data")  # line:256
        OOOOO0OO0OO0OOO0O.last_gold = O0OOOO0000O000OOO.get("data").get("last_gold")  # line:257
        O00000O00000O0OO0 = O00OOO00OOOOO0OOO.get("remain_read")  # line:258
        O00OOO00O00OOOO00 = f'今日已经阅读了{O00OOO00OOOOO0OOO.get("day_read")}篇文章,剩余{O00000O00000O0OO0}未阅读，今日获取金币{O00OOO00OOOOO0OOO.get("day_gold")}，剩余{OOOOO0OO0OO0OOO0O.last_gold}'  # line:259
        printlog(f'{OOOOO0OO0OO0OOO0O.name}:{O00OOO00O00OOOO00}')  # line:260
        OOOOO0OO0OO0OOO0O.msg += (O00OOO00O00OOOO00 + '\n')  # line:261
        if O00000O00000O0OO0 == 0:  # line:262
            return False  # line:263
        return True  # line:264

    def getKey(O0OOO00O0000O0OOO):  # line:266
        O000OO0OOO0O0OOOO = 'http://1695724331.umis.top/yunonline/v1/wtmpdomain'  # line:267
        O0O00O0000O0OO0O0 = f'unionid={O0OOO00O0000O0OOO.ysm_uid}'  # line:268
        OO0O0OOO000O000OO = O0OOO00O0000O0OOO.sec.post(O000OO0OOO0O0OOOO, data=O0O00O0000O0OO0O0).json()  # line:269
        debugger(f'getkey {OO0O0OOO000O000OO}')  # line:270
        OOO0O000OO0O0OOO0 = OO0O0OOO000O000OO.get('data').get('domain')  # line:271
        O0OOO00O0000O0OOO.uk = parse_qs(urlparse(OOO0O000OO0O0OOO0).query).get('uk')[0]  # line:272
        OOOOOO0OOOO000000 = urlparse(OOO0O000OO0O0OOO0).netloc  # line:273
        O0OOO00O0000O0OOO.headers = {'Connection': 'keep-alive',
                                     'Accept': 'application/json, text/javascript, */*; q=0.01',
                                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
                                     'Origin': f'https://{OOOOOO0OOOO000000}', 'Sec-Fetch-Site': 'cross-site',
                                     'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty',
                                     'Accept-Encoding': 'gzip, deflate, br',
                                     'Accept-Language': 'zh-CN,zh', }  # line:284

    def read(OO0000OOO0OOO00O0):  # line:286
        time.sleep(3)  # line:287
        OOOOOO0OO0O00O0OO = {'uk': OO0000OOO0OOO00O0.uk}  # line:288
        OOOO0O0OO00O0O000 = 0  # line:289
        while True:  # line:290
            OOOOOO0000OOO000O = f'https://nsr.zsf2023e458.cloud/yunonline/v1/do_read'  # line:291
            OO00OO000O00OOOOO = requests.get(OOOOOO0000OOO000O, headers=OO0000OOO0OOO00O0.headers,
                                             params=OOOOOO0OO0O00O0OO)  # line:292
            OO0000OOO0OOO00O0.msg += ('-' * 50 + '\n')  # line:293
            debugger(f'read1 {OO00OO000O00OOOOO.text}')  # line:294
            OO00OO000O00OOOOO = OO00OO000O00OOOOO.json()  # line:295
            if OO00OO000O00OOOOO.get('errcode') == 0:  # line:296
                O000O0O0O00OOOO0O = OO00OO000O00OOOOO.get('data').get('link')  # line:297
                OO00OOOOOO0OO0OO0 = OO0000OOO0OOO00O0.jump(O000O0O0O00OOOO0O)  # line:298
                if 'mp.weixin' in OO00OOOOOO0OO0OO0:  # line:299
                    O0O0OO0O0000O0OOO = getmpinfo(OO00OOOOOO0OO0OO0)  # line:300
                    OOO00000OOO0O0OOO = O0O0OO0O0000O0OOO['biz']  # line:301
                    OO0000OOO0OOO00O0.msg += ('开始阅读 ' + O0O0OO0O0000O0OOO['text'] + '\n')  # line:302
                    printlog(f'{OO0000OOO0OOO00O0.name}:开始阅读 ' + O0O0OO0O0000O0OOO['text'])  # line:303
                    if OOO00000OOO0O0OOO in checklist:  # line:304
                        if sendable:  # line:305
                            send(f"{O0O0OO0O0000O0OOO['text']}", title=f'{OO0000OOO0OOO00O0.name} 小阅阅过检测',
                                 url=OO00OOOOOO0OO0OO0)  # line:306
                        if pushable:  # line:307
                            push(f'{OO0000OOO0OOO00O0.name}\n点击阅读检测文章\n{O0O0OO0O0000O0OOO["text"]}',
                                 f'{OO0000OOO0OOO00O0.name} 小阅阅过检测', OO00OOOOOO0OO0OO0)  # line:309
                        OO0000OOO0OOO00O0.msg += '遇到检测文章，已发送到微信，手动阅读，暂停60秒\n'  # line:310
                        printlog(f'{OO0000OOO0OOO00O0.name}:遇到检测文章，已发送到微信，手动阅读，暂停60秒')  # line:311
                        time.sleep(60)  # line:312
                else:  # line:313
                    OO0000OOO0OOO00O0.msg += f'{OO0000OOO0OOO00O0.name} 小阅阅跳转到 {OO00OOOOOO0OO0OO0}\n'  # line:314
                    printlog(f'{OO0000OOO0OOO00O0.name}: 小阅阅跳转到 {OO00OOOOOO0OO0OO0}')  # line:315
                    continue  # line:316
                OO0000OO0000O00O0 = random.randint(7, 10)  # line:317
                OO0000OOO0OOO00O0.msg += f'本次模拟读{OO0000OO0000O00O0}秒\n'  # line:318
                time.sleep(OO0000OO0000O00O0)  # line:319
                OOOOOO0000OOO000O = f'https://nsr.zsf2023e458.cloud/yunonline/v1/get_read_gold?uk={OO0000OOO0OOO00O0.uk}&time={OO0000OO0000O00O0}&timestamp={ts()}'  # line:320
                requests.get(OOOOOO0000OOO000O, headers=OO0000OOO0OOO00O0.headers)  # line:321
            elif OO00OO000O00OOOOO.get('errcode') == 405:  # line:322
                printlog(f'{OO0000OOO0OOO00O0.name}:阅读重复')  # line:323
                OO0000OOO0OOO00O0.msg += '阅读重复\n'  # line:324
                time.sleep(1.5)  # line:325
            elif OO00OO000O00OOOOO.get('errcode') == 407:  # line:326
                printlog(f'{OO0000OOO0OOO00O0.name}:{OO00OO000O00OOOOO.get("msg")}')  # line:327
                OO0000OOO0OOO00O0.msg += (OO00OO000O00OOOOO.get('msg') + '\n')  # line:328
                return True  # line:329
            else:  # line:330
                printlog(f'{OO0000OOO0OOO00O0.name}:{OO00OO000O00OOOOO.get("msg")}')  # line:331
                OO0000OOO0OOO00O0.msg += (OO00OO000O00OOOOO.get("msg") + '\n')  # line:332
                time.sleep(1.5)  # line:333

    def jump(O0O0O00O00OO0OO0O, O0OO0O0O0OO00O0OO):  # line:335
        OOOOO00000O0OO0OO = urlparse(O0OO0O0O0OO00O0OO).netloc  # line:336
        OO0OO0OO00O0OOOO0 = {'Host': OOOOO00000O0OO0OO, 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1',
                             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
                             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                             'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh',
                             'Cookie': f'ysmuid={O0O0O00O00OO0OO0O.ysmuid}', }  # line:346
        O00OO00O0OOO00OO0 = requests.get(O0OO0O0O0OO00O0OO, headers=OO0OO0OO00O0OOOO0,
                                         allow_redirects=False)  # line:347
        O0OOOO000O0OO000O = O00OO00O0OOO00OO0.headers.get('Location')  # line:348
        return O0OOOO000O0OO000O  # line:349

    def withdraw(O00O0000OOOOOOO00):  # line:351
        if not O00O0000OOOOOOO00.unionid:  # line:352
            return False  # line:353
        if int(O00O0000OOOOOOO00.last_gold) < txbz:  # line:354
            printlog(f'{O00O0000OOOOOOO00.name} 没有达到你设置的提现标准{txbz}')  # line:355
            O00O0000OOOOOOO00.msg += f'没有达到你设置的提现标准{txbz}\n'  # line:356
            return False  # line:357
        O00OOO0OO00OO00O0 = int(int(O00O0000OOOOOOO00.last_gold) / 1000) * 1000  # line:358
        O00O0000OOOOOOO00.msg += f'本次提现金币{O00OOO0OO00OO00O0}\n'  # line:359
        printlog(f'{O00O0000OOOOOOO00.name}:本次提现金币{O00OOO0OO00OO00O0}')  # line:360
        if O00OOO0OO00OO00O0:  # line:362
            OOO000000OO0OOOOO = f'http://{O00O0000OOOOOOO00.netloc}/yunonline/v1/user_gold'  # line:363
            printlog(OOO000000OO0OOOOO)  # line:364
            OOOO0OOO0O0OOO0OO = f'unionid={O00O0000OOOOOOO00.unionid}&request_id={O00O0000OOOOOOO00.request_id}&gold={O00OOO0OO00OO00O0}'  # line:365
            OOO0OO0O00O0OOO0O = O00O0000OOOOOOO00.sec.post(OOO000000OO0OOOOO, data=OOOO0OOO0O0OOO0OO)  # line:366
            debugger(f'gold {OOO0OO0O00O0OOO0O.text}')  # line:367
            OOO000000OO0OOOOO = f'http://{O00O0000OOOOOOO00.netloc}/yunonline/v1/withdraw'  # line:368
            OOOO0OOO0O0OOO0OO = f'unionid={O00O0000OOOOOOO00.unionid}&signid={O00O0000OOOOOOO00.request_id}&ua=0&ptype=0&paccount=&pname='  # line:369
            OOO0OO0O00O0OOO0O = O00O0000OOOOOOO00.sec.post(OOO000000OO0OOOOO, data=OOOO0OOO0O0OOO0OO)  # line:370
            debugger(f'withdraw {OOO0OO0O00O0OOO0O.text}')  # line:371
            O00O0000OOOOOOO00.msg += f"提现结果 {OOO0OO0O00O0OOO0O.json()['msg']}"  # line:372
            printlog(f'{O00O0000OOOOOOO00.name}:提现结果 {OOO0OO0O00O0OOO0O.json()["msg"]}')  # line:373

    def run(O0O0OO000OOO00OOO):  # line:375
        O0O0OO000OOO00OOO.msg += ('=' * 50 + f'\n账号：{O0O0OO000OOO00OOO.name}开始任务\n')  # line:376
        printlog(f'账号：{O0O0OO000OOO00OOO.name}开始任务')  # line:377
        if not O0O0OO000OOO00OOO.init():  # line:378
            return False  # line:379
        O0O0OO000OOO00OOO.something()  # line:380
        if O0O0OO000OOO00OOO.user_info():  # line:381
            O0O0OO000OOO00OOO.getKey()  # line:382
            O0O0OO000OOO00OOO.read()  # line:383
            O0O0OO000OOO00OOO.user_info()  # line:384
            time.sleep(0.5)  # line:385
        O0O0OO000OOO00OOO.withdraw()  # line:386
        printlog(f'账号：{O0O0OO000OOO00OOO.name} 本轮任务结束')  # line:387
        if not printf:  # line:388
            print(O0O0OO000OOO00OOO.msg)  # line:389


def yd(O00OO00O0OO0OOOO0):  # line:392
    while not O00OO00O0OO0OOOO0.empty():  # line:393
        O00OO0OO0OOO0O00O = O00OO00O0OO0OOOO0.get()  # line:394
        OO00O0O000O00O0OO = XYY(O00OO0OO0OOO0O00O)  # line:395
        OO00O0O000O00O0OO.run()  # line:396


def get_ver():  # line:399
    O0O00OO0000OOO000 = 'kxyyV2 V2.3'  # line:400
    O0OO0OO00000O0OOO = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}  # line:403
    OO00O0000000O0OOO = requests.get(
        'https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',
        headers=O0OO0OO00000O0OOO).json()  # line:405
    O0OOO0000OOO00000 = O0O00OO0000OOO000.split(' ')[1]  # line:406
    O0O000000OOOO0OO0 = OO00O0000000O0OOO.get('version').get(O0O00OO0000OOO000.split(' ')[0])  # line:407
    O000OO00OOOO0O00O = f"当前版本 {O0OOO0000OOO00000}，仓库版本 {O0O000000OOOO0OO0}"  # line:408
    if O0OOO0000OOO00000 < O0O000000OOOO0OO0:  # line:409
        O000OO00OOOO0O00O += '\n' + '请到https://github.com/kxs2018/xiaoym下载最新版本'  # line:410
    return O000OO00OOOO0O00O  # line:411


def main():  # line:414
    print("-" * 50 + f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n' + '-' * 50)  # line:415
    O00OOO0O0OOOO0O00 = os.getenv('xyyck')  # line:416
    if not O00OOO0O0OOOO0O00:  # line:417
        print('请仔细阅读脚本上方注释并设置好ck')  # line:418
        exit()  # line:419
    try:  # line:420
        O00OOO0O0OOOO0O00 = ast.literal_eval(O00OOO0O0OOOO0O00)  # line:421
    except:  # line:422
        pass  # line:423
    OO0O0O0OO00OOOOOO = []  # line:424
    OO0OOOOOOOOO0OO00 = Queue()  # line:425
    for O00O0O00000OO0O0O, OOOO00OO000OOOO00 in enumerate(O00OOO0O0OOOO0O00, start=1):  # line:426
        printlog(f'{OOOO00OO000OOOO00}\n以上是第{O00O0O00000OO0O0O}个账号的ck，如不正确，请检查ck填写格式')  # line:427
        OO0OOOOOOOOO0OO00.put(OOOO00OO000OOOO00)  # line:428
    for O00O0O00000OO0O0O in range(max_workers):  # line:429
        O0OOOOOOO00OO000O = threading.Thread(target=yd, args=(OO0OOOOOOOOO0OO00,))  # line:430
        O0OOOOOOO00OO000O.start()  # line:431
        OO0O0O0OO00OOOOOO.append(O0OOOOOOO00OO000O)  # line:432
        time.sleep(30)  # line:433
    for OO0O00OOO0OO0000O in OO0O0O0OO00OOOOOO:  # line:434
        OO0O00OOO0OO0000O.join()  # line:435


if __name__ == '__main__':  # line:438
    main ()  # line:439
