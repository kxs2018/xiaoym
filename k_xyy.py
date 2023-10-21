# -*- coding: utf-8 -*-
# k_xyy
# Author: 惜之酱
"""
new Env('小阅阅');
先运行脚本，有问题到群里问 http://t.me/xiaoymgroup
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
    OO000OO0OO0O0O0OO ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:38
    OO0O0OO0OO00OO0OO =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OO000OO0OO0O0O0OO ).json ()#line:39
    return OO0O0OO0OO00OO0OO #line:40
_OOOO0OO0O00O0O0O0 =get_msg ()#line:43
try :#line:44
    from lxml import etree #line:45
except :#line:46
    print (_OOOO0OO0O00O0O0O0 .get ('help')['lxml'])#line:47
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
        print (_OOOO0OO0O00O0O0O0 .get ('help')['qwbotkey'])#line:58
        exit ()#line:59
if pushable :#line:61
    pushconfig =os .getenv ('pushconfig')#line:62
    if not pushconfig :#line:63
        print (_OOOO0OO0O00O0O0O0 .get ('help')['pushconfig'])#line:64
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
            print (_OOOO0OO0O00O0O0O0 .get ('help')['pushconfig'])#line:81
            exit ()#line:82
if not pushable and not sendable :#line:83
    print ('⛔️啥通知方式都不配置，你想上天吗')#line:84
    exit ()#line:85
def ftime ():#line:88
    O0OO00O0O0OO0OOOO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:89
    return O0OO00O0O0OO0OOOO #line:90
def debugger (O00OOO00000000O0O ):#line:93
    if debug :#line:94
        print (O00OOO00000000O0O )#line:95
def printlog (OO0O0O0000OOOO0OO ):#line:98
    if printf :#line:99
        print (OO0O0O0000OOOO0OO )#line:100
def send (OOOOO00O000OO0O00 ,title ='通知',url =None ):#line:103
    if not url :#line:104
        OO0000OOO00OO0OOO ={"msgtype":"text","text":{"content":f"{title}\n\n{OOOOO00O000OO0O00}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:111
    else :#line:112
        OO0000OOO00OO0OOO ={"msgtype":"news","news":{"articles":[{"title":title ,"description":OOOOO00O000OO0O00 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:117
    O0O0OO0O0OO00000O =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:118
    O00O0000O0O00OOOO =requests .post (O0O0OO0O0OO00000O ,data =json .dumps (OO0000OOO00OO0OOO )).json ()#line:119
    if O00O0000O0O00OOOO .get ('errcode')!=0 :#line:120
        print ('消息发送失败，请检查key和发送格式')#line:121
        return False #line:122
    return O00O0000O0O00OOOO #line:123
def push (O00OO0OO00OOOOOO0 ,title ='通知',url ='',uid =None ):#line:126
    if uid :#line:127
        uids .append (uid )#line:128
    O000O0OOOOO0O0OO0 ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',O00OO0OO00OOOOOO0 ).replace ('url',url )#line:130
    OO0OO0O0O0O000O0O ={"appToken":appToken ,"content":O000O0OOOOO0O0OO0 ,"summary":title ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:140
    O00OOOOO000OOOOOO ='http://wxpusher.zjiecode.com/api/send/message'#line:141
    O00000OO0O0O0O0O0 =requests .post (url =O00OOOOO000OOOOOO ,json =OO0OO0O0O0O000O0O ).json ()#line:142
    if O00000OO0O0O0O0O0 .get ('code')!=1000 :#line:143
        print (O00000OO0O0O0O0O0 .get ('msg'),O00000OO0O0O0O0O0 )#line:144
    return O00000OO0O0O0O0O0 #line:145
def getmpinfo (O0O00O0OOO00O000O ):#line:148
    if not O0O00O0OOO00O000O or O0O00O0OOO00O000O =='':#line:149
        return False #line:150
    O0O0OO00O0OO00O00 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:152
    OOOO0O00O00OOO00O =requests .get (O0O00O0OOO00O000O ,headers =O0O0OO00O0OO00O00 )#line:153
    OOO0OO0O000OOO0OO =etree .HTML (OOOO0O00O00OOO00O .text )#line:154
    O0O0O000OOO0O00OO =OOO0OO0O000OOO0OO .xpath ('//meta[@*="og:title"]/@content')#line:155
    if O0O0O000OOO0O00OO :#line:156
        O0O0O000OOO0O00OO =O0O0O000OOO0O00OO [0 ]#line:157
    try :#line:158
        if 'biz='in O0O00O0OOO00O000O :#line:159
            OO0000000O0OO0OOO =re .findall (r'biz=(.*?)&',O0O00O0OOO00O000O )[0 ]#line:160
        else :#line:161
            OOOOOO0OOO0O0OO00 =OOO0OO0O000OOO0OO .xpath ('//meta[@*="og:url"]/@content')[0 ]#line:162
            OO0000000O0OO0OOO =re .findall (r'biz=(.*?)&',str (OOOOOO0OOO0O0OO00 ))[0 ]#line:163
    except :#line:164
        return False #line:165
    OO0OOOO00O000O0O0 =OOO0OO0O000OOO0OO .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:166
    if OO0OOOO00O000O0O0 :#line:167
        OO0OOOO00O000O0O0 =OO0OOOO00O000O0O0 [0 ].strip ()#line:168
    OOO00000OO0O00OO0 =re .findall (r"user_name.DATA'\) : '(.*?)'",OOOO0O00O00OOO00O .text )or OOO0OO0O000OOO0OO .xpath ('//span[@class="profile_meta_value"]/text()')#line:170
    if OOO00000OO0O00OO0 :#line:171
        OOO00000OO0O00OO0 =OOO00000OO0O00OO0 [0 ]#line:172
    OOOOOO0OOO0OOO0O0 =re .findall (r'createTime = \'(.*)\'',OOOO0O00O00OOO00O .text )#line:173
    if OOOOOO0OOO0OOO0O0 :#line:174
        OOOOOO0OOO0OOO0O0 =OOOOOO0OOO0OOO0O0 [0 ][5 :]#line:175
    O000OOO00O0O000OO =f'{OOOOOO0OOO0OOO0O0}|{O0O0O000OOO0O00OO[:8]}|{OO0000000O0OO0OOO}|{OO0OOOO00O000O0O0}|{OOO00000OO0O00OO0}'#line:176
    OO00O00O000OOOOO0 ={'biz':OO0000000O0OO0OOO ,'username':OO0OOOO00O000O0O0 ,'text':O000OOO00O0O000OO }#line:177
    return OO00O00O000OOOOO0 #line:178
def ts ():#line:181
    return str (int (time .time ()))+'000'#line:182
def generate_md5 (O00OO0O0O0O000OO0 ):#line:185
    O0O0OOO000O0O0OOO =hashlib .md5 ()#line:186
    O0O0OOO000O0O0OOO .update (O00OO0O0O0O000OO0 .encode ('utf-8'))#line:187
    return O0O0OOO000O0O0OOO .hexdigest ()#line:188
try :#line:191
    with open ('xyy_check.json','r',encoding ='utf-8')as f :#line:192
        checkdict =json .loads (f .read ())#line:193
        print ('✅获取检测号信息成功，请到https://t.me/xiaoymgroup获取最新检测号文件')#line:194
except :#line:195
    print ('⛔️没有找到检测号字典，请到https://t.me/xiaoymgroup获取最新检测号文件，程序退出')#line:196
    exit ()#line:197
class XYY :#line:200
    def __init__ (O0OO0O0000OOO00O0 ,O00O00OOO00OO0OOO ):#line:201
        O0OO0O0000OOO00O0 .name =O00O00OOO00OO0OOO ['name']#line:202
        O0OO0O0000OOO00O0 .ysm_uid =None #line:203
        O0OO0O0000OOO00O0 .last_gold =None #line:204
        O0OO0O0000OOO00O0 .un =None #line:205
        O0OO0O0000OOO00O0 .biz =None #line:206
        O0OO0O0000OOO00O0 .uid =O00O00OOO00OO0OOO .get ('uid')#line:207
        O0OO0O0000OOO00O0 .ysmuid =O00O00OOO00OO0OOO .get ('ysmuid')#line:208
        O0OO0O0000OOO00O0 .sec =requests .session ()#line:209
        O0OO0O0000OOO00O0 .sec .headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Cookie':f'ysmuid={O0OO0O0000OOO00O0.ysmuid};',}#line:214
        O0OO0O0000OOO00O0 .host =O0OO0O0000OOO00O0 .get_host ()#line:215
        O0OO0O0000OOO00O0 .msg =''#line:216
    @staticmethod #line:218
    def get_host ():#line:219
        OOO00OO0OOOO00O0O ='https://ot34022.khdsfa.top:10251/yunonline/v1/auth/6d288b175355d987746598c6c11c0227'#line:220
        OOO00O0O000OO00OO ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309071d) XWEB/8447 Flue'}#line:222
        O000OOO0OO0OOOOO0 =requests .get (OOO00OO0OOOO00O0O ,headers =OOO00O0O000OO00OO ,allow_redirects =False )#line:223
        OO0OOOOO0OO00OO00 =O000OOO0OO0OOOOO0 .headers .get ('Location')#line:224
        O00O0OO0O00O0O0O0 =urlparse (OO0OOOOO0OO00OO00 ).netloc #line:225
        return 'http://'+O00O0OO0O00O0O0O0 #line:226
    def init (OOO0OOO00O00O00OO ):#line:228
        if not OOO0OOO00O00O00OO .ysmuid :#line:229
            print ('⛔️ck没有ysmuid，不能运行本脚本，自动退出')#line:230
            return False #line:231
        OO0O0O0OOOO0OO000 =0 #line:232
        while OO0O0O0OOOO0OO000 <5 :#line:233
            OO00000OOOO00O0O0 =OOO0OOO00O00O00OO .sec .get (OOO0OOO00O00O00OO .host ).text #line:234
            OOO0OOO00O00O00OO .ysm_uid =re .findall (r'unionid="(o.*?)";',OO00000OOOO00O0O0 )#line:235
            if OOO0OOO00O00O00OO .ysm_uid :#line:236
                OOO0OOO00O00O00OO .ysm_uid =OOO0OOO00O00O00OO .ysm_uid [0 ]#line:237
                OOO0O00O000O00O0O =re .findall (r'href="(.*?)">提现',OO00000OOOO00O0O0 )#line:238
                if OOO0O00O000O00O0O :#line:239
                    OOO0O00O000O00O0O =OOO0O00O000O00O0O [0 ]#line:240
                    O0O0O00OO0OOOO000 =parse_qs (urlparse (OOO0O00O000O00O0O ).query )#line:241
                    OOO0OOO00O00O00OO .unionid =O0O0O00OO0OOOO000 .get ('unionid')[0 ]#line:242
                    OOO0OOO00O00O00OO .request_id =O0O0O00OO0OOOO000 .get ('request_id')[0 ]#line:243
                else :#line:244
                    printlog (f'【{OOO0OOO00O00O00OO.name}】: ⛔️获取提现参数失败，本次不提现')#line:245
                    OOO0OOO00O00O00OO .msg +=f'⛔️获取提现参数失败，本次不提现\n'#line:246
                return True #line:247
            else :#line:248
                OO0O0O0OOOO0OO000 +=1 #line:249
                continue #line:250
        printlog (f'【{OOO0OOO00O00O00OO.name}】: ⛔️获取ysm_uid失败，请检查账号有效性')#line:251
        OOO0OOO00O00O00OO .msg +='⛔️获取ysm_uid失败，请检查账号有效性\n'#line:252
        return False #line:253
    def something (O0OOO0000OOO00O00 ):#line:255
        OO00OOOO0O000O0OO =f'{O0OOO0000OOO00O00.host}/yunonline/v1/sign_info'#line:256
        OOOO0O0OOO0O000O0 ={'time':ts (),'unionid':O0OOO0000OOO00O00 .ysm_uid }#line:257
        O0OOO0000OOO00O00 .sec .get (OO00OOOO0O000O0OO ,params =OOOO0O0OOO0O000O0 )#line:258
        OO00OOOO0O000O0OO =f'{O0OOO0000OOO00O00.host}/yunonline/v1/hasWechat'#line:259
        OOOO0O0OOO0O000O0 .pop ('time')#line:260
        O0OOO0000OOO00O00 .sec .get (OO00OOOO0O000O0OO ,params =OOOO0O0OOO0O000O0 )#line:261
        OO00OOOO0O000O0OO =f'{O0OOO0000OOO00O00.host}/yunonline/v1/devtouid'#line:262
        OOOO0O0OOO0O000O0 .update ({'devid':generate_md5 (O0OOO0000OOO00O00 .ysm_uid )})#line:263
        O0OOO0000OOO00O00 .sec .post (OO00OOOO0O000O0OO ,data =OOOO0O0OOO0O000O0 )#line:264
    def user_info (OOOOO00OO0O0OO000 ):#line:266
        O0OO0OOOO0OO0O0OO =f'{OOOOO00OO0O0OO000.host}/yunonline/v1/gold?unionid={OOOOO00OO0O0OO000.ysm_uid}&time={ts()}'#line:267
        O00OOO000O0O0O00O =OOOOO00OO0O0OO000 .sec .get (O0OO0OOOO0OO0O0OO ).json ()#line:268
        debugger (f'userinfo {O00OOO000O0O0O00O}')#line:269
        O00OOOOOO0O0000OO =O00OOO000O0O0O00O .get ("data")#line:270
        OOOOO00OO0O0OO000 .last_gold =O00OOO000O0O0O00O .get ("data").get ("last_gold")#line:271
        OOOOO000O0000OO0O =O00OOOOOO0O0000OO .get ("remain_read")#line:272
        OO0O000OOO00000OO =f'今日已经阅读了{O00OOOOOO0O0000OO.get("day_read")}篇文章,剩余{OOOOO000O0000OO0O}未阅读，今日获取金币{O00OOOOOO0O0000OO.get("day_gold")}，剩余{OOOOO00OO0O0OO000.last_gold}'#line:273
        printlog (f'【{OOOOO00OO0O0OO000.name}】:{OO0O000OOO00000OO}')#line:274
        OOOOO00OO0O0OO000 .msg +=(OO0O000OOO00000OO +'\n')#line:275
        if OOOOO000O0000OO0O ==0 :#line:276
            return False #line:277
        return True #line:278
    def getKey (O0OO0O0OOO000OOO0 ):#line:280
        O0OOO00000000O000 =f'{O0OO0O0OOO000OOO0.host}/yunonline/v1/wtmpdomain'#line:281
        O000OO0O00O0OO0O0 =f'unionid={O0OO0O0OOO000OOO0.ysm_uid}'#line:282
        OOOO000OOO00O00OO =O0OO0O0OOO000OOO0 .sec .post (O0OOO00000000O000 ,data =O000OO0O00O0OO0O0 ).json ()#line:283
        debugger (f'getkey {OOOO000OOO00O00OO}')#line:284
        OO000000OOOOO0OOO =OOOO000OOO00O00OO .get ('data').get ('domain')#line:285
        O0OO0O0OOO000OOO0 .uk =parse_qs (urlparse (OO000000OOOOO0OOO ).query ).get ('uk')[0 ]#line:286
        OOO00OOO0O00OO000 =urlparse (OO000000OOOOO0OOO ).netloc #line:287
        O0OO0O0OOO000OOO0 .headers ={'Connection':'keep-alive','Accept':'application/json, text/javascript, */*; q=0.01','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue','Origin':f'https://{OOO00OOO0O00OO000}','Sec-Fetch-Site':'cross-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh',}#line:298
    def read (OOOOOO0000OOOOOO0 ):#line:300
        time .sleep (3 )#line:301
        O00O000OOO000000O ={'uk':OOOOOO0000OOOOOO0 .uk }#line:302
        while True :#line:303
            O000OO0OO0O0OOO0O =f'https://nsr.zsf2023e458.cloud/yunonline/v1/do_read'#line:304
            OOOOOO0000OOO00OO =requests .get (O000OO0OO0O0OOO0O ,headers =OOOOOO0000OOOOOO0 .headers ,params =O00O000OOO000000O )#line:305
            OOOOOO0000OOOOOO0 .msg +=('-'*50 +'\n')#line:306
            debugger (f'read1 {OOOOOO0000OOO00OO.text}')#line:307
            OOOOOO0000OOO00OO =OOOOOO0000OOO00OO .json ()#line:308
            if OOOOOO0000OOO00OO .get ('errcode')==0 :#line:309
                OO0OO00OOO00O000O =OOOOOO0000OOO00OO .get ('data').get ('link')#line:310
                OOOO0OOOO00O0OOOO =OOOOOO0000OOOOOO0 .jump (OO0OO00OOO00O000O )#line:311
                if 'mp.weixin'in OOOO0OOOO00O0OOOO :#line:312
                    OO0OO0OOO000O0OO0 =getmpinfo (OOOO0OOOO00O0OOOO )#line:313
                    OOOOOO0000OOOOOO0 .biz =OO0OO0OOO000O0OO0 ['biz']#line:314
                    OOOOOO0000OOOOOO0 .un =OO0OO0OOO000O0OO0 ['username']#line:315
                    OOOOOO0000OOOOOO0 .msg +=('开始阅读 '+OO0OO0OOO000O0OO0 ['text']+'\n')#line:316
                    printlog (f'【{OOOOOO0000OOOOOO0.name}】:开始阅读 '+OO0OO0OOO000O0OO0 ['text'])#line:317
                    if OOOOOO0000OOOOOO0 .biz in checkdict .keys ():#line:318
                        if sendable :#line:319
                            send (f"{OO0OO0OOO000O0OO0['text']}",title =f'【{OOOOOO0000OOOOOO0.name}】: 小阅阅过检测',url =OOOO0OOOO00O0OOOO )#line:320
                        if pushable :#line:321
                            push (f'{OOOOOO0000OOOOOO0.name}\n点击阅读检测文章\n{OO0OO0OOO000O0OO0["text"]}',f'【{OOOOOO0000OOOOOO0.name}】: 小阅阅过检测',OOOO0OOOO00O0OOOO ,OOOOOO0000OOOOOO0 .uid )#line:323
                        OOOOOO0000OOOOOO0 .msg +='遇到检测文章，已发送到微信，手动阅读，暂停60秒\n'#line:324
                        printlog (f'【{OOOOOO0000OOOOOO0.name}】:遇到检测文章，已发送到微信，手动阅读，暂停60秒')#line:325
                        time .sleep (60 )#line:326
                else :#line:327
                    OOOOOO0000OOOOOO0 .msg +=f'【{OOOOOO0000OOOOOO0.name}】: 小阅阅跳转到 {OOOO0OOOO00O0OOOO}\n'#line:328
                    printlog (f'【{OOOOOO0000OOOOOO0.name}】: 小阅阅跳转到 {OOOO0OOOO00O0OOOO}')#line:329
                    continue #line:330
                O0O0OOOOO00O00OOO =random .randint (7 ,10 )#line:331
                OOOOOO0000OOOOOO0 .msg +=f'本次模拟读{O0O0OOOOO00O00OOO}秒\n'#line:332
                time .sleep (O0O0OOOOO00O00OOO )#line:333
                O000OO0OO0O0OOO0O =f'https://nsr.zsf2023e458.cloud/yunonline/v1/get_read_gold?uk={OOOOOO0000OOOOOO0.uk}&time={O0O0OOOOO00O00OOO}&timestamp={ts()}'#line:334
                OOOOOO0000OOO00OO =requests .get (O000OO0OO0O0OOO0O ,headers =OOOOOO0000OOOOOO0 .headers ).json ()#line:335
                debugger (f'check {OOOOOO0000OOO00OO}')#line:336
                if OOOOOO0000OOO00OO .get ('errcode')==0 :#line:337
                    printlog (f'【{OOOOOO0000OOOOOO0.name}】:✅阅读成功，获得金币{OOOOOO0000OOO00OO.get("data").get("gold")}，已读{OOOOOO0000OOO00OO.get("data").get("day_read")}，现有金币{OOOOOO0000OOO00OO.get("data").get("last_gold")}')#line:338
            elif OOOOOO0000OOO00OO .get ('errcode')==405 :#line:339
                printlog (f'【{OOOOOO0000OOOOOO0.name}】:阅读重复')#line:340
                OOOOOO0000OOOOOO0 .msg +='阅读重复\n'#line:341
                time .sleep (1.5 )#line:342
            elif OOOOOO0000OOO00OO .get ('errcode')==407 :#line:343
                printlog (f'【{OOOOOO0000OOOOOO0.name}】: {OOOOOO0000OOO00OO.get("msg")}')#line:344
                OOOOOO0000OOOOOO0 .msg +=(OOOOOO0000OOO00OO .get ('msg')+'\n')#line:345
                return True #line:346
            else :#line:347
                printlog (f'【{OOOOOO0000OOOOOO0.name}】:{OOOOOO0000OOO00OO.get("msg")}')#line:348
                OOOOOO0000OOOOOO0 .msg +=(OOOOOO0000OOO00OO .get ("msg")+'\n')#line:349
                time .sleep (1.5 )#line:350
    def jump (OO0OOOO00O000O00O ,OO0000000000O00OO ):#line:352
        O0000OO00OO0O00OO =urlparse (OO0000000000O00OO ).netloc #line:353
        OO000OO000O0O0OOO ={'Host':O0000OO00OO0O00OO ,'Connection':'keep-alive','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh','Cookie':f'ysmuid={OO0OOOO00O000O00O.ysmuid}',}#line:363
        O000000OO0O0OO0OO =requests .get (OO0000000000O00OO ,headers =OO000OO000O0O0OOO ,allow_redirects =False )#line:364
        O00OOO00O0000O0OO =O000000OO0O0OO0OO .headers .get ('Location')#line:365
        return O00OOO00O0000O0OO #line:366
    def withdraw (OO000O00OOOO00OOO ):#line:368
        if not OO000O00OOOO00OOO .unionid :#line:369
            return False #line:370
        if int (OO000O00OOOO00OOO .last_gold )<txbz :#line:371
            printlog (f'【{OO000O00OOOO00OOO.name}】: 没有达到你设置的提现标准{txbz}')#line:372
            OO000O00OOOO00OOO .msg +=f'没有达到你设置的提现标准{txbz}\n'#line:373
            return False #line:374
        O0O00O00000OO0OO0 =int (int (OO000O00OOOO00OOO .last_gold )/1000 )*1000 #line:375
        OO000O00OOOO00OOO .msg +=f'本次提现金币{O0O00O00000OO0OO0}\n'#line:376
        printlog (f'【{OO000O00OOOO00OOO.name}】:✅本次提现金币{O0O00O00000OO0OO0}')#line:377
        if O0O00O00000OO0OO0 :#line:378
            OO0O0OOOO0O0O000O =f'{OO000O00OOOO00OOO.host}/yunonline/v1/user_gold'#line:379
            O0OOO000000OOO0OO =f'unionid={OO000O00OOOO00OOO.unionid}&request_id={OO000O00OOOO00OOO.request_id}&gold={O0O00O00000OO0OO0}'#line:380
            O0O0000OOO0O0OOOO =OO000O00OOOO00OOO .sec .post (OO0O0OOOO0O0O000O ,data =O0OOO000000OOO0OO )#line:381
            debugger (f'gold {O0O0000OOO0O0OOOO.text}')#line:382
            OO0O0OOOO0O0O000O =f'{OO000O00OOOO00OOO.host}/yunonline/v1/withdraw'#line:383
            O0OOO000000OOO0OO =f'unionid={OO000O00OOOO00OOO.unionid}&signid={OO000O00OOOO00OOO.request_id}&ua=0&ptype=0&paccount=&pname='#line:384
            O0O0000OOO0O0OOOO =OO000O00OOOO00OOO .sec .post (OO0O0OOOO0O0O000O ,data =O0OOO000000OOO0OO )#line:385
            debugger (f'withdraw {O0O0000OOO0O0OOOO.text}')#line:386
            OO000O00OOOO00OOO .msg +=f"提现结果 {O0O0000OOO0O0OOOO.json()['msg']}"#line:387
            printlog (f'【{OO000O00OOOO00OOO.name}】:提现结果 {O0O0000OOO0O0OOOO.json()["msg"]}')#line:388
    def run (OO0OOOO0O0OO00O00 ):#line:390
        OO0OOOO0O0OO00O00 .msg +=('='*50 +f'\n账号：{OO0OOOO0O0OO00O00.name}开始任务\n')#line:391
        printlog (f'【{OO0OOOO0O0OO00O00.name}】:开始任务')#line:392
        if not OO0OOOO0O0OO00O00 .init ():#line:393
            return False #line:394
        OO0OOOO0O0OO00O00 .something ()#line:395
        if OO0OOOO0O0OO00O00 .user_info ():#line:396
            OO0OOOO0O0OO00O00 .getKey ()#line:397
            OO0OOOO0O0OO00O00 .read ()#line:398
            OO0OOOO0O0OO00O00 .user_info ()#line:399
            time .sleep (0.5 )#line:400
        OO0OOOO0O0OO00O00 .withdraw ()#line:401
        printlog (f'【{OO0OOOO0O0OO00O00.name}】:✅本轮任务结束')#line:402
        if not printf :#line:403
            print (OO0OOOO0O0OO00O00 .msg )#line:404
def yd (OO0O0000O00000OOO ):#line:407
    while not OO0O0000O00000OOO .empty ():#line:408
        OO0000O0O0000O00O =OO0O0000O00000OOO .get ()#line:409
        OOO0O0OO0O0OO00O0 =XYY (OO0000O0O0000O00O )#line:410
        OOO0O0OO0O0OO00O0 .run ()#line:411
def get_info ():#line:414
    print ("="*50 +f'\n✅github仓库：https://github.com/kxs2018/xiaoym\n✅极狐仓库:https://jihulab.com/xizhiai/xiaoym\n✅By:惜之酱\t\thttp://t.me/xiaoymgroup\n'+'-'*50 )#line:416
    print (f"✅{_OOOO0OO0O00O0O0O0.get('msg')['小阅阅']}")#line:417
    OO0O00O00O0OOOO00 ='v2.5'#line:418
    O0OOOO00O0O0O00O0 =_OOOO0OO0O00O0O0O0 ['version']['小阅阅']#line:419
    print ('-'*50 +f'\n当前版本{OO0O00O00O0OOOO00}，仓库版本{O0OOOO00O0O0O00O0}\n✅{_OOOO0OO0O00O0O0O0["update_log"]["小阅阅"]}')#line:420
    if OO0O00O00O0OOOO00 <O0OOOO00O0O0O00O0 :#line:421
        print ('⛔️请到仓库下载最新版本k_xyy.py')#line:422
    print ("="*50 )#line:423
    return True #line:424
def main ():#line:427
    get_info ()#line:428
    O000O0O00O0O0000O =os .getenv ('xyyck')#line:429
    if not O000O0O00O0O0000O :#line:430
        print ('⛔️没有获取到账号，程序退出')#line:431
        exit ()#line:432
    try :#line:433
        O000O0O00O0O0000O =ast .literal_eval (O000O0O00O0O0000O )#line:434
    except :#line:435
        pass #line:436
    OOO0O00OOO00O0O00 =[]#line:437
    OO0000OO0OOOO00O0 =Queue ()#line:438
    printlog (f'✅共获取到{len(O000O0O00O0O0000O)}个账号，如不正确，请检查ck填写格式')#line:439
    for O0O000O000O00O000 ,OOOOOOOO0OOO0OO00 in enumerate (O000O0O00O0O0000O ,start =1 ):#line:440
        OO0000OO0OOOO00O0 .put (OOOOOOOO0OOO0OO00 )#line:441
    for O0O000O000O00O000 in range (max_workers ):#line:442
        OOOOO0O0OOO000000 =threading .Thread (target =yd ,args =(OO0000OO0OOOO00O0 ,))#line:443
        OOOOO0O0OOO000000 .start ()#line:444
        OOO0O00OOO00O0O00 .append (OOOOO0O0OOO000000 )#line:445
        time .sleep (delay_time )#line:446
    for OOO00O0OO000O0OOO in OOO0O00OOO00O0O00 :#line:447
        OOO00O0OO000O0OOO .join ()#line:448
    with open ('xyy_check.json','w',encoding ='utf-8')as O0OOOOOOO0O0O0O0O :#line:449
        O0OOOOOOO0O0O0O0O .write (json .dumps (checkdict ))#line:450
if __name__ =='__main__':#line:453
    main ()#line:454
