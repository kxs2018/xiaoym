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


checklist =['MzI0MjE5MTc0OA==','MzU2OTczNzcwNg==','Mzg5NjcyMzgyOA==','MjM5MTA5ODYzNQ==','MzI0MjY0NTY3Ng==','MzIzNjgyOTE1Ng==','MzA3MTI5NDc5Mw==','MzU5OTgwOTQ1NQ==','MzA3NDM1OTExMQ==','MzI3MTA5MTkwNQ==','Mzg2MTI0Mzc1Nw==','MzIxNTcyODI5OA==','MzAwNzA3MDAzMw==','MzI2MjA0MzEwNA==','MzIxNjA4NDg4NA==','MzA3MzczODIzNg==','MzI1MDAwNDY1NA==','Mzg5NzA2Nzc2MA==','MzU5NzgwMTgwMQ==','MjM5Mjc5NjMyMw==','MzU5NTczMzA0MQ==','Mzg3MjA3OTgwNQ==','MzU1ODI4MjI4Nw==','MzA5MDIzODA0NQ==','MzkzMjUyNTk1OA==','Mzg4OTA1MzI0Ng==','MzIzNzU4NzE5NQ==','MjM5MTk3NTQyOQ==','MjM5NjY4Mzk5OQ==','MzUyMzk1MTAyNg==','MzUwOTk5NDI0MQ==','Mzg2NjExNDI2Mw==','MzAxMjE1MTYyMQ==','MzIxNjEzMDg2OQ==','MzkxMDI2NTgwMw==','MzI4NDY5MjkwNA==']#line:90
def ftime ():#line:93
    OO0OO0O00000OOOO0 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:94
    return OO0OO0O00000OOOO0 #line:95
def debugger (O0OO00O00O0OOO0O0 ):#line:98
    if debug :#line:99
        print (O0OO00O00O0OOO0O0 )#line:100
def printlog (OOOOO0O0000O0O000 ):#line:103
    if printf :#line:104
        print (OOOOO0O0000O0O000 )#line:105
