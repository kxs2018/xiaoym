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
import datetime
import threading
import ast
import json
import os
import random
import re
from queue import Queue
import requests

try:
    from lxml import etree
except:
    print('请仔细阅读脚本上方注释中的“no module named lxml 解决方案”')
    exit()
import time
from urllib.parse import urlparse, parse_qs

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
txbz = 8000  # 不低于3000，平台标准为3000
"""设置为8000，即为8毛起提"""

qwbotkey =os .getenv ('qwbotkey')#line:57
if not qwbotkey :#line:58
    print ('请仔细阅读上方注释并设置好key')#line:59
    exit ()#line:60
checklist =['MzkxNTE3MzQ4MQ==','Mzg5MjM0MDEwNw==','MzUzODY4NzE2OQ==','MzkyMjE3MzYxMg==','MzkxNjMwNDIzOA==','Mzg3NzUxMjc5Mg==','Mzg4NTcwODE1NA==','Mzk0ODIxODE4OQ==','Mzg2NjUyMjI1NA==','MzIzMDczODg4Mw==','Mzg5ODUyMzYzMQ==','MzU0NzI5Mjc4OQ==','Mzg5MDgxODAzMg==']#line:65
def ftime ():#line:68
    O00OO0000OOO000O0 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:69
    return O00OO0000OOO000O0 #line:70
def debugger (OOO0000OOOOOOOO00 ):#line:73
    if debug :#line:74
        print (OOO0000OOOOOOOO00 )#line:75
def printlog (O0OOOO0O000O000O0 ):#line:78
    if printf :#line:79
        print (O0OOOO0O000O000O0 )#line:80
