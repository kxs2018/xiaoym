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
    O0OO0000O000OOOOO ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:55
    OO0OO0O00OOO0O0O0 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O0OO0000O000OOOOO ).json ()#line:56
    return OO0OO0O00OOO0O0O0 #line:57
_OOOOO0000OOOOOO0O =get_msg ()#line:60
try :#line:61
    from lxml import etree #line:62
except :#line:63
    print (_OOOOO0000OOOOOO0O .get ('help')['lxml'])#line:64
if sendable :#line:66
    qwbotkey =os .getenv ('qwbotkey')#line:67
    if not qwbotkey :#line:68
        print (_OOOOO0000OOOOOO0O .get ('help')['qwbotkey'])#line:69
        exit ()#line:70
if pushable :#line:72
    pushconfig =os .getenv ('pushconfig')#line:73
    if not pushconfig :#line:74
        print (_OOOOO0000OOOOOO0O .get ('help')['pushconfig'])#line:75
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
            print (_OOOOO0000OOOOOO0O .get ('help')['pushconfig'])#line:92
            exit ()#line:93
if not pushable and not sendable :#line:94
    print ('啥通知方式都不配置，你想上天吗')#line:95
    exit ()#line:96
def ftime ():#line:99
    O0OOO0000OO000O00 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:100
    return O0OOO0000OO000O00 #line:101
def debugger (O0O0OOO0OO0O00OO0 ):#line:104
    if debug :#line:105
        print (O0O0OOO0OO0O00OO0 )#line:106
def printlog (O0O0OO0OO00O00O0O ):#line:109
    if printf :#line:110
        print (O0O0OO0OO00O00O0O )#line:111
