# -*- coding: utf-8 -*-
# k_mtz
# Author: 惜之酱
"""
new Env('每天赚');
先运行脚本，有问题到群里问 http://t.me/xiaoymgroup
每天赚入口：http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552
"""
try:
    from config import mtz_config
except:
    mtz_config = {
        'printf': 1,  # 实时日志开关 1为开，0为关
        'debug': 0,  # debug模式开关
        'txbz': 1000,  # 设置提现标准 不低于1000，平台的提现标准为1000
        'sendable': 1,  # 企业微信推送开关 1为开，0为关 开启后必须设置qwbotkey才能运行
        'pushable': 0,  # wxpusher推送开关 开启后必须设置pushconfig才能运行
        'max_workers': 5,  # 线程数量设置 填入数字，设置同时跑任务的数量
        'delay_time': 20,  # 设置为20即每隔20秒新增一个号做任务，直到数量达到max_workers
        'total_num': 18,  # 设置单轮任务最小数量"""设置为18即本轮数量小于18不继续阅读"""
        'blacklist': [],  # 提现黑名单设置，在列表里的账号转移积分，否则提现
        'move_id': '',  # 设置积分转移id
    }

printf = mtz_config['printf']
debug = mtz_config['debug']
sendable = mtz_config['sendable']
pushable = mtz_config['pushable']
max_workers = mtz_config['max_workers']
delay_time = mtz_config['delay_time']
total_num = mtz_config['total_num']
txbz = mtz_config['txbz']
blacklist =mtz_config ['blacklist']#line:33
move_id =mtz_config ['move_id']#line:34
import json #line:36
import os #line:37
import random #line:38
import requests #line:39
import re #line:40
import time #line:41
import ast #line:42
import datetime #line:43
import threading #line:44
from queue import Queue #line:45
from urllib .parse import urlparse #line:46
def get_msg ():#line:49
    OOO00O000O000O00O ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:51
    OOOOO00O00OOOOOO0 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OOO00O000O000O00O ).json ()#line:52
    return OOOOO00O00OOOOOO0 #line:53
_OO0000OO0OO0OOOOO =get_msg ()#line:56
try :#line:57
    from lxml import etree #line:58
except :#line:59
    print (_OO0000OO0OO0OOOOO .get ('help')['lxml'])#line:60
if sendable :#line:62
    qwbotkey =os .getenv ('qwbotkey')#line:63
    if not qwbotkey :#line:64
        print (_OO0000OO0OO0OOOOO .get ('help')['qwbotkey'])#line:65
        exit ()#line:66
if pushable :#line:68
    pushconfig =os .getenv ('pushconfig')#line:69
    if not pushconfig :#line:70
        print (_OO0000OO0OO0OOOOO .get ('help')['pushconfig'])#line:71
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
            print (_OO0000OO0OO0OOOOO .get ('help')['pushconfig'])#line:88
            exit ()#line:89
if not pushable and not sendable :#line:90
    print ('啥通知方式都不配置，你想上天吗')#line:91
    exit ()#line:92
def ftime ():#line:95
    O0OOO000O00OOO0O0 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:96
    return O0OOO000O00OOO0O0 #line:97
def debugger (O0OOO00O00000O0OO ):#line:100
    if debug :#line:101
        print (O0OOO00O00000O0OO )#line:102
def printlog (OOOOO000OOOO0OO00 ):#line:105
    if printf :#line:106
        print (OOOOO000OOOO0OO00 )#line:107
def send (OOOO0O0OOO0O00000 ,title ='通知',url =None ):#line:110
    if not url :#line:111
        O0OOOO000O0000OO0 ={"msgtype":"text","text":{"content":f"{title}\n\n{OOOO0O0OOO0O00000}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg群：https://t.me/xiaoymgroup\n通知时间：{ftime()}",}}#line:118
    else :#line:119
        O0OOOO000O0000OO0 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":OOOO0O0OOO0O00000 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:124
    O0000OO00000O0O00 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:125
    O0OO0O00000OO00O0 =requests .post (O0000OO00000O0O00 ,data =json .dumps (O0OOOO000O0000OO0 )).json ()#line:126
    if O0OO0O00000OO00O0 .get ('errcode')!=0 :#line:127
        print ('消息发送失败，请检查key和发送格式')#line:128
        return False #line:129
    return O0OO0O00000OO00O0 #line:130
