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
    OOO00000000OOO0OO ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:44
    OO00OOOO000O0O0OO =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OOO00000000OOO0OO ).json ()#line:45
    return OO00OOOO000O0O0OO #line:46
_OOOOO0000000O00OO =get_msg ()#line:49
try :#line:50
    from lxml import etree #line:51
except :#line:52
    print (_OOOOO0000000O00OO .get ('help')['lxml'])#line:53
if sendable :#line:54
    qwbotkey =os .getenv ('qwbotkey')#line:55
    if not qwbotkey :#line:56
        print (_OOOOO0000000O00OO .get ('help')['qwbotkey'])#line:57
        exit ()#line:58
if pushable :#line:60
    pushconfig =os .getenv ('pushconfig')#line:61
    if not pushconfig :#line:62
        print (_OOOOO0000000O00OO .get ('help')['pushconfig'])#line:63
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
            print (_OOOOO0000000O00OO .get ('help')['pushconfig'])#line:80
            exit ()#line:81
if not pushable and not sendable :#line:82
    print ('啥通知方式都不配置，你想上天吗')#line:83
    exit ()#line:84
def ftime ():#line:87
    OO00000O00OO00OOO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:88
    return OO00000O00OO00OOO #line:89
def debugger (OOOOO000O00000O00 ):#line:92
    if debug :#line:93
        print (OOOOO000O00000O00 )#line:94
def printlog (O0OO0000000000OOO ):#line:97
    if printf :#line:98
        print (O0OO0000000000OOO )#line:99
