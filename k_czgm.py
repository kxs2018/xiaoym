# -*- coding: utf-8 -*-
# k充值购买阅读
"""
new Env('钢镚');
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
    O0OOO000O000O000O =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:99
    return O0OOO000O000O000O #line:100
def debugger (OO000OO0O0000OOO0 ):#line:103
    if debug :#line:104
        print (OO000OO0O0000OOO0 )#line:105
def printlog (OOOO0OO0O0OO0000O ):#line:108
    if printf :#line:109
        print (OOOO0OO0O0OO0000O )#line:110
def push (OO0O00OO00OOO0OOO ,O0OO00OOOOOO0OOOO ,OOOOOOOO0OO0OOOOO ,uid =None ):#line:113
    if uid :#line:114
        uids .append (uid )#line:115
    OOO00OO0O0O0OOO0O ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',OO0O00OO00OOO0OOO ).replace ('url',OOOOOOOO0OO0OOOOO )#line:117
    OO00OOOO000OOO000 ={"appToken":appToken ,"content":OOO00OO0O0O0OOO0O ,"summary":O0OO00OOOOOO0OOOO ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":OOOOOOOO0OO0OOOOO ,"verifyPay":False }#line:127
    OO0O0OOO0O00OO00O ='http://wxpusher.zjiecode.com/api/send/message'#line:128
    OO00OO0O000OO00O0 =requests .post (url =OO0O0OOO0O00OO00O ,json =OO00OOOO000OOO000 ).json ()#line:129
    if OO00OO0O000OO00O0 .get ('code')!=1000 :#line:130
        print (OO00OO0O000OO00O0 .get ('msg'),OO00OO0O000OO00O0 )#line:131
    return OO00OO0O000OO00O0 #line:132
def send (O00O0O000OOO00O00 ,title ='通知',url =None ):#line:135
    if not title or not url :#line:136
        OO0OO0OOO0O00O0O0 ={"msgtype":"text","text":{"content":f"{title}\n\n{O00O0O000OOO00O00}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:143
    else :#line:144
        OO0OO0OOO0O00O0O0 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O00O0O000OOO00O00 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:149
    OOO0OOO00O00O0O0O =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:150
    OO0O0000OOOO00OO0 =requests .post (OOO0OOO00O00O0O0O ,data =json .dumps (OO0OO0OOO0O00O0O0 )).json ()#line:151
    if OO0O0000OOOO00OO0 .get ('errcode')!=0 :#line:152
        print ('消息发送失败，请检查key和发送格式')#line:153
        return False #line:154
    return OO0O0000OOOO00OO0 #line:155
def getmpinfo (OO00OOOO0O0000OO0 ):#line:158
    if not OO00OOOO0O0000OO0 or OO00OOOO0O0000OO0 =='':#line:159
        return False #line:160
    O00OO00OOO0O000O0 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:162
    OOOO000000OOO0000 =requests .get (OO00OOOO0O0000OO0 ,headers =O00OO00OOO0O000O0 )#line:163
    OO0OOOO0000OO00O0 =etree .HTML (OOOO000000OOO0000 .text )#line:164
    O00000OOOO0O0O0OO =OO0OOOO0000OO00O0 .xpath ('//meta[@*="og:title"]/@content')#line:166
    if O00000OOOO0O0O0OO :#line:167
        O00000OOOO0O0O0OO =O00000OOOO0O0O0OO [0 ]#line:168
    O0O00O00O0OO0OOOO =OO0OOOO0000OO00O0 .xpath ('//meta[@*="og:url"]/@content')#line:169
    if O0O00O00O0OO0OOOO :#line:170
        O0O00O00O0OO0OOOO =O0O00O00O0OO0OOOO [0 ].encode ().decode ()#line:171
    try :#line:172
        O0OOO0O00OOOOOOOO =re .findall (r'biz=(.*?)&',OO00OOOO0O0000OO0 )[0 ]#line:173
    except :#line:174
        O0OOO0O00OOOOOOOO =re .findall (r'biz=(.*?)&',O0O00O00O0OO0OOOO )[0 ]#line:175
    if not O0OOO0O00OOOOOOOO :#line:176
        return False #line:177
    OOOO0000000OOO0O0 =OO0OOOO0000OO00O0 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:178
    if OOOO0000000OOO0O0 :#line:179
        OOOO0000000OOO0O0 =OOOO0000000OOO0O0 [0 ].strip ()#line:180
    O000O0O0O00O00O00 =re .findall (r"user_name.DATA'\) : '(.*?)'",OOOO000000OOO0000 .text )or OO0OOOO0000OO00O0 .xpath ('//span[@class="profile_meta_value"]/text()')#line:182
    if O000O0O0O00O00O00 :#line:183
        O000O0O0O00O00O00 =O000O0O0O00O00O00 [0 ]#line:184
    O00OO0OO0O00O00OO =re .findall (r'createTime = \'(.*)\'',OOOO000000OOO0000 .text )#line:185
    if O00OO0OO0O00O00OO :#line:186
        O00OO0OO0O00O00OO =O00OO0OO0O00O00OO [0 ][5 :]#line:187
    O0O0OO00OOO0OOOOO =f'{O00OO0OO0O00O00OO}|{O00000OOOO0O0O0OO}|{O0OOO0O00OOOOOOOO}|{OOOO0000000OOO0O0}|{O000O0O0O00O00O00}'#line:188
    O0O0OOO0000OOO0O0 ={'biz':O0OOO0O00OOOOOOOO ,'text':O0O0OO00OOO0OOOOO }#line:189
    return O0O0OOO0000OOO0O0 #line:190
class CZGM :#line:193
    def __init__ (O00OOOO0OOO0O0OOO ,OOO0OO0OO0O000OO0 ):#line:194
        O00OOOO0OOO0O0OOO .name =OOO0OO0OO0O000OO0 ['name']#line:195
        O00OOOO0OOO0O0OOO .headers ={"User-Agent":"Mozilla/5.0 (Linux; Android 9; V1923A Build/PQ3B.190801.06161913; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36 MMWEBID/5635 MicroMessenger/8.0.40.2420(0x28002837) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64","Cookie":OOO0OO0OO0O000OO0 ['ck']}#line:199
        O00OOOO0OOO0O0OOO .sec =requests .session ()#line:200
        O00OOOO0OOO0O0OOO .sec .headers =O00OOOO0OOO0O0OOO .headers #line:201
        O00OOOO0OOO0O0OOO .sio =StringIO ()#line:202
    @staticmethod #line:204
    def sha_256 (OO0O00O000O0O000O ):#line:205
        OO0OO0OOOO000O00O =f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={OO0O00O000O0O000O}'#line:206
        OO0O0O00OO00OO00O =hashlib .sha256 ()#line:207
        OO0O0O00OO00OO00O .update (OO0OO0OOOO000O00O .encode ())#line:208
        O0O00OO0O00O00000 =OO0O0O00OO00OO00O .hexdigest ()#line:209
        return O0O00OO0O00O00000 #line:210
    def get_share_link (OOO0OO000O0O00O0O ):#line:212
        O00O0O0OO0O0O000O ='http://2502567.dx.wcydtd.7tojpq6xbpco0.cloud/share'#line:213
        OO00OO0O000OOO0O0 ={"time":str (int (time .time ())),"sign":OOO0OO000O0O00O0O .sha_256 (str (int (time .time ())))}#line:217
        OOOO0O00OOOOOOOO0 =OOO0OO000O0O00O0O .sec .get (O00O0O0OO0O0O000O ,data =OO00OO0O000OOO0O0 ).json ()#line:218
        O0OO0OO0O0O000O00 =OOOO0O00OOOOOOOO0 ['data']['share_link'][0 ]#line:219
        return O0OO0OO0O0O000O00 #line:220
    def read_info (O0O00O00OOOO0OOO0 ):#line:222
        try :#line:223
            OOOO00O00000O0O0O =f'http://2502567.dx.wcydtd.7tojpq6xbpco0.cloud/read/info'#line:224
            OO00O0O0OO00OOO00 ={"time":str (int (time .time ())),"sign":O0O00O00OOOO0OOO0 .sha_256 (str (int (time .time ())))}#line:228
            O0OO0O0O0O00OOO00 =O0O00O00OOOO0OOO0 .sec .get (OOOO00O00000O0O0O ,data =OO00O0O0OO00OOO00 )#line:229
            debugger (f'readfinfo {O0OO0O0O0O00OOO00.text}')#line:230
            try :#line:231
                O0O0OO0O000O0OO00 =O0OO0O0O0O00OOO00 .json ()#line:232
                O0O00O00OOOO0OOO0 .remain =O0O0OO0O000O0OO00 .get ("data").get ("remain")#line:233
                O000OO000000OOO00 =f'今日已经阅读了{O0O0OO0O000O0OO00.get("data").get("read")}篇文章，今日总金币{O0O0OO0O000O0OO00.get("data").get("gold")}，剩余{O0O00O00OOOO0OOO0.remain}\n邀请链接：{O0O00O00OOOO0OOO0.get_share_link()}'#line:234
                printlog (f'{O0O00O00OOOO0OOO0.name}:{O000OO000000OOO00}')#line:235
                O0O00O00OOOO0OOO0 .sio .write (O000OO000000OOO00 +'\n')#line:236
                return True #line:237
            except :#line:238
                printlog (f'{O0O00O00OOOO0OOO0.name}:{O0OO0O0O0O00OOO00.text}')#line:239
                O0O00O00OOOO0OOO0 .sio .write (O0OO0O0O0O00OOO00 .text +'\n')#line:240
                return False #line:241
        except :#line:242
            printlog (f'{O0O00O00OOOO0OOO0.name}:获取用户信息失败，账号异常，请检查你的ck')#line:243
            O0O00O00OOOO0OOO0 .sio .write ('获取用户信息失败，账号异常，请检查你的ck\n')#line:244
            send ('{self.name}:获取用户信息失败，账号异常，请检查你的ck','钢镚阅读ck失效通知')#line:245
            return False #line:246
    def task_finish (O00OO00OO0O0OO000 ):#line:248
        O0O00O0OO0O00O0OO ="http://2502567.dx.wcydtd.7tojpq6xbpco0.cloud/read/finish"#line:249
        OOOO00O0OO000OO00 ={"time":str (int (time .time ())),"sign":O00OO00OO0O0OO000 .sha_256 (str (int (time .time ())))}#line:253
        OO00O0OO0OO000000 =O00OO00OO0O0OO000 .sec .post (O0O00O0OO0O00O0OO ,data =OOOO00O0OO000OO00 ).json ()#line:254
        debugger (f'finish {OO00O0OO0OO000000}')#line:255
        O00OO00OO0O0OO000 .sio .write (f'finish  {OO00O0OO0OO000000}\n')#line:256
        if OO00O0OO0OO000000 .get ('code')!=0 :#line:257
            printlog (f'{O00OO00OO0O0OO000.name}:{OO00O0OO0OO000000.get("message")}')#line:258
            O00OO00OO0O0OO000 .sio .write (OO00O0OO0OO000000 .get ('message')+'\n')#line:259
            return False #line:260
        elif OO00O0OO0OO000000 ['data']['check']is False :#line:261
            OO00O0OOOOO00O00O =OO00O0OO0OO000000 ['data']['gain']#line:262
            OOO0OOO0O0O0OOOO0 =OO00O0OO0OO000000 ['data']['read']#line:263
            O00OO00OO0O0OO000 .sio .write (f"阅读文章成功，获得钢镚[{OO00O0OOOOO00O00O}]，已读{OOO0OOO0O0O0OOOO0}\n")#line:264
            printlog (f'{O00OO00OO0O0OO000.name}: 阅读文章成功，获得钢镚[{OO00O0OOOOO00O00O}]，已读{OOO0OOO0O0O0OOOO0}')#line:265
            return True #line:266
    def read (OOO0O0000OO00OO00 ):#line:268
        while True :#line:269
            OOO0O0000OO00OO00 .sio .write ('-'*50 +'\n')#line:270
            O00O00O00OO000OOO =f'http://2502567.dx.wcydtd.7tojpq6xbpco0.cloud/read/task'#line:271
            OO0O0OOOO0OOO000O ={"time":str (int (time .time ())),"sign":OOO0O0000OO00OO00 .sha_256 (str (int (time .time ())))}#line:275
            OOO0O00OO00O000O0 =OOO0O0000OO00OO00 .sec .get (O00O00O00OO000OOO ,data =OO0O0OOOO0OOO000O ).json ()#line:276
            debugger (f'read {OOO0O00OO00O000O0}')#line:277
            if OOO0O00OO00O000O0 .get ('code')!=0 :#line:278
                OOO0O0000OO00OO00 .sio .write (OOO0O00OO00O000O0 ['message']+'\n')#line:279
                printlog (f'{OOO0O0000OO00OO00.name}:{OOO0O00OO00O000O0["message"]}')#line:280
                return False #line:281
            else :#line:282
                OO00OOOOO0000O0O0 =OOO0O00OO00O000O0 .get ('data').get ('link')#line:283
                printlog (f'{OOO0O0000OO00OO00.name}:获取到阅读链接成功')#line:284
                OOO0O0000OO00OO00 .sio .write (f'获取到阅读链接成功\n')#line:285
                O0O000OOOOOOO0000 =OO00OOOOO0000O0O0 .encode ().decode ()#line:286
                O00O00OO00OO0OO00 =getmpinfo (O0O000OOOOOOO0000 )#line:287
                O000000OOO0OOOOO0 =O00O00OO00OO0OO00 ['biz']#line:288
                OOO0O0000OO00OO00 .sio .write (f'开始阅读 '+O00O00OO00OO0OO00 ['text']+'\n')#line:289
                printlog (f'{OOO0O0000OO00OO00.name}:开始阅读 '+O00O00OO00OO0OO00 ['text'])#line:290
                if O000000OOO0OOOOO0 in checklist :#line:291
                    OOO0O0000OO00OO00 .sio .write ("正在阅读检测文章，发送通知，暂停60秒\n")#line:292
                    printlog (f'{OOO0O0000OO00OO00.name}:正在阅读检测文章，发送通知，暂停60秒')#line:293
                    if sendable :#line:294
                        send (O00O00OO00OO0OO00 ['text'],f'{OOO0O0000OO00OO00.name}钢镚阅读检测',O0O000OOOOOOO0000 )#line:295
                    if pushable :#line:296
                        push (f'{OOO0O0000OO00OO00.name}\n点击阅读检测文章\n{O00O00OO00OO0OO00["text"]}',f'{OOO0O0000OO00OO00.name} 钢镚过检测',O0O000OOOOOOO0000 )#line:298
                    time .sleep (60 )#line:299
                O0OO0O00O0000OOO0 =random .randint (7 ,10 )#line:300
                OOO0O0000OO00OO00 .sio .write (f'本次模拟阅读{O0OO0O00O0000OOO0}秒\n')#line:301
                time .sleep (O0OO0O00O0000OOO0 )#line:302
                OOO0O0000OO00OO00 .task_finish ()#line:303
    def withdraw (OO00OO0OOO0OOO00O ):#line:305
        if OO00OO0OOO0OOO00O .remain <txbz :#line:306
            OO00OO0OOO0OOO00O .sio .write (f'没有达到你设置的提现标准{txbz}\n')#line:307
            printlog (f'{OO00OO0OOO0OOO00O.name}:没有达到你设置的提现标准{txbz}')#line:308
            return False #line:309
        OO0O0OOOOO0O0OO0O =f'http://2502567.dx.wcydtd.7tojpq6xbpco0.cloud/withdraw/wechat'#line:310
        OOOOO0OOO0O0O0000 ={"time":str (int (time .time ())),"sign":OO00OO0OOO0OOO00O .sha_256 (str (int (time .time ())))}#line:312
        OO00OOOOOO00O0OO0 =OO00OO0OOO0OOO00O .sec .get (OO0O0OOOOO0O0OO0O ,data =OOOOO0OOO0O0O0000 ).json ()#line:313
        OO00OO0OOO0OOO00O .sio .write (f"提现结果：{OO00OOOOOO00O0OO0.get('message')}\n")#line:314
        printlog (f'{OO00OO0OOO0OOO00O.name}:提现结果  {OO00OOOOOO00O0OO0.get("message")}')#line:315
    def run (O0OOOOOO0O00O000O ):#line:317
        O0OOOOOO0O00O000O .sio .write ('='*50 +f'\n账号：{O0OOOOOO0O00O000O.name}开始任务\n')#line:318
        if O0OOOOOO0O00O000O .read_info ():#line:319
            O0OOOOOO0O00O000O .read ()#line:320
            O0OOOOOO0O00O000O .read_info ()#line:321
            O0OOOOOO0O00O000O .withdraw ()#line:322
            OOO0OO0O00OO00000 =O0OOOOOO0O00O000O .sio .getvalue ()#line:323
            if not printf :#line:324
                print (OOO0OO0O00OO00000 )#line:325
def yd (O0OOO0O0OOOOOOOO0 ):#line:328
    while not O0OOO0O0OOOOOOOO0 .empty ():#line:329
        OO0OOO0O00O0O0O00 =O0OOO0O0OOOOOOOO0 .get ()#line:330
        O0OOOO0OOO00OOO00 =CZGM (OO0OOO0O00O0O0O00 )#line:331
        O0OOOO0OOO00OOO00 .run ()#line:332
def get_ver ():#line:335
    O00O00O0O0000OOOO ='kzcgm V1.3.2'#line:336
    O0O000OOOOOO0O000 ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:339
    O00000O0000O0O00O =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O0O000OOOOOO0O000 ).json ()#line:341
    O000O0O0OO0O0000O =O00O00O0O0000OOOO .split (' ')[1 ]#line:342
    O0O0OOO000O0OOO0O =O00000O0000O0O00O .get ('version').get (O00O00O0O0000OOOO .split (' ')[0 ])#line:343
    O0OOOO00O0OOOO0OO =f"当前版本 {O000O0O0OO0O0000O}，仓库版本 {O0O0OOO000O0OOO0O}"#line:344
    if O000O0O0OO0O0000O <O0O0OOO000O0OOO0O :#line:345
        O0OOOO00O0OOOO0OO +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:346
    return O0OOOO00O0OOOO0OO #line:347
def main ():#line:350
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:351
    OOOOO0O0OOO0000OO =os .getenv ('czgmck')#line:352
    if not OOOOO0O0OOO0000OO :#line:353
        print ('请仔细阅读脚本上方注释，并配置好czgmck')#line:354
        exit ()#line:355
    O000OO0OO0OO0OOOO =[]#line:356
    try :#line:357
        OOOOO0O0OOO0000OO =ast .literal_eval (OOOOO0O0OOO0000OO )#line:358
    except :#line:359
        pass #line:360
    OO0OOO00OO0000OO0 =Queue ()#line:361
    for O000O0OOO0O0O0O0O ,OO0O0O00OO0000O0O in enumerate (OOOOO0O0OOO0000OO ,start =1 ):#line:362
        print (f'{OO0O0O00OO0000O0O}\n以上是第{O000O0OOO0O0O0O0O}个账号的ck，如不正确，请检查ck填写格式')#line:363
        OO0OOO00OO0000OO0 .put (OO0O0O00OO0000O0O )#line:364
    for O000O0OOO0O0O0O0O in range (max_workers ):#line:365
        OO00O00000O0O0O0O =threading .Thread (target =yd ,args =(OO0OOO00OO0000OO0 ,))#line:366
        OO00O00000O0O0O0O .start ()#line:367
        O000OO0OO0OO0OOOO .append (OO00O00000O0O0O0O )#line:368
        time .sleep (20 )#line:369
    for OOOO0OO0OO0OO000O in O000OO0OO0OO0OOOO :#line:370
        OOOO0OO0OO0OO000O .join ()#line:371
if __name__ =='__main__':#line:374
    main ()#line:375