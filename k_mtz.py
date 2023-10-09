# -*- coding: utf-8 -*-
# k_mtz
# Author: 惜之酱
"""
每天赚入口：http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552
"""
"""实时日志开关"""
printf = 1
"""1为开，0为关"""

"""debug模式开关"""
debug = 0
"""1为开，打印调试日志；0为关，不打印"""

"""设置提现标准"""
txbz = 1000  # 不低于1000，平台的提现标准为1000
"""设置为1000，即为1元起提"""

"""企业微信推送开关"""
sendable = 1  # 开启后必须设置qwbotkey才能运行
"""1为开，0为关"""

"""wxpusher推送开关"""
pushable = 1  # 开启后必须设置pushconfig才能运行
"""1为开，0为关"""

"""线程数量设置"""
max_workers = 5
"""填入数字，设置同时跑任务的数量"""

"""并发延迟设置"""
delay_time = 20
"""设置为20即每隔20秒新增一个号做任务，直到数量达到max_workers"""

import json #line:35
import os #line:36
import random #line:37
import requests #line:38
import re #line:39
import time #line:40
import ast #line:41
def get_msg ():#line:44
    OO000000OO00OOO00 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:46
    O000OOO00O0O0O0OO =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OO000000OO00OOO00 ).json ()#line:47
    return O000OOO00O0O0O0OO #line:48
_OO0OO00O0O0000OO0 =get_msg ()#line:51
try :#line:52
    from lxml import etree #line:53
except :#line:54
    print (_OO0OO00O0O0000OO0 .get ('help')['lxml'])#line:55
    exit ()#line:56
import datetime #line:58
import threading #line:59
from queue import Queue #line:60
if sendable :#line:62
    qwbotkey =os .getenv ('qwbotkey')#line:63
    if not qwbotkey :#line:64
        print (_OO0OO00O0O0000OO0 .get ('help')['qwbotkey'])#line:65
        exit ()#line:66
if pushable :#line:68
    pushconfig =os .getenv ('pushconfig')#line:69
    if not pushconfig :#line:70
        print (_OO0OO00O0O0000OO0 .get ('help')['pushconfig'])#line:71
        exit ()#line:72
    try :#line:73
        pushconfig =ast .literal_eval (pushconfig )#line:74
    except :#line:75
        pass #line:76
    if isinstance (pushconfig ,dict ):#line:77
        appToken =pushconfig ['appToken']#line:78
        uids =pushconfig ['uids']#line:79
        topicids =pushconfig ['topicids']#line:80
    else :#line:81
        try :#line:82
            "appToken=AT_pCenRjs;uids=['UID_9MZ','UID_T4xlqWx9x'];topicids=['xxx']"#line:83
            appToken =pushconfig .split (';')[0 ].split ('=')[1 ]#line:84
            uids =ast .literal_eval (pushconfig .split (';')[1 ].split ('=')[1 ])#line:85
            topicids =ast .literal_eval (pushconfig .split (';')[2 ].split ('=')[1 ])#line:86
        except :#line:87
            print (_OO0OO00O0O0000OO0 .get ('help')['pushconfig'])#line:88
            exit ()#line:89
def ftime ():#line:92
    OO00O0OOOOO000000 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:93
    return OO00O0OOOOO000000 #line:94
def debugger (O000OO00OOO00OO00 ):#line:97
    if debug :#line:98
        print (O000OO00OOO00OO00 )#line:99
def printlog (O000O00O00000O000 ):#line:102
    if printf :#line:103
        print (O000O00O00000O000 )#line:104
