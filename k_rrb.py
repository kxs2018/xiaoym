# -*- coding: utf-8 -*-
# k_rrb
# Author: 惜之酱

"""
new Env('人人帮');
先运行脚本，有问题再问
入口：http://ebb.maisucaiya.cloud/user/index.html?mid=1702983440137322496
如微信打不开，可复制到浏览器打开
"""
"""实时日志开关"""
printf = 1
"""1为开，0为关"""

"""debug模式开关"""
debug = 1
"""1为开，打印调试日志；0为关，不打印"""

"""企业微信推送开关"""
sendable = 1  # 开启后必须设置qwbotkey才能运行
"""1为开，0为关"""

"""wxpusher推送开关"""
pushable = 1  # 开启后必须设置pushconfig才能运行
"""1为开，0为关"""

"""线程数量设置"""
max_workers = 5
"""设置为3，即最多有3个任务同时进行"""

"""设置提现标准"""
txbz = 5000  # 不低于5000，平台的提现标准为5000
"""设置为5000，即为5毛起提"""

"""并发延迟设置"""
delay_time = 40
"""设置为40即每隔40秒新增一个号做任务，直到数量达到max_workers"""

import json #line:34
from random import randint #line:35
import os #line:36
import time #line:37
import requests #line:38
import ast #line:39
import re #line:40
import datetime #line:41
import threading #line:42
from queue import Queue #line:43
def get_msg ():#line:46
    O0OOO0OOOO0OOO0O0 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:48
    O000O000O00O0O0O0 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O0OOO0OOOO0OOO0O0 ).json ()#line:49
    return O000O000O00O0O0O0 #line:50
_O0O0OOOOOO0OO0O00 =get_msg ()#line:53
try :#line:54
    from lxml import etree #line:55
except :#line:56
    print (_O0O0OOOOOO0OO0O00 .get ('help')['lxml'])#line:57
if sendable :#line:59
    qwbotkey =os .getenv ('qwbotkey')#line:60
    if not qwbotkey :#line:61
        print (_O0O0OOOOOO0OO0O00 .get ('help')['qwbotkey'])#line:62
        exit ()#line:63
if pushable :#line:65
    pushconfig =os .getenv ('pushconfig')#line:66
    if not pushconfig :#line:67
        print (_O0O0OOOOOO0OO0O00 .get ('help')['pushconfig'])#line:68
        exit ()#line:69
    try :#line:70
        pushconfig =ast .literal_eval (pushconfig )#line:71
    except :#line:72
        pass #line:73
    if isinstance (pushconfig ,dict ):#line:74
        appToken =pushconfig ['appToken']#line:75
        uids =pushconfig ['uids']#line:76
        topicids =pushconfig ['topicids']#line:77
    else :#line:78
        try :#line:79
            "appToken=AT_pCenRjs;uids=['UID_9MZ','UID_T4xlqWx9x'];topicids=['xxx']"#line:80
            appToken =pushconfig .split (';')[0 ].split ('=')[1 ]#line:81
            uids =ast .literal_eval (pushconfig .split (';')[1 ].split ('=')[1 ])#line:82
            topicids =ast .literal_eval (pushconfig .split (';')[2 ].split ('=')[1 ])#line:83
        except :#line:84
            print (_O0O0OOOOOO0OO0O00 .get ('help')['pushconfig'])#line:85
            exit ()#line:86
if not pushable and not sendable :#line:88
    print ('啥通知方式都不配置，你想上天吗')#line:89
    exit ()#line:90
def ftime ():#line:93
    O00O0O000000O0000 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:94
    return O00O0O000000O0000 #line:95
def debugger (O000O0OOO00000OO0 ):#line:98
    if debug :#line:99
        print (O000O0OOO00000OO0 )#line:100
def printlog (OO0O0O0O0OOO0O000 ):#line:103
    if printf :#line:104
        print (OO0O0O0O0OOO0O000 )#line:105
