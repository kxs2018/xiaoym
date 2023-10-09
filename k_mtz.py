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

"""设置单轮任务最小数量"""
total_num = 18
"""设置为18即每轮数量小于18不继续阅读"""

import json #line:40
import os #line:41
import random #line:42
import requests #line:43
import re #line:44
import time #line:45
import ast #line:46
def get_msg ():#line:49
    O000OO0O0O0OOO0O0 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:51
    O00OOO000OO0OOOO0 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O000OO0O0O0OOO0O0 ).json ()#line:52
    return O00OOO000OO0OOOO0 #line:53
_O0O0OOO00O0000OO0 =get_msg ()#line:56
try :#line:57
    from lxml import etree #line:58
except :#line:59
    print (_O0O0OOO00O0000OO0 .get ('help')['lxml'])#line:60
    exit ()#line:61
import datetime #line:63
import threading #line:64
from queue import Queue #line:65
if sendable :#line:67
    qwbotkey =os .getenv ('qwbotkey')#line:68
    if not qwbotkey :#line:69
        print (_O0O0OOO00O0000OO0 .get ('help')['qwbotkey'])#line:70
        exit ()#line:71
if pushable :#line:73
    pushconfig =os .getenv ('pushconfig')#line:74
    if not pushconfig :#line:75
        print (_O0O0OOO00O0000OO0 .get ('help')['pushconfig'])#line:76
        exit ()#line:77
    try :#line:78
        pushconfig =ast .literal_eval (pushconfig )#line:79
    except :#line:80
        pass #line:81
    if isinstance (pushconfig ,dict ):#line:82
        appToken =pushconfig ['appToken']#line:83
        uids =pushconfig ['uids']#line:84
        topicids =pushconfig ['topicids']#line:85
    else :#line:86
        try :#line:87
            "appToken=AT_pCenRjs;uids=['UID_9MZ','UID_T4xlqWx9x'];topicids=['xxx']"#line:88
            appToken =pushconfig .split (';')[0 ].split ('=')[1 ]#line:89
            uids =ast .literal_eval (pushconfig .split (';')[1 ].split ('=')[1 ])#line:90
            topicids =ast .literal_eval (pushconfig .split (';')[2 ].split ('=')[1 ])#line:91
        except :#line:92
            print (_O0O0OOO00O0000OO0 .get ('help')['pushconfig'])#line:93
            exit ()#line:94
def ftime ():#line:97
    OOO00O0O00O0O0000 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:98
    return OOO00O0O00O0O0000 #line:99
def debugger (O00O0OOO0O0OOOOO0 ):#line:102
    if debug :#line:103
        print (O00O0OOO0O0OOOOO0 )#line:104
def printlog (OO0OO000OO00OO0OO ):#line:107
    if printf :#line:108
        print (OO0OO000OO00OO0OO )#line:109
