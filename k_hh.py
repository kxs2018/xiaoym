# -*- coding: utf-8 -*-
# k_hh
# Author: 惜之酱
"""
new Env('花花');
入口：http://mr181283238.yxjbhdl.cn/user/index.html?mid=EG5EVNLF3
"""
try:
    from config import hh_config
except:
    hh_config = {
        'printf': 1,  # 实时日志开关 1为开，0为关

        'debug': 1,  # debug模式开关 1为开，打印调试日志；0为关，不打印

        'max_workers': 5,  # 线程数量设置 设置为5，即最多有5个任务同时进行

        'txbz': 5000,  # 设置提现标准 不低于3000，平台标准为3000 设置为8000，即为8毛起提

        'sendable': 1,  # 企业微信推送开关 1开0关

        'pushable': 1,  # wxpusher推送开关 1开0关

        'delay_time': 30  # 并发延迟设置 设置为20即每隔20秒新增一个号做任务，直到数量达到max_workers
    }

printf = hh_config['printf']
debug = hh_config['debug']
sendable = hh_config['sendable']
pushable = hh_config['pushable']
max_workers = hh_config['max_workers']
txbz = hh_config['txbz']
delay_time = hh_config['delay_time']

import json #line:23
from random import randint #line:24
import os #line:25
import time #line:26
import requests #line:27
import ast #line:28
import re #line:29
import datetime #line:31
import threading #line:32
from queue import Queue #line:33
def get_msg ():#line:42
    O0O0O0OOOOOOOO000 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:44
    OOO000OO00OOO0000 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O0O0O0OOOOOOOO000 ).json ()#line:45
    return OOO000OO00OOO0000 #line:46
_OO00O00O0O0OOOOOO =get_msg ()#line:49
try :#line:50
    from lxml import etree #line:51
except :#line:52
    print (_OO00O00O0O0OOOOOO .get ('help')['lxml'])#line:53
if sendable :#line:54
    qwbotkey =os .getenv ('qwbotkey')#line:55
    if not qwbotkey :#line:56
        print (_OO00O00O0O0OOOOOO .get ('help')['qwbotkey'])#line:57
        exit ()#line:58
if pushable :#line:60
    pushconfig =os .getenv ('pushconfig')#line:61
    if not pushconfig :#line:62
        print (_OO00O00O0O0OOOOOO .get ('help')['pushconfig'])#line:63
        exit ()#line:64
    try :#line:65
        pushconfig =ast .literal_eval (pushconfig )#line:66
    except :#line:67
        pass #line:68
    if isinstance (pushconfig ,dict ):#line:69
        appToken =pushconfig ['appToken']#line:70
        uids =pushconfig ['uids']#line:71
        topicids =pushconfig ['topicids']#line:72
    else :#line:73
        try :#line:74
            "appToken=AT_pCenRjs;uids=['UID_9MZ','UID_T4xlqWx9x'];topicids=['xxx']"#line:75
            appToken =pushconfig .split (';')[0 ].split ('=')[1 ]#line:76
            uids =ast .literal_eval (pushconfig .split (';')[1 ].split ('=')[1 ])#line:77
            topicids =ast .literal_eval (pushconfig .split (';')[2 ].split ('=')[1 ])#line:78
        except :#line:79
            print (_OO00O00O0O0OOOOOO .get ('help')['pushconfig'])#line:80
            exit ()#line:81
if not pushable and not sendable :#line:82
    print ('啥通知方式都不配置，你想上天吗')#line:83
    exit ()#line:84
def ftime ():#line:87
    O00OOOO000000OO00 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:88
    return O00OOOO000000OO00 #line:89
def debugger (OO0OOOO0O00000OOO ):#line:92
    if debug :#line:93
        print (OO0OOOO0O00000OOO )#line:94
def printlog (O0OO0O00O00O00OO0 ):#line:97
    if printf :#line:98
        print (O0OO0O00O00O00OO0 )#line:99