def send (O00OOOOOOO00OOOO0 ,title ='通知',url =None ):#line:108
    if not title or not url :#line:109
        O0OOOO0O0O000OO00 ={"msgtype":"text","text":{"content":f"{title}\n\n{O00OOOOOOO00OOOO0}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:116
    else :#line:117
        O0OOOO0O0O000OO00 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O00OOOOOOO00OOOO0 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:122
    O00O0OO0OO0O0O0OO =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:123
    O00OO0O00O0000O00 =requests .post (O00O0OO0OO0O0O0OO ,data =json .dumps (O0OOOO0O0O000OO00 )).json ()#line:124
    if O00OO0O00O0000O00 .get ('errcode')!=0 :#line:125
        print ('消息发送失败，请检查key和发送格式')#line:126
        return False #line:127
    return O00OO0O00O0000O00 #line:128
def push (OOOOO0O0000OO0OO0 ,title ='通知',url ='',uid =None ):#line:131
    if uid :#line:132
        uids .append (uid )#line:133
    O0O00OOOOO00O0000 ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',OOOOO0O0000OO0OO0 ).replace ('url',url )#line:135
    OOO0OO00OOO0O00O0 ={"appToken":appToken ,"content":O0O00OOOOO00O0000 ,"summary":title ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:145
    OOO000O000O00OO00 ='http://wxpusher.zjiecode.com/api/send/message'#line:146
    OOO00000O000000OO =requests .post (url =OOO000O000O00OO00 ,json =OOO0OO00OOO0O00O0 ).json ()#line:147
    if OOO00000O000000OO .get ('code')!=1000 :#line:148
        print (OOO00000O000000OO .get ('msg'),OOO00000O000000OO )#line:149
    return OOO00000O000000OO #line:150
def getmpinfo (O00O00000OOOO00O0 ):#line:153
    if not O00O00000OOOO00O0 or O00O00000OOOO00O0 =='':#line:154
        return False #line:155
    OOO0O0O0OOOO0OO00 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:157
    OOOOO00O00OOO000O =requests .get (O00O00000OOOO00O0 ,headers =OOO0O0O0OOOO0OO00 )#line:158
    OO0O0OO0O0OOO00OO =etree .HTML (OOOOO00O00OOO000O .text )#line:159
    OOO0000000O0000O0 =OO0O0OO0O0OOO00OO .xpath ('//meta[@*="og:title"]/@content')#line:161
    if OOO0000000O0000O0 :#line:162
        OOO0000000O0000O0 =OOO0000000O0000O0 [0 ]#line:163
    OO000O0OO0000O0O0 =OO0O0OO0O0OOO00OO .xpath ('//meta[@*="og:url"]/@content')#line:164
    if OO000O0OO0000O0O0 :#line:165
        OO000O0OO0000O0O0 =OO000O0OO0000O0O0 [0 ].encode ().decode ()#line:166
    try :#line:167
        OOOO00OOO0OO0O000 =re .findall (r'biz=(.*?)&',O00O00000OOOO00O0 )[0 ]#line:168
    except :#line:169
        OOOO00OOO0OO0O000 =re .findall (r'biz=(.*?)&',OO000O0OO0000O0O0 )[0 ]#line:170
    if not OOOO00OOO0OO0O000 :#line:171
        return False #line:172
    O00OOO0O0OO0OO0OO =OO0O0OO0O0OOO00OO .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:173
    if O00OOO0O0OO0OO0OO :#line:174
        O00OOO0O0OO0OO0OO =O00OOO0O0OO0OO0OO [0 ].strip ()#line:175
    O000O0O00000O0OO0 =re .findall (r"user_name.DATA'\) : '(.*?)'",OOOOO00O00OOO000O .text )or OO0O0OO0O0OOO00OO .xpath ('//span[@class="profile_meta_value"]/text()')#line:177
    if O000O0O00000O0OO0 :#line:178
        O000O0O00000O0OO0 =O000O0O00000O0OO0 [0 ]#line:179
    O0O00OOOOOOOOOOO0 =re .findall (r'createTime = \'(.*)\'',OOOOO00O00OOO000O .text )#line:180
    if O0O00OOOOOOOOOOO0 :#line:181
        O0O00OOOOOOOOOOO0 =O0O00OOOOOOOOOOO0 [0 ][5 :]#line:182
    O0OOOOOOOOO0O0OOO =f'{O0O00OOOOOOOOOOO0}||{OOO0000000O0000O0[:10]}||{OOOO00OOO0OO0O000}||{O00OOO0O0OO0OO0OO}'#line:183
    O000OOO0OOOO0O000 ={'biz':OOOO00OOO0OO0O000 ,'text':O0OOOOOOOOO0O0OOO }#line:184
    return O000OOO0OOOO0O000 #line:185
checkdict ={'Mzg2Mzk3Mjk5NQ==':'小鱼儿','MjM5NjU4NTE0MA==':'财事汇','MzkwMjI2ODY5Ng==':'A每日新菜','Mzg3NzEwMzI1Nw==':'A爱玩品牌传奇','MzIyMDg0MzA1OQ==':'服装加工宝','Mzg4NTQ5NDkxMQ==':'秣宝网','Mzk0NjIwNzk0Mg==':'检索宝','MzU3NjA5MDYyMw==':'重庆翊宝智慧电子装置有限公司','MzU1Nzc2ODI0MA==':'星空财研','MzUxMDgxMjMxMw==':'美术宝1对1','MzU4NDMyMTE1MQ==':'海雀Alcidae','MzI4MDE0MzM2NQ==':'强宝时尚','MzA3Nzc5MDMyNg==':'考研红宝书','MjM5Njk5NjYyMQ==':'宝和祥茶业','MzA4NDAyNTQ2MA==':'嘉财万贯','MzIzMjk2MjM5MQ==':'花生酥陪你学','MzkyMDE0NTI2OA==':'重庆市租房宝','MzI0NDI0NzU4OQ==':'九舞文学',}#line:194
class RRBYD :#line:197
    def __init__ (O0OOO0O00OO00O0OO ,OOO0OOOOOO0OOOOO0 ):#line:198
        O0OOO0O00OO00O0OO .un =OOO0OOOOOO0OOOOO0 ['un']#line:199
        O0OOO0O00OO00O0OO .uid =OOO0OOOOOO0OOOOO0 ['uid']#line:200
        O0OOO0O00OO00O0OO .wuid =OOO0OOOOOO0OOOOO0 .get ('wuid')#line:201
        O0OOO0O00OO00O0OO .headers ={'Host':'ebb.vinse.cn','un':O0OOO0O00OO00O0OO .un ,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue','uid':O0OOO0O00OO00O0OO .uid ,'platform':'0','token':OOO0OOOOOO0OOOOO0 ['token'],'Origin':'http://ebb101.twopinkone.cloud','Referer':'http://ebb101.twopinkone.cloud/',}#line:209
        O0OOO0O00OO00O0OO .msg =''#line:210
        O0OOO0O00OO00O0OO .daycount =None #line:211
    def userinfo (OO0OOOO0000OOOOO0 ):#line:213
        OOO0O00O000000OOO ='http://ebb.vinse.cn/api/user/info'#line:214
        O00OO0O0OOOO00OOO =requests .post (OOO0O00O000000OOO ,headers =OO0OOOO0000OOOOO0 .headers ,json ={"pageSize":10 }).json ()#line:215
        debugger (f'userinfo {O00OO0O0OOOO00OOO}')#line:216
        if O00OO0O0OOOO00OOO .get ('code')!=0 :#line:217
            OO0OOOO0000OOOOO0 .msg +=f'{OO0OOOO0000OOOOO0.un} cookie失效'+'\n'#line:218
            printlog (f'{OO0OOOO0000OOOOO0.un} cookie失效')#line:219
            return 0 #line:220
        O0OOOO000OO00OOO0 =O00OO0O0OOOO00OOO .get ('result')#line:221
        OO0OOOO0000OOOOO0 .nickname =O0OOOO000OO00OOO0 .get ('nickName')[0 :3 ]+'*'+O0OOOO000OO00OOO0 .get ('nickName')[-4 :]#line:222
        O00O000OOO00O00OO =O0OOOO000OO00OOO0 .get ('integralCurrent')#line:223
        O00OO00O0OO00OO0O =O0OOOO000OO00OOO0 .get ('integralTotal')#line:224
        OO0OOOO0000OOOOO0 .msg +=f'【{OO0OOOO0000OOOOO0.nickname}】:当前共有帮豆{O00O000OOO00O00OO}，总共获得帮豆{O00OO00O0OO00OO0O}\n'#line:225
        printlog (f'【{OO0OOOO0000OOOOO0.nickname}】:当前共有帮豆{O00O000OOO00O00OO}，总共获得帮豆{O00OO00O0OO00OO0O}')#line:226
        return O00O000OOO00O00OO #line:227
    def sign (O000OO00000OOOOOO ):#line:229
        OOO00O0O0OOOO00OO ='http://ebb.vinse.cn/api/user/sign'#line:230
        OO00OOO000OO0000O =requests .post (OOO00O0O0OOOO00OO ,headers =O000OO00000OOOOOO .headers ,json ={"pageSize":10 }).json ()#line:231
        debugger (f'sign {OO00OOO000OO0000O}')#line:232
        if OO00OOO000OO0000O .get ('code')==0 :#line:233
            O000OO00000OOOOOO .msg +=f'签到成功，获得帮豆{OO00OOO000OO0000O.get("result").get("point")}'+'\n'#line:234
            printlog (f'【{O000OO00000OOOOOO.nickname}】:签到成功，获得帮豆{OO00OOO000OO0000O.get("result").get("point")}')#line:235
        elif OO00OOO000OO0000O .get ('code')==99 :#line:236
            O000OO00000OOOOOO .msg +=OO00OOO000OO0000O .get ('msg')+'\n'#line:237
        else :#line:238
            O000OO00000OOOOOO .msg +='签到错误'+'\n'#line:239
    def reward (OO00OO000O0OOOO0O ):#line:241
        OO0OO0OO00O000O0O ='http://ebb.vinse.cn/api/user/receiveOneDivideReward'#line:242
        O0O0O0O0O00OOO0O0 =requests .post (OO0OO0OO00O000O0O ,headers =OO00OO000O0OOOO0O .headers ,json ={"pageSize":10 }).json ()#line:243
        if O0O0O0O0O00OOO0O0 .get ('code')==0 :#line:244
            OO00OO000O0OOOO0O .msg +=f"领取一级帮豆：{O0O0O0O0O00OOO0O0.get('msg')}\n"#line:245
            printlog (f"【{OO00OO000O0OOOO0O.nickname}】:领取一级帮豆：{O0O0O0O0O00OOO0O0.get('msg')}")#line:246
        OO0OO0OO00O000O0O ='http://ebb.vinse.cn/api/user/receiveTwoDivideReward'#line:247
        O0O0O0O0O00OOO0O0 =requests .post (OO0OO0OO00O000O0O ,headers =OO00OO000O0OOOO0O .headers ,json ={"pageSize":10 }).json ()#line:248
        if O0O0O0O0O00OOO0O0 .get ('code')==0 :#line:249
            OO00OO000O0OOOO0O .msg +=f"领取二级帮豆：{O0O0O0O0O00OOO0O0.get('msg')}"+'\n'#line:250
            printlog (f"【{OO00OO000O0OOOO0O.nickname}】:领取二级帮豆：{O0O0O0O0O00OOO0O0.get('msg')}")#line:251
    def getentry (O0O0OOO00O0O0OOOO ):#line:253
        OOOO00000O00OO0OO ={'Host':'u.cocozx.cn',"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Origin":"http://ebb101.twopinkone.cloud","Sec-Fetch-Site":"cross-site","Sec - Fetch - Mode":"cors","Sec - Fetch - Dest":"empty"}#line:260
        OO00O00OOO0O00000 =f'https://u.cocozx.cn/ipa/read/getEntryUrl?fr=ebb0726&uid={O0O0OOO00O0O0OOOO.uid}'#line:261
        OO000O00O0OO00O00 =requests .get (OO00O00OOO0O00000 ,headers =OOOO00000O00OO0OO ).json ()#line:262
        debugger (f'getentry {OO000O00O0OO00O00}')#line:263
        O0O00OOO000O0OO00 =OO000O00O0OO00O00 .get ('result')#line:264
        if OO000O00O0OO00O00 .get ('code')==0 :#line:265
            OOO00OO0OO0O0OOOO =O0O00OOO000O0OO00 .get ('url')#line:266
            O0O0OOO00O0O0OOOO .entryurl =re .findall (r'(http://.*?)/',OOO00OO0OO0O0OOOO )[0 ]#line:267
        else :#line:268
            O0O0OOO00O0O0OOOO .msg +="阅读链接获取失败"+'\n'#line:269
            printlog (f"【{O0O0OOO00O0O0OOOO.nickname}】:阅读链接获取失败")#line:270
    def read (O000OO00O00O0OOO0 ):#line:272
        OO0OO0OOOOO00O00O ={"Origin":O000OO00O00O0OOO0 .entryurl ,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Host":"u.cocozx.cn"}#line:277
        O00O00O0OOO0O0O00 ={"fr":"ebb0726","uid":O000OO00O00O0OOO0 .uid ,"un":'',"token":'',"pageSize":20 }#line:278
        O0OO0OO00O000OO0O ='http://u.cocozx.cn/ipa/read/info'#line:279
        OOO0O00O0O0OOO00O =requests .post (O0OO0OO00O000OO0O ,headers =OO0OO0OOOOO00O00O ,json =O00O00O0OOO0O0O00 ).json ()#line:280
        O0OO000000OOO00OO =OOO0O00O0O0OOO00O .get ('result').get ("dayCount")#line:281
        O0OO0OO00O000OO0O ='http://u.cocozx.cn/ipa/read/read'#line:282
        while True :#line:283
            OOO0O00O0O0OOO00O =requests .post (O0OO0OO00O000OO0O ,headers =OO0OO0OOOOO00O00O ,json =O00O00O0OOO0O0O00 )#line:284
            debugger ("read "+OOO0O00O0O0OOO00O .text )#line:285
            O0O0O0OO00O00O000 =OOO0O00O0O0OOO00O .json ().get ('result')#line:286
            O0OOO000OOO00O0OO =O0O0O0OO00O00O000 .get ('url')#line:287
            if O0O0O0OO00O00O000 ['status']==10 :#line:288
                OOO00OO00O0OOO00O =getmpinfo (O0OOO000OOO00O0OO )#line:289
                if not OOO00OO00O0OOO00O :#line:290
                    printlog (f'【{O000OO00O00O0OOO0.nickname}】:获取文章信息失败，程序中止')#line:291
                    return False #line:292
                O000OO00O00O0OOO0 .msg +='-'*50 +'\n开始阅读 '+OOO00OO00O0OOO00O .get ('text')+'\n'#line:293
                printlog (f"【{O000OO00O00O0OOO0.nickname}】:\n开始阅读  {OOO00OO00O0OOO00O.get('text')}")#line:294
                O000OO00O000OO00O =OOO00OO00O0OOO00O .get ('biz')#line:295
                if O000OO00O000OO00O in checkdict .keys ()or O0OO000000OOO00OO in [0 ,5 ]or O000OO00O00O0OOO0 .daycount in [0 ,5 ]:#line:296
                    O000OO00O00O0OOO0 .msg +='正在阅读检测文章\n发送通知，暂停60秒\n'#line:297
                    printlog (f"【{O000OO00O00O0OOO0.nickname}】:正在阅读检测文章\n发送通知，暂停60秒")#line:298
                    if sendable :#line:299
                        send (OOO00OO00O0OOO00O ['text'],f'【{O000OO00O00O0OOO0.nickname}】  人人帮阅读正在读检测文章',O0OOO000OOO00O0OO )#line:300
                    if pushable :#line:301
                        push (f'{O000OO00O00O0OOO0.nickname} \n点击阅读检测文章\n{OOO00OO00O0OOO00O["text"]}',f'{O000OO00O00O0OOO0.nickname}  人人帮阅读过检测文章',O0OOO000OOO00O0OO ,O000OO00O00O0OOO0 .wuid )#line:303
                    time .sleep (60 )#line:304
                OO00000O0OOOOOO00 =randint (7 ,10 )#line:305
                time .sleep (OO00000O0OOOOOO00 )#line:306
                O000OO00O00O0OOO0 .submit ()#line:307
            elif O0O0O0OO00O00O000 ['status']==60 :#line:308
                O000OO00O00O0OOO0 .msg +='文章已经全部读完了\n'#line:309
                printlog (f"【{O000OO00O00O0OOO0.nickname}】:文章已经全部读完了")#line:310
                break #line:311
            elif O0O0O0OO00O00O000 ['status']==30 :#line:312
                time .sleep (2 )#line:313
                continue #line:314
            elif O0O0O0OO00O00O000 ['status']==50 :#line:315
                O000OO00O00O0OOO0 .msg +='阅读失效\n'#line:316
                printlog (f"【{O000OO00O00O0OOO0.nickname}】:阅读失效")#line:317
                break #line:318
            else :#line:319
                break #line:320
        time .sleep (2 )#line:321
    def submit (OO000O0OO0000O0OO ):#line:323
        OOOOOOOO0OOO000O0 ='http://u.cocozx.cn/ipa/read/submit'#line:324
        O00O0O0O000O0000O ={"Origin":OO000O0OO0000O0OO .entryurl ,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Host":"u.cocozx.cn"}#line:329
        OO0OOOO0OOO0OOO0O ={"fr":"ebb0726","uid":OO000O0OO0000O0OO .uid ,"un":'',"token":'',"pageSize":20 }#line:330
        OO0OO0O00OO000OO0 =requests .post (OOOOOOOO0OOO000O0 ,headers =O00O0O0O000O0000O ,json =OO0OOOO0OOO0OOO0O ).json ()#line:331
        debugger (f"submit {OO0OO0O00OO000OO0}")#line:332
        O0000OO0OOO00000O =OO0OO0O00OO000OO0 .get ('result')#line:333
        OO000O0OO0000O0OO .daycount =O0000OO0OOO00000O .get ("dayCount")#line:334
        OO0O0OO0O00O0OO0O =O0000OO0OOO00000O .get ("dayMax")#line:335
        O0O00OOO000OOOO0O =O0000OO0OOO00000O .get ("progress")#line:336
        OO000O0OO0000O0OO .msg +=f"今日已阅读{OO000O0OO0000O0OO.daycount}，本轮剩余{O0O00OOO000OOOO0O}，单日最高{OO0O0OO0O00O0OO0O}\n"#line:337
        printlog (f"【{OO000O0OO0000O0OO.nickname}】:今日已阅读{OO000O0OO0000O0OO.daycount}，本轮剩余{O0O00OOO000OOOO0O}，单日最高{OO0O0OO0O00O0OO0O}")#line:338
    def tx (OO00O0000OOOO0O0O ):#line:340
        global txje #line:341
        OOO0O0OO0OOO000O0 =OO00O0000OOOO0O0O .userinfo ()#line:342
        if OOO0O0OO0OOO000O0 <txbz :#line:343
            OO00O0000OOOO0O0O .msg +='帮豆不够提现标准，明儿请早\n'#line:344
            printlog (f"【{OO00O0000OOOO0O0O.nickname}】:帮豆不够提现标准，明儿请早")#line:345
            return #line:346
        elif 5000 <=OOO0O0OO0OOO000O0 <10000 :#line:347
            txje =5000 #line:348
        elif 10000 <=OOO0O0OO0OOO000O0 <50000 :#line:349
            txje =10000 #line:350
        elif 50000 <=OOO0O0OO0OOO000O0 <100000 :#line:351
            txje =50000 #line:352
        elif OOO0O0OO0OOO000O0 >=100000 :#line:353
            txje =100000 #line:354
        O0O000O000O0OOO00 =f"http://ebb.vinse.cn/apiuser/aliWd"#line:355
        OOOO000O00000000O ={"val":txje ,"pageSize":10 }#line:356
        O00O00O0O0OO0O00O =requests .post (O0O000O000O0OOO00 ,headers =OO00O0000OOOO0O0O .headers ,json =OOOO000O00000000O ).json ()#line:357
        printlog (f'【{OO00O0000OOOO0O0O.nickname}】:提现结果 {O00O00O0O0OO0O00O.get("msg")}')#line:358
        if O00O00O0O0OO0O00O .get ('code')==0 :#line:359
            if sendable :#line:360
                send (f'【{OO00O0000OOOO0O0O.nickname}】 人人帮提现支付宝{txje / 10000}元',title ='人人帮阅读提现到账')#line:361
            if pushable :#line:362
                push (f'【{OO00O0000OOOO0O0O.nickname}】 人人帮提现支付宝{txje / 10000}元',title ='人人帮阅读提现到账',uid =OO00O0000OOOO0O0O .wuid )#line:363
    def run (OOO0O0O000O00O0OO ):#line:365
        OOO0O0O000O00O0OO .msg +='='*50 +'\n'#line:366
        if OOO0O0O000O00O0OO .userinfo ():#line:367
            OOO0O0O000O00O0OO .sign ()#line:368
            OOO0O0O000O00O0OO .getentry ()#line:369
            time .sleep (1 )#line:370
            OOO0O0O000O00O0OO .read ()#line:371
            OOO0O0O000O00O0OO .reward ()#line:372
            OOO0O0O000O00O0OO .tx ()#line:373
        if not printf :#line:374
            print (OOO0O0O000O00O0OO .msg .strip ())#line:375
def yd (O00OOOOO00OO0O0O0 ):#line:378
    while not O00OOOOO00OO0O0O0 .empty ():#line:379
        OO00O000OO00OO00O =O00OOOOO00OO0O0O0 .get ()#line:380
        OOO00000OO000O00O =RRBYD (OO00O000OO00OO00O )#line:381
        OOO00000OO000O00O .run ()#line:382
def get_info ():#line:385
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:387
    print ('入口：http://ebb.maisucaiya.cloud/user/index.html?mid=1702983440137322496')#line:388
    OOO000000OO0O000O ='v1.4'#line:389
    O0000OOOO0OO0OO0O =_O0O0OOOOOO0OO0O00 ['version']['k_rrb']#line:390
    print (f'当前版本{OOO000000OO0O000O}，仓库版本{O0000OOOO0OO0OO0O}\n{_O0O0OOOOOO0OO0O00["update_log"]["人人帮"]}')#line:391
    if OOO000000OO0O000O <O0000OOOO0OO0OO0O :#line:392
        print ('请到仓库下载最新版本k_rrb.py')#line:393
    print ("="*25 )#line:394
def main ():#line:397
    get_info ()#line:398
    O0OOOOOOO00OO0OOO =os .getenv ('rrbck')#line:399
    if not O0OOOOOOO00OO0OOO :#line:400
        print (_O0O0OOOOOO0OO0O00 .get ('msg')['人人帮'])#line:401
        exit ()#line:402
    try :#line:403
        O0OOOOOOO00OO0OOO =ast .literal_eval (O0OOOOOOO00OO0OOO )#line:404
    except :#line:405
        pass #line:406
    OO00OO0OO000OO0O0 =Queue ()#line:407
    O0000O00OOOOO00OO =[]#line:408
    printlog (f'共获取到{len(O0OOOOOOO00OO0OOO)}个账号，如不正确，请检查ck填写格式')#line:409
    for O0OO0OO0O000OO0O0 ,OO00000O000O00OOO in enumerate (O0OOOOOOO00OO0OOO ,start =1 ):#line:410
        OO00OO0OO000OO0O0 .put (OO00000O000O00OOO )#line:411
    for O0OO0OO0O000OO0O0 in range (max_workers ):#line:412
        O0000O0000O0O00OO =threading .Thread (target =yd ,args =(OO00OO0OO000OO0O0 ,))#line:413
        O0000O0000O0O00OO .start ()#line:414
        O0000O00OOOOO00OO .append (O0000O0000O0O00OO )#line:415
        time .sleep (delay_time )#line:416
    for OOO0O000OOO0OOO00 in O0000O00OOOOO00OO :#line:417
        OOO0O000OOO0OOO00 .join ()#line:418
if __name__ =='__main__':#line:421
    main ()#line:422
