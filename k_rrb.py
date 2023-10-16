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
    OO0O0OOO00OO000OO ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:48
    O00OOOOO000OOOO00 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OO0O0OOO00OO000OO ).json ()#line:49
    return O00OOOOO000OOOO00 #line:50
_OOO0O0O00OO0O0000 =get_msg ()#line:53
try :#line:54
    from lxml import etree #line:55
except :#line:56
    print (_OOO0O0O00OO0O0000 .get ('help')['lxml'])#line:57
if sendable :#line:59
    qwbotkey =os .getenv ('qwbotkey')#line:60
    if not qwbotkey :#line:61
        print (_OOO0O0O00OO0O0000 .get ('help')['qwbotkey'])#line:62
        exit ()#line:63
if pushable :#line:65
    pushconfig =os .getenv ('pushconfig')#line:66
    if not pushconfig :#line:67
        print (_OOO0O0O00OO0O0000 .get ('help')['pushconfig'])#line:68
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
            print (_OOO0O0O00OO0O0000 .get ('help')['pushconfig'])#line:85
            exit ()#line:86
if not pushable and not sendable :#line:88
    print ('啥通知方式都不配置，你想上天吗')#line:89
    exit ()#line:90
def ftime ():#line:93
    O0000O0OOO000O000 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:94
    return O0000O0OOO000O000 #line:95
def debugger (O000000O0OOOOO0OO ):#line:98
    if debug :#line:99
        print (O000000O0OOOOO0OO )#line:100
def printlog (O0O0000OOO00OO000 ):#line:103
    if printf :#line:104
        print (O0O0000OOO00OO000 )#line:105
