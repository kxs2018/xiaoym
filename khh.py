"""
花花阅读入口：http://mr138301519.nmyebvvmntj.cloud/user/index.html?mid=EG5EVNLF3

http://u.cocozx.cn/api/user/info
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
3. 如果装不上，①请ssh连接到服务器 ②docker exec -it ql bash (ql是青龙容器的名字，不会就问百度) ③pip install pip -U
4. 再装不上依赖就放弃吧
------------------------------------------------------
提现标准默认是5000
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
txbz = 5000  # 不低于3000，平台的提现标准为3000
"""设置为5000，即为5毛起提"""

qwbotkey =os .getenv ('qwbotkey')#line:61
if not qwbotkey :#line:63
    print ('请仔细阅读脚本开头的注释并配置好qwbotkey')#line:64
    exit ()#line:65
def ftime ():#line:68
    OOO00O00O0O0O0OO0 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:69
    return OOO00O00O0O0O0OO0 #line:70
def debugger (O0OO0000O0O0OO0OO ):#line:73
    if debug :#line:74
        print (O0OO0000O0O0OO0OO )#line:75
def printlog (O000O000000OO00OO ):#line:78
    if printf :#line:79
        print (O000O000000OO00OO )#line:80
def send (O000O0OOO000O0000 ,title ='通知',url =None ):#line:83
    if not title or not url :#line:84
        O0OO00OO0000OOO0O ={"msgtype":"text","text":{"content":f"{title}\n\n{O000O0OOO000O0000}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:91
    else :#line:92
        O0OO00OO0000OOO0O ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O000O0OOO000O0000 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:105
    OOO0OO00O00OOO00O =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:106
    OO000OO0O000O0OOO =requests .post (OOO0OO00O00OOO00O ,data =json .dumps (O0OO00OO0000OOO0O )).json ()#line:107
    if OO000OO0O000O0OOO .get ('errcode')!=0 :#line:108
        print ('消息发送失败，请检查key和发送格式')#line:109
        return False #line:110
    return OO000OO0O000O0OOO #line:111
def getmpinfo (O0O0OOOOOOOOOOOO0 ):#line:114
    if not O0O0OOOOOOOOOOOO0 or O0O0OOOOOOOOOOOO0 =='':#line:115
        return False #line:116
    O0OO0OO00OOOO0OOO ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:118
    OOOO00O0OO0OO0OOO =requests .get (O0O0OOOOOOOOOOOO0 ,headers =O0OO0OO00OOOO0OOO )#line:119
    OOO00O0OO0O00O00O =etree .HTML (OOOO00O0OO0OO0OOO .text )#line:120
    OOO00O00O0O0O000O =OOO00O0OO0O00O00O .xpath ('//meta[@*="og:title"]/@content')#line:122
    if OOO00O00O0O0O000O :#line:123
        OOO00O00O0O0O000O =OOO00O00O0O0O000O [0 ]#line:124
    O000O0OOOO0O0O0O0 =OOO00O0OO0O00O00O .xpath ('//meta[@*="og:url"]/@content')#line:125
    if O000O0OOOO0O0O0O0 :#line:126
        O000O0OOOO0O0O0O0 =O000O0OOOO0O0O0O0 [0 ].encode ().decode ()#line:127
    try :#line:128
        O000OOO00OOO0000O =re .findall (r'biz=(.*?)&',O0O0OOOOOOOOOOOO0 )#line:129
    except :#line:130
        O000OOO00OOO0000O =re .findall (r'biz=(.*?)&',O000O0OOOO0O0O0O0 )#line:131
    if O000OOO00OOO0000O :#line:132
        O000OOO00OOO0000O =O000OOO00OOO0000O [0 ]#line:133
    OOO0OO0O0OOOO0000 =OOO00O0OO0O00O00O .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:134
    if OOO0OO0O0OOOO0000 :#line:135
        OOO0OO0O0OOOO0000 =OOO0OO0O0OOOO0000 [0 ].strip ()#line:136
    O0OOOOOO00O0O0O00 =re .findall (r"user_name.DATA'\) : '(.*?)'",OOOO00O0OO0OO0OOO .text )or OOO00O0OO0O00O00O .xpath ('//span[@class="profile_meta_value"]/text()')#line:138
    if O0OOOOOO00O0O0O00 :#line:139
        O0OOOOOO00O0O0O00 =O0OOOOOO00O0O0O00 [0 ]#line:140
    O0O0O0OOOO00O0000 =re .findall (r'createTime = \'(.*)\'',OOOO00O0OO0OO0OOO .text )#line:141
    if O0O0O0OOOO00O0000 :#line:142
        O0O0O0OOOO00O0000 =O0O0O0OOOO00O0000 [0 ][5 :]#line:143
    OOO0000OO0OO00O0O =f'{O0O0O0OOOO00O0000} {OOO00O00O0O0O000O}'#line:144
    O0O0OOOOO0OO0OOOO ={'biz':O000OOO00OOO0000O ,'text':OOO0000OO0OO00O0O }#line:145
    return O0O0OOOOO0OO0OOOO #line:146
class Allinone :#line:149
    def __init__ (O0OOO0OO000O00O0O ,OO00OO0OO0O0O000O ):#line:150
        O0OOO0OO000O00O0O .name =OO00OO0OO0O0O000O ['name']#line:151
        O0OOO0OO000O00O0O .s =requests .session ()#line:152
        O0OOO0OO000O00O0O .payload ={"un":OO00OO0OO0O0O000O ['un'],"token":OO00OO0OO0O0O000O ['token'],"pageSize":20 }#line:153
        O0OOO0OO000O00O0O .s .headers ={'Accept':'application/json, text/javascript, */*; q=0.01','Content-Type':'application/json; charset=UTF-8','Host':'u.cocozx.cn','Connection':'keep-alive','User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",'Origin':'http://mr1694971896247.dswxin.cn',}#line:159
        O0OOO0OO000O00O0O .headers =O0OOO0OO000O00O0O .s .headers .copy ()#line:160
        O0OOO0OO000O00O0O .msg =''#line:161
    def get_readhost (O00O0OO0O0OOO00O0 ):#line:163
        O000000OO0O0OO0O0 ="http://u.cocozx.cn/api/user/getReadHost"#line:164
        OOOOO000O000O0OO0 =O00O0OO0O0OOO00O0 .s .post (O000000OO0O0OO0O0 ,json =O00O0OO0O0OOO00O0 .payload ).json ()#line:165
        debugger (f'readhome {OOOOO000O000O0OO0}')#line:166
        O00O0OO0O0OOO00O0 .readhost =OOOOO000O000O0OO0 .get ('result')['host']#line:167
        O00O0OO0O0OOO00O0 .headers ['Origin']=O00O0OO0O0OOO00O0 .readhost #line:168
        O00O0OO0O0OOO00O0 .msg +=f'邀请链接：{O00O0OO0O0OOO00O0.readhost}/user/index.html?mid={O00O0OO0O0OOO00O0.huid}\n'#line:169
        printlog (f"{O00O0OO0O0OOO00O0.name}:邀请链接：{O00O0OO0O0OOO00O0.readhost}/user/index.html?mid={O00O0OO0O0OOO00O0.huid}")#line:170
    def stataccess (OO000OOO0OO0O0000 ):#line:172
        OOOOOOO00OOOOOOOO ='http://u.cocozx.cn/api/user/statAccess'#line:173
        OO000OOO0OO0O0000 .s .post (OOOOOOO00OOOOOOOO ,json =OO000OOO0OO0O0000 .payload ).json ()#line:174
    def get_info (O0OO00OOO0000OO00 ):#line:176
        try :#line:177
            OOOO0O00O000000OO =O0OO00OOO0000OO00 .s .post ("http://u.cocozx.cn/api/user/info",json =O0OO00OOO0000OO00 .payload ).json ()#line:178
            OOOO00O00000O00O0 =OOOO0O00O000000OO .get ("result")#line:179
            debugger (f'get_info {OOOO0O00O000000OO}')#line:180
            O0O00OOOO000O000O =OOOO00O00000O00O0 .get ('us')#line:181
            if O0O00OOOO000O000O ==2 :#line:182
                O0OO00OOO0000OO00 .msg +=f'账号：{O0OO00OOO0000OO00.name}已被封\n'#line:183
                printlog (f'账号：{O0OO00OOO0000OO00.name}已被封')#line:184
                return False #line:185
            O0OO00OOO0000OO00 .msg +=f"""账号:{O0OO00OOO0000OO00.name}，今日阅读次数:{OOOO00O00000O00O0["dayCount"]}，当前花儿:{OOOO00O00000O00O0["moneyCurrent"]}，累计阅读次数:{OOOO00O00000O00O0["doneWx"]}\n"""#line:186
            printlog (f"""账号:{O0OO00OOO0000OO00.name}，今日阅读次数:{OOOO00O00000O00O0["dayCount"]}，当前花儿:{OOOO00O00000O00O0["moneyCurrent"]}，累计阅读次数:{OOOO00O00000O00O0["doneWx"]}""")#line:188
            O00000000OO0O0O0O =int (OOOO00O00000O00O0 ["moneyCurrent"])#line:189
            O0OO00OOO0000OO00 .huid =OOOO00O00000O00O0 .get ('uid')#line:190
            return O00000000OO0O0O0O #line:191
        except :#line:192
            return False #line:193
    def psmoneyc (O0OO000O0OOO000OO ):#line:195
        O0OO00O0OO00O0O00 ={**O0OO000O0OOO000OO .payload ,**{'mid':O0OO000O0OOO000OO .huid }}#line:196
        try :#line:197
            O00OO0000OOOOO0O0 =O0OO000O0OOO000OO .s .post ("http://u.cocozx.cn/api/user/psmoneyc",json =O0OO00O0OO00O0O00 ).json ()#line:198
            O0OO000O0OOO000OO .msg +=f"感谢下级送来的{O00OO0000OOOOO0O0['result']['val']}花儿\n"#line:199
        except :#line:200
            pass #line:201
        return #line:202
    def get_status (OO0OO00O0O0OO0O00 ):#line:204
        OO0O0O0O0OO000OO0 =requests .post ("http://u.cocozx.cn/api/user/read",headers =OO0OO00O0O0OO0O00 .headers ,json =OO0OO00O0O0OO0O00 .payload ).json ()#line:205
        debugger (f'getstatus {OO0O0O0O0OO000OO0}')#line:206
        OO0OO00O0O0OO0O00 .status =OO0O0O0O0OO000OO0 .get ("result").get ("status")#line:207
        if OO0OO00O0O0OO0O00 .status ==40 :#line:208
            OO0OO00O0O0OO0O00 .msg +="文章还没有准备好\n"#line:209
            printlog (f"{OO0OO00O0O0OO0O00.name}:文章还没有准备好")#line:210
            return #line:211
        elif OO0OO00O0O0OO0O00 .status ==50 :#line:212
            OO0OO00O0O0OO0O00 .msg +="阅读失效\n"#line:213
            printlog (f"{OO0OO00O0O0OO0O00.name}:阅读失效")#line:214
            return #line:215
        elif OO0OO00O0O0OO0O00 .status ==60 :#line:216
            OO0OO00O0O0OO0O00 .msg +="已经全部阅读完了\n"#line:217
            printlog (f"{OO0OO00O0O0OO0O00.name}:已经全部阅读完了")#line:218
            return #line:219
        elif OO0OO00O0O0OO0O00 .status ==70 :#line:220
            OO0OO00O0O0OO0O00 .msg +="下一轮还未开启\n"#line:221
            printlog (f"{OO0OO00O0O0OO0O00.name}:下一轮还未开启")#line:222
            return #line:223
        elif OO0OO00O0O0OO0O00 .status ==10 :#line:224
            OOOO0OO00O0OO000O =OO0O0O0O0OO000OO0 ["result"]["url"]#line:225
            OO0OO00O0O0OO0O00 .msg +='-'*50 +"\n阅读链接获取成功\n"#line:226
            printlog (f"{OO0OO00O0O0OO0O00.name}:阅读链接获取成功")#line:227
            return OOOO0OO00O0OO000O #line:228
    def submit (OO0O0OOO0OOOOOOOO ):#line:230
        OOO0OOO000O000O0O ={**{'type':1 },**OO0O0OOO0OOOOOOOO .payload }#line:231
        OOO0OOOOO000OOO00 =requests .post ("http://u.cocozx.cn/api/user/submit?zx=&xz=1",headers =OO0O0OOO0OOOOOOOO .headers ,json =OOO0OOO000O000O0O )#line:232
        O00O0O0000O0000OO =OOO0OOOOO000OOO00 .json ().get ('result')#line:233
        debugger ('submit '+OOO0OOOOO000OOO00 .text )#line:234
        OO0O0OOO0OOOOOOOO .msg +=f'阅读成功,获得花儿{O00O0O0000O0000OO["val"]}，当前剩余次数:{O00O0O0000O0000OO["progress"]}\n'#line:235
        printlog (f"{OO0O0OOO0OOOOOOOO.name}:阅读成功,获得花儿{O00O0O0000O0000OO['val']}，当前剩余次数:{O00O0O0000O0000OO['progress']}")#line:236
    def read (OO0OO0OOOOO0O0OO0 ):#line:238
        while True :#line:239
            O0OOO0O0O0O000O0O =OO0OO0OOOOO0O0OO0 .get_status ()#line:240
            if not O0OOO0O0O0O000O0O :#line:241
                if OO0OO0OOOOO0O0OO0 .status ==30 :#line:242
                    time .sleep (3 )#line:243
                    continue #line:244
                break #line:245
            OOO00OOO0OO0OOO00 =getmpinfo (O0OOO0O0O0O000O0O )#line:246
            OO0OO0OOOOO0O0OO0 .msg +='开始阅读 '+OOO00OOO0OO0OOO00 ['text']+'\n'#line:247
            printlog (f'{OO0OO0OOOOO0O0OO0.name}:开始阅读 '+OOO00OOO0OO0OOO00 ['text'])#line:248
            O0O0O0O000000O000 =randint (7 ,10 )#line:249
            if OOO00OOO0OO0OOO00 ['biz']=="Mzg2Mzk3Mjk5NQ==":#line:250
                OO0OO0OOOOO0O0OO0 .msg +='当前正在阅读检测文章\n'#line:251
                printlog (f'{OO0OO0OOOOO0O0OO0.name}:正在阅读检测文章')#line:252
                send (f'{OO0OO0OOOOO0O0OO0.name}  花花阅读正在读检测文章',OOO00OOO0OO0OOO00 ['text'],O0OOO0O0O0O000O0O )#line:253
                time .sleep (60 )#line:254
            printlog (f'{OO0OO0OOOOO0O0OO0.name}：模拟阅读{O0O0O0O000000O000}秒')#line:255
            time .sleep (O0O0O0O000000O000 )#line:256
            OO0OO0OOOOO0O0OO0 .submit ()#line:257
    def tixian (OO000OOOO00OO000O ):#line:259
        global txe #line:260
        O0000O0000000O0OO =OO000OOOO00OO000O .get_info ()#line:261
        if O0000O0000000O0OO <txbz :#line:262
            OO000OOOO00OO000O .msg +='你的花儿不多了\n'#line:263
            printlog (f'{OO000OOOO00OO000O.name}你的花儿不多了')#line:264
            return False #line:265
        if 10000 <=O0000O0000000O0OO <49999 :#line:266
            txe =10000 #line:267
        elif 5000 <=O0000O0000000O0OO <10000 :#line:268
            txe =5000 #line:269
        elif 3000 <=O0000O0000000O0OO <5000 :#line:270
            txe =3000 #line:271
        elif O0000O0000000O0OO >=50000 :#line:272
            txe =50000 #line:273
        OO000OOOO00OO000O .msg +=f"提现金额:{txe}"#line:274
        printlog (f'{OO000OOOO00OO000O.name}提现金额:{txe}')#line:275
        OOOO0O0O0O00000O0 ={**OO000OOOO00OO000O .payload ,**{"val":txe }}#line:276
        try :#line:277
            OOOOO0OO00OOOOO00 =OO000OOOO00OO000O .s .post ("http://u.cocozx.cn/api/user/wd",json =OOOO0O0O0O00000O0 ).json ()#line:278
            OO000OOOO00OO000O .msg +=f"提现结果:{OOOOO0OO00OOOOO00.get('msg')}\n"#line:279
            printlog (f'{OO000OOOO00OO000O.name}提现结果：{OOOOO0OO00OOOOO00.get("msg")}')#line:280
        except :#line:281
            OO000OOOO00OO000O .msg +=f"自动提现不成功，发送通知手动提现\n"#line:282
            printlog (f"{OO000OOOO00OO000O.name}:自动提现不成功，发送通知手动提现")#line:283
            send (f'可提现金额 {int(txe) / 10000}元，点击提现',title =f'惜之酱提醒您 {OO000OOOO00OO000O.name} 花花阅读可以提现了',url =f'{OO000OOOO00OO000O.readhost}/user/index.html?mid=FK73K93DA')#line:285
    def run (O0OOO0O00OOOOO0O0 ):#line:287
        if O0OOO0O00OOOOO0O0 .get_info ():#line:288
            O0OOO0O00OOOOO0O0 .stataccess ()#line:289
            O0OOO0O00OOOOO0O0 .get_readhost ()#line:290
            O0OOO0O00OOOOO0O0 .psmoneyc ()#line:291
            O0OOO0O00OOOOO0O0 .read ()#line:292
            O0OOO0O00OOOOO0O0 .tixian ()#line:293
        if not printf :#line:294
            print (O0OOO0O00OOOOO0O0 .msg .strip ())#line:295
def yd (OO0OO0O000OOO0OO0 ):#line:298
    while not OO0OO0O000OOO0OO0 .empty ():#line:299
        OO000OOOOO0O00OO0 =OO0OO0O000OOO0OO0 .get ()#line:300
        try :#line:301
            O0OOOO0000000OO00 =Allinone (OO000OOOOO0O00OO0 )#line:302
            O0OOOO0000000OO00 .run ()#line:303
        except Exception as OO00OOOOOO0OO00OO :#line:304
            print (OO00OOOOOO0OO00OO )#line:305
def get_ver ():#line:308
    O0OOOO00OO00OO0O0 ='khh V1.2'#line:309
    O00000OOOOOOO0OOO ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:312
    OO0OOO0OO0000O0O0 =requests .get ('https://ghproxy.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json',headers =O00000OOOOOOO0OOO ).json ()#line:314
    OO00O0O0000000OOO =O0OOOO00OO00OO0O0 .split (' ')[1 ]#line:315
    OOOO0000O0OO0OOOO =OO0OOO0OO0000O0O0 .get ('version').get (O0OOOO00OO00OO0O0 .split (' ')[0 ])#line:316
    O00OO000OO0OOO00O =f"当前版本 {OO00O0O0000000OOO}，仓库版本 {OOOO0000O0OO0OOOO}"#line:317
    if OO00O0O0000000OOO <OOOO0000O0OO0OOOO :#line:318
        O00OO000OO0OOO00O +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:319
    return O00OO000OO0OOO00O #line:320
def main ():#line:323
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:324
    O0OO000O000OO0000 =os .getenv ('aiock')#line:325
    if not O0OO000O000OO0000 :#line:326
        print ('请仔细阅读脚本开头的注释并配置好aiock')#line:327
        exit ()#line:328
    try :#line:329
        O0OO000O000OO0000 =ast .literal_eval (O0OO000O000OO0000 )#line:330
    except :#line:331
        pass #line:332
    OO00OO0000O0OOO00 =Queue ()#line:333
    OOOOO0O0OOO0O0OOO =[]#line:334
    for OOO0O00OO0O000O0O ,O000O0OOOOO00OOO0 in enumerate (O0OO000O000OO0000 ,start =1 ):#line:335
        printlog (f'{O000O0OOOOO00OOO0}\n以上是账号{OOO0O00OO0O000O0O}的ck，请核对是否正确，如不正确，请检查ck填写格式')#line:336
        OO00OO0000O0OOO00 .put (O000O0OOOOO00OOO0 )#line:337
    for OOO0O00OO0O000O0O in range (max_workers ):#line:338
        OOOO0O0O0OOO000OO =threading .Thread (target =yd ,args =(OO00OO0000O0OOO00 ,))#line:339
        OOOO0O0O0OOO000OO .start ()#line:340
        OOOOO0O0OOO0O0OOO .append (OOOO0O0O0OOO000OO )#line:341
        time .sleep (40 )#line:342
    for OO0000OOO000O0OOO in OOOOO0O0OOO0O0OOO :#line:343
        OO0000OOO000O0OOO .join ()#line:344
if __name__ =='__main__':#line:347
    main ()#line:348