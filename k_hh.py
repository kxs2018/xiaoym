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
    OOO0OOO0OOOO0O0O0 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:44
    O000O000O0O000OO0 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OOO0OOO0OOOO0O0O0 ).json ()#line:45
    return O000O000O0O000OO0 #line:46
_O0OOO0O0O0O00000O =get_msg ()#line:49
try :#line:50
    from lxml import etree #line:51
except :#line:52
    print (_O0OOO0O0O0O00000O .get ('help')['lxml'])#line:53
if sendable :#line:54
    qwbotkey =os .getenv ('qwbotkey')#line:55
    if not qwbotkey :#line:56
        print (_O0OOO0O0O0O00000O .get ('help')['qwbotkey'])#line:57
        exit ()#line:58
if pushable :#line:60
    pushconfig =os .getenv ('pushconfig')#line:61
    if not pushconfig :#line:62
        print (_O0OOO0O0O0O00000O .get ('help')['pushconfig'])#line:63
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
            print (_O0OOO0O0O0O00000O .get ('help')['pushconfig'])#line:80
            exit ()#line:81
if not pushable and not sendable :#line:82
    print ('啥通知方式都不配置，你想上天吗')#line:83
    exit ()#line:84
def ftime ():#line:87
    OOO0O0000OO000OOO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:88
    return OOO0O0000OO000OOO #line:89
def debugger (O0OOOO0OO00OOOO00 ):#line:92
    if debug :#line:93
        print (O0OOOO0OO00OOOO00 )#line:94
def printlog (O00O0000O00000OOO ):#line:97
    if printf :#line:98
        print (O00O0000O00000OOO )#line:99
