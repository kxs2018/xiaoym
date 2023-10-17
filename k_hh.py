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
    OOOO00O00000OOOOO ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:44
    O0O0O00O0OOO000OO =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OOOO00O00000OOOOO ).json ()#line:45
    return O0O0O00O0OOO000OO #line:46
_OOOOOO0OOO000O0OO =get_msg ()#line:49
try :#line:50
    from lxml import etree #line:51
except :#line:52
    print (_OOOOOO0OOO000O0OO .get ('help')['lxml'])#line:53
if sendable :#line:54
    qwbotkey =os .getenv ('qwbotkey')#line:55
    if not qwbotkey :#line:56
        print (_OOOOOO0OOO000O0OO .get ('help')['qwbotkey'])#line:57
        exit ()#line:58
if pushable :#line:60
    pushconfig =os .getenv ('pushconfig')#line:61
    if not pushconfig :#line:62
        print (_OOOOOO0OOO000O0OO .get ('help')['pushconfig'])#line:63
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
            print (_OOOOOO0OOO000O0OO .get ('help')['pushconfig'])#line:80
            exit ()#line:81
if not pushable and not sendable :#line:82
    print ('啥通知方式都不配置，你想上天吗')#line:83
    exit ()#line:84
def ftime ():#line:87
    O00000OO00O0OOOO0 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:88
    return O00000OO00O0OOOO0 #line:89
def debugger (OO000O00O0000OO0O ):#line:92
    if debug :#line:93
        print (OO000O00O0000OO0O )#line:94
def printlog (O000O0OOO0OOO00OO ):#line:97
    if printf :#line:98
        print (O000O0OOO0OOO00OO )#line:99
