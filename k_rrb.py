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
    O0O0O0O000O00OO0O ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:49
    O0O0OOO0OO00000OO =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O0O0O0O000O00OO0O ).json ()#line:50
    return O0O0OOO0OO00000OO #line:51
_O0O00OO0O00O0000O =get_msg ()#line:54
try :#line:55
    from lxml import etree #line:56
except :#line:57
    print (_O0O00OO0O00O0000O .get ('help')['lxml'])#line:58
if sendable :#line:60
    qwbotkey =os .getenv ('qwbotkey')#line:61
    if not qwbotkey :#line:62
        print (_O0O00OO0O00O0000O .get ('help')['qwbotkey'])#line:63
        exit ()#line:64
if pushable :#line:66
    pushconfig =os .getenv ('pushconfig')#line:67
    if not pushconfig :#line:68
        print (_O0O00OO0O00O0000O .get ('help')['pushconfig'])#line:69
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
            print (_O0O00OO0O00O0000O .get ('help')['pushconfig'])#line:86
            exit ()#line:87
if not pushable and not sendable :#line:89
    print ('啥通知方式都不配置，你想上天吗')#line:90
    exit ()#line:91
def ftime ():#line:94
    OO00OO00OOOO0000O =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:95
    return OO00OO00OOOO0000O #line:96
def debugger (O0O0OOOOOO0OO000O ):#line:99
    if debug :#line:100
        print (O0O0OOOOOO0OO000O )#line:101
def printlog (O000O0000OO0O0OOO ):#line:104
    if printf :#line:105
        print (O000O0000OO0O0OOO )#line:106
