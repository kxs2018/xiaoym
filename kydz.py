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


checklist =['MzU2OTczNzcwNg==','MzU5NTczMzA0MQ==','MzUwOTk5NDI0MQ==','MjM5Mjc5NjMyMw==','MzIxNjEzMDg2OQ==','MzUyMzk1MTAyNg==','MzI0MjE5MTc0OA==','MzU1ODI4MjI4Nw==','Mzg4OTA1MzI0Ng==','Mzg2MTI0Mzc1Nw==','MzU5NzgwMTgwMQ==','MzI3MTA5MTkwNQ==','Mzg5NjcyMzgyOA==','MjM5NjY4Mzk5OQ==','MzI1MDAwNDY1NA==','MjM5MTA5ODYzNQ==','MzAwNzA3MDAzMw==','MzkzMjUyNTk1OA==','MzAwNzA3MDAzMw==','MzI4NDY5MjkwNA==','MzIzNjgyOTE1Ng==','MzI2MjA0MzEwNA==','MzI0MjE5MTc0OA==','Mzg2NjExNDI2Mw==','MzAxMjE1MTYyMQ==']#line:94
def ftime ():#line:97
    OOOOO0000O0OOO0O0 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:98
    return OOOOO0000O0OOO0O0 #line:99
def debugger (O0OO0O0OOO0O0OOO0 ):#line:102
    if debug :#line:103
        print (O0OO0O0OOO0O0OOO0 )#line:104
def printlog (O000O0O0OOO00OOOO ):#line:107
    if printf :#line:108
        print (O000O0O0OOO00OOOO )#line:109
