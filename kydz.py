# -*- coding: utf-8 -*-
# kydz
# Author: kk
# date：2023/9/27
"""
仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
入口：http://5851278349.buemxve.cn/?jgwq=3340348&goid=itrb
http://5851278349.buemxve.cn/?jgwq=3340348&goid=itrb 抓包这个链接 抓出唯一一个cookie 把7bfe3c8f4d51851的值
或者http://wxr.jjyii.com/user/getinfo?v=3 a_h_n值/后面的字符串 填入ck
建议手动阅读几篇再使用脚本！！！
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
export ydzck="[{'name':'xxx','ck':'xxx'},{'name':'xxx','ck':'xxx'}]"
===============================================================
no module named lxml 解决方案
1. 配置文件搜索 PipMirror，如果网址包含douban的，请改为下方的网址
PipMirror="https://pypi.tuna.tsinghua.edu.cn/simple"
2. 依赖管理-python 添加 lxml
3. 如果装不上，①请ssh连接到服务器 ②docker exec -it ql bash (ql是青龙容器的名字，docker ps可查询) ③pip install pip -U
===============================================================
"""
import threading
import ast
import hashlib
import json
import os
import random
import re
import time
from queue import Queue
import requests
import datetime
from lxml import etree
from urllib.parse import unquote, urlparse, parse_qs

"""实时日志开关"""
printf = 1
"""1为开，0为关"""

"""debug模式开关"""
debug = 0
"""1为开，打印调试日志；0为关，不打印"""

"""线程数量设置"""
max_workers = 3
"""设置为5，即最多有5个任务同时进行"""

"""设置提现标准"""
txbz = 5000  # 不低于3000，平台标准为3000
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
pushable = 0  # 开启后必须设置pushconfig才能运行
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


checklist =['MzI0MjE5MTc0OA==','MzU2OTczNzcwNg==','Mzg5NjcyMzgyOA==','MjM5MTA5ODYzNQ==','MzI0MjY0NTY3Ng==','MzIzNjgyOTE1Ng==','MzA3MTI5NDc5Mw==','MzU5OTgwOTQ1NQ==','MzA3NDM1OTExMQ==','MzI3MTA5MTkwNQ==','Mzg2MTI0Mzc1Nw==','MzIxNTcyODI5OA==','MzAwNzA3MDAzMw==','MzI2MjA0MzEwNA==','MzIxNjA4NDg4NA==','MzA3MzczODIzNg==','MzI1MDAwNDY1NA==','Mzg5NzA2Nzc2MA==','MzU5NzgwMTgwMQ==','MjM5Mjc5NjMyMw==','MzU5NTczMzA0MQ==','Mzg3MjA3OTgwNQ==','MzU1ODI4MjI4Nw==','MzA5MDIzODA0NQ==','MzkzMjUyNTk1OA==','Mzg4OTA1MzI0Ng==','MzIzNzU4NzE5NQ==','MjM5MTk3NTQyOQ==','MjM5NjY4Mzk5OQ==','MzUyMzk1MTAyNg==','MzUwOTk5NDI0MQ==','Mzg2NjExNDI2Mw==','MzAxMjE1MTYyMQ==','MzIxNjEzMDg2OQ==','MzkxMDI2NTgwMw==','MzI4NDY5MjkwNA==']#line:97
def ftime ():#line:100
    O00OOOO0O0OO000O0 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:101
    return O00OOOO0O0OO000O0 #line:102
def debugger (O0O0OO0OOO0O00OO0 ):#line:105
    if debug :#line:106
        print (O0O0OO0OOO0O00OO0 )#line:107
def printlog (OO0OOO00O000OO0OO ):#line:110
    if printf :#line:111
        print (OO0OOO00O000OO0OO )#line:112
