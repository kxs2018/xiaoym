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
    O0OOO0OOO0OOO0O00 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:46
    OOOO000O0O0O0OOO0 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O0OOO0OOO0OOO0O00 ).json ()#line:47
    return OOOO000O0O0O0OOO0 #line:48
_OO00OOOOO0O000OOO =get_msg ()#line:51
try :#line:52
    from lxml import etree #line:53
except :#line:54
    print (_OO00OOOOO0O000OOO .get ('help')['lxml'])#line:55
    exit ()#line:56
import datetime #line:58
import threading #line:59
from queue import Queue #line:60
if sendable :#line:62
    qwbotkey =os .getenv ('qwbotkey')#line:63
    if not qwbotkey :#line:64
        print (_OO00OOOOO0O000OOO .get ('help')['qwbotkey'])#line:65
        exit ()#line:66
if pushable :#line:68
    pushconfig =os .getenv ('pushconfig')#line:69
    if not pushconfig :#line:70
        print (_OO00OOOOO0O000OOO .get ('help')['pushconfig'])#line:71
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
            print (_OO00OOOOO0O000OOO .get ('help')['pushconfig'])#line:88
            exit ()#line:89
def ftime ():#line:92
    O0000000000OO00OO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:93
    return O0000000000OO00OO #line:94
def debugger (OOO00OOO000OO0O00 ):#line:97
    if debug :#line:98
        print (OOO00OOO000OO0O00 )#line:99
def printlog (O00000OO00O0O0O00 ):#line:102
    if printf :#line:103
        print (O00000OO00O0O0O00 )#line:104
