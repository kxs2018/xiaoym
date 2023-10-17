# -*- coding: utf-8 -*-
# k_rrb
# Author: 惜之酱

"""
new Env('人人帮');
先运行脚本，有问题再问
入口：http://ebb.maisucaiya.cloud/user/index.html?mid=1702983440137322496
如微信打不开，可复制到浏览器打开
"""
try:
    from config import rrb_config
except:
    rrb_config = {
        'printf': 1,  # 实时日志开关 1为开，0为关

        'debug': 0,  # debug模式开关 1为开，打印调试日志；0为关，不打印

        'max_workers': 5,  # 线程数量设置 设置为5，即最多有5个任务同时进行

        'txbz': 10000,  # 设置提现标准 不低于3000，平台标准为3000 设置为8000，即为8毛起提

        'sendable': 1,  # 企业微信推送开关 1开0关

        'pushable': 1,  # wxpusher推送开关 1开0关

        'delay_time': 20  # 并发延迟设置 设置为20即每隔20秒新增一个号做任务，直到数量达到max_workers
    }
printf = rrb_config['printf']
debug = rrb_config['debug']
sendable = rrb_config['sendable']
pushable = rrb_config['pushable']
max_workers = rrb_config['max_workers']
txbz = rrb_config['txbz']
delay_time = rrb_config['delay_time']
import json #line:35
from random import randint #line:36
import os #line:37
import time #line:38
import requests #line:39
import ast #line:40
import re #line:41
import datetime #line:42
import threading #line:43
from queue import Queue #line:44
def get_msg ():#line:47
    OOO0O0OOO0000OO00 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:49
    OOOOO0OO0OOO0O0O0 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OOO0O0OOO0000OO00 ).json ()#line:50
    return OOOOO0OO0OOO0O0O0 #line:51
_OOOOOOO0OO00O0OOO =get_msg ()#line:54
try :#line:55
    from lxml import etree #line:56
except :#line:57
    print (_OOOOOOO0OO00O0OOO .get ('help')['lxml'])#line:58
if sendable :#line:60
    qwbotkey =os .getenv ('qwbotkey')#line:61
    if not qwbotkey :#line:62
        print (_OOOOOOO0OO00O0OOO .get ('help')['qwbotkey'])#line:63
        exit ()#line:64
if pushable :#line:66
    pushconfig =os .getenv ('pushconfig')#line:67
    if not pushconfig :#line:68
        print (_OOOOOOO0OO00O0OOO .get ('help')['pushconfig'])#line:69
        exit ()#line:70
    try :#line:71
        pushconfig =ast .literal_eval (pushconfig )#line:72
    except :#line:73
        pass #line:74
    if isinstance (pushconfig ,dict ):#line:75
        appToken =pushconfig ['appToken']#line:76
        uids =pushconfig ['uids']#line:77
        topicids =pushconfig ['topicids']#line:78
    else :#line:79
        try :#line:80
            "appToken=AT_pCenRjs;uids=['UID_9MZ','UID_T4xlqWx9x'];topicids=['xxx']"#line:81
            appToken =pushconfig .split (';')[0 ].split ('=')[1 ]#line:82
            uids =ast .literal_eval (pushconfig .split (';')[1 ].split ('=')[1 ])#line:83
            topicids =ast .literal_eval (pushconfig .split (';')[2 ].split ('=')[1 ])#line:84
        except :#line:85
            print (_OOOOOOO0OO00O0OOO .get ('help')['pushconfig'])#line:86
            exit ()#line:87
if not pushable and not sendable :#line:89
    print ('啥通知方式都不配置，你想上天吗')#line:90
    exit ()#line:91
def ftime ():#line:94
    OOO0OO0OOO000OOOO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:95
    return OOO0OO0OOO000OOOO #line:96
def debugger (O000000O0OOO0OOOO ):#line:99
    if debug :#line:100
        print (O000000O0OOO0OOOO )#line:101
def printlog (OOO00O0OOOOO0O0OO ):#line:104
    if printf :#line:105
        print (OOO00O0OOOOO0O0OO )#line:106
