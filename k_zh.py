# -*- coding: utf-8 -*-
# k_zh
# Author: 惜之酱
"""
先运行脚本，有问题再到群里问
new Env('智慧阅读');
入口：http://mr181125495.forsranaa.cloud/oz/index.html?mid=4G7QUZY8Y
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

import json #line:24
from random import randint #line:25
import os #line:26
import time #line:27
import requests #line:28
import ast #line:29
import re #line:30
import datetime #line:31
import threading #line:32
from queue import Queue #line:33
def get_msg ():#line:44
    O0O0000O00OOO0OO0 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:46
    OOOO00OO0OOO0O0OO =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O0O0000O00OOO0OO0 ).json ()#line:47
    return OOOO00OO0OOO0O0OO #line:48
_OO000000000OO0O00 =get_msg ()#line:51
try :#line:53
    from lxml import etree #line:54
except :#line:55
    print (_OO000000000OO0O00 .get ('help')['lxml'])#line:56
if sendable :#line:57
    qwbotkey =os .getenv ('qwbotkey')#line:58
    if not qwbotkey :#line:59
        print (_OO000000000OO0O00 .get ('help')['qwbotkey'])#line:60
        exit ()#line:61
if pushable :#line:63
    pushconfig =os .getenv ('pushconfig')#line:64
    if not pushconfig :#line:65
        print (_OO000000000OO0O00 .get ('help')['pushconfig'])#line:66
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
            print (_OO000000000OO0O00 .get ('help')['pushconfig'])#line:83
            exit ()#line:84
if not pushable and not sendable :#line:85
    print ('啥通知方式都不配置，你想上天吗')#line:86
    exit ()#line:87
def ftime ():#line:90
    O0OO0O000O0O000OO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:91
    return O0OO0O000O0O000OO #line:92
def debugger (O0O0O0OOOOOOO0OOO ):#line:95
    if debug :#line:96
        print (O0O0O0OOOOOOO0OOO )#line:97
def printlog (O0O00OOOO000OO00O ):#line:100
    if printf :#line:101
        print (O0O00OOOO000OO00O )#line:102
def send (OO00OOO0OOO0O0OO0 ,title ='通知',url =None ):#line:105
    if not title or not url :#line:106
        OOOO000O000OOOOO0 ={"msgtype":"text","text":{"content":f"{title}\n\n{OO00OOO0OOO0O0OO0}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg群：https://t.me/xiaoymgroup\n通知时间：{ftime()}",}}#line:113
    else :#line:114
        OOOO000O000OOOOO0 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":OO00OOO0OOO0O0OO0 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:127
    OO000O00O00O0OOOO =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:128
    OO0O0O0O0O00O000O =requests .post (OO000O00O00O0OOOO ,data =json .dumps (OOOO000O000OOOOO0 )).json ()#line:129
    if OO0O0O0O0O00O000O .get ('errcode')!=0 :#line:130
        print ('消息发送失败，请检查key和发送格式')#line:131
        return False #line:132
    return OO0O0O0O0O00O000O #line:133
def push (OO000O000O000OOO0 ,title ='通知',url ='',uid =None ):#line:136
    if uid :#line:137
        uids .append (uid )#line:138
    OOO00O000OO000OO0 ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入tg群](https://t.me/xiaoymgroup)</font>".replace ('msg',OO000O000O000OOO0 ).replace ('url',url )#line:140
    OOOO0O0O0O00OOOOO ={"appToken":appToken ,"content":OOO00O000OO000OO0 ,"summary":title ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:150
    OOOOOOOOOOOOO000O ='http://wxpusher.zjiecode.com/api/send/message'#line:151
    O00O00O0000O00O00 =requests .post (url =OOOOOOOOOOOOO000O ,json =OOOO0O0O0O00OOOOO ).json ()#line:152
    if O00O00O0000O00O00 .get ('code')!=1000 :#line:153
        print (O00O00O0000O00O00 .get ('msg'),O00O00O0000O00O00 )#line:154
    return O00O00O0000O00O00 #line:155
def getmpinfo (O0OOOO0000O00000O ):#line:158
    if not O0OOOO0000O00000O or O0OOOO0000O00000O =='':#line:159
        return False #line:160
    OOOO0OO00000OO00O ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:162
    O00OO000OO00O000O =requests .get (O0OOOO0000O00000O ,headers =OOOO0OO00000OO00O )#line:163
    OOO000OOO0OO0OO00 =etree .HTML (O00OO000OO00O000O .text )#line:164
    O0O0OOO0O00000000 =OOO000OOO0OO0OO00 .xpath ('//meta[@*="og:title"]/@content')#line:166
    if O0O0OOO0O00000000 :#line:167
        O0O0OOO0O00000000 =O0O0OOO0O00000000 [0 ]#line:168
    O000O000O0O0000OO =OOO000OOO0OO0OO00 .xpath ('//meta[@*="og:url"]/@content')#line:169
    if O000O000O0O0000OO :#line:170
        O000O000O0O0000OO =O000O000O0O0000OO [0 ].encode ().decode ()#line:171
    try :#line:172
        O00O0000O0O0O00OO =re .findall (r'biz=(.*?)&',O0OOOO0000O00000O )[0 ]#line:173
    except :#line:174
        O00O0000O0O0O00OO =re .findall (r'biz=(.*?)&',O000O000O0O0000OO )[0 ]#line:175
    if not O00O0000O0O0O00OO :#line:176
        return False #line:177
    OO0OOO00OO0O00000 =OOO000OOO0OO0OO00 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:178
    if OO0OOO00OO0O00000 :#line:179
        OO0OOO00OO0O00000 =OO0OOO00OO0O00000 [0 ].strip ()#line:180
    O0O000O0OO0OO00O0 =re .findall (r"user_name.DATA'\) : '(.*?)'",O00OO000OO00O000O .text )or OOO000OOO0OO0OO00 .xpath ('//span[@class="profile_meta_value"]/text()')#line:182
    if O0O000O0OO0OO00O0 :#line:183
        O0O000O0OO0OO00O0 =O0O000O0OO0OO00O0 [0 ]#line:184
    OO0OO00OO0OO000OO =re .findall (r'createTime = \'(.*)\'',O00OO000OO00O000O .text )#line:185
    if OO0OO00OO0OO000OO :#line:186
        OO0OO00OO0OO000OO =OO0OO00OO0OO000OO [0 ][5 :]#line:187
    OOO0OOOOO0000O00O =f'{OO0OO00OO0OO000OO}|{O0O0OOO0O00000000[:10]}|{O00O0000O0O0O00OO}|{OO0OOO00OO0O00000}'#line:188
    O000O0OO0OOOO0OO0 ={'biz':O00O0000O0O0O00OO ,'username':OO0OOO00OO0O00000 ,'text':OOO0OOOOO0000O00O }#line:189
    return O000O0OO0OOOO0OO0 #line:190
try :#line:193
    with open ('checkdict.json','r',encoding ='utf-8')as f :#line:194
        checkdict_local =json .loads (f .read ())#line:195
except :#line:196
    pass #line:197
checkdict ={'Mzg2Mzk3Mjk5NQ==':'小鱼儿','MjM5NjU4NTE0MA==':'财事汇','MzkwMjI2ODY5Ng==':'A每日新菜','Mzg3NzEwMzI1Nw==':'A爱玩品牌传奇','MzIyMDg0MzA1OQ==':'服装加工宝','Mzg4NTQ5NDkxMQ==':'秣宝网','Mzk0NjIwNzk0Mg==':'检索宝','MzU3NjA5MDYyMw==':'重庆翊宝智慧电子装置有限公司','MzU1Nzc2ODI0MA==':'星空财研','MzUxMDgxMjMxMw==':'美术宝1对1','MzU4NDMyMTE1MQ==':'海雀Alcidae','MzI4MDE0MzM2NQ==':'强宝时尚','MzA3Nzc5MDMyNg==':'考研红宝书','MjM5Njk5NjYyMQ==':'宝和祥茶业','MzA4NDAyNTQ2MA==':'嘉财万贯','MzIzMjk2MjM5MQ==':'花生酥陪你学','MzkyMDE0NTI2OA==':'重庆市租房宝','MzI0NDI0NzU4OQ==':'九舞文学','MjM5NDAzMjgzNg==':'东风卡车之友','MzI1NjUxMTc0Mw==':'爱普生商教投影机','MzIyNzU3NDIwMA==':'川名堂','MzAwMDUwOTczNg==':'0','MzI4NjYyNTEzMw==':'0','MzI5MDQxNjExNg==':'0','Mzg3MzA0MTkyMw==':'0','MzU0MTUzMTUxOQ==':'0',"MzUxMDA4OTk5MA==":'',}#line:206
try :#line:207
    checkdict ={**checkdict ,**checkdict_local }#line:208
except :#line:209
    pass #line:210
class Allinone :#line:213
    def __init__ (O0OO00OO000OO00OO ,OOOOOOOOO0OO00O00 ):#line:214
        O0OO00OO000OO00OO .uid =OOOOOOOOO0OO00O00 .get ('uid')#line:215
        O0OO00OO000OO00OO .name =OOOOOOOOO0OO00O00 ['name']#line:216
        O0OO00OO000OO00OO .username =None #line:217
        O0OO00OO000OO00OO .biz =None #line:218
        O0OO00OO000OO00OO .s =requests .session ()#line:219
        O0OO00OO000OO00OO .payload ={"un":OOOOOOOOO0OO00O00 ['un'],"token":OOOOOOOOO0OO00O00 ['token'],"pageSize":20 }#line:220
        O0OO00OO000OO00OO .s .headers ={'Accept':'application/json, text/javascript, */*; q=0.01','Content-Type':'application/json; charset=UTF-8','Host':'u.cocozx.cn','Connection':'keep-alive','Origin':'http://mr1694957965536.qwydu.com','User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",'Accept-Encoding':'gzip, deflate'}#line:227
        O0OO00OO000OO00OO .headers =O0OO00OO000OO00OO .s .headers .copy ()#line:228
        O0OO00OO000OO00OO .msg =''#line:229
    def get_readhost (OOOO00O0OOOOO0OO0 ):#line:231
        O0OOO00OOO00O0O0O ="http://u.cocozx.cn/api/oz/getReadHost"#line:232
        O0OO0O0OOOOO0O0OO =OOOO00O0OOOOO0OO0 .s .post (O0OOO00OOO00O0O0O ,json =OOOO00O0OOOOO0OO0 .payload ).json ()#line:233
        debugger (f'readhome {O0OO0O0OOOOO0O0OO}')#line:234
        OOOO00O0OOOOO0OO0 .readhost =O0OO0O0OOOOO0O0OO .get ('result')['host']#line:235
        OOOO00O0OOOOO0OO0 .headers ['Origin']=OOOO00O0OOOOO0OO0 .readhost #line:236
        OOOO00O0OOOOO0OO0 .msg +=f'邀请链接：{OOOO00O0OOOOO0OO0.readhost}/oz/index.html?mid={OOOO00O0OOOOO0OO0.huid}\n'#line:237
        printlog (f"{OOOO00O0OOOOO0OO0.name}:邀请链接：{OOOO00O0OOOOO0OO0.readhost}/oz/index.html?mid={OOOO00O0OOOOO0OO0.huid}")#line:238
    def get_info (O0000OO0OOO00OOO0 ):#line:240
        O00O00OOOOO0OO0O0 ='\u0034\u0033\u0033\u0057\u0048\u004d\u0032\u0056\u0057'if O0000OO0OOO00OOO0 .name =='AI'else '\u0034\u0047\u0037\u0051\u0055\u005a\u0059\u0038\u0059'#line:241
        OOOO00OO0O0OOOO00 ={**O0000OO0OOO00OOO0 .payload ,**{'\u0063\u006f\u0064\u0065':O00O00OOOOO0OO0O0 }}#line:242
        try :#line:243
            OO0OO0OOO0O00000O =O0000OO0OOO00OOO0 .s .post ("http://u.cocozx.cn/api/oz/info",json =OOOO00OO0O0OOOO00 ).json ()#line:244
            OO0OO00O00OO0OO00 =OO0OO0OOO0O00000O .get ("result")#line:245
            debugger (f'get_info {OO0OO0OOO0O00000O}')#line:246
            O0O0O00000OOO000O =OO0OO00O00OO0OO00 .get ('us')#line:247
            if O0O0O00000OOO000O ==2 :#line:248
                O0000OO0OOO00OOO0 .msg +=f'{O0000OO0OOO00OOO0.name}已被封\n'#line:249
                printlog (f'{O0000OO0OOO00OOO0.name}已被封')#line:250
                return False #line:251
            O0000OO0OOO00OOO0 .msg +=f"""{O0000OO0OOO00OOO0.name}:今日阅读次数:{OO0OO00O00OO0OO00["dayCount"]}，当前智慧:{OO0OO00O00OO0OO00["moneyCurrent"]}，累计阅读次数:{OO0OO00O00OO0OO00["doneWx"]}\n"""#line:252
            printlog (f"""{O0000OO0OOO00OOO0.name}:今日阅读次数:{OO0OO00O00OO0OO00["dayCount"]}，当前智慧:{OO0OO00O00OO0OO00["moneyCurrent"]}，累计阅读次数:{OO0OO00O00OO0OO00["doneWx"]}""")#line:254
            OO00O0OOO0OOOOO0O =int (OO0OO00O00OO0OO00 ["moneyCurrent"])#line:255
            O0000OO0OOO00OOO0 .huid =OO0OO00O00OO0OO00 .get ('uid')#line:256
            return OO00O0OOO0OOOOO0O #line:257
        except :#line:258
            return False #line:259
    def get_status (O0O000O00O0000000 ):#line:261
        O00O0OOO000O0OOOO =requests .post ("http://u.cocozx.cn/api/oz/read",headers =O0O000O00O0000000 .headers ,json =O0O000O00O0000000 .payload ).json ()#line:262
        debugger (f'getstatus {O00O0OOO000O0OOOO}')#line:263
        O0O000O00O0000000 .status =O00O0OOO000O0OOOO .get ("result").get ("status")#line:264
        if O0O000O00O0000000 .status ==40 :#line:265
            O0O000O00O0000000 .msg +="文章还没有准备好\n"#line:266
            printlog (f"{O0O000O00O0000000.name}:文章还没有准备好")#line:267
            return #line:268
        elif O0O000O00O0000000 .status ==50 :#line:269
            O0O000O00O0000000 .msg +="阅读失效\n"#line:270
            printlog (f"{O0O000O00O0000000.name}:阅读失效")#line:271
            if O0O000O00O0000000 .biz is not None :#line:272
                checkdict .update ({O0O000O00O0000000 .biz :O0O000O00O0000000 .username })#line:273
            return #line:274
        elif O0O000O00O0000000 .status ==60 :#line:275
            O0O000O00O0000000 .msg +="已经全部阅读完了\n"#line:276
            printlog (f"{O0O000O00O0000000.name}:已经全部阅读完了")#line:277
            return #line:278
        elif O0O000O00O0000000 .status ==70 :#line:279
            O0O000O00O0000000 .msg +="下一轮还未开启\n"#line:280
            printlog (f"{O0O000O00O0000000.name}:下一轮还未开启")#line:281
            return #line:282
        elif O0O000O00O0000000 .status ==10 :#line:283
            OOO00OOOOOOOOO0O0 =O00O0OOO000O0OOOO ["result"]["url"]#line:284
            O0O000O00O0000000 .msg +='-'*50 +"\n阅读链接获取成功\n"#line:285
            return OOO00OOOOOOOOO0O0 #line:286
    def submit (O0O00O0000000000O ):#line:288
        OO00O000000O00O00 ={**{'type':1 },**O0O00O0000000000O .payload }#line:289
        OOOO0OOOO0O0OO0OO =requests .post ("http://u.cocozx.cn/api/oz/submit?zx=&xz=1",headers =O0O00O0000000000O .headers ,json =OO00O000000O00O00 )#line:290
        O0OOO0OO0OO0OOO00 =OOOO0OOOO0O0OO0OO .json ().get ('result')#line:291
        debugger ('submit '+OOOO0OOOO0O0OO0OO .text )#line:292
        O0O00O0000000000O .msg +=f"阅读成功,获得智慧{O0OOO0OO0OO0OOO00['val']}，当前剩余次数:{O0OOO0OO0OO0OOO00['progress']}\n"#line:293
        printlog (f"{O0O00O0000000000O.name}:阅读成功,获得智慧{O0OOO0OO0OO0OOO00['val']}，当前剩余次数:{O0OOO0OO0OO0OOO00['progress']}")#line:294
    def read (O00OO0OO0OOOO0000 ):#line:296
        while True :#line:297
            O0O00000O00O0O000 =O00OO0OO0OOOO0000 .get_status ()#line:298
            if not O0O00000O00O0O000 :#line:299
                if O00OO0OO0OOOO0000 .status ==30 :#line:300
                    time .sleep (3 )#line:301
                    continue #line:302
                break #line:303
            O0O0OOO0O0O000OOO =getmpinfo (O0O00000O00O0O000 )#line:304
            O00OO0OO0OOOO0000 .username =O0O0OOO0O0O000OOO ['username']#line:305
            O00OO0OO0OOOO0000 .biz =O0O0OOO0O0O000OOO ['biz']#line:306
            O00OO0OO0OOOO0000 .msg +='开始阅读 '+O0O0OOO0O0O000OOO ['text']+'\n'#line:307
            printlog (f'{O00OO0OO0OOOO0000.name}:开始阅读 '+O0O0OOO0O0O000OOO ['text'])#line:308
            O0OO0OOO000O000O0 =randint (7 ,10 )#line:309
            if O0O0OOO0O0O000OOO ['biz']in checkdict .keys ():#line:310
                O00OO0OO0OOOO0000 .msg +='当前正在阅读检测文章\n'#line:311
                printlog (f'{O00OO0OO0OOOO0000.name}:正在阅读检测文章')#line:312
                if sendable :#line:313
                    send (O0O0OOO0O0O000OOO ['text'],f'{O00OO0OO0OOOO0000.name}  智慧阅读正在读检测文章',O0O00000O00O0O000 )#line:314
                if pushable :#line:315
                    push (f'【{O00OO0OO0OOOO0000.name}】\n点击阅读检测文章\n{O0O0OOO0O0O000OOO["text"]}',f'【{O00OO0OO0OOOO0000.name}】 智慧过检测',O0O00000O00O0O000 ,O00OO0OO0OOOO0000 .uid )#line:317
                time .sleep (60 )#line:318
            time .sleep (O0OO0OOO000O000O0 )#line:319
            O00OO0OO0OOOO0000 .submit ()#line:320
    def tixian (OO0O0O00O0O00OOOO ):#line:322
        global txe #line:323
        OOOO00O00000000O0 =OO0O0O00O0O00OOOO .get_info ()#line:324
        if OOOO00O00000000O0 <txbz :#line:325
            OO0O0O00O0O00OOOO .msg +='你的智慧不多了\n'#line:326
            printlog (f'{OO0O0O00O0O00OOOO.name}:你的智慧不多了')#line:327
            return False #line:328
        elif 10000 <=OOOO00O00000000O0 <49999 :#line:329
            txe =10000 #line:330
        elif 50000 <=OOOO00O00000000O0 <100000 :#line:331
            txe =50000 #line:332
        elif 3000 <=OOOO00O00000000O0 <10000 :#line:333
            txe =3000 #line:334
        elif OOOO00O00000000O0 >=100000 :#line:335
            txe =100000 #line:336
        OO0O0O00O0O00OOOO .msg +=f"提现金额:{txe}\n"#line:337
        printlog (f'{OO0O0O00O0O00OOOO.name}:提现金额 {txe}')#line:338
        O0O00OOOO0OO00OOO ={**OO0O0O00O0O00OOOO .payload ,**{"val":txe }}#line:339
        try :#line:340
            O0O000O0O0OO0O0OO =OO0O0O00O0O00OOOO .s .post ("http://u.cocozx.cn/api/oz/wdmoney",json =O0O00OOOO0OO00OOO ).json ()#line:341
            OO0O0O00O0O00OOOO .msg +=f'提现结果：{O0O000O0O0OO0O0OO.get("msg")}\n'#line:342
            printlog (f'{OO0O0O00O0O00OOOO.name}:提现结果 {O0O000O0O0OO0O0OO.get("msg")}')#line:343
        except :#line:344
            OO0O0O00O0O00OOOO .msg +=f"自动提现不成功，发送通知手动提现\n"#line:345
            printlog (f"{OO0O0O00O0O00OOOO.name}:自动提现不成功，发送通知手动提现")#line:346
            if sendable :#line:347
                send (f'可提现金额 {int(txe) / 10000}元，点击提现',f'惜之酱提醒您 {OO0O0O00O0O00OOOO.name} 智慧阅读可以提现了',f'{OO0O0O00O0O00OOOO.readhost}/oz/index.html?mid=QX5E9WLGS')#line:349
            if pushable :#line:350
                push (f'可提现金额 {int(txe) / 10000}元，点击提现',f'惜之酱提醒您 {OO0O0O00O0O00OOOO.name} 智慧阅读可以提现了',f'{OO0O0O00O0O00OOOO.readhost}/oz/index.html?mid=QX5E9WLGS',OO0O0O00O0O00OOOO .uid )#line:352
    def run (O0OO00O0OOO00O00O ):#line:354
        O0OO00O0OOO00O00O .msg +='*'*50 +'\n'#line:355
        if O0OO00O0OOO00O00O .get_info ():#line:356
            O0OO00O0OOO00O00O .get_readhost ()#line:357
            O0OO00O0OOO00O00O .read ()#line:358
            O0OO00O0OOO00O00O .tixian ()#line:359
        if not printf :#line:360
            print (O0OO00O0OOO00O00O .msg .strip ())#line:361
def yd (O0OOOO0O0O0000OOO ):#line:364
    while not O0OOOO0O0O0000OOO .empty ():#line:365
        OOOO0OO0OO0000O0O =O0OOOO0O0O0000OOO .get ()#line:366
        OO00OO0OO00OO0000 =Allinone (OOOO0OO0OO0000O0O )#line:367
        OO00OO0OO00OO0000 .run ()#line:368
def get_info ():#line:371
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:373
    print ('入口：http://mr181125495.forsranaa.cloud/oz/index.html?mid=4G7QUZY8Y')#line:374
    OOOOOOO000000O000 ='v1.4'#line:375
    OO00O0OOO0O00OOO0 =_OO000000000OO0O00 ['version'].get ('智慧')#line:376
    print (f'当前版本{OOOOOOO000000O000}，仓库版本{OO00O0OOO0O00OOO0}\n{_OO000000000OO0O00["update_log"]["花花"]}')#line:377
    if OOOOOOO000000O000 <OO00O0OOO0O00OOO0 :#line:378
        print ('请到仓库下载最新版本k_zh.py')#line:379
    return True #line:380
def main ():#line:383
    O000O0O0O0O0O00OO =get_info ()#line:384
    O000OO0O000OOOO00 =os .getenv ('zhck')#line:385
    if not O000OO0O000OOOO00 :#line:386
        O000OO0O000OOOO00 =os .getenv ('aiock')#line:387
        if not O000OO0O000OOOO00 :#line:388
            print (_OO000000000OO0O00 .get ('msg')['智慧'])#line:389
            exit ()#line:390
    try :#line:391
        O000OO0O000OOOO00 =ast .literal_eval (O000OO0O000OOOO00 )#line:392
    except :#line:393
        pass #line:394
    print ('-'*20 )#line:395
    print (f'共获取到{len(O000OO0O000OOOO00)}个账号，如与实际不符，请检查ck填写方式')#line:396
    print ("="*25 )#line:397
    OO0O00OOOO00O0OOO =Queue ()#line:398
    O000OO00O00000OOO =[]#line:399
    if not O000O0O0O0O0O00OO :#line:400
        exit ()#line:401
    for OOOO0OOO00OOO0000 ,O0OO0O0OO0OOO000O in enumerate (O000OO0O000OOOO00 ,start =1 ):#line:402
        OO0O00OOOO00O0OOO .put (O0OO0O0OO0OOO000O )#line:403
    for OOOO0OOO00OOO0000 in range (max_workers ):#line:404
        O00OO0OOOO00OOOO0 =threading .Thread (target =yd ,args =(OO0O00OOOO00O0OOO ,))#line:405
        O00OO0OOOO00OOOO0 .start ()#line:406
        O000OO00O00000OOO .append (O00OO0OOOO00OOOO0 )#line:407
        time .sleep (delay_time )#line:408
    for OO0O00OO000O00O00 in O000OO00O00000OOO :#line:409
        OO0O00OO000O00O00 .join ()#line:410
    print ('-'*25 +f'\n{checkdict}')#line:411
    with open ('checkdict.json','w',encoding ='utf-8')as O000O0OO0O00OO000 :#line:412
        O000O0OO0O00OO000 .write (json .dumps (checkdict ))#line:413
if __name__ =='__main__':#line:416
    main ()#line:417
