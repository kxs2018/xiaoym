# -*- coding: utf-8 -*-
"""
new Env('充值购买（钢镚）');
先运行脚本，有问题再到群里问
充值购买阅读入口：http://2502807.m5zzxd1ywp.9o8883.qhcf3j7v04pa.cloud/?p=2502807
"""

try:
    from config import cmzg_config
except:
    cmzg_config = {
        'printf': 1,  # 实时日志开关,1为开，0为关

        'debug': 1,  # debug模式开关,1为开,0为关

        'max_workers': 5,  # 线程数量设置,设置为5，即最多有5个任务同时进行

        'txbz': 8000,  # 设置提现标准,不低于3000，平台3000起提,设置为8000，即为8毛起提

        'sendable': 1,  # 企业微信推送开关,1为开，0为关开启后必须设置qwbotkey才能运行

        'pushable': 1,  # wxpusher推送开关,1为开，0为关,开启后必须设置pushconfig才能运行

        'delay_time': 30  # 并发延迟设置,设置为30即每隔30秒新增一个号做任务，直到数量达到max_workers
    }

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
import time

def get_msg ():#line:41
    OOO0O0O0OO0O000OO ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:43
    O0OOOO0OOOO0OO00O =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OOO0O0O0OO0O000OO ).json ()#line:44
    return O0OOOO0OOOO0OO00O #line:45
_O0O0000OO0OO00OOO =get_msg ()#line:48
try :#line:49
    from lxml import etree #line:50
except :#line:51
    print (_O0O0000OO0OO00OOO .get ('help')['lxml'])#line:52
printf =cmzg_config ['printf']#line:53
debug =cmzg_config ['debug']#line:54
max_workers =cmzg_config ['max_workers']#line:55
txbz =cmzg_config ['txbz']#line:56
sendable =cmzg_config ['sendable']#line:57
delay_time =cmzg_config ['delay_time']#line:58
pushable =cmzg_config ['pushable']#line:59
if sendable :#line:60
    qwbotkey =os .getenv ('qwbotkey')#line:61
    if not qwbotkey :#line:62
        print (_O0O0000OO0OO00OOO .get ('help')['qwbotkey'])#line:63
        exit ()#line:64
if pushable :#line:66
    pushconfig =os .getenv ('pushconfig')#line:67
    if not pushconfig :#line:68
        print (_O0O0000OO0OO00OOO .get ('help')['pushconfig'])#line:69
        exit ()#line:70
    try :#line:71
        pushconfig =ast .literal_eval (pushconfig )#line:72
    except :#line:73
        pass #line:74
    if isinstance (pushconfig ,dict ):#line:75
        appToken =pushconfig ['appToken']#line:76
        uids =pushconfig ['uids']#line:77
        topicids =pushconfig ['topicids']#line:78
    else :#line:79
        try :#line:80
            "appToken=AT_pCenRjs;uids=['UID_9MZ','UID_T4xlqWx9x'];topicids=['xxx']"#line:81
            appToken =pushconfig .split (';')[0 ].split ('=')[1 ]#line:82
            uids =ast .literal_eval (pushconfig .split (';')[1 ].split ('=')[1 ])#line:83
            topicids =ast .literal_eval (pushconfig .split (';')[2 ].split ('=')[1 ])#line:84
        except :#line:85
            print (_O0O0000OO0OO00OOO .get ('help')['pushconfig'])#line:86
            exit ()#line:87
if not pushable and not sendable :#line:88
    print ('啥通知方式都不配置，你想上天吗')#line:89
    exit ()#line:90
checklist =['MzkyMzI5NjgxMA==','MzkzMzI5NjQ3MA==','Mzg5NTU4MzEyNQ==','Mzg3NzY5Nzg0NQ==','MzU5OTgxNjg1Mg==','Mzg4OTY5Njg4Mw==','MzI1ODcwNTgzNA==',"Mzg2NDY5NzU0Mw==",]#line:95
def ftime ():#line:98
    O00OOO0OO00OOOOOO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:99
    return O00OOO0OO00OOOOOO #line:100