def send (OOOOOOOOOO0000O00 ,O000OO0O0O0O0O0O0 ='通知',OO00O0O0OO00OO000 =None ):#line:107
    if not OO00O0O0OO00OO000 :#line:108
        O00O00O0OO0OOO0O0 ={"msgtype":"text","text":{"content":f"{O000OO0O0O0O0O0O0}\n\n{OOOOOOOOOO0000O00}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:115
    else :#line:116
        O00O00O0OO0OOO0O0 ={"msgtype":"news","news":{"articles":[{"title":O000OO0O0O0O0O0O0 ,"description":OOOOOOOOOO0000O00 ,"url":OO00O0O0OO00OO000 ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:121
    OO00OOOO000000OO0 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:122
    O0OOOO0O00O0OOOO0 =requests .post (OO00OOOO000000OO0 ,data =json .dumps (O00O00O0OO0OOO0O0 )).json ()#line:123
    if O0OOOO0O00O0OOOO0 .get ('errcode')!=0 :#line:124
        print ('消息发送失败，请检查key和发送格式')#line:125
        return False #line:126
    return O0OOOO0O00O0OOOO0 #line:127
def push (OO0OOOO0000OOO00O ,O0OOOO0O0OOO00O0O ,O000O00000O0O0O0O ='',OOO0OOOO0OOO0OOOO =None ):#line:130
    if OOO0OOOO0OOO0OOOO :#line:131
        uids .append (OOO0OOOO0OOO0OOOO )#line:132
    O0OO0OOO0OOOO0OO0 ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',OO0OOOO0000OOO00O ).replace ('url',O000O00000O0O0O0O )#line:134
    O00OOOOO0O0OO0000 ={"appToken":appToken ,"content":O0OO0OOO0OOOO0OO0 ,"summary":O0OOOO0O0OOO00O0O ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":O000O00000O0O0O0O ,"verifyPay":False }#line:144
    O0OOOOOO00OO0O000 ='http://wxpusher.zjiecode.com/api/send/message'#line:145
    O0OOOO000O0O0OOO0 =requests .post (url =O0OOOOOO00OO0O000 ,json =O00OOOOO0O0OO0000 ).json ()#line:146
    if O0OOOO000O0O0OOO0 .get ('code')!=1000 :#line:147
        print (O0OOOO000O0O0OOO0 .get ('msg'),O0OOOO000O0O0OOO0 )#line:148
    return O0OOOO000O0O0OOO0 #line:149
def getmpinfo (O0OO000OO0O0OOO00 ):#line:152
    if not O0OO000OO0O0OOO00 or O0OO000OO0O0OOO00 =='':#line:153
        return False #line:154
    O00O00000O00OOOO0 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:156
    OOOOO000O0OO000OO =requests .get (O0OO000OO0O0OOO00 ,headers =O00O00000O00OOOO0 )#line:157
    OOOOO0OO00O00O0O0 =etree .HTML (OOOOO000O0OO000OO .text )#line:158
    O0OOOOOO0OO0O000O =OOOOO0OO00O00O0O0 .xpath ('//meta[@*="og:title"]/@content')#line:159
    if O0OOOOOO0OO0O000O :#line:160
        O0OOOOOO0OO0O000O =O0OOOOOO0OO0O000O [0 ]#line:161
    try :#line:162
        if 'biz='in O0OO000OO0O0OOO00 :#line:163
            OOOOOOOO0O0OO0O0O =re .findall (r'biz=(.*?)&',O0OO000OO0O0OOO00 )[0 ]#line:164
        else :#line:165
            O00OOO00000OO0OO0 =OOOOO0OO00O00O0O0 .xpath ('//meta[@*="og:url"]/@content')[0 ]#line:166
            OOOOOOOO0O0OO0O0O =re .findall (r'biz=(.*?)&',str (O00OOO00000OO0OO0 ))[0 ]#line:167
    except :#line:168
        return False #line:169
    O00000O00000000O0 =OOOOO0OO00O00O0O0 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:170
    if O00000O00000000O0 :#line:171
        O00000O00000000O0 =O00000O00000000O0 [0 ].strip ()#line:172
    OOO0O0OO0OOO00O0O =re .findall (r"user_name.DATA'\) : '(.*?)'",OOOOO000O0OO000OO .text )or OOOOO0OO00O00O0O0 .xpath ('//span[@class="profile_meta_value"]/text()')#line:174
    if OOO0O0OO0OOO00O0O :#line:175
        OOO0O0OO0OOO00O0O =OOO0O0OO0OOO00O0O [0 ]#line:176
    OOOOOOO000OOOOOO0 =re .findall (r'createTime = \'(.*)\'',OOOOO000O0OO000OO .text )#line:177
    if OOOOOOO000OOOOOO0 :#line:178
        OOOOOOO000OOOOOO0 =OOOOOOO000OOOOOO0 [0 ][5 :]#line:179
    O0000OO00O000OO00 =f'{OOOOOOO000OOOOOO0}|{O0OOOOOO0OO0O000O}|{OOOOOOOO0O0OO0O0O}|{O00000O00000000O0}|{OOO0O0OO0OOO00O0O}'#line:180
    OOO000O000O0OOOO0 ={'biz':OOOOOOOO0O0OO0O0O ,'text':O0000OO00O000OO00 }#line:181
    return OOO000O000O0OOOO0 #line:182
class MTZYD :#line:185
    def __init__ (OO0OOOOOOOO000OOO ,OOO0O000O000O0O0O ):#line:186
        OOO0O000O000O0O0O =OOO0O000O000O0O0O .split (';')#line:187
        if ''in OOO0O000O000O0O0O :#line:188
            OOO0O000O000O0O0O .pop ('')#line:189
        OO0OOOOOOOO000OOO .name =OOO0O000O000O0O0O [0 ].split ('=')[1 ]#line:190
        OO0OOOOOOOO000OOO .uid =OOO0O000O000O0O0O [2 ].split ('=')[1 ]if len (OOO0O000O000O0O0O )==3 else None #line:191
        OO0OOOOOOOO000OOO .ck =OOO0O000O000O0O0O [1 ].split ('=')[1 ]#line:192
        OO0OOOOOOOO000OOO .s =requests .session ()#line:193
        OO0OOOOOOOO000OOO .s .headers ={'Authorization':OO0OOOOOOOO000OOO .ck ,'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5279 MMWEBSDK/20230805 MMWEBID/2833 MicroMessenger/8.0.42.2460(0x28002A3B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Accept':'*/*','Origin':'http://61695315208.tt.bendishenghuochwl1.cn','Referer':'http://61695315208.tt.bendishenghuochwl1.cn/','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh',}#line:203
        OO0OOOOOOOO000OOO .msg =''#line:204
    def user_info (OO0O0O00000O0O000 ):#line:206
        OO0000000OO000O0O ='http://api.mengmorwpt1.cn/h5_share/user/info'#line:207
        O0OOO0O00O0O0O0OO =OO0O0O00000O0O000 .s .post (OO0000000OO000O0O ,json ={"openid":0 }).json ()#line:208
        debugger (f'userinfo {O0OOO0O00O0O0O0OO}')#line:209
        if O0OOO0O00O0O0O0OO .get ('code')==200 :#line:210
            O0O00OO00OO0OOO00 =O0OOO0O00O0O0O0OO .get ('data').get ('nickname')#line:211
            OO0O0O00000O0O000 .points =O0OOO0O00O0O0O0OO .get ('data').get ('points')-O0OOO0O00O0O0O0OO .get ('data').get ('withdraw_points')#line:212
            O0OOO0O00O0O0O0OO =OO0O0O00000O0O000 .s .post ('http://api.mengmorwpt1.cn/h5_share/user/sign',json ={"openid":0 })#line:213
            debugger (f'签到 {O0OOO0O00O0O0O0OO.json()}')#line:214
            OOO0000OOO000OOO0 =O0OOO0O00O0O0O0OO .json ().get ('message')#line:215
            OO0O0O00000O0O000 .msg +=f'\n{OO0O0O00000O0O000.name}:{O0O00OO00OO0OOO00},现有积分：{OO0O0O00000O0O000.points}，{OOO0000OOO000OOO0}\n'+'-'*50 +'\n'#line:216
            printlog (f'{OO0O0O00000O0O000.name}:{O0O00OO00OO0OOO00},现有积分：{OO0O0O00000O0O000.points}，{OOO0000OOO000OOO0}')#line:217
            OO0000000OO000O0O ='http://api.mengmorwpt1.cn/h5_share/user/up_profit_ratio'#line:218
            O0OO0O000OO00OOO0 ={"openid":0 }#line:219
            try :#line:220
                O0OOO0O00O0O0O0OO =OO0O0O00000O0O000 .s .post (OO0000000OO000O0O ,json =O0OO0O000OO00OOO0 ).json ()#line:221
                if O0OOO0O00O0O0O0OO .get ('code')==500 :#line:222
                    raise #line:223
                OO0O0O00000O0O000 .msg +=f'代理升级：{O0OOO0O00O0O0O0OO.get("message")}\n'#line:224
            except :#line:225
                OO0000000OO000O0O ='http://api.mengmorwpt1.cn/h5_share/user/task_reward'#line:226
                for OO00OO0O00000000O in range (0 ,8 ):#line:227
                    O0OO0O000OO00OOO0 ={"type":OO00OO0O00000000O ,"openid":0 }#line:228
                    O0OOO0O00O0O0O0OO =OO0O0O00000O0O000 .s .post (OO0000000OO000O0O ,json =O0OO0O000OO00OOO0 ).json ()#line:229
                    if '积分未满'in O0OOO0O00O0O0O0OO .get ('message'):#line:230
                        break #line:231
                    if O0OOO0O00O0O0O0OO .get ('code')!=500 :#line:232
                        OO0O0O00000O0O000 .msg +='主页奖励积分：'+O0OOO0O00O0O0O0OO .get ('message')+'\n'#line:233
                    OO00OO0O00000000O +=1 #line:234
                    time .sleep (0.5 )#line:235
            return True #line:236
        else :#line:237
            OO0O0O00000O0O000 .msg +='获取账号信息异常，检查cookie是否失效\n'#line:238
            printlog (f'{OO0O0O00000O0O000.name}:获取账号信息异常，检查cookie是否失效')#line:239
            if sendable :#line:240
                send (f'{OO0O0O00000O0O000.name} 每天赚获取账号信息异常，检查cookie是否失效','每天赚账号异常通知')#line:241
            if pushable :#line:242
                push (f'{OO0O0O00000O0O000.name} 每天赚获取账号信息异常，检查cookie是否失效','每天赚账号异常通知',uid =OO0O0O00000O0O000 .uid )#line:243
            return False #line:244
    def get_read (O0O00O00OO0OO00O0 ):#line:246
        OO0O00O00OOOO00O0 ='http://api.mengmorwpt1.cn/h5_share/daily/get_read'#line:247
        O0O0OO00O0OO000OO ={"openid":0 }#line:248
        O0OOOOO0O000O0O0O =0 #line:249
        while O0OOOOO0O000O0O0O <10 :#line:250
            O00OO000O0OO00O0O =O0O00O00OO0OO00O0 .s .post (OO0O00O00OOOO00O0 ,json =O0O0OO00O0OO000OO ).json ()#line:251
            debugger (f'getread {O00OO000O0OO00O0O}')#line:252
            if O00OO000O0OO00O0O .get ('code')==200 :#line:253
                O0O00O00OO0OO00O0 .link =O00OO000O0OO00O0O .get ('data').get ('link')#line:254
                return True #line:255
            elif '获取失败'in O00OO000O0OO00O0O .get ('message'):#line:256
                time .sleep (15 )#line:257
                O0OOOOO0O000O0O0O +=1 #line:258
                continue #line:259
            else :#line:260
                O0O00O00OO0OO00O0 .msg +=O00OO000O0OO00O0O .get ('message')+'\n'#line:261
                printlog (f'{O0O00O00OO0OO00O0.name}:{O00OO000O0OO00O0O.get("message")}')#line:262
                return False #line:263
    def gettaskinfo (O0000000OOOOO0O00 ,OO0O0OO00OO000OO0 ):#line:265
        for OOOO0O0O000OO00O0 in OO0O0OO00OO000OO0 :#line:266
            if OOOO0O0O000OO00O0 .get ('url'):#line:267
                return OOOO0O0O000OO00O0 #line:268
    def dotasks (O000000000OO0000O ):#line:270
        O00OOO0OOO0OO0O00 ={'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Origin':'http://nei594688.594688be.com.byymmmcm3.cn','Referer':'http://nei594688.594688be.com.byymmmcm3.cn/','Accept-Encoding':'gzip, deflate',}#line:277
        O00O00OOO00O00O0O =1 #line:278
        while True :#line:279
            OO0O0000O0O0000O0 ={"href":O000000000OO0000O .link }#line:280
            OOO0OOOOOOOO0OO0O ='https://api.wanjd.cn/wxread/articles/tasks'#line:281
            O0OOOOO0O0O000OOO =requests .post (OOO0OOOOOOOO0OO0O ,headers =O00OOO0OOO0OO0O00 ,json =OO0O0000O0O0000O0 ).json ()#line:282
            O0OOO0O0OO0OO0OO0 =O0OOOOO0O0O000OOO .get ('data')#line:283
            debugger (f'tasks {O0OOO0O0OO0OO0OO0}')#line:284
            OOO000OO00OOOO00O =[O00O0OO0O00O000O0 ['is_read']for O00O0OO0O00O000O0 in O0OOO0O0OO0OO0OO0 ]#line:285
            if 0 not in OOO000OO00OOOO00O :#line:286
                break #line:287
            if O0OOOOO0O0O000OOO .get ('code')!=200 :#line:288
                O000000000OO0000O .msg +=O0OOOOO0O0O000OOO .get ('message')+'\n'#line:289
                printlog (f'{O000000000OO0000O.name}:{O0OOOOO0O0O000OOO.get("message")}')#line:290
                break #line:291
            else :#line:292
                O0O000O000OOO0OOO =O000000000OO0000O .gettaskinfo (O0OOOOO0O0O000OOO ['data'])#line:293
                if not O0O000O000OOO0OOO :#line:294
                    break #line:295
                OOO000O00O0O0O0OO =O0O000O000OOO0OOO .get ('url')#line:296
                printlog (f"{O000000000OO0000O.name}:本轮任务数量 {len(O0OOO0O0OO0OO0OO0)}")#line:297
                OO00OOOO0OO0O000O =O0O000O000OOO0OOO ['id']#line:298
                debugger (OO00OOOO0OO0O000O )#line:299
                OO0O0000O0O0000O0 .update ({"id":OO00OOOO0OO0O000O })#line:300
                O0O0000O00O000O00 =getmpinfo (OOO000O00O0O0O0OO )#line:301
                try :#line:302
                    O000000000OO0000O .msg +='正在阅读 '+O0O0000O00O000O00 ['text']+'\n'#line:303
                    printlog (f'{O000000000OO0000O.name}:正在阅读{O0O0000O00O000O00["text"]}')#line:304
                except :#line:305
                    O000000000OO0000O .msg +='获取文章信息失败\n'#line:306
                    printlog (f'{O000000000OO0000O.name}:获取文章信息失败')#line:307
                    break #line:308
                if len (str (OO00OOOO0OO0O000O ))<5 :#line:309
                    if O00O00OOO00O00O0O ==3 :#line:310
                        if sendable :#line:311
                            send ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',f'{O000000000OO0000O.name} 美添赚检测',)#line:314
                        if pushable :#line:315
                            push ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',f'{O000000000OO0000O.name} 美添赚检测',)#line:318
                        break #line:319
                    if sendable :#line:320
                        send (O0O0000O00O000O00 .get ('text'),f'{O000000000OO0000O.name} 美添赚过检测',OOO000O00O0O0O0OO )#line:321
                    if pushable :#line:322
                        push (f'{O000000000OO0000O.name} 本轮任务数量{len(O0OOO0O0OO0OO0OO0)-1}\n点击阅读检测文章\n{O0O0000O00O000O00["text"]}',f'{O000000000OO0000O.name} 美添赚过检测',OOO000O00O0O0O0OO ,uid =O000000000OO0000O .uid )#line:324
                    O000000000OO0000O .msg +='发送通知，暂停50秒\n'#line:325
                    printlog (f'{O000000000OO0000O.name}:发送通知，暂停50秒')#line:326
                    O00O00OOO00O00O0O +=1 #line:327
                    time .sleep (50 )#line:328
                O0000O0OO00O00000 =random .randint (7 ,10 )#line:329
                time .sleep (O0000O0OO00O00000 )#line:330
                OOO0OOOOOOOO0OO0O ='https://api.wanjd.cn/wxread/articles/three_read'#line:331
                O0OOOOO0O0O000OOO =requests .post (OOO0OOOOOOOO0OO0O ,headers =O00OOO0OOO0OO0O00 ,json =OO0O0000O0O0000O0 ).json ()#line:332
                if O0OOOOO0O0O000OOO .get ('code')==200 :#line:333
                    O000000000OO0000O .msg +='阅读成功'+'\n'+'-'*50 +'\n'#line:334
                    printlog (f'{O000000000OO0000O.name}:阅读成功')#line:335
                if O0OOOOO0O0O000OOO .get ('code')!=200 :#line:336
                    O000000000OO0000O .msg +=O0OOOOO0O0O000OOO .get ('message')+'\n'+'-'*50 +'\n'#line:337
                    printlog (f'{O000000000OO0000O.name}:{O0OOOOO0O0O000OOO.get("message")}')#line:338
                    break #line:339
        OOO0OOOOOOOO0OO0O ='https://api.wanjd.cn/wxread/articles/check_success'#line:340
        OO0O0000O0O0000O0 ={'type':1 ,'href':O000000000OO0000O .link }#line:341
        O0OOOOO0O0O000OOO =requests .post (OOO0OOOOOOOO0OO0O ,headers =O00OOO0OOO0OO0O00 ,json =OO0O0000O0O0000O0 ).json ()#line:342
        debugger (f'check {O0OOOOO0O0O000OOO}')#line:343
        O000000000OO0000O .msg +=O0OOOOO0O0O000OOO .get ('message')+'\n'#line:344
        printlog (f'{O000000000OO0000O.name}:{O0OOOOO0O0O000OOO.get("message")}')#line:345
    def withdraw (O00OOOOOOO00O0OOO ):#line:347
        if O00OOOOOOO00O0OOO .points <txbz :#line:348
            O00OOOOOOO00O0OOO .msg +=f'没有达到你设置的提现标准{txbz}\n'#line:349
            printlog (f'{O00OOOOOOO00O0OOO.name}:没有达到你设置的提现标准{txbz}')#line:350
            return False #line:351
        OOO000O0OO0OOOOO0 ='http://api.mengmorwpt1.cn/h5_share/user/withdraw'#line:352
        O0O00OO00O00OOOO0 =O00OOOOOOO00O0OOO .s .post (OOO000O0OO0OOOOO0 ).json ()#line:353
        O00OOOOOOO00O0OOO .msg +='提现结果'+O0O00OO00O00OOOO0 .get ('message')+'\n'#line:354
        printlog (f'{O00OOOOOOO00O0OOO.name}:提现结果 {O0O00OO00O00OOOO0.get("message")}')#line:355
        if O0O00OO00O00OOOO0 .get ('code')==200 :#line:356
            if sendable :#line:357
                send (f'{O00OOOOOOO00O0OOO.name} 已提现到红包，请在服务通知内及时领取','每天赚提现通知')#line:358
            if pushable :#line:359
                push (f'{O00OOOOOOO00O0OOO.name} 已提现到红包，请在服务通知内及时领取','每天赚提现通知',uid =O00OOOOOOO00O0OOO .uid )#line:360
    def run (O0OO00O0000O00OO0 ):#line:362
        O0OO00O0000O00OO0 .msg +='*'*50 +f'\n账号：{O0OO00O0000O00OO0.name}开始任务\n'#line:363
        printlog (f'账号：{O0OO00O0000O00OO0.name}开始任务')#line:364
        if not O0OO00O0000O00OO0 .user_info ():#line:365
            return False #line:366
        if O0OO00O0000O00OO0 .get_read ():#line:367
            O0OO00O0000O00OO0 .dotasks ()#line:368
            O0OO00O0000O00OO0 .user_info ()#line:369
        O0OO00O0000O00OO0 .withdraw ()#line:370
        printlog (f'账号：{O0OO00O0000O00OO0.name}:任务结束')#line:371
        if not printf :#line:372
            print (O0OO00O0000O00OO0 .msg .strip ())#line:373
            print (f'账号：{O0OO00O0000O00OO0.name}任务结束')#line:374
def yd (OOO00OO0OO0000O00 ):#line:377
    while not OOO00OO0OO0000O00 .empty ():#line:378
        O0O0OO00O0O00OOO0 =OOO00OO0OO0000O00 .get ()#line:379
        O0O0000OOO000000O =MTZYD (O0O0OO00O0O00OOO0 )#line:380
        O0O0000OOO000000O .run ()#line:381
def get_info ():#line:384
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:386
    print ('入口：http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552')#line:387
    OOOOOO0OO00OOOO0O ='V2.1'#line:388
    OOOOOO00O0O00OO0O =_OO00OOOOO0O000OOO ['version']['k_mtz']#line:389
    print (f'当前版本{OOOOOO0OO00OOOO0O}，仓库版本{OOOOOO00O0O00OO0O}')#line:390
    if OOOOOO0OO00OOOO0O <OOOOOO00O0O00OO0O :#line:391
        print ('请到仓库下载最新版本k_mtz.py')#line:392
    print ("="*25 )#line:393
def main ():#line:396
    get_info ()#line:397
    OOOO0OOO0O0OO0OO0 =os .getenv ('mtzv2ck')#line:398
    if not OOOO0OOO0O0OO0OO0 :#line:399
        print (_OO00OOOOO0O000OOO .get ('msg')['每天赚'])#line:400
        exit ()#line:401
    OOOO0OOO0O0OO0OO0 =OOOO0OOO0O0OO0OO0 .split ('&')#line:402
    OO0OO0O00OO000000 =Queue ()#line:403
    OO0O00OOO0OOO0O0O =[]#line:404
    for OO0OOO00O0OOOOOO0 ,OO00OO0OOO0OOOO00 in enumerate (OOOO0OOO0O0OO0OO0 ,start =1 ):#line:405
        OO0OO0O00OO000000 .put (OO00OO0OOO0OOOO00 )#line:406
    for OO0OOO00O0OOOOOO0 in range (max_workers ):#line:407
        O0O00000000O00O00 =threading .Thread (target =yd ,args =(OO0OO0O00OO000000 ,))#line:408
        O0O00000000O00O00 .start ()#line:409
        OO0O00OOO0OOO0O0O .append (O0O00000000O00O00 )#line:410
        time .sleep (delay_time )#line:411
    for O0OO0OOO0O0OOOO0O in OO0O00OOO0OOO0O0O :#line:412
        O0OO0OOO0O0OOOO0O .join ()#line:413
if __name__ =='__main__':#line:416
    main ()#line:417
