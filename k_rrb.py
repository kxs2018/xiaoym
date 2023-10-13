# -*- coding: utf-8 -*-
# k_rrb
# Author: 惜之酱

"""
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
    O0OOO0O00O000OOOO ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:48
    O0OO0OOOOO0O000O0 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O0OOO0O00O000OOOO ).json ()#line:49
    return O0OO0OOOOO0O000O0 #line:50
_OOO0OOOOO0O0O00OO =get_msg ()#line:53
try :#line:54
    from lxml import etree #line:55
except :#line:56
    print (_OOO0OOOOO0O0O00OO .get ('help')['lxml'])#line:57
if sendable :#line:59
    qwbotkey =os .getenv ('qwbotkey')#line:60
    if not qwbotkey :#line:61
        print (_OOO0OOOOO0O0O00OO .get ('help')['qwbotkey'])#line:62
        exit ()#line:63
if pushable :#line:65
    pushconfig =os .getenv ('pushconfig')#line:66
    if not pushconfig :#line:67
        print (_OOO0OOOOO0O0O00OO .get ('help')['pushconfig'])#line:68
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
            print (_OOO0OOOOO0O0O00OO .get ('help')['pushconfig'])#line:85
            exit ()#line:86
if not pushable and not sendable :#line:88
    print ('啥通知方式都不配置，你想上天吗')#line:89
    exit ()#line:90
def ftime ():#line:93
    OOO00OOOOO000O0OO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:94
    return OOO00OOOOO000O0OO #line:95
def debugger (O0O00OO00O00O0O0O ):#line:98
    if debug :#line:99
        print (O0O00OO00O00O0O0O )#line:100
def printlog (O0000OO00O00OO0OO ):#line:103
    if printf :#line:104
        print (O0000OO00O00OO0OO )#line:105
def send (OOOO0OO0OOOOOO00O ,title ='通知',url =None ):#line:108
    if not title or not url :#line:109
        O00O0OO00O00O000O ={"msgtype":"text","text":{"content":f"{title}\n\n{OOOO0OO0OOOOOO00O}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:116
    else :#line:117
        O00O0OO00O00O000O ={"msgtype":"news","news":{"articles":[{"title":title ,"description":OOOO0OO0OOOOOO00O ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:122
    O00O000O0O000OOO0 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:123
    O0O0000OOO00OOOOO =requests .post (O00O000O0O000OOO0 ,data =json .dumps (O00O0OO00O00O000O )).json ()#line:124
    if O0O0000OOO00OOOOO .get ('errcode')!=0 :#line:125
        print ('消息发送失败，请检查key和发送格式')#line:126
        return False #line:127
    return O0O0000OOO00OOOOO #line:128
def push (OO00O0OOO000OO0OO ,title ='通知',url ='',uid =None ):#line:131
    if uid :#line:132
        uids .append (uid )#line:133
    O0O0OO0O0O0O0O00O ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',OO00O0OOO000OO0OO ).replace ('url',url )#line:135
    OOO00O00OOOOO0O0O ={"appToken":appToken ,"content":O0O0OO0O0O0O0O00O ,"summary":title ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:145
    O0OO000OOOOOOOO00 ='http://wxpusher.zjiecode.com/api/send/message'#line:146
    OOOOO0O0O000O00O0 =requests .post (url =O0OO000OOOOOOOO00 ,json =OOO00O00OOOOO0O0O ).json ()#line:147
    if OOOOO0O0O000O00O0 .get ('code')!=1000 :#line:148
        print (OOOOO0O0O000O00O0 .get ('msg'),OOOOO0O0O000O00O0 )#line:149
    return OOOOO0O0O000O00O0 #line:150
def getmpinfo (OOO00OOO0OOO0O00O ):#line:153
    if not OOO00OOO0OOO0O00O or OOO00OOO0OOO0O00O =='':#line:154
        return False #line:155
    OO000O0OO0O0O0OOO ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:157
    OOOO0O000O000OO00 =requests .get (OOO00OOO0OOO0O00O ,headers =OO000O0OO0O0O0OOO )#line:158
    O0OOOO000OOOO0O0O =etree .HTML (OOOO0O000O000OO00 .text )#line:159
    OO0O0O0O000OO00O0 =O0OOOO000OOOO0O0O .xpath ('//meta[@*="og:title"]/@content')#line:161
    if OO0O0O0O000OO00O0 :#line:162
        OO0O0O0O000OO00O0 =OO0O0O0O000OO00O0 [0 ]#line:163
    OO0OOOOO000OO00OO =O0OOOO000OOOO0O0O .xpath ('//meta[@*="og:url"]/@content')#line:164
    if OO0OOOOO000OO00OO :#line:165
        OO0OOOOO000OO00OO =OO0OOOOO000OO00OO [0 ].encode ().decode ()#line:166
    try :#line:167
        OOOOO000OOOOO00OO =re .findall (r'biz=(.*?)&',OOO00OOO0OOO0O00O )[0 ]#line:168
    except :#line:169
        OOOOO000OOOOO00OO =re .findall (r'biz=(.*?)&',OO0OOOOO000OO00OO )[0 ]#line:170
    if not OOOOO000OOOOO00OO :#line:171
        return False #line:172
    O0OO0OOOOOOO0O000 =O0OOOO000OOOO0O0O .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:173
    if O0OO0OOOOOOO0O000 :#line:174
        O0OO0OOOOOOO0O000 =O0OO0OOOOOOO0O000 [0 ].strip ()#line:175
    O0O00OOO0OOO00OO0 =re .findall (r"user_name.DATA'\) : '(.*?)'",OOOO0O000O000OO00 .text )or O0OOOO000OOOO0O0O .xpath ('//span[@class="profile_meta_value"]/text()')#line:177
    if O0O00OOO0OOO00OO0 :#line:178
        O0O00OOO0OOO00OO0 =O0O00OOO0OOO00OO0 [0 ]#line:179
    OO0O0O00OOO00O0OO =re .findall (r'createTime = \'(.*)\'',OOOO0O000O000OO00 .text )#line:180
    if OO0O0O00OOO00O0OO :#line:181
        OO0O0O00OOO00O0OO =OO0O0O00OOO00O0OO [0 ][5 :]#line:182
    OOOO0O0O0000OOOO0 =f'{OO0O0O00OOO00O0OO} {OO0O0O0O000OO00O0}'#line:183
    OOOO000OOOO0OO0OO ={'biz':OOOOO000OOOOO00OO ,'text':OOOO0O0O0000OOOO0 }#line:184
    return OOOO000OOOO0OO0OO #line:185
class RRBYD :#line:188
    def __init__ (OOOO0O00OO000O0O0 ,O00OO0OO00OO0O000 ):#line:189
        OOOO0O00OO000O0O0 .un =O00OO0OO00OO0O000 ['un']#line:190
        OOOO0O00OO000O0O0 .uid =O00OO0OO00OO0O000 ['uid']#line:191
        OOOO0O00OO000O0O0 .wuid =O00OO0OO00OO0O000 .get ('wuid')#line:192
        OOOO0O00OO000O0O0 .headers ={'Host':'ebb.vinse.cn','un':OOOO0O00OO000O0O0 .un ,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue','uid':OOOO0O00OO000O0O0 .uid ,'platform':'0','token':O00OO0OO00OO0O000 ['token'],'Origin':'http://ebb10.twopinkone.cloud','Referer':'http://ebb10.twopinkone.cloud/',}#line:200
        OOOO0O00OO000O0O0 .msg =''#line:201
    def userinfo (O0000000OO00O000O ):#line:203
        O0O00OOO000O000O0 ='http://ebb.vinse.cn/api/user/info'#line:204
        OO000OO0O0OOO0O0O =requests .post (O0O00OOO000O000O0 ,headers =O0000000OO00O000O .headers ,json ={"pageSize":10 }).json ()#line:205
        debugger (f'userinfo {OO000OO0O0OOO0O0O}')#line:206
        if OO000OO0O0OOO0O0O .get ('code')!=0 :#line:207
            O0000000OO00O000O .msg +=f'{O0000000OO00O000O.un} cookie失效'+'\n'#line:208
            printlog (f'{O0000000OO00O000O.un} cookie失效')#line:209
            return 0 #line:210
        O000OO0OO0OO0OOO0 =OO000OO0O0OOO0O0O .get ('result')#line:211
        O0000000OO00O000O .nickname =O000OO0OO0OO0OOO0 .get ('nickName')[0 :3 ]+'****'+O000OO0OO0OO0OOO0 .get ('nickName')[-4 :]#line:212
        O000O0000OOO00O0O =O000OO0OO0OO0OOO0 .get ('integralCurrent')#line:213
        O0O0OOO0O0OOO00O0 =O000OO0OO0OO0OOO0 .get ('integralTotal')#line:214
        O0000000OO00O000O .msg +=f'【{O0000000OO00O000O.nickname}】:当前共有帮豆{O000O0000OOO00O0O}，总共获得帮豆{O0O0OOO0O0OOO00O0}\n'#line:215
        printlog (f'【{O0000000OO00O000O.nickname}】:当前共有帮豆{O000O0000OOO00O0O}，总共获得帮豆{O0O0OOO0O0OOO00O0}')#line:216
        return O000O0000OOO00O0O #line:217
    def sign (OO00O000O0OOOO0OO ):#line:219
        OOO0O00000000OOOO ='http://ebb.vinse.cn/api/user/sign'#line:220
        OOOO000OOOO0O0O00 =requests .post (OOO0O00000000OOOO ,headers =OO00O000O0OOOO0OO .headers ,json ={"pageSize":10 }).json ()#line:221
        debugger (f'sign {OOOO000OOOO0O0O00}')#line:222
        if OOOO000OOOO0O0O00 .get ('code')==0 :#line:223
            OO00O000O0OOOO0OO .msg +=f'签到成功，获得帮豆{OOOO000OOOO0O0O00.get("result").get("point")}'+'\n'#line:224
            printlog (f'【{OO00O000O0OOOO0OO.nickname}】:签到成功，获得帮豆{OOOO000OOOO0O0O00.get("result").get("point")}')#line:225
        elif OOOO000OOOO0O0O00 .get ('code')==99 :#line:226
            OO00O000O0OOOO0OO .msg +=OOOO000OOOO0O0O00 .get ('msg')+'\n'#line:227
        else :#line:228
            OO00O000O0OOOO0OO .msg +='签到错误'+'\n'#line:229
    def reward (OO0000O0O0O000000 ):#line:231
        OO0O0OO00OOO0OO0O ='http://ebb.vinse.cn/api/user/receiveOneDivideReward'#line:232
        O0O0O0O00000000O0 =requests .post (OO0O0OO00OOO0OO0O ,headers =OO0000O0O0O000000 .headers ,json ={"pageSize":10 }).json ()#line:233
        if O0O0O0O00000000O0 .get ('code')==0 :#line:234
            OO0000O0O0O000000 .msg +=f"领取一级帮豆：{O0O0O0O00000000O0.get('msg')}\n"#line:235
            printlog (f"【{OO0000O0O0O000000.nickname}】:领取一级帮豆：{O0O0O0O00000000O0.get('msg')}")#line:236
        OO0O0OO00OOO0OO0O ='http://ebb.vinse.cn/api/user/receiveTwoDivideReward'#line:237
        O0O0O0O00000000O0 =requests .post (OO0O0OO00OOO0OO0O ,headers =OO0000O0O0O000000 .headers ,json ={"pageSize":10 }).json ()#line:238
        if O0O0O0O00000000O0 .get ('code')==0 :#line:239
            OO0000O0O0O000000 .msg +=f"领取二级帮豆：{O0O0O0O00000000O0.get('msg')}"+'\n'#line:240
            printlog (f"【{OO0000O0O0O000000.nickname}】:领取二级帮豆：{O0O0O0O00000000O0.get('msg')}")#line:241
    def getentry (OO00000O00OO0OO0O ):#line:243
        OO0O000OOO0OO0000 ={'Host':'u.cocozx.cn',"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Origin":"http://ebb10.twopinkone.cloud","Sec-Fetch-Site":"cross-site","Sec - Fetch - Mode":"cors","Sec - Fetch - Dest":"empty"}#line:250
        O00OO0OO0OOOOO000 =f'https://u.cocozx.cn/ipa/read/getEntryUrl?fr=ebb0726&uid={OO00000O00OO0OO0O.uid}'#line:251
        OO0000O000OOOOO00 =requests .get (O00OO0OO0OOOOO000 ,headers =OO0O000OOO0OO0000 ).json ()#line:252
        debugger (f'getentry {OO0000O000OOOOO00}')#line:253
        OOO000OOO00OO0000 =OO0000O000OOOOO00 .get ('result')#line:254
        if OO0000O000OOOOO00 .get ('code')==0 :#line:255
            O00OO00O0000O00OO =OOO000OOO00OO0000 .get ('url')#line:256
            OO00000O00OO0OO0O .entryurl =re .findall (r'(http://.*?)/',O00OO00O0000O00OO )[0 ]#line:257
        else :#line:258
            OO00000O00OO0OO0O .msg +="阅读链接获取失败"+'\n'#line:259
            printlog (f"【{OO00000O00OO0OO0O.nickname}】:阅读链接获取失败")#line:260
    def read (O0O00O00OOO000O0O ):#line:262
        O00O0000OOOO00OO0 ={"Origin":O0O00O00OOO000O0O .entryurl ,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Host":"u.cocozx.cn"}#line:267
        for OO0OOO0OO00O000O0 in range (1 ,3 ):#line:268
            OO000OO0OOO0OO0OO ={"fr":"ebb0726","uid":O0O00O00OOO000O0O .uid ,"group":OO0OOO0OO00O000O0 ,"un":'',"token":'',"pageSize":20 }#line:269
            OO0O00OOO0OOOO0O0 ='http://u.cocozx.cn/ipa/read/read'#line:270
            while True :#line:271
                O0OOOO00O00OOO0O0 =requests .post (OO0O00OOO0OOOO0O0 ,headers =O00O0000OOOO00OO0 ,json =OO000OO0OOO0OO0OO )#line:272
                debugger ("read "+O0OOOO00O00OOO0O0 .text )#line:273
                OO0OOOO0O00O0OOO0 =O0OOOO00O00OOO0O0 .json ().get ('result')#line:274
                OOO00OOO000O00O0O =OO0OOOO0O00O0OOO0 .get ('url')#line:275
                if OO0OOOO0O00O0OOO0 ['status']==10 :#line:276
                    OOO000OOOOO00OO0O =getmpinfo (OOO00OOO000O00O0O )#line:277
                    if not OOO000OOOOO00OO0O :#line:278
                        printlog (f'【{O0O00O00OOO000O0O.nickname}】:获取文章信息失败，程序中止')#line:279
                        return False #line:280
                    O0O00O00OOO000O0O .msg +='-'*50 +'\n开始阅读 '+OOO000OOOOO00OO0O .get ('text')+'\n'#line:281
                    printlog (f"【{O0O00O00OOO000O0O.nickname}】:\n开始阅读  {OOO000OOOOO00OO0O.get('text')}")#line:282
                    OOOO000O0OOOO0O00 =OOO000OOOOO00OO0O .get ('biz')#line:283
                    if OOOO000O0OOOO0O00 =='Mzg2Mzk3Mjk5NQ==':#line:284
                        O0O00O00OOO000O0O .msg +='正在阅读检测文章\n发送通知，暂停60秒\n'#line:285
                        printlog (f"【{O0O00O00OOO000O0O.nickname}】:正在阅读检测文章\n发送通知，暂停60秒")#line:286
                        if sendable :#line:287
                            send (f'【{O0O00O00OOO000O0O.nickname}】  人人帮阅读正在读检测文章',OOO000OOOOO00OO0O ['text'],OOO00OOO000O00O0O )#line:288
                        if pushable :#line:289
                            push (f'{O0O00O00OOO000O0O.nickname} \n点击阅读检测文章\n{OOO000OOOOO00OO0O["text"]}',f'{O0O00O00OOO000O0O.nickname}  人人帮阅读过检测文章',OOO00OOO000O00O0O ,O0O00O00OOO000O0O .wuid )#line:291
                        time .sleep (60 )#line:292
                    O00O0OO0O0OOO0000 =randint (7 ,10 )#line:293
                    time .sleep (O00O0OO0O0OOO0000 )#line:294
                    O0O00O00OOO000O0O .submit (OO0OOO0OO00O000O0 )#line:295
                elif OO0OOOO0O00O0OOO0 ['status']==60 :#line:296
                    O0O00O00OOO000O0O .msg +='文章已经全部读完了\n'#line:297
                    printlog (f"【{O0O00O00OOO000O0O.nickname}】:文章已经全部读完了")#line:298
                    break #line:299
                elif OO0OOOO0O00O0OOO0 ['status']==30 :#line:300
                    time .sleep (2 )#line:301
                    continue #line:302
                elif OO0OOOO0O00O0OOO0 ['status']==50 :#line:303
                    O0O00O00OOO000O0O .msg +='阅读失效\n'#line:304
                    printlog (f"【{O0O00O00OOO000O0O.nickname}】:阅读失效")#line:305
                    break #line:306
                else :#line:307
                    break #line:308
            time .sleep (2 )#line:309
    def submit (O0O00OO000000O00O ,O0O0O00OOOO00OO0O ):#line:311
        OOOOO00OOO00OOO00 ='http://u.cocozx.cn/ipa/read/submit'#line:312
        O0OOOOO00OOOOO0O0 ={"Origin":O0O00OO000000O00O .entryurl ,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Host":"u.cocozx.cn"}#line:317
        OO00OO00O0O000000 ={"fr":"ebb0726","uid":O0O00OO000000O00O .uid ,"group":O0O0O00OOOO00OO0O ,"un":'',"token":'',"pageSize":20 }#line:318
        O0O0OO0000OO000O0 =requests .post (OOOOO00OOO00OOO00 ,headers =O0OOOOO00OOOOO0O0 ,json =OO00OO00O0O000000 ).json ()#line:319
        debugger (f"submit {O0O0OO0000OO000O0}")#line:320
        O000O0OO0000OO000 =O0O0OO0000OO000O0 .get ('result')#line:321
        OOOO0OOOOO0000OO0 =O000O0OO0000OO000 .get ("dayCount")#line:322
        O00O0OOO00O0OO00O =O000O0OO0000OO000 .get ("dayMax")#line:323
        O000O00O0O0O000OO =O000O0OO0000OO000 .get ("progress")#line:324
        O0O00OO000000O00O .msg +=f"今日已阅读{OOOO0OOOOO0000OO0}，本轮剩余{O000O00O0O0O000OO}，单日最高{O00O0OOO00O0OO00O}\n"#line:325
        printlog (f"【{O0O00OO000000O00O.nickname}】:今日已阅读{OOOO0OOOOO0000OO0}，本轮剩余{O000O00O0O0O000OO}，单日最高{O00O0OOO00O0OO00O}")#line:326
    def tx (OOO0O000O00O00O0O ):#line:328
        global txje #line:329
        O000O0OOO0O00OOO0 =OOO0O000O00O00O0O .userinfo ()#line:330
        if O000O0OOO0O00OOO0 <txbz :#line:331
            OOO0O000O00O00O0O .msg +='帮豆不够提现标准，明儿请早\n'#line:332
            printlog (f"【{OOO0O000O00O00O0O.nickname}】:帮豆不够提现标准，明儿请早")#line:333
            return #line:334
        elif 5000 <=O000O0OOO0O00OOO0 <10000 :#line:335
            txje =5000 #line:336
        elif 10000 <=O000O0OOO0O00OOO0 <50000 :#line:337
            txje =10000 #line:338
        elif 50000 <=O000O0OOO0O00OOO0 <100000 :#line:339
            txje =50000 #line:340
        elif O000O0OOO0O00OOO0 >=100000 :#line:341
            txje =100000 #line:342
        OOO000O0OO000OOO0 =f"http://ebb.vinse.cn/apiuser/aliWd"#line:343
        OOO0O0OO000OOO0OO ={"val":txje ,"pageSize":10 }#line:344
        OOOOO0O0OOOOOO0OO =requests .post (OOO000O0OO000OOO0 ,headers =OOO0O000O00O00O0O .headers ,json =OOO0O0OO000OOO0OO ).json ()#line:345
        print (f'【{OOO0O000O00O00O0O.nickname}】:提现结果 {OOOOO0O0OOOOOO0OO.get("msg")}')#line:346
        if OOOOO0O0OOOOOO0OO .get ('code')==0 :#line:347
            if sendable :#line:348
                send (f'【{OOO0O000O00O00O0O.nickname}】 人人帮提现支付宝{txje / 10000}元',title ='人人帮阅读提现到账')#line:349
            if pushable :#line:350
                push (f'【{OOO0O000O00O00O0O.nickname}】 人人帮提现支付宝{txje / 10000}元',title ='人人帮阅读提现到账',uid =OOO0O000O00O00O0O .wuid )#line:351
    def run (OOO000OOO0OOOO0OO ):#line:353
        OOO000OOO0OOOO0OO .msg +='='*50 +'\n'#line:354
        if OOO000OOO0OOOO0OO .userinfo ():#line:355
            OOO000OOO0OOOO0OO .sign ()#line:356
            OOO000OOO0OOOO0OO .getentry ()#line:357
            time .sleep (1 )#line:358
            OOO000OOO0OOOO0OO .read ()#line:359
            OOO000OOO0OOOO0OO .reward ()#line:360
            OOO000OOO0OOOO0OO .tx ()#line:361
        if not printf :#line:362
            print (OOO000OOO0OOOO0OO .msg .strip ())#line:363
def yd (O0O0O000O0OOOOO00 ):#line:366
    while not O0O0O000O0OOOOO00 .empty ():#line:367
        O0OO0OO00O0000OOO =O0O0O000O0OOOOO00 .get ()#line:368
        OOOOO0O0000000O00 =RRBYD (O0OO0OO00O0000OOO )#line:369
        OOOOO0O0000000O00 .run ()#line:370
def get_info ():#line:373
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:375
    print ('入口：http://ebb.maisucaiya.cloud/user/index.html?mid=1702983440137322496')#line:376
    OOOO000OOO000O0OO ='v1.3'#line:377
    O0O000OO0O00OO00O =_OOO0OOOOO0O0O00OO ['version']['k_rrb']#line:378
    print (f'当前版本{OOOO000OOO000O0OO}，仓库版本{O0O000OO0O00OO00O}\n{_OOO0OOOOO0O0O00OO["update_log"]["人人帮"]}')#line:379
    if OOOO000OOO000O0OO <O0O000OO0O00OO00O :#line:380
        print ('请到仓库下载最新版本k_rrb.py')#line:381
    print ("="*25 )#line:382
def main ():#line:385
    get_info ()#line:386
    OOOOOO000O0OOOOOO =os .getenv ('rrbck')#line:387
    if not OOOOOO000O0OOOOOO :#line:388
        print (_OOO0OOOOO0O0O00OO .get ('msg')['人人帮'])#line:389
        exit ()#line:390
    try :#line:391
        OOOOOO000O0OOOOOO =ast .literal_eval (OOOOOO000O0OOOOOO )#line:392
    except :#line:393
        pass #line:394
    OOO0000O00O000000 =Queue ()#line:395
    OOOOOOOO0OO00000O =[]#line:396
    for O0O00OO0OO0OOO0O0 ,O0OO0000O0OOOOO0O in enumerate (OOOOOO000O0OOOOOO ,start =1 ):#line:397
        printlog (f'{O0OO0000O0OOOOO0O}\n以上是账号{O0O00OO0OO0OOO0O0}的ck，如不正确，请检查ck填写格式')#line:398
        OOO0000O00O000000 .put (O0OO0000O0OOOOO0O )#line:399
    for O0O00OO0OO0OOO0O0 in range (max_workers ):#line:400
        O0OO0O0O00O0OOOOO =threading .Thread (target =yd ,args =(OOO0000O00O000000 ,))#line:401
        O0OO0O0O00O0OOOOO .start ()#line:402
        OOOOOOOO0OO00000O .append (O0OO0O0O00O0OOOOO )#line:403
        time .sleep (delay_time )#line:404
    for O0OOOO000OO000O00 in OOOOOOOO0OO00000O :#line:405
        O0OOOO000OO000O00 .join ()#line:406
if __name__ =='__main__':#line:409
    main ()#line:410
