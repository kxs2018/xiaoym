# -*- coding: utf-8 -*-
# k充值购买阅读
"""
仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
充值购买阅读入口：http://2502807.jl.sgzzlb.sg6gdkelit8js.cloud/?p=2502807
阅读文章抓出gfsessionid

推送检测文章   将多个账号检测文章推送至将多个账号检测文章推送至目标微信目标微信，手动点击链接完成检测阅读

qwbotkey为企业微信webhook机器人后面的 key
参考 https://github.com/kxs2018/yuedu/blob/main/获取企业微信群机器人key.md 获取key，并关注插件！！！
===============================================================
青龙面板，在配置文件里添加
export qwbotkey="qwbotkey"
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

qwbotkey =os .getenv ('qwbotkey')#line:60
if not qwbotkey :#line:61
    print ('请仔细阅读上方注释，并配置好qwbotkey')#line:62
    exit ()#line:63
checklist =['MzkyMzI5NjgxMA==','MzkzMzI5NjQ3MA==','Mzg5NTU4MzEyNQ==','Mzg3NzY5Nzg0NQ==','MzU5OTgxNjg1Mg==','Mzg4OTY5Njg4Mw==','MzI1ODcwNTgzNA==',"Mzg2NDY5NzU0Mw==",]#line:68
def ftime ():#line:71
    OOOO0O0OO000O0OO0 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:72
    return OOOO0O0OO000O0OO0 #line:73
def debugger (O0OOOOOOO0O00OO00 ):#line:76
    if debug :#line:77
        print (O0OOOOOOO0O00OO00 )#line:78
def printlog (O000O00OO000OOOOO ):#line:81
    if printf :#line:82
        print (O000O00OO000OOOOO )#line:83
def send (OOO0OOO0O00OO0OO0 ,title ='通知',url =None ):#line:86
    if not title or not url :#line:87
        OOOO000OOO00OOOO0 ={"msgtype":"text","text":{"content":f"{title}\n\n{OOO0OOO0O00OO0OO0}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:94
    else :#line:95
        OOOO000OOO00OOOO0 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":OOO0OOO0O00OO0OO0 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:100
    O00O00O00OO00OO0O =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:101
    OO0O0OO000O000OOO =requests .post (O00O00O00OO00OO0O ,data =json .dumps (OOOO000OOO00OOOO0 )).json ()#line:102
    if OO0O0OO000O000OOO .get ('errcode')!=0 :#line:103
        print ('消息发送失败，请检查key和发送格式')#line:104
        return False #line:105
    return OO0O0OO000O000OOO #line:106
def getmpinfo (OO0OO0O0OO00OOOOO ):#line:109
    if not OO0OO0O0OO00OOOOO or OO0OO0O0OO00OOOOO =='':#line:110
        return False #line:111
    O00OOO000O000OO00 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:113
    OO00OOOOOO00O0O00 =requests .get (OO0OO0O0OO00OOOOO ,headers =O00OOO000O000OO00 )#line:114
    O00OOO0O00000O00O =etree .HTML (OO00OOOOOO00O0O00 .text )#line:115
    O0O0000O0OO0O0000 =O00OOO0O00000O00O .xpath ('//meta[@*="og:title"]/@content')#line:117
    if O0O0000O0OO0O0000 :#line:118
        O0O0000O0OO0O0000 =O0O0000O0OO0O0000 [0 ]#line:119
    O0000O0000O0O0OOO =O00OOO0O00000O00O .xpath ('//meta[@*="og:url"]/@content')#line:120
    if O0000O0000O0O0OOO :#line:121
        O0000O0000O0O0OOO =O0000O0000O0O0OOO [0 ].encode ().decode ()#line:122
    try :#line:123
        O0O0000O00OO0O0OO =re .findall (r'biz=(.*?)&',OO0OO0O0OO00OOOOO )#line:124
    except :#line:125
        O0O0000O00OO0O0OO =re .findall (r'biz=(.*?)&',O0000O0000O0O0OOO )#line:126
    if O0O0000O00OO0O0OO :#line:127
        O0O0000O00OO0O0OO =O0O0000O00OO0O0OO [0 ]#line:128
    else :#line:129
        return False #line:130
    O0O0O00O0OO0O0000 =O00OOO0O00000O00O .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:131
    if O0O0O00O0OO0O0000 :#line:132
        O0O0O00O0OO0O0000 =O0O0O00O0OO0O0000 [0 ].strip ()#line:133
    O0OO0OO00O00OO000 =re .findall (r"user_name.DATA'\) : '(.*?)'",OO00OOOOOO00O0O00 .text )or O00OOO0O00000O00O .xpath ('//span[@class="profile_meta_value"]/text()')#line:135
    if O0OO0OO00O00OO000 :#line:136
        O0OO0OO00O00OO000 =O0OO0OO00O00OO000 [0 ]#line:137
    O0OO000OO0OO000O0 =re .findall (r'createTime = \'(.*)\'',OO00OOOOOO00O0O00 .text )#line:138
    if O0OO000OO0OO000O0 :#line:139
        O0OO000OO0OO000O0 =O0OO000OO0OO000O0 [0 ][5 :]#line:140
    OO000OOO0000OOO00 =f'{O0OO000OO0OO000O0}|{O0O0000O0OO0O0000}|{O0O0000O00OO0O0OO}|{O0O0O00O0OO0O0000}|{O0OO0OO00O00OO000}'#line:141
    O0OOO0000O0OO000O ={'biz':O0O0000O00OO0O0OO ,'text':OO000OOO0000OOO00 }#line:142
    return O0OOO0000O0OO000O #line:143
class CZGM :#line:146
    def __init__ (OOO0OO00OOOO0OOO0 ,OOOO0OO00O0O0O00O ):#line:147
        OOO0OO00OOOO0OOO0 .name =OOOO0OO00O0O0O00O ['name']#line:148
        OOO0OO00OOOO0OOO0 .headers ={"User-Agent":"Mozilla/5.0 (Linux; Android 9; V1923A Build/PQ3B.190801.06161913; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36 MMWEBID/5635 MicroMessenger/8.0.40.2420(0x28002837) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64","Cookie":OOOO0OO00O0O0O00O ['ck']}#line:152
        OOO0OO00OOOO0OOO0 .sec =requests .session ()#line:153
        OOO0OO00OOOO0OOO0 .sec .headers =OOO0OO00OOOO0OOO0 .headers #line:154
        OOO0OO00OOOO0OOO0 .sio =StringIO ()#line:155
    @staticmethod #line:157
    def sha_256 (O0000O0000OO000O0 ):#line:158
        OOOO0000OO0OOO000 =f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={O0000O0000OO000O0}'#line:159
        OOOOO000OO00OOO00 =hashlib .sha256 ()#line:160
        OOOOO000OO00OOO00 .update (OOOO0000OO0OOO000 .encode ())#line:161
        OOOOO000O0000O0OO =OOOOO000OO00OOO00 .hexdigest ()#line:162
        return OOOOO000O0000O0OO #line:163
    def get_share_link (O00O00O000OOOOOOO ):#line:165
        OOOO0O0O0000000OO ='http://2502567.oz6lsvinhxxa.xcgh.aqk84n5fq0rg.cloud/share'#line:166
        O0O00OOO00O0O0OO0 ={"time":str (int (time .time ())),"sign":O00O00O000OOOOOOO .sha_256 (str (int (time .time ())))}#line:170
        O00O0OOO00OO00OO0 =O00O00O000OOOOOOO .sec .get (OOOO0O0O0000000OO ,data =O0O00OOO00O0O0OO0 ).json ()#line:171
        OOOO0O000000000O0 =O00O0OOO00OO00OO0 ['data']['share_link'][0 ]#line:172
        return OOOO0O000000000O0 #line:173
    def read_info (O0000OOOOO00O00O0 ):#line:175
        try :#line:176
            OOO00OO00OOOO0000 =f'http://2502567.oz6lsvinhxxa.xcgh.aqk84n5fq0rg.cloud/read/info'#line:177
            O00OOO0OOOOO00000 ={"time":str (int (time .time ())),"sign":O0000OOOOO00O00O0 .sha_256 (str (int (time .time ())))}#line:181
            O0O0O0OO0O000000O =O0000OOOOO00O00O0 .sec .get (OOO00OO00OOOO0000 ,data =O00OOO0OOOOO00000 )#line:182
            debugger (f'readfinfo {O0O0O0OO0O000000O.text}')#line:183
            try :#line:184
                OOO0O0O0O0000OO00 =O0O0O0OO0O000000O .json ()#line:185
                O0000OOOOO00O00O0 .remain =OOO0O0O0O0000OO00 .get ("data").get ("remain")#line:186
                O0OOO000OO00OO0OO =f'今日已经阅读了{OOO0O0O0O0000OO00.get("data").get("read")}篇文章，今日总金币{OOO0O0O0O0000OO00.get("data").get("gold")}，剩余{O0000OOOOO00O00O0.remain}\n邀请链接：{O0000OOOOO00O00O0.get_share_link()}'#line:187
                printlog (f'{O0000OOOOO00O00O0.name}:{O0OOO000OO00OO0OO}')#line:188
                O0000OOOOO00O00O0 .sio .write (O0OOO000OO00OO0OO +'\n')#line:189
                return True #line:190
            except :#line:191
                printlog (f'{O0000OOOOO00O00O0.name}:{O0O0O0OO0O000000O.text}')#line:192
                O0000OOOOO00O00O0 .sio .write (O0O0O0OO0O000000O .text +'\n')#line:193
                return False #line:194
        except :#line:195
            printlog (f'{O0000OOOOO00O00O0.name}:获取用户信息失败，账号异常，请检查你的ck')#line:196
            O0000OOOOO00O00O0 .sio .write ('获取用户信息失败，账号异常，请检查你的ck\n')#line:197
            send ('{self.name}:获取用户信息失败，账号异常，请检查你的ck','钢镚阅读ck失效通知')#line:198
            return False #line:199
    def task_finish (OOOOOO0OO0000OOOO ):#line:201
        OO0OO00O00O00OOOO ="http://2502567.oz6lsvinhxxa.xcgh.aqk84n5fq0rg.cloud/read/finish"#line:202
        OOO0O0O000OOOO0O0 ={"time":str (int (time .time ())),"sign":OOOOOO0OO0000OOOO .sha_256 (str (int (time .time ())))}#line:206
        O000O00O0OO0O0000 =OOOOOO0OO0000OOOO .sec .post (OO0OO00O00O00OOOO ,data =OOO0O0O000OOOO0O0 ).json ()#line:207
        debugger (f'finish {O000O00O0OO0O0000}')#line:208
        OOOOOO0OO0000OOOO .sio .write (f'finish  {O000O00O0OO0O0000}\n')#line:209
        if O000O00O0OO0O0000 .get ('code')!=0 :#line:210
            printlog (f'{OOOOOO0OO0000OOOO.name}:{O000O00O0OO0O0000.get("message")}')#line:211
            OOOOOO0OO0000OOOO .sio .write (O000O00O0OO0O0000 .get ('message')+'\n')#line:212
            return False #line:213
        elif O000O00O0OO0O0000 ['data']['check']is False :#line:214
            O0000000O00000OOO =O000O00O0OO0O0000 ['data']['gain']#line:215
            OOO0OO000OOO00OO0 =O000O00O0OO0O0000 ['data']['read']#line:216
            OOOOOO0OO0000OOOO .sio .write (f"阅读文章成功，获得钢镚[{O0000000O00000OOO}]，已读{OOO0OO000OOO00OO0}\n")#line:217
            printlog (f'{OOOOOO0OO0000OOOO.name}: 阅读文章成功，获得钢镚[{O0000000O00000OOO}]，已读{OOO0OO000OOO00OO0}')#line:218
            return True #line:219
    def read (O0OO0O0OOOOO00000 ):#line:221
        OOOO0O0O0OOO0OO00 =0 #line:222
        while True :#line:223
            O0OO0O0OOOOO00000 .sio .write ('-'*50 +'\n')#line:224
            O0000000O00000O0O =f'http://2502567.oz6lsvinhxxa.xcgh.aqk84n5fq0rg.cloud/read/task'#line:225
            OOO0O0O0O00000OOO ={"time":str (int (time .time ())),"sign":O0OO0O0OOOOO00000 .sha_256 (str (int (time .time ())))}#line:229
            OO0OOOO000OO0O0O0 =O0OO0O0OOOOO00000 .sec .get (O0000000O00000O0O ,data =OOO0O0O0O00000OOO ).json ()#line:230
            debugger (f'read {OO0OOOO000OO0O0O0}')#line:231
            if OO0OOOO000OO0O0O0 .get ('code')!=0 :#line:232
                O0OO0O0OOOOO00000 .sio .write (OO0OOOO000OO0O0O0 ['message']+'\n')#line:233
                printlog (f'{O0OO0O0OOOOO00000.name}:{OO0OOOO000OO0O0O0["message"]}')#line:234
                return False #line:235
            else :#line:236
                O0OO00000OOO0000O =OO0OOOO000OO0O0O0 .get ('data').get ('link')#line:237
                printlog (f'{O0OO0O0OOOOO00000.name}:获取到阅读链接成功')#line:238
                O0OO0O0OOOOO00000 .sio .write (f'获取到阅读链接成功\n')#line:239
                OOOO0OOOO00OO00OO =O0OO00000OOO0000O .encode ().decode ()#line:240
                OOO00O00O0OOOOO0O =getmpinfo (OOOO0OOOO00OO00OO )#line:241
                if not OOO00O00O0OOOOO0O :#line:242
                    OOOO0O0O0OOO0OO00 +=1 #line:243
                    if OOOO0O0O0OOO0OO00 ==2 :#line:244
                        printlog (f'{O0OO0O0OOOOO00000.name}:获取文章信息失败已达3次，程序中止')#line:245
                        break #line:246
                    time .sleep (5 )#line:247
                    continue #line:248
                OO0OO00OO000OO0OO =OOO00O00O0OOOOO0O ['biz']#line:249
                O0OO0O0OOOOO00000 .sio .write (f'开始阅读 '+OOO00O00O0OOOOO0O ['text']+'\n')#line:250
                printlog (f'{O0OO0O0OOOOO00000.name}:开始阅读 '+OOO00O00O0OOOOO0O ['text'])#line:251
                if OO0OO00OO000OO0OO in checklist :#line:252
                    O0OO0O0OOOOO00000 .sio .write ("正在阅读检测文章，发送通知，暂停50秒\n")#line:253
                    printlog (f'{O0OO0O0OOOOO00000.name}:正在阅读检测文章，发送通知，暂停50秒')#line:254
                    send (OOO00O00O0OOOOO0O ['text'],f'{O0OO0O0OOOOO00000.name}钢镚阅读检测',OOOO0OOOO00OO00OO )#line:255
                    time .sleep (50 )#line:256
                OO00000O0OOOOOOO0 =random .randint (7 ,10 )#line:257
                O0OO0O0OOOOO00000 .sio .write (f'本次模拟阅读{OO00000O0OOOOOOO0}秒\n')#line:258
                time .sleep (OO00000O0OOOOOOO0 )#line:259
                O0OO0O0OOOOO00000 .task_finish ()#line:260
    def withdraw (OOO0O0000OO0000OO ):#line:262
        if OOO0O0000OO0000OO .remain <txbz :#line:263
            OOO0O0000OO0000OO .sio .write (f'没有达到你设置的提现标准{txbz}\n')#line:264
            printlog (f'{OOO0O0000OO0000OO.name}:没有达到你设置的提现标准{txbz}')#line:265
            return False #line:266
        O0OO00O00O000O000 =f'http://2502567.oz6lsvinhxxa.xcgh.aqk84n5fq0rg.cloud/withdraw/wechat'#line:267
        O0000000O0O0O00OO ={"time":str (int (time .time ())),"sign":OOO0O0000OO0000OO .sha_256 (str (int (time .time ())))}#line:269
        OO000O00OOO0O0OO0 =OOO0O0000OO0000OO .sec .get (O0OO00O00O000O000 ,data =O0000000O0O0O00OO ).json ()#line:270
        OOO0O0000OO0000OO .sio .write (f"提现结果：{OO000O00OOO0O0OO0.get('message')}\n")#line:271
        printlog (f'{OOO0O0000OO0000OO.name}:提现结果  {OO000O00OOO0O0OO0.get("message")}')#line:272
    def run (OO0O0OO0OO00000O0 ):#line:274
        OO0O0OO0OO00000O0 .sio .write ('='*50 +f'\n账号：{OO0O0OO0OO00000O0.name}开始任务\n')#line:275
        if OO0O0OO0OO00000O0 .read_info ():#line:276
            OO0O0OO0OO00000O0 .read ()#line:277
            OO0O0OO0OO00000O0 .read_info ()#line:278
            OO0O0OO0OO00000O0 .withdraw ()#line:279
            O000O0OO0OOOO0O0O =OO0O0OO0OO00000O0 .sio .getvalue ()#line:280
            if not printf :#line:281
                print (O000O0OO0OOOO0O0O )#line:282
def yd (OO0OO0OO0OO0O00OO ):#line:285
    while not OO0OO0OO0OO0O00OO .empty ():#line:286
        O00O0OOOOO0OO0OO0 =OO0OO0OO0OO0O00OO .get ()#line:287
        O00000000OOOO0O0O =CZGM (O00O0OOOOO0OO0OO0 )#line:288
        O00000000OOOO0O0O .run ()#line:289
def get_ver ():#line:292
    O00OOOOO000OOOO0O ='kzcgm V1.2'#line:293
    OOOOOOOOO0OO00000 ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:296
    O0O00000OOO000000 =requests .get ('https://ghproxy.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json',headers =OOOOOOOOO0OO00000 ).json ()#line:298
    OOO0O0000OO0OOO00 =O00OOOOO000OOOO0O .split (' ')[1 ]#line:299
    O0O0O0O000000OO00 =O0O00000OOO000000 .get ('version').get (O00OOOOO000OOOO0O .split (' ')[0 ])#line:300
    OO0O00O00000OOOOO =f"当前版本 {OOO0O0000OO0OOO00}，仓库版本 {O0O0O0O000000OO00}"#line:301
    if OOO0O0000OO0OOO00 <O0O0O0O000000OO00 :#line:302
        OO0O00O00000OOOOO +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:303
    return OO0O00O00000OOOOO #line:304
def main ():#line:307
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:308
    OO0000O0OO0O0OO0O =os .getenv ('czgmck')#line:309
    if not OO0000O0OO0O0OO0O :#line:310
        print ('请仔细阅读脚本上方注释，并配置好czgmck')#line:311
        exit ()#line:312
    OOO0000OO00OO00OO =[]#line:313
    try :#line:314
        OO0000O0OO0O0OO0O =ast .literal_eval (OO0000O0OO0O0OO0O )#line:315
    except :#line:316
        pass #line:317
    O00OO000OOOO0O0O0 =Queue ()#line:318
    for OO0O000O000O0O0OO ,O0O0000O0OO00O000 in enumerate (OO0000O0OO0O0OO0O ,start =1 ):#line:319
        print (f'{O0O0000O0OO00O000}\n以上是第{OO0O000O000O0O0OO}个账号的ck，如不正确，请检查ck填写格式')#line:320
        O00OO000OOOO0O0O0 .put (O0O0000O0OO00O000 )#line:321
    for OO0O000O000O0O0OO in range (max_workers ):#line:322
        O0O0000O000000OOO =threading .Thread (target =yd ,args =(O00OO000OOOO0O0O0 ,))#line:323
        O0O0000O000000OOO .start ()#line:324
        OOO0000OO00OO00OO .append (O0O0000O000000OOO )#line:325
        time .sleep (20 )#line:326
    for OO0O0000O000O0OO0 in OOO0000OO00OO00OO :#line:327
        OO0O0000O000O0OO0 .join ()#line:328
if __name__ =='__main__':#line:331
    main ()#line:332
