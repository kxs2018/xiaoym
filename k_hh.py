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
def get_msg ():#line:43
    O0000OO0O0OOO0OO0 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:45
    OOOOO000OO00000OO =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O0000OO0O0OOO0OO0 ).json ()#line:46
    return OOOOO000OO00000OO #line:47
_O00000000OO00O000 =get_msg ()#line:50
try :#line:51
    from lxml import etree #line:52
except :#line:53
    print (_O00000000OO00O000 .get ('help')['lxml'])#line:54
if sendable :#line:55
    qwbotkey =os .getenv ('qwbotkey')#line:56
    if not qwbotkey :#line:57
        print (_O00000000OO00O000 .get ('help')['qwbotkey'])#line:58
        exit ()#line:59
if pushable :#line:61
    pushconfig =os .getenv ('pushconfig')#line:62
    if not pushconfig :#line:63
        print (_O00000000OO00O000 .get ('help')['pushconfig'])#line:64
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
            print (_O00000000OO00O000 .get ('help')['pushconfig'])#line:81
            exit ()#line:82
if not pushable and not sendable :#line:83
    print ('啥通知方式都不配置，你想上天吗')#line:84
    exit ()#line:85
def ftime ():#line:88
    O0000OO0OOO0O0O0O =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:89
    return O0000OO0OOO0O0O0O #line:90
def debugger (O00OOOO00OO0000OO ):#line:93
    if debug :#line:94
        print (O00OOOO00OO0000OO )#line:95
def printlog (O00000O0000O0O0O0 ):#line:98
    if printf :#line:99
        print (O00000O0000O0O0O0 )#line:100
