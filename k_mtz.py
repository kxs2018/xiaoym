# -*- coding: utf-8 -*-
# k_mtz
# Author: 惜之酱
"""
先运行脚本，有问题到群里问 http://t.me/xizhiaigroup
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

import json #line:41
import os #line:42
import random #line:43
import requests #line:44
import re #line:45
import time #line:46
import ast #line:47
import datetime #line:48
import threading #line:49
from queue import Queue #line:50

def get_msg ():#line:53
    OOOO0000O0O0OOOO0 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:55
    O00OO0OO00000OOO0 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OOOO0000O0O0OOOO0 ).json ()#line:56
    return O00OO0OO00000OOO0 #line:57
_O0O00OO00O0000O0O =get_msg ()#line:60
try :#line:61
    from lxml import etree #line:62
except :#line:63
    print (_O0O00OO00O0000O0O .get ('help')['lxml'])#line:64
if sendable :#line:66
    qwbotkey =os .getenv ('qwbotkey')#line:67
    if not qwbotkey :#line:68
        print (_O0O00OO00O0000O0O .get ('help')['qwbotkey'])#line:69
        exit ()#line:70
if pushable :#line:72
    pushconfig =os .getenv ('pushconfig')#line:73
    if not pushconfig :#line:74
        print (_O0O00OO00O0000O0O .get ('help')['pushconfig'])#line:75
        exit ()#line:76
    try :#line:77
        pushconfig =ast .literal_eval (pushconfig )#line:78
    except :#line:79
        pass #line:80
    if isinstance (pushconfig ,dict ):#line:81
        appToken =pushconfig ['appToken']#line:82
        uids =pushconfig ['uids']#line:83
        topicids =pushconfig ['topicids']#line:84
    else :#line:85
        try :#line:86
            "appToken=AT_pCenRjs;uids=['UID_9MZ','UID_T4xlqWx9x'];topicids=['xxx']"#line:87
            appToken =pushconfig .split (';')[0 ].split ('=')[1 ]#line:88
            uids =ast .literal_eval (pushconfig .split (';')[1 ].split ('=')[1 ])#line:89
            topicids =ast .literal_eval (pushconfig .split (';')[2 ].split ('=')[1 ])#line:90
        except :#line:91
            print (_O0O00OO00O0000O0O .get ('help')['pushconfig'])#line:92
            exit ()#line:93
if not pushable and not sendable :#line:94
    print ('啥通知方式都不配置，你想上天吗')#line:95
    exit ()#line:96
def ftime ():#line:98
    O0O0000000O000O00 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:99
    return O0O0000000O000O00 #line:100
def debugger (OO00OO0OOOO00O000 ):#line:103
    if debug :#line:104
        print (OO00OO0OOOO00O000 )#line:105
def printlog (O0O0OO0O0O0OO0O0O ):#line:108
    if printf :#line:109
        print (O0O0OO0O0O0OO0O0O )#line:110
def send (O000OO000O0O0OO00 ,title ='通知',url =None ):#line:113
    if not url :#line:114
        O0OOO00O000OOO0OO ={"msgtype":"text","text":{"content":f"{title}\n\n{O000OO000O0O0OO00}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:121
    else :#line:122
        O0OOO00O000OOO0OO ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O000OO000O0O0OO00 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:127
    OOOO0O0O0OOO0O000 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:128
    O0O000O0OO00OOO0O =requests .post (OOOO0O0O0OOO0O000 ,data =json .dumps (O0OOO00O000OOO0OO )).json ()#line:129
    if O0O000O0OO00OOO0O .get ('errcode')!=0 :#line:130
        print ('消息发送失败，请检查key和发送格式')#line:131
        return False #line:132
    return O0O000O0OO00OOO0O #line:133
def push (OO00O0OOOOOO0OOO0 ,O00O000OOOO0O0000 ,url ='',uid =None ):#line:136
    if uid :#line:137
        uids .append (uid )#line:138
    O0000OOO0O000OO0O ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',OO00O0OOOOOO0OOO0 ).replace ('url',url )#line:140
    OO000000OOO0OOO00 ={"appToken":appToken ,"content":O0000OOO0O000OO0O ,"summary":O00O000OOOO0O0000 ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:150
    OO0O0OOO0O0000O00 ='http://wxpusher.zjiecode.com/api/send/message'#line:151
    OO0000OO00000000O =requests .post (url =OO0O0OOO0O0000O00 ,json =OO000000OOO0OOO00 ).json ()#line:152
    if OO0000OO00000000O .get ('code')!=1000 :#line:153
        print (OO0000OO00000000O .get ('msg'),OO0000OO00000000O )#line:154
    return OO0000OO00000000O #line:155
def getmpinfo (O0OO0O0OOOOOO00O0 ):#line:158
    if not O0OO0O0OOOOOO00O0 or O0OO0O0OOOOOO00O0 =='':#line:159
        return False #line:160
    O0O0O00O0000000O0 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:162
    O00O00O0OOOO000OO =requests .get (O0OO0O0OOOOOO00O0 ,headers =O0O0O00O0000000O0 )#line:163
    O0O00O00O000000O0 =etree .HTML (O00O00O0OOOO000OO .text )#line:164
    O00OOOOO00O00000O =O0O00O00O000000O0 .xpath ('//meta[@*="og:title"]/@content')#line:165
    if O00OOOOO00O00000O :#line:166
        O00OOOOO00O00000O =O00OOOOO00O00000O [0 ]#line:167
    try :#line:168
        if 'biz='in O0OO0O0OOOOOO00O0 :#line:169
            O00OO0O000O00OOOO =re .findall (r'biz=(.*?)&',O0OO0O0OOOOOO00O0 )[0 ]#line:170
        else :#line:171
            OO000000OO00O0OO0 =O0O00O00O000000O0 .xpath ('//meta[@*="og:url"]/@content')[0 ]#line:172
            O00OO0O000O00OOOO =re .findall (r'biz=(.*?)&',str (OO000000OO00O0OO0 ))[0 ]#line:173
    except :#line:174
        return False #line:175
    OOOO0000OO0000O0O =O0O00O00O000000O0 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:176
    if OOOO0000OO0000O0O :#line:177
        OOOO0000OO0000O0O =OOOO0000OO0000O0O [0 ].strip ()#line:178
    OOO000OO00000O0OO =re .findall (r"user_name.DATA'\) : '(.*?)'",O00O00O0OOOO000OO .text )or O0O00O00O000000O0 .xpath ('//span[@class="profile_meta_value"]/text()')#line:180
    if OOO000OO00000O0OO :#line:181
        OOO000OO00000O0OO =OOO000OO00000O0OO [0 ]#line:182
    O0OOOO0OO0OOOOO00 =re .findall (r'createTime = \'(.*)\'',O00O00O0OOOO000OO .text )#line:183
    if O0OOOO0OO0OOOOO00 :#line:184
        O0OOOO0OO0OOOOO00 =O0OOOO0OO0OOOOO00 [0 ][5 :]#line:185
    OOOOOOOOOO0OOO0O0 =f'{O0OOOO0OO0OOOOO00}|{O00OOOOO00O00000O}|{O00OO0O000O00OOOO}|{OOOO0000OO0000O0O}|{OOO000OO00000O0OO}'#line:186
    OOO0OOO0OO0OOO0OO ={'biz':O00OO0O000O00OOOO ,'text':OOOOOOOOOO0OOO0O0 }#line:187
    return OOO0OOO0OO0OOO0OO #line:188
def read_file ():#line:191
    with open ('mtztoken.json','r',encoding ='utf-8')as OOO00OO000OO0OO0O :#line:192
        return json .loads (OOO00OO000OO0OO0O .read ())#line:193
def write_file (OO0O0OO0OOO0O00O0 ):#line:196
    with open ('mtztoken.json','w',encoding ='utf-8')as OOOOO0O0O0O00O000 :#line:197
        OOOOO0O0O0O00O000 .write (json .dumps (OO0O0OO0OOO0O00O0 ))#line:198
class MTZYD :#line:201
    def __init__ (OOO000O00O0O000OO ,OO0OO0OOO0O0OOOO0 ,OOO0O00OOOO0OO000 ):#line:202
        OOO0O00OOOO0OO000 =OOO0O00OOOO0OO000 .split ('#')#line:203
        if ''in OOO0O00OOOO0OO000 :#line:204
            OOO0O00OOOO0OO000 .pop ('')#line:205
        OOO000O00O0O000OO .index =OO0OO0OOO0O0OOOO0 #line:206
        OOO000O00O0O000OO .uid =OOO0O00OOOO0OO000 [1 ]if len (OOO0O00OOOO0OO000 )==2 else None #line:207
        OOO000O00O0O000OO .url =OOO0O00OOOO0OO000 [0 ]#line:208
        OOO000O00O0O000OO .s =requests .session ()#line:209
        OOO000O00O0O000OO .s .headers ={'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5279 MMWEBSDK/20230805 MMWEBID/2833 MicroMessenger/8.0.42.2460(0x28002A3B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Accept':'*/*','Origin':'http://61695315208.tt.bendishenghuochwl1.cn','Referer':'http://61695315208.tt.bendishenghuochwl1.cn/','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh',}#line:217
        OOO000O00O0O000OO .msg =''#line:218
    def init (OOOOO0OO0O0OO0OO0 ):#line:220
        O00O00O0O0OOOOOO0 ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309071d) XWEB/8447 Flue','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',}#line:224
        O0O0O00O0OOO000O0 =requests .get (OOOOO0OO0O0OO0OO0 .url ,headers =O00O00O0O0OOOOOO0 ,allow_redirects =False ).json ()#line:225
        debugger (f'init {O0O0O00O0OOO000O0}')#line:226
        O000OO00O0O000O0O =O0O0O00O0OOO000O0 .get ('data').get ('token')#line:227
        try :#line:228
            OOOO00O0OO0OOOO00 =read_file ()#line:229
        except :#line:230
            OOOO00O0OO0OOOO00 ={}#line:231
        if O000OO00O0O000O0O :#line:232
            OOOOO0OO0O0OO0OO0 .s .headers .update ({'Authorization':O000OO00O0O000O0O })#line:233
            OOOO00O0OO0OOOO00 .update ({OOOOO0OO0O0OO0OO0 .index :O000OO00O0O000O0O })#line:234
            write_file (OOOO00O0OO0OOOO00 )#line:235
        else :#line:236
            OOOOO0OO0O0OO0OO0 .msg +='链接失效，请重新抓取\n'#line:237
            printlog (f'【账号{OOOOO0OO0O0OO0OO0.index}】:链接失效，请重新抓取')#line:238
            if sendable :#line:239
                send (f'【账号{OOOOO0OO0O0OO0OO0.index}】 每天赚链接失效，请重新抓取','每天赚链接失效通知')#line:240
            if pushable :#line:241
                push (f'【账号{OOOOO0OO0O0OO0OO0.index}】 每天赚链接失效，请重新抓取','每天赚链接通知','http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552',OOOOO0OO0O0OO0OO0 .uid )#line:243
            OOOOO0OO0O0OO0OO0 .s .headers .update ({'Authorization':OOOO00O0OO0OOOO00 [OOOOO0OO0O0OO0OO0 .index ]})#line:244
    def user_info (O0O0000000OOOO000 ):#line:247
        O0O0OO0O0O0OOOO00 ='http://api.mengmorwpt1.cn/h5_share/user/info'#line:248
        O000OOO0OO00OO0OO =O0O0000000OOOO000 .s .post (O0O0OO0O0O0OOOO00 ,json ={"openid":0 }).json ()#line:249
        debugger (f'userinfo {O000OOO0OO00OO0OO}')#line:250
        if O000OOO0OO00OO0OO .get ('code')==200 :#line:251
            O0O0000000OOOO000 .nickname =O000OOO0OO00OO0OO .get ('data').get ('nickname')#line:252
            O0O0000000OOOO000 .points =O000OOO0OO00OO0OO .get ('data').get ('points')-O000OOO0OO00OO0OO .get ('data').get ('withdraw_points')#line:253
            O000OOO0OO00OO0OO =O0O0000000OOOO000 .s .post ('http://api.mengmorwpt1.cn/h5_share/user/sign',json ={"openid":0 })#line:254
            debugger (f'签到 {O000OOO0OO00OO0OO.json()}')#line:255
            O000OOO0O00OOOOO0 =O000OOO0OO00OO0OO .json ().get ('message')#line:256
            O0O0000000OOOO000 .msg +=f'\n【账号{O0O0000000OOOO000.index}】:{O0O0000000OOOO000.nickname},现有积分：{O0O0000000OOOO000.points}，{O000OOO0O00OOOOO0}\n'+'-'*50 +'\n'#line:257
            printlog (f'【账号{O0O0000000OOOO000.index}】:{O0O0000000OOOO000.nickname},现有积分：{O0O0000000OOOO000.points}，{O000OOO0O00OOOOO0}')#line:258
            O0O0OO0O0O0OOOO00 ='http://api.mengmorwpt1.cn/h5_share/user/up_profit_ratio'#line:259
            OOOO000OOOO0OO000 ={"openid":0 }#line:260
            try :#line:261
                O000OOO0OO00OO0OO =O0O0000000OOOO000 .s .post (O0O0OO0O0O0OOOO00 ,json =OOOO000OOOO0OO000 ).json ()#line:262
                if O000OOO0OO00OO0OO .get ('code')==500 :#line:263
                    raise #line:264
                O0O0000000OOOO000 .msg +=f'代理升级：{O000OOO0OO00OO0OO.get("message")}\n'#line:265
                printlog (f'代理升级：{O000OOO0OO00OO0OO.get("message")}\n')#line:266
            except :#line:267
                O0O0OO0O0O0OOOO00 ='http://api.mengmorwpt1.cn/h5_share/user/task_reward'#line:268
                for OOO0OO00O0OO00000 in range (0 ,8 ):#line:269
                    OOOO000OOOO0OO000 ={"type":OOO0OO00O0OO00000 ,"openid":0 }#line:270
                    O000OOO0OO00OO0OO =O0O0000000OOOO000 .s .post (O0O0OO0O0O0OOOO00 ,json =OOOO000OOOO0OO000 ).json ()#line:271
                    if '积分未满'in O000OOO0OO00OO0OO .get ('message'):#line:272
                        break #line:273
                    if O000OOO0OO00OO0OO .get ('code')!=500 :#line:274
                        O0O0000000OOOO000 .msg +='主页奖励积分：'+O000OOO0OO00OO0OO .get ('message')+'\n'#line:275
                        printlog (f'【账号{O0O0000000OOOO000.index}】:主页奖励积分 {O000OOO0OO00OO0OO.get("message")}')#line:276
                    OOO0OO00O0OO00000 +=1 #line:277
                    time .sleep (0.5 )#line:278
            return True #line:279
        else :#line:280
            O0O0000000OOOO000 .msg +='获取账号信息异常，检查cookie是否失效\n'#line:281
            printlog (f'【账号{O0O0000000OOOO000.index}】:获取账号信息异常，检查cookie是否失效')#line:282
            return False #line:283
    def get_read (OOOOO00OO0000000O ):#line:285
        O00OO00O000OO00O0 ='http://api.mengmorwpt1.cn/h5_share/daily/get_read'#line:286
        O0OO0O0OOOO0000OO ={"openid":0 }#line:287
        O000O00OO0O00O000 =0 #line:288
        while O000O00OO0O00O000 <10 :#line:289
            OO000OOO000OOO000 =OOOOO00OO0000000O .s .post (O00OO00O000OO00O0 ,json =O0OO0O0OOOO0000OO ).json ()#line:290
            debugger (f'getread {OO000OOO000OOO000}')#line:291
            if OO000OOO000OOO000 .get ('code')==200 :#line:292
                OOOOO00OO0000000O .link =OO000OOO000OOO000 .get ('data').get ('link')#line:293
                return True #line:294
            elif '获取失败'in OO000OOO000OOO000 .get ('message'):#line:295
                time .sleep (15 )#line:296
                O000O00OO0O00O000 +=1 #line:297
                continue #line:298
            else :#line:299
                OOOOO00OO0000000O .msg +=OO000OOO000OOO000 .get ('message')+'\n'#line:300
                printlog (f'【账号{OOOOO00OO0000000O.index}】:{OO000OOO000OOO000.get("message")}')#line:301
                return False #line:302
    def gettaskinfo (OOOO0OOOOOO0O0OO0 ,O0O0O0O00OO0OOOO0 ):#line:304
        for OOO00O0OO00O00O0O in O0O0O0O00OO0OOOO0 :#line:305
            if OOO00O0OO00O00O0O .get ('url'):#line:306
                return OOO00O0OO00O00O0O #line:307
    def dotasks (OOOO000OO0O0O0000 ):#line:309
        O0OOOO000OOOO0OOO ={'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Origin':'http://nei594688.594688be.com.byymmmcm3.cn','Referer':'http://nei594688.594688be.com.byymmmcm3.cn/','Accept-Encoding':'gzip, deflate',}#line:316
        O000000O0O0O00OOO =0 #line:317
        while True :#line:318
            OO0OOO00O0OO00O00 ={"href":OOOO000OO0O0O0000 .link }#line:319
            OO0O0OO00O0000O0O ='https://api.wanjd.cn/wxread/articles/tasks'#line:320
            OOO00000O0OO00OO0 =requests .post (OO0O0OO00O0000O0O ,headers =O0OOOO000OOOO0OOO ,json =OO0OOO00O0OO00O00 ).json ()#line:321
            O00OO0000O00O0000 =OOO00000O0OO00OO0 .get ('data')#line:322
            debugger (f'tasks {O00OO0000O00O0000}')#line:323
            O0O0O0O0O0O0O0O0O =[OO0O00000OOOO00O0 ['is_read']for OO0O00000OOOO00O0 in O00OO0000O00O0000 ]#line:324
            if 0 not in O0O0O0O0O0O0O0O0O :#line:325
                break #line:326
            if OOO00000O0OO00OO0 .get ('code')!=200 :#line:327
                OOOO000OO0O0O0000 .msg +=OOO00000O0OO00OO0 .get ('message')+'\n'#line:328
                printlog (f'【账号{OOOO000OO0O0O0000.index}】:{OOO00000O0OO00OO0.get("message")}')#line:329
                break #line:330
            else :#line:331
                O0OOOO00OO00000OO =OOOO000OO0O0O0000 .gettaskinfo (OOO00000O0OO00OO0 ['data'])#line:332
                if not O0OOOO00OO00000OO :#line:333
                    break #line:334
                OO0OO00OO0OO00000 =O0OOOO00OO00000OO .get ('url')#line:335
                if len (O00OO0000O00O0000 )<total_num :#line:336
                    printlog (f'【账号{OOOO000OO0O0O0000.index}】:任务数量小于{total_num}，任务中止')#line:337
                    break #line:338
                OO000OOOOO000O00O =O0OOOO00OO00000OO ['id']#line:339
                debugger (OO000OOOOO000O00O )#line:340
                OO0OOO00O0OO00O00 .update ({"id":OO000OOOOO000O00O })#line:341
                O00O00OOO0000OO0O =getmpinfo (OO0OO00OO0OO00000 )#line:342
                try :#line:343
                    OOOO000OO0O0O0000 .msg +='正在阅读 '+O00O00OOO0000OO0O ['text']+'\n'#line:344
                    printlog (f'【账号{OOOO000OO0O0O0000.index}】:正在阅读{O00O00OOO0000OO0O["text"]}')#line:345
                except :#line:346
                    OOOO000OO0O0O0000 .msg +='获取文章信息失败\n'#line:347
                    printlog (f'【账号{OOOO000OO0O0O0000.index}】:获取文章信息失败')#line:348
                    break #line:349
                if len (str (OO000OOOOO000O00O ))<5 :#line:350
                    if O000000O0O0O00OOO ==3 :#line:351
                        if sendable :#line:352
                            send ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',f'【账号{OOOO000OO0O0O0000.index}】 美添赚过检测',)#line:355
                        if pushable :#line:356
                            push ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束\n点击阅读检测文章',f'【账号{OOOO000OO0O0O0000.index}】 美添赚过检测',)#line:359
                        break #line:360
                    if sendable :#line:361
                        send (O00O00OOO0000OO0O .get ('text'),f'【账号{OOOO000OO0O0O0000.index}】{OOOO000OO0O0O0000.nickname} 美添赚过检测',OO0OO00OO0OO00000 )#line:362
                    if pushable :#line:363
                        push (f'【账号{OOOO000OO0O0O0000.index}】{OOOO000OO0O0O0000.nickname} 本轮任务数量{len(O00OO0000O00O0000) - 1}\n点击阅读检测文章\n{O00O00OOO0000OO0O["text"]}',f'【账号{OOOO000OO0O0O0000.index}】 {OOOO000OO0O0O0000.nickname}美添赚过检测',OO0OO00OO0OO00000 ,OOOO000OO0O0O0000 .uid )#line:366
                    OOOO000OO0O0O0000 .msg +='发送通知，暂停50秒\n'#line:367
                    printlog (f'【账号{OOOO000OO0O0O0000.index}】:发送通知，暂停50秒')#line:368
                    O000000O0O0O00OOO +=1 #line:369
                    time .sleep (50 )#line:370
                OO00000000OO0OOOO =random .randint (7 ,10 )#line:371
                time .sleep (OO00000000OO0OOOO )#line:372
                OO0O0OO00O0000O0O ='https://api.wanjd.cn/wxread/articles/three_read'#line:373
                OOO00000O0OO00OO0 =requests .post (OO0O0OO00O0000O0O ,headers =O0OOOO000OOOO0OOO ,json =OO0OOO00O0OO00O00 ).json ()#line:374
                if OOO00000O0OO00OO0 .get ('code')==200 :#line:375
                    OOOO000OO0O0O0000 .msg +='阅读成功'+'\n'+'-'*50 +'\n'#line:376
                    printlog (f'【账号{OOOO000OO0O0O0000.index}】:阅读成功')#line:377
                if OOO00000O0OO00OO0 .get ('code')!=200 :#line:378
                    OOOO000OO0O0O0000 .msg +=OOO00000O0OO00OO0 .get ('message')+'\n'+'-'*50 +'\n'#line:379
                    printlog (f'【账号{OOOO000OO0O0O0000.index}】:{OOO00000O0OO00OO0.get("message")}')#line:380
                    break #line:381
        OO0O0OO00O0000O0O ='https://api.wanjd.cn/wxread/articles/check_success'#line:382
        OO0OOO00O0OO00O00 ={'type':1 ,'href':OOOO000OO0O0O0000 .link }#line:383
        OOO00000O0OO00OO0 =requests .post (OO0O0OO00O0000O0O ,headers =O0OOOO000OOOO0OOO ,json =OO0OOO00O0OO00O00 ).json ()#line:384
        debugger (f'check {OOO00000O0OO00OO0}')#line:385
        OOOO000OO0O0O0000 .msg +=OOO00000O0OO00OO0 .get ('message')+'\n'#line:386
        printlog (f'【账号{OOOO000OO0O0O0000.index}】:{OOO00000O0OO00OO0.get("message")}')#line:387
    def withdraw (OOO00O00000OOO0O0 ):#line:389
        if OOO00O00000OOO0O0 .points <txbz :#line:390
            OOO00O00000OOO0O0 .msg +=f'没有达到你设置的提现标准{txbz}\n'#line:391
            printlog (f'【账号{OOO00O00000OOO0O0.index}】:没有达到你设置的提现标准{txbz}')#line:392
            return False #line:393
        O0OO00OO00OOOO0OO ='http://api.mengmorwpt1.cn/h5_share/user/withdraw'#line:394
        O00OOOOO0O0OO0O00 =OOO00O00000OOO0O0 .s .post (O0OO00OO00OOOO0OO ).json ()#line:395
        OOO00O00000OOO0O0 .msg +='提现结果'+O00OOOOO0O0OO0O00 .get ('message')+'\n'#line:396
        printlog (f'【账号{OOO00O00000OOO0O0.index}】:提现结果 {O00OOOOO0O0OO0O00.get("message")}')#line:397
        if O00OOOOO0O0OO0O00 .get ('code')==200 :#line:398
            if sendable :#line:399
                send (f'【账号{OOO00O00000OOO0O0.index}】:已提现到红包，请在服务通知内及时领取','每天赚提现通知')#line:400
            if pushable :#line:401
                push (f'【账号{OOO00O00000OOO0O0.index}】:已提现到红包，请在服务通知内及时领取','每天赚提现通知','https://jihulab.com/xizhiai/xiaoym',OOO00O00000OOO0O0 .uid )#line:403
    def run (O00O0O00000O0O0O0 ):#line:405
        O00O0O00000O0O0O0 .msg +='*'*50 +f'\n【账号{O00O0O00000O0O0O0.index}】:开始任务\n'#line:406
        printlog (f'【账号{O00O0O00000O0O0O0.index}】:开始任务')#line:407
        O00O0O00000O0O0O0 .init ()#line:408
        if not O00O0O00000O0O0O0 .user_info ():#line:409
            return False #line:410
        if O00O0O00000O0O0O0 .get_read ():#line:411
            O00O0O00000O0O0O0 .dotasks ()#line:412
            O00O0O00000O0O0O0 .user_info ()#line:413
        O00O0O00000O0O0O0 .withdraw ()#line:414
        printlog (f'【账号{O00O0O00000O0O0O0.index}】:任务结束')#line:415
        if not printf :#line:416
            print (O00O0O00000O0O0O0 .msg .strip ())#line:417
            print (f'【账号{O00O0O00000O0O0O0.index}】:任务结束')#line:418
def yd (O0000O0O0OO0O0000 ):#line:421
    while not O0000O0O0OO0O0000 .empty ():#line:422
        OO00OOOOO000O0OO0 ,OO00OOO0O00O0O000 =O0000O0O0OO0O0000 .get ()#line:423
        O00OO00OOOOO0OOOO =MTZYD (OO00OOOOO000O0OO0 ,OO00OOO0O00O0O000 )#line:424
        O00OO00OOOOO0OOOO .run ()#line:425
def get_info ():#line:428
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:430
    print ('入口：http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552')#line:431
    O0OO0O0OOOO0O00O0 ='V2.3'#line:432
    O0O0O00000000O00O =_O0O00OO00O0000O0O ['version']['k_mtz']#line:433
    print (f'当前版本{O0OO0O0OOOO0O00O0}，仓库版本{O0O0O00000000O00O}\n{_O0O00OO00O0000O0O["update_log"]["每天赚"]}')#line:434
    if O0OO0O0OOOO0O00O0 <O0O0O00000000O00O :#line:435
        print ('请到仓库下载最新版本k_mtz.py')#line:436
    print ("="*25 )#line:437
def main ():#line:440
    get_info ()#line:441
    O0O0OO0O000OO00OO =os .getenv ('mtzurl')#line:442
    if not O0O0OO0O000OO00OO :#line:443
        print (_O0O00OO00O0000O0O .get ('msg')['每天赚'])#line:444
        exit ()#line:445
    OO000O0O0OO0O0OO0 =Queue ()#line:446
    O00O00OOO0OOOOO0O =[]#line:447
    O00O0O00OOO0OOOOO =O0O0OO0O000OO00OO .replace ('&&','\n').split ('\n')#line:448
    for O0O00000000O0O000 ,OOOOOOO000O0OO000 in enumerate (O00O0O00OOO0OOOOO ,start =1 ):#line:449
        OO000O0O0OO0O0OO0 .put ([O0O00000000O0O000 ,OOOOOOO000O0OO000 ])#line:450
    for O0O00000000O0O000 in range (max_workers ):#line:451
        OO00O0O00OOOO0O00 =threading .Thread (target =yd ,args =(OO000O0O0OO0O0OO0 ,))#line:452
        OO00O0O00OOOO0O00 .start ()#line:453
        O00O00OOO0OOOOO0O .append (OO00O0O00OOOO0O00 )#line:454
        time .sleep (delay_time )#line:455
    for O0OO0O00OOO00O00O in O00O00OOO0OOOOO0O :#line:456
        O0OO0O00OOO00O00O .join ()#line:457
if __name__ =='__main__':#line:460
    main ()#line:461
