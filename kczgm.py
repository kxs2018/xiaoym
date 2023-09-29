# -*- coding: utf-8 -*-
# k充值购买阅读
"""
仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
充值购买阅读入口：http://2502807.jl.sgzzlb.sg6gdkelit8js.cloud/?p=2502807
阅读文章抓出gfsessionid
===============================================================
推送检测文章   将多个账号检测文章推送至将多个账号检测文章推送至目标微信目标微信，手动点击链接完成检测阅读
1.企业微信群机器人
qwbotkey为企业微信webhook机器人后面的 key，填入qwbotkey
参考 https://github.com/kxs2018/yuedu/blob/main/获取企业微信群机器人key.md 获取key，并关注插件！！！
2.wxpusher公众号
参考https://wxpusher.zjiecode.com/docs/#/ 获取apptoken、topicids、uids，填入pushconfig
---------------------------------------------------------------
青龙面板，在配置文件里添加
export qwbotkey="qwbotkey"
export pushconfig="{'appToken': 'AT_pCenRjs', 'uids': ['UID_9MZ','UID_T4xlqWx9x'], 'topicids': [''],}"
export czgmck="[{'name':'xxx','ck':'gfsessionid=xxx'},{'name':'xxx','ck':'gfsessionid=xxx'},]"
---------------------------------------------------------------
no module named lxml 解决方案
1. 配置文件搜索 PipMirror，如果网址包含douban的，请改为下方的网址
PipMirror="https://pypi.tuna.tsinghua.edu.cn/simple"
2. 依赖管理-python 添加 lxml
3. 如果装不上，①请ssh连接到服务器 ②docker exec -it ql bash (ql是青龙容器的名字，不会就问百度) ③pip install pip -U
4. 再装不上依赖就放弃吧
===============================================================
"""
from io import StringIO
import threading
import ast
import hashlib
import json
import os
import random
import re
from queue import Queue
import requests
import datetime

try:
    from lxml import etree
except:
    print('请仔细阅读脚本上方注释中的“no module named lxml 解决方案”')
    exit()
import time

"""实时日志开关"""
printf = 1
"""1为开，0为关"""

"""debug模式开关"""
debug = 0
"""1为开，打印调试日志；0为关，不打印"""

"""线程数量设置"""
max_workers = 5
"""设置为5，即最多有5个任务同时进行"""

"""设置提现标准"""
txbz = 8000  # 不低于3000，平台3000起提
"""设置为8000，即为8毛起提"""

"""企业微信推送开关"""
sendable = 1  # 开启后必须设置qwbotkey才能运行
"""1为开，0为关"""
if sendable:
    qwbotkey = os.getenv('qwbotkey')
    if not qwbotkey:
        print('请仔细阅读上方注释并设置好key')
        exit()
"""wxpusher推送开关"""
pushable = 1  # 开启后必须设置pushconfig才能运行
"""1为开，0为关"""
if pushable:
    pushconfig = os.getenv('pushconfig')
    if not pushconfig:
        print('请仔细阅读上方注释并设置好pushconfig')
        exit()
    try:
        pushconfig = ast.literal_eval(pushconfig)
    except:
        pass
    if pushconfig:
        appToken = pushconfig['appToken']
        uids = pushconfig['uids']
        topicids = pushconfig['topicids']
if not pushable and not sendable:
    print('企业微信和wxpusher至少配置一个才可运行')
    exit()

checklist =['MzkyMzI5NjgxMA==','MzkzMzI5NjQ3MA==','Mzg5NTU4MzEyNQ==','Mzg3NzY5Nzg0NQ==','MzU5OTgxNjg1Mg==','Mzg4OTY5Njg4Mw==','MzI1ODcwNTgzNA==',"Mzg2NDY5NzU0Mw==",]#line:95
def ftime ():#line:98
    O000000OO0O000O0O =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:99
    return O000000OO0O000O0O #line:100