def send (O0OO00O00OO00000O ,title ='通知',url =None ):#line:108
    if not url :#line:109
        OOOOO000OO00O0O0O ={"msgtype":"text","text":{"content":f"{title}\n\n{O0OO00O00OO00000O}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:116
    else :#line:117
        OOOOO000OO00O0O0O ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O0OO00O00OO00000O ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:122
    OO0OO00000O0O0000 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:123
    O00O0O00O000O00OO =requests .post (OO0OO00000O0O0000 ,data =json .dumps (OOOOO000OO00O0O0O )).json ()#line:124
    if O00O0O00O000O00OO .get ('errcode')!=0 :#line:125
        print ('消息发送失败，请检查key和发送格式')#line:126
        return False #line:127
    return O00O0O00O000O00OO #line:128
def push (O00OO0OO00OOOO00O ,O0OO00O00O0OOO0OO ,OOO000O00O00OO00O ,uid =None ):#line:131
    if uid :#line:132
        uids .append (uid )#line:133
    OO0OOO0O0000O00O0 ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',O00OO0OO00OOOO00O ).replace ('url',OOO000O00O00OO00O )#line:135
    OO0O00O00OO0OOO0O ={"appToken":appToken ,"content":OO0OOO0O0000O00O0 ,"summary":O0OO00O00O0OOO0OO ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":OOO000O00O00OO00O ,"verifyPay":False }#line:145
    OO000O0000O0O0O0O ='http://wxpusher.zjiecode.com/api/send/message'#line:146
    OOOO0OOO00O00O000 =requests .post (url =OO000O0000O0O0O0O ,json =OO0O00O00OO0OOO0O ).json ()#line:147
    if OOOO0OOO00O00O000 .get ('code')!=1000 :#line:148
        print (OOOO0OOO00O00O000 .get ('msg'),OOOO0OOO00O00O000 )#line:149
    return OOOO0OOO00O00O000 #line:150
def getmpinfo (OOO00O0000OOOOO0O ):#line:153
    if not OOO00O0000OOOOO0O or OOO00O0000OOOOO0O =='':#line:154
        return False #line:155
    O0O0OO0000O0000O0 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:157
    OOO00000O0OO00000 =requests .get (OOO00O0000OOOOO0O ,headers =O0O0OO0000O0000O0 )#line:158
    OO00O00OOOOO00OO0 =etree .HTML (OOO00000O0OO00000 .text )#line:159
    O000O000O000OOO00 =OO00O00OOOOO00OO0 .xpath ('//meta[@*="og:title"]/@content')#line:160
    if O000O000O000OOO00 :#line:161
        O000O000O000OOO00 =O000O000O000OOO00 [0 ]#line:162
    O00OO00000OOO000O =OO00O00OOOOO00OO0 .xpath ('//meta[@*="og:url"]/@content')#line:163
    if O00OO00000OOO000O :#line:164
        O00OO00000OOO000O =O00OO00000OOO000O [0 ].encode ().decode ()#line:165
    try :#line:166
        OOO0O0O0OOOO000O0 =re .findall (r'biz=(.*?)&',OOO00O0000OOOOO0O )#line:167
    except :#line:168
        OOO0O0O0OOOO000O0 =re .findall (r'biz=(.*?)&',O00OO00000OOO000O )#line:169
    if OOO0O0O0OOOO000O0 :#line:170
        OOO0O0O0OOOO000O0 =OOO0O0O0OOOO000O0 [0 ]#line:171
    else :#line:172
        return False #line:173
    O00OO000OOO000O00 =OO00O00OOOOO00OO0 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:174
    if O00OO000OOO000O00 :#line:175
        O00OO000OOO000O00 =O00OO000OOO000O00 [0 ].strip ()#line:176
    O0O000O0O00OOO0O0 =re .findall (r"user_name.DATA'\) : '(.*?)'",OOO00000O0OO00000 .text )or OO00O00OOOOO00OO0 .xpath ('//span[@class="profile_meta_value"]/text()')#line:178
    if O0O000O0O00OOO0O0 :#line:179
        O0O000O0O00OOO0O0 =O0O000O0O00OOO0O0 [0 ]#line:180
    OO00O0OO0OOOOOOOO =re .findall (r'createTime = \'(.*)\'',OOO00000O0OO00000 .text )#line:181
    if OO00O0OO0OOOOOOOO :#line:182
        OO00O0OO0OOOOOOOO =OO00O0OO0OOOOOOOO [0 ][5 :]#line:183
    OOOOOOO0O00000O00 =f'{OO00O0OO0OOOOOOOO}|{O000O000O000OOO00}|{OOO0O0O0OOOO000O0}|{O00OO000OOO000O00}|{O0O000O0O00OOO0O0}'#line:184
    O0OOO0OO0000OOO0O ={'biz':OOO0O0O0OOOO000O0 ,'text':OOOOOOO0O00000O00 }#line:185
    return O0OOO0OO0000OOO0O #line:186
class YDZ :#line:189
    def __init__ (O0O0O0OOO0OO0O000 ,O0OOO0000OOOOOOOO ):#line:190
        O0O0O0OOO0OO0O000 .uid =O0OOO0000OOOOOOOO .get ('uid')#line:191
        O0O0O0OOO0OO0O000 .name =O0OOO0000OOOOOOOO .get ('name')#line:192
        O0O0O0OOO0OO0O000 .s =requests .session ()#line:193
        O0O0O0OOO0OO0O000 .ck =O0OOO0000OOOOOOOO .get ('ck')#line:194
        O0O0O0OOO0OO0O000 .msg =''#line:195
        O0O0O0OOO0OO0O000 .s .headers ={'Proxy-Connection':'keep-alive','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5279 MMWEBSDK/20230805 MMWEBID/2833 MicroMessenger/8.0.42.2460(0x28002A35) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9','a_h_n':f'http%3A%2F%2F5851583901.uzwxeze.cn%2F%3Fjgwq%3D3340348%26goid%3Ditrb/{O0O0O0OOO0OO0O000.ck}','cookie':f'7bfe3c8f4d51851={O0O0O0OOO0OO0O000.ck}'}#line:202
    def init (OO0OOO0000OO0O0OO ):#line:204
        try :#line:205
            OOO00OOO0000OO0O0 ='http://5851583901.uzwxeze.cn/?jgwq=3340348&goid=itrb'#line:206
            O000000OO0O00O0OO =OO0OOO0000OO0O0OO .s .get (OOO00OOO0000OO0O0 ).text #line:207
            O000000OO0O00O0OO =re .sub ('\s','',O000000OO0O00O0OO )#line:209
            OO0OOO0000OO0O0OO .nickname =re .findall (r'nname=\'(.*?)\',',O000000OO0O00O0OO )[0 ]#line:210
            OO00O0O0O0000OOOO =re .findall (r'uid=\'(\d+)\'',O000000OO0O00O0OO )[0 ]#line:211
            O00OO0OO0O000O00O =f'http://58515{random.randint(10000, 99999)}.uzwxeze.cn/?jgwq={OO00O0O0O0000OOOO}&goid=itrb/{OO0OOO0000OO0O0OO.ck}'#line:212
            OO0OOO0000OO0O0OO .s .headers .update ({'a_h_n':O00OO0OO0O000O00O })#line:213
            return True #line:214
        except :#line:215
            printlog (f'{OO0OOO0000OO0O0OO.name} 账号信息获取错误，请检查ck有效性')#line:216
            OO0OOO0000OO0O0OO .msg +='账号信息获取错误，请检查ck有效性\n'#line:217
            return False #line:218
    def getinfo (OO0OO0OOO0OO0OO00 ):#line:220
        OOO0OOOO0OOO0O00O ='http://wxr.jjyii.com/user/getinfo?v=3'#line:221
        OO0O00000OOO0OO00 =OO0OO0OOO0OO0OO00 .s .get (OOO0OOOO0OOO0O00O ).json ()#line:222
        debugger (f'getinfo2 {OO0O00000OOO0OO00}')#line:223
        OOO00O0OO0OO00O00 =OO0O00000OOO0OO00 .get ('data')#line:224
        OO0OO0OOO0OO0OO00 .count =OOO00O0OO0OO00O00 .get ('count')#line:225
        OO0OO0OOO0OO0OO00 .gold =OOO00O0OO0OO00O00 .get ('balance')#line:226
        O00O0OO00O00O0OOO =OOO00O0OO0OO00O00 .get ('hm')#line:227
        O0000OO0OOOO0000O =OOO00O0OO0OO00O00 .get ('hs')#line:228
        printlog (f'账号:{OO0OO0OOO0OO0OO00.nickname},当前金币{OO0OO0OOO0OO0OO00.gold}，今日已读{OO0OO0OOO0OO0OO00.count}')#line:229
        OO0OO0OOO0OO0OO00 .msg +=f'账号:{OO0OO0OOO0OO0OO00.nickname},当前金币{OO0OO0OOO0OO0OO00.gold}，今日已读{OO0OO0OOO0OO0OO00.count}\n'#line:230
        if O00O0OO00O00O0OOO !=0 or O0000OO0OOOO0000O !=0 :#line:231
            printlog (f'{OO0OO0OOO0OO0OO00.nickname} 本轮次已结束，{O00O0OO00O00O0OOO}分钟后可继续任务')#line:232
            OO0OO0OOO0OO0OO00 .msg +='本轮次已结束，{hm}分钟后可继续任务\n'#line:233
            return False #line:234
        return True #line:235
    def read (OOO00O0O0O0OO0O00 ):#line:237
        O00000O0O0O000OO0 =random .randint (10000 ,99999 )#line:238
        OO0000000OO00O000 =f'http://58517{O00000O0O0O000OO0}.fgloceb.cn/?a=gt&goid=itrb&_v=3890/{OOO00O0O0O0OO0O00.ck}'#line:239
        OO0O00OO00O0OOOOO ='http://wxr.jjyii.com/r/get?v=10'#line:240
        O0OO0O00OO00OOO0O ={'o':f'http://58517{O00000O0O0O000OO0}.ulzqwjf.cn/?a=gt&goid=itrb&_v=3890','t':'quick'}#line:242
        OO0000OO0OOO0O0OO =0 #line:243
        O0O0OOOO00OO0O0OO =0 #line:244
        while OO0000OO0OOO0O0OO <30 and O0O0OOOO00OO0O0OO <5 :#line:245
            if not OOO00O0O0O0OO0O00 .getinfo ():#line:246
                break #line:247
            O00000O0O0000O0OO =OOO00O0O0O0OO0O00 .s .post (OO0O00OO00O0OOOOO ,data =O0OO0O00OO00OOO0O ).json ()#line:248
            debugger (f'read {O00000O0O0000O0OO}')#line:249
            OOO00000O0OOO000O =O00000O0O0000O0OO .get ('data').get ('url')#line:250
            if O00000O0O0000O0OO .get ('data').get ('uiv'):#line:251
                printlog (f'{OOO00O0O0O0OO0O00.nickname} 号已黑，明天继续')#line:252
                OOO00O0O0O0OO0O00 .msg +=f'号已黑，明天继续\n'#line:253
                break #line:254
            if not OOO00000O0OOO000O :#line:255
                printlog (f'{OOO00O0O0O0OO0O00.nickname} 没有获取到阅读链接，正在重试')#line:256
                OOO00O0O0O0OO0O00 .msg +='没有获取到阅读链接，正在重试\n'#line:257
                time .sleep (5 )#line:258
                O0O0OOOO00OO0O0OO +=1 #line:259
                continue #line:260
            OOO0OOO0O00000O0O =getmpinfo (OOO00000O0OOO000O )#line:261
            try :#line:262
                printlog (f'{OOO00O0O0O0OO0O00.nickname} 正在阅读 {OOO0OOO0O00000O0O["text"]}')#line:263
                OOO00O0O0O0OO0O00 .msg +=f'正在阅读 {OOO0OOO0O00000O0O["text"]}\n'#line:264
            except :#line:265
                printlog (f'{OOO00O0O0O0OO0O00.nickname} 正在阅读 {OOO0OOO0O00000O0O["biz"]}')#line:266
                OOO00O0O0O0OO0O00 .msg +=f'正在阅读 {OOO0OOO0O00000O0O["biz"]}\n'#line:267
            if 'chksm'in OOO00000O0OOO000O or (OOO0OOO0O00000O0O ["biz"]in checklist ):#line:268
                printlog (f'{OOO00O0O0O0OO0O00.nickname} 正在阅读检测文章，发送通知，暂停60秒')#line:269
                OOO00O0O0O0OO0O00 .msg +='正在阅读检测文章，发送通知，暂停60秒\n'#line:270
                if sendable :#line:271
                    send (f'{OOO00O0O0O0OO0O00.nickname}\n点击阅读检测文章',f'{OOO00O0O0O0OO0O00.name} 阅读赚过检测',OOO00000O0OOO000O )#line:272
                if pushable :#line:273
                    push (f'{OOO00O0O0O0OO0O00.nickname}\n点击阅读检测文章\n{OOO0OOO0O00000O0O["text"]}',f'{OOO00O0O0O0OO0O00.name} 阅读赚过检测',OOO00000O0OOO000O ,OOO00O0O0O0OO0O00 .uid )#line:274
                time .sleep (60 )#line:275
            O00000O0O0O000OO0 =random .randint (7 ,10 )#line:276
            OOO00O0O0O0OO0O00 .msg +='模拟阅读{t}秒\n'#line:277
            time .sleep (O00000O0O0O000OO0 )#line:278
            OO0000OOO00O0OO00 ='http://wxr.jjyii.com/r/ck'#line:279
            OOOOOOOO00O000O0O ={'Accept':'application/json, text/javascript, */*; q=0.01','Origin':'http://5851780833.ebrmrwy.cn','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',}#line:282
            OOO00O0O0O0OO0O00 .s .headers .update (OOOOOOOO00O000O0O )#line:283
            O00000O0O0000O0OO =OOO00O0O0O0OO0O00 .s .post (OO0000OOO00O0OO00 ,data ={'t':'quick'}).json ()#line:284
            debugger (f'check {O00000O0O0000O0OO}')#line:285
            OOO0OOO0O00O0O00O =O00000O0O0000O0OO .get ('data').get ('gold')#line:286
            if OOO0OOO0O00O0O00O :#line:287
                printlog (f'{OOO00O0O0O0OO0O00.nickname} 阅读成功，获得金币{OOO0OOO0O00O0O00O}')#line:288
                OOO00O0O0O0OO0O00 .msg +=f'阅读成功，获得金币{OOO0OOO0O00O0O00O}\n'#line:289
            OO0000OO0OOO0O0OO +=1 #line:290
    def cash (O0O0000O00OOOO00O ):#line:292
        if O0O0000O00OOOO00O .gold <txbz :#line:293
            printlog (f'{O0O0000O00OOOO00O.nickname} 你的金币不多了')#line:294
            O0O0000O00OOOO00O .msg +='你的金币不多了\n'#line:295
            return False #line:296
        OOO0O0OOO0O0O0OOO =int (O0O0000O00OOOO00O .gold /1000 )*1000 #line:297
        printlog (f'{O0O0000O00OOOO00O.nickname} 本次提现：{OOO0O0OOO0O0O0OOO}')#line:298
        O0O0000O00OOOO00O .msg +=f'本次提现：{OOO0O0OOO0O0O0OOO}\n'#line:299
        OOO000O0OOO0OOO00 ='http://wxr.jjyii.com/mine/cash'#line:300
        O0O00OOOO00O0O00O =O0O0000O00OOOO00O .s .post (OOO000O0OOO0OOO00 )#line:301
        if O0O00OOOO00O0O00O .json ().get ('code')==1 :#line:302
            printlog (f'{O0O0000O00OOOO00O.nickname} 提现成功')#line:303
            O0O0000O00OOOO00O .msg +='提现成功\n'#line:304
        else :#line:305
            debugger (O0O00OOOO00O0O00O .text )#line:306
            printlog (f'{O0O0000O00OOOO00O.nickname} 提现失败')#line:307
            O0O0000O00OOOO00O .msg +='提现失败\n'#line:308
    def run (OOOO0O0O000O0O0OO ):#line:310
        if OOOO0O0O000O0O0OO .init ():#line:311
            OOOO0O0O000O0O0OO .read ()#line:312
        OOOO0O0O000O0O0OO .cash ()#line:313
        if not printf :#line:314
            print (OOOO0O0O000O0O0OO .msg )#line:315
def yd (OO00O00O00O0O0000 ):#line:318
    while not OO00O00O00O0O0000 .empty ():#line:319
        O000O0000OO00OOOO =OO00O00O00O0O0000 .get ()#line:320
        O000O00000OO0OOO0 =YDZ (O000O0000OO00OOOO )#line:321
        O000O00000OO0OOO0 .run ()#line:322
def get_ver ():#line:325
    OOOO0O0O0OO0O00OO ='kydz V0.1.9'#line:326
    O00OO00O0O0OOOOO0 ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:329
    OO0O000OO00OOO00O =requests .get ('https://ghproxy.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json',headers =O00OO00O0O0OOOOO0 ).json ()#line:331
    OOOOOO0OO0OOO0O0O =OOOO0O0O0OO0O00OO .split (' ')[1 ]#line:332
    O0OO00000OO000OOO =OO0O000OO00OOO00O .get ('version').get (OOOO0O0O0OO0O00OO .split (' ')[0 ])#line:333
    O0O0O0O00000O0OOO =f"当前版本 {OOOOOO0OO0OOO0O0O}，仓库版本 {O0OO00000OO000OOO}"#line:334
    if OOOOOO0OO0OOO0O0O <O0OO00000OO000OOO :#line:335
        O0O0O0O00000O0OOO +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:336
    return O0O0O0O00000O0OOO #line:337
def main ():#line:340
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:341
    O0O0OO0000OOO0OO0 =os .getenv ('ydzck')#line:342
    if not O0O0OO0000OOO0OO0 :#line:343
        print ('仔细阅读脚本上方注释，配置好ydzck')#line:344
        return False #line:345
    try :#line:346
        O0O0OO0000OOO0OO0 =ast .literal_eval (O0O0OO0000OOO0OO0 )#line:347
    except :#line:348
        pass #line:349
    OO00OO00O0O0O0O00 =[]#line:350
    O000OOO00OOO0O0O0 =Queue ()#line:351
    for OO0OOO00000OOO0OO ,OO00O00O00000OOOO in enumerate (O0O0OO0000OOO0OO0 ):#line:352
        printlog (f'{OO00O00O00000OOOO}\n以上是账号{OO0OOO00000OOO0OO}的ck，请核对是否正确，如不正确，请检查ck填写格式')#line:353
        O000OOO00OOO0O0O0 .put (OO00O00O00000OOOO )#line:354
    for OO0OOO00000OOO0OO in range (max_workers ):#line:355
        OO0OOO0OO0OO000OO =threading .Thread (target =yd ,args =(O000OOO00OOO0O0O0 ,))#line:356
        OO0OOO0OO0OO000OO .start ()#line:357
        OO00OO00O0O0O0O00 .append (OO0OOO0OO0OO000OO )#line:358
        time .sleep (30 )#line:359
    for O0OOOOOO0O0O0OOO0 in OO00OO00O0O0O0O00 :#line:360
        O0OOOOOO0O0O0OOO0 .join ()#line:361
if __name__ =='__main__':#line:364
    main ()#line:365
