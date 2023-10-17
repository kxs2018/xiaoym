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
def get_msg ():#line:42
    O000OOOO0OOO0000O ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:44
    OOOOOOO000O0OO00O =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O000OOOO0OOO0000O ).json ()#line:45
    return OOOOOOO000O0OO00O #line:46
_O00OO0OOOO00O0O00 =get_msg ()#line:49
try :#line:51
    from lxml import etree #line:52
except :#line:53
    print (_O00OO0OOOO00O0O00 .get ('help')['lxml'])#line:54
if sendable :#line:55
    qwbotkey =os .getenv ('qwbotkey')#line:56
    if not qwbotkey :#line:57
        print (_O00OO0OOOO00O0O00 .get ('help')['qwbotkey'])#line:58
        exit ()#line:59
if pushable :#line:61
    pushconfig =os .getenv ('pushconfig')#line:62
    if not pushconfig :#line:63
        print (_O00OO0OOOO00O0O00 .get ('help')['pushconfig'])#line:64
        exit ()#line:65
    try :#line:66
        pushconfig =ast .literal_eval (pushconfig )#line:67
    except :#line:68
        pass #line:69
    if isinstance (pushconfig ,dict ):#line:70
        appToken =pushconfig ['appToken']#line:71
        uids =pushconfig ['uids']#line:72
        topicids =pushconfig ['topicids']#line:73
    else :#line:74
        try :#line:75
            "appToken=AT_pCenRjs;uids=['UID_9MZ','UID_T4xlqWx9x'];topicids=['xxx']"#line:76
            appToken =pushconfig .split (';')[0 ].split ('=')[1 ]#line:77
            uids =ast .literal_eval (pushconfig .split (';')[1 ].split ('=')[1 ])#line:78
            topicids =ast .literal_eval (pushconfig .split (';')[2 ].split ('=')[1 ])#line:79
        except :#line:80
            print (_O00OO0OOOO00O0O00 .get ('help')['pushconfig'])#line:81
            exit ()#line:82
if not pushable and not sendable :#line:83
    print ('啥通知方式都不配置，你想上天吗')#line:84
    exit ()#line:85
def ftime ():#line:88
    O0O0000OO0O000O00 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:89
    return O0O0000OO0O000O00 #line:90
def printlog (O000000O0O0O000OO ):#line:93
    if printf :#line:94
        print (O000000O0O0O000OO )#line:95
def debugger (O0OO0O0000000O0OO ):#line:98
    if debug :#line:99
        print (O0OO0O0000000O0OO )#line:100
