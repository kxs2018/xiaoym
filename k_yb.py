# -*- coding: utf-8 -*-
# k_yb
# Author: 惜之酱
"""
new Env('元宝');
入口：http://mr181335235.ahmgfulpshw.cloud/coin/index.html?mid=DG52AW2N6
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
txbz = 10000  # 不低于3000，平台的提现标准为3000
"""设置为10000，即为1块起提"""

"""并发延迟设置"""
delay_time = 30
"""设置为30即每隔30秒新增一个号做任务，直到数量达到max_workers"""

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
def get_msg ():#line:35
    O0O0OO000OOOO0O00 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:37
    OO000O0O0OOOO00O0 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O0O0OO000OOOO0O00 ).json ()#line:38
    return OO000O0O0OOOO00O0 #line:39
_O0OO000O00O00O000 =get_msg ()#line:42
try :#line:44
    from lxml import etree #line:45
except :#line:46
    print (_O0OO000O00O00O000 .get ('help')['lxml'])#line:47
qwbotkey =os .getenv ('qwbotkey')#line:48
if not qwbotkey :#line:49
    print (_O0OO000O00O00O000 .get ('help')['qwbotkey'])#line:50
    exit ()#line:51
def ftime ():#line:54
    O000O0O0OOO0O0O0O =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:55
    return O000O0O0OOO0O0O0O #line:56
def printlog (O0OOOOOOO00O0O000 ):#line:59
    if printf :#line:60
        print (O0OOOOOOO00O0O000 )#line:61
def debugger (OOO000OOO00O0000O ):#line:64
    if debug :#line:65
        print (OOO000OOO00O0000O )#line:66
def send (O00O00OOO00OO00O0 ,O000O00O000000OOO ='通知',O00O00O00OOOOOO00 =None ):#line:69
    if not O000O00O000000OOO or not O00O00O00OOOOOO00 :#line:70
        OO000OO0O00000O0O ={"msgtype":"text","text":{"content":f"{O000O00O000000OOO}\n\n{O00O00OOO00OO00O0}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:77
    else :#line:78
        OO000OO0O00000O0O ={"msgtype":"news","news":{"articles":[{"title":O000O00O000000OOO ,"description":O00O00OOO00OO00O0 ,"url":O00O00O00OOOOOO00 ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:91
    OOO0O00O0000O00O0 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:92
    O0O00O0O0O0OOOO00 =requests .post (OOO0O00O0000O00O0 ,data =json .dumps (OO000OO0O00000O0O )).json ()#line:93
    if O0O00O0O0O0OOOO00 .get ('errcode')!=0 :#line:94
        print ('消息发送失败，请检查key和发送格式')#line:95
        return False #line:96
    return O0O00O0O0O0OOOO00 #line:97
def getmpinfo (O0O0O000O0O00000O ):#line:100
    if not O0O0O000O0O00000O or O0O0O000O0O00000O =='':#line:101
        return False #line:102
    OO000O0OOOOOOOOOO ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:104
    O00OO0OO00O000O0O =requests .get (O0O0O000O0O00000O ,headers =OO000O0OOOOOOOOOO )#line:105
    O0OO000O0OO0OO00O =etree .HTML (O00OO0OO00O000O0O .text )#line:106
    O0OOOOO000O0O00O0 =O0OO000O0OO0OO00O .xpath ('//meta[@*="og:title"]/@content')#line:108
    if O0OOOOO000O0O00O0 :#line:109
        O0OOOOO000O0O00O0 =O0OOOOO000O0O00O0 [0 ]#line:110
    OO0OO00O0OO000OOO =O0OO000O0OO0OO00O .xpath ('//meta[@*="og:url"]/@content')#line:111
    if OO0OO00O0OO000OOO :#line:112
        OO0OO00O0OO000OOO =OO0OO00O0OO000OOO [0 ].encode ().decode ()#line:113
    try :#line:114
        O0OO0O0000O00O0OO =re .findall (r'biz=(.*?)&',O0O0O000O0O00000O )[0 ]#line:115
    except :#line:116
        O0OO0O0000O00O0OO =re .findall (r'biz=(.*?)&',OO0OO00O0OO000OOO )[0 ]#line:117
    if not O0OO0O0000O00O0OO :#line:118
        return False #line:119
    OO0O0O0000OOO0O00 =O0OO000O0OO0OO00O .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:120
    if OO0O0O0000OOO0O00 :#line:121
        OO0O0O0000OOO0O00 =OO0O0O0000OOO0O00 [0 ].strip ()#line:122
    O0OO0000OOOO000O0 =re .findall (r"user_name.DATA'\) : '(.*?)'",O00OO0OO00O000O0O .text )or O0OO000O0OO0OO00O .xpath ('//span[@class="profile_meta_value"]/text()')#line:124
    if O0OO0000OOOO000O0 :#line:125
        O0OO0000OOOO000O0 =O0OO0000OOOO000O0 [0 ]#line:126
    OOOO00O0OOO00O0OO =re .findall (r'createTime = \'(.*)\'',O00OO0OO00O000O0O .text )#line:127
    if OOOO00O0OOO00O0OO :#line:128
        OOOO00O0OOO00O0OO =OOOO00O0OOO00O0OO [0 ][5 :]#line:129
    OOO00O0OO00O00O0O =f'{OOOO00O0OOO00O0OO}|{O0OOOOO000O0O00O0}'#line:130
    O000O0O0OO0OO00O0 ={'biz':O0OO0O0000O00O0OO ,'text':OOO00O0OO00O00O0O }#line:131
    return O000O0O0OO0OO00O0 #line:132
class Allinone :#line:135
    def __init__ (OO000O00OO000O0O0 ,OO0OOO0OOO00OO000 ):#line:136
        OO000O00OO000O0O0 .name =OO0OOO0OOO00OO000 ['name']#line:137
        OO000O00OO000O0O0 .s =requests .session ()#line:138
        OO000O00OO000O0O0 .payload ={"un":OO0OOO0OOO00OO000 ['un'],"token":OO0OOO0OOO00OO000 ['token'],"pageSize":20 }#line:139
        OO000O00OO000O0O0 .s .headers ={'Accept':'application/json, text/javascript, */*; q=0.01','Content-Type':'application/json; charset=UTF-8','Host':'u.cocozx.cn','Connection':'keep-alive','User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",'Accept-Encoding':'gzip, deflate'}#line:145
        OO000O00OO000O0O0 .msg =''#line:146
    def get_info (O00OOOO00000OOOOO ):#line:148
        O0O0OO0O0OOOOO0OO ='CS5T87Q98'if O00OOOO00000OOOOO .name =='AI'else 'DG52AW2N6'#line:149
        OOO00OO0000O0O0OO ={**O00OOOO00000OOOOO .payload ,**{'code':O0O0OO0O0OOOOO0OO }}#line:150
        try :#line:151
            OO0O0O0O0000OOO0O =O00OOOO00000OOOOO .s .post ("http://u.cocozx.cn/api/coin/info",json =OOO00OO0000O0O0OO ).json ()#line:152
            O0O0OOOOOO0000000 =OO0O0O0O0000OOO0O .get ("result")#line:153
            debugger (f'get_info {OO0O0O0O0000OOO0O}')#line:154
            OOOO0OO0OO0O00O00 =O0O0OOOOOO0000000 .get ('us')#line:155
            if OOOO0OO0OO0O00O00 ==2 :#line:156
                O00OOOO00000OOOOO .msg +=f'{O00OOOO00000OOOOO.name}已被封\n'#line:157
                printlog (f'{O00OOOO00000OOOOO.name}已被封')#line:158
                return False #line:159
            O00OOOO00000OOOOO .msg +=f"""{O00OOOO00000OOOOO.name}:今日阅读次数:{O0O0OOOOOO0000000["dayCount"]}，当前元宝:{O0O0OOOOOO0000000["moneyCurrent"]}，累计阅读次数:{O0O0OOOOOO0000000["doneWx"]}\n"""#line:161
            printlog (f"""{O00OOOO00000OOOOO.name}:今日阅读次数:{O0O0OOOOOO0000000["dayCount"]}，当前元宝:{O0O0OOOOOO0000000["moneyCurrent"]}，累计阅读次数:{O0O0OOOOOO0000000["doneWx"]}""")#line:163
            OOOOOO00O00O00000 =int (O0O0OOOOOO0000000 ["moneyCurrent"])#line:164
            O00OOOO00000OOOOO .huid =O0O0OOOOOO0000000 .get ('uid')#line:165
            return OOOOOO00O00O00000 #line:166
        except :#line:167
            return False #line:168
    def get_readhost (OO0O000OOO0O0O00O ):#line:170
        OOO0000OOO00OOO00 ="http://u.cocozx.cn/api/coin/getReadHost"#line:171
        O00OOO0OO0OO00O0O =OO0O000OOO0O0O00O .s .post (OOO0000OOO00OOO00 ,json =OO0O000OOO0O0O00O .payload ).json ()#line:172
        debugger (f'readhome {O00OOO0OO0OO00O0O}')#line:173
        OO0O000OOO0O0O00O .readhost =O00OOO0OO0OO00O0O .get ('result')['host']#line:174
        OO0O000OOO0O0O00O .msg +=f'邀请链接：{OO0O000OOO0O0O00O.readhost}/oz/index.html?mid={OO0O000OOO0O0O00O.huid}\n'#line:175
        printlog (f"{OO0O000OOO0O0O00O.name}:邀请链接：{OO0O000OOO0O0O00O.readhost}/oz/index.html?mid={OO0O000OOO0O0O00O.huid}")#line:176
    def get_status (OOO0OOOOO000OO00O ):#line:178
        O0O0OOOOOOO000OO0 =OOO0OOOOO000OO00O .s .post ("http://u.cocozx.cn/api/coin/read",json =OOO0OOOOO000OO00O .payload ).json ()#line:179
        debugger (f'getstatus {O0O0OOOOOOO000OO0}')#line:180
        OOO0OOOOO000OO00O .status =O0O0OOOOOOO000OO0 .get ("result").get ("status")#line:181
        if OOO0OOOOO000OO00O .status ==40 :#line:182
            OOO0OOOOO000OO00O .msg +="文章还没有准备好\n"#line:183
            printlog (f"{OOO0OOOOO000OO00O.name}:文章还没有准备好")#line:184
            return #line:185
        elif OOO0OOOOO000OO00O .status ==50 :#line:186
            OOO0OOOOO000OO00O .msg +="阅读失效\n"#line:187
            printlog (f"{OOO0OOOOO000OO00O.name}:阅读失效")#line:188
            return #line:189
        elif OOO0OOOOO000OO00O .status ==60 :#line:190
            OOO0OOOOO000OO00O .msg +="已经全部阅读完了\n"#line:191
            printlog (f"{OOO0OOOOO000OO00O.name}:已经全部阅读完了")#line:192
            return #line:193
        elif OOO0OOOOO000OO00O .status ==70 :#line:194
            OOO0OOOOO000OO00O .msg +="下一轮还未开启\n"#line:195
            printlog (f"{OOO0OOOOO000OO00O.name}:下一轮还未开启")#line:196
            return #line:197
        elif OOO0OOOOO000OO00O .status ==10 :#line:198
            OO00O0O000000O00O =O0O0OOOOOOO000OO0 ["result"]["url"]#line:199
            OOO0OOOOO000OO00O .msg +='-'*50 +"\n阅读链接获取成功\n"#line:200
            return OO00O0O000000O00O #line:201
    def submit (OO00O0O0O000O0000 ):#line:203
        OOOOO0O0O00O0O0O0 ={**{'type':1 },**OO00O0O0O000O0000 .payload }#line:204
        OOO0O0OOO000000OO =OO00O0O0O000O0000 .s .post ("http://u.cocozx.cn/api/coin/submit?zx=&xz=1",json =OOOOO0O0O00O0O0O0 )#line:205
        O0OOOO00OOO000O0O =OOO0O0OOO000000OO .json ().get ('result')#line:206
        debugger ('submit '+OOO0O0OOO000000OO .text )#line:207
        OO00O0O0O000O0000 .msg +=f"阅读成功,获得元宝{O0OOOO00OOO000O0O['val']}，当前剩余次数:{O0OOOO00OOO000O0O['progress']}\n"#line:208
        printlog (f"{OO00O0O0O000O0000.name}:阅读成功,获得元宝{O0OOOO00OOO000O0O['val']}，当前剩余次数:{O0OOOO00OOO000O0O['progress']}")#line:209
    def read (O0OOO000OO00000O0 ):#line:211
        while True :#line:212
            O000O0O00O0O00O00 =O0OOO000OO00000O0 .get_status ()#line:213
            if not O000O0O00O0O00O00 :#line:214
                if O0OOO000OO00000O0 .status ==30 :#line:215
                    time .sleep (3 )#line:216
                    continue #line:217
                break #line:218
            O0O0O0O0O000O00OO =getmpinfo (O000O0O00O0O00O00 )#line:219
            if not O0O0O0O0O000O00OO :#line:220
                printlog (f'{O0OOO000OO00000O0.name}:获取文章信息失败，程序中止')#line:221
                return False #line:222
            O0OOO000OO00000O0 .msg +='开始阅读 '+O0O0O0O0O000O00OO ['text']+'\n'#line:223
            printlog (f'{O0OOO000OO00000O0.name}:开始阅读 '+O0O0O0O0O000O00OO ['text'])#line:224
            OOOOO000O0O000OOO =randint (7 ,10 )#line:225
            if O0O0O0O0O000O00OO ['biz']=="Mzg2Mzk3Mjk5NQ==":#line:226
                O0OOO000OO00000O0 .msg +='正在阅读检测文章\n'#line:227
                printlog (f'{O0OOO000OO00000O0.name}:正在阅读检测文章')#line:228
                send (f'{O0OOO000OO00000O0.name}  元宝阅读过检测',O0O0O0O0O000O00OO ['text'],O000O0O00O0O00O00 )#line:229
                time .sleep (60 )#line:230
            time .sleep (OOOOO000O0O000OOO )#line:231
            O0OOO000OO00000O0 .submit ()#line:232
    def tixian (OOO00O00OOOO0000O ):#line:234
        global txe #line:235
        OO0OOO0O0O00000O0 =OOO00O00OOOO0000O .get_info ()#line:236
        if OO0OOO0O0O00000O0 <txbz :#line:237
            OOO00O00OOOO0000O .msg +='你的元宝已不足\n'#line:238
            printlog (f'{OOO00O00OOOO0000O.name}:你的元宝已不足')#line:239
            return False #line:240
        elif 10000 <=OO0OOO0O0O00000O0 <49999 :#line:241
            txe =10000 #line:242
        elif 50000 <=OO0OOO0O0O00000O0 <100000 :#line:243
            txe =50000 #line:244
        elif 3000 <=OO0OOO0O0O00000O0 <10000 :#line:245
            txe =3000 #line:246
        elif OO0OOO0O0O00000O0 >=100000 :#line:247
            txe =100000 #line:248
        OOO00O00OOOO0000O .msg +=f"提现金额:{txe}\n"#line:249
        printlog (f'{OOO00O00OOOO0000O.name}:提现金额 {txe}')#line:250
        OO00O00O0OO00O0O0 ="http://u.cocozx.cn/api/coin/wdmoney"#line:251
        OOO0OOO0O000OOOO0 ={**OOO00O00OOOO0000O .payload ,**{"val":txe }}#line:252
        try :#line:253
            OOOO00OO00O0O0O00 =OOO00O00OOOO0000O .s .post (OO00O00O0OO00O0O0 ,json =OOO0OOO0O000OOOO0 ).json ()#line:254
            OOO00O00OOOO0000O .msg +=f'提现结果：{OOOO00OO00O0O0O00.get("msg")}\n'#line:255
            printlog (f'{OOO00O00OOOO0000O.name}:提现结果 {OOOO00OO00O0O0O00.get("msg")}')#line:256
        except :#line:257
            OOO00O00OOOO0000O .msg +=f"自动提现不成功，发送通知手动提现\n"#line:258
            printlog (f"{OOO00O00OOOO0000O.name}:自动提现不成功，发送通知手动提现")#line:259
            send (f'可提现金额 {int(txe) / 10000}元，点击提现',f'惜之酱提醒您 {OOO00O00OOOO0000O.name} 元宝阅读可以提现了',f'{OOO00O00OOOO0000O.readhost}/coin/index.html?mid=CS5T87Q98')#line:261
    def run (O000OOO00OOO0O000 ):#line:263
        if O000OOO00OOO0O000 .get_info ():#line:264
            O000OOO00OOO0O000 .get_readhost ()#line:265
            O000OOO00OOO0O000 .read ()#line:266
            O000OOO00OOO0O000 .tixian ()#line:267
        if not printf :#line:268
            print (O000OOO00OOO0O000 .msg .strip ())#line:269
def yd (O0OOOOOO00O0000O0 ):#line:272
    while not O0OOOOOO00O0000O0 .empty ():#line:273
        O00O000000O0O0OOO =O0OOOOOO00O0000O0 .get ()#line:274
        O0000O0OOO00000OO =Allinone (O00O000000O0O0OOO )#line:275
        O0000O0OOO00000OO .run ()#line:276
def get_info ():#line:279
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*20 )#line:281
    print ('入口：http://mr181335235.ahmgfulpshw.cloud/coin/index.html?mid=DG52AW2N6')#line:282
    OOOO0OOO0O00OOO0O ='V1.3'#line:283
    O0O0OOO0000000O0O =_O0OO000O00O00O000 ['version']['k_yb']or _O0OO000O00O00O000 ['version']['kyb']#line:284
    print (f'当前版本{OOOO0OOO0O00OOO0O}，仓库版本{O0O0OOO0000000O0O}\n{_O0OO000O00O00O000["update_log"]["花花"]}')#line:285
    if OOOO0OOO0O00OOO0O <O0O0OOO0000000O0O :#line:286
        print ('请到仓库下载最新版本k_ybb.py')#line:287
def main ():#line:291
    get_info ()#line:292
    OO0OOO00OOO0OO0OO =os .getenv ('ybck')#line:293
    if not OO0OOO00OOO0OO0OO :#line:294
        OO0OOO00OOO0OO0OO =os .getenv ('aiock')#line:295
        if not OO0OOO00OOO0OO0OO :#line:296
            print (_O0OO000O00O00O000 .get ('msg')['元宝'])#line:297
            exit ()#line:298
    try :#line:299
        OO0OOO00OOO0OO0OO =ast .literal_eval (OO0OOO00OOO0OO0OO )#line:300
    except :#line:301
        pass #line:302
    O0OOO0OO00000OO00 =Queue ()#line:303
    OOO0O0OOOOOOOOO00 =[]#line:304
    print ('-'*20 )#line:305
    print (f'共获取到{len(OO0OOO00OOO0OO0OO)}个账号，如与实际不符，请检查ck填写方式')#line:306
    print ("="*25 )#line:307
    for O0000OOOO00OOO0O0 ,O0OO00000OOOOOOO0 in enumerate (OO0OOO00OOO0OO0OO ,start =1 ):#line:308
        O0OOO0OO00000OO00 .put (O0OO00000OOOOOOO0 )#line:309
    for O0000OOOO00OOO0O0 in range (max_workers ):#line:310
        O0O0OOOOO0OOOO0O0 =threading .Thread (target =yd ,args =(O0OOO0OO00000OO00 ,))#line:311
        O0O0OOOOO0OOOO0O0 .start ()#line:312
        OOO0O0OOOOOOOOO00 .append (O0O0OOOOO0OOOO0O0 )#line:313
        time .sleep (delay_time )#line:314
    for OOOOOOOOO00O0000O in OOO0O0OOOOOOOOO00 :#line:315
        OOOOOOOOO00O0000O .join ()#line:316
if __name__ =='__main__':#line:319
    main ()#line:320
