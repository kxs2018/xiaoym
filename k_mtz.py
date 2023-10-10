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
import json #line:40
import os #line:41
import random #line:42
import requests #line:43
import re #line:44
import time #line:45
import ast #line:46
def get_msg ():#line:49
    O0OO00O000000O0O0 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:51
    O0OO0OO0OOO000O0O =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O0OO00O000000O0O0 ).json ()#line:52
    return O0OO0OO0OOO000O0O #line:53
_OOO0OOOO0000OOO0O =get_msg ()#line:56
try :#line:57
    from lxml import etree #line:58
except :#line:59
    print (_OOO0OOOO0000OOO0O .get ('help')['lxml'])#line:60
    exit ()#line:61
import datetime #line:63
import threading #line:64
from queue import Queue #line:65
if sendable :#line:67
    qwbotkey =os .getenv ('qwbotkey')#line:68
    if not qwbotkey :#line:69
        print (_OOO0OOOO0000OOO0O .get ('help')['qwbotkey'])#line:70
        exit ()#line:71
if pushable :#line:73
    pushconfig =os .getenv ('pushconfig')#line:74
    if not pushconfig :#line:75
        print (_OOO0OOOO0000OOO0O .get ('help')['pushconfig'])#line:76
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
            print (_OOO0OOOO0000OOO0O .get ('help')['pushconfig'])#line:93
            exit ()#line:94
def ftime ():#line:97
    O0O000O00O000OOOO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:98
    return O0O000O00O000OOOO #line:99
def debugger (OOOO00OOOO0000OO0 ):#line:102
    if debug :#line:103
        print (OOOO00OOOO0000OO0 )#line:104
def printlog (OO0OO0000O0O0OOOO ):#line:107
    if printf :#line:108
        print (OO0OO0000O0O0OOOO )#line:109
