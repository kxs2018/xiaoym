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

qwbotkey =os .getenv ('qwbotkey')#line:62
if not qwbotkey :#line:63
    print ('请仔细阅读脚本开头的注释并配置好qwbotkey')#line:64
    exit ()#line:65
def ftime ():#line:68
    O00O00OOO000OO000 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:69
    return O00O00OOO000OO000 #line:70
def debugger (O0OOO0OO000OOO000 ):#line:73
    if debug :#line:74
        print (O0OOO0OO000OOO000 )#line:75
def printlog (O00000OOOO000O00O ):#line:78
    if printf :#line:79
        print (O00000OOOO000O00O )#line:80
def send (O0000O000000O0000 ,title ='通知',url =None ):#line:83
    if not title or not url :#line:84
        OO0000O00O0O0O0OO ={"msgtype":"text","text":{"content":f"{title}\n\n{O0000O000000O0000}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:91
    else :#line:92
        OO0000O00O0O0O0OO ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O0000O000000O0000 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:105
    O0O0000OO0O0OOOOO =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:106
    OOOOOO0OOO000O00O =requests .post (O0O0000OO0O0OOOOO ,data =json .dumps (OO0000O00O0O0O0OO )).json ()#line:107
    if OOOOOO0OOO000O00O .get ('errcode')!=0 :#line:108
        print ('消息发送失败，请检查key和发送格式')#line:109
        return False #line:110
    return OOOOOO0OOO000O00O #line:111
def getmpinfo (OO0000O0O000O0OOO ):#line:114
    if not OO0000O0O000O0OOO or OO0000O0O000O0OOO =='':#line:115
        return False #line:116
    OOO000000000O000O ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:118
    OOOO00OO00O00OOOO =requests .get (OO0000O0O000O0OOO ,headers =OOO000000000O000O )#line:119
    O00O000OO0O00OOO0 =etree .HTML (OOOO00OO00O00OOOO .text )#line:120
    OO000000O00OO0OO0 =O00O000OO0O00OOO0 .xpath ('//meta[@*="og:title"]/@content')#line:122
    if OO000000O00OO0OO0 :#line:123
        OO000000O00OO0OO0 =OO000000O00OO0OO0 [0 ]#line:124
    O0O0OO0000OO00000 =O00O000OO0O00OOO0 .xpath ('//meta[@*="og:url"]/@content')#line:125
    if O0O0OO0000OO00000 :#line:126
        O0O0OO0000OO00000 =O0O0OO0000OO00000 [0 ].encode ().decode ()#line:127
    try :#line:128
        O0OOOOOOO0O00O0OO =re .findall (r'biz=(.*?)&',OO0000O0O000O0OOO )#line:129
    except :#line:130
        O0OOOOOOO0O00O0OO =re .findall (r'biz=(.*?)&',O0O0OO0000OO00000 )#line:131
    if O0OOOOOOO0O00O0OO :#line:132
        O0OOOOOOO0O00O0OO =O0OOOOOOO0O00O0OO [0 ]#line:133
    else :#line:134
        return False #line:135
    O0O00000O00OO0O0O =O00O000OO0O00OOO0 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:136
    if O0O00000O00OO0O0O :#line:137
        O0O00000O00OO0O0O =O0O00000O00OO0O0O [0 ].strip ()#line:138
    O0000OO0O00O00O00 =re .findall (r"user_name.DATA'\) : '(.*?)'",OOOO00OO00O00OOOO .text )or O00O000OO0O00OOO0 .xpath ('//span[@class="profile_meta_value"]/text()')#line:140
    if O0000OO0O00O00O00 :#line:141
        O0000OO0O00O00O00 =O0000OO0O00O00O00 [0 ]#line:142
    O0OO000O00O0OO00O =re .findall (r'createTime = \'(.*)\'',OOOO00OO00O00OOOO .text )#line:143
    if O0OO000O00O0OO00O :#line:144
        O0OO000O00O0OO00O =O0OO000O00O0OO00O [0 ][5 :]#line:145
    O00O000OO00O0OO00 =f'{O0OO000O00O0OO00O} {OO000000O00OO0OO0}'#line:146
    OOOOOOOOO0OO0OOOO ={'biz':O0OOOOOOO0O00O0OO ,'text':O00O000OO00O0OO00 }#line:147
    return OOOOOOOOO0OO0OOOO #line:148
class Allinone :#line:151
    def __init__ (O0OOO0O0O000O0O0O ,O0O0O0O0O0OOO0000 ):#line:152
        O0OOO0O0O000O0O0O .name =O0O0O0O0O0OOO0000 ['name']#line:153
        O0OOO0O0O000O0O0O .s =requests .session ()#line:154
        O0OOO0O0O000O0O0O .payload ={"un":O0O0O0O0O0OOO0000 ['un'],"token":O0O0O0O0O0OOO0000 ['token'],"pageSize":20 }#line:155
        O0OOO0O0O000O0O0O .s .headers ={'Accept':'application/json, text/javascript, */*; q=0.01','Content-Type':'application/json; charset=UTF-8','Host':'u.cocozx.cn','Connection':'keep-alive','Origin':'http://mr1694957965536.qwydu.com','User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",'Accept-Encoding':'gzip, deflate'}#line:162
        O0OOO0O0O000O0O0O .headers =O0OOO0O0O000O0O0O .s .headers .copy ()#line:163
        O0OOO0O0O000O0O0O .msg =''#line:164
    def get_readhost (OO000OOOO000O000O ):#line:166
        O0OOOOOOO000OO000 ="http://u.cocozx.cn/api/oz/getReadHost"#line:167
        OO0OOO00O0OOO0OOO =OO000OOOO000O000O .s .post (O0OOOOOOO000OO000 ,json =OO000OOOO000O000O .payload ).json ()#line:168
        debugger (f'readhome {OO0OOO00O0OOO0OOO}')#line:169
        OO000OOOO000O000O .readhost =OO0OOO00O0OOO0OOO .get ('result')['host']#line:170
        OO000OOOO000O000O .headers ['Origin']=OO000OOOO000O000O .readhost #line:171
        OO000OOOO000O000O .msg +=f'邀请链接：{OO000OOOO000O000O.readhost}/oz/index.html?mid={OO000OOOO000O000O.huid}\n'#line:172
        printlog (f"{OO000OOOO000O000O.name}:邀请链接：{OO000OOOO000O000O.readhost}/oz/index.html?mid={OO000OOOO000O000O.huid}")#line:173
    def get_info (OOOOO000O00O0OOO0 ):#line:175
        OO0O00O00OOOO0O0O ={**OOOOO000O00O0OOO0 .payload ,**{'code':'4G7QUZY8Y'}}#line:176
        try :#line:177
            OOOO0OOOOO00OOO0O =OOOOO000O00O0OOO0 .s .post ("http://u.cocozx.cn/api/oz/info",json =OO0O00O00OOOO0O0O ).json ()#line:178
            OO00OO0000O0OO00O =OOOO0OOOOO00OOO0O .get ("result")#line:179
            debugger (f'get_info {OOOO0OOOOO00OOO0O}')#line:180
            O0O00OO0OO0O00O0O =OO00OO0000O0OO00O .get ('us')#line:181
            if O0O00OO0OO0O00O0O ==2 :#line:182
                OOOOO000O00O0OOO0 .msg +=f'账号：{OOOOO000O00O0OOO0.name}已被封\n'#line:183
                printlog (f'账号：{OOOOO000O00O0OOO0.name}已被封')#line:184
                return False #line:185
            OOOOO000O00O0OOO0 .msg +=f"""账号:{OOOOO000O00O0OOO0.name}，今日阅读次数:{OO00OO0000O0OO00O["dayCount"]}，当前智慧:{OO00OO0000O0OO00O["moneyCurrent"]}，累计阅读次数:{OO00OO0000O0OO00O["doneWx"]}\n"""#line:186
            printlog (f"""账号:{OOOOO000O00O0OOO0.name}，今日阅读次数:{OO00OO0000O0OO00O["dayCount"]}，当前智慧:{OO00OO0000O0OO00O["moneyCurrent"]}，累计阅读次数:{OO00OO0000O0OO00O["doneWx"]}""")#line:188
            O0000OOO0OOOO0OOO =int (OO00OO0000O0OO00O ["moneyCurrent"])#line:189
            OOOOO000O00O0OOO0 .huid =OO00OO0000O0OO00O .get ('uid')#line:190
            return O0000OOO0OOOO0OOO #line:191
        except :#line:192
            return False #line:193
    def get_status (O000O0O00O00OOO0O ):#line:195
        O0O0O0OOOOOO00OO0 =requests .post ("http://u.cocozx.cn/api/oz/read",headers =O000O0O00O00OOO0O .headers ,json =O000O0O00O00OOO0O .payload ).json ()#line:196
        debugger (f'getstatus {O0O0O0OOOOOO00OO0}')#line:197
        O000O0O00O00OOO0O .status =O0O0O0OOOOOO00OO0 .get ("result").get ("status")#line:198
        if O000O0O00O00OOO0O .status ==40 :#line:199
            O000O0O00O00OOO0O .msg +="文章还没有准备好\n"#line:200
            printlog (f"{O000O0O00O00OOO0O.name}:文章还没有准备好")#line:201
            return #line:202
        elif O000O0O00O00OOO0O .status ==50 :#line:203
            O000O0O00O00OOO0O .msg +="阅读失效\n"#line:204
            printlog (f"{O000O0O00O00OOO0O.name}:阅读失效")#line:205
            return #line:206
        elif O000O0O00O00OOO0O .status ==60 :#line:207
            O000O0O00O00OOO0O .msg +="已经全部阅读完了\n"#line:208
            printlog (f"{O000O0O00O00OOO0O.name}:已经全部阅读完了")#line:209
            return #line:210
        elif O000O0O00O00OOO0O .status ==70 :#line:211
            O000O0O00O00OOO0O .msg +="下一轮还未开启\n"#line:212
            printlog (f"{O000O0O00O00OOO0O.name}:下一轮还未开启")#line:213
            return #line:214
        elif O000O0O00O00OOO0O .status ==10 :#line:215
            O0OO000O0O0OO0OOO =O0O0O0OOOOOO00OO0 ["result"]["url"]#line:216
            O000O0O00O00OOO0O .msg +='-'*50 +"\n阅读链接获取成功\n"#line:217
            printlog (f"{O000O0O00O00OOO0O.name}:阅读链接获取成功")#line:218
            return O0OO000O0O0OO0OOO #line:219
    def submit (OO00O0O0O0O0O0OOO ):#line:221
        OOO00OOO0OOOO00OO ={**{'type':1 },**OO00O0O0O0O0O0OOO .payload }#line:222
        OOO000O0OO0O00OOO =requests .post ("http://u.cocozx.cn/api/oz/submit?zx=&xz=1",headers =OO00O0O0O0O0O0OOO .headers ,json =OOO00OOO0OOOO00OO )#line:223
        O0O0000O0O00OO0O0 =OOO000O0OO0O00OOO .json ().get ('result')#line:224
        debugger ('submit '+OOO000O0OO0O00OOO .text )#line:225
        OO00O0O0O0O0O0OOO .msg +=f"阅读成功,获得智慧{O0O0000O0O00OO0O0['val']}，当前剩余次数:{O0O0000O0O00OO0O0['progress']}\n"#line:226
        printlog (f"{OO00O0O0O0O0O0OOO.name}:阅读成功,获得智慧{O0O0000O0O00OO0O0['val']}，当前剩余次数:{O0O0000O0O00OO0O0['progress']}")#line:227
    def read (O000O00OOO00O00O0 ):#line:229
        O0O0000OOOOOOOOOO =1 #line:230
        while True :#line:231
            OO0O0O0O000000OOO =O000O00OOO00O00O0 .get_status ()#line:232
            if not OO0O0O0O000000OOO :#line:233
                if O000O00OOO00O00O0 .status ==30 :#line:234
                    time .sleep (3 )#line:235
                    continue #line:236
                break #line:237
            OOOOO0OO0OO00O000 =getmpinfo (OO0O0O0O000000OOO )#line:238
            if not OOOOO0OO0OO00O000 :#line:239
                O0O0000OOOOOOOOOO +=1 #line:240
                if O0O0000OOOOOOOOOO ==3 :#line:241
                    printlog (f'{O000O00OOO00O00O0.name}:获取文章信息失败已达3次，程序中止')#line:242
                    return False #line:243
                time .sleep (5 )#line:244
                continue #line:245
            O000O00OOO00O00O0 .msg +='开始阅读 '+OOOOO0OO0OO00O000 ['text']+'\n'#line:246
            printlog (f'{O000O00OOO00O00O0.name}:开始阅读 '+OOOOO0OO0OO00O000 ['text'])#line:247
            O00OOOOO0O00OO00O =randint (7 ,10 )#line:248
            if OOOOO0OO0OO00O000 ['biz']=="Mzg2Mzk3Mjk5NQ==":#line:249
                O000O00OOO00O00O0 .msg +='当前正在阅读检测文章\n'#line:250
                printlog (f'{O000O00OOO00O00O0.name}:正在阅读检测文章')#line:251
                send (f'{O000O00OOO00O00O0.name}  智慧阅读正在读检测文章',OOOOO0OO0OO00O000 ['text'],OO0O0O0O000000OOO )#line:252
                time .sleep (60 )#line:253
            printlog (f'{O000O00OOO00O00O0.name}：模拟阅读{O00OOOOO0O00OO00O}秒')#line:254
            time .sleep (O00OOOOO0O00OO00O )#line:255
            O000O00OOO00O00O0 .submit ()#line:256
    def tixian (OOO0OOO0OO000000O ):#line:258
        global txe #line:259
        OOO000OO00000O000 =OOO0OOO0OO000000O .get_info ()#line:260
        if OOO000OO00000O000 <txbz :#line:261
            OOO0OOO0OO000000O .msg +='你的智慧不多了\n'#line:262
            printlog (f'{OOO0OOO0OO000000O.name}你的智慧不多了')#line:263
            return False #line:264
        elif 10000 <=OOO000OO00000O000 <49999 :#line:265
            txe =10000 #line:266
        elif 50000 <=OOO000OO00000O000 <100000 :#line:267
            txe =50000 #line:268
        elif 3000 <=OOO000OO00000O000 <10000 :#line:269
            txe =3000 #line:270
        elif OOO000OO00000O000 >=100000 :#line:271
            txe =100000 #line:272
        OOO0OOO0OO000000O .msg +=f"提现金额:{txe}\n"#line:273
        printlog (f'{OOO0OOO0OO000000O.name}提现金额:{txe}')#line:274
        O000OO000OOO0O00O ={**OOO0OOO0OO000000O .payload ,**{"val":txe }}#line:275
        try :#line:276
            OOO0O0OO00000OOOO =OOO0OOO0OO000000O .s .post ("http://u.cocozx.cn/api/oz/wdmoney",json =O000OO000OOO0O00O ).json ()#line:277
            OOO0OOO0OO000000O .msg +=f'提现结果：{OOO0O0OO00000OOOO.get("msg")}\n'#line:278
            printlog (f'{OOO0OOO0OO000000O.name}提现结果：{OOO0O0OO00000OOOO.get("msg")}')#line:279
        except :#line:280
            OOO0OOO0OO000000O .msg +=f"自动提现不成功，发送通知手动提现\n"#line:281
            printlog (f"{OOO0OOO0OO000000O.name}:自动提现不成功，发送通知手动提现")#line:282
            send (f'可提现金额 {int(txe) / 10000}元，点击提现',title =f'惜之酱提醒您 {OOO0OOO0OO000000O.name} 智慧阅读可以提现了',url =f'{OOO0OOO0OO000000O.readhost}/oz/index.html?mid=QX5E9WLGS')#line:284
    def run (O0O000O0OO0O0OOOO ):#line:286
        O0O000O0OO0O0OOOO .msg +='*'*50 +'\n'#line:287
        if O0O000O0OO0O0OOOO .get_info ():#line:288
            O0O000O0OO0O0OOOO .get_readhost ()#line:289
            O0O000O0OO0O0OOOO .read ()#line:290
            O0O000O0OO0O0OOOO .tixian ()#line:291
        if not printf :#line:292
            print (O0O000O0OO0O0OOOO .msg .strip ())#line:293
def yd (OO0OO000OOO0O00O0 ):#line:296
    while not OO0OO000OOO0O00O0 .empty ():#line:297
        O0OO0000O0OO0O000 =OO0OO000OOO0O00O0 .get ()#line:298
        O0OOOO0OOO0O00OOO =Allinone (O0OO0000O0OO0O000 )#line:299
        O0OOOO0OOO0O00OOO .run ()#line:300
def get_ver ():#line:303
    OO0O000OO00OO0OOO ='kzh V1.2'#line:304
    O0OOO0O0O000OO00O ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:307
    OOOOOO00OO000OO00 =requests .get ('https://gitclone.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json',headers =O0OOO0O0O000OO00O ).json ()#line:309
    OO0O0O0O0000O0000 =OO0O000OO00OO0OOO .split (' ')[1 ]#line:310
    O00OOOOOO0OO0OOOO =OOOOOO00OO000OO00 .get ('version').get (OO0O000OO00OO0OOO .split (' ')[0 ])#line:311
    OOO000OO0O0OO0OOO =f"当前版本 {OO0O0O0O0000O0000}，仓库版本 {O00OOOOOO0OO0OOOO}"#line:312
    if OO0O0O0O0000O0000 <O00OOOOOO0OO0OOOO :#line:313
        OOO000OO0O0OO0OOO +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:314
    return OOO000OO0O0OO0OOO #line:315
def main ():#line:318
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:319
    OOO0O0O0O0000OO00 =os .getenv ('aiock')#line:320
    if not OOO0O0O0O0000OO00 :#line:321
        print ('请仔细阅读脚本开头的注释并配置好aiock')#line:322
        exit ()#line:323
    try :#line:324
        OOO0O0O0O0000OO00 =ast .literal_eval (OOO0O0O0O0000OO00 )#line:325
    except :#line:326
        pass #line:327
    OO00O00O0000000O0 =Queue ()#line:328
    OO0OOOOO0OO00OOOO =[]#line:329
    for OOO0OO0O00OO000OO ,OOOOOOO0OOOO000OO in enumerate (OOO0O0O0O0000OO00 ,start =1 ):#line:330
        printlog (f'{OOOOOOO0OOOO000OO}\n以上是账号{OOO0OO0O00OO000OO}的ck，如不正确，请检查ck填写格式')#line:331
        OO00O00O0000000O0 .put (OOOOOOO0OOOO000OO )#line:332
    for OOO0OO0O00OO000OO in range (max_workers ):#line:333
        OOO00O000O000O000 =threading .Thread (target =yd ,args =(OO00O00O0000000O0 ,))#line:334
        OOO00O000O000O000 .start ()#line:335
        OO0OOOOO0OO00OOOO .append (OOO00O000O000O000 )#line:336
        time .sleep (40 )#line:337
    for O00OO0OOO00O0OO00 in OO0OOOOO0OO00OOOO :#line:338
        O00OO0OOO00O0OO00 .join ()#line:339
if __name__ =='__main__':#line:342
    main ()#line:343
