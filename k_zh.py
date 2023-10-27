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
    OOOO0000O00OOOOOO ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:46
    OO0OO00OO0O0OO0O0 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OOOO0000O00OOOOOO ).json ()#line:47
    return OO0OO00OO0O0OO0O0 #line:48
_OO00OO000O0O00000 =get_msg ()#line:51
try :#line:53
    from lxml import etree #line:54
except :#line:55
    print (_OO00OO000O0O00000 .get ('help')['lxml'])#line:56
if sendable :#line:57
    qwbotkey =os .getenv ('qwbotkey')#line:58
    if not qwbotkey :#line:59
        print (_OO00OO000O0O00000 .get ('help')['qwbotkey'])#line:60
        exit ()#line:61
if pushable :#line:63
    pushconfig =os .getenv ('pushconfig')#line:64
    if not pushconfig :#line:65
        print (_OO00OO000O0O00000 .get ('help')['pushconfig'])#line:66
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
            print (_OO00OO000O0O00000 .get ('help')['pushconfig'])#line:83
            exit ()#line:84
if not pushable and not sendable :#line:85
    print ('啥通知方式都不配置，你想上天吗')#line:86
    exit ()#line:87
def ftime ():#line:90
    O00O0O0O0O00O0O00 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:91
    return O00O0O0O0O00O0O00 #line:92
def debugger (OO0000OOO00O0O000 ):#line:95
    if debug :#line:96
        print (OO0000OOO00O0O000 )#line:97
def printlog (OOOOOOOO0000O00OO ):#line:100
    if printf :#line:101
        print (OOOOOOOO0000O00OO )#line:102
