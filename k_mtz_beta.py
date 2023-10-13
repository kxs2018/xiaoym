# -*- coding: utf-8 -*-
# k_mtz_beta
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
    OOOO0OOOO0O0OO00O ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:55
    OO0OO0OOO00O00000 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OOOO0OOOO0O0OO00O ).json ()#line:56
    return OO0OO0OOO00O00000 #line:57
_OOOOO0OOOOOOO0OO0 =get_msg ()#line:60
try :#line:61
    from lxml import etree #line:62
except :#line:63
    print (_OOOOO0OOOOOOO0OO0 .get ('help')['lxml'])#line:64
if sendable :#line:66
    qwbotkey =os .getenv ('qwbotkey')#line:67
    if not qwbotkey :#line:68
        print (_OOOOO0OOOOOOO0OO0 .get ('help')['qwbotkey'])#line:69
        exit ()#line:70
if pushable :#line:72
    pushconfig =os .getenv ('pushconfig')#line:73
    if not pushconfig :#line:74
        print (_OOOOO0OOOOOOO0OO0 .get ('help')['pushconfig'])#line:75
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
            print (_OOOOO0OOOOOOO0OO0 .get ('help')['pushconfig'])#line:92
            exit ()#line:93
if not pushable and not sendable :#line:94
    print ('啥通知方式都不配置，你想上天吗')#line:95
    exit ()#line:96
def ftime ():#line:99
    O0OO00000O00OOOOO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:100
    return O0OO00000O00OOOOO #line:101
def debugger (O00OO0O00OO0O000O ):#line:104
    if debug :#line:105
        print (O00OO0O00OO0O000O )#line:106
def printlog (OOOO000O0O0OOOOO0 ):#line:109
    if printf :#line:110
        print (OOOO000O0O0OOOOO0 )#line:111