def send (OO000000OOO0O000O ,title ='通知',url =None ):#line:102
    if not title or not url :#line:103
        OOO0O0OO00000O000 ={"msgtype":"text","text":{"content":f"{title}\n\n{OO000000OOO0O000O}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:110
    else :#line:111
        OOO0O0OO00000O000 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":OO000000OOO0O000O ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:124
    O0000OOO0OOOO0O00 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:125
    O00OO00000O00000O =requests .post (O0000OOO0OOOO0O00 ,data =json .dumps (OOO0O0OO00000O000 )).json ()#line:126
    if O00OO00000O00000O .get ('errcode')!=0 :#line:127
        print ('消息发送失败，请检查key和发送格式')#line:128
        return False #line:129
    return O00OO00000O00000O #line:130
def push (OOO00OOO00OO00OOO ,title ='通知',url ='',uid =None ):#line:133
    if uid :#line:134
        uids .append (uid )#line:135
    O00OOOOO0O0OOO00O ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',OOO00OOO00OO00OOO ).replace ('url',url )#line:137
    OO0O00OOOO00O00OO ={"appToken":appToken ,"content":O00OOOOO0O0OOO00O ,"summary":title ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:147
    OOOO0O0O00000O000 ='http://wxpusher.zjiecode.com/api/send/message'#line:148
    OO0O0O0O000O00O00 =requests .post (url =OOOO0O0O00000O000 ,json =OO0O00OOOO00O00OO ).json ()#line:149
    if OO0O0O0O000O00O00 .get ('code')!=1000 :#line:150
        print (OO0O0O0O000O00O00 .get ('msg'),OO0O0O0O000O00O00 )#line:151
    return OO0O0O0O000O00O00 #line:152
def getmpinfo (O00O0O00O00OOO0O0 ):#line:155
    if not O00O0O00O00OOO0O0 or O00O0O00O00OOO0O0 =='':#line:156
        return False #line:157
    OOOOO00O0OO00OOOO ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:159
    OOO00O0O0O0O00O00 =requests .get (O00O0O00O00OOO0O0 ,headers =OOOOO00O0OO00OOOO )#line:160
    OOOOOO0O00O0O00O0 =etree .HTML (OOO00O0O0O0O00O00 .text )#line:161
    O000OOOO0OO0OOOO0 =OOOOOO0O00O0O00O0 .xpath ('//meta[@*="og:title"]/@content')#line:163
    if O000OOOO0OO0OOOO0 :#line:164
        O000OOOO0OO0OOOO0 =O000OOOO0OO0OOOO0 [0 ]#line:165
    O0O0OO0000O0O0OOO =OOOOOO0O00O0O00O0 .xpath ('//meta[@*="og:url"]/@content')#line:166
    if O0O0OO0000O0O0OOO :#line:167
        O0O0OO0000O0O0OOO =O0O0OO0000O0O0OOO [0 ].encode ().decode ()#line:168
    try :#line:169
        OO0OOO0O0OO0O0000 =re .findall (r'biz=(.*?)&',O00O0O00O00OOO0O0 )[0 ]#line:170
    except :#line:171
        OO0OOO0O0OO0O0000 =re .findall (r'biz=(.*?)&',O0O0OO0000O0O0OOO )[0 ]#line:172
    if not OO0OOO0O0OO0O0000 :#line:173
        return False #line:174
    OO00OOOO00OO00OOO =OOOOOO0O00O0O00O0 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:175
    if OO00OOOO00OO00OOO :#line:176
        OO00OOOO00OO00OOO =OO00OOOO00OO00OOO [0 ].strip ()#line:177
    O00OO000OOOO0OOO0 =re .findall (r"user_name.DATA'\) : '(.*?)'",OOO00O0O0O0O00O00 .text )or OOOOOO0O00O0O00O0 .xpath ('//span[@class="profile_meta_value"]/text()')#line:179
    if O00OO000OOOO0OOO0 :#line:180
        O00OO000OOOO0OOO0 =O00OO000OOOO0OOO0 [0 ]#line:181
    OOOO0OO0OO0000O0O =re .findall (r'createTime = \'(.*)\'',OOO00O0O0O0O00O00 .text )#line:182
    if OOOO0OO0OO0000O0O :#line:183
        OOOO0OO0OO0000O0O =OOOO0OO0OO0000O0O [0 ][5 :]#line:184
    OO0OOOOOO0OOOO0OO =f'{OOOO0OO0OO0000O0O}|{O000OOOO0OO0OOOO0[:10]}|{OO0OOO0O0OO0O0000}|{OO00OOOO00OO00OOO}'#line:185
    O0O000000OOO0O00O ={'biz':OO0OOO0O0OO0O0000 ,'username':OO00OOOO00OO00OOO ,'text':OO0OOOOOO0OOOO0OO }#line:186
    return O0O000000OOO0O00O #line:187
try :#line:190
    with open ('checkdict.json','r',encoding ='utf-8')as f :#line:191
        checkdict =json .loads (f .read ())#line:192
except :#line:193
    checkdict ={'Mzg2Mzk3Mjk5NQ==':'小鱼儿','MjM5NjU4NTE0MA==':'财事汇','MzkwMjI2ODY5Ng==':'A每日新菜','Mzg3NzEwMzI1Nw==':'A爱玩品牌传奇','MzIyMDg0MzA1OQ==':'服装加工宝','Mzg4NTQ5NDkxMQ==':'秣宝网','Mzk0NjIwNzk0Mg==':'检索宝','MzU3NjA5MDYyMw==':'重庆翊宝智慧电子装置有限公司','MzU1Nzc2ODI0MA==':'星空财研','MzUxMDgxMjMxMw==':'美术宝1对1','MzU4NDMyMTE1MQ==':'海雀Alcidae','MzI4MDE0MzM2NQ==':'强宝时尚','MzA3Nzc5MDMyNg==':'考研红宝书','MjM5Njk5NjYyMQ==':'宝和祥茶业','MzA4NDAyNTQ2MA==':'嘉财万贯','MzIzMjk2MjM5MQ==':'花生酥陪你学','MzkyMDE0NTI2OA==':'重庆市租房宝','MzI0NDI0NzU4OQ==':'九舞文学','MjM5NDAzMjgzNg==':'东风卡车之友'}#line:200
class Allinone :#line:203
    def __init__ (O00O000OO0OOO00OO ,OOOO00O000O0O00O0 ):#line:204
        O00O000OO0OOO00OO .name =OOOO00O000O0O00O0 ['name']#line:205
        O00O000OO0OOO00OO .uid =OOOO00O000O0O00O0 ['uid']#line:206
        O00O000OO0OOO00OO .username =None #line:207
        O00O000OO0OOO00OO .biz =None #line:208
        O00O000OO0OOO00OO .s =requests .session ()#line:209
        O00O000OO0OOO00OO .payload ={"un":OOOO00O000O0O00O0 ['un'],"token":OOOO00O000O0O00O0 ['token'],"pageSize":20 }#line:210
        O00O000OO0OOO00OO .s .headers ={'Accept':'application/json, text/javascript, */*; q=0.01','Content-Type':'application/json; charset=UTF-8','Host':'u.cocozx.cn','Connection':'keep-alive','User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",}#line:216
        O00O000OO0OOO00OO .headers =O00O000OO0OOO00OO .s .headers .copy ()#line:217
        O00O000OO0OOO00OO .msg =''#line:218
    def get_readhost (O00OO00O0OO00O0O0 ):#line:220
        O00000O0O00OO0OOO ="http://u.cocozx.cn/api/user/getReadHost"#line:221
        O0O000OO00000OOOO =O00OO00O0OO00O0O0 .s .post (O00000O0O00OO0OOO ,json =O00OO00O0OO00O0O0 .payload ).json ()#line:222
        debugger (f'readhome {O0O000OO00000OOOO}')#line:223
        O00OO00O0OO00O0O0 .readhost =O0O000OO00000OOOO .get ('result')['host']#line:224
        O00OO00O0OO00O0O0 .headers ['Origin']=O00OO00O0OO00O0O0 .readhost #line:225
        O00OO00O0OO00O0O0 .msg +=f'邀请链接：{O00OO00O0OO00O0O0.readhost}/user/index.html?mid={O00OO00O0OO00O0O0.huid}\n'#line:226
        printlog (f"{O00OO00O0OO00O0O0.name}:邀请链接 {O00OO00O0OO00O0O0.readhost}/user/index.html?mid={O00OO00O0OO00O0O0.huid}")#line:227
    def stataccess (O000000O0OOO000O0 ):#line:229
        OOOO0O0O000OO00OO ='http://u.cocozx.cn/api/user/statAccess'#line:230
        O000000O0OOO000O0 .s .post (OOOO0O0O000OO00OO ,json =O000000O0OOO000O0 .payload ).json ()#line:231
    def get_info (O00OOOO0O00000O00 ):#line:233
        try :#line:234
            OOOO000O0OO000OO0 =O00OOOO0O00000O00 .s .post ("http://u.cocozx.cn/api/user/info",json =O00OOOO0O00000O00 .payload ).json ()#line:235
            OO0OOOOOO0O0000O0 =OOOO000O0OO000OO0 .get ("result")#line:236
            debugger (f'get_info {OOOO000O0OO000OO0}')#line:237
            O0O00000OOO00OO0O =OO0OOOOOO0O0000O0 .get ('us')#line:238
            if O0O00000OOO00OO0O ==2 :#line:239
                O00OOOO0O00000O00 .msg +=f'{O00OOOO0O00000O00.name}已被封\n'#line:240
                printlog (f'{O00OOOO0O00000O00.name}已被封')#line:241
                return False #line:242
            O00OOOO0O00000O00 .msg +=f"""{O00OOOO0O00000O00.name}:今日阅读次数:{OO0OOOOOO0O0000O0["dayCount"]}，当前花儿:{OO0OOOOOO0O0000O0["moneyCurrent"]}，累计阅读次数:{OO0OOOOOO0O0000O0["doneWx"]}\n"""#line:243
            printlog (f"""{O00OOOO0O00000O00.name}:今日阅读次数:{OO0OOOOOO0O0000O0["dayCount"]}，当前花儿:{OO0OOOOOO0O0000O0["moneyCurrent"]}，累计阅读次数:{OO0OOOOOO0O0000O0["doneWx"]}""")#line:245
            OOOOO00OO00000O0O =int (OO0OOOOOO0O0000O0 ["moneyCurrent"])#line:246
            O00OOOO0O00000O00 .huid =OO0OOOOOO0O0000O0 .get ('uid')#line:247
            return OOOOO00OO00000O0O #line:248
        except :#line:249
            return False #line:250
    def psmoneyc (OO000O00O0000O00O ):#line:252
        O0OO00000OO0OOOO0 ={**OO000O00O0000O00O .payload ,**{'mid':OO000O00O0000O00O .huid }}#line:253
        try :#line:254
            OO0O00OO000OO00O0 =OO000O00O0000O00O .s .post ("http://u.cocozx.cn/api/user/psmoneyc",json =O0OO00000OO0OOOO0 ).json ()#line:255
            OO000O00O0000O00O .msg +=f"感谢下级送来的{OO0O00OO000OO00O0['result']['val']}花儿\n"#line:256
            printlog (f"{OO000O00O0000O00O.name}:感谢下级送来的{OO0O00OO000OO00O0['result']['val']}花儿")#line:257
        except :#line:258
            pass #line:259
        return #line:260
    def get_status (OO0O00OOO0OO00OO0 ):#line:262
        O0O0O000000OOOO0O =requests .post ("http://u.cocozx.cn/api/user/read",headers =OO0O00OOO0OO00OO0 .headers ,json =OO0O00OOO0OO00OO0 .payload ).json ()#line:263
        debugger (f'getstatus {O0O0O000000OOOO0O}')#line:264
        OO0O00OOO0OO00OO0 .status =O0O0O000000OOOO0O .get ("result").get ("status")#line:265
        if OO0O00OOO0OO00OO0 .status ==40 :#line:266
            OO0O00OOO0OO00OO0 .msg +="文章还没有准备好\n"#line:267
            printlog (f"{OO0O00OOO0OO00OO0.name}:文章还没有准备好")#line:268
            return #line:269
        elif OO0O00OOO0OO00OO0 .status ==50 :#line:270
            OO0O00OOO0OO00OO0 .msg +="阅读失效\n"#line:271
            printlog (f"{OO0O00OOO0OO00OO0.name}:阅读失效")#line:272
            if OO0O00OOO0OO00OO0 .biz is not None :#line:273
                if checkdict .update ({OO0O00OOO0OO00OO0 .biz :OO0O00OOO0OO00OO0 .username }):#line:274
                    print (f'checkdict添加检测号{OO0O00OOO0OO00OO0.biz}: {OO0O00OOO0OO00OO0.username}')#line:275
            return #line:276
        elif OO0O00OOO0OO00OO0 .status ==60 :#line:277
            OO0O00OOO0OO00OO0 .msg +="已经全部阅读完了\n"#line:278
            printlog (f"{OO0O00OOO0OO00OO0.name}:已经全部阅读完了")#line:279
            return #line:280
        elif OO0O00OOO0OO00OO0 .status ==70 :#line:281
            OO0O00OOO0OO00OO0 .msg +="下一轮还未开启\n"#line:282
            printlog (f"{OO0O00OOO0OO00OO0.name}:下一轮还未开启")#line:283
            return #line:284
        elif OO0O00OOO0OO00OO0 .status ==10 :#line:285
            O0OO00O0OO0O000OO =O0O0O000000OOOO0O ["result"]["url"]#line:286
            OO0O00OOO0OO00OO0 .msg +='-'*50 +"\n阅读链接获取成功\n"#line:287
            return O0OO00O0OO0O000OO #line:288
    def submit (O0OOOO0O0O0O0OO0O ):#line:290
        O0OOO000O0000OOOO ={**{'type':1 },**O0OOOO0O0O0O0OO0O .payload }#line:291
        O0OO0000OOOO0O00O =requests .post ("http://u.cocozx.cn/api/user/submit?zx=&xz=1",headers =O0OOOO0O0O0O0OO0O .headers ,json =O0OOO000O0000OOOO )#line:292
        O0O0O00O00O000OO0 =O0OO0000OOOO0O00O .json ().get ('result')#line:293
        debugger ('submit '+O0OO0000OOOO0O00O .text )#line:294
        O0OOOO0O0O0O0OO0O .msg +=f'阅读成功,获得花儿{O0O0O00O00O000OO0["val"]}，剩余次数:{O0O0O00O00O000OO0["progress"]}\n'#line:295
        printlog (f"{O0OOOO0O0O0O0OO0O.name}:阅读成功,获得花儿{O0O0O00O00O000OO0['val']}，剩余次数:{O0O0O00O00O000OO0['progress']}")#line:296
    def read (O0O0O0OOO0000O00O ):#line:298
        while True :#line:299
            OO00OOO0OO0O0OO0O =O0O0O0OOO0000O00O .get_status ()#line:300
            if not OO00OOO0OO0O0OO0O :#line:301
                if O0O0O0OOO0000O00O .status ==30 :#line:302
                    time .sleep (3 )#line:303
                    continue #line:304
                break #line:305
            O0OO0OO00OOO0O0OO =getmpinfo (OO00OOO0OO0O0OO0O )#line:306
            if not O0OO0OO00OOO0O0OO :#line:307
                printlog (f'{O0O0O0OOO0000O00O.name}:获取文章信息失败，程序中止')#line:308
                return False #line:309
            O0O0O0OOO0000O00O .msg +='开始阅读 '+O0OO0OO00OOO0O0OO ['text']+'\n'#line:310
            printlog (f'{O0O0O0OOO0000O00O.name}:开始阅读 '+O0OO0OO00OOO0O0OO ['text'])#line:311
            OO0O000OO000O00O0 =randint (7 ,10 )#line:312
            if O0OO0OO00OOO0O0OO ['biz']in checkdict .keys ():#line:313
                O0O0O0OOO0000O00O .msg +='当前正在阅读检测文章\n'#line:314
                printlog (f'{O0O0O0OOO0000O00O.name}:正在阅读检测文章')#line:315
                if sendable :#line:316
                    send (O0OO0OO00OOO0O0OO ['text'],f'{O0O0O0OOO0000O00O.name}  花花阅读正在读检测文章',OO00OOO0OO0O0OO0O )#line:317
                if pushable :#line:318
                    push (O0OO0OO00OOO0O0OO ['text'],f'{O0O0O0OOO0000O00O.name}  花花阅读正在读检测文章',OO00OOO0OO0O0OO0O ,O0O0O0OOO0000O00O .uid )#line:319
                time .sleep (60 )#line:320
            time .sleep (OO0O000OO000O00O0 )#line:321
            O0O0O0OOO0000O00O .submit ()#line:322
    def tixian (O0000O0000OO000OO ):#line:324
        global txe #line:325
        OO0OO0OOO0OOOO0OO =O0000O0000OO000OO .get_info ()#line:326
        if OO0OO0OOO0OOOO0OO <txbz :#line:327
            O0000O0000OO000OO .msg +='你的花儿不多了\n'#line:328
            printlog (f'{O0000O0000OO000OO.name}:你的花儿不多了')#line:329
            return False #line:330
        if 10000 <=OO0OO0OOO0OOOO0OO <49999 :#line:331
            txe =10000 #line:332
        elif 5000 <=OO0OO0OOO0OOOO0OO <10000 :#line:333
            txe =5000 #line:334
        elif 3000 <=OO0OO0OOO0OOOO0OO <5000 :#line:335
            txe =3000 #line:336
        elif OO0OO0OOO0OOOO0OO >=50000 :#line:337
            txe =50000 #line:338
        O0000O0000OO000OO .msg +=f"提现金额:{txe}"#line:339
        printlog (f'{O0000O0000OO000OO.name}:提现金额 {txe}')#line:340
        OOO00O0O00OOO00OO ={**O0000O0000OO000OO .payload ,**{"val":txe }}#line:341
        try :#line:342
            O0O0OOOOO0O000OOO =O0000O0000OO000OO .s .post ("http://u.cocozx.cn/api/user/wd",json =OOO00O0O00OOO00OO ).json ()#line:343
            O0000O0000OO000OO .msg +=f"提现结果:{O0O0OOOOO0O000OOO.get('msg')}\n"#line:344
            printlog (f'{O0000O0000OO000OO.name}:提现结果 {O0O0OOOOO0O000OOO.get("msg")}')#line:345
        except :#line:346
            O0000O0000OO000OO .msg +=f"自动提现不成功，发送通知手动提现\n"#line:347
            printlog (f"{O0000O0000OO000OO.name}:自动提现不成功，发送通知手动提现")#line:348
            if sendable :#line:349
                send (f'可提现金额 {int(txe) / 10000}元，点击提现',f'惜之酱提醒您 {O0000O0000OO000OO.name} 花花阅读可以提现了',f'{O0000O0000OO000OO.readhost}/user/index.html?mid=FK73K93DA')#line:351
            if pushable :#line:352
                push (f'可提现金额 {int(txe) / 10000}元，点击提现',f'惜之酱提醒您 {O0000O0000OO000OO.name} 花花阅读可以提现了',f'{O0000O0000OO000OO.readhost}/user/index.html?mid=FK73K93DA',O0000O0000OO000OO .uid )#line:354
    def run (O0OOOOO0O0O0000OO ):#line:356
        if O0OOOOO0O0O0000OO .get_info ():#line:357
            O0OOOOO0O0O0000OO .stataccess ()#line:358
            O0OOOOO0O0O0000OO .get_readhost ()#line:359
            O0OOOOO0O0O0000OO .psmoneyc ()#line:360
            O0OOOOO0O0O0000OO .read ()#line:361
            O0OOOOO0O0O0000OO .tixian ()#line:362
        if not printf :#line:363
            print (O0OOOOO0O0O0000OO .msg .strip ())#line:364
def yd (OO000OO00O0O00OO0 ):#line:367
    while not OO000OO00O0O00OO0 .empty ():#line:368
        O0O000O00O0O00OO0 =OO000OO00O0O00OO0 .get ()#line:369
        try :#line:370
            O0OO000OOOOOO0O0O =Allinone (O0O000O00O0O00OO0 )#line:371
            O0OO000OOOOOO0O0O .run ()#line:372
        except Exception as OO0OO0OO0O0000O00 :#line:373
            print (OO0OO0OO0O0000O00 )#line:374
def get_info ():#line:377
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*20 )#line:379
    print ('入口：http://mr181283238.yxjbhdl.cn/user/index.html?mid=EG5EVNLF3')#line:380
    O00OO0OOO0OO000OO ='V1.4'#line:381
    OO0OOO0O00O000O0O =_OOOOOO0OOO000O0OO ['version']['花花']#line:382
    print (f'当前版本{O00OO0OOO0OO000OO}，仓库版本{OO0OOO0O00O000O0O}\n{_OOOOOO0OOO000O0OO["update_log"]["花花"]}')#line:383
    if O00OO0OOO0OO000OO <OO0OOO0O00O000O0O :#line:384
        print ('请到仓库下载最新版本k_hh.py')#line:385
    return True #line:386
def main ():#line:389
    O000000OOO00O00O0 =get_info ()#line:390
    OOOO0OOO0OOOO0OOO =os .getenv ('hhck')#line:391
    if not OOOO0OOO0OOOO0OOO :#line:392
        OOOO0OOO0OOOO0OOO =os .getenv ('aiock')#line:393
        if not OOOO0OOO0OOOO0OOO :#line:394
            print (_OOOOOO0OOO000O0OO .get ('msg')['花花'])#line:395
            exit ()#line:396
    try :#line:397
        OOOO0OOO0OOOO0OOO =ast .literal_eval (OOOO0OOO0OOOO0OOO )#line:398
    except :#line:399
        pass #line:400
    O0O0O00O0000OO000 =Queue ()#line:401
    OOO00O0OO0OO0O0OO =[]#line:402
    print ('-'*20 )#line:403
    print (f'共获取到{len(OOOO0OOO0OOOO0OOO)}个账号，如与实际不符，请检查ck填写方式')#line:404
    print ("="*25 )#line:405
    if not O000000OOO00O00O0 :#line:406
        exit ()#line:407
    for OO000OO0O0OO00000 ,OOOO0OO0OOO0OOOO0 in enumerate (OOOO0OOO0OOOO0OOO ,start =1 ):#line:408
        O0O0O00O0000OO000 .put (OOOO0OO0OOO0OOOO0 )#line:409
    for OO000OO0O0OO00000 in range (max_workers ):#line:410
        O0O0OOOO0O0O0OO0O =threading .Thread (target =yd ,args =(O0O0O00O0000OO000 ,))#line:411
        O0O0OOOO0O0O0OO0O .start ()#line:412
        OOO00O0OO0OO0O0OO .append (O0O0OOOO0O0O0OO0O )#line:413
        time .sleep (delay_time )#line:414
    for O0OOOO0OO00000OOO in OOO00O0OO0OO0O0OO :#line:415
        O0OOOO0OO00000OOO .join ()#line:416
    with open ('checkdict.json','w',encoding ='utf-8')as O000O00OOO0O0O000 :#line:417
        O000O00OOO0O0O000 .write (json .dumps (checkdict ))#line:418
if __name__ =='__main__':#line:421
    main ()#line:422
