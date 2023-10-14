# -*- coding: utf-8 -*-
# k_zh
# Author: 惜之酱
"""
new Env('智慧');
入口：http://mr181125495.forsranaa.cloud/oz/index.html?mid=4G7QUZY8Y
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
def get_msg ():#line:36
    O00OOO0OO0O000O0O ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:38
    OO00O000O0OOO0O00 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O00OOO0OO0O000O0O ).json ()#line:39
    return OO00O000O0OOO0O00 #line:40
_O0O0O0O0OOOOOO0OO =get_msg ()#line:43
try :#line:45
    from lxml import etree #line:46
except :#line:47
    print (_O0O0O0O0OOOOOO0OO .get ('help')['lxml'])#line:48
qwbotkey =os .getenv ('qwbotkey')#line:49
if not qwbotkey :#line:50
    print (_O0O0O0O0OOOOOO0OO .get ('help')['qwbotkey'])#line:51
    exit ()#line:52
def ftime ():#line:55
    OO000OOOOOOO0OO0O =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:56
    return OO000OOOOOOO0OO0O #line:57
def debugger (O0O0OOOOOOO00OOO0 ):#line:60
    if debug :#line:61
        print (O0O0OOOOOOO00OOO0 )#line:62
def printlog (O00O0OOO0O000O000 ):#line:65
    if printf :#line:66
        print (O00O0OOO0O000O000 )#line:67
def send (O0O0OO00O000O0000 ,OOOO0O00OO000OO00 ='通知',OOOO0OOOOOO0OO0OO =None ):#line:70
    if not OOOO0O00OO000OO00 or not OOOO0OOOOOO0OO0OO :#line:71
        OOOOO00OOO00O0O00 ={"msgtype":"text","text":{"content":f"{OOOO0O00OO000OO00}\n\n{O0O0OO00O000O0000}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:78
    else :#line:79
        OOOOO00OOO00O0O00 ={"msgtype":"news","news":{"articles":[{"title":OOOO0O00OO000OO00 ,"description":O0O0OO00O000O0000 ,"url":OOOO0OOOOOO0OO0OO ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:92
    O0OOO000O0O00O00O =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:93
    O0O0O000O00O00O0O =requests .post (O0OOO000O0O00O00O ,data =json .dumps (OOOOO00OOO00O0O00 )).json ()#line:94
    if O0O0O000O00O00O0O .get ('errcode')!=0 :#line:95
        print ('消息发送失败，请检查key和发送格式')#line:96
        return False #line:97
    return O0O0O000O00O00O0O #line:98
def getmpinfo (O0OOO00O0O0000O00 ):#line:101
    if not O0OOO00O0O0000O00 or O0OOO00O0O0000O00 =='':#line:102
        return False #line:103
    O0O0OOOO0000O00O0 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:105
    O0O0O00OO000O00O0 =requests .get (O0OOO00O0O0000O00 ,headers =O0O0OOOO0000O00O0 )#line:106
    OO000OOO0O0O0O00O =etree .HTML (O0O0O00OO000O00O0 .text )#line:107
    OOO0OO0O00O00OO00 =OO000OOO0O0O0O00O .xpath ('//meta[@*="og:title"]/@content')#line:109
    if OOO0OO0O00O00OO00 :#line:110
        OOO0OO0O00O00OO00 =OOO0OO0O00O00OO00 [0 ]#line:111
    O0000O0O0OO0OOOOO =OO000OOO0O0O0O00O .xpath ('//meta[@*="og:url"]/@content')#line:112
    if O0000O0O0OO0OOOOO :#line:113
        O0000O0O0OO0OOOOO =O0000O0O0OO0OOOOO [0 ].encode ().decode ()#line:114
    try :#line:115
        OO0O0OOOOO0OOO0O0 =re .findall (r'biz=(.*?)&',O0OOO00O0O0000O00 )[0 ]#line:116
    except :#line:117
        OO0O0OOOOO0OOO0O0 =re .findall (r'biz=(.*?)&',O0000O0O0OO0OOOOO )[0 ]#line:118
    if not OO0O0OOOOO0OOO0O0 :#line:119
        return False #line:120
    OO0OOO0OOOOOO00O0 =OO000OOO0O0O0O00O .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:121
    if OO0OOO0OOOOOO00O0 :#line:122
        OO0OOO0OOOOOO00O0 =OO0OOO0OOOOOO00O0 [0 ].strip ()#line:123
    O0O00000O00O0O0OO =re .findall (r"user_name.DATA'\) : '(.*?)'",O0O0O00OO000O00O0 .text )or OO000OOO0O0O0O00O .xpath ('//span[@class="profile_meta_value"]/text()')#line:125
    if O0O00000O00O0O0OO :#line:126
        O0O00000O00O0O0OO =O0O00000O00O0O0OO [0 ]#line:127
    O0OO0000O0000000O =re .findall (r'createTime = \'(.*)\'',O0O0O00OO000O00O0 .text )#line:128
    if O0OO0000O0000000O :#line:129
        O0OO0000O0000000O =O0OO0000O0000000O [0 ][5 :]#line:130
    OO000O0O00OOOO0OO =f'{O0OO0000O0000000O} {OOO0OO0O00O00OO00}'#line:131
    O0OOO0O0OO0O0OO0O ={'biz':OO0O0OOOOO0OOO0O0 ,'text':OO000O0O00OOOO0OO }#line:132
    return O0OOO0O0OO0O0OO0O #line:133
class Allinone :#line:136
    def __init__ (O000O00O0OO0OOO00 ,OOOO00O00OOO00OOO ):#line:137
        O000O00O0OO0OOO00 .name =OOOO00O00OOO00OOO ['name']#line:138
        O000O00O0OO0OOO00 .s =requests .session ()#line:139
        O000O00O0OO0OOO00 .payload ={"un":OOOO00O00OOO00OOO ['un'],"token":OOOO00O00OOO00OOO ['token'],"pageSize":20 }#line:140
        O000O00O0OO0OOO00 .s .headers ={'Accept':'application/json, text/javascript, */*; q=0.01','Content-Type':'application/json; charset=UTF-8','Host':'u.cocozx.cn','Connection':'keep-alive','Origin':'http://mr1694957965536.qwydu.com','User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",'Accept-Encoding':'gzip, deflate'}#line:147
        O000O00O0OO0OOO00 .headers =O000O00O0OO0OOO00 .s .headers .copy ()#line:148
        O000O00O0OO0OOO00 .msg =''#line:149
    def get_readhost (OOOO00OOO00O0OO00 ):#line:151
        O000OOO0OO00OOO0O ="http://u.cocozx.cn/api/oz/getReadHost"#line:152
        O0O0OO0OOO0O0OOOO =OOOO00OOO00O0OO00 .s .post (O000OOO0OO00OOO0O ,json =OOOO00OOO00O0OO00 .payload ).json ()#line:153
        debugger (f'readhome {O0O0OO0OOO0O0OOOO}')#line:154
        OOOO00OOO00O0OO00 .readhost =O0O0OO0OOO0O0OOOO .get ('result')['host']#line:155
        OOOO00OOO00O0OO00 .headers ['Origin']=OOOO00OOO00O0OO00 .readhost #line:156
        OOOO00OOO00O0OO00 .msg +=f'邀请链接：{OOOO00OOO00O0OO00.readhost}/oz/index.html?mid={OOOO00OOO00O0OO00.huid}\n'#line:157
        printlog (f"{OOOO00OOO00O0OO00.name}:邀请链接：{OOOO00OOO00O0OO00.readhost}/oz/index.html?mid={OOOO00OOO00O0OO00.huid}")#line:158
    def get_info (OO0O00O00OOOO0OOO ):#line:160
        O000O000000O0OO00 ='\u0034\u0033\u0033\u0057\u0048\u004d\u0032\u0056\u0057'if OO0O00O00OOOO0OOO .name =='AI'else '\u0034\u0047\u0037\u0051\u0055\u005a\u0059\u0038\u0059'#line:161
        OOOOO0O0OO0OOOO0O ={**OO0O00O00OOOO0OOO .payload ,**{'\u0063\u006f\u0064\u0065':O000O000000O0OO00 }}#line:162
        try :#line:163
            O0O0O0000O0O00O00 =OO0O00O00OOOO0OOO .s .post ("http://u.cocozx.cn/api/oz/info",json =OOOOO0O0OO0OOOO0O ).json ()#line:164
            OO00000O00O00OO00 =O0O0O0000O0O00O00 .get ("result")#line:165
            debugger (f'get_info {O0O0O0000O0O00O00}')#line:166
            OOOO00000O0OO0OOO =OO00000O00O00OO00 .get ('us')#line:167
            if OOOO00000O0OO0OOO ==2 :#line:168
                OO0O00O00OOOO0OOO .msg +=f'{OO0O00O00OOOO0OOO.name}已被封\n'#line:169
                printlog (f'{OO0O00O00OOOO0OOO.name}已被封')#line:170
                return False #line:171
            OO0O00O00OOOO0OOO .msg +=f"""{OO0O00O00OOOO0OOO.name}:今日阅读次数:{OO00000O00O00OO00["dayCount"]}，当前智慧:{OO00000O00O00OO00["moneyCurrent"]}，累计阅读次数:{OO00000O00O00OO00["doneWx"]}\n"""#line:172
            printlog (f"""{OO0O00O00OOOO0OOO.name}:今日阅读次数:{OO00000O00O00OO00["dayCount"]}，当前智慧:{OO00000O00O00OO00["moneyCurrent"]}，累计阅读次数:{OO00000O00O00OO00["doneWx"]}""")#line:174
            OOOOOOO00OOO0O0O0 =int (OO00000O00O00OO00 ["moneyCurrent"])#line:175
            OO0O00O00OOOO0OOO .huid =OO00000O00O00OO00 .get ('uid')#line:176
            return OOOOOOO00OOO0O0O0 #line:177
        except :#line:178
            return False #line:179
    def get_status (O0OO0000O0OOO0000 ):#line:181
        O0O00O0O000O0OOO0 =requests .post ("http://u.cocozx.cn/api/oz/read",headers =O0OO0000O0OOO0000 .headers ,json =O0OO0000O0OOO0000 .payload ).json ()#line:182
        debugger (f'getstatus {O0O00O0O000O0OOO0}')#line:183
        O0OO0000O0OOO0000 .status =O0O00O0O000O0OOO0 .get ("result").get ("status")#line:184
        if O0OO0000O0OOO0000 .status ==40 :#line:185
            O0OO0000O0OOO0000 .msg +="文章还没有准备好\n"#line:186
            printlog (f"{O0OO0000O0OOO0000.name}:文章还没有准备好")#line:187
            return #line:188
        elif O0OO0000O0OOO0000 .status ==50 :#line:189
            O0OO0000O0OOO0000 .msg +="阅读失效\n"#line:190
            printlog (f"{O0OO0000O0OOO0000.name}:阅读失效")#line:191
            return #line:192
        elif O0OO0000O0OOO0000 .status ==60 :#line:193
            O0OO0000O0OOO0000 .msg +="已经全部阅读完了\n"#line:194
            printlog (f"{O0OO0000O0OOO0000.name}:已经全部阅读完了")#line:195
            return #line:196
        elif O0OO0000O0OOO0000 .status ==70 :#line:197
            O0OO0000O0OOO0000 .msg +="下一轮还未开启\n"#line:198
            printlog (f"{O0OO0000O0OOO0000.name}:下一轮还未开启")#line:199
            return #line:200
        elif O0OO0000O0OOO0000 .status ==10 :#line:201
            OOOO0000000000OO0 =O0O00O0O000O0OOO0 ["result"]["url"]#line:202
            O0OO0000O0OOO0000 .msg +='-'*50 +"\n阅读链接获取成功\n"#line:203
            return OOOO0000000000OO0 #line:204
    def submit (O0OOO000O0000O0OO ):#line:206
        OOO0000OOO0O00000 ={**{'type':1 },**O0OOO000O0000O0OO .payload }#line:207
        O0OO0OO0O0O000OO0 =requests .post ("http://u.cocozx.cn/api/oz/submit?zx=&xz=1",headers =O0OOO000O0000O0OO .headers ,json =OOO0000OOO0O00000 )#line:208
        O000000O0000000OO =O0OO0OO0O0O000OO0 .json ().get ('result')#line:209
        debugger ('submit '+O0OO0OO0O0O000OO0 .text )#line:210
        O0OOO000O0000O0OO .msg +=f"阅读成功,获得智慧{O000000O0000000OO['val']}，当前剩余次数:{O000000O0000000OO['progress']}\n"#line:211
        printlog (f"{O0OOO000O0000O0OO.name}:阅读成功,获得智慧{O000000O0000000OO['val']}，当前剩余次数:{O000000O0000000OO['progress']}")#line:212
    def read (OOOOO00OOO0O00OOO ):#line:214
        O00O00O00O00OO00O =1 #line:215
        while True :#line:216
            O00OOO0O0O00O0OOO =OOOOO00OOO0O00OOO .get_status ()#line:217
            if not O00OOO0O0O00O0OOO :#line:218
                if OOOOO00OOO0O00OOO .status ==30 :#line:219
                    time .sleep (3 )#line:220
                    continue #line:221
                break #line:222
            OOOOO0O0O00O0O0O0 =getmpinfo (O00OOO0O0O00O0OOO )#line:223
            OOOOO00OOO0O00OOO .msg +='开始阅读 '+OOOOO0O0O00O0O0O0 ['text']+'\n'#line:224
            printlog (f'{OOOOO00OOO0O00OOO.name}:开始阅读 '+OOOOO0O0O00O0O0O0 ['text'])#line:225
            OOOOO0OO0000OO0OO =randint (7 ,10 )#line:226
            if OOOOO0O0O00O0O0O0 ['biz']=="Mzg2Mzk3Mjk5NQ==":#line:227
                OOOOO00OOO0O00OOO .msg +='当前正在阅读检测文章\n'#line:228
                printlog (f'{OOOOO00OOO0O00OOO.name}:正在阅读检测文章')#line:229
                send (f'{OOOOO00OOO0O00OOO.name}  智慧阅读正在读检测文章',OOOOO0O0O00O0O0O0 ['text'],O00OOO0O0O00O0OOO )#line:230
                time .sleep (60 )#line:231
            time .sleep (OOOOO0OO0000OO0OO )#line:232
            OOOOO00OOO0O00OOO .submit ()#line:233
    def tixian (O000OO0O0O0O0O0OO ):#line:235
        global txe #line:236
        OO00OO0OOO0O0OO00 =O000OO0O0O0O0O0OO .get_info ()#line:237
        if OO00OO0OOO0O0OO00 <txbz :#line:238
            O000OO0O0O0O0O0OO .msg +='你的智慧不多了\n'#line:239
            printlog (f'{O000OO0O0O0O0O0OO.name}:你的智慧不多了')#line:240
            return False #line:241
        elif 10000 <=OO00OO0OOO0O0OO00 <49999 :#line:242
            txe =10000 #line:243
        elif 50000 <=OO00OO0OOO0O0OO00 <100000 :#line:244
            txe =50000 #line:245
        elif 3000 <=OO00OO0OOO0O0OO00 <10000 :#line:246
            txe =3000 #line:247
        elif OO00OO0OOO0O0OO00 >=100000 :#line:248
            txe =100000 #line:249
        O000OO0O0O0O0O0OO .msg +=f"提现金额:{txe}\n"#line:250
        printlog (f'{O000OO0O0O0O0O0OO.name}:提现金额 {txe}')#line:251
        O00O0O0OO00O000OO ={**O000OO0O0O0O0O0OO .payload ,**{"val":txe }}#line:252
        try :#line:253
            OOO00O00OO0OO00OO =O000OO0O0O0O0O0OO .s .post ("http://u.cocozx.cn/api/oz/wdmoney",json =O00O0O0OO00O000OO ).json ()#line:254
            O000OO0O0O0O0O0OO .msg +=f'提现结果：{OOO00O00OO0OO00OO.get("msg")}\n'#line:255
            printlog (f'{O000OO0O0O0O0O0OO.name}:提现结果 {OOO00O00OO0OO00OO.get("msg")}')#line:256
        except :#line:257
            O000OO0O0O0O0O0OO .msg +=f"自动提现不成功，发送通知手动提现\n"#line:258
            printlog (f"{O000OO0O0O0O0O0OO.name}:自动提现不成功，发送通知手动提现")#line:259
            send (f'可提现金额 {int(txe) / 10000}元，点击提现',f'惜之酱提醒您 {O000OO0O0O0O0O0OO.name} 智慧阅读可以提现了',f'{O000OO0O0O0O0O0OO.readhost}/oz/index.html?mid=QX5E9WLGS')#line:261
    def run (O00O0O0OOOO00OOO0 ):#line:263
        O00O0O0OOOO00OOO0 .msg +='*'*50 +'\n'#line:264
        if O00O0O0OOOO00OOO0 .get_info ():#line:265
            O00O0O0OOOO00OOO0 .get_readhost ()#line:266
            O00O0O0OOOO00OOO0 .read ()#line:267
            O00O0O0OOOO00OOO0 .tixian ()#line:268
        if not printf :#line:269
            print (O00O0O0OOOO00OOO0 .msg .strip ())#line:270
def yd (OOO00000000OOO0OO ):#line:273
    while not OOO00000000OOO0OO .empty ():#line:274
        O0O0O0000O0O0OOO0 =OOO00000000OOO0OO .get ()#line:275
        OOO00OOOOOOOO0OOO =Allinone (O0O0O0000O0O0OOO0 )#line:276
        OOO00OOOOOOOO0OOO .run ()#line:277
def get_info ():#line:280
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:282
    print ('入口：http://mr181125495.forsranaa.cloud/oz/index.html?mid=4G7QUZY8Y')#line:283
    OOOO0O0000O0OOO00 ='V1.3'#line:284
    O00000000OOO000O0 =_O0O0O0O0OOOOOO0OO ['version'].get ('k_zh')or _O0O0O0O0OOOOOO0OO ['version']['kzh']#line:285
    print (f'当前版本{OOOO0O0000O0OOO00}，仓库版本{O00000000OOO000O0}\n{_O0O0O0O0OOOOOO0OO["update_log"]["花花"]}')#line:286
    if OOOO0O0000O0OOO00 <O00000000OOO000O0 :#line:287
        print ('请到仓库下载最新版本k_zh.py')#line:288
def main ():#line:292
    get_info ()#line:293
    OO0O00000OOOOOOOO =os .getenv ('zhck')#line:294
    if not OO0O00000OOOOOOOO :#line:295
        OO0O00000OOOOOOOO =os .getenv ('aiock')#line:296
        if not OO0O00000OOOOOOOO :#line:297
            print (_O0O0O0O0OOOOOO0OO .get ('msg')['智慧'])#line:298
            exit ()#line:299
    try :#line:300
        OO0O00000OOOOOOOO =ast .literal_eval (OO0O00000OOOOOOOO )#line:301
    except :#line:302
        pass #line:303
    print ('-'*20 )#line:304
    print (f'共获取到{len(OO0O00000OOOOOOOO)}个账号，如与实际不符，请检查ck填写方式')#line:305
    print ("="*25 )#line:306
    O000000O00OOOO00O =Queue ()#line:307
    OO0O00000O00O00O0 =[]#line:308
    for OOO0O0O00O0OO0000 ,O00OO0O0O000OO0O0 in enumerate (OO0O00000OOOOOOOO ,start =1 ):#line:309
        O000000O00OOOO00O .put (O00OO0O0O000OO0O0 )#line:310
    for OOO0O0O00O0OO0000 in range (max_workers ):#line:311
        O0OOO00O00O0OOO0O =threading .Thread (target =yd ,args =(O000000O00OOOO00O ,))#line:312
        O0OOO00O00O0OOO0O .start ()#line:313
        OO0O00000O00O00O0 .append (O0OOO00O00O0OOO0O )#line:314
        time .sleep (delay_time )#line:315
    for OOOO00O000OOO0000 in OO0O00000O00O00O0 :#line:316
        OOOO00O000OOO0000 .join ()#line:317
if __name__ =='__main__':#line:320
    main ()#line:321