def send (OO0O0O0000OOO000O ,title ='通知',url =None ):#line:112
    if not url :#line:113
        OO00000O0000000O0 ={"msgtype":"text","text":{"content":f"{title}\n\n{OO0O0O0000OOO000O}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:120
    else :#line:121
        OO00000O0000000O0 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":OO0O0O0000OOO000O ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:126
    O00O000O00O0O0000 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:127
    O0OO000O0OOOOO0O0 =requests .post (O00O000O00O0O0000 ,data =json .dumps (OO00000O0000000O0 )).json ()#line:128
    if O0OO000O0OOOOO0O0 .get ('errcode')!=0 :#line:129
        print ('消息发送失败，请检查key和发送格式')#line:130
        return False #line:131
    return O0OO000O0OOOOO0O0 #line:132
def push (O0OO000OOO00O0000 ,OOO00O0O00OO0OO00 ,url ='',uid =None ):#line:135
    if uid :#line:136
        uids .append (uid )#line:137
    O0OOOOOO0O00O00OO ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',O0OO000OOO00O0000 ).replace ('url',url )#line:139
    OO0O0O00O0O0000O0 ={"appToken":appToken ,"content":O0OOOOOO0O00O00OO ,"summary":OOO00O0O00OO0OO00 ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:149
    O00000OO0O0OO0O0O ='http://wxpusher.zjiecode.com/api/send/message'#line:150
    OOO00000OO0OOO000 =requests .post (url =O00000OO0O0OO0O0O ,json =OO0O0O00O0O0000O0 ).json ()#line:151
    if OOO00000OO0OOO000 .get ('code')!=1000 :#line:152
        print (OOO00000OO0OOO000 .get ('msg'),OOO00000OO0OOO000 )#line:153
    return OOO00000OO0OOO000 #line:154
def getmpinfo (OOOOO0OO0O00000OO ):#line:157
    if not OOOOO0OO0O00000OO or OOOOO0OO0O00000OO =='':#line:158
        return False #line:159
    OOO00O000O0O0O0OO ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:161
    OOO0O0OOO0O0O0OOO =requests .get (OOOOO0OO0O00000OO ,headers =OOO00O000O0O0O0OO )#line:162
    O0OO00O000O0O0O00 =etree .HTML (OOO0O0OOO0O0O0OOO .text )#line:163
    O0OOO0O00OOO0OO00 =O0OO00O000O0O0O00 .xpath ('//meta[@*="og:title"]/@content')#line:164
    if O0OOO0O00OOO0OO00 :#line:165
        O0OOO0O00OOO0OO00 =O0OOO0O00OOO0OO00 [0 ]#line:166
    try :#line:167
        if 'biz='in OOOOO0OO0O00000OO :#line:168
            O0O00OO000O000O0O =re .findall (r'biz=(.*?)&',OOOOO0OO0O00000OO )[0 ]#line:169
        else :#line:170
            OOOOO0OOO00O0OOO0 =O0OO00O000O0O0O00 .xpath ('//meta[@*="og:url"]/@content')[0 ]#line:171
            O0O00OO000O000O0O =re .findall (r'biz=(.*?)&',str (OOOOO0OOO00O0OOO0 ))[0 ]#line:172
    except :#line:173
        return False #line:174
    OOOO0OO0OOO000O00 =O0OO00O000O0O0O00 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:175
    if OOOO0OO0OOO000O00 :#line:176
        OOOO0OO0OOO000O00 =OOOO0OO0OOO000O00 [0 ].strip ()#line:177
    O000O0O00000O0O0O =re .findall (r"user_name.DATA'\) : '(.*?)'",OOO0O0OOO0O0O0OOO .text )or O0OO00O000O0O0O00 .xpath ('//span[@class="profile_meta_value"]/text()')#line:179
    if O000O0O00000O0O0O :#line:180
        O000O0O00000O0O0O =O000O0O00000O0O0O [0 ]#line:181
    OOOOOOOOO000OOO00 =re .findall (r'createTime = \'(.*)\'',OOO0O0OOO0O0O0OOO .text )#line:182
    if OOOOOOOOO000OOO00 :#line:183
        OOOOOOOOO000OOO00 =OOOOOOOOO000OOO00 [0 ][5 :]#line:184
    O0OOOOOOOO00OO000 =f'{OOOOOOOOO000OOO00}|{O0OOO0O00OOO0OO00}|{O0O00OO000O000O0O}|{OOOO0OO0OOO000O00}|{O000O0O00000O0O0O}'#line:185
    O0OO0O0000O000O0O ={'biz':O0O00OO000O000O0O ,'text':O0OOOOOOOO00OO000 }#line:186
    return O0OO0O0000O000O0O #line:187
class MTZYD :#line:190
    def __init__ (OOO0000O00O0O0O0O ,OOOO0000OOO00O00O ):#line:191
        OOOO0000OOO00O00O =OOOO0000OOO00O00O .split (';')#line:192
        if ''in OOOO0000OOO00O00O :#line:193
            OOOO0000OOO00O00O .pop ('')#line:194
        OOO0000O00O0O0O0O .name =OOOO0000OOO00O00O [0 ].split ('=')[1 ]#line:195
        OOO0000O00O0O0O0O .uid =OOOO0000OOO00O00O [2 ].split ('=')[1 ]if len (OOOO0000OOO00O00O )==3 else None #line:196
        OOO0000O00O0O0O0O .ck =OOOO0000OOO00O00O [1 ].split ('=')[1 ]#line:197
        OOO0000O00O0O0O0O .s =requests .session ()#line:198
        OOO0000O00O0O0O0O .s .headers ={'Authorization':OOO0000O00O0O0O0O .ck ,'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5279 MMWEBSDK/20230805 MMWEBID/2833 MicroMessenger/8.0.42.2460(0x28002A3B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Accept':'*/*','Origin':'http://61695315208.tt.bendishenghuochwl1.cn','Referer':'http://61695315208.tt.bendishenghuochwl1.cn/','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh',}#line:208
        OOO0000O00O0O0O0O .msg =''#line:209
    def user_info (O00000O0OO00O0OOO ):#line:211
        O0OOOOO0OOO000O00 ='http://api.mengmorwpt1.cn/h5_share/user/info'#line:212
        O00O00OOOOO0O0OOO =O00000O0OO00O0OOO .s .post (O0OOOOO0OOO000O00 ,json ={"openid":0 }).json ()#line:213
        debugger (f'userinfo {O00O00OOOOO0O0OOO}')#line:214
        if O00O00OOOOO0O0OOO .get ('code')==200 :#line:215
            O0OOO0O00O0O00000 =O00O00OOOOO0O0OOO .get ('data').get ('nickname')#line:216
            O00000O0OO00O0OOO .points =O00O00OOOOO0O0OOO .get ('data').get ('points')-O00O00OOOOO0O0OOO .get ('data').get ('withdraw_points')#line:217
            O00O00OOOOO0O0OOO =O00000O0OO00O0OOO .s .post ('http://api.mengmorwpt1.cn/h5_share/user/sign',json ={"openid":0 })#line:218
            debugger (f'签到 {O00O00OOOOO0O0OOO.json()}')#line:219
            OOO0O000O0O0OOOO0 =O00O00OOOOO0O0OOO .json ().get ('message')#line:220
            O00000O0OO00O0OOO .msg +=f'\n{O00000O0OO00O0OOO.name}:{O0OOO0O00O0O00000},现有积分：{O00000O0OO00O0OOO.points}，{OOO0O000O0O0OOOO0}\n'+'-'*50 +'\n'#line:221
            printlog (f'{O00000O0OO00O0OOO.name}:现有积分：{O00000O0OO00O0OOO.points}，{OOO0O000O0O0OOOO0}')#line:222
            O0OOOOO0OOO000O00 ='http://api.mengmorwpt1.cn/h5_share/user/up_profit_ratio'#line:223
            O00OOO0O0OO000000 ={"openid":0 }#line:224
            try :#line:225
                O00O00OOOOO0O0OOO =O00000O0OO00O0OOO .s .post (O0OOOOO0OOO000O00 ,json =O00OOO0O0OO000000 ).json ()#line:226
                if O00O00OOOOO0O0OOO .get ('code')==500 :#line:227
                    raise #line:228
                O00000O0OO00O0OOO .msg +=f'代理升级：{O00O00OOOOO0O0OOO.get("message")}\n'#line:229
                printlog (f'代理升级：{O00O00OOOOO0O0OOO.get("message")}\n')#line:230
            except :#line:231
                O0OOOOO0OOO000O00 ='http://api.mengmorwpt1.cn/h5_share/user/task_reward'#line:232
                for O000O000OO0O00OO0 in range (0 ,8 ):#line:233
                    O00OOO0O0OO000000 ={"type":O000O000OO0O00OO0 ,"openid":0 }#line:234
                    O00O00OOOOO0O0OOO =O00000O0OO00O0OOO .s .post (O0OOOOO0OOO000O00 ,json =O00OOO0O0OO000000 ).json ()#line:235
                    if '积分未满'in O00O00OOOOO0O0OOO .get ('message'):#line:236
                        break #line:237
                    if O00O00OOOOO0O0OOO .get ('code')!=500 :#line:238
                        O00000O0OO00O0OOO .msg +='主页奖励积分：'+O00O00OOOOO0O0OOO .get ('message')+'\n'#line:239
                        printlog (f'{O00000O0OO00O0OOO.name}:主页奖励积分 {O00O00OOOOO0O0OOO.get("message")}')#line:240
                    O000O000OO0O00OO0 +=1 #line:241
                    time .sleep (0.5 )#line:242
            return True #line:243
        else :#line:244
            O00000O0OO00O0OOO .msg +='获取账号信息异常，检查cookie是否失效\n'#line:245
            printlog (f'{O00000O0OO00O0OOO.name}:获取账号信息异常，检查cookie是否失效')#line:246
            if sendable :#line:247
                send (f'{O00000O0OO00O0OOO.name} 每天赚获取账号信息异常，检查cookie是否失效','每天赚账号异常通知')#line:248
            if pushable :#line:249
                push (f'{O00000O0OO00O0OOO.name} 每天赚获取账号信息异常，检查cookie是否失效','每天赚账号异常通知','http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552',O00000O0OO00O0OOO .uid )#line:251
            return False #line:252
    def get_read (O0000O0OOO0000O00 ):#line:254
        O00OOO000OO0OOOOO ='http://api.mengmorwpt1.cn/h5_share/daily/get_read'#line:255
        OOOOO00OOO00OOOOO ={"openid":0 }#line:256
        O0O00OOOO0OOOOO0O =0 #line:257
        while O0O00OOOO0OOOOO0O <10 :#line:258
            O000O00O0O0OOO0O0 =O0000O0OOO0000O00 .s .post (O00OOO000OO0OOOOO ,json =OOOOO00OOO00OOOOO ).json ()#line:259
            debugger (f'getread {O000O00O0O0OOO0O0}')#line:260
            if O000O00O0O0OOO0O0 .get ('code')==200 :#line:261
                O0000O0OOO0000O00 .link =O000O00O0O0OOO0O0 .get ('data').get ('link')#line:262
                return True #line:263
            elif '获取失败'in O000O00O0O0OOO0O0 .get ('message'):#line:264
                time .sleep (15 )#line:265
                O0O00OOOO0OOOOO0O +=1 #line:266
                continue #line:267
            else :#line:268
                O0000O0OOO0000O00 .msg +=O000O00O0O0OOO0O0 .get ('message')+'\n'#line:269
                printlog (f'{O0000O0OOO0000O00.name}:{O000O00O0O0OOO0O0.get("message")}')#line:270
                return False #line:271
    def gettaskinfo (OOOO00O00OO00OO00 ,O0O00OOO0OO00000O ):#line:273
        for OO0OOOOOOO00O0000 in O0O00OOO0OO00000O :#line:274
            if OO0OOOOOOO00O0000 .get ('url'):#line:275
                return OO0OOOOOOO00O0000 #line:276
    def dotasks (O0O0OOOO000OO0O00 ):#line:278
        OO0O0000OOO00O0O0 ={'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Origin':'http://nei594688.594688be.com.byymmmcm3.cn','Referer':'http://nei594688.594688be.com.byymmmcm3.cn/','Accept-Encoding':'gzip, deflate',}#line:285
        OO0000OOO00OO0O00 =0 #line:286
        while True :#line:287
            O0O000OOOOOO000OO ={"href":O0O0OOOO000OO0O00 .link }#line:288
            O0000O00OOO0000O0 ='https://api.wanjd.cn/wxread/articles/tasks'#line:289
            OOOOOO0O0OOOO0000 =requests .post (O0000O00OOO0000O0 ,headers =OO0O0000OOO00O0O0 ,json =O0O000OOOOOO000OO ).json ()#line:290
            O0OOO000OOOO00000 =OOOOOO0O0OOOO0000 .get ('data')#line:291
            debugger (f'tasks {O0OOO000OOOO00000}')#line:292
            OO0OO0OO00OOOOO0O =[OOOO0O000O00OOO00 ['is_read']for OOOO0O000O00OOO00 in O0OOO000OOOO00000 ]#line:293
            if 0 not in OO0OO0OO00OOOOO0O :#line:294
                break #line:295
            if OOOOOO0O0OOOO0000 .get ('code')!=200 :#line:296
                O0O0OOOO000OO0O00 .msg +=OOOOOO0O0OOOO0000 .get ('message')+'\n'#line:297
                printlog (f'{O0O0OOOO000OO0O00.name}:{OOOOOO0O0OOOO0000.get("message")}')#line:298
                break #line:299
            else :#line:300
                O000O00OOOO0OOO0O =O0O0OOOO000OO0O00 .gettaskinfo (OOOOOO0O0OOOO0000 ['data'])#line:301
                if not O000O00OOOO0OOO0O :#line:302
                    break #line:303
                OOO0OO0OOO0OO00OO =O000O00OOOO0OOO0O .get ('url')#line:304
                if len (O0OOO000OOOO00000 )<total_num :#line:305
                    printlog (f'{O0O0OOOO000OO0O00.name}:任务数量小于{total_num}，任务中止')#line:306
                    break #line:307
                OOO0OOOOO0000OO00 =O000O00OOOO0OOO0O ['id']#line:308
                debugger (OOO0OOOOO0000OO00 )#line:309
                O0O000OOOOOO000OO .update ({"id":OOO0OOOOO0000OO00 })#line:310
                O0O000O0O0O0OOOOO =getmpinfo (OOO0OO0OOO0OO00OO )#line:311
                try :#line:312
                    O0O0OOOO000OO0O00 .msg +='正在阅读 '+O0O000O0O0O0OOOOO ['text']+'\n'#line:313
                    printlog (f'{O0O0OOOO000OO0O00.name}:正在阅读{O0O000O0O0O0OOOOO["text"]}')#line:314
                except :#line:315
                    O0O0OOOO000OO0O00 .msg +='获取文章信息失败\n'#line:316
                    printlog (f'{O0O0OOOO000OO0O00.name}:获取文章信息失败')#line:317
                    break #line:318
                if len (str (OOO0OOOOO0000OO00 ))<5 :#line:319
                    if OO0000OOO00OO0O00 ==3 :#line:320
                        if sendable :#line:321
                            send ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',f'{O0O0OOOO000OO0O00.name} 美添赚检测',)#line:324
                        if pushable :#line:325
                            push ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',f'{O0O0OOOO000OO0O00.name} 美添赚检测',)#line:328
                        break #line:329
                    if sendable :#line:330
                        send (O0O000O0O0O0OOOOO .get ('text'),f'{O0O0OOOO000OO0O00.name} 美添赚过检测',OOO0OO0OOO0OO00OO )#line:331
                    if pushable :#line:332
                        push (f'{O0O0OOOO000OO0O00.name} 本轮任务数量{len(O0OOO000OOOO00000) - 1}\n点击阅读检测文章\n{O0O000O0O0O0OOOOO["text"]}',f'{O0O0OOOO000OO0O00.name} 美添赚过检测',OOO0OO0OOO0OO00OO ,O0O0OOOO000OO0O00 .uid )#line:335
                    O0O0OOOO000OO0O00 .msg +='发送通知，暂停50秒\n'#line:336
                    printlog (f'{O0O0OOOO000OO0O00.name}:发送通知，暂停50秒')#line:337
                    OO0000OOO00OO0O00 +=1 #line:338
                    time .sleep (50 )#line:339
                O000OOOOO0O00OOO0 =random .randint (7 ,10 )#line:340
                time .sleep (O000OOOOO0O00OOO0 )#line:341
                O0000O00OOO0000O0 ='https://api.wanjd.cn/wxread/articles/three_read'#line:342
                OOOOOO0O0OOOO0000 =requests .post (O0000O00OOO0000O0 ,headers =OO0O0000OOO00O0O0 ,json =O0O000OOOOOO000OO ).json ()#line:343
                if OOOOOO0O0OOOO0000 .get ('code')==200 :#line:344
                    O0O0OOOO000OO0O00 .msg +='阅读成功'+'\n'+'-'*50 +'\n'#line:345
                    printlog (f'{O0O0OOOO000OO0O00.name}:阅读成功')#line:346
                if OOOOOO0O0OOOO0000 .get ('code')!=200 :#line:347
                    O0O0OOOO000OO0O00 .msg +=OOOOOO0O0OOOO0000 .get ('message')+'\n'+'-'*50 +'\n'#line:348
                    printlog (f'{O0O0OOOO000OO0O00.name}:{OOOOOO0O0OOOO0000.get("message")}')#line:349
                    break #line:350
        O0000O00OOO0000O0 ='https://api.wanjd.cn/wxread/articles/check_success'#line:351
        O0O000OOOOOO000OO ={'type':1 ,'href':O0O0OOOO000OO0O00 .link }#line:352
        OOOOOO0O0OOOO0000 =requests .post (O0000O00OOO0000O0 ,headers =OO0O0000OOO00O0O0 ,json =O0O000OOOOOO000OO ).json ()#line:353
        debugger (f'check {OOOOOO0O0OOOO0000}')#line:354
        O0O0OOOO000OO0O00 .msg +=OOOOOO0O0OOOO0000 .get ('message')+'\n'#line:355
        printlog (f'{O0O0OOOO000OO0O00.name}:{OOOOOO0O0OOOO0000.get("message")}')#line:356
    def withdraw (O00O00OOOOOO0OOO0 ):#line:358
        if O00O00OOOOOO0OOO0 .points <txbz :#line:359
            O00O00OOOOOO0OOO0 .msg +=f'没有达到你设置的提现标准{txbz}\n'#line:360
            printlog (f'{O00O00OOOOOO0OOO0.name}:没有达到你设置的提现标准{txbz}')#line:361
            return False #line:362
        OOO000O0O000O000O ='http://api.mengmorwpt1.cn/h5_share/user/withdraw'#line:363
        OO00OO000000O0OO0 =O00O00OOOOOO0OOO0 .s .post (OOO000O0O000O000O ).json ()#line:364
        O00O00OOOOOO0OOO0 .msg +='提现结果'+OO00OO000000O0OO0 .get ('message')+'\n'#line:365
        printlog (f'{O00O00OOOOOO0OOO0.name}:提现结果 {OO00OO000000O0OO0.get("message")}')#line:366
        if OO00OO000000O0OO0 .get ('code')==200 :#line:367
            if sendable :#line:368
                send (f'{O00O00OOOOOO0OOO0.name}:已提现到红包，请在服务通知内及时领取','每天赚提现通知')#line:369
            if pushable :#line:370
                push (f'{O00O00OOOOOO0OOO0.name}:已提现到红包，请在服务通知内及时领取','每天赚提现通知','https://jihulab.com/xizhiai/xiaoym',O00O00OOOOOO0OOO0 .uid )#line:372
    def run (OOO0OOOO00O000O0O ):#line:374
        OOO0OOOO00O000O0O .msg +='*'*50 +f'\n{OOO0OOOO00O000O0O.name}:开始任务\n'#line:375
        printlog (f'{OOO0OOOO00O000O0O.name}:开始任务')#line:376
        if not OOO0OOOO00O000O0O .user_info ():#line:377
            return False #line:378
        if OOO0OOOO00O000O0O .get_read ():#line:379
            OOO0OOOO00O000O0O .dotasks ()#line:380
            OOO0OOOO00O000O0O .user_info ()#line:381
        OOO0OOOO00O000O0O .withdraw ()#line:382
        printlog (f'{OOO0OOOO00O000O0O.name}:任务结束')#line:383
        if not printf :#line:384
            print (OOO0OOOO00O000O0O .msg .strip ())#line:385
            print (f'{OOO0OOOO00O000O0O.name}:任务结束')#line:386
def yd (O0000O00O00OO0O00 ):#line:389
    while not O0000O00O00OO0O00 .empty ():#line:390
        O0OO00OOO0OOOOO0O =O0000O00O00OO0O00 .get ()#line:391
        O00OO00O00O0OO00O =MTZYD (O0OO00OOO0OOOOO0O )#line:392
        O00OO00O00O0OO00O .run ()#line:393
def get_info ():#line:396
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:398
    print ('入口：http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552')#line:399
    OOOOOOOO000OOO0O0 ='V2.2'#line:400
    O0OOO000O00OOO000 =_OOO0OOOO0000OOO0O ['version']['k_mtz']#line:401
    print (f'当前版本{OOOOOOOO000OOO0O0}，仓库版本{O0OOO000O00OOO000}\n{_OOO0OOOO0000OOO0O["update_log"]["每天赚"]}')#line:402
    if OOOOOOOO000OOO0O0 <O0OOO000O00OOO000 :#line:403
        print ('请到仓库下载最新版本k_mtz.py')#line:404
    print ("="*25 )#line:405
def main ():#line:408
    get_info ()#line:409
    OOOOO0O0OO00O000O =os .getenv ('mtzv2ck')#line:410
    if not OOOOO0O0OO00O000O :#line:411
        print (_OOO0OOOO0000OOO0O .get ('msg')['每天赚'])#line:412
        exit ()#line:413
    OOOOO0O0OO00O000O =OOOOO0O0OO00O000O .split ('&')#line:414
    OO0OOOOOOOOOOO0OO =Queue ()#line:415
    OO0OO0O000O00O0O0 =[]#line:416
    for O0O0OOOO0000OO0OO ,O0000OO000O00O0O0 in enumerate (OOOOO0O0OO00O000O ,start =1 ):#line:417
        OO0OOOOOOOOOOO0OO .put (O0000OO000O00O0O0 )#line:418
    for O0O0OOOO0000OO0OO in range (max_workers ):#line:419
        OOOOO0O00O0O000O0 =threading .Thread (target =yd ,args =(OO0OOOOOOOOOOO0OO ,))#line:420
        OOOOO0O00O0O000O0 .start ()#line:421
        OO0OO0O000O00O0O0 .append (OOOOO0O00O0O000O0 )#line:422
        time .sleep (delay_time )#line:423
    for O000OO0000OO0OO0O in OO0OO0O000O00O0O0 :#line:424
        O000OO0000OO0OO0O .join ()#line:425
if __name__ =='__main__':#line:428
    main ()#line:429
