# -*- coding: utf-8 -*-
# k_yb
# Author: 惜之酱
"""
new Env('元宝');
入口：http://mr181335235.ahmgfulpshw.cloud/coin/index.html?mid=DG52AW2N6
"""
try:
    from config import aio_config
except:
    aio_config = {
        'printf': 1,  # 实时日志开关 1为开，0为关

        'debug': 0,  # debug模式开关 1为开，打印调试日志；0为关，不打印

        'max_workers': 5,  # 线程数量设置 设置为5，即最多有5个任务同时进行

        'txbz': 10000,  # 设置提现标准 不低于3000，平台标准为3000 设置为8000，即为8毛起提

        'sendable': 1,  # 企业微信推送开关 1开0关

        'pushable': 1,  # wxpusher推送开关 1开0关

        'delay_time': 20  # 并发延迟设置 设置为20即每隔20秒新增一个号做任务，直到数量达到max_workers
    }

printf = aio_config['printf']
debug = aio_config['debug']
sendable = aio_config['sendable']
pushable = aio_config['pushable']
max_workers = aio_config['max_workers']
txbz = aio_config['txbz']
delay_time = aio_config['delay_time']

import json
from random import randint
import os
import time
import requests
import ast
import re
import datetime
import threading
from queue import Queue
def get_msg ():#line:44
    OO0O0OOOOO0O0O0O0 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:46
    OOOOO0OOOO0OO0O00 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OO0O0OOOOO0O0O0O0 ).json ()#line:47
    return OOOOO0OOOO0OO0O00 #line:48
_OOOO00000OOO0OO00 =get_msg ()#line:51
try :#line:53
    from lxml import etree #line:54
except :#line:55
    print (_OOOO00000OOO0OO00 .get ('help')['lxml'])#line:56
if sendable :#line:57
    qwbotkey =os .getenv ('qwbotkey')#line:58
    if not qwbotkey :#line:59
        print (_OOOO00000OOO0OO00 .get ('help')['qwbotkey'])#line:60
        exit ()#line:61
if pushable :#line:63
    pushconfig =os .getenv ('pushconfig')#line:64
    if not pushconfig :#line:65
        print (_OOOO00000OOO0OO00 .get ('help')['pushconfig'])#line:66
        exit ()#line:67
    try :#line:68
        pushconfig =ast .literal_eval (pushconfig )#line:69
    except :#line:70
        pass #line:71
    if isinstance (pushconfig ,dict ):#line:72
        appToken =pushconfig ['appToken']#line:73
        uids =pushconfig ['uids']#line:74
        topicids =pushconfig ['topicids']#line:75
    else :#line:76
        try :#line:77
            "appToken=AT_pCenRjs;uids=['UID_9MZ','UID_T4xlqWx9x'];topicids=['xxx']"#line:78
            appToken =pushconfig .split (';')[0 ].split ('=')[1 ]#line:79
            uids =ast .literal_eval (pushconfig .split (';')[1 ].split ('=')[1 ])#line:80
            topicids =ast .literal_eval (pushconfig .split (';')[2 ].split ('=')[1 ])#line:81
        except :#line:82
            print (_OOOO00000OOO0OO00 .get ('help')['pushconfig'])#line:83
            exit ()#line:84
if not pushable and not sendable :#line:85
    print ('啥通知方式都不配置，你想上天吗')#line:86
    exit ()#line:87
def ftime ():#line:90
    OO00OO0000OO0OOOO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:91
    return OO00OO0000OO0OOOO #line:92
def printlog (OOOOO0O00O0OOO0O0 ):#line:95
    if printf :#line:96
        print (OOOOO0O00O0OOO0O0 )#line:97
def debugger (OOOO0000O000000OO ):#line:100
    if debug :#line:101
        print (OOOO0000O000000OO )#line:102