def send (OO0O0OOO000OO00O0 ,title ='通知',url =None ):#line:105
    if not title or not url :#line:106
        OOO00OOO0OOOOO000 ={"msgtype":"text","text":{"content":f"{title}\n\n{OO0O0OOO000OO00O0}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:113
    else :#line:114
        OOO00OOO0OOOOO000 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":OO0O0OOO000OO00O0 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:127
    OOO000O0OO0O0000O =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:128
    O000OO00OOO0OOOO0 =requests .post (OOO000O0OO0O0000O ,data =json .dumps (OOO00OOO0OOOOO000 )).json ()#line:129
    if O000OO00OOO0OOOO0 .get ('errcode')!=0 :#line:130
        print ('消息发送失败，请检查key和发送格式')#line:131
        return False #line:132
    return O000OO00OOO0OOOO0 #line:133
def push (OOOOOOOO0000OO000 ,title ='通知',url ='',uid =None ):#line:136
    if uid :#line:137
        uids .append (uid )#line:138
    OOOOOO00000000OO0 ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',OOOOOOOO0000OO000 ).replace ('url',url )#line:140
    OOOO00OO00O0OO00O ={"appToken":appToken ,"content":OOOOOO00000000OO0 ,"summary":title ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:150
    O0O0OO000O000O0OO ='http://wxpusher.zjiecode.com/api/send/message'#line:151
    OOO0OO0OO0000OO0O =requests .post (url =O0O0OO000O000O0OO ,json =OOOO00OO00O0OO00O ).json ()#line:152
    if OOO0OO0OO0000OO0O .get ('code')!=1000 :#line:153
        print (OOO0OO0OO0000OO0O .get ('msg'),OOO0OO0OO0000OO0O )#line:154
    return OOO0OO0OO0000OO0O #line:155
def getmpinfo (OO0O0O0O000O00O00 ):#line:158
    if not OO0O0O0O000O00O00 or OO0O0O0O000O00O00 =='':#line:159
        return False #line:160
    O000000OO0O00OO00 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:162
    O000O00OO0O00000O =requests .get (OO0O0O0O000O00O00 ,headers =O000000OO0O00OO00 )#line:163
    OO0O00O0O000O0O0O =etree .HTML (O000O00OO0O00000O .text )#line:164
    O0OO00O0O00O000O0 =OO0O00O0O000O0O0O .xpath ('//meta[@*="og:title"]/@content')#line:166
    if O0OO00O0O00O000O0 :#line:167
        O0OO00O0O00O000O0 =O0OO00O0O00O000O0 [0 ]#line:168
    OO00O0000OO000OOO =OO0O00O0O000O0O0O .xpath ('//meta[@*="og:url"]/@content')#line:169
    if OO00O0000OO000OOO :#line:170
        OO00O0000OO000OOO =OO00O0000OO000OOO [0 ].encode ().decode ()#line:171
    try :#line:172
        O00000000000OO00O =re .findall (r'biz=(.*?)&',OO0O0O0O000O00O00 )[0 ]#line:173
    except :#line:174
        O00000000000OO00O =re .findall (r'biz=(.*?)&',OO00O0000OO000OOO )[0 ]#line:175
    if not O00000000000OO00O :#line:176
        return False #line:177
    O0000OOOO0O0O000O =OO0O00O0O000O0O0O .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:178
    if O0000OOOO0O0O000O :#line:179
        O0000OOOO0O0O000O =O0000OOOO0O0O000O [0 ].strip ()#line:180
    OO00O0OOOO00OOO00 =re .findall (r"user_name.DATA'\) : '(.*?)'",O000O00OO0O00000O .text )or OO0O00O0O000O0O0O .xpath ('//span[@class="profile_meta_value"]/text()')#line:182
    if OO00O0OOOO00OOO00 :#line:183
        OO00O0OOOO00OOO00 =OO00O0OOOO00OOO00 [0 ]#line:184
    OOO000OO000000O0O =re .findall (r'createTime = \'(.*)\'',O000O00OO0O00000O .text )#line:185
    if OOO000OO000000O0O :#line:186
        OOO000OO000000O0O =OOO000OO000000O0O [0 ][5 :]#line:187
    OO0OOO0O0OO0OO0OO =f'{OOO000OO000000O0O}|{O0OO00O0O00O000O0[:10]}|{O00000000000OO00O}|{O0000OOOO0O0O000O}'#line:188
    OOO00OOOO0OO0OOO0 ={'biz':O00000000000OO00O ,'username':O0000OOOO0O0O000O ,'text':OO0OOO0O0OO0OO0OO }#line:189
    return OOO00OOOO0OO0OOO0 #line:190
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
    def __init__ (OO000O0OOOO000OOO ,OO0OO000O0OO0OO0O ):#line:214
        OO000O0OOOO000OOO .uid =OO0OO000O0OO0OO0O .get ('uid')#line:215
        OO000O0OOOO000OOO .name =OO0OO000O0OO0OO0O ['name']#line:216
        OO000O0OOOO000OOO .username =None #line:217
        OO000O0OOOO000OOO .biz =None #line:218
        OO000O0OOOO000OOO .s =requests .session ()#line:219
        OO000O0OOOO000OOO .payload ={"un":OO0OO000O0OO0OO0O ['un'],"token":OO0OO000O0OO0OO0O ['token'],"pageSize":20 }#line:220
        OO000O0OOOO000OOO .s .headers ={'Accept':'application/json, text/javascript, */*; q=0.01','Content-Type':'application/json; charset=UTF-8','Host':'u.cocozx.cn','Connection':'keep-alive','Origin':'http://mr1694957965536.qwydu.com','User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",'Accept-Encoding':'gzip, deflate'}#line:227
        OO000O0OOOO000OOO .headers =OO000O0OOOO000OOO .s .headers .copy ()#line:228
        OO000O0OOOO000OOO .msg =''#line:229
    def get_readhost (O000OOO0OO0OOOO00 ):#line:231
        OOO0OO0O0OOOOOOO0 ="http://u.cocozx.cn/api/oz/getReadHost"#line:232
        OOO0O000OO00OO0OO =O000OOO0OO0OOOO00 .s .post (OOO0OO0O0OOOOOOO0 ,json =O000OOO0OO0OOOO00 .payload ).json ()#line:233
        debugger (f'readhome {OOO0O000OO00OO0OO}')#line:234
        O000OOO0OO0OOOO00 .readhost =OOO0O000OO00OO0OO .get ('result')['host']#line:235
        O000OOO0OO0OOOO00 .headers ['Origin']=O000OOO0OO0OOOO00 .readhost #line:236
        O000OOO0OO0OOOO00 .msg +=f'邀请链接：{O000OOO0OO0OOOO00.readhost}/oz/index.html?mid={O000OOO0OO0OOOO00.huid}\n'#line:237
        printlog (f"{O000OOO0OO0OOOO00.name}:邀请链接：{O000OOO0OO0OOOO00.readhost}/oz/index.html?mid={O000OOO0OO0OOOO00.huid}")#line:238
    def get_info (O0O00000O0OOOO0O0 ):#line:240
        O0OO0O0O00OOO0OOO ='\u0034\u0033\u0033\u0057\u0048\u004d\u0032\u0056\u0057'if O0O00000O0OOOO0O0 .name =='AI'else '\u0034\u0047\u0037\u0051\u0055\u005a\u0059\u0038\u0059'#line:241
        O0O0O0O0OOOOO0O00 ={**O0O00000O0OOOO0O0 .payload ,**{'\u0063\u006f\u0064\u0065':O0OO0O0O00OOO0OOO }}#line:242
        try :#line:243
            OOOO000O000O0O0OO =O0O00000O0OOOO0O0 .s .post ("http://u.cocozx.cn/api/oz/info",json =O0O0O0O0OOOOO0O00 ).json ()#line:244
            O00O00O0O00O0O0O0 =OOOO000O000O0O0OO .get ("result")#line:245
            debugger (f'get_info {OOOO000O000O0O0OO}')#line:246
            OO00OOO0OOOOOO0O0 =O00O00O0O00O0O0O0 .get ('us')#line:247
            if OO00OOO0OOOOOO0O0 ==2 :#line:248
                O0O00000O0OOOO0O0 .msg +=f'{O0O00000O0OOOO0O0.name}已被封\n'#line:249
                printlog (f'{O0O00000O0OOOO0O0.name}已被封')#line:250
                return False #line:251
            O0O00000O0OOOO0O0 .msg +=f"""{O0O00000O0OOOO0O0.name}:今日阅读次数:{O00O00O0O00O0O0O0["dayCount"]}，当前智慧:{O00O00O0O00O0O0O0["moneyCurrent"]}\n"""#line:252
            printlog (f"""{O0O00000O0OOOO0O0.name}:今日阅读次数:{O00O00O0O00O0O0O0["dayCount"]}，当前智慧:{O00O00O0O00O0O0O0["moneyCurrent"]}""")#line:254
            O0O0OO0OO00000O0O =int (O00O00O0O00O0O0O0 ["moneyCurrent"])#line:255
            O0O00000O0OOOO0O0 .huid =O00O00O0O00O0O0O0 .get ('uid')#line:256
            return O0O0OO0OO00000O0O #line:257
        except :#line:258
            return False #line:259
    def get_status (OO000O0O000000O0O ):#line:261
        OO0O000OO0OOOO000 =requests .post ("http://u.cocozx.cn/api/oz/read",headers =OO000O0O000000O0O .headers ,json =OO000O0O000000O0O .payload ).json ()#line:262
        debugger (f'getstatus {OO0O000OO0OOOO000}')#line:263
        OO000O0O000000O0O .status =OO0O000OO0OOOO000 .get ("result").get ("status")#line:264
        if OO000O0O000000O0O .status ==40 :#line:265
            OO000O0O000000O0O .msg +="文章还没有准备好\n"#line:266
            printlog (f"{OO000O0O000000O0O.name}:文章还没有准备好")#line:267
            return #line:268
        elif OO000O0O000000O0O .status ==50 :#line:269
            OO000O0O000000O0O .msg +="阅读失效\n"#line:270
            printlog (f"{OO000O0O000000O0O.name}:阅读失效")#line:271
            if OO000O0O000000O0O .biz is not None :#line:272
                checkdict .update ({OO000O0O000000O0O .biz :OO000O0O000000O0O .username })#line:273
            return #line:274
        elif OO000O0O000000O0O .status ==60 :#line:275
            OO000O0O000000O0O .msg +="已经全部阅读完了\n"#line:276
            printlog (f"{OO000O0O000000O0O.name}:已经全部阅读完了")#line:277
            return #line:278
        elif OO000O0O000000O0O .status ==70 :#line:279
            OO000O0O000000O0O .msg +="下一轮还未开启\n"#line:280
            printlog (f"{OO000O0O000000O0O.name}:下一轮还未开启")#line:281
            return #line:282
        elif OO000O0O000000O0O .status ==10 :#line:283
            O0O000O0OO0000OOO =OO0O000OO0OOOO000 ["result"]["url"]#line:284
            OO000O0O000000O0O .msg +='-'*50 +"\n阅读链接获取成功\n"#line:285
            return O0O000O0OO0000OOO #line:286
    def submit (O0000O000OOOO0000 ):#line:288
        OOO0OOO00OOOO000O ={**{'type':1 },**O0000O000OOOO0000 .payload }#line:289
        O0O0OO0O0O0O0OO00 =requests .post ("http://u.cocozx.cn/api/oz/submit?zx=&xz=1",headers =O0000O000OOOO0000 .headers ,json =OOO0OOO00OOOO000O )#line:290
        OO0000OO0OO00OOOO =O0O0OO0O0O0O0OO00 .json ().get ('result')#line:291
        debugger ('submit '+O0O0OO0O0O0O0OO00 .text )#line:292
        O0000O000OOOO0000 .msg +=f"阅读成功,获得智慧{OO0000OO0OO00OOOO['val']}，当前剩余次数:{OO0000OO0OO00OOOO['progress']}\n"#line:293
        printlog (f"{O0000O000OOOO0000.name}:阅读成功,获得智慧{OO0000OO0OO00OOOO['val']}，当前剩余次数:{OO0000OO0OO00OOOO['progress']}")#line:294
    def read (O00OO00O000OOO000 ):#line:296
        while True :#line:297
            O0000OO0000O0O0OO =O00OO00O000OOO000 .get_status ()#line:298
            if not O0000OO0000O0O0OO :#line:299
                if O00OO00O000OOO000 .status ==30 :#line:300
                    time .sleep (3 )#line:301
                    continue #line:302
                break #line:303
            O000OO0O00O0OO00O =getmpinfo (O0000OO0000O0O0OO )#line:304
            O00OO00O000OOO000 .username =O000OO0O00O0OO00O ['username']#line:305
            O00OO00O000OOO000 .biz =O000OO0O00O0OO00O ['biz']#line:306
            O00OO00O000OOO000 .msg +='开始阅读 '+O000OO0O00O0OO00O ['text']+'\n'#line:307
            printlog (f'{O00OO00O000OOO000.name}:开始阅读 '+O000OO0O00O0OO00O ['text'])#line:308
            O0000OO0000OO0OOO =randint (7 ,10 )#line:309
            if O000OO0O00O0OO00O ['biz']in checkdict .keys ():#line:310
                O00OO00O000OOO000 .msg +='当前正在阅读检测文章\n'#line:311
                printlog (f'{O00OO00O000OOO000.name}:正在阅读检测文章')#line:312
                if sendable :#line:313
                    send (O000OO0O00O0OO00O ['text'],f'{O00OO00O000OOO000.name}  智慧阅读正在读检测文章',O0000OO0000O0O0OO )#line:314
                if pushable :#line:315
                    push (f'【{O00OO00O000OOO000.name}】\n点击阅读检测文章\n{O000OO0O00O0OO00O["text"]}',f'【{O00OO00O000OOO000.name}】 智慧过检测',O0000OO0000O0O0OO ,O00OO00O000OOO000 .uid )#line:317
                time .sleep (60 )#line:318
            time .sleep (O0000OO0000OO0OOO )#line:319
            O00OO00O000OOO000 .submit ()#line:320
    def tixian (O0OOOOOO0O0OOO000 ):#line:322
        global txe #line:323
        OOOO0OO000OOOO0O0 =O0OOOOOO0O0OOO000 .get_info ()#line:324
        if OOOO0OO000OOOO0O0 <txbz :#line:325
            O0OOOOOO0O0OOO000 .msg +='你的智慧不多了\n'#line:326
            printlog (f'{O0OOOOOO0O0OOO000.name}:你的智慧不多了')#line:327
            return False #line:328
        elif 10000 <=OOOO0OO000OOOO0O0 <49999 :#line:329
            txe =10000 #line:330
        elif 50000 <=OOOO0OO000OOOO0O0 <100000 :#line:331
            txe =50000 #line:332
        elif 3000 <=OOOO0OO000OOOO0O0 <10000 :#line:333
            txe =3000 #line:334
        elif OOOO0OO000OOOO0O0 >=100000 :#line:335
            txe =100000 #line:336
        O0OOOOOO0O0OOO000 .msg +=f"提现金额:{txe}\n"#line:337
        printlog (f'{O0OOOOOO0O0OOO000.name}:提现金额 {txe}')#line:338
        O0OOOOO0OOO0OOOO0 ={**O0OOOOOO0O0OOO000 .payload ,**{"val":txe }}#line:339
        try :#line:340
            OO00OOOO0O0OO0O0O =O0OOOOOO0O0OOO000 .s .post ("http://u.cocozx.cn/api/oz/wdmoney",json =O0OOOOO0OOO0OOOO0 ).json ()#line:341
            O0OOOOOO0O0OOO000 .msg +=f'提现结果：{OO00OOOO0O0OO0O0O.get("msg")}\n'#line:342
            printlog (f'{O0OOOOOO0O0OOO000.name}:提现结果 {OO00OOOO0O0OO0O0O.get("msg")}')#line:343
        except :#line:344
            O0OOOOOO0O0OOO000 .msg +=f"自动提现不成功，发送通知手动提现\n"#line:345
            printlog (f"{O0OOOOOO0O0OOO000.name}:自动提现不成功，发送通知手动提现")#line:346
            if sendable :#line:347
                send (f'可提现金额 {int(txe) / 10000}元，点击提现',f'惜之酱提醒您 {O0OOOOOO0O0OOO000.name} 智慧阅读可以提现了',f'{O0OOOOOO0O0OOO000.readhost}/oz/index.html?mid=QX5E9WLGS')#line:349
            if pushable :#line:350
                push (f'可提现金额 {int(txe) / 10000}元，点击提现',f'惜之酱提醒您 {O0OOOOOO0O0OOO000.name} 智慧阅读可以提现了',f'{O0OOOOOO0O0OOO000.readhost}/oz/index.html?mid=QX5E9WLGS',O0OOOOOO0O0OOO000 .uid )#line:352
    def run (O0OO00OO00000O0O0 ):#line:354
        O0OO00OO00000O0O0 .msg +='*'*50 +'\n'#line:355
        if O0OO00OO00000O0O0 .get_info ():#line:356
            O0OO00OO00000O0O0 .get_readhost ()#line:357
            O0OO00OO00000O0O0 .read ()#line:358
            O0OO00OO00000O0O0 .tixian ()#line:359
        if not printf :#line:360
            print (O0OO00OO00000O0O0 .msg .strip ())#line:361
def yd (O0OO000OO0O0O00O0 ):#line:364
    while not O0OO000OO0O0O00O0 .empty ():#line:365
        OOOOOOO00OOOO00O0 =O0OO000OO0O0O00O0 .get ()#line:366
        OOO00O000OO0OO000 =Allinone (OOOOOOO00OOOO00O0 )#line:367
        OOO00O000OO0OO000 .run ()#line:368
def get_info ():#line:371
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:373
    print ('入口：http://mr181125495.forsranaa.cloud/oz/index.html?mid=4G7QUZY8Y')#line:374
    O00000OOO0OOO00O0 ='v1.5'#line:375
    O000000O0O0OOOOOO =_OO00OO000O0O00000 ['version'].get ('智慧')#line:376
    print (f'当前版本{O00000OOO0OOO00O0}，仓库版本{O000000O0O0OOOOOO}\n{_OO00OO000O0O00000["update_log"]["花花"]}')#line:377
    if O00000OOO0OOO00O0 <O000000O0O0OOOOOO :#line:378
        print ('请到仓库下载最新版本k_zh.py')#line:379
    return True #line:380
def main ():#line:383
    O00O00O000OO00000 =get_info ()#line:384
    OOOOOO0O00O00OO00 =os .getenv ('zhck')#line:385
    if not OOOOOO0O00O00OO00 :#line:386
        OOOOOO0O00O00OO00 =os .getenv ('aiock')#line:387
        if not OOOOOO0O00O00OO00 :#line:388
            print (_OO00OO000O0O00000 .get ('msg')['智慧'])#line:389
            exit ()#line:390
    try :#line:391
        OOOOOO0O00O00OO00 =ast .literal_eval (OOOOOO0O00O00OO00 )#line:392
    except :#line:393
        pass #line:394
    print ('-'*20 )#line:395
    print (f'共获取到{len(OOOOOO0O00O00OO00)}个账号，如与实际不符，请检查ck填写方式')#line:396
    print ("="*25 )#line:397
    O0OO0O00OO00O0OO0 =Queue ()#line:398
    OO000000000O0OOOO =[]#line:399
    if not O00O00O000OO00000 :#line:400
        exit ()#line:401
    for O00O0O0O0O0OO00O0 ,OOO00O000OOO000O0 in enumerate (OOOOOO0O00O00OO00 ,start =1 ):#line:402
        O0OO0O00OO00O0OO0 .put (OOO00O000OOO000O0 )#line:403
    for O00O0O0O0O0OO00O0 in range (max_workers ):#line:404
        OOO0OOOOO0OO00O00 =threading .Thread (target =yd ,args =(O0OO0O00OO00O0OO0 ,))#line:405
        OOO0OOOOO0OO00O00 .start ()#line:406
        OO000000000O0OOOO .append (OOO0OOOOO0OO00O00 )#line:407
        time .sleep (delay_time )#line:408
    for O000000O0OO000OOO in OO000000000O0OOOO :#line:409
        O000000O0OO000OOO .join ()#line:410
    print ('-'*25 +f'\n{checkdict}')#line:411
    with open ('checkdict.json','w',encoding ='utf-8')as O0000O0O0OOO00O0O :#line:412
        O0000O0O0OOO00O0O .write (json .dumps (checkdict ))#line:413
if __name__ =='__main__':#line:416
    main ()#line:417