def send (O0O0O0O000OOO00O0 ,title ='通知',url =None ):#line:102
    if not title or not url :#line:103
        OOOO000000O00O00O ={"msgtype":"text","text":{"content":f"{title}\n\n{O0O0O0O000OOO00O0}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:110
    else :#line:111
        OOOO000000O00O00O ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O0O0O0O000OOO00O0 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:124
    O0OO000000OO0OOO0 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:125
    O000OO0O00O0O0O00 =requests .post (O0OO000000OO0OOO0 ,data =json .dumps (OOOO000000O00O00O )).json ()#line:126
    if O000OO0O00O0O0O00 .get ('errcode')!=0 :#line:127
        print ('消息发送失败，请检查key和发送格式')#line:128
        return False #line:129
    return O000OO0O00O0O0O00 #line:130
def push (OOO000OOO0OO0OO0O ,title ='通知',url ='',uid =None ):#line:133
    if uid :#line:134
        uids .append (uid )#line:135
    O0O00O000O0OOOOOO ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',OOO000OOO0OO0OO0O ).replace ('url',url )#line:137
    O0O0OO0OO0OOOOO00 ={"appToken":appToken ,"content":O0O00O000O0OOOOOO ,"summary":title ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:147
    O000O000OOOOO0OO0 ='http://wxpusher.zjiecode.com/api/send/message'#line:148
    OOOO0O0OOOO0000OO =requests .post (url =O000O000OOOOO0OO0 ,json =O0O0OO0OO0OOOOO00 ).json ()#line:149
    if OOOO0O0OOOO0000OO .get ('code')!=1000 :#line:150
        print (OOOO0O0OOOO0000OO .get ('msg'),OOOO0O0OOOO0000OO )#line:151
    return OOOO0O0OOOO0000OO #line:152
def getmpinfo (OOOOO0O0O0O0OO0OO ):#line:155
    if not OOOOO0O0O0O0OO0OO or OOOOO0O0O0O0OO0OO =='':#line:156
        return False #line:157
    OOO00O0OOO0O0OO00 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:159
    O00OO0O0OO0O0O000 =requests .get (OOOOO0O0O0O0OO0OO ,headers =OOO00O0OOO0O0OO00 )#line:160
    OO000000O0O000O00 =etree .HTML (O00OO0O0OO0O0O000 .text )#line:161
    OO0OO0000OO0O0000 =OO000000O0O000O00 .xpath ('//meta[@*="og:title"]/@content')#line:163
    if OO0OO0000OO0O0000 :#line:164
        OO0OO0000OO0O0000 =OO0OO0000OO0O0000 [0 ]#line:165
    OO0000000OO0O00OO =OO000000O0O000O00 .xpath ('//meta[@*="og:url"]/@content')#line:166
    if OO0000000OO0O00OO :#line:167
        OO0000000OO0O00OO =OO0000000OO0O00OO [0 ].encode ().decode ()#line:168
    try :#line:169
        O00OOO00O0OO00OO0 =re .findall (r'biz=(.*?)&',OOOOO0O0O0O0OO0OO )[0 ]#line:170
    except :#line:171
        O00OOO00O0OO00OO0 =re .findall (r'biz=(.*?)&',OO0000000OO0O00OO )[0 ]#line:172
    if not O00OOO00O0OO00OO0 :#line:173
        return False #line:174
    O000O000OO0O0000O =OO000000O0O000O00 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:175
    if O000O000OO0O0000O :#line:176
        O000O000OO0O0000O =O000O000OO0O0000O [0 ].strip ()#line:177
    O00OOOOOO000OO000 =re .findall (r"user_name.DATA'\) : '(.*?)'",O00OO0O0OO0O0O000 .text )or OO000000O0O000O00 .xpath ('//span[@class="profile_meta_value"]/text()')#line:179
    if O00OOOOOO000OO000 :#line:180
        O00OOOOOO000OO000 =O00OOOOOO000OO000 [0 ]#line:181
    O000OO0000000O000 =re .findall (r'createTime = \'(.*)\'',O00OO0O0OO0O0O000 .text )#line:182
    if O000OO0000000O000 :#line:183
        O000OO0000000O000 =O000OO0000000O000 [0 ][5 :]#line:184
    O0000O00OO0O0000O =f'{O000OO0000000O000}|{OO0OO0000OO0O0000[:10]}|{O00OOO00O0OO00OO0}|{O000O000OO0O0000O}'#line:185
    OOOOOOOOOO0O00OO0 ={'biz':O00OOO00O0OO00OO0 ,'username':O000O000OO0O0000O ,'text':O0000O00OO0O0000O }#line:186
    return OOOOOOOOOO0O00OO0 #line:187
try :#line:190
    with open ('checkdict.json','r',encoding ='utf-8')as f :#line:191
        cd_local =json .loads (f .read ())#line:192
except :#line:193
    pass #line:194
checkdict ={'Mzg2Mzk3Mjk5NQ==':'小鱼儿','MjM5NjU4NTE0MA==':'财事汇','MzkwMjI2ODY5Ng==':'A每日新菜','Mzg3NzEwMzI1Nw==':'A爱玩品牌传奇','MzIyMDg0MzA1OQ==':'服装加工宝','Mzg4NTQ5NDkxMQ==':'秣宝网','Mzk0NjIwNzk0Mg==':'检索宝','MzU3NjA5MDYyMw==':'重庆翊宝智慧电子装置有限公司','MzU1Nzc2ODI0MA==':'星空财研','MzUxMDgxMjMxMw==':'美术宝1对1','MzU4NDMyMTE1MQ==':'海雀Alcidae','MzI4MDE0MzM2NQ==':'强宝时尚','MzA3Nzc5MDMyNg==':'考研红宝书','MjM5Njk5NjYyMQ==':'宝和祥茶业','MzA4NDAyNTQ2MA==':'嘉财万贯','MzIzMjk2MjM5MQ==':'花生酥陪你学','MzkyMDE0NTI2OA==':'重庆市租房宝','MzI0NDI0NzU4OQ==':'九舞文学','MjM5NDAzMjgzNg==':'东风卡车之友','MzI1NjUxMTc0Mw==':'爱普生商教投影机','MzIyNzU3NDIwMA==':'川名堂'}#line:202
if cd_local :#line:203
    checkdict ={**checkdict ,**cd_local }#line:204
class Allinone :#line:207
    def __init__ (OOO000OO0O000O0OO ,OOO000000O00O00OO ):#line:208
        OOO000OO0O000O0OO .name =OOO000000O00O00OO ['name']#line:209
        OOO000OO0O000O0OO .uid =OOO000000O00O00OO .get ('uid')#line:210
        OOO000OO0O000O0OO .username =None #line:211
        OOO000OO0O000O0OO .biz =None #line:212
        OOO000OO0O000O0OO .s =requests .session ()#line:213
        OOO000OO0O000O0OO .payload ={"un":OOO000000O00O00OO ['un'],"token":OOO000000O00O00OO ['token'],"pageSize":20 }#line:214
        OOO000OO0O000O0OO .s .headers ={'Accept':'application/json, text/javascript, */*; q=0.01','Content-Type':'application/json; charset=UTF-8','Host':'u.cocozx.cn','Connection':'keep-alive','User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",}#line:220
        OOO000OO0O000O0OO .headers =OOO000OO0O000O0OO .s .headers .copy ()#line:221
        OOO000OO0O000O0OO .msg =''#line:222
    def get_readhost (O00OO000O0O000OO0 ):#line:224
        OO0OOO00000O00O0O ="http://u.cocozx.cn/api/user/getReadHost"#line:225
        O00O000OO00OOOO00 =O00OO000O0O000OO0 .s .post (OO0OOO00000O00O0O ,json =O00OO000O0O000OO0 .payload ).json ()#line:226
        debugger (f'readhome {O00O000OO00OOOO00}')#line:227
        O00OO000O0O000OO0 .readhost =O00O000OO00OOOO00 .get ('result')['host']#line:228
        O00OO000O0O000OO0 .headers ['Origin']=O00OO000O0O000OO0 .readhost #line:229
        O00OO000O0O000OO0 .msg +=f'邀请链接：{O00OO000O0O000OO0.readhost}/user/index.html?mid={O00OO000O0O000OO0.huid}\n'#line:230
        printlog (f"{O00OO000O0O000OO0.name}:邀请链接 {O00OO000O0O000OO0.readhost}/user/index.html?mid={O00OO000O0O000OO0.huid}")#line:231
    def stataccess (OOOOOOOOOO0O0O00O ):#line:233
        O00OOOOO000OOO0OO ='http://u.cocozx.cn/api/user/statAccess'#line:234
        OOOOOOOOOO0O0O00O .s .post (O00OOOOO000OOO0OO ,json =OOOOOOOOOO0O0O00O .payload ).json ()#line:235
    def get_info (O00OOOOO0OO0OOO00 ):#line:237
        try :#line:238
            O0OO00OO000OOO00O =O00OOOOO0OO0OOO00 .s .post ("http://u.cocozx.cn/api/user/info",json =O00OOOOO0OO0OOO00 .payload ).json ()#line:239
            O00O0O00O00OOO0OO =O0OO00OO000OOO00O .get ("result")#line:240
            debugger (f'get_info {O0OO00OO000OOO00O}')#line:241
            OO000000O000O0OOO =O00O0O00O00OOO0OO .get ('us')#line:242
            if OO000000O000O0OOO ==2 :#line:243
                O00OOOOO0OO0OOO00 .msg +=f'{O00OOOOO0OO0OOO00.name}已被封\n'#line:244
                printlog (f'{O00OOOOO0OO0OOO00.name}已被封')#line:245
                return False #line:246
            O00OOOOO0OO0OOO00 .msg +=f"""{O00OOOOO0OO0OOO00.name}:今日阅读次数:{O00O0O00O00OOO0OO["dayCount"]}，当前花儿:{O00O0O00O00OOO0OO["moneyCurrent"]}，累计阅读次数:{O00O0O00O00OOO0OO["doneWx"]}\n"""#line:247
            printlog (f"""{O00OOOOO0OO0OOO00.name}:今日阅读次数:{O00O0O00O00OOO0OO["dayCount"]}，当前花儿:{O00O0O00O00OOO0OO["moneyCurrent"]}，累计阅读次数:{O00O0O00O00OOO0OO["doneWx"]}""")#line:249
            O000O00O0O0OOO0O0 =int (O00O0O00O00OOO0OO ["moneyCurrent"])#line:250
            O00OOOOO0OO0OOO00 .huid =O00O0O00O00OOO0OO .get ('uid')#line:251
            return O000O00O0O0OOO0O0 #line:252
        except :#line:253
            return False #line:254
    def psmoneyc (O00OOO000000O0OOO ):#line:256
        O0OOOOOOO000OOO00 ={**O00OOO000000O0OOO .payload ,**{'mid':O00OOO000000O0OOO .huid }}#line:257
        try :#line:258
            O0OO0O000O00OO00O =O00OOO000000O0OOO .s .post ("http://u.cocozx.cn/api/user/psmoneyc",json =O0OOOOOOO000OOO00 ).json ()#line:259
            O00OOO000000O0OOO .msg +=f"感谢下级送来的{O0OO0O000O00OO00O['result']['val']}花儿\n"#line:260
            printlog (f"{O00OOO000000O0OOO.name}:感谢下级送来的{O0OO0O000O00OO00O['result']['val']}花儿")#line:261
        except :#line:262
            pass #line:263
        return #line:264
    def get_status (O0O0OO0O00O0OOOOO ):#line:266
        OOO0OO00OO0OOO0O0 =requests .post ("http://u.cocozx.cn/api/user/read",headers =O0O0OO0O00O0OOOOO .headers ,json =O0O0OO0O00O0OOOOO .payload ).json ()#line:267
        debugger (f'getstatus {OOO0OO00OO0OOO0O0}')#line:268
        O0O0OO0O00O0OOOOO .status =OOO0OO00OO0OOO0O0 .get ("result").get ("status")#line:269
        if O0O0OO0O00O0OOOOO .status ==40 :#line:270
            O0O0OO0O00O0OOOOO .msg +="文章还没有准备好\n"#line:271
            printlog (f"{O0O0OO0O00O0OOOOO.name}:文章还没有准备好")#line:272
            return #line:273
        elif O0O0OO0O00O0OOOOO .status ==50 :#line:274
            O0O0OO0O00O0OOOOO .msg +="阅读失效\n"#line:275
            printlog (f"{O0O0OO0O00O0OOOOO.name}:阅读失效")#line:276
            if O0O0OO0O00O0OOOOO .biz is not None :#line:277
                if checkdict .update ({O0O0OO0O00O0OOOOO .biz :O0O0OO0O00O0OOOOO .username }):#line:278
                    print (f'checkdict添加检测号{O0O0OO0O00O0OOOOO.biz}: {O0O0OO0O00O0OOOOO.username}')#line:279
            return #line:280
        elif O0O0OO0O00O0OOOOO .status ==60 :#line:281
            O0O0OO0O00O0OOOOO .msg +="已经全部阅读完了\n"#line:282
            printlog (f"{O0O0OO0O00O0OOOOO.name}:已经全部阅读完了")#line:283
            return #line:284
        elif O0O0OO0O00O0OOOOO .status ==70 :#line:285
            O0O0OO0O00O0OOOOO .msg +="下一轮还未开启\n"#line:286
            printlog (f"{O0O0OO0O00O0OOOOO.name}:下一轮还未开启")#line:287
            return #line:288
        elif O0O0OO0O00O0OOOOO .status ==10 :#line:289
            O0OOOO00OOOO0OO0O =OOO0OO00OO0OOO0O0 ["result"]["url"]#line:290
            O0O0OO0O00O0OOOOO .msg +='-'*50 +"\n阅读链接获取成功\n"#line:291
            return O0OOOO00OOOO0OO0O #line:292
    def submit (OOO0OOO0OOOOO0000 ):#line:294
        OO0OO000O0O0OOO0O ={**{'type':1 },**OOO0OOO0OOOOO0000 .payload }#line:295
        O0000OO00000O0OOO =requests .post ("http://u.cocozx.cn/api/user/submit?zx=&xz=1",headers =OOO0OOO0OOOOO0000 .headers ,json =OO0OO000O0O0OOO0O )#line:296
        OO0O0OOOO0OOO0O00 =O0000OO00000O0OOO .json ().get ('result')#line:297
        debugger ('submit '+O0000OO00000O0OOO .text )#line:298
        OOO0OOO0OOOOO0000 .msg +=f'阅读成功,获得花儿{OO0O0OOOO0OOO0O00["val"]}，剩余次数:{OO0O0OOOO0OOO0O00["progress"]}\n'#line:299
        printlog (f"{OOO0OOO0OOOOO0000.name}:阅读成功,获得花儿{OO0O0OOOO0OOO0O00['val']}，剩余次数:{OO0O0OOOO0OOO0O00['progress']}")#line:300
    def read (O00O000O000OOO000 ):#line:302
        while True :#line:303
            OO0O0OO0OOO0O0O0O =O00O000O000OOO000 .get_status ()#line:304
            if not OO0O0OO0OOO0O0O0O :#line:305
                if O00O000O000OOO000 .status ==30 :#line:306
                    time .sleep (3 )#line:307
                    continue #line:308
                break #line:309
            OOO00OOOO000OO000 =getmpinfo (OO0O0OO0OOO0O0O0O )#line:310
            if not OOO00OOOO000OO000 :#line:311
                printlog (f'{O00O000O000OOO000.name}:获取文章信息失败，程序中止')#line:312
                return False #line:313
            O00O000O000OOO000 .msg +='开始阅读 '+OOO00OOOO000OO000 ['text']+'\n'#line:314
            O00O000O000OOO000 .username =OOO00OOOO000OO000 ['username']#line:315
            O00O000O000OOO000 .biz =OOO00OOOO000OO000 ['biz']#line:316
            printlog (f'{O00O000O000OOO000.name}:开始阅读 '+OOO00OOOO000OO000 ['text'])#line:317
            O0O00O00OOO0000O0 =randint (7 ,10 )#line:318
            if O00O000O000OOO000 .biz in checkdict .keys ():#line:319
                O00O000O000OOO000 .msg +='当前正在阅读检测文章\n'#line:320
                printlog (f'{O00O000O000OOO000.name}:正在阅读检测文章')#line:321
                if sendable :#line:322
                    send (OOO00OOOO000OO000 ['text'],f'{O00O000O000OOO000.name}  花花阅读正在读检测文章',OO0O0OO0OOO0O0O0O )#line:323
                if pushable :#line:324
                    push (f'【{O00O000O000OOO000.name}】\n点击阅读检测文章\n{OOO00OOOO000OO000["text"]}',f'【{O00O000O000OOO000.name}】 花花过检测',OO0O0OO0OOO0O0O0O ,O00O000O000OOO000 .uid )#line:326
                time .sleep (60 )#line:327
            time .sleep (O0O00O00OOO0000O0 )#line:328
            O00O000O000OOO000 .submit ()#line:329
    def tixian (O0O0OO0O0OO0OOO00 ):#line:331
        global txe #line:332
        O0O00OO00OO0000OO =O0O0OO0O0OO0OOO00 .get_info ()#line:333
        if O0O00OO00OO0000OO <txbz :#line:334
            O0O0OO0O0OO0OOO00 .msg +='你的花儿不多了\n'#line:335
            printlog (f'{O0O0OO0O0OO0OOO00.name}:你的花儿不多了')#line:336
            return False #line:337
        if 10000 <=O0O00OO00OO0000OO <49999 :#line:338
            txe =10000 #line:339
        elif 5000 <=O0O00OO00OO0000OO <10000 :#line:340
            txe =5000 #line:341
        elif 3000 <=O0O00OO00OO0000OO <5000 :#line:342
            txe =3000 #line:343
        elif O0O00OO00OO0000OO >=50000 :#line:344
            txe =50000 #line:345
        O0O0OO0O0OO0OOO00 .msg +=f"提现金额:{txe}"#line:346
        printlog (f'{O0O0OO0O0OO0OOO00.name}:提现金额 {txe}')#line:347
        OOOOOO0OO0OOO00OO ={**O0O0OO0O0OO0OOO00 .payload ,**{"val":txe }}#line:348
        try :#line:349
            OO00O00OOO0000000 =O0O0OO0O0OO0OOO00 .s .post ("http://u.cocozx.cn/api/user/wd",json =OOOOOO0OO0OOO00OO ).json ()#line:350
            O0O0OO0O0OO0OOO00 .msg +=f"提现结果:{OO00O00OOO0000000.get('msg')}\n"#line:351
            printlog (f'{O0O0OO0O0OO0OOO00.name}:提现结果 {OO00O00OOO0000000.get("msg")}')#line:352
        except :#line:353
            O0O0OO0O0OO0OOO00 .msg +=f"自动提现不成功，发送通知手动提现\n"#line:354
            printlog (f"{O0O0OO0O0OO0OOO00.name}:自动提现不成功，发送通知手动提现")#line:355
            if sendable :#line:356
                send (f'可提现金额 {int(txe) / 10000}元，点击提现',f'惜之酱提醒您 {O0O0OO0O0OO0OOO00.name} 花花阅读可以提现了',f'{O0O0OO0O0OO0OOO00.readhost}/user/index.html?mid=FK73K93DA')#line:358
            if pushable :#line:359
                push (f'可提现金额 {int(txe) / 10000}元，点击提现',f'惜之酱提醒您 {O0O0OO0O0OO0OOO00.name} 花花阅读可以提现了',f'{O0O0OO0O0OO0OOO00.readhost}/user/index.html?mid=FK73K93DA',O0O0OO0O0OO0OOO00 .uid )#line:361
    def run (O0OOOO0OOO000O0O0 ):#line:363
        if O0OOOO0OOO000O0O0 .get_info ():#line:364
            O0OOOO0OOO000O0O0 .stataccess ()#line:365
            O0OOOO0OOO000O0O0 .get_readhost ()#line:366
            O0OOOO0OOO000O0O0 .psmoneyc ()#line:367
            O0OOOO0OOO000O0O0 .read ()#line:368
            O0OOOO0OOO000O0O0 .tixian ()#line:369
        if not printf :#line:370
            print (O0OOOO0OOO000O0O0 .msg .strip ())#line:371
def yd (OO0OO0O0000OO00O0 ):#line:374
    while not OO0OO0O0000OO00O0 .empty ():#line:375
        O0OOOOO0OOOOOOO0O =OO0OO0O0000OO00O0 .get ()#line:376
        try :#line:377
            O0000OOO00000OO00 =Allinone (O0OOOOO0OOOOOOO0O )#line:378
            O0000OOO00000OO00 .run ()#line:379
        except Exception as OO0O0O00O0OOOOOOO :#line:380
            print (OO0O0O00O0OOOOOOO )#line:381
def get_info ():#line:384
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*20 )#line:386
    print ('入口：http://mr181283238.yxjbhdl.cn/user/index.html?mid=EG5EVNLF3')#line:387
    O00O0OOO0000OOO00 ='V1.4'#line:388
    O0OOO0000000OO00O =_OOOOO0000000O00OO ['version']['花花']#line:389
    print (f'当前版本{O00O0OOO0000OOO00}，仓库版本{O0OOO0000000OO00O}\n{_OOOOO0000000O00OO["update_log"]["花花"]}')#line:390
    if O00O0OOO0000OOO00 <O0OOO0000000OO00O :#line:391
        print ('请到仓库下载最新版本k_hh.py')#line:392
    return True #line:393
def main ():#line:396
    OO00O0O00000O0O0O =get_info ()#line:397
    print (checkdict )#line:398
    O0OO0000OOOOOOOO0 =os .getenv ('hhck')#line:399
    if not O0OO0000OOOOOOOO0 :#line:400
        O0OO0000OOOOOOOO0 =os .getenv ('aiock')#line:401
        if not O0OO0000OOOOOOOO0 :#line:402
            print (_OOOOO0000000O00OO .get ('msg')['花花'])#line:403
            exit ()#line:404
    try :#line:405
        O0OO0000OOOOOOOO0 =ast .literal_eval (O0OO0000OOOOOOOO0 )#line:406
    except :#line:407
        pass #line:408
    OOOOOOO0O0OOOOOOO =Queue ()#line:409
    OOO00O0OOO00OO0OO =[]#line:410
    print ('-'*20 )#line:411
    print (f'共获取到{len(O0OO0000OOOOOOOO0)}个账号，如与实际不符，请检查ck填写方式')#line:412
    print ("="*25 )#line:413
    if not OO00O0O00000O0O0O :#line:414
        exit ()#line:415
    for OOOOO0OOO0O00O0OO ,OOO0OOOO000OOO00O in enumerate (O0OO0000OOOOOOOO0 ,start =1 ):#line:416
        OOOOOOO0O0OOOOOOO .put (OOO0OOOO000OOO00O )#line:417
    for OOOOO0OOO0O00O0OO in range (max_workers ):#line:418
        OO00OO0O0000OOO0O =threading .Thread (target =yd ,args =(OOOOOOO0O0OOOOOOO ,))#line:419
        OO00OO0O0000OOO0O .start ()#line:420
        OOO00O0OOO00OO0OO .append (OO00OO0O0000OOO0O )#line:421
        time .sleep (delay_time )#line:422
    for OOO00OO00OOO0O000 in OOO00O0OOO00OO0OO :#line:423
        OOO00OO00OOO0O000 .join ()#line:424
    print ('-'*25 +f'\n{checkdict}')#line:425
    with open ('checkdict.json','w',encoding ='utf-8')as OOOOOOOO00000000O :#line:426
        OOOOOOOO00000000O .write (json .dumps (checkdict ))#line:427
if __name__ =='__main__':#line:430
    main ()#line:431