def push (OOOO0OO0O000OO00O ,title ='通知',url ='',uid =None ):#line:133
    if uid :#line:134
        uids .clear ()#line:135
        uids .append (uid )#line:136
    OO00O00OO0O0OOO0O ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入tg群](https://t.me/xiaoymgroup)</font>".replace ('msg',OOOO0OO0O000OO00O ).replace ('url',url )#line:138
    O0000OO00O000O00O ={"appToken":appToken ,"content":OO00O00OO0O0OOO0O ,"summary":title ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:148
    O00O000O000O0O0O0 ='http://wxpusher.zjiecode.com/api/send/message'#line:149
    OO00OO00O00O000O0 =requests .post (url =O00O000O000O0O0O0 ,json =O0000OO00O000O00O ).json ()#line:150
    if OO00OO00O00O000O0 .get ('code')!=1000 :#line:151
        print (OO00OO00O00O000O0 .get ('msg'),OO00OO00O00O000O0 )#line:152
    return OO00OO00O00O000O0 #line:153
def getmpinfo (O0O0OOO00O0OOO0O0 ):#line:156
    if not O0O0OOO00O0OOO0O0 or O0O0OOO00O0OOO0O0 =='':#line:157
        return False #line:158
    OOOO000OO0OO0OOO0 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:160
    OO0O0O000OOO00O00 =requests .get (O0O0OOO00O0OOO0O0 ,headers =OOOO000OO0OO0OOO0 )#line:161
    O0OOOOOOOOO0O00OO =etree .HTML (OO0O0O000OOO00O00 .text )#line:162
    OO0O00O0OO0OOO0O0 =O0OOOOOOOOO0O00OO .xpath ('//meta[@*="og:title"]/@content')#line:163
    if OO0O00O0OO0OOO0O0 :#line:164
        OO0O00O0OO0OOO0O0 =OO0O00O0OO0OOO0O0 [0 ]#line:165
    try :#line:166
        if 'biz='in O0O0OOO00O0OOO0O0 :#line:167
            OOOOOO000O0O0OO0O =re .findall (r'biz=(.*?)&',O0O0OOO00O0OOO0O0 )[0 ]#line:168
        else :#line:169
            O00OO00000O0O000O =O0OOOOOOOOO0O00OO .xpath ('//meta[@*="og:url"]/@content')[0 ]#line:170
            OOOOOO000O0O0OO0O =re .findall (r'biz=(.*?)&',str (O00OO00000O0O000O ))[0 ]#line:171
    except :#line:172
        return False #line:173
    OO0OOO000O00000O0 =O0OOOOOOOOO0O00OO .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:174
    if OO0OOO000O00000O0 :#line:175
        OO0OOO000O00000O0 =OO0OOO000O00000O0 [0 ].strip ()#line:176
    OOO00O0OOOO0O00OO =re .findall (r"user_name.DATA'\) : '(.*?)'",OO0O0O000OOO00O00 .text )or O0OOOOOOOOO0O00OO .xpath ('//span[@class="profile_meta_value"]/text()')#line:178
    if OOO00O0OOOO0O00OO :#line:179
        OOO00O0OOOO0O00OO =OOO00O0OOOO0O00OO [0 ]#line:180
    O0OOO0O0O000O0O0O =re .findall (r'createTime = \'(.*)\'',OO0O0O000OOO00O00 .text )#line:181
    if O0OOO0O0O000O0O0O :#line:182
        O0OOO0O0O000O0O0O =O0OOO0O0O000O0O0O [0 ][5 :]#line:183
    O00O00000O0000OOO =f'{O0OOO0O0O000O0O0O}|{OO0O00O0OO0OOO0O0[:10]}|{OOOOOO000O0O0OO0O}|{OO0OOO000O00000O0}|{OOO00O0OOOO0O00OO}'#line:184
    O0O000OOO0O0000O0 ={'biz':OOOOOO000O0O0OO0O ,'text':O00O00000O0000OOO }#line:185
    return O0O000OOO0O0000O0 #line:186
class MTZYD :#line:189
    def __init__ (OO00O00O00OO0000O ,O000O0OO0OOO0OO0O ):#line:190
        O000O0OO0OOO0OO0O =O000O0OO0OOO0OO0O .split (';')#line:191
        if ''in O000O0OO0OOO0OO0O :#line:192
            O000O0OO0OOO0OO0O .pop ('')#line:193
        OO00O00O00OO0000O .name =O000O0OO0OOO0OO0O [0 ].split ('=')[1 ]#line:194
        OO00O00O00OO0000O .uid =O000O0OO0OOO0OO0O [2 ].split ('=')[1 ]if len (O000O0OO0OOO0OO0O )==3 else None #line:195
        OO00O00O00OO0000O .ck =O000O0OO0OOO0OO0O [1 ].split ('=')[1 ]#line:196
        OO00O00O00OO0000O .s =requests .session ()#line:197
        OO00O00O00OO0000O .host =OO00O00O00OO0000O .get_host ()#line:198
        OO00O00O00OO0000O .s .headers ={'Authorization':OO00O00O00OO0000O .ck ,'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5279 MMWEBSDK/20230805 MMWEBID/2833 MicroMessenger/8.0.42.2460(0x28002A3B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Accept':'*/*','Origin':OO00O00O00OO0000O .host ,'Referer':f'{OO00O00O00OO0000O.host}/','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh',}#line:208
        OO00O00O00OO0000O .c =0 #line:209
        OO00O00O00OO0000O .msg =''#line:210
    @staticmethod #line:212
    def get_host ():#line:213
        O0OOOO00O00OOOOOO ='http://tg.api.mengmorwpt2.cn/h5_share/ads/tg?user_id='#line:214
        OO0000000O0O0O0O0 ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309071d) XWEB/8447 Flue'}#line:216
        OOO0000O0O0O0O0OO =requests .get (O0OOOO00O00OOOOOO ,headers =OO0000000O0O0O0O0 ,allow_redirects =False )#line:217
        O0O00OO00O0O000OO =OOO0000O0O0O0O0OO .headers .get ('Location')#line:218
        OO0OOO0O00OOO00O0 =urlparse (O0O00OO00O0O000OO ).netloc #line:219
        return 'http://'+OO0OOO0O00OOO00O0 #line:220
    def user_info (O00O0OO00OO0O0000 ):#line:222
        O0OOO0OO00OO0000O ='https://api2.wanjd.cn/h5_share/user/info'#line:223
        OO0OOO0O0OOOO00OO =O00O0OO00OO0O0000 .s .post (O0OOO0OO00OO0000O ,json ={"openid":0 }).json ()#line:224
        debugger (f'userinfo {OO0OOO0O0OOOO00OO}')#line:225
        if OO0OOO0O0OOOO00OO .get ('code')==200 :#line:226
            O00O0OO00OO0O0000 .nickname =OO0OOO0O0OOOO00OO .get ('data').get ('nickname')#line:227
            O00O0OO00OO0O0000 .points =OO0OOO0O0OOOO00OO .get ('data').get ('points')-OO0OOO0O0OOOO00OO .get ('data').get ('used_points')#line:228
            OO0OOO0O0OOOO00OO =O00O0OO00OO0O0000 .s .post ('https://api2.wanjd.cn/h5_share/user/sign',json ={"openid":0 })#line:229
            debugger (f'签到 {OO0OOO0O0OOOO00OO.json()}')#line:230
            OOO0O000OO00OO0O0 =OO0OOO0O0OOOO00OO .json ().get ('message')#line:231
            O00O0OO00OO0O0000 .msg +=f'\n【{O00O0OO00OO0O0000.name}】:{O00O0OO00OO0O0000.nickname},现有积分：{O00O0OO00OO0O0000.points}，{OOO0O000OO00OO0O0}\n'+'-'*50 +'\n'#line:232
            printlog (f'【{O00O0OO00OO0O0000.name}】:{O00O0OO00OO0O0000.nickname},现有积分：{O00O0OO00OO0O0000.points}，{OOO0O000OO00OO0O0}')#line:233
            O0OOO0OO00OO0000O ='http://api2.wanjd.cn/h5_share/user/up_profit_ratio'#line:234
            OOOOO0O0O00O0O0OO ={"openid":0 }#line:235
            try :#line:236
                OO0OOO0O0OOOO00OO =O00O0OO00OO0O0000 .s .post (O0OOO0OO00OO0000O ,json =OOOOO0O0O00O0O0OO ).json ()#line:237
                if OO0OOO0O0OOOO00OO .get ('code')==500 :#line:238
                    raise #line:239
                O00O0OO00OO0O0000 .msg +=f'代理升级：{OO0OOO0O0OOOO00OO.get("message")}\n'#line:240
                printlog (f'【{O00O0OO00OO0O0000.name}】:代理升级：{OO0OOO0O0OOOO00OO.get("message")}')#line:241
            except :#line:242
                O0OOO0OO00OO0000O ='http://api2.wanjd.cn/h5_share/user/task_reward'#line:243
                for O0O00OO0OOOO0O0O0 in [1 ,2 ,3 ]:#line:244
                    OOOOO0O0O00O0O0OO ={"type":O0O00OO0OOOO0O0O0 ,"openid":0 }#line:245
                    OO0OOO0O0OOOO00OO =O00O0OO00OO0O0000 .s .post (O0OOO0OO00OO0000O ,json =OOOOO0O0O00O0O0OO ).json ()#line:246
                    if '积分未满'in OO0OOO0O0OOOO00OO .get ('message'):#line:247
                        break #line:248
                    if OO0OOO0O0OOOO00OO .get ('code')!=500 :#line:249
                        O00O0OO00OO0O0000 .msg +='主页活动奖励积分：'+OO0OOO0O0OOOO00OO .get ('message')+'\n'#line:250
                        printlog (f'【{O00O0OO00OO0O0000.name}】:主页{O0O00OO0OOOO0O0O0}级活动奖励积分 {OO0OOO0O0OOOO00OO.get("message")}')#line:251
                        time .sleep (1 )#line:252
                O0OOO0OO00OO0000O ='https://api2.wanjd.cn/h5_share/user/publicize'#line:253
                for O0O00OO0OOOO0O0O0 in range (1 ,5 ):#line:254
                    OOOOO0O0O00O0O0OO ={"type":O0O00OO0OOOO0O0O0 ,"openid":0 }#line:255
                    OO0OOO0O0OOOO00OO =O00O0OO00OO0O0000 .s .post (O0OOO0OO00OO0000O ,json =OOOOO0O0O00O0O0OO ).json ()#line:256
                    if '积分未满'in OO0OOO0O0OOOO00OO .get ('message'):#line:257
                        break #line:258
                    if OO0OOO0O0OOOO00OO .get ('code')!=500 :#line:259
                        O00O0OO00OO0O0000 .msg +='主页推广奖励积分：'+OO0OOO0O0OOOO00OO .get ('message')+'\n'#line:260
                        printlog (f'【{O00O0OO00OO0O0000.name}】:主页{O0O00OO0OOOO0O0O0}级推广奖励积分 {OO0OOO0O0OOOO00OO.get("message")}')#line:261
                        time .sleep (1 )#line:262
            return True #line:263
        else :#line:264
            O00O0OO00OO0O0000 .msg +='获取账号信息异常，检查cookie是否失效\n'#line:265
            printlog (f'【{O00O0OO00OO0O0000.name}】:获取账号信息异常，检查cookie是否失效')#line:266
            if pushable :#line:267
                push (f'【{O00O0OO00OO0O0000.name}】:获取账号信息异常，检查cookie是否失效',f'【{O00O0OO00OO0O0000.name}】账号异常通知',uid =O00O0OO00OO0O0000 .uid )#line:268
            if sendable :#line:269
                send (f'【{O00O0OO00OO0O0000.name}】:获取账号信息异常，检查cookie是否失效',f'【{O00O0OO00OO0O0000.name}】账号异常通知')#line:270
            return False #line:271
    def get_read (OO000000OOOO00OO0 ):#line:273
        OOO0000O00OOO0OO0 ='http://api2.wanjd.cn/h5_share/daily/get_read'#line:274
        O00O0O0O0O0O0O0O0 ={"openid":0 }#line:275
        OO0OOOO000OO000O0 =0 #line:276
        while OO0OOOO000OO000O0 <10 :#line:277
            O000OO00OOOOOO0OO =OO000000OOOO00OO0 .s .post (OOO0000O00OOO0OO0 ,json =O00O0O0O0O0O0O0O0 ).json ()#line:278
            debugger (f'getread {O000OO00OOOOOO0OO}')#line:279
            if O000OO00OOOOOO0OO .get ('code')==200 :#line:280
                OO000000OOOO00OO0 .link =O000OO00OOOOOO0OO .get ('data').get ('link')#line:281
                return True #line:282
            elif '获取失败'in O000OO00OOOOOO0OO .get ('message'):#line:283
                time .sleep (15 )#line:284
                OO0OOOO000OO000O0 +=1 #line:285
                continue #line:286
            else :#line:287
                OO000000OOOO00OO0 .msg +=O000OO00OOOOOO0OO .get ('message')+'\n'#line:288
                printlog (f'【{OO000000OOOO00OO0.name}】:{O000OO00OOOOOO0OO.get("message")}')#line:289
                return False #line:290
    def gettaskinfo (O0OOOOO00OO0000OO ,OOO00OOOOO0OOOOOO ):#line:292
        for O000OO00O0O0OO00O in OOO00OOOOO0OOOOOO :#line:293
            if O000OO00O0O0OO00O .get ('url'):#line:294
                return O000OO00O0O0OO00O #line:295
    def dotasks (OO0O000O000OOO000 ):#line:297
        O0OO0000OOO00O00O =urlparse (OO0O000O000OOO000 .link ).netloc #line:298
        OOOO0O0OO00O00OO0 ={'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Origin':f'http://{O0OO0000OOO00O00O}','Referer':f'http://{O0OO0000OOO00O00O}/','Accept-Encoding':'gzip, deflate',}#line:305
        OO000OOOO0O00OOOO =0 #line:306
        while True :#line:307
            O000OO0O00O0OOO00 ={"href":OO0O000O000OOO000 .link }#line:308
            OOOOOOO0000O0OOO0 ='https://api2.wanjd.cn/wxread/articles/tasks'#line:309
            OO00OO0OOOO000O00 =requests .post (OOOOOOO0000O0OOO0 ,headers =OOOO0O0OO00O00OO0 ,json =O000OO0O00O0OOO00 )#line:310
            debugger (f'tasks {OO00OO0OOOO000O00.text}')#line:311
            OO00OO0OOOO000O00 =OO00OO0OOOO000O00 .json ()#line:312
            OO0OO00O0OO00O0OO =OO00OO0OOOO000O00 .get ('data')#line:313
            debugger (f'tasks {OO0OO00O0OO00O0OO}')#line:314
            O0000OO0O00OO000O =[OOO0O0OOO0000OO0O ['is_read']for OOO0O0OOO0000OO0O in OO0OO00O0OO00O0OO ]#line:315
            if 0 not in O0000OO0O00OO000O :#line:316
                break #line:317
            if OO00OO0OOOO000O00 .get ('code')!=200 :#line:318
                OO0O000O000OOO000 .msg +=OO00OO0OOOO000O00 .get ('message')+'\n'#line:319
                printlog (f'【{OO0O000O000OOO000.name}】:{OO00OO0OOOO000O00.get("message")}')#line:320
                break #line:321
            else :#line:322
                O0OO0O00OOOO0OOO0 =OO0O000O000OOO000 .gettaskinfo (OO00OO0OOOO000O00 ['data'])#line:323
                if not O0OO0O00OOOO0OOO0 :#line:324
                    break #line:325
                OOOOOO00O00OO000O =O0OO0O00OOOO0OOO0 .get ('url')#line:326
                if len (OO0OO00O0OO00O0OO )<total_num :#line:327
                    printlog (f'【{OO0O000O000OOO000.name}】:任务数量小于{total_num}，任务中止')#line:328
                    break #line:329
                OO0O00OO0O0OO0O0O =O0OO0O00OOOO0OOO0 ['id']#line:330
                debugger (OO0O00OO0O0OO0O0O )#line:331
                O000OO0O00O0OOO00 .update ({"id":OO0O00OO0O0OO0O0O })#line:332
                O00O0O0OO00O0O0O0 =getmpinfo (OOOOOO00O00OO000O )#line:333
                try :#line:334
                    OO0O000O000OOO000 .msg +='正在阅读 '+O00O0O0OO00O0O0O0 ['text']+'\n'#line:335
                    printlog (f'【{OO0O000O000OOO000.name}】:正在阅读{O00O0O0OO00O0O0O0["text"]}')#line:336
                except :#line:337
                    OO0O000O000OOO000 .msg +='获取文章信息失败\n'#line:338
                    printlog (f'【{OO0O000O000OOO000.name}】:获取文章信息失败')#line:339
                    break #line:340
                if len (str (OO0O00OO0O0OO0O0O ))<5 :#line:341
                    if OO000OOOO0O00OOOO ==3 :#line:342
                        OO0OOO0O00000O0OO =f'【{OO0O000O000OOO000.name}】 检测已经三次了，可能账号触发了平台的风险机制，请稍候再试或换号过检测，此次任务结束'#line:343
                        printlog (OO0OOO0O00000O0OO )#line:344
                        OO0O000O000OOO000 .msg +=OO0OOO0O00000O0OO +'\n'#line:345
                        break #line:346
                    if sendable :#line:347
                        send (O00O0O0OO00O0O0O0 .get ('text'),f'【{OO0O000O000OOO000.name}】{OO0O000O000OOO000.nickname} 美添赚过检测',OOOOOO00O00OO000O )#line:348
                    if pushable :#line:349
                        push (f'【{OO0O000O000OOO000.name}】{OO0O000O000OOO000.nickname} 本轮任务数量{len(OO0OO00O0OO00O0OO) - 1}\n点击阅读检测文章\n{O00O0O0OO00O0O0O0["text"]}',f'【{OO0O000O000OOO000.name}】 {OO0O000O000OOO000.nickname}美添赚过检测',OOOOOO00O00OO000O ,OO0O000O000OOO000 .uid )#line:353
                    OO0O000O000OOO000 .msg +='发送通知，暂停50秒\n'#line:354
                    printlog (f'【{OO0O000O000OOO000.name}】:发送通知，暂停50秒')#line:355
                    OO000OOOO0O00OOOO +=1 #line:356
                    time .sleep (50 )#line:357
                OOOO0O00OOO0O0OOO =random .randint (7 ,10 )#line:358
                time .sleep (OOOO0O00OOO0O0OOO )#line:359
                OOOOOOO0000O0OOO0 ='https://api2.wanjd.cn/wxread/articles/three_read'#line:360
                OO00OO0OOOO000O00 =requests .post (OOOOOOO0000O0OOO0 ,headers =OOOO0O0OO00O00OO0 ,json =O000OO0O00O0OOO00 ).json ()#line:361
                if OO00OO0OOOO000O00 .get ('code')==200 :#line:362
                    OO0O000O000OOO000 .msg +='阅读成功'+'\n'+'-'*50 +'\n'#line:363
                    OO0O000O000OOO000 .c +=1 #line:364
                if OO00OO0OOOO000O00 .get ('code')!=200 :#line:365
                    OO0O000O000OOO000 .msg +=OO00OO0OOOO000O00 .get ('message')+'\n'+'-'*50 +'\n'#line:366
                    printlog (f'【{OO0O000O000OOO000.name}】:{OO00OO0OOOO000O00.get("message")}')#line:367
                    break #line:368
        OOOOOOO0000O0OOO0 ='https://api2.wanjd.cn/wxread/articles/check_success'#line:369
        O000OO0O00O0OOO00 ={'type':1 ,'href':OO0O000O000OOO000 .link }#line:370
        OO00OO0OOOO000O00 =requests .post (OOOOOOO0000O0OOO0 ,headers =OOOO0O0OO00O00OO0 ,json =O000OO0O00O0OOO00 ).json ()#line:371
        debugger (f'check {OO00OO0OOOO000O00}')#line:372
        OO0O000O000OOO000 .msg +=OO00OO0OOOO000O00 .get ('message')+'\n'#line:373
        printlog (f'【{OO0O000O000OOO000.name}】:{OO00OO0OOOO000O00.get("message")}')#line:374
    def withdraw (O00O0000000OOOO0O ):#line:376
        if O00O0000000OOOO0O .points <txbz :#line:377
            O00O0000000OOOO0O .msg +=f'没有达到你设置的提现标准{txbz}\n'#line:378
            printlog (f'【{O00O0000000OOOO0O.name}】:没有达到你设置的提现标准{txbz}')#line:379
            return False #line:380
        OOOO00000OOOO00OO ='https://api2.wanjd.cn/h5_share/user/withdraw'#line:381
        O00O0OOOOO000O00O =O00O0000000OOOO0O .s .post (OOOO00000OOOO00OO ).json ()#line:382
        O00O0000000OOOO0O .msg +='提现结果'+O00O0OOOOO000O00O .get ('message')+'\n'#line:383
        printlog (f'【{O00O0000000OOOO0O.name}】:提现结果 {O00O0OOOOO000O00O.get("message")}')#line:384
        if O00O0OOOOO000O00O .get ('code')==200 :#line:385
            if sendable :#line:386
                send (f'【{O00O0000000OOOO0O.name}】:已提现到红包，请在服务通知内及时领取','每天赚提现通知')#line:387
            if pushable :#line:388
                push (f'【{O00O0000000OOOO0O.name}】:已提现到红包，请在服务通知内及时领取','每天赚提现通知','https://jihulab.com/xizhiai/xiaoym',O00O0000000OOOO0O .uid )#line:390
    def run (O00000000O0OOO0O0 ):#line:392
        O00000000O0OOO0O0 .msg +='*'*50 +f'\n【{O00000000O0OOO0O0.name}】:开始任务\n'#line:393
        if not O00000000O0OOO0O0 .user_info ():#line:394
            return False #line:395
        if O00000000O0OOO0O0 .get_read ():#line:396
            O00000000O0OOO0O0 .dotasks ()#line:397
            if O00000000O0OOO0O0 .c >1 :#line:398
                O00000000O0OOO0O0 .user_info ()#line:399
        O00000000O0OOO0O0 .withdraw ()#line:400
        if not printf :#line:401
            print (O00000000O0OOO0O0 .msg .strip ())#line:402
            print (f'【{O00000000O0OOO0O0.name}】:任务结束')#line:403
def yd (O0OOOOO00OO0OOOOO ):#line:406
    while not O0OOOOO00OO0OOOOO .empty ():#line:407
        OO0000OO0000O000O =O0OOOOO00OO0OOOOO .get ()#line:408
        O0000OOOOO00OOO0O =MTZYD (OO0000OO0000O000O )#line:409
        O0000OOOOO00OOO0O .run ()#line:410
def get_info ():#line:413
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\t\ttg群：https://t.me/xiaoymgroup\n'+'-'*50 )#line:415
    print ('入口：http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552')#line:416
    OOOO0O0O0O0O00O0O ='v2.4'#line:417
    OOOOOO0O0O0000OOO =_OO0000OO0OO0OOOOO ['version']['每天赚']#line:418
    print (f'当前版本{OOOO0O0O0O0O00O0O}，仓库版本{OOOOOO0O0O0000OOO}\n{_OO0000OO0OO0OOOOO["update_log"]["每天赚"]}')#line:419
    if OOOO0O0O0O0O00O0O <OOOOOO0O0O0000OOO :#line:420
        print ('请到仓库下载最新版本k_mtz.py')#line:421
    print ('-'*20 )#line:422
    print (_OO0000OO0OO0OOOOO .get ('msg')['每天赚'])#line:423
    print ("="*25 )#line:424
    return True #line:425
def main ():#line:428
    O00OO0O00OOOO0000 =get_info ()#line:429
    O0O00O00OOOO000OO =os .getenv ('mtzv2ck')#line:430
    if not O0O00O00OOOO000OO :#line:431
        print ('没有获取到账号，程序退出')#line:432
        exit ()#line:433
    O0O00O00OOOO000OO =O0O00O00OOOO000OO .split ('&')#line:434
    O00O0O0O0OO0OO000 =Queue ()#line:435
    OOO0OO00000000O00 =[]#line:436
    print (f'共获取到{len(O0O00O00OOOO000OO)}个账号\n'+'*'*20 )#line:437
    if not O00OO0O00OOOO0000 :#line:438
        exit ()#line:439
    for OOO00OO0O000OO0OO ,O000OO000O0OOO000 in enumerate (O0O00O00OOOO000OO ,start =1 ):#line:440
        O00O0O0O0OO0OO000 .put (O000OO000O0OOO000 )#line:441
    for OOO00OO0O000OO0OO in range (max_workers ):#line:442
        OO00OOOOO00OOO0O0 =threading .Thread (target =yd ,args =(O00O0O0O0OO0OO000 ,))#line:443
        OO00OOOOO00OOO0O0 .start ()#line:444
        OOO0OO00000000O00 .append (OO00OOOOO00OOO0O0 )#line:445
        time .sleep (delay_time )#line:446
    for OO0OO0O00OOO0OO0O in OOO0OO00000000O00 :#line:447
        OO0OO0O00OOO0OO0O .join ()#line:448
if __name__ =='__main__':#line:451
    main ()#line:452
