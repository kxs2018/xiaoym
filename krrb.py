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
import json  # line:28
from random import randint  # line:29
import os  # line:30
import time  # line:31
import requests  # line:32
import ast  # line:33
import re  # line:34

try:  # line:36
    from lxml import etree  # line:37
except:  # line:38
    print('请仔细阅读脚本上方注释中的“no module named lxml 解决方案”')  # line:39
    exit()  # line:40
import datetime  # line:41
import threading  # line:42
from queue import Queue  # line:43

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

qwbotkey = os.getenv('qwbotkey')  # line:61
if not qwbotkey:  # line:62
    print('请仔细阅读脚本开头的注释并配置好qwbotkey')  # line:63
    exit()  # line:64


def ftime ():#line:67
    O0O0O00O0O000OO0O =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:68
    return O0O0O00O0O000OO0O #line:69
def debugger (OO0OOO0O000OO0OO0 ):#line:72
    if debug :#line:73
        print (OO0OOO0O000OO0OO0 )#line:74
def printlog (O00OO000000O0O00O ):#line:77
    if printf :#line:78
        print (O00OO000000O0O00O )#line:79
def send (O0O00O0OO00O00000 ,title ='通知',url =None ):#line:82
    if not title or not url :#line:83
        OOO000O0000OOO0O0 ={"msgtype":"text","text":{"content":f"{title}\n\n{O0O00O0OO00O00000}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:90
    else :#line:91
        OOO000O0000OOO0O0 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O0O00O0OO00O00000 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:96
    O0O0OO00O0OOO000O =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:97
    O0OOO0OOO000000OO =requests .post (O0O0OO00O0OOO000O ,data =json .dumps (OOO000O0000OOO0O0 )).json ()#line:98
    if O0OOO0OOO000000OO .get ('errcode')!=0 :#line:99
        print ('消息发送失败，请检查key和发送格式')#line:100
        return False #line:101
    return O0OOO0OOO000000OO #line:102
def getmpinfo (OO000O0OOO000OO00 ):#line:105
    if not OO000O0OOO000OO00 or OO000O0OOO000OO00 =='':#line:106
        return False #line:107
    O00OO0OO000000OOO ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:109
    O0OO00OOO00OOO00O =requests .get (OO000O0OOO000OO00 ,headers =O00OO0OO000000OOO )#line:110
    O0O0OO000OO000OOO =etree .HTML (O0OO00OOO00OOO00O .text )#line:111
    OO0O0OOO00OOO000O =O0O0OO000OO000OOO .xpath ('//meta[@*="og:title"]/@content')#line:113
    if OO0O0OOO00OOO000O :#line:114
        OO0O0OOO00OOO000O =OO0O0OOO00OOO000O [0 ]#line:115
    O0OO0O00000OO00OO =O0O0OO000OO000OOO .xpath ('//meta[@*="og:url"]/@content')#line:116
    if O0OO0O00000OO00OO :#line:117
        O0OO0O00000OO00OO =O0OO0O00000OO00OO [0 ].encode ().decode ()#line:118
    try :#line:119
        O0OO0O0O0O00O0OOO =re .findall (r'biz=(.*?)&',OO000O0OOO000OO00 )[0 ]#line:120
    except :#line:121
        O0OO0O0O0O00O0OOO =re .findall (r'biz=(.*?)&',O0OO0O00000OO00OO )[0 ]#line:122
    if not O0OO0O0O0O00O0OOO :#line:123
        return False #line:124
    O0OOO00OOO00O00OO =O0O0OO000OO000OOO .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:125
    if O0OOO00OOO00O00OO :#line:126
        O0OOO00OOO00O00OO =O0OOO00OOO00O00OO [0 ].strip ()#line:127
    O00O000OOOOO0O00O =re .findall (r"user_name.DATA'\) : '(.*?)'",O0OO00OOO00OOO00O .text )or O0O0OO000OO000OOO .xpath ('//span[@class="profile_meta_value"]/text()')#line:129
    if O00O000OOOOO0O00O :#line:130
        O00O000OOOOO0O00O =O00O000OOOOO0O00O [0 ]#line:131
    OOO000000O0O0000O =re .findall (r'createTime = \'(.*)\'',O0OO00OOO00OOO00O .text )#line:132
    if OOO000000O0O0000O :#line:133
        OOO000000O0O0000O =OOO000000O0O0000O [0 ][5 :]#line:134
    O0OOOOO00O0OO0O00 =f'{OOO000000O0O0000O} {OO0O0OOO00OOO000O}'#line:135
    O000O0O0O00OO0000 ={'biz':O0OO0O0O0O00O0OOO ,'text':O0OOOOO00O0OO0O00 }#line:136
    return O000O0O0O00OO0000 #line:137
class RRBYD :#line:140
    def __init__ (O00000O0O0OOOOOOO ,OO0OOO00000OOO00O ):#line:141
        O00000O0O0OOOOOOO .ck =OO0OOO00000OOO00O #line:142
        O00000O0O0OOOOOOO .headers ={'Host':'ebb.vinse.cn','un':O00000O0O0OOOOOOO .ck ['un'],'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue','uid':O00000O0O0OOOOOOO .ck ['uid'],'platform':'0','token':O00000O0O0OOOOOOO .ck ['token'],'Origin':'http://ebb10.twopinkone.cloud','Referer':'http://ebb10.twopinkone.cloud/',}#line:150
        O00000O0O0OOOOOOO .msg =''#line:151
    def userinfo (O0OOO00O00O0O00OO ):#line:153
        O00OO00O0O0O000OO ='http://ebb.vinse.cn/api/user/info'#line:154
        OO0OO000O000OOOO0 =requests .post (O00OO00O0O0O000OO ,headers =O0OOO00O00O0O00OO .headers ,json ={"pageSize":10 }).json ()#line:155
        debugger (f'userinfo {OO0OO000O000OOOO0}')#line:156
        if OO0OO000O000OOOO0 .get ('code')!=0 :#line:157
            O0OOO00O00O0O00OO .msg +=f'{O0OOO00O00O0O00OO.ck["un"]} cookie失效'+'\n'#line:158
            printlog (f'{O0OOO00O00O0O00OO.ck["un"]} cookie失效')#line:159
            return 0 #line:160
        O00OO00O0000OO000 =OO0OO000O000OOOO0 .get ('result')#line:161
        O0OOO00O00O0O00OO .nickname =O00OO00O0000OO000 .get ('nickName')[0 :3 ]+'****'+O00OO00O0000OO000 .get ('nickName')[-4 :]#line:162
        OO0O0O0O00OOO0O00 =O00OO00O0000OO000 .get ('integralCurrent')#line:163
        O0O0O000O000O0O00 =O00OO00O0000OO000 .get ('integralTotal')#line:164
        O0OOO00O00O0O00OO .msg +=f'用户：{O0OOO00O00O0O00OO.nickname},当前共有帮豆{OO0O0O0O00OOO0O00}，总共获得帮豆{O0O0O000O000O0O00}\n'#line:165
        printlog (f'{O0OOO00O00O0O00OO.nickname},当前共有帮豆{OO0O0O0O00OOO0O00}，总共获得帮豆{O0O0O000O000O0O00}')#line:166
        return OO0O0O0O00OOO0O00 #line:167
    def sign (OOO0O00O0O0O000OO ):#line:169
        O00OOOOO0OOOOO000 ='http://ebb.vinse.cn/api/user/sign'#line:170
        OO00O0000O00O0O00 =requests .post (O00OOOOO0OOOOO000 ,headers =OOO0O00O0O0O000OO .headers ,json ={"pageSize":10 }).json ()#line:171
        debugger (f'sign {OO00O0000O00O0O00}')#line:172
        if OO00O0000O00O0O00 .get ('code')==0 :#line:173
            OOO0O00O0O0O000OO .msg +=f'签到成功，获得帮豆{OO00O0000O00O0O00.get("result").get("point")}'+'\n'#line:174
            printlog (f'{OOO0O00O0O0O000OO.nickname}:签到成功，获得帮豆{OO00O0000O00O0O00.get("result").get("point")}')#line:175
        elif OO00O0000O00O0O00 .get ('code')==99 :#line:176
            OOO0O00O0O0O000OO .msg +=OO00O0000O00O0O00 .get ('msg')+'\n'#line:177
        else :#line:178
            OOO0O00O0O0O000OO .msg +='签到错误'+'\n'#line:179
    def reward (O0OO00000OO00OOOO ):#line:181
        OO0OO0OOO0O00O0O0 ='http://ebb.vinse.cn/api/user/receiveOneDivideReward'#line:182
        OOOOOOOO0OOO0OO00 =requests .post (OO0OO0OOO0O00O0O0 ,headers =O0OO00000OO00OOOO .headers ,json ={"pageSize":10 }).json ()#line:183
        if OOOOOOOO0OOO0OO00 .get ('code')==0 :#line:184
            O0OO00000OO00OOOO .msg +=f"领取一级帮豆：{OOOOOOOO0OOO0OO00.get('msg')}\n"#line:185
            printlog (f"{O0OO00000OO00OOOO.nickname}:领取一级帮豆：{OOOOOOOO0OOO0OO00.get('msg')}")#line:186
        OO0OO0OOO0O00O0O0 ='http://ebb.vinse.cn/api/user/receiveTwoDivideReward'#line:187
        OOOOOOOO0OOO0OO00 =requests .post (OO0OO0OOO0O00O0O0 ,headers =O0OO00000OO00OOOO .headers ,json ={"pageSize":10 }).json ()#line:188
        if OOOOOOOO0OOO0OO00 .get ('code')==0 :#line:189
            O0OO00000OO00OOOO .msg +=f"领取二级帮豆：{OOOOOOOO0OOO0OO00.get('msg')}"+'\n'#line:190
            printlog (f"{O0OO00000OO00OOOO.nickname}:领取二级帮豆：{OOOOOOOO0OOO0OO00.get('msg')}")#line:191
    def getentry (O0OOO00OO00O00OOO ):#line:193
        OO0O000OO00O00O00 ={'Host':'u.cocozx.cn',"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Origin":"http://ebb10.twopinkone.cloud","Sec-Fetch-Site":"cross-site","Sec - Fetch - Mode":"cors","Sec - Fetch - Dest":"empty"}#line:200
        O000O0O00O00000O0 =f'https://u.cocozx.cn/ipa/read/getEntryUrl?fr=ebb0726&uid={O0OOO00OO00O00OOO.ck["uid"]}'#line:201
        OOO0OOOO0OO0OOOOO =requests .get (O000O0O00O00000O0 ,headers =OO0O000OO00O00O00 ).json ()#line:202
        debugger (f'getentry {OOO0OOOO0OO0OOOOO}')#line:203
        OOOO00O000O0OO000 =OOO0OOOO0OO0OOOOO .get ('result')#line:204
        if OOO0OOOO0OO0OOOOO .get ('code')==0 :#line:205
            OO00000000OOOO0OO =OOOO00O000O0OO000 .get ('url')#line:206
            O0OOO00OO00O00OOO .entryurl =re .findall (r'(http://.*?)/',OO00000000OOOO0OO )[0 ]#line:207
        else :#line:208
            O0OOO00OO00O00OOO .msg +="阅读链接获取失败"+'\n'#line:209
            printlog (f"{O0OOO00OO00O00OOO.nickname}:阅读链接获取失败")#line:210
    def read (OOOOOOOO00OOOO000 ):#line:212
        O000OO0OO00OO0O0O ={"Origin":OOOOOOOO00OOOO000 .entryurl ,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Host":"u.cocozx.cn"}#line:217
        for O00O00O0OOOOOOO0O in range (1 ,3 ):#line:218
            OO0O0OO0O00OO0000 ={"fr":"ebb0726","uid":OOOOOOOO00OOOO000 .ck ['uid'],"group":O00O00O0OOOOOOO0O ,"un":'',"token":'',"pageSize":20 }#line:219
            O0000OO0000OOOO00 ='http://u.cocozx.cn/ipa/read/read'#line:220
            while True :#line:221
                O00O0O000O00OO0OO =requests .post (O0000OO0000OOOO00 ,headers =O000OO0OO00OO0O0O ,json =OO0O0OO0O00OO0000 )#line:222
                debugger ("read "+O00O0O000O00OO0OO .text )#line:223
                O000O00O00O0O00OO =O00O0O000O00OO0OO .json ().get ('result')#line:224
                OO0OO0O0O0OOOO0O0 =O000O00O00O0O00OO .get ('url')#line:225
                if O000O00O00O0O00OO ['status']==10 :#line:226
                    O0000000O0O0OOO00 =getmpinfo (OO0OO0O0O0OOOO0O0 )#line:227
                    if not O0000000O0O0OOO00 :#line:228
                        printlog (f'{OOOOOOOO00OOOO000.nickname}:获取文章信息失败，程序中止')#line:229
                        return False #line:230
                    OOOOOOOO00OOOO000 .msg +='-'*50 +'\n开始阅读 '+O0000000O0O0OOO00 .get ('text')+'\n'#line:231
                    printlog (f"{OOOOOOOO00OOOO000.nickname}:\n开始阅读  {O0000000O0O0OOO00.get('text')}")#line:232
                    O0OO00000OOOO000O =O0000000O0O0OOO00 .get ('biz')#line:233
                    if O0OO00000OOOO000O =='Mzg2Mzk3Mjk5NQ==':#line:234
                        OOOOOOOO00OOOO000 .msg +='正在阅读检测文章\n发送通知，暂停60秒\n'#line:235
                        printlog (f"{OOOOOOOO00OOOO000.nickname}:正在阅读检测文章\n发送通知，暂停60秒")#line:236
                        send (f'{OOOOOOOO00OOOO000.nickname}  人人帮阅读正在读检测文章',O0000000O0O0OOO00 ['text'],OO0OO0O0O0OOOO0O0 )#line:237
                        time .sleep (60 )#line:238
                    O0OO00O00O0O0O000 =randint (7 ,10 )#line:239
                    time .sleep (O0OO00O00O0O0O000 )#line:240
                    OOOOOOOO00OOOO000 .submit (O00O00O0OOOOOOO0O )#line:241
                elif O000O00O00O0O00OO ['status']==60 :#line:242
                    OOOOOOOO00OOOO000 .msg +='文章已经全部读完了\n'#line:243
                    printlog (f"{OOOOOOOO00OOOO000.nickname}:文章已经全部读完了")#line:244
                    break #line:245
                elif O000O00O00O0O00OO ['status']==30 :#line:246
                    time .sleep (2 )#line:247
                    continue #line:248
                elif O000O00O00O0O00OO ['status']==50 :#line:249
                    OOOOOOOO00OOOO000 .msg +='阅读失效\n'#line:250
                    printlog (f"{OOOOOOOO00OOOO000.nickname}:阅读失效")#line:251
                    break #line:252
                else :#line:253
                    break #line:254
            time .sleep (2 )#line:255
    def submit (OO0OO000OO0OOOO0O ,OOO0O000O0OO00OO0 ):#line:257
        OO00O0OO0O00OO0OO ='http://u.cocozx.cn/ipa/read/submit'#line:258
        O000OO0O00OO00O0O ={"Origin":OO0OO000OO0OOOO0O .entryurl ,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue","Host":"u.cocozx.cn"}#line:263
        OO0OO0000000OOO0O ={"fr":"ebb0726","uid":OO0OO000OO0OOOO0O .ck ['uid'],"group":OOO0O000O0OO00OO0 ,"un":'',"token":'',"pageSize":20 }#line:264
        O0OO0O000OO0O000O =requests .post (OO00O0OO0O00OO0OO ,headers =O000OO0O00OO00O0O ,json =OO0OO0000000OOO0O ).json ()#line:265
        debugger (f"submit {O0OO0O000OO0O000O}")#line:266
        OOOO00OO0OOO0OO00 =O0OO0O000OO0O000O .get ('result')#line:267
        OOO0O0OO0OOO000OO =OOOO00OO0OOO0OO00 .get ("dayCount")#line:268
        OO0000O0OO000OOOO =OOOO00OO0OOO0OO00 .get ("dayMax")#line:269
        OOO00000O0O000OOO =OOOO00OO0OOO0OO00 .get ("progress")#line:270
        OO0OO000OO0OOOO0O .msg +=f"今日已阅读{OOO0O0OO0OOO000OO}，本轮剩余{OOO00000O0O000OOO}，单日最高{OO0000O0OO000OOOO}\n"#line:271
        printlog (f"{OO0OO000OO0OOOO0O.nickname}:今日已阅读{OOO0O0OO0OOO000OO}，本轮剩余{OOO00000O0O000OOO}，单日最高{OO0000O0OO000OOOO}")#line:272
    def tx (O0OO0OOOOOO0OO0OO ):#line:274
        global txje #line:275
        OO0OOOO000O000OOO =O0OO0OOOOOO0OO0OO .userinfo ()#line:276
        if OO0OOOO000O000OOO <txbz :#line:277
            O0OO0OOOOOO0OO0OO .msg +='帮豆不够提现标准，明儿请早\n'#line:278
            printlog (f"{O0OO0OOOOOO0OO0OO.nickname}:帮豆不够提现标准，明儿请早")#line:279
            return #line:280
        elif 5000 <=OO0OOOO000O000OOO <10000 :#line:281
            txje =5000 #line:282
        elif 10000 <=OO0OOOO000O000OOO <50000 :#line:283
            txje =10000 #line:284
        elif 50000 <=OO0OOOO000O000OOO <100000 :#line:285
            txje =50000 #line:286
        elif OO0OOOO000O000OOO >=100000 :#line:287
            txje =100000 #line:288
        OOOOOO000O0OOO000 =f"http://ebb.vinse.cn/apiuser/aliWd"#line:289
        O00OO00OO00000O0O ={"val":txje ,"pageSize":10 }#line:290
        OOO00O0OO0OO0OO00 =requests .post (OOOOOO000O0OOO000 ,headers =O0OO0OOOOOO0OO0OO .headers ,json =O00OO00OO00000O0O ).json ()#line:291
        if OOO00O0OO0OO0OO00 .get ('code')==0 :#line:292
            send (f'{O0OO0OOOOOO0OO0OO.nickname} 人人帮提现支付宝{txje / 10000}元',title ='人人帮阅读提现到账')#line:293
    def run (O0000OO00OO0OO00O ):#line:295
        O0000OO00OO0OO00O .msg +='='*50 +'\n'#line:296
        if O0000OO00OO0OO00O .userinfo ():#line:297
            O0000OO00OO0OO00O .sign ()#line:298
            O0000OO00OO0OO00O .reward ()#line:299
            O0000OO00OO0OO00O .getentry ()#line:300
            time .sleep (1 )#line:301
            O0000OO00OO0OO00O .read ()#line:302
            O0000OO00OO0OO00O .tx ()#line:303
        if not printf :#line:304
            print (O0000OO00OO0OO00O .msg .strip ())#line:305
def yd (OO00OOO00O000OOOO ):#line:308
    while not OO00OOO00O000OOOO .empty ():#line:309
        O00O0O00O00OOO0O0 =OO00OOO00O000OOOO .get ()#line:310
        O000OO00OO0O0OO00 =RRBYD (O00O0O00O00OOO0O0 )#line:311
        O000OO00OO0O0OO00 .run ()#line:312
def get_ver ():#line:315
    O0O0O0O0OOOO00O00 ='krrb V1.2.2'#line:316
    O0O0OO0000OOOOO00 ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:319
    OO00OO0OO0OOO000O =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O0O0OO0000OOOOO00 ).json ()#line:321
    O0OO00O00OO000O0O =O0O0O0O0OOOO00O00 .split (' ')[1 ]#line:322
    O0O0OOOOOOOO00O0O =OO00OO0OO0OOO000O .get ('version').get (O0O0O0O0OOOO00O00 .split (' ')[0 ])#line:323
    O00O0000000OO0OOO =f"当前版本 {O0OO00O00OO000O0O}，仓库版本 {O0O0OOOOOOOO00O0O}"#line:324
    if O0OO00O00OO000O0O <O0O0OOOOOOOO00O0O :#line:325
        O00O0000000OO0OOO +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:326
    return O00O0000000OO0OOO #line:327
def main ():#line:330
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:331
    OOO0O000O00O0OOO0 =os .getenv ('rrbck')#line:332
    if not OOO0O000O00O0OOO0 :#line:333
        print ('请仔细阅读脚本开头的注释并配置好rrbck')#line:334
        exit ()#line:335
    try :#line:336
        OOO0O000O00O0OOO0 =ast .literal_eval (OOO0O000O00O0OOO0 )#line:337
    except :#line:338
        pass #line:339
    OO000OO00O000O0O0 =Queue ()#line:340
    O0OOOO00OO0O0OO0O =[]#line:341
    for O0000000O0O0O00OO ,O000OOOOOO0O0OOO0 in enumerate (OOO0O000O00O0OOO0 ,start =1 ):#line:342
        printlog (f'{O000OOOOOO0O0OOO0}\n以上是账号{O0000000O0O0O00OO}的ck，如不正确，请检查ck填写格式')#line:343
        OO000OO00O000O0O0 .put (O000OOOOOO0O0OOO0 )#line:344
    for O0000000O0O0O00OO in range (max_workers ):#line:345
        O0O0O0OOO0OOO00OO =threading .Thread (target =yd ,args =(OO000OO00O000O0O0 ,))#line:346
        O0O0O0OOO0OOO00OO .start ()#line:347
        O0OOOO00OO0O0OO0O .append (O0O0O0OOO0OOO00OO )#line:348
        time .sleep (40 )#line:349
    for OO0O00O0000OOOOOO in O0OOOO00OO0O0OO0O :#line:350
        OO0O00O0000OOOOOO .join ()#line:351
if __name__ =='__main__':#line:354
    main ()#line:355
