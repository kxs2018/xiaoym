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


checklist =['MzU2OTczNzcwNg==','MzU5NTczMzA0MQ==','MzUwOTk5NDI0MQ==','MjM5Mjc5NjMyMw==','MzIxNjEzMDg2OQ==','MzUyMzk1MTAyNg==','MzI0MjE5MTc0OA==','MzU1ODI4MjI4Nw==','Mzg4OTA1MzI0Ng==','Mzg2MTI0Mzc1Nw==','MzU5NzgwMTgwMQ==','MzI3MTA5MTkwNQ==','Mzg5NjcyMzgyOA==','MjM5NjY4Mzk5OQ==','MzI1MDAwNDY1NA==','MjM5MTA5ODYzNQ==','MzAwNzA3MDAzMw==','MzkzMjUyNTk1OA==','MzAwNzA3MDAzMw==','MzI4NDY5MjkwNA==','MzIzNjgyOTE1Ng==','MzI2MjA0MzEwNA==','MzI0MjE5MTc0OA==','Mzg2NjExNDI2Mw==',]#line:94
def ftime ():#line:97
    O00OOOOO00OOO0OO0 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:98
    return O00OOOOO00OOO0OO0 #line:99
def debugger (OO00OOO00O0OO0O0O ):#line:102
    if debug :#line:103
        print (OO00OOO00O0OO0O0O )#line:104
def printlog (OOO000O0O00OOO000 ):#line:107
    if printf :#line:108
        print (OOO000O0O00OOO000 )#line:109
