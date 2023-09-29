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

qwbotkey = os.getenv('qwbotkey')  # line:61
if not qwbotkey:  # line:63
    print('请仔细阅读脚本开头的注释并配置好qwbotkey')  # line:64
    exit()  # line:65


def ftime ():#line:68
    OO0O0O00O00OO000O =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:69
    return OO0O0O00O00OO000O #line:70
def debugger (OOOO00000000O00O0 ):#line:73
    if debug :#line:74
        print (OOOO00000000O00O0 )#line:75
def printlog (OO0OO000O00OOO0OO ):#line:78
    if printf :#line:79
        print (OO0OO000O00OOO0OO )#line:80
def send (O0000OOO000O0OOO0 ,title ='通知',url =None ):#line:83
    if not title or not url :#line:84
        OOO0OOO0O0O00OOO0 ={"msgtype":"text","text":{"content":f"{title}\n\n{O0000OOO000O0OOO0}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:91
    else :#line:92
        OOO0OOO0O0O00OOO0 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O0000OOO000O0OOO0 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:105
    OO0O0O00OOO0OOOO0 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:106
    O00O00OO0OOOOOOOO =requests .post (OO0O0O00OOO0OOOO0 ,data =json .dumps (OOO0OOO0O0O00OOO0 )).json ()#line:107
    if O00O00OO0OOOOOOOO .get ('errcode')!=0 :#line:108
        print ('消息发送失败，请检查key和发送格式')#line:109
        return False #line:110
    return O00O00OO0OOOOOOOO #line:111
def getmpinfo (O00O0O0O0000O0O00 ):#line:114
    if not O00O0O0O0000O0O00 or O00O0O0O0000O0O00 =='':#line:115
        return False #line:116
    O00O00O0OO000OOOO ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:118
    OO0O000000O000OOO =requests .get (O00O0O0O0000O0O00 ,headers =O00O00O0OO000OOOO )#line:119
    O00OO0000OO0O0000 =etree .HTML (OO0O000000O000OOO .text )#line:120
    O0O00OO000OO0OO0O =O00OO0000OO0O0000 .xpath ('//meta[@*="og:title"]/@content')#line:122
    if O0O00OO000OO0OO0O :#line:123
        O0O00OO000OO0OO0O =O0O00OO000OO0OO0O [0 ]#line:124
    O00O0OO0OO00O0OOO =O00OO0000OO0O0000 .xpath ('//meta[@*="og:url"]/@content')#line:125
    if O00O0OO0OO00O0OOO :#line:126
        O00O0OO0OO00O0OOO =O00O0OO0OO00O0OOO [0 ].encode ().decode ()#line:127
    try :#line:128
        OOO00OOO00O00OO0O =re .findall (r'biz=(.*?)&',O00O0O0O0000O0O00 )[0 ]#line:129
    except :#line:130
        OOO00OOO00O00OO0O =re .findall (r'biz=(.*?)&',O00O0OO0OO00O0OOO )[0 ]#line:131
    if not OOO00OOO00O00OO0O :#line:132
        return False #line:133
    OO0O0OOO00000O0OO =O00OO0000OO0O0000 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:134
    if OO0O0OOO00000O0OO :#line:135
        OO0O0OOO00000O0OO =OO0O0OOO00000O0OO [0 ].strip ()#line:136
    OOO0OO00O0000O000 =re .findall (r"user_name.DATA'\) : '(.*?)'",OO0O000000O000OOO .text )or O00OO0000OO0O0000 .xpath ('//span[@class="profile_meta_value"]/text()')#line:138
    if OOO0OO00O0000O000 :#line:139
        OOO0OO00O0000O000 =OOO0OO00O0000O000 [0 ]#line:140
    OOO00000O00OOOOO0 =re .findall (r'createTime = \'(.*)\'',OO0O000000O000OOO .text )#line:141
    if OOO00000O00OOOOO0 :#line:142
        OOO00000O00OOOOO0 =OOO00000O00OOOOO0 [0 ][5 :]#line:143
    OOOOO00OO0O0OOOO0 =f'{OOO00000O00OOOOO0} {O0O00OO000OO0OO0O}'#line:144
    OOOOO00OO00OOO00O ={'biz':OOO00OOO00O00OO0O ,'text':OOOOO00OO0O0OOOO0 }#line:145
    return OOOOO00OO00OOO00O #line:146
class Allinone :#line:149
    def __init__ (O0OO0OOO0O00OO000 ,OOO00OOO000OOO0O0 ):#line:150
        O0OO0OOO0O00OO000 .name =OOO00OOO000OOO0O0 ['name']#line:151
        O0OO0OOO0O00OO000 .s =requests .session ()#line:152
        O0OO0OOO0O00OO000 .payload ={"un":OOO00OOO000OOO0O0 ['un'],"token":OOO00OOO000OOO0O0 ['token'],"pageSize":20 }#line:153
        O0OO0OOO0O00OO000 .s .headers ={'Accept':'application/json, text/javascript, */*; q=0.01','Content-Type':'application/json; charset=UTF-8','Host':'u.cocozx.cn','Connection':'keep-alive','User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",'Origin':'http://mr1694971896247.dswxin.cn',}#line:159
        O0OO0OOO0O00OO000 .headers =O0OO0OOO0O00OO000 .s .headers .copy ()#line:160
        O0OO0OOO0O00OO000 .msg =''#line:161
    def get_readhost (OO00OO0000OOOO000 ):#line:163
        O00OOO000O0O0O0O0 ="http://u.cocozx.cn/api/user/getReadHost"#line:164
        OOOO0000O00O00OO0 =OO00OO0000OOOO000 .s .post (O00OOO000O0O0O0O0 ,json =OO00OO0000OOOO000 .payload ).json ()#line:165
        debugger (f'readhome {OOOO0000O00O00OO0}')#line:166
        OO00OO0000OOOO000 .readhost =OOOO0000O00O00OO0 .get ('result')['host']#line:167
        OO00OO0000OOOO000 .headers ['Origin']=OO00OO0000OOOO000 .readhost #line:168
        OO00OO0000OOOO000 .msg +=f'邀请链接：{OO00OO0000OOOO000.readhost}/user/index.html?mid={OO00OO0000OOOO000.huid}\n'#line:169
        printlog (f"{OO00OO0000OOOO000.name}:邀请链接：{OO00OO0000OOOO000.readhost}/user/index.html?mid={OO00OO0000OOOO000.huid}")#line:170
    def stataccess (OOOOOOOOO0OOO000O ):#line:172
        OOO0000OO0OO000OO ='http://u.cocozx.cn/api/user/statAccess'#line:173
        OOOOOOOOO0OOO000O .s .post (OOO0000OO0OO000OO ,json =OOOOOOOOO0OOO000O .payload ).json ()#line:174
    def get_info (O0OOOO00O000O000O ):#line:176
        try :#line:177
            OOOOOOO0O0O0000O0 =O0OOOO00O000O000O .s .post ("http://u.cocozx.cn/api/user/info",json =O0OOOO00O000O000O .payload ).json ()#line:178
            O0OO0OO00OO0OO0OO =OOOOOOO0O0O0000O0 .get ("result")#line:179
            debugger (f'get_info {OOOOOOO0O0O0000O0}')#line:180
            O00OOOO00OO0O00O0 =O0OO0OO00OO0OO0OO .get ('us')#line:181
            if O00OOOO00OO0O00O0 ==2 :#line:182
                O0OOOO00O000O000O .msg +=f'账号：{O0OOOO00O000O000O.name}已被封\n'#line:183
                printlog (f'账号：{O0OOOO00O000O000O.name}已被封')#line:184
                return False #line:185
            O0OOOO00O000O000O .msg +=f"""账号:{O0OOOO00O000O000O.name}，今日阅读次数:{O0OO0OO00OO0OO0OO["dayCount"]}，当前花儿:{O0OO0OO00OO0OO0OO["moneyCurrent"]}，累计阅读次数:{O0OO0OO00OO0OO0OO["doneWx"]}\n"""#line:186
            printlog (f"""账号:{O0OOOO00O000O000O.name}，今日阅读次数:{O0OO0OO00OO0OO0OO["dayCount"]}，当前花儿:{O0OO0OO00OO0OO0OO["moneyCurrent"]}，累计阅读次数:{O0OO0OO00OO0OO0OO["doneWx"]}""")#line:188
            OO0OO00O00O0OO0O0 =int (O0OO0OO00OO0OO0OO ["moneyCurrent"])#line:189
            O0OOOO00O000O000O .huid =O0OO0OO00OO0OO0OO .get ('uid')#line:190
            return OO0OO00O00O0OO0O0 #line:191
        except :#line:192
            return False #line:193
    def psmoneyc (O0OOO0O0OO0O0OO00 ):#line:195
        O0OO00000OOO0O00O ={**O0OOO0O0OO0O0OO00 .payload ,**{'mid':O0OOO0O0OO0O0OO00 .huid }}#line:196
        try :#line:197
            O0O00O00O0O00O0OO =O0OOO0O0OO0O0OO00 .s .post ("http://u.cocozx.cn/api/user/psmoneyc",json =O0OO00000OOO0O00O ).json ()#line:198
            O0OOO0O0OO0O0OO00 .msg +=f"感谢下级送来的{O0O00O00O0O00O0OO['result']['val']}花儿\n"#line:199
        except :#line:200
            pass #line:201
        return #line:202
    def get_status (O0OO000O000O000O0 ):#line:204
        O0OOO00OO00OO000O =requests .post ("http://u.cocozx.cn/api/user/read",headers =O0OO000O000O000O0 .headers ,json =O0OO000O000O000O0 .payload ).json ()#line:205
        debugger (f'getstatus {O0OOO00OO00OO000O}')#line:206
        O0OO000O000O000O0 .status =O0OOO00OO00OO000O .get ("result").get ("status")#line:207
        if O0OO000O000O000O0 .status ==40 :#line:208
            O0OO000O000O000O0 .msg +="文章还没有准备好\n"#line:209
            printlog (f"{O0OO000O000O000O0.name}:文章还没有准备好")#line:210
            return #line:211
        elif O0OO000O000O000O0 .status ==50 :#line:212
            O0OO000O000O000O0 .msg +="阅读失效\n"#line:213
            printlog (f"{O0OO000O000O000O0.name}:阅读失效")#line:214
            return #line:215
        elif O0OO000O000O000O0 .status ==60 :#line:216
            O0OO000O000O000O0 .msg +="已经全部阅读完了\n"#line:217
            printlog (f"{O0OO000O000O000O0.name}:已经全部阅读完了")#line:218
            return #line:219
        elif O0OO000O000O000O0 .status ==70 :#line:220
            O0OO000O000O000O0 .msg +="下一轮还未开启\n"#line:221
            printlog (f"{O0OO000O000O000O0.name}:下一轮还未开启")#line:222
            return #line:223
        elif O0OO000O000O000O0 .status ==10 :#line:224
            O0OO00000OOOOOOOO =O0OOO00OO00OO000O ["result"]["url"]#line:225
            O0OO000O000O000O0 .msg +='-'*50 +"\n阅读链接获取成功\n"#line:226
            printlog (f"{O0OO000O000O000O0.name}:阅读链接获取成功")#line:227
            return O0OO00000OOOOOOOO #line:228
    def submit (O00O0O00O0O0OOOOO ):#line:230
        OOOOO00000000OOO0 ={**{'type':1 },**O00O0O00O0O0OOOOO .payload }#line:231
        O0OOOOO0O0OO00000 =requests .post ("http://u.cocozx.cn/api/user/submit?zx=&xz=1",headers =O00O0O00O0O0OOOOO .headers ,json =OOOOO00000000OOO0 )#line:232
        OOO0O0OOOOOO0OOO0 =O0OOOOO0O0OO00000 .json ().get ('result')#line:233
        debugger ('submit '+O0OOOOO0O0OO00000 .text )#line:234
        O00O0O00O0O0OOOOO .msg +=f'阅读成功,获得花儿{OOO0O0OOOOOO0OOO0["val"]}，当前剩余次数:{OOO0O0OOOOOO0OOO0["progress"]}\n'#line:235
        printlog (f"{O00O0O00O0O0OOOOO.name}:阅读成功,获得花儿{OOO0O0OOOOOO0OOO0['val']}，当前剩余次数:{OOO0O0OOOOOO0OOO0['progress']}")#line:236
    def read (OOOOOOO0OO0OO0OOO ):#line:238
        while True :#line:239
            O00O000OOO000O0O0 =OOOOOOO0OO0OO0OOO .get_status ()#line:240
            if not O00O000OOO000O0O0 :#line:241
                if OOOOOOO0OO0OO0OOO .status ==30 :#line:242
                    time .sleep (3 )#line:243
                    continue #line:244
                break #line:245
            OOOOOOOOOO00O000O =getmpinfo (O00O000OOO000O0O0 )#line:246
            if not OOOOOOOOOO00O000O :#line:247
                printlog (f'{OOOOOOO0OO0OO0OOO.name}:获取文章信息失败，程序中止')#line:248
                return False #line:249
            OOOOOOO0OO0OO0OOO .msg +='开始阅读 '+OOOOOOOOOO00O000O ['text']+'\n'#line:250
            printlog (f'{OOOOOOO0OO0OO0OOO.name}:开始阅读 '+OOOOOOOOOO00O000O ['text'])#line:251
            OO00OO0OO00O0000O =randint (7 ,10 )#line:252
            if OOOOOOOOOO00O000O ['biz']=="Mzg2Mzk3Mjk5NQ==":#line:253
                OOOOOOO0OO0OO0OOO .msg +='当前正在阅读检测文章\n'#line:254
                printlog (f'{OOOOOOO0OO0OO0OOO.name}:正在阅读检测文章')#line:255
                send (f'{OOOOOOO0OO0OO0OOO.name}  花花阅读正在读检测文章',OOOOOOOOOO00O000O ['text'],O00O000OOO000O0O0 )#line:256
                time .sleep (60 )#line:257
            printlog (f'{OOOOOOO0OO0OO0OOO.name}：模拟阅读{OO00OO0OO00O0000O}秒')#line:258
            time .sleep (OO00OO0OO00O0000O )#line:259
            OOOOOOO0OO0OO0OOO .submit ()#line:260
    def tixian (OO0O00OO0OO00OO00 ):#line:262
        global txe #line:263
        OO0O0OO0000O00O0O =OO0O00OO0OO00OO00 .get_info ()#line:264
        if OO0O0OO0000O00O0O <txbz :#line:265
            OO0O00OO0OO00OO00 .msg +='你的花儿不多了\n'#line:266
            printlog (f'{OO0O00OO0OO00OO00.name}你的花儿不多了')#line:267
            return False #line:268
        if 10000 <=OO0O0OO0000O00O0O <49999 :#line:269
            txe =10000 #line:270
        elif 5000 <=OO0O0OO0000O00O0O <10000 :#line:271
            txe =5000 #line:272
        elif 3000 <=OO0O0OO0000O00O0O <5000 :#line:273
            txe =3000 #line:274
        elif OO0O0OO0000O00O0O >=50000 :#line:275
            txe =50000 #line:276
        OO0O00OO0OO00OO00 .msg +=f"提现金额:{txe}"#line:277
        printlog (f'{OO0O00OO0OO00OO00.name}提现金额:{txe}')#line:278
        OOO000OO00O0OO00O ={**OO0O00OO0OO00OO00 .payload ,**{"val":txe }}#line:279
        try :#line:280
            O000O0OOOOO0O0O00 =OO0O00OO0OO00OO00 .s .post ("http://u.cocozx.cn/api/user/wd",json =OOO000OO00O0OO00O ).json ()#line:281
            OO0O00OO0OO00OO00 .msg +=f"提现结果:{O000O0OOOOO0O0O00.get('msg')}\n"#line:282
            printlog (f'{OO0O00OO0OO00OO00.name}提现结果：{O000O0OOOOO0O0O00.get("msg")}')#line:283
        except :#line:284
            OO0O00OO0OO00OO00 .msg +=f"自动提现不成功，发送通知手动提现\n"#line:285
            printlog (f"{OO0O00OO0OO00OO00.name}:自动提现不成功，发送通知手动提现")#line:286
            send (f'可提现金额 {int(txe) / 10000}元，点击提现',title =f'惜之酱提醒您 {OO0O00OO0OO00OO00.name} 花花阅读可以提现了',url =f'{OO0O00OO0OO00OO00.readhost}/user/index.html?mid=FK73K93DA')#line:288
    def run (O00O0O0OOOOO0OOO0 ):#line:290
        if O00O0O0OOOOO0OOO0 .get_info ():#line:291
            O00O0O0OOOOO0OOO0 .stataccess ()#line:292
            O00O0O0OOOOO0OOO0 .get_readhost ()#line:293
            O00O0O0OOOOO0OOO0 .psmoneyc ()#line:294
            O00O0O0OOOOO0OOO0 .read ()#line:295
            O00O0O0OOOOO0OOO0 .tixian ()#line:296
        if not printf :#line:297
            print (O00O0O0OOOOO0OOO0 .msg .strip ())#line:298
def yd (O0O000OO00OO00OO0 ):#line:301
    while not O0O000OO00OO00OO0 .empty ():#line:302
        OO000OO0O0O0OO0O0 =O0O000OO00OO00OO0 .get ()#line:303
        try :#line:304
            O0OOOOOOOO0OOO0OO =Allinone (OO000OO0O0O0OO0O0 )#line:305
            O0OOOOOOOO0OOO0OO .run ()#line:306
        except Exception as O000OOO0OO000O0O0 :#line:307
            print (O000OOO0OO000O0O0 )#line:308
def get_ver ():#line:311
    O0O00OO0OOOOO0000 ='khh V1.2.2'#line:312
    OOO000OOOOOO00O0O ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:315
    OO0O0O00O00O0O000 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OOO000OOOOOO00O0O ).json ()#line:317
    OOOOO0O0O0O0O00OO =O0O00OO0OOOOO0000 .split (' ')[1 ]#line:318
    O000OOOO000OO0O0O =OO0O0O00O00O0O000 .get ('version').get (O0O00OO0OOOOO0000 .split (' ')[0 ])#line:319
    OOOOOOO0OOO000O0O =f"当前版本 {OOOOO0O0O0O0O00OO}，仓库版本 {O000OOOO000OO0O0O}"#line:320
    if OOOOO0O0O0O0O00OO <O000OOOO000OO0O0O :#line:321
        OOOOOOO0OOO000O0O +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:322
    return OOOOOOO0OOO000O0O #line:323
def main ():#line:326
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:327
    OOO00OO0O00OOOOOO =os .getenv ('aiock')#line:328
    if not OOO00OO0O00OOOOOO :#line:329
        print ('请仔细阅读脚本开头的注释并配置好aiock')#line:330
        exit ()#line:331
    try :#line:332
        OOO00OO0O00OOOOOO =ast .literal_eval (OOO00OO0O00OOOOOO )#line:333
    except :#line:334
        pass #line:335
    OO0O0O0OOOO0000OO =Queue ()#line:336
    OOO00OO00OOO0OOO0 =[]#line:337
    for O0OOO00O00000O000 ,O000O00O000O00O0O in enumerate (OOO00OO0O00OOOOOO ,start =1 ):#line:338
        printlog (f'{O000O00O000O00O0O}\n以上是账号{O0OOO00O00000O000}的ck，请核对是否正确，如不正确，请检查ck填写格式')#line:339
        OO0O0O0OOOO0000OO .put (O000O00O000O00O0O )#line:340
    for O0OOO00O00000O000 in range (max_workers ):#line:341
        O0O0000O000O000OO =threading .Thread (target =yd ,args =(OO0O0O0OOOO0000OO ,))#line:342
        O0O0000O000O000OO .start ()#line:343
        OOO00OO00OOO0OOO0 .append (O0O0000O000O000OO )#line:344
        time .sleep (40 )#line:345
    for O00O0O0O0OOOOOOO0 in OOO00OO00OOO0OOO0 :#line:346
        O00O0O0O0OOOOOOO0 .join ()#line:347
if __name__ =='__main__':#line:350
    main ()#line:351