def send (O0OO0OO0O0O0OOO0O ,title ='通知',url =None ):#line:102
    if not title or not url :#line:103
        O0OOOO0O0O0OOO00O ={"msgtype":"text","text":{"content":f"{title}\n\n{O0OO0OO0O0O0OOO0O}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:110
    else :#line:111
        O0OOOO0O0O0OOO00O ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O0OO0OO0O0O0OOO0O ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:124
    O000O0O000OOOOO00 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:125
    OO00O00OOOOOO0OOO =requests .post (O000O0O000OOOOO00 ,data =json .dumps (O0OOOO0O0O0OOO00O )).json ()#line:126
    if OO00O00OOOOOO0OOO .get ('errcode')!=0 :#line:127
        print ('消息发送失败，请检查key和发送格式')#line:128
        return False #line:129
    return OO00O00OOOOOO0OOO #line:130
def push (OOO0O00O0O00OOOOO ,title ='通知',url ='',uid =None ):#line:133
    if uid :#line:134
        uids .append (uid )#line:135
    OOOOO0OO000O0OOOO ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',OOO0O00O0O00OOOOO ).replace ('url',url )#line:137
    O00OOOOOO00OO0O00 ={"appToken":appToken ,"content":OOOOO0OO000O0OOOO ,"summary":title ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:147
    OO0OOO0OOO000OO00 ='http://wxpusher.zjiecode.com/api/send/message'#line:148
    O00O0OOO0O00OOO0O =requests .post (url =OO0OOO0OOO000OO00 ,json =O00OOOOOO00OO0O00 ).json ()#line:149
    if O00O0OOO0O00OOO0O .get ('code')!=1000 :#line:150
        print (O00O0OOO0O00OOO0O .get ('msg'),O00O0OOO0O00OOO0O )#line:151
    return O00O0OOO0O00OOO0O #line:152
def getmpinfo (OO00O0O0000000OOO ):#line:155
    if not OO00O0O0000000OOO or OO00O0O0000000OOO =='':#line:156
        return False #line:157
    OOOO000OOOOOO0000 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:159
    O00000O0OOOOOO000 =requests .get (OO00O0O0000000OOO ,headers =OOOO000OOOOOO0000 )#line:160
    O00O00OO0OOO00OO0 =etree .HTML (O00000O0OOOOOO000 .text )#line:161
    O00O0O0OO0OOO0OOO =O00O00OO0OOO00OO0 .xpath ('//meta[@*="og:title"]/@content')#line:163
    if O00O0O0OO0OOO0OOO :#line:164
        O00O0O0OO0OOO0OOO =O00O0O0OO0OOO0OOO [0 ]#line:165
    O0OOOOOOOO00O0O00 =O00O00OO0OOO00OO0 .xpath ('//meta[@*="og:url"]/@content')#line:166
    if O0OOOOOOOO00O0O00 :#line:167
        O0OOOOOOOO00O0O00 =O0OOOOOOOO00O0O00 [0 ].encode ().decode ()#line:168
    try :#line:169
        O000OO0000OOOO00O =re .findall (r'biz=(.*?)&',OO00O0O0000000OOO )[0 ]#line:170
    except :#line:171
        O000OO0000OOOO00O =re .findall (r'biz=(.*?)&',O0OOOOOOOO00O0O00 )[0 ]#line:172
    if not O000OO0000OOOO00O :#line:173
        return False #line:174
    OO0O0O00OO00OOO0O =O00O00OO0OOO00OO0 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:175
    if OO0O0O00OO00OOO0O :#line:176
        OO0O0O00OO00OOO0O =OO0O0O00OO00OOO0O [0 ].strip ()#line:177
    OOO0OO0O0OOOOOOO0 =re .findall (r"user_name.DATA'\) : '(.*?)'",O00000O0OOOOOO000 .text )or O00O00OO0OOO00OO0 .xpath ('//span[@class="profile_meta_value"]/text()')#line:179
    if OOO0OO0O0OOOOOOO0 :#line:180
        OOO0OO0O0OOOOOOO0 =OOO0OO0O0OOOOOOO0 [0 ]#line:181
    OOO0000O0OO000O00 =re .findall (r'createTime = \'(.*)\'',O00000O0OOOOOO000 .text )#line:182
    if OOO0000O0OO000O00 :#line:183
        OOO0000O0OO000O00 =OOO0000O0OO000O00 [0 ][5 :]#line:184
    OOOO0OOO0OO0OOO00 =f'{OOO0000O0OO000O00}|{O00O0O0OO0OOO0OOO[:10]}|{O000OO0000OOOO00O}|{OO0O0O00OO00OOO0O}'#line:185
    O00OO0O00O00000O0 ={'biz':O000OO0000OOOO00O ,'username':OO0O0O00OO00OOO0O ,'text':OOOO0OOO0OO0OOO00 }#line:186
    return O00OO0O00O00000O0 #line:187
try :#line:190
    with open ('checkdict.json','r',encoding ='utf-8')as f :#line:191
        cd_local =json .loads (f .read ())#line:192
except :#line:193
    pass #line:194
checkdict ={'Mzg2Mzk3Mjk5NQ==':'小鱼儿','MjM5NjU4NTE0MA==':'财事汇','MzkwMjI2ODY5Ng==':'A每日新菜','Mzg3NzEwMzI1Nw==':'A爱玩品牌传奇','MzIyMDg0MzA1OQ==':'服装加工宝','Mzg4NTQ5NDkxMQ==':'秣宝网','Mzk0NjIwNzk0Mg==':'检索宝','MzU3NjA5MDYyMw==':'重庆翊宝智慧电子装置有限公司','MzU1Nzc2ODI0MA==':'星空财研','MzUxMDgxMjMxMw==':'美术宝1对1','MzU4NDMyMTE1MQ==':'海雀Alcidae','MzI4MDE0MzM2NQ==':'强宝时尚','MzA3Nzc5MDMyNg==':'考研红宝书','MjM5Njk5NjYyMQ==':'宝和祥茶业','MzA4NDAyNTQ2MA==':'嘉财万贯','MzIzMjk2MjM5MQ==':'花生酥陪你学','MzkyMDE0NTI2OA==':'重庆市租房宝','MzI0NDI0NzU4OQ==':'九舞文学','MjM5NDAzMjgzNg==':'东风卡车之友','MzI1NjUxMTc0Mw==':'爱普生商教投影机','MzIyNzU3NDIwMA==':'川名堂','MzAwMDUwOTczNg==':'0','MzI4NjYyNTEzMw==':'0','MzI5MDQxNjExNg==':'0','Mzg3MzA0MTkyMw==':'0','MzU0MTUzMTUxOQ==':'0',}#line:206
try :#line:207
    checkdict ={**checkdict ,**cd_local }#line:208
except :#line:209
    pass #line:210
class Allinone :#line:213
    def __init__ (O0O0O0OO0O00OO0OO ,O0OOO0O0O00O0000O ):#line:214
        O0O0O0OO0O00OO0OO .name =O0OOO0O0O00O0000O ['name']#line:215
        O0O0O0OO0O00OO0OO .uid =O0OOO0O0O00O0000O .get ('uid')#line:216
        O0O0O0OO0O00OO0OO .username =None #line:217
        O0O0O0OO0O00OO0OO .biz =None #line:218
        O0O0O0OO0O00OO0OO .s =requests .session ()#line:219
        O0O0O0OO0O00OO0OO .payload ={"un":O0OOO0O0O00O0000O ['un'],"token":O0OOO0O0O00O0000O ['token'],"pageSize":20 }#line:220
        O0O0O0OO0O00OO0OO .s .headers ={'Accept':'application/json, text/javascript, */*; q=0.01','Content-Type':'application/json; charset=UTF-8','Host':'u.cocozx.cn','Connection':'keep-alive','User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",}#line:226
        O0O0O0OO0O00OO0OO .headers =O0O0O0OO0O00OO0OO .s .headers .copy ()#line:227
        O0O0O0OO0O00OO0OO .msg =''#line:228
    def get_readhost (OO0OO0O00OO00OOOO ):#line:230
        O00O000000O00000O ="http://u.cocozx.cn/api/user/getReadHost"#line:231
        OOO00000O0O00O000 =OO0OO0O00OO00OOOO .s .post (O00O000000O00000O ,json =OO0OO0O00OO00OOOO .payload ).json ()#line:232
        debugger (f'readhome {OOO00000O0O00O000}')#line:233
        OO0OO0O00OO00OOOO .readhost =OOO00000O0O00O000 .get ('result')['host']#line:234
        OO0OO0O00OO00OOOO .headers ['Origin']=OO0OO0O00OO00OOOO .readhost #line:235
        OO0OO0O00OO00OOOO .msg +=f'邀请链接：{OO0OO0O00OO00OOOO.readhost}/user/index.html?mid={OO0OO0O00OO00OOOO.huid}\n'#line:236
        printlog (f"{OO0OO0O00OO00OOOO.name}:邀请链接 {OO0OO0O00OO00OOOO.readhost}/user/index.html?mid={OO0OO0O00OO00OOOO.huid}")#line:237
    def stataccess (OO0OOO0000O00OOO0 ):#line:239
        OOOO000OOO00O0OO0 ='http://u.cocozx.cn/api/user/statAccess'#line:240
        OO0OOO0000O00OOO0 .s .post (OOOO000OOO00O0OO0 ,json =OO0OOO0000O00OOO0 .payload ).json ()#line:241
    def get_info (O0O0O0OO0O0OOO000 ):#line:243
        try :#line:244
            O00OOO00OO00OO0O0 =O0O0O0OO0O0OOO000 .s .post ("http://u.cocozx.cn/api/user/info",json =O0O0O0OO0O0OOO000 .payload ).json ()#line:245
            O0OOO000OOOO0OOO0 =O00OOO00OO00OO0O0 .get ("result")#line:246
            debugger (f'get_info {O00OOO00OO00OO0O0}')#line:247
            O00O0O0OO00OO0OOO =O0OOO000OOOO0OOO0 .get ('us')#line:248
            if O00O0O0OO00OO0OOO ==2 :#line:249
                O0O0O0OO0O0OOO000 .msg +=f'{O0O0O0OO0O0OOO000.name}已被封\n'#line:250
                printlog (f'{O0O0O0OO0O0OOO000.name}已被封')#line:251
                return False #line:252
            O0O0O0OO0O0OOO000 .msg +=f"""{O0O0O0OO0O0OOO000.name}:今日阅读次数:{O0OOO000OOOO0OOO0["dayCount"]}，当前花儿:{O0OOO000OOOO0OOO0["moneyCurrent"]}，累计阅读次数:{O0OOO000OOOO0OOO0["doneWx"]}\n"""#line:253
            printlog (f"""{O0O0O0OO0O0OOO000.name}:今日阅读次数:{O0OOO000OOOO0OOO0["dayCount"]}，当前花儿:{O0OOO000OOOO0OOO0["moneyCurrent"]}，累计阅读次数:{O0OOO000OOOO0OOO0["doneWx"]}""")#line:255
            OO0000OOO00O00O00 =int (O0OOO000OOOO0OOO0 ["moneyCurrent"])#line:256
            O0O0O0OO0O0OOO000 .huid =O0OOO000OOOO0OOO0 .get ('uid')#line:257
            return OO0000OOO00O00O00 #line:258
        except :#line:259
            return False #line:260
    def psmoneyc (O00OOO000O0OOOO0O ):#line:262
        OO000O0O0OOO0O0O0 ={**O00OOO000O0OOOO0O .payload ,**{'mid':O00OOO000O0OOOO0O .huid }}#line:263
        try :#line:264
            O0O00O00OO00O00O0 =O00OOO000O0OOOO0O .s .post ("http://u.cocozx.cn/api/user/psmoneyc",json =OO000O0O0OOO0O0O0 ).json ()#line:265
            O00OOO000O0OOOO0O .msg +=f"感谢下级送来的{O0O00O00OO00O00O0['result']['val']}花儿\n"#line:266
            printlog (f"{O00OOO000O0OOOO0O.name}:感谢下级送来的{O0O00O00OO00O00O0['result']['val']}花儿")#line:267
        except :#line:268
            pass #line:269
        return #line:270
    def get_status (OOOOOO000O0OO0O00 ):#line:272
        OOO00O0O0OOO0OO00 =requests .post ("http://u.cocozx.cn/api/user/read",headers =OOOOOO000O0OO0O00 .headers ,json =OOOOOO000O0OO0O00 .payload ).json ()#line:273
        debugger (f'getstatus {OOO00O0O0OOO0OO00}')#line:274
        OOOOOO000O0OO0O00 .status =OOO00O0O0OOO0OO00 .get ("result").get ("status")#line:275
        if OOOOOO000O0OO0O00 .status ==40 :#line:276
            OOOOOO000O0OO0O00 .msg +="文章还没有准备好\n"#line:277
            printlog (f"{OOOOOO000O0OO0O00.name}:文章还没有准备好")#line:278
            return #line:279
        elif OOOOOO000O0OO0O00 .status ==50 :#line:280
            OOOOOO000O0OO0O00 .msg +="阅读失效\n"#line:281
            printlog (f"{OOOOOO000O0OO0O00.name}:阅读失效")#line:282
            if OOOOOO000O0OO0O00 .biz is not None :#line:283
                if checkdict .update ({OOOOOO000O0OO0O00 .biz :OOOOOO000O0OO0O00 .username }):#line:284
                    print (f'checkdict添加检测号{OOOOOO000O0OO0O00.biz}: {OOOOOO000O0OO0O00.username}')#line:285
            return #line:286
        elif OOOOOO000O0OO0O00 .status ==60 :#line:287
            OOOOOO000O0OO0O00 .msg +="已经全部阅读完了\n"#line:288
            printlog (f"{OOOOOO000O0OO0O00.name}:已经全部阅读完了")#line:289
            return #line:290
        elif OOOOOO000O0OO0O00 .status ==70 :#line:291
            OOOOOO000O0OO0O00 .msg +="下一轮还未开启\n"#line:292
            printlog (f"{OOOOOO000O0OO0O00.name}:下一轮还未开启")#line:293
            return #line:294
        elif OOOOOO000O0OO0O00 .status ==10 :#line:295
            O0OOO0O0OO00OO00O =OOO00O0O0OOO0OO00 ["result"]["url"]#line:296
            OOOOOO000O0OO0O00 .msg +='-'*50 +"\n阅读链接获取成功\n"#line:297
            return O0OOO0O0OO00OO00O #line:298
    def submit (OOOOO0OOOO0000OO0 ):#line:300
        OOOOO0O0O00O0OO0O ={**{'type':1 },**OOOOO0OOOO0000OO0 .payload }#line:301
        OO0OO0O0O0O0OOOO0 =requests .post ("http://u.cocozx.cn/api/user/submit?zx=&xz=1",headers =OOOOO0OOOO0000OO0 .headers ,json =OOOOO0O0O00O0OO0O )#line:302
        OOO00O00O00O0OO0O =OO0OO0O0O0O0OOOO0 .json ().get ('result')#line:303
        debugger ('submit '+OO0OO0O0O0O0OOOO0 .text )#line:304
        OOOOO0OOOO0000OO0 .msg +=f'阅读成功,获得花儿{OOO00O00O00O0OO0O["val"]}，剩余次数:{OOO00O00O00O0OO0O["progress"]}\n'#line:305
        printlog (f"{OOOOO0OOOO0000OO0.name}:阅读成功,获得花儿{OOO00O00O00O0OO0O['val']}，剩余次数:{OOO00O00O00O0OO0O['progress']}")#line:306
    def read (OOOOOOOO0O0O00000 ):#line:308
        while True :#line:309
            O00OO0O000OO0OO0O =OOOOOOOO0O0O00000 .get_status ()#line:310
            if not O00OO0O000OO0OO0O :#line:311
                if OOOOOOOO0O0O00000 .status ==30 :#line:312
                    time .sleep (3 )#line:313
                    continue #line:314
                break #line:315
            OO0O0000OO0000OOO =getmpinfo (O00OO0O000OO0OO0O )#line:316
            if not OO0O0000OO0000OOO :#line:317
                printlog (f'{OOOOOOOO0O0O00000.name}:获取文章信息失败，程序中止')#line:318
                return False #line:319
            OOOOOOOO0O0O00000 .msg +='开始阅读 '+OO0O0000OO0000OOO ['text']+'\n'#line:320
            OOOOOOOO0O0O00000 .username =OO0O0000OO0000OOO ['username']#line:321
            OOOOOOOO0O0O00000 .biz =OO0O0000OO0000OOO ['biz']#line:322
            printlog (f'{OOOOOOOO0O0O00000.name}:开始阅读 '+OO0O0000OO0000OOO ['text'])#line:323
            O0OO0OOOO000O00OO =randint (7 ,10 )#line:324
            if OOOOOOOO0O0O00000 .biz in checkdict .keys ():#line:325
                OOOOOOOO0O0O00000 .msg +='当前正在阅读检测文章\n'#line:326
                printlog (f'{OOOOOOOO0O0O00000.name}:正在阅读检测文章')#line:327
                if sendable :#line:328
                    send (OO0O0000OO0000OOO ['text'],f'{OOOOOOOO0O0O00000.name}  花花阅读正在读检测文章',O00OO0O000OO0OO0O )#line:329
                if pushable :#line:330
                    push (f'【{OOOOOOOO0O0O00000.name}】\n点击阅读检测文章\n{OO0O0000OO0000OOO["text"]}',f'【{OOOOOOOO0O0O00000.name}】 花花过检测',O00OO0O000OO0OO0O ,OOOOOOOO0O0O00000 .uid )#line:332
                time .sleep (60 )#line:333
            time .sleep (O0OO0OOOO000O00OO )#line:334
            OOOOOOOO0O0O00000 .submit ()#line:335
    def tixian (O0OO00O0OOO00O0OO ):#line:337
        global txe #line:338
        OOOOOOOO0O00OO0OO =O0OO00O0OOO00O0OO .get_info ()#line:339
        if OOOOOOOO0O00OO0OO <txbz :#line:340
            O0OO00O0OOO00O0OO .msg +='你的花儿不多了\n'#line:341
            printlog (f'{O0OO00O0OOO00O0OO.name}:你的花儿不多了')#line:342
            return False #line:343
        if 10000 <=OOOOOOOO0O00OO0OO <49999 :#line:344
            txe =10000 #line:345
        elif 5000 <=OOOOOOOO0O00OO0OO <10000 :#line:346
            txe =5000 #line:347
        elif 3000 <=OOOOOOOO0O00OO0OO <5000 :#line:348
            txe =3000 #line:349
        elif OOOOOOOO0O00OO0OO >=50000 :#line:350
            txe =50000 #line:351
        O0OO00O0OOO00O0OO .msg +=f"提现金额:{txe}"#line:352
        printlog (f'{O0OO00O0OOO00O0OO.name}:提现金额 {txe}')#line:353
        OOO0OOO00O00O0OOO ={**O0OO00O0OOO00O0OO .payload ,**{"val":txe }}#line:354
        try :#line:355
            OO0O0O000O0OOOO0O =O0OO00O0OOO00O0OO .s .post ("http://u.cocozx.cn/api/user/wd",json =OOO0OOO00O00O0OOO ).json ()#line:356
            O0OO00O0OOO00O0OO .msg +=f"提现结果:{OO0O0O000O0OOOO0O.get('msg')}\n"#line:357
            printlog (f'{O0OO00O0OOO00O0OO.name}:提现结果 {OO0O0O000O0OOOO0O.get("msg")}')#line:358
        except :#line:359
            O0OO00O0OOO00O0OO .msg +=f"自动提现不成功，发送通知手动提现\n"#line:360
            printlog (f"{O0OO00O0OOO00O0OO.name}:自动提现不成功，发送通知手动提现")#line:361
            if sendable :#line:362
                send (f'可提现金额 {int(txe) / 10000}元，点击提现',f'惜之酱提醒您 {O0OO00O0OOO00O0OO.name} 花花阅读可以提现了',f'{O0OO00O0OOO00O0OO.readhost}/user/index.html?mid=FK73K93DA')#line:364
            if pushable :#line:365
                push (f'可提现金额 {int(txe) / 10000}元，点击提现',f'惜之酱提醒您 {O0OO00O0OOO00O0OO.name} 花花阅读可以提现了',f'{O0OO00O0OOO00O0OO.readhost}/user/index.html?mid=FK73K93DA',O0OO00O0OOO00O0OO .uid )#line:367
    def run (O00O00O0OO00O000O ):#line:369
        if O00O00O0OO00O000O .get_info ():#line:370
            O00O00O0OO00O000O .stataccess ()#line:371
            O00O00O0OO00O000O .get_readhost ()#line:372
            O00O00O0OO00O000O .psmoneyc ()#line:373
            O00O00O0OO00O000O .read ()#line:374
            O00O00O0OO00O000O .tixian ()#line:375
        if not printf :#line:376
            print (O00O00O0OO00O000O .msg .strip ())#line:377
def yd (O0O0OOOO000OO00OO ):#line:380
    while not O0O0OOOO000OO00OO .empty ():#line:381
        OOO00O000OO00OO00 =O0O0OOOO000OO00OO .get ()#line:382
        try :#line:383
            OO000000OOOOOO000 =Allinone (OOO00O000OO00OO00 )#line:384
            OO000000OOOOOO000 .run ()#line:385
        except Exception as O0OOOOO00O0OO00O0 :#line:386
            print (O0OOOOO00O0OO00O0 )#line:387
def get_info ():#line:390
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*20 )#line:392
    print ('入口：http://mr181283238.yxjbhdl.cn/user/index.html?mid=EG5EVNLF3')#line:393
    OO00OO00O0O0OOOOO ='V1.4'#line:394
    OOOOO0OOO00OO0OOO =_OO00O00O0O0OOOOOO ['version']['花花']#line:395
    print (f'当前版本{OO00OO00O0O0OOOOO}，仓库版本{OOOOO0OOO00OO0OOO}\n{_OO00O00O0O0OOOOOO["update_log"]["花花"]}')#line:396
    if OO00OO00O0O0OOOOO <OOOOO0OOO00OO0OOO :#line:397
        print ('请到仓库下载最新版本k_hh.py')#line:398
    return True #line:399
def main ():#line:402
    OOO00000O00O0O00O =get_info ()#line:403
    print (checkdict )#line:404
    O00O00OOO0OOO00O0 =os .getenv ('hhck')#line:405
    if not O00O00OOO0OOO00O0 :#line:406
        O00O00OOO0OOO00O0 =os .getenv ('aiock')#line:407
        if not O00O00OOO0OOO00O0 :#line:408
            print (_OO00O00O0O0OOOOOO .get ('msg')['花花'])#line:409
            exit ()#line:410
    try :#line:411
        O00O00OOO0OOO00O0 =ast .literal_eval (O00O00OOO0OOO00O0 )#line:412
    except :#line:413
        pass #line:414
    OO0O0O000000OO0O0 =Queue ()#line:415
    OO0O0OO0OO0O000O0 =[]#line:416
    print ('-'*20 )#line:417
    print (f'共获取到{len(O00O00OOO0OOO00O0)}个账号，如与实际不符，请检查ck填写方式')#line:418
    print ("="*25 )#line:419
    if not OOO00000O00O0O00O :#line:420
        exit ()#line:421
    for OO0O00OOO0O00000O ,OOOO0OOO00OOO0OO0 in enumerate (O00O00OOO0OOO00O0 ,start =1 ):#line:422
        OO0O0O000000OO0O0 .put (OOOO0OOO00OOO0OO0 )#line:423
    for OO0O00OOO0O00000O in range (max_workers ):#line:424
        OO0000O0OO0OO0OO0 =threading .Thread (target =yd ,args =(OO0O0O000000OO0O0 ,))#line:425
        OO0000O0OO0OO0OO0 .start ()#line:426
        OO0O0OO0OO0O000O0 .append (OO0000O0OO0OO0OO0 )#line:427
        time .sleep (delay_time )#line:428
    for OOO0000O00000OO0O in OO0O0OO0OO0O000O0 :#line:429
        OOO0000O00000OO0O .join ()#line:430
    print ('-'*25 +f'\n{checkdict}')#line:431
    with open ('checkdict.json','w',encoding ='utf-8')as O0O0OOO000O0O000O :#line:432
        O0O0OOO000O0O000O .write (json .dumps (checkdict ))#line:433
if __name__ =='__main__':#line:436
    main ()#line:437