def send (O00O0OOO00OO0O0O0 ,title ='通知',url =None ):#line:103
    if not title or not url :#line:104
        O0O0O00O00O00O00O ={"msgtype":"text","text":{"content":f"{title}\n\n{O00O0OOO00OO0O0O0}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:111
    else :#line:112
        O0O0O00O00O00O00O ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O00O0OOO00OO0O0O0 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:125
    O0OO000O00000OOOO =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:126
    O0OO0O0O000OO00OO =requests .post (O0OO000O00000OOOO ,data =json .dumps (O0O0O00O00O00O00O )).json ()#line:127
    if O0OO0O0O000OO00OO .get ('errcode')!=0 :#line:128
        print ('消息发送失败，请检查key和发送格式')#line:129
        return False #line:130
    return O0OO0O0O000OO00OO #line:131
def push (O000OOO0OO00OOO0O ,title ='通知',url ='',uid =None ):#line:134
    if uid :#line:135
        uids .append (uid )#line:136
    O00OO0O0O00OO0OO0 ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',O000OOO0OO00OOO0O ).replace ('url',url )#line:138
    OOO000OOOOO00O000 ={"appToken":appToken ,"content":O00OO0O0O00OO0OO0 ,"summary":title ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:148
    OO00O0O0O0OOOOO00 ='http://wxpusher.zjiecode.com/api/send/message'#line:149
    OO0O0O0O000000OOO =requests .post (url =OO00O0O0O0OOOOO00 ,json =OOO000OOOOO00O000 ).json ()#line:150
    if OO0O0O0O000000OOO .get ('code')!=1000 :#line:151
        print (OO0O0O0O000000OOO .get ('msg'),OO0O0O0O000000OOO )#line:152
    return OO0O0O0O000000OOO #line:153
def getmpinfo (OOO0OOO0OOOOO0O00 ):#line:156
    if not OOO0OOO0OOOOO0O00 or OOO0OOO0OOOOO0O00 =='':#line:157
        return False #line:158
    O00O0O000000O0OOO ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:160
    OO00O0O00000O00OO =requests .get (OOO0OOO0OOOOO0O00 ,headers =O00O0O000000O0OOO )#line:161
    OO00OOOO000OOOO00 =etree .HTML (OO00O0O00000O00OO .text )#line:162
    O0OO00O00OO00OO00 =OO00OOOO000OOOO00 .xpath ('//meta[@*="og:title"]/@content')#line:164
    if O0OO00O00OO00OO00 :#line:165
        O0OO00O00OO00OO00 =O0OO00O00OO00OO00 [0 ]#line:166
    OO0OOO0O00OOO0OO0 =OO00OOOO000OOOO00 .xpath ('//meta[@*="og:url"]/@content')#line:167
    if OO0OOO0O00OOO0OO0 :#line:168
        OO0OOO0O00OOO0OO0 =OO0OOO0O00OOO0OO0 [0 ].encode ().decode ()#line:169
    try :#line:170
        O0OO000O00OOOO0OO =re .findall (r'biz=(.*?)&',OOO0OOO0OOOOO0O00 )[0 ]#line:171
    except :#line:172
        O0OO000O00OOOO0OO =re .findall (r'biz=(.*?)&',OO0OOO0O00OOO0OO0 )[0 ]#line:173
    if not O0OO000O00OOOO0OO :#line:174
        return False #line:175
    O00000000OO000OO0 =OO00OOOO000OOOO00 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:176
    if O00000000OO000OO0 :#line:177
        O00000000OO000OO0 =O00000000OO000OO0 [0 ].strip ()#line:178
    O0O0OO000OO0OOO0O =re .findall (r"user_name.DATA'\) : '(.*?)'",OO00O0O00000O00OO .text )or OO00OOOO000OOOO00 .xpath ('//span[@class="profile_meta_value"]/text()')#line:180
    if O0O0OO000OO0OOO0O :#line:181
        O0O0OO000OO0OOO0O =O0O0OO000OO0OOO0O [0 ]#line:182
    OOO0OOOO0O0O00OO0 =re .findall (r'createTime = \'(.*)\'',OO00O0O00000O00OO .text )#line:183
    if OOO0OOOO0O0O00OO0 :#line:184
        OOO0OOOO0O0O00OO0 =OOO0OOOO0O0O00OO0 [0 ][5 :]#line:185
    O0OO0O000OOO00O0O =f'{OOO0OOOO0O0O00OO0}|{O0OO00O00OO00OO00[:10]}|{O0OO000O00OOOO0OO}|{O00000000OO000OO0}'#line:186
    O00OO00000O0O000O ={'biz':O0OO000O00OOOO0OO ,'username':O00000000OO000OO0 ,'text':O0OO0O000OOO00O0O }#line:187
    return O00OO00000O0O000O #line:188
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
    def __init__ (OO0OO0O00O0O000O0 ,OO00O0OO00OOO0OOO ):#line:212
        OO0OO0O00O0O000O0 .name =OO00O0OO00OOO0OOO ['name']#line:213
        OO0OO0O00O0O000O0 .uid =OO00O0OO00OOO0OOO .get ('uid')#line:214
        OO0OO0O00O0O000O0 .username =None #line:215
        OO0OO0O00O0O000O0 .biz =None #line:216
        OO0OO0O00O0O000O0 .s =requests .session ()#line:217
        OO0OO0O00O0O000O0 .payload ={"un":OO00O0OO00OOO0OOO ['un'],"token":OO00O0OO00OOO0OOO ['token'],"pageSize":20 }#line:218
        OO0OO0O00O0O000O0 .s .headers ={'Accept':'application/json, text/javascript, */*; q=0.01','Content-Type':'application/json; charset=UTF-8','Host':'u.cocozx.cn','Connection':'keep-alive','User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",}#line:224
        OO0OO0O00O0O000O0 .headers =OO0OO0O00O0O000O0 .s .headers .copy ()#line:225
        OO0OO0O00O0O000O0 .msg =''#line:226
    def get_readhost (OO0O000000000000O ):#line:228
        O0O0O0O00000O0OO0 ="http://u.cocozx.cn/api/user/getReadHost"#line:229
        OO00O00OO000O00OO =OO0O000000000000O .s .post (O0O0O0O00000O0OO0 ,json =OO0O000000000000O .payload ).json ()#line:230
        debugger (f'readhome {OO00O00OO000O00OO}')#line:231
        OO0O000000000000O .readhost =OO00O00OO000O00OO .get ('result')['host']#line:232
        OO0O000000000000O .headers ['Origin']=OO0O000000000000O .readhost #line:233
        OO0O000000000000O .msg +=f'邀请链接：{OO0O000000000000O.readhost}/user/index.html?mid={OO0O000000000000O.huid}\n'#line:234
        printlog (f"{OO0O000000000000O.name}:邀请链接 {OO0O000000000000O.readhost}/user/index.html?mid={OO0O000000000000O.huid}")#line:235
    def stataccess (OOOO0O0O00O00OO00 ):#line:237
        O00OO00OO0O0OOOO0 ='http://u.cocozx.cn/api/user/statAccess'#line:238
        OOOO0O0O00O00OO00 .s .post (O00OO00OO0O0OOOO0 ,json =OOOO0O0O00O00OO00 .payload ).json ()#line:239
    def get_info (OO00000O0O000OO0O ):#line:241
        try :#line:242
            O0O000OOOOO0OOOO0 =OO00000O0O000OO0O .s .post ("http://u.cocozx.cn/api/user/info",json =OO00000O0O000OO0O .payload ).json ()#line:243
            O00O0O00O0O00000O =O0O000OOOOO0OOOO0 .get ("result")#line:244
            debugger (f'get_info {O0O000OOOOO0OOOO0}')#line:245
            O000OOO000OOOO000 =O00O0O00O0O00000O .get ('us')#line:246
            if O000OOO000OOOO000 ==2 :#line:247
                OO00000O0O000OO0O .msg +=f'{OO00000O0O000OO0O.name}已被封\n'#line:248
                printlog (f'{OO00000O0O000OO0O.name}已被封')#line:249
                return False #line:250
            OO00000O0O000OO0O .msg +=f"""{OO00000O0O000OO0O.name}:今日阅读次数:{O00O0O00O0O00000O["dayCount"]}，当前花儿:{O00O0O00O0O00000O["moneyCurrent"]}\n"""#line:251
            printlog (f"""{OO00000O0O000OO0O.name}:今日阅读次数:{O00O0O00O0O00000O["dayCount"]}，当前花儿:{O00O0O00O0O00000O["moneyCurrent"]}""")#line:253
            O00O0OO00O0O0OOOO =int (O00O0O00O0O00000O ["moneyCurrent"])#line:254
            OO00000O0O000OO0O .huid =O00O0O00O0O00000O .get ('uid')#line:255
            return O00O0OO00O0O0OOOO #line:256
        except :#line:257
            return False #line:258
    def psmoneyc (OOO00OOO0OO0OOO0O ):#line:260
        OO0O00OOOO0O00OO0 ={**OOO00OOO0OO0OOO0O .payload ,**{'mid':OOO00OOO0OO0OOO0O .huid }}#line:261
        try :#line:262
            OOO000OO0000O0OO0 =OOO00OOO0OO0OOO0O .s .post ("http://u.cocozx.cn/api/user/psmoneyc",json =OO0O00OOOO0O00OO0 ).json ()#line:263
            OOO00OOO0OO0OOO0O .msg +=f"感谢下级送来的{OOO000OO0000O0OO0['result']['val']}花儿\n"#line:264
            printlog (f"{OOO00OOO0OO0OOO0O.name}:感谢下级送来的{OOO000OO0000O0OO0['result']['val']}花儿")#line:265
        except :#line:266
            pass #line:267
        return #line:268
    def get_status (O0OO0000000O000O0 ):#line:270
        OO0O0OO0O000OO0O0 =requests .post ("http://u.cocozx.cn/api/user/read",headers =O0OO0000000O000O0 .headers ,json =O0OO0000000O000O0 .payload ).json ()#line:271
        debugger (f'getstatus {OO0O0OO0O000OO0O0}')#line:272
        O0OO0000000O000O0 .status =OO0O0OO0O000OO0O0 .get ("result").get ("status")#line:273
        if O0OO0000000O000O0 .status ==40 :#line:274
            O0OO0000000O000O0 .msg +="文章还没有准备好\n"#line:275
            printlog (f"{O0OO0000000O000O0.name}:文章还没有准备好")#line:276
            return #line:277
        elif O0OO0000000O000O0 .status ==50 :#line:278
            O0OO0000000O000O0 .msg +="阅读失效\n"#line:279
            printlog (f"{O0OO0000000O000O0.name}:阅读失效")#line:280
            if O0OO0000000O000O0 .biz is not None :#line:281
                if checkdict .update ({O0OO0000000O000O0 .biz :O0OO0000000O000O0 .username }):#line:282
                    print (f'checkdict添加检测号{O0OO0000000O000O0.biz}: {O0OO0000000O000O0.username}')#line:283
            return #line:284
        elif O0OO0000000O000O0 .status ==60 :#line:285
            O0OO0000000O000O0 .msg +="已经全部阅读完了\n"#line:286
            printlog (f"{O0OO0000000O000O0.name}:已经全部阅读完了")#line:287
            return #line:288
        elif O0OO0000000O000O0 .status ==70 :#line:289
            O0OO0000000O000O0 .msg +="下一轮还未开启\n"#line:290
            printlog (f"{O0OO0000000O000O0.name}:下一轮还未开启")#line:291
            return #line:292
        elif O0OO0000000O000O0 .status ==10 :#line:293
            O0OOO0OOO00O0OOOO =OO0O0OO0O000OO0O0 ["result"]["url"]#line:294
            O0OO0000000O000O0 .msg +='-'*50 +"\n阅读链接获取成功\n"#line:295
            return O0OOO0OOO00O0OOOO #line:296
    def submit (OO0OOO000000000OO ):#line:298
        O0OO00O00OO0O00OO ={**{'type':1 },**OO0OOO000000000OO .payload }#line:299
        O00O000O00OO00000 =requests .post ("http://u.cocozx.cn/api/user/submit?zx=&xz=1",headers =OO0OOO000000000OO .headers ,json =O0OO00O00OO0O00OO )#line:300
        OOO0O000O0OOO00OO =O00O000O00OO00000 .json ().get ('result')#line:301
        debugger ('submit '+O00O000O00OO00000 .text )#line:302
        OO0OOO000000000OO .msg +=f'阅读成功,获得花儿{OOO0O000O0OOO00OO["val"]}，剩余次数:{OOO0O000O0OOO00OO["progress"]}\n'#line:303
        printlog (f"{OO0OOO000000000OO.name}:阅读成功,获得花儿{OOO0O000O0OOO00OO['val']}，剩余次数:{OOO0O000O0OOO00OO['progress']}")#line:304
    def read (OO0OO00OOOO00OO00 ):#line:306
        while True :#line:307
            OO0000OOOO00O0O00 =OO0OO00OOOO00OO00 .get_status ()#line:308
            if not OO0000OOOO00O0O00 :#line:309
                if OO0OO00OOOO00OO00 .status ==30 :#line:310
                    time .sleep (3 )#line:311
                    continue #line:312
                break #line:313
            O00OO0OO000OOO0O0 =getmpinfo (OO0000OOOO00O0O00 )#line:314
            if not O00OO0OO000OOO0O0 :#line:315
                printlog (f'{OO0OO00OOOO00OO00.name}:获取文章信息失败，程序中止')#line:316
                return False #line:317
            OO0OO00OOOO00OO00 .msg +='开始阅读 '+O00OO0OO000OOO0O0 ['text']+'\n'#line:318
            OO0OO00OOOO00OO00 .username =O00OO0OO000OOO0O0 ['username']#line:319
            OO0OO00OOOO00OO00 .biz =O00OO0OO000OOO0O0 ['biz']#line:320
            printlog (f'{OO0OO00OOOO00OO00.name}:开始阅读 '+O00OO0OO000OOO0O0 ['text'])#line:321
            OO0O0OO00O00000O0 =randint (7 ,10 )#line:322
            if OO0OO00OOOO00OO00 .biz in checkdict .keys ():#line:323
                OO0OO00OOOO00OO00 .msg +='当前正在阅读检测文章\n'#line:324
                printlog (f'{OO0OO00OOOO00OO00.name}:正在阅读检测文章')#line:325
                if sendable :#line:326
                    send (O00OO0OO000OOO0O0 ['text'],f'{OO0OO00OOOO00OO00.name}  花花阅读正在读检测文章',OO0000OOOO00O0O00 )#line:327
                if pushable :#line:328
                    push (f'【{OO0OO00OOOO00OO00.name}】\n点击阅读检测文章\n{O00OO0OO000OOO0O0["text"]}',f'【{OO0OO00OOOO00OO00.name}】 花花过检测',OO0000OOOO00O0O00 ,OO0OO00OOOO00OO00 .uid )#line:330
                time .sleep (60 )#line:331
            time .sleep (OO0O0OO00O00000O0 )#line:332
            OO0OO00OOOO00OO00 .submit ()#line:333
    def tixian (OOO0000O0OOO00O0O ):#line:335
        global txe #line:336
        OOOOOO0OO00O0OOOO =OOO0000O0OOO00O0O .get_info ()#line:337
        if OOOOOO0OO00O0OOOO <txbz :#line:338
            OOO0000O0OOO00O0O .msg +='你的花儿不多了\n'#line:339
            printlog (f'{OOO0000O0OOO00O0O.name}:你的花儿不多了')#line:340
            return False #line:341
        if 10000 <=OOOOOO0OO00O0OOOO <49999 :#line:342
            txe =10000 #line:343
        elif 5000 <=OOOOOO0OO00O0OOOO <10000 :#line:344
            txe =5000 #line:345
        elif 3000 <=OOOOOO0OO00O0OOOO <5000 :#line:346
            txe =3000 #line:347
        elif OOOOOO0OO00O0OOOO >=50000 :#line:348
            txe =50000 #line:349
        OOO0000O0OOO00O0O .msg +=f"提现金额:{txe}"#line:350
        printlog (f'{OOO0000O0OOO00O0O.name}:提现金额 {txe}')#line:351
        OO0O0O0OOO00O00O0 ={**OOO0000O0OOO00O0O .payload ,**{"val":txe }}#line:352
        try :#line:353
            O0000O0O0O00O0O00 =OOO0000O0OOO00O0O .s .post ("http://u.cocozx.cn/api/user/wd",json =OO0O0O0OOO00O00O0 ).json ()#line:354
            OOO0000O0OOO00O0O .msg +=f"提现结果:{O0000O0O0O00O0O00.get('msg')}\n"#line:355
            printlog (f'{OOO0000O0OOO00O0O.name}:提现结果 {O0000O0O0O00O0O00.get("msg")}')#line:356
        except :#line:357
            OOO0000O0OOO00O0O .msg +=f"自动提现不成功，发送通知手动提现\n"#line:358
            printlog (f"{OOO0000O0OOO00O0O.name}:自动提现不成功，发送通知手动提现")#line:359
            if sendable :#line:360
                send (f'可提现金额 {int(txe) / 10000}元，点击提现',f'惜之酱提醒您 {OOO0000O0OOO00O0O.name} 花花阅读可以提现了',f'{OOO0000O0OOO00O0O.readhost}/user/index.html?mid=FK73K93DA')#line:362
            if pushable :#line:363
                push (f'可提现金额 {int(txe) / 10000}元，点击提现',f'惜之酱提醒您 {OOO0000O0OOO00O0O.name} 花花阅读可以提现了',f'{OOO0000O0OOO00O0O.readhost}/user/index.html?mid=FK73K93DA',OOO0000O0OOO00O0O .uid )#line:365
    def run (OO00O0O000000O0O0 ):#line:367
        if OO00O0O000000O0O0 .get_info ():#line:368
            OO00O0O000000O0O0 .stataccess ()#line:369
            OO00O0O000000O0O0 .get_readhost ()#line:370
            OO00O0O000000O0O0 .psmoneyc ()#line:371
            OO00O0O000000O0O0 .read ()#line:372
            OO00O0O000000O0O0 .tixian ()#line:373
        if not printf :#line:374
            print (OO00O0O000000O0O0 .msg .strip ())#line:375
def yd (O00O0O0OO0OOO0OOO ):#line:378
    while not O00O0O0OO0OOO0OOO .empty ():#line:379
        O0O00OOOO0000000O =O00O0O0OO0OOO0OOO .get ()#line:380
        try :#line:381
            O00OOOOO0000OO00O =Allinone (O0O00OOOO0000000O )#line:382
            O00OOOOO0000OO00O .run ()#line:383
        except Exception as OO0OOOOOO0000O00O :#line:384
            print (OO0OOOOOO0000O00O )#line:385
def get_info ():#line:388
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*20 )#line:390
    print ('入口：http://mr181283238.yxjbhdl.cn/user/index.html?mid=EG5EVNLF3')#line:391
    OOOOOO0O00OOOOOOO ='v1.5'#line:392
    OOO0O0OOO000OOOO0 =_O00000000OO00O000 ['version']['花花']#line:393
    print (f'当前版本{OOOOOO0O00OOOOOOO}，仓库版本{OOO0O0OOO000OOOO0}\n{_O00000000OO00O000["update_log"]["花花"]}')#line:394
    if OOOOOO0O00OOOOOOO <OOO0O0OOO000OOOO0 :#line:395
        print ('请到仓库下载最新版本k_hh.py')#line:396
    return True #line:397
def main ():#line:400
    O0O000O000OO0OO00 =get_info ()#line:401
    O0000OOOO000O0O00 =os .getenv ('hhck')#line:402
    if not O0000OOOO000O0O00 :#line:403
        O0000OOOO000O0O00 =os .getenv ('aiock')#line:404
        if not O0000OOOO000O0O00 :#line:405
            print (_O00000000OO00O000 .get ('msg')['花花'])#line:406
            exit ()#line:407
    try :#line:408
        O0000OOOO000O0O00 =ast .literal_eval (O0000OOOO000O0O00 )#line:409
    except :#line:410
        pass #line:411
    O00000O0OO00O00O0 =Queue ()#line:412
    OOO0O0000OO0O0O0O =[]#line:413
    print ('-'*20 )#line:414
    print (f'共获取到{len(O0000OOOO000O0O00)}个账号，如与实际不符，请检查ck填写方式')#line:415
    print ("="*25 )#line:416
    if not O0O000O000OO0OO00 :#line:417
        exit ()#line:418
    for O0O0O0OO0O00O0O0O ,O0OOO00000000O00O in enumerate (O0000OOOO000O0O00 ,start =1 ):#line:419
        O00000O0OO00O00O0 .put (O0OOO00000000O00O )#line:420
    for O0O0O0OO0O00O0O0O in range (max_workers ):#line:421
        O0O00O0OOOO0O0OO0 =threading .Thread (target =yd ,args =(O00000O0OO00O00O0 ,))#line:422
        O0O00O0OOOO0O0OO0 .start ()#line:423
        OOO0O0000OO0O0O0O .append (O0O00O0OOOO0O0OO0 )#line:424
        time .sleep (delay_time )#line:425
    for O0O0O00000O0OOO00 in OOO0O0000OO0O0O0O :#line:426
        O0O0O00000O0OOO00 .join ()#line:427
    print ('-'*25 +f'\n{checkdict}')#line:428
    with open ('checkdict.json','w',encoding ='utf-8')as O0OOOOOOO00OO000O :#line:429
        O0OOOOOOO00OO000O .write (json .dumps (checkdict ))#line:430
if __name__ =='__main__':#line:433
    main ()#line:434
