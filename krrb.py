# -*- coding: utf-8 -*-
# 人人帮
# Author: kk
# date：2023/8/25 16:35
"""
入口：http://ebb.maisucaiya.cloud/user/index.html?mid=1702983440137322496
如微信打不开，可复制到浏览器打开
抓包 http://ebb10.twopinkone.cloud/user/index.html?mid=1702983440137322496
cookie里的un token uid值

内置推送企业微信群机器人
参考 https://github.com/kxs2018/yuedu/blob/main/获取企业微信群机器人key.md 获取key，并关注插件！！！

export rrbck="[{'un': 'xxxx', 'token': 'xxxxx','uid':'xxxx'}]"
export qwbotkey="abcdefg"
------------------------------------------------------
no module named lxml 解决方案
1. 配置文件搜索 PipMirror，如果网址包含douban的，请改为下方的网址
PipMirror="https://pypi.tuna.tsinghua.edu.cn/simple"
2. 依赖管理-python 添加 lxml
3. 如果装不上，①请ssh连接到服务器 ②docker exec -it ql bash (ql是青龙容器的名字，不会就问百度) ③pip install pip -U
4. 再装不上依赖就放弃吧
------------------------------------------------------
提现标准默认是5000
达到标准自动提现到支付宝，请提前绑定支付宝
支付宝绑双账号方法：1.提前在支付宝设置好邮箱 2.手机号可以绑一号，邮箱可以绑一号
"""
import json #line:28
from random import randint #line:29
import os #line:30
import time #line:31
import requests #line:32
import ast #line:33
import re #line:34
try :#line:36
    from lxml import etree #line:37
except :#line:38
    print ('请仔细阅读脚本上方注释中的“no module named lxml 解决方案”')#line:39
    exit ()#line:40
import datetime #line:41
import threading #line:42
from queue import Queue #line:43
"""实时日志开关"""#line:45
printf =1 #line:46
"""1为开，0为关"""#line:47
"""debug模式开关"""#line:49
debug =0 #line:50
"""1为开，打印调试日志；0为关，不打印"""#line:51
"""线程数量设置"""#line:53
max_workers =3 #line:54
"""设置为3，即最多有3个任务同时进行"""#line:55
"""设置提现标准"""#line:57
txbz =5000 #line:58
"""设置为5000，即为5毛起提"""#line:59
qwbotkey =os .getenv ('qwbotkey')#line:61
rrbck =os .getenv ('rrbck')#line:62
if not qwbotkey or not rrbck :#line:63
    print ('请仔细阅读脚本开头的注释并配置好qwbotkey和rrbck')#line:64
    exit ()#line:65
def ftime ():#line:68
    O000OOO0OOO0OO000 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:69
    return O000OOO0OOO0OO000 #line:70
def debugger (text ):#line:73
    if debug :#line:74
        print (text )#line:75
def printlog (text ):#line:78
    if printf :#line:79
        print (text )#line:80
