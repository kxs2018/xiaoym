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
    OO0O00OOOOOO00000 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:38
    OO0O00000000OOO0O =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OO0O00OOOOOO00000 ).json ()#line:39
    return OO0O00000000OOO0O #line:40
_O0O0OO000O0OO0O00 =get_msg ()#line:43
try :#line:44
    from lxml import etree #line:45
except :#line:46
    print (_O0O0OO000O0OO0O00 .get ('help')['lxml'])#line:47
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
        print (_O0O0OO000O0OO0O00 .get ('help')['qwbotkey'])#line:58
        exit ()#line:59
if pushable :#line:61
    pushconfig =os .getenv ('pushconfig')#line:62
    if not pushconfig :#line:63
        print (_O0O0OO000O0OO0O00 .get ('help')['pushconfig'])#line:64
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
            print (_O0O0OO000O0OO0O00 .get ('help')['pushconfig'])#line:81
            exit ()#line:82
if not pushable and not sendable :#line:83
    print ('⛔️啥通知方式都不配置，你想上天吗')#line:84
    exit ()#line:85
def ftime ():#line:88
    OOOO0O0OO0OOO000O =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:89
    return OOOO0O0OO0OOO000O #line:90
def debugger (O000O0OOOO0OOO0O0 ):#line:93
    if debug :#line:94
        print (O000O0OOOO0OOO0O0 )#line:95
def printlog (OOO0O00O00O00OOO0 ):#line:98
    if printf :#line:99
        print (OOO0O00O00O00OOO0 )#line:100