def send (O0OOO0O0O00O00OOO ,title ='通知',url =None ):#line:112
    if not url :#line:113
        OO00O0O00O00O00O0 ={"msgtype":"text","text":{"content":f"{title}\n\n{O0OOO0O0O00O00OOO}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:120
    else :#line:121
        OO00O0O00O00O00O0 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O0OOO0O0O00O00OOO ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:126
    OOO0000000O0O0OOO =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:127
    O00OO0000O0O00000 =requests .post (OOO0000000O0O0OOO ,data =json .dumps (OO00O0O00O00O00O0 )).json ()#line:128
    if O00OO0000O0O00000 .get ('errcode')!=0 :#line:129
        print ('消息发送失败，请检查key和发送格式')#line:130
        return False #line:131
    return O00OO0000O0O00000 #line:132
def push (OOOOOOO00OO00O0O0 ,O0O0OOO0000OO0O0O ,O0OOO00OOO0OO0OO0 ,uid =None ):#line:135
    if uid :#line:136
        uids .append (uid )#line:137
    O000O0OOOO0000OOO ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',OOOOOOO00OO00O0O0 ).replace ('url',O0OOO00OOO0OO0OO0 )#line:139
    OOOO00O0OOO0OOO00 ={"appToken":appToken ,"content":O000O0OOOO0000OOO ,"summary":O0O0OOO0000OO0O0O ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":O0OOO00OOO0OO0OO0 ,"verifyPay":False }#line:149
    O000O00O0OO00OOOO ='http://wxpusher.zjiecode.com/api/send/message'#line:150
    O0O0O0O0O00O0OO0O =requests .post (url =O000O00O0OO00OOOO ,json =OOOO00O0OOO0OOO00 ).json ()#line:151
    if O0O0O0O0O00O0OO0O .get ('code')!=1000 :#line:152
        print (O0O0O0O0O00O0OO0O .get ('msg'),O0O0O0O0O00O0OO0O )#line:153
    return O0O0O0O0O00O0OO0O #line:154
def getmpinfo (O00O0000000O00O0O ):#line:157
    if not O00O0000000O00O0O or O00O0000000O00O0O =='':#line:158
        return False #line:159
    OOO00OOO0OOOOO0O0 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:161
    O000OO000O00OOOOO =requests .get (O00O0000000O00O0O ,headers =OOO00OOO0OOOOO0O0 )#line:162
    OO0O00OO0O00OOOO0 =etree .HTML (O000OO000O00OOOOO .text )#line:163
    O0O0O0O0OOOOOO000 =OO0O00OO0O00OOOO0 .xpath ('//meta[@*="og:title"]/@content')#line:164
    if O0O0O0O0OOOOOO000 :#line:165
        O0O0O0O0OOOOOO000 =O0O0O0O0OOOOOO000 [0 ]#line:166
    O000OOOO00OO0O000 =OO0O00OO0O00OOOO0 .xpath ('//meta[@*="og:url"]/@content')#line:167
    if O000OOOO00OO0O000 :#line:168
        O000OOOO00OO0O000 =O000OOOO00OO0O000 [0 ].encode ().decode ()#line:169
    try :#line:170
        OO0000OOOO0O00O0O =re .findall (r'biz=(.*?)&',O00O0000000O00O0O )#line:171
    except :#line:172
        OO0000OOOO0O00O0O =re .findall (r'biz=(.*?)&',O000OOOO00OO0O000 )#line:173
    if OO0000OOOO0O00O0O :#line:174
        OO0000OOOO0O00O0O =OO0000OOOO0O00O0O [0 ]#line:175
    else :#line:176
        return False #line:177
    O000O0O0O00OOOOO0 =OO0O00OO0O00OOOO0 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:178
    if O000O0O0O00OOOOO0 :#line:179
        O000O0O0O00OOOOO0 =O000O0O0O00OOOOO0 [0 ].strip ()#line:180
    O000OO0000O000O00 =re .findall (r"user_name.DATA'\) : '(.*?)'",O000OO000O00OOOOO .text )or OO0O00OO0O00OOOO0 .xpath ('//span[@class="profile_meta_value"]/text()')#line:182
    if O000OO0000O000O00 :#line:183
        O000OO0000O000O00 =O000OO0000O000O00 [0 ]#line:184
    O000O0OOOOO0O00O0 =re .findall (r'createTime = \'(.*)\'',O000OO000O00OOOOO .text )#line:185
    if O000O0OOOOO0O00O0 :#line:186
        O000O0OOOOO0O00O0 =O000O0OOOOO0O00O0 [0 ][5 :]#line:187
    O00OOO0O0OO0O0OOO =f'{O000O0OOOOO0O00O0}|{O0O0O0O0OOOOOO000}|{OO0000OOOO0O00O0O}|{O000O0O0O00OOOOO0}|{O000OO0000O000O00}'#line:188
    O00O0OOO000000OOO ={'biz':OO0000OOOO0O00O0O ,'text':O00OOO0O0OO0O0OOO }#line:189
    return O00O0OOO000000OOO #line:190
class YDZ :#line:193
    def __init__ (OO0O0000O0O0000OO ,O00O0O00000O0OOO0 ):#line:194
        OO0O0000O0O0000OO .uid =O00O0O00000O0OOO0 .get ('uid')#line:195
        OO0O0000O0O0000OO .name =O00O0O00000O0OOO0 .get ('name')#line:196
        OO0O0000O0O0000OO .s =requests .session ()#line:197
        OO0O0000O0O0000OO .ck =O00O0O00000O0OOO0 .get ('ck')#line:198
        OO0O0000O0O0000OO .msg =''#line:199
        OO0O0000O0O0000OO .s .headers ={'Proxy-Connection':'keep-alive','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8431 Flue','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9','a_h_n':f'http%3A%2F%2F5851535337.udqyeba.cn%2F%3Fjgwq%3D3340348%26goid%3Ditrb/{OO0O0000O0O0000OO.ck}','cookie':f'7bfe3c8f4d51851={OO0O0000O0O0000OO.ck}'}#line:206
    def init (OOO000O0OOO0000OO ):#line:208
        try :#line:209
            OO0OOO0O0OOOO000O ='http://5851599460.udqyeba.cn/?jgwq=3340348&goid=itrb'#line:210
            O000OO00O0O0O00O0 =OOO000O0OOO0000OO .s .get (OO0OOO0O0OOOO000O ).text #line:211
            O000OO00O0O0O00O0 =re .sub ('\s','',O000OO00O0O0O00O0 )#line:213
            OOO000O0OOO0000OO .nickname =re .findall (r'nname=\'(.*?)\',',O000OO00O0O0O00O0 )[0 ]#line:214
            OOOOOOOO000O0OOOO =re .findall (r'uid=\'(\d+)\'',O000OO00O0O0O00O0 )[0 ]#line:215
            OO00O0O000OOOOOOO =f'http://58515{random.randint(10000, 99999)}.udqyeba.cn/?jgwq={OOOOOOOO000O0OOOO}&goid=itrb/{OOO000O0OOO0000OO.ck}'#line:216
            OOO000O0OOO0000OO .s .headers .update ({'a_h_n':OO00O0O000OOOOOOO })#line:217
            return True #line:218
        except :#line:219
            printlog (f'{OOO000O0OOO0000OO.name} 账号信息获取错误，请检查ck有效性')#line:220
            OOO000O0OOO0000OO .msg +='账号信息获取错误，请检查ck有效性\n'#line:221
            return False #line:222
    def getinfo (O0OO0O00000O00OO0 ):#line:224
        O000OOOOO000OO00O ='http://wxr.jjyii.com/user/getinfo?v=3'#line:225
        OOO000O00OOO0OOO0 =O0OO0O00000O00OO0 .s .get (O000OOOOO000OO00O ).json ()#line:226
        debugger (f'getinfo2 {OOO000O00OOO0OOO0}')#line:227
        OOO0O0OOOOOO00O0O =OOO000O00OOO0OOO0 .get ('data')#line:228
        O0OO0O00000O00OO0 .count =OOO0O0OOOOOO00O0O .get ('count')#line:229
        O0OO0O00000O00OO0 .gold =OOO0O0OOOOOO00O0O .get ('balance')#line:230
        O00O00OOOO0000O00 =OOO0O0OOOOOO00O0O .get ('hm')#line:231
        O00O000000O0OOO0O =OOO0O0OOOOOO00O0O .get ('hs')#line:232
        printlog (f'账号:{O0OO0O00000O00OO0.nickname},当前金币{O0OO0O00000O00OO0.gold}，今日已读{O0OO0O00000O00OO0.count}')#line:233
        O0OO0O00000O00OO0 .msg +=f'账号:{O0OO0O00000O00OO0.nickname},当前金币{O0OO0O00000O00OO0.gold}，今日已读{O0OO0O00000O00OO0.count}\n'#line:234
        if O00O00OOOO0000O00 !=0 or O00O000000O0OOO0O !=0 :#line:235
            printlog (f'{O0OO0O00000O00OO0.nickname} 本轮次已结束，{O00O00OOOO0000O00}分钟后可继续任务')#line:236
            O0OO0O00000O00OO0 .msg +='本轮次已结束，{hm}分钟后可继续任务\n'#line:237
            return False #line:238
        return True #line:239
    def read (O00OOOO0000OOO00O ):#line:241
        O00000000000OOOOO ='http://wxr.jjyii.com/r/get?v=10'#line:242
        O00O0O000O000OO00 ={'o':f'http://58517{random.randint(10000, 99999)}.ulzqwjf.cn/?a=gt','goid':'itrb','_v':'3890','t':'quick'}#line:244
        OOOOO0OOOOOO00OOO =0 #line:245
        O00O0O0OOO000OOO0 =0 #line:246
        while OOOOO0OOOOOO00OOO <30 and O00O0O0OOO000OOO0 <5 :#line:247
            if not O00OOOO0000OOO00O .getinfo ():#line:248
                break #line:249
            OO00000OOO000OO00 =O00OOOO0000OOO00O .s .post (O00000000000OOOOO ,data =O00O0O000O000OO00 ).json ()#line:250
            debugger (f'read {OO00000OOO000OO00}')#line:251
            O0O0000000OO00O0O =OO00000OOO000OO00 .get ('data').get ('url')#line:252
            if not O0O0000000OO00O0O :#line:253
                printlog (f'{O00OOOO0000OOO00O.nickname} 没有获取到阅读链接，正在重试')#line:254
                O00OOOO0000OOO00O .msg +='没有获取到阅读链接，正在重试\n'#line:255
                time .sleep (5 )#line:256
                O00O0O0OOO000OOO0 +=1 #line:257
                continue #line:258
            OOOOO00OOO0O000O0 =getmpinfo (O0O0000000OO00O0O )#line:259
            try :#line:260
                printlog (f'{O00OOOO0000OOO00O.nickname} 正在阅读 {OOOOO00OOO0O000O0["text"]}')#line:261
                O00OOOO0000OOO00O .msg +=f'正在阅读 {OOOOO00OOO0O000O0["text"]}\n'#line:262
            except :#line:263
                printlog (f'{O00OOOO0000OOO00O.nickname} 正在阅读 {OOOOO00OOO0O000O0["biz"]}')#line:264
                O00OOOO0000OOO00O .msg +=f'正在阅读 {OOOOO00OOO0O000O0["biz"]}\n'#line:265
            if 'chksm'in O0O0000000OO00O0O or (OOOOO00OOO0O000O0 ["biz"]in checklist ):#line:266
                printlog (f'{O00OOOO0000OOO00O.nickname} 正在阅读检测文章，发送通知，暂停60秒')#line:267
                O00OOOO0000OOO00O .msg +='正在阅读检测文章，发送通知，暂停60秒\n'#line:268
                if sendable :#line:269
                    send (f'{O00OOOO0000OOO00O.nickname}\n点击阅读检测文章',f'{O00OOOO0000OOO00O.name} 阅读赚过检测',O0O0000000OO00O0O )#line:270
                if pushable :#line:271
                    push (f'{O00OOOO0000OOO00O.nickname}\n点击阅读检测文章\n{OOOOO00OOO0O000O0["text"]}',f'{O00OOOO0000OOO00O.name} 阅读赚过检测',O0O0000000OO00O0O ,O00OOOO0000OOO00O .uid )#line:272
                time .sleep (60 )#line:273
            O0O0OOO0OO0OOO0O0 =random .randint (7 ,10 )#line:274
            O00OOOO0000OOO00O .msg +='模拟阅读{t}秒\n'#line:275
            time .sleep (O0O0OOO0OO0OOO0O0 )#line:276
            O0OOO000O0O000000 ='http://wxr.jjyii.com/r/ck'#line:277
            OO0O00O00OO00OO0O ={'Accept':'application/json, text/javascript, */*; q=0.01','Origin':'http://5851780833.ebrmrwy.cn','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',}#line:280
            O00OOOO0000OOO00O .s .headers .update (OO0O00O00OO00OO0O )#line:281
            OO00000OOO000OO00 =O00OOOO0000OOO00O .s .post (O0OOO000O0O000000 ,data ={'t':'quick'}).json ()#line:282
            debugger (f'check {OO00000OOO000OO00}')#line:283
            OO0000O000OOOOOO0 =OO00000OOO000OO00 .get ('data').get ('gold')#line:284
            if OO0000O000OOOOOO0 :#line:285
                printlog (f'{O00OOOO0000OOO00O.nickname} 阅读成功，获得金币{OO0000O000OOOOOO0}')#line:286
                O00OOOO0000OOO00O .msg +=f'阅读成功，获得金币{OO0000O000OOOOOO0}\n'#line:287
            OOOOO0OOOOOO00OOO +=1 #line:288
    def cash (O00OO0OOOOOOOOOO0 ):#line:290
        if O00OO0OOOOOOOOOO0 .gold <txbz :#line:291
            printlog (f'{O00OO0OOOOOOOOOO0.nickname} 你的金币不多了')#line:292
            O00OO0OOOOOOOOOO0 .msg +='你的金币不多了\n'#line:293
            return False #line:294
        O0O0OO0OO000OO0O0 =int (O00OO0OOOOOOOOOO0 .gold /1000 )*1000 #line:295
        printlog (f'{O00OO0OOOOOOOOOO0.nickname} 本次提现：{O0O0OO0OO000OO0O0}')#line:296
        O00OO0OOOOOOOOOO0 .msg +=f'本次提现：{O0O0OO0OO000OO0O0}\n'#line:297
        OO0OO00OOOOOOOOO0 ='http://wxr.jjyii.com/mine/cash'#line:298
        O000OO0OO000O00O0 =O00OO0OOOOOOOOOO0 .s .post (OO0OO00OOOOOOOOO0 )#line:299
        if O000OO0OO000O00O0 .json ().get ('code')==1 :#line:300
            printlog (f'{O00OO0OOOOOOOOOO0.nickname} 提现成功')#line:301
            O00OO0OOOOOOOOOO0 .msg +='提现成功\n'#line:302
        else :#line:303
            debugger (O000OO0OO000O00O0 .text )#line:304
            printlog (f'{O00OO0OOOOOOOOOO0.nickname} 提现失败')#line:305
            O00OO0OOOOOOOOOO0 .msg +='提现失败\n'#line:306
    def run (OOO0O00OO0OO00O00 ):#line:308
        if OOO0O00OO0OO00O00 .init ():#line:309
            OOO0O00OO0OO00O00 .read ()#line:310
        OOO0O00OO0OO00O00 .cash ()#line:311
        if not printf :#line:312
            print (OOO0O00OO0OO00O00 .msg )#line:313
def yd (OOOO000OOOO00OOOO ):#line:316
    while not OOOO000OOOO00OOOO .empty ():#line:317
        O0000OOOO0O0000OO =OOOO000OOOO00OOOO .get ()#line:318
        O0O000OO00OOO00O0 =YDZ (O0000OOOO0O0000OO )#line:319
        O0O000OO00OOO00O0 .run ()#line:320
def get_ver ():#line:323
    O0000OO000OOOO0O0 ='kydz V0.1.6'#line:324
    OO0O00OOOO00OO000 ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:327
    OO00000000O00OO0O =requests .get ('https://ghproxy.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json',headers =OO0O00OOOO00OO000 ).json ()#line:329
    OO0O000O0O0O00O0O =O0000OO000OOOO0O0 .split (' ')[1 ]#line:330
    OO0O0OOO00O0OO0O0 =OO00000000O00OO0O .get ('version').get (O0000OO000OOOO0O0 .split (' ')[0 ])#line:331
    OO0000O00O0OOOOO0 =f"当前版本 {OO0O000O0O0O00O0O}，仓库版本 {OO0O0OOO00O0OO0O0}"#line:332
    if OO0O000O0O0O00O0O <OO0O0OOO00O0OO0O0 :#line:333
        OO0000O00O0OOOOO0 +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:334
    return OO0000O00O0OOOOO0 #line:335
def main ():#line:338
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:339
    O0O00000O00O0O0O0 =os .getenv ('ydzck')#line:340
    if not O0O00000O00O0O0O0 :#line:341
        print ('仔细阅读脚本上方注释，配置好ydzck')#line:342
        return False #line:343
    try :#line:344
        O0O00000O00O0O0O0 =ast .literal_eval (O0O00000O00O0O0O0 )#line:345
    except :#line:346
        pass #line:347
    O0O0OO0000O0O0O0O =[]#line:348
    OOO0000O0OOOOO000 =Queue ()#line:349
    for O00OO0OO00OO0O0OO ,O0OOOOOO000000O00 in enumerate (O0O00000O00O0O0O0 ):#line:350
        printlog (f'{O0OOOOOO000000O00}\n以上是账号{O00OO0OO00OO0O0OO}的ck，请核对是否正确，如不正确，请检查ck填写格式')#line:351
        OOO0000O0OOOOO000 .put (O0OOOOOO000000O00 )#line:352
    for O00OO0OO00OO0O0OO in range (max_workers ):#line:353
        OO0OO0O00O00OO0OO =threading .Thread (target =yd ,args =(OOO0000O0OOOOO000 ,))#line:354
        OO0OO0O00O00OO0OO .start ()#line:355
        O0O0OO0000O0O0O0O .append (OO0OO0O00O00OO0OO )#line:356
        time .sleep (30 )#line:357
    for O000000O0O00O0000 in O0O0OO0000O0O0O0O :#line:358
        O000000O0O00O0000 .join ()#line:359
if __name__ =='__main__':#line:362
    main ()#line:363