def send (msg ,title ='通知',url =None ):#line:83
    if not title or not url :#line:84
        O00O00OOOOO000OOO ={"msgtype":"text","text":{"content":f"{title}\n\n{msg}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:91
    else :#line:92
        O00O00OOOOO000OOO ={"msgtype":"news","news":{"articles":[{"title":title ,"description":msg ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:97
    OO00OO0O0O0000O00 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:98
    O0OOOOOO0O0OO0OO0 =requests .post (OO00OO0O0O0000O00 ,data =json .dumps (O00O00OOOOO000OOO )).json ()#line:99
    if O0OOOOOO0O0OO0OO0 .get ('errcode')!=0 :#line:100
        print ('消息发送失败，请检查key和发送格式')#line:101
        return False #line:102
    return O0OOOOOO0O0OO0OO0 #line:103
def getmpinfo (link ):#line:106
    if not link or link =='':#line:107
        return False #line:108
    O00O0O0OO000O0000 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:110
    O000O0OO0OOO000O0 =requests .get (link ,headers =O00O0O0OO000O0000 )#line:111
    O0O000OOO0OOO000O =etree .HTML (O000O0OO0OOO000O0 .text )#line:112
    OOOO0OOOO0OOOO00O =O0O000OOO0OOO000O .xpath ('//meta[@*="og:title"]/@content')#line:114
    if OOOO0OOOO0OOOO00O :#line:115
        OOOO0OOOO0OOOO00O =OOOO0OOOO0OOOO00O [0 ]#line:116
    O0OOOOOO0O0OOOOO0 =O0O000OOO0OOO000O .xpath ('//meta[@*="og:url"]/@content')#line:117
    if O0OOOOOO0O0OOOOO0 :#line:118
        O0OOOOOO0O0OOOOO0 =O0OOOOOO0O0OOOOO0 [0 ].encode ().decode ()#line:119
    O0OOO000O0OOO0O00 =re .findall (r'biz=(.*?)&',link )or re .findall (r'biz=(.*?)&',O0OOOOOO0O0OOOOO0 )#line:120
    if O0OOO000O0OOO0O00 :#line:121
        O0OOO000O0OOO0O00 =O0OOO000O0OOO0O00 [0 ]#line:122
    OOOOOOOOOOOO0O00O =O0O000OOO0OOO000O .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:123
    if OOOOOOOOOOOO0O00O :#line:124
        OOOOOOOOOOOO0O00O =OOOOOOOOOOOO0O00O [0 ].strip ()#line:125
    O0OO0OOO00OO0O000 =re .findall (r"user_name.DATA'\) : '(.*?)'",O000O0OO0OOO000O0 .text )or O0O000OOO0OOO000O .xpath ('//span[@class="profile_meta_value"]/text()')#line:127
    if O0OO0OOO00OO0O000 :#line:128
        O0OO0OOO00OO0O000 =O0OO0OOO00OO0O000 [0 ]#line:129
    O0OOOOOOOOO0OOOOO =re .findall (r'createTime = \'(.*)\'',O000O0OO0OOO000O0 .text )#line:130
    if O0OOOOOOOOO0OOOOO :#line:131
        O0OOOOOOOOO0OOOOO =O0OOOOOOOOO0OOOOO [0 ][5 :]#line:132
    OOO00OO0OO00O0000 =f'{O0OOOOOOOOO0OOOOO} {OOOO0OOOO0OOOO00O}'#line:133
    OO0O0000O000OOOO0 ={'biz':O0OOO000O0OOO0O00 ,'text':OOO00OO0OO00O0000 }#line:134
    return OO0O0000O000OOOO0 #line:135
class RRBYD :#line:138
    def __init__ (self ,ck ):#line:139
        self .ck =ck #line:140
        self .headers ={'Host':'ebb.vinse.cn','un':self .ck ['un'],'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue','uid':self .ck ['uid'],'platform':'0','token':self .ck ['token'],'Origin':'http://ebb10.twopinkone.cloud','Referer':'http://ebb10.twopinkone.cloud/',}#line:148
        self .msg =''#line:149
    def userinfo (self ):#line:151
        O000000000OOOO000 ='http://ebb.vinse.cn/api/user/info'#line:152
        O0OO00O000OOOO0OO =requests .post (O000000000OOOO000 ,headers =self .headers ,json ={"pageSize":10 }).json ()#line:153
        debugger (f'userinfo {O0OO00O000OOOO0OO}')#line:154
        if O0OO00O000OOOO0OO .get ('code')!=0 :#line:155
            self .msg +=f'{self.ck["un"]} cookie失效'+'\n'#line:156
            printlog (f'{self.ck["un"]} cookie失效')#line:157
            return 0 #line:158
        O000OO000OO0OO000 =O0OO00O000OOOO0OO .get ('result')#line:159
        self .nickname =O000OO000OO0OO000 .get ('nickName')[0 :3 ]+'****'+O000OO000OO0OO000 .get ('nickName')[-4 :]#line:160
        OOOOOOOOO000O0OO0 =O000OO000OO0OO000 .get ('integralCurrent')#line:161
        O00OOO00OO0OO00OO =O000OO000OO0OO000 .get ('integralTotal')#line:162
        self .msg +=f'用户：{self.nickname},当前共有帮豆{OOOOOOOOO000O0OO0}，总共获得帮豆{O00OOO00OO0OO00OO}\n'#line:163
        printlog (f'{self.nickname},当前共有帮豆{OOOOOOOOO000O0OO0}，总共获得帮豆{O00OOO00OO0OO00OO}')#line:164
        return OOOOOOOOO000O0OO0 #line:165
    def sign (self ):#line:167
        O00O0OO0O0OOO0000 ='http://ebb.vinse.cn/api/user/sign'#line:168
        O0000OO000000OO00 =requests .post (O00O0OO0O0OOO0000 ,headers =self .headers ,json ={"pageSize":10 }).json ()#line:169
        debugger (f'sign {O0000OO000000OO00}')#line:170
        if O0000OO000000OO00 .get ('code')==0 :#line:171
            self .msg +=f'签到成功，获得帮豆{O0000OO000000OO00.get("result").get("point")}'+'\n'#line:172
            printlog (f'{self.nickname}:签到成功，获得帮豆{O0000OO000000OO00.get("result").get("point")}')#line:173
        elif O0000OO000000OO00 .get ('code')==99 :#line:174
            self .msg +=O0000OO000000OO00 .get ('msg')+'\n'#line:175
        else :#line:176
            self .msg +='签到错误'+'\n'#line:177
    def reward (self ):#line:179
        O0O000OOOOO0OOOOO ='http://ebb.vinse.cn/api/user/receiveOneDivideReward'#line:180
        O0O0O000OOO00OO00 =requests .post (O0O000OOOOO0OOOOO ,headers =self .headers ,json ={"pageSize":10 }).json ()#line:181
        if O0O0O000OOO00OO00 .get ('code')==0 :#line:182
            self .msg +=f"领取一级帮豆：{O0O0O000OOO00OO00.get('msg')}\n"#line:183
            printlog (f"{self.nickname}:领取一级帮豆：{O0O0O000OOO00OO00.get('msg')}")#line:184
        O0O000OOOOO0OOOOO ='http://ebb.vinse.cn/api/user/receiveTwoDivideReward'#line:185
        O0O0O000OOO00OO00 =requests .post (O0O000OOOOO0OOOOO ,headers =self .headers ,json ={"pageSize":10 }).json ()#line:186
        if O0O0O000OOO00OO00 .get ('code')==0 :#line:187
            self .msg +=f"领取二级帮豆：{O0O0O000OOO00OO00.get('msg')}"+'\n'#line:188
            printlog (f"{self.nickname}:领取二级帮豆：{O0O0O000OOO00OO00.get('msg')}")#line:189
    def getentry (self ):#line:191
        OOO0O00OOO0OO0O0O ={'Host':'u.cocozx.cn',"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Origin":"http://ebb10.twopinkone.cloud","Sec-Fetch-Site":"cross-site","Sec - Fetch - Mode":"cors","Sec - Fetch - Dest":"empty"}#line:198
        O0O000OO0O0O0000O =f'https://u.cocozx.cn/ipa/read/getEntryUrl?fr=ebb0726&uid={self.ck["uid"]}'#line:199
        OOOOOO00OO00OOO0O =requests .get (O0O000OO0O0O0000O ,headers =OOO0O00OOO0OO0O0O ).json ()#line:200
        debugger (f'getentry {OOOOOO00OO00OOO0O}')#line:201
        O0O0000O00O000OOO =OOOOOO00OO00OOO0O .get ('result')#line:202
        if OOOOOO00OO00OOO0O .get ('code')==0 :#line:203
            OO000O0000000O0OO =O0O0000O00O000OOO .get ('url')#line:204
            self .entryurl =re .findall (r'(http://.*?)/',OO000O0000000O0OO )[0 ]#line:205
        else :#line:206
            self .msg +="阅读链接获取失败"+'\n'#line:207
            printlog (f"{self.nickname}:阅读链接获取失败")#line:208
    def read (self ):#line:210
        OO0OO00O0OO00OO0O ={"Origin":self .entryurl ,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Host":"u.cocozx.cn"}#line:215
        for OO000O00O00OOO0OO in range (1 ,3 ):#line:216
            OO00OOOO00OO00O0O ={"fr":"ebb0726","uid":self .ck ['uid'],"group":OO000O00O00OOO0OO ,"un":'',"token":'',"pageSize":20 }#line:217
            O000OOO0OOOO00OO0 ='http://u.cocozx.cn/ipa/read/read'#line:218
            while True :#line:219
                O00O000O0O000OOOO =requests .post (O000OOO0OOOO00OO0 ,headers =OO0OO00O0OO00OO0O ,json =OO00OOOO00OO00O0O )#line:220
                debugger ("read "+O00O000O0O000OOOO .text )#line:221
                OOO0OO0O00OOO0OOO =O00O000O0O000OOOO .json ().get ('result')#line:222
                O0OOOO00OOO00O00O =OOO0OO0O00OOO0OOO .get ('url')#line:223
                if OOO0OO0O00OOO0OOO ['status']==10 :#line:224
                    O000OO0000O00OO00 =getmpinfo (O0OOOO00OOO00O00O )#line:225
                    self .msg +='-'*50 +'\n开始阅读 '+O000OO0000O00OO00 .get ('text')+'\n'#line:226
                    printlog (f"{self.nickname}:\n开始阅读  {O000OO0000O00OO00.get('text')}")#line:227
                    OO000OO0OOOO0000O =O000OO0000O00OO00 .get ('biz')#line:228
                    if OO000OO0OOOO0000O =='Mzg2Mzk3Mjk5NQ==':#line:229
                        self .msg +='正在阅读检测文章\n发送通知，暂停50秒\n'#line:230
                        printlog (f"{self.nickname}:正在阅读检测文章\n发送通知，暂停50秒")#line:231
                        send (title =O000OO0000O00OO00 ['text'],msg =f'{self.nickname}  人人帮阅读正在读检测文章',url =O0OOOO00OOO00O00O )#line:232
                        time .sleep (50 )#line:233
                    OO0OOO0O00O00O0O0 =randint (7 ,10 )#line:234
                    time .sleep (OO0OOO0O00O00O0O0 )#line:235
                    self .submit (OO000O00O00OOO0OO )#line:236
                elif OOO0OO0O00OOO0OOO ['status']==60 :#line:237
                    self .msg +='文章已经全部读完了\n'#line:238
                    printlog (f"{self.nickname}:文章已经全部读完了")#line:239
                    break #line:240
                elif OOO0OO0O00OOO0OOO ['status']==30 :#line:241
                    time .sleep (2 )#line:242
                    continue #line:243
                elif OOO0OO0O00OOO0OOO ['status']==50 :#line:244
                    self .msg +='阅读失效\n'#line:245
                    printlog (f"{self.nickname}:阅读失效")#line:246
                    break #line:247
                else :#line:248
                    break #line:249
            time .sleep (2 )#line:250
    def submit (self ,group ):#line:252
        OO0000O0O00OOO0O0 ='http://u.cocozx.cn/ipa/read/submit'#line:253
        OOOOO00OOO0OO000O ={"Origin":self .entryurl ,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Host":"u.cocozx.cn"}#line:258
        O0OOOO0OO0000O000 ={"fr":"ebb0726","uid":self .ck ['uid'],"group":group ,"un":'',"token":'',"pageSize":20 }#line:259
        OOOOO0OO0O00O0OO0 =requests .post (OO0000O0O00OOO0O0 ,headers =OOOOO00OOO0OO000O ,json =O0OOOO0OO0000O000 ).json ()#line:260
        debugger (f"submit {OOOOO0OO0O00O0OO0}")#line:261
        OO00O0O000O0OO00O =OOOOO0OO0O00O0OO0 .get ('result')#line:262
        OOO0OOO0OOO0000O0 =OO00O0O000O0OO00O .get ("dayCount")#line:263
        O000O0O0OOO0O000O =OO00O0O000O0OO00O .get ("dayMax")#line:264
        OO0OOOO0O0O000O0O =OO00O0O000O0OO00O .get ("progress")#line:265
        self .msg +=f"今日已阅读{OOO0OOO0OOO0000O0}，本轮剩余{OO0OOOO0O0O000O0O}，单日最高{O000O0O0OOO0O000O}\n"#line:266
        printlog (f"{self.nickname}:今日已阅读{OOO0OOO0OOO0000O0}，本轮剩余{OO0OOOO0O0O000O0O}，单日最高{O000O0O0OOO0O000O}")#line:267
    def tx (self ):#line:269
        global txje #line:270
        OO0O000000O000000 =self .userinfo ()#line:271
        if OO0O000000O000000 <txbz :#line:272
            self .msg +='帮豆不够提现标准，明儿请早\n'#line:273
            printlog (f"{self.nickname}:帮豆不够提现标准，明儿请早")#line:274
            return #line:275
        elif 5000 <=OO0O000000O000000 <10000 :#line:276
            txje =5000 #line:277
        elif 10000 <=OO0O000000O000000 <50000 :#line:278
            txje =10000 #line:279
        elif 50000 <=OO0O000000O000000 <100000 :#line:280
            txje =50000 #line:281
        elif OO0O000000O000000 >=100000 :#line:282
            txje =100000 #line:283
        O0O0O000O0O0000O0 =f"http://ebb.vinse.cn/apiuser/aliWd"#line:284
        OO0OO00OO0O0OOO00 ={"val":txje ,"pageSize":10 }#line:285
        O000O0OOO0000O00O =requests .post (O0O0O000O0O0000O0 ,headers =self .headers ,json =OO0OO00OO0O0OOO00 ).json ()#line:286
        if O000O0OOO0000O00O .get ('code')==0 :#line:287
            send (f'{self.nickname} 人人帮提现支付宝{txje / 10000}元',title ='人人帮阅读提现到账')#line:288
    def run (self ):#line:290
        self .msg +='='*50 +'\n'#line:291
        if self .userinfo ():#line:292
            self .sign ()#line:293
            self .reward ()#line:294
            self .getentry ()#line:295
            time .sleep (1 )#line:296
            self .read ()#line:297
            self .tx ()#line:298
        if not printf :#line:299
            print (self .msg .strip ())#line:300
def yd (q ):#line:303
    while not q .empty ():#line:304
        OOOO00O0OO0OO0O00 =q .get ()#line:305
        OO000O0OOOOOOO0OO =RRBYD (OOOO00O0OO0OO0O00 )#line:306
        OO000O0OOOOOOO0OO .run ()#line:307
def get_ver ():#line:310
    O00O000OO00OO0000 ='krrb V1.1.2'#line:311
    OO0O0OO0O00000O00 ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:314
    OO000OO0O000O0OOO =requests .get ('https://ghproxy.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json',headers =OO0O0OO0O00000O00 ).json ()#line:316
    O00OOOOO0OO00OO00 =O00O000OO00OO0000 .split (' ')[1 ]#line:317
    O00O0O0OO00000OO0 =OO000OO0O000O0OOO .get ('version').get (O00O000OO00OO0000 .split (' ')[0 ])#line:318
    O0OO000O000OOO0O0 =f"当前版本 {O00OOOOO0OO00OO00}，仓库版本 {O00O0O0OO00000OO0}"#line:319
    if O00OOOOO0OO00OO00 <O00O0O0OO00000OO0 :#line:320
        O0OO000O000OOO0O0 +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:321
    return O0OO000O000OOO0O0 #line:322
def main (rrbck ):#line:325
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:326
    try :#line:327
        rrbck =ast .literal_eval (rrbck )#line:328
    except :#line:329
        pass #line:330
    OOOO0OOOO00O0OO0O =Queue ()#line:331
    O0OOOOO00O0OO0O00 =[]#line:332
    for OOOO000000OO0O00O ,OOOO0000000O0O0O0 in enumerate (rrbck ,start =1 ):#line:333
        printlog (f'{OOOO0000000O0O0O0}\n以上是账号{OOOO000000OO0O00O}的ck，请核对是否正确，如不正确，请检查ck填写格式')#line:334
        OOOO0OOOO00O0OO0O .put (OOOO0000000O0O0O0 )#line:335
    for OOOO000000OO0O00O in range (max_workers ):#line:336
        OOOOO0000OO00O000 =threading .Thread (target =yd ,args =(OOOO0OOOO00O0OO0O ,))#line:337
        OOOOO0000OO00O000 .start ()#line:338
        O0OOOOO00O0OO0O00 .append (OOOOO0000OO00O000 )#line:339
        time .sleep (30 )#line:340
    for O000OO0000OO0OOOO in O0OOOOO00O0OO0O00 :#line:341
        O000OO0000OO0OOOO .join ()#line:342
if __name__ =='__main__':#line:345
    main (rrbck )#line:346