def send (OOOOO0OO0OO0OO00O ,title ='通知',url =None ):#line:114
    if not url :#line:115
        O00OOO0000000O0OO ={"msgtype":"text","text":{"content":f"{title}\n\n{OOOOO0OO0OO0OO00O}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:122
    else :#line:123
        O00OOO0000000O0OO ={"msgtype":"news","news":{"articles":[{"title":title ,"description":OOOOO0OO0OO0OO00O ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:128
    OOO0O00O0O0OO0O0O =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:129
    OOO00O00O0OO00O0O =requests .post (OOO0O00O0O0OO0O0O ,data =json .dumps (O00OOO0000000O0OO )).json ()#line:130
    if OOO00O00O0OO00O0O .get ('errcode')!=0 :#line:131
        print ('消息发送失败，请检查key和发送格式')#line:132
        return False #line:133
    return OOO00O00O0OO00O0O #line:134
def push (O0O0OOOO0OOO0O0O0 ,O0OOO0OOOO0OO0OO0 ,url ='',uid =None ):#line:137
    if uid :#line:138
        uids .append (uid )#line:139
    OO0OO0O0OO00OOOOO ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',O0O0OOOO0OOO0O0O0 ).replace ('url',url )#line:141
    O000O0O000O0O00OO ={"appToken":appToken ,"content":OO0OO0O0OO00OOOOO ,"summary":O0OOO0OOOO0OO0OO0 ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:151
    O0OO0OOOOO0OOOOO0 ='http://wxpusher.zjiecode.com/api/send/message'#line:152
    O000O0O0OO0O0O000 =requests .post (url =O0OO0OOOOO0OOOOO0 ,json =O000O0O000O0O00OO ).json ()#line:153
    if O000O0O0OO0O0O000 .get ('code')!=1000 :#line:154
        print (O000O0O0OO0O0O000 .get ('msg'),O000O0O0OO0O0O000 )#line:155
    return O000O0O0OO0O0O000 #line:156
def getmpinfo (OO0O00OO0O00O0O0O ):#line:159
    if not OO0O00OO0O00O0O0O or OO0O00OO0O00O0O0O =='':#line:160
        return False #line:161
    OO0O00OOO000O0OOO ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:163
    OO0OO00000OO000OO =requests .get (OO0O00OO0O00O0O0O ,headers =OO0O00OOO000O0OOO )#line:164
    O00OOOO0O00O0OOO0 =etree .HTML (OO0OO00000OO000OO .text )#line:165
    O000O0OO00O00O0O0 =O00OOOO0O00O0OOO0 .xpath ('//meta[@*="og:title"]/@content')#line:166
    if O000O0OO00O00O0O0 :#line:167
        O000O0OO00O00O0O0 =O000O0OO00O00O0O0 [0 ]#line:168
    try :#line:169
        if 'biz='in OO0O00OO0O00O0O0O :#line:170
            OO00O00OO0000000O =re .findall (r'biz=(.*?)&',OO0O00OO0O00O0O0O )[0 ]#line:171
        else :#line:172
            O0OO0000OOOOOOO0O =O00OOOO0O00O0OOO0 .xpath ('//meta[@*="og:url"]/@content')[0 ]#line:173
            OO00O00OO0000000O =re .findall (r'biz=(.*?)&',str (O0OO0000OOOOOOO0O ))[0 ]#line:174
    except :#line:175
        return False #line:176
    O000OOOOOO000OOO0 =O00OOOO0O00O0OOO0 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:177
    if O000OOOOOO000OOO0 :#line:178
        O000OOOOOO000OOO0 =O000OOOOOO000OOO0 [0 ].strip ()#line:179
    OO000000O00O0OOO0 =re .findall (r"user_name.DATA'\) : '(.*?)'",OO0OO00000OO000OO .text )or O00OOOO0O00O0OOO0 .xpath ('//span[@class="profile_meta_value"]/text()')#line:181
    if OO000000O00O0OOO0 :#line:182
        OO000000O00O0OOO0 =OO000000O00O0OOO0 [0 ]#line:183
    OO0OO0OO0O0OO00OO =re .findall (r'createTime = \'(.*)\'',OO0OO00000OO000OO .text )#line:184
    if OO0OO0OO0O0OO00OO :#line:185
        OO0OO0OO0O0OO00OO =OO0OO0OO0O0OO00OO [0 ][5 :]#line:186
    O0OO00OOO00OO0000 =f'{OO0OO0OO0O0OO00OO}|{O000O0OO00O00O0O0}|{OO00O00OO0000000O}|{O000OOOOOO000OOO0}|{OO000000O00O0OOO0}'#line:187
    OOO0O0O0O00OO00OO ={'biz':OO00O00OO0000000O ,'text':O0OO00OOO00OO0000 }#line:188
    return OOO0O0O0O00OO00OO #line:189
def read_file ():#line:192
    with open ('mtztoken.json','r',encoding ='utf-8')as O0O0OOO0OO0OOO000 :#line:193
        return json .loads (O0O0OOO0OO0OOO000 .read ())#line:194
def write_file (OOO0OO0OO0OOOOOO0 ):#line:197
    with open ('mtztoken.json','w',encoding ='utf-8')as OOOOO0OO0OOO0O0O0 :#line:198
        OOOOO0OO0OOO0O0O0 .write (json .dumps (OOO0OO0OO0OOOOOO0 ))#line:199
class MTZYD :#line:202
    def __init__ (OO0O0000OO00O0OOO ,OOO0OO00OOO0OO0O0 ):#line:203
        OOO0OO00OOO0OO0O0 =OOO0OO00OOO0OO0O0 .split (';')#line:204
        if ''in OOO0OO00OOO0OO0O0 :#line:205
            OOO0OO00OOO0OO0O0 .pop ('')#line:206
        OO0O0000OO00O0OOO .index =OOO0OO00OOO0OO0O0 [0 ].split ('=')[1 ]#line:207
        OO0O0000OO00O0OOO .uid =OOO0OO00OOO0OO0O0 [2 ].split ('=')[1 ]if len (OOO0OO00OOO0OO0O0 )==3 else None #line:208
        OO0O0000OO00O0OOO .openid =OOO0OO00OOO0OO0O0 [1 ].split ('=')[1 ]#line:209
        OO0O0000OO00O0OOO .s =requests .session ()#line:210
        OO0O0000OO00O0OOO .s .headers ={'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5279 MMWEBSDK/20230805 MMWEBID/2833 MicroMessenger/8.0.42.2460(0x28002A3B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Accept':'*/*','Origin':'http://61695315208.tt.bendishenghuochwl1.cn','Referer':'http://61695315208.tt.bendishenghuochwl1.cn/','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh',}#line:218
        OO0O0000OO00O0OOO .msg =''#line:219
    def init (O0O00O0O00OO0000O ):#line:221
        OOO0O0O0O0O0O00OO ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309071d) XWEB/8447 Flue','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',}#line:225
        OOO0OOOO00OOOOOO0 =str (int (time .time ()))#line:226
        OOOOOOOO0OO0000O0 =f'http://api.mengmorwpt1.cn/h5_share/user/ccz?openid={O0O00O0O00OO0000O.openid}&ru=http://2{OOO0OOOO00OOOOOO0}.tv.mmcmbyym2.top/pages/app/daily/daily?openid={self.openid}#NHSKAJWPLKDJATHBEBKSLMNBFLKAGUJKGD='#line:227
        OO00O0000O0OOO0O0 =requests .get (OOOOOOOO0OO0000O0 ,headers =OOO0O0O0O0O0O00OO ,allow_redirects =False ).json ()#line:228
        debugger (f'init {OO00O0000O0OOO0O0}')#line:229
        OOOO0000O0O00O0OO =OO00O0000O0OOO0O0 .get ('data').get ('token')#line:230
        try :#line:231
            O0O0O00OOO00O0OO0 =read_file ()#line:232
        except :#line:233
            O0O0O00OOO00O0OO0 ={}#line:234
        if OOOO0000O0O00O0OO :#line:235
            O0O00O0O00OO0000O .s .headers .update ({'Authorization':OOOO0000O0O00O0OO })#line:236
            O0O0O00OOO00O0OO0 .update ({O0O00O0O00OO0000O .index :OOOO0000O0O00O0OO })#line:237
            write_file (O0O0O00OOO00O0OO0 )#line:238
        else :#line:239
            O0O00O0O00OO0000O .msg +='链接失效，请重新抓取\n'#line:240
            printlog (f'【{O0O00O0O00OO0000O.index}】:链接失效，请重新抓取')#line:241
            if sendable :#line:242
                send (f'【{O0O00O0O00OO0000O.index}】 每天赚链接失效，请重新抓取','每天赚链接失效通知')#line:243
            if pushable :#line:244
                push (f'【{O0O00O0O00OO0000O.index}】 每天赚链接失效，请重新抓取','每天赚链接通知','http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552',O0O00O0O00OO0000O .uid )#line:246
            O0O00O0O00OO0000O .s .headers .update ({'Authorization':O0O0O00OOO00O0OO0 [O0O00O0O00OO0000O .index ]})#line:247
    def user_info (O0000O000O0O0O000 ):#line:249
        O0O000O0000O0O0OO ='http://api.mengmorwpt1.cn/h5_share/user/info'#line:250
        O0OO000O0OO00OOO0 =O0000O000O0O0O000 .s .post (O0O000O0000O0O0OO ,json ={"openid":0 }).json ()#line:251
        debugger (f'userinfo {O0OO000O0OO00OOO0}')#line:252
        if O0OO000O0OO00OOO0 .get ('code')==200 :#line:253
            O0000O000O0O0O000 .nickname =O0OO000O0OO00OOO0 .get ('data').get ('nickname')#line:254
            O0000O000O0O0O000 .points =O0OO000O0OO00OOO0 .get ('data').get ('points')-O0OO000O0OO00OOO0 .get ('data').get ('withdraw_points')#line:255
            O0OO000O0OO00OOO0 =O0000O000O0O0O000 .s .post ('http://api.mengmorwpt1.cn/h5_share/user/sign',json ={"openid":0 })#line:256
            debugger (f'签到 {O0OO000O0OO00OOO0.json()}')#line:257
            O0O0000OO00000O0O =O0OO000O0OO00OOO0 .json ().get ('message')#line:258
            O0000O000O0O0O000 .msg +=f'\n【{O0000O000O0O0O000.index}】:{O0000O000O0O0O000.nickname},现有积分：{O0000O000O0O0O000.points}，{O0O0000OO00000O0O}\n'+'-'*50 +'\n'#line:259
            printlog (f'【{O0000O000O0O0O000.index}】:{O0000O000O0O0O000.nickname},现有积分：{O0000O000O0O0O000.points}，{O0O0000OO00000O0O}')#line:260
            O0O000O0000O0O0OO ='http://api.mengmorwpt1.cn/h5_share/user/up_profit_ratio'#line:261
            OOO0O000O0O0000O0 ={"openid":0 }#line:262
            try :#line:263
                O0OO000O0OO00OOO0 =O0000O000O0O0O000 .s .post (O0O000O0000O0O0OO ,json =OOO0O000O0O0000O0 ).json ()#line:264
                if O0OO000O0OO00OOO0 .get ('code')==500 :#line:265
                    raise #line:266
                O0000O000O0O0O000 .msg +=f'代理升级：{O0OO000O0OO00OOO0.get("message")}\n'#line:267
                printlog (f'代理升级：{O0OO000O0OO00OOO0.get("message")}\n')#line:268
            except :#line:269
                O0O000O0000O0O0OO ='http://api.mengmorwpt1.cn/h5_share/user/task_reward'#line:270
                for O0O000O0OOOO0OO0O in range (0 ,8 ):#line:271
                    OOO0O000O0O0000O0 ={"type":O0O000O0OOOO0OO0O ,"openid":0 }#line:272
                    O0OO000O0OO00OOO0 =O0000O000O0O0O000 .s .post (O0O000O0000O0O0OO ,json =OOO0O000O0O0000O0 ).json ()#line:273
                    if '积分未满'in O0OO000O0OO00OOO0 .get ('message'):#line:274
                        break #line:275
                    if O0OO000O0OO00OOO0 .get ('code')!=500 :#line:276
                        O0000O000O0O0O000 .msg +='主页奖励积分：'+O0OO000O0OO00OOO0 .get ('message')+'\n'#line:277
                        printlog (f'【{O0000O000O0O0O000.index}】:主页奖励积分 {O0OO000O0OO00OOO0.get("message")}')#line:278
                    O0O000O0OOOO0OO0O +=1 #line:279
                    time .sleep (0.5 )#line:280
            return True #line:281
        else :#line:282
            O0000O000O0O0O000 .msg +='获取账号信息异常，检查cookie是否失效\n'#line:283
            printlog (f'【{O0000O000O0O0O000.index}】:获取账号信息异常，检查cookie是否失效')#line:284
            return False #line:285
    def get_read (O00O0O0O0OOO000O0 ):#line:287
        O000000O0O0OOO0OO ='http://api.mengmorwpt1.cn/h5_share/daily/get_read'#line:288
        OO0O00O0000OO00OO ={"openid":0 }#line:289
        OO0OOOO0OOO000000 =0 #line:290
        while OO0OOOO0OOO000000 <10 :#line:291
            O000O0000O00OOO00 =O00O0O0O0OOO000O0 .s .post (O000000O0O0OOO0OO ,json =OO0O00O0000OO00OO ).json ()#line:292
            debugger (f'getread {O000O0000O00OOO00}')#line:293
            if O000O0000O00OOO00 .get ('code')==200 :#line:294
                O00O0O0O0OOO000O0 .link =O000O0000O00OOO00 .get ('data').get ('link')#line:295
                return True #line:296
            elif '获取失败'in O000O0000O00OOO00 .get ('message'):#line:297
                time .sleep (15 )#line:298
                OO0OOOO0OOO000000 +=1 #line:299
                continue #line:300
            else :#line:301
                O00O0O0O0OOO000O0 .msg +=O000O0000O00OOO00 .get ('message')+'\n'#line:302
                printlog (f'【{O00O0O0O0OOO000O0.index}】:{O000O0000O00OOO00.get("message")}')#line:303
                return False #line:304
    def gettaskinfo (OO0O00OO0000O00O0 ,O000000000OO0OOOO ):#line:306
        for OO0OO00OO000O0O00 in O000000000OO0OOOO :#line:307
            if OO0OO00OO000O0O00 .get ('url'):#line:308
                return OO0OO00OO000O0O00 #line:309
    def dotasks (OO0000O00OOO0OO0O ):#line:311
        O00O00OOOO00OO00O ={'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Origin':'http://nei594688.594688be.com.byymmmcm3.cn','Referer':'http://nei594688.594688be.com.byymmmcm3.cn/','Accept-Encoding':'gzip, deflate',}#line:318
        OOO00OO0000O000O0 =0 #line:319
        while True :#line:320
            O000OO0OOOO00000O ={"href":OO0000O00OOO0OO0O .link }#line:321
            OO0OO00000OOO0000 ='https://api.wanjd.cn/wxread/articles/tasks'#line:322
            OOO00000O00O000O0 =requests .post (OO0OO00000OOO0000 ,headers =O00O00OOOO00OO00O ,json =O000OO0OOOO00000O ).json ()#line:323
            OOOO0OO00O00O0OOO =OOO00000O00O000O0 .get ('data')#line:324
            debugger (f'tasks {OOOO0OO00O00O0OOO}')#line:325
            OOO0O0O0OOO0O00O0 =[OO0OOOOO0OO0000OO ['is_read']for OO0OOOOO0OO0000OO in OOOO0OO00O00O0OOO ]#line:326
            if 0 not in OOO0O0O0OOO0O00O0 :#line:327
                break #line:328
            if OOO00000O00O000O0 .get ('code')!=200 :#line:329
                OO0000O00OOO0OO0O .msg +=OOO00000O00O000O0 .get ('message')+'\n'#line:330
                printlog (f'【{OO0000O00OOO0OO0O.index}】:{OOO00000O00O000O0.get("message")}')#line:331
                break #line:332
            else :#line:333
                O0O0OO0O0O00O0O0O =OO0000O00OOO0OO0O .gettaskinfo (OOO00000O00O000O0 ['data'])#line:334
                if not O0O0OO0O0O00O0O0O :#line:335
                    break #line:336
                O0000OOOO0OOO0O0O =O0O0OO0O0O00O0O0O .get ('url')#line:337
                if len (OOOO0OO00O00O0OOO )<total_num :#line:338
                    printlog (f'【{OO0000O00OOO0OO0O.index}】:任务数量小于{total_num}，任务中止')#line:339
                    break #line:340
                OOO000OO0000O0O00 =O0O0OO0O0O00O0O0O ['id']#line:341
                debugger (OOO000OO0000O0O00 )#line:342
                O000OO0OOOO00000O .update ({"id":OOO000OO0000O0O00 })#line:343
                OOOO000OOOOO0O00O =getmpinfo (O0000OOOO0OOO0O0O )#line:344
                try :#line:345
                    OO0000O00OOO0OO0O .msg +='正在阅读 '+OOOO000OOOOO0O00O ['text']+'\n'#line:346
                    printlog (f'【{OO0000O00OOO0OO0O.index}】:正在阅读{OOOO000OOOOO0O00O["text"]}')#line:347
                except :#line:348
                    OO0000O00OOO0OO0O .msg +='获取文章信息失败\n'#line:349
                    printlog (f'【{OO0000O00OOO0OO0O.index}】:获取文章信息失败')#line:350
                    break #line:351
                if len (str (OOO000OO0000O0O00 ))<5 :#line:352
                    if OOO00OO0000O000O0 ==3 :#line:353
                        if sendable :#line:354
                            send ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',f'【{OO0000O00OOO0OO0O.index}】 美添赚过检测',)#line:357
                        if pushable :#line:358
                            push ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束\n点击阅读检测文章',f'【{OO0000O00OOO0OO0O.index}】 美添赚过检测',)#line:361
                        break #line:362
                    if sendable :#line:363
                        send (OOOO000OOOOO0O00O .get ('text'),f'【{OO0000O00OOO0OO0O.index}】{OO0000O00OOO0OO0O.nickname} 美添赚过检测',O0000OOOO0OOO0O0O )#line:364
                    if pushable :#line:365
                        push (f'【{OO0000O00OOO0OO0O.index}】{OO0000O00OOO0OO0O.nickname} 本轮任务数量{len(OOOO0OO00O00O0OOO) - 1}\n点击阅读检测文章\n{OOOO000OOOOO0O00O["text"]}',f'【{OO0000O00OOO0OO0O.index}】 {OO0000O00OOO0OO0O.nickname}美添赚过检测',O0000OOOO0OOO0O0O ,OO0000O00OOO0OO0O .uid )#line:369
                    OO0000O00OOO0OO0O .msg +='发送通知，暂停50秒\n'#line:370
                    printlog (f'【{OO0000O00OOO0OO0O.index}】:发送通知，暂停50秒')#line:371
                    OOO00OO0000O000O0 +=1 #line:372
                    time .sleep (50 )#line:373
                OOOOO00OOO0OO0O00 =random .randint (7 ,10 )#line:374
                time .sleep (OOOOO00OOO0OO0O00 )#line:375
                OO0OO00000OOO0000 ='https://api.wanjd.cn/wxread/articles/three_read'#line:376
                OOO00000O00O000O0 =requests .post (OO0OO00000OOO0000 ,headers =O00O00OOOO00OO00O ,json =O000OO0OOOO00000O ).json ()#line:377
                if OOO00000O00O000O0 .get ('code')==200 :#line:378
                    OO0000O00OOO0OO0O .msg +='阅读成功'+'\n'+'-'*50 +'\n'#line:379
                    printlog (f'【{OO0000O00OOO0OO0O.index}】:阅读成功')#line:380
                if OOO00000O00O000O0 .get ('code')!=200 :#line:381
                    OO0000O00OOO0OO0O .msg +=OOO00000O00O000O0 .get ('message')+'\n'+'-'*50 +'\n'#line:382
                    printlog (f'【{OO0000O00OOO0OO0O.index}】:{OOO00000O00O000O0.get("message")}')#line:383
                    break #line:384
        OO0OO00000OOO0000 ='https://api.wanjd.cn/wxread/articles/check_success'#line:385
        O000OO0OOOO00000O ={'type':1 ,'href':OO0000O00OOO0OO0O .link }#line:386
        OOO00000O00O000O0 =requests .post (OO0OO00000OOO0000 ,headers =O00O00OOOO00OO00O ,json =O000OO0OOOO00000O ).json ()#line:387
        debugger (f'check {OOO00000O00O000O0}')#line:388
        OO0000O00OOO0OO0O .msg +=OOO00000O00O000O0 .get ('message')+'\n'#line:389
        printlog (f'【{OO0000O00OOO0OO0O.index}】:{OOO00000O00O000O0.get("message")}')#line:390
    def withdraw (O0O00O0O0O0OO0O0O ):#line:392
        if O0O00O0O0O0OO0O0O .points <txbz :#line:393
            O0O00O0O0O0OO0O0O .msg +=f'没有达到你设置的提现标准{txbz}\n'#line:394
            printlog (f'【{O0O00O0O0O0OO0O0O.index}】:没有达到你设置的提现标准{txbz}')#line:395
            return False #line:396
        OO0OO0O00OOOOOOO0 ='http://api.mengmorwpt1.cn/h5_share/user/withdraw'#line:397
        OOO0000000OOOOO00 =O0O00O0O0O0OO0O0O .s .post (OO0OO0O00OOOOOOO0 ).json ()#line:398
        O0O00O0O0O0OO0O0O .msg +='提现结果'+OOO0000000OOOOO00 .get ('message')+'\n'#line:399
        printlog (f'【{O0O00O0O0O0OO0O0O.index}】:提现结果 {OOO0000000OOOOO00.get("message")}')#line:400
        if OOO0000000OOOOO00 .get ('code')==200 :#line:401
            if sendable :#line:402
                send (f'【{O0O00O0O0O0OO0O0O.index}】:已提现到红包，请在服务通知内及时领取','每天赚提现通知')#line:403
            if pushable :#line:404
                push (f'【{O0O00O0O0O0OO0O0O.index}】:已提现到红包，请在服务通知内及时领取','每天赚提现通知','https://jihulab.com/xizhiai/xiaoym',O0O00O0O0O0OO0O0O .uid )#line:406
    def run (O0O0000O00OOOOOOO ):#line:408
        O0O0000O00OOOOOOO .msg +='*'*50 +f'\n【{O0O0000O00OOOOOOO.index}】:开始任务\n'#line:409
        printlog (f'【{O0O0000O00OOOOOOO.index}】:开始任务')#line:410
        O0O0000O00OOOOOOO .init ()#line:411
        if not O0O0000O00OOOOOOO .user_info ():#line:412
            return False #line:413
        if O0O0000O00OOOOOOO .get_read ():#line:414
            O0O0000O00OOOOOOO .dotasks ()#line:415
            O0O0000O00OOOOOOO .user_info ()#line:416
        O0O0000O00OOOOOOO .withdraw ()#line:417
        printlog (f'【{O0O0000O00OOOOOOO.index}】:任务结束')#line:418
        if not printf :#line:419
            print (O0O0000O00OOOOOOO .msg .strip ())#line:420
            print (f'【{O0O0000O00OOOOOOO.index}】:任务结束')#line:421
def yd (OO00OOO0OOOO00O00 ):#line:424
    while not OO00OOO0OOOO00O00 .empty ():#line:425
        O000OOO0O00O00OOO =OO00OOO0OOOO00O00 .get ()#line:426
        OO0OO00OOOOO0000O =MTZYD (O000OOO0O00O00OOO )#line:427
        OO0OO00OOOOO0000O .run ()#line:428
def get_info ():#line:431
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:433
    print ('入口：http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552')#line:434
    OOO00000OO0OO000O ='V2.4.0'#line:435
    O0OOOO00OOOO0000O =_OOOOO0OOOOOOO0OO0 ['version']['k_mtz_beta']#line:436
    print (f'当前版本{OOO00000OO0OO000O}，仓库版本{O0OOOO00OOOO0000O}\n{_OOOOO0OOOOOOO0OO0["update_log"]["每天赚beta"]}')#line:437
    if OOO00000OO0OO000O <O0OOOO00OOOO0000O :#line:438
        print ('请到仓库下载最新版本k_mtz_beta.py')#line:439
    print ("="*25 )#line:440
def main ():#line:443
    get_info ()#line:444
    O000OOO00O00O000O =os .getenv ('mtzck')#line:445
    if not O000OOO00O00O000O :#line:446
        print (_OOOOO0OOOOOOO0OO0 .get ('msg')['每天赚beta'])#line:447
        exit ()#line:448
    OOO000000OO0OOOOO =Queue ()#line:449
    O0O00O0OO000O00O0 =[]#line:450
    O000OOO00O00O000O =O000OOO00O00O000O .replace ('&&','\n').split ('\n')#line:451
    for O0OO0OOO0O0O0000O ,OOO00O00OOOO000O0 in enumerate (O000OOO00O00O000O ,start =1 ):#line:452
        OOO000000OO0OOOOO .put ([O0OO0OOO0O0O0000O ,OOO00O00OOOO000O0 ])#line:453
    for O0OO0OOO0O0O0000O in range (max_workers ):#line:454
        O000O0OO0OO0OO00O =threading .Thread (target =yd ,args =(OOO000000OO0OOOOO ,))#line:455
        O000O0OO0OO0OO00O .start ()#line:456
        O0O00O0OO000O00O0 .append (O000O0OO0OO0OO00O )#line:457
        time .sleep (delay_time )#line:458
    for OOO0O0OOOO0O0OOO0 in O0O00O0OO000O00O0 :#line:459
        OOO0O0OOOO0O0OOO0 .join ()#line:460
if __name__ =='__main__':#line:463
    main ()#line:464