def send (O000O0OOOO00O0O00 ,title ='通知',url =None ):#line:103
    if not title or not url :#line:104
        O000O0O0000OO00O0 ={"msgtype":"text","text":{"content":f"{title}\n\n{O000O0OOOO00O0O00}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:111
    else :#line:112
        O000O0O0000OO00O0 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O000O0OOOO00O0O00 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:125
    OO00000OO000O0000 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:126
    OO0000OOO0OOOOO00 =requests .post (OO00000OO000O0000 ,data =json .dumps (O000O0O0000OO00O0 )).json ()#line:127
    if OO0000OOO0OOOOO00 .get ('errcode')!=0 :#line:128
        print ('消息发送失败，请检查key和发送格式')#line:129
        return False #line:130
    return OO0000OOO0OOOOO00 #line:131
def push (OOOO00OOOO0OOOOO0 ,title ='通知',url ='',uid =None ):#line:134
    if uid :#line:135
        uids .append (uid )#line:136
    OOOO0000OOOO0OOOO ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',OOOO00OOOO0OOOOO0 ).replace ('url',url )#line:138
    OO00OO0O000OO000O ={"appToken":appToken ,"content":OOOO0000OOOO0OOOO ,"summary":title ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:148
    OO0O0OOO000OOO000 ='http://wxpusher.zjiecode.com/api/send/message'#line:149
    O0OOOOO00OO0OOOOO =requests .post (url =OO0O0OOO000OOO000 ,json =OO00OO0O000OO000O ).json ()#line:150
    if O0OOOOO00OO0OOOOO .get ('code')!=1000 :#line:151
        print (O0OOOOO00OO0OOOOO .get ('msg'),O0OOOOO00OO0OOOOO )#line:152
    return O0OOOOO00OO0OOOOO #line:153
def getmpinfo (OOOO0O0OOO0O00O00 ):#line:156
    if not OOOO0O0OOO0O00O00 or OOOO0O0OOO0O00O00 =='':#line:157
        return False #line:158
    OOO00O00000OO00OO ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:160
    O0000OOO0O0O0O0OO =requests .get (OOOO0O0OOO0O00O00 ,headers =OOO00O00000OO00OO )#line:161
    O0O0OOO0OO0OO0OOO =etree .HTML (O0000OOO0O0O0O0OO .text )#line:162
    OOOO000O00OOO0O0O =O0O0OOO0OO0OO0OOO .xpath ('//meta[@*="og:title"]/@content')#line:164
    if OOOO000O00OOO0O0O :#line:165
        OOOO000O00OOO0O0O =OOOO000O00OOO0O0O [0 ]#line:166
    OOOO00O00O00OO000 =O0O0OOO0OO0OO0OOO .xpath ('//meta[@*="og:url"]/@content')#line:167
    if OOOO00O00O00OO000 :#line:168
        OOOO00O00O00OO000 =OOOO00O00O00OO000 [0 ].encode ().decode ()#line:169
    try :#line:170
        O0000OO0O0O0OOO0O =re .findall (r'biz=(.*?)&',OOOO0O0OOO0O00O00 )[0 ]#line:171
    except :#line:172
        O0000OO0O0O0OOO0O =re .findall (r'biz=(.*?)&',OOOO00O00O00OO000 )[0 ]#line:173
    if not O0000OO0O0O0OOO0O :#line:174
        return False #line:175
    O0O0OOOO00OO0O00O =O0O0OOO0OO0OO0OOO .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:176
    if O0O0OOOO00OO0O00O :#line:177
        O0O0OOOO00OO0O00O =O0O0OOOO00OO0O00O [0 ].strip ()#line:178
    OO0OO0000OOOOO0O0 =re .findall (r"user_name.DATA'\) : '(.*?)'",O0000OOO0O0O0O0OO .text )or O0O0OOO0OO0OO0OOO .xpath ('//span[@class="profile_meta_value"]/text()')#line:180
    if OO0OO0000OOOOO0O0 :#line:181
        OO0OO0000OOOOO0O0 =OO0OO0000OOOOO0O0 [0 ]#line:182
    O00OO0OOO0O000000 =re .findall (r'createTime = \'(.*)\'',O0000OOO0O0O0O0OO .text )#line:183
    if O00OO0OOO0O000000 :#line:184
        O00OO0OOO0O000000 =O00OO0OOO0O000000 [0 ][5 :]#line:185
    OO00OO00O0O00O0O0 =f'{O00OO0OOO0O000000}|{OOOO000O00OOO0O0O[:10]}|{O0000OO0O0O0OOO0O}|{O0O0OOOO00OO0O00O}'#line:186
    OOOO0OO00O0O0OO00 ={'biz':O0000OO0O0O0OOO0O ,'username':O0O0OOOO00OO0O00O ,'text':OO00OO00O0O00O0O0 }#line:187
    return OOOO0OO00O0O0OO00 #line:188
try :#line:191
    with open ('checkdict.json','r',encoding ='utf-8')as f :#line:192
        checkdict_local =json .loads (f .read ())#line:193
except :#line:194
    pass #line:195
checkdict ={'Mzg2Mzk3Mjk5NQ==':'小鱼儿','MjM5NjU4NTE0MA==':'财事汇','MzkwMjI2ODY5Ng==':'A每日新菜','Mzg3NzEwMzI1Nw==':'A爱玩品牌传奇','MzIyMDg0MzA1OQ==':'服装加工宝','Mzg4NTQ5NDkxMQ==':'秣宝网','Mzk0NjIwNzk0Mg==':'检索宝','MzU3NjA5MDYyMw==':'重庆翊宝智慧电子装置有限公司','MzU1Nzc2ODI0MA==':'星空财研','MzUxMDgxMjMxMw==':'美术宝1对1','MzU4NDMyMTE1MQ==':'海雀Alcidae','MzI4MDE0MzM2NQ==':'强宝时尚','MzA3Nzc5MDMyNg==':'考研红宝书','MjM5Njk5NjYyMQ==':'宝和祥茶业','MzA4NDAyNTQ2MA==':'嘉财万贯','MzIzMjk2MjM5MQ==':'花生酥陪你学','MzkyMDE0NTI2OA==':'重庆市租房宝','MzI0NDI0NzU4OQ==':'九舞文学','MjM5NDAzMjgzNg==':'东风卡车之友','MzI1NjUxMTc0Mw==':'爱普生商教投影机','MzIyNzU3NDIwMA==':'川名堂','MzAwMDUwOTczNg==':'0','MzI4NjYyNTEzMw==':'0','MzI5MDQxNjExNg==':'0','Mzg3MzA0MTkyMw==':'0','MzU0MTUzMTUxOQ==':'0',"MzUxMDA4OTk5MA==":'',}#line:204
try :#line:205
    checkdict ={**checkdict ,**checkdict_local }#line:206
except :#line:207
    pass #line:208
class Allinone :#line:211
    def __init__ (OOO00O00O0000000O ,OOO0OO0O0OOOOO0OO ):#line:212
        OOO00O00O0000000O .name =OOO0OO0O0OOOOO0OO ['name']#line:213
        OOO00O00O0000000O .uid =OOO0OO0O0OOOOO0OO .get ('uid')#line:214
        OOO00O00O0000000O .username =None #line:215
        OOO00O00O0000000O .biz =None #line:216
        OOO00O00O0000000O .s =requests .session ()#line:217
        OOO00O00O0000000O .payload ={"un":OOO0OO0O0OOOOO0OO ['un'],"token":OOO0OO0O0OOOOO0OO ['token'],"pageSize":20 }#line:218
        OOO00O00O0000000O .s .headers ={'Accept':'application/json, text/javascript, */*; q=0.01','Content-Type':'application/json; charset=UTF-8','Host':'u.cocozx.cn','Connection':'keep-alive','User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",'Accept-Encoding':'gzip, deflate'}#line:224
        OOO00O00O0000000O .msg =''#line:225
    def get_info (OOO000OO0O0OO00O0 ):#line:227
        OOO0O0OOO0OO000OO ='CS5T87Q98'if OOO000OO0O0OO00O0 .name =='AI'else 'DG52AW2N6'#line:228
        OO00000OO00O0OO00 ={**OOO000OO0O0OO00O0 .payload ,**{'code':OOO0O0OOO0OO000OO }}#line:229
        try :#line:230
            O0OOO0OO0000O00OO =OOO000OO0O0OO00O0 .s .post ("http://u.cocozx.cn/api/coin/info",json =OO00000OO00O0OO00 ).json ()#line:231
            O0000OO0OO0O000OO =O0OOO0OO0000O00OO .get ("result")#line:232
            debugger (f'get_info {O0OOO0OO0000O00OO}')#line:233
            OO0OO000O0O000OO0 =O0000OO0OO0O000OO .get ('us')#line:234
            if OO0OO000O0O000OO0 ==2 :#line:235
                OOO000OO0O0OO00O0 .msg +=f'{OOO000OO0O0OO00O0.name}已被封\n'#line:236
                printlog (f'{OOO000OO0O0OO00O0.name}已被封')#line:237
                return False #line:238
            OOO000OO0O0OO00O0 .msg +=f"""{OOO000OO0O0OO00O0.name}:今日阅读次数:{O0000OO0OO0O000OO["dayCount"]}，当前元宝:{O0000OO0OO0O000OO["moneyCurrent"]}，累计阅读次数:{O0000OO0OO0O000OO["doneWx"]}\n"""#line:240
            printlog (f"""{OOO000OO0O0OO00O0.name}:今日阅读次数:{O0000OO0OO0O000OO["dayCount"]}，当前元宝:{O0000OO0OO0O000OO["moneyCurrent"]}，累计阅读次数:{O0000OO0OO0O000OO["doneWx"]}""")#line:242
            O0O0O0O00O0OO0000 =int (O0000OO0OO0O000OO ["moneyCurrent"])#line:243
            OOO000OO0O0OO00O0 .huid =O0000OO0OO0O000OO .get ('uid')#line:244
            return O0O0O0O00O0OO0000 #line:245
        except :#line:246
            return False #line:247
    def get_readhost (OOO0OOOO000OO0O00 ):#line:249
        O00O0O000O0O000O0 ="http://u.cocozx.cn/api/coin/getReadHost"#line:250
        O00O0O00OOOOO0O0O =OOO0OOOO000OO0O00 .s .post (O00O0O000O0O000O0 ,json =OOO0OOOO000OO0O00 .payload ).json ()#line:251
        debugger (f'readhome {O00O0O00OOOOO0O0O}')#line:252
        OOO0OOOO000OO0O00 .readhost =O00O0O00OOOOO0O0O .get ('result')['host']#line:253
        OOO0OOOO000OO0O00 .msg +=f'邀请链接：{OOO0OOOO000OO0O00.readhost}/oz/index.html?mid={OOO0OOOO000OO0O00.huid}\n'#line:254
        printlog (f"{OOO0OOOO000OO0O00.name}:邀请链接：{OOO0OOOO000OO0O00.readhost}/oz/index.html?mid={OOO0OOOO000OO0O00.huid}")#line:255
    def get_status (OOO00O0OO0O00O00O ):#line:257
        O0OOOO0O0O000OOOO =OOO00O0OO0O00O00O .s .post ("http://u.cocozx.cn/api/coin/read",json =OOO00O0OO0O00O00O .payload ).json ()#line:258
        debugger (f'getstatus {O0OOOO0O0O000OOOO}')#line:259
        OOO00O0OO0O00O00O .status =O0OOOO0O0O000OOOO .get ("result").get ("status")#line:260
        if OOO00O0OO0O00O00O .status ==40 :#line:261
            OOO00O0OO0O00O00O .msg +="文章还没有准备好\n"#line:262
            printlog (f"{OOO00O0OO0O00O00O.name}:文章还没有准备好")#line:263
            return #line:264
        elif OOO00O0OO0O00O00O .status ==50 :#line:265
            OOO00O0OO0O00O00O .msg +="阅读失效\n"#line:266
            printlog (f"{OOO00O0OO0O00O00O.name}:阅读失效")#line:267
            if OOO00O0OO0O00O00O .biz is not None :#line:268
                checkdict .update ({OOO00O0OO0O00O00O .biz :OOO00O0OO0O00O00O .username })#line:269
            return #line:270
        elif OOO00O0OO0O00O00O .status ==60 :#line:271
            OOO00O0OO0O00O00O .msg +="已经全部阅读完了\n"#line:272
            printlog (f"{OOO00O0OO0O00O00O.name}:已经全部阅读完了")#line:273
            return #line:274
        elif OOO00O0OO0O00O00O .status ==70 :#line:275
            OOO00O0OO0O00O00O .msg +="下一轮还未开启\n"#line:276
            printlog (f"{OOO00O0OO0O00O00O.name}:下一轮还未开启")#line:277
            return #line:278
        elif OOO00O0OO0O00O00O .status ==10 :#line:279
            OO00OO0O0O0O0OO00 =O0OOOO0O0O000OOOO ["result"]["url"]#line:280
            OOO00O0OO0O00O00O .msg +='-'*50 +"\n阅读链接获取成功\n"#line:281
            return OO00OO0O0O0O0OO00 #line:282
    def submit (O00O0O00O00O0OOO0 ):#line:284
        O0O0000000OO0O0O0 ={**{'type':1 },**O00O0O00O00O0OOO0 .payload }#line:285
        OO0O0O0O00000O0O0 =O00O0O00O00O0OOO0 .s .post ("http://u.cocozx.cn/api/coin/submit?zx=&xz=1",json =O0O0000000OO0O0O0 )#line:286
        OOOO0O00O0O00OOOO =OO0O0O0O00000O0O0 .json ().get ('result')#line:287
        debugger ('submit '+OO0O0O0O00000O0O0 .text )#line:288
        O00O0O00O00O0OOO0 .msg +=f"阅读成功,获得元宝{OOOO0O00O0O00OOOO['val']}，当前剩余次数:{OOOO0O00O0O00OOOO['progress']}\n"#line:289
        printlog (f"{O00O0O00O00O0OOO0.name}:阅读成功,获得元宝{OOOO0O00O0O00OOOO['val']}，当前剩余次数:{OOOO0O00O0O00OOOO['progress']}")#line:290
    def read (O0O0OOO0O0OOO0OOO ):#line:292
        while True :#line:293
            OO000OOOO000OOOO0 =O0O0OOO0O0OOO0OOO .get_status ()#line:294
            if not OO000OOOO000OOOO0 :#line:295
                if O0O0OOO0O0OOO0OOO .status ==30 :#line:296
                    time .sleep (3 )#line:297
                    continue #line:298
                break #line:299
            OO00OO00OO0OO00O0 =getmpinfo (OO000OOOO000OOOO0 )#line:300
            if not OO00OO00OO0OO00O0 :#line:301
                printlog (f'{O0O0OOO0O0OOO0OOO.name}:获取文章信息失败，程序中止')#line:302
                return False #line:303
            O0O0OOO0O0OOO0OOO .msg +='开始阅读 '+OO00OO00OO0OO00O0 ['text']+'\n'#line:304
            printlog (f'{O0O0OOO0O0OOO0OOO.name}:开始阅读 '+OO00OO00OO0OO00O0 ['text'])#line:305
            OO0O00OO000OO0OO0 =randint (7 ,10 )#line:306
            if OO00OO00OO0OO00O0 ['biz']in checkdict .keys ():#line:307
                O0O0OOO0O0OOO0OOO .msg +='正在阅读检测文章\n'#line:308
                printlog (f'{O0O0OOO0O0OOO0OOO.name}:正在阅读检测文章')#line:309
                if sendable :#line:310
                    send (OO00OO00OO0OO00O0 ['text'],f'{O0O0OOO0O0OOO0OOO.name}  元宝阅读正在读检测文章',OO000OOOO000OOOO0 )#line:311
                if pushable :#line:312
                    push (f'【{O0O0OOO0O0OOO0OOO.name}】\n点击阅读检测文章\n{OO00OO00OO0OO00O0["text"]}',f'【{O0O0OOO0O0OOO0OOO.name}】 元宝过检测',OO000OOOO000OOOO0 ,O0O0OOO0O0OOO0OOO .uid )#line:314
                time .sleep (60 )#line:315
            time .sleep (OO0O00OO000OO0OO0 )#line:316
            O0O0OOO0O0OOO0OOO .submit ()#line:317
    def tixian (O0000OO00O0000OO0 ):#line:319
        global txe #line:320
        OOOO00O0O0OOOO0OO =O0000OO00O0000OO0 .get_info ()#line:321
        if OOOO00O0O0OOOO0OO <txbz :#line:322
            O0000OO00O0000OO0 .msg +='你的元宝已不足\n'#line:323
            printlog (f'{O0000OO00O0000OO0.name}:你的元宝已不足')#line:324
            return False #line:325
        elif 10000 <=OOOO00O0O0OOOO0OO <49999 :#line:326
            txe =10000 #line:327
        elif 50000 <=OOOO00O0O0OOOO0OO <100000 :#line:328
            txe =50000 #line:329
        elif 3000 <=OOOO00O0O0OOOO0OO <10000 :#line:330
            txe =3000 #line:331
        elif OOOO00O0O0OOOO0OO >=100000 :#line:332
            txe =100000 #line:333
        O0000OO00O0000OO0 .msg +=f"提现金额:{txe}\n"#line:334
        printlog (f'{O0000OO00O0000OO0.name}:提现金额 {txe}')#line:335
        OOOOO00OOO00OOO0O ="http://u.cocozx.cn/api/coin/wdmoney"#line:336
        O0000OOO0O000OOO0 ={**O0000OO00O0000OO0 .payload ,**{"val":txe }}#line:337
        try :#line:338
            OOOOOO0O0OOOOO0OO =O0000OO00O0000OO0 .s .post (OOOOO00OOO00OOO0O ,json =O0000OOO0O000OOO0 ).json ()#line:339
            O0000OO00O0000OO0 .msg +=f'提现结果：{OOOOOO0O0OOOOO0OO.get("msg")}\n'#line:340
            printlog (f'{O0000OO00O0000OO0.name}:提现结果 {OOOOOO0O0OOOOO0OO.get("msg")}')#line:341
        except :#line:342
            O0000OO00O0000OO0 .msg +=f"自动提现不成功，发送通知手动提现\n"#line:343
            printlog (f"{O0000OO00O0000OO0.name}:自动提现不成功，发送通知手动提现")#line:344
            if sendable :#line:345
                send (f'可提现金额 {int(txe) / 10000}元，点击提现',f'惜之酱提醒您 {O0000OO00O0000OO0.name} 花花阅读可以提现了',f'{O0000OO00O0000OO0.readhost}/coin/index.html?mid=CS5T87Q98')#line:347
            if pushable :#line:348
                push (f'可提现金额 {int(txe) / 10000}元，点击提现',f'惜之酱提醒您 {O0000OO00O0000OO0.name} 花花阅读可以提现了',f'{O0000OO00O0000OO0.readhost}/coin/index.html?mid=CS5T87Q98',O0000OO00O0000OO0 .uid )#line:350
    def run (O00O0O000000O0OOO ):#line:352
        if O00O0O000000O0OOO .get_info ():#line:353
            O00O0O000000O0OOO .get_readhost ()#line:354
            O00O0O000000O0OOO .read ()#line:355
            O00O0O000000O0OOO .tixian ()#line:356
        if not printf :#line:357
            print (O00O0O000000O0OOO .msg .strip ())#line:358
def yd (O0O0OOO0O0O0O0O0O ):#line:361
    while not O0O0OOO0O0O0O0O0O .empty ():#line:362
        OOOOOOO0OO00000OO =O0O0OOO0O0O0O0O0O .get ()#line:363
        OOOOO0OO00OO000OO =Allinone (OOOOOOO0OO00000OO )#line:364
        OOOOO0OO00OO000OO .run ()#line:365
def get_info ():#line:368
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*20 )#line:370
    print ('入口：http://mr181335235.ahmgfulpshw.cloud/coin/index.html?mid=DG52AW2N6')#line:371
    O0OO0OO0O0000OOO0 ='v1.4'#line:372
    OO0O0O0OOO0O0OO00 =_O00OO0OOOO00O0O00 ['version']['元宝']#line:373
    print (f'当前版本{O0OO0OO0O0000OOO0}，仓库版本{OO0O0O0OOO0O0OO00}\n{_O00OO0OOOO00O0O00["update_log"]["花花"]}')#line:374
    if O0OO0OO0O0000OOO0 <OO0O0O0OOO0O0OO00 :#line:375
        print ('请到仓库下载最新版本k_ybb.py')#line:376
    return True #line:377
def main ():#line:380
    OOOO0O0O00OO0OO00 =get_info ()#line:381
    OOO00OOOOO0O0OO00 =os .getenv ('ybck')#line:382
    if not OOO00OOOOO0O0OO00 :#line:383
        OOO00OOOOO0O0OO00 =os .getenv ('aiock')#line:384
        if not OOO00OOOOO0O0OO00 :#line:385
            print (_O00OO0OOOO00O0O00 .get ('msg')['元宝'])#line:386
            exit ()#line:387
    try :#line:388
        OOO00OOOOO0O0OO00 =ast .literal_eval (OOO00OOOOO0O0OO00 )#line:389
    except :#line:390
        pass #line:391
    O00O000OOO00OOOOO =Queue ()#line:392
    OO00OO000O0O0OO0O =[]#line:393
    print ('-'*20 )#line:394
    print (f'共获取到{len(OOO00OOOOO0O0OO00)}个账号，如与实际不符，请检查ck填写方式')#line:395
    print ("="*25 )#line:396
    if not OOOO0O0O00OO0OO00 :#line:397
        exit ()#line:398
    for O0OO0OOOO000OOOOO ,OO0OO0O0OOO00O00O in enumerate (OOO00OOOOO0O0OO00 ,start =1 ):#line:399
        O00O000OOO00OOOOO .put (OO0OO0O0OOO00O00O )#line:400
    for O0OO0OOOO000OOOOO in range (max_workers ):#line:401
        O0OOOO000000000O0 =threading .Thread (target =yd ,args =(O00O000OOO00OOOOO ,))#line:402
        O0OOOO000000000O0 .start ()#line:403
        OO00OO000O0O0OO0O .append (O0OOOO000000000O0 )#line:404
        time .sleep (delay_time )#line:405
    for O0O000OOO0OO000OO in OO00OO000O0O0OO0O :#line:406
        O0O000OOO0OO000OO .join ()#line:407
    print ('-'*25 +f'\n{checkdict}')#line:408
    with open ('checkdict.json','w',encoding ='utf-8')as OOOO0OOOO0OOOOO00 :#line:409
        OOOO0OOOO0OOOOO00 .write (json .dumps (checkdict ))#line:410
if __name__ =='__main__':#line:413
    main ()#line:414