def send (O00OO0OO00OO0000O ,title ='通知',url =None ):#line:103
    if not url :#line:104
        O000O0OOO00OOOO00 ={"msgtype":"text","text":{"content":f"{title}\n\n{O00OO0OO00OO0000O}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:111
    else :#line:112
        O000O0OOO00OOOO00 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O00OO0OO00OO0000O ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:117
    O0OO00O0O0000000O =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:118
    O000OO000000O0OOO =requests .post (O0OO00O0O0000000O ,data =json .dumps (O000O0OOO00OOOO00 )).json ()#line:119
    if O000OO000000O0OOO .get ('errcode')!=0 :#line:120
        print ('消息发送失败，请检查key和发送格式')#line:121
        return False #line:122
    return O000OO000000O0OOO #line:123
def push (OO000OO00O0OO0OOO ,title ='通知',url ='',uid =None ):#line:126
    if uid :#line:127
        uids .append (uid )#line:128
    OO0OO00OO0O000OOO ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',OO000OO00O0OO0OOO ).replace ('url',url )#line:130
    OOOO0O00OO00000O0 ={"appToken":appToken ,"content":OO0OO00OO0O000OOO ,"summary":title ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:140
    O0O00O0OOO0O00O00 ='http://wxpusher.zjiecode.com/api/send/message'#line:141
    O0O00OO00OOOO00OO =requests .post (url =O0O00O0OOO0O00O00 ,json =OOOO0O00OO00000O0 ).json ()#line:142
    if O0O00OO00OOOO00OO .get ('code')!=1000 :#line:143
        print (O0O00OO00OOOO00OO .get ('msg'),O0O00OO00OOOO00OO )#line:144
    return O0O00OO00OOOO00OO #line:145
def getmpinfo (O0OOOO0O00O0OOO00 ):#line:148
    if not O0OOOO0O00O0OOO00 or O0OOOO0O00O0OOO00 =='':#line:149
        return False #line:150
    O0000O0O00O00OOOO ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:152
    OOOO0O00000OO0O00 =requests .get (O0OOOO0O00O0OOO00 ,headers =O0000O0O00O00OOOO )#line:153
    OOOOO000OO0OOO0O0 =etree .HTML (OOOO0O00000OO0O00 .text )#line:154
    OO0000O0O0000O00O =OOOOO000OO0OOO0O0 .xpath ('//meta[@*="og:title"]/@content')#line:155
    if OO0000O0O0000O00O :#line:156
        OO0000O0O0000O00O =OO0000O0O0000O00O [0 ]#line:157
    try :#line:158
        if 'biz='in O0OOOO0O00O0OOO00 :#line:159
            O0000O0O0OO00OOO0 =re .findall (r'biz=(.*?)&',O0OOOO0O00O0OOO00 )[0 ]#line:160
        else :#line:161
            OO00O0000OO00OO00 =OOOOO000OO0OOO0O0 .xpath ('//meta[@*="og:url"]/@content')[0 ]#line:162
            O0000O0O0OO00OOO0 =re .findall (r'biz=(.*?)&',str (OO00O0000OO00OO00 ))[0 ]#line:163
    except :#line:164
        return False #line:165
    O0O0O00OO000OOOOO =OOOOO000OO0OOO0O0 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:166
    if O0O0O00OO000OOOOO :#line:167
        O0O0O00OO000OOOOO =O0O0O00OO000OOOOO [0 ].strip ()#line:168
    OOO0O0O000000O00O =re .findall (r"user_name.DATA'\) : '(.*?)'",OOOO0O00000OO0O00 .text )or OOOOO000OO0OOO0O0 .xpath ('//span[@class="profile_meta_value"]/text()')#line:170
    if OOO0O0O000000O00O :#line:171
        OOO0O0O000000O00O =OOO0O0O000000O00O [0 ]#line:172
    O00OOOOO0O0O0O00O =re .findall (r'createTime = \'(.*)\'',OOOO0O00000OO0O00 .text )#line:173
    if O00OOOOO0O0O0O00O :#line:174
        O00OOOOO0O0O0O00O =O00OOOOO0O0O0O00O [0 ][5 :]#line:175
    OOO0000000O0OOO00 =f'{O00OOOOO0O0O0O00O}|{OO0000O0O0000O00O[:8]}|{O0000O0O0OO00OOO0}|{O0O0O00OO000OOOOO}|{OOO0O0O000000O00O}'#line:176
    OOO000O00O0OOO00O ={'biz':O0000O0O0OO00OOO0 ,'username':O0O0O00OO000OOOOO ,'text':OOO0000000O0OOO00 }#line:177
    return OOO000O00O0OOO00O #line:178
def ts ():#line:181
    return str (int (time .time ()))+'000'#line:182
def generate_md5 (O0O000OOO0OOOOO00 ):#line:185
    OO000OO0OOO0000OO =hashlib .md5 ()#line:186
    OO000OO0OOO0000OO .update (O0O000OOO0OOOOO00 .encode ('utf-8'))#line:187
    return OO000OO0OOO0000OO .hexdigest ()#line:188
try :#line:191
    with open ('xyy_check.json','r',encoding ='utf-8')as f :#line:192
        checkdict =json .loads (f .read ())#line:193
        print ('✅获取检测号信息成功，请到https://t.me/xizhiaigroup获取最新检测号文件')#line:194
except :#line:195
    print ('⛔️没有找到检测号字典，请到https://t.me/xizhiaigroup获取最新检测号文件，程序退出')#line:196
    exit ()#line:197
class XYY :#line:200
    def __init__ (OOOOO0O000OOO0OO0 ,OOOOOOO0O00O0O00O ):#line:201
        OOOOO0O000OOO0OO0 .name =OOOOOOO0O00O0O00O ['name']#line:202
        OOOOO0O000OOO0OO0 .ysm_uid =None #line:203
        OOOOO0O000OOO0OO0 .last_gold =None #line:204
        OOOOO0O000OOO0OO0 .un =None #line:205
        OOOOO0O000OOO0OO0 .biz =None #line:206
        OOOOO0O000OOO0OO0 .uid =OOOOOOO0O00O0O00O .get ('uid')#line:207
        OOOOO0O000OOO0OO0 .ysmuid =OOOOOOO0O00O0O00O .get ('ysmuid')#line:208
        OOOOO0O000OOO0OO0 .sec =requests .session ()#line:209
        OOOOO0O000OOO0OO0 .sec .headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Cookie':f'ysmuid={OOOOO0O000OOO0OO0.ysmuid};',}#line:214
        OOOOO0O000OOO0OO0 .host =OOOOO0O000OOO0OO0 .get_host ()#line:215
        OOOOO0O000OOO0OO0 .msg =''#line:216
    @staticmethod #line:218
    def get_host ():#line:219
        O000O00000000000O ='https://ot34022.khdsfa.top:10251/yunonline/v1/auth/6d288b175355d987746598c6c11c0227'#line:220
        O0O0OO0OO0OO00O00 ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309071d) XWEB/8447 Flue'}#line:222
        O0O00OOOO0OOOO0O0 =requests .get (O000O00000000000O ,headers =O0O0OO0OO0OO00O00 ,allow_redirects =False )#line:223
        OOO0000O0O00OOOO0 =O0O00OOOO0OOOO0O0 .headers .get ('Location')#line:224
        OOOO000OOO00O0O0O =urlparse (OOO0000O0O00OOOO0 ).netloc #line:225
        return 'http://'+OOOO000OOO00O0O0O #line:226
    def init (O0O000OOO0OOOOOO0 ):#line:228
        if not O0O000OOO0OOOOOO0 .ysmuid :#line:229
            print ('⛔️ck没有ysmuid，不能运行本脚本，自动退出')#line:230
            return False #line:231
        O0OOOOO0O000OO000 =0 #line:232
        while O0OOOOO0O000OO000 <5 :#line:233
            OOOO00O00000OO0OO =O0O000OOO0OOOOOO0 .sec .get (O0O000OOO0OOOOOO0 .host ).text #line:234
            O0O000OOO0OOOOOO0 .ysm_uid =re .findall (r'unionid="(o.*?)";',OOOO00O00000OO0OO )#line:235
            if O0O000OOO0OOOOOO0 .ysm_uid :#line:236
                O0O000OOO0OOOOOO0 .ysm_uid =O0O000OOO0OOOOOO0 .ysm_uid [0 ]#line:237
                OO00OOO000OO00O0O =re .findall (r'href="(.*?)">提现',OOOO00O00000OO0OO )#line:238
                if OO00OOO000OO00O0O :#line:239
                    OO00OOO000OO00O0O =OO00OOO000OO00O0O [0 ]#line:240
                    OOO00O0O0O0OO00O0 =parse_qs (urlparse (OO00OOO000OO00O0O ).query )#line:241
                    O0O000OOO0OOOOOO0 .unionid =OOO00O0O0O0OO00O0 .get ('unionid')[0 ]#line:242
                    O0O000OOO0OOOOOO0 .request_id =OOO00O0O0O0OO00O0 .get ('request_id')[0 ]#line:243
                else :#line:244
                    printlog (f'【{O0O000OOO0OOOOOO0.name}】: ⛔️获取提现参数失败，本次不提现')#line:245
                    O0O000OOO0OOOOOO0 .msg +=f'⛔️获取提现参数失败，本次不提现\n'#line:246
                return True #line:247
            else :#line:248
                O0OOOOO0O000OO000 +=1 #line:249
                continue #line:250
        printlog (f'【{O0O000OOO0OOOOOO0.name}】: ⛔️获取ysm_uid失败，请检查账号有效性')#line:251
        O0O000OOO0OOOOOO0 .msg +='⛔️获取ysm_uid失败，请检查账号有效性\n'#line:252
        return False #line:253
    def something (O0000O000OO00000O ):#line:255
        OO00O0OOO00OOO00O =f'{O0000O000OO00000O.host}/yunonline/v1/sign_info'#line:256
        OO00000O000O00OOO ={'time':ts (),'unionid':O0000O000OO00000O .ysm_uid }#line:257
        O0000O000OO00000O .sec .get (OO00O0OOO00OOO00O ,params =OO00000O000O00OOO )#line:258
        OO00O0OOO00OOO00O =f'{O0000O000OO00000O.host}/yunonline/v1/hasWechat'#line:259
        OO00000O000O00OOO .pop ('time')#line:260
        O0000O000OO00000O .sec .get (OO00O0OOO00OOO00O ,params =OO00000O000O00OOO )#line:261
        OO00O0OOO00OOO00O =f'{O0000O000OO00000O.host}/yunonline/v1/devtouid'#line:262
        OO00000O000O00OOO .update ({'devid':generate_md5 (O0000O000OO00000O .ysm_uid )})#line:263
        O0000O000OO00000O .sec .post (OO00O0OOO00OOO00O ,data =OO00000O000O00OOO )#line:264
    def user_info (O0000OO00O0OOOO00 ):#line:266
        OOOO000OOOOOOO0O0 =f'{O0000OO00O0OOOO00.host}/yunonline/v1/gold?unionid={O0000OO00O0OOOO00.ysm_uid}&time={ts()}'#line:267
        OOOO0O00O0OOOOOO0 =O0000OO00O0OOOO00 .sec .get (OOOO000OOOOOOO0O0 ).json ()#line:268
        debugger (f'userinfo {OOOO0O00O0OOOOOO0}')#line:269
        OOOO00O0OOOO000O0 =OOOO0O00O0OOOOOO0 .get ("data")#line:270
        O0000OO00O0OOOO00 .last_gold =OOOO0O00O0OOOOOO0 .get ("data").get ("last_gold")#line:271
        OOO0OO0O00O00OOOO =OOOO00O0OOOO000O0 .get ("remain_read")#line:272
        O00000O00OOO00OOO =f'今日已经阅读了{OOOO00O0OOOO000O0.get("day_read")}篇文章,剩余{OOO0OO0O00O00OOOO}未阅读，今日获取金币{OOOO00O0OOOO000O0.get("day_gold")}，剩余{O0000OO00O0OOOO00.last_gold}'#line:273
        printlog (f'【{O0000OO00O0OOOO00.name}】:{O00000O00OOO00OOO}')#line:274
        O0000OO00O0OOOO00 .msg +=(O00000O00OOO00OOO +'\n')#line:275
        if OOO0OO0O00O00OOOO ==0 :#line:276
            return False #line:277
        return True #line:278
    def getKey (O0000O0OO0OO00000 ):#line:280
        OOO0O00OO0000000O =f'{O0000O0OO0OO00000.host}/yunonline/v1/wtmpdomain'#line:281
        O0OO0OO00OOOOO00O =f'unionid={O0000O0OO0OO00000.ysm_uid}'#line:282
        OO000OO0OOOOO0O00 =O0000O0OO0OO00000 .sec .post (OOO0O00OO0000000O ,data =O0OO0OO00OOOOO00O ).json ()#line:283
        debugger (f'getkey {OO000OO0OOOOO0O00}')#line:284
        OO0000OO00OOO000O =OO000OO0OOOOO0O00 .get ('data').get ('domain')#line:285
        O0000O0OO0OO00000 .uk =parse_qs (urlparse (OO0000OO00OOO000O ).query ).get ('uk')[0 ]#line:286
        OOOO0O000OO0OOO00 =urlparse (OO0000OO00OOO000O ).netloc #line:287
        O0000O0OO0OO00000 .headers ={'Connection':'keep-alive','Accept':'application/json, text/javascript, */*; q=0.01','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue','Origin':f'https://{OOOO0O000OO0OOO00}','Sec-Fetch-Site':'cross-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh',}#line:298
    def read (OO0OO00O0OO00000O ):#line:300
        time .sleep (3 )#line:301
        OOO000OO0O0OOOO0O ={'uk':OO0OO00O0OO00000O .uk }#line:302
        while True :#line:303
            OO0OO000O0OO0O0OO =f'https://nsr.zsf2023e458.cloud/yunonline/v1/do_read'#line:304
            OO00OO0O000O0OO0O =requests .get (OO0OO000O0OO0O0OO ,headers =OO0OO00O0OO00000O .headers ,params =OOO000OO0O0OOOO0O )#line:305
            OO0OO00O0OO00000O .msg +=('-'*50 +'\n')#line:306
            debugger (f'read1 {OO00OO0O000O0OO0O.text}')#line:307
            OO00OO0O000O0OO0O =OO00OO0O000O0OO0O .json ()#line:308
            if OO00OO0O000O0OO0O .get ('errcode')==0 :#line:309
                O0000000OO0OOOOOO =OO00OO0O000O0OO0O .get ('data').get ('link')#line:310
                O00O0OOOO00OOO0O0 =OO0OO00O0OO00000O .jump (O0000000OO0OOOOOO )#line:311
                if 'mp.weixin'in O00O0OOOO00OOO0O0 :#line:312
                    O0OOO000OOO00OO00 =getmpinfo (O00O0OOOO00OOO0O0 )#line:313
                    OO0OO00O0OO00000O .biz =O0OOO000OOO00OO00 ['biz']#line:314
                    OO0OO00O0OO00000O .un =O0OOO000OOO00OO00 ['username']#line:315
                    OO0OO00O0OO00000O .msg +=('开始阅读 '+O0OOO000OOO00OO00 ['text']+'\n')#line:316
                    printlog (f'【{OO0OO00O0OO00000O.name}】:开始阅读 '+O0OOO000OOO00OO00 ['text'])#line:317
                    if OO0OO00O0OO00000O .biz in checkdict .keys ():#line:318
                        if sendable :#line:319
                            send (f"{O0OOO000OOO00OO00['text']}",title =f'【{OO0OO00O0OO00000O.name}】: 小阅阅过检测',url =O00O0OOOO00OOO0O0 )#line:320
                        if pushable :#line:321
                            push (f'{OO0OO00O0OO00000O.name}\n点击阅读检测文章\n{O0OOO000OOO00OO00["text"]}',f'【{OO0OO00O0OO00000O.name}】: 小阅阅过检测',O00O0OOOO00OOO0O0 ,OO0OO00O0OO00000O .uid )#line:323
                        OO0OO00O0OO00000O .msg +='遇到检测文章，已发送到微信，手动阅读，暂停60秒\n'#line:324
                        printlog (f'【{OO0OO00O0OO00000O.name}】:遇到检测文章，已发送到微信，手动阅读，暂停60秒')#line:325
                        time .sleep (60 )#line:326
                else :#line:327
                    OO0OO00O0OO00000O .msg +=f'【{OO0OO00O0OO00000O.name}】: 小阅阅跳转到 {O00O0OOOO00OOO0O0}\n'#line:328
                    printlog (f'【{OO0OO00O0OO00000O.name}】: 小阅阅跳转到 {O00O0OOOO00OOO0O0}')#line:329
                    continue #line:330
                O000O0OO0OOOOO00O =random .randint (7 ,10 )#line:331
                OO0OO00O0OO00000O .msg +=f'本次模拟读{O000O0OO0OOOOO00O}秒\n'#line:332
                time .sleep (O000O0OO0OOOOO00O )#line:333
                OO0OO000O0OO0O0OO =f'https://nsr.zsf2023e458.cloud/yunonline/v1/get_read_gold?uk={OO0OO00O0OO00000O.uk}&time={O000O0OO0OOOOO00O}&timestamp={ts()}'#line:334
                OO00OO0O000O0OO0O =requests .get (OO0OO000O0OO0O0OO ,headers =OO0OO00O0OO00000O .headers ).json ()#line:335
                debugger (f'check {OO00OO0O000O0OO0O}')#line:336
            elif OO00OO0O000O0OO0O .get ('errcode')==405 :#line:337
                printlog (f'【{OO0OO00O0OO00000O.name}】:阅读重复')#line:338
                OO0OO00O0OO00000O .msg +='阅读重复\n'#line:339
                time .sleep (1.5 )#line:340
            elif OO00OO0O000O0OO0O .get ('errcode')==407 :#line:341
                printlog (f'【{OO0OO00O0OO00000O.name}】: {OO00OO0O000O0OO0O.get("msg")}')#line:342
                OO0OO00O0OO00000O .msg +=(OO00OO0O000O0OO0O .get ('msg')+'\n')#line:343
                return True #line:344
            else :#line:345
                printlog (f'【{OO0OO00O0OO00000O.name}】:{OO00OO0O000O0OO0O.get("msg")}')#line:346
                OO0OO00O0OO00000O .msg +=(OO00OO0O000O0OO0O .get ("msg")+'\n')#line:347
                time .sleep (1.5 )#line:348
    def jump (O00O0OOOO0000000O ,OO000OO00O0O00O0O ):#line:350
        O00OO00O0OO00O000 =urlparse (OO000OO00O0O00O0O ).netloc #line:351
        O00OOOOO0OOO0OO00 ={'Host':O00OO00O0OO00O000 ,'Connection':'keep-alive','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh','Cookie':f'ysmuid={O00O0OOOO0000000O.ysmuid}',}#line:361
        O000000O00OOOOOO0 =requests .get (OO000OO00O0O00O0O ,headers =O00OOOOO0OOO0OO00 ,allow_redirects =False )#line:362
        O0OOO00OO0OOO0O00 =O000000O00OOOOOO0 .headers .get ('Location')#line:363
        return O0OOO00OO0OOO0O00 #line:364
    def withdraw (O0OOO00OOOOOO0000 ):#line:366
        if not O0OOO00OOOOOO0000 .unionid :#line:367
            return False #line:368
        if int (O0OOO00OOOOOO0000 .last_gold )<txbz :#line:369
            printlog (f'【{O0OOO00OOOOOO0000.name}】: 没有达到你设置的提现标准{txbz}')#line:370
            O0OOO00OOOOOO0000 .msg +=f'没有达到你设置的提现标准{txbz}\n'#line:371
            return False #line:372
        OOOO0000OOOO00O0O =int (int (O0OOO00OOOOOO0000 .last_gold )/1000 )*1000 #line:373
        O0OOO00OOOOOO0000 .msg +=f'本次提现金币{OOOO0000OOOO00O0O}\n'#line:374
        printlog (f'【{O0OOO00OOOOOO0000.name}】:本次提现金币{OOOO0000OOOO00O0O}')#line:375
        if OOOO0000OOOO00O0O :#line:376
            OO0000OO0OO000OOO =f'{O0OOO00OOOOOO0000.host}/yunonline/v1/user_gold'#line:377
            OO00000OOOO0OO00O =f'unionid={O0OOO00OOOOOO0000.unionid}&request_id={O0OOO00OOOOOO0000.request_id}&gold={OOOO0000OOOO00O0O}'#line:378
            O000OOOOO0OOOOOO0 =O0OOO00OOOOOO0000 .sec .post (OO0000OO0OO000OOO ,data =OO00000OOOO0OO00O )#line:379
            debugger (f'gold {O000OOOOO0OOOOOO0.text}')#line:380
            OO0000OO0OO000OOO =f'{O0OOO00OOOOOO0000.host}/yunonline/v1/withdraw'#line:381
            OO00000OOOO0OO00O =f'unionid={O0OOO00OOOOOO0000.unionid}&signid={O0OOO00OOOOOO0000.request_id}&ua=0&ptype=0&paccount=&pname='#line:382
            O000OOOOO0OOOOOO0 =O0OOO00OOOOOO0000 .sec .post (OO0000OO0OO000OOO ,data =OO00000OOOO0OO00O )#line:383
            debugger (f'withdraw {O000OOOOO0OOOOOO0.text}')#line:384
            O0OOO00OOOOOO0000 .msg +=f"提现结果 {O000OOOOO0OOOOOO0.json()['msg']}"#line:385
            printlog (f'【{O0OOO00OOOOOO0000.name}】:提现结果 {O000OOOOO0OOOOOO0.json()["msg"]}')#line:386
    def run (OOOO00OO000O000OO ):#line:388
        OOOO00OO000O000OO .msg +=('='*50 +f'\n账号：{OOOO00OO000O000OO.name}开始任务\n')#line:389
        printlog (f'【{OOOO00OO000O000OO.name}】:开始任务')#line:390
        if not OOOO00OO000O000OO .init ():#line:391
            return False #line:392
        OOOO00OO000O000OO .something ()#line:393
        if OOOO00OO000O000OO .user_info ():#line:394
            OOOO00OO000O000OO .getKey ()#line:395
            OOOO00OO000O000OO .read ()#line:396
            OOOO00OO000O000OO .user_info ()#line:397
            time .sleep (0.5 )#line:398
        OOOO00OO000O000OO .withdraw ()#line:399
        printlog (f'【{OOOO00OO000O000OO.name}】:本轮任务结束')#line:400
        if not printf :#line:401
            print (OOOO00OO000O000OO .msg )#line:402
def yd (OO0O000O0OO0O0OOO ):#line:405
    while not OO0O000O0OO0O0OOO .empty ():#line:406
        OOOOOO0O00O00000O =OO0O000O0OO0O0OOO .get ()#line:407
        O0OO00O0000O0O0OO =XYY (OOOOOO0O00O00000O )#line:408
        O0OO00O0000O0O0OO .run ()#line:409
def get_info ():#line:412
    print ("="*50 +f'\n✅github仓库：https://github.com/kxs2018/xiaoym\n✅极狐仓库:https://jihulab.com/xizhiai/xiaoym\n✅By:惜之酱\n'+'-'*50 )#line:414
    print (f"✅{_O0O0OO000O0OO0O00.get('msg')['小阅阅']}")#line:415
    O00O0OOOOOO0000O0 ='v2.5'#line:416
    OOOOOO00O0O0000OO =_O0O0OO000O0OO0O00 ['version']['小阅阅']#line:417
    print (f'当前版本{O00O0OOOOOO0000O0}，仓库版本{OOOOOO00O0O0000OO}\n{_O0O0OO000O0OO0O00["update_log"]["小阅阅"]}')#line:418
    print ('-'*50 +f'\n当前版本{O00O0OOOOOO0000O0}，仓库版本{OOOOOO00O0O0000OO}\n✅{_O0O0OO000O0OO0O00["update_log"]["小阅阅"]}')#line:419
    if O00O0OOOOOO0000O0 <OOOOOO00O0O0000OO :#line:420
        print ('⛔️请到仓库下载最新版本k_xyy.py')#line:421
    print ("="*50 )#line:422
    return True #line:423
def main ():#line:426
    get_info ()#line:427
    OOOO0O00OOO0O00OO =os .getenv ('xyyck')#line:428
    if not OOOO0O00OOO0O00OO :#line:429
        print ('⛔️没有获取到账号，程序退出')#line:430
        exit ()#line:431
    try :#line:432
        OOOO0O00OOO0O00OO =ast .literal_eval (OOOO0O00OOO0O00OO )#line:433
    except :#line:434
        pass #line:435
    OOO00OO00O0O0OOO0 =[]#line:436
    O00OOO0OO0OOO00O0 =Queue ()#line:437
    printlog (f'✅共获取到{len(OOOO0O00OOO0O00OO)}个账号，如不正确，请检查ck填写格式')#line:438
    for O0000OOOO0OOOO000 ,O0O0O000O00O0O00O in enumerate (OOOO0O00OOO0O00OO ,start =1 ):#line:439
        O00OOO0OO0OOO00O0 .put (O0O0O000O00O0O00O )#line:440
    for O0000OOOO0OOOO000 in range (max_workers ):#line:441
        O00OO00O000O000OO =threading .Thread (target =yd ,args =(O00OOO0OO0OOO00O0 ,))#line:442
        O00OO00O000O000OO .start ()#line:443
        OOO00OO00O0O0OOO0 .append (O00OO00O000O000OO )#line:444
        time .sleep (delay_time )#line:445
    for OO0O0O000O0O000O0 in OOO00OO00O0O0OOO0 :#line:446
        OO0O0O000O0O000O0 .join ()#line:447
    with open ('xyy_check.json','w',encoding ='utf-8')as O0O00O000O0O0OOOO :#line:448
        O0O00O000O0O0OOOO .write (json .dumps (checkdict ))#line:449
if __name__ =='__main__':#line:452
    main ()#line:453