def send (OO0OOO0OOOOOO0OOO ,O00000O0OO00O000O ='通知',OOO0O00O0OO0OO00O =None ):#line:107
    if not OOO0O00O0OO0OO00O :#line:108
        O000000O0O0O0OOOO ={"msgtype":"text","text":{"content":f"{O00000O0OO00O000O}\n\n{OO0OOO0OOOOOO0OOO}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:115
    else :#line:116
        O000000O0O0O0OOOO ={"msgtype":"news","news":{"articles":[{"title":O00000O0OO00O000O ,"description":OO0OOO0OOOOOO0OOO ,"url":OOO0O00O0OO0OO00O ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:121
    OOOOO000O000O00OO =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:122
    OOOO0OOOO00OO0000 =requests .post (OOOOO000O000O00OO ,data =json .dumps (O000000O0O0O0OOOO )).json ()#line:123
    if OOOO0OOOO00OO0000 .get ('errcode')!=0 :#line:124
        print ('消息发送失败，请检查key和发送格式')#line:125
        return False #line:126
    return OOOO0OOOO00OO0000 #line:127
def push (OOO00O0O0OOOOOO00 ,O0O0OO0OO000O0O00 ,OO00O0OO0OOOOO000 ='',O000OOOOOO00OO0O0 =None ):#line:130
    if O000OOOOOO00OO0O0 :#line:131
        uids .append (O000OOOOOO00OO0O0 )#line:132
    O00OOO0OOO0OOOO00 ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',OOO00O0O0OOOOOO00 ).replace ('url',OO00O0OO0OOOOO000 )#line:134
    O00OOO0O0OO0O00O0 ={"appToken":appToken ,"content":O00OOO0OOO0OOOO00 ,"summary":O0O0OO0OO000O0O00 ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":OO00O0OO0OOOOO000 ,"verifyPay":False }#line:144
    OOOO0O0O00O00O0OO ='http://wxpusher.zjiecode.com/api/send/message'#line:145
    O000OOO0O0OO0OOOO =requests .post (url =OOOO0O0O00O00O0OO ,json =O00OOO0O0OO0O00O0 ).json ()#line:146
    if O000OOO0O0OO0OOOO .get ('code')!=1000 :#line:147
        print (O000OOO0O0OO0OOOO .get ('msg'),O000OOO0O0OO0OOOO )#line:148
    return O000OOO0O0OO0OOOO #line:149
def getmpinfo (O000OO0000OO00O00 ):#line:152
    if not O000OO0000OO00O00 or O000OO0000OO00O00 =='':#line:153
        return False #line:154
    O00000OO000OO0O00 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:156
    O0000OO0O00OO0O0O =requests .get (O000OO0000OO00O00 ,headers =O00000OO000OO0O00 )#line:157
    OO0OOO0OOOO000000 =etree .HTML (O0000OO0O00OO0O0O .text )#line:158
    O00000O00O00OO000 =OO0OOO0OOOO000000 .xpath ('//meta[@*="og:title"]/@content')#line:159
    if O00000O00O00OO000 :#line:160
        O00000O00O00OO000 =O00000O00O00OO000 [0 ]#line:161
    try :#line:162
        if 'biz='in O000OO0000OO00O00 :#line:163
            O0OO0OOO0OOO00O00 =re .findall (r'biz=(.*?)&',O000OO0000OO00O00 )[0 ]#line:164
        else :#line:165
            O00000O0000O0000O =OO0OOO0OOOO000000 .xpath ('//meta[@*="og:url"]/@content')[0 ]#line:166
            O0OO0OOO0OOO00O00 =re .findall (r'biz=(.*?)&',str (O00000O0000O0000O ))[0 ]#line:167
    except :#line:168
        return False #line:169
    OO0OO0OO0O00000O0 =OO0OOO0OOOO000000 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:170
    if OO0OO0OO0O00000O0 :#line:171
        OO0OO0OO0O00000O0 =OO0OO0OO0O00000O0 [0 ].strip ()#line:172
    OO0000OOOO00O00OO =re .findall (r"user_name.DATA'\) : '(.*?)'",O0000OO0O00OO0O0O .text )or OO0OOO0OOOO000000 .xpath ('//span[@class="profile_meta_value"]/text()')#line:174
    if OO0000OOOO00O00OO :#line:175
        OO0000OOOO00O00OO =OO0000OOOO00O00OO [0 ]#line:176
    OO0O0OO0OOOOO0OOO =re .findall (r'createTime = \'(.*)\'',O0000OO0O00OO0O0O .text )#line:177
    if OO0O0OO0OOOOO0OOO :#line:178
        OO0O0OO0OOOOO0OOO =OO0O0OO0OOOOO0OOO [0 ][5 :]#line:179
    OO0O000O0O0O0O000 =f'{OO0O0OO0OOOOO0OOO}|{O00000O00O00OO000}|{O0OO0OOO0OOO00O00}|{OO0OO0OO0O00000O0}|{OO0000OOOO00O00OO}'#line:180
    OO00O00OOOOOO0000 ={'biz':O0OO0OOO0OOO00O00 ,'text':OO0O000O0O0O0O000 }#line:181
    return OO00O00OOOOOO0000 #line:182
class MTZYD :#line:185
    def __init__ (OOOO0O0OOO0OOO000 ,O000O0O00OO0OO0OO ):#line:186
        O000O0O00OO0OO0OO =O000O0O00OO0OO0OO .split (';')#line:187
        if ''in O000O0O00OO0OO0OO :#line:188
            O000O0O00OO0OO0OO .pop ('')#line:189
        OOOO0O0OOO0OOO000 .name =O000O0O00OO0OO0OO [0 ].split ('=')[1 ]#line:190
        OOOO0O0OOO0OOO000 .uid =O000O0O00OO0OO0OO [2 ].split ('=')[1 ]if len (O000O0O00OO0OO0OO )==3 else None #line:191
        OOOO0O0OOO0OOO000 .ck =O000O0O00OO0OO0OO [1 ].split ('=')[1 ]#line:192
        OOOO0O0OOO0OOO000 .s =requests .session ()#line:193
        OOOO0O0OOO0OOO000 .s .headers ={'Authorization':OOOO0O0OOO0OOO000 .ck ,'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5279 MMWEBSDK/20230805 MMWEBID/2833 MicroMessenger/8.0.42.2460(0x28002A3B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Accept':'*/*','Origin':'http://61695315208.tt.bendishenghuochwl1.cn','Referer':'http://61695315208.tt.bendishenghuochwl1.cn/','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh',}#line:203
        OOOO0O0OOO0OOO000 .msg =''#line:204
    def user_info (OO000OO00OOOOOO00 ):#line:206
        O00000OOO0O0O00O0 ='http://api.mengmorwpt1.cn/h5_share/user/info'#line:207
        OOOOOOO00OOO000OO =OO000OO00OOOOOO00 .s .post (O00000OOO0O0O00O0 ,json ={"openid":0 }).json ()#line:208
        debugger (f'userinfo {OOOOOOO00OOO000OO}')#line:209
        if OOOOOOO00OOO000OO .get ('code')==200 :#line:210
            OO000OO00OOOOOO00 .nickname =OOOOOOO00OOO000OO .get ('data').get ('nickname')#line:211
            OO000OO00OOOOOO00 .points =OOOOOOO00OOO000OO .get ('data').get ('points')-OOOOOOO00OOO000OO .get ('data').get ('withdraw_points')#line:212
            OOOOOOO00OOO000OO =OO000OO00OOOOOO00 .s .post ('http://api.mengmorwpt1.cn/h5_share/user/sign',json ={"openid":0 })#line:213
            debugger (f'签到 {OOOOOOO00OOO000OO.json()}')#line:214
            O0000O0O00O0OO00O =OOOOOOO00OOO000OO .json ().get ('message')#line:215
            OO000OO00OOOOOO00 .msg +=f'\n{OO000OO00OOOOOO00.name}:{OO000OO00OOOOOO00.nickname},现有积分：{OO000OO00OOOOOO00.points}，{O0000O0O00O0OO00O}\n'+'-'*50 +'\n'#line:216
            printlog (f'{OO000OO00OOOOOO00.name}:{OO000OO00OOOOOO00.nickname},现有积分：{OO000OO00OOOOOO00.points}，{O0000O0O00O0OO00O}')#line:217
            O00000OOO0O0O00O0 ='http://api.mengmorwpt1.cn/h5_share/user/up_profit_ratio'#line:218
            OOOO0000O0OO0OOO0 ={"openid":0 }#line:219
            try :#line:220
                OOOOOOO00OOO000OO =OO000OO00OOOOOO00 .s .post (O00000OOO0O0O00O0 ,json =OOOO0000O0OO0OOO0 ).json ()#line:221
                if OOOOOOO00OOO000OO .get ('code')==500 :#line:222
                    raise #line:223
                OO000OO00OOOOOO00 .msg +=f'代理升级：{OOOOOOO00OOO000OO.get("message")}\n'#line:224
            except :#line:225
                O00000OOO0O0O00O0 ='http://api.mengmorwpt1.cn/h5_share/user/task_reward'#line:226
                for OO00O00OO0O0O0O00 in range (0 ,8 ):#line:227
                    OOOO0000O0OO0OOO0 ={"type":OO00O00OO0O0O0O00 ,"openid":0 }#line:228
                    OOOOOOO00OOO000OO =OO000OO00OOOOOO00 .s .post (O00000OOO0O0O00O0 ,json =OOOO0000O0OO0OOO0 ).json ()#line:229
                    if '积分未满'in OOOOOOO00OOO000OO .get ('message'):#line:230
                        break #line:231
                    if OOOOOOO00OOO000OO .get ('code')!=500 :#line:232
                        OO000OO00OOOOOO00 .msg +='主页奖励积分：'+OOOOOOO00OOO000OO .get ('message')+'\n'#line:233
                    OO00O00OO0O0O0O00 +=1 #line:234
                    time .sleep (0.5 )#line:235
            return True #line:236
        else :#line:237
            OO000OO00OOOOOO00 .msg +='获取账号信息异常，检查cookie是否失效\n'#line:238
            printlog (f'{OO000OO00OOOOOO00.name}:获取账号信息异常，检查cookie是否失效')#line:239
            if sendable :#line:240
                send (f'{OO000OO00OOOOOO00.name} 每天赚获取账号信息异常，检查cookie是否失效','每天赚账号异常通知')#line:241
            if pushable :#line:242
                push (f'{OO000OO00OOOOOO00.name} 每天赚获取账号信息异常，检查cookie是否失效','每天赚账号异常通知',uid =OO000OO00OOOOOO00 .uid )#line:243
            return False #line:244
    def get_read (O0000O0O0OO00000O ):#line:246
        O0O000O0000O0OO00 ='http://api.mengmorwpt1.cn/h5_share/daily/get_read'#line:247
        O0O0OO0O0O00OO0OO ={"openid":0 }#line:248
        OO0000OO0OOO0OOOO =0 #line:249
        while OO0000OO0OOO0OOOO <10 :#line:250
            OO000O0O000OOO0OO =O0000O0O0OO00000O .s .post (O0O000O0000O0OO00 ,json =O0O0OO0O0O00OO0OO ).json ()#line:251
            debugger (f'getread {OO000O0O000OOO0OO}')#line:252
            if OO000O0O000OOO0OO .get ('code')==200 :#line:253
                O0000O0O0OO00000O .link =OO000O0O000OOO0OO .get ('data').get ('link')#line:254
                return True #line:255
            elif '获取失败'in OO000O0O000OOO0OO .get ('message'):#line:256
                time .sleep (15 )#line:257
                OO0000OO0OOO0OOOO +=1 #line:258
                continue #line:259
            else :#line:260
                O0000O0O0OO00000O .msg +=OO000O0O000OOO0OO .get ('message')+'\n'#line:261
                printlog (f'{O0000O0O0OO00000O.name}:{OO000O0O000OOO0OO.get("message")}')#line:262
                return False #line:263
    def gettaskinfo (O00000000OOO0OOOO ,OO0O0OOOOOO0OO00O ):#line:265
        for OOO00O0OO0OOOOO00 in OO0O0OOOOOO0OO00O :#line:266
            if OOO00O0OO0OOOOO00 .get ('url'):#line:267
                return OOO00O0OO0OOOOO00 #line:268
    def dotasks (O0O000OO0OO0O0O0O ):#line:270
        OOOOOO000OOOO00OO ={'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Origin':'http://nei594688.594688be.com.byymmmcm3.cn','Referer':'http://nei594688.594688be.com.byymmmcm3.cn/','Accept-Encoding':'gzip, deflate',}#line:277
        OO0O00OOO00O0O000 =1 #line:278
        while True :#line:279
            OOO00O0O000O00000 ={"href":O0O000OO0OO0O0O0O .link }#line:280
            O0O00000OOOO00O00 ='https://api.wanjd.cn/wxread/articles/tasks'#line:281
            O0O00000O00000OOO =requests .post (O0O00000OOOO00O00 ,headers =OOOOOO000OOOO00OO ,json =OOO00O0O000O00000 ).json ()#line:282
            O00OOOO00O0O00OOO =O0O00000O00000OOO .get ('data')#line:283
            debugger (f'tasks {O00OOOO00O0O00OOO}')#line:284
            O0OO0OOOOO0OOOOO0 =[OO0O00O00O0000000 ['is_read']for OO0O00O00O0000000 in O00OOOO00O0O00OOO ]#line:285
            if 0 not in O0OO0OOOOO0OOOOO0 :#line:286
                break #line:287
            if O0O00000O00000OOO .get ('code')!=200 :#line:288
                O0O000OO0OO0O0O0O .msg +=O0O00000O00000OOO .get ('message')+'\n'#line:289
                printlog (f'{O0O000OO0OO0O0O0O.name}:{O0O00000O00000OOO.get("message")}')#line:290
                break #line:291
            else :#line:292
                OO0O00O0O000O00OO =O0O000OO0OO0O0O0O .gettaskinfo (O0O00000O00000OOO ['data'])#line:293
                if not OO0O00O0O000O00OO :#line:294
                    break #line:295
                O0OO000O0OO000O0O =OO0O00O0O000O00OO .get ('url')#line:296
                printlog (f"{O0O000OO0OO0O0O0O.nickname}:本轮任务数量 {len(O00OOOO00O0O00OOO)}")#line:297
                OOOO0OOO00OO0OO00 =OO0O00O0O000O00OO ['id']#line:298
                debugger (OOOO0OOO00OO0OO00 )#line:299
                OOO00O0O000O00000 .update ({"id":OOOO0OOO00OO0OO00 })#line:300
                OO0000O0O00OO000O =getmpinfo (O0OO000O0OO000O0O )#line:301
                try :#line:302
                    O0O000OO0OO0O0O0O .msg +='正在阅读 '+OO0000O0O00OO000O ['text']+'\n'#line:303
                    printlog (f'{O0O000OO0OO0O0O0O.name}:正在阅读{OO0000O0O00OO000O["text"]}')#line:304
                except :#line:305
                    O0O000OO0OO0O0O0O .msg +='获取文章信息失败\n'#line:306
                    printlog (f'{O0O000OO0OO0O0O0O.name}:获取文章信息失败')#line:307
                    break #line:308
                if len (str (OOOO0OOO00OO0OO00 ))<5 :#line:309
                    if OO0O00OOO00O0O000 ==3 :#line:310
                        if sendable :#line:311
                            send ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',f'{O0O000OO0OO0O0O0O.name} 美添赚检测',)#line:314
                        if pushable :#line:315
                            push ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',f'{O0O000OO0OO0O0O0O.name} 美添赚检测',)#line:318
                        break #line:319
                    if sendable :#line:320
                        send (OO0000O0O00OO000O .get ('text'),f'{O0O000OO0OO0O0O0O.name} 美添赚过检测',O0OO000O0OO000O0O )#line:321
                    if pushable :#line:322
                        push (f'{O0O000OO0OO0O0O0O.name} 本轮任务数量{len(O00OOOO00O0O00OOO)-1}\n点击阅读检测文章\n{OO0000O0O00OO000O["text"]}',f'{O0O000OO0OO0O0O0O.name} 美添赚过检测',O0OO000O0OO000O0O ,uid =O0O000OO0OO0O0O0O .uid )#line:324
                    O0O000OO0OO0O0O0O .msg +='发送通知，暂停50秒\n'#line:325
                    printlog (f'{O0O000OO0OO0O0O0O.name}:发送通知，暂停50秒')#line:326
                    OO0O00OOO00O0O000 +=1 #line:327
                    time .sleep (50 )#line:328
                O000000OO00OO0O00 =random .randint (7 ,10 )#line:329
                time .sleep (O000000OO00OO0O00 )#line:330
                O0O00000OOOO00O00 ='https://api.wanjd.cn/wxread/articles/three_read'#line:331
                O0O00000O00000OOO =requests .post (O0O00000OOOO00O00 ,headers =OOOOOO000OOOO00OO ,json =OOO00O0O000O00000 ).json ()#line:332
                if O0O00000O00000OOO .get ('code')==200 :#line:333
                    O0O000OO0OO0O0O0O .msg +='阅读成功'+'\n'+'-'*50 +'\n'#line:334
                    printlog (f'{O0O000OO0OO0O0O0O.name}:阅读成功')#line:335
                if O0O00000O00000OOO .get ('code')!=200 :#line:336
                    O0O000OO0OO0O0O0O .msg +=O0O00000O00000OOO .get ('message')+'\n'+'-'*50 +'\n'#line:337
                    printlog (f'{O0O000OO0OO0O0O0O.name}:{O0O00000O00000OOO.get("message")}')#line:338
                    break #line:339
        O0O00000OOOO00O00 ='https://api.wanjd.cn/wxread/articles/check_success'#line:340
        OOO00O0O000O00000 ={'type':1 ,'href':O0O000OO0OO0O0O0O .link }#line:341
        O0O00000O00000OOO =requests .post (O0O00000OOOO00O00 ,headers =OOOOOO000OOOO00OO ,json =OOO00O0O000O00000 ).json ()#line:342
        debugger (f'check {O0O00000O00000OOO}')#line:343
        O0O000OO0OO0O0O0O .msg +=O0O00000O00000OOO .get ('message')+'\n'#line:344
        printlog (f'{O0O000OO0OO0O0O0O.name}:{O0O00000O00000OOO.get("message")}')#line:345
    def withdraw (OO0O00O0OOOOO0O00 ):#line:347
        if OO0O00O0OOOOO0O00 .points <txbz :#line:348
            OO0O00O0OOOOO0O00 .msg +=f'没有达到你设置的提现标准{txbz}\n'#line:349
            printlog (f'{OO0O00O0OOOOO0O00.name}:没有达到你设置的提现标准{txbz}')#line:350
            return False #line:351
        O00O000O00OO00O0O ='http://api.mengmorwpt1.cn/h5_share/user/withdraw'#line:352
        O000OO0OO0O0OOOO0 =OO0O00O0OOOOO0O00 .s .post (O00O000O00OO00O0O ).json ()#line:353
        OO0O00O0OOOOO0O00 .msg +='提现结果'+O000OO0OO0O0OOOO0 .get ('message')+'\n'#line:354
        printlog (f'{OO0O00O0OOOOO0O00.name}:提现结果 {O000OO0OO0O0OOOO0.get("message")}')#line:355
        if O000OO0OO0O0OOOO0 .get ('code')==200 :#line:356
            if sendable :#line:357
                send (f'{OO0O00O0OOOOO0O00.name} 已提现到红包，请在服务通知内及时领取','每天赚提现通知')#line:358
            if pushable :#line:359
                push (f'{OO0O00O0OOOOO0O00.name} 已提现到红包，请在服务通知内及时领取','每天赚提现通知',uid =OO0O00O0OOOOO0O00 .uid )#line:360
    def run (OO0O0OOOOO000OO0O ):#line:362
        OO0O0OOOOO000OO0O .msg +='*'*50 +f'\n账号：{OO0O0OOOOO000OO0O.name}开始任务\n'#line:363
        printlog (f'账号：{OO0O0OOOOO000OO0O.name}开始任务')#line:364
        if not OO0O0OOOOO000OO0O .user_info ():#line:365
            return False #line:366
        if OO0O0OOOOO000OO0O .get_read ():#line:367
            OO0O0OOOOO000OO0O .dotasks ()#line:368
            OO0O0OOOOO000OO0O .user_info ()#line:369
        OO0O0OOOOO000OO0O .withdraw ()#line:370
        printlog (f'账号：{OO0O0OOOOO000OO0O.name}:任务结束')#line:371
        if not printf :#line:372
            print (OO0O0OOOOO000OO0O .msg .strip ())#line:373
            print (f'账号：{OO0O0OOOOO000OO0O.name}任务结束')#line:374
def yd (O0O0OO00O00O00O00 ):#line:377
    while not O0O0OO00O00O00O00 .empty ():#line:378
        OOO0O000O0O00OO0O =O0O0OO00O00O00O00 .get ()#line:379
        OOO0OOOO0O0OO0O0O =MTZYD (OOO0O000O0O00OO0O )#line:380
        OOO0OOOO0O0OO0O0O .run ()#line:381
def get_info ():#line:384
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:386
    print ('入口：http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552')#line:387
    O0O000O00O0O0OOOO ='V2.1'#line:388
    O00O0O0O0OOOO0000 =_OO0OO00O0O0000OO0 ['version']['k_mtz']#line:389
    print (f'当前版本{O0O000O00O0O0OOOO}，仓库版本{O00O0O0O0OOOO0000}')#line:390
    if O0O000O00O0O0OOOO <O00O0O0O0OOOO0000 :#line:391
        print ('请到仓库下载最新版本k_mtz.py')#line:392
    print ("="*25 )#line:393
def main ():#line:396
    get_info ()#line:397
    OOOO0OOOO000OO0OO =os .getenv ('mtzv2ck')#line:398
    if not OOOO0OOOO000OO0OO :#line:399
        print (_OO0OO00O0O0000OO0 .get ('msg')['每天赚'])#line:400
        exit ()#line:401
    OOOO0OOOO000OO0OO =OOOO0OOOO000OO0OO .split ('&')#line:402
    OO000O0OOO00OOO00 =Queue ()#line:403
    O0O0O0OOO0000O00O =[]#line:404
    for OO0OOO0O000OOO00O ,OOO00OOO0O000OO00 in enumerate (OOOO0OOOO000OO0OO ,start =1 ):#line:405
        OO000O0OOO00OOO00 .put (OOO00OOO0O000OO00 )#line:406
    for OO0OOO0O000OOO00O in range (max_workers ):#line:407
        OO00OO0O000O0OO00 =threading .Thread (target =yd ,args =(OO000O0OOO00OOO00 ,))#line:408
        OO00OO0O000O0OO00 .start ()#line:409
        O0O0O0OOO0000O00O .append (OO00OO0O000O0OO00 )#line:410
        time .sleep (20 )#line:411
    for O0OO0OOO0OO0OO000 in O0O0O0OOO0000O00O :#line:412
        O0OO0OOO0OO0OO000 .join ()#line:413
if __name__ =='__main__':#line:416
    main ()#line:417