def send (OOO00OOO0OO0O0O00 ,title ='通知',url =None ):#line:109
    if not title or not url :#line:110
        O0000OO00OO00O0O0 ={"msgtype":"text","text":{"content":f"{title}\n\n{OOO00OOO0OO0O0O00}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:117
    else :#line:118
        O0000OO00OO00O0O0 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":OOO00OOO0OO0O0O00 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:123
    O00O00OO000OO0OOO =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:124
    O00O00O00OOOO00O0 =requests .post (O00O00OO000OO0OOO ,data =json .dumps (O0000OO00OO00O0O0 )).json ()#line:125
    if O00O00O00OOOO00O0 .get ('errcode')!=0 :#line:126
        print ('消息发送失败，请检查key和发送格式')#line:127
        return False #line:128
    return O00O00O00OOOO00O0 #line:129
def push (O00000OOO0O0OO0OO ,title ='通知',url ='',uid =None ):#line:132
    if uid :#line:133
        uids .append (uid )#line:134
    OO0OO00O00OO00OOO ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',O00000OOO0O0OO0OO ).replace ('url',url )#line:136
    OOOO00OO00OO0OO0O ={"appToken":appToken ,"content":OO0OO00O00OO00OOO ,"summary":title ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:146
    O0O0OOO0000OO0O0O ='http://wxpusher.zjiecode.com/api/send/message'#line:147
    OO0OO0OOO0OOOOOO0 =requests .post (url =O0O0OOO0000OO0O0O ,json =OOOO00OO00OO0OO0O ).json ()#line:148
    if OO0OO0OOO0OOOOOO0 .get ('code')!=1000 :#line:149
        print (OO0OO0OOO0OOOOOO0 .get ('msg'),OO0OO0OOO0OOOOOO0 )#line:150
    return OO0OO0OOO0OOOOOO0 #line:151
def getmpinfo (OO000O0OOOO0O00O0 ):#line:154
    if not OO000O0OOOO0O00O0 or OO000O0OOOO0O00O0 =='':#line:155
        return False #line:156
    OOOO00OO00O0000O0 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:158
    O00000OOO000OOO0O =requests .get (OO000O0OOOO0O00O0 ,headers =OOOO00OO00O0000O0 )#line:159
    O0O0OOOOOOO0OOOOO =etree .HTML (O00000OOO000OOO0O .text )#line:160
    OO00O0000000O0O00 =O0O0OOOOOOO0OOOOO .xpath ('//meta[@*="og:title"]/@content')#line:162
    if OO00O0000000O0O00 :#line:163
        OO00O0000000O0O00 =OO00O0000000O0O00 [0 ]#line:164
    OOO0O0OOOO0000OO0 =O0O0OOOOOOO0OOOOO .xpath ('//meta[@*="og:url"]/@content')#line:165
    if OOO0O0OOOO0000OO0 :#line:166
        OOO0O0OOOO0000OO0 =OOO0O0OOOO0000OO0 [0 ].encode ().decode ()#line:167
    try :#line:168
        OO00OO000O00O0O00 =re .findall (r'biz=(.*?)&',OO000O0OOOO0O00O0 )[0 ]#line:169
    except :#line:170
        OO00OO000O00O0O00 =re .findall (r'biz=(.*?)&',OOO0O0OOOO0000OO0 )[0 ]#line:171
    if not OO00OO000O00O0O00 :#line:172
        return False #line:173
    O00000OOO00O00OOO =O0O0OOOOOOO0OOOOO .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:174
    if O00000OOO00O00OOO :#line:175
        O00000OOO00O00OOO =O00000OOO00O00OOO [0 ].strip ()#line:176
    O00O0O0O0O00O0O00 =re .findall (r"user_name.DATA'\) : '(.*?)'",O00000OOO000OOO0O .text )or O0O0OOOOOOO0OOOOO .xpath ('//span[@class="profile_meta_value"]/text()')#line:178
    if O00O0O0O0O00O0O00 :#line:179
        O00O0O0O0O00O0O00 =O00O0O0O0O00O0O00 [0 ]#line:180
    OOOO000O0O00O00O0 =re .findall (r'createTime = \'(.*)\'',O00000OOO000OOO0O .text )#line:181
    if OOOO000O0O00O00O0 :#line:182
        OOOO000O0O00O00O0 =OOOO000O0O00O00O0 [0 ][5 :]#line:183
    O00O0O000O0OOOOOO =f'{OOOO000O0O00O00O0}|{OO00O0000000O0O00[:10]}|{OO00OO000O00O0O00}|{O00000OOO00O00OOO}'#line:184
    OO0O000OOO0O00O0O ={'biz':OO00OO000O00O0O00 ,'username':O00000OOO00O00OOO ,'text':O00O0O000O0OOOOOO }#line:185
    return OO0O000OOO0O00O0O #line:186
try :#line:189
    with open ('checkdict.json','r',encoding ='utf-8')as f :#line:190
        checkdict_local =json .loads (f .read ())#line:191
except :#line:192
    pass #line:193
checkdict ={'Mzg2Mzk3Mjk5NQ==':'小鱼儿','MjM5NjU4NTE0MA==':'财事汇','MzkwMjI2ODY5Ng==':'A每日新菜','Mzg3NzEwMzI1Nw==':'A爱玩品牌传奇','MzIyMDg0MzA1OQ==':'服装加工宝','Mzg4NTQ5NDkxMQ==':'秣宝网','Mzk0NjIwNzk0Mg==':'检索宝','MzU3NjA5MDYyMw==':'重庆翊宝智慧电子装置有限公司','MzU1Nzc2ODI0MA==':'星空财研','MzUxMDgxMjMxMw==':'美术宝1对1','MzU4NDMyMTE1MQ==':'海雀Alcidae','MzI4MDE0MzM2NQ==':'强宝时尚','MzA3Nzc5MDMyNg==':'考研红宝书','MjM5Njk5NjYyMQ==':'宝和祥茶业','MzA4NDAyNTQ2MA==':'嘉财万贯','MzIzMjk2MjM5MQ==':'花生酥陪你学','MzkyMDE0NTI2OA==':'重庆市租房宝','MzI0NDI0NzU4OQ==':'九舞文学','MjM5NDAzMjgzNg==':'东风卡车之友','MzI1NjUxMTc0Mw==':'爱普生商教投影机','MzIyNzU3NDIwMA==':'川名堂','MzAwMDUwOTczNg==':'0','MzI4NjYyNTEzMw==':'0','MzI5MDQxNjExNg==':'0','Mzg3MzA0MTkyMw==':'0','MzU0MTUzMTUxOQ==':'0',}#line:202
try :#line:203
    checkdict ={**checkdict ,**checkdict_local }#line:204
except :#line:205
    pass #line:206
class RRBYD :#line:209
    def __init__ (OOO00O00OOO000O0O ,O0O00OOOO000O0O00 ):#line:210
        OOO00O00OOO000O0O .un =O0O00OOOO000O0O00 ['un']#line:211
        OOO00O00OOO000O0O .uid =O0O00OOOO000O0O00 ['uid']#line:212
        OOO00O00OOO000O0O .username =None #line:213
        OOO00O00OOO000O0O .biz =None #line:214
        OOO00O00OOO000O0O .wuid =O0O00OOOO000O0O00 .get ('wuid')#line:215
        OOO00O00OOO000O0O .headers ={'Host':'ebb.vinse.cn','un':OOO00O00OOO000O0O .un ,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue','uid':OOO00O00OOO000O0O .uid ,'platform':'0','token':O0O00OOOO000O0O00 ['token'],'Origin':'http://ebb101.twopinkone.cloud','Referer':'http://ebb101.twopinkone.cloud/',}#line:223
        OOO00O00OOO000O0O .msg =''#line:224
        OOO00O00OOO000O0O .daycount =None #line:225
    def userinfo (O00000OO0O0OOOO0O ):#line:227
        OOOO00OO0OOO0O000 ='http://ebb.vinse.cn/api/user/info'#line:228
        OOOOOO0O00OO000OO =requests .post (OOOO00OO0OOO0O000 ,headers =O00000OO0O0OOOO0O .headers ,json ={"pageSize":10 }).json ()#line:229
        debugger (f'userinfo {OOOOOO0O00OO000OO}')#line:230
        if OOOOOO0O00OO000OO .get ('code')!=0 :#line:231
            O00000OO0O0OOOO0O .msg +=f'{O00000OO0O0OOOO0O.un} cookie失效'+'\n'#line:232
            printlog (f'{O00000OO0O0OOOO0O.un} cookie失效')#line:233
            return 0 #line:234
        OOOOO0000OOOOO000 =OOOOOO0O00OO000OO .get ('result')#line:235
        O00000OO0O0OOOO0O .nickname =OOOOO0000OOOOO000 .get ('nickName')[0 :3 ]+'*'+OOOOO0000OOOOO000 .get ('nickName')[-4 :]#line:236
        OOOOOO0OOOO0O0OOO =OOOOO0000OOOOO000 .get ('integralCurrent')#line:237
        OOOO0OO00OOO00OOO =OOOOO0000OOOOO000 .get ('integralTotal')#line:238
        O00000OO0O0OOOO0O .msg +=f'【{O00000OO0O0OOOO0O.nickname}】:当前共有帮豆{OOOOOO0OOOO0O0OOO}，总共获得帮豆{OOOO0OO00OOO00OOO}\n'#line:239
        printlog (f'【{O00000OO0O0OOOO0O.nickname}】:当前共有帮豆{OOOOOO0OOOO0O0OOO}，总共获得帮豆{OOOO0OO00OOO00OOO}')#line:240
        return OOOOOO0OOOO0O0OOO #line:241
    def sign (O00OOO0OOO0OOO000 ):#line:243
        OOO000OO0OO00000O ='http://ebb.vinse.cn/api/user/sign'#line:244
        O000O0OO0O00O0O0O =requests .post (OOO000OO0OO00000O ,headers =O00OOO0OOO0OOO000 .headers ,json ={"pageSize":10 }).json ()#line:245
        debugger (f'sign {O000O0OO0O00O0O0O}')#line:246
        if O000O0OO0O00O0O0O .get ('code')==0 :#line:247
            O00OOO0OOO0OOO000 .msg +=f'签到成功，获得帮豆{O000O0OO0O00O0O0O.get("result").get("point")}'+'\n'#line:248
            printlog (f'【{O00OOO0OOO0OOO000.nickname}】:签到成功，获得帮豆{O000O0OO0O00O0O0O.get("result").get("point")}')#line:249
        elif O000O0OO0O00O0O0O .get ('code')==99 :#line:250
            O00OOO0OOO0OOO000 .msg +=O000O0OO0O00O0O0O .get ('msg')+'\n'#line:251
        else :#line:252
            O00OOO0OOO0OOO000 .msg +='签到错误'+'\n'#line:253
    def reward (OOOOOO0OO0O0OO00O ):#line:255
        OO00OO0O00O00O000 ='http://ebb.vinse.cn/api/user/receiveOneDivideReward'#line:256
        OOO00000OOO00OOO0 =requests .post (OO00OO0O00O00O000 ,headers =OOOOOO0OO0O0OO00O .headers ,json ={"pageSize":10 }).json ()#line:257
        if OOO00000OOO00OOO0 .get ('code')==0 :#line:258
            OOOOOO0OO0O0OO00O .msg +=f"领取一级帮豆：{OOO00000OOO00OOO0.get('msg')}\n"#line:259
            printlog (f"【{OOOOOO0OO0O0OO00O.nickname}】:领取一级帮豆：{OOO00000OOO00OOO0.get('msg')}")#line:260
        OO00OO0O00O00O000 ='http://ebb.vinse.cn/api/user/receiveTwoDivideReward'#line:261
        OOO00000OOO00OOO0 =requests .post (OO00OO0O00O00O000 ,headers =OOOOOO0OO0O0OO00O .headers ,json ={"pageSize":10 }).json ()#line:262
        if OOO00000OOO00OOO0 .get ('code')==0 :#line:263
            OOOOOO0OO0O0OO00O .msg +=f"领取二级帮豆：{OOO00000OOO00OOO0.get('msg')}"+'\n'#line:264
            printlog (f"【{OOOOOO0OO0O0OO00O.nickname}】:领取二级帮豆：{OOO00000OOO00OOO0.get('msg')}")#line:265
    def getentry (OOO0000OO00OO0OO0 ):#line:267
        OOOOO0O0OOOO0OOOO ={'Host':'u.cocozx.cn',"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Origin":"http://ebb101.twopinkone.cloud","Sec-Fetch-Site":"cross-site","Sec - Fetch - Mode":"cors","Sec - Fetch - Dest":"empty"}#line:274
        OO00O000OO0O0O000 =f'https://u.cocozx.cn/ipa/read/getEntryUrl?fr=ebb0726&uid={OOO0000OO00OO0OO0.uid}'#line:275
        OOO0OO00O000000O0 =requests .get (OO00O000OO0O0O000 ,headers =OOOOO0O0OOOO0OOOO ).json ()#line:276
        debugger (f'getentry {OOO0OO00O000000O0}')#line:277
        OO00OOOOO00O0000O =OOO0OO00O000000O0 .get ('result')#line:278
        if OOO0OO00O000000O0 .get ('code')==0 :#line:279
            OOOOO0OO0OOO0OO00 =OO00OOOOO00O0000O .get ('url')#line:280
            OOO0000OO00OO0OO0 .entryurl =re .findall (r'(http://.*?)/',OOOOO0OO0OOO0OO00 )[0 ]#line:281
        else :#line:282
            OOO0000OO00OO0OO0 .msg +="阅读链接获取失败"+'\n'#line:283
            printlog (f"【{OOO0000OO00OO0OO0.nickname}】:阅读链接获取失败")#line:284
    def read (OO00O000OOO000OO0 ):#line:286
        OOO00O00OOO0OOO00 ={"Origin":OO00O000OOO000OO0 .entryurl ,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Host":"u.cocozx.cn"}#line:291
        O0OOOO0O00O00O000 ={"fr":"ebb0726","uid":OO00O000OOO000OO0 .uid ,"un":'',"token":'',"pageSize":20 }#line:292
        O00000OO0OOO0OOO0 ='http://u.cocozx.cn/ipa/read/info'#line:293
        OO0OO0OOO000O0O00 =requests .post (O00000OO0OOO0OOO0 ,headers =OOO00O00OOO0OOO00 ,json =O0OOOO0O00O00O000 ).json ()#line:294
        OOOO0O0O0O0OO0O00 =OO0OO0OOO000O0O00 .get ('result').get ("dayCount")#line:295
        O00000OO0OOO0OOO0 ='http://u.cocozx.cn/ipa/read/read'#line:296
        while True :#line:297
            OO0OO0OOO000O0O00 =requests .post (O00000OO0OOO0OOO0 ,headers =OOO00O00OOO0OOO00 ,json =O0OOOO0O00O00O000 )#line:298
            debugger ("read "+OO0OO0OOO000O0O00 .text )#line:299
            OO00OO00OOO0OOOO0 =OO0OO0OOO000O0O00 .json ().get ('result')#line:300
            O0000000OO00000O0 =OO00OO00OOO0OOOO0 .get ('url')#line:301
            if OO00OO00OOO0OOOO0 ['status']==10 :#line:302
                O0000OOO0000O0OOO =getmpinfo (O0000000OO00000O0 )#line:303
                if not O0000OOO0000O0OOO :#line:304
                    printlog (f'【{OO00O000OOO000OO0.nickname}】:获取文章信息失败，程序中止')#line:305
                    return False #line:306
                OO00O000OOO000OO0 .msg +='-'*50 +'\n开始阅读 '+O0000OOO0000O0OOO .get ('text')+'\n'#line:307
                printlog (f"【{OO00O000OOO000OO0.nickname}】:\n开始阅读  {O0000OOO0000O0OOO.get('text')}")#line:308
                OO00O000OOO000OO0 .biz =O0000OOO0000O0OOO .get ('biz')#line:309
                OO00O000OOO000OO0 .username =O0000OOO0000O0OOO .get ('username')#line:310
                if OO00O000OOO000OO0 .biz in checkdict .keys ()or OOOO0O0O0O0OO0O00 in [0 ,5 ]or OO00O000OOO000OO0 .daycount in [0 ,5 ]:#line:311
                    OO00O000OOO000OO0 .msg +='正在阅读检测文章\n发送通知，暂停60秒\n'#line:312
                    printlog (f"【{OO00O000OOO000OO0.nickname}】:正在阅读检测文章\n发送通知，暂停60秒")#line:313
                    if sendable :#line:314
                        send (O0000OOO0000O0OOO ['text'],f'【{OO00O000OOO000OO0.nickname}】  人人帮阅读正在读检测文章',O0000000OO00000O0 )#line:315
                    if pushable :#line:316
                        push (f'{OO00O000OOO000OO0.nickname} \n点击阅读检测文章\n{O0000OOO0000O0OOO["text"]}',f'{OO00O000OOO000OO0.nickname}  人人帮阅读过检测文章',O0000000OO00000O0 ,OO00O000OOO000OO0 .wuid )#line:318
                    time .sleep (60 )#line:319
                O0OO000O0OO0OO000 =randint (7 ,10 )#line:320
                time .sleep (O0OO000O0OO0OO000 )#line:321
                OO00O000OOO000OO0 .submit ()#line:322
            elif OO00OO00OOO0OOOO0 ['status']==60 :#line:323
                OO00O000OOO000OO0 .msg +='文章已经全部读完了\n'#line:324
                printlog (f"【{OO00O000OOO000OO0.nickname}】:文章已经全部读完了")#line:325
                break #line:326
            elif OO00OO00OOO0OOOO0 ['status']==30 :#line:327
                time .sleep (2 )#line:328
                continue #line:329
            elif OO00OO00OOO0OOOO0 ['status']==50 :#line:330
                OO00O000OOO000OO0 .msg +='阅读失效\n'#line:331
                printlog (f"【{OO00O000OOO000OO0.nickname}】:阅读失效")#line:332
                if OO00O000OOO000OO0 .biz is not None :#line:333
                    checkdict .update ({OO00O000OOO000OO0 .biz :OO00O000OOO000OO0 .username })#line:334
                    print (checkdict .get (OO00O000OOO000OO0 .biz ))#line:335
                break #line:336
            else :#line:337
                break #line:338
        time .sleep (2 )#line:339
    def submit (O000O000O00OOO0O0 ):#line:341
        OO0000OOOOOO00OOO ='http://u.cocozx.cn/ipa/read/submit'#line:342
        O00OOOO000OOOO0O0 ={"Origin":O000O000O00OOO0O0 .entryurl ,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Host":"u.cocozx.cn"}#line:347
        OOOOOO0000OO00OO0 ={"fr":"ebb0726","uid":O000O000O00OOO0O0 .uid ,"un":'',"token":'',"pageSize":20 }#line:348
        OOOOO000OO0OO0O00 =requests .post (OO0000OOOOOO00OOO ,headers =O00OOOO000OOOO0O0 ,json =OOOOOO0000OO00OO0 ).json ()#line:349
        debugger (f"submit {OOOOO000OO0OO0O00}")#line:350
        OOO0000000OO00O0O =OOOOO000OO0OO0O00 .get ('result')#line:351
        O000O000O00OOO0O0 .daycount =OOO0000000OO00O0O .get ("dayCount")#line:352
        OOOOOO0OO0O0O0O00 =OOO0000000OO00O0O .get ("dayMax")#line:353
        OO0000OOO000000O0 =OOO0000000OO00O0O .get ("progress")#line:354
        O000O000O00OOO0O0 .msg +=f"今日已阅读{O000O000O00OOO0O0.daycount}，本轮剩余{OO0000OOO000000O0}，单日最高{OOOOOO0OO0O0O0O00}\n"#line:355
        printlog (f"【{O000O000O00OOO0O0.nickname}】:今日已阅读{O000O000O00OOO0O0.daycount}，本轮剩余{OO0000OOO000000O0}，单日最高{OOOOOO0OO0O0O0O00}")#line:356
    def tx (OO00OO000O0O00OO0 ):#line:358
        global txje #line:359
        O0OO000000000O0OO =OO00OO000O0O00OO0 .userinfo ()#line:360
        if O0OO000000000O0OO <txbz :#line:361
            OO00OO000O0O00OO0 .msg +='帮豆不够提现标准，明儿请早\n'#line:362
            printlog (f"【{OO00OO000O0O00OO0.nickname}】:帮豆不够提现标准，明儿请早")#line:363
            return #line:364
        elif 5000 <=O0OO000000000O0OO <10000 :#line:365
            txje =5000 #line:366
        elif 10000 <=O0OO000000000O0OO <50000 :#line:367
            txje =10000 #line:368
        elif 50000 <=O0OO000000000O0OO <100000 :#line:369
            txje =50000 #line:370
        elif O0OO000000000O0OO >=100000 :#line:371
            txje =100000 #line:372
        OO0000OO000O0O000 =f"http://ebb.vinse.cn/apiuser/aliWd"#line:373
        O0OOO0000OOOO0OOO ={"val":txje ,"pageSize":10 }#line:374
        O000O00OO00OOO0OO =requests .post (OO0000OO000O0O000 ,headers =OO00OO000O0O00OO0 .headers ,json =O0OOO0000OOOO0OOO ).json ()#line:375
        printlog (f'【{OO00OO000O0O00OO0.nickname}】:提现结果 {O000O00OO00OOO0OO.get("msg")}')#line:376
        if O000O00OO00OOO0OO .get ('code')==0 :#line:377
            if sendable :#line:378
                send (f'【{OO00OO000O0O00OO0.nickname}】 人人帮提现支付宝{txje / 10000}元',title ='人人帮阅读提现到账')#line:379
            if pushable :#line:380
                push (f'【{OO00OO000O0O00OO0.nickname}】 人人帮提现支付宝{txje / 10000}元',title ='人人帮阅读提现到账',uid =OO00OO000O0O00OO0 .wuid )#line:381
    def run (O0OO000O0000O00OO ):#line:383
        O0OO000O0000O00OO .msg +='='*50 +'\n'#line:384
        if O0OO000O0000O00OO .userinfo ():#line:385
            O0OO000O0000O00OO .sign ()#line:386
            O0OO000O0000O00OO .getentry ()#line:387
            time .sleep (1 )#line:388
            O0OO000O0000O00OO .read ()#line:389
            O0OO000O0000O00OO .reward ()#line:390
            O0OO000O0000O00OO .tx ()#line:391
        if not printf :#line:392
            print (O0OO000O0000O00OO .msg .strip ())#line:393
def yd (OO00O00O0000O00OO ):#line:396
    while not OO00O00O0000O00OO .empty ():#line:397
        OO00OOO00000OO000 =OO00O00O0000O00OO .get ()#line:398
        OO0O000000OO000O0 =RRBYD (OO00OOO00000OO000 )#line:399
        OO0O000000OO000O0 .run ()#line:400
def get_info ():#line:403
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:405
    print ('入口：http://ebb.maisucaiya.cloud/user/index.html?mid=1702983440137322496')#line:406
    OOO00000O0O000OO0 ='v1.4.1'#line:407
    OO00O00O0OOO0OOO0 =_O0O00OO0O00O0000O ['version']['人人帮']#line:408
    print (f'当前版本{OOO00000O0O000OO0}，仓库版本{OO00O00O0OOO0OOO0}\n{_O0O00OO0O00O0000O["update_log"]["人人帮"]}')#line:409
    if OOO00000O0O000OO0 <OO00O00O0OOO0OOO0 :#line:410
        print ('请到仓库下载最新版本k_rrb.py')#line:411
    print ("="*25 )#line:412
    return True #line:413
def main ():#line:416
    OOOOOO0000OOOOO0O =get_info ()#line:417
    O000OOOO0O0OOO00O =os .getenv ('rrbck')#line:418
    if not O000OOOO0O0OOO00O :#line:419
        print (_O0O00OO0O00O0000O .get ('msg')['人人帮'])#line:420
        exit ()#line:421
    try :#line:422
        O000OOOO0O0OOO00O =ast .literal_eval (O000OOOO0O0OOO00O )#line:423
    except :#line:424
        pass #line:425
    OOOOOO000000000O0 =Queue ()#line:426
    OOO00OOO00O0OO000 =[]#line:427
    printlog (f'共获取到{len(O000OOOO0O0OOO00O)}个账号，如不正确，请检查ck填写格式')#line:428
    if not OOOOOO0000OOOOO0O :#line:429
        exit ()#line:430
    for O0OO0OOO00000OOO0 ,O000O0O0O0O00O000 in enumerate (O000OOOO0O0OOO00O ,start =1 ):#line:431
        OOOOOO000000000O0 .put (O000O0O0O0O00O000 )#line:432
    for O0OO0OOO00000OOO0 in range (max_workers ):#line:433
        OO0O0OO0O00O0OOO0 =threading .Thread (target =yd ,args =(OOOOOO000000000O0 ,))#line:434
        OO0O0OO0O00O0OOO0 .start ()#line:435
        OOO00OOO00O0OO000 .append (OO0O0OO0O00O0OOO0 )#line:436
        time .sleep (delay_time )#line:437
    for O0O00000OOO000O0O in OOO00OOO00O0OO000 :#line:438
        O0O00000OOO000O0O .join ()#line:439
    print ('-'*25 +f'\n{checkdict}')#line:440
    with open ('checkdict.json','w',encoding ='utf-8')as OOO00O0OOO0OOO00O :#line:441
        OOO00O0OOO0OOO00O .write (json .dumps (checkdict ))#line:442
if __name__ =='__main__':#line:445
    main ()#line:446
