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
    O0000O000O0OOOOO0 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:46
    OO0O0O0OOOO000O0O =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O0000O000O0OOOOO0 ).json ()#line:47
    return OO0O0O0OOOO000O0O #line:48
_O0OO0O00O0OOO0OOO =get_msg ()#line:51
try :#line:52
    from lxml import etree #line:53
except :#line:54
    print (_O0OO0O00O0OOO0OOO .get ('help')['lxml'])#line:55
    exit ()#line:56
import datetime #line:58
import threading #line:59
from queue import Queue #line:60
if sendable :#line:62
    qwbotkey =os .getenv ('qwbotkey')#line:63
    if not qwbotkey :#line:64
        print (_O0OO0O00O0OOO0OOO .get ('help')['qwbotkey'])#line:65
        exit ()#line:66
if pushable :#line:68
    pushconfig =os .getenv ('pushconfig')#line:69
    if not pushconfig :#line:70
        print (_O0OO0O00O0OOO0OOO .get ('help')['pushconfig'])#line:71
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
            print (_O0OO0O00O0OOO0OOO .get ('help')['pushconfig'])#line:88
            exit ()#line:89
def ftime ():#line:92
    OOOOO000O000000OO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:93
    return OOOOO000O000000OO #line:94
def debugger (OOOOOOO0O0O0O0OO0 ):#line:97
    if debug :#line:98
        print (OOOOOOO0O0O0O0OO0 )#line:99
def printlog (O00O0000O00OO00OO ):#line:102
    if printf :#line:103
        print (O00O0000O00OO00OO )#line:104