def send (OO00O0OO0OO000OOO ,title ='通知',url =None ):#line:112
    if not url :#line:113
        O00OO0O000OOOO0O0 ={"msgtype":"text","text":{"content":f"{title}\n\n{OO00O0OO0OO000OOO}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:120
    else :#line:121
        O00OO0O000OOOO0O0 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":OO00O0OO0OO000OOO ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:126
    O00OOO0OOOO00OOOO =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:127
    O0OOOO0000OO00000 =requests .post (O00OOO0OOOO00OOOO ,data =json .dumps (O00OO0O000OOOO0O0 )).json ()#line:128
    if O0OOOO0000OO00000 .get ('errcode')!=0 :#line:129
        print ('消息发送失败，请检查key和发送格式')#line:130
        return False #line:131
    return O0OOOO0000OO00000 #line:132
def push (O00OO0OO0OOO0O0OO ,OOOO00OOOOOOOO00O ,O00O00000O0O0O0O0 ,uid =None ):#line:135
    if uid :#line:136
        uids .append (uid )#line:137
    OO00000O00O0O0000 ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',O00OO0OO0OOO0O0OO ).replace ('url',O00O00000O0O0O0O0 )#line:139
    OOO0OO0O00O0O00OO ={"appToken":appToken ,"content":OO00000O00O0O0000 ,"summary":OOOO00OOOOOOOO00O ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":O00O00000O0O0O0O0 ,"verifyPay":False }#line:149
    OO0OOOO0O000000OO ='http://wxpusher.zjiecode.com/api/send/message'#line:150
    O00OO0OO0OOOOO000 =requests .post (url =OO0OOOO0O000000OO ,json =OOO0OO0O00O0O00OO ).json ()#line:151
    if O00OO0OO0OOOOO000 .get ('code')!=1000 :#line:152
        print (O00OO0OO0OOOOO000 .get ('msg'),O00OO0OO0OOOOO000 )#line:153
    return O00OO0OO0OOOOO000 #line:154
def getmpinfo (O0O00000O0OO000O0 ):#line:157
    if not O0O00000O0OO000O0 or O0O00000O0OO000O0 =='':#line:158
        return False #line:159
    OO0O00OO00O000O00 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:161
    OOOO00O0OO00000O0 =requests .get (O0O00000O0OO000O0 ,headers =OO0O00OO00O000O00 )#line:162
    O0OO0OO0000O0000O =etree .HTML (OOOO00O0OO00000O0 .text )#line:163
    OOOOO0O00O0000OOO =O0OO0OO0000O0000O .xpath ('//meta[@*="og:title"]/@content')#line:164
    if OOOOO0O00O0000OOO :#line:165
        OOOOO0O00O0000OOO =OOOOO0O00O0000OOO [0 ]#line:166
    O000O0OO00O0OOOO0 =O0OO0OO0000O0000O .xpath ('//meta[@*="og:url"]/@content')#line:167
    if O000O0OO00O0OOOO0 :#line:168
        O000O0OO00O0OOOO0 =O000O0OO00O0OOOO0 [0 ].encode ().decode ()#line:169
    try :#line:170
        O000O0OO000OO0O0O =re .findall (r'biz=(.*?)&',O0O00000O0OO000O0 )#line:171
    except :#line:172
        O000O0OO000OO0O0O =re .findall (r'biz=(.*?)&',O000O0OO00O0OOOO0 )#line:173
    if O000O0OO000OO0O0O :#line:174
        O000O0OO000OO0O0O =O000O0OO000OO0O0O [0 ]#line:175
    else :#line:176
        return False #line:177
    O0000O0O000O0OOO0 =O0OO0OO0000O0000O .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:178
    if O0000O0O000O0OOO0 :#line:179
        O0000O0O000O0OOO0 =O0000O0O000O0OOO0 [0 ].strip ()#line:180
    O00OOOO0O00OO0OOO =re .findall (r"user_name.DATA'\) : '(.*?)'",OOOO00O0OO00000O0 .text )or O0OO0OO0000O0000O .xpath ('//span[@class="profile_meta_value"]/text()')#line:182
    if O00OOOO0O00OO0OOO :#line:183
        O00OOOO0O00OO0OOO =O00OOOO0O00OO0OOO [0 ]#line:184
    O0000OOO0OO0OO0O0 =re .findall (r'createTime = \'(.*)\'',OOOO00O0OO00000O0 .text )#line:185
    if O0000OOO0OO0OO0O0 :#line:186
        O0000OOO0OO0OO0O0 =O0000OOO0OO0OO0O0 [0 ][5 :]#line:187
    OOO000O0O00O0OO0O =f'{O0000OOO0OO0OO0O0}|{OOOOO0O00O0000OOO}|{O000O0OO000OO0O0O}|{O0000O0O000O0OOO0}|{O00OOOO0O00OO0OOO}'#line:188
    O00000OO0O0OOOOO0 ={'biz':O000O0OO000OO0O0O ,'text':OOO000O0O00O0OO0O }#line:189
    return O00000OO0O0OOOOO0 #line:190
class YDZ :#line:193
    def __init__ (OO00OO0O000OOOOOO ,O00OO0OO0O000O0O0 ):#line:194
        OO00OO0O000OOOOOO .uid =O00OO0OO0O000O0O0 .get ('uid')#line:195
        OO00OO0O000OOOOOO .name =O00OO0OO0O000O0O0 .get ('name')#line:196
        OO00OO0O000OOOOOO .s =requests .session ()#line:197
        OO00OO0O000OOOOOO .ck =O00OO0OO0O000O0O0 .get ('ck')#line:198
        OO00OO0O000OOOOOO .msg =''#line:199
        OO00OO0O000OOOOOO .s .headers ={'Proxy-Connection':'keep-alive','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5279 MMWEBSDK/20230805 MMWEBID/2833 MicroMessenger/8.0.42.2460(0x28002A35) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9','a_h_n':f'http%3A%2F%2F5851583901.uzwxeze.cn%2F%3Fjgwq%3D3340348%26goid%3Ditrb/{OO00OO0O000OOOOOO.ck}','cookie':f'7bfe3c8f4d51851={OO00OO0O000OOOOOO.ck}'}#line:206
    def init (O00O0O00000OOO000 ):#line:208
        try :#line:209
            OO0OO0OO000OO00O0 ='http://5851583901.uzwxeze.cn/?jgwq=3340348&goid=itrb'#line:210
            O00O0000O0O000O0O =O00O0O00000OOO000 .s .get (OO0OO0OO000OO00O0 ).text #line:211
            O00O0000O0O000O0O =re .sub ('\s','',O00O0000O0O000O0O )#line:213
            O00O0O00000OOO000 .nickname =re .findall (r'nname=\'(.*?)\',',O00O0000O0O000O0O )[0 ]#line:214
            OO00O000O00OOO0O0 =re .findall (r'uid=\'(\d+)\'',O00O0000O0O000O0O )[0 ]#line:215
            O0O0OOO0O0OOO0OOO =f'http://58515{random.randint(10000, 99999)}.uzwxeze.cn/?jgwq={OO00O000O00OOO0O0}&goid=itrb/{O00O0O00000OOO000.ck}'#line:216
            O00O0O00000OOO000 .s .headers .update ({'a_h_n':O0O0OOO0O0OOO0OOO })#line:217
            return True #line:218
        except :#line:219
            printlog (f'{O00O0O00000OOO000.name} 账号信息获取错误，请检查ck有效性')#line:220
            O00O0O00000OOO000 .msg +='账号信息获取错误，请检查ck有效性\n'#line:221
            return False #line:222
    def getinfo (O0OOO00OO0OOOO00O ):#line:224
        O0OO0O000OO00O00O ='http://wxr.jjyii.com/user/getinfo?v=3'#line:225
        OOO0O0OO0O00O000O =O0OOO00OO0OOOO00O .s .get (O0OO0O000OO00O00O ).json ()#line:226
        debugger (f'getinfo2 {OOO0O0OO0O00O000O}')#line:227
        OOO0O0O0OO00O0O00 =OOO0O0OO0O00O000O .get ('data')#line:228
        O0OOO00OO0OOOO00O .count =OOO0O0O0OO00O0O00 .get ('count')#line:229
        O0OOO00OO0OOOO00O .gold =OOO0O0O0OO00O0O00 .get ('balance')#line:230
        OO000OO0OO0OO00O0 =OOO0O0O0OO00O0O00 .get ('hm')#line:231
        O0O00O000OO0OOOOO =OOO0O0O0OO00O0O00 .get ('hs')#line:232
        printlog (f'账号:{O0OOO00OO0OOOO00O.nickname},当前金币{O0OOO00OO0OOOO00O.gold}，今日已读{O0OOO00OO0OOOO00O.count}')#line:233
        O0OOO00OO0OOOO00O .msg +=f'账号:{O0OOO00OO0OOOO00O.nickname},当前金币{O0OOO00OO0OOOO00O.gold}，今日已读{O0OOO00OO0OOOO00O.count}\n'#line:234
        if OO000OO0OO0OO00O0 !=0 or O0O00O000OO0OOOOO !=0 :#line:235
            printlog (f'{O0OOO00OO0OOOO00O.nickname} 本轮次已结束，{OO000OO0OO0OO00O0}分钟后可继续任务')#line:236
            O0OOO00OO0OOOO00O .msg +='本轮次已结束，{hm}分钟后可继续任务\n'#line:237
            return False #line:238
        return True #line:239
    def read (O0OOOO00O0OOO0OO0 ):#line:241
        OOO00OOO0OOOOO0OO =random .randint (10000 ,99999 )#line:242
        OO00000OO00OO0OOO =f'http://58517{OOO00OOO0OOOOO0OO}.fgloceb.cn/?a=gt&goid=itrb&_v=3890/{O0OOOO00O0OOO0OO0.ck}'#line:243
        OOOOO0OOOO0O00OOO ='http://wxr.jjyii.com/r/get?v=10'#line:244
        OO00O00OOOO0000O0 ={'o':f'http://58517{OOO00OOO0OOOOO0OO}.ulzqwjf.cn/?a=gt&goid=itrb&_v=3890','t':'quick'}#line:246
        OOO0OO0O0000OOO0O =0 #line:247
        O0O00OO0O00000O00 =0 #line:248
        while OOO0OO0O0000OOO0O <30 and O0O00OO0O00000O00 <5 :#line:249
            if not O0OOOO00O0OOO0OO0 .getinfo ():#line:250
                break #line:251
            OO000O0O000O000OO =O0OOOO00O0OOO0OO0 .s .post (OOOOO0OOOO0O00OOO ,data =OO00O00OOOO0000O0 ).json ()#line:252
            debugger (f'read {OO000O0O000O000OO}')#line:253
            O00OOO00O0OO0O0OO =OO000O0O000O000OO .get ('data').get ('url')#line:254
            if OO000O0O000O000OO .get ('data').get ('uiv'):#line:255
                printlog (f'{O0OOOO00O0OOO0OO0.nickname} 号已黑，明天继续')#line:256
                O0OOOO00O0OOO0OO0 .msg +=f'号已黑，明天继续\n'#line:257
                break #line:258
            if not O00OOO00O0OO0O0OO :#line:259
                printlog (f'{O0OOOO00O0OOO0OO0.nickname} 没有获取到阅读链接，正在重试')#line:260
                O0OOOO00O0OOO0OO0 .msg +='没有获取到阅读链接，正在重试\n'#line:261
                time .sleep (5 )#line:262
                O0O00OO0O00000O00 +=1 #line:263
                continue #line:264
            O0OOO0O0O0OOOOO0O =getmpinfo (O00OOO00O0OO0O0OO )#line:265
            try :#line:266
                printlog (f'{O0OOOO00O0OOO0OO0.nickname} 正在阅读 {O0OOO0O0O0OOOOO0O["text"]}')#line:267
                O0OOOO00O0OOO0OO0 .msg +=f'正在阅读 {O0OOO0O0O0OOOOO0O["text"]}\n'#line:268
            except :#line:269
                printlog (f'{O0OOOO00O0OOO0OO0.nickname} 正在阅读 {O0OOO0O0O0OOOOO0O["biz"]}')#line:270
                O0OOOO00O0OOO0OO0 .msg +=f'正在阅读 {O0OOO0O0O0OOOOO0O["biz"]}\n'#line:271
            if 'chksm'in O00OOO00O0OO0O0OO or (O0OOO0O0O0OOOOO0O ["biz"]in checklist ):#line:272
                printlog (f'{O0OOOO00O0OOO0OO0.nickname} 正在阅读检测文章，发送通知，暂停60秒')#line:273
                O0OOOO00O0OOO0OO0 .msg +='正在阅读检测文章，发送通知，暂停60秒\n'#line:274
                if sendable :#line:275
                    send (f'{O0OOOO00O0OOO0OO0.nickname}\n点击阅读检测文章',f'{O0OOOO00O0OOO0OO0.name} 阅读赚过检测',O00OOO00O0OO0O0OO )#line:276
                if pushable :#line:277
                    push (f'{O0OOOO00O0OOO0OO0.nickname}\n点击阅读检测文章\n{O0OOO0O0O0OOOOO0O["text"]}',f'{O0OOOO00O0OOO0OO0.name} 阅读赚过检测',O00OOO00O0OO0O0OO ,O0OOOO00O0OOO0OO0 .uid )#line:278
                time .sleep (60 )#line:279
            OOO00OOO0OOOOO0OO =random .randint (7 ,10 )#line:280
            O0OOOO00O0OOO0OO0 .msg +='模拟阅读{t}秒\n'#line:281
            time .sleep (OOO00OOO0OOOOO0OO )#line:282
            OOOOOOOOOO0O0OO0O ='http://wxr.jjyii.com/r/ck'#line:283
            O0O000OOO0OOOO0O0 ={'Accept':'application/json, text/javascript, */*; q=0.01','Origin':'http://5851780833.ebrmrwy.cn','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',}#line:286
            O0OOOO00O0OOO0OO0 .s .headers .update (O0O000OOO0OOOO0O0 )#line:287
            OO000O0O000O000OO =O0OOOO00O0OOO0OO0 .s .post (OOOOOOOOOO0O0OO0O ,data ={'t':'quick'}).json ()#line:288
            debugger (f'check {OO000O0O000O000OO}')#line:289
            OO0OO0O0OOOOO0000 =OO000O0O000O000OO .get ('data').get ('gold')#line:290
            if OO0OO0O0OOOOO0000 :#line:291
                printlog (f'{O0OOOO00O0OOO0OO0.nickname} 阅读成功，获得金币{OO0OO0O0OOOOO0000}')#line:292
                O0OOOO00O0OOO0OO0 .msg +=f'阅读成功，获得金币{OO0OO0O0OOOOO0000}\n'#line:293
            OOO0OO0O0000OOO0O +=1 #line:294
    def cash (O00OO00OOOOO0000O ):#line:296
        if O00OO00OOOOO0000O .gold <txbz :#line:297
            printlog (f'{O00OO00OOOOO0000O.nickname} 你的金币不多了')#line:298
            O00OO00OOOOO0000O .msg +='你的金币不多了\n'#line:299
            return False #line:300
        OO0O0O0O0OOO0OOOO =int (O00OO00OOOOO0000O .gold /1000 )*1000 #line:301
        printlog (f'{O00OO00OOOOO0000O.nickname} 本次提现：{OO0O0O0O0OOO0OOOO}')#line:302
        O00OO00OOOOO0000O .msg +=f'本次提现：{OO0O0O0O0OOO0OOOO}\n'#line:303
        O0000O0OOO0OOOO00 ='http://wxr.jjyii.com/mine/cash'#line:304
        OOOOO0OO000000000 =O00OO00OOOOO0000O .s .post (O0000O0OOO0OOOO00 )#line:305
        if OOOOO0OO000000000 .json ().get ('code')==1 :#line:306
            printlog (f'{O00OO00OOOOO0000O.nickname} 提现成功')#line:307
            O00OO00OOOOO0000O .msg +='提现成功\n'#line:308
        else :#line:309
            debugger (OOOOO0OO000000000 .text )#line:310
            printlog (f'{O00OO00OOOOO0000O.nickname} 提现失败')#line:311
            O00OO00OOOOO0000O .msg +='提现失败\n'#line:312
    def run (OOO0O0OOO0000O0OO ):#line:314
        if OOO0O0OOO0000O0OO .init ():#line:315
            OOO0O0OOO0000O0OO .read ()#line:316
        OOO0O0OOO0000O0OO .cash ()#line:317
        if not printf :#line:318
            print (OOO0O0OOO0000O0OO .msg )#line:319
def yd (O0O0O0000OO0O0OOO ):#line:322
    while not O0O0O0000OO0O0OOO .empty ():#line:323
        O0000O0OOO0000O00 =O0O0O0000OO0O0OOO .get ()#line:324
        OO00OOOOO00OO00OO =YDZ (O0000O0OOO0000O00 )#line:325
        OO00OOOOO00OO00OO .run ()#line:326
def get_ver ():#line:329
    OOO00O0O000000OO0 ='kydz V0.1.8'#line:330
    OOOOOOOO0OO0O0000 ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:333
    O0000O00O0OOOO00O =requests .get ('https://ghproxy.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json',headers =OOOOOOOO0OO0O0000 ).json ()#line:335
    O00O000O00OO00000 =OOO00O0O000000OO0 .split (' ')[1 ]#line:336
    OO0OOOO00OO000OOO =O0000O00O0OOOO00O .get ('version').get (OOO00O0O000000OO0 .split (' ')[0 ])#line:337
    OO0OOO000O0000OO0 =f"当前版本 {O00O000O00OO00000}，仓库版本 {OO0OOOO00OO000OOO}"#line:338
    if O00O000O00OO00000 <OO0OOOO00OO000OOO :#line:339
        OO0OOO000O0000OO0 +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:340
    return OO0OOO000O0000OO0 #line:341
def main ():#line:344
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:345
    OO0O000OOOOOO0O00 =os .getenv ('ydzck')#line:346
    if not OO0O000OOOOOO0O00 :#line:347
        print ('仔细阅读脚本上方注释，配置好ydzck')#line:348
        return False #line:349
    try :#line:350
        OO0O000OOOOOO0O00 =ast .literal_eval (OO0O000OOOOOO0O00 )#line:351
    except :#line:352
        pass #line:353
    OO0OO0000O000OOO0 =[]#line:354
    O0OOO0O0000000OOO =Queue ()#line:355
    for O000OO0OO0O0OO000 ,O0OOO0O0OOO0OO0O0 in enumerate (OO0O000OOOOOO0O00 ):#line:356
        printlog (f'{O0OOO0O0OOO0OO0O0}\n以上是账号{O000OO0OO0O0OO000}的ck，请核对是否正确，如不正确，请检查ck填写格式')#line:357
        O0OOO0O0000000OOO .put (O0OOO0O0OOO0OO0O0 )#line:358
    for O000OO0OO0O0OO000 in range (max_workers ):#line:359
        O0O00OO000OOO00OO =threading .Thread (target =yd ,args =(O0OOO0O0000000OOO ,))#line:360
        O0O00OO000OOO00OO .start ()#line:361
        OO0OO0000O000OOO0 .append (O0O00OO000OOO00OO )#line:362
        time .sleep (30 )#line:363
    for OOO0O0OOO00O00O00 in OO0OO0000O000OOO0 :#line:364
        OOO0O0OOO00O00O00 .join ()#line:365
if __name__ =='__main__':#line:368
    main ()#line:369