def debugger (O0OOOO0O0OOO00O0O ):#line:103
    if debug :#line:104
        print (O0OOOO0O0OOO00O0O )#line:105
def printlog (O000O00OOO00OOOOO ):#line:108
    if printf :#line:109
        print (O000O00OOO00OOOOO )#line:110
def push (OO000O0OO0000O0OO ,OOOOO00O0000O00OO ,OOO0O00OOO0O00OO0 ,uid =None ):#line:113
    if uid :#line:114
        uids .append (uid )#line:115
    O0000OOO0OO00O000 ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',OO000O0OO0000O0OO ).replace ('url',OOO0O00OOO0O00OO0 )#line:117
    O0OOOO0O0OOO0OOO0 ={"appToken":appToken ,"content":O0000OOO0OO00O000 ,"summary":OOOOO00O0000O00OO ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":OOO0O00OOO0O00OO0 ,"verifyPay":False }#line:127
    OO0O00OO0OOOO00O0 ='http://wxpusher.zjiecode.com/api/send/message'#line:128
    O0O00O0O0O000O0OO =requests .post (url =OO0O00OO0OOOO00O0 ,json =O0OOOO0O0OOO0OOO0 ).json ()#line:129
    if O0O00O0O0O000O0OO .get ('code')!=1000 :#line:130
        print (O0O00O0O0O000O0OO .get ('msg'),O0O00O0O0O000O0OO )#line:131
    return O0O00O0O0O000O0OO #line:132
def send (O0OO0OO0O000OOOO0 ,title ='通知',url =None ):#line:135
    if not title or not url :#line:136
        O0OO0OO00O00OOOO0 ={"msgtype":"text","text":{"content":f"{title}\n\n{O0OO0OO0O000OOOO0}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:143
    else :#line:144
        O0OO0OO00O00OOOO0 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O0OO0OO0O000OOOO0 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:149
    O00000OOO00000O00 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:150
    O00000OO0O000O0O0 =requests .post (O00000OOO00000O00 ,data =json .dumps (O0OO0OO00O00OOOO0 )).json ()#line:151
    if O00000OO0O000O0O0 .get ('errcode')!=0 :#line:152
        print ('消息发送失败，请检查key和发送格式')#line:153
        return False #line:154
    return O00000OO0O000O0O0 #line:155
def getmpinfo (OOOO0O0OO0OOOOOOO ):#line:158
    if not OOOO0O0OO0OOOOOOO or OOOO0O0OO0OOOOOOO =='':#line:159
        return False #line:160
    OOOOOOO0O00OO0OOO ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:162
    OO0O0OO00OO0OOOO0 =requests .get (OOOO0O0OO0OOOOOOO ,headers =OOOOOOO0O00OO0OOO )#line:163
    OO0O0O0OOO0000O00 =etree .HTML (OO0O0OO00OO0OOOO0 .text )#line:164
    O00OOOO0OOO0OO0O0 =OO0O0O0OOO0000O00 .xpath ('//meta[@*="og:title"]/@content')#line:166
    if O00OOOO0OOO0OO0O0 :#line:167
        O00OOOO0OOO0OO0O0 =O00OOOO0OOO0OO0O0 [0 ]#line:168
    O00OOO00O0OOOO0O0 =OO0O0O0OOO0000O00 .xpath ('//meta[@*="og:url"]/@content')#line:169
    if O00OOO00O0OOOO0O0 :#line:170
        O00OOO00O0OOOO0O0 =O00OOO00O0OOOO0O0 [0 ].encode ().decode ()#line:171
    try :#line:172
        OO000OO0000OO0OOO =re .findall (r'biz=(.*?)&',OOOO0O0OO0OOOOOOO )[0 ]#line:173
    except :#line:174
        OO000OO0000OO0OOO =re .findall (r'biz=(.*?)&',O00OOO00O0OOOO0O0 )[0 ]#line:175
    if not OO000OO0000OO0OOO :#line:176
        return False #line:177
    O00O0O000OOOO00OO =OO0O0O0OOO0000O00 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:178
    if O00O0O000OOOO00OO :#line:179
        O00O0O000OOOO00OO =O00O0O000OOOO00OO [0 ].strip ()#line:180
    O000O0000OOOO00OO =re .findall (r"user_name.DATA'\) : '(.*?)'",OO0O0OO00OO0OOOO0 .text )or OO0O0O0OOO0000O00 .xpath ('//span[@class="profile_meta_value"]/text()')#line:182
    if O000O0000OOOO00OO :#line:183
        O000O0000OOOO00OO =O000O0000OOOO00OO [0 ]#line:184
    O0O0OOOO00OO0O0OO =re .findall (r'createTime = \'(.*)\'',OO0O0OO00OO0OOOO0 .text )#line:185
    if O0O0OOOO00OO0O0OO :#line:186
        O0O0OOOO00OO0O0OO =O0O0OOOO00OO0O0OO [0 ][5 :]#line:187
    OOO000OOO00O000OO =f'{O0O0OOOO00OO0O0OO}|{O00OOOO0OOO0OO0O0}|{OO000OO0000OO0OOO}|{O00O0O000OOOO00OO}|{O000O0000OOOO00OO}'#line:188
    O0OOOOOOO0OO0OOOO ={'biz':OO000OO0000OO0OOO ,'text':OOO000OOO00O000OO }#line:189
    return O0OOOOOOO0OO0OOOO #line:190
class CZGM :#line:193
    def __init__ (OO0O00O00O0OOOOOO ,O0000OOO00OO0OO00 ):#line:194
        OO0O00O00O0OOOOOO .name =O0000OOO00OO0OO00 ['name']#line:195
        OO0O00O00O0OOOOOO .headers ={"User-Agent":"Mozilla/5.0 (Linux; Android 9; V1923A Build/PQ3B.190801.06161913; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36 MMWEBID/5635 MicroMessenger/8.0.40.2420(0x28002837) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64","Cookie":O0000OOO00OO0OO00 ['ck']}#line:199
        OO0O00O00O0OOOOOO .sec =requests .session ()#line:200
        OO0O00O00O0OOOOOO .sec .headers =OO0O00O00O0OOOOOO .headers #line:201
        OO0O00O00O0OOOOOO .sio =StringIO ()#line:202
    @staticmethod #line:204
    def sha_256 (OO00O00O0000000O0 ):#line:205
        OOOOOO00OO000O0O0 =f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={OO00O00O0000000O0}'#line:206
        O0O0OO00OOO0000O0 =hashlib .sha256 ()#line:207
        O0O0OO00OOO0000O0 .update (OOOOOO00OO000O0O0 .encode ())#line:208
        O0O000OO00OOO00O0 =O0O0OO00OOO0000O0 .hexdigest ()#line:209
        return O0O000OO00OOO00O0 #line:210
    def get_share_link (OO0O00OO00OO0OOO0 ):#line:212
        O0O00O00OOOO0O00O ='http://2502567.dx.wcydtd.7tojpq6xbpco0.cloud/share'#line:213
        OO00000O0O000OOO0 ={"time":str (int (time .time ())),"sign":OO0O00OO00OO0OOO0 .sha_256 (str (int (time .time ())))}#line:217
        OO0OOOO0O00O00O0O =OO0O00OO00OO0OOO0 .sec .get (O0O00O00OOOO0O00O ,data =OO00000O0O000OOO0 ).json ()#line:218
        OOO0OO0O00O0O000O =OO0OOOO0O00O00O0O ['data']['share_link'][0 ]#line:219
        return OOO0OO0O00O0O000O #line:220
    def read_info (OOO0OO000O0000OO0 ):#line:222
        try :#line:223
            O0OO0O0OOOOOO0O0O =f'http://2502567.dx.wcydtd.7tojpq6xbpco0.cloud/read/info'#line:224
            O0OOOOO000OOO000O ={"time":str (int (time .time ())),"sign":OOO0OO000O0000OO0 .sha_256 (str (int (time .time ())))}#line:228
            OOO0O0000O00O00OO =OOO0OO000O0000OO0 .sec .get (O0OO0O0OOOOOO0O0O ,data =O0OOOOO000OOO000O )#line:229
            debugger (f'readfinfo {OOO0O0000O00O00OO.text}')#line:230
            try :#line:231
                OO000O0OOOO0O0OOO =OOO0O0000O00O00OO .json ()#line:232
                OOO0OO000O0000OO0 .remain =OO000O0OOOO0O0OOO .get ("data").get ("remain")#line:233
                OOO0000OO0OO0OO00 =f'今日已经阅读了{OO000O0OOOO0O0OOO.get("data").get("read")}篇文章，今日总金币{OO000O0OOOO0O0OOO.get("data").get("gold")}，剩余{OOO0OO000O0000OO0.remain}\n邀请链接：{OOO0OO000O0000OO0.get_share_link()}'#line:234
                printlog (f'{OOO0OO000O0000OO0.name}:{OOO0000OO0OO0OO00}')#line:235
                OOO0OO000O0000OO0 .sio .write (OOO0000OO0OO0OO00 +'\n')#line:236
                return True #line:237
            except :#line:238
                printlog (f'{OOO0OO000O0000OO0.name}:{OOO0O0000O00O00OO.text}')#line:239
                OOO0OO000O0000OO0 .sio .write (OOO0O0000O00O00OO .text +'\n')#line:240
                return False #line:241
        except :#line:242
            printlog (f'{OOO0OO000O0000OO0.name}:获取用户信息失败，账号异常，请检查你的ck')#line:243
            OOO0OO000O0000OO0 .sio .write ('获取用户信息失败，账号异常，请检查你的ck\n')#line:244
            send ('{self.name}:获取用户信息失败，账号异常，请检查你的ck','钢镚阅读ck失效通知')#line:245
            return False #line:246
    def task_finish (OO0000OOOO0O00O00 ):#line:248
        O00000O0000OOOOO0 ="http://2502567.dx.wcydtd.7tojpq6xbpco0.cloud/read/finish"#line:249
        OOO000O000O000OO0 ={"time":str (int (time .time ())),"sign":OO0000OOOO0O00O00 .sha_256 (str (int (time .time ())))}#line:253
        OOOOO0000OOO000O0 =OO0000OOOO0O00O00 .sec .post (O00000O0000OOOOO0 ,data =OOO000O000O000OO0 ).json ()#line:254
        debugger (f'finish {OOOOO0000OOO000O0}')#line:255
        OO0000OOOO0O00O00 .sio .write (f'finish  {OOOOO0000OOO000O0}\n')#line:256
        if OOOOO0000OOO000O0 .get ('code')!=0 :#line:257
            printlog (f'{OO0000OOOO0O00O00.name}:{OOOOO0000OOO000O0.get("message")}')#line:258
            OO0000OOOO0O00O00 .sio .write (OOOOO0000OOO000O0 .get ('message')+'\n')#line:259
            return False #line:260
        elif OOOOO0000OOO000O0 ['data']['check']is False :#line:261
            O0O0OO0000O000O00 =OOOOO0000OOO000O0 ['data']['gain']#line:262
            OOO0O0OO0O0OO0000 =OOOOO0000OOO000O0 ['data']['read']#line:263
            OO0000OOOO0O00O00 .sio .write (f"阅读文章成功，获得钢镚[{O0O0OO0000O000O00}]，已读{OOO0O0OO0O0OO0000}\n")#line:264
            printlog (f'{OO0000OOOO0O00O00.name}: 阅读文章成功，获得钢镚[{O0O0OO0000O000O00}]，已读{OOO0O0OO0O0OO0000}')#line:265
            return True #line:266
    def read (OO000O00O000000OO ):#line:268
        while True :#line:269
            OO000O00O000000OO .sio .write ('-'*50 +'\n')#line:270
            OOOOO00O0OO0OO0O0 =f'http://2502567.dx.wcydtd.7tojpq6xbpco0.cloud/read/task'#line:271
            O00O0O000OO0O0OO0 ={"time":str (int (time .time ())),"sign":OO000O00O000000OO .sha_256 (str (int (time .time ())))}#line:275
            OO0O00O00OO0000O0 =OO000O00O000000OO .sec .get (OOOOO00O0OO0OO0O0 ,data =O00O0O000OO0O0OO0 ).json ()#line:276
            debugger (f'read {OO0O00O00OO0000O0}')#line:277
            if OO0O00O00OO0000O0 .get ('code')!=0 :#line:278
                OO000O00O000000OO .sio .write (OO0O00O00OO0000O0 ['message']+'\n')#line:279
                printlog (f'{OO000O00O000000OO.name}:{OO0O00O00OO0000O0["message"]}')#line:280
                return False #line:281
            else :#line:282
                O0O0O0O000OO0O00O =OO0O00O00OO0000O0 .get ('data').get ('link')#line:283
                printlog (f'{OO000O00O000000OO.name}:获取到阅读链接成功')#line:284
                OO000O00O000000OO .sio .write (f'获取到阅读链接成功\n')#line:285
                O0OO00O000OOO00OO =O0O0O0O000OO0O00O .encode ().decode ()#line:286
                O0OO0OO0OO00OOO00 =getmpinfo (O0OO00O000OOO00OO )#line:287
                OOOO0O0OO00OOO0O0 =O0OO0OO0OO00OOO00 ['biz']#line:288
                OO000O00O000000OO .sio .write (f'开始阅读 '+O0OO0OO0OO00OOO00 ['text']+'\n')#line:289
                printlog (f'{OO000O00O000000OO.name}:开始阅读 '+O0OO0OO0OO00OOO00 ['text'])#line:290
                if OOOO0O0OO00OOO0O0 in checklist :#line:291
                    OO000O00O000000OO .sio .write ("正在阅读检测文章，发送通知，暂停60秒\n")#line:292
                    printlog (f'{OO000O00O000000OO.name}:正在阅读检测文章，发送通知，暂停60秒')#line:293
                    if sendable :#line:294
                        send (O0OO0OO0OO00OOO00 ['text'],f'{OO000O00O000000OO.name}钢镚阅读检测',O0OO00O000OOO00OO )#line:295
                    if pushable :#line:296
                        push (f'{OO000O00O000000OO.name}\n点击阅读检测文章\n{O0OO0OO0OO00OOO00["text"]}',f'{OO000O00O000000OO.name} 钢镚过检测',O0OO00O000OOO00OO )#line:298
                    time .sleep (60 )#line:299
                OOOOOOOO0OO00O00O =random .randint (7 ,10 )#line:300
                OO000O00O000000OO .sio .write (f'本次模拟阅读{OOOOOOOO0OO00O00O}秒\n')#line:301
                time .sleep (OOOOOOOO0OO00O00O )#line:302
                OO000O00O000000OO .task_finish ()#line:303
    def withdraw (OOOOOOO000OO00O00 ):#line:305
        if OOOOOOO000OO00O00 .remain <txbz :#line:306
            OOOOOOO000OO00O00 .sio .write (f'没有达到你设置的提现标准{txbz}\n')#line:307
            printlog (f'{OOOOOOO000OO00O00.name}:没有达到你设置的提现标准{txbz}')#line:308
            return False #line:309
        OO0OO0000OOO000O0 =f'http://2502567.dx.wcydtd.7tojpq6xbpco0.cloud/withdraw/wechat'#line:310
        OOO00O0000O00O000 ={"time":str (int (time .time ())),"sign":OOOOOOO000OO00O00 .sha_256 (str (int (time .time ())))}#line:312
        OOOOO0O00O000O0O0 =OOOOOOO000OO00O00 .sec .get (OO0OO0000OOO000O0 ,data =OOO00O0000O00O000 ).json ()#line:313
        OOOOOOO000OO00O00 .sio .write (f"提现结果：{OOOOO0O00O000O0O0.get('message')}\n")#line:314
        printlog (f'{OOOOOOO000OO00O00.name}:提现结果  {OOOOO0O00O000O0O0.get("message")}')#line:315
    def run (OO00OOO0O00OO00O0 ):#line:317
        OO00OOO0O00OO00O0 .sio .write ('='*50 +f'\n账号：{OO00OOO0O00OO00O0.name}开始任务\n')#line:318
        if OO00OOO0O00OO00O0 .read_info ():#line:319
            OO00OOO0O00OO00O0 .read ()#line:320
            OO00OOO0O00OO00O0 .read_info ()#line:321
            OO00OOO0O00OO00O0 .withdraw ()#line:322
            O0OOOO00OO0O0OOO0 =OO00OOO0O00OO00O0 .sio .getvalue ()#line:323
            if not printf :#line:324
                print (O0OOOO00OO0O0OOO0 )#line:325
def yd (OO0OO0OO00O0O0000 ):#line:328
    while not OO0OO0OO00O0O0000 .empty ():#line:329
        O000OOO00OO0OO0OO =OO0OO0OO00O0O0000 .get ()#line:330
        OO00O0O0OOO00O000 =CZGM (O000OOO00OO0OO0OO )#line:331
        OO00O0O0OOO00O000 .run ()#line:332
def get_ver ():#line:335
    OOO0O0OO0OO00000O ='kzcgm V1.3.1'#line:336
    OOO0O00OOOOOOOOOO ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:339
    O000OOOO0OO00O000 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OOO0O00OOOOOOOOOO ).json ()#line:341
    OO0O0OOO0O000O000 =OOO0O0OO0OO00000O .split (' ')[1 ]#line:342
    OO0O0OO0000OO0OO0 =O000OOOO0OO00O000 .get ('version').get (OOO0O0OO0OO00000O .split (' ')[0 ])#line:343
    OOOO0O00OOOOO0O0O =f"当前版本 {OO0O0OOO0O000O000}，仓库版本 {OO0O0OO0000OO0OO0}"#line:344
    if OO0O0OOO0O000O000 <OO0O0OO0000OO0OO0 :#line:345
        OOOO0O00OOOOO0O0O +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:346
    return OOOO0O00OOOOO0O0O #line:347
def main ():#line:350
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:351
    O00000OO0OOO0O00O =os .getenv ('czgmck')#line:352
    if not O00000OO0OOO0O00O :#line:353
        print ('请仔细阅读脚本上方注释，并配置好czgmck')#line:354
        exit ()#line:355
    OO000OO000OO000O0 =[]#line:356
    try :#line:357
        O00000OO0OOO0O00O =ast .literal_eval (O00000OO0OOO0O00O )#line:358
    except :#line:359
        pass #line:360
    OOO0OOOOOOO0OO00O =Queue ()#line:361
    for OO0O0000OOO0O0OOO ,OO0OOO0000OOO0000 in enumerate (O00000OO0OOO0O00O ,start =1 ):#line:362
        print (f'{OO0OOO0000OOO0000}\n以上是第{OO0O0000OOO0O0OOO}个账号的ck，如不正确，请检查ck填写格式')#line:363
        OOO0OOOOOOO0OO00O .put (OO0OOO0000OOO0000 )#line:364
    for OO0O0000OOO0O0OOO in range (max_workers ):#line:365
        O000O0O0OO0O00O00 =threading .Thread (target =yd ,args =(OOO0OOOOOOO0OO00O ,))#line:366
        O000O0O0OO0O00O00 .start ()#line:367
        OO000OO000OO000O0 .append (O000O0O0OO0O00O00 )#line:368
        time .sleep (20 )#line:369
    for O0OOO00O0OOO00000 in OO000OO000OO000O0 :#line:370
        O0OOO00O0OOO00000 .join ()#line:371
if __name__ =='__main__':#line:374
    main ()#line:375
