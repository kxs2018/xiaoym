# -*- coding: utf-8 -*-
# k充值购买阅读
"""
仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
充值购买阅读入口：http://2502807.jl.sgzzlb.sg6gdkelit8js.cloud/?p=2502807
阅读文章抓出gfsessionid
===============================================================
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
export czgmck="[{'name':'xxx','ck':'gfsessionid=xxx'},{'name':'xxx','ck':'gfsessionid=xxx'},]"
---------------------------------------------------------------
no module named lxml 解决方案
1. 配置文件搜索 PipMirror，如果网址包含douban的，请改为下方的网址
PipMirror="https://pypi.tuna.tsinghua.edu.cn/simple"
2. 依赖管理-python 添加 lxml
3. 如果装不上，①请ssh连接到服务器 ②docker exec -it ql bash (ql是青龙容器的名字，不会就问百度) ③pip install pip -U
4. 再装不上依赖就放弃吧
===============================================================
"""
from io import StringIO
import threading
import ast
import hashlib
import json
import os
import random
import re
from queue import Queue
import requests
import datetime

try:
    from lxml import etree
except:
    print('请仔细阅读脚本上方注释中的“no module named lxml 解决方案”')
    exit()
import time

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
txbz = 8000  # 不低于3000，平台3000起提
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

checklist =['MzkyMzI5NjgxMA==','MzkzMzI5NjQ3MA==','Mzg5NTU4MzEyNQ==','Mzg3NzY5Nzg0NQ==','MzU5OTgxNjg1Mg==','Mzg4OTY5Njg4Mw==','MzI1ODcwNTgzNA==',"Mzg2NDY5NzU0Mw==",]#line:94
def ftime ():#line:97
    OOO0OOO0OO0OOO0OO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:98
    return OOO0OOO0OO0OOO0OO #line:99
def debugger (OO0OOOOOOO0OOOOOO ):#line:102
    if debug :#line:103
        print (OO0OOOOOOO0OOOOOO )#line:104
def printlog (O000OO00O000OO0OO ):#line:107
    if printf :#line:108
        print (O000OO00O000OO0OO )#line:109