def debugger (OO0OOO000O000OO00 ):#line:103
    if debug :#line:104
        print (OO0OOO000O000OO00 )#line:105
def printlog (OO0OO000OOO00O000 ):#line:108
    if printf :#line:109
        print (OO0OO000OOO00O000 )#line:110
def send (O0O0O0O0O000OO0OO ,title ='通知',url =None ):#line:113
    if not url :#line:114
        OOO000OOO000O00OO ={"msgtype":"text","text":{"content":f"{title}\n\n{O0O0O0O0O000OO0OO}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:121
    else :#line:122
        OOO000OOO000O00OO ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O0O0O0O0O000OO0OO ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:127
    OO00OO0OO0O000000 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:128
    O0O000O00O0O000O0 =requests .post (OO00OO0OO0O000000 ,data =json .dumps (OOO000OOO000O00OO )).json ()#line:129
    if O0O000O00O0O000O0 .get ('errcode')!=0 :#line:130
        print ('消息发送失败，请检查key和发送格式')#line:131
        return False #line:132
    return O0O000O00O0O000O0 #line:133
def push (OO0O00OOOO00O0OO0 ,title ='通知',url ='',uid =None ):#line:136
    if uid :#line:137
        uids .append (uid )#line:138
    OO0O0O00000OO0OO0 ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',OO0O00OOOO00O0OO0 ).replace ('url',url )#line:140
    O0000O000OO0O000O ={"appToken":appToken ,"content":OO0O0O00000OO0OO0 ,"summary":title ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:150
    OO0O0O00O00OO0OOO ='http://wxpusher.zjiecode.com/api/send/message'#line:151
    OOO00O0O0O0O00OOO =requests .post (url =OO0O0O00O00OO0OOO ,json =O0000O000OO0O000O ).json ()#line:152
    if OOO00O0O0O0O00OOO .get ('code')!=1000 :#line:153
        print (OOO00O0O0O0O00OOO .get ('msg'),OOO00O0O0O0O00OOO )#line:154
    return OOO00O0O0O0O00OOO #line:155
def getmpinfo (O00O0O0OOO0OOOO00 ):#line:158
    if not O00O0O0OOO0OOOO00 or O00O0O0OOO0OOOO00 =='':#line:159
        return False #line:160
    OO00OOOO0OO00O00O ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:162
    O000OO000O0OOO000 =requests .get (O00O0O0OOO0OOOO00 ,headers =OO00OOOO0OO00O00O )#line:163
    OO0O0OOOO00OO0O00 =etree .HTML (O000OO000O0OOO000 .text )#line:164
    O0O000OOOO0OO0OO0 =OO0O0OOOO00OO0O00 .xpath ('//meta[@*="og:title"]/@content')#line:165
    if O0O000OOOO0OO0OO0 :#line:166
        O0O000OOOO0OO0OO0 =O0O000OOOO0OO0OO0 [0 ]#line:167
    try :#line:168
        if 'biz='in O00O0O0OOO0OOOO00 :#line:169
            OOOOO0OO00O0OO00O =re .findall (r'biz=(.*?)&',O00O0O0OOO0OOOO00 )[0 ]#line:170
        else :#line:171
            OO0OOOO00O000OOOO =OO0O0OOOO00OO0O00 .xpath ('//meta[@*="og:url"]/@content')[0 ]#line:172
            OOOOO0OO00O0OO00O =re .findall (r'biz=(.*?)&',str (OO0OOOO00O000OOOO ))[0 ]#line:173
    except :#line:174
        return False #line:175
    O0OOO0OOO00O0O000 =OO0O0OOOO00OO0O00 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:176
    if O0OOO0OOO00O0O000 :#line:177
        O0OOO0OOO00O0O000 =O0OOO0OOO00O0O000 [0 ].strip ()#line:178
    OO0O00O00OOO0O00O =re .findall (r"user_name.DATA'\) : '(.*?)'",O000OO000O0OOO000 .text )or OO0O0OOOO00OO0O00 .xpath ('//span[@class="profile_meta_value"]/text()')#line:180
    if OO0O00O00OOO0O00O :#line:181
        OO0O00O00OOO0O00O =OO0O00O00OOO0O00O [0 ]#line:182
    OOO00OOOO000OO0OO =re .findall (r'createTime = \'(.*)\'',O000OO000O0OOO000 .text )#line:183
    if OOO00OOOO000OO0OO :#line:184
        OOO00OOOO000OO0OO =OOO00OOOO000OO0OO [0 ][5 :]#line:185
    OO0O0OOO0OOO0O0O0 =f'{OOO00OOOO000OO0OO}|{O0O000OOOO0OO0OO0[:11]}|{OOOOO0OO00O0OO00O}|{O0OOO0OOO00O0O000}|{OO0O00O00OOO0O00O}'#line:186
    O0O0O00OOOOO0O0O0 ={'biz':OOOOO0OO00O0OO00O ,'text':OO0O0OOO0OOO0O0O0 }#line:187
    return O0O0O00OOOOO0O0O0 #line:188
class CZGM :#line:191
    def __init__ (OOO0OOO0000O00O0O ,OO00000OOOO000OOO ):#line:192
        OOO0OOO0000O00O0O .name =OO00000OOOO000OOO ['name']#line:193
        OOO0OOO0000O00O0O .uid =OO00000OOOO000OOO .get ('uid')#line:194
        OOO0OOO0000O00O0O .headers ={"User-Agent":"Mozilla/5.0 (Linux; Android 9; V1923A Build/PQ3B.190801.06161913; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36 MMWEBID/5635 MicroMessenger/8.0.40.2420(0x28002837) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64","Cookie":OO00000OOOO000OOO ['ck']}#line:198
        OOO0OOO0000O00O0O .sec =requests .session ()#line:199
        OOO0OOO0000O00O0O .sec .headers =OOO0OOO0000O00O0O .headers #line:200
        OOO0OOO0000O00O0O .sio =StringIO ()#line:201
    @staticmethod #line:203
    def sha_256 (O00O00O0000OOOOOO ):#line:204
        O0OOO000O0OO0OO0O =f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={O00O00O0000OOOOOO}'#line:205
        O00O000OOOOO000OO =hashlib .sha256 ()#line:206
        O00O000OOOOO000OO .update (O0OOO000O0OO0OO0O .encode ())#line:207
        OO0O000OO0OOOOOOO =O00O000OOOOO000OO .hexdigest ()#line:208
        return OO0O000OO0OOOOOOO #line:209
    def get_share_link (OOO0OOO0O000OOO0O ):#line:211
        O00O00O0O0OOO0O0O ='http://2502567.dx.wcydtd.7tojpq6xbpco0.cloud/share'#line:212
        OO0OOOOO0OO0OO00O ={"time":str (int (time .time ())),"sign":OOO0OOO0O000OOO0O .sha_256 (str (int (time .time ())))}#line:216
        O0OOOOO000000O0OO =OOO0OOO0O000OOO0O .sec .get (O00O00O0O0OOO0O0O ,data =OO0OOOOO0OO0OO00O ).json ()#line:217
        OO0O00O0O0O0OO0OO =O0OOOOO000000O0OO ['data']['share_link'][0 ]#line:218
        return OO0O00O0O0O0OO0OO #line:219
    def read_info (OO00O000O000O000O ):#line:221
        try :#line:222
            O0O000O000OOO00OO =f'http://2502567.dx.wcydtd.7tojpq6xbpco0.cloud/read/info'#line:223
            OOO0O0OOOO0O0O0OO ={"time":str (int (time .time ())),"sign":OO00O000O000O000O .sha_256 (str (int (time .time ())))}#line:227
            OOOOOOOOO0OO0OOOO =OO00O000O000O000O .sec .get (O0O000O000OOO00OO ,data =OOO0O0OOOO0O0O0OO )#line:228
            debugger (f'readfinfo {OOOOOOOOO0OO0OOOO.text}')#line:229
            try :#line:230
                OO0O0O00O0O0O0O0O =OOOOOOOOO0OO0OOOO .json ()#line:231
                OO00O000O000O000O .remain =OO0O0O00O0O0O0O0O .get ("data").get ("remain")#line:232
                O00000O0O00OO0OO0 =f'今日已经阅读了{OO0O0O00O0O0O0O0O.get("data").get("read")}篇文章，今日总金币{OO0O0O00O0O0O0O0O.get("data").get("gold")}，剩余{OO00O000O000O000O.remain}'#line:233
                debugger (f'【{OO00O000O000O000O.name}】邀请链接：{OO00O000O000O000O.get_share_link()}')#line:234
                printlog (f'【{OO00O000O000O000O.name}】:{O00000O0O00OO0OO0}')#line:235
                OO00O000O000O000O .sio .write (O00000O0O00OO0OO0 +'\n')#line:236
                return True #line:237
            except :#line:238
                printlog (f'【{OO00O000O000O000O.name}】:{OOOOOOOOO0OO0OOOO.text}')#line:239
                OO00O000O000O000O .sio .write (OOOOOOOOO0OO0OOOO .text +'\n')#line:240
                return False #line:241
        except :#line:242
            printlog (f'【{OO00O000O000O000O.name}】:获取用户信息失败，账号异常，请检查你的ck')#line:243
            OO00O000O000O000O .sio .write ('获取用户信息失败，账号异常，请检查你的ck\n')#line:244
            send (f'【{OO00O000O000O000O.name}】:获取用户信息失败，账号异常，请检查你的ck','钢镚阅读ck失效通知')#line:245
            return False #line:246
    def task_finish (O0O0O0OO00000O000 ):#line:248
        O00O000O0OOO0O000 ="http://2502567.dx.wcydtd.7tojpq6xbpco0.cloud/read/finish"#line:249
        OO00O0O0O00000O0O =str (int (time .time ()))#line:250
        O00OO000O0O000OOO ={"time":OO00O0O0O00000O0O ,"sign":O0O0O0OO00000O000 .sha_256 (OO00O0O0O00000O0O )}#line:254
        OOOOOOO0O000O00OO =O0O0O0OO00000O000 .sec .post (O00O000O0OOO0O000 ,data =O00OO000O0O000OOO ).json ()#line:255
        debugger (f'finish {OOOOOOO0O000O00OO}')#line:256
        O0O0O0OO00000O000 .sio .write (f'finish  {OOOOOOO0O000O00OO}\n')#line:257
        if OOOOOOO0O000O00OO .get ('code')!=0 :#line:258
            printlog (f'【{O0O0O0OO00000O000.name}】:{OOOOOOO0O000O00OO.get("message")}')#line:259
            O0O0O0OO00000O000 .sio .write (OOOOOOO0O000O00OO .get ('message')+'\n')#line:260
            return False #line:261
        elif OOOOOOO0O000O00OO ['data']['check']is False :#line:262
            O0O000O0OOOOOO0OO =OOOOOOO0O000O00OO ['data']['gain']#line:263
            OOO0000O0OOOO00O0 =OOOOOOO0O000O00OO ['data']['read']#line:264
            O0O0O0OO00000O000 .sio .write (f"阅读文章成功，获得钢镚[{O0O000O0OOOOOO0OO}]，已读{OOO0000O0OOOO00O0}\n")#line:265
            printlog (f'【{O0O0O0OO00000O000.name}】: 阅读文章成功，获得钢镚[{O0O000O0OOOOOO0OO}]，已读{OOO0000O0OOOO00O0}')#line:266
            return True #line:267
    def read (OO0OO0OO00O0O00O0 ):#line:269
        while True :#line:270
            OO0OO0OO00O0O00O0 .sio .write ('-'*50 +'\n')#line:271
            OO0O00OOOOOO000OO =str (int (time .time ()))#line:272
            OOOOOOO0OO00OO000 =f'http://2502567.dx.wcydtd.7tojpq6xbpco0.cloud/read/task'#line:273
            OOO0OO0O000OO0O0O ={"time":OO0O00OOOOOO000OO ,"sign":OO0OO0OO00O0O00O0 .sha_256 (OO0O00OOOOOO000OO )}#line:277
            OOOOOOO0OOOO00OO0 =OO0OO0OO00O0O00O0 .sec .get (OOOOOOO0OO00OO000 ,data =OOO0OO0O000OO0O0O ).json ()#line:278
            debugger (f'read {OOOOOOO0OOOO00OO0}')#line:279
            if OOOOOOO0OOOO00OO0 .get ('code')!=0 :#line:280
                OO0OO0OO00O0O00O0 .sio .write (OOOOOOO0OOOO00OO0 ['message']+'\n')#line:281
                printlog (f'【{OO0OO0OO00O0O00O0.name}】:{OOOOOOO0OOOO00OO0["message"]}')#line:282
                return False #line:283
            else :#line:284
                O000OO00O0O0O000O =OOOOOOO0OOOO00OO0 .get ('data').get ('link')#line:285
                printlog (f'【{OO0OO0OO00O0O00O0.name}】:获取到阅读链接成功')#line:286
                OO0OO0OO00O0O00O0 .sio .write (f'获取到阅读链接成功\n')#line:287
                OOO0O000O00O0000O =O000OO00O0O0O000O .encode ().decode ()#line:288
                OO00OO00O0000OO00 =getmpinfo (OOO0O000O00O0000O )#line:289
                O00O00O00OOO0OO0O =OO00OO00O0000OO00 ['biz']#line:290
                OO0OO0OO00O0O00O0 .sio .write (f'开始阅读 '+OO00OO00O0000OO00 ['text']+'\n')#line:291
                printlog (f'【{OO0OO0OO00O0O00O0.name}】:开始阅读 '+OO00OO00O0000OO00 ['text'])#line:292
                if O00O00O00OOO0OO0O in checklist :#line:293
                    OO0OO0OO00O0O00O0 .sio .write ("正在阅读检测文章，发送通知，暂停60秒\n")#line:294
                    printlog (f'【{OO0OO0OO00O0O00O0.name}】:正在阅读检测文章，发送通知，暂停60秒')#line:295
                    if sendable :#line:296
                        send (OO00OO00O0000OO00 ['text'],f'【{OO0OO0OO00O0O00O0.name}】钢镚阅读检测',OOO0O000O00O0000O )#line:297
                    if pushable :#line:298
                        push (f'【{OO0OO0OO00O0O00O0.name}】\n点击阅读检测文章\n{OO00OO00O0000OO00["text"]}',f'【{OO0OO0OO00O0O00O0.name}】 钢镚过检测',OOO0O000O00O0000O ,OO0OO0OO00O0O00O0 .uid )#line:300
                    time .sleep (60 )#line:301
                OO0O00OOOOOO000OO =random .randint (7 ,10 )#line:302
                OO0OO0OO00O0O00O0 .sio .write (f'本次模拟阅读{OO0O00OOOOOO000OO}秒\n')#line:303
                time .sleep (OO0O00OOOOOO000OO )#line:304
                OO0OO0OO00O0O00O0 .task_finish ()#line:305
    def withdraw (OO0OOOO00O0OOOO0O ):#line:307
        if OO0OOOO00O0OOOO0O .remain <txbz :#line:308
            OO0OOOO00O0OOOO0O .sio .write (f'没有达到你设置的提现标准{txbz}\n')#line:309
            printlog (f'【{OO0OOOO00O0OOOO0O.name}】:没有达到你设置的提现标准{txbz}')#line:310
            return False #line:311
        OOOO00OOOOO0OO0OO =f'http://2502567.dx.wcydtd.7tojpq6xbpco0.cloud/withdraw/wechat'#line:312
        OO0OO0O0OO0OOO0OO =str (int (time .time ()))#line:313
        OO0OO0000O0OO000O ={"time":OO0OO0O0OO0OOO0OO ,"sign":OO0OOOO00O0OOOO0O .sha_256 (OO0OO0O0OO0OOO0OO )}#line:315
        O000OOOOO00OOOOOO =OO0OOOO00O0OOOO0O .sec .get (OOOO00OOOOO0OO0OO ,data =OO0OO0000O0OO000O ).json ()#line:316
        OO0OOOO00O0OOOO0O .sio .write (f"提现结果：{O000OOOOO00OOOOOO.get('message')}\n")#line:317
        printlog (f'【{OO0OOOO00O0OOOO0O.name}】:提现结果  {O000OOOOO00OOOOOO.get("message")}')#line:318
    def run (OOO0OOOOO000OOOO0 ):#line:320
        OOO0OOOOO000OOOO0 .sio .write ('='*50 +f'\n【{OOO0OOOOO000OOOO0.name}】:开始任务\n')#line:321
        if OOO0OOOOO000OOOO0 .read_info ():#line:322
            OOO0OOOOO000OOOO0 .read ()#line:323
            OOO0OOOOO000OOOO0 .read_info ()#line:324
            OOO0OOOOO000OOOO0 .withdraw ()#line:325
            OO00OOO00000O0OOO =OOO0OOOOO000OOOO0 .sio .getvalue ()#line:326
            if not printf :#line:327
                print (OO00OOO00000O0OOO )#line:328
def yd (OOO0000000O0000OO ):#line:331
    while not OOO0000000O0000OO .empty ():#line:332
        O00OO000O000O0O00 =OOO0000000O0000OO .get ()#line:333
        OOO00OOOOO0OOOOO0 =CZGM (O00OO000O000O0O00 )#line:334
        OOO00OOOOO0OOOOO0 .run ()#line:335
def get_info ():#line:338
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:340
    print ('入口：http://2502807.m5zzxd1ywp.9o8883.qhcf3j7v04pa.cloud/?p=2502807')#line:341
    OO00OO000OO0O0O00 ='V1.5'#line:342
    O0O000O0O000OO0OO =_O0O0000OO0OO00OOO ['version']['钢镚']#line:343
    print (f'当前版本{OO00OO000OO0O0O00}，仓库版本{O0O000O0O000OO0OO}\n{_O0O0000OO0OO00OOO["update_log"]["钢镚"]}')#line:344
    if OO00OO000OO0O0O00 <O0O000O0O000OO0OO :#line:345
        print ('请到仓库下载最新版本k_czgm.py')#line:346
    print ("="*25 )#line:347
def main ():#line:350
    get_info ()#line:351
    O0OO0000O000OO0O0 =os .getenv ('czgmck')#line:352
    if not O0OO0000O000OO0O0 :#line:353
        print (_O0O0000OO0OO00OOO .get ('msg')['钢镚'])#line:354
        exit ()#line:355
    O00O00O0O0OOOO000 =[]#line:356
    try :#line:357
        O0OO0000O000OO0O0 =ast .literal_eval (O0OO0000O000OO0O0 )#line:358
    except :#line:359
        pass #line:360
    OOOO0O00O0OO0OOOO =Queue ()#line:361
    for OO000OO0000000OOO ,O0OOO00000O0O00O0 in enumerate (O0OO0000O000OO0O0 ,start =1 ):#line:362
        print (f'{O0OOO00000O0O00O0}\n以上是第{OO000OO0000000OOO}个账号的ck，如不正确，请检查ck填写格式')#line:363
        OOOO0O00O0OO0OOOO .put (O0OOO00000O0O00O0 )#line:364
    for OO000OO0000000OOO in range (max_workers ):#line:365
        OO0O0000O00OO0OOO =threading .Thread (target =yd ,args =(OOOO0O00O0OO0OOOO ,))#line:366
        OO0O0000O00OO0OOO .start ()#line:367
        O00O00O0O0OOOO000 .append (OO0O0000O00OO0OOO )#line:368
        time .sleep (delay_time )#line:369
    for O0OOOO0O000OOO0O0 in O00O00O0O0OOOO000 :#line:370
        O0OOOO0O000OOO0O0 .join ()#line:371
if __name__ =='__main__':#line:374
    main ()#line:375
