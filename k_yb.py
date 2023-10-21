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
    OOO000O00OO00OOOO ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:46
    O0OOOO0000O0O00OO =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OOO000O00OO00OOOO ).json ()#line:47
    return O0OOOO0000O0O00OO #line:48
_O0OO0OOOO00OOO00O =get_msg ()#line:51
try :#line:53
    from lxml import etree #line:54
except :#line:55
    print (_O0OO0OOOO00OOO00O .get ('help')['lxml'])#line:56
if sendable :#line:57
    qwbotkey =os .getenv ('qwbotkey')#line:58
    if not qwbotkey :#line:59
        print (_O0OO0OOOO00OOO00O .get ('help')['qwbotkey'])#line:60
        exit ()#line:61
if pushable :#line:63
    pushconfig =os .getenv ('pushconfig')#line:64
    if not pushconfig :#line:65
        print (_O0OO0OOOO00OOO00O .get ('help')['pushconfig'])#line:66
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
            print (_O0OO0OOOO00OOO00O .get ('help')['pushconfig'])#line:83
            exit ()#line:84
if not pushable and not sendable :#line:85
    print ('啥通知方式都不配置，你想上天吗')#line:86
    exit ()#line:87
def ftime ():#line:90
    O0OO0000OO000OO0O =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:91
    return O0OO0000OO000OO0O #line:92
def printlog (OOO0OOO0O00000O00 ):#line:95
    if printf :#line:96
        print (OOO0OOO0O00000O00 )#line:97
def debugger (O0OO0O00OOO0O0OOO ):#line:100
    if debug :#line:101
        print (O0OO0O00OOO0O0OOO )#line:102
def send (O00000O0000O0OO0O ,title ='通知',url =None ):#line:105
    if not title or not url :#line:106
        OOO0O00OOO000OOO0 ={"msgtype":"text","text":{"content":f"{title}\n\n{O00000O0000O0OO0O}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg群：https://t.me/xiaoymgroup\n通知时间：{ftime()}",}}#line:113
    else :#line:114
        OOO0O00OOO000OOO0 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O00000O0000O0OO0O ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:127
    OOOOOOOOOOOOO000O =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:128
    O00OOOO0O00O0O00O =requests .post (OOOOOOOOOOOOO000O ,data =json .dumps (OOO0O00OOO000OOO0 )).json ()#line:129
    if O00OOOO0O00O0O00O .get ('errcode')!=0 :#line:130
        print ('消息发送失败，请检查key和发送格式')#line:131
        return False #line:132
    return O00OOOO0O00O0O00O #line:133