def send (O0OOOOOO0O0O00000 ,title ='通知',url =None ):#line:108
    if not title or not url :#line:109
        OOOOOO00OOO0O0O00 ={"msgtype":"text","text":{"content":f"{title}\n\n{O0OOOOOO0O0O00000}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:116
    else :#line:117
        OOOOOO00OOO0O0O00 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O0OOOOOO0O0O00000 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:122
    OO000O0OOO0OOO0OO =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:123
    O000O0O00O0OOO000 =requests .post (OO000O0OOO0OOO0OO ,data =json .dumps (OOOOOO00OOO0O0O00 )).json ()#line:124
    if O000O0O00O0OOO000 .get ('errcode')!=0 :#line:125
        print ('消息发送失败，请检查key和发送格式')#line:126
        return False #line:127
    return O000O0O00O0OOO000 #line:128
def push (OO00O0000OOO00000 ,title ='通知',url ='',uid =None ):#line:131
    if uid :#line:132
        uids .append (uid )#line:133
    O0O0OOO000O000OO0 ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',OO00O0000OOO00000 ).replace ('url',url )#line:135
    O0O0OO0OOOO00O0OO ={"appToken":appToken ,"content":O0O0OOO000O000OO0 ,"summary":title ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:145
    O00OO0OO0OO0OOOO0 ='http://wxpusher.zjiecode.com/api/send/message'#line:146
    OOO00O000O0OO00O0 =requests .post (url =O00OO0OO0OO0OOOO0 ,json =O0O0OO0OOOO00O0OO ).json ()#line:147
    if OOO00O000O0OO00O0 .get ('code')!=1000 :#line:148
        print (OOO00O000O0OO00O0 .get ('msg'),OOO00O000O0OO00O0 )#line:149
    return OOO00O000O0OO00O0 #line:150
def getmpinfo (O0O0OOO000O0OOO0O ):#line:153
    if not O0O0OOO000O0OOO0O or O0O0OOO000O0OOO0O =='':#line:154
        return False #line:155
    O000OOO0O00OOO00O ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:157
    OOO000OO0O0O00000 =requests .get (O0O0OOO000O0OOO0O ,headers =O000OOO0O00OOO00O )#line:158
    O000OOO0000OOOO00 =etree .HTML (OOO000OO0O0O00000 .text )#line:159
    OOO00OOOOO00OOOO0 =O000OOO0000OOOO00 .xpath ('//meta[@*="og:title"]/@content')#line:161
    if OOO00OOOOO00OOOO0 :#line:162
        OOO00OOOOO00OOOO0 =OOO00OOOOO00OOOO0 [0 ]#line:163
    O0O0OO0OOO0O00OOO =O000OOO0000OOOO00 .xpath ('//meta[@*="og:url"]/@content')#line:164
    if O0O0OO0OOO0O00OOO :#line:165
        O0O0OO0OOO0O00OOO =O0O0OO0OOO0O00OOO [0 ].encode ().decode ()#line:166
    try :#line:167
        O0O0O00000OO0O0OO =re .findall (r'biz=(.*?)&',O0O0OOO000O0OOO0O )[0 ]#line:168
    except :#line:169
        O0O0O00000OO0O0OO =re .findall (r'biz=(.*?)&',O0O0OO0OOO0O00OOO )[0 ]#line:170
    if not O0O0O00000OO0O0OO :#line:171
        return False #line:172
    O0O0O00OO000OO00O =O000OOO0000OOOO00 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:173
    if O0O0O00OO000OO00O :#line:174
        O0O0O00OO000OO00O =O0O0O00OO000OO00O [0 ].strip ()#line:175
    O0000OO0OO0O000O0 =re .findall (r"user_name.DATA'\) : '(.*?)'",OOO000OO0O0O00000 .text )or O000OOO0000OOOO00 .xpath ('//span[@class="profile_meta_value"]/text()')#line:177
    if O0000OO0OO0O000O0 :#line:178
        O0000OO0OO0O000O0 =O0000OO0OO0O000O0 [0 ]#line:179
    OOOOO0O00OOO0OO0O =re .findall (r'createTime = \'(.*)\'',OOO000OO0O0O00000 .text )#line:180
    if OOOOO0O00OOO0OO0O :#line:181
        OOOOO0O00OOO0OO0O =OOOOO0O00OOO0OO0O [0 ][5 :]#line:182
    O0OO0OO0OOOOOOO00 =f'{OOOOO0O00OOO0OO0O}||{OOO00OOOOO00OOOO0[:10]}||{O0O0O00000OO0O0OO}||{O0O0O00OO000OO00O}'#line:183
    OOO00000O0OO0000O ={'biz':O0O0O00000OO0O0OO ,'text':O0OO0OO0OOOOOOO00 }#line:184
    return OOO00000O0OO0000O #line:185
checklist = ['Mzg2Mzk3Mjk5NQ==', 'MjM5NjU4NTE0MA==','MzkwMjI2ODY5Ng==','Mzg3NzEwMzI1Nw==','MzIyMDg0MzA1OQ==']#line:188
class RRBYD :#line:191
    def __init__ (O0000OO00O00000OO ,O0OOO000OOOO00OO0 ):#line:192
        O0000OO00O00000OO .un =O0OOO000OOOO00OO0 ['un']#line:193
        O0000OO00O00000OO .uid =O0OOO000OOOO00OO0 ['uid']#line:194
        O0000OO00O00000OO .wuid =O0OOO000OOOO00OO0 .get ('wuid')#line:195
        O0000OO00O00000OO .headers ={'Host':'ebb.vinse.cn','un':O0000OO00O00000OO .un ,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue','uid':O0000OO00O00000OO .uid ,'platform':'0','token':O0OOO000OOOO00OO0 ['token'],'Origin':'http://ebb101.twopinkone.cloud','Referer':'http://ebb101.twopinkone.cloud/',}#line:203
        O0000OO00O00000OO .msg =''#line:204
    def userinfo (O0O000O0O0OOO0O00 ):#line:206
        O00OOOOOOOOO0O0O0 ='http://ebb.vinse.cn/api/user/info'#line:207
        O0O0O0O0OOOO00O0O =requests .post (O00OOOOOOOOO0O0O0 ,headers =O0O000O0O0OOO0O00 .headers ,json ={"pageSize":10 }).json ()#line:208
        debugger (f'userinfo {O0O0O0O0OOOO00O0O}')#line:209
        if O0O0O0O0OOOO00O0O .get ('code')!=0 :#line:210
            O0O000O0O0OOO0O00 .msg +=f'{O0O000O0O0OOO0O00.un} cookie失效'+'\n'#line:211
            printlog (f'{O0O000O0O0OOO0O00.un} cookie失效')#line:212
            return 0 #line:213
        OOO0O00O0O0O0O0O0 =O0O0O0O0OOOO00O0O .get ('result')#line:214
        O0O000O0O0OOO0O00 .nickname =OOO0O00O0O0O0O0O0 .get ('nickName')[0 :3 ]+'*'+OOO0O00O0O0O0O0O0 .get ('nickName')[-4 :]#line:215
        O0O0O0O0O000OOOO0 =OOO0O00O0O0O0O0O0 .get ('integralCurrent')#line:216
        OO000000OO00000OO =OOO0O00O0O0O0O0O0 .get ('integralTotal')#line:217
        O0O000O0O0OOO0O00 .msg +=f'【{O0O000O0O0OOO0O00.nickname}】:当前共有帮豆{O0O0O0O0O000OOOO0}，总共获得帮豆{OO000000OO00000OO}\n'#line:218
        printlog (f'【{O0O000O0O0OOO0O00.nickname}】:当前共有帮豆{O0O0O0O0O000OOOO0}，总共获得帮豆{OO000000OO00000OO}')#line:219
        return O0O0O0O0O000OOOO0 #line:220
    def sign (O0OOO00O0O0O0O0O0 ):#line:222
        OO0OOO0000O00OO00 ='http://ebb.vinse.cn/api/user/sign'#line:223
        O0O000OO0000O00OO =requests .post (OO0OOO0000O00OO00 ,headers =O0OOO00O0O0O0O0O0 .headers ,json ={"pageSize":10 }).json ()#line:224
        debugger (f'sign {O0O000OO0000O00OO}')#line:225
        if O0O000OO0000O00OO .get ('code')==0 :#line:226
            O0OOO00O0O0O0O0O0 .msg +=f'签到成功，获得帮豆{O0O000OO0000O00OO.get("result").get("point")}'+'\n'#line:227
            printlog (f'【{O0OOO00O0O0O0O0O0.nickname}】:签到成功，获得帮豆{O0O000OO0000O00OO.get("result").get("point")}')#line:228
        elif O0O000OO0000O00OO .get ('code')==99 :#line:229
            O0OOO00O0O0O0O0O0 .msg +=O0O000OO0000O00OO .get ('msg')+'\n'#line:230
        else :#line:231
            O0OOO00O0O0O0O0O0 .msg +='签到错误'+'\n'#line:232
    def reward (O00OOOOOO0OOOO000 ):#line:234
        OOO000O0OOOOOO00O ='http://ebb.vinse.cn/api/user/receiveOneDivideReward'#line:235
        O0O0OO0O00O000OOO =requests .post (OOO000O0OOOOOO00O ,headers =O00OOOOOO0OOOO000 .headers ,json ={"pageSize":10 }).json ()#line:236
        if O0O0OO0O00O000OOO .get ('code')==0 :#line:237
            O00OOOOOO0OOOO000 .msg +=f"领取一级帮豆：{O0O0OO0O00O000OOO.get('msg')}\n"#line:238
            printlog (f"【{O00OOOOOO0OOOO000.nickname}】:领取一级帮豆：{O0O0OO0O00O000OOO.get('msg')}")#line:239
        OOO000O0OOOOOO00O ='http://ebb.vinse.cn/api/user/receiveTwoDivideReward'#line:240
        O0O0OO0O00O000OOO =requests .post (OOO000O0OOOOOO00O ,headers =O00OOOOOO0OOOO000 .headers ,json ={"pageSize":10 }).json ()#line:241
        if O0O0OO0O00O000OOO .get ('code')==0 :#line:242
            O00OOOOOO0OOOO000 .msg +=f"领取二级帮豆：{O0O0OO0O00O000OOO.get('msg')}"+'\n'#line:243
            printlog (f"【{O00OOOOOO0OOOO000.nickname}】:领取二级帮豆：{O0O0OO0O00O000OOO.get('msg')}")#line:244
    def getentry (O00O0OO000OO0OO00 ):#line:246
        O0O0O00OO00000000 ={'Host':'u.cocozx.cn',"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Origin":"http://ebb101.twopinkone.cloud","Sec-Fetch-Site":"cross-site","Sec - Fetch - Mode":"cors","Sec - Fetch - Dest":"empty"}#line:253
        OOOO000OOOO0O0OO0 =f'https://u.cocozx.cn/ipa/read/getEntryUrl?fr=ebb0726&uid={O00O0OO000OO0OO00.uid}'#line:254
        O0OO0O00OO0O0OOO0 =requests .get (OOOO000OOOO0O0OO0 ,headers =O0O0O00OO00000000 ).json ()#line:255
        debugger (f'getentry {O0OO0O00OO0O0OOO0}')#line:256
        O00O0OO0OOOOO0O00 =O0OO0O00OO0O0OOO0 .get ('result')#line:257
        if O0OO0O00OO0O0OOO0 .get ('code')==0 :#line:258
            O0O0OO00OOOOOOOOO =O00O0OO0OOOOO0O00 .get ('url')#line:259
            O00O0OO000OO0OO00 .entryurl =re .findall (r'(http://.*?)/',O0O0OO00OOOOOOOOO )[0 ]#line:260
        else :#line:261
            O00O0OO000OO0OO00 .msg +="阅读链接获取失败"+'\n'#line:262
            printlog (f"【{O00O0OO000OO0OO00.nickname}】:阅读链接获取失败")#line:263
    def read (O00OOOO00O0O0OOO0 ):#line:265
        OOO0000O00OOOOOOO ={"Origin":O00OOOO00O0O0OOO0 .entryurl ,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Host":"u.cocozx.cn"}#line:270
        OOO0OO00OO00O0O00 ={"fr":"ebb0726","uid":O00OOOO00O0O0OOO0 .uid ,"un":'',"token":'',"pageSize":20 }#line:271
        OO000000O0O0OO0O0 ='http://u.cocozx.cn/ipa/read/read'#line:272
        while True :#line:273
            OO0000OOOOOO00OO0 =requests .post (OO000000O0O0OO0O0 ,headers =OOO0000O00OOOOOOO ,json =OOO0OO00OO00O0O00 )#line:274
            debugger ("read "+OO0000OOOOOO00OO0 .text )#line:275
            OOO0O0OOO0O0O0OOO =OO0000OOOOOO00OO0 .json ().get ('result')#line:276
            O00OO0O00O000O000 =OOO0O0OOO0O0O0OOO .get ('url')#line:277
            if OOO0O0OOO0O0O0OOO ['status']==10 :#line:278
                OO0O000OOOOO00O00 =getmpinfo (O00OO0O00O000O000 )#line:279
                if not OO0O000OOOOO00O00 :#line:280
                    printlog (f'【{O00OOOO00O0O0OOO0.nickname}】:获取文章信息失败，程序中止')#line:281
                    return False #line:282
                O00OOOO00O0O0OOO0 .msg +='-'*50 +'\n开始阅读 '+OO0O000OOOOO00O00 .get ('text')+'\n'#line:283
                printlog (f"【{O00OOOO00O0O0OOO0.nickname}】:\n开始阅读  {OO0O000OOOOO00O00.get('text')}")#line:284
                OOOOOOOO0000O000O =OO0O000OOOOO00O00 .get ('biz')#line:285
                if OOOOOOOO0000O000O in checklist :#line:286
                    O00OOOO00O0O0OOO0 .msg +='正在阅读检测文章\n发送通知，暂停60秒\n'#line:287
                    printlog (f"【{O00OOOO00O0O0OOO0.nickname}】:正在阅读检测文章\n发送通知，暂停60秒")#line:288
                    if sendable :#line:289
                        send (f'【{O00OOOO00O0O0OOO0.nickname}】  人人帮阅读正在读检测文章',OO0O000OOOOO00O00 ['text'],O00OO0O00O000O000 )#line:290
                    if pushable :#line:291
                        push (f'{O00OOOO00O0O0OOO0.nickname} \n点击阅读检测文章\n{OO0O000OOOOO00O00["text"]}',f'{O00OOOO00O0O0OOO0.nickname}  人人帮阅读过检测文章',O00OO0O00O000O000 ,O00OOOO00O0O0OOO0 .wuid )#line:293
                    time .sleep (60 )#line:294
                O00OOOO000O0O0000 =randint (7 ,10 )#line:295
                time .sleep (O00OOOO000O0O0000 )#line:296
                O00OOOO00O0O0OOO0 .submit ()#line:297
            elif OOO0O0OOO0O0O0OOO ['status']==60 :#line:298
                O00OOOO00O0O0OOO0 .msg +='文章已经全部读完了\n'#line:299
                printlog (f"【{O00OOOO00O0O0OOO0.nickname}】:文章已经全部读完了")#line:300
                break #line:301
            elif OOO0O0OOO0O0O0OOO ['status']==30 :#line:302
                time .sleep (2 )#line:303
                continue #line:304
            elif OOO0O0OOO0O0O0OOO ['status']==50 :#line:305
                O00OOOO00O0O0OOO0 .msg +='阅读失效\n'#line:306
                printlog (f"【{O00OOOO00O0O0OOO0.nickname}】:阅读失效")#line:307
                break #line:308
            else :#line:309
                break #line:310
        time .sleep (2 )#line:311
    def submit (OO0O00OOO0O000O0O ):#line:313
        O0OO00OO0O0OOOOOO ='http://u.cocozx.cn/ipa/read/submit'#line:314
        OOOOO00O00OOO0OOO ={"Origin":OO0O00OOO0O000O0O .entryurl ,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Host":"u.cocozx.cn"}#line:319
        O0O0OOO000O0O0O00 ={"fr":"ebb0726","uid":OO0O00OOO0O000O0O .uid ,"un":'',"token":'',"pageSize":20 }#line:320
        O00O00O0OO0O0000O =requests .post (O0OO00OO0O0OOOOOO ,headers =OOOOO00O00OOO0OOO ,json =O0O0OOO000O0O0O00 ).json ()#line:321
        debugger (f"submit {O00O00O0OO0O0000O}")#line:322
        OO00OOOO0OOO0O000 =O00O00O0OO0O0000O .get ('result')#line:323
        OO0O0OO00O0O00O00 =OO00OOOO0OOO0O000 .get ("dayCount")#line:324
        O0000O0O00OOO0000 =OO00OOOO0OOO0O000 .get ("dayMax")#line:325
        O000OO0O0OOOOOOOO =OO00OOOO0OOO0O000 .get ("progress")#line:326
        OO0O00OOO0O000O0O .msg +=f"今日已阅读{OO0O0OO00O0O00O00}，本轮剩余{O000OO0O0OOOOOOOO}，单日最高{O0000O0O00OOO0000}\n"#line:327
        printlog (f"【{OO0O00OOO0O000O0O.nickname}】:今日已阅读{OO0O0OO00O0O00O00}，本轮剩余{O000OO0O0OOOOOOOO}，单日最高{O0000O0O00OOO0000}")#line:328
    def tx (O0000O000O0000000 ):#line:330
        global txje #line:331
        O00O0O000000O00O0 =O0000O000O0000000 .userinfo ()#line:332
        if O00O0O000000O00O0 <txbz :#line:333
            O0000O000O0000000 .msg +='帮豆不够提现标准，明儿请早\n'#line:334
            printlog (f"【{O0000O000O0000000.nickname}】:帮豆不够提现标准，明儿请早")#line:335
            return #line:336
        elif 5000 <=O00O0O000000O00O0 <10000 :#line:337
            txje =5000 #line:338
        elif 10000 <=O00O0O000000O00O0 <50000 :#line:339
            txje =10000 #line:340
        elif 50000 <=O00O0O000000O00O0 <100000 :#line:341
            txje =50000 #line:342
        elif O00O0O000000O00O0 >=100000 :#line:343
            txje =100000 #line:344
        O0OOOOO0000OO00OO =f"http://ebb.vinse.cn/apiuser/aliWd"#line:345
        O00OO0OO000O00OOO ={"val":txje ,"pageSize":10 }#line:346
        O000O0OOOOOO00OO0 =requests .post (O0OOOOO0000OO00OO ,headers =O0000O000O0000000 .headers ,json =O00OO0OO000O00OOO ).json ()#line:347
        printlog (f'【{O0000O000O0000000.nickname}】:提现结果 {O000O0OOOOOO00OO0.get("msg")}')#line:348
        if O000O0OOOOOO00OO0 .get ('code')==0 :#line:349
            if sendable :#line:350
                send (f'【{O0000O000O0000000.nickname}】 人人帮提现支付宝{txje / 10000}元',title ='人人帮阅读提现到账')#line:351
            if pushable :#line:352
                push (f'【{O0000O000O0000000.nickname}】 人人帮提现支付宝{txje / 10000}元',title ='人人帮阅读提现到账',uid =O0000O000O0000000 .wuid )#line:353
    def run (O00000OO0O0O0O0O0 ):#line:355
        O00000OO0O0O0O0O0 .msg +='='*50 +'\n'#line:356
        if O00000OO0O0O0O0O0 .userinfo ():#line:357
            O00000OO0O0O0O0O0 .sign ()#line:358
            O00000OO0O0O0O0O0 .getentry ()#line:359
            time .sleep (1 )#line:360
            O00000OO0O0O0O0O0 .read ()#line:361
            O00000OO0O0O0O0O0 .reward ()#line:362
            O00000OO0O0O0O0O0 .tx ()#line:363
        if not printf :#line:364
            print (O00000OO0O0O0O0O0 .msg .strip ())#line:365
def yd (OO0OO00OO0O0O0O0O ):#line:368
    while not OO0OO00OO0O0O0O0O .empty ():#line:369
        O0OO00O0O000O0000 =OO0OO00OO0O0O0O0O .get ()#line:370
        O0O0OOOO00OOO0OO0 =RRBYD (O0OO00O0O000O0000 )#line:371
        O0O0OOOO00OOO0OO0 .run ()#line:372
def get_info ():#line:375
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:377
    print ('入口：http://ebb.maisucaiya.cloud/user/index.html?mid=1702983440137322496')#line:378
    OO0O000OOO00O0O00 ='v1.4'#line:379
    OOOOOO0000OO0OOOO =_OOO0O0O00OO0O0000 ['version']['k_rrb']#line:380
    print (f'当前版本{OO0O000OOO00O0O00}，仓库版本{OOOOOO0000OO0OOOO}\n{_OOO0O0O00OO0O0000["update_log"]["人人帮"]}')#line:381
    if OO0O000OOO00O0O00 <OOOOOO0000OO0OOOO :#line:382
        print ('请到仓库下载最新版本k_rrb.py')#line:383
    print ("="*25 )#line:384
def main ():#line:387
    get_info ()#line:388
    OOOO00OOO00O0OO00 =os .getenv ('rrbck')#line:389
    if not OOOO00OOO00O0OO00 :#line:390
        print (_OOO0O0O00OO0O0000 .get ('msg')['人人帮'])#line:391
        exit ()#line:392
    try :#line:393
        OOOO00OOO00O0OO00 =ast .literal_eval (OOOO00OOO00O0OO00 )#line:394
    except :#line:395
        pass #line:396
    O0O0000OOO0OOOO00 =Queue ()#line:397
    O000O0O0000O0OOOO =[]#line:398
    printlog (f'共获取到{len(OOOO00OOO00O0OO00)}个账号，如不正确，请检查ck填写格式')#line:399
    for OO0O0O0O0OOO0O000 ,OOOO0OO00OO0O0OOO in enumerate (OOOO00OOO00O0OO00 ,start =1 ):#line:400
        O0O0000OOO0OOOO00 .put (OOOO0OO00OO0O0OOO )#line:401
    for OO0O0O0O0OOO0O000 in range (max_workers ):#line:402
        O00O000O00OOO0000 =threading .Thread (target =yd ,args =(O0O0000OOO0OOOO00 ,))#line:403
        O00O000O00OOO0000 .start ()#line:404
        O000O0O0000O0OOOO .append (O00O000O00OOO0000 )#line:405
        time .sleep (delay_time )#line:406
    for O00O0OO0O00O00OOO in O000O0O0000O0OOOO :#line:407
        O00O0OO0O00O00OOO .join ()#line:408
if __name__ =='__main__':#line:411
    main ()#line:412