def send (O0O0OO0OOO0O0OOO0 ,title ='通知',url =None ):#line:115
    if not url :#line:116
        O0O00000OO0OOO0O0 ={"msgtype":"text","text":{"content":f"{title}\n\n{O0O0OO0OOO0O0OOO0}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:123
    else :#line:124
        O0O00000OO0OOO0O0 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O0O0OO0OOO0O0OOO0 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:129
    O00OO0O00OOOOOO0O =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:130
    O00O0000O00O00OOO =requests .post (O00OO0O00OOOOOO0O ,data =json .dumps (O0O00000OO0OOO0O0 )).json ()#line:131
    if O00O0000O00O00OOO .get ('errcode')!=0 :#line:132
        print ('消息发送失败，请检查key和发送格式')#line:133
        return False #line:134
    return O00O0000O00O00OOO #line:135
def push (O0OO0O0OOOO0O0OO0 ,O0000O0O0OO0O0OO0 ,OO00OOOOO0OO0O0OO ,uid =None ):#line:138
    if uid :#line:139
        uids .append (uid )#line:140
    OO0OO0OOOO0OO0O0O ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',O0OO0O0OOOO0O0OO0 ).replace ('url',OO00OOOOO0OO0O0OO )#line:142
    OOOO000O0OOOO00O0 ={"appToken":appToken ,"content":OO0OO0OOOO0OO0O0O ,"summary":O0000O0O0OO0O0OO0 ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":OO00OOOOO0OO0O0OO ,"verifyPay":False }#line:152
    O00OOO0OO000O0O00 ='http://wxpusher.zjiecode.com/api/send/message'#line:153
    OOOO0O00O0O0O00OO =requests .post (url =O00OOO0OO000O0O00 ,json =OOOO000O0OOOO00O0 ).json ()#line:154
    if OOOO0O00O0O0O00OO .get ('code')!=1000 :#line:155
        print (OOOO0O00O0O0O00OO .get ('msg'),OOOO0O00O0O0O00OO )#line:156
    return OOOO0O00O0O0O00OO #line:157
def getmpinfo (OO0O0OOOOOOO0O0O0 ):#line:160
    if not OO0O0OOOOOOO0O0O0 or OO0O0OOOOOOO0O0O0 =='':#line:161
        return False #line:162
    OOOOO00000O00OO00 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:164
    OO00OO0O0OO0OO0OO =requests .get (OO0O0OOOOOOO0O0O0 ,headers =OOOOO00000O00OO00 )#line:165
    OO0OOO0O000O00O00 =etree .HTML (OO00OO0O0OO0OO0OO .text )#line:166
    OO00OO0O00OOO0000 =OO0OOO0O000O00O00 .xpath ('//meta[@*="og:title"]/@content')#line:167
    if OO00OO0O00OOO0000 :#line:168
        OO00OO0O00OOO0000 =OO00OO0O00OOO0000 [0 ]#line:169
    OOO000O0O0OOOOOOO =OO0OOO0O000O00O00 .xpath ('//meta[@*="og:url"]/@content')#line:170
    if OOO000O0O0OOOOOOO :#line:171
        OOO000O0O0OOOOOOO =OOO000O0O0OOOOOOO [0 ].encode ().decode ()#line:172
    try :#line:173
        OO0OO00000O00OOOO =re .findall (r'biz=(.*?)&',OO0O0OOOOOOO0O0O0 )#line:174
    except :#line:175
        OO0OO00000O00OOOO =re .findall (r'biz=(.*?)&',OOO000O0O0OOOOOOO )#line:176
    if OO0OO00000O00OOOO :#line:177
        OO0OO00000O00OOOO =OO0OO00000O00OOOO [0 ]#line:178
    else :#line:179
        return False #line:180
    O00OO0O0O000O0OOO =OO0OOO0O000O00O00 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:181
    if O00OO0O0O000O0OOO :#line:182
        O00OO0O0O000O0OOO =O00OO0O0O000O0OOO [0 ].strip ()#line:183
    O000O00000O0OOOOO =re .findall (r"user_name.DATA'\) : '(.*?)'",OO00OO0O0OO0OO0OO .text )or OO0OOO0O000O00O00 .xpath ('//span[@class="profile_meta_value"]/text()')#line:185
    if O000O00000O0OOOOO :#line:186
        O000O00000O0OOOOO =O000O00000O0OOOOO [0 ]#line:187
    O00OO0O000O00OOOO =re .findall (r'createTime = \'(.*)\'',OO00OO0O0OO0OO0OO .text )#line:188
    if O00OO0O000O00OOOO :#line:189
        O00OO0O000O00OOOO =O00OO0O000O00OOOO [0 ][5 :]#line:190
    O0OO0OO0000O00O0O =f'{O00OO0O000O00OOOO}|{OO00OO0O00OOO0000}|{OO0OO00000O00OOOO}|{O00OO0O0O000O0OOO}|{O000O00000O0OOOOO}'#line:191
    OO0O00OOO0O0OO00O ={'biz':OO0OO00000O00OOOO ,'text':O0OO0OO0000O00O0O }#line:192
    return OO0O00OOO0O0OO00O #line:193
class YDZ :#line:196
    def __init__ (O0OOOOOO0OO00000O ,O000O00OO0O00OOO0 ):#line:197
        O0OOOOOO0OO00000O .uid =O000O00OO0O00OOO0 .get ('uid')#line:198
        O0OOOOOO0OO00000O .name =O000O00OO0O00OOO0 .get ('name')#line:199
        O0OOOOOO0OO00000O .s =requests .session ()#line:200
        O0OOOOOO0OO00000O .ck =O000O00OO0O00OOO0 .get ('ck')#line:201
        O0OOOOOO0OO00000O .msg =''#line:202
        O0OOOOOO0OO00000O .s .headers ={'Proxy-Connection':'keep-alive','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5279 MMWEBSDK/20230805 MMWEBID/2833 MicroMessenger/8.0.42.2460(0x28002A35) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9','a_h_n':f'http%3A%2F%2F5851583901.uzwxeze.cn%2F%3Fjgwq%3D3340348%26goid%3Ditrb/{O0OOOOOO0OO00000O.ck}','cookie':f'7bfe3c8f4d51851={O0OOOOOO0OO00000O.ck}'}#line:209
    def init (OO0O00OOOOO00O000 ):#line:211
        try :#line:212
            OO000OO0O0OO000OO ='http://5851583901.uzwxeze.cn/?jgwq=3340348&goid=itrb'#line:213
            O0OOOOOO000OO00O0 =OO0O00OOOOO00O000 .s .get (OO000OO0O0OO000OO ).text #line:214
            O0OOOOOO000OO00O0 =re .sub ('\s','',O0OOOOOO000OO00O0 )#line:216
            OO0O00OOOOO00O000 .nickname =re .findall (r'nname=\'(.*?)\',',O0OOOOOO000OO00O0 )[0 ]#line:217
            O0OOO0000OOOO000O =re .findall (r'uid=\'(\d+)\'',O0OOOOOO000OO00O0 )[0 ]#line:218
            O0O00OO000000OOO0 =f'http://58515{random.randint(10000, 99999)}.uzwxeze.cn/?jgwq={O0OOO0000OOOO000O}&goid=itrb/{OO0O00OOOOO00O000.ck}'#line:219
            OO0O00OOOOO00O000 .s .headers .update ({'a_h_n':O0O00OO000000OOO0 })#line:220
            return True #line:221
        except :#line:222
            printlog (f'{OO0O00OOOOO00O000.name} 账号信息获取错误，请检查ck有效性')#line:223
            OO0O00OOOOO00O000 .msg +='账号信息获取错误，请检查ck有效性\n'#line:224
            return False #line:225
    def getinfo (OO0000OOO00000OO0 ):#line:227
        O00OO00O0OO0O0OOO ='http://wxr.jjyii.com/user/getinfo?v=3'#line:228
        O0OOO00O0OO0OO00O =OO0000OOO00000OO0 .s .get (O00OO00O0OO0O0OOO ).json ()#line:229
        debugger (f'getinfo2 {O0OOO00O0OO0OO00O}')#line:230
        OO00000O00OO0O0O0 =O0OOO00O0OO0OO00O .get ('data')#line:231
        OO0000OOO00000OO0 .count =OO00000O00OO0O0O0 .get ('count')#line:232
        OO0000OOO00000OO0 .gold =OO00000O00OO0O0O0 .get ('balance')#line:233
        OO0O0OO0000O0OO0O =OO00000O00OO0O0O0 .get ('hm')#line:234
        O00OOO0O00OOOO0O0 =OO00000O00OO0O0O0 .get ('hs')#line:235
        printlog (f'账号:{OO0000OOO00000OO0.nickname},当前金币{OO0000OOO00000OO0.gold}，今日已读{OO0000OOO00000OO0.count}')#line:236
        OO0000OOO00000OO0 .msg +=f'账号:{OO0000OOO00000OO0.nickname},当前金币{OO0000OOO00000OO0.gold}，今日已读{OO0000OOO00000OO0.count}\n'#line:237
        if OO0O0OO0000O0OO0O !=0 or O00OOO0O00OOOO0O0 !=0 :#line:238
            printlog (f'{OO0000OOO00000OO0.nickname} 本轮次已结束，{OO0O0OO0000O0OO0O}分钟后可继续任务')#line:239
            OO0000OOO00000OO0 .msg +='本轮次已结束，{hm}分钟后可继续任务\n'#line:240
            return False #line:241
        return True #line:242
    def read (O0O000OO00O000OOO ):#line:244
        O0OO00O0O0OOO0OOO =random .randint (10000 ,99999 )#line:245
        OO0OO0OO000O0OO0O =f'http://58517{O0OO00O0O0OOO0OOO}.fgloceb.cn/?a=gt&goid=itrb&_v=3890/{O0O000OO00O000OOO.ck}'#line:246
        OO0OOOOOO000O0000 ='http://wxr.jjyii.com/r/get?v=10'#line:247
        O00000OO0OOOOOOOO ={'o':f'http://58517{O0OO00O0O0OOO0OOO}.ulzqwjf.cn/?a=gt&goid=itrb&_v=3890','t':'quick'}#line:249
        OOO0OOOO0O0O0O0O0 =0 #line:250
        OOOOOOOO0000OOO0O =0 #line:251
        while OOO0OOOO0O0O0O0O0 <30 and OOOOOOOO0000OOO0O <5 :#line:252
            if not O0O000OO00O000OOO .getinfo ():#line:253
                break #line:254
            OOOO0O0O00O0O000O =O0O000OO00O000OOO .s .post (OO0OOOOOO000O0000 ,data =O00000OO0OOOOOOOO ).json ()#line:255
            debugger (f'read {OOOO0O0O00O0O000O}')#line:256
            OOOO00000OO00OOOO =OOOO0O0O00O0O000O .get ('data').get ('url')#line:257
            if OOOO0O0O00O0O000O .get ('data').get ('uiv'):#line:258
                printlog (f'{O0O000OO00O000OOO.nickname} 号已黑，明天继续')#line:259
                O0O000OO00O000OOO .msg +=f'号已黑，明天继续\n'#line:260
                break #line:261
            if not OOOO00000OO00OOOO :#line:262
                printlog (f'{O0O000OO00O000OOO.nickname} 没有获取到阅读链接，正在重试')#line:263
                O0O000OO00O000OOO .msg +='没有获取到阅读链接，正在重试\n'#line:264
                time .sleep (5 )#line:265
                OOOOOOOO0000OOO0O +=1 #line:266
                continue #line:267
            OO0OOO0000000OO00 =getmpinfo (OOOO00000OO00OOOO )#line:268
            try :#line:269
                printlog (f'{O0O000OO00O000OOO.nickname} 正在阅读 {OO0OOO0000000OO00["text"]}')#line:270
                O0O000OO00O000OOO .msg +=f'正在阅读 {OO0OOO0000000OO00["text"]}\n'#line:271
            except :#line:272
                printlog (f'{O0O000OO00O000OOO.nickname} 正在阅读 {OO0OOO0000000OO00["biz"]}')#line:273
                O0O000OO00O000OOO .msg +=f'正在阅读 {OO0OOO0000000OO00["biz"]}\n'#line:274
            if 'chksm'in OOOO00000OO00OOOO or (OO0OOO0000000OO00 ["biz"]in checklist )or O0O000OO00O000OOO .count %30 ==0 or O0O000OO00O000OOO .count ==1 :#line:275
                printlog (f'{O0O000OO00O000OOO.nickname} 正在阅读检测文章，发送通知，暂停60秒')#line:276
                O0O000OO00O000OOO .msg +='正在阅读检测文章，发送通知，暂停60秒\n'#line:277
                if sendable :#line:278
                    send (f'{O0O000OO00O000OOO.nickname}\n点击阅读检测文章',f'{O0O000OO00O000OOO.name} 阅读赚过检测',OOOO00000OO00OOOO )#line:279
                if pushable :#line:280
                    push (f'{O0O000OO00O000OOO.nickname}\n点击阅读检测文章\n{OO0OOO0000000OO00["text"]}',f'{O0O000OO00O000OOO.name} 阅读赚过检测',OOOO00000OO00OOOO ,O0O000OO00O000OOO .uid )#line:282
                time .sleep (60 )#line:283
            O0OO00O0O0OOO0OOO =random .randint (7 ,10 )#line:284
            O0O000OO00O000OOO .msg +=f'模拟阅读{O0OO00O0O0OOO0OOO}秒\n'#line:285
            time .sleep (O0OO00O0O0OOO0OOO )#line:286
            O0OOO00O0OOOOOO00 ='http://wxr.jjyii.com/r/ck'#line:287
            O0000000000OOO00O ={'Accept':'application/json, text/javascript, */*; q=0.01','Origin':'http://5851780833.ebrmrwy.cn','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',}#line:290
            O0O000OO00O000OOO .s .headers .update (O0000000000OOO00O )#line:291
            OOOO0O0O00O0O000O =O0O000OO00O000OOO .s .post (O0OOO00O0OOOOOO00 ,data ={'t':'quick'}).json ()#line:292
            debugger (f'check {OOOO0O0O00O0O000O}')#line:293
            OO0O0O00OO0OO0000 =OOOO0O0O00O0O000O .get ('data').get ('gold')#line:294
            if OO0O0O00OO0OO0000 :#line:295
                printlog (f'{O0O000OO00O000OOO.nickname} 阅读成功，获得金币{OO0O0O00OO0OO0000}')#line:296
                O0O000OO00O000OOO .msg +=f'阅读成功，获得金币{OO0O0O00OO0OO0000}\n'#line:297
            OOO0OOOO0O0O0O0O0 +=1 #line:298
    def cash (OO0OOOOOOO0O00O0O ):#line:300
        if OO0OOOOOOO0O00O0O .gold <txbz :#line:301
            printlog (f'{OO0OOOOOOO0O00O0O.nickname} 你的金币不多了')#line:302
            OO0OOOOOOO0O00O0O .msg +='你的金币不多了\n'#line:303
            return False #line:304
        OOOOOOO000O000OO0 =int (OO0OOOOOOO0O00O0O .gold /1000 )*1000 #line:305
        printlog (f'{OO0OOOOOOO0O00O0O.nickname} 本次提现：{OOOOOOO000O000OO0}')#line:306
        OO0OOOOOOO0O00O0O .msg +=f'本次提现：{OOOOOOO000O000OO0}\n'#line:307
        O00000OOOO00O00O0 ='http://wxr.jjyii.com/mine/cash'#line:308
        O0O0O000OO00O0000 =OO0OOOOOOO0O00O0O .s .post (O00000OOOO00O00O0 )#line:309
        if O0O0O000OO00O0000 .json ().get ('code')==1 :#line:310
            printlog (f'{OO0OOOOOOO0O00O0O.nickname} 提现成功')#line:311
            OO0OOOOOOO0O00O0O .msg +='提现成功\n'#line:312
        else :#line:313
            debugger (O0O0O000OO00O0000 .text )#line:314
            printlog (f'{OO0OOOOOOO0O00O0O.nickname} 提现失败')#line:315
            OO0OOOOOOO0O00O0O .msg +='提现失败\n'#line:316
    def run (O0OOOOO000O0OOOOO ):#line:318
        if O0OOOOO000O0OOOOO .init ():#line:319
            O0OOOOO000O0OOOOO .read ()#line:320
        O0OOOOO000O0OOOOO .cash ()#line:321
        if not printf :#line:322
            print (O0OOOOO000O0OOOOO .msg )#line:323
def yd (O0OOOO0000OOOO0OO ):#line:326
    while not O0OOOO0000OOOO0OO .empty ():#line:327
        OOOO00OO0O000OOOO =O0OOOO0000OOOO0OO .get ()#line:328
        O0O00OOO0OO0O00O0 =YDZ (OOOO00OO0O000OOOO )#line:329
        O0O00OOO0OO0O00O0 .run ()#line:330
def get_ver ():#line:333
    O0O0O000O000OOOOO ='kydz V0.2.0'#line:334
    OOOOOO00OOOO0O00O ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:337
    O00000O00OOO00OO0 =requests .get ('https://ghproxy.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json',headers =OOOOOO00OOOO0O00O ).json ()#line:339
    O00OOOO000O000O00 =O0O0O000O000OOOOO .split (' ')[1 ]#line:340
    O0OO000OOOO0OOO0O =O00000O00OOO00OO0 .get ('version').get (O0O0O000O000OOOOO .split (' ')[0 ])#line:341
    OOO00000OOO00OO0O =f"当前版本 {O00OOOO000O000O00}，仓库版本 {O0OO000OOOO0OOO0O}"#line:342
    if O00OOOO000O000O00 <O0OO000OOOO0OOO0O :#line:343
        OOO00000OOO00OO0O +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:344
    return OOO00000OOO00OO0O #line:345
def main ():#line:348
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:349
    OO0O000000OO0OOO0 =os .getenv ('ydzck')#line:350
    if not OO0O000000OO0OOO0 :#line:351
        print ('仔细阅读脚本上方注释，配置好ydzck')#line:352
        return False #line:353
    try :#line:354
        OO0O000000OO0OOO0 =ast .literal_eval (OO0O000000OO0OOO0 )#line:355
    except :#line:356
        pass #line:357
    OO0O0OOOOO00000OO =[]#line:358
    OO000OO0OOO00000O =Queue ()#line:359
    for O0O0O0OOOO00O00O0 ,OO00O0OOO00000O0O in enumerate (OO0O000000OO0OOO0 ):#line:360
        printlog (f'{OO00O0OOO00000O0O}\n以上是账号{O0O0O0OOOO00O00O0}的ck，请核对是否正确，如不正确，请检查ck填写格式')#line:361
        OO000OO0OOO00000O .put (OO00O0OOO00000O0O )#line:362
    for O0O0O0OOOO00O00O0 in range (max_workers ):#line:363
        OOO00O0000000O000 =threading .Thread (target =yd ,args =(OO000OO0OOO00000O ,))#line:364
        OOO00O0000000O000 .start ()#line:365
        OO0O0OOOOO00000OO .append (OOO00O0000000O000 )#line:366
        time .sleep (30 )#line:367
    for OOOO0O0OOO00OO0OO in OO0O0OOOOO00000OO :#line:368
        OOOO0O0OOO00OO0OO .join ()#line:369
if __name__ =='__main__':#line:372
    main ()#line:373