def send (O00OO00OO0O00O0OO ,title ='通知',url =None ):#line:114
    if not url :#line:115
        OOO0000000000O0OO ={"msgtype":"text","text":{"content":f"{title}\n\n{O00OO00OO0O00O0OO}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:122
    else :#line:123
        OOO0000000000O0OO ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O00OO00OO0O00O0OO ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:128
    O0000000OO00OO0OO =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:129
    O0O0O0O00O0OOO0OO =requests .post (O0000000OO00OO0OO ,data =json .dumps (OOO0000000000O0OO )).json ()#line:130
    if O0O0O0O00O0OOO0OO .get ('errcode')!=0 :#line:131
        print ('消息发送失败，请检查key和发送格式')#line:132
        return False #line:133
    return O0O0O0O00O0OOO0OO #line:134
def push (O000OO000O0O0000O ,O0OO00OOO0O0OOO00 ,url ='',uid =None ):#line:137
    if uid :#line:138
        uids .append (uid )#line:139
    OO00OO0OO0OOO0OO0 ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',O000OO000O0O0000O ).replace ('url',url )#line:141
    OO000O0O0O0O0O0OO ={"appToken":appToken ,"content":OO00OO0OO0OOO0OO0 ,"summary":O0OO00OOO0O0OOO00 ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:151
    OOOO00OO0O0O000O0 ='http://wxpusher.zjiecode.com/api/send/message'#line:152
    O0O00O0O0000O00O0 =requests .post (url =OOOO00OO0O0O000O0 ,json =OO000O0O0O0O0O0OO ).json ()#line:153
    if O0O00O0O0000O00O0 .get ('code')!=1000 :#line:154
        print (O0O00O0O0000O00O0 .get ('msg'),O0O00O0O0000O00O0 )#line:155
    return O0O00O0O0000O00O0 #line:156
def getmpinfo (O0OO00O000OOOOO00 ):#line:159
    if not O0OO00O000OOOOO00 or O0OO00O000OOOOO00 =='':#line:160
        return False #line:161
    OO0OO00O000OOO000 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:163
    OOOOOOO000OOO0OOO =requests .get (O0OO00O000OOOOO00 ,headers =OO0OO00O000OOO000 )#line:164
    OOO000OO00OOO00O0 =etree .HTML (OOOOOOO000OOO0OOO .text )#line:165
    O0OO00O0000O0O000 =OOO000OO00OOO00O0 .xpath ('//meta[@*="og:title"]/@content')#line:166
    if O0OO00O0000O0O000 :#line:167
        O0OO00O0000O0O000 =O0OO00O0000O0O000 [0 ]#line:168
    try :#line:169
        if 'biz='in O0OO00O000OOOOO00 :#line:170
            OOO00OOOO0000OOO0 =re .findall (r'biz=(.*?)&',O0OO00O000OOOOO00 )[0 ]#line:171
        else :#line:172
            OO000O0000OOOO00O =OOO000OO00OOO00O0 .xpath ('//meta[@*="og:url"]/@content')[0 ]#line:173
            OOO00OOOO0000OOO0 =re .findall (r'biz=(.*?)&',str (OO000O0000OOOO00O ))[0 ]#line:174
    except :#line:175
        return False #line:176
    OO0O000OO00OO0OOO =OOO000OO00OOO00O0 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:177
    if OO0O000OO00OO0OOO :#line:178
        OO0O000OO00OO0OOO =OO0O000OO00OO0OOO [0 ].strip ()#line:179
    OO00O000OOOOO000O =re .findall (r"user_name.DATA'\) : '(.*?)'",OOOOOOO000OOO0OOO .text )or OOO000OO00OOO00O0 .xpath ('//span[@class="profile_meta_value"]/text()')#line:181
    if OO00O000OOOOO000O :#line:182
        OO00O000OOOOO000O =OO00O000OOOOO000O [0 ]#line:183
    O0OOO0OOOOO00000O =re .findall (r'createTime = \'(.*)\'',OOOOOOO000OOO0OOO .text )#line:184
    if O0OOO0OOOOO00000O :#line:185
        O0OOO0OOOOO00000O =O0OOO0OOOOO00000O [0 ][5 :]#line:186
    OOOOOO0O0000000O0 =f'{O0OOO0OOOOO00000O}|{O0OO00O0000O0O000}|{OOO00OOOO0000OOO0}|{OO0O000OO00OO0OOO}|{OO00O000OOOOO000O}'#line:187
    O0OOOOO00OOO0OOOO ={'biz':OOO00OOOO0000OOO0 ,'text':OOOOOO0O0000000O0 }#line:188
    return O0OOOOO00OOO0OOOO #line:189
def read_file ():#line:192
    with open ('mtztoken.json','r',encoding ='utf-8')as OO0OOO000O0OOO0OO :#line:193
        return json .loads (OO0OOO000O0OOO0OO .read ())#line:194
def write_file (O0OO0O0OOO0000000 ):#line:197
    with open ('mtztoken.json','w',encoding ='utf-8')as OOO000O0OOO000O0O :#line:198
        OOO000O0OOO000O0O .write (json .dumps (O0OO0O0OOO0000000 ))#line:199
class MTZYD :#line:202
    def __init__ (O0O0O0000OO00O00O ,OOO0O0OO000O0O0O0 ):#line:203
        OOO0O0OO000O0O0O0 =OOO0O0OO000O0O0O0 .split (';')#line:204
        if ''in OOO0O0OO000O0O0O0 :#line:205
            OOO0O0OO000O0O0O0 .pop ('')#line:206
        O0O0O0000OO00O00O .index =OOO0O0OO000O0O0O0 [0 ].split ('=')[1 ]#line:207
        O0O0O0000OO00O00O .uid =OOO0O0OO000O0O0O0 [2 ].split ('=')[1 ]if len (OOO0O0OO000O0O0O0 )==3 else None #line:208
        O0O0O0000OO00O00O .openid =OOO0O0OO000O0O0O0 [1 ].split ('=')[1 ]#line:209
        O0O0O0000OO00O00O .s =requests .session ()#line:210
        O0O0O0000OO00O00O .s .headers ={'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5279 MMWEBSDK/20230805 MMWEBID/2833 MicroMessenger/8.0.42.2460(0x28002A3B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Accept':'*/*','Origin':'http://61695315208.tt.bendishenghuochwl1.cn','Referer':'http://61695315208.tt.bendishenghuochwl1.cn/','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh',}#line:218
        O0O0O0000OO00O00O .msg =''#line:219
    def init (O0OO00OOO0O0O00OO ):#line:221
        O00O0O00OOOO0OOOO ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309071d) XWEB/8447 Flue','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',}#line:225
        O00O0OOO00OO0O0OO =str (int (time .time ()))#line:226
        O0O0OO00O0OOOOOO0 =f'http://api.mengmorwpt1.cn/h5_share/user/ccz?openid={O0OO00OOO0O0O00OO.openid}&ru=http://2{O00O0OOO00OO0O0OO}.tv.mmcmbyym2.top/pages/app/daily/daily?openid={O0OO00OOO0O0O00OO.openid}#NHSKAJWPLKDJATHBEBKSLMNBFLKAGUJKGD='#line:227
        OOO00000O00O000OO =requests .get (O0O0OO00O0OOOOOO0 ,headers =O00O0O00OOOO0OOOO ,allow_redirects =False ).json ()#line:228
        debugger (f'init {OOO00000O00O000OO}')#line:229
        OOO0O0OO0000OOOO0 =OOO00000O00O000OO .get ('data').get ('token')#line:230
        try :#line:231
            O0OO000000OO0O000 =read_file ()#line:232
        except :#line:233
            O0OO000000OO0O000 ={}#line:234
        if OOO0O0OO0000OOOO0 :#line:235
            O0OO00OOO0O0O00OO .s .headers .update ({'Authorization':OOO0O0OO0000OOOO0 })#line:236
            O0OO000000OO0O000 .update ({O0OO00OOO0O0O00OO .index :OOO0O0OO0000OOOO0 })#line:237
            write_file (O0OO000000OO0O000 )#line:238
        else :#line:239
            O0OO00OOO0O0O00OO .msg +='链接失效，请重新抓取\n'#line:240
            printlog (f'【{O0OO00OOO0O0O00OO.index}】:链接失效，请重新抓取')#line:241
            if sendable :#line:242
                send (f'【{O0OO00OOO0O0O00OO.index}】 每天赚链接失效，请重新抓取','每天赚链接失效通知')#line:243
            if pushable :#line:244
                push (f'【{O0OO00OOO0O0O00OO.index}】 每天赚链接失效，请重新抓取','每天赚链接通知','http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552',O0OO00OOO0O0O00OO .uid )#line:246
            O0OO00OOO0O0O00OO .s .headers .update ({'Authorization':O0OO000000OO0O000 [O0OO00OOO0O0O00OO .index ]})#line:247
    def user_info (O000O000OOO0000O0 ):#line:249
        O00O00000OO0OO00O ='http://api.mengmorwpt1.cn/h5_share/user/info'#line:250
        O0OO0OO00O000O000 =O000O000OOO0000O0 .s .post (O00O00000OO0OO00O ,json ={"openid":0 }).json ()#line:251
        debugger (f'userinfo {O0OO0OO00O000O000}')#line:252
        if O0OO0OO00O000O000 .get ('code')==200 :#line:253
            O000O000OOO0000O0 .nickname =O0OO0OO00O000O000 .get ('data').get ('nickname')#line:254
            O000O000OOO0000O0 .points =O0OO0OO00O000O000 .get ('data').get ('points')-O0OO0OO00O000O000 .get ('data').get ('withdraw_points')#line:255
            O0OO0OO00O000O000 =O000O000OOO0000O0 .s .post ('http://api.mengmorwpt1.cn/h5_share/user/sign',json ={"openid":0 })#line:256
            debugger (f'签到 {O0OO0OO00O000O000.json()}')#line:257
            O0000OO00OOO0OOOO =O0OO0OO00O000O000 .json ().get ('message')#line:258
            O000O000OOO0000O0 .msg +=f'\n【{O000O000OOO0000O0.index}】:{O000O000OOO0000O0.nickname},现有积分：{O000O000OOO0000O0.points}，{O0000OO00OOO0OOOO}\n'+'-'*50 +'\n'#line:259
            printlog (f'【{O000O000OOO0000O0.index}】:{O000O000OOO0000O0.nickname},现有积分：{O000O000OOO0000O0.points}，{O0000OO00OOO0OOOO}')#line:260
            O00O00000OO0OO00O ='http://api.mengmorwpt1.cn/h5_share/user/up_profit_ratio'#line:261
            O000O0O00O00OO00O ={"openid":0 }#line:262
            try :#line:263
                O0OO0OO00O000O000 =O000O000OOO0000O0 .s .post (O00O00000OO0OO00O ,json =O000O0O00O00OO00O ).json ()#line:264
                if O0OO0OO00O000O000 .get ('code')==500 :#line:265
                    raise #line:266
                O000O000OOO0000O0 .msg +=f'代理升级：{O0OO0OO00O000O000.get("message")}\n'#line:267
                printlog (f'代理升级：{O0OO0OO00O000O000.get("message")}\n')#line:268
            except :#line:269
                O00O00000OO0OO00O ='http://api.mengmorwpt1.cn/h5_share/user/task_reward'#line:270
                for O000OO00O000O0O00 in range (0 ,8 ):#line:271
                    O000O0O00O00OO00O ={"type":O000OO00O000O0O00 ,"openid":0 }#line:272
                    O0OO0OO00O000O000 =O000O000OOO0000O0 .s .post (O00O00000OO0OO00O ,json =O000O0O00O00OO00O ).json ()#line:273
                    if '积分未满'in O0OO0OO00O000O000 .get ('message'):#line:274
                        break #line:275
                    if O0OO0OO00O000O000 .get ('code')!=500 :#line:276
                        O000O000OOO0000O0 .msg +='主页奖励积分：'+O0OO0OO00O000O000 .get ('message')+'\n'#line:277
                        printlog (f'【{O000O000OOO0000O0.index}】:主页奖励积分 {O0OO0OO00O000O000.get("message")}')#line:278
                    O000OO00O000O0O00 +=1 #line:279
                    time .sleep (0.5 )#line:280
            return True #line:281
        else :#line:282
            O000O000OOO0000O0 .msg +='获取账号信息异常，检查cookie是否失效\n'#line:283
            printlog (f'【{O000O000OOO0000O0.index}】:获取账号信息异常，检查cookie是否失效')#line:284
            return False #line:285
    def get_read (OO0OO0000O0000O00 ):#line:287
        OO0O0OOO00O00O00O ='http://api.mengmorwpt1.cn/h5_share/daily/get_read'#line:288
        OO0O0O00000O00OOO ={"openid":0 }#line:289
        OO00O000OO0OO00O0 =0 #line:290
        while OO00O000OO0OO00O0 <10 :#line:291
            OO000OO00O0000000 =OO0OO0000O0000O00 .s .post (OO0O0OOO00O00O00O ,json =OO0O0O00000O00OOO ).json ()#line:292
            debugger (f'getread {OO000OO00O0000000}')#line:293
            if OO000OO00O0000000 .get ('code')==200 :#line:294
                OO0OO0000O0000O00 .link =OO000OO00O0000000 .get ('data').get ('link')#line:295
                return True #line:296
            elif '获取失败'in OO000OO00O0000000 .get ('message'):#line:297
                time .sleep (15 )#line:298
                OO00O000OO0OO00O0 +=1 #line:299
                continue #line:300
            else :#line:301
                OO0OO0000O0000O00 .msg +=OO000OO00O0000000 .get ('message')+'\n'#line:302
                printlog (f'【{OO0OO0000O0000O00.index}】:{OO000OO00O0000000.get("message")}')#line:303
                return False #line:304
    def gettaskinfo (OO00000O0O0OOOOO0 ,O0OOO0O0O0OO00000 ):#line:306
        for O00OO00OO0OOOOOO0 in O0OOO0O0O0OO00000 :#line:307
            if O00OO00OO0OOOOOO0 .get ('url'):#line:308
                return O00OO00OO0OOOOOO0 #line:309
    def dotasks (OOO00OO0000O00OO0 ):#line:311
        OOOO0O0O0O0OO0OOO ={'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Origin':'http://nei594688.594688be.com.byymmmcm3.cn','Referer':'http://nei594688.594688be.com.byymmmcm3.cn/','Accept-Encoding':'gzip, deflate',}#line:318
        O0OOO000OOO0O0O0O =0 #line:319
        while True :#line:320
            OO0O000O0OO00OOO0 ={"href":OOO00OO0000O00OO0 .link }#line:321
            O0OOO000OO00OOOOO ='https://api.wanjd.cn/wxread/articles/tasks'#line:322
            OO000O00O0O0OOOOO =requests .post (O0OOO000OO00OOOOO ,headers =OOOO0O0O0O0OO0OOO ,json =OO0O000O0OO00OOO0 ).json ()#line:323
            O0O00OO0OO0O000OO =OO000O00O0O0OOOOO .get ('data')#line:324
            debugger (f'tasks {O0O00OO0OO0O000OO}')#line:325
            O0O0OO0O0O0OO000O =[O0OO000OOO0OOO0O0 ['is_read']for O0OO000OOO0OOO0O0 in O0O00OO0OO0O000OO ]#line:326
            if 0 not in O0O0OO0O0O0OO000O :#line:327
                break #line:328
            if OO000O00O0O0OOOOO .get ('code')!=200 :#line:329
                OOO00OO0000O00OO0 .msg +=OO000O00O0O0OOOOO .get ('message')+'\n'#line:330
                printlog (f'【{OOO00OO0000O00OO0.index}】:{OO000O00O0O0OOOOO.get("message")}')#line:331
                break #line:332
            else :#line:333
                OO000OO0OO00OOO00 =OOO00OO0000O00OO0 .gettaskinfo (OO000O00O0O0OOOOO ['data'])#line:334
                if not OO000OO0OO00OOO00 :#line:335
                    break #line:336
                O00O000OO000OO0O0 =OO000OO0OO00OOO00 .get ('url')#line:337
                if len (O0O00OO0OO0O000OO )<total_num :#line:338
                    printlog (f'【{OOO00OO0000O00OO0.index}】:任务数量小于{total_num}，任务中止')#line:339
                    break #line:340
                OO00000OOOOOO0OO0 =OO000OO0OO00OOO00 ['id']#line:341
                debugger (OO00000OOOOOO0OO0 )#line:342
                OO0O000O0OO00OOO0 .update ({"id":OO00000OOOOOO0OO0 })#line:343
                OOO000OO0O0OOOO00 =getmpinfo (O00O000OO000OO0O0 )#line:344
                try :#line:345
                    OOO00OO0000O00OO0 .msg +='正在阅读 '+OOO000OO0O0OOOO00 ['text']+'\n'#line:346
                    printlog (f'【{OOO00OO0000O00OO0.index}】:正在阅读{OOO000OO0O0OOOO00["text"]}')#line:347
                except :#line:348
                    OOO00OO0000O00OO0 .msg +='获取文章信息失败\n'#line:349
                    printlog (f'【{OOO00OO0000O00OO0.index}】:获取文章信息失败')#line:350
                    break #line:351
                if len (str (OO00000OOOOOO0OO0 ))<5 :#line:352
                    if O0OOO000OOO0O0O0O ==3 :#line:353
                        if sendable :#line:354
                            send ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',f'【{OOO00OO0000O00OO0.index}】 美添赚过检测',)#line:357
                        if pushable :#line:358
                            push ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束\n点击阅读检测文章',f'【{OOO00OO0000O00OO0.index}】 美添赚过检测',)#line:361
                        break #line:362
                    if sendable :#line:363
                        send (OOO000OO0O0OOOO00 .get ('text'),f'【{OOO00OO0000O00OO0.index}】{OOO00OO0000O00OO0.nickname} 美添赚过检测',O00O000OO000OO0O0 )#line:364
                    if pushable :#line:365
                        push (f'【{OOO00OO0000O00OO0.index}】{OOO00OO0000O00OO0.nickname} 本轮任务数量{len(O0O00OO0OO0O000OO) - 1}\n点击阅读检测文章\n{OOO000OO0O0OOOO00["text"]}',f'【{OOO00OO0000O00OO0.index}】 {OOO00OO0000O00OO0.nickname}美添赚过检测',O00O000OO000OO0O0 ,OOO00OO0000O00OO0 .uid )#line:369
                    OOO00OO0000O00OO0 .msg +='发送通知，暂停50秒\n'#line:370
                    printlog (f'【{OOO00OO0000O00OO0.index}】:发送通知，暂停50秒')#line:371
                    O0OOO000OOO0O0O0O +=1 #line:372
                    time .sleep (50 )#line:373
                OOO00OOO0OO0OOO0O =random .randint (7 ,10 )#line:374
                time .sleep (OOO00OOO0OO0OOO0O )#line:375
                O0OOO000OO00OOOOO ='https://api.wanjd.cn/wxread/articles/three_read'#line:376
                OO000O00O0O0OOOOO =requests .post (O0OOO000OO00OOOOO ,headers =OOOO0O0O0O0OO0OOO ,json =OO0O000O0OO00OOO0 ).json ()#line:377
                if OO000O00O0O0OOOOO .get ('code')==200 :#line:378
                    OOO00OO0000O00OO0 .msg +='阅读成功'+'\n'+'-'*50 +'\n'#line:379
                    printlog (f'【{OOO00OO0000O00OO0.index}】:阅读成功')#line:380
                if OO000O00O0O0OOOOO .get ('code')!=200 :#line:381
                    OOO00OO0000O00OO0 .msg +=OO000O00O0O0OOOOO .get ('message')+'\n'+'-'*50 +'\n'#line:382
                    printlog (f'【{OOO00OO0000O00OO0.index}】:{OO000O00O0O0OOOOO.get("message")}')#line:383
                    break #line:384
        O0OOO000OO00OOOOO ='https://api.wanjd.cn/wxread/articles/check_success'#line:385
        OO0O000O0OO00OOO0 ={'type':1 ,'href':OOO00OO0000O00OO0 .link }#line:386
        OO000O00O0O0OOOOO =requests .post (O0OOO000OO00OOOOO ,headers =OOOO0O0O0O0OO0OOO ,json =OO0O000O0OO00OOO0 ).json ()#line:387
        debugger (f'check {OO000O00O0O0OOOOO}')#line:388
        OOO00OO0000O00OO0 .msg +=OO000O00O0O0OOOOO .get ('message')+'\n'#line:389
        printlog (f'【{OOO00OO0000O00OO0.index}】:{OO000O00O0O0OOOOO.get("message")}')#line:390
    def withdraw (O0OOOO0000OO0000O ):#line:392
        if O0OOOO0000OO0000O .points <txbz :#line:393
            O0OOOO0000OO0000O .msg +=f'没有达到你设置的提现标准{txbz}\n'#line:394
            printlog (f'【{O0OOOO0000OO0000O.index}】:没有达到你设置的提现标准{txbz}')#line:395
            return False #line:396
        OOO0O00OOOOOOO00O ='http://api.mengmorwpt1.cn/h5_share/user/withdraw'#line:397
        O0O000OOO00000000 =O0OOOO0000OO0000O .s .post (OOO0O00OOOOOOO00O ).json ()#line:398
        O0OOOO0000OO0000O .msg +='提现结果'+O0O000OOO00000000 .get ('message')+'\n'#line:399
        printlog (f'【{O0OOOO0000OO0000O.index}】:提现结果 {O0O000OOO00000000.get("message")}')#line:400
        if O0O000OOO00000000 .get ('code')==200 :#line:401
            if sendable :#line:402
                send (f'【{O0OOOO0000OO0000O.index}】:已提现到红包，请在服务通知内及时领取','每天赚提现通知')#line:403
            if pushable :#line:404
                push (f'【{O0OOOO0000OO0000O.index}】:已提现到红包，请在服务通知内及时领取','每天赚提现通知','https://jihulab.com/xizhiai/xiaoym',O0OOOO0000OO0000O .uid )#line:406
    def run (OOO0O0OO0OO000O00 ):#line:408
        OOO0O0OO0OO000O00 .msg +='*'*50 +f'\n【{OOO0O0OO0OO000O00.index}】:开始任务\n'#line:409
        printlog (f'【{OOO0O0OO0OO000O00.index}】:开始任务')#line:410
        OOO0O0OO0OO000O00 .init ()#line:411
        if not OOO0O0OO0OO000O00 .user_info ():#line:412
            return False #line:413
        if OOO0O0OO0OO000O00 .get_read ():#line:414
            OOO0O0OO0OO000O00 .dotasks ()#line:415
            OOO0O0OO0OO000O00 .user_info ()#line:416
        OOO0O0OO0OO000O00 .withdraw ()#line:417
        printlog (f'【{OOO0O0OO0OO000O00.index}】:任务结束')#line:418
        if not printf :#line:419
            print (OOO0O0OO0OO000O00 .msg .strip ())#line:420
            print (f'【{OOO0O0OO0OO000O00.index}】:任务结束')#line:421
def yd (OO0OO000OO00O0O0O ):#line:424
    while not OO0OO000OO00O0O0O .empty ():#line:425
        OOOOOOO000O0O0O00 =OO0OO000OO00O0O0O .get ()#line:426
        OOOOO0OO0O0000000 =MTZYD (OOOOOOO000O0O0O00 )#line:427
        OOOOO0OO0O0000000 .run ()#line:428
def get_info ():#line:431
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:433
    print ('入口：http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552')#line:434
    O000000O000OO00OO ='V2.4.0'#line:435
    O0O000O0000OO000O =_OOOOO0000OOOOOO0O ['version']['k_mtz_beta']#line:436
    print (f'当前版本{O000000O000OO00OO}，仓库版本{O0O000O0000OO000O}\n{_OOOOO0000OOOOOO0O["update_log"]["每天赚beta"]}')#line:437
    if O000000O000OO00OO <O0O000O0000OO000O :#line:438
        print ('请到仓库下载最新版本k_mtz_beta.py')#line:439
    print ("="*25 )#line:440
def main ():#line:443
    get_info ()#line:444
    OO0OO0O0O00OO000O =os .getenv ('mtzck')#line:445
    if not OO0OO0O0O00OO000O :#line:446
        print (_OOOOO0000OOOOOO0O .get ('msg')['每天赚beta'])#line:447
        exit ()#line:448
    O0OO0O0O0O0O00O0O =Queue ()#line:449
    OOOO0OOO00O0OOO0O =[]#line:450
    OO0OO0O0O00OO000O =OO0OO0O0O00OO000O .replace ('&','\n').split ('\n')#line:451
    for OOOOO0OOO000OO000 ,O00000OO0OOOOOOOO in enumerate (OO0OO0O0O00OO000O ,start =1 ):#line:452
        O0OO0O0O0O0O00O0O .put (O00000OO0OOOOOOOO )#line:453
    for OOOOO0OOO000OO000 in range (max_workers ):#line:454
        OOO0OOOOOO0000000 =threading .Thread (target =yd ,args =(O0OO0O0O0O0O00O0O ,))#line:455
        OOO0OOOOOO0000000 .start ()#line:456
        OOOO0OOO00O0OOO0O .append (OOO0OOOOOO0000000 )#line:457
        time .sleep (delay_time )#line:458
    for OO0O0O0OO0O0O00O0 in OOOO0OOO00O0OOO0O :#line:459
        OO0O0O0OO0O0O00O0 .join ()#line:460
if __name__ =='__main__':#line:463
    main ()#line:464
