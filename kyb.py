# -*- coding: utf-8 -*-
# 元宝阅读多线程单文件版
# Author: kk
# date：2023/9/18 20:45
"""
元宝阅读入口：http://mr139508131.cwejqylmo.cloud/coin/index.html?mid=CS5T87Q98
http://u.cocozx.cn/api/ox/info
抓包 info接口的请求体中的un和token参数

注意：脚本变量使用的单引号、双引号、逗号都是英文状态的
注意：脚本变量使用的单引号、双引号、逗号都是英文状态的
注意：脚本变量使用的单引号、双引号、逗号都是英文状态的
------------------------------------------------------
内置推送企业微信群机器人
参考 https://github.com/kxs2018/yuedu/blob/main/获取企业微信群机器人key.md 获取key，并关注插件！！！

青龙配置文件
export aiock="[{'un': 'xxxx', 'token': 'xxxxx','name':'彦祖'},{'un': 'xxxx', 'token': 'xxxxx','name':'彦祖'},{'un': 'xxxx', 'token': 'xxxxx','name':'彦祖'},]"

export qwbotkey="abcdefg"
------------------------------------------------------
no module named lxml 解决方案
1. 配置文件搜索 PipMirror，如果网址包含douban的，请改为下方的网址
PipMirror="https://pypi.tuna.tsinghua.edu.cn/simple"
2. 依赖管理-python 添加 lxml
3. 如果装不上，①请ssh连接到服务器 ②docker exec -it ql bash (ql是青龙容器的名字，不会问百度) ③pip install pip -U
4. 再装不上依赖就放弃吧
------------------------------------------------------
提现标准默认是3000
达到标准自动提现
"""
import json
from random import randint
import os
import time
import requests
import ast
import re

try:
    from lxml import etree
except:
    print('请仔细阅读脚本上方注释中的“no module named lxml 解决方案”')
    exit()
import datetime
import threading
from queue import Queue

"""实时打印日志开关"""
printf = 1
"""1为开，0为关"""

"""debug模式开关"""
debug = 0
"""1为开，打印调试日志；0为关，不打印"""

"""线程数量设置"""
max_workers = 3
"""设置为3，即最多有3个任务同时进行"""

"""设置提现标准"""
txbz = 10000  # 不低于3000，平台的提现标准为3000
"""设置为10000，即为1元起提"""

qwbotkey = os.getenv('qwbotkey')  # line:65
if not qwbotkey:  # line:66
    print('请仔细阅读脚本开头的注释并配置好qwbotkey')  # line:67
    exit()  # line:68


def ftime ():#line:71
    O000O000O0O00OOOO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:72
    return O000O000O0O00OOOO #line:73
def printlog (OOO0O0OO0O00O0000 ):#line:76
    if printf :#line:77
        print (OOO0O0OO0O00O0000 )#line:78
def debugger (OO000000O0OO00O0O ):#line:81
    if debug :#line:82
        print (OO000000O0OO00O0O )#line:83
