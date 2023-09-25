# -*- coding: utf-8 -*-
# k小阅阅阅读多线程V2.0
# Author: kk
# date：2023/9/24
"""
仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
小阅阅阅读入口：https://wi83860.aiskill.top:10251/yunonline/v1/auth/0489574c00307cdb933067188854e498?codeurl=wi83860.aiskill.top:10251&codeuserid=2&time=1695092177
阅读文章抓出ysm_uid 建议手动阅读5篇左右再使用脚本，不然100%黑！！！
推送检测文章   将多个账号检测文章推送至将多个账号检测文章推送至目标微信目标微信，手动点击链接完成检测阅读
key为企业微信webhook机器人后面的 key
===============================================================
青龙面板，在配置文件里添加
export qwbotkey="key"
export xyyck="[{'name':'xxx','ysmuid':'xxx'},{'name':'xxx','ysmuid':'xxx'}]"
===============================================================
no module named lxml 解决方案
1. 配置文件搜索 PipMirror，如果网址包含douban的，请改为下方的网址
PipMirror="https://pypi.tuna.tsinghua.edu.cn/simple"
2. 依赖管理-python 添加 lxml
3. 如果装不上，①请ssh连接到服务器 ②docker exec -it ql bash (ql是青龙容器的名字，docker ps可查询) ③pip install pip -U
===============================================================
"""
import datetime #line:23
import threading #line:24
import ast #line:25
import json #line:26
import os #line:27
import random #line:28
import re #line:29
from queue import Queue #line:30
import requests #line:31
try :#line:33
    from lxml import etree #line:34
except :#line:35
    print ('请仔细阅读脚本上方注释中的“no module named lxml 解决方案”')#line:36
    exit ()#line:37
import time #line:38
from urllib .parse import urlparse ,parse_qs #line:39

"""实时日志开关"""#line:41
printf =1 #line:42
"""1为开，0为关"""#line:43

"""debug模式开关"""#line:45
debug =0 #line:46
"""1为开，打印调试日志；0为关，不打印"""#line:47

"""线程数量设置"""#line:49
max_workers =5 #line:50
"""设置为5，即最多有5个任务同时进行"""#line:51

"""设置提现标准"""#line:53
txbz =8000 #line:54
"""设置为8000，即为8毛起提"""#line:55

qwbotkey =os .getenv ('qwbotkey')#line:57
xyyck =os .getenv ('xyyck')#line:58
if not qwbotkey or not xyyck :#line:59
    print ('请仔细阅读上方注释并设置好key和ck')#line:60
    exit ()#line:61
checklist =['MzkxNTE3MzQ4MQ==','Mzg5MjM0MDEwNw==','MzUzODY4NzE2OQ==','MzkyMjE3MzYxMg==','MzkxNjMwNDIzOA==','Mzg3NzUxMjc5Mg==','Mzg4NTcwODE1NA==','Mzk0ODIxODE4OQ==','Mzg2NjUyMjI1NA==','MzIzMDczODg4Mw==','Mzg5ODUyMzYzMQ==','MzU0NzI5Mjc4OQ==','Mzg5MDgxODAzMg==']#line:66
def ftime ():#line:69
    O0OOO0OOOOOOOOOO0 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:70
    return O0OOO0OOOOOOOOOO0 #line:71
def debugger (text ):#line:74
    if debug :#line:75
        print (text )#line:76
def printlog (text ):#line:79
    if printf :#line:80
        print (text )#line:81