def push (OO0OO0OO000O0O000 ,OOO00OOOO0O0OOOO0 ,O0OO0O00OOOO000O0 ,uid =None ):#line:112
    if uid :#line:113
        uids .append (uid )#line:114
    OOOOO00OO0OO00O00 ="<font size=5>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',OO0OO0OO000O0O000 ).replace ('url',O0OO0O00OOOO000O0 )#line:116
    OOOOOO0O000O0OOOO ={"appToken":appToken ,"content":OOOOO00OO0OO00O00 ,"summary":OOO00OOOO0O0OOOO0 ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":O0OO0O00OOOO000O0 ,"verifyPay":False }#line:126
    OO0O0000O000O0O0O ='http://wxpusher.zjiecode.com/api/send/message'#line:127
    OOO00OOOO0O0OO0O0 =requests .post (url =OO0O0000O000O0O0O ,json =OOOOOO0O000O0OOOO ).json ()#line:128
    if OOO00OOOO0O0OO0O0 .get ('code')!=1000 :#line:129
        print (OOO00OOOO0O0OO0O0 .get ('msg'),OOO00OOOO0O0OO0O0 )#line:130
    return OOO00OOOO0O0OO0O0 #line:131
def send (O00000OO0OOO00O00 ,title ='通知',url =None ):#line:134
    if not title or not url :#line:135
        OO000OO0O0OOOOOOO ={"msgtype":"text","text":{"content":f"{title}\n\n{O00000OO0OOO00O00}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:142
    else :#line:143
        OO000OO0O0OOOOOOO ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O00000OO0OOO00O00 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:148
    OO00OOOOO0OO000O0 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:149
    O00OOOO0OO00O0O0O =requests .post (OO00OOOOO0OO000O0 ,data =json .dumps (OO000OO0O0OOOOOOO )).json ()#line:150
    if O00OOOO0OO00O0O0O .get ('errcode')!=0 :#line:151
        print ('消息发送失败，请检查key和发送格式')#line:152
        return False #line:153
    return O00OOOO0OO00O0O0O #line:154
def getmpinfo (O0OO00OOOO00O0000 ):#line:157
    if not O0OO00OOOO00O0000 or O0OO00OOOO00O0000 =='':#line:158
        return False #line:159
    OOOOO0OO00O0O000O ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:161
    OO0O0OOOO0O0OO000 =requests .get (O0OO00OOOO00O0000 ,headers =OOOOO0OO00O0O000O )#line:162
    O000O0OOOO000OO00 =etree .HTML (OO0O0OOOO0O0OO000 .text )#line:163
    O0OO0000O0OO00O0O =O000O0OOOO000OO00 .xpath ('//meta[@*="og:title"]/@content')#line:165
    if O0OO0000O0OO00O0O :#line:166
        O0OO0000O0OO00O0O =O0OO0000O0OO00O0O [0 ]#line:167
    OOOOOOOOOO0OO0OO0 =O000O0OOOO000OO00 .xpath ('//meta[@*="og:url"]/@content')#line:168
    if OOOOOOOOOO0OO0OO0 :#line:169
        OOOOOOOOOO0OO0OO0 =OOOOOOOOOO0OO0OO0 [0 ].encode ().decode ()#line:170
    try :#line:171
        O0O0OOO00OOOO0000 =re .findall (r'biz=(.*?)&',O0OO00OOOO00O0000 )#line:172
    except :#line:173
        O0O0OOO00OOOO0000 =re .findall (r'biz=(.*?)&',OOOOOOOOOO0OO0OO0 )#line:174
    if O0O0OOO00OOOO0000 :#line:175
        O0O0OOO00OOOO0000 =O0O0OOO00OOOO0000 [0 ]#line:176
    else :#line:177
        return False #line:178
    O00OOO00OO0O0O0OO =O000O0OOOO000OO00 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:179
    if O00OOO00OO0O0O0OO :#line:180
        O00OOO00OO0O0O0OO =O00OOO00OO0O0O0OO [0 ].strip ()#line:181
    OO0OO0OOO0OOOO0OO =re .findall (r"user_name.DATA'\) : '(.*?)'",OO0O0OOOO0O0OO000 .text )or O000O0OOOO000OO00 .xpath ('//span[@class="profile_meta_value"]/text()')#line:183
    if OO0OO0OOO0OOOO0OO :#line:184
        OO0OO0OOO0OOOO0OO =OO0OO0OOO0OOOO0OO [0 ]#line:185
    O0O0O0OOOOOO000O0 =re .findall (r'createTime = \'(.*)\'',OO0O0OOOO0O0OO000 .text )#line:186
    if O0O0O0OOOOOO000O0 :#line:187
        O0O0O0OOOOOO000O0 =O0O0O0OOOOOO000O0 [0 ][5 :]#line:188
    OO00O0O00O0O00OOO =f'{O0O0O0OOOOOO000O0}|{O0OO0000O0OO00O0O}|{O0O0OOO00OOOO0000}|{O00OOO00OO0O0O0OO}|{OO0OO0OOO0OOOO0OO}'#line:189
    O000OOO000O0OOOOO ={'biz':O0O0OOO00OOOO0000 ,'text':OO00O0O00O0O00OOO }#line:190
    return O000OOO000O0OOOOO #line:191
class CZGM :#line:194
    def __init__ (O0O00OO0OO0O000O0 ,OOO00O00000O00OO0 ):#line:195
        O0O00OO0OO0O000O0 .name =OOO00O00000O00OO0 ['name']#line:196
        O0O00OO0OO0O000O0 .headers ={"User-Agent":"Mozilla/5.0 (Linux; Android 9; V1923A Build/PQ3B.190801.06161913; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36 MMWEBID/5635 MicroMessenger/8.0.40.2420(0x28002837) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64","Cookie":OOO00O00000O00OO0 ['ck']}#line:200
        O0O00OO0OO0O000O0 .sec =requests .session ()#line:201
        O0O00OO0OO0O000O0 .sec .headers =O0O00OO0OO0O000O0 .headers #line:202
        O0O00OO0OO0O000O0 .sio =StringIO ()#line:203
    @staticmethod #line:205
    def sha_256 (O000000O0OOOOOO00 ):#line:206
        OOOOOO0OOO0000000 =f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={O000000O0OOOOOO00}'#line:207
        O0O0O00OOOOOOO000 =hashlib .sha256 ()#line:208
        O0O0O00OOOOOOO000 .update (OOOOOO0OOO0000000 .encode ())#line:209
        OOOOOOO0O0O0OO0OO =O0O0O00OOOOOOO000 .hexdigest ()#line:210
        return OOOOOOO0O0O0OO0OO #line:211
    def get_share_link (OOOOOO00O0000O00O ):#line:213
        O00O0000O00OOOOOO ='http://2502567.dx.wcydtd.7tojpq6xbpco0.cloud/share'#line:214
        OO0O0O000OO0O0OO0 ={"time":str (int (time .time ())),"sign":OOOOOO00O0000O00O .sha_256 (str (int (time .time ())))}#line:218
        O0O0OO0OOO00OOO0O =OOOOOO00O0000O00O .sec .get (O00O0000O00OOOOOO ,data =OO0O0O000OO0O0OO0 ).json ()#line:219
        O000OO0O0O0000O00 =O0O0OO0OOO00OOO0O ['data']['share_link'][0 ]#line:220
        return O000OO0O0O0000O00 #line:221
    def read_info (OOOOO00O00000O0OO ):#line:223
        try :#line:224
            OO0OOOOO0O0OOO0OO =f'http://2502567.dx.wcydtd.7tojpq6xbpco0.cloud/read/info'#line:225
            O0000O0O000O0OO0O ={"time":str (int (time .time ())),"sign":OOOOO00O00000O0OO .sha_256 (str (int (time .time ())))}#line:229
            OO00O0OOOO0O00OOO =OOOOO00O00000O0OO .sec .get (OO0OOOOO0O0OOO0OO ,data =O0000O0O000O0OO0O )#line:230
            debugger (f'readfinfo {OO00O0OOOO0O00OOO.text}')#line:231
            try :#line:232
                OOO0OOOOO0O0OO0O0 =OO00O0OOOO0O00OOO .json ()#line:233
                OOOOO00O00000O0OO .remain =OOO0OOOOO0O0OO0O0 .get ("data").get ("remain")#line:234
                O000O0OO0O000000O =f'今日已经阅读了{OOO0OOOOO0O0OO0O0.get("data").get("read")}篇文章，今日总金币{OOO0OOOOO0O0OO0O0.get("data").get("gold")}，剩余{OOOOO00O00000O0OO.remain}\n邀请链接：{OOOOO00O00000O0OO.get_share_link()}'#line:235
                printlog (f'{OOOOO00O00000O0OO.name}:{O000O0OO0O000000O}')#line:236
                OOOOO00O00000O0OO .sio .write (O000O0OO0O000000O +'\n')#line:237
                return True #line:238
            except :#line:239
                printlog (f'{OOOOO00O00000O0OO.name}:{OO00O0OOOO0O00OOO.text}')#line:240
                OOOOO00O00000O0OO .sio .write (OO00O0OOOO0O00OOO .text +'\n')#line:241
                return False #line:242
        except :#line:243
            printlog (f'{OOOOO00O00000O0OO.name}:获取用户信息失败，账号异常，请检查你的ck')#line:244
            OOOOO00O00000O0OO .sio .write ('获取用户信息失败，账号异常，请检查你的ck\n')#line:245
            send ('{self.name}:获取用户信息失败，账号异常，请检查你的ck','钢镚阅读ck失效通知')#line:246
            return False #line:247
    def task_finish (OOO0O00O000OOOO00 ):#line:249
        O000O000OOOO000O0 ="http://2502567.dx.wcydtd.7tojpq6xbpco0.cloud/read/finish"#line:250
        O0O00OOO0O0000O0O ={"time":str (int (time .time ())),"sign":OOO0O00O000OOOO00 .sha_256 (str (int (time .time ())))}#line:254
        O0O000000OOOO00O0 =OOO0O00O000OOOO00 .sec .post (O000O000OOOO000O0 ,data =O0O00OOO0O0000O0O ).json ()#line:255
        debugger (f'finish {O0O000000OOOO00O0}')#line:256
        OOO0O00O000OOOO00 .sio .write (f'finish  {O0O000000OOOO00O0}\n')#line:257
        if O0O000000OOOO00O0 .get ('code')!=0 :#line:258
            printlog (f'{OOO0O00O000OOOO00.name}:{O0O000000OOOO00O0.get("message")}')#line:259
            OOO0O00O000OOOO00 .sio .write (O0O000000OOOO00O0 .get ('message')+'\n')#line:260
            return False #line:261
        elif O0O000000OOOO00O0 ['data']['check']is False :#line:262
            O0OO000O000O0OOOO =O0O000000OOOO00O0 ['data']['gain']#line:263
            O000O00OOOOOOOOO0 =O0O000000OOOO00O0 ['data']['read']#line:264
            OOO0O00O000OOOO00 .sio .write (f"阅读文章成功，获得钢镚[{O0OO000O000O0OOOO}]，已读{O000O00OOOOOOOOO0}\n")#line:265
            printlog (f'{OOO0O00O000OOOO00.name}: 阅读文章成功，获得钢镚[{O0OO000O000O0OOOO}]，已读{O000O00OOOOOOOOO0}')#line:266
            return True #line:267
    def read (O0O0O0OO0OOOO000O ):#line:269
        while True :#line:270
            O0O0O0OO0OOOO000O .sio .write ('-'*50 +'\n')#line:271
            O0O000OOOO000OO00 =f'http://2502567.dx.wcydtd.7tojpq6xbpco0.cloud/read/task'#line:272
            O00OOO00OO00O0OO0 ={"time":str (int (time .time ())),"sign":O0O0O0OO0OOOO000O .sha_256 (str (int (time .time ())))}#line:276
            OO000OOOO0OOOO0OO =O0O0O0OO0OOOO000O .sec .get (O0O000OOOO000OO00 ,data =O00OOO00OO00O0OO0 ).json ()#line:277
            debugger (f'read {OO000OOOO0OOOO0OO}')#line:278
            if OO000OOOO0OOOO0OO .get ('code')!=0 :#line:279
                O0O0O0OO0OOOO000O .sio .write (OO000OOOO0OOOO0OO ['message']+'\n')#line:280
                printlog (f'{O0O0O0OO0OOOO000O.name}:{OO000OOOO0OOOO0OO["message"]}')#line:281
                return False #line:282
            else :#line:283
                O00OO0O0OOOOO000O =OO000OOOO0OOOO0OO .get ('data').get ('link')#line:284
                printlog (f'{O0O0O0OO0OOOO000O.name}:获取到阅读链接成功')#line:285
                O0O0O0OO0OOOO000O .sio .write (f'获取到阅读链接成功\n')#line:286
                OO00OO00O00OOOO00 =O00OO0O0OOOOO000O .encode ().decode ()#line:287
                O00OOOO0O00O0OO0O =getmpinfo (OO00OO00O00OOOO00 )#line:288
                O000OO00OO00O00OO =O00OOOO0O00O0OO0O ['biz']#line:289
                O0O0O0OO0OOOO000O .sio .write (f'开始阅读 '+O00OOOO0O00O0OO0O ['text']+'\n')#line:290
                printlog (f'{O0O0O0OO0OOOO000O.name}:开始阅读 '+O00OOOO0O00O0OO0O ['text'])#line:291
                if O000OO00OO00O00OO in checklist :#line:292
                    O0O0O0OO0OOOO000O .sio .write ("正在阅读检测文章，发送通知，暂停60秒\n")#line:293
                    printlog (f'{O0O0O0OO0OOOO000O.name}:正在阅读检测文章，发送通知，暂停60秒')#line:294
                    if sendable :#line:295
                        send (O00OOOO0O00O0OO0O ['text'],f'{O0O0O0OO0OOOO000O.name}钢镚阅读检测',OO00OO00O00OOOO00 )#line:296
                    if pushable :#line:297
                        push (f'{O0O0O0OO0OOOO000O.name}\n点击阅读检测文章\n{O00OOOO0O00O0OO0O["text"]}',f'{O0O0O0OO0OOOO000O.name} 钢镚过检测',OO00OO00O00OOOO00 )#line:299
                    time .sleep (60 )#line:300
                O0OO000OOOO0OO0O0 =random .randint (7 ,10 )#line:301
                O0O0O0OO0OOOO000O .sio .write (f'本次模拟阅读{O0OO000OOOO0OO0O0}秒\n')#line:302
                time .sleep (O0OO000OOOO0OO0O0 )#line:303
                O0O0O0OO0OOOO000O .task_finish ()#line:304
    def withdraw (O00O0O00O00OOOO00 ):#line:306
        if O00O0O00O00OOOO00 .remain <txbz :#line:307
            O00O0O00O00OOOO00 .sio .write (f'没有达到你设置的提现标准{txbz}\n')#line:308
            printlog (f'{O00O0O00O00OOOO00.name}:没有达到你设置的提现标准{txbz}')#line:309
            return False #line:310
        O000OO00O0O0OO00O =f'http://2502567.dx.wcydtd.7tojpq6xbpco0.cloud/withdraw/wechat'#line:311
        OO0000OOOO00O0OOO ={"time":str (int (time .time ())),"sign":O00O0O00O00OOOO00 .sha_256 (str (int (time .time ())))}#line:313
        OOO000OOOO000OO0O =O00O0O00O00OOOO00 .sec .get (O000OO00O0O0OO00O ,data =OO0000OOOO00O0OOO ).json ()#line:314
        O00O0O00O00OOOO00 .sio .write (f"提现结果：{OOO000OOOO000OO0O.get('message')}\n")#line:315
        printlog (f'{O00O0O00O00OOOO00.name}:提现结果  {OOO000OOOO000OO0O.get("message")}')#line:316
    def run (O000OOOO0OO00000O ):#line:318
        O000OOOO0OO00000O .sio .write ('='*50 +f'\n账号：{O000OOOO0OO00000O.name}开始任务\n')#line:319
        if O000OOOO0OO00000O .read_info ():#line:320
            O000OOOO0OO00000O .read ()#line:321
            O000OOOO0OO00000O .read_info ()#line:322
            O000OOOO0OO00000O .withdraw ()#line:323
            O0O0O0OO00OOOOO0O =O000OOOO0OO00000O .sio .getvalue ()#line:324
            if not printf :#line:325
                print (O0O0O0OO00OOOOO0O )#line:326
def yd (OOO000O00OOO00OO0 ):#line:329
    while not OOO000O00OOO00OO0 .empty ():#line:330
        OO0O0O0OO00OOOOOO =OOO000O00OOO00OO0 .get ()#line:331
        OOO000000OO000000 =CZGM (OO0O0O0OO00OOOOOO )#line:332
        OOO000000OO000000 .run ()#line:333
def get_ver ():#line:336
    OO0OOO00OOOO0000O ='kzcgm V1.3'#line:337
    OOOO0O0OOOO0000OO ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:340
    OOO00OOOOO000O000 =requests .get ('https://ghproxy.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json',headers =OOOO0O0OOOO0000OO ).json ()#line:342
    O0O00O0O0O00O00OO =OO0OOO00OOOO0000O .split (' ')[1 ]#line:343
    OO00OO0O000OOOOO0 =OOO00OOOOO000O000 .get ('version').get (OO0OOO00OOOO0000O .split (' ')[0 ])#line:344
    O0O000OO0OOOO0OOO =f"当前版本 {O0O00O0O0O00O00OO}，仓库版本 {OO00OO0O000OOOOO0}"#line:345
    if O0O00O0O0O00O00OO <OO00OO0O000OOOOO0 :#line:346
        O0O000OO0OOOO0OOO +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:347
    return O0O000OO0OOOO0OOO #line:348
def main ():#line:351
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:352
    OOOO0OOOO00000O0O =os .getenv ('czgmck')#line:353
    if not OOOO0OOOO00000O0O :#line:354
        print ('请仔细阅读脚本上方注释，并配置好czgmck')#line:355
        exit ()#line:356
    OOO0O00O00O0O0OO0 =[]#line:357
    try :#line:358
        OOOO0OOOO00000O0O =ast .literal_eval (OOOO0OOOO00000O0O )#line:359
    except :#line:360
        pass #line:361
    OO000O0O0O0OOOOOO =Queue ()#line:362
    for OOOOOO0O0000OOO00 ,OO0O0O0O0000OO000 in enumerate (OOOO0OOOO00000O0O ,start =1 ):#line:363
        print (f'{OO0O0O0O0000OO000}\n以上是第{OOOOOO0O0000OOO00}个账号的ck，如不正确，请检查ck填写格式')#line:364
        OO000O0O0O0OOOOOO .put (OO0O0O0O0000OO000 )#line:365
    for OOOOOO0O0000OOO00 in range (max_workers ):#line:366
        O0O0O00000000000O =threading .Thread (target =yd ,args =(OO000O0O0O0OOOOOO ,))#line:367
        O0O0O00000000000O .start ()#line:368
        OOO0O00O00O0O0OO0 .append (O0O0O00000000000O )#line:369
        time .sleep (20 )#line:370
    for OO00O0000OO0O0OOO in OOO0O00O00O0O0OO0 :#line:371
        OO00O0000OO0O0OOO .join ()#line:372
if __name__ =='__main__':#line:375
    main ()#line:376