def send (OO00OO0O0OO00O000 ,O0OO0OOOOOO0O00OO ='通知',OO0O0OOO00O0000O0 =None ):#line:112
    if not OO0O0OOO00O0000O0 :#line:113
        O0OO000O000O0000O ={"msgtype":"text","text":{"content":f"{O0OO0OOOOOO0O00OO}\n\n{OO00OO0O0OO00O000}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:120
    else :#line:121
        O0OO000O000O0000O ={"msgtype":"news","news":{"articles":[{"title":O0OO0OOOOOO0O00OO ,"description":OO00OO0O0OO00O000 ,"url":OO0O0OOO00O0000O0 ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:126
    OO000O0OO00000OO0 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:127
    O0OO0OO00OO00O000 =requests .post (OO000O0OO00000OO0 ,data =json .dumps (O0OO000O000O0000O )).json ()#line:128
    if O0OO0OO00OO00O000 .get ('errcode')!=0 :#line:129
        print ('消息发送失败，请检查key和发送格式')#line:130
        return False #line:131
    return O0OO0OO00OO00O000 #line:132
def push (OO00O0000O0OO0O0O ,O00O0OOOOO0O0O00O ,O0O00OOO0O000O00O ='',OO0O000OOO0000OOO =None ):#line:135
    if OO0O000OOO0000OOO :#line:136
        uids .append (OO0O000OOO0000OOO )#line:137
    OO00O000O0O000OO0 ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',OO00O0000O0OO0O0O ).replace ('url',O0O00OOO0O000O00O )#line:139
    O000OOO0OO000O0O0 ={"appToken":appToken ,"content":OO00O000O0O000OO0 ,"summary":O00O0OOOOO0O0O00O ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":O0O00OOO0O000O00O ,"verifyPay":False }#line:149
    O0O00OO0OOO00O0OO ='http://wxpusher.zjiecode.com/api/send/message'#line:150
    OOO0OO0OOOOOOO000 =requests .post (url =O0O00OO0OOO00O0OO ,json =O000OOO0OO000O0O0 ).json ()#line:151
    if OOO0OO0OOOOOOO000 .get ('code')!=1000 :#line:152
        print (OOO0OO0OOOOOOO000 .get ('msg'),OOO0OO0OOOOOOO000 )#line:153
    return OOO0OO0OOOOOOO000 #line:154
def getmpinfo (O00O000OOOO0OO00O ):#line:157
    if not O00O000OOOO0OO00O or O00O000OOOO0OO00O =='':#line:158
        return False #line:159
    O0OOO0OO0O0000O00 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:161
    OO0000OOOO0OOOOOO =requests .get (O00O000OOOO0OO00O ,headers =O0OOO0OO0O0000O00 )#line:162
    O0000O000OO0O0O0O =etree .HTML (OO0000OOOO0OOOOOO .text )#line:163
    OO0OOOOO0OOO00000 =O0000O000OO0O0O0O .xpath ('//meta[@*="og:title"]/@content')#line:164
    if OO0OOOOO0OOO00000 :#line:165
        OO0OOOOO0OOO00000 =OO0OOOOO0OOO00000 [0 ]#line:166
    try :#line:167
        if 'biz='in O00O000OOOO0OO00O :#line:168
            O000OOOOO0OO0O0OO =re .findall (r'biz=(.*?)&',O00O000OOOO0OO00O )[0 ]#line:169
        else :#line:170
            O0OO0O0OOO0O0000O =O0000O000OO0O0O0O .xpath ('//meta[@*="og:url"]/@content')[0 ]#line:171
            O000OOOOO0OO0O0OO =re .findall (r'biz=(.*?)&',str (O0OO0O0OOO0O0000O ))[0 ]#line:172
    except :#line:173
        return False #line:174
    OOO00OO0O00OO0000 =O0000O000OO0O0O0O .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:175
    if OOO00OO0O00OO0000 :#line:176
        OOO00OO0O00OO0000 =OOO00OO0O00OO0000 [0 ].strip ()#line:177
    OO0O00O00OO00O00O =re .findall (r"user_name.DATA'\) : '(.*?)'",OO0000OOOO0OOOOOO .text )or O0000O000OO0O0O0O .xpath ('//span[@class="profile_meta_value"]/text()')#line:179
    if OO0O00O00OO00O00O :#line:180
        OO0O00O00OO00O00O =OO0O00O00OO00O00O [0 ]#line:181
    OOOOO00OO0O000O0O =re .findall (r'createTime = \'(.*)\'',OO0000OOOO0OOOOOO .text )#line:182
    if OOOOO00OO0O000O0O :#line:183
        OOOOO00OO0O000O0O =OOOOO00OO0O000O0O [0 ][5 :]#line:184
    OOO0O000O00O00OO0 =f'{OOOOO00OO0O000O0O}|{OO0OOOOO0OOO00000}|{O000OOOOO0OO0O0OO}|{OOO00OO0O00OO0000}|{OO0O00O00OO00O00O}'#line:185
    OOOOOOO0O00OO00O0 ={'biz':O000OOOOO0OO0O0OO ,'text':OOO0O000O00O00OO0 }#line:186
    return OOOOOOO0O00OO00O0 #line:187
class MTZYD :#line:190
    def __init__ (OOOO0OO00OO0000OO ,OOOO00OOO0O000OO0 ):#line:191
        OOOO00OOO0O000OO0 =OOOO00OOO0O000OO0 .split (';')#line:192
        if ''in OOOO00OOO0O000OO0 :#line:193
            OOOO00OOO0O000OO0 .pop ('')#line:194
        OOOO0OO00OO0000OO .name =OOOO00OOO0O000OO0 [0 ].split ('=')[1 ]#line:195
        OOOO0OO00OO0000OO .uid =OOOO00OOO0O000OO0 [2 ].split ('=')[1 ]if len (OOOO00OOO0O000OO0 )==3 else None #line:196
        OOOO0OO00OO0000OO .ck =OOOO00OOO0O000OO0 [1 ].split ('=')[1 ]#line:197
        OOOO0OO00OO0000OO .s =requests .session ()#line:198
        OOOO0OO00OO0000OO .s .headers ={'Authorization':OOOO0OO00OO0000OO .ck ,'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5279 MMWEBSDK/20230805 MMWEBID/2833 MicroMessenger/8.0.42.2460(0x28002A3B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Accept':'*/*','Origin':'http://61695315208.tt.bendishenghuochwl1.cn','Referer':'http://61695315208.tt.bendishenghuochwl1.cn/','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh',}#line:208
        OOOO0OO00OO0000OO .msg =''#line:209
    def user_info (OO0OO0OO0O00O00O0 ):#line:211
        OO0OOOO000O0O00O0 ='http://api.mengmorwpt1.cn/h5_share/user/info'#line:212
        O0OO0O00000O0OO00 =OO0OO0OO0O00O00O0 .s .post (OO0OOOO000O0O00O0 ,json ={"openid":0 }).json ()#line:213
        debugger (f'userinfo {O0OO0O00000O0OO00}')#line:214
        if O0OO0O00000O0OO00 .get ('code')==200 :#line:215
            OO0000O0O0OOOO00O =O0OO0O00000O0OO00 .get ('data').get ('nickname')#line:216
            OO0OO0OO0O00O00O0 .points =O0OO0O00000O0OO00 .get ('data').get ('points')-O0OO0O00000O0OO00 .get ('data').get ('withdraw_points')#line:217
            O0OO0O00000O0OO00 =OO0OO0OO0O00O00O0 .s .post ('http://api.mengmorwpt1.cn/h5_share/user/sign',json ={"openid":0 })#line:218
            debugger (f'签到 {O0OO0O00000O0OO00.json()}')#line:219
            OO0OOOO00OOO0O000 =O0OO0O00000O0OO00 .json ().get ('message')#line:220
            OO0OO0OO0O00O00O0 .msg +=f'\n{OO0OO0OO0O00O00O0.name}:{OO0000O0O0OOOO00O},现有积分：{OO0OO0OO0O00O00O0.points}，{OO0OOOO00OOO0O000}\n'+'-'*50 +'\n'#line:221
            printlog (f'{OO0OO0OO0O00O00O0.name}:{OO0000O0O0OOOO00O},现有积分：{OO0OO0OO0O00O00O0.points}，{OO0OOOO00OOO0O000}')#line:222
            OO0OOOO000O0O00O0 ='http://api.mengmorwpt1.cn/h5_share/user/up_profit_ratio'#line:223
            O0OO00OOO0O00OO00 ={"openid":0 }#line:224
            try :#line:225
                O0OO0O00000O0OO00 =OO0OO0OO0O00O00O0 .s .post (OO0OOOO000O0O00O0 ,json =O0OO00OOO0O00OO00 ).json ()#line:226
                if O0OO0O00000O0OO00 .get ('code')==500 :#line:227
                    raise #line:228
                OO0OO0OO0O00O00O0 .msg +=f'代理升级：{O0OO0O00000O0OO00.get("message")}\n'#line:229
            except :#line:230
                OO0OOOO000O0O00O0 ='http://api.mengmorwpt1.cn/h5_share/user/task_reward'#line:231
                for OOO00OOO0OO000O0O in range (0 ,8 ):#line:232
                    O0OO00OOO0O00OO00 ={"type":OOO00OOO0OO000O0O ,"openid":0 }#line:233
                    O0OO0O00000O0OO00 =OO0OO0OO0O00O00O0 .s .post (OO0OOOO000O0O00O0 ,json =O0OO00OOO0O00OO00 ).json ()#line:234
                    if '积分未满'in O0OO0O00000O0OO00 .get ('message'):#line:235
                        break #line:236
                    if O0OO0O00000O0OO00 .get ('code')!=500 :#line:237
                        OO0OO0OO0O00O00O0 .msg +='主页奖励积分：'+O0OO0O00000O0OO00 .get ('message')+'\n'#line:238
                    OOO00OOO0OO000O0O +=1 #line:239
                    time .sleep (0.5 )#line:240
            return True #line:241
        else :#line:242
            OO0OO0OO0O00O00O0 .msg +='获取账号信息异常，检查cookie是否失效\n'#line:243
            printlog (f'{OO0OO0OO0O00O00O0.name}:获取账号信息异常，检查cookie是否失效')#line:244
            if sendable :#line:245
                send (f'{OO0OO0OO0O00O00O0.name} 每天赚获取账号信息异常，检查cookie是否失效','每天赚账号异常通知')#line:246
            if pushable :#line:247
                push (f'{OO0OO0OO0O00O00O0.name} 每天赚获取账号信息异常，检查cookie是否失效','每天赚账号异常通知',uid =OO0OO0OO0O00O00O0 .uid )#line:248
            return False #line:249
    def get_read (OOO0O000OO00OOO00 ):#line:251
        O0OOOO00O000000OO ='http://api.mengmorwpt1.cn/h5_share/daily/get_read'#line:252
        O0O00OOOO00O0O000 ={"openid":0 }#line:253
        O00OOOOO0OO0O0OOO =0 #line:254
        while O00OOOOO0OO0O0OOO <10 :#line:255
            OOO0OOOO0000OOOO0 =OOO0O000OO00OOO00 .s .post (O0OOOO00O000000OO ,json =O0O00OOOO00O0O000 ).json ()#line:256
            debugger (f'getread {OOO0OOOO0000OOOO0}')#line:257
            if OOO0OOOO0000OOOO0 .get ('code')==200 :#line:258
                OOO0O000OO00OOO00 .link =OOO0OOOO0000OOOO0 .get ('data').get ('link')#line:259
                return True #line:260
            elif '获取失败'in OOO0OOOO0000OOOO0 .get ('message'):#line:261
                time .sleep (15 )#line:262
                O00OOOOO0OO0O0OOO +=1 #line:263
                continue #line:264
            else :#line:265
                OOO0O000OO00OOO00 .msg +=OOO0OOOO0000OOOO0 .get ('message')+'\n'#line:266
                printlog (f'{OOO0O000OO00OOO00.name}:{OOO0OOOO0000OOOO0.get("message")}')#line:267
                return False #line:268
    def gettaskinfo (OOOOOO000OOOOOO0O ,OOOO000OOO0000O00 ):#line:270
        for OOO0OOOOOOO0OOOO0 in OOOO000OOO0000O00 :#line:271
            if OOO0OOOOOOO0OOOO0 .get ('url'):#line:272
                return OOO0OOOOOOO0OOOO0 #line:273
    def dotasks (O0OOOO000O0OOOO00 ):#line:275
        OOO000000OO0O000O ={'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Origin':'http://nei594688.594688be.com.byymmmcm3.cn','Referer':'http://nei594688.594688be.com.byymmmcm3.cn/','Accept-Encoding':'gzip, deflate',}#line:282
        OO0OO00O000O00000 =0 #line:283
        while True :#line:284
            O00OO0O0000OO0000 ={"href":O0OOOO000O0OOOO00 .link }#line:285
            OOO0OO000O0OO0000 ='https://api.wanjd.cn/wxread/articles/tasks'#line:286
            O0O0OOOOO0O00O00O =requests .post (OOO0OO000O0OO0000 ,headers =OOO000000OO0O000O ,json =O00OO0O0000OO0000 ).json ()#line:287
            OO0O0O000O0OO0O0O =O0O0OOOOO0O00O00O .get ('data')#line:288
            debugger (f'tasks {OO0O0O000O0OO0O0O}')#line:289
            OOO000OO0O00OO0O0 =[OO00O000OOOO0OO0O ['is_read']for OO00O000OOOO0OO0O in OO0O0O000O0OO0O0O ]#line:290
            if 0 not in OOO000OO0O00OO0O0 :#line:291
                break #line:292
            if O0O0OOOOO0O00O00O .get ('code')!=200 :#line:293
                O0OOOO000O0OOOO00 .msg +=O0O0OOOOO0O00O00O .get ('message')+'\n'#line:294
                printlog (f'{O0OOOO000O0OOOO00.name}:{O0O0OOOOO0O00O00O.get("message")}')#line:295
                break #line:296
            else :#line:297
                OOOOOOOO0OOO0O0O0 =O0OOOO000O0OOOO00 .gettaskinfo (O0O0OOOOO0O00O00O ['data'])#line:298
                if not OOOOOOOO0OOO0O0O0 :#line:299
                    break #line:300
                O0000OO00O000000O =OOOOOOOO0OOO0O0O0 .get ('url')#line:301
                printlog (f"{O0OOOO000O0OOOO00.name}:本轮任务数量 {len(OO0O0O000O0OO0O0O)}")#line:302
                if len (OO0O0O000O0OO0O0O )<total_num :#line:303
                    printlog (f'{O0OOOO000O0OOOO00.name}:任务数量小于{total_num}，任务中止')#line:304
                O0OO0O0O000OO000O =OOOOOOOO0OOO0O0O0 ['id']#line:305
                debugger (O0OO0O0O000OO000O )#line:306
                O00OO0O0000OO0000 .update ({"id":O0OO0O0O000OO000O })#line:307
                O00O00O0O0000O00O =getmpinfo (O0000OO00O000000O )#line:308
                try :#line:309
                    O0OOOO000O0OOOO00 .msg +='正在阅读 '+O00O00O0O0000O00O ['text']+'\n'#line:310
                    printlog (f'{O0OOOO000O0OOOO00.name}:正在阅读{O00O00O0O0000O00O["text"]}')#line:311
                except :#line:312
                    O0OOOO000O0OOOO00 .msg +='获取文章信息失败\n'#line:313
                    printlog (f'{O0OOOO000O0OOOO00.name}:获取文章信息失败')#line:314
                    break #line:315
                if len (str (O0OO0O0O000OO000O ))<5 :#line:316
                    if OO0OO00O000O00000 ==3 :#line:317
                        if sendable :#line:318
                            send ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',f'{O0OOOO000O0OOOO00.name} 美添赚检测',)#line:321
                        if pushable :#line:322
                            push ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',f'{O0OOOO000O0OOOO00.name} 美添赚检测',)#line:325
                        break #line:326
                    if sendable :#line:327
                        send (O00O00O0O0000O00O .get ('text'),f'{O0OOOO000O0OOOO00.name} 美添赚过检测',O0000OO00O000000O )#line:328
                    if pushable :#line:329
                        push (f'{O0OOOO000O0OOOO00.name} 本轮任务数量{len(OO0O0O000O0OO0O0O)-1}\n点击阅读检测文章\n{O00O00O0O0000O00O["text"]}',f'{O0OOOO000O0OOOO00.name} 美添赚过检测',O0000OO00O000000O ,uid =O0OOOO000O0OOOO00 .uid )#line:331
                    O0OOOO000O0OOOO00 .msg +='发送通知，暂停50秒\n'#line:332
                    printlog (f'{O0OOOO000O0OOOO00.name}:发送通知，暂停50秒')#line:333
                    OO0OO00O000O00000 +=1 #line:334
                    time .sleep (50 )#line:335
                OO00O0OO000OOOOOO =random .randint (7 ,10 )#line:336
                time .sleep (OO00O0OO000OOOOOO )#line:337
                OOO0OO000O0OO0000 ='https://api.wanjd.cn/wxread/articles/three_read'#line:338
                O0O0OOOOO0O00O00O =requests .post (OOO0OO000O0OO0000 ,headers =OOO000000OO0O000O ,json =O00OO0O0000OO0000 ).json ()#line:339
                if O0O0OOOOO0O00O00O .get ('code')==200 :#line:340
                    O0OOOO000O0OOOO00 .msg +='阅读成功'+'\n'+'-'*50 +'\n'#line:341
                    printlog (f'{O0OOOO000O0OOOO00.name}:阅读成功')#line:342
                if O0O0OOOOO0O00O00O .get ('code')!=200 :#line:343
                    O0OOOO000O0OOOO00 .msg +=O0O0OOOOO0O00O00O .get ('message')+'\n'+'-'*50 +'\n'#line:344
                    printlog (f'{O0OOOO000O0OOOO00.name}:{O0O0OOOOO0O00O00O.get("message")}')#line:345
                    break #line:346
        OOO0OO000O0OO0000 ='https://api.wanjd.cn/wxread/articles/check_success'#line:347
        O00OO0O0000OO0000 ={'type':1 ,'href':O0OOOO000O0OOOO00 .link }#line:348
        O0O0OOOOO0O00O00O =requests .post (OOO0OO000O0OO0000 ,headers =OOO000000OO0O000O ,json =O00OO0O0000OO0000 ).json ()#line:349
        debugger (f'check {O0O0OOOOO0O00O00O}')#line:350
        O0OOOO000O0OOOO00 .msg +=O0O0OOOOO0O00O00O .get ('message')+'\n'#line:351
        printlog (f'{O0OOOO000O0OOOO00.name}:{O0O0OOOOO0O00O00O.get("message")}')#line:352
    def withdraw (O0OO0O00O0OOOO000 ):#line:354
        if O0OO0O00O0OOOO000 .points <txbz :#line:355
            O0OO0O00O0OOOO000 .msg +=f'没有达到你设置的提现标准{txbz}\n'#line:356
            printlog (f'{O0OO0O00O0OOOO000.name}:没有达到你设置的提现标准{txbz}')#line:357
            return False #line:358
        O0000OO00OOOOOO0O ='http://api.mengmorwpt1.cn/h5_share/user/withdraw'#line:359
        OO0OO0OO0O0000OOO =O0OO0O00O0OOOO000 .s .post (O0000OO00OOOOOO0O ).json ()#line:360
        O0OO0O00O0OOOO000 .msg +='提现结果'+OO0OO0OO0O0000OOO .get ('message')+'\n'#line:361
        printlog (f'{O0OO0O00O0OOOO000.name}:提现结果 {OO0OO0OO0O0000OOO.get("message")}')#line:362
        if OO0OO0OO0O0000OOO .get ('code')==200 :#line:363
            if sendable :#line:364
                send (f'{O0OO0O00O0OOOO000.name} 已提现到红包，请在服务通知内及时领取','每天赚提现通知')#line:365
            if pushable :#line:366
                push (f'{O0OO0O00O0OOOO000.name} 已提现到红包，请在服务通知内及时领取','每天赚提现通知',uid =O0OO0O00O0OOOO000 .uid )#line:367
    def run (OOO00OO0OO000OO0O ):#line:369
        OOO00OO0OO000OO0O .msg +='*'*50 +f'\n账号：{OOO00OO0OO000OO0O.name}开始任务\n'#line:370
        printlog (f'账号：{OOO00OO0OO000OO0O.name}开始任务')#line:371
        if not OOO00OO0OO000OO0O .user_info ():#line:372
            return False #line:373
        if OOO00OO0OO000OO0O .get_read ():#line:374
            OOO00OO0OO000OO0O .dotasks ()#line:375
            OOO00OO0OO000OO0O .user_info ()#line:376
        OOO00OO0OO000OO0O .withdraw ()#line:377
        printlog (f'账号：{OOO00OO0OO000OO0O.name}:任务结束')#line:378
        if not printf :#line:379
            print (OOO00OO0OO000OO0O .msg .strip ())#line:380
            print (f'账号：{OOO00OO0OO000OO0O.name}任务结束')#line:381
def yd (OOO0O00O0OOO00000 ):#line:384
    while not OOO0O00O0OOO00000 .empty ():#line:385
        OO00OOOO00O000OOO =OOO0O00O0OOO00000 .get ()#line:386
        OOOO0O0OOOOOO0000 =MTZYD (OO00OOOO00O000OOO )#line:387
        OOOO0O0OOOOOO0000 .run ()#line:388
def get_info ():#line:391
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:393
    print ('入口：http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552')#line:394
    O00O0OO00OOO0O000 ='V2.2'#line:395
    O0O0O00O0000OO0OO =_O0O0OOO00O0000OO0 ['version']['k_mtz']#line:396
    print (f'当前版本{O00O0OO00OOO0O000}，仓库版本{O0O0O00O0000OO0OO}\n{_O0O0OOO00O0000OO0["update_log"]["每天赚"]}')#line:397
    if O00O0OO00OOO0O000 <O0O0O00O0000OO0OO :#line:398
        print ('请到仓库下载最新版本k_mtz.py')#line:399
    print ("="*25 )#line:400
def main ():#line:403
    get_info ()#line:404
    OO00O0O0O0O0O00O0 =os .getenv ('mtzv2ck')#line:405
    if not OO00O0O0O0O0O00O0 :#line:406
        print (_O0O0OOO00O0000OO0 .get ('msg')['每天赚'])#line:407
        exit ()#line:408
    OO00O0O0O0O0O00O0 =OO00O0O0O0O0O00O0 .split ('&')#line:409
    OOO000O0OOOO00OOO =Queue ()#line:410
    O00OOOO00OO0OO0OO =[]#line:411
    for O0O0O00O0OOO00O0O ,OO0OOO0000O0OO000 in enumerate (OO00O0O0O0O0O00O0 ,start =1 ):#line:412
        OOO000O0OOOO00OOO .put (OO0OOO0000O0OO000 )#line:413
    for O0O0O00O0OOO00O0O in range (max_workers ):#line:414
        O0000O0O000OO00OO =threading .Thread (target =yd ,args =(OOO000O0OOOO00OOO ,))#line:415
        O0000O0O000OO00OO .start ()#line:416
        O00OOOO00OO0OO0OO .append (O0000O0O000OO00OO )#line:417
        time .sleep (delay_time )#line:418
    for OOOOOO0OO0OO0O000 in O00OOOO00OO0OO0OO :#line:419
        OOOOOO0OO0OO0O000 .join ()#line:420
if __name__ =='__main__':#line:423
    main ()#line:424
