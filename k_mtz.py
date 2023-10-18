# -*- coding: utf-8 -*-
# k_mtz
# Author: 惜之酱
"""
new Env('每天赚');
先运行脚本，有问题到群里问 http://t.me/xizhiaigroup
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
        'total_num': 18  # 设置单轮任务最小数量"""设置为18即本轮数量小于18不继续阅读"""
    }

printf = mtz_config['printf']
debug = mtz_config['debug']
sendable = mtz_config['sendable']
pushable = mtz_config['pushable']
max_workers = mtz_config['max_workers']
delay_time = mtz_config['delay_time']
total_num = mtz_config['total_num']


import json #line:40
import os #line:41
import random #line:42
import requests #line:43
import re #line:44
import time #line:45
import ast #line:46
import datetime
import threading
from queue import Queue
def get_msg ():#line:1
    OO00OO0O00OOO000O ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:3
    OO0000O0OO00O0O0O =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OO00OO0O00OOO000O ).json ()#line:4
    return OO0000O0OO00O0O0O #line:5
_OO000OOO0OO0O000O =get_msg ()#line:8
try :#line:9
    from lxml import etree #line:10
except :#line:11
    print (_OO000OOO0OO0O000O .get ('help')['lxml'])#line:12
if sendable :#line:14
    qwbotkey =os .getenv ('qwbotkey')#line:15
    if not qwbotkey :#line:16
        print (_OO000OOO0OO0O000O .get ('help')['qwbotkey'])#line:17
        exit ()#line:18
if pushable :#line:20
    pushconfig =os .getenv ('pushconfig')#line:21
    if not pushconfig :#line:22
        print (_OO000OOO0OO0O000O .get ('help')['pushconfig'])#line:23
        exit ()#line:24
    try :#line:25
        pushconfig =ast .literal_eval (pushconfig )#line:26
    except :#line:27
        pass #line:28
    if isinstance (pushconfig ,dict ):#line:29
        appToken =pushconfig ['appToken']#line:30
        uids =pushconfig ['uids']#line:31
        topicids =pushconfig ['topicids']#line:32
    else :#line:33
        try :#line:34
            "appToken=AT_pCenRjs;uids=['UID_9MZ','UID_T4xlqWx9x'];topicids=['xxx']"#line:35
            appToken =pushconfig .split (';')[0 ].split ('=')[1 ]#line:36
            uids =ast .literal_eval (pushconfig .split (';')[1 ].split ('=')[1 ])#line:37
            topicids =ast .literal_eval (pushconfig .split (';')[2 ].split ('=')[1 ])#line:38
        except :#line:39
            print (_OO000OOO0OO0O000O .get ('help')['pushconfig'])#line:40
            exit ()#line:41
if not pushable and not sendable :#line:42
    print ('啥通知方式都不配置，你想上天吗')#line:43
    exit ()#line:44
def ftime ():#line:47
    O000O00OO00000OOO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:48
    return O000O00OO00000OOO #line:49
def debugger (O0O0OO0OO0OOO000O ):#line:52
    if debug :#line:53
        print (O0O0OO0OO0OOO000O )#line:54
def printlog (O00000000O00OOO00 ):#line:57
    if printf :#line:58
        print (O00000000O00OOO00 )#line:59
def send (O0OOO00000OOO0O00 ,title ='通知',url =None ):#line:62
    if not url :#line:63
        OO000OOO0O0OOOOOO ={"msgtype":"text","text":{"content":f"{title}\n\n{O0OOO00000OOO0O00}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:70
    else :#line:71
        OO000OOO0O0OOOOOO ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O0OOO00000OOO0O00 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:76
    O00OO0O00O00O00OO =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:77
    OOO0OO0OO00O0O0OO =requests .post (O00OO0O00O00O00OO ,data =json .dumps (OO000OOO0O0OOOOOO )).json ()#line:78
    if OOO0OO0OO00O0O0OO .get ('errcode')!=0 :#line:79
        print ('消息发送失败，请检查key和发送格式')#line:80
        return False #line:81
    return OOO0OO0OO00O0O0OO #line:82
def push (OOOOO0OO0OO000000 ,title ='通知',url ='',uid =None ):#line:85
    if uid :#line:86
        uids .append (uid )#line:87
    OO0OOOO00OOO000OO ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',OOOOO0OO0OO000000 ).replace ('url',url )#line:89
    OOOO0OOO00000OO00 ={"appToken":appToken ,"content":OO0OOOO00OOO000OO ,"summary":title ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:99
    OO0O0O000000O00O0 ='http://wxpusher.zjiecode.com/api/send/message'#line:100
    OOOO00OO0OO0OOO0O =requests .post (url =OO0O0O000000O00O0 ,json =OOOO0OOO00000OO00 ).json ()#line:101
    if OOOO00OO0OO0OOO0O .get ('code')!=1000 :#line:102
        print (OOOO00OO0OO0OOO0O .get ('msg'),OOOO00OO0OO0OOO0O )#line:103
    return OOOO00OO0OO0OOO0O #line:104
def getmpinfo (O0O0OO00O0OOOOO00 ):#line:107
    if not O0O0OO00O0OOOOO00 or O0O0OO00O0OOOOO00 =='':#line:108
        return False #line:109
    O0OO0OOOO00OOO00O ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:111
    OO0OO0O0O0OOO0000 =requests .get (O0O0OO00O0OOOOO00 ,headers =O0OO0OOOO00OOO00O )#line:112
    O0000OO00O0O00000 =etree .HTML (OO0OO0O0O0OOO0000 .text )#line:113
    OO000000O0OO00OOO =O0000OO00O0O00000 .xpath ('//meta[@*="og:title"]/@content')#line:114
    if OO000000O0OO00OOO :#line:115
        OO000000O0OO00OOO =OO000000O0OO00OOO [0 ]#line:116
    try :#line:117
        if 'biz='in O0O0OO00O0OOOOO00 :#line:118
            OOOOOO0O0O0O00O00 =re .findall (r'biz=(.*?)&',O0O0OO00O0OOOOO00 )[0 ]#line:119
        else :#line:120
            OOO0O00O0OOO000O0 =O0000OO00O0O00000 .xpath ('//meta[@*="og:url"]/@content')[0 ]#line:121
            OOOOOO0O0O0O00O00 =re .findall (r'biz=(.*?)&',str (OOO0O00O0OOO000O0 ))[0 ]#line:122
    except :#line:123
        return False #line:124
    O00OO0000O00OO0O0 =O0000OO00O0O00000 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:125
    if O00OO0000O00OO0O0 :#line:126
        O00OO0000O00OO0O0 =O00OO0000O00OO0O0 [0 ].strip ()#line:127
    O00OO0000OO00OOOO =re .findall (r"user_name.DATA'\) : '(.*?)'",OO0OO0O0O0OOO0000 .text )or O0000OO00O0O00000 .xpath ('//span[@class="profile_meta_value"]/text()')#line:129
    if O00OO0000OO00OOOO :#line:130
        O00OO0000OO00OOOO =O00OO0000OO00OOOO [0 ]#line:131
    OOO0O0OO0OO0O0O00 =re .findall (r'createTime = \'(.*)\'',OO0OO0O0O0OOO0000 .text )#line:132
    if OOO0O0OO0OO0O0O00 :#line:133
        OOO0O0OO0OO0O0O00 =OOO0O0OO0OO0O0O00 [0 ][5 :]#line:134
    O00O000000000O00O =f'{OOO0O0OO0OO0O0O00}|{OO000000O0OO00OOO[:10]}|{OOOOOO0O0O0O00O00}|{O00OO0000O00OO0O0}|{O00OO0000OO00OOOO}'#line:135
    OOO0OO00O000OOO00 ={'biz':OOOOOO0O0O0O00O00 ,'text':O00O000000000O00O }#line:136
    return OOO0OO00O000OOO00 #line:137
class MTZYD :#line:140
    def __init__ (O0O0OO0OOOO000O0O ,OOO0OO00O0000000O ):#line:141
        OOO0OO00O0000000O =OOO0OO00O0000000O .split (';')#line:142
        if ''in OOO0OO00O0000000O :#line:143
            OOO0OO00O0000000O .pop ('')#line:144
        O0O0OO0OOOO000O0O .name =OOO0OO00O0000000O [0 ].split ('=')[1 ]#line:145
        O0O0OO0OOOO000O0O .uid =OOO0OO00O0000000O [2 ].split ('=')[1 ]if len (OOO0OO00O0000000O )==3 else None #line:146
        O0O0OO0OOOO000O0O .ck =OOO0OO00O0000000O [1 ].split ('=')[1 ]#line:147
        O0O0OO0OOOO000O0O .s =requests .session ()#line:148
        O0O0OO0OOOO000O0O .s .headers ={'Authorization':O0O0OO0OOOO000O0O .ck ,'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5279 MMWEBSDK/20230805 MMWEBID/2833 MicroMessenger/8.0.42.2460(0x28002A3B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Accept':'*/*','Origin':'http://51697622081.tt.bendishenghuochwl1.cn','Referer':'http://51697622081.tt.bendishenghuochwl1.cn/','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh',}#line:158
        O0O0OO0OOOO000O0O .msg =''#line:159
    def user_info (OOOOOOO0000O00OO0 ):#line:161
        OOOO00O0O0O00O0O0 ='https://api2.wanjd.cn/h5_share/user/info'#line:162
        O0O0OO0OO0000O00O =OOOOOOO0000O00OO0 .s .post (OOOO00O0O0O00O0O0 ,json ={"openid":0 }).json ()#line:163
        debugger (f'userinfo {O0O0OO0OO0000O00O}')#line:164
        if O0O0OO0OO0000O00O .get ('code')==200 :#line:165
            OOOOOOO0000O00OO0 .nickname =O0O0OO0OO0000O00O .get ('data').get ('nickname')#line:166
            OOOOOOO0000O00OO0 .points =O0O0OO0OO0000O00O .get ('data').get ('points')-O0O0OO0OO0000O00O .get ('data').get ('withdraw_points')#line:167
            O0O0OO0OO0000O00O =OOOOOOO0000O00OO0 .s .post ('https://api2.wanjd.cn/h5_share/user/info',json ={"openid":0 })#line:168
            debugger (f'签到 {O0O0OO0OO0000O00O.json()}')#line:169
            OO00OO0OOOO00O0OO =O0O0OO0OO0000O00O .json ().get ('message')#line:170
            OOOOOOO0000O00OO0 .msg +=f'\n【{OOOOOOO0000O00OO0.name}】:{OOOOOOO0000O00OO0.nickname},现有积分：{OOOOOOO0000O00OO0.points}，{OO00OO0OOOO00O0OO}\n'+'-'*50 +'\n'#line:171
            printlog (f'【{OOOOOOO0000O00OO0.name}】:{OOOOOOO0000O00OO0.nickname},现有积分：{OOOOOOO0000O00OO0.points}，{OO00OO0OOOO00O0OO}')#line:172
            OOOO00O0O0O00O0O0 ='http://api2.wanjd.cn/h5_share/user/up_profit_ratio'#line:173
            OO000O0O00O0O00O0 ={"openid":0 }#line:174
            try :#line:175
                O0O0OO0OO0000O00O =OOOOOOO0000O00OO0 .s .post (OOOO00O0O0O00O0O0 ,json =OO000O0O00O0O00O0 ).json ()#line:176
                if O0O0OO0OO0000O00O .get ('code')==500 :#line:177
                    raise #line:178
                OOOOOOO0000O00OO0 .msg +=f'代理升级：{O0O0OO0OO0000O00O.get("message")}\n'#line:179
                printlog (f'代理升级：{O0O0OO0OO0000O00O.get("message")}\n')#line:180
            except :#line:181
                OOOO00O0O0O00O0O0 ='http://api2.wanjd.cn/h5_share/user/task_reward'#line:182
                for OO00000OOO0OOOO0O in range (0 ,8 ):#line:183
                    OO000O0O00O0O00O0 ={"type":OO00000OOO0OOOO0O ,"openid":0 }#line:184
                    O0O0OO0OO0000O00O =OOOOOOO0000O00OO0 .s .post (OOOO00O0O0O00O0O0 ,json =OO000O0O00O0O00O0 ).json ()#line:185
                    if '积分未满'in O0O0OO0OO0000O00O .get ('message'):#line:186
                        break #line:187
                    if O0O0OO0OO0000O00O .get ('code')!=500 :#line:188
                        OOOOOOO0000O00OO0 .msg +='主页奖励积分：'+O0O0OO0OO0000O00O .get ('message')+'\n'#line:189
                        printlog (f'【{OOOOOOO0000O00OO0.name}】:主页奖励积分 {O0O0OO0OO0000O00O.get("message")}')#line:190
                    OO00000OOO0OOOO0O +=1 #line:191
                    time .sleep (0.5 )#line:192
            return True #line:193
        else :#line:194
            OOOOOOO0000O00OO0 .msg +='获取账号信息异常，检查cookie是否失效\n'#line:195
            printlog (f'【{OOOOOOO0000O00OO0.name}】:获取账号信息异常，检查cookie是否失效')#line:196
            return False #line:197
    def get_read (O00O0OO00OO000O0O ):#line:199
        OO0000OO0O0O00OO0 ='http://api2.wanjd.cn/h5_share/daily/get_read'#line:200
        O0O0O00OOO0OOO0O0 ={"openid":0 }#line:201
        O00000OO000O0OOO0 =0 #line:202
        while O00000OO000O0OOO0 <10 :#line:203
            O00000O0O000OO00O =O00O0OO00OO000O0O .s .post (OO0000OO0O0O00OO0 ,json =O0O0O00OOO0OOO0O0 ).json ()#line:204
            debugger (f'getread {O00000O0O000OO00O}')#line:205
            if O00000O0O000OO00O .get ('code')==200 :#line:206
                O00O0OO00OO000O0O .link =O00000O0O000OO00O .get ('data').get ('link')#line:207
                return True #line:208
            elif '获取失败'in O00000O0O000OO00O .get ('message'):#line:209
                time .sleep (15 )#line:210
                O00000OO000O0OOO0 +=1 #line:211
                continue #line:212
            else :#line:213
                O00O0OO00OO000O0O .msg +=O00000O0O000OO00O .get ('message')+'\n'#line:214
                printlog (f'【{O00O0OO00OO000O0O.name}】:{O00000O0O000OO00O.get("message")}')#line:215
                return False #line:216
    def gettaskinfo (O000OO0OO0000OOO0 ,OOOO00OO0OOO00OOO ):#line:218
        for OOO00000OO000O0O0 in OOOO00OO0OOO00OOO :#line:219
            if OOO00000OO000O0O0 .get ('url'):#line:220
                return OOO00000OO000O0O0 #line:221
    def dotasks (O0OO00O0OO000OO0O ):#line:223
        O00OOOO0OO000OO0O ={'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Origin':'http://nei594688.594688be.com.byymmmcm3.cn','Referer':'http://nei594688.594688be.com.byymmmcm3.cn/','Accept-Encoding':'gzip, deflate',}#line:230
        OOOO0O00O00OOOO00 =0 #line:231
        while True :#line:232
            OO0OOOOO0O0OO0O0O ={"href":O0OO00O0OO000OO0O .link }#line:233
            OO0OO0OO0OOOOO0O0 ='https://api2.wanjd.cn/wxread/articles/tasks'#line:234
            OOO0OO0O0OOOOOO0O =requests .post (OO0OO0OO0OOOOO0O0 ,headers =O00OOOO0OO000OO0O ,json =OO0OOOOO0O0OO0O0O ).json ()#line:235
            O00O00OOOOO0O0O0O =OOO0OO0O0OOOOOO0O .get ('data')#line:236
            debugger (f'tasks {O00O00OOOOO0O0O0O}')#line:237
            O0OO0OO0O0O000000 =[O00O00O00O0OO0O00 ['is_read']for O00O00O00O0OO0O00 in O00O00OOOOO0O0O0O ]#line:238
            if 0 not in O0OO0OO0O0O000000 :#line:239
                break #line:240
            if OOO0OO0O0OOOOOO0O .get ('code')!=200 :#line:241
                O0OO00O0OO000OO0O .msg +=OOO0OO0O0OOOOOO0O .get ('message')+'\n'#line:242
                printlog (f'【{O0OO00O0OO000OO0O.name}】:{OOO0OO0O0OOOOOO0O.get("message")}')#line:243
                break #line:244
            else :#line:245
                O0OO0OO00000000OO =O0OO00O0OO000OO0O .gettaskinfo (OOO0OO0O0OOOOOO0O ['data'])#line:246
                if not O0OO0OO00000000OO :#line:247
                    break #line:248
                O0OOO0OO000O000OO =O0OO0OO00000000OO .get ('url')#line:249
                if len (O00O00OOOOO0O0O0O )<total_num :#line:250
                    printlog (f'【{O0OO00O0OO000OO0O.name}】:任务数量小于{total_num}，任务中止')#line:251
                    break #line:252
                O0O0000OO0000O00O =O0OO0OO00000000OO ['id']#line:253
                debugger (O0O0000OO0000O00O )#line:254
                OO0OOOOO0O0OO0O0O .update ({"id":O0O0000OO0000O00O })#line:255
                OOO0O0000O0O0OO00 =getmpinfo (O0OOO0OO000O000OO )#line:256
                try :#line:257
                    O0OO00O0OO000OO0O .msg +='正在阅读 '+OOO0O0000O0O0OO00 ['text']+'\n'#line:258
                    printlog (f'【{O0OO00O0OO000OO0O.name}】:正在阅读{OOO0O0000O0O0OO00["text"]}')#line:259
                except :#line:260
                    O0OO00O0OO000OO0O .msg +='获取文章信息失败\n'#line:261
                    printlog (f'【{O0OO00O0OO000OO0O.name}】:获取文章信息失败')#line:262
                    break #line:263
                if len (str (O0O0000OO0000O00O ))<5 :#line:264
                    if OOOO0O00O00OOOO00 ==3 :#line:265
                        if sendable :#line:266
                            send ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',f'【{O0OO00O0OO000OO0O.name}】 美添赚过检测',)#line:269
                        if pushable :#line:270
                            push ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束\n点击阅读检测文章',f'【{O0OO00O0OO000OO0O.name}】 美添赚过检测',)#line:273
                        break #line:274
                    if sendable :#line:275
                        send (OOO0O0000O0O0OO00 .get ('text'),f'【{O0OO00O0OO000OO0O.name}】{O0OO00O0OO000OO0O.nickname} 美添赚过检测',O0OOO0OO000O000OO )#line:276
                    if pushable :#line:277
                        push (f'【{O0OO00O0OO000OO0O.name}】{O0OO00O0OO000OO0O.nickname} 本轮任务数量{len(O00O00OOOOO0O0O0O) - 1}\n点击阅读检测文章\n{OOO0O0000O0O0OO00["text"]}',f'【{O0OO00O0OO000OO0O.name}】 {O0OO00O0OO000OO0O.nickname}美添赚过检测',O0OOO0OO000O000OO ,O0OO00O0OO000OO0O .uid )#line:281
                    O0OO00O0OO000OO0O .msg +='发送通知，暂停50秒\n'#line:282
                    printlog (f'【{O0OO00O0OO000OO0O.name}】:发送通知，暂停50秒')#line:283
                    OOOO0O00O00OOOO00 +=1 #line:284
                    time .sleep (50 )#line:285
                O0O00O0O0O0O0OOO0 =random .randint (7 ,10 )#line:286
                time .sleep (O0O00O0O0O0O0OOO0 )#line:287
                OO0OO0OO0OOOOO0O0 ='https://api2.wanjd.cn/wxread/articles/three_read'#line:288
                OOO0OO0O0OOOOOO0O =requests .post (OO0OO0OO0OOOOO0O0 ,headers =O00OOOO0OO000OO0O ,json =OO0OOOOO0O0OO0O0O ).json ()#line:289
                if OOO0OO0O0OOOOOO0O .get ('code')==200 :#line:290
                    O0OO00O0OO000OO0O .msg +='阅读成功'+'\n'+'-'*50 +'\n'#line:291
                    printlog (f'【{O0OO00O0OO000OO0O.name}】:阅读成功')#line:292
                if OOO0OO0O0OOOOOO0O .get ('code')!=200 :#line:293
                    O0OO00O0OO000OO0O .msg +=OOO0OO0O0OOOOOO0O .get ('message')+'\n'+'-'*50 +'\n'#line:294
                    printlog (f'【{O0OO00O0OO000OO0O.name}】:{OOO0OO0O0OOOOOO0O.get("message")}')#line:295
                    break #line:296
        OO0OO0OO0OOOOO0O0 ='https://api2.wanjd.cn/wxread/articles/check_success'#line:297
        OO0OOOOO0O0OO0O0O ={'type':1 ,'href':O0OO00O0OO000OO0O .link }#line:298
        OOO0OO0O0OOOOOO0O =requests .post (OO0OO0OO0OOOOO0O0 ,headers =O00OOOO0OO000OO0O ,json =OO0OOOOO0O0OO0O0O ).json ()#line:299
        debugger (f'check {OOO0OO0O0OOOOOO0O}')#line:300
        O0OO00O0OO000OO0O .msg +=OOO0OO0O0OOOOOO0O .get ('message')+'\n'#line:301
        printlog (f'【{O0OO00O0OO000OO0O.name}】:{OOO0OO0O0OOOOOO0O.get("message")}')#line:302
    def withdraw (O00O0O0O0OO0O0O00 ):#line:304
        if O00O0O0O0OO0O0O00 .points <txbz :#line:305
            O00O0O0O0OO0O0O00 .msg +=f'没有达到你设置的提现标准{txbz}\n'#line:306
            printlog (f'【{O00O0O0O0OO0O0O00.name}】:没有达到你设置的提现标准{txbz}')#line:307
            return False #line:308
        O00000OOO0OO0O000 ='https://api2.wanjd.cn/h5_share/user/withdraw'#line:309
        O0O0OO0O000000O00 =O00O0O0O0OO0O0O00 .s .post (O00000OOO0OO0O000 ).json ()#line:310
        O00O0O0O0OO0O0O00 .msg +='提现结果'+O0O0OO0O000000O00 .get ('message')+'\n'#line:311
        printlog (f'【{O00O0O0O0OO0O0O00.name}】:提现结果 {O0O0OO0O000000O00.get("message")}')#line:312
        if O0O0OO0O000000O00 .get ('code')==200 :#line:313
            if sendable :#line:314
                send (f'【{O00O0O0O0OO0O0O00.name}】:已提现到红包，请在服务通知内及时领取','每天赚提现通知')#line:315
            if pushable :#line:316
                push (f'【{O00O0O0O0OO0O0O00.name}】:已提现到红包，请在服务通知内及时领取','每天赚提现通知','https://jihulab.com/xizhiai/xiaoym',O00O0O0O0OO0O0O00 .uid )#line:318
    def run (O0O0OO00O000O0O00 ):#line:320
        O0O0OO00O000O0O00 .msg +='*'*50 +f'\n【{O0O0OO00O000O0O00.name}】:开始任务\n'#line:321
        printlog (f'【{O0O0OO00O000O0O00.name}】:开始任务')#line:322
        if not O0O0OO00O000O0O00 .user_info ():#line:323
            return False #line:324
        if O0O0OO00O000O0O00 .get_read ():#line:325
            O0O0OO00O000O0O00 .dotasks ()#line:326
            O0O0OO00O000O0O00 .user_info ()#line:327
        O0O0OO00O000O0O00 .withdraw ()#line:328
        printlog (f'【{O0O0OO00O000O0O00.name}】:任务结束')#line:329
        if not printf :#line:330
            print (O0O0OO00O000O0O00 .msg .strip ())#line:331
            print (f'【{O0O0OO00O000O0O00.name}】:任务结束')#line:332
def yd (O000OO0000O00O0O0 ):#line:335
    while not O000OO0000O00O0O0 .empty ():#line:336
        OO0O00000O00OO0O0 =O000OO0000O00O0O0 .get ()#line:337
        OOO000O0OOOO000O0 =MTZYD (OO0O00000O00OO0O0 )#line:338
        OOO000O0OOOO000O0 .run ()#line:339
def get_info ():#line:342
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:344
    print ('入口：http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552')#line:345
    O00O0O00O0OO00000 ='v2.3'#line:346
    OO0O0OOOOOOO00OOO =_OO000OOO0OO0O000O ['version']['k_mtz']#line:347
    print (f'当前版本{O00O0O00O0OO00000}，仓库版本{OO0O0OOOOOOO00OOO}\n{_OO000OOO0OO0O000O["update_log"]["每天赚"]}')#line:348
    if O00O0O00O0OO00000 <OO0O0OOOOOOO00OOO :#line:349
        print ('请到仓库下载最新版本k_mtz.py')#line:350
    print ("="*25 )#line:351
    return True #line:352
def main ():#line:355
    O0O0O00O000O0000O =get_info ()#line:356
    O0OO000OO00O00OOO =os .getenv ('mtzv2ck')#line:357
    if not O0OO000OO00O00OOO :#line:358
        print (_OO000OOO0OO0O000O .get ('msg')['每天赚'])#line:359
        exit ()#line:360
    O0OO000OO00O00OOO =O0OO000OO00O00OOO .split ('&')#line:361
    O0O0O0OO0OOO00OOO =Queue ()#line:362
    OOOOOO00OOOO00O0O =[]#line:363
    print (f'共获取到{len(O0OO000OO00O00OOO)}个账号\n'+'*'*20 )#line:364
    if not O0O0O00O000O0000O :#line:365
        exit ()#line:366
    for O00O00000O0O00000 ,OOO0OOO00OOOO0O00 in enumerate (O0OO000OO00O00OOO ,start =1 ):#line:367
        O0O0O0OO0OOO00OOO .put (OOO0OOO00OOOO0O00 )#line:368
    for O00O00000O0O00000 in range (max_workers ):#line:369
        OOOO0000OOOO0000O =threading .Thread (target =yd ,args =(O0O0O0OO0OOO00OOO ,))#line:370
        OOOO0000OOOO0000O .start ()#line:371
        OOOOOO00OOOO00O0O .append (OOOO0000OOOO0000O )#line:372
        time .sleep (delay_time )#line:373
    for O0OOO00O0O0OO0O0O in OOOOOO00OOOO00O0O :#line:374
        O0OOO00O0O0OO0O0O .join ()#line:375
if __name__ =='__main__':#line:378
    main ()#line:379