def send (O00O0O000O0OO000O ,title ='通知',url =None ):#line:105
    if not title or not url :#line:106
        OO00OOOOOO0O00000 ={"msgtype":"text","text":{"content":f"{title}\n\n{O00O0O000O0OO000O}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:113
    else :#line:114
        OO00OOOOOO0O00000 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O00O0O000O0OO000O ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:127
    OOO00OOO00OO00OOO =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:128
    OO0O00OO0000O0O0O =requests .post (OOO00OOO00OO00OOO ,data =json .dumps (OO00OOOOOO0O00000 )).json ()#line:129
    if OO0O00OO0000O0O0O .get ('errcode')!=0 :#line:130
        print ('消息发送失败，请检查key和发送格式')#line:131
        return False #line:132
    return OO0O00OO0000O0O0O #line:133
def push (O0OO0000OO0O0OOOO ,title ='通知',url ='',uid =None ):#line:136
    if uid :#line:137
        uids .append (uid )#line:138
    O000O0OO0O0O0OO0O ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',O0OO0000OO0O0OOOO ).replace ('url',url )#line:140
    O0000OO0OO0O00O00 ={"appToken":appToken ,"content":O000O0OO0O0O0OO0O ,"summary":title ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:150
    O00000O0OOOO000OO ='http://wxpusher.zjiecode.com/api/send/message'#line:151
    OOOO0O00O0OO0OOOO =requests .post (url =O00000O0OOOO000OO ,json =O0000OO0OO0O00O00 ).json ()#line:152
    if OOOO0O00O0OO0OOOO .get ('code')!=1000 :#line:153
        print (OOOO0O00O0OO0OOOO .get ('msg'),OOOO0O00O0OO0OOOO )#line:154
    return OOOO0O00O0OO0OOOO #line:155
def getmpinfo (OO0000O000O0O000O ):#line:158
    if not OO0000O000O0O000O or OO0000O000O0O000O =='':#line:159
        return False #line:160
    O000O00O00OO0O0OO ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:162
    O0O0O0000O0OOO0O0 =requests .get (OO0000O000O0O000O ,headers =O000O00O00OO0O0OO )#line:163
    OO00O000OO00O0000 =etree .HTML (O0O0O0000O0OOO0O0 .text )#line:164
    O00OO0000O00O0OO0 =OO00O000OO00O0000 .xpath ('//meta[@*="og:title"]/@content')#line:166
    if O00OO0000O00O0OO0 :#line:167
        O00OO0000O00O0OO0 =O00OO0000O00O0OO0 [0 ]#line:168
    O00OO00O0O00OO0O0 =OO00O000OO00O0000 .xpath ('//meta[@*="og:url"]/@content')#line:169
    if O00OO00O0O00OO0O0 :#line:170
        O00OO00O0O00OO0O0 =O00OO00O0O00OO0O0 [0 ].encode ().decode ()#line:171
    try :#line:172
        O0OOOOO0O00O0OOO0 =re .findall (r'biz=(.*?)&',OO0000O000O0O000O )[0 ]#line:173
    except :#line:174
        O0OOOOO0O00O0OOO0 =re .findall (r'biz=(.*?)&',O00OO00O0O00OO0O0 )[0 ]#line:175
    if not O0OOOOO0O00O0OOO0 :#line:176
        return False #line:177
    OO00000OO0O0O00OO =OO00O000OO00O0000 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:178
    if OO00000OO0O0O00OO :#line:179
        OO00000OO0O0O00OO =OO00000OO0O0O00OO [0 ].strip ()#line:180
    OO00OOO0O0OO0O0OO =re .findall (r"user_name.DATA'\) : '(.*?)'",O0O0O0000O0OOO0O0 .text )or OO00O000OO00O0000 .xpath ('//span[@class="profile_meta_value"]/text()')#line:182
    if OO00OOO0O0OO0O0OO :#line:183
        OO00OOO0O0OO0O0OO =OO00OOO0O0OO0O0OO [0 ]#line:184
    O0OOOOO00O0OO0OOO =re .findall (r'createTime = \'(.*)\'',O0O0O0000O0OOO0O0 .text )#line:185
    if O0OOOOO00O0OO0OOO :#line:186
        O0OOOOO00O0OO0OOO =O0OOOOO00O0OO0OOO [0 ][5 :]#line:187
    OOOO0OO0OOOOO000O =f'{O0OOOOO00O0OO0OOO}|{O00OO0000O00O0OO0[:10]}|{O0OOOOO0O00O0OOO0}|{OO00000OO0O0O00OO}'#line:188
    OOO0O0O0000OOOOO0 ={'biz':O0OOOOO0O00O0OOO0 ,'username':OO00000OO0O0O00OO ,'text':OOOO0OO0OOOOO000O }#line:189
    return OOO0O0O0000OOOOO0 #line:190
try :#line:193
    with open ('checkdict.json','r',encoding ='utf-8')as f :#line:194
        checkdict_local =json .loads (f .read ())#line:195
except :#line:196
    pass #line:197
checkdict ={'Mzg2Mzk3Mjk5NQ==':'小鱼儿','MjM5NjU4NTE0MA==':'财事汇','MzkwMjI2ODY5Ng==':'A每日新菜','Mzg3NzEwMzI1Nw==':'A爱玩品牌传奇','MzIyMDg0MzA1OQ==':'服装加工宝','Mzg4NTQ5NDkxMQ==':'秣宝网','Mzk0NjIwNzk0Mg==':'检索宝','MzU3NjA5MDYyMw==':'重庆翊宝智慧电子装置有限公司','MzU1Nzc2ODI0MA==':'星空财研','MzUxMDgxMjMxMw==':'美术宝1对1','MzU4NDMyMTE1MQ==':'海雀Alcidae','MzI4MDE0MzM2NQ==':'强宝时尚','MzA3Nzc5MDMyNg==':'考研红宝书','MjM5Njk5NjYyMQ==':'宝和祥茶业','MzA4NDAyNTQ2MA==':'嘉财万贯','MzIzMjk2MjM5MQ==':'花生酥陪你学','MzkyMDE0NTI2OA==':'重庆市租房宝','MzI0NDI0NzU4OQ==':'九舞文学','MjM5NDAzMjgzNg==':'东风卡车之友','MzI1NjUxMTc0Mw==':'爱普生商教投影机','MzIyNzU3NDIwMA==':'川名堂','MzAwMDUwOTczNg==':'0','MzI4NjYyNTEzMw==':'0','MzI5MDQxNjExNg==':'0','Mzg3MzA0MTkyMw==':'0','MzU0MTUzMTUxOQ==':'0',"MzUxMDA4OTk5MA==":'','Mzg2Nzc0Mjg0NA==':'多啦A梦的小古筝'}#line:207
try :#line:208
    checkdict ={**checkdict ,**checkdict_local }#line:209
except :#line:210
    pass #line:211
class Allinone :#line:214
    def __init__ (OOO0O0OOO0O0OO0OO ,OOOO0OO0OOOO000OO ):#line:215
        OOO0O0OOO0O0OO0OO .name =OOOO0OO0OOOO000OO ['name']#line:216
        OOO0O0OOO0O0OO0OO .uid =OOOO0OO0OOOO000OO .get ('uid')#line:217
        OOO0O0OOO0O0OO0OO .username =None #line:218
        OOO0O0OOO0O0OO0OO .biz =None #line:219
        OOO0O0OOO0O0OO0OO .s =requests .session ()#line:220
        OOO0O0OOO0O0OO0OO .payload ={"un":OOOO0OO0OOOO000OO ['un'],"token":OOOO0OO0OOOO000OO ['token'],"pageSize":20 }#line:221
        OOO0O0OOO0O0OO0OO .s .headers ={'Accept':'application/json, text/javascript, */*; q=0.01','Content-Type':'application/json; charset=UTF-8','Host':'u.cocozx.cn','Connection':'keep-alive','User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",'Accept-Encoding':'gzip, deflate'}#line:227
        OOO0O0OOO0O0OO0OO .msg =''#line:228
    def get_info (OOOO00000OOO0OOOO ):#line:230
        OOOO0OO0000O0O0OO ='\u0043\u0053\u0035\u0054\u0038\u0037\u0051\u0039\u0038'if OOOO00000OOO0OOOO .name =='\u0041\u0049'else '\u0044\u0047\u0035\u0032\u0041\u0057\u0032\u004e\u0036'#line:231
        O0OO0OO0O0OO00000 ={**OOOO00000OOO0OOOO .payload ,**{'code':OOOO0OO0000O0O0OO }}#line:232
        try :#line:233
            O0000O0O0O0OOOO00 =OOOO00000OOO0OOOO .s .post ("http://u.cocozx.cn/api/coin/info",json =O0OO0OO0O0OO00000 ).json ()#line:234
            O0OOO0OO0OOO0OOO0 =O0000O0O0O0OOOO00 .get ("result")#line:235
            debugger (f'get_info {O0000O0O0O0OOOO00}')#line:236
            OO0OO000O000OOOOO =O0OOO0OO0OOO0OOO0 .get ('us')#line:237
            if OO0OO000O000OOOOO ==2 :#line:238
                OOOO00000OOO0OOOO .msg +=f'{OOOO00000OOO0OOOO.name}已被封\n'#line:239
                printlog (f'{OOOO00000OOO0OOOO.name}已被封')#line:240
                return False #line:241
            OOOO00000OOO0OOOO .msg +=f"""{OOOO00000OOO0OOOO.name}:今日阅读次数:{O0OOO0OO0OOO0OOO0["dayCount"]}，当前元宝:{O0OOO0OO0OOO0OOO0["moneyCurrent"]}\n"""#line:243
            printlog (f"""{OOOO00000OOO0OOOO.name}:今日阅读次数:{O0OOO0OO0OOO0OOO0["dayCount"]}，当前元宝:{O0OOO0OO0OOO0OOO0["moneyCurrent"]}""")#line:245
            OO0O000O0O0OOOO0O =int (O0OOO0OO0OOO0OOO0 ["moneyCurrent"])#line:246
            OOOO00000OOO0OOOO .huid =O0OOO0OO0OOO0OOO0 .get ('uid')#line:247
            return OO0O000O0O0OOOO0O #line:248
        except :#line:249
            return False #line:250
    def get_readhost (O0O0OOO00OOOO00O0 ):#line:252
        O00OO0O000OOOOOO0 ="http://u.cocozx.cn/api/coin/getReadHost"#line:253
        O00OO0OO0O0O0OOO0 =O0O0OOO00OOOO00O0 .s .post (O00OO0O000OOOOOO0 ,json =O0O0OOO00OOOO00O0 .payload ).json ()#line:254
        debugger (f'readhome {O00OO0OO0O0O0OOO0}')#line:255
        O0O0OOO00OOOO00O0 .readhost =O00OO0OO0O0O0OOO0 .get ('result')['host']#line:256
        O0O0OOO00OOOO00O0 .msg +=f'邀请链接：{O0O0OOO00OOOO00O0.readhost}/coin/index.html?mid={O0O0OOO00OOOO00O0.huid}\n'#line:257
        printlog (f"{O0O0OOO00OOOO00O0.name}:邀请链接：{O0O0OOO00OOOO00O0.readhost}/coin/index.html?mid={O0O0OOO00OOOO00O0.huid}")#line:258
    def get_status (OO000000OO0OO0O00 ):#line:260
        O00000OO000000OOO =OO000000OO0OO0O00 .s .post ("http://u.cocozx.cn/api/coin/read",json =OO000000OO0OO0O00 .payload ).json ()#line:261
        debugger (f'getstatus {O00000OO000000OOO}')#line:262
        OO000000OO0OO0O00 .status =O00000OO000000OOO .get ("result").get ("status")#line:263
        if OO000000OO0OO0O00 .status ==40 :#line:264
            OO000000OO0OO0O00 .msg +="文章还没有准备好\n"#line:265
            printlog (f"{OO000000OO0OO0O00.name}:文章还没有准备好")#line:266
            return #line:267
        elif OO000000OO0OO0O00 .status ==50 :#line:268
            OO000000OO0OO0O00 .msg +="阅读失效\n"#line:269
            printlog (f"{OO000000OO0OO0O00.name}:阅读失效")#line:270
            if OO000000OO0OO0O00 .biz is not None :#line:271
                checkdict .update ({OO000000OO0OO0O00 .biz :OO000000OO0OO0O00 .username })#line:272
            return #line:273
        elif OO000000OO0OO0O00 .status ==60 :#line:274
            OO000000OO0OO0O00 .msg +="已经全部阅读完了\n"#line:275
            printlog (f"{OO000000OO0OO0O00.name}:已经全部阅读完了")#line:276
            return #line:277
        elif OO000000OO0OO0O00 .status ==70 :#line:278
            OO000000OO0OO0O00 .msg +="下一轮还未开启\n"#line:279
            printlog (f"{OO000000OO0OO0O00.name}:下一轮还未开启")#line:280
            return #line:281
        elif OO000000OO0OO0O00 .status ==10 :#line:282
            OO00OO0OO0O0O0OOO =O00000OO000000OOO ["result"]["url"]#line:283
            OO000000OO0OO0O00 .msg +='-'*50 +"\n阅读链接获取成功\n"#line:284
            return OO00OO0OO0O0O0OOO #line:285
    def submit (O0O0000O0OO0O0O0O ):#line:287
        OOOO000OO0O0O000O ={**{'type':1 },**O0O0000O0OO0O0O0O .payload }#line:288
        OOOOO0O00O00000OO =O0O0000O0OO0O0O0O .s .post ("http://u.cocozx.cn/api/coin/submit?zx=&xz=1",json =OOOO000OO0O0O000O )#line:289
        OO000OO000O0O0O0O =OOOOO0O00O00000OO .json ().get ('result')#line:290
        debugger ('submit '+OOOOO0O00O00000OO .text )#line:291
        O0O0000O0OO0O0O0O .msg +=f"阅读成功,获得元宝{OO000OO000O0O0O0O['val']}，当前剩余次数:{OO000OO000O0O0O0O['progress']}\n"#line:292
        printlog (f"{O0O0000O0OO0O0O0O.name}:阅读成功,获得元宝{OO000OO000O0O0O0O['val']}，当前剩余次数:{OO000OO000O0O0O0O['progress']}")#line:293
    def read (O0O0O0OO00O000000 ):#line:295
        while True :#line:296
            O0OOOOO000O000000 =O0O0O0OO00O000000 .get_status ()#line:297
            if not O0OOOOO000O000000 :#line:298
                if O0O0O0OO00O000000 .status ==30 :#line:299
                    time .sleep (3 )#line:300
                    continue #line:301
                break #line:302
            O00O0OOO0OO000000 =getmpinfo (O0OOOOO000O000000 )#line:303
            if not O00O0OOO0OO000000 :#line:304
                printlog (f'{O0O0O0OO00O000000.name}:获取文章信息失败，程序中止')#line:305
                return False #line:306
            O0O0O0OO00O000000 .msg +='开始阅读 '+O00O0OOO0OO000000 ['text']+'\n'#line:307
            O0O0O0OO00O000000 .username =O00O0OOO0OO000000 ['username']#line:308
            O0O0O0OO00O000000 .biz =O00O0OOO0OO000000 ['biz']#line:309
            printlog (f'{O0O0O0OO00O000000.name}:开始阅读 '+O00O0OOO0OO000000 ['text'])#line:310
            OOO00O0OOOO0OOOOO =randint (7 ,10 )#line:311
            if O0O0O0OO00O000000 .biz in checkdict .keys ():#line:312
                O0O0O0OO00O000000 .msg +='正在阅读检测文章\n'#line:313
                printlog (f'{O0O0O0OO00O000000.name}:正在阅读检测文章')#line:314
                if sendable :#line:315
                    send (O00O0OOO0OO000000 ['text'],f'{O0O0O0OO00O000000.name}  元宝阅读正在读检测文章',O0OOOOO000O000000 )#line:316
                if pushable :#line:317
                    push (f'【{O0O0O0OO00O000000.name}】\n点击阅读检测文章\n{O00O0OOO0OO000000["text"]}',f'【{O0O0O0OO00O000000.name}】 元宝过检测',O0OOOOO000O000000 ,O0O0O0OO00O000000 .uid )#line:319
                time .sleep (60 )#line:320
            time .sleep (OOO00O0OOOO0OOOOO )#line:321
            O0O0O0OO00O000000 .submit ()#line:322
    def tixian (OO0OOOOO00OO0O0OO ):#line:324
        global txe #line:325
        OOO000OO00OOO000O =OO0OOOOO00OO0O0OO .get_info ()#line:326
        if OOO000OO00OOO000O <txbz :#line:327
            OO0OOOOO00OO0O0OO .msg +='你的元宝已不足\n'#line:328
            printlog (f'{OO0OOOOO00OO0O0OO.name}:你的元宝已不足')#line:329
            return False #line:330
        elif 10000 <=OOO000OO00OOO000O <49999 :#line:331
            txe =10000 #line:332
        elif 50000 <=OOO000OO00OOO000O <100000 :#line:333
            txe =50000 #line:334
        elif 3000 <=OOO000OO00OOO000O <10000 :#line:335
            txe =3000 #line:336
        elif OOO000OO00OOO000O >=100000 :#line:337
            txe =100000 #line:338
        OO0OOOOO00OO0O0OO .msg +=f"提现金额:{txe}\n"#line:339
        printlog (f'{OO0OOOOO00OO0O0OO.name}:提现金额 {txe}')#line:340
        OOO00O00OO000O000 ="http://u.cocozx.cn/api/coin/wdmoney"#line:341
        OO000O000O00OOO0O ={**OO0OOOOO00OO0O0OO .payload ,**{"val":txe }}#line:342
        try :#line:343
            OOO0000OOO00O00O0 =OO0OOOOO00OO0O0OO .s .post (OOO00O00OO000O000 ,json =OO000O000O00OOO0O ).json ()#line:344
            OO0OOOOO00OO0O0OO .msg +=f'提现结果：{OOO0000OOO00O00O0.get("msg")}\n'#line:345
            printlog (f'{OO0OOOOO00OO0O0OO.name}:提现结果 {OOO0000OOO00O00O0.get("msg")}')#line:346
        except :#line:347
            OO0OOOOO00OO0O0OO .msg +=f"自动提现不成功，发送通知手动提现\n"#line:348
            printlog (f"{OO0OOOOO00OO0O0OO.name}:自动提现不成功，发送通知手动提现")#line:349
            if sendable :#line:350
                send (f'可提现金额 {int(txe) / 10000}元，点击提现',f'惜之酱提醒您 {OO0OOOOO00OO0O0OO.name} 花花阅读可以提现了',f'{OO0OOOOO00OO0O0OO.readhost}/coin/index.html?mid=CS5T87Q98')#line:352
            if pushable :#line:353
                push (f'可提现金额 {int(txe) / 10000}元，点击提现',f'惜之酱提醒您 {OO0OOOOO00OO0O0OO.name} 花花阅读可以提现了',f'{OO0OOOOO00OO0O0OO.readhost}/coin/index.html?mid=CS5T87Q98',OO0OOOOO00OO0O0OO .uid )#line:355
    def run (O00OO0OO0OOO0OOO0 ):#line:357
        if O00OO0OO0OOO0OOO0 .get_info ():#line:358
            O00OO0OO0OOO0OOO0 .get_readhost ()#line:359
            O00OO0OO0OOO0OOO0 .read ()#line:360
            O00OO0OO0OOO0OOO0 .tixian ()#line:361
        if not printf :#line:362
            print (O00OO0OO0OOO0OOO0 .msg .strip ())#line:363
def yd (O00OOO000000O0O00 ):#line:366
    while not O00OOO000000O0O00 .empty ():#line:367
        O00000O00O0OOOO00 =O00OOO000000O0O00 .get ()#line:368
        O000OO0000OO0OOO0 =Allinone (O00000O00O0OOOO00 )#line:369
        O000OO0000OO0OOO0 .run ()#line:370
def get_info ():#line:373
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*20 )#line:375
    print ('入口：http://mr181335235.ahmgfulpshw.cloud/coin/index.html?mid=DG52AW2N6')#line:376
    O000O0OOOOO00OO00 ='v1.5'#line:377
    O00O000000000OO0O =_OOOO00000OOO0OO00 ['version']['元宝']#line:378
    print (f'当前版本{O000O0OOOOO00OO00}，仓库版本{O00O000000000OO0O}\n{_OOOO00000OOO0OO00["update_log"]["花花"]}')#line:379
    if O000O0OOOOO00OO00 <O00O000000000OO0O :#line:380
        print ('请到仓库下载最新版本k_ybb.py')#line:381
    return True #line:382
def main ():#line:385
    OOO00O0OO0OOO00O0 =get_info ()#line:386
    O0OOOO00O0O00O000 =os .getenv ('ybck')#line:387
    if not O0OOOO00O0O00O000 :#line:388
        O0OOOO00O0O00O000 =os .getenv ('aiock')#line:389
        if not O0OOOO00O0O00O000 :#line:390
            print (_OOOO00000OOO0OO00 .get ('msg')['元宝'])#line:391
            exit ()#line:392
    try :#line:393
        O0OOOO00O0O00O000 =ast .literal_eval (O0OOOO00O0O00O000 )#line:394
    except :#line:395
        pass #line:396
    O00OO00OOOOOOOO0O =Queue ()#line:397
    O0OO0O000OOO00O0O =[]#line:398
    print ('-'*20 )#line:399
    print (f'共获取到{len(O0OOOO00O0O00O000)}个账号，如与实际不符，请检查ck填写方式')#line:400
    print ("="*25 )#line:401
    if not OOO00O0OO0OOO00O0 :#line:402
        exit ()#line:403
    for OO000OOOOOOOOO000 ,O00OOO0OO0O000O00 in enumerate (O0OOOO00O0O00O000 ,start =1 ):#line:404
        O00OO00OOOOOOOO0O .put (O00OOO0OO0O000O00 )#line:405
    for OO000OOOOOOOOO000 in range (max_workers ):#line:406
        O00O0O00O0O0O00O0 =threading .Thread (target =yd ,args =(O00OO00OOOOOOOO0O ,))#line:407
        O00O0O00O0O0O00O0 .start ()#line:408
        O0OO0O000OOO00O0O .append (O00O0O00O0O0O00O0 )#line:409
        time .sleep (delay_time )#line:410
    for OO0OOOO00000OOO0O in O0OO0O000OOO00O0O :#line:411
        OO0OOOO00000OOO0O .join ()#line:412
    print ('-'*25 +f'\n{checkdict}')#line:413
    with open ('checkdict.json','w',encoding ='utf-8')as O0000000OOOO000OO :#line:414
        O0000000OOOO000OO .write (json .dumps (checkdict ))#line:415
if __name__ =='__main__':#line:418
    main ()#line:419