def send (O0O0O0OO0O000OO00 ,title ='通知',url =None ):#line:102
    if not title or not url :#line:103
        OO00O0O0000OO0O0O ={"msgtype":"text","text":{"content":f"{title}\n\n{O0O0O0OO0O000OO00}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:110
    else :#line:111
        OO00O0O0000OO0O0O ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O0O0O0OO0O000OO00 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:124
    OO00OOOOOOOOOOO00 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:125
    O00000000OO0O00OO =requests .post (OO00OOOOOOOOOOO00 ,data =json .dumps (OO00O0O0000OO0O0O )).json ()#line:126
    if O00000000OO0O00OO .get ('errcode')!=0 :#line:127
        print ('消息发送失败，请检查key和发送格式')#line:128
        return False #line:129
    return O00000000OO0O00OO #line:130
def push (O0O0000OO0000OO00 ,title ='通知',url ='',uid =None ):#line:133
    if uid :#line:134
        uids .append (uid )#line:135
    OO0O000OO0OOO0000 ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',O0O0000OO0000OO00 ).replace ('url',url )#line:137
    O00O000000OO00O0O ={"appToken":appToken ,"content":OO0O000OO0OOO0000 ,"summary":title ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:147
    OO0000O0OO0O0O0O0 ='http://wxpusher.zjiecode.com/api/send/message'#line:148
    OO0OOOO0OOOOO0O0O =requests .post (url =OO0000O0OO0O0O0O0 ,json =O00O000000OO00O0O ).json ()#line:149
    if OO0OOOO0OOOOO0O0O .get ('code')!=1000 :#line:150
        print (OO0OOOO0OOOOO0O0O .get ('msg'),OO0OOOO0OOOOO0O0O )#line:151
    return OO0OOOO0OOOOO0O0O #line:152
def getmpinfo (O0O000O0O0OO000OO ):#line:155
    if not O0O000O0O0OO000OO or O0O000O0O0OO000OO =='':#line:156
        return False #line:157
    OO00O0O00O0O0O0O0 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:159
    O0OOO00OOOO00000O =requests .get (O0O000O0O0OO000OO ,headers =OO00O0O00O0O0O0O0 )#line:160
    OOOOO000OO00OO0OO =etree .HTML (O0OOO00OOOO00000O .text )#line:161
    O0OOOOOO00OO0OOO0 =OOOOO000OO00OO0OO .xpath ('//meta[@*="og:title"]/@content')#line:163
    if O0OOOOOO00OO0OOO0 :#line:164
        O0OOOOOO00OO0OOO0 =O0OOOOOO00OO0OOO0 [0 ]#line:165
    OOO000O0000O0000O =OOOOO000OO00OO0OO .xpath ('//meta[@*="og:url"]/@content')#line:166
    if OOO000O0000O0000O :#line:167
        OOO000O0000O0000O =OOO000O0000O0000O [0 ].encode ().decode ()#line:168
    try :#line:169
        O00OO0O0OOO0OOO0O =re .findall (r'biz=(.*?)&',O0O000O0O0OO000OO )[0 ]#line:170
    except :#line:171
        O00OO0O0OOO0OOO0O =re .findall (r'biz=(.*?)&',OOO000O0000O0000O )[0 ]#line:172
    if not O00OO0O0OOO0OOO0O :#line:173
        return False #line:174
    OOO0OO00000OOOOOO =OOOOO000OO00OO0OO .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:175
    if OOO0OO00000OOOOOO :#line:176
        OOO0OO00000OOOOOO =OOO0OO00000OOOOOO [0 ].strip ()#line:177
    OO0O00OO0OOOO0O00 =re .findall (r"user_name.DATA'\) : '(.*?)'",O0OOO00OOOO00000O .text )or OOOOO000OO00OO0OO .xpath ('//span[@class="profile_meta_value"]/text()')#line:179
    if OO0O00OO0OOOO0O00 :#line:180
        OO0O00OO0OOOO0O00 =OO0O00OO0OOOO0O00 [0 ]#line:181
    OO00OOO0O000O00OO =re .findall (r'createTime = \'(.*)\'',O0OOO00OOOO00000O .text )#line:182
    if OO00OOO0O000O00OO :#line:183
        OO00OOO0O000O00OO =OO00OOO0O000O00OO [0 ][5 :]#line:184
    O0O00OOOO0OO00O0O =f'{OO00OOO0O000O00OO}|{O0OOOOOO00OO0OOO0[:10]}|{O00OO0O0OOO0OOO0O}|{OOO0OO00000OOOOOO}'#line:185
    O00O0000O00OOO0OO ={'biz':O00OO0O0OOO0OOO0O ,'username':OOO0OO00000OOOOOO ,'text':O0O00OOOO0OO00O0O }#line:186
    return O00O0000O00OOO0OO #line:187
try :#line:190
    with open ('checkdict.json','r',encoding ='utf-8')as f :#line:191
        cd_local =json .loads (f .read ())#line:192
except :#line:193
    pass #line:194
checkdict ={'Mzg2Mzk3Mjk5NQ==':'小鱼儿','MjM5NjU4NTE0MA==':'财事汇','MzkwMjI2ODY5Ng==':'A每日新菜','Mzg3NzEwMzI1Nw==':'A爱玩品牌传奇','MzIyMDg0MzA1OQ==':'服装加工宝','Mzg4NTQ5NDkxMQ==':'秣宝网','Mzk0NjIwNzk0Mg==':'检索宝','MzU3NjA5MDYyMw==':'重庆翊宝智慧电子装置有限公司','MzU1Nzc2ODI0MA==':'星空财研','MzUxMDgxMjMxMw==':'美术宝1对1','MzU4NDMyMTE1MQ==':'海雀Alcidae','MzI4MDE0MzM2NQ==':'强宝时尚','MzA3Nzc5MDMyNg==':'考研红宝书','MjM5Njk5NjYyMQ==':'宝和祥茶业','MzA4NDAyNTQ2MA==':'嘉财万贯','MzIzMjk2MjM5MQ==':'花生酥陪你学','MzkyMDE0NTI2OA==':'重庆市租房宝','MzI0NDI0NzU4OQ==':'九舞文学','MjM5NDAzMjgzNg==':'东风卡车之友','MzI1NjUxMTc0Mw==':'爱普生商教投影机','MzIyNzU3NDIwMA==':'川名堂'}#line:202
if cd_local :#line:203
    checkdict ={**checkdict ,**cd_local }#line:204
class Allinone :#line:207
    def __init__ (OO0O0O0O0OO000O00 ,O00000O0O000O00OO ):#line:208
        OO0O0O0O0OO000O00 .name =O00000O0O000O00OO ['name']#line:209
        OO0O0O0O0OO000O00 .uid =O00000O0O000O00OO .get ('uid')#line:210
        OO0O0O0O0OO000O00 .username =None #line:211
        OO0O0O0O0OO000O00 .biz =None #line:212
        OO0O0O0O0OO000O00 .s =requests .session ()#line:213
        OO0O0O0O0OO000O00 .payload ={"un":O00000O0O000O00OO ['un'],"token":O00000O0O000O00OO ['token'],"pageSize":20 }#line:214
        OO0O0O0O0OO000O00 .s .headers ={'Accept':'application/json, text/javascript, */*; q=0.01','Content-Type':'application/json; charset=UTF-8','Host':'u.cocozx.cn','Connection':'keep-alive','User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",}#line:220
        OO0O0O0O0OO000O00 .headers =OO0O0O0O0OO000O00 .s .headers .copy ()#line:221
        OO0O0O0O0OO000O00 .msg =''#line:222
    def get_readhost (O0O000O0OO0OO0O00 ):#line:224
        OO00OOO0OO00O0OOO ="http://u.cocozx.cn/api/user/getReadHost"#line:225
        OOOOOOO000O0OOO00 =O0O000O0OO0OO0O00 .s .post (OO00OOO0OO00O0OOO ,json =O0O000O0OO0OO0O00 .payload ).json ()#line:226
        debugger (f'readhome {OOOOOOO000O0OOO00}')#line:227
        O0O000O0OO0OO0O00 .readhost =OOOOOOO000O0OOO00 .get ('result')['host']#line:228
        O0O000O0OO0OO0O00 .headers ['Origin']=O0O000O0OO0OO0O00 .readhost #line:229
        O0O000O0OO0OO0O00 .msg +=f'邀请链接：{O0O000O0OO0OO0O00.readhost}/user/index.html?mid={O0O000O0OO0OO0O00.huid}\n'#line:230
        printlog (f"{O0O000O0OO0OO0O00.name}:邀请链接 {O0O000O0OO0OO0O00.readhost}/user/index.html?mid={O0O000O0OO0OO0O00.huid}")#line:231
    def stataccess (O00OOOOO00O00O0O0 ):#line:233
        O0O000OO0OOOOOO0O ='http://u.cocozx.cn/api/user/statAccess'#line:234
        O00OOOOO00O00O0O0 .s .post (O0O000OO0OOOOOO0O ,json =O00OOOOO00O00O0O0 .payload ).json ()#line:235
    def get_info (O0OO0OOO00O00000O ):#line:237
        try :#line:238
            O0OO00O0O00O0OOO0 =O0OO0OOO00O00000O .s .post ("http://u.cocozx.cn/api/user/info",json =O0OO0OOO00O00000O .payload ).json ()#line:239
            OO0OO0O000OO00OOO =O0OO00O0O00O0OOO0 .get ("result")#line:240
            debugger (f'get_info {O0OO00O0O00O0OOO0}')#line:241
            O00O0OOOO0O0O0O00 =OO0OO0O000OO00OOO .get ('us')#line:242
            if O00O0OOOO0O0O0O00 ==2 :#line:243
                O0OO0OOO00O00000O .msg +=f'{O0OO0OOO00O00000O.name}已被封\n'#line:244
                printlog (f'{O0OO0OOO00O00000O.name}已被封')#line:245
                return False #line:246
            O0OO0OOO00O00000O .msg +=f"""{O0OO0OOO00O00000O.name}:今日阅读次数:{OO0OO0O000OO00OOO["dayCount"]}，当前花儿:{OO0OO0O000OO00OOO["moneyCurrent"]}，累计阅读次数:{OO0OO0O000OO00OOO["doneWx"]}\n"""#line:247
            printlog (f"""{O0OO0OOO00O00000O.name}:今日阅读次数:{OO0OO0O000OO00OOO["dayCount"]}，当前花儿:{OO0OO0O000OO00OOO["moneyCurrent"]}，累计阅读次数:{OO0OO0O000OO00OOO["doneWx"]}""")#line:249
            OOOOO00O0OOOO0OO0 =int (OO0OO0O000OO00OOO ["moneyCurrent"])#line:250
            O0OO0OOO00O00000O .huid =OO0OO0O000OO00OOO .get ('uid')#line:251
            return OOOOO00O0OOOO0OO0 #line:252
        except :#line:253
            return False #line:254
    def psmoneyc (OO0OO00O0O000OO00 ):#line:256
        O0OO00O0OOO00O00O ={**OO0OO00O0O000OO00 .payload ,**{'mid':OO0OO00O0O000OO00 .huid }}#line:257
        try :#line:258
            OOOO000000O00OOO0 =OO0OO00O0O000OO00 .s .post ("http://u.cocozx.cn/api/user/psmoneyc",json =O0OO00O0OOO00O00O ).json ()#line:259
            OO0OO00O0O000OO00 .msg +=f"感谢下级送来的{OOOO000000O00OOO0['result']['val']}花儿\n"#line:260
            printlog (f"{OO0OO00O0O000OO00.name}:感谢下级送来的{OOOO000000O00OOO0['result']['val']}花儿")#line:261
        except :#line:262
            pass #line:263
        return #line:264
    def get_status (OOOO000OO0OOO00O0 ):#line:266
        OOOOO0O000O00OO0O =requests .post ("http://u.cocozx.cn/api/user/read",headers =OOOO000OO0OOO00O0 .headers ,json =OOOO000OO0OOO00O0 .payload ).json ()#line:267
        debugger (f'getstatus {OOOOO0O000O00OO0O}')#line:268
        OOOO000OO0OOO00O0 .status =OOOOO0O000O00OO0O .get ("result").get ("status")#line:269
        if OOOO000OO0OOO00O0 .status ==40 :#line:270
            OOOO000OO0OOO00O0 .msg +="文章还没有准备好\n"#line:271
            printlog (f"{OOOO000OO0OOO00O0.name}:文章还没有准备好")#line:272
            return #line:273
        elif OOOO000OO0OOO00O0 .status ==50 :#line:274
            OOOO000OO0OOO00O0 .msg +="阅读失效\n"#line:275
            printlog (f"{OOOO000OO0OOO00O0.name}:阅读失效")#line:276
            if OOOO000OO0OOO00O0 .biz is not None :#line:277
                if checkdict .update ({OOOO000OO0OOO00O0 .biz :OOOO000OO0OOO00O0 .username }):#line:278
                    print (f'checkdict添加检测号{OOOO000OO0OOO00O0.biz}: {OOOO000OO0OOO00O0.username}')#line:279
            return #line:280
        elif OOOO000OO0OOO00O0 .status ==60 :#line:281
            OOOO000OO0OOO00O0 .msg +="已经全部阅读完了\n"#line:282
            printlog (f"{OOOO000OO0OOO00O0.name}:已经全部阅读完了")#line:283
            return #line:284
        elif OOOO000OO0OOO00O0 .status ==70 :#line:285
            OOOO000OO0OOO00O0 .msg +="下一轮还未开启\n"#line:286
            printlog (f"{OOOO000OO0OOO00O0.name}:下一轮还未开启")#line:287
            return #line:288
        elif OOOO000OO0OOO00O0 .status ==10 :#line:289
            OOO0O00OOOOOO0OOO =OOOOO0O000O00OO0O ["result"]["url"]#line:290
            OOOO000OO0OOO00O0 .msg +='-'*50 +"\n阅读链接获取成功\n"#line:291
            return OOO0O00OOOOOO0OOO #line:292
    def submit (O0O0OOO00O0O00O00 ):#line:294
        OO0O0O00O0000OO0O ={**{'type':1 },**O0O0OOO00O0O00O00 .payload }#line:295
        O00O000OO0OOO00OO =requests .post ("http://u.cocozx.cn/api/user/submit?zx=&xz=1",headers =O0O0OOO00O0O00O00 .headers ,json =OO0O0O00O0000OO0O )#line:296
        OOO00000O0000OO0O =O00O000OO0OOO00OO .json ().get ('result')#line:297
        debugger ('submit '+O00O000OO0OOO00OO .text )#line:298
        O0O0OOO00O0O00O00 .msg +=f'阅读成功,获得花儿{OOO00000O0000OO0O["val"]}，剩余次数:{OOO00000O0000OO0O["progress"]}\n'#line:299
        printlog (f"{O0O0OOO00O0O00O00.name}:阅读成功,获得花儿{OOO00000O0000OO0O['val']}，剩余次数:{OOO00000O0000OO0O['progress']}")#line:300
    def read (OO00OOOOO0000O00O ):#line:302
        while True :#line:303
            O00000OOO00O00O00 =OO00OOOOO0000O00O .get_status ()#line:304
            if not O00000OOO00O00O00 :#line:305
                if OO00OOOOO0000O00O .status ==30 :#line:306
                    time .sleep (3 )#line:307
                    continue #line:308
                break #line:309
            OO00OO000000OO0OO =getmpinfo (O00000OOO00O00O00 )#line:310
            if not OO00OO000000OO0OO :#line:311
                printlog (f'{OO00OOOOO0000O00O.name}:获取文章信息失败，程序中止')#line:312
                return False #line:313
            OO00OOOOO0000O00O .msg +='开始阅读 '+OO00OO000000OO0OO ['text']+'\n'#line:314
            OO00OOOOO0000O00O .username =OO00OO000000OO0OO ['username']#line:315
            OO00OOOOO0000O00O .biz =OO00OO000000OO0OO ['biz']#line:316
            printlog (f'{OO00OOOOO0000O00O.name}:开始阅读 '+OO00OO000000OO0OO ['text'])#line:317
            O0OOOOO000000OOOO =randint (7 ,10 )#line:318
            if OO00OOOOO0000O00O .biz in checkdict .keys ():#line:319
                OO00OOOOO0000O00O .msg +='当前正在阅读检测文章\n'#line:320
                printlog (f'{OO00OOOOO0000O00O.name}:正在阅读检测文章')#line:321
                if sendable :#line:322
                    send (OO00OO000000OO0OO ['text'],f'{OO00OOOOO0000O00O.name}  花花阅读正在读检测文章',O00000OOO00O00O00 )#line:323
                if pushable :#line:324
                    push (f'【{OO00OOOOO0000O00O.name}】\n点击阅读检测文章\n{OO00OO000000OO0OO["text"]}',f'【{OO00OOOOO0000O00O.name}】 花花过检测',O00000OOO00O00O00 ,OO00OOOOO0000O00O .uid )#line:326
                time .sleep (60 )#line:327
            time .sleep (O0OOOOO000000OOOO )#line:328
            OO00OOOOO0000O00O .submit ()#line:329
    def tixian (O0OO0O0OO0O000O00 ):#line:331
        global txe #line:332
        O0O000O00O00OOOOO =O0OO0O0OO0O000O00 .get_info ()#line:333
        if O0O000O00O00OOOOO <txbz :#line:334
            O0OO0O0OO0O000O00 .msg +='你的花儿不多了\n'#line:335
            printlog (f'{O0OO0O0OO0O000O00.name}:你的花儿不多了')#line:336
            return False #line:337
        if 10000 <=O0O000O00O00OOOOO <49999 :#line:338
            txe =10000 #line:339
        elif 5000 <=O0O000O00O00OOOOO <10000 :#line:340
            txe =5000 #line:341
        elif 3000 <=O0O000O00O00OOOOO <5000 :#line:342
            txe =3000 #line:343
        elif O0O000O00O00OOOOO >=50000 :#line:344
            txe =50000 #line:345
        O0OO0O0OO0O000O00 .msg +=f"提现金额:{txe}"#line:346
        printlog (f'{O0OO0O0OO0O000O00.name}:提现金额 {txe}')#line:347
        OOO0OO0OO0O0O0O00 ={**O0OO0O0OO0O000O00 .payload ,**{"val":txe }}#line:348
        try :#line:349
            O00O0O0OOOOO0OOOO =O0OO0O0OO0O000O00 .s .post ("http://u.cocozx.cn/api/user/wd",json =OOO0OO0OO0O0O0O00 ).json ()#line:350
            O0OO0O0OO0O000O00 .msg +=f"提现结果:{O00O0O0OOOOO0OOOO.get('msg')}\n"#line:351
            printlog (f'{O0OO0O0OO0O000O00.name}:提现结果 {O00O0O0OOOOO0OOOO.get("msg")}')#line:352
        except :#line:353
            O0OO0O0OO0O000O00 .msg +=f"自动提现不成功，发送通知手动提现\n"#line:354
            printlog (f"{O0OO0O0OO0O000O00.name}:自动提现不成功，发送通知手动提现")#line:355
            if sendable :#line:356
                send (f'可提现金额 {int(txe) / 10000}元，点击提现',f'惜之酱提醒您 {O0OO0O0OO0O000O00.name} 花花阅读可以提现了',f'{O0OO0O0OO0O000O00.readhost}/user/index.html?mid=FK73K93DA')#line:358
            if pushable :#line:359
                push (f'可提现金额 {int(txe) / 10000}元，点击提现',f'惜之酱提醒您 {O0OO0O0OO0O000O00.name} 花花阅读可以提现了',f'{O0OO0O0OO0O000O00.readhost}/user/index.html?mid=FK73K93DA',O0OO0O0OO0O000O00 .uid )#line:361
    def run (O0O00O000O0O0O0OO ):#line:363
        if O0O00O000O0O0O0OO .get_info ():#line:364
            O0O00O000O0O0O0OO .stataccess ()#line:365
            O0O00O000O0O0O0OO .get_readhost ()#line:366
            O0O00O000O0O0O0OO .psmoneyc ()#line:367
            O0O00O000O0O0O0OO .read ()#line:368
            O0O00O000O0O0O0OO .tixian ()#line:369
        if not printf :#line:370
            print (O0O00O000O0O0O0OO .msg .strip ())#line:371
def yd (OOOO00OO0OOOOO0O0 ):#line:374
    while not OOOO00OO0OOOOO0O0 .empty ():#line:375
        OO00O0OO00OOO0O0O =OOOO00OO0OOOOO0O0 .get ()#line:376
        try :#line:377
            O0OOO00OOO000OO00 =Allinone (OO00O0OO00OOO0O0O )#line:378
            O0OOO00OOO000OO00 .run ()#line:379
        except Exception as O00OO0OOOOOO0OO00 :#line:380
            print (O00OO0OOOOOO0OO00 )#line:381
def get_info ():#line:384
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*20 )#line:386
    print ('入口：http://mr181283238.yxjbhdl.cn/user/index.html?mid=EG5EVNLF3')#line:387
    OO0OOO0000O0OOOOO ='V1.4'#line:388
    OOOO0O00OO00000OO =_O0OOO0O0O0O00000O ['version']['花花']#line:389
    print (f'当前版本{OO0OOO0000O0OOOOO}，仓库版本{OOOO0O00OO00000OO}\n{_O0OOO0O0O0O00000O["update_log"]["花花"]}')#line:390
    if OO0OOO0000O0OOOOO <OOOO0O00OO00000OO :#line:391
        print ('请到仓库下载最新版本k_hh.py')#line:392
    return True #line:393
def main ():#line:396
    O000O0OOO00O000O0 =get_info ()#line:397
    O00O0O000O0000000 =os .getenv ('hhck')#line:398
    if not O00O0O000O0000000 :#line:399
        O00O0O000O0000000 =os .getenv ('aiock')#line:400
        if not O00O0O000O0000000 :#line:401
            print (_O0OOO0O0O0O00000O .get ('msg')['花花'])#line:402
            exit ()#line:403
    try :#line:404
        O00O0O000O0000000 =ast .literal_eval (O00O0O000O0000000 )#line:405
    except :#line:406
        pass #line:407
    O0000OO0O0OOOO000 =Queue ()#line:408
    OO00O00OO00OOOO00 =[]#line:409
    print ('-'*20 )#line:410
    print (f'共获取到{len(O00O0O000O0000000)}个账号，如与实际不符，请检查ck填写方式')#line:411
    print ("="*25 )#line:412
    if not O000O0OOO00O000O0 :#line:413
        exit ()#line:414
    for OOO00OOO0OO0OOOOO ,OO00O00OOO0OO0000 in enumerate (O00O0O000O0000000 ,start =1 ):#line:415
        O0000OO0O0OOOO000 .put (OO00O00OOO0OO0000 )#line:416
    for OOO00OOO0OO0OOOOO in range (max_workers ):#line:417
        O0O0000O0O000O0O0 =threading .Thread (target =yd ,args =(O0000OO0O0OOOO000 ,))#line:418
        O0O0000O0O000O0O0 .start ()#line:419
        OO00O00OO00OOOO00 .append (O0O0000O0O000O0O0 )#line:420
        time .sleep (delay_time )#line:421
    for OOO0000O0O0O0OO00 in OO00O00OO00OOOO00 :#line:422
        OOO0000O0O0O0OO00 .join ()#line:423
    with open ('checkdict.json','w',encoding ='utf-8')as OO0O0O0O0000O000O :#line:424
        OO0O0O0O0000O000O .write (json .dumps (checkdict ))#line:425
if __name__ =='__main__':#line:428
    main ()#line:429
