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

"""实时日志开关"""
printf = 1
"""1为开，0为关"""

"""debug模式开关"""
debug = 0
"""1为开，打印调试日志；0为关，不打印"""

"""线程数量设置"""
max_workers = 3
"""设置为3，即最多有3个任务同时进行"""

"""设置提现标准"""
txbz = 5000  # 不低于5000，平台的提现标准为5000
"""设置为5000，即为5毛起提"""

qwbotkey =os .getenv ('qwbotkey')#line:61
if not qwbotkey :#line:62
    print ('请仔细阅读脚本开头的注释并配置好qwbotkey')#line:63
    exit ()#line:64
def ftime ():#line:67
    O00OO00O0O0OO0O00 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:68
    return O00OO00O0O0OO0O00 #line:69
def debugger (O0OOOOO0OOO000OO0 ):#line:72
    if debug :#line:73
        print (O0OOOOO0OOO000OO0 )#line:74
def printlog (OO00O0OOOO0OO0OO0 ):#line:77
    if printf :#line:78
        print (OO00O0OOOO0OO0OO0 )#line:79
def send (O0O00000OOOOOOO0O ,title ='通知',url =None ):#line:82
    if not title or not url :#line:83
        O00OO0O0000OOO000 ={"msgtype":"text","text":{"content":f"{title}\n\n{O0O00000OOOOOOO0O}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:90
    else :#line:91
        O00OO0O0000OOO000 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O0O00000OOOOOOO0O ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:96
    OO00OO0000O0OO000 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:97
    O00O00OOOOO0O0OOO =requests .post (OO00OO0000O0OO000 ,data =json .dumps (O00OO0O0000OOO000 )).json ()#line:98
    if O00O00OOOOO0O0OOO .get ('errcode')!=0 :#line:99
        print ('消息发送失败，请检查key和发送格式')#line:100
        return False #line:101
    return O00O00OOOOO0O0OOO #line:102
def getmpinfo (O0O00OOO0OOO0000O ):#line:105
    if not O0O00OOO0OOO0000O or O0O00OOO0OOO0000O =='':#line:106
        return False #line:107
    O0O0O00OOOO0O0OOO ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:109
    OOO0000OOO0O00000 =requests .get (O0O00OOO0OOO0000O ,headers =O0O0O00OOOO0O0OOO )#line:110
    OOO0O0O0OOO00OO00 =etree .HTML (OOO0000OOO0O00000 .text )#line:111
    O0O00O0O000O00O0O =OOO0O0O0OOO00OO00 .xpath ('//meta[@*="og:title"]/@content')#line:113
    if O0O00O0O000O00O0O :#line:114
        O0O00O0O000O00O0O =O0O00O0O000O00O0O [0 ]#line:115
    O0OO0O0O00000OO0O =OOO0O0O0OOO00OO00 .xpath ('//meta[@*="og:url"]/@content')#line:116
    if O0OO0O0O00000OO0O :#line:117
        O0OO0O0O00000OO0O =O0OO0O0O00000OO0O [0 ].encode ().decode ()#line:118
    try :#line:119
        OO0O0OO0OOOOO000O =re .findall (r'biz=(.*?)&',O0O00OOO0OOO0000O )#line:120
    except :#line:121
        OO0O0OO0OOOOO000O =re .findall (r'biz=(.*?)&',O0OO0O0O00000OO0O )#line:122
    if OO0O0OO0OOOOO000O :#line:123
        OO0O0OO0OOOOO000O =OO0O0OO0OOOOO000O [0 ]#line:124
    else :#line:125
        return False #line:126
    O0OOOO000OOO0O000 =OOO0O0O0OOO00OO00 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:127
    if O0OOOO000OOO0O000 :#line:128
        O0OOOO000OOO0O000 =O0OOOO000OOO0O000 [0 ].strip ()#line:129
    O000OO0O0OO0000O0 =re .findall (r"user_name.DATA'\) : '(.*?)'",OOO0000OOO0O00000 .text )or OOO0O0O0OOO00OO00 .xpath ('//span[@class="profile_meta_value"]/text()')#line:131
    if O000OO0O0OO0000O0 :#line:132
        O000OO0O0OO0000O0 =O000OO0O0OO0000O0 [0 ]#line:133
    O00O0000OOO0O0OO0 =re .findall (r'createTime = \'(.*)\'',OOO0000OOO0O00000 .text )#line:134
    if O00O0000OOO0O0OO0 :#line:135
        O00O0000OOO0O0OO0 =O00O0000OOO0O0OO0 [0 ][5 :]#line:136
    O000OOO000OO0O000 =f'{O00O0000OOO0O0OO0} {O0O00O0O000O00O0O}'#line:137
    O00OO0O0000O00000 ={'biz':OO0O0OO0OOOOO000O ,'text':O000OOO000OO0O000 }#line:138
    return O00OO0O0000O00000 #line:139
class RRBYD :#line:142
    def __init__ (O0O00O0OO0O0O0OOO ,OO000O0O00O00OO0O ):#line:143
        O0O00O0OO0O0O0OOO .ck =OO000O0O00O00OO0O #line:144
        O0O00O0OO0O0O0OOO .headers ={'Host':'ebb.vinse.cn','un':O0O00O0OO0O0O0OOO .ck ['un'],'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue','uid':O0O00O0OO0O0O0OOO .ck ['uid'],'platform':'0','token':O0O00O0OO0O0O0OOO .ck ['token'],'Origin':'http://ebb10.twopinkone.cloud','Referer':'http://ebb10.twopinkone.cloud/',}#line:152
        O0O00O0OO0O0O0OOO .msg =''#line:153
    def userinfo (O0O0O00O00O00O0OO ):#line:155
        O0OO0O0000O00O0O0 ='http://ebb.vinse.cn/api/user/info'#line:156
        OOOO00OO0000O0O00 =requests .post (O0OO0O0000O00O0O0 ,headers =O0O0O00O00O00O0OO .headers ,json ={"pageSize":10 }).json ()#line:157
        debugger (f'userinfo {OOOO00OO0000O0O00}')#line:158
        if OOOO00OO0000O0O00 .get ('code')!=0 :#line:159
            O0O0O00O00O00O0OO .msg +=f'{O0O0O00O00O00O0OO.ck["un"]} cookie失效'+'\n'#line:160
            printlog (f'{O0O0O00O00O00O0OO.ck["un"]} cookie失效')#line:161
            return 0 #line:162
        O0O00O0OO00OO0O00 =OOOO00OO0000O0O00 .get ('result')#line:163
        O0O0O00O00O00O0OO .nickname =O0O00O0OO00OO0O00 .get ('nickName')[0 :3 ]+'****'+O0O00O0OO00OO0O00 .get ('nickName')[-4 :]#line:164
        O000O00O0O00000OO =O0O00O0OO00OO0O00 .get ('integralCurrent')#line:165
        O0OO00O0O00O0000O =O0O00O0OO00OO0O00 .get ('integralTotal')#line:166
        O0O0O00O00O00O0OO .msg +=f'用户：{O0O0O00O00O00O0OO.nickname},当前共有帮豆{O000O00O0O00000OO}，总共获得帮豆{O0OO00O0O00O0000O}\n'#line:167
        printlog (f'{O0O0O00O00O00O0OO.nickname},当前共有帮豆{O000O00O0O00000OO}，总共获得帮豆{O0OO00O0O00O0000O}')#line:168
        return O000O00O0O00000OO #line:169
    def sign (O000O000O00OOOOO0 ):#line:171
        O000OO000O00OOOOO ='http://ebb.vinse.cn/api/user/sign'#line:172
        OO000O00OOOOO0O00 =requests .post (O000OO000O00OOOOO ,headers =O000O000O00OOOOO0 .headers ,json ={"pageSize":10 }).json ()#line:173
        debugger (f'sign {OO000O00OOOOO0O00}')#line:174
        if OO000O00OOOOO0O00 .get ('code')==0 :#line:175
            O000O000O00OOOOO0 .msg +=f'签到成功，获得帮豆{OO000O00OOOOO0O00.get("result").get("point")}'+'\n'#line:176
            printlog (f'{O000O000O00OOOOO0.nickname}:签到成功，获得帮豆{OO000O00OOOOO0O00.get("result").get("point")}')#line:177
        elif OO000O00OOOOO0O00 .get ('code')==99 :#line:178
            O000O000O00OOOOO0 .msg +=OO000O00OOOOO0O00 .get ('msg')+'\n'#line:179
        else :#line:180
            O000O000O00OOOOO0 .msg +='签到错误'+'\n'#line:181
    def reward (OOO0OOO0O0O0OO000 ):#line:183
        O00O0O0OO00000OOO ='http://ebb.vinse.cn/api/user/receiveOneDivideReward'#line:184
        OO000OOO0OOOO00OO =requests .post (O00O0O0OO00000OOO ,headers =OOO0OOO0O0O0OO000 .headers ,json ={"pageSize":10 }).json ()#line:185
        if OO000OOO0OOOO00OO .get ('code')==0 :#line:186
            OOO0OOO0O0O0OO000 .msg +=f"领取一级帮豆：{OO000OOO0OOOO00OO.get('msg')}\n"#line:187
            printlog (f"{OOO0OOO0O0O0OO000.nickname}:领取一级帮豆：{OO000OOO0OOOO00OO.get('msg')}")#line:188
        O00O0O0OO00000OOO ='http://ebb.vinse.cn/api/user/receiveTwoDivideReward'#line:189
        OO000OOO0OOOO00OO =requests .post (O00O0O0OO00000OOO ,headers =OOO0OOO0O0O0OO000 .headers ,json ={"pageSize":10 }).json ()#line:190
        if OO000OOO0OOOO00OO .get ('code')==0 :#line:191
            OOO0OOO0O0O0OO000 .msg +=f"领取二级帮豆：{OO000OOO0OOOO00OO.get('msg')}"+'\n'#line:192
            printlog (f"{OOO0OOO0O0O0OO000.nickname}:领取二级帮豆：{OO000OOO0OOOO00OO.get('msg')}")#line:193
    def getentry (O00OO0OOO0OO0OOOO ):#line:195
        OO00000O0O00OOOO0 ={'Host':'u.cocozx.cn',"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Origin":"http://ebb10.twopinkone.cloud","Sec-Fetch-Site":"cross-site","Sec - Fetch - Mode":"cors","Sec - Fetch - Dest":"empty"}#line:202
        O0OO0OOO0O0OOOOO0 =f'https://u.cocozx.cn/ipa/read/getEntryUrl?fr=ebb0726&uid={O00OO0OOO0OO0OOOO.ck["uid"]}'#line:203
        O0OO000000OO0OOOO =requests .get (O0OO0OOO0O0OOOOO0 ,headers =OO00000O0O00OOOO0 ).json ()#line:204
        debugger (f'getentry {O0OO000000OO0OOOO}')#line:205
        O000OO0O0OO0000OO =O0OO000000OO0OOOO .get ('result')#line:206
        if O0OO000000OO0OOOO .get ('code')==0 :#line:207
            O0O00O0O0OO00OOOO =O000OO0O0OO0000OO .get ('url')#line:208
            O00OO0OOO0OO0OOOO .entryurl =re .findall (r'(http://.*?)/',O0O00O0O0OO00OOOO )[0 ]#line:209
        else :#line:210
            O00OO0OOO0OO0OOOO .msg +="阅读链接获取失败"+'\n'#line:211
            printlog (f"{O00OO0OOO0OO0OOOO.nickname}:阅读链接获取失败")#line:212
    def read (OOOO0O0O00O000OO0 ):#line:214
        O0OOOO0O000000000 ={"Origin":OOOO0O0O00O000OO0 .entryurl ,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Host":"u.cocozx.cn"}#line:219
        for OOO0OO00O00OOO000 in range (1 ,3 ):#line:220
            O0OO000O0O00O0000 ={"fr":"ebb0726","uid":OOOO0O0O00O000OO0 .ck ['uid'],"group":OOO0OO00O00OOO000 ,"un":'',"token":'',"pageSize":20 }#line:221
            O0O0OO00OOOO0OO0O ='http://u.cocozx.cn/ipa/read/read'#line:222
            while True :#line:223
                OOO0O0000O0OOOO00 =requests .post (O0O0OO00OOOO0OO0O ,headers =O0OOOO0O000000000 ,json =O0OO000O0O00O0000 )#line:224
                debugger ("read "+OOO0O0000O0OOOO00 .text )#line:225
                OO0O0OO0OO0O00OOO =OOO0O0000O0OOOO00 .json ().get ('result')#line:226
                OOOO00O0OO0O000OO =OO0O0OO0OO0O00OOO .get ('url')#line:227
                if OO0O0OO0OO0O00OOO ['status']==10 :#line:228
                    OOOOO0000O0O00000 =getmpinfo (OOOO00O0OO0O000OO )#line:229
                    if not OOOOO0000O0O00000 :#line:230
                        printlog (f'{OOOO0O0O00O000OO0.nickname}:获取文章信息失败，程序中止')#line:231
                        return False #line:232
                    OOOO0O0O00O000OO0 .msg +='-'*50 +'\n开始阅读 '+OOOOO0000O0O00000 .get ('text')+'\n'#line:233
                    printlog (f"{OOOO0O0O00O000OO0.nickname}:\n开始阅读  {OOOOO0000O0O00000.get('text')}")#line:234
                    OO00OO000O0OO00O0 =OOOOO0000O0O00000 .get ('biz')#line:235
                    if OO00OO000O0OO00O0 =='Mzg2Mzk3Mjk5NQ==':#line:236
                        OOOO0O0O00O000OO0 .msg +='正在阅读检测文章\n发送通知，暂停60秒\n'#line:237
                        printlog (f"{OOOO0O0O00O000OO0.nickname}:正在阅读检测文章\n发送通知，暂停60秒")#line:238
                        send (f'{OOOO0O0O00O000OO0.nickname}  人人帮阅读正在读检测文章',title =OOOOO0000O0O00000 ['text'],url =OOOO00O0OO0O000OO )#line:239
                        time .sleep (60 )#line:240
                    OO000O0O0OO0O0OO0 =randint (7 ,10 )#line:241
                    time .sleep (OO000O0O0OO0O0OO0 )#line:242
                    OOOO0O0O00O000OO0 .submit (OOO0OO00O00OOO000 )#line:243
                elif OO0O0OO0OO0O00OOO ['status']==60 :#line:244
                    OOOO0O0O00O000OO0 .msg +='文章已经全部读完了\n'#line:245
                    printlog (f"{OOOO0O0O00O000OO0.nickname}:文章已经全部读完了")#line:246
                    break #line:247
                elif OO0O0OO0OO0O00OOO ['status']==30 :#line:248
                    time .sleep (2 )#line:249
                    continue #line:250
                elif OO0O0OO0OO0O00OOO ['status']==50 :#line:251
                    OOOO0O0O00O000OO0 .msg +='阅读失效\n'#line:252
                    printlog (f"{OOOO0O0O00O000OO0.nickname}:阅读失效")#line:253
                    break #line:254
                else :#line:255
                    break #line:256
            time .sleep (2 )#line:257
    def submit (O00000O0O00OO0O0O ,OO0O000OO000OOO00 ):#line:259
        OOO0OOOOO00O0O000 ='http://u.cocozx.cn/ipa/read/submit'#line:260
        O0OOOOO000OOO0O00 ={"Origin":O00000O0O00OO0O0O .entryurl ,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Host":"u.cocozx.cn"}#line:265
        O000OO0O00000OOO0 ={"fr":"ebb0726","uid":O00000O0O00OO0O0O .ck ['uid'],"group":OO0O000OO000OOO00 ,"un":'',"token":'',"pageSize":20 }#line:266
        OO00OO00000000O0O =requests .post (OOO0OOOOO00O0O000 ,headers =O0OOOOO000OOO0O00 ,json =O000OO0O00000OOO0 ).json ()#line:267
        debugger (f"submit {OO00OO00000000O0O}")#line:268
        O0O0O0OOO000000O0 =OO00OO00000000O0O .get ('result')#line:269
        O0OO0OO0OOO00O0O0 =O0O0O0OOO000000O0 .get ("dayCount")#line:270
        OO00O0OOOOO00000O =O0O0O0OOO000000O0 .get ("dayMax")#line:271
        O0OO00OO0O00OOOO0 =O0O0O0OOO000000O0 .get ("progress")#line:272
        O00000O0O00OO0O0O .msg +=f"今日已阅读{O0OO0OO0OOO00O0O0}，本轮剩余{O0OO00OO0O00OOOO0}，单日最高{OO00O0OOOOO00000O}\n"#line:273
        printlog (f"{O00000O0O00OO0O0O.nickname}:今日已阅读{O0OO0OO0OOO00O0O0}，本轮剩余{O0OO00OO0O00OOOO0}，单日最高{OO00O0OOOOO00000O}")#line:274
    def tx (OO0O00000O00O00O0 ):#line:276
        global txje #line:277
        O0O000O0000O0O0O0 =OO0O00000O00O00O0 .userinfo ()#line:278
        if O0O000O0000O0O0O0 <txbz :#line:279
            OO0O00000O00O00O0 .msg +='帮豆不够提现标准，明儿请早\n'#line:280
            printlog (f"{OO0O00000O00O00O0.nickname}:帮豆不够提现标准，明儿请早")#line:281
            return #line:282
        elif 5000 <=O0O000O0000O0O0O0 <10000 :#line:283
            txje =5000 #line:284
        elif 10000 <=O0O000O0000O0O0O0 <50000 :#line:285
            txje =10000 #line:286
        elif 50000 <=O0O000O0000O0O0O0 <100000 :#line:287
            txje =50000 #line:288
        elif O0O000O0000O0O0O0 >=100000 :#line:289
            txje =100000 #line:290
        O000O00OOO0OOO0O0 =f"http://ebb.vinse.cn/apiuser/aliWd"#line:291
        OOO00O0OOOO000OO0 ={"val":txje ,"pageSize":10 }#line:292
        OO0O0OOOO00O00OO0 =requests .post (O000O00OOO0OOO0O0 ,headers =OO0O00000O00O00O0 .headers ,json =OOO00O0OOOO000OO0 ).json ()#line:293
        if OO0O0OOOO00O00OO0 .get ('code')==0 :#line:294
            send (f'{OO0O00000O00O00O0.nickname} 人人帮提现支付宝{txje / 10000}元',title ='人人帮阅读提现到账')#line:295
    def run (O0O0000OOO00O0OOO ):#line:297
        O0O0000OOO00O0OOO .msg +='='*50 +'\n'#line:298
        if O0O0000OOO00O0OOO .userinfo ():#line:299
            O0O0000OOO00O0OOO .sign ()#line:300
            O0O0000OOO00O0OOO .reward ()#line:301
            O0O0000OOO00O0OOO .getentry ()#line:302
            time .sleep (1 )#line:303
            O0O0000OOO00O0OOO .read ()#line:304
            O0O0000OOO00O0OOO .tx ()#line:305
        if not printf :#line:306
            print (O0O0000OOO00O0OOO .msg .strip ())#line:307
def yd (O0OOO00O0O0OO0O00 ):#line:310
    while not O0OOO00O0O0OO0O00 .empty ():#line:311
        O0O0O0OO000OO000O =O0OOO00O0O0OO0O00 .get ()#line:312
        OO0000O0OOOO0O0O0 =RRBYD (O0O0O0OO000OO000O )#line:313
        OO0000O0OOOO0O0O0 .run ()#line:314
def get_ver ():#line:317
    OO0OO0O0O0O000000 ='krrb V1.2.1'#line:318
    O00000OOOO0O0O0OO ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:321
    OOOO00O0O0O0OOOO0 =requests .get ('https://gitclone.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json',headers =O00000OOOO0O0O0OO ).json ()#line:323
    O00O0OOOOOO0000O0 =OO0OO0O0O0O000000 .split (' ')[1 ]#line:324
    OO0OO000OOOOO000O =OOOO00O0O0O0OOOO0 .get ('version').get (OO0OO0O0O0O000000 .split (' ')[0 ])#line:325
    OOOO00OOO0OO0O0O0 =f"当前版本 {O00O0OOOOOO0000O0}，仓库版本 {OO0OO000OOOOO000O}"#line:326
    if O00O0OOOOOO0000O0 <OO0OO000OOOOO000O :#line:327
        OOOO00OOO0OO0O0O0 +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:328
    return OOOO00OOO0OO0O0O0 #line:329
def main ():#line:332
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:333
    O00OOO0000O0OOOO0 =os .getenv ('rrbck')#line:334
    if not O00OOO0000O0OOOO0 :#line:335
        print ('请仔细阅读脚本开头的注释并配置好rrbck')#line:336
        exit ()#line:337
    try :#line:338
        O00OOO0000O0OOOO0 =ast .literal_eval (O00OOO0000O0OOOO0 )#line:339
    except :#line:340
        pass #line:341
    OOO0O0O0O0OOO0000 =Queue ()#line:342
    OO0OOOO0O0000OO00 =[]#line:343
    for O00O0O0000OO0O00O ,O000O0O00OOOO00OO in enumerate (O00OOO0000O0OOOO0 ,start =1 ):#line:344
        printlog (f'{O000O0O00OOOO00OO}\n以上是账号{O00O0O0000OO0O00O}的ck，如不正确，请检查ck填写格式')#line:345
        OOO0O0O0O0OOO0000 .put (O000O0O00OOOO00OO )#line:346
    for O00O0O0000OO0O00O in range (max_workers ):#line:347
        OO000O0000O0O0000 =threading .Thread (target =yd ,args =(OOO0O0O0O0OOO0000 ,))#line:348
        OO000O0000O0O0000 .start ()#line:349
        OO0OOOO0O0000OO00 .append (OO000O0000O0O0000 )#line:350
        time .sleep (40 )#line:351
    for O0OOO0O0O0OOO000O in OO0OOOO0O0000OO00 :#line:352
        O0OOO0O0O0OOO000O .join ()#line:353
if __name__ =='__main__':#line:356
    main ()#line:357
