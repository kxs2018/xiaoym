# -*- coding: utf-8 -*-
# k_hh
# Author: 惜之酱
"""
入口：http://mr181283238.yxjbhdl.cn/user/index.html?mid=EG5EVNLF3
"""
"""实时打印日志开关"""
printf = 1
"""1为开，0为关"""

"""debug模式开关"""
debug = 0
"""1为开，打印调试日志；0为关，不打印"""

"""线程数量设置"""
max_workers = 4
"""设置为4，即最多有4个任务同时进行"""

"""设置提现标准"""
txbz = 5000  # 不低于3000，平台的提现标准为3000
"""设置为5000，即为5毛起提"""

"""并发延迟设置"""
delay_time = 30
"""设置为30即每隔30秒新增一个号做任务，直到数量达到max_workers"""

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
def get_msg ():#line:35
    OOO000O0O00O00OO0 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:37
    OOO000O0O0O0O0OO0 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OOO000O0O00O00OO0 ).json ()#line:38
    return OOO000O0O0O0O0OO0 #line:39
_OO00OO00OO00OOOOO =get_msg ()#line:42
try :#line:43
    from lxml import etree #line:44
except :#line:45
    print (_OO00OO00OO00OOOOO .get ('help')['lxml'])#line:46
qwbotkey =os .getenv ('qwbotkey')#line:47
if not qwbotkey :#line:49
    print (_OO00OO00OO00OOOOO .get ('help')['qwbotkey'])#line:50
    exit ()#line:51
def ftime ():#line:54
    O0OOOO0000OOO0OO0 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:55
    return O0OOOO0000OOO0OO0 #line:56
def debugger (O00O00O0O0OOO0000 ):#line:59
    if debug :#line:60
        print (O00O00O0O0OOO0000 )#line:61
def printlog (O0OOO00OOO0OOOOO0 ):#line:64
    if printf :#line:65
        print (O0OOO00OOO0OOOOO0 )#line:66