def push (O00OOOOO0O0O000OO ,title ='通知',url ='',uid =None ):#line:136
    if uid :#line:137
        uids .append (uid )#line:138
    O0OOO000O0O0OO0O0 ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入tg群](https://t.me/xiaoymgroup)</font>".replace ('msg',O00OOOOO0O0O000OO ).replace ('url',url )#line:140
    O0000O0O00OOOO000 ={"appToken":appToken ,"content":O0OOO000O0O0OO0O0 ,"summary":title ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:150
    OOO00OO000OO0O000 ='http://wxpusher.zjiecode.com/api/send/message'#line:151
    O0O0O0O0OOO00OO0O =requests .post (url =OOO00OO000OO0O000 ,json =O0000O0O00OOOO000 ).json ()#line:152
    if O0O0O0O0OOO00OO0O .get ('code')!=1000 :#line:153
        print (O0O0O0O0OOO00OO0O .get ('msg'),O0O0O0O0OOO00OO0O )#line:154
    return O0O0O0O0OOO00OO0O #line:155
def getmpinfo (O0OOOO000OOO0O0O0 ):#line:158
    if not O0OOOO000OOO0O0O0 or O0OOOO000OOO0O0O0 =='':#line:159
        return False #line:160
    O0O0OOO0000OO0O0O ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:162
    O000O0OOO0OOO0OOO =requests .get (O0OOOO000OOO0O0O0 ,headers =O0O0OOO0000OO0O0O )#line:163
    O0O0OOO0O00000000 =etree .HTML (O000O0OOO0OOO0OOO .text )#line:164
    OO0O000OO00O000OO =O0O0OOO0O00000000 .xpath ('//meta[@*="og:title"]/@content')#line:166
    if OO0O000OO00O000OO :#line:167
        OO0O000OO00O000OO =OO0O000OO00O000OO [0 ]#line:168
    O0O00O0O0O00O0O0O =O0O0OOO0O00000000 .xpath ('//meta[@*="og:url"]/@content')#line:169
    if O0O00O0O0O00O0O0O :#line:170
        O0O00O0O0O00O0O0O =O0O00O0O0O00O0O0O [0 ].encode ().decode ()#line:171
    try :#line:172
        OOO0O00OO0O00O0O0 =re .findall (r'biz=(.*?)&',O0OOOO000OOO0O0O0 )[0 ]#line:173
    except :#line:174
        OOO0O00OO0O00O0O0 =re .findall (r'biz=(.*?)&',O0O00O0O0O00O0O0O )[0 ]#line:175
    if not OOO0O00OO0O00O0O0 :#line:176
        return False #line:177
    O00OO0000OOO00000 =O0O0OOO0O00000000 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:178
    if O00OO0000OOO00000 :#line:179
        O00OO0000OOO00000 =O00OO0000OOO00000 [0 ].strip ()#line:180
    OOOOOO0O0O00O00OO =re .findall (r"user_name.DATA'\) : '(.*?)'",O000O0OOO0OOO0OOO .text )or O0O0OOO0O00000000 .xpath ('//span[@class="profile_meta_value"]/text()')#line:182
    if OOOOOO0O0O00O00OO :#line:183
        OOOOOO0O0O00O00OO =OOOOOO0O0O00O00OO [0 ]#line:184
    O0O0OO0O000OOO0OO =re .findall (r'createTime = \'(.*)\'',O000O0OOO0OOO0OOO .text )#line:185
    if O0O0OO0O000OOO0OO :#line:186
        O0O0OO0O000OOO0OO =O0O0OO0O000OOO0OO [0 ][5 :]#line:187
    OOO0OO0O0OOOO000O =f'{O0O0OO0O000OOO0OO}|{OO0O000OO00O000OO[:10]}|{OOO0O00OO0O00O0O0}|{O00OO0000OOO00000}'#line:188
    OOO00OOO0O00O00O0 ={'biz':OOO0O00OO0O00O0O0 ,'username':O00OO0000OOO00000 ,'text':OOO0OO0O0OOOO000O }#line:189
    return OOO00OOO0O00O00O0 #line:190
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
    def __init__ (OO000O0OOO0O000O0 ,O000O000O00O00000 ):#line:215
        OO000O0OOO0O000O0 .name =O000O000O00O00000 ['name']#line:216
        OO000O0OOO0O000O0 .uid =O000O000O00O00000 .get ('uid')#line:217
        OO000O0OOO0O000O0 .username =None #line:218
        OO000O0OOO0O000O0 .biz =None #line:219
        OO000O0OOO0O000O0 .s =requests .session ()#line:220
        OO000O0OOO0O000O0 .payload ={"un":O000O000O00O00000 ['un'],"token":O000O000O00O00000 ['token'],"pageSize":20 }#line:221
        OO000O0OOO0O000O0 .s .headers ={'Accept':'application/json, text/javascript, */*; q=0.01','Content-Type':'application/json; charset=UTF-8','Host':'u.cocozx.cn','Connection':'keep-alive','User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",'Accept-Encoding':'gzip, deflate'}#line:227
        OO000O0OOO0O000O0 .msg =''#line:228
    def get_info (OOO0OOOOO0O0OOO0O ):#line:230
        O0OOO000OO00OO0OO ='CS5T87Q98'if OOO0OOOOO0O0OOO0O .name =='AI'else 'DG52AW2N6'#line:231
        O000O0OOOO00OO0O0 ={**OOO0OOOOO0O0OOO0O .payload ,**{'code':O0OOO000OO00OO0OO }}#line:232
        try :#line:233
            OOOOO0OO000OO0O00 =OOO0OOOOO0O0OOO0O .s .post ("http://u.cocozx.cn/api/coin/info",json =O000O0OOOO00OO0O0 ).json ()#line:234
            OOO000O0O0OOO000O =OOOOO0OO000OO0O00 .get ("result")#line:235
            debugger (f'get_info {OOOOO0OO000OO0O00}')#line:236
            O00O00OO0O000OO0O =OOO000O0O0OOO000O .get ('us')#line:237
            if O00O00OO0O000OO0O ==2 :#line:238
                OOO0OOOOO0O0OOO0O .msg +=f'{OOO0OOOOO0O0OOO0O.name}已被封\n'#line:239
                printlog (f'{OOO0OOOOO0O0OOO0O.name}已被封')#line:240
                return False #line:241
            OOO0OOOOO0O0OOO0O .msg +=f"""{OOO0OOOOO0O0OOO0O.name}:今日阅读次数:{OOO000O0O0OOO000O["dayCount"]}，当前元宝:{OOO000O0O0OOO000O["moneyCurrent"]}，累计阅读次数:{OOO000O0O0OOO000O["doneWx"]}\n"""#line:243
            printlog (f"""{OOO0OOOOO0O0OOO0O.name}:今日阅读次数:{OOO000O0O0OOO000O["dayCount"]}，当前元宝:{OOO000O0O0OOO000O["moneyCurrent"]}，累计阅读次数:{OOO000O0O0OOO000O["doneWx"]}""")#line:245
            O000OO0000OOOO00O =int (OOO000O0O0OOO000O ["moneyCurrent"])#line:246
            OOO0OOOOO0O0OOO0O .huid =OOO000O0O0OOO000O .get ('uid')#line:247
            return O000OO0000OOOO00O #line:248
        except :#line:249
            return False #line:250
    def get_readhost (OOOOO0O00O00O00OO ):#line:252
        OOO000O00OOO0OO0O ="http://u.cocozx.cn/api/coin/getReadHost"#line:253
        OOO0O0OOOOO0OOO00 =OOOOO0O00O00O00OO .s .post (OOO000O00OOO0OO0O ,json =OOOOO0O00O00O00OO .payload ).json ()#line:254
        debugger (f'readhome {OOO0O0OOOOO0OOO00}')#line:255
        OOOOO0O00O00O00OO .readhost =OOO0O0OOOOO0OOO00 .get ('result')['host']#line:256
        OOOOO0O00O00O00OO .msg +=f'邀请链接：{OOOOO0O00O00O00OO.readhost}/oz/index.html?mid={OOOOO0O00O00O00OO.huid}\n'#line:257
        printlog (f"{OOOOO0O00O00O00OO.name}:邀请链接：{OOOOO0O00O00O00OO.readhost}/oz/index.html?mid={OOOOO0O00O00O00OO.huid}")#line:258
    def get_status (OOO000OOOO0O00000 ):#line:260
        O00OO00OOOOOO0OO0 =OOO000OOOO0O00000 .s .post ("http://u.cocozx.cn/api/coin/read",json =OOO000OOOO0O00000 .payload ).json ()#line:261
        debugger (f'getstatus {O00OO00OOOOOO0OO0}')#line:262
        OOO000OOOO0O00000 .status =O00OO00OOOOOO0OO0 .get ("result").get ("status")#line:263
        if OOO000OOOO0O00000 .status ==40 :#line:264
            OOO000OOOO0O00000 .msg +="文章还没有准备好\n"#line:265
            printlog (f"{OOO000OOOO0O00000.name}:文章还没有准备好")#line:266
            return #line:267
        elif OOO000OOOO0O00000 .status ==50 :#line:268
            OOO000OOOO0O00000 .msg +="阅读失效\n"#line:269
            printlog (f"{OOO000OOOO0O00000.name}:阅读失效")#line:270
            if OOO000OOOO0O00000 .biz is not None :#line:271
                checkdict .update ({OOO000OOOO0O00000 .biz :OOO000OOOO0O00000 .username })#line:272
            return #line:273
        elif OOO000OOOO0O00000 .status ==60 :#line:274
            OOO000OOOO0O00000 .msg +="已经全部阅读完了\n"#line:275
            printlog (f"{OOO000OOOO0O00000.name}:已经全部阅读完了")#line:276
            return #line:277
        elif OOO000OOOO0O00000 .status ==70 :#line:278
            OOO000OOOO0O00000 .msg +="下一轮还未开启\n"#line:279
            printlog (f"{OOO000OOOO0O00000.name}:下一轮还未开启")#line:280
            return #line:281
        elif OOO000OOOO0O00000 .status ==10 :#line:282
            O0OO0O00OOO0000OO =O00OO00OOOOOO0OO0 ["result"]["url"]#line:283
            OOO000OOOO0O00000 .msg +='-'*50 +"\n阅读链接获取成功\n"#line:284
            return O0OO0O00OOO0000OO #line:285
    def submit (O0000O0OOO00OO0OO ):#line:287
        OO0OO000OOOOO0OOO ={**{'type':1 },**O0000O0OOO00OO0OO .payload }#line:288
        O000OO0000000O0O0 =O0000O0OOO00OO0OO .s .post ("http://u.cocozx.cn/api/coin/submit?zx=&xz=1",json =OO0OO000OOOOO0OOO )#line:289
        O00000O00O0OO0000 =O000OO0000000O0O0 .json ().get ('result')#line:290
        debugger ('submit '+O000OO0000000O0O0 .text )#line:291
        O0000O0OOO00OO0OO .msg +=f"阅读成功,获得元宝{O00000O00O0OO0000['val']}，当前剩余次数:{O00000O00O0OO0000['progress']}\n"#line:292
        printlog (f"{O0000O0OOO00OO0OO.name}:阅读成功,获得元宝{O00000O00O0OO0000['val']}，当前剩余次数:{O00000O00O0OO0000['progress']}")#line:293
    def read (O0O0OOOOOO00OOO0O ):#line:295
        while True :#line:296
            O00000O00OOO0O00O =O0O0OOOOOO00OOO0O .get_status ()#line:297
            if not O00000O00OOO0O00O :#line:298
                if O0O0OOOOOO00OOO0O .status ==30 :#line:299
                    time .sleep (3 )#line:300
                    continue #line:301
                break #line:302
            OOOO0O00OOO00O000 =getmpinfo (O00000O00OOO0O00O )#line:303
            if not OOOO0O00OOO00O000 :#line:304
                printlog (f'{O0O0OOOOOO00OOO0O.name}:获取文章信息失败，程序中止')#line:305
                return False #line:306
            O0O0OOOOOO00OOO0O .msg +='开始阅读 '+OOOO0O00OOO00O000 ['text']+'\n'#line:307
            O0O0OOOOOO00OOO0O .username =OOOO0O00OOO00O000 ['username']#line:308
            O0O0OOOOOO00OOO0O .biz =OOOO0O00OOO00O000 ['biz']#line:309
            printlog (f'{O0O0OOOOOO00OOO0O.name}:开始阅读 '+OOOO0O00OOO00O000 ['text'])#line:310
            OOO0O0OO00O00000O =randint (7 ,10 )#line:311
            if O0O0OOOOOO00OOO0O .biz in checkdict .keys ():#line:312
                O0O0OOOOOO00OOO0O .msg +='正在阅读检测文章\n'#line:313
                printlog (f'{O0O0OOOOOO00OOO0O.name}:正在阅读检测文章')#line:314
                if sendable :#line:315
                    send (OOOO0O00OOO00O000 ['text'],f'{O0O0OOOOOO00OOO0O.name}  元宝阅读正在读检测文章',O00000O00OOO0O00O )#line:316
                if pushable :#line:317
                    push (f'【{O0O0OOOOOO00OOO0O.name}】\n点击阅读检测文章\n{OOOO0O00OOO00O000["text"]}',f'【{O0O0OOOOOO00OOO0O.name}】 元宝过检测',O00000O00OOO0O00O ,O0O0OOOOOO00OOO0O .uid )#line:319
                time .sleep (60 )#line:320
            time .sleep (OOO0O0OO00O00000O )#line:321
            O0O0OOOOOO00OOO0O .submit ()#line:322
    def tixian (OOOOO0O00000000OO ):#line:324
        global txe #line:325
        O0000O000OOOOO0O0 =OOOOO0O00000000OO .get_info ()#line:326
        if O0000O000OOOOO0O0 <txbz :#line:327
            OOOOO0O00000000OO .msg +='你的元宝已不足\n'#line:328
            printlog (f'{OOOOO0O00000000OO.name}:你的元宝已不足')#line:329
            return False #line:330
        elif 10000 <=O0000O000OOOOO0O0 <49999 :#line:331
            txe =10000 #line:332
        elif 50000 <=O0000O000OOOOO0O0 <100000 :#line:333
            txe =50000 #line:334
        elif 3000 <=O0000O000OOOOO0O0 <10000 :#line:335
            txe =3000 #line:336
        elif O0000O000OOOOO0O0 >=100000 :#line:337
            txe =100000 #line:338
        OOOOO0O00000000OO .msg +=f"提现金额:{txe}\n"#line:339
        printlog (f'{OOOOO0O00000000OO.name}:提现金额 {txe}')#line:340
        OO00O00OOO0OO0000 ="http://u.cocozx.cn/api/coin/wdmoney"#line:341
        O0O00OO000OO000OO ={**OOOOO0O00000000OO .payload ,**{"val":txe }}#line:342
        try :#line:343
            O0O0OO0O0000OO00O =OOOOO0O00000000OO .s .post (OO00O00OOO0OO0000 ,json =O0O00OO000OO000OO ).json ()#line:344
            OOOOO0O00000000OO .msg +=f'提现结果：{O0O0OO0O0000OO00O.get("msg")}\n'#line:345
            printlog (f'{OOOOO0O00000000OO.name}:提现结果 {O0O0OO0O0000OO00O.get("msg")}')#line:346
        except :#line:347
            OOOOO0O00000000OO .msg +=f"自动提现不成功，发送通知手动提现\n"#line:348
            printlog (f"{OOOOO0O00000000OO.name}:自动提现不成功，发送通知手动提现")#line:349
            if sendable :#line:350
                send (f'可提现金额 {int(txe) / 10000}元，点击提现',f'惜之酱提醒您 {OOOOO0O00000000OO.name} 花花阅读可以提现了',f'{OOOOO0O00000000OO.readhost}/coin/index.html?mid=CS5T87Q98')#line:352
            if pushable :#line:353
                push (f'可提现金额 {int(txe) / 10000}元，点击提现',f'惜之酱提醒您 {OOOOO0O00000000OO.name} 花花阅读可以提现了',f'{OOOOO0O00000000OO.readhost}/coin/index.html?mid=CS5T87Q98',OOOOO0O00000000OO .uid )#line:355
    def run (O0OOO0OOO0OO0O000 ):#line:357
        if O0OOO0OOO0OO0O000 .get_info ():#line:358
            O0OOO0OOO0OO0O000 .get_readhost ()#line:359
            O0OOO0OOO0OO0O000 .read ()#line:360
            O0OOO0OOO0OO0O000 .tixian ()#line:361
        if not printf :#line:362
            print (O0OOO0OOO0OO0O000 .msg .strip ())#line:363
def yd (O00OO0OO00O0OOO00 ):#line:366
    while not O00OO0OO00O0OOO00 .empty ():#line:367
        O0O0000000OOOO0OO =O00OO0OO00O0OOO00 .get ()#line:368
        O00OOO0O000OO0000 =Allinone (O0O0000000OOOO0OO )#line:369
        O00OOO0O000OO0000 .run ()#line:370
def get_info ():#line:373
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*20 )#line:375
    print ('入口：http://mr181335235.ahmgfulpshw.cloud/coin/index.html?mid=DG52AW2N6')#line:376
    OO0OOOOOO000000O0 ='v1.4'#line:377
    OO00O0O0O0O0O0O00 =_O0OO0OOOO00OOO00O ['version']['元宝']#line:378
    print (f'当前版本{OO0OOOOOO000000O0}，仓库版本{OO00O0O0O0O0O0O00}\n{_O0OO0OOOO00OOO00O["update_log"]["花花"]}')#line:379
    if OO0OOOOOO000000O0 <OO00O0O0O0O0O0O00 :#line:380
        print ('请到仓库下载最新版本k_ybb.py')#line:381
    return True #line:382
def main ():#line:385
    O00000O0OOOOO00O0 =get_info ()#line:386
    OOO0O00O00O0OO00O =os .getenv ('ybck')#line:387
    if not OOO0O00O00O0OO00O :#line:388
        OOO0O00O00O0OO00O =os .getenv ('aiock')#line:389
        if not OOO0O00O00O0OO00O :#line:390
            print (_O0OO0OOOO00OOO00O .get ('msg')['元宝'])#line:391
            exit ()#line:392
    try :#line:393
        OOO0O00O00O0OO00O =ast .literal_eval (OOO0O00O00O0OO00O )#line:394
    except :#line:395
        pass #line:396
    OO00OO0OO000OOOO0 =Queue ()#line:397
    O00000O0O0O0OOOOO =[]#line:398
    print ('-'*20 )#line:399
    print (f'共获取到{len(OOO0O00O00O0OO00O)}个账号，如与实际不符，请检查ck填写方式')#line:400
    print ("="*25 )#line:401
    if not O00000O0OOOOO00O0 :#line:402
        exit ()#line:403
    for OOOO00O0O0000OO00 ,OOO0O0O00OOOOO000 in enumerate (OOO0O00O00O0OO00O ,start =1 ):#line:404
        OO00OO0OO000OOOO0 .put (OOO0O0O00OOOOO000 )#line:405
    for OOOO00O0O0000OO00 in range (max_workers ):#line:406
        O0OO00O0OOO000O00 =threading .Thread (target =yd ,args =(OO00OO0OO000OOOO0 ,))#line:407
        O0OO00O0OOO000O00 .start ()#line:408
        O00000O0O0O0OOOOO .append (O0OO00O0OOO000O00 )#line:409
        time .sleep (delay_time )#line:410
    for O000O0OO0O000O00O in O00000O0O0O0OOOOO :#line:411
        O000O0OO0O000O00O .join ()#line:412
    print ('-'*25 +f'\n{checkdict}')#line:413
    with open ('checkdict.json','w',encoding ='utf-8')as OO000OO000O00OOOO :#line:414
        OO000OO000O00OOOO .write (json .dumps (checkdict ))#line:415
if __name__ =='__main__':#line:418
    main ()#line:419
