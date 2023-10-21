# -*- coding: utf-8 -*-
"""
new Env('充值购买（钢镚）');
先运行脚本，有问题再到群里问 https://t.me/xiaoymgroup
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
from urllib.parse import urlparse

def get_msg ():#line:40
    O00O00O00O0O0O0O0 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:42
    O0O00000O00O0000O =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O00O00O00O0O0O0O0 ).json ()#line:43
    return O0O00000O00O0000O #line:44
_OO00OO000O00O0000 =get_msg ()#line:47
try :#line:48
    from lxml import etree #line:49
except :#line:50
    print (_OO00OO000O00O0000 .get ('help')['lxml'])#line:51
printf =cmzg_config ['printf']#line:52
debug =cmzg_config ['debug']#line:53
max_workers =cmzg_config ['max_workers']#line:54
txbz =cmzg_config ['txbz']#line:55
sendable =cmzg_config ['sendable']#line:56
delay_time =cmzg_config ['delay_time']#line:57
pushable =cmzg_config ['pushable']#line:58
if sendable :#line:59
    qwbotkey =os .getenv ('qwbotkey')#line:60
    if not qwbotkey :#line:61
        print (_OO00OO000O00O0000 .get ('help')['qwbotkey'])#line:62
        exit ()#line:63
if pushable :#line:65
    pushconfig =os .getenv ('pushconfig')#line:66
    if not pushconfig :#line:67
        print (_OO00OO000O00O0000 .get ('help')['pushconfig'])#line:68
        exit ()#line:69
    try :#line:70
        pushconfig =ast .literal_eval (pushconfig )#line:71
    except :#line:72
        pass #line:73
    if isinstance (pushconfig ,dict ):#line:74
        appToken =pushconfig ['appToken']#line:75
        uids =pushconfig ['uids']#line:76
        topicids =pushconfig ['topicids']#line:77
    else :#line:78
        try :#line:79
            "appToken=AT_pCenRjs;uids=['UID_9MZ','UID_T4xlqWx9x'];topicids=['xxx']"#line:80
            appToken =pushconfig .split (';')[0 ].split ('=')[1 ]#line:81
            uids =ast .literal_eval (pushconfig .split (';')[1 ].split ('=')[1 ])#line:82
            topicids =ast .literal_eval (pushconfig .split (';')[2 ].split ('=')[1 ])#line:83
        except :#line:84
            print (_OO00OO000O00O0000 .get ('help')['pushconfig'])#line:85
            exit ()#line:86
if not pushable and not sendable :#line:87
    print ('啥通知方式都不配置，你想上天吗')#line:88
    exit ()#line:89
checklist =['MzkyMzI5NjgxMA==','MzkzMzI5NjQ3MA==','Mzg5NTU4MzEyNQ==','Mzg3NzY5Nzg0NQ==','MzU5OTgxNjg1Mg==','Mzg4OTY5Njg4Mw==','MzI1ODcwNTgzNA==',"Mzg2NDY5NzU0Mw==",]#line:94
def ftime ():#line:97
    OO0O0O00000OOOO0O =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:98
    return OO0O0O00000OOOO0O #line:99
def debugger (O00OOO0000OOOOOOO ):#line:102
    if debug :#line:103
        print (O00OOO0000OOOOOOO )#line:104
def printlog (O00O0OO0000000000 ):#line:107
    if printf :#line:108
        print (O00O0OO0000000000 )#line:109
def send (OOOO00000O0O00OO0 ,title ='通知',url =None ):#line:112
    if not url :#line:113
        O0OO0000O0OOO0OO0 ={"msgtype":"text","text":{"content":f"{title}\n\n{OOOO00000O0O00OO0}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg群：https://t.me/xiaoymgroup\n通知时间：{ftime()}",}}#line:120
    else :#line:121
        O0OO0000O0OOO0OO0 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":OOOO00000O0O00OO0 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:126
    OO0OOO0O000O0OO00 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:127
    OO0O0OO0O0O0OO0O0 =requests .post (OO0OOO0O000O0OO00 ,data =json .dumps (O0OO0000O0OOO0OO0 )).json ()#line:128
    if OO0O0OO0O0O0OO0O0 .get ('errcode')!=0 :#line:129
        print ('消息发送失败，请检查key和发送格式')#line:130
        return False #line:131
    return OO0O0OO0O0O0OO0O0 #line:132
def push (O0000O0O0000OO0O0 ,title ='通知',url ='',uid =None ):#line:135
    if uid :#line:136
        uids .clear ()#line:137
        uids .append (uid )#line:138
    O0000000OOO00OOOO ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入tg群](https://t.me/xiaoymgroup)</font>".replace ('msg',O0000O0O0000OO0O0 ).replace ('url',url )#line:140
    O0OOOOOO0O0OOO0OO ={"appToken":appToken ,"content":O0000000OOO00OOOO ,"summary":title ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:150
    O0OO00OO00O000O00 ='http://wxpusher.zjiecode.com/api/send/message'#line:151
    O0O000OOO0O0OO00O =requests .post (url =O0OO00OO00O000O00 ,json =O0OOOOOO0O0OOO0OO ).json ()#line:152
    if O0O000OOO0O0OO00O .get ('code')!=1000 :#line:153
        print (O0O000OOO0O0OO00O .get ('msg'),O0O000OOO0O0OO00O )#line:154
    return O0O000OOO0O0OO00O #line:155
def getmpinfo (OO000OO0O0O000O00 ):#line:158
    if not OO000OO0O0O000O00 or OO000OO0O0O000O00 =='':#line:159
        return False #line:160
    OO0OOOO00OOOO0O00 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:162
    OOOOOO0O00O00O0O0 =requests .get (OO000OO0O0O000O00 ,headers =OO0OOOO00OOOO0O00 )#line:163
    OO0000O0OOOO000O0 =etree .HTML (OOOOOO0O00O00O0O0 .text )#line:164
    O00OOOOOOO000OOO0 =OO0000O0OOOO000O0 .xpath ('//meta[@*="og:title"]/@content')#line:165
    if O00OOOOOOO000OOO0 :#line:166
        O00OOOOOOO000OOO0 =O00OOOOOOO000OOO0 [0 ]#line:167
    try :#line:168
        if 'biz='in OO000OO0O0O000O00 :#line:169
            OOOOO0O00O0OO000O =re .findall (r'biz=(.*?)&',OO000OO0O0O000O00 )[0 ]#line:170
        else :#line:171
            OO0000OOOO0O00OO0 =OO0000O0OOOO000O0 .xpath ('//meta[@*="og:url"]/@content')[0 ]#line:172
            OOOOO0O00O0OO000O =re .findall (r'biz=(.*?)&',str (OO0000OOOO0O00OO0 ))[0 ]#line:173
    except :#line:174
        return False #line:175
    OO0OOOO00O00OO00O =OO0000O0OOOO000O0 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:176
    if OO0OOOO00O00OO00O :#line:177
        OO0OOOO00O00OO00O =OO0OOOO00O00OO00O [0 ].strip ()#line:178
    OO00OO0OOO00OOO00 =re .findall (r"user_name.DATA'\) : '(.*?)'",OOOOOO0O00O00O0O0 .text )or OO0000O0OOOO000O0 .xpath ('//span[@class="profile_meta_value"]/text()')#line:180
    if OO00OO0OOO00OOO00 :#line:181
        OO00OO0OOO00OOO00 =OO00OO0OOO00OOO00 [0 ]#line:182
    O0OOO000O0O0OOOOO =re .findall (r'createTime = \'(.*)\'',OOOOOO0O00O00O0O0 .text )#line:183
    if O0OOO000O0O0OOOOO :#line:184
        O0OOO000O0O0OOOOO =O0OOO000O0O0OOOOO [0 ][5 :]#line:185
    OOO000O0O0O0O00O0 =f'{O0OOO000O0O0OOOOO}|{O00OOOOOOO000OOO0[:8]}|{OOOOO0O00O0OO000O}|{OO0OOOO00O00OO00O}'#line:186
    O0OOO0OO00O0000OO ={'biz':OOOOO0O00O0OO000O ,'text':OOO000O0O0O0O00O0 }#line:187
    return O0OOO0OO00O0000OO #line:188
class CZGM :#line:191
    def __init__ (OO0OO0OO0OOOO0OO0 ,OO0OO0000O000OO0O ):#line:192
        OO0OO0OO0OOOO0OO0 .name =OO0OO0000O000OO0O ['name']#line:193
        OO0OO0OO0OOOO0OO0 .uid =OO0OO0000O000OO0O .get ('uid')#line:194
        OO0OO0OO0OOOO0OO0 .sec =requests .session ()#line:195
        OO0OO0OO0OOOO0OO0 .sec .headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309071d) XWEB/8447 Flue","Cookie":OO0OO0000O000OO0O ['ck']}#line:199
        OO0OO0OO0OOOO0OO0 .c =0 #line:200
        OO0OO0OO0OOOO0OO0 .host =OO0OO0OO0OOOO0OO0 .get_host ()#line:201
        OO0OO0OO0OOOO0OO0 .msg =''#line:202
        OO0OO0OO0OOOO0OO0 .remain =0 #line:203
    @staticmethod #line:205
    def get_host ():#line:206
        OOO0O0O0OO0OOOOO0 ='http://2478987.jl.sgzzlb.sg6gdkelit8js.cloud/?p='#line:207
        OOOO0O00O00O0O0OO ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309071d) XWEB/8447 Flue'}#line:209
        O00000O0O0O0OOOOO =requests .get (OOO0O0O0OO0OOOOO0 ,headers =OOOO0O00O00O0O0OO ,allow_redirects =False )#line:210
        O0O00O0OOO0O0OOO0 =O00000O0O0O0OOOOO .headers .get ('Location')#line:211
        O0O0O0000O00O0000 =urlparse (O0O00O0OOO0O0OOO0 ).netloc #line:212
        return 'http://'+O0O0O0000O00O0000 #line:213
    @staticmethod #line:215
    def sha_256 (O000O00OOOO0OO0O0 ):#line:216
        OOOO0O00000O0O000 =f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={O000O00OOOO0OO0O0}'#line:217
        OO0O00OO00O00OO00 =hashlib .sha256 ()#line:218
        OO0O00OO00O00OO00 .update (OOOO0O00000O0O000 .encode ())#line:219
        O00000OO0O0OOOOO0 =OO0O00OO00O00OO00 .hexdigest ()#line:220
        return O00000OO0O0OOOOO0 #line:221
    def get_share_link (OOO00O00O0OO00000 ):#line:223
        O0O0000000O0O0OO0 =str (int (time .time ()))#line:224
        OOOOOO00O0O00OOOO =f'{OOO00O00O0OO00000.host}/share'#line:225
        O00000OOO0OOOOO00 ={"time":O0O0000000O0O0OO0 ,"sign":OOO00O00O0OO00000 .sha_256 (O0O0000000O0O0OO0 )}#line:229
        O00000O0OO00OO00O =OOO00O00O0OO00000 .sec .get (OOOOOO00O0O00OOOO ,data =O00000OOO0OOOOO00 ).json ()#line:230
        OO00OO0O0OOO00OO0 =O00000O0OO00OO00O ['data']['share_link'][0 ]#line:231
        return OO00OO0O0OOO00OO0 #line:232
    def read_info (OOO0OOO000OOOO0O0 ):#line:234
        try :#line:235
            O0OOOO0O00OOOO000 =f'{OOO0OOO000OOOO0O0.host}/read/info'#line:236
            OOO00OO00OOOOO000 =str (int (time .time ()))#line:237
            O00O0O0O00OO00000 ={"time":OOO00OO00OOOOO000 ,"sign":OOO0OOO000OOOO0O0 .sha_256 (OOO00OO00OOOOO000 )}#line:241
            O0O0O0OO0O000000O =OOO0OOO000OOOO0O0 .sec .get (O0OOOO0O00OOOO000 ,data =O00O0O0O00OO00000 )#line:242
            debugger (f'readfinfo {O0O0O0OO0O000000O.text}')#line:243
            try :#line:244
                O0O00OO0000O0O0OO =O0O0O0OO0O000000O .json ()#line:245
                OOO0OOO000OOOO0O0 .remain =O0O00OO0000O0O0OO .get ("data").get ("remain")#line:246
                O0OO00OOOOOOO000O =f'今日已经阅读了{O0O00OO0000O0O0OO.get("data").get("read")}篇文章，现有金币{OOO0OOO000OOOO0O0.remain}'#line:247
                debugger (f'【{OOO0OOO000OOOO0O0.name}】邀请链接：{OOO0OOO000OOOO0O0.get_share_link()}')#line:248
                printlog (f'【{OOO0OOO000OOOO0O0.name}】:{O0OO00OOOOOOO000O}')#line:249
                OOO0OOO000OOOO0O0 .msg +=O0OO00OOOOOOO000O +'\n'#line:250
                return True #line:251
            except :#line:252
                printlog (f'【{OOO0OOO000OOOO0O0.name}】:{O0O0O0OO0O000000O.text}')#line:253
                OOO0OOO000OOOO0O0 .msg +=(O0O0O0OO0O000000O .text +'\n')#line:254
                return False #line:255
        except :#line:256
            printlog (f'【{OOO0OOO000OOOO0O0.name}】:获取用户信息失败，账号异常，请检查你的ck')#line:257
            OOO0OOO000OOOO0O0 .msg +='获取用户信息失败，账号异常，请检查你的ck\n'#line:258
            try :#line:259
                send (f'【{OOO0OOO000OOOO0O0.name}】:获取用户信息失败，账号异常，请检查你的ck','钢镚阅读ck失效通知')#line:260
            except :#line:261
                push (f'【{OOO0OOO000OOOO0O0.name}】:获取用户信息失败，账号异常，请检查你的ck','钢镚阅读ck失效通知')#line:262
            return False #line:263
    def task_finish (OOO0O0OOO0O000000 ):#line:265
        OO0O0OOOO0OOOOO00 =f"{OOO0O0OOO0O000000.host}/read/finish"#line:266
        O0000O0O00O0O0OOO =str (int (time .time ()))#line:267
        OOOOO0OOO00O00O00 ={"time":O0000O0O00O0O0OOO ,"sign":OOO0O0OOO0O000000 .sha_256 (O0000O0O00O0O0OOO )}#line:271
        OOO00OOOOO00O0O00 =OOO0O0OOO0O000000 .sec .post (OO0O0OOOO0OOOOO00 ,data =OOOOO0OOO00O00O00 ).json ()#line:272
        debugger (f'finish {OOO00OOOOO00O0O00}')#line:273
        if OOO00OOOOO00O0O00 .get ('code')!=0 :#line:274
            printlog (f'【{OOO0O0OOO0O000000.name}】:{OOO00OOOOO00O0O00.get("message")}')#line:275
            OOO0O0OOO0O000000 .msg +=(OOO00OOOOO00O0O00 .get ('message')+'\n')#line:276
            return False #line:277
        elif OOO00OOOOO00O0O00 ['data']['check']is False :#line:278
            O0O00OO0OOOOOO000 =OOO00OOOOO00O0O00 ['data']['gain']#line:279
            OOO0OOO00O0OO000O =OOO00OOOOO00O0O00 ['data']['read']#line:280
            OOO0O0OOO0O000000 .msg +=f"阅读文章成功，获得钢镚[{O0O00OO0OOOOOO000}]，已读{OOO0OOO00O0OO000O}\n"#line:281
            printlog (f'【{OOO0O0OOO0O000000.name}】: 阅读文章成功，获得钢镚[{O0O00OO0OOOOOO000}]，已读{OOO0OOO00O0OO000O}')#line:282
            return True #line:283
    def read (O0000OO000OO0OO0O ):#line:285
        while True :#line:286
            O0000OO000OO0OO0O .msg +='-'*50 +'\n'#line:287
            OOO0OO0O00OO00O00 =str (int (time .time ()))#line:288
            OO0O0OOO000OO0O0O =f'{O0000OO000OO0OO0O.host}/read/task'#line:289
            OOO0OO00O0O00OO0O ={"time":OOO0OO0O00OO00O00 ,"sign":O0000OO000OO0OO0O .sha_256 (OOO0OO0O00OO00O00 )}#line:293
            OO00000O000O0OOO0 =O0000OO000OO0OO0O .sec .get (OO0O0OOO000OO0O0O ,data =OOO0OO00O0O00OO0O ).json ()#line:294
            debugger (f'read {OO00000O000O0OOO0}')#line:295
            if OO00000O000O0OOO0 .get ('code')!=0 :#line:296
                O0000OO000OO0OO0O .msg +=(OO00000O000O0OOO0 ['message']+'\n')#line:297
                printlog (f'【{O0000OO000OO0OO0O.name}】:{OO00000O000O0OOO0["message"]}')#line:298
                return False #line:299
            else :#line:300
                O0OOOOOOOO00O0O00 =OO00000O000O0OOO0 .get ('data').get ('link')#line:301
                O0000OO000OO0OO0O .msg +=f'获取到阅读链接成功\n'#line:302
                OOOO0O00O0O0O0OO0 =O0OOOOOOOO00O0O00 .encode ().decode ()#line:303
                OO0OO0OOO0OO0OOOO =getmpinfo (OOOO0O00O0O0O0OO0 )#line:304
                O0OO00O00OOOO00O0 =OO0OO0OOO0OO0OOOO ['biz']#line:305
                O0000OO000OO0OO0O .msg +=f'开始阅读 '+OO0OO0OOO0OO0OOOO ['text']+'\n'#line:306
                printlog (f'【{O0000OO000OO0OO0O.name}】:开始阅读 '+OO0OO0OOO0OO0OOOO ['text'])#line:307
                if O0OO00O00OOOO00O0 in checklist :#line:308
                    O0000OO000OO0OO0O .msg +="正在阅读检测文章，发送通知，暂停60秒\n"#line:309
                    printlog (f'【{O0000OO000OO0OO0O.name}】:正在阅读检测文章，发送通知，暂停60秒')#line:310
                    if sendable :#line:311
                        send (OO0OO0OOO0OO0OOOO ['text'],f'【{O0000OO000OO0OO0O.name}】钢镚阅读检测',OOOO0O00O0O0O0OO0 )#line:312
                    if pushable :#line:313
                        push (f'【{O0000OO000OO0OO0O.name}】\n点击阅读检测文章\n{OO0OO0OOO0OO0OOOO["text"]}',f'【{O0000OO000OO0OO0O.name}】 钢镚过检测',OOOO0O00O0O0O0OO0 ,O0000OO000OO0OO0O .uid )#line:315
                    time .sleep (60 )#line:316
                OOO0OO0O00OO00O00 =random .randint (7 ,10 )#line:317
                O0000OO000OO0OO0O .msg +=f'本次模拟阅读{OOO0OO0O00OO00O00}秒\n'#line:318
                time .sleep (OOO0OO0O00OO00O00 )#line:319
                O0000OO000OO0OO0O .task_finish ()#line:320
                O0000OO000OO0OO0O .c +=1 #line:321
    def withdraw (O000O0O00O0O00O0O ):#line:323
        if O000O0O00O0O00O0O .remain <txbz :#line:324
            O000O0O00O0O00O0O .msg +=f'没有达到提现标准\n'#line:325
            printlog (f'【{O000O0O00O0O00O0O.name}】:没有达到提现标准')#line:326
            return False #line:327
        OO000O00000000000 =f'{O000O0O00O0O00O0O.host}/withdraw/wechat'#line:328
        OO00O0000OOO00000 =str (int (time .time ()))#line:329
        O000OO0OOOO0000OO ={"time":OO00O0000OOO00000 ,"sign":O000O0O00O0O00O0O .sha_256 (OO00O0000OOO00000 )}#line:331
        O00O000O00000OO00 =O000O0O00O0O00O0O .sec .get (OO000O00000000000 ,data =O000OO0OOOO0000OO ).json ()#line:332
        O000O0O00O0O00O0O .msg +=f"提现结果：{O00O000O00000OO00.get('message')}\n"#line:333
        printlog (f'【{O000O0O00O0O00O0O.name}】:提现结果  {O00O000O00000OO00.get("message")}')#line:334
    def run (O000OO0OOO0O0O0O0 ):#line:336
        O000OO0OOO0O0O0O0 .msg +=('='*50 +f'\n【{O000OO0OOO0O0O0O0.name}】:开始任务\n')#line:337
        if O000OO0OOO0O0O0O0 .read_info ():#line:338
            O000OO0OOO0O0O0O0 .read ()#line:339
            if O000OO0OOO0O0O0O0 .c >1 :#line:340
                O000OO0OOO0O0O0O0 .read_info ()#line:341
            O000OO0OOO0O0O0O0 .withdraw ()#line:342
            if not printf :#line:343
                print (O000OO0OOO0O0O0O0 .msg )#line:344
def yd (O0OO0OO00OOOOOOOO ):#line:347
    while not O0OO0OO00OOOOOOOO .empty ():#line:348
        OO0OO0O00OOO0O000 =O0OO0OO00OOOOOOOO .get ()#line:349
        O0OOO0000O0OOO000 =CZGM (OO0OO0O00OOO0O000 )#line:350
        O0OOO0000O0OOO000 .run ()#line:351
def get_info ():#line:354
    print ("="*50 +f'\n✅github仓库：https://github.com/kxs2018/xiaoym\n✅极狐仓库:https://jihulab.com/xizhiai/xiaoym\n✅By:惜之酱\n'+'-'*50 )#line:356
    print (f"✅{_OO00OO000O00O0000.get('msg')['钢镚']}")#line:357
    O0OOO00O00O0OOO00 ='v1.6'#line:358
    OO0O0O000O00OOO00 =_OO00OO000O00O0000 ['version']['钢镚']#line:359
    print ('-'*50 +f'\n当前版本{O0OOO00O00O0OOO00}，仓库版本{OO0O0O000O00OOO00}\n✅{_OO00OO000O00O0000["update_log"]["钢镚"]}')#line:360
    if O0OOO00O00O0OOO00 <OO0O0O000O00OOO00 :#line:361
        print ('⛔️请到仓库下载最新版本k_czgm.py')#line:362
    print ("="*50 )#line:363
    return True #line:364
def main ():#line:367
    O0O0OOOO000O0000O =get_info ()#line:368
    OO000OO00O0O0000O =os .getenv ('czgmck')#line:369
    if not OO000OO00O0O0000O :#line:370
        exit ()#line:371
    OO000O0O00000OOOO =[]#line:372
    try :#line:373
        OO000OO00O0O0000O =ast .literal_eval (OO000OO00O0O0000O )#line:374
    except :#line:375
        pass #line:376
    OOOO00000000000O0 =Queue ()#line:377
    print ('*'*50 +f'\n✅共获取到{len(OO000OO00O0O0000O)}个账号，如与实际不符，请检查ck填写格式\n'+'*'*50 )#line:378
    for OO0OOOOO00OOOOO00 ,OO0O000OOOO00OO0O in enumerate (OO000OO00O0O0000O ,start =1 ):#line:379
        OOOO00000000000O0 .put (OO0O000OOOO00OO0O )#line:380
    if not O0O0OOOO000O0000O :#line:381
        exit ()#line:382
    for OO0OOOOO00OOOOO00 in range (max_workers ):#line:383
        OOO00O0O0OO0OO00O =threading .Thread (target =yd ,args =(OOOO00000000000O0 ,))#line:384
        OOO00O0O0OO0OO00O .start ()#line:385
        OO000O0O00000OOOO .append (OOO00O0O0OO0OO00O )#line:386
        time .sleep (delay_time )#line:387
    for OOO0OO00O00OOOO00 in OO000O0O00000OOOO :#line:388
        OOO0OO00O00OOOO00 .join ()#line:389
if __name__ =='__main__':#line:392
    main ()#line:393