def send (OOOOOOOOOOOOO0O0O ,OO0O000O0OOO00O0O ='通知',OOOO0OOO0O000OO0O =None ):#line:69
    if not OO0O000O0OOO00O0O or not OOOO0OOO0O000OO0O :#line:70
        OO0OOOOO0OOO000O0 ={"msgtype":"text","text":{"content":f"{OO0O000O0OOO00O0O}\n\n{OOOOOOOOOOOOO0O0O}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:77
    else :#line:78
        OO0OOOOO0OOO000O0 ={"msgtype":"news","news":{"articles":[{"title":OO0O000O0OOO00O0O ,"description":OOOOOOOOOOOOO0O0O ,"url":OOOO0OOO0O000OO0O ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:91
    O0000O0O0O00OO00O =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:92
    OOOOO00O00O0OO0O0 =requests .post (O0000O0O0O00OO00O ,data =json .dumps (OO0OOOOO0OOO000O0 )).json ()#line:93
    if OOOOO00O00O0OO0O0 .get ('errcode')!=0 :#line:94
        print ('消息发送失败，请检查key和发送格式')#line:95
        return False #line:96
    return OOOOO00O00O0OO0O0 #line:97
def getmpinfo (OOO00OOO0000OOOOO ):#line:100
    if not OOO00OOO0000OOOOO or OOO00OOO0000OOOOO =='':#line:101
        return False #line:102
    OOO0OOOO00O0O0OOO ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:104
    OOOO00O0O00OO00O0 =requests .get (OOO00OOO0000OOOOO ,headers =OOO0OOOO00O0O0OOO )#line:105
    O0O0000OOOOOOO0O0 =etree .HTML (OOOO00O0O00OO00O0 .text )#line:106
    O00OOOO00OO0OO0O0 =O0O0000OOOOOOO0O0 .xpath ('//meta[@*="og:title"]/@content')#line:108
    if O00OOOO00OO0OO0O0 :#line:109
        O00OOOO00OO0OO0O0 =O00OOOO00OO0OO0O0 [0 ]#line:110
    O000O0000000O00O0 =O0O0000OOOOOOO0O0 .xpath ('//meta[@*="og:url"]/@content')#line:111
    if O000O0000000O00O0 :#line:112
        O000O0000000O00O0 =O000O0000000O00O0 [0 ].encode ().decode ()#line:113
    try :#line:114
        OOO00OO0OO00O0OO0 =re .findall (r'biz=(.*?)&',OOO00OOO0000OOOOO )[0 ]#line:115
    except :#line:116
        OOO00OO0OO00O0OO0 =re .findall (r'biz=(.*?)&',O000O0000000O00O0 )[0 ]#line:117
    if not OOO00OO0OO00O0OO0 :#line:118
        return False #line:119
    OO000O0O0O00O0O00 =O0O0000OOOOOOO0O0 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:120
    if OO000O0O0O00O0O00 :#line:121
        OO000O0O0O00O0O00 =OO000O0O0O00O0O00 [0 ].strip ()#line:122
    OOO00O0OO000OOO00 =re .findall (r"user_name.DATA'\) : '(.*?)'",OOOO00O0O00OO00O0 .text )or O0O0000OOOOOOO0O0 .xpath ('//span[@class="profile_meta_value"]/text()')#line:124
    if OOO00O0OO000OOO00 :#line:125
        OOO00O0OO000OOO00 =OOO00O0OO000OOO00 [0 ]#line:126
    O000O0OOOO00O0O00 =re .findall (r'createTime = \'(.*)\'',OOOO00O0O00OO00O0 .text )#line:127
    if O000O0OOOO00O0O00 :#line:128
        O000O0OOOO00O0O00 =O000O0OOOO00O0O00 [0 ][5 :]#line:129
    OOOOO000O00000OOO =f'{O000O0OOOO00O0O00} {O00OOOO00OO0OO0O0}'#line:130
    OOOOOO00O0O00O000 ={'biz':OOO00OO0OO00O0OO0 ,'text':OOOOO000O00000OOO }#line:131
    return OOOOOO00O0O00O000 #line:132
class Allinone :#line:135
    def __init__ (O00O0O000OOOOO00O ,O0OO0O00OO0O000OO ):#line:136
        O00O0O000OOOOO00O .name =O0OO0O00OO0O000OO ['name']#line:137
        O00O0O000OOOOO00O .s =requests .session ()#line:138
        O00O0O000OOOOO00O .payload ={"un":O0OO0O00OO0O000OO ['un'],"token":O0OO0O00OO0O000OO ['token'],"pageSize":20 }#line:139
        O00O0O000OOOOO00O .s .headers ={'Accept':'application/json, text/javascript, */*; q=0.01','Content-Type':'application/json; charset=UTF-8','Host':'u.cocozx.cn','Connection':'keep-alive','User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",'Origin':'http://mr1694971896247.dswxin.cn',}#line:145
        O00O0O000OOOOO00O .headers =O00O0O000OOOOO00O .s .headers .copy ()#line:146
        O00O0O000OOOOO00O .msg =''#line:147
    def get_readhost (OOO0OOOOOO0O00OO0 ):#line:149
        OO0OOO000O00OOOOO ="http://u.cocozx.cn/api/user/getReadHost"#line:150
        OO0OO0O00000O00OO =OOO0OOOOOO0O00OO0 .s .post (OO0OOO000O00OOOOO ,json =OOO0OOOOOO0O00OO0 .payload ).json ()#line:151
        debugger (f'readhome {OO0OO0O00000O00OO}')#line:152
        OOO0OOOOOO0O00OO0 .readhost =OO0OO0O00000O00OO .get ('result')['host']#line:153
        OOO0OOOOOO0O00OO0 .headers ['Origin']=OOO0OOOOOO0O00OO0 .readhost #line:154
        OOO0OOOOOO0O00OO0 .msg +=f'邀请链接：{OOO0OOOOOO0O00OO0.readhost}/user/index.html?mid={OOO0OOOOOO0O00OO0.huid}\n'#line:155
        printlog (f"{OOO0OOOOOO0O00OO0.name}:邀请链接 {OOO0OOOOOO0O00OO0.readhost}/user/index.html?mid={OOO0OOOOOO0O00OO0.huid}")#line:156
    def stataccess (OO0OOO0O0OO0O0000 ):#line:158
        O00O0OOO0000OO00O ='http://u.cocozx.cn/api/user/statAccess'#line:159
        OO0OOO0O0OO0O0000 .s .post (O00O0OOO0000OO00O ,json =OO0OOO0O0OO0O0000 .payload ).json ()#line:160
    def get_info (O0O0O0O0O0OO00O0O ):#line:162
        try :#line:163
            O0O0OO00000O0OO00 =O0O0O0O0O0OO00O0O .s .post ("http://u.cocozx.cn/api/user/info",json =O0O0O0O0O0OO00O0O .payload ).json ()#line:164
            OOO00OO00O0OO00OO =O0O0OO00000O0OO00 .get ("result")#line:165
            debugger (f'get_info {O0O0OO00000O0OO00}')#line:166
            O0OO00O0OO0000O0O =OOO00OO00O0OO00OO .get ('us')#line:167
            if O0OO00O0OO0000O0O ==2 :#line:168
                O0O0O0O0O0OO00O0O .msg +=f'{O0O0O0O0O0OO00O0O.name}已被封\n'#line:169
                printlog (f'{O0O0O0O0O0OO00O0O.name}已被封')#line:170
                return False #line:171
            O0O0O0O0O0OO00O0O .msg +=f"""{O0O0O0O0O0OO00O0O.name}:今日阅读次数:{OOO00OO00O0OO00OO["dayCount"]}，当前花儿:{OOO00OO00O0OO00OO["moneyCurrent"]}，累计阅读次数:{OOO00OO00O0OO00OO["doneWx"]}\n"""#line:172
            printlog (f"""{O0O0O0O0O0OO00O0O.name}:今日阅读次数:{OOO00OO00O0OO00OO["dayCount"]}，当前花儿:{OOO00OO00O0OO00OO["moneyCurrent"]}，累计阅读次数:{OOO00OO00O0OO00OO["doneWx"]}""")#line:174
            OO0O00OOO0OOOOOO0 =int (OOO00OO00O0OO00OO ["moneyCurrent"])#line:175
            O0O0O0O0O0OO00O0O .huid =OOO00OO00O0OO00OO .get ('uid')#line:176
            return OO0O00OOO0OOOOOO0 #line:177
        except :#line:178
            return False #line:179
    def psmoneyc (OOOOOO0OO000OOOO0 ):#line:181
        OO0OOOO0O0OO0O0OO ={**OOOOOO0OO000OOOO0 .payload ,**{'mid':OOOOOO0OO000OOOO0 .huid }}#line:182
        try :#line:183
            O0O00O0O00000000O =OOOOOO0OO000OOOO0 .s .post ("http://u.cocozx.cn/api/user/psmoneyc",json =OO0OOOO0O0OO0O0OO ).json ()#line:184
            OOOOOO0OO000OOOO0 .msg +=f"感谢下级送来的{O0O00O0O00000000O['result']['val']}花儿\n"#line:185
            printlog (f"{OOOOOO0OO000OOOO0.name}:感谢下级送来的{O0O00O0O00000000O['result']['val']}花儿")#line:186
        except :#line:187
            pass #line:188
        return #line:189
    def get_status (O0O0O0OOO0000000O ):#line:191
        O000O0O00OO0OOOOO =requests .post ("http://u.cocozx.cn/api/user/read",headers =O0O0O0OOO0000000O .headers ,json =O0O0O0OOO0000000O .payload ).json ()#line:192
        debugger (f'getstatus {O000O0O00OO0OOOOO}')#line:193
        O0O0O0OOO0000000O .status =O000O0O00OO0OOOOO .get ("result").get ("status")#line:194
        if O0O0O0OOO0000000O .status ==40 :#line:195
            O0O0O0OOO0000000O .msg +="文章还没有准备好\n"#line:196
            printlog (f"{O0O0O0OOO0000000O.name}:文章还没有准备好")#line:197
            return #line:198
        elif O0O0O0OOO0000000O .status ==50 :#line:199
            O0O0O0OOO0000000O .msg +="阅读失效\n"#line:200
            printlog (f"{O0O0O0OOO0000000O.name}:阅读失效")#line:201
            return #line:202
        elif O0O0O0OOO0000000O .status ==60 :#line:203
            O0O0O0OOO0000000O .msg +="已经全部阅读完了\n"#line:204
            printlog (f"{O0O0O0OOO0000000O.name}:已经全部阅读完了")#line:205
            return #line:206
        elif O0O0O0OOO0000000O .status ==70 :#line:207
            O0O0O0OOO0000000O .msg +="下一轮还未开启\n"#line:208
            printlog (f"{O0O0O0OOO0000000O.name}:下一轮还未开启")#line:209
            return #line:210
        elif O0O0O0OOO0000000O .status ==10 :#line:211
            OOOOO0OOO00OO0000 =O000O0O00OO0OOOOO ["result"]["url"]#line:212
            O0O0O0OOO0000000O .msg +='-'*50 +"\n阅读链接获取成功\n"#line:213
            return OOOOO0OOO00OO0000 #line:214
    def submit (O0OOO0OO00O00OOO0 ):#line:216
        OOO0000O0000000O0 ={**{'type':1 },**O0OOO0OO00O00OOO0 .payload }#line:217
        OO0O000O0O00OOO00 =requests .post ("http://u.cocozx.cn/api/user/submit?zx=&xz=1",headers =O0OOO0OO00O00OOO0 .headers ,json =OOO0000O0000000O0 )#line:218
        OO00000OOO000OOO0 =OO0O000O0O00OOO00 .json ().get ('result')#line:219
        debugger ('submit '+OO0O000O0O00OOO00 .text )#line:220
        O0OOO0OO00O00OOO0 .msg +=f'阅读成功,获得花儿{OO00000OOO000OOO0["val"]}，剩余次数:{OO00000OOO000OOO0["progress"]}\n'#line:221
        printlog (f"{O0OOO0OO00O00OOO0.name}:阅读成功,获得花儿{OO00000OOO000OOO0['val']}，剩余次数:{OO00000OOO000OOO0['progress']}")#line:222
    def read (OOOO0OO000O000000 ):#line:224
        while True :#line:225
            OOO0OO0O0OO0OOO0O =OOOO0OO000O000000 .get_status ()#line:226
            if not OOO0OO0O0OO0OOO0O :#line:227
                if OOOO0OO000O000000 .status ==30 :#line:228
                    time .sleep (3 )#line:229
                    continue #line:230
                break #line:231
            O0OOO0OOO00OOO0OO =getmpinfo (OOO0OO0O0OO0OOO0O )#line:232
            if not O0OOO0OOO00OOO0OO :#line:233
                printlog (f'{OOOO0OO000O000000.name}:获取文章信息失败，程序中止')#line:234
                return False #line:235
            OOOO0OO000O000000 .msg +='开始阅读 '+O0OOO0OOO00OOO0OO ['text']+'\n'#line:236
            printlog (f'{OOOO0OO000O000000.name}:开始阅读 '+O0OOO0OOO00OOO0OO ['text'])#line:237
            O0OO000000O00O000 =randint (7 ,10 )#line:238
            if O0OOO0OOO00OOO0OO ['biz']=="Mzg2Mzk3Mjk5NQ==":#line:239
                OOOO0OO000O000000 .msg +='当前正在阅读检测文章\n'#line:240
                printlog (f'{OOOO0OO000O000000.name}:正在阅读检测文章')#line:241
                send (f'{OOOO0OO000O000000.name}  花花阅读正在读检测文章',O0OOO0OOO00OOO0OO ['text'],OOO0OO0O0OO0OOO0O )#line:242
                time .sleep (60 )#line:243
            time .sleep (O0OO000000O00O000 )#line:244
            OOOO0OO000O000000 .submit ()#line:245
    def tixian (O00OOO00O00OOO0OO ):#line:247
        global txe #line:248
        OO00O0OOO0O000OO0 =O00OOO00O00OOO0OO .get_info ()#line:249
        if OO00O0OOO0O000OO0 <txbz :#line:250
            O00OOO00O00OOO0OO .msg +='你的花儿不多了\n'#line:251
            printlog (f'{O00OOO00O00OOO0OO.name}:你的花儿不多了')#line:252
            return False #line:253
        if 10000 <=OO00O0OOO0O000OO0 <49999 :#line:254
            txe =10000 #line:255
        elif 5000 <=OO00O0OOO0O000OO0 <10000 :#line:256
            txe =5000 #line:257
        elif 3000 <=OO00O0OOO0O000OO0 <5000 :#line:258
            txe =3000 #line:259
        elif OO00O0OOO0O000OO0 >=50000 :#line:260
            txe =50000 #line:261
        O00OOO00O00OOO0OO .msg +=f"提现金额:{txe}"#line:262
        printlog (f'{O00OOO00O00OOO0OO.name}:提现金额 {txe}')#line:263
        O0O0000OO0OO00OO0 ={**O00OOO00O00OOO0OO .payload ,**{"val":txe }}#line:264
        try :#line:265
            O0O0OO0OO0O00O0O0 =O00OOO00O00OOO0OO .s .post ("http://u.cocozx.cn/api/user/wd",json =O0O0000OO0OO00OO0 ).json ()#line:266
            O00OOO00O00OOO0OO .msg +=f"提现结果:{O0O0OO0OO0O00O0O0.get('msg')}\n"#line:267
            printlog (f'{O00OOO00O00OOO0OO.name}:提现结果 {O0O0OO0OO0O00O0O0.get("msg")}')#line:268
        except :#line:269
            O00OOO00O00OOO0OO .msg +=f"自动提现不成功，发送通知手动提现\n"#line:270
            printlog (f"{O00OOO00O00OOO0OO.name}:自动提现不成功，发送通知手动提现")#line:271
            send (f'可提现金额 {int(txe) / 10000}元，点击提现',f'惜之酱提醒您 {O00OOO00O00OOO0OO.name} 花花阅读可以提现了',f'{O00OOO00O00OOO0OO.readhost}/user/index.html?mid=FK73K93DA')#line:273
    def run (OOOOOO0OO00O0O0OO ):#line:275
        if OOOOOO0OO00O0O0OO .get_info ():#line:276
            OOOOOO0OO00O0O0OO .stataccess ()#line:277
            OOOOOO0OO00O0O0OO .get_readhost ()#line:278
            OOOOOO0OO00O0O0OO .psmoneyc ()#line:279
            OOOOOO0OO00O0O0OO .read ()#line:280
            OOOOOO0OO00O0O0OO .tixian ()#line:281
        if not printf :#line:282
            print (OOOOOO0OO00O0O0OO .msg .strip ())#line:283
def yd (O000O0O0O0OO0O0OO ):#line:286
    while not O000O0O0O0OO0O0OO .empty ():#line:287
        O00O00O00000O00OO =O000O0O0O0OO0O0OO .get ()#line:288
        try :#line:289
            OO00OO00OOOO0O0O0 =Allinone (O00O00O00000O00OO )#line:290
            OO00OO00OOOO0O0O0 .run ()#line:291
        except Exception as OO00O000O00O0000O :#line:292
            print (OO00O000O00O0000O )#line:293
def get_info ():#line:296
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*20 )#line:298
    print ('入口：http://mr181283238.yxjbhdl.cn/user/index.html?mid=EG5EVNLF3')#line:299
    OO00OOO0O0OO0OOOO ='V2.2'#line:300
    O00000000O0OOO00O =_OO00OO00OO00OOOOO ['version'].get ('k_hh')or _OO00OO00OO00OOOOO ['version']['khh']#line:301
    print (f'当前版本{OO00OOO0O0OO0OOOO}，仓库版本{O00000000O0OOO00O}\n{_OO00OO00OO00OOOOO["update_log"]["花花"]}')#line:302
    if OO00OOO0O0OO0OOOO <O00000000O0OOO00O :#line:303
        print ('请到仓库下载最新版本k_hh.py')#line:304
def main ():#line:308
    get_info ()#line:309
    OOOOO0OO0000O0000 =os .getenv ('hhck')#line:310
    if not OOOOO0OO0000O0000 :#line:311
        OOOOO0OO0000O0000 =os .getenv ('aiock')#line:312
        if not OOOOO0OO0000O0000 :#line:313
            print (_OO00OO00OO00OOOOO .get ('msg')['花花'])#line:314
            exit ()#line:315
    try :#line:316
        OOOOO0OO0000O0000 =ast .literal_eval (OOOOO0OO0000O0000 )#line:317
    except :#line:318
        pass #line:319
    O00O0OO00O000O0OO =Queue ()#line:320
    OOO00OOO00000O000 =[]#line:321
    print ('-'*20 )#line:322
    print (f'共获取到{len(OOOOO0OO0000O0000)}个账号，如与实际不符，请检查ck填写方式')#line:323
    print ("="*25 )#line:324
    for OOO0000O00OOOOO0O ,OOO0O0OO000O0O0OO in enumerate (OOOOO0OO0000O0000 ,start =1 ):#line:325
        O00O0OO00O000O0OO .put (OOO0O0OO000O0O0OO )#line:326
    for OOO0000O00OOOOO0O in range (max_workers ):#line:327
        O0OO00OOO0O000OO0 =threading .Thread (target =yd ,args =(O00O0OO00O000O0OO ,))#line:328
        O0OO00OOO0O000OO0 .start ()#line:329
        OOO00OOO00000O000 .append (O0OO00OOO0O000OO0 )#line:330
        time .sleep (delay_time )#line:331
    for O0OO0OOOO00OOO0OO in OOO00OOO00000O000 :#line:332
        O0OO0OOOO00OOO0OO .join ()#line:333
if __name__ =='__main__':#line:336
    main ()#line:337