def send (OOO0OOOO0O0O0O00O ,title ='通知',url =None ):#line:109
    if not title or not url :#line:110
        OOOOOO0O000000000 ={"msgtype":"text","text":{"content":f"{title}\n\n{OOO0OOOO0O0O0O00O}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:117
    else :#line:118
        OOOOOO0O000000000 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":OOO0OOOO0O0O0O00O ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:123
    OOO0OOO0OO0OO0OOO =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:124
    O00000OO000O0O0O0 =requests .post (OOO0OOO0OO0OO0OOO ,data =json .dumps (OOOOOO0O000000000 )).json ()#line:125
    if O00000OO000O0O0O0 .get ('errcode')!=0 :#line:126
        print ('消息发送失败，请检查key和发送格式')#line:127
        return False #line:128
    return O00000OO000O0O0O0 #line:129
def push (O000O000OOO0O0000 ,title ='通知',url ='',uid =None ):#line:132
    if uid :#line:133
        uids .append (uid )#line:134
    O00O00O00OO0O0OOO ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',O000O000OOO0O0000 ).replace ('url',url )#line:136
    OOOOOOO0OO0000O00 ={"appToken":appToken ,"content":O00O00O00OO0O0OOO ,"summary":title ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:146
    OO0O000OO0000000O ='http://wxpusher.zjiecode.com/api/send/message'#line:147
    OOO0O00OO0000O000 =requests .post (url =OO0O000OO0000000O ,json =OOOOOOO0OO0000O00 ).json ()#line:148
    if OOO0O00OO0000O000 .get ('code')!=1000 :#line:149
        print (OOO0O00OO0000O000 .get ('msg'),OOO0O00OO0000O000 )#line:150
    return OOO0O00OO0000O000 #line:151
def getmpinfo (O00OOO0OO00OO00OO ):#line:154
    if not O00OOO0OO00OO00OO or O00OOO0OO00OO00OO =='':#line:155
        return False #line:156
    OO00OO000000O0000 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:158
    O0O000O0OO0000OO0 =requests .get (O00OOO0OO00OO00OO ,headers =OO00OO000000O0000 )#line:159
    O0OOOOOOOOO00O0OO =etree .HTML (O0O000O0OO0000OO0 .text )#line:160
    O000OO00O0OO000O0 =O0OOOOOOOOO00O0OO .xpath ('//meta[@*="og:title"]/@content')#line:162
    if O000OO00O0OO000O0 :#line:163
        O000OO00O0OO000O0 =O000OO00O0OO000O0 [0 ]#line:164
    OO000OOOOOO0OOO0O =O0OOOOOOOOO00O0OO .xpath ('//meta[@*="og:url"]/@content')#line:165
    if OO000OOOOOO0OOO0O :#line:166
        OO000OOOOOO0OOO0O =OO000OOOOOO0OOO0O [0 ].encode ().decode ()#line:167
    try :#line:168
        OOOO0O0000OO0OO00 =re .findall (r'biz=(.*?)&',O00OOO0OO00OO00OO )[0 ]#line:169
    except :#line:170
        OOOO0O0000OO0OO00 =re .findall (r'biz=(.*?)&',OO000OOOOOO0OOO0O )[0 ]#line:171
    if not OOOO0O0000OO0OO00 :#line:172
        return False #line:173
    OO00O00OO0OOOO0OO =O0OOOOOOOOO00O0OO .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:174
    if OO00O00OO0OOOO0OO :#line:175
        OO00O00OO0OOOO0OO =OO00O00OO0OOOO0OO [0 ].strip ()#line:176
    OO00O0OOO00OOOO00 =re .findall (r"user_name.DATA'\) : '(.*?)'",O0O000O0OO0000OO0 .text )or O0OOOOOOOOO00O0OO .xpath ('//span[@class="profile_meta_value"]/text()')#line:178
    if OO00O0OOO00OOOO00 :#line:179
        OO00O0OOO00OOOO00 =OO00O0OOO00OOOO00 [0 ]#line:180
    OOO00OO000OOO00OO =re .findall (r'createTime = \'(.*)\'',O0O000O0OO0000OO0 .text )#line:181
    if OOO00OO000OOO00OO :#line:182
        OOO00OO000OOO00OO =OOO00OO000OOO00OO [0 ][5 :]#line:183
    OO0O0O0OO0O0000OO =f'{OOO00OO000OOO00OO}|{O000OO00O0OO000O0[:10]}|{OOOO0O0000OO0OO00}|{OO00O00OO0OOOO0OO}'#line:184
    O0OOO0OOO0O0O0OOO ={'biz':OOOO0O0000OO0OO00 ,'username':OO00O00OO0OOOO0OO ,'text':OO0O0O0OO0O0000OO }#line:185
    return O0OOO0OOO0O0O0OOO #line:186
try :#line:189
    with open ('checkdict.json','r',encoding ='utf-8')as f :#line:190
        checkdict_local =json .loads (f .read ())#line:191
except :#line:192
    pass #line:193
checkdict ={'Mzg2Mzk3Mjk5NQ==':'小鱼儿','MjM5NjU4NTE0MA==':'财事汇','MzkwMjI2ODY5Ng==':'A每日新菜','Mzg3NzEwMzI1Nw==':'A爱玩品牌传奇','MzIyMDg0MzA1OQ==':'服装加工宝','Mzg4NTQ5NDkxMQ==':'秣宝网','Mzk0NjIwNzk0Mg==':'检索宝','MzU3NjA5MDYyMw==':'重庆翊宝智慧电子装置有限公司','MzU1Nzc2ODI0MA==':'星空财研','MzUxMDgxMjMxMw==':'美术宝1对1','MzU4NDMyMTE1MQ==':'海雀Alcidae','MzI4MDE0MzM2NQ==':'强宝时尚','MzA3Nzc5MDMyNg==':'考研红宝书','MjM5Njk5NjYyMQ==':'宝和祥茶业','MzA4NDAyNTQ2MA==':'嘉财万贯','MzIzMjk2MjM5MQ==':'花生酥陪你学','MzkyMDE0NTI2OA==':'重庆市租房宝','MzI0NDI0NzU4OQ==':'九舞文学','MjM5NDAzMjgzNg==':'东风卡车之友','MzI1NjUxMTc0Mw==':'爱普生商教投影机','MzIyNzU3NDIwMA==':'川名堂','MzAwMDUwOTczNg==':'0','MzI4NjYyNTEzMw==':'0','MzI5MDQxNjExNg==':'0','Mzg3MzA0MTkyMw==':'0','MzU0MTUzMTUxOQ==':'0','MzIzNDU2ODUxMA==':''}#line:202
try :#line:203
    checkdict ={**checkdict ,**checkdict_local }#line:204
except :#line:205
    pass #line:206
class RRBYD :#line:209
    def __init__ (OOO0O0OO00000OO0O ,O000O0O00O00O0000 ):#line:210
        OOO0O0OO00000OO0O .un =O000O0O00O00O0000 ['un']#line:211
        OOO0O0OO00000OO0O .uid =O000O0O00O00O0000 ['uid']#line:212
        OOO0O0OO00000OO0O .username =None #line:213
        OOO0O0OO00000OO0O .biz =None #line:214
        OOO0O0OO00000OO0O .wuid =O000O0O00O00O0000 .get ('wuid')#line:215
        OOO0O0OO00000OO0O .headers ={'Host':'ebb.vinse.cn','un':OOO0O0OO00000OO0O .un ,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue','uid':OOO0O0OO00000OO0O .uid ,'platform':'0','token':O000O0O00O00O0000 ['token'],'Origin':'http://ebb101.twopinkone.cloud','Referer':'http://ebb101.twopinkone.cloud/',}#line:223
        OOO0O0OO00000OO0O .msg =''#line:224
        OOO0O0OO00000OO0O .daycount =None #line:225
    def userinfo (O0O0OOO0O000OO000 ):#line:227
        O0O00OOO0O0OO00OO ='http://ebb.vinse.cn/api/user/info'#line:228
        OOOO00O0O00OOOOOO =requests .post (O0O00OOO0O0OO00OO ,headers =O0O0OOO0O000OO000 .headers ,json ={"pageSize":10 }).json ()#line:229
        debugger (f'userinfo {OOOO00O0O00OOOOOO}')#line:230
        if OOOO00O0O00OOOOOO .get ('code')!=0 :#line:231
            O0O0OOO0O000OO000 .msg +=f'{O0O0OOO0O000OO000.un} cookie失效'+'\n'#line:232
            printlog (f'{O0O0OOO0O000OO000.un} cookie失效')#line:233
            return 0 #line:234
        OO0OO0O0O0000O00O =OOOO00O0O00OOOOOO .get ('result')#line:235
        O0O0OOO0O000OO000 .nickname =OO0OO0O0O0000O00O .get ('nickName')[0 :3 ]+'*'+OO0OO0O0O0000O00O .get ('nickName')[-4 :]#line:236
        O0O00O0OOOOOOOOO0 =OO0OO0O0O0000O00O .get ('integralCurrent')#line:237
        O0000OOO0O0OO0OO0 =OO0OO0O0O0000O00O .get ('integralTotal')#line:238
        O0O0OOO0O000OO000 .msg +=f'【{O0O0OOO0O000OO000.nickname}】:当前共有帮豆{O0O00O0OOOOOOOOO0}，总共获得帮豆{O0000OOO0O0OO0OO0}\n'#line:239
        printlog (f'【{O0O0OOO0O000OO000.nickname}】:当前共有帮豆{O0O00O0OOOOOOOOO0}，总共获得帮豆{O0000OOO0O0OO0OO0}')#line:240
        return O0O00O0OOOOOOOOO0 #line:241
    def sign (O0OO00O00OO000O00 ):#line:243
        O00O0OOO0OOOO000O ='http://ebb.vinse.cn/api/user/sign'#line:244
        OO0OOO00OOOOOO0O0 =requests .post (O00O0OOO0OOOO000O ,headers =O0OO00O00OO000O00 .headers ,json ={"pageSize":10 }).json ()#line:245
        debugger (f'sign {OO0OOO00OOOOOO0O0}')#line:246
        if OO0OOO00OOOOOO0O0 .get ('code')==0 :#line:247
            O0OO00O00OO000O00 .msg +=f'签到成功，获得帮豆{OO0OOO00OOOOOO0O0.get("result").get("point")}'+'\n'#line:248
            printlog (f'【{O0OO00O00OO000O00.nickname}】:签到成功，获得帮豆{OO0OOO00OOOOOO0O0.get("result").get("point")}')#line:249
        elif OO0OOO00OOOOOO0O0 .get ('code')==99 :#line:250
            O0OO00O00OO000O00 .msg +=OO0OOO00OOOOOO0O0 .get ('msg')+'\n'#line:251
        else :#line:252
            O0OO00O00OO000O00 .msg +='签到错误'+'\n'#line:253
    def reward (O0O00O00O000O0OOO ):#line:255
        OO0O00O00O00000OO ='http://ebb.vinse.cn/api/user/receiveOneDivideReward'#line:256
        OOO0000000O0OO00O =requests .post (OO0O00O00O00000OO ,headers =O0O00O00O000O0OOO .headers ,json ={"pageSize":10 }).json ()#line:257
        if OOO0000000O0OO00O .get ('code')==0 :#line:258
            O0O00O00O000O0OOO .msg +=f"领取一级帮豆：{OOO0000000O0OO00O.get('msg')}\n"#line:259
            printlog (f"【{O0O00O00O000O0OOO.nickname}】:领取一级帮豆：{OOO0000000O0OO00O.get('msg')}")#line:260
        OO0O00O00O00000OO ='http://ebb.vinse.cn/api/user/receiveTwoDivideReward'#line:261
        OOO0000000O0OO00O =requests .post (OO0O00O00O00000OO ,headers =O0O00O00O000O0OOO .headers ,json ={"pageSize":10 }).json ()#line:262
        if OOO0000000O0OO00O .get ('code')==0 :#line:263
            O0O00O00O000O0OOO .msg +=f"领取二级帮豆：{OOO0000000O0OO00O.get('msg')}"+'\n'#line:264
            printlog (f"【{O0O00O00O000O0OOO.nickname}】:领取二级帮豆：{OOO0000000O0OO00O.get('msg')}")#line:265
    def getentry (O00000OO00O0OO000 ):#line:267
        O000O00OOO0OOOOO0 ={'Host':'u.cocozx.cn',"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Origin":"http://ebb101.twopinkone.cloud","Sec-Fetch-Site":"cross-site","Sec - Fetch - Mode":"cors","Sec - Fetch - Dest":"empty"}#line:274
        OOO0O00O0000O000O =f'https://u.cocozx.cn/ipa/read/getEntryUrl?fr=ebb0726&uid={O00000OO00O0OO000.uid}'#line:275
        O00OO0000O0OO00O0 =requests .get (OOO0O00O0000O000O ,headers =O000O00OOO0OOOOO0 ).json ()#line:276
        debugger (f'getentry {O00OO0000O0OO00O0}')#line:277
        O00OO00OO00O0OOO0 =O00OO0000O0OO00O0 .get ('result')#line:278
        if O00OO0000O0OO00O0 .get ('code')==0 :#line:279
            OO00O0O0OOO00O000 =O00OO00OO00O0OOO0 .get ('url')#line:280
            O00000OO00O0OO000 .entryurl =re .findall (r'(http://.*?)/',OO00O0O0OOO00O000 )[0 ]#line:281
        else :#line:282
            O00000OO00O0OO000 .msg +="阅读链接获取失败"+'\n'#line:283
            printlog (f"【{O00000OO00O0OO000.nickname}】:阅读链接获取失败")#line:284
    def read (O0OO0O0OO000000OO ):#line:286
        O0O0OO00OOOOO0O00 ={"Origin":O0OO0O0OO000000OO .entryurl ,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Host":"u.cocozx.cn"}#line:291
        O0O0OOO0O0OO0OOOO ={"fr":"ebb0726","uid":O0OO0O0OO000000OO .uid ,"un":'',"token":'',"pageSize":20 }#line:292
        OO000O000OO00O0OO ='http://u.cocozx.cn/ipa/read/info'#line:293
        OO0OOO00OOO0OO00O =requests .post (OO000O000OO00O0OO ,headers =O0O0OO00OOOOO0O00 ,json =O0O0OOO0O0OO0OOOO ).json ()#line:294
        O0O00O000O0O000OO =OO0OOO00OOO0OO00O .get ('result').get ("dayCount")#line:295
        OO000O000OO00O0OO ='http://u.cocozx.cn/ipa/read/read'#line:296
        while True :#line:297
            OO0OOO00OOO0OO00O =requests .post (OO000O000OO00O0OO ,headers =O0O0OO00OOOOO0O00 ,json =O0O0OOO0O0OO0OOOO )#line:298
            debugger ("read "+OO0OOO00OOO0OO00O .text )#line:299
            O00O00OOOO00O0OOO =OO0OOO00OOO0OO00O .json ().get ('result')#line:300
            OOO0O0OOOO0OOOOO0 =O00O00OOOO00O0OOO .get ('url')#line:301
            if O00O00OOOO00O0OOO ['status']==10 :#line:302
                OOOOO0OO000OO0OOO =getmpinfo (OOO0O0OOOO0OOOOO0 )#line:303
                if not OOOOO0OO000OO0OOO :#line:304
                    printlog (f'【{O0OO0O0OO000000OO.nickname}】:获取文章信息失败，程序中止')#line:305
                    return False #line:306
                O0OO0O0OO000000OO .msg +='-'*50 +'\n开始阅读 '+OOOOO0OO000OO0OOO .get ('text')+'\n'#line:307
                printlog (f"【{O0OO0O0OO000000OO.nickname}】:\n开始阅读  {OOOOO0OO000OO0OOO.get('text')}")#line:308
                O0OO0O0OO000000OO .biz =OOOOO0OO000OO0OOO .get ('biz')#line:309
                O0OO0O0OO000000OO .username =OOOOO0OO000OO0OOO .get ('username')#line:310
                if O0OO0O0OO000000OO .biz in checkdict .keys ()or (O0O00O000O0O000OO in [0 ,5 ])or (O0OO0O0OO000000OO .daycount in [0 ,5 ]):#line:311
                    O0O00O000O0O000OO +=1 #line:312
                    O0OO0O0OO000000OO .msg +='正在阅读检测文章\n发送通知，暂停60秒\n'#line:313
                    printlog (f"【{O0OO0O0OO000000OO.nickname}】:正在阅读检测文章\n发送通知，暂停60秒")#line:314
                    if sendable :#line:315
                        send (OOOOO0OO000OO0OOO ['text'],f'【{O0OO0O0OO000000OO.nickname}】  人人帮阅读正在读检测文章',OOO0O0OOOO0OOOOO0 )#line:316
                    if pushable :#line:317
                        push (f'{O0OO0O0OO000000OO.nickname} \n点击阅读检测文章\n{OOOOO0OO000OO0OOO["text"]}',f'{O0OO0O0OO000000OO.nickname}  人人帮阅读过检测文章',OOO0O0OOOO0OOOOO0 ,O0OO0O0OO000000OO .wuid )#line:319
                    time .sleep (60 )#line:320
                OO0O0O00OOOOOOOO0 =randint (7 ,10 )#line:321
                time .sleep (OO0O0O00OOOOOOOO0 )#line:322
                O0OO0O0OO000000OO .submit ()#line:323
            elif O00O00OOOO00O0OOO ['status']==60 :#line:324
                O0OO0O0OO000000OO .msg +='文章已经全部读完了\n'#line:325
                printlog (f"【{O0OO0O0OO000000OO.nickname}】:文章已经全部读完了")#line:326
                break #line:327
            elif O00O00OOOO00O0OOO ['status']==30 :#line:328
                time .sleep (2 )#line:329
                continue #line:330
            elif O00O00OOOO00O0OOO ['status']==50 :#line:331
                O0OO0O0OO000000OO .msg +='阅读失效\n'#line:332
                printlog (f"【{O0OO0O0OO000000OO.nickname}】:阅读失效")#line:333
                if O0OO0O0OO000000OO .biz is not None :#line:334
                    checkdict .update ({O0OO0O0OO000000OO .biz :O0OO0O0OO000000OO .username })#line:335
                    print (checkdict .get (O0OO0O0OO000000OO .biz ))#line:336
                break #line:337
            else :#line:338
                break #line:339
        time .sleep (2 )#line:340
    def submit (O0000O000O0O0O0OO ):#line:342
        OO00000OO0O0O0000 ='http://u.cocozx.cn/ipa/read/submit'#line:343
        O00OOOOO00O00OO00 ={"Origin":O0000O000O0O0O0OO .entryurl ,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Host":"u.cocozx.cn"}#line:348
        O0OO0OO0O0O0000OO ={"fr":"ebb0726","uid":O0000O000O0O0O0OO .uid ,"un":'',"token":'',"pageSize":20 }#line:349
        O0000OOO0O0OOO000 =requests .post (OO00000OO0O0O0000 ,headers =O00OOOOO00O00OO00 ,json =O0OO0OO0O0O0000OO ).json ()#line:350
        debugger (f"submit {O0000OOO0O0OOO000}")#line:351
        OOOO00O0OO00OO00O =O0000OOO0O0OOO000 .get ('result')#line:352
        O0000O000O0O0O0OO .daycount =OOOO00O0OO00OO00O .get ("dayCount")#line:353
        OOOOOO0OOO00OO0OO =OOOO00O0OO00OO00O .get ("dayMax")#line:354
        O0O0O00O0O000000O =OOOO00O0OO00OO00O .get ("progress")#line:355
        O0000O000O0O0O0OO .msg +=f"今日已阅读{O0000O000O0O0O0OO.daycount}，本轮剩余{O0O0O00O0O000000O}，单日最高{OOOOOO0OOO00OO0OO}\n"#line:356
        printlog (f"【{O0000O000O0O0O0OO.nickname}】:今日已阅读{O0000O000O0O0O0OO.daycount}，本轮剩余{O0O0O00O0O000000O}，单日最高{OOOOOO0OOO00OO0OO}")#line:357
    def tx (OOO0OOOO0OOO00OOO ):#line:359
        global txje #line:360
        O0OO0000OO00O00O0 =OOO0OOOO0OOO00OOO .userinfo ()#line:361
        if O0OO0000OO00O00O0 <txbz :#line:362
            OOO0OOOO0OOO00OOO .msg +='帮豆不够提现标准，明儿请早\n'#line:363
            printlog (f"【{OOO0OOOO0OOO00OOO.nickname}】:帮豆不够提现标准，明儿请早")#line:364
            return #line:365
        elif 5000 <=O0OO0000OO00O00O0 <10000 :#line:366
            txje =5000 #line:367
        elif 10000 <=O0OO0000OO00O00O0 <50000 :#line:368
            txje =10000 #line:369
        elif 50000 <=O0OO0000OO00O00O0 <100000 :#line:370
            txje =50000 #line:371
        elif O0OO0000OO00O00O0 >=100000 :#line:372
            txje =100000 #line:373
        O0O0O0OO00000O0OO =f"http://ebb.vinse.cn/apiuser/aliWd"#line:374
        O00OO00000000OOOO ={"val":txje ,"pageSize":10 }#line:375
        O0OOO0OOO00OOO0OO =requests .post (O0O0O0OO00000O0OO ,headers =OOO0OOOO0OOO00OOO .headers ,json =O00OO00000000OOOO ).json ()#line:376
        printlog (f'【{OOO0OOOO0OOO00OOO.nickname}】:提现结果 {O0OOO0OOO00OOO0OO.get("msg")}')#line:377
        if O0OOO0OOO00OOO0OO .get ('code')==0 :#line:378
            if sendable :#line:379
                send (f'【{OOO0OOOO0OOO00OOO.nickname}】 人人帮提现支付宝{txje / 10000}元',title ='人人帮阅读提现到账')#line:380
            if pushable :#line:381
                push (f'【{OOO0OOOO0OOO00OOO.nickname}】 人人帮提现支付宝{txje / 10000}元',title ='人人帮阅读提现到账',uid =OOO0OOOO0OOO00OOO .wuid )#line:382
    def run (O0O0O0OO000000OOO ):#line:384
        O0O0O0OO000000OOO .msg +='='*50 +'\n'#line:385
        if O0O0O0OO000000OOO .userinfo ():#line:386
            O0O0O0OO000000OOO .sign ()#line:387
            O0O0O0OO000000OOO .getentry ()#line:388
            time .sleep (1 )#line:389
            O0O0O0OO000000OOO .read ()#line:390
            O0O0O0OO000000OOO .reward ()#line:391
            O0O0O0OO000000OOO .tx ()#line:392
        if not printf :#line:393
            print (O0O0O0OO000000OOO .msg .strip ())#line:394
def yd (O0000OOO00OO0000O ):#line:397
    while not O0000OOO00OO0000O .empty ():#line:398
        O00O0000O000O0O0O =O0000OOO00OO0000O .get ()#line:399
        O0000OOOOOOOOO000 =RRBYD (O00O0000O000O0O0O )#line:400
        O0000OOOOOOOOO000 .run ()#line:401
def get_info ():#line:404
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:406
    print ('入口：http://ebb.maisucaiya.cloud/user/index.html?mid=1702983440137322496')#line:407
    OOO0O000OOOOOOOOO ='v1.4.1'#line:408
    O00OO000000000O0O =_OOOOOOO0OO00O0OOO ['version']['人人帮']#line:409
    print (f'当前版本{OOO0O000OOOOOOOOO}，仓库版本{O00OO000000000O0O}\n{_OOOOOOO0OO00O0OOO["update_log"]["人人帮"]}')#line:410
    if OOO0O000OOOOOOOOO <O00OO000000000O0O :#line:411
        print ('请到仓库下载最新版本k_rrb.py')#line:412
    print ("="*25 )#line:413
    return True #line:414
def main ():#line:417
    OO000O00OOOOO0OOO =get_info ()#line:418
    O0O000O00O0OO00OO =os .getenv ('rrbck')#line:419
    if not O0O000O00O0OO00OO :#line:420
        print (_OOOOOOO0OO00O0OOO .get ('msg')['人人帮'])#line:421
        exit ()#line:422
    try :#line:423
        O0O000O00O0OO00OO =ast .literal_eval (O0O000O00O0OO00OO )#line:424
    except :#line:425
        pass #line:426
    OO0OO00O00OO0O000 =Queue ()#line:427
    O0O0OO000O0OOOO00 =[]#line:428
    printlog (f'共获取到{len(O0O000O00O0OO00OO)}个账号，如不正确，请检查ck填写格式')#line:429
    if not OO000O00OOOOO0OOO :#line:430
        exit ()#line:431
    for OO0O00O00OO0O0O0O ,O0O0O0O0O0OO0000O in enumerate (O0O000O00O0OO00OO ,start =1 ):#line:432
        OO0OO00O00OO0O000 .put (O0O0O0O0O0OO0000O )#line:433
    for OO0O00O00OO0O0O0O in range (max_workers ):#line:434
        O000OO000OO0O00OO =threading .Thread (target =yd ,args =(OO0OO00O00OO0O000 ,))#line:435
        O000OO000OO0O00OO .start ()#line:436
        O0O0OO000O0OOOO00 .append (O000OO000OO0O00OO )#line:437
        time .sleep (delay_time )#line:438
    for OO00O0O000OOOOO00 in O0O0OO000O0OOOO00 :#line:439
        OO00O0O000OOOOO00 .join ()#line:440
    print ('-'*25 +f'\n{checkdict}')#line:441
    with open ('checkdict.json','w',encoding ='utf-8')as OOO0OOO0000O0O0O0 :#line:442
        OOO0OOO0000O0O0O0 .write (json .dumps (checkdict ))#line:443
if __name__ =='__main__':#line:446
    main ()#line:447
