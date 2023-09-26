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

qwbotkey =os .getenv ('qwbotkey')#line:65
if not qwbotkey :#line:66
    print ('请仔细阅读脚本开头的注释并配置好qwbotkey')#line:67
    exit ()#line:68
def ftime ():#line:71
    OOOOOO0OO0O0O0OO0 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:72
    return OOOOOO0OO0O0O0OO0 #line:73
def printlog (O0O0OOOO0OO00OO0O ):#line:76
    if printf :#line:77
        print (O0O0OOOO0OO00OO0O )#line:78
def debugger (OOOO00OO00OOOOO0O ):#line:81
    if debug :#line:82
        print (OOOO00OO00OOOOO0O )#line:83
def send (O0OOO000000O000OO ,title ='通知',url =None ):#line:86
    if not title or not url :#line:87
        OO000OO000OO00OO0 ={"msgtype":"text","text":{"content":f"{title}\n\n{O0OOO000000O000OO}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:94
    else :#line:95
        OO000OO000OO00OO0 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O0OOO000000O000OO ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:108
    OOOOOOOOOOO0O0OOO =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:109
    O000O0000O00OO00O =requests .post (OOOOOOOOOOO0O0OOO ,data =json .dumps (OO000OO000OO00OO0 )).json ()#line:110
    if O000O0000O00OO00O .get ('errcode')!=0 :#line:111
        print ('消息发送失败，请检查key和发送格式')#line:112
        return False #line:113
    return O000O0000O00OO00O #line:114
def getmpinfo (O00OO0O0OO0O0OO00 ):#line:117
    if not O00OO0O0OO0O0OO00 or O00OO0O0OO0O0OO00 =='':#line:118
        return False #line:119
    O0O000OOO000000O0 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:121
    OO0O0O000O0OO0O0O =requests .get (O00OO0O0OO0O0OO00 ,headers =O0O000OOO000000O0 )#line:122
    O0O0OOO0OO0O000OO =etree .HTML (OO0O0O000O0OO0O0O .text )#line:123
    O0O0O00OOO00OO0O0 =O0O0OOO0OO0O000OO .xpath ('//meta[@*="og:title"]/@content')#line:125
    if O0O0O00OOO00OO0O0 :#line:126
        O0O0O00OOO00OO0O0 =O0O0O00OOO00OO0O0 [0 ]#line:127
    OOOO00OOO0O0OO0O0 =O0O0OOO0OO0O000OO .xpath ('//meta[@*="og:url"]/@content')#line:128
    if OOOO00OOO0O0OO0O0 :#line:129
        OOOO00OOO0O0OO0O0 =OOOO00OOO0O0OO0O0 [0 ].encode ().decode ()#line:130
    try :#line:131
        OO00O0O0O0O00OO00 =re .findall (r'biz=(.*?)&',O00OO0O0OO0O0OO00 )#line:132
    except :#line:133
        OO00O0O0O0O00OO00 =re .findall (r'biz=(.*?)&',OOOO00OOO0O0OO0O0 )#line:134
    if OO00O0O0O0O00OO00 :#line:135
        OO00O0O0O0O00OO00 =OO00O0O0O0O00OO00 [0 ]#line:136
    else :#line:137
        return False #line:138
    OO00O0000OO0000OO =O0O0OOO0OO0O000OO .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:139
    if OO00O0000OO0000OO :#line:140
        OO00O0000OO0000OO =OO00O0000OO0000OO [0 ].strip ()#line:141
    O0O000OOO0OO0OO00 =re .findall (r"user_name.DATA'\) : '(.*?)'",OO0O0O000O0OO0O0O .text )or O0O0OOO0OO0O000OO .xpath ('//span[@class="profile_meta_value"]/text()')#line:143
    if O0O000OOO0OO0OO00 :#line:144
        O0O000OOO0OO0OO00 =O0O000OOO0OO0OO00 [0 ]#line:145
    OOOOO000O0O00OO0O =re .findall (r'createTime = \'(.*)\'',OO0O0O000O0OO0O0O .text )#line:146
    if OOOOO000O0O00OO0O :#line:147
        OOOOO000O0O00OO0O =OOOOO000O0O00OO0O [0 ][5 :]#line:148
    OO0O0O000O0O0O000 =f'{OOOOO000O0O00OO0O}|{O0O0O00OOO00OO0O0}'#line:149
    O0O00OOO00O0O0O0O ={'biz':OO00O0O0O0O00OO00 ,'text':OO0O0O000O0O0O000 }#line:150
    return O0O00OOO00O0O0O0O #line:151
class Allinone :#line:154
    def __init__ (O00O0O0OOOO00O0OO ,OO00OO0O00000OOO0 ):#line:155
        O00O0O0OOOO00O0OO .name =OO00OO0O00000OOO0 ['name']#line:156
        O00O0O0OOOO00O0OO .s =requests .session ()#line:157
        O00O0O0OOOO00O0OO .payload ={"un":OO00OO0O00000OOO0 ['un'],"token":OO00OO0O00000OOO0 ['token'],"pageSize":20 }#line:158
        O00O0O0OOOO00O0OO .s .headers ={'Accept':'application/json, text/javascript, */*; q=0.01','Content-Type':'application/json; charset=UTF-8','Host':'u.cocozx.cn','Connection':'keep-alive','User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",'Accept-Encoding':'gzip, deflate'}#line:164
        O00O0O0OOOO00O0OO .msg =''#line:165
    def get_info (O0O0O00OO00O0O00O ):#line:167
        O000O000OOO0O0000 ={**O0O0O00OO00O0O00O .payload ,**{'code':'CS5T87Q98'}}#line:168
        try :#line:169
            OO0000OOO00O0000O =O0O0O00OO00O0O00O .s .post ("http://u.cocozx.cn/api/coin/info",json =O000O000OOO0O0000 ).json ()#line:170
            O0O0OOOOOO000OOO0 =OO0000OOO00O0000O .get ("result")#line:171
            debugger (f'get_info {OO0000OOO00O0000O}')#line:172
            O0000000OOOOO00OO =O0O0OOOOOO000OOO0 .get ('us')#line:173
            if O0000000OOOOO00OO ==2 :#line:174
                O0O0O00OO00O0O00O .msg +=f'账号：{O0O0O00OO00O0O00O.name}已被封\n'#line:175
                printlog (f'账号：{O0O0O00OO00O0O00O.name}已被封')#line:176
                return False #line:177
            O0O0O00OO00O0O00O .msg +=f"""账号:{O0O0O00OO00O0O00O.name}，今日阅读次数:{O0O0OOOOOO000OOO0["dayCount"]}，当前元宝:{O0O0OOOOOO000OOO0["moneyCurrent"]}，累计阅读次数:{O0O0OOOOOO000OOO0["doneWx"]}\n"""#line:179
            printlog (f"""账号:{O0O0O00OO00O0O00O.name}，今日阅读次数:{O0O0OOOOOO000OOO0["dayCount"]}，当前元宝:{O0O0OOOOOO000OOO0["moneyCurrent"]}，累计阅读次数:{O0O0OOOOOO000OOO0["doneWx"]}""")#line:181
            OO00O0O0O0OOO0OO0 =int (O0O0OOOOOO000OOO0 ["moneyCurrent"])#line:182
            O0O0O00OO00O0O00O .huid =O0O0OOOOOO000OOO0 .get ('uid')#line:183
            return OO00O0O0O0OOO0OO0 #line:184
        except :#line:185
            return False #line:186
    def get_readhost (OOOOOOOOO0OO00OOO ):#line:188
        O0OO0OO0O0000OOO0 ="http://u.cocozx.cn/api/coin/getReadHost"#line:189
        O0O0OOO0OO0O0O00O =OOOOOOOOO0OO00OOO .s .post (O0OO0OO0O0000OOO0 ,json =OOOOOOOOO0OO00OOO .payload ).json ()#line:190
        debugger (f'readhome {O0O0OOO0OO0O0O00O}')#line:191
        OOOOOOOOO0OO00OOO .readhost =O0O0OOO0OO0O0O00O .get ('result')['host']#line:192
        OOOOOOOOO0OO00OOO .msg +=f'邀请链接：{OOOOOOOOO0OO00OOO.readhost}/oz/index.html?mid={OOOOOOOOO0OO00OOO.huid}\n'#line:193
        printlog (f"{OOOOOOOOO0OO00OOO.name}:邀请链接：{OOOOOOOOO0OO00OOO.readhost}/oz/index.html?mid={OOOOOOOOO0OO00OOO.huid}")#line:194
    def get_status (OO0O0000OO0O0O000 ):#line:196
        O00000OO0O0OOOO00 =OO0O0000OO0O0O000 .s .post ("http://u.cocozx.cn/api/coin/read",json =OO0O0000OO0O0O000 .payload ).json ()#line:197
        debugger (f'getstatus {O00000OO0O0OOOO00}')#line:198
        OO0O0000OO0O0O000 .status =O00000OO0O0OOOO00 .get ("result").get ("status")#line:199
        if OO0O0000OO0O0O000 .status ==40 :#line:200
            OO0O0000OO0O0O000 .msg +="文章还没有准备好\n"#line:201
            printlog (f"{OO0O0000OO0O0O000.name}:文章还没有准备好")#line:202
            return #line:203
        elif OO0O0000OO0O0O000 .status ==50 :#line:204
            OO0O0000OO0O0O000 .msg +="阅读失效\n"#line:205
            printlog (f"{OO0O0000OO0O0O000.name}:阅读失效")#line:206
            return #line:207
        elif OO0O0000OO0O0O000 .status ==60 :#line:208
            OO0O0000OO0O0O000 .msg +="已经全部阅读完了\n"#line:209
            printlog (f"{OO0O0000OO0O0O000.name}:已经全部阅读完了")#line:210
            return #line:211
        elif OO0O0000OO0O0O000 .status ==70 :#line:212
            OO0O0000OO0O0O000 .msg +="下一轮还未开启\n"#line:213
            printlog (f"{OO0O0000OO0O0O000.name}:下一轮还未开启")#line:214
            return #line:215
        elif OO0O0000OO0O0O000 .status ==10 :#line:216
            O0OO00OO0O000000O =O00000OO0O0OOOO00 ["result"]["url"]#line:217
            OO0O0000OO0O0O000 .msg +='-'*50 +"\n阅读链接获取成功\n"#line:218
            printlog (f"{OO0O0000OO0O0O000.name}: 阅读链接获取成功")#line:219
            return O0OO00OO0O000000O #line:220
    def submit (O00OO0OO00O0OO0OO ):#line:222
        OOOOOO0O00OOO0OO0 ={**{'type':1 },**O00OO0OO00O0OO0OO .payload }#line:223
        O0OOOO0O0000O000O =O00OO0OO00O0OO0OO .s .post ("http://u.cocozx.cn/api/coin/submit?zx=&xz=1",json =OOOOOO0O00OOO0OO0 )#line:224
        O00O0O00OOO000O0O =O0OOOO0O0000O000O .json ().get ('result')#line:225
        debugger ('submit '+O0OOOO0O0000O000O .text )#line:226
        O00OO0OO00O0OO0OO .msg +=f"阅读成功,获得元宝{O00O0O00OOO000O0O['val']}，当前剩余次数:{O00O0O00OOO000O0O['progress']}\n"#line:227
        printlog (f"{O00OO0OO00O0OO0OO.name}:阅读成功,获得元宝{O00O0O00OOO000O0O['val']}，当前剩余次数:{O00O0O00OOO000O0O['progress']}")#line:228
    def read (O000000OO000O0OOO ):#line:230
        while True :#line:231
            OOOO0OO0OO0000OOO =O000000OO000O0OOO .get_status ()#line:232
            if not OOOO0OO0OO0000OOO :#line:233
                if O000000OO000O0OOO .status ==30 :#line:234
                    time .sleep (3 )#line:235
                    continue #line:236
                break #line:237
            O00O0OOO0OOO0OOO0 =getmpinfo (OOOO0OO0OO0000OOO )#line:238
            if not O00O0OOO0OOO0OOO0 :#line:239
                printlog (f'{O000000OO000O0OOO.name}:获取文章信息失败，程序中止')#line:240
                return False #line:241
            O000000OO000O0OOO .msg +='开始阅读 '+O00O0OOO0OOO0OOO0 ['text']+'\n'#line:242
            printlog (f'{O000000OO000O0OOO.name}:开始阅读 '+O00O0OOO0OOO0OOO0 ['text'])#line:243
            O0OO0O0000O0O0OO0 =randint (7 ,10 )#line:244
            if O00O0OOO0OOO0OOO0 ['biz']=="Mzg2Mzk3Mjk5NQ==":#line:245
                O000000OO000O0OOO .msg +='正在阅读检测文章\n'#line:246
                printlog (f'{O000000OO000O0OOO.name}:正在阅读检测文章')#line:247
                send (title =O00O0OOO0OOO0OOO0 ['text'],msg =f'{O000000OO000O0OOO.name}  元宝阅读过检测',url =OOOO0OO0OO0000OOO )#line:248
                time .sleep (60 )#line:249
            printlog (f'模拟阅读{O0OO0O0000O0O0OO0}秒')#line:250
            time .sleep (O0OO0O0000O0O0OO0 )#line:251
            O000000OO000O0OOO .submit ()#line:252
    def tixian (OO00OOOO0O0O0O0O0 ):#line:254
        global txe #line:255
        O0O0OO0O000OO0O00 =OO00OOOO0O0O0O0O0 .get_info ()#line:256
        if O0O0OO0O000OO0O00 <txbz :#line:257
            OO00OOOO0O0O0O0O0 .msg +='你的元宝已不足\n'#line:258
            printlog (f'{OO00OOOO0O0O0O0O0.name}你的元宝已不足')#line:259
            return False #line:260
        elif 10000 <=O0O0OO0O000OO0O00 <49999 :#line:261
            txe =10000 #line:262
        elif 50000 <=O0O0OO0O000OO0O00 <100000 :#line:263
            txe =50000 #line:264
        elif 3000 <=O0O0OO0O000OO0O00 <10000 :#line:265
            txe =3000 #line:266
        elif O0O0OO0O000OO0O00 >=100000 :#line:267
            txe =100000 #line:268
        OO00OOOO0O0O0O0O0 .msg +=f"提现金额:{txe}\n"#line:269
        printlog (f'{OO00OOOO0O0O0O0O0.name}提现金额:{txe}')#line:270
        OO0OO00OOO000OOOO ="http://u.cocozx.cn/api/coin/wdmoney"#line:271
        OO000OOO00OO0O00O ={**OO00OOOO0O0O0O0O0 .payload ,**{"val":txe }}#line:272
        try :#line:273
            O0O0OOOO0OO00O0O0 =OO00OOOO0O0O0O0O0 .s .post (OO0OO00OOO000OOOO ,json =OO000OOO00OO0O00O ).json ()#line:274
            OO00OOOO0O0O0O0O0 .msg +=f'提现结果：{O0O0OOOO0OO00O0O0.get("msg")}\n'#line:275
            printlog (f'{OO00OOOO0O0O0O0O0.name}提现结果：{O0O0OOOO0OO00O0O0.get("msg")}')#line:276
        except :#line:277
            OO00OOOO0O0O0O0O0 .msg +=f"自动提现不成功，发送通知手动提现\n"#line:278
            printlog (f"{OO00OOOO0O0O0O0O0.name}:自动提现不成功，发送通知手动提现")#line:279
            send (f'可提现金额 {int(txe) / 10000}元，点击提现',title =f'惜之酱提醒您 {OO00OOOO0O0O0O0O0.name} 元宝阅读可以提现了',url =f'{OO00OOOO0O0O0O0O0.readhost}/coin/index.html?mid=CS5T87Q98')#line:281
    def run (O00OO0OOOOO0OO0O0 ):#line:283
        if O00OO0OOOOO0OO0O0 .get_info ():#line:284
            O00OO0OOOOO0OO0O0 .get_readhost ()#line:285
            O00OO0OOOOO0OO0O0 .read ()#line:286
            O00OO0OOOOO0OO0O0 .tixian ()#line:287
        if not printf :#line:288
            print (O00OO0OOOOO0OO0O0 .msg .strip ())#line:289
def yd (OO0O0000OOOOOOO00 ):#line:292
    while not OO0O0000OOOOOOO00 .empty ():#line:293
        OOO00O000O00OO0OO =OO0O0000OOOOOOO00 .get ()#line:294
        O00OO0O0OOOO000O0 =Allinone (OOO00O000O00OO0OO )#line:295
        O00OO0O0OOOO000O0 .run ()#line:296
def get_ver ():#line:299
    OO00000OO0O0O00OO ='kyb V1.2'#line:300
    OO0OO0OOO0OOO000O ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:303
    OOOOO0O00000OO000 =requests .get ('https://ghproxy.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json',headers =OO0OO0OOO0OOO000O ).json ()#line:305
    OO00O00O000OOO000 =OO00000OO0O0O00OO .split (' ')[1 ]#line:306
    O0OOO0OO0O00OO0O0 =OOOOO0O00000OO000 .get ('version').get (OO00000OO0O0O00OO .split (' ')[0 ])#line:307
    OOO0O0OO0OOO000O0 =f"当前版本 {OO00O00O000OOO000}，仓库版本 {O0OOO0OO0O00OO0O0}"#line:308
    if OO00O00O000OOO000 <O0OOO0OO0O00OO0O0 :#line:309
        OOO0O0OO0OOO000O0 +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:310
    return OOO0O0OO0OOO000O0 #line:311
def main ():#line:314
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:315
    O00O0O0OOOOO0O0OO =os .getenv ('aiock')#line:316
    if not O00O0O0OOOOO0O0OO :#line:317
        print ('请仔细阅读脚本开头的注释并配置好aiock')#line:318
        exit ()#line:319
    try :#line:320
        O00O0O0OOOOO0O0OO =ast .literal_eval (O00O0O0OOOOO0O0OO )#line:321
    except :#line:322
        pass #line:323
    O000O0O0O0OOO0O00 =Queue ()#line:324
    OO0000O0O0OOOOO0O =[]#line:325
    for O0O0O0O0000OO0OO0 ,OO00OOOO000O0O00O in enumerate (O00O0O0OOOOO0O0OO ,start =1 ):#line:326
        printlog (f'{OO00OOOO000O0O00O}\n以上是账号{O0O0O0O0000OO0OO0}的ck，请核对是否正确，如不正确，请检查ck填写格式')#line:327
        O000O0O0O0OOO0O00 .put (OO00OOOO000O0O00O )#line:328
    for O0O0O0O0000OO0OO0 in range (max_workers ):#line:329
        OOO0O0O0OO000O00O =threading .Thread (target =yd ,args =(O000O0O0O0OOO0O00 ,))#line:330
        OOO0O0O0OO000O00O .start ()#line:331
        OO0000O0O0OOOOO0O .append (OOO0O0O0OO000O00O )#line:332
        time .sleep (30 )#line:333
    for O00OOO0OOOOOO0OO0 in OO0000O0O0OOOOO0O :#line:334
        O00OOO0OOOOOO0OO0 .join ()#line:335
if __name__ =='__main__':#line:338
    main ()#line:339