def send (O00O00OO00OO000O0 ,OOOO0OOOO00OO0O0O ='通知',O00OO0OOOOOOO0OOO =None ):#line:107
    if not O00OO0OOOOOOO0OOO :#line:108
        OO00O0OO00000000O ={"msgtype":"text","text":{"content":f"{OOOO0OOOO00OO0O0O}\n\n{O00O00OO00OO000O0}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:115
    else :#line:116
        OO00O0OO00000000O ={"msgtype":"news","news":{"articles":[{"title":OOOO0OOOO00OO0O0O ,"description":O00O00OO00OO000O0 ,"url":O00OO0OOOOOOO0OOO ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:121
    O0OO0O0O00O0OOO0O =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:122
    OO0OOO00O00OO0OO0 =requests .post (O0OO0O0O00O0OOO0O ,data =json .dumps (OO00O0OO00000000O )).json ()#line:123
    if OO0OOO00O00OO0OO0 .get ('errcode')!=0 :#line:124
        print ('消息发送失败，请检查key和发送格式')#line:125
        return False #line:126
    return OO0OOO00O00OO0OO0 #line:127
def push (O00OO0O0000000OO0 ,OOOOO0OOO000O0OOO ,OO0000000O0OOOOOO ='',O00OO0OO00000OO00 =None ):#line:130
    if O00OO0OO00000OO00 :#line:131
        uids .append (O00OO0OO00000OO00 )#line:132
    O0O00O0OOO00OOOO0 ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',O00OO0O0000000OO0 ).replace ('url',OO0000000O0OOOOOO )#line:134
    OO000O0000OOOO0O0 ={"appToken":appToken ,"content":O0O00O0OOO00OOOO0 ,"summary":OOOOO0OOO000O0OOO ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":OO0000000O0OOOOOO ,"verifyPay":False }#line:144
    O00OO0OO0OOOOOOOO ='http://wxpusher.zjiecode.com/api/send/message'#line:145
    O0OO00000OOO0OOOO =requests .post (url =O00OO0OO0OOOOOOOO ,json =OO000O0000OOOO0O0 ).json ()#line:146
    if O0OO00000OOO0OOOO .get ('code')!=1000 :#line:147
        print (O0OO00000OOO0OOOO .get ('msg'),O0OO00000OOO0OOOO )#line:148
    return O0OO00000OOO0OOOO #line:149
def getmpinfo (O0OO00O0000O00O0O ):#line:152
    if not O0OO00O0000O00O0O or O0OO00O0000O00O0O =='':#line:153
        return False #line:154
    OOO000OOOOO00O0OO ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:156
    O00000O0OO0O00OOO =requests .get (O0OO00O0000O00O0O ,headers =OOO000OOOOO00O0OO )#line:157
    O0O0OOO00O0O0OOOO =etree .HTML (O00000O0OO0O00OOO .text )#line:158
    OOOO00O000O000OOO =O0O0OOO00O0O0OOOO .xpath ('//meta[@*="og:title"]/@content')#line:159
    if OOOO00O000O000OOO :#line:160
        OOOO00O000O000OOO =OOOO00O000O000OOO [0 ]#line:161
    try :#line:162
        if 'biz='in O0OO00O0000O00O0O :#line:163
            OO00000OO0O0O0OO0 =re .findall (r'biz=(.*?)&',O0OO00O0000O00O0O )[0 ]#line:164
        else :#line:165
            O0O000OO0OO0000OO =O0O0OOO00O0O0OOOO .xpath ('//meta[@*="og:url"]/@content')[0 ]#line:166
            OO00000OO0O0O0OO0 =re .findall (r'biz=(.*?)&',str (O0O000OO0OO0000OO ))[0 ]#line:167
    except :#line:168
        return False #line:169
    O0O0O00O0O00OOO00 =O0O0OOO00O0O0OOOO .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:170
    if O0O0O00O0O00OOO00 :#line:171
        O0O0O00O0O00OOO00 =O0O0O00O0O00OOO00 [0 ].strip ()#line:172
    O0OO0000OO0OOOO0O =re .findall (r"user_name.DATA'\) : '(.*?)'",O00000O0OO0O00OOO .text )or O0O0OOO00O0O0OOOO .xpath ('//span[@class="profile_meta_value"]/text()')#line:174
    if O0OO0000OO0OOOO0O :#line:175
        O0OO0000OO0OOOO0O =O0OO0000OO0OOOO0O [0 ]#line:176
    O0OOO0000OO0000O0 =re .findall (r'createTime = \'(.*)\'',O00000O0OO0O00OOO .text )#line:177
    if O0OOO0000OO0000O0 :#line:178
        O0OOO0000OO0000O0 =O0OOO0000OO0000O0 [0 ][5 :]#line:179
    OOO0O0OO0O00O0OOO =f'{O0OOO0000OO0000O0}|{OOOO00O000O000OOO}|{OO00000OO0O0O0OO0}|{O0O0O00O0O00OOO00}|{O0OO0000OO0OOOO0O}'#line:180
    OOOOOO00OO00000O0 ={'biz':OO00000OO0O0O0OO0 ,'text':OOO0O0OO0O00O0OOO }#line:181
    return OOOOOO00OO00000O0 #line:182
class MTZYD :#line:185
    def __init__ (O00OO0000O0O00000 ,O0O0O0OO0OO000OO0 ):#line:186
        O0O0O0OO0OO000OO0 =O0O0O0OO0OO000OO0 .split (';')#line:187
        if ''in O0O0O0OO0OO000OO0 :#line:188
            O0O0O0OO0OO000OO0 .pop ('')#line:189
        O00OO0000O0O00000 .name =O0O0O0OO0OO000OO0 [0 ].split ('=')[1 ]#line:190
        O00OO0000O0O00000 .uid =O0O0O0OO0OO000OO0 [2 ].split ('=')[1 ]if len (O0O0O0OO0OO000OO0 )==3 else None #line:191
        O00OO0000O0O00000 .ck =O0O0O0OO0OO000OO0 [1 ].split ('=')[1 ]#line:192
        O00OO0000O0O00000 .s =requests .session ()#line:193
        O00OO0000O0O00000 .s .headers ={'Authorization':O00OO0000O0O00000 .ck ,'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5279 MMWEBSDK/20230805 MMWEBID/2833 MicroMessenger/8.0.42.2460(0x28002A3B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Accept':'*/*','Origin':'http://61695315208.tt.bendishenghuochwl1.cn','Referer':'http://61695315208.tt.bendishenghuochwl1.cn/','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh',}#line:203
        O00OO0000O0O00000 .msg =''#line:204
    def user_info (OOO00000OO000OOOO ):#line:206
        OOOO0OOOOOOO0O0O0 ='http://api.mengmorwpt1.cn/h5_share/user/info'#line:207
        OOO0OOO00O00OO00O =OOO00000OO000OOOO .s .post (OOOO0OOOOOOO0O0O0 ,json ={"openid":0 }).json ()#line:208
        debugger (f'userinfo {OOO0OOO00O00OO00O}')#line:209
        if OOO0OOO00O00OO00O .get ('code')==200 :#line:210
            O0OO00O0OOOO0OOOO =OOO0OOO00O00OO00O .get ('data').get ('nickname')#line:211
            OOO00000OO000OOOO .points =OOO0OOO00O00OO00O .get ('data').get ('points')-OOO0OOO00O00OO00O .get ('data').get ('withdraw_points')#line:212
            OOO0OOO00O00OO00O =OOO00000OO000OOOO .s .post ('http://api.mengmorwpt1.cn/h5_share/user/sign',json ={"openid":0 })#line:213
            debugger (f'签到 {OOO0OOO00O00OO00O.json()}')#line:214
            O00OOO00000OOOOOO =OOO0OOO00O00OO00O .json ().get ('message')#line:215
            OOO00000OO000OOOO .msg +=f'\n{OOO00000OO000OOOO.name}:{O0OO00O0OOOO0OOOO},现有积分：{OOO00000OO000OOOO.points}，{O00OOO00000OOOOOO}\n'+'-'*50 +'\n'#line:216
            printlog (f'{OOO00000OO000OOOO.name}:{O0OO00O0OOOO0OOOO},现有积分：{OOO00000OO000OOOO.points}，{O00OOO00000OOOOOO}')#line:217
            OOOO0OOOOOOO0O0O0 ='http://api.mengmorwpt1.cn/h5_share/user/up_profit_ratio'#line:218
            OOOO0O0OOO000OO0O ={"openid":0 }#line:219
            try :#line:220
                OOO0OOO00O00OO00O =OOO00000OO000OOOO .s .post (OOOO0OOOOOOO0O0O0 ,json =OOOO0O0OOO000OO0O ).json ()#line:221
                if OOO0OOO00O00OO00O .get ('code')==500 :#line:222
                    raise #line:223
                OOO00000OO000OOOO .msg +=f'代理升级：{OOO0OOO00O00OO00O.get("message")}\n'#line:224
            except :#line:225
                OOOO0OOOOOOO0O0O0 ='http://api.mengmorwpt1.cn/h5_share/user/task_reward'#line:226
                for OO0O0OO00O00OOO00 in range (0 ,8 ):#line:227
                    OOOO0O0OOO000OO0O ={"type":OO0O0OO00O00OOO00 ,"openid":0 }#line:228
                    OOO0OOO00O00OO00O =OOO00000OO000OOOO .s .post (OOOO0OOOOOOO0O0O0 ,json =OOOO0O0OOO000OO0O ).json ()#line:229
                    if '积分未满'in OOO0OOO00O00OO00O .get ('message'):#line:230
                        break #line:231
                    if OOO0OOO00O00OO00O .get ('code')!=500 :#line:232
                        OOO00000OO000OOOO .msg +='主页奖励积分：'+OOO0OOO00O00OO00O .get ('message')+'\n'#line:233
                    OO0O0OO00O00OOO00 +=1 #line:234
                    time .sleep (0.5 )#line:235
            return True #line:236
        else :#line:237
            OOO00000OO000OOOO .msg +='获取账号信息异常，检查cookie是否失效\n'#line:238
            printlog (f'{OOO00000OO000OOOO.name}:获取账号信息异常，检查cookie是否失效')#line:239
            if sendable :#line:240
                send (f'{OOO00000OO000OOOO.name} 每天赚获取账号信息异常，检查cookie是否失效','每天赚账号异常通知')#line:241
            if pushable :#line:242
                push (f'{OOO00000OO000OOOO.name} 每天赚获取账号信息异常，检查cookie是否失效','每天赚账号异常通知',uid =OOO00000OO000OOOO .uid )#line:243
            return False #line:244
    def get_read (O00O0OOO0OO0000O0 ):#line:246
        O00O00OOOOO0O0O00 ='http://api.mengmorwpt1.cn/h5_share/daily/get_read'#line:247
        OOO0000OOOO00O0OO ={"openid":0 }#line:248
        OO000O0OO000OO000 =0 #line:249
        while OO000O0OO000OO000 <10 :#line:250
            OO0000O0O0000O0OO =O00O0OOO0OO0000O0 .s .post (O00O00OOOOO0O0O00 ,json =OOO0000OOOO00O0OO ).json ()#line:251
            debugger (f'getread {OO0000O0O0000O0OO}')#line:252
            if OO0000O0O0000O0OO .get ('code')==200 :#line:253
                O00O0OOO0OO0000O0 .link =OO0000O0O0000O0OO .get ('data').get ('link')#line:254
                return True #line:255
            elif '获取失败'in OO0000O0O0000O0OO .get ('message'):#line:256
                time .sleep (15 )#line:257
                OO000O0OO000OO000 +=1 #line:258
                continue #line:259
            else :#line:260
                O00O0OOO0OO0000O0 .msg +=OO0000O0O0000O0OO .get ('message')+'\n'#line:261
                printlog (f'{O00O0OOO0OO0000O0.name}:{OO0000O0O0000O0OO.get("message")}')#line:262
                return False #line:263
    def gettaskinfo (O00O00OO00OOOO0O0 ,OOO00O0OOO0O0O0O0 ):#line:265
        for O0OOO000OO0O0O0OO in OOO00O0OOO0O0O0O0 :#line:266
            if O0OOO000OO0O0O0OO .get ('url'):#line:267
                return O0OOO000OO0O0O0OO #line:268
    def dotasks (O000OOOOOO0OO00O0 ):#line:270
        OO0OOO0OO0OOOO0O0 ={'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Origin':'http://nei594688.594688be.com.byymmmcm3.cn','Referer':'http://nei594688.594688be.com.byymmmcm3.cn/','Accept-Encoding':'gzip, deflate',}#line:277
        OOO0000OOO0OO0O00 =1 #line:278
        while True :#line:279
            OOOO0OO00O00OOOO0 ={"href":O000OOOOOO0OO00O0 .link }#line:280
            O00OO0O000O0OO0O0 ='https://api.wanjd.cn/wxread/articles/tasks'#line:281
            OO0OO000O0O00OO0O =requests .post (O00OO0O000O0OO0O0 ,headers =OO0OOO0OO0OOOO0O0 ,json =OOOO0OO00O00OOOO0 ).json ()#line:282
            OO0O0OO00O000OOO0 =OO0OO000O0O00OO0O .get ('data')#line:283
            debugger (f'tasks {OO0O0OO00O000OOO0}')#line:284
            OOO000OOO000000O0 =[O00O0OOO0000O00OO ['is_read']for O00O0OOO0000O00OO in OO0O0OO00O000OOO0 ]#line:285
            if 0 not in OOO000OOO000000O0 :#line:286
                break #line:287
            if OO0OO000O0O00OO0O .get ('code')!=200 :#line:288
                O000OOOOOO0OO00O0 .msg +=OO0OO000O0O00OO0O .get ('message')+'\n'#line:289
                printlog (f'{O000OOOOOO0OO00O0.name}:{OO0OO000O0O00OO0O.get("message")}')#line:290
                break #line:291
            else :#line:292
                OOO000O00OO0O0O0O =O000OOOOOO0OO00O0 .gettaskinfo (OO0OO000O0O00OO0O ['data'])#line:293
                if not OOO000O00OO0O0O0O :#line:294
                    break #line:295
                O00OO0OOOOOOOO0OO =OOO000O00OO0O0O0O .get ('url')#line:296
                printlog (f"{O000OOOOOO0OO00O0.name}:本轮任务数量 {len(OO0O0OO00O000OOO0)}")#line:297
                OOO0OOO0OOOOOO0O0 =OOO000O00OO0O0O0O ['id']#line:298
                debugger (OOO0OOO0OOOOOO0O0 )#line:299
                OOOO0OO00O00OOOO0 .update ({"id":OOO0OOO0OOOOOO0O0 })#line:300
                O00OO0OO0O0OO0OO0 =getmpinfo (O00OO0OOOOOOOO0OO )#line:301
                try :#line:302
                    O000OOOOOO0OO00O0 .msg +='正在阅读 '+O00OO0OO0O0OO0OO0 ['text']+'\n'#line:303
                    printlog (f'{O000OOOOOO0OO00O0.name}:正在阅读{O00OO0OO0O0OO0OO0["text"]}')#line:304
                except :#line:305
                    O000OOOOOO0OO00O0 .msg +='获取文章信息失败\n'#line:306
                    printlog (f'{O000OOOOOO0OO00O0.name}:获取文章信息失败')#line:307
                    break #line:308
                if len (str (OOO0OOO0OOOOOO0O0 ))<5 :#line:309
                    if OOO0000OOO0OO0O00 ==3 :#line:310
                        if sendable :#line:311
                            send ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',f'{O000OOOOOO0OO00O0.name} 美添赚检测',)#line:314
                        if pushable :#line:315
                            push ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',f'{O000OOOOOO0OO00O0.name} 美添赚检测',)#line:318
                        break #line:319
                    if sendable :#line:320
                        send (O00OO0OO0O0OO0OO0 .get ('text'),f'{O000OOOOOO0OO00O0.name} 美添赚过检测',O00OO0OOOOOOOO0OO )#line:321
                    if pushable :#line:322
                        push (f'{O000OOOOOO0OO00O0.name} 本轮任务数量{len(OO0O0OO00O000OOO0)-1}\n点击阅读检测文章\n{O00OO0OO0O0OO0OO0["text"]}',f'{O000OOOOOO0OO00O0.name} 美添赚过检测',O00OO0OOOOOOOO0OO ,uid =O000OOOOOO0OO00O0 .uid )#line:324
                    O000OOOOOO0OO00O0 .msg +='发送通知，暂停50秒\n'#line:325
                    printlog (f'{O000OOOOOO0OO00O0.name}:发送通知，暂停50秒')#line:326
                    OOO0000OOO0OO0O00 +=1 #line:327
                    time .sleep (50 )#line:328
                OOOOOOOOOO0O00O00 =random .randint (7 ,10 )#line:329
                time .sleep (OOOOOOOOOO0O00O00 )#line:330
                O00OO0O000O0OO0O0 ='https://api.wanjd.cn/wxread/articles/three_read'#line:331
                OO0OO000O0O00OO0O =requests .post (O00OO0O000O0OO0O0 ,headers =OO0OOO0OO0OOOO0O0 ,json =OOOO0OO00O00OOOO0 ).json ()#line:332
                if OO0OO000O0O00OO0O .get ('code')==200 :#line:333
                    O000OOOOOO0OO00O0 .msg +='阅读成功'+'\n'+'-'*50 +'\n'#line:334
                    printlog (f'{O000OOOOOO0OO00O0.name}:阅读成功')#line:335
                if OO0OO000O0O00OO0O .get ('code')!=200 :#line:336
                    O000OOOOOO0OO00O0 .msg +=OO0OO000O0O00OO0O .get ('message')+'\n'+'-'*50 +'\n'#line:337
                    printlog (f'{O000OOOOOO0OO00O0.name}:{OO0OO000O0O00OO0O.get("message")}')#line:338
                    break #line:339
        O00OO0O000O0OO0O0 ='https://api.wanjd.cn/wxread/articles/check_success'#line:340
        OOOO0OO00O00OOOO0 ={'type':1 ,'href':O000OOOOOO0OO00O0 .link }#line:341
        OO0OO000O0O00OO0O =requests .post (O00OO0O000O0OO0O0 ,headers =OO0OOO0OO0OOOO0O0 ,json =OOOO0OO00O00OOOO0 ).json ()#line:342
        debugger (f'check {OO0OO000O0O00OO0O}')#line:343
        O000OOOOOO0OO00O0 .msg +=OO0OO000O0O00OO0O .get ('message')+'\n'#line:344
        printlog (f'{O000OOOOOO0OO00O0.name}:{OO0OO000O0O00OO0O.get("message")}')#line:345
    def withdraw (OO0O000000OO0O0OO ):#line:347
        if OO0O000000OO0O0OO .points <txbz :#line:348
            OO0O000000OO0O0OO .msg +=f'没有达到你设置的提现标准{txbz}\n'#line:349
            printlog (f'{OO0O000000OO0O0OO.name}:没有达到你设置的提现标准{txbz}')#line:350
            return False #line:351
        OO000000O0O0O0OO0 ='http://api.mengmorwpt1.cn/h5_share/user/withdraw'#line:352
        OO0OO000O0OOO0OO0 =OO0O000000OO0O0OO .s .post (OO000000O0O0O0OO0 ).json ()#line:353
        OO0O000000OO0O0OO .msg +='提现结果'+OO0OO000O0OOO0OO0 .get ('message')+'\n'#line:354
        printlog (f'{OO0O000000OO0O0OO.name}:提现结果 {OO0OO000O0OOO0OO0.get("message")}')#line:355
        if OO0OO000O0OOO0OO0 .get ('code')==200 :#line:356
            if sendable :#line:357
                send (f'{OO0O000000OO0O0OO.name} 已提现到红包，请在服务通知内及时领取','每天赚提现通知')#line:358
            if pushable :#line:359
                push (f'{OO0O000000OO0O0OO.name} 已提现到红包，请在服务通知内及时领取','每天赚提现通知',uid =OO0O000000OO0O0OO .uid )#line:360
    def run (O0OOO0OOO00OO0O0O ):#line:362
        O0OOO0OOO00OO0O0O .msg +='*'*50 +f'\n账号：{O0OOO0OOO00OO0O0O.name}开始任务\n'#line:363
        printlog (f'账号：{O0OOO0OOO00OO0O0O.name}开始任务')#line:364
        if not O0OOO0OOO00OO0O0O .user_info ():#line:365
            return False #line:366
        if O0OOO0OOO00OO0O0O .get_read ():#line:367
            O0OOO0OOO00OO0O0O .dotasks ()#line:368
            O0OOO0OOO00OO0O0O .user_info ()#line:369
        O0OOO0OOO00OO0O0O .withdraw ()#line:370
        printlog (f'账号：{O0OOO0OOO00OO0O0O.name}:任务结束')#line:371
        if not printf :#line:372
            print (O0OOO0OOO00OO0O0O .msg .strip ())#line:373
            print (f'账号：{O0OOO0OOO00OO0O0O.name}任务结束')#line:374
def yd (OOOO0OO00O0O0OO0O ):#line:377
    while not OOOO0OO00O0O0OO0O .empty ():#line:378
        O000000OOOO0OO000 =OOOO0OO00O0O0OO0O .get ()#line:379
        O0O00O00OOOOOOO0O =MTZYD (O000000OOOO0OO000 )#line:380
        O0O00O00OOOOOOO0O .run ()#line:381
def get_info ():#line:384
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:386
    print ('入口：http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552')#line:387
    OO00O00OOOO0O0000 ='V2.1'#line:388
    OOOOOO00OO0O00000 =_O0OO0O00O0OOO0OOO ['version']['k_mtz']#line:389
    print (f'当前版本{OO00O00OOOO0O0000}，仓库版本{OOOOOO00OO0O00000}')#line:390
    if OO00O00OOOO0O0000 <OOOOOO00OO0O00000 :#line:391
        print ('请到仓库下载最新版本k_mtz.py')#line:392
    print ("="*25 )#line:393
def main ():#line:396
    get_info ()#line:397
    O00O00O00OO0O00O0 =os .getenv ('mtzv2ck')#line:398
    if not O00O00O00OO0O00O0 :#line:399
        print (_O0OO0O00O0OOO0OOO .get ('msg')['每天赚'])#line:400
        exit ()#line:401
    O00O00O00OO0O00O0 =O00O00O00OO0O00O0 .split ('&')#line:402
    O000O00OO0O0O0000 =Queue ()#line:403
    O000000O00O0O0O0O =[]#line:404
    for OO00O0O00OOOOO00O ,OOOO0OOOOOOOO0OOO in enumerate (O00O00O00OO0O00O0 ,start =1 ):#line:405
        O000O00OO0O0O0000 .put (OOOO0OOOOOOOO0OOO )#line:406
    for OO00O0O00OOOOO00O in range (max_workers ):#line:407
        O0OOOO00000OOO00O =threading .Thread (target =yd ,args =(O000O00OO0O0O0000 ,))#line:408
        O0OOOO00000OOO00O .start ()#line:409
        O000000O00O0O0O0O .append (O0OOOO00000OOO00O )#line:410
        time .sleep (20 )#line:411
    for O00OOOOO0O00O0O00 in O000000O00O0O0O0O :#line:412
        O00OOOOO0O00O0O00 .join ()#line:413
if __name__ =='__main__':#line:416
    main ()#line:417