def send (OOOOO000OOOOOO0OO ,title ='通知',url =None ):#line:86
    if not title or not url :#line:87
        O0O000000000OO00O ={"msgtype":"text","text":{"content":f"{title}\n\n{OOOOO000OOOOOO0OO}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:94
    else :#line:95
        O0O000000000OO00O ={"msgtype":"news","news":{"articles":[{"title":title ,"description":OOOOO000OOOOOO0OO ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:108
    O00O00OOOO0O0O00O =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:109
    OO0O0OO0OO0OO0000 =requests .post (O00O00OOOO0O0O00O ,data =json .dumps (O0O000000000OO00O )).json ()#line:110
    if OO0O0OO0OO0OO0000 .get ('errcode')!=0 :#line:111
        print ('消息发送失败，请检查key和发送格式')#line:112
        return False #line:113
    return OO0O0OO0OO0OO0000 #line:114
def getmpinfo (O0OO000O00O0OOO0O ):#line:117
    if not O0OO000O00O0OOO0O or O0OO000O00O0OOO0O =='':#line:118
        return False #line:119
    O0O000OOO0000OOO0 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:121
    OOOO0000O0O00O0OO =requests .get (O0OO000O00O0OOO0O ,headers =O0O000OOO0000OOO0 )#line:122
    O000O00OOOO00O0OO =etree .HTML (OOOO0000O0O00O0OO .text )#line:123
    OO00OO0O00O0O0OOO =O000O00OOOO00O0OO .xpath ('//meta[@*="og:title"]/@content')#line:125
    if OO00OO0O00O0O0OOO :#line:126
        OO00OO0O00O0O0OOO =OO00OO0O00O0O0OOO [0 ]#line:127
    O0O0O000OOO0O0OOO =O000O00OOOO00O0OO .xpath ('//meta[@*="og:url"]/@content')#line:128
    if O0O0O000OOO0O0OOO :#line:129
        O0O0O000OOO0O0OOO =O0O0O000OOO0O0OOO [0 ].encode ().decode ()#line:130
    try :#line:131
        O0O00000OOO0OO0O0 =re .findall (r'biz=(.*?)&',O0OO000O00O0OOO0O )[0 ]#line:132
    except :#line:133
        O0O00000OOO0OO0O0 =re .findall (r'biz=(.*?)&',O0O0O000OOO0O0OOO )[0 ]#line:134
    if not O0O00000OOO0OO0O0 :#line:135
        return False #line:136
    O000OO00OO000O0OO =O000O00OOOO00O0OO .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:137
    if O000OO00OO000O0OO :#line:138
        O000OO00OO000O0OO =O000OO00OO000O0OO [0 ].strip ()#line:139
    OO000OO0O00O0O00O =re .findall (r"user_name.DATA'\) : '(.*?)'",OOOO0000O0O00O0OO .text )or O000O00OOOO00O0OO .xpath ('//span[@class="profile_meta_value"]/text()')#line:141
    if OO000OO0O00O0O00O :#line:142
        OO000OO0O00O0O00O =OO000OO0O00O0O00O [0 ]#line:143
    OOO000O0OO0OO0000 =re .findall (r'createTime = \'(.*)\'',OOOO0000O0O00O0OO .text )#line:144
    if OOO000O0OO0OO0000 :#line:145
        OOO000O0OO0OO0000 =OOO000O0OO0OO0000 [0 ][5 :]#line:146
    O0O00000O0OO0OOO0 =f'{OOO000O0OO0OO0000}|{OO00OO0O00O0O0OOO}'#line:147
    O000000OOOOO00OOO ={'biz':O0O00000OOO0OO0O0 ,'text':O0O00000O0OO0OOO0 }#line:148
    return O000000OOOOO00OOO #line:149
class Allinone :#line:152
    def __init__ (OOOO0000O00O00OO0 ,O0O0O000O0OO0000O ):#line:153
        OOOO0000O00O00OO0 .name =O0O0O000O0OO0000O ['name']#line:154
        OOOO0000O00O00OO0 .s =requests .session ()#line:155
        OOOO0000O00O00OO0 .payload ={"un":O0O0O000O0OO0000O ['un'],"token":O0O0O000O0OO0000O ['token'],"pageSize":20 }#line:156
        OOOO0000O00O00OO0 .s .headers ={'Accept':'application/json, text/javascript, */*; q=0.01','Content-Type':'application/json; charset=UTF-8','Host':'u.cocozx.cn','Connection':'keep-alive','User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",'Accept-Encoding':'gzip, deflate'}#line:162
        OOOO0000O00O00OO0 .msg =''#line:163
    def get_info (O0OO0OOO0000OOO0O ):#line:165
        OOO00000O0OOOOO0O ='CS5T87Q98'if O0OO0OOO0000OOO0O .name =='AI'else 'DG52AW2N6'#line:166
        O0OOOOO00OOOO0O0O ={**O0OO0OOO0000OOO0O .payload ,**{'code':OOO00000O0OOOOO0O }}#line:167
        try :#line:168
            O0OO00OO000OOOOO0 =O0OO0OOO0000OOO0O .s .post ("http://u.cocozx.cn/api/coin/info",json =O0OOOOO00OOOO0O0O ).json ()#line:169
            OO0O00OOOOO0O0OOO =O0OO00OO000OOOOO0 .get ("result")#line:170
            debugger (f'get_info {O0OO00OO000OOOOO0}')#line:171
            O0000O0O0O00OOOOO =OO0O00OOOOO0O0OOO .get ('us')#line:172
            if O0000O0O0O00OOOOO ==2 :#line:173
                O0OO0OOO0000OOO0O .msg +=f'账号：{O0OO0OOO0000OOO0O.name}已被封\n'#line:174
                printlog (f'账号：{O0OO0OOO0000OOO0O.name}已被封')#line:175
                return False #line:176
            O0OO0OOO0000OOO0O .msg +=f"""账号:{O0OO0OOO0000OOO0O.name}，今日阅读次数:{OO0O00OOOOO0O0OOO["dayCount"]}，当前元宝:{OO0O00OOOOO0O0OOO["moneyCurrent"]}，累计阅读次数:{OO0O00OOOOO0O0OOO["doneWx"]}\n"""#line:178
            printlog (f"""账号:{O0OO0OOO0000OOO0O.name}，今日阅读次数:{OO0O00OOOOO0O0OOO["dayCount"]}，当前元宝:{OO0O00OOOOO0O0OOO["moneyCurrent"]}，累计阅读次数:{OO0O00OOOOO0O0OOO["doneWx"]}""")#line:180
            O0OO00O0O00000OO0 =int (OO0O00OOOOO0O0OOO ["moneyCurrent"])#line:181
            O0OO0OOO0000OOO0O .huid =OO0O00OOOOO0O0OOO .get ('uid')#line:182
            return O0OO00O0O00000OO0 #line:183
        except :#line:184
            return False #line:185
    def get_readhost (O00O00O0000OO0O00 ):#line:187
        O00OOOOO0O0O0OOOO ="http://u.cocozx.cn/api/coin/getReadHost"#line:188
        OOOOOO0O000OO0000 =O00O00O0000OO0O00 .s .post (O00OOOOO0O0O0OOOO ,json =O00O00O0000OO0O00 .payload ).json ()#line:189
        debugger (f'readhome {OOOOOO0O000OO0000}')#line:190
        O00O00O0000OO0O00 .readhost =OOOOOO0O000OO0000 .get ('result')['host']#line:191
        O00O00O0000OO0O00 .msg +=f'邀请链接：{O00O00O0000OO0O00.readhost}/oz/index.html?mid={O00O00O0000OO0O00.huid}\n'#line:192
        printlog (f"{O00O00O0000OO0O00.name}:邀请链接：{O00O00O0000OO0O00.readhost}/oz/index.html?mid={O00O00O0000OO0O00.huid}")#line:193
    def get_status (O00OO00O000O0O0O0 ):#line:195
        O000O0OO0O0OOO000 =O00OO00O000O0O0O0 .s .post ("http://u.cocozx.cn/api/coin/read",json =O00OO00O000O0O0O0 .payload ).json ()#line:196
        debugger (f'getstatus {O000O0OO0O0OOO000}')#line:197
        O00OO00O000O0O0O0 .status =O000O0OO0O0OOO000 .get ("result").get ("status")#line:198
        if O00OO00O000O0O0O0 .status ==40 :#line:199
            O00OO00O000O0O0O0 .msg +="文章还没有准备好\n"#line:200
            printlog (f"{O00OO00O000O0O0O0.name}:文章还没有准备好")#line:201
            return #line:202
        elif O00OO00O000O0O0O0 .status ==50 :#line:203
            O00OO00O000O0O0O0 .msg +="阅读失效\n"#line:204
            printlog (f"{O00OO00O000O0O0O0.name}:阅读失效")#line:205
            return #line:206
        elif O00OO00O000O0O0O0 .status ==60 :#line:207
            O00OO00O000O0O0O0 .msg +="已经全部阅读完了\n"#line:208
            printlog (f"{O00OO00O000O0O0O0.name}:已经全部阅读完了")#line:209
            return #line:210
        elif O00OO00O000O0O0O0 .status ==70 :#line:211
            O00OO00O000O0O0O0 .msg +="下一轮还未开启\n"#line:212
            printlog (f"{O00OO00O000O0O0O0.name}:下一轮还未开启")#line:213
            return #line:214
        elif O00OO00O000O0O0O0 .status ==10 :#line:215
            OO0OOO0OOOO0OOOO0 =O000O0OO0O0OOO000 ["result"]["url"]#line:216
            O00OO00O000O0O0O0 .msg +='-'*50 +"\n阅读链接获取成功\n"#line:217
            printlog (f"{O00OO00O000O0O0O0.name}: 阅读链接获取成功")#line:218
            return OO0OOO0OOOO0OOOO0 #line:219
    def submit (OOOOO000000000OO0 ):#line:221
        OOOO0O0O0O0OOOOO0 ={**{'type':1 },**OOOOO000000000OO0 .payload }#line:222
        OO0O0O0OO0O0O00OO =OOOOO000000000OO0 .s .post ("http://u.cocozx.cn/api/coin/submit?zx=&xz=1",json =OOOO0O0O0O0OOOOO0 )#line:223
        O0OOOO00O0O0OOOO0 =OO0O0O0OO0O0O00OO .json ().get ('result')#line:224
        debugger ('submit '+OO0O0O0OO0O0O00OO .text )#line:225
        OOOOO000000000OO0 .msg +=f"阅读成功,获得元宝{O0OOOO00O0O0OOOO0['val']}，当前剩余次数:{O0OOOO00O0O0OOOO0['progress']}\n"#line:226
        printlog (f"{OOOOO000000000OO0.name}:阅读成功,获得元宝{O0OOOO00O0O0OOOO0['val']}，当前剩余次数:{O0OOOO00O0O0OOOO0['progress']}")#line:227
    def read (O00O0OOOOO0OO00O0 ):#line:229
        while True :#line:230
            OOO00O00O0O0OOOO0 =O00O0OOOOO0OO00O0 .get_status ()#line:231
            if not OOO00O00O0O0OOOO0 :#line:232
                if O00O0OOOOO0OO00O0 .status ==30 :#line:233
                    time .sleep (3 )#line:234
                    continue #line:235
                break #line:236
            O00OO00OO0O00O00O =getmpinfo (OOO00O00O0O0OOOO0 )#line:237
            if not O00OO00OO0O00O00O :#line:238
                printlog (f'{O00O0OOOOO0OO00O0.name}:获取文章信息失败，程序中止')#line:239
                return False #line:240
            O00O0OOOOO0OO00O0 .msg +='开始阅读 '+O00OO00OO0O00O00O ['text']+'\n'#line:241
            printlog (f'{O00O0OOOOO0OO00O0.name}:开始阅读 '+O00OO00OO0O00O00O ['text'])#line:242
            OOO0OOOOO0OO0OOOO =randint (7 ,10 )#line:243
            if O00OO00OO0O00O00O ['biz']=="Mzg2Mzk3Mjk5NQ==":#line:244
                O00O0OOOOO0OO00O0 .msg +='正在阅读检测文章\n'#line:245
                printlog (f'{O00O0OOOOO0OO00O0.name}:正在阅读检测文章')#line:246
                send (f'{O00O0OOOOO0OO00O0.name}  元宝阅读过检测',O00OO00OO0O00O00O ['text'],OOO00O00O0O0OOOO0 )#line:247
                time .sleep (60 )#line:248
            printlog (f'模拟阅读{OOO0OOOOO0OO0OOOO}秒')#line:249
            time .sleep (OOO0OOOOO0OO0OOOO )#line:250
            O00O0OOOOO0OO00O0 .submit ()#line:251
    def tixian (O00O0O0OO0000O0OO ):#line:253
        global txe #line:254
        O00O0000O00OO0OOO =O00O0O0OO0000O0OO .get_info ()#line:255
        if O00O0000O00OO0OOO <txbz :#line:256
            O00O0O0OO0000O0OO .msg +='你的元宝已不足\n'#line:257
            printlog (f'{O00O0O0OO0000O0OO.name}你的元宝已不足')#line:258
            return False #line:259
        elif 10000 <=O00O0000O00OO0OOO <49999 :#line:260
            txe =10000 #line:261
        elif 50000 <=O00O0000O00OO0OOO <100000 :#line:262
            txe =50000 #line:263
        elif 3000 <=O00O0000O00OO0OOO <10000 :#line:264
            txe =3000 #line:265
        elif O00O0000O00OO0OOO >=100000 :#line:266
            txe =100000 #line:267
        O00O0O0OO0000O0OO .msg +=f"提现金额:{txe}\n"#line:268
        printlog (f'{O00O0O0OO0000O0OO.name}提现金额:{txe}')#line:269
        OOO000O0O0O000OO0 ="http://u.cocozx.cn/api/coin/wdmoney"#line:270
        OOO00OOOOOOO0O000 ={**O00O0O0OO0000O0OO .payload ,**{"val":txe }}#line:271
        try :#line:272
            OOOOO00O0000OO00O =O00O0O0OO0000O0OO .s .post (OOO000O0O0O000OO0 ,json =OOO00OOOOOOO0O000 ).json ()#line:273
            O00O0O0OO0000O0OO .msg +=f'提现结果：{OOOOO00O0000OO00O.get("msg")}\n'#line:274
            printlog (f'{O00O0O0OO0000O0OO.name}提现结果：{OOOOO00O0000OO00O.get("msg")}')#line:275
        except :#line:276
            O00O0O0OO0000O0OO .msg +=f"自动提现不成功，发送通知手动提现\n"#line:277
            printlog (f"{O00O0O0OO0000O0OO.name}:自动提现不成功，发送通知手动提现")#line:278
            send (f'可提现金额 {int(txe) / 10000}元，点击提现',title =f'惜之酱提醒您 {O00O0O0OO0000O0OO.name} 元宝阅读可以提现了',url =f'{O00O0O0OO0000O0OO.readhost}/coin/index.html?mid=CS5T87Q98')#line:280
    def run (OOOOOO00000O0000O ):#line:282
        if OOOOOO00000O0000O .get_info ():#line:283
            OOOOOO00000O0000O .get_readhost ()#line:284
            OOOOOO00000O0000O .read ()#line:285
            OOOOOO00000O0000O .tixian ()#line:286
        if not printf :#line:287
            print (OOOOOO00000O0000O .msg .strip ())#line:288
def yd (O0O0OOOOOO0O00OOO ):#line:291
    while not O0O0OOOOOO0O00OOO .empty ():#line:292
        OO0OOOO000OO000OO =O0O0OOOOOO0O00OOO .get ()#line:293
        OOO000O000OOOOO00 =Allinone (OO0OOOO000OO000OO )#line:294
        OOO000O000OOOOO00 .run ()#line:295
def get_ver ():#line:298
    OOO00OO00O0O0O0OO ='kyb V1.2.2'#line:299
    O0000O000O00O00OO ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:302
    OOOOO00OOOOOO000O =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O0000O000O00O00OO ).json ()#line:304
    OOOOO0OO0O0O00OO0 =OOO00OO00O0O0O0OO .split (' ')[1 ]#line:305
    O0O00OO000OOOO0OO =OOOOO00OOOOOO000O .get ('version').get (OOO00OO00O0O0O0OO .split (' ')[0 ])#line:306
    OOO0OO0OO00000OO0 =f"当前版本 {OOOOO0OO0O0O00OO0}，仓库版本 {O0O00OO000OOOO0OO}"#line:307
    if OOOOO0OO0O0O00OO0 <O0O00OO000OOOO0OO :#line:308
        OOO0OO0OO00000OO0 +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:309
    return OOO0OO0OO00000OO0 #line:310
def main ():#line:313
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:314
    OO0OOOO0O0OOO0O0O =os .getenv ('aiock')#line:315
    if not OO0OOOO0O0OOO0O0O :#line:316
        print ('请仔细阅读脚本开头的注释并配置好aiock')#line:317
        exit ()#line:318
    try :#line:319
        OO0OOOO0O0OOO0O0O =ast .literal_eval (OO0OOOO0O0OOO0O0O )#line:320
    except :#line:321
        pass #line:322
    OOO0OO0O0OOOOOOO0 =Queue ()#line:323
    OO00OOO000O0OO0O0 =[]#line:324
    for O0OOOOO0OOO00O0O0 ,OO000O0OOO0OO000O in enumerate (OO0OOOO0O0OOO0O0O ,start =1 ):#line:325
        printlog (f'{OO000O0OOO0OO000O}\n以上是账号{O0OOOOO0OOO00O0O0}的ck，请核对是否正确，如不正确，请检查ck填写格式')#line:326
        OOO0OO0O0OOOOOOO0 .put (OO000O0OOO0OO000O )#line:327
    for O0OOOOO0OOO00O0O0 in range (max_workers ):#line:328
        O00O0O0O00000O0OO =threading .Thread (target =yd ,args =(OOO0OO0O0OOOOOOO0 ,))#line:329
        O00O0O0O00000O0OO .start ()#line:330
        OO00OOO000O0OO0O0 .append (O00O0O0O00000O0OO )#line:331
        time .sleep (30 )#line:332
    for O00000O0OOO0O000O in OO00OOO000O0OO0O0 :#line:333
        O00000O0OOO0O000O .join ()#line:334
if __name__ =='__main__':#line:337
    main ()#line:338