def send (msg ,title ='通知',url =None ):#line:84
    if not url :#line:85
        OO0O0OOOO0OOOOO00 ={"msgtype":"text","text":{"content":f"{title}\n\n{msg}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:92
    else :#line:93
        OO0O0OOOO0OOOOO00 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":msg ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:98
    OOOO0OO00000OOO0O =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:99
    OOO0OOO0OO000O0OO =requests .post (OOOO0OO00000OOO0O ,data =json .dumps (OO0O0OOOO0OOOOO00 )).json ()#line:100
    if OOO0OOO0OO000O0OO .get ('errcode')!=0 :#line:101
        print ('消息发送失败，请检查key和发送格式')#line:102
        return False #line:103
    return OOO0OOO0OO000O0OO #line:104
def getmpinfo (link ):#line:107
    if not link or link =='':#line:108
        return False #line:109
    OO00000O000000OOO ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:111
    OO00O0O0O000OOOO0 =requests .get (link ,headers =OO00000O000000OOO )#line:112
    OOO000OO000OO00OO =etree .HTML (OO00O0O0O000OOOO0 .text )#line:113
    OOOO0OO00O00OO000 =OOO000OO000OO00OO .xpath ('//meta[@*="og:title"]/@content')#line:115
    if OOOO0OO00O00OO000 :#line:116
        OOOO0OO00O00OO000 =OOOO0OO00O00OO000 [0 ]#line:117
    OOOO0O00O0OO0000O =OOO000OO000OO00OO .xpath ('//meta[@*="og:url"]/@content')#line:118
    if OOOO0O00O0OO0000O :#line:119
        OOOO0O00O0OO0000O =OOOO0O00O0OO0000O [0 ].encode ().decode ()#line:120
    try :#line:121
        O0O00O0OOOOO000O0 =re .findall (r'biz=(.*?)&',link )#line:122
    except :#line:123
        O0O00O0OOOOO000O0 =re .findall (r'biz=(.*?)&',OOOO0O00O0OO0000O )#line:124
    if O0O00O0OOOOO000O0 :#line:125
        O0O00O0OOOOO000O0 =O0O00O0OOOOO000O0 [0 ]#line:126
    else :#line:127
        return False #line:128
    O0O0000000OOO0000 =OOO000OO000OO00OO .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:129
    if O0O0000000OOO0000 :#line:130
        O0O0000000OOO0000 =O0O0000000OOO0000 [0 ].strip ()#line:131
    OO0OOOO000OO0OOO0 =re .findall (r"user_name.DATA'\) : '(.*?)'",OO00O0O0O000OOOO0 .text )or OOO000OO000OO00OO .xpath ('//span[@class="profile_meta_value"]/text()')#line:133
    if OO0OOOO000OO0OOO0 :#line:134
        OO0OOOO000OO0OOO0 =OO0OOOO000OO0OOO0 [0 ]#line:135
    O0O00O0O0OOO0000O =re .findall (r'createTime = \'(.*)\'',OO00O0O0O000OOOO0 .text )#line:136
    if O0O00O0O0OOO0000O :#line:137
        O0O00O0O0OOO0000O =O0O00O0O0OOO0000O [0 ][5 :]#line:138
    O0OO000OO00O0O0O0 =f'{O0O00O0O0OOO0000O}|{OOOO0OO00O00OO000}|{O0O00O0OOOOO000O0}|{O0O0000000OOO0000}|{OO0OOOO000OO0OOO0}'#line:139
    O000OO0O0O00O00O0 ={'biz':O0O00O0OOOOO000O0 ,'text':O0OO000OO00O0O0O0 }#line:140
    return O000OO0O0O00O00O0 #line:141
def ts ():#line:144
    return str (int (time .time ()))+'000'#line:145
class XYY :#line:148
    def __init__ (self ,cg ):#line:149
        self .name =cg ['name']#line:150
        self .ysm_uid =None #line:151
        self .ysmuid =cg .get ('ysmuid')#line:152
        self .sec =requests .session ()#line:153
        self .sec .headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Cookie':f'ysmuid={self.ysmuid};',}#line:158
        self .msg =''#line:159
    def init (self ):#line:161
        if not self .ysmuid :#line:163
            print ('ck没有ysmuid，不能运行本脚本，自动退出')#line:164
            return False #line:165
        OOOOO0O00OOOOO0O0 =0 #line:166
        while OOOOO0O00OOOOO0O0 <5 :#line:167
            O00000O0000O0O0OO =self .sec .get ('http://1695480664.snak.top/').text #line:168
            self .ysm_uid =re .findall (r'unionid="(o.*?)";',O00000O0000O0O0OO )#line:169
            if self .ysm_uid :#line:170
                self .ysm_uid =self .ysm_uid [0 ]#line:171
                OOO00O0O000000O0O =re .findall (r'href="(.*?)">提现',O00000O0000O0O0OO )#line:172
                if OOO00O0O000000O0O :#line:173
                    OOO00O0O000000O0O =OOO00O0O000000O0O [0 ]#line:174
                    OOOOO0O0O0O0OOOOO =parse_qs (urlparse (OOO00O0O000000O0O ).query )#line:175
                    self .unionid =OOOOO0O0O0O0OOOOO .get ('unionid')[0 ]#line:176
                    self .request_id =OOOOO0O0O0O0OOOOO .get ('request_id')[0 ]#line:177
                    self .netloc =urlparse (OOO00O0O000000O0O ).netloc #line:178
                else :#line:179
                    printlog (f'{self.name} 获取提现参数失败，本次不提现')#line:180
                    self .msg +=f'获取提现参数失败，本次不提现\n'#line:181
                return True #line:182
            else :#line:183
                OOOOO0O00OOOOO0O0 +=1 #line:184
                continue #line:185
        printlog (f'{self.name} 获取ysm_uid失败，请检查账号有效性')#line:186
        self .msg +='获取ysm_uid失败，请检查账号有效性\n'#line:187
        return False #line:188
    def user_info (self ):#line:190
        OOO0O0000O000000O =f'http://1695492718.snak.top/yunonline/v1/gold?unionid={self.ysm_uid}&time={ts()}'#line:191
        O000O0O00OOO0OOOO =self .sec .get (OOO0O0000O000000O ).json ()#line:192
        debugger (f'userinfo {O000O0O00OOO0OOOO}')#line:193
        O0OO0O0O0O0O0OO0O =O000O0O00OOO0OOOO .get ("data")#line:194
        self .last_gold =O000O0O00OOO0OOOO .get ("data").get ("last_gold")#line:195
        O0OO0OO0O0O0OO00O =O0OO0O0O0O0O0OO0O .get ("remain_read")#line:196
        OOO0000OO0O0O00OO =f'今日已经阅读了{O0OO0O0O0O0O0OO0O.get("day_read")}篇文章,剩余{O0OO0OO0O0O0OO00O}未阅读，今日获取金币{O0OO0O0O0O0O0OO0O.get("day_gold")}，剩余{self.last_gold}'#line:197
        printlog (f'{self.name}:{OOO0000OO0O0O00OO}')#line:198
        self .msg +=(OOO0000OO0O0O00OO +'\n')#line:199
        if O0OO0OO0O0O0OO00O ==0 :#line:200
            return False #line:201
        return True #line:202
    def getKey (self ):#line:204
        O0O0O0O00000O00OO ='http://1695492718.snak.top/yunonline/v1/wtmpdomain'#line:205
        O0OO000O0OO0O0000 =f'unionid={self.ysm_uid}'#line:206
        OO0OO0OO0O000O000 =self .sec .post (O0O0O0O00000O00OO ,data =O0OO000O0OO0O0000 ).json ()#line:207
        debugger (f'getkey {OO0OO0OO0O000O000}')#line:208
        O00OOOOOOOO0000O0 =OO0OO0OO0O000O000 .get ('data').get ('domain')#line:209
        self .uk =parse_qs (urlparse (O00OOOOOOOO0000O0 ).query ).get ('uk')[0 ]#line:210
        OO0O0OO0O00O0O00O =urlparse (O00OOOOOOOO0000O0 ).netloc #line:211
        self .headers ={'Connection':'keep-alive','Accept':'application/json, text/javascript, */*; q=0.01','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue','Origin':f'https://{OO0O0OO0O00O0O00O}','Sec-Fetch-Site':'cross-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh',}#line:222
    def read (self ):#line:224
        time .sleep (3 )#line:225
        O0O0O00OO0OOO0000 ={'uk':self .uk }#line:226
        while True :#line:227
            O00000O00OOO00O00 =f'https://nsr.zsf2023e458.cloud/yunonline/v1/do_read'#line:228
            O0O000OOOO0OOOO00 =requests .get (O00000O00OOO00O00 ,headers =self .headers ,params =O0O0O00OO0OOO0000 )#line:229
            self .msg +=('-'*50 +'\n')#line:230
            debugger (f'read1 {O0O000OOOO0OOOO00.text}')#line:231
            O0O000OOOO0OOOO00 =O0O000OOOO0OOOO00 .json ()#line:232
            if O0O000OOOO0OOOO00 .get ('errcode')==0 :#line:233
                OOO0000O000O000O0 =O0O000OOOO0OOOO00 .get ('data').get ('link')#line:234
                OO0OOOO000O0000OO =self .jump (OOO0000O000O000O0 )#line:235
                if 'mp.weixin'in OO0OOOO000O0000OO :#line:236
                    O0O00O0O0O0O0OO0O =getmpinfo (OO0OOOO000O0000OO )#line:237
                    if not O0O00O0O0O0O0OO0O :#line:238
                        printlog ('获取文章信息失败，程序中止')#line:239
                        return False #line:240
                    O00O0O0OO000000OO =O0O00O0O0O0O0OO0O ['biz']#line:241
                    self .msg +=('开始阅读 '+O0O00O0O0O0O0OO0O ['text']+'\n')#line:242
                    printlog (f'{self.name}:开始阅读 '+O0O00O0O0O0O0OO0O ['text'])#line:243
                    if O00O0O0OO000000OO in checklist :#line:244
                        send (msg =f"{O0O00O0O0O0O0OO0O['text']}",title =f'{self.name} 小阅阅阅读过检测',url =OO0OOOO000O0000OO )#line:245
                        self .msg +='遇到检测文章，已发送到微信，手动阅读，暂停50秒\n'#line:246
                        printlog (f'{self.name}:遇到检测文章，已发送到微信，手动阅读，暂停50秒')#line:247
                        time .sleep (50 )#line:248
                else :#line:249
                    self .msg +=f'{self.name} 小阅阅跳转到 {OO0OOOO000O0000OO}\n'#line:250
                    printlog (f'{self.name}: 小阅阅跳转到 {OO0OOOO000O0000OO}')#line:251
                    continue #line:252
                OOO00O0O00O00000O =random .randint (7 ,10 )#line:253
                self .msg +=f'本次模拟读{OOO00O0O00O00000O}秒\n'#line:254
                time .sleep (OOO00O0O00O00000O )#line:255
                O00000O00OOO00O00 =f'https://nsr.zsf2023e458.cloud/yunonline/v1/get_read_gold?uk={self.uk}&time={OOO00O0O00O00000O}&timestamp={ts()}'#line:256
                requests .get (O00000O00OOO00O00 ,headers =self .headers )#line:257
            elif O0O000OOOO0OOOO00 .get ('errcode')==405 :#line:258
                printlog (f'{self.name}:阅读重复')#line:259
                self .msg +='阅读重复\n'#line:260
                time .sleep (1.5 )#line:261
            elif O0O000OOOO0OOOO00 .get ('errcode')==407 :#line:262
                printlog (f'{self.name}:{O0O000OOOO0OOOO00.get("msg")}')#line:263
                self .msg +=(O0O000OOOO0OOOO00 .get ('msg')+'\n')#line:264
                return True #line:265
            else :#line:266
                printlog (f'{self.name}:{O0O000OOOO0OOOO00.get("msg")}')#line:267
                self .msg +=(O0O000OOOO0OOOO00 .get ("msg")+'\n')#line:268
                time .sleep (1.5 )#line:269
    def jump (self ,link ):#line:271
        OO0OOO00OO00000OO =urlparse (link ).netloc #line:272
        O00O00OOOO00000O0 ={'Host':OO0OOO00OO00000OO ,'Connection':'keep-alive','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh','Cookie':f'ysmuid={self.ysmuid}',}#line:282
        OO000OO000OO00OOO =requests .get (link ,headers =O00O00OOOO00000O0 ,allow_redirects =False )#line:283
        OOO0O0OOO0O0O000O =OO000OO000OO00OOO .headers .get ('Location')#line:284
        return OOO0O0OOO0O0O000O #line:285
    def withdraw (self ):#line:287
        if not self .unionid :#line:288
            return False #line:289
        if int (self .last_gold )<txbz :#line:290
            printlog (f'{self.name} 没有达到你设置的提现标准{txbz}')#line:291
            self .msg +=f'没有达到你设置的提现标准{txbz}\n'#line:292
            return False #line:293
        OOOOOO0OOOOOOOOO0 =int (int (self .last_gold )/1000 )*1000 #line:294
        self .msg +=f'本次提现金币{OOOOOO0OOOOOOOOO0}\n'#line:295
        printlog (f'{self.name}:本次提现金币{OOOOOO0OOOOOOOOO0}')#line:296
        if OOOOOO0OOOOOOOOO0 :#line:298
            O00OO0O000O0OO0O0 =f'http://{self.netloc}/yunonline/v1/user_gold'#line:299
            printlog (O00OO0O000O0OO0O0 )#line:300
            OO0OOOO0OOOOOOO0O =f'unionid={self.unionid}&request_id={self.request_id}&gold={OOOOOO0OOOOOOOOO0}'#line:301
            O0O00O00000O0OOOO =self .sec .post (O00OO0O000O0OO0O0 ,data =OO0OOOO0OOOOOOO0O )#line:302
            debugger (f'gold {O0O00O00000O0OOOO.text}')#line:303
            O00OO0O000O0OO0O0 =f'http://{self.netloc}/yunonline/v1/withdraw'#line:304
            OO0OOOO0OOOOOOO0O =f'unionid={self.unionid}&signid={self.request_id}&ua=0&ptype=0&paccount=&pname='#line:305
            O0O00O00000O0OOOO =self .sec .post (O00OO0O000O0OO0O0 ,data =OO0OOOO0OOOOOOO0O )#line:306
            debugger (f'withdraw {O0O00O00000O0OOOO.text}')#line:307
            self .msg +=f"提现结果 {O0O00O00000O0OOOO.json()['msg']}"#line:308
            printlog (f'{self.name}:提现结果 {O0O00O00000O0OOOO.json()["msg"]}')#line:309
    def run (self ):#line:311
        self .msg +=('='*50 +f'\n账号：{self.name}开始任务\n')#line:312
        printlog (f'账号：{self.name}开始任务')#line:313
        if not self .init ():#line:314
            return False #line:315
        if self .user_info ():#line:316
            self .getKey ()#line:317
            self .read ()#line:318
            self .user_info ()#line:319
            time .sleep (0.5 )#line:320
        self .withdraw ()#line:321
        printlog (f'账号：{self.name} 本轮任务结束')#line:322
        if not printf :#line:323
            print (self .msg )#line:324
def yd (q ):#line:327
    while not q .empty ():#line:328
        OO000OO0O00OOO0O0 =q .get ()#line:329
        OOOO00O00O0O00000 =XYY (OO000OO0O00OOO0O0 )#line:330
        OOOO00O00O0O00000 .run ()#line:331
def get_ver ():#line:334
    O0OOOO00OO000O0O0 ='kxyyV2 V2.1'#line:335
    OOOO0000OOO00000O ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:338
    OOOOOO0OOOOOOOOOO =requests .get ('https://ghproxy.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json',headers =OOOO0000OOO00000O ).json ()#line:340
    OO0O000OOOO000O00 =O0OOOO00OO000O0O0 .split (' ')[1 ]#line:341
    OO0OOO0OO0OO00000 =OOOOOO0OOOOOOOOOO .get ('version').get (O0OOOO00OO000O0O0 .split (' ')[0 ])#line:342
    OOOOO0O0000000000 =f"当前版本 {OO0O000OOOO000O00}，仓库版本 {OO0OOO0OO0OO00000}"#line:343
    if OO0O000OOOO000O00 <OO0OOO0OO0OO00000 :#line:344
        OOOOO0O0000000000 +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:345
    return OOOOO0O0000000000 #line:346
def main (xyyck ):#line:349
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:350
    try :#line:351
        xyyck =ast .literal_eval (xyyck )#line:352
    except :#line:353
        pass #line:354
    O0O0OO0OO00OOOO0O =[]#line:355
    O0OO000OO0OO00OOO =Queue ()#line:356
    for O00OOOO0OOO0O0OO0 in xyyck :#line:357
        printlog (f'{O00OOOO0OOO0O0OO0}\n以上是{O00OOOO0OOO0O0OO0["name"]}的ck，请核对是否正确，如不正确，请检查ck填写格式')#line:358
        O0OO000OO0OO00OOO .put (O00OOOO0OOO0O0OO0 )#line:359
    for O00OOOO0OOO0O0OO0 in range (max_workers ):#line:360
        O00OOOOO0000O0O00 =threading .Thread (target =yd ,args =(O0OO000OO0OO00OOO ,))#line:361
        O00OOOOO0000O0O00 .start ()#line:362
        O0O0OO0OO00OOOO0O .append (O00OOOOO0000O0O00 )#line:363
        time .sleep (20 )#line:364
    for OO0OOOOOOO00OO00O in O0O0OO0OO00OOOO0O :#line:365
        OO0OOOOOOO00OO00O .join ()#line:366
if __name__ =='__main__':#line:369
    main (xyyck )#line:370
