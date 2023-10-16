# -*- coding: utf-8 -*-
# k_xyy
# Author: 惜之酱
"""
new Env('小阅阅');
先运行脚本，有问题到群里问 http://t.me/xizhiaigroup
"""
try:
    from config import xyy_config
except:
    xyy_config = {
        'printf': 1,  # 实时日志开关 1为开，0为关
        'debug': 0,  # debug模式开关 1为开，打印调试日志；0为关，不打印
        'max_workers': 5,  # 线程数量设置 设置为5，即最多有5个任务同时进行
        'txbz': 8000,  # 设置提现标准 不低于3000，平台标准为3000 设置为8000，即为8毛起提
        'sendable': 1,  # 企业微信推送开关 1开0关
        'pushable': 1,  # wxpusher推送开关 1开0关
        'delay_time': 20  # 并发延迟设置 设置为20即每隔20秒新增一个号做任务，直到数量达到max_workers
    }

import datetime
import hashlib
import threading
import ast
import json
import os
import random
import re
from queue import Queue
import requests
import time
from urllib.parse import urlparse, parse_qs
def get_msg ():#line:36
    O0O0OO00OOO0OO000 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:38
    O0000O0O0OOOOO00O =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O0O0OO00OOO0OO000 ).json ()#line:39
    return O0000O0O0OOOOO00O #line:40
_O00OOO00O0OOO0O00 =get_msg ()#line:43
try :#line:44
    from lxml import etree #line:45
except :#line:46
    print (_O00OOO00O0OOO0O00 .get ('help')['lxml'])#line:47
printf =xyy_config ['printf']#line:48
debug =xyy_config ['debug']#line:49
max_workers =xyy_config ['max_workers']#line:50
txbz =xyy_config ['txbz']#line:51
sendable =xyy_config ['sendable']#line:52
pushable =xyy_config ['pushable']#line:53
delay_time =xyy_config ['delay_time']#line:54
if sendable :#line:55
    qwbotkey =os .getenv ('qwbotkey')#line:56
    if not qwbotkey :#line:57
        print (_O00OOO00O0OOO0O00 .get ('help')['qwbotkey'])#line:58
        exit ()#line:59
if pushable :#line:61
    pushconfig =os .getenv ('pushconfig')#line:62
    if not pushconfig :#line:63
        print (_O00OOO00O0OOO0O00 .get ('help')['pushconfig'])#line:64
        exit ()#line:65
    try :#line:66
        pushconfig =ast .literal_eval (pushconfig )#line:67
    except :#line:68
        pass #line:69
    if isinstance (pushconfig ,dict ):#line:70
        appToken =pushconfig ['appToken']#line:71
        uids =pushconfig ['uids']#line:72
        topicids =pushconfig ['topicids']#line:73
    else :#line:74
        try :#line:75
            "appToken=AT_pCenRjs;uids=['UID_9MZ','UID_T4xlqWx9x'];topicids=['xxx']"#line:76
            appToken =pushconfig .split (';')[0 ].split ('=')[1 ]#line:77
            uids =ast .literal_eval (pushconfig .split (';')[1 ].split ('=')[1 ])#line:78
            topicids =ast .literal_eval (pushconfig .split (';')[2 ].split ('=')[1 ])#line:79
        except :#line:80
            print (_O00OOO00O0OOO0O00 .get ('help')['pushconfig'])#line:81
            exit ()#line:82
if not pushable and not sendable :#line:83
    print ('啥通知方式都不配置，你想上天吗')#line:84
    exit ()#line:85
checklist =['MzIxOTY1ODcyNA==','MzI2ODcxNzc5NA==','MzA5NzI2NjI1NA==','MzkzODE5NTQwNQ==','MzkxNTE3MzQ4MQ==','Mzg5MjM0MDEwNw==','MzUzODY4NzE2OQ==','MzkyMjE3MzYxMg==','MzkxNjMwNDIzOA==','Mzg3NzUxMjc5Mg==','Mzg4NTcwODE1NA==','Mzk0ODIxODE4OQ==','Mzg2NjUyMjI1NA==','MzIzMDczODg4Mw==','Mzg5ODUyMzYzMQ==','MzU0NzI5Mjc4OQ==','Mzg5MDgxODAzMg==','MjM5MDQzNTMwMQ==','MzkzMjM3OTAxMQ==','MjM5NTE4NTg3Mg==']#line:90
def ftime ():#line:93
    O0O0O0OO0OO0O0O00 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:94
    return O0O0O0OO0OO0O0O00 #line:95
def debugger (O0O0OO0O00OO0OOOO ):#line:98
    if debug :#line:99
        print (O0O0OO0O00OO0OOOO )#line:100
def printlog (O00000OO0O0O00O0O ):#line:103
    if printf :#line:104
        print (O00000OO0O0O00O0O )#line:105
def send (OO0OO0OO0000OOO00 ,title ='通知',url =None ):#line:108
    if not url :#line:109
        O000OOO0O00OO0OOO ={"msgtype":"text","text":{"content":f"{title}\n\n{OO0OO0OO0000OOO00}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:116
    else :#line:117
        O000OOO0O00OO0OOO ={"msgtype":"news","news":{"articles":[{"title":title ,"description":OO0OO0OO0000OOO00 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:122
    OOO000000OO000000 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:123
    OOO0OO0000OOO00OO =requests .post (OOO000000OO000000 ,data =json .dumps (O000OOO0O00OO0OOO )).json ()#line:124
    if OOO0OO0000OOO00OO .get ('errcode')!=0 :#line:125
        print ('消息发送失败，请检查key和发送格式')#line:126
        return False #line:127
    return OOO0OO0000OOO00OO #line:128
def push (OOO0O0O0000000O0O ,title ='通知',url ='',uid =None ):#line:131
    if uid :#line:132
        uids .append (uid )#line:133
    OO0O00O0O0O0O000O ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',OOO0O0O0000000O0O ).replace ('url',url )#line:135
    OO00000O0O000OOOO ={"appToken":appToken ,"content":OO0O00O0O0O0O000O ,"summary":title ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:145
    OOOOO000O0OO0OOOO ='http://wxpusher.zjiecode.com/api/send/message'#line:146
    O00O0OO0O00000O0O =requests .post (url =OOOOO000O0OO0OOOO ,json =OO00000O0O000OOOO ).json ()#line:147
    if O00O0OO0O00000O0O .get ('code')!=1000 :#line:148
        print (O00O0OO0O00000O0O .get ('msg'),O00O0OO0O00000O0O )#line:149
    return O00O0OO0O00000O0O #line:150
def getmpinfo (O0OO0O0O0OOO000O0 ):#line:153
    if not O0OO0O0O0OOO000O0 or O0OO0O0O0OOO000O0 =='':#line:154
        return False #line:155
    O000OO00O00O0000O ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:157
    OO0OO0OOO00O000O0 =requests .get (O0OO0O0O0OOO000O0 ,headers =O000OO00O00O0000O )#line:158
    O00O00OOO00O000O0 =etree .HTML (OO0OO0OOO00O000O0 .text )#line:159
    O000000O0OO0OOO0O =O00O00OOO00O000O0 .xpath ('//meta[@*="og:title"]/@content')#line:160
    if O000000O0OO0OOO0O :#line:161
        O000000O0OO0OOO0O =O000000O0OO0OOO0O [0 ]#line:162
    try :#line:163
        if 'biz='in O0OO0O0O0OOO000O0 :#line:164
            O0O0OOOOOO0OO0O00 =re .findall (r'biz=(.*?)&',O0OO0O0O0OOO000O0 )[0 ]#line:165
        else :#line:166
            OO0OOO0OOOO0000OO =O00O00OOO00O000O0 .xpath ('//meta[@*="og:url"]/@content')[0 ]#line:167
            O0O0OOOOOO0OO0O00 =re .findall (r'biz=(.*?)&',str (OO0OOO0OOOO0000OO ))[0 ]#line:168
    except :#line:169
        return False #line:170
    O00OO0O0000OO0OO0 =O00O00OOO00O000O0 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:171
    if O00OO0O0000OO0OO0 :#line:172
        O00OO0O0000OO0OO0 =O00OO0O0000OO0OO0 [0 ].strip ()#line:173
    O0000OO0OOO00000O =re .findall (r"user_name.DATA'\) : '(.*?)'",OO0OO0OOO00O000O0 .text )or O00O00OOO00O000O0 .xpath ('//span[@class="profile_meta_value"]/text()')#line:175
    if O0000OO0OOO00000O :#line:176
        O0000OO0OOO00000O =O0000OO0OOO00000O [0 ]#line:177
    O0OOOOOO000OO0000 =re .findall (r'createTime = \'(.*)\'',OO0OO0OOO00O000O0 .text )#line:178
    if O0OOOOOO000OO0000 :#line:179
        O0OOOOOO000OO0000 =O0OOOOOO000OO0000 [0 ][5 :]#line:180
    OOO000O0O0OO0O0OO =f'{O0OOOOOO000OO0000}|{O000000O0OO0OOO0O[:8]}|{O0O0OOOOOO0OO0O00}|{O00OO0O0000OO0OO0}|{O0000OO0OOO00000O}'#line:181
    OO0O00000OOO000OO ={'biz':O0O0OOOOOO0OO0O00 ,'text':OOO000O0O0OO0O0OO }#line:182
    return OO0O00000OOO000OO #line:183
def ts ():#line:186
    return str (int (time .time ()))+'000'#line:187
def generate_md5 (O00000O0O00O0OO0O ):#line:190
    OOOOO0OOOOOO00000 =hashlib .md5 ()#line:191
    OOOOO0OOOOOO00000 .update (O00000O0O00O0OO0O .encode ('utf-8'))#line:192
    return OOOOO0OOOOOO00000 .hexdigest ()#line:193
class XYY :#line:196
    def __init__ (OOOO000OOOO0O0OOO ,O0O00OOO00O000O00 ):#line:197
        OOOO000OOOO0O0OOO .name =O0O00OOO00O000O00 ['name']#line:198
        OOOO000OOOO0O0OOO .ysm_uid =None #line:199
        OOOO000OOOO0O0OOO .last_gold =None #line:200
        OOOO000OOOO0O0OOO .uid =O0O00OOO00O000O00 .get ('uid')#line:201
        OOOO000OOOO0O0OOO .ysmuid =O0O00OOO00O000O00 .get ('ysmuid')#line:202
        OOOO000OOOO0O0OOO .sec =requests .session ()#line:203
        OOOO000OOOO0O0OOO .sec .headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Cookie':f'ysmuid={OOOO000OOOO0O0OOO.ysmuid};',}#line:208
        OOOO000OOOO0O0OOO .msg =''#line:209
    def init (OO00O00O00O00O0OO ):#line:211
        if not OO00O00O00O00O0OO .ysmuid :#line:212
            print ('ck没有ysmuid，不能运行本脚本，自动退出')#line:213
            return False #line:214
        O00O0O0O00O0OO0O0 =0 #line:215
        while O00O0O0O00O0OO0O0 <5 :#line:216
            O0OO0000OO00OOO00 =OO00O00O00O00O0OO .sec .get ('http://1697428750.jeasy.site/').text #line:217
            OO00O00O00O00O0OO .ysm_uid =re .findall (r'unionid="(o.*?)";',O0OO0000OO00OOO00 )#line:218
            if OO00O00O00O00O0OO .ysm_uid :#line:219
                OO00O00O00O00O0OO .ysm_uid =OO00O00O00O00O0OO .ysm_uid [0 ]#line:220
                O000OO0OOOO00O0OO =re .findall (r'href="(.*?)">提现',O0OO0000OO00OOO00 )#line:221
                if O000OO0OOOO00O0OO :#line:222
                    O000OO0OOOO00O0OO =O000OO0OOOO00O0OO [0 ]#line:223
                    OO0OO0O0OOO0OOOO0 =parse_qs (urlparse (O000OO0OOOO00O0OO ).query )#line:224
                    OO00O00O00O00O0OO .unionid =OO0OO0O0OOO0OOOO0 .get ('unionid')[0 ]#line:225
                    OO00O00O00O00O0OO .request_id =OO0OO0O0OOO0OOOO0 .get ('request_id')[0 ]#line:226
                    OO00O00O00O00O0OO .netloc =urlparse (O000OO0OOOO00O0OO ).netloc #line:227
                else :#line:228
                    printlog (f'【{OO00O00O00O00O0OO.name}】: 获取提现参数失败，本次不提现')#line:229
                    OO00O00O00O00O0OO .msg +=f'获取提现参数失败，本次不提现\n'#line:230
                return True #line:231
            else :#line:232
                O00O0O0O00O0OO0O0 +=1 #line:233
                continue #line:234
        printlog (f'【{OO00O00O00O00O0OO.name}】: 获取ysm_uid失败，请检查账号有效性')#line:235
        OO00O00O00O00O0OO .msg +='获取ysm_uid失败，请检查账号有效性\n'#line:236
        return False #line:237
    def something (O000O0O0O00O00OOO ):#line:239
        O0O00O0O0O0OOO0OO ='http://1695724331.umis.top/yunonline/v1/sign_info'#line:240
        OOO0O0OOO000O0O00 ={'time':ts (),'unionid':O000O0O0O00O00OOO .ysm_uid }#line:241
        O000O0O0O00O00OOO .sec .get (O0O00O0O0O0OOO0OO ,params =OOO0O0OOO000O0O00 )#line:242
        O0O00O0O0O0OOO0OO ='http://1695724331.umis.top/yunonline/v1/hasWechat'#line:243
        OOO0O0OOO000O0O00 .pop ('time')#line:244
        O000O0O0O00O00OOO .sec .get (O0O00O0O0O0OOO0OO ,params =OOO0O0OOO000O0O00 )#line:245
        O0O00O0O0O0OOO0OO ='http://1695724142.umis.top/yunonline/v1/devtouid'#line:246
        OOO0O0OOO000O0O00 .update ({'devid':generate_md5 (O000O0O0O00O00OOO .ysm_uid )})#line:247
        O000O0O0O00O00OOO .sec .post (O0O00O0O0O0OOO0OO ,data =OOO0O0OOO000O0O00 )#line:248
    def user_info (O00OOOO0O0OOOOO00 ):#line:250
        OO0000O00O0O0OO00 =f'http://1695724331.umis.top/yunonline/v1/gold?unionid={O00OOOO0O0OOOOO00.ysm_uid}&time={ts()}'#line:251
        OOOOO00000OOOO0OO =O00OOOO0O0OOOOO00 .sec .get (OO0000O00O0O0OO00 ).json ()#line:252
        debugger (f'userinfo {OOOOO00000OOOO0OO}')#line:253
        OO0O00OO0O0O0O00O =OOOOO00000OOOO0OO .get ("data")#line:254
        O00OOOO0O0OOOOO00 .last_gold =OOOOO00000OOOO0OO .get ("data").get ("last_gold")#line:255
        O000OO0OOOO00O00O =OO0O00OO0O0O0O00O .get ("remain_read")#line:256
        O0000OOOOO0OOO000 =f'今日已经阅读了{OO0O00OO0O0O0O00O.get("day_read")}篇文章,剩余{O000OO0OOOO00O00O}未阅读，今日获取金币{OO0O00OO0O0O0O00O.get("day_gold")}，剩余{O00OOOO0O0OOOOO00.last_gold}'#line:257
        printlog (f'【{O00OOOO0O0OOOOO00.name}】:{O0000OOOOO0OOO000}')#line:258
        O00OOOO0O0OOOOO00 .msg +=(O0000OOOOO0OOO000 +'\n')#line:259
        if O000OO0OOOO00O00O ==0 :#line:260
            return False #line:261
        return True #line:262
    def getKey (OOO0O00OOOO00O0OO ):#line:264
        O0000O000OOOO0000 ='http://1695724331.umis.top/yunonline/v1/wtmpdomain'#line:265
        O0O00OOOO0O0O0O0O =f'unionid={OOO0O00OOOO00O0OO.ysm_uid}'#line:266
        OOO0O0O0000O0000O =OOO0O00OOOO00O0OO .sec .post (O0000O000OOOO0000 ,data =O0O00OOOO0O0O0O0O ).json ()#line:267
        debugger (f'getkey {OOO0O0O0000O0000O}')#line:268
        O0O0OOOO0000O0O0O =OOO0O0O0000O0000O .get ('data').get ('domain')#line:269
        OOO0O00OOOO00O0OO .uk =parse_qs (urlparse (O0O0OOOO0000O0O0O ).query ).get ('uk')[0 ]#line:270
        OOO0O00OOO00OOOOO =urlparse (O0O0OOOO0000O0O0O ).netloc #line:271
        OOO0O00OOOO00O0OO .headers ={'Connection':'keep-alive','Accept':'application/json, text/javascript, */*; q=0.01','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue','Origin':f'https://{OOO0O00OOO00OOOOO}','Sec-Fetch-Site':'cross-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh',}#line:282
    def read (OO00O0O0000OO0OOO ):#line:284
        time .sleep (3 )#line:285
        O00O0OOOO0OO000O0 ={'uk':OO00O0O0000OO0OOO .uk }#line:286
        while True :#line:287
            OO00OOOO0O00OOOO0 =f'https://nsr.zsf2023e458.cloud/yunonline/v1/do_read'#line:288
            O0OOO00OOOOOOO000 =requests .get (OO00OOOO0O00OOOO0 ,headers =OO00O0O0000OO0OOO .headers ,params =O00O0OOOO0OO000O0 )#line:289
            OO00O0O0000OO0OOO .msg +=('-'*50 +'\n')#line:290
            debugger (f'read1 {O0OOO00OOOOOOO000.text}')#line:291
            O0OOO00OOOOOOO000 =O0OOO00OOOOOOO000 .json ()#line:292
            if O0OOO00OOOOOOO000 .get ('errcode')==0 :#line:293
                O0OOO000OO0OO00O0 =O0OOO00OOOOOOO000 .get ('data').get ('link')#line:294
                O000O000OOO0O0O00 =OO00O0O0000OO0OOO .jump (O0OOO000OO0OO00O0 )#line:295
                if 'mp.weixin'in O000O000OOO0O0O00 :#line:296
                    O00OO0OO00OO0OO0O =getmpinfo (O000O000OOO0O0O00 )#line:297
                    OO0OO00O0OO0OO0OO =O00OO0OO00OO0OO0O ['biz']#line:298
                    OO00O0O0000OO0OOO .msg +=('开始阅读 '+O00OO0OO00OO0OO0O ['text']+'\n')#line:299
                    printlog (f'【{OO00O0O0000OO0OOO.name}】:开始阅读 '+O00OO0OO00OO0OO0O ['text'])#line:300
                    if OO0OO00O0OO0OO0OO in checklist :#line:301
                        if sendable :#line:302
                            send (f"{O00OO0OO00OO0OO0O['text']}",title =f'【{OO00O0O0000OO0OOO.name}】: 小阅阅过检测',url =O000O000OOO0O0O00 )#line:303
                        if pushable :#line:304
                            push (f'{OO00O0O0000OO0OOO.name}\n点击阅读检测文章\n{O00OO0OO00OO0OO0O["text"]}',f'【{OO00O0O0000OO0OOO.name}】: 小阅阅过检测',O000O000OOO0O0O00 ,OO00O0O0000OO0OOO .uid )#line:306
                        OO00O0O0000OO0OOO .msg +='遇到检测文章，已发送到微信，手动阅读，暂停60秒\n'#line:307
                        printlog (f'【{OO00O0O0000OO0OOO.name}】:遇到检测文章，已发送到微信，手动阅读，暂停60秒')#line:308
                        time .sleep (60 )#line:309
                else :#line:310
                    OO00O0O0000OO0OOO .msg +=f'【{OO00O0O0000OO0OOO.name}】: 小阅阅跳转到 {O000O000OOO0O0O00}\n'#line:311
                    printlog (f'【{OO00O0O0000OO0OOO.name}】: 小阅阅跳转到 {O000O000OOO0O0O00}')#line:312
                    continue #line:313
                OO00OOOO0O00O00O0 =random .randint (7 ,10 )#line:314
                OO00O0O0000OO0OOO .msg +=f'本次模拟读{OO00OOOO0O00O00O0}秒\n'#line:315
                time .sleep (OO00OOOO0O00O00O0 )#line:316
                OO00OOOO0O00OOOO0 =f'https://nsr.zsf2023e458.cloud/yunonline/v1/get_read_gold?uk={OO00O0O0000OO0OOO.uk}&time={OO00OOOO0O00O00O0}&timestamp={ts()}'#line:317
                requests .get (OO00OOOO0O00OOOO0 ,headers =OO00O0O0000OO0OOO .headers )#line:318
            elif O0OOO00OOOOOOO000 .get ('errcode')==405 :#line:319
                printlog (f'【{OO00O0O0000OO0OOO.name}】:阅读重复')#line:320
                OO00O0O0000OO0OOO .msg +='阅读重复\n'#line:321
                time .sleep (1.5 )#line:322
            elif O0OOO00OOOOOOO000 .get ('errcode')==407 :#line:323
                printlog (f'【{OO00O0O0000OO0OOO.name}】: {O0OOO00OOOOOOO000.get("msg")}')#line:324
                OO00O0O0000OO0OOO .msg +=(O0OOO00OOOOOOO000 .get ('msg')+'\n')#line:325
                return True #line:326
            else :#line:327
                printlog (f'【{OO00O0O0000OO0OOO.name}】:{O0OOO00OOOOOOO000.get("msg")}')#line:328
                OO00O0O0000OO0OOO .msg +=(O0OOO00OOOOOOO000 .get ("msg")+'\n')#line:329
                time .sleep (1.5 )#line:330
    def jump (OOO0O0O000O0O0O0O ,OO00OO0OOOOOOOOO0 ):#line:332
        O00O0OO0OOOOO000O =urlparse (OO00OO0OOOOOOOOO0 ).netloc #line:333
        OO000OOOOOOOOOOOO ={'Host':O00O0OO0OOOOO000O ,'Connection':'keep-alive','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh','Cookie':f'ysmuid={OOO0O0O000O0O0O0O.ysmuid}',}#line:343
        O000OOOO0O0OOOO0O =requests .get (OO00OO0OOOOOOOOO0 ,headers =OO000OOOOOOOOOOOO ,allow_redirects =False )#line:344
        O0OOOO00O0OOOO00O =O000OOOO0O0OOOO0O .headers .get ('Location')#line:345
        return O0OOOO00O0OOOO00O #line:346
    def withdraw (O0OOOO0OO00OOO00O ):#line:348
        if not O0OOOO0OO00OOO00O .unionid :#line:349
            return False #line:350
        if int (O0OOOO0OO00OOO00O .last_gold )<txbz :#line:351
            printlog (f'【{O0OOOO0OO00OOO00O.name}】: 没有达到你设置的提现标准{txbz}')#line:352
            O0OOOO0OO00OOO00O .msg +=f'没有达到你设置的提现标准{txbz}\n'#line:353
            return False #line:354
        OOOOO000000OO00OO =int (int (O0OOOO0OO00OOO00O .last_gold )/1000 )*1000 #line:355
        O0OOOO0OO00OOO00O .msg +=f'本次提现金币{OOOOO000000OO00OO}\n'#line:356
        printlog (f'【{O0OOOO0OO00OOO00O.name}】:本次提现金币{OOOOO000000OO00OO}')#line:357
        if OOOOO000000OO00OO :#line:359
            OOOO0O0OO0OOO0000 =f'http://{O0OOOO0OO00OOO00O.netloc}/yunonline/v1/user_gold'#line:360
            # printlog (OOOO0O0OO0OOO0000 )#line:361
            O0O0OO00OO000OO0O =f'unionid={O0OOOO0OO00OOO00O.unionid}&request_id={O0OOOO0OO00OOO00O.request_id}&gold={OOOOO000000OO00OO}'#line:362
            OO0OOOO0OOO0O00OO =O0OOOO0OO00OOO00O .sec .post (OOOO0O0OO0OOO0000 ,data =O0O0OO00OO000OO0O )#line:363
            debugger (f'gold {OO0OOOO0OOO0O00OO.text}')#line:364
            OOOO0O0OO0OOO0000 =f'http://{O0OOOO0OO00OOO00O.netloc}/yunonline/v1/withdraw'#line:365
            O0O0OO00OO000OO0O =f'unionid={O0OOOO0OO00OOO00O.unionid}&signid={O0OOOO0OO00OOO00O.request_id}&ua=0&ptype=0&paccount=&pname='#line:366
            OO0OOOO0OOO0O00OO =O0OOOO0OO00OOO00O .sec .post (OOOO0O0OO0OOO0000 ,data =O0O0OO00OO000OO0O )#line:367
            debugger (f'withdraw {OO0OOOO0OOO0O00OO.text}')#line:368
            O0OOOO0OO00OOO00O .msg +=f"提现结果 {OO0OOOO0OOO0O00OO.json()['msg']}"#line:369
            printlog (f'【{O0OOOO0OO00OOO00O.name}】:提现结果 {OO0OOOO0OOO0O00OO.json()["msg"]}')#line:370
    def run (O00O0OOO0OOO0O000 ):#line:372
        O00O0OOO0OOO0O000 .msg +=('='*50 +f'\n账号：{O00O0OOO0OOO0O000.name}开始任务\n')#line:373
        printlog (f'【{O00O0OOO0OOO0O000.name}】:开始任务')#line:374
        if not O00O0OOO0OOO0O000 .init ():#line:375
            return False #line:376
        O00O0OOO0OOO0O000 .something ()#line:377
        if O00O0OOO0OOO0O000 .user_info ():#line:378
            O00O0OOO0OOO0O000 .getKey ()#line:379
            O00O0OOO0OOO0O000 .read ()#line:380
            O00O0OOO0OOO0O000 .user_info ()#line:381
            time .sleep (0.5 )#line:382
        O00O0OOO0OOO0O000 .withdraw ()#line:383
        printlog (f'【{O00O0OOO0OOO0O000.name}】:本轮任务结束')#line:384
        if not printf :#line:385
            print (O00O0OOO0OOO0O000 .msg )#line:386
def yd (OOOOO000O0O00O000 ):#line:389
    while not OOOOO000O0O00O000 .empty ():#line:390
        O0OOO0O000O0O0000 =OOOOO000O0O00O000 .get ()#line:391
        OOO0O00000OO00O00 =XYY (O0OOO0O000O0O0000 )#line:392
        OOO0O00000OO00O00 .run ()#line:393
def get_info ():#line:396
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:398
    print ('入口：http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552')#line:399
    OO00OO000000OO000 ='v2.4.2'#line:400
    O0OO0OOO000O0O00O =_O00OOO00O0OOO0O00 ['version']['小阅阅']#line:401
    print (f'当前版本{OO00OO000000OO000}，仓库版本{O0OO0OOO000O0O00O}\n{_O00OOO00O0OOO0O00["update_log"]["小阅阅"]}')#line:402
    if OO00OO000000OO000 <O0OO0OOO000O0O00O :#line:403
        print ('请到仓库下载最新版本k_xyy.py')#line:404
    print ("="*25 )#line:405
def main ():#line:408
    get_info ()#line:409
    O0O0OO0O00O0000OO =os .getenv ('xyyck')#line:410
    if not O0O0OO0O00O0000OO :#line:411
        print (_O00OOO00O0OOO0O00 .get ('msg')['小阅阅'])#line:412
        exit ()#line:413
    try :#line:414
        O0O0OO0O00O0000OO =ast .literal_eval (O0O0OO0O00O0000OO )#line:415
    except :#line:416
        pass #line:417
    O0OO0O0O00O0000OO =[]#line:418
    O000O0OOO000OO000 =Queue ()#line:419
    printlog (f'共获取到{len(O0O0OO0O00O0000OO)}个账号，如不正确，请检查ck填写格式')#line:420
    for O0OOOOOOOO0O0OO00 ,O00O000OOOO000OO0 in enumerate (O0O0OO0O00O0000OO ,start =1 ):#line:421
        O000O0OOO000OO000 .put (O00O000OOOO000OO0 )#line:422
    for O0OOOOOOOO0O0OO00 in range (max_workers ):#line:423
        O00O0000O00O0000O =threading .Thread (target =yd ,args =(O000O0OOO000OO000 ,))#line:424
        O00O0000O00O0000O .start ()#line:425
        O0OO0O0O00O0000OO .append (O00O0000O00O0000O )#line:426
        time .sleep (delay_time )#line:427
    for O000OOO0OO0OO0O0O in O0OO0O0O00O0000OO :#line:428
        O000OOO0OO0OO0O0O .join ()#line:429
if __name__ =='__main__':#line:432
    main ()#line:433