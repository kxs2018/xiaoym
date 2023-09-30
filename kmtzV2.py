# -*- coding: utf-8 -*-
# kmtzV2
# Author: kk
# date：2023/9/28 20:12
"""
每天赚入口：http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552
推送检测文章
1.通过企业微信机器人推送到企业微信群，请务必用微信关注微信插件并配置好机器人key
qwbotkey="xxxxxxxxx"
参考https://github.com/kxs2018/yuedu/blob/main/获取企业微信群机器人key.md 获取key，并关注插件！！！
2.wxpusher公众号
参考https://wxpusher.zjiecode.com/docs/#/ 获取apptoken、topicids、uids，填入pushconfig
pushconfig="appToken=AT_pCenRjs;uids=['UID_9MZ','UID_T4xlqWx9x'];topicids=['xxxx']"
环境变量pushconfig 值appToken=AT_pCenRjs;uids=['UID_9MZ','UID_T4xlqWx9x'];topicids=['xxxx']
单发时无需设置uids topicids，留空但需保留[]，在mtzv2ck中配置uid
注：用过1.x版本的无需再次设置

打开活动入口，抓包的任意接口headers中的Authorization参数，填入ck。
单账户填写样式(这里只是样式，不要填这里)
mtzv2ck="name=xxx;ck=share:login:xxxx;uid=xxx" 配置环境变量中不带引号
多账号用&连接，或者环境变量中添加多个mtzv2ck
其中uid为wxpusher单对单发送通知专用，群发和企业微信无需配置

参数解释
name:账号名，你可以随便填，用来推送时分辨哪一个账号
ck:账号的ck,抓包的任意接口headers中的Authorization参数，格式为share:login:xxxx
------------------------------------------------------------------------
运行提示 no module named lxml 解决方法
1. 在配置文件找到
## 安装python依赖时指定pip源
PipMirror="https://pypi.tuna.tsinghua.edu.cn/simple"
如果这条链接包含douban的，换成和上面一样的
2. 依赖-python 添加lxml
3. 如果装不上，尝试升级pip：①ssh连接到服务器 ②docker exec -it ql bash ③pip install pip -U
ql是青龙容器的名字，docker ps可查询
"""

import json
import os
import random
import requests
import re
import time
import ast

try:
    from lxml import etree
except:
    print('请仔细阅读脚本上方注释中的“no module named lxml 解决方案”')
    exit()
import datetime
import threading
from queue import Queue

"""实时日志开关"""
printf = 1
"""1为开，0为关"""

"""debug模式开关"""
debug = 0
"""1为开，打印调试日志；0为关，不打印"""

"""线程数量设置"""
max_workers = 5
"""填入数字，设置同时跑任务的数量"""

"""设置提现标准"""
txbz = 1000  # 不低于1000，平台的提现标准为1000
"""设置为1000，即为1元起提"""

"""企业微信推送开关"""
sendable = 1  # 开启后必须设置qwbotkey才能运行
"""1为开，0为关"""
if sendable:
    qwbotkey = os.getenv('qwbotkey')
    if not qwbotkey:
        print('请仔细阅读上方注释并设置好key')
        exit()

"""wxpusher推送开关"""
pushable = 0  # 开启后必须设置pushconfig才能运行
"""1为开，0为关"""

if pushable :#line:1
    pushconfig =os .getenv ('pushconfig')#line:2
    if not pushconfig :#line:3
        print ('请仔细阅读上方注释并设置好pushconfig')#line:4
        exit ()#line:5
    try :#line:6
        pushconfig =ast .literal_eval (pushconfig )#line:7
    except :#line:8
        pass #line:9
    if isinstance (pushconfig ,dict ):#line:10
        appToken =pushconfig ['appToken']#line:11
        uids =pushconfig ['uids']#line:12
        topicids =pushconfig ['topicids']#line:13
    else :#line:14
        try :#line:15
            "appToken=AT_pCenRjs;uids=['UID_9MZ','UID_T4xlqWx9x'];topicids=['xxx']"#line:16
            appToken =pushconfig .split (';')[0 ].split ('=')[1 ]#line:17
            uids =ast .literal_eval (pushconfig .split (';')[1 ].split ('=')[1 ])#line:18
            topicids =ast .literal_eval (pushconfig .split (';')[2 ].split ('=')[1 ])#line:19
        except :#line:20
            print ('请仔细阅读上方注释并设置好pushconfig')#line:21
            exit ()#line:22
def ftime ():#line:107
    O0O0OOOOOO0OOOO00 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:108
    return O0O0OOOOOO0OOOO00 #line:109
def debugger (O0000OO00OO000OOO ):#line:112
    if debug :#line:113
        print (O0000OO00OO000OOO )#line:114
def printlog (OO0O0000OO0OO0OOO ):#line:117
    if printf :#line:118
        print (OO0O0000OO0OO0OOO )#line:119
def send (O0OOO00O0OOO000OO ,title ='通知',url =None ):#line:122
    if not url :#line:123
        OO0000000O000OOOO ={"msgtype":"text","text":{"content":f"{title}\n\n{O0OOO00O0OOO000OO}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:130
    else :#line:131
        OO0000000O000OOOO ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O0OOO00O0OOO000OO ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:136
    O0O0O0O0O00000OO0 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:137
    O0O000O0O0OOOO000 =requests .post (O0O0O0O0O00000OO0 ,data =json .dumps (OO0000000O000OOOO )).json ()#line:138
    if O0O000O0O0OOOO000 .get ('errcode')!=0 :#line:139
        print ('消息发送失败，请检查key和发送格式')#line:140
        return False #line:141
    return O0O000O0O0OOOO000 #line:142
def push (O0O00000OOOO00OO0 ,OO0O00000000O0O00 ,url ='',uid =None ):#line:145
    if uid :#line:146
        uids .append (uid )#line:147
    OO000OO0O00O0O0OO ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',O0O00000OOOO00OO0 ).replace ('url',url )#line:149
    O0OOOO0O0OOOOOOO0 ={"appToken":appToken ,"content":OO000OO0O00O0O0OO ,"summary":OO0O00000000O0O00 ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:159
    O00OOOO0OOO0OOOO0 ='http://wxpusher.zjiecode.com/api/send/message'#line:160
    O0OOO0OOO0O0OOO00 =requests .post (url =O00OOOO0OOO0OOOO0 ,json =O0OOOO0O0OOOOOOO0 ).json ()#line:161
    if O0OOO0OOO0O0OOO00 .get ('code')!=1000 :#line:162
        print (O0OOO0OOO0O0OOO00 .get ('msg'),O0OOO0OOO0O0OOO00 )#line:163
    return O0OOO0OOO0O0OOO00 #line:164
def getmpinfo (OO000000OOO0O00OO ):#line:167
    if not OO000000OOO0O00OO or OO000000OOO0O00OO =='':#line:168
        return False #line:169
    O0OO00O00OO0000O0 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:171
    O00O00OOOO0000OOO =requests .get (OO000000OOO0O00OO ,headers =O0OO00O00OO0000O0 )#line:172
    OO0000OOOOOO000O0 =etree .HTML (O00O00OOOO0000OOO .text )#line:173
    O0OOOOO0OOOOO00OO =OO0000OOOOOO000O0 .xpath ('//meta[@*="og:title"]/@content')#line:174
    if O0OOOOO0OOOOO00OO :#line:175
        O0OOOOO0OOOOO00OO =O0OOOOO0OOOOO00OO [0 ]#line:176
    try :#line:177
        if 'biz='in OO000000OOO0O00OO :#line:178
            OOOOOOOOO00000O0O =re .findall (r'biz=(.*?)&',OO000000OOO0O00OO )[0 ]#line:179
        else :#line:180
            O0O0000OOOOOOO000 =OO0000OOOOOO000O0 .xpath ('//meta[@*="og:url"]/@content')[0 ]#line:181
            OOOOOOOOO00000O0O =re .findall (r'biz=(.*?)&',str (O0O0000OOOOOOO000 ))[0 ]#line:182
    except :#line:183
        return False #line:184
    OO0O0OOO0OOOOOO0O =OO0000OOOOOO000O0 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:185
    if OO0O0OOO0OOOOOO0O :#line:186
        OO0O0OOO0OOOOOO0O =OO0O0OOO0OOOOOO0O [0 ].strip ()#line:187
    O000OO00OOO0O0O00 =re .findall (r"user_name.DATA'\) : '(.*?)'",O00O00OOOO0000OOO .text )or OO0000OOOOOO000O0 .xpath ('//span[@class="profile_meta_value"]/text()')#line:189
    if O000OO00OOO0O0O00 :#line:190
        O000OO00OOO0O0O00 =O000OO00OOO0O0O00 [0 ]#line:191
    O00OO0OO0OO00O0O0 =re .findall (r'createTime = \'(.*)\'',O00O00OOOO0000OOO .text )#line:192
    if O00OO0OO0OO00O0O0 :#line:193
        O00OO0OO0OO00O0O0 =O00OO0OO0OO00O0O0 [0 ][5 :]#line:194
    OOO00O0O00O00OO0O =f'{O00OO0OO0OO00O0O0}|{O0OOOOO0OOOOO00OO}|{OOOOOOOOO00000O0O}|{OO0O0OOO0OOOOOO0O}|{O000OO00OOO0O0O00}'#line:195
    OOO0OO00OOO00O0OO ={'biz':OOOOOOOOO00000O0O ,'text':OOO00O0O00O00OO0O }#line:196
    return OOO0OO00OOO00O0OO #line:197
class MTZYD :#line:200
    def __init__ (OOO0O0O00O00000O0 ,OO0O00O0OO0O0OO0O ):#line:201
        OO0O00O0OO0O0OO0O =OO0O00O0OO0O0OO0O .split (';')#line:202
        if ''in OO0O00O0OO0O0OO0O :#line:203
            OO0O00O0OO0O0OO0O .pop ('')#line:204
        OOO0O0O00O00000O0 .name =OO0O00O0OO0O0OO0O [0 ].split ('=')[1 ]#line:205
        OOO0O0O00O00000O0 .uid =OO0O00O0OO0O0OO0O [2 ].split ('=')[1 ]if len (OO0O00O0OO0O0OO0O )==3 else None #line:206
        OOO0O0O00O00000O0 .ck =OO0O00O0OO0O0OO0O [1 ].split ('=')[1 ]#line:207
        OOO0O0O00O00000O0 .s =requests .session ()#line:208
        OOO0O0O00O00000O0 .s .headers ={'Authorization':OOO0O0O00O00000O0 .ck ,'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Accept':'*/*','Origin':'http://61695315208.tt.bendishenghuochwl1.cn','Referer':'http://61695315208.tt.bendishenghuochwl1.cn/','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh',}#line:218
        OOO0O0O00O00000O0 .msg =''#line:219
    def user_info (OOO0O000O0OO00OO0 ):#line:221
        OOOOOOO00OO0000OO ='http://api.mengmorwpt1.cn/h5_share/user/info'#line:222
        O000O00OO0O000O00 =OOO0O000O0OO00OO0 .s .post (OOOOOOO00OO0000OO ,json ={"openid":0 }).json ()#line:223
        debugger (f'userinfo {O000O00OO0O000O00}')#line:224
        if O000O00OO0O000O00 .get ('code')==200 :#line:225
            OOO0O000O0OO00OO0 .nickname =O000O00OO0O000O00 .get ('data').get ('nickname')#line:226
            OOO0O000O0OO00OO0 .points =O000O00OO0O000O00 .get ('data').get ('points')-O000O00OO0O000O00 .get ('data').get ('withdraw_points')#line:227
            O000O00OO0O000O00 =OOO0O000O0OO00OO0 .s .post ('http://api.mengmorwpt1.cn/h5_share/user/sign',json ={"openid":0 })#line:228
            debugger (f'签到 {O000O00OO0O000O00.json()}')#line:229
            OOOOOOOOOOO00O000 =O000O00OO0O000O00 .json ().get ('message')#line:230
            OOO0O000O0OO00OO0 .msg +=f'\n账号：{OOO0O000O0OO00OO0.nickname},现有积分：{OOO0O000O0OO00OO0.points}，{OOOOOOOOOOO00O000}\n'+'-'*50 +'\n'#line:231
            printlog (f'{OOO0O000O0OO00OO0.nickname}:现有积分：{OOO0O000O0OO00OO0.points}，{OOOOOOOOOOO00O000}')#line:232
            OOOOOOO00OO0000OO ='http://api.mengmorwpt1.cn/h5_share/user/up_profit_ratio'#line:233
            OO000O00OOO00O000 ={"openid":0 }#line:234
            try :#line:235
                O000O00OO0O000O00 =OOO0O000O0OO00OO0 .s .post (OOOOOOO00OO0000OO ,json =OO000O00OOO00O000 ).json ()#line:236
                if O000O00OO0O000O00 .get ('code')==500 :#line:237
                    raise #line:238
                OOO0O000O0OO00OO0 .msg +=f'代理升级：{O000O00OO0O000O00.get("message")}\n'#line:239
            except :#line:240
                OOOOOOO00OO0000OO ='http://api.mengmorwpt1.cn/h5_share/user/task_reward'#line:241
                for OOOOOO0OO0OOO00OO in range (0 ,8 ):#line:242
                    OO000O00OOO00O000 ={"type":OOOOOO0OO0OOO00OO ,"openid":0 }#line:243
                    O000O00OO0O000O00 =OOO0O000O0OO00OO0 .s .post (OOOOOOO00OO0000OO ,json =OO000O00OOO00O000 ).json ()#line:244
                    if '积分未满'in O000O00OO0O000O00 .get ('message'):#line:245
                        break #line:246
                    if O000O00OO0O000O00 .get ('code')!=500 :#line:247
                        OOO0O000O0OO00OO0 .msg +='主页奖励积分：'+O000O00OO0O000O00 .get ('message')+'\n'#line:248
                    OOOOOO0OO0OOO00OO +=1 #line:249
                    time .sleep (0.5 )#line:250
            return True #line:251
        else :#line:252
            OOO0O000O0OO00OO0 .msg +='获取账号信息异常，检查cookie是否失效\n'#line:253
            printlog (f'{OOO0O000O0OO00OO0.name}:获取账号信息异常，检查cookie是否失效')#line:254
            if sendable :#line:255
                send (f'{OOO0O000O0OO00OO0.name} 每天赚获取账号信息异常，检查cookie是否失效','每天赚账号异常通知')#line:256
            if pushable :#line:257
                push (f'{OOO0O000O0OO00OO0.name} 每天赚获取账号信息异常，检查cookie是否失效','每天赚账号异常通知',uid =OOO0O000O0OO00OO0 .uid )#line:258
            return False #line:259
    def get_read (OOOOO0O00O0OO00O0 ):#line:261
        OO0OOO0O00OO00000 ='http://api.mengmorwpt1.cn/h5_share/daily/get_read'#line:262
        OOO000O0OO000O0OO ={"openid":0 }#line:263
        OOOO0OOO00O0000OO =0 #line:264
        while OOOO0OOO00O0000OO <10 :#line:265
            O0O00OOO00O00O00O =OOOOO0O00O0OO00O0 .s .post (OO0OOO0O00OO00000 ,json =OOO000O0OO000O0OO ).json ()#line:266
            debugger (f'getread {O0O00OOO00O00O00O}')#line:267
            if O0O00OOO00O00O00O .get ('code')==200 :#line:268
                OOOOO0O00O0OO00O0 .link =O0O00OOO00O00O00O .get ('data').get ('link')#line:269
                return True #line:270
            elif '获取失败'in O0O00OOO00O00O00O .get ('message'):#line:271
                time .sleep (15 )#line:272
                OOOO0OOO00O0000OO +=1 #line:273
                continue #line:274
            else :#line:275
                OOOOO0O00O0OO00O0 .msg +=O0O00OOO00O00O00O .get ('message')+'\n'#line:276
                printlog (f'{OOOOO0O00O0OO00O0.nickname}:{O0O00OOO00O00O00O.get("message")}')#line:277
                return False #line:278
    def gettaskinfo (O0OO0O00OO0000000 ,O00O0OOO0O00O00O0 ):#line:280
        for O0OO000O00OO0000O in O00O0OOO0O00O00O0 :#line:281
            if O0OO000O00OO0000O .get ('url'):#line:282
                return O0OO000O00OO0000O #line:283
    def dotasks (O0O0O00O0OOO000O0 ):#line:285
        OO0000OO0O0O00O00 ={'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Origin':'http://nei594688.594688be.com.byymmmcm3.cn','Referer':'http://nei594688.594688be.com.byymmmcm3.cn/','Accept-Encoding':'gzip, deflate',}#line:292
        O00OO0OO0OOOOOOO0 =1 #line:293
        while True :#line:294
            OOOO0O0O0OOO000OO ={"href":O0O0O00O0OOO000O0 .link }#line:295
            OO00O0O000OO0000O ='https://api.wanjd.cn/wxread/articles/tasks'#line:296
            OO0OO0O0OO0O0O000 =requests .post (OO00O0O000OO0000O ,headers =OO0000OO0O0O00O00 ,json =OOOO0O0O0OOO000OO ).json ()#line:297
            OO0O00O0O0O0000OO =OO0OO0O0OO0O0O000 .get ('data')#line:298
            debugger (f'tasks {OO0O00O0O0O0000OO}')#line:299
            OOOOOO0000OO00OO0 =[O0O00OOOOOO0O0O00 ['is_read']for O0O00OOOOOO0O0O00 in OO0O00O0O0O0000OO ]#line:300
            if 0 not in OOOOOO0000OO00OO0 :#line:301
                break #line:302
            if OO0OO0O0OO0O0O000 .get ('code')!=200 :#line:303
                O0O0O00O0OOO000O0 .msg +=OO0OO0O0OO0O0O000 .get ('message')+'\n'#line:304
                printlog (f'{O0O0O00O0OOO000O0.nickname}:{OO0OO0O0OO0O0O000.get("message")}')#line:305
                break #line:306
            else :#line:307
                O0OOO00OO0OO0O0O0 =O0O0O00O0OOO000O0 .gettaskinfo (OO0OO0O0OO0O0O000 ['data'])#line:308
                if not O0OOO00OO0OO0O0O0 :#line:309
                    break #line:310
                OOO0OOO00O0O000O0 =O0OOO00OO0OO0O0O0 .get ('url')#line:311
                OOOO0O0OOO0O0O000 =O0OOO00OO0OO0O0O0 ['id']#line:312
                debugger (OOOO0O0OOO0O0O000 )#line:313
                OOOO0O0O0OOO000OO .update ({"id":OOOO0O0OOO0O0O000 })#line:314
                O00OO0OO0O00OO000 =getmpinfo (OOO0OOO00O0O000O0 )#line:315
                try :#line:316
                    O0O0O00O0OOO000O0 .msg +='正在阅读 '+O00OO0OO0O00OO000 ['text']+'\n'#line:317
                    printlog (f'{O0O0O00O0OOO000O0.nickname}:正在阅读{O00OO0OO0O00OO000["text"]}')#line:318
                except :#line:319
                    O0O0O00O0OOO000O0 .msg +='获取文章信息失败\n'#line:320
                    printlog (f'{O0O0O00O0OOO000O0.nickname}:获取文章信息失败')#line:321
                    break #line:322
                if len (str (OOOO0O0OOO0O0O000 ))<5 :#line:323
                    if O00OO0OO0OOOOOOO0 ==3 :#line:324
                        if sendable :#line:325
                            send ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',f'{O0O0O00O0OOO000O0.nickname} 美添赚检测',)#line:328
                        if pushable :#line:329
                            push ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',f'{O0O0O00O0OOO000O0.nickname} 美添赚检测',)#line:332
                        break #line:333
                    if sendable :#line:334
                        send (O00OO0OO0O00OO000 .get ('text'),f'{O0O0O00O0OOO000O0.nickname} 美添赚过检测',OOO0OOO00O0O000O0 )#line:335
                    if pushable :#line:336
                        push (f'{O0O0O00O0OOO000O0.name}\n点击阅读检测文章\n{O00OO0OO0O00OO000["text"]}',f'{O0O0O00O0OOO000O0.nickname} 美添赚过检测',OOO0OOO00O0O000O0 ,uid =O0O0O00O0OOO000O0 .uid )#line:338
                    O0O0O00O0OOO000O0 .msg +='发送通知，暂停50秒\n'#line:339
                    printlog (f'{O0O0O00O0OOO000O0.nickname}:发送通知，暂停50秒')#line:340
                    O00OO0OO0OOOOOOO0 +=1 #line:341
                    time .sleep (50 )#line:342
                OO0OO000OOOOO0000 =random .randint (7 ,10 )#line:343
                time .sleep (OO0OO000OOOOO0000 )#line:344
                OO00O0O000OO0000O ='https://api.wanjd.cn/wxread/articles/three_read'#line:345
                OO0OO0O0OO0O0O000 =requests .post (OO00O0O000OO0000O ,headers =OO0000OO0O0O00O00 ,json =OOOO0O0O0OOO000OO ).json ()#line:346
                if OO0OO0O0OO0O0O000 .get ('code')==200 :#line:347
                    O0O0O00O0OOO000O0 .msg +='阅读成功'+'\n'+'-'*50 +'\n'#line:348
                    printlog (f'{O0O0O00O0OOO000O0.nickname}:阅读成功')#line:349
                if OO0OO0O0OO0O0O000 .get ('code')!=200 :#line:350
                    O0O0O00O0OOO000O0 .msg +=OO0OO0O0OO0O0O000 .get ('message')+'\n'+'-'*50 +'\n'#line:351
                    printlog (f'{O0O0O00O0OOO000O0.nickname}:{OO0OO0O0OO0O0O000.get("message")}')#line:352
                    break #line:353
        OO00O0O000OO0000O ='https://api.wanjd.cn/wxread/articles/check_success'#line:354
        OOOO0O0O0OOO000OO ={'type':1 ,'href':O0O0O00O0OOO000O0 .link }#line:355
        OO0OO0O0OO0O0O000 =requests .post (OO00O0O000OO0000O ,headers =OO0000OO0O0O00O00 ,json =OOOO0O0O0OOO000OO ).json ()#line:356
        debugger (f'check {OO0OO0O0OO0O0O000}')#line:357
        O0O0O00O0OOO000O0 .msg +=OO0OO0O0OO0O0O000 .get ('message')+'\n'#line:358
        printlog (f'{O0O0O00O0OOO000O0.nickname}:{OO0OO0O0OO0O0O000.get("message")}')#line:359
    def withdraw (O0OOO0OOO0O000O0O ):#line:361
        if O0OOO0OOO0O000O0O .points <txbz :#line:362
            O0OOO0OOO0O000O0O .msg +=f'没有达到你设置的提现标准{txbz}\n'#line:363
            printlog (f'{O0OOO0OOO0O000O0O.nickname}:没有达到你设置的提现标准{txbz}')#line:364
            return False #line:365
        O00O0O0O00O00OO00 ='http://api.mengmorwpt1.cn/h5_share/user/withdraw'#line:366
        OOO000OOO0O0OO0OO =O0OOO0OOO0O000O0O .s .post (O00O0O0O00O00OO00 ).json ()#line:367
        O0OOO0OOO0O000O0O .msg +='提现结果'+OOO000OOO0O0OO0OO .get ('message')+'\n'#line:368
        printlog (f'{O0OOO0OOO0O000O0O.nickname}:提现结果 {OOO000OOO0O0OO0OO.get("message")}')#line:369
        if OOO000OOO0O0OO0OO .get ('code')==200 :#line:370
            if sendable :#line:371
                send (f'{O0OOO0OOO0O000O0O.name} 已提现到红包，请在服务通知内及时领取','每天赚提现通知')#line:372
            if pushable :#line:373
                push (f'{O0OOO0OOO0O000O0O.name} 已提现到红包，请在服务通知内及时领取','每天赚提现通知',uid =O0OOO0OOO0O000O0O .uid )#line:374
    def run (OOO0OO0O00OO00000 ):#line:376
        OOO0OO0O00OO00000 .msg +='*'*50 +f'\n账号：{OOO0OO0O00OO00000.name}开始任务\n'#line:377
        printlog (f'账号：{OOO0OO0O00OO00000.name}开始任务')#line:378
        if not OOO0OO0O00OO00000 .user_info ():#line:379
            return False #line:380
        if OOO0OO0O00OO00000 .get_read ():#line:381
            OOO0OO0O00OO00000 .dotasks ()#line:382
            OOO0OO0O00OO00000 .user_info ()#line:383
        OOO0OO0O00OO00000 .withdraw ()#line:384
        printlog (f'账号：{OOO0OO0O00OO00000.name}:任务结束')#line:385
        if not printf :#line:386
            print (OOO0OO0O00OO00000 .msg .strip ())#line:387
            print (f'账号：{OOO0OO0O00OO00000.name}任务结束')#line:388
def yd (O00OOOOOO000O0O0O ):#line:390
    while not O00OOOOOO000O0O0O .empty ():#line:391
        O00OOOOOO00O0OO0O =O00OOOOOO000O0O0O .get ()#line:392
        O00000O0O0OO0000O =MTZYD (O00OOOOOO00O0OO0O )#line:393
        O00000O0O0OO0000O .run ()#line:394
def get_ver ():#line:397
    O0O0O0OOO0O0OOO0O ='kmtzV2 V2.0'#line:398
    O0O0OO0OO0O0OO000 ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:401
    O0OOO0O0OO00O0O0O =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O0O0OO0OO0O0OO000 ).json ()#line:403
    O00O0OO0OO0000000 =O0O0O0OOO0O0OOO0O .split (' ')[1 ]#line:404
    O000O0O00OO0O0O00 =O0OOO0O0OO00O0O0O .get ('version').get (O0O0O0OOO0O0OOO0O .split (' ')[0 ])#line:405
    O00OOOO00O0OOOO0O =f"当前版本 {O00O0OO0OO0000000}，仓库版本 {O000O0O00OO0O0O00}"#line:406
    if O00O0OO0OO0000000 <O000O0O00OO0O0O00 :#line:407
        O00OOOO00O0OOOO0O +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:408
    return O00OOOO00O0OOOO0O #line:409
def main ():#line:412
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:413
    O0O00O000OOO000O0 =os .getenv ('mtzv2ck')#line:414
    if not O0O00O000OOO000O0 :#line:415
        print ('请仔细阅读上方注释并配置好key和ck')#line:416
        exit ()#line:417
    O0O00O000OOO000O0 =O0O00O000OOO000O0 .split ('&')#line:418
    O00O0O0OO0O000O00 =Queue ()#line:419
    O0OO000O00O0OOOO0 =[]#line:420
    for OOOO00OO0O0O0O0O0 ,O0000O00O0OOO0O00 in enumerate (O0O00O000OOO000O0 ,start =1 ):#line:421
        printlog (f'{O0000O00O0OOO0O00}\n以上是账号{OOOO00OO0O0O0O0O0}的ck，如不正确，请检查ck填写格式')#line:422
        O00O0O0OO0O000O00 .put (O0000O00O0OOO0O00 )#line:423
    for OOOO00OO0O0O0O0O0 in range (max_workers ):#line:424
        O00O0O0OOO0O0O0O0 =threading .Thread (target =yd ,args =(O00O0O0OO0O000O00 ,))#line:425
        O00O0O0OOO0O0O0O0 .start ()#line:426
        O0OO000O00O0OOOO0 .append (O00O0O0OOO0O0O0O0 )#line:427
        time .sleep (20 )#line:428
    for O0OO00OOO0O000000 in O0OO000O00O0OOOO0 :#line:429
        O0OO00OOO0O000000 .join ()#line:430
if __name__ =='__main__':#line:433
    main ()#line:434
