"""
智慧阅读入口：http://mr1694397085936.qmpcsxu.cn/oz/index.html?mid=QX5E9WLGS

http://u.cocozx.cn/api/ox/info
抓包 info接口的请求体中的un和token参数

注意：脚本变量使用的单引号、双引号、逗号都是英文状态的
注意：脚本变量使用的单引号、双引号、逗号都是英文状态的
注意：脚本变量使用的单引号、双引号、逗号都是英文状态的
------------------------------------------------------
内置推送企业微信群机器人
参考 https://github.com/kxs2018/yuedu/blob/main/获取企业微信群机器人key.md 获取key，并关注插件！！！

青龙配置文件
export aiock='''[{"un": "xxxx", "token": "xxxxx","name":"彦祖"}]'''
export qwbotkey="abcdefg"
------------------------------------------------------
no module named lxml 解决方案
1. 配置文件搜索 PipMirror，如果网址包含douban的，请改为下方的网址
PipMirror="https://pypi.tuna.tsinghua.edu.cn/simple"
2. 依赖管理-python 添加 lxml
3. 如果装不上，①请ssh连接到服务器 ②docker exec -it ql bash (ql是青龙容器的名字，docker ps可查看) ③pip install pip -U
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

qwbotkey = os.getenv('qwbotkey')  # line:62
if not qwbotkey:  # line:63
    print('请仔细阅读脚本开头的注释并配置好qwbotkey')  # line:64
    exit()  # line:65


def ftime ():#line:68
    OOO0000O0OOOOO00O =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:69
    return OOO0000O0OOOOO00O #line:70
def debugger (O000O000O00OOO00O ):#line:73
    if debug :#line:74
        print (O000O000O00OOO00O )#line:75
def printlog (O0OO000O0O0O0O00O ):#line:78
    if printf :#line:79
        print (O0OO000O0O0O0O00O )#line:80
def send (O0O0OOOO000O00OOO ,title ='通知',url =None ):#line:83
    if not title or not url :#line:84
        OOO0OO00OO00OOO0O ={"msgtype":"text","text":{"content":f"{title}\n\n{O0O0OOOO000O00OOO}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:91
    else :#line:92
        OOO0OO00OO00OOO0O ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O0O0OOOO000O00OOO ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:105
    O00O0OO000O0O0O00 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:106
    O0OO000OO0OO0O000 =requests .post (O00O0OO000O0O0O00 ,data =json .dumps (OOO0OO00OO00OOO0O )).json ()#line:107
    if O0OO000OO0OO0O000 .get ('errcode')!=0 :#line:108
        print ('消息发送失败，请检查key和发送格式')#line:109
        return False #line:110
    return O0OO000OO0OO0O000 #line:111
def getmpinfo (O0OOO0O00OO0O0OOO ):#line:114
    if not O0OOO0O00OO0O0OOO or O0OOO0O00OO0O0OOO =='':#line:115
        return False #line:116
    O00OO0O00OO00O0OO ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:118
    O0000O0OO0O000000 =requests .get (O0OOO0O00OO0O0OOO ,headers =O00OO0O00OO00O0OO )#line:119
    O0OO000O00000OOOO =etree .HTML (O0000O0OO0O000000 .text )#line:120
    O0OO00O0OOOOOOO00 =O0OO000O00000OOOO .xpath ('//meta[@*="og:title"]/@content')#line:122
    if O0OO00O0OOOOOOO00 :#line:123
        O0OO00O0OOOOOOO00 =O0OO00O0OOOOOOO00 [0 ]#line:124
    O0O0O0O0OOO000OO0 =O0OO000O00000OOOO .xpath ('//meta[@*="og:url"]/@content')#line:125
    if O0O0O0O0OOO000OO0 :#line:126
        O0O0O0O0OOO000OO0 =O0O0O0O0OOO000OO0 [0 ].encode ().decode ()#line:127
    try :#line:128
        O0000O000OOO0000O =re .findall (r'biz=(.*?)&',O0OOO0O00OO0O0OOO )[0 ]#line:129
    except :#line:130
        O0000O000OOO0000O =re .findall (r'biz=(.*?)&',O0O0O0O0OOO000OO0 )[0 ]#line:131
    if not O0000O000OOO0000O :#line:132
        return False #line:133
    O0OOO00000OO00OO0 =O0OO000O00000OOOO .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:134
    if O0OOO00000OO00OO0 :#line:135
        O0OOO00000OO00OO0 =O0OOO00000OO00OO0 [0 ].strip ()#line:136
    OOOO0OO00OOOOOO0O =re .findall (r"user_name.DATA'\) : '(.*?)'",O0000O0OO0O000000 .text )or O0OO000O00000OOOO .xpath ('//span[@class="profile_meta_value"]/text()')#line:138
    if OOOO0OO00OOOOOO0O :#line:139
        OOOO0OO00OOOOOO0O =OOOO0OO00OOOOOO0O [0 ]#line:140
    O00O0OOO0OOO00OO0 =re .findall (r'createTime = \'(.*)\'',O0000O0OO0O000000 .text )#line:141
    if O00O0OOO0OOO00OO0 :#line:142
        O00O0OOO0OOO00OO0 =O00O0OOO0OOO00OO0 [0 ][5 :]#line:143
    O0O0O00OOO0O0OO0O =f'{O00O0OOO0OOO00OO0} {O0OO00O0OOOOOOO00}'#line:144
    OO000OOO00O0O00O0 ={'biz':O0000O000OOO0000O ,'text':O0O0O00OOO0O0OO0O }#line:145
    return OO000OOO00O0O00O0 #line:146
class Allinone :#line:149
    def __init__ (O0O0O0O0OO0000O0O ,OOOO0O000O000OO00 ):#line:150
        O0O0O0O0OO0000O0O .name =OOOO0O000O000OO00 ['name']#line:151
        O0O0O0O0OO0000O0O .s =requests .session ()#line:152
        O0O0O0O0OO0000O0O .payload ={"un":OOOO0O000O000OO00 ['un'],"token":OOOO0O000O000OO00 ['token'],"pageSize":20 }#line:153
        O0O0O0O0OO0000O0O .s .headers ={'Accept':'application/json, text/javascript, */*; q=0.01','Content-Type':'application/json; charset=UTF-8','Host':'u.cocozx.cn','Connection':'keep-alive','Origin':'http://mr1694957965536.qwydu.com','User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",'Accept-Encoding':'gzip, deflate'}#line:160
        O0O0O0O0OO0000O0O .headers =O0O0O0O0OO0000O0O .s .headers .copy ()#line:161
        O0O0O0O0OO0000O0O .msg =''#line:162
    def get_readhost (OOO0O0OO0OOOOOO0O ):#line:164
        OO0OO00O00O00OOOO ="http://u.cocozx.cn/api/oz/getReadHost"#line:165
        OO000000000OOO0O0 =OOO0O0OO0OOOOOO0O .s .post (OO0OO00O00O00OOOO ,json =OOO0O0OO0OOOOOO0O .payload ).json ()#line:166
        debugger (f'readhome {OO000000000OOO0O0}')#line:167
        OOO0O0OO0OOOOOO0O .readhost =OO000000000OOO0O0 .get ('result')['host']#line:168
        OOO0O0OO0OOOOOO0O .headers ['Origin']=OOO0O0OO0OOOOOO0O .readhost #line:169
        OOO0O0OO0OOOOOO0O .msg +=f'邀请链接：{OOO0O0OO0OOOOOO0O.readhost}/oz/index.html?mid={OOO0O0OO0OOOOOO0O.huid}\n'#line:170
        printlog (f"{OOO0O0OO0OOOOOO0O.name}:邀请链接：{OOO0O0OO0OOOOOO0O.readhost}/oz/index.html?mid={OOO0O0OO0OOOOOO0O.huid}")#line:171
    def get_info (O00O0O0O0OO0OOOO0 ):#line:173
        OOO00O00OO00O0000 ='QX5E9WLGS'if O00O0O0O0OO0OOOO0 .name =='AI'else '4G7QUZY8Y'#line:174
        OOOOO00OOO0O00000 ={**O00O0O0O0OO0OOOO0 .payload ,**{'code':OOO00O00OO00O0000 }}#line:175
        try :#line:176
            O0O0OO000O000O0O0 =O00O0O0O0OO0OOOO0 .s .post ("http://u.cocozx.cn/api/oz/info",json =OOOOO00OOO0O00000 ).json ()#line:177
            OO0OO00O00000OO0O =O0O0OO000O000O0O0 .get ("result")#line:178
            debugger (f'get_info {O0O0OO000O000O0O0}')#line:179
            OO000O0O0O0O0O0OO =OO0OO00O00000OO0O .get ('us')#line:180
            if OO000O0O0O0O0O0OO ==2 :#line:181
                O00O0O0O0OO0OOOO0 .msg +=f'账号：{O00O0O0O0OO0OOOO0.name}已被封\n'#line:182
                printlog (f'账号：{O00O0O0O0OO0OOOO0.name}已被封')#line:183
                return False #line:184
            O00O0O0O0OO0OOOO0 .msg +=f"""账号:{O00O0O0O0OO0OOOO0.name}，今日阅读次数:{OO0OO00O00000OO0O["dayCount"]}，当前智慧:{OO0OO00O00000OO0O["moneyCurrent"]}，累计阅读次数:{OO0OO00O00000OO0O["doneWx"]}\n"""#line:185
            printlog (f"""账号:{O00O0O0O0OO0OOOO0.name}，今日阅读次数:{OO0OO00O00000OO0O["dayCount"]}，当前智慧:{OO0OO00O00000OO0O["moneyCurrent"]}，累计阅读次数:{OO0OO00O00000OO0O["doneWx"]}""")#line:187
            OOOO0O00OOOOO0O00 =int (OO0OO00O00000OO0O ["moneyCurrent"])#line:188
            O00O0O0O0OO0OOOO0 .huid =OO0OO00O00000OO0O .get ('uid')#line:189
            return OOOO0O00OOOOO0O00 #line:190
        except :#line:191
            return False #line:192
    def get_status (OO000O0OOO00O0OO0 ):#line:194
        O0O0OO00O000OO000 =requests .post ("http://u.cocozx.cn/api/oz/read",headers =OO000O0OOO00O0OO0 .headers ,json =OO000O0OOO00O0OO0 .payload ).json ()#line:195
        debugger (f'getstatus {O0O0OO00O000OO000}')#line:196
        OO000O0OOO00O0OO0 .status =O0O0OO00O000OO000 .get ("result").get ("status")#line:197
        if OO000O0OOO00O0OO0 .status ==40 :#line:198
            OO000O0OOO00O0OO0 .msg +="文章还没有准备好\n"#line:199
            printlog (f"{OO000O0OOO00O0OO0.name}:文章还没有准备好")#line:200
            return #line:201
        elif OO000O0OOO00O0OO0 .status ==50 :#line:202
            OO000O0OOO00O0OO0 .msg +="阅读失效\n"#line:203
            printlog (f"{OO000O0OOO00O0OO0.name}:阅读失效")#line:204
            return #line:205
        elif OO000O0OOO00O0OO0 .status ==60 :#line:206
            OO000O0OOO00O0OO0 .msg +="已经全部阅读完了\n"#line:207
            printlog (f"{OO000O0OOO00O0OO0.name}:已经全部阅读完了")#line:208
            return #line:209
        elif OO000O0OOO00O0OO0 .status ==70 :#line:210
            OO000O0OOO00O0OO0 .msg +="下一轮还未开启\n"#line:211
            printlog (f"{OO000O0OOO00O0OO0.name}:下一轮还未开启")#line:212
            return #line:213
        elif OO000O0OOO00O0OO0 .status ==10 :#line:214
            O0O0OOO0O00O0O0OO =O0O0OO00O000OO000 ["result"]["url"]#line:215
            OO000O0OOO00O0OO0 .msg +='-'*50 +"\n阅读链接获取成功\n"#line:216
            printlog (f"{OO000O0OOO00O0OO0.name}:阅读链接获取成功")#line:217
            return O0O0OOO0O00O0O0OO #line:218
    def submit (O0OOO0O0OO0O00O0O ):#line:220
        OOO0O000OO00O00OO ={**{'type':1 },**O0OOO0O0OO0O00O0O .payload }#line:221
        OOO00O00OO00O0O0O =requests .post ("http://u.cocozx.cn/api/oz/submit?zx=&xz=1",headers =O0OOO0O0OO0O00O0O .headers ,json =OOO0O000OO00O00OO )#line:222
        O000O0O0O0OO00OOO =OOO00O00OO00O0O0O .json ().get ('result')#line:223
        debugger ('submit '+OOO00O00OO00O0O0O .text )#line:224
        O0OOO0O0OO0O00O0O .msg +=f"阅读成功,获得智慧{O000O0O0O0OO00OOO['val']}，当前剩余次数:{O000O0O0O0OO00OOO['progress']}\n"#line:225
        printlog (f"{O0OOO0O0OO0O00O0O.name}:阅读成功,获得智慧{O000O0O0O0OO00OOO['val']}，当前剩余次数:{O000O0O0O0OO00OOO['progress']}")#line:226
    def read (OOO00OO00O0O00000 ):#line:228
        OOO0O0O00O00000OO =1 #line:229
        while True :#line:230
            O0OOOOO00OOO0OO00 =OOO00OO00O0O00000 .get_status ()#line:231
            if not O0OOOOO00OOO0OO00 :#line:232
                if OOO00OO00O0O00000 .status ==30 :#line:233
                    time .sleep (3 )#line:234
                    continue #line:235
                break #line:236
            O0OO000OOOOOOOO00 =getmpinfo (O0OOOOO00OOO0OO00 )#line:237
            OOO00OO00O0O00000 .msg +='开始阅读 '+O0OO000OOOOOOOO00 ['text']+'\n'#line:238
            printlog (f'{OOO00OO00O0O00000.name}:开始阅读 '+O0OO000OOOOOOOO00 ['text'])#line:239
            OO0O0OOO0O0OO0OOO =randint (7 ,10 )#line:240
            if O0OO000OOOOOOOO00 ['biz']=="Mzg2Mzk3Mjk5NQ==":#line:241
                OOO00OO00O0O00000 .msg +='当前正在阅读检测文章\n'#line:242
                printlog (f'{OOO00OO00O0O00000.name}:正在阅读检测文章')#line:243
                send (f'{OOO00OO00O0O00000.name}  智慧阅读正在读检测文章',O0OO000OOOOOOOO00 ['text'],O0OOOOO00OOO0OO00 )#line:244
                time .sleep (60 )#line:245
            printlog (f'{OOO00OO00O0O00000.name}：模拟阅读{OO0O0OOO0O0OO0OOO}秒')#line:246
            time .sleep (OO0O0OOO0O0OO0OOO )#line:247
            OOO00OO00O0O00000 .submit ()#line:248
    def tixian (O0000O00000000000 ):#line:250
        global txe #line:251
        O000O00OO00OO00O0 =O0000O00000000000 .get_info ()#line:252
        if O000O00OO00OO00O0 <txbz :#line:253
            O0000O00000000000 .msg +='你的智慧不多了\n'#line:254
            printlog (f'{O0000O00000000000.name}你的智慧不多了')#line:255
            return False #line:256
        elif 10000 <=O000O00OO00OO00O0 <49999 :#line:257
            txe =10000 #line:258
        elif 50000 <=O000O00OO00OO00O0 <100000 :#line:259
            txe =50000 #line:260
        elif 3000 <=O000O00OO00OO00O0 <10000 :#line:261
            txe =3000 #line:262
        elif O000O00OO00OO00O0 >=100000 :#line:263
            txe =100000 #line:264
        O0000O00000000000 .msg +=f"提现金额:{txe}\n"#line:265
        printlog (f'{O0000O00000000000.name}提现金额:{txe}')#line:266
        OOO000OO0OO00OOOO ={**O0000O00000000000 .payload ,**{"val":txe }}#line:267
        try :#line:268
            O0OO00OOO000OO000 =O0000O00000000000 .s .post ("http://u.cocozx.cn/api/oz/wdmoney",json =OOO000OO0OO00OOOO ).json ()#line:269
            O0000O00000000000 .msg +=f'提现结果：{O0OO00OOO000OO000.get("msg")}\n'#line:270
            printlog (f'{O0000O00000000000.name}提现结果：{O0OO00OOO000OO000.get("msg")}')#line:271
        except :#line:272
            O0000O00000000000 .msg +=f"自动提现不成功，发送通知手动提现\n"#line:273
            printlog (f"{O0000O00000000000.name}:自动提现不成功，发送通知手动提现")#line:274
            send (f'可提现金额 {int(txe) / 10000}元，点击提现',title =f'惜之酱提醒您 {O0000O00000000000.name} 智慧阅读可以提现了',url =f'{O0000O00000000000.readhost}/oz/index.html?mid=QX5E9WLGS')#line:276
    def run (OO000000O00OO00O0 ):#line:278
        OO000000O00OO00O0 .msg +='*'*50 +'\n'#line:279
        if OO000000O00OO00O0 .get_info ():#line:280
            OO000000O00OO00O0 .get_readhost ()#line:281
            OO000000O00OO00O0 .read ()#line:282
            OO000000O00OO00O0 .tixian ()#line:283
        if not printf :#line:284
            print (OO000000O00OO00O0 .msg .strip ())#line:285
def yd (O0OOOO0000000O0OO ):#line:288
    while not O0OOOO0000000O0OO .empty ():#line:289
        OOO0O0O0OO0O0OO00 =O0OOOO0000000O0OO .get ()#line:290
        O0OO0000O0O00O00O =Allinone (OOO0O0O0OO0O0OO00 )#line:291
        O0OO0000O0O00O00O .run ()#line:292
def get_ver ():#line:295
    O0000OOO00O0OO000 ='kzh V1.2.2'#line:296
    O00O0O0O00000OO0O ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:299
    OO00OOO0O0O000O0O =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O00O0O0O00000OO0O ).json ()#line:301
    OOOO0OO000000O0OO =O0000OOO00O0OO000 .split (' ')[1 ]#line:302
    OOOO00O0OO00OO000 =OO00OOO0O0O000O0O .get ('version').get (O0000OOO00O0OO000 .split (' ')[0 ])#line:303
    O0OO0O0OO0OO00O00 =f"当前版本 {OOOO0OO000000O0OO}，仓库版本 {OOOO00O0OO00OO000}"#line:304
    if OOOO0OO000000O0OO <OOOO00O0OO00OO000 :#line:305
        O0OO0O0OO0OO00O00 +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:306
    return O0OO0O0OO0OO00O00 #line:307
def main ():#line:310
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:311
    OOOO0OO00OO0OO00O =os .getenv ('aiock')#line:312
    if not OOOO0OO00OO0OO00O :#line:313
        print ('请仔细阅读脚本开头的注释并配置好aiock')#line:314
        exit ()#line:315
    try :#line:316
        OOOO0OO00OO0OO00O =ast .literal_eval (OOOO0OO00OO0OO00O )#line:317
    except :#line:318
        pass #line:319
    O0O0O00OO0000OOO0 =Queue ()#line:320
    OO000OO00O000OO0O =[]#line:321
    for OOOO00OOOOO0OOOOO ,O0O0OOOOOO000OO00 in enumerate (OOOO0OO00OO0OO00O ,start =1 ):#line:322
        printlog (f'{O0O0OOOOOO000OO00}\n以上是账号{OOOO00OOOOO0OOOOO}的ck，如不正确，请检查ck填写格式')#line:323
        O0O0O00OO0000OOO0 .put (O0O0OOOOOO000OO00 )#line:324
    for OOOO00OOOOO0OOOOO in range (max_workers ):#line:325
        OOO0OO0000O00OOO0 =threading .Thread (target =yd ,args =(O0O0O00OO0000OOO0 ,))#line:326
        OOO0OO0000O00OOO0 .start ()#line:327
        OO000OO00O000OO0O .append (OOO0OO0000O00OOO0 )#line:328
        time .sleep (40 )#line:329
    for O0O0O0O0OOOOO0OOO in OO000OO00O000OO0O :#line:330
        O0O0O0O0OOOOO0OOO .join ()#line:331
if __name__ =='__main__':#line:334
    main ()#line:335