def send (OO0000OOO0OOO00O0 ,title ='通知',url =None ):#line:83
    if not url :#line:84
        OOO0OOO0000O00O00 ={"msgtype":"text","text":{"content":f"{title}\n\n{OO0000OOO0OOO00O0}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:91
    else :#line:92
        OOO0OOO0000O00O00 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":OO0000OOO0OOO00O0 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:97
    O00OO000OO000OO0O =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:98
    O00OO0O000O000OOO =requests .post (O00OO000OO000OO0O ,data =json .dumps (OOO0OOO0000O00O00 )).json ()#line:99
    if O00OO0O000O000OOO .get ('errcode')!=0 :#line:100
        print ('消息发送失败，请检查key和发送格式')#line:101
        return False #line:102
    return O00OO0O000O000OOO #line:103
def getmpinfo (OOO00000O0OO00000 ):#line:106
    if not OOO00000O0OO00000 or OOO00000O0OO00000 =='':#line:107
        return False #line:108
    O0O000O00O0OO0OOO ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:110
    O0O000000O000O00O =requests .get (OOO00000O0OO00000 ,headers =O0O000O00O0OO0OOO )#line:111
    O0OO0000OO000O0OO =etree .HTML (O0O000000O000O00O .text )#line:112
    OO0OO0O0O0OO0O00O =O0OO0000OO000O0OO .xpath ('//meta[@*="og:title"]/@content')#line:114
    if OO0OO0O0O0OO0O00O :#line:115
        OO0OO0O0O0OO0O00O =OO0OO0O0O0OO0O00O [0 ]#line:116
    OOOO0OOOOO0O000O0 =O0OO0000OO000O0OO .xpath ('//meta[@*="og:url"]/@content')#line:117
    if OOOO0OOOOO0O000O0 :#line:118
        OOOO0OOOOO0O000O0 =OOOO0OOOOO0O000O0 [0 ].encode ().decode ()#line:119
    try :#line:120
        O00O0O0O0OOO0000O =re .findall (r'biz=(.*?)&',OOO00000O0OO00000 )#line:121
    except :#line:122
        O00O0O0O0OOO0000O =re .findall (r'biz=(.*?)&',OOOO0OOOOO0O000O0 )#line:123
    if O00O0O0O0OOO0000O :#line:124
        O00O0O0O0OOO0000O =O00O0O0O0OOO0000O [0 ]#line:125
    else :#line:126
        return False #line:127
    O0OO000O0OO0OO0OO =O0OO0000OO000O0OO .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:128
    if O0OO000O0OO0OO0OO :#line:129
        O0OO000O0OO0OO0OO =O0OO000O0OO0OO0OO [0 ].strip ()#line:130
    OOO0OOO00OO0OO0OO =re .findall (r"user_name.DATA'\) : '(.*?)'",O0O000000O000O00O .text )or O0OO0000OO000O0OO .xpath ('//span[@class="profile_meta_value"]/text()')#line:132
    if OOO0OOO00OO0OO0OO :#line:133
        OOO0OOO00OO0OO0OO =OOO0OOO00OO0OO0OO [0 ]#line:134
    OOOO00O0OO00OOOO0 =re .findall (r'createTime = \'(.*)\'',O0O000000O000O00O .text )#line:135
    if OOOO00O0OO00OOOO0 :#line:136
        OOOO00O0OO00OOOO0 =OOOO00O0OO00OOOO0 [0 ][5 :]#line:137
    O000OOOOO00O0O0O0 =f'{OOOO00O0OO00OOOO0}|{OO0OO0O0O0OO0O00O}|{O00O0O0O0OOO0000O}|{O0OO000O0OO0OO0OO}|{OOO0OOO00OO0OO0OO}'#line:138
    O0OOO0O0OO00000O0 ={'biz':O00O0O0O0OOO0000O ,'text':O000OOOOO00O0O0O0 }#line:139
    return O0OOO0O0OO00000O0 #line:140
def ts ():#line:143
    return str (int (time .time ()))+'000'#line:144
class XYY :#line:147
    def __init__ (OO0O00OOOOOO0O0O0 ,O0O0OOO0OO0OOO000 ):#line:148
        OO0O00OOOOOO0O0O0 .name =O0O0OOO0OO0OOO000 ['name']#line:149
        OO0O00OOOOOO0O0O0 .ysm_uid =None #line:150
        OO0O00OOOOOO0O0O0 .ysmuid =O0O0OOO0OO0OOO000 .get ('ysmuid')#line:151
        OO0O00OOOOOO0O0O0 .sec =requests .session ()#line:152
        OO0O00OOOOOO0O0O0 .sec .headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Cookie':f'ysmuid={OO0O00OOOOOO0O0O0.ysmuid};',}#line:157
        OO0O00OOOOOO0O0O0 .msg =''#line:158
    def init (OOOO0OO0O0O0O0OOO ):#line:160
        ""#line:161
        if not OOOO0OO0O0O0O0OOO .ysmuid :#line:162
            print ('ck没有ysmuid，不能运行本脚本，自动退出')#line:163
            return False #line:164
        O0OOO0OO0O00OOO0O =0 #line:165
        while O0OOO0OO0O00OOO0O <5 :#line:166
            OOO0O0OOOO0O00OO0 =OOOO0OO0O0O0O0OOO .sec .get ('http://1695480664.snak.top/').text #line:167
            OOOO0OO0O0O0O0OOO .ysm_uid =re .findall (r'unionid="(o.*?)";',OOO0O0OOOO0O00OO0 )#line:168
            if OOOO0OO0O0O0O0OOO .ysm_uid :#line:169
                OOOO0OO0O0O0O0OOO .ysm_uid =OOOO0OO0O0O0O0OOO .ysm_uid [0 ]#line:170
                O0OO0OOO0OOOOOO00 =re .findall (r'href="(.*?)">提现',OOO0O0OOOO0O00OO0 )#line:171
                if O0OO0OOO0OOOOOO00 :#line:172
                    O0OO0OOO0OOOOOO00 =O0OO0OOO0OOOOOO00 [0 ]#line:173
                    O0000O0OO000OO000 =parse_qs (urlparse (O0OO0OOO0OOOOOO00 ).query )#line:174
                    OOOO0OO0O0O0O0OOO .unionid =O0000O0OO000OO000 .get ('unionid')[0 ]#line:175
                    OOOO0OO0O0O0O0OOO .request_id =O0000O0OO000OO000 .get ('request_id')[0 ]#line:176
                    OOOO0OO0O0O0O0OOO .netloc =urlparse (O0OO0OOO0OOOOOO00 ).netloc #line:177
                else :#line:178
                    printlog (f'{OOOO0OO0O0O0O0OOO.name} 获取提现参数失败，本次不提现')#line:179
                    OOOO0OO0O0O0O0OOO .msg +=f'获取提现参数失败，本次不提现\n'#line:180
                return True #line:181
            else :#line:182
                O0OOO0OO0O00OOO0O +=1 #line:183
                continue #line:184
        printlog (f'{OOOO0OO0O0O0O0OOO.name} 获取ysm_uid失败，请检查账号有效性')#line:185
        OOOO0OO0O0O0O0OOO .msg +='获取ysm_uid失败，请检查账号有效性\n'#line:186
        return False #line:187
    def user_info (O0OOO00O00O0OOOOO ):#line:189
        OOOO00O0O0000OO0O =f'http://1695492718.snak.top/yunonline/v1/gold?unionid={O0OOO00O00O0OOOOO.ysm_uid}&time={ts()}'#line:190
        OOO0O000OOOOOOOOO =O0OOO00O00O0OOOOO .sec .get (OOOO00O0O0000OO0O ).json ()#line:191
        debugger (f'userinfo {OOO0O000OOOOOOOOO}')#line:192
        O0000000OOOOO00OO =OOO0O000OOOOOOOOO .get ("data")#line:193
        O0OOO00O00O0OOOOO .last_gold =OOO0O000OOOOOOOOO .get ("data").get ("last_gold")#line:194
        O0OO00O0O00O00OOO =O0000000OOOOO00OO .get ("remain_read")#line:195
        O0000000O0000OO0O =f'今日已经阅读了{O0000000OOOOO00OO.get("day_read")}篇文章,剩余{O0OO00O0O00O00OOO}未阅读，今日获取金币{O0000000OOOOO00OO.get("day_gold")}，剩余{O0OOO00O00O0OOOOO.last_gold}'#line:196
        printlog (f'{O0OOO00O00O0OOOOO.name}:{O0000000O0000OO0O}')#line:197
        O0OOO00O00O0OOOOO .msg +=(O0000000O0000OO0O +'\n')#line:198
        if O0OO00O0O00O00OOO ==0 :#line:199
            return False #line:200
        return True #line:201
    def getKey (OO0O0OOO00OO00000 ):#line:203
        O0OOOO00OO000OO0O ='http://1695492718.snak.top/yunonline/v1/wtmpdomain'#line:204
        O000OOO0OO0OOO0OO =f'unionid={OO0O0OOO00OO00000.ysm_uid}'#line:205
        OO0O000O0O00OOOO0 =OO0O0OOO00OO00000 .sec .post (O0OOOO00OO000OO0O ,data =O000OOO0OO0OOO0OO ).json ()#line:206
        debugger (f'getkey {OO0O000O0O00OOOO0}')#line:207
        OOOO00O0O0OO0000O =OO0O000O0O00OOOO0 .get ('data').get ('domain')#line:208
        OO0O0OOO00OO00000 .uk =parse_qs (urlparse (OOOO00O0O0OO0000O ).query ).get ('uk')[0 ]#line:209
        O0000OOOOOOO00OO0 =urlparse (OOOO00O0O0OO0000O ).netloc #line:210
        OO0O0OOO00OO00000 .headers ={'Connection':'keep-alive','Accept':'application/json, text/javascript, */*; q=0.01','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue','Origin':f'https://{O0000OOOOOOO00OO0}','Sec-Fetch-Site':'cross-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh',}#line:221
    def read (OO0O00OOO0O00O00O ):#line:223
        time .sleep (3 )#line:224
        OO0O0O0O0OOOOOO00 ={'uk':OO0O00OOO0O00O00O .uk }#line:225
        OOO00OOO0O0O0O0O0 =0 #line:226
        while True :#line:227
            OO0O00O000000O0O0 =f'https://nsr.zsf2023e458.cloud/yunonline/v1/do_read'#line:228
            OOO00000O0O00O00O =requests .get (OO0O00O000000O0O0 ,headers =OO0O00OOO0O00O00O .headers ,params =OO0O0O0O0OOOOOO00 )#line:229
            OO0O00OOO0O00O00O .msg +=('-'*50 +'\n')#line:230
            debugger (f'read1 {OOO00000O0O00O00O.text}')#line:231
            OOO00000O0O00O00O =OOO00000O0O00O00O .json ()#line:232
            if OOO00000O0O00O00O .get ('errcode')==0 :#line:233
                O0OO00OOOO00O0O00 =OOO00000O0O00O00O .get ('data').get ('link')#line:234
                OO0O00O0OO0O0OOO0 =OO0O00OOO0O00O00O .jump (O0OO00OOOO00O0O00 )#line:235
                if 'mp.weixin'in OO0O00O0OO0O0OOO0 :#line:236
                    OO00OO0O00OOO0OOO =getmpinfo (OO0O00O0OO0O0OOO0 )#line:237
                    if not OO00OO0O00OOO0OOO :#line:238
                        OOO00OOO0O0O0O0O0 +=1 #line:239
                        if OOO00OOO0O0O0O0O0 ==2 :#line:240
                            printlog (f'{OO0O00OOO0O00O00O.name}:获取文章信息失败已达3次，程序中止')#line:241
                            break #line:242
                        time .sleep (5 )#line:243
                        continue #line:244
                    O0OO00O0O00O0OOOO =OO00OO0O00OOO0OOO ['biz']#line:245
                    OO0O00OOO0O00O00O .msg +=('开始阅读 '+OO00OO0O00OOO0OOO ['text']+'\n')#line:246
                    printlog (f'{OO0O00OOO0O00O00O.name}:开始阅读 '+OO00OO0O00OOO0OOO ['text'])#line:247
                    if O0OO00O0O00O0OOOO in checklist :#line:248
                        send (f"{OO00OO0O00OOO0OOO['text']}",title =f'{OO0O00OOO0O00O00O.name} 小阅阅阅读过检测',url =OO0O00O0OO0O0OOO0 )#line:249
                        OO0O00OOO0O00O00O .msg +='遇到检测文章，已发送到微信，手动阅读，暂停60秒\n'#line:250
                        printlog (f'{OO0O00OOO0O00O00O.name}:遇到检测文章，已发送到微信，手动阅读，暂停60秒')#line:251
                        time .sleep (60 )#line:252
                else :#line:253
                    OO0O00OOO0O00O00O .msg +=f'{OO0O00OOO0O00O00O.name} 小阅阅跳转到 {OO0O00O0OO0O0OOO0}\n'#line:254
                    printlog (f'{OO0O00OOO0O00O00O.name}: 小阅阅跳转到 {OO0O00O0OO0O0OOO0}')#line:255
                    continue #line:256
                O0000O0000000O000 =random .randint (7 ,10 )#line:257
                OO0O00OOO0O00O00O .msg +=f'本次模拟读{O0000O0000000O000}秒\n'#line:258
                time .sleep (O0000O0000000O000 )#line:259
                OO0O00O000000O0O0 =f'https://nsr.zsf2023e458.cloud/yunonline/v1/get_read_gold?uk={OO0O00OOO0O00O00O.uk}&time={O0000O0000000O000}&timestamp={ts()}'#line:260
                requests .get (OO0O00O000000O0O0 ,headers =OO0O00OOO0O00O00O .headers )#line:261
            elif OOO00000O0O00O00O .get ('errcode')==405 :#line:262
                printlog (f'{OO0O00OOO0O00O00O.name}:阅读重复')#line:263
                OO0O00OOO0O00O00O .msg +='阅读重复\n'#line:264
                time .sleep (1.5 )#line:265
            elif OOO00000O0O00O00O .get ('errcode')==407 :#line:266
                printlog (f'{OO0O00OOO0O00O00O.name}:{OOO00000O0O00O00O.get("msg")}')#line:267
                OO0O00OOO0O00O00O .msg +=(OOO00000O0O00O00O .get ('msg')+'\n')#line:268
                return True #line:269
            else :#line:270
                printlog (f'{OO0O00OOO0O00O00O.name}:{OOO00000O0O00O00O.get("msg")}')#line:271
                OO0O00OOO0O00O00O .msg +=(OOO00000O0O00O00O .get ("msg")+'\n')#line:272
                time .sleep (1.5 )#line:273
    def jump (O0OOO00O0O000OOO0 ,O0O0O00000OOOOO00 ):#line:275
        OOO00OOO000O00OO0 =urlparse (O0O0O00000OOOOO00 ).netloc #line:276
        OOOOO0OO000OOOO00 ={'Host':OOO00OOO000O00OO0 ,'Connection':'keep-alive','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh','Cookie':f'ysmuid={O0OOO00O0O000OOO0.ysmuid}',}#line:286
        OOOO0OO0O0000OO0O =requests .get (O0O0O00000OOOOO00 ,headers =OOOOO0OO000OOOO00 ,allow_redirects =False )#line:287
        OO000O00OO00O00OO =OOOO0OO0O0000OO0O .headers .get ('Location')#line:288
        return OO000O00OO00O00OO #line:289
    def withdraw (O0O00OOO000O0OOO0 ):#line:291
        if not O0O00OOO000O0OOO0 .unionid :#line:292
            return False #line:293
        if int (O0O00OOO000O0OOO0 .last_gold )<txbz :#line:294
            printlog (f'{O0O00OOO000O0OOO0.name} 没有达到你设置的提现标准{txbz}')#line:295
            O0O00OOO000O0OOO0 .msg +=f'没有达到你设置的提现标准{txbz}\n'#line:296
            return False #line:297
        O00OO0OOOOO000OOO =int (int (O0O00OOO000O0OOO0 .last_gold )/1000 )*1000 #line:298
        O0O00OOO000O0OOO0 .msg +=f'本次提现金币{O00OO0OOOOO000OOO}\n'#line:299
        printlog (f'{O0O00OOO000O0OOO0.name}:本次提现金币{O00OO0OOOOO000OOO}')#line:300
        if O00OO0OOOOO000OOO :#line:302
            O000OO000O0O0OOO0 =f'http://{O0O00OOO000O0OOO0.netloc}/yunonline/v1/user_gold'#line:303
            printlog (O000OO000O0O0OOO0 )#line:304
            OO00OO0OOO0O000OO =f'unionid={O0O00OOO000O0OOO0.unionid}&request_id={O0O00OOO000O0OOO0.request_id}&gold={O00OO0OOOOO000OOO}'#line:305
            OOOO0OOO00OOO0OOO =O0O00OOO000O0OOO0 .sec .post (O000OO000O0O0OOO0 ,data =OO00OO0OOO0O000OO )#line:306
            debugger (f'gold {OOOO0OOO00OOO0OOO.text}')#line:307
            O000OO000O0O0OOO0 =f'http://{O0O00OOO000O0OOO0.netloc}/yunonline/v1/withdraw'#line:308
            OO00OO0OOO0O000OO =f'unionid={O0O00OOO000O0OOO0.unionid}&signid={O0O00OOO000O0OOO0.request_id}&ua=0&ptype=0&paccount=&pname='#line:309
            OOOO0OOO00OOO0OOO =O0O00OOO000O0OOO0 .sec .post (O000OO000O0O0OOO0 ,data =OO00OO0OOO0O000OO )#line:310
            debugger (f'withdraw {OOOO0OOO00OOO0OOO.text}')#line:311
            O0O00OOO000O0OOO0 .msg +=f"提现结果 {OOOO0OOO00OOO0OOO.json()['msg']}"#line:312
            printlog (f'{O0O00OOO000O0OOO0.name}:提现结果 {OOOO0OOO00OOO0OOO.json()["msg"]}')#line:313
    def run (O00O000O000OOOOO0 ):#line:315
        O00O000O000OOOOO0 .msg +=('='*50 +f'\n账号：{O00O000O000OOOOO0.name}开始任务\n')#line:316
        printlog (f'账号：{O00O000O000OOOOO0.name}开始任务')#line:317
        if not O00O000O000OOOOO0 .init ():#line:318
            return False #line:319
        if O00O000O000OOOOO0 .user_info ():#line:320
            O00O000O000OOOOO0 .getKey ()#line:321
            O00O000O000OOOOO0 .read ()#line:322
            O00O000O000OOOOO0 .user_info ()#line:323
            time .sleep (0.5 )#line:324
        O00O000O000OOOOO0 .withdraw ()#line:325
        printlog (f'账号：{O00O000O000OOOOO0.name} 本轮任务结束')#line:326
        if not printf :#line:327
            print (O00O000O000OOOOO0 .msg )#line:328
def yd (O0O0000O00O0O00O0 ):#line:331
    while not O0O0000O00O0O00O0 .empty ():#line:332
        OO00OO0O00OOOOOO0 =O0O0000O00O0O00O0 .get ()#line:333
        O00OOO00OOOOOO0O0 =XYY (OO00OO0O00OOOOOO0 )#line:334
        O00OOO00OOOOOO0O0 .run ()#line:335
def get_ver ():#line:338
    O00000O00O000O0O0 ='kxyyV2 V2.2'#line:339
    O0O0OOOO0000O0O00 ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:342
    O00OO0OO0O00000OO =requests .get ('https://ghproxy.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json',headers =O0O0OOOO0000O0O00 ).json ()#line:344
    OOO00OOOO0OO0O00O =O00000O00O000O0O0 .split (' ')[1 ]#line:345
    O000OO00OOO00O0OO =O00OO0OO0O00000OO .get ('version').get (O00000O00O000O0O0 .split (' ')[0 ])#line:346
    OOO0OO0O000OO0000 =f"当前版本 {OOO00OOOO0OO0O00O}，仓库版本 {O000OO00OOO00O0OO}"#line:347
    if OOO00OOOO0OO0O00O <O000OO00OOO00O0OO :#line:348
        OOO0OO0O000OO0000 +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:349
    return OOO0OO0O000OO0000 #line:350
def main ():#line:353
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:354
    OOO00000OO00OO000 =os .getenv ('xyyck')#line:355
    if not OOO00000OO00OO000 :#line:356
        print ('请仔细阅读脚本上方注释并设置好ck')#line:357
        exit ()#line:358
    try :#line:359
        OOO00000OO00OO000 =ast .literal_eval (OOO00000OO00OO000 )#line:360
    except :#line:361
        pass #line:362
    O0OO0OO00O0OO0OO0 =[]#line:363
    OO0O0O000OO0000O0 =Queue ()#line:364
    for O0OO0000O00O00OO0 ,O00O0O00OOOOO00O0 in enumerate (OOO00000OO00OO000 ,start =1 ):#line:365
        printlog (f'{O00O0O00OOOOO00O0}\n以上是第{O0OO0000O00O00OO0}个账号的ck，如不正确，请检查ck填写格式')#line:366
        OO0O0O000OO0000O0 .put (O00O0O00OOOOO00O0 )#line:367
    for O0OO0000O00O00OO0 in range (max_workers ):#line:368
        O00OOOOO0O0OOO000 =threading .Thread (target =yd ,args =(OO0O0O000OO0000O0 ,))#line:369
        O00OOOOO0O0OOO000 .start ()#line:370
        O0OO0OO00O0OO0OO0 .append (O00OOOOO0O0OOO000 )#line:371
        time .sleep (30 )#line:372
    for O0000O0OO0O0OO000 in O0OO0OO00O0OO0OO0 :#line:373
        O0000O0OO0O0OO000 .join ()#line:374
if __name__ =='__main__':#line:377
    main ()#line:378
