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


checklist =['MzU2OTczNzcwNg==','MzU5NTczMzA0MQ==','MzUwOTk5NDI0MQ==','MjM5Mjc5NjMyMw==','MzIxNjEzMDg2OQ==','MzUyMzk1MTAyNg==','MzI0MjE5MTc0OA==','MzU1ODI4MjI4Nw==','Mzg4OTA1MzI0Ng==','Mzg2MTI0Mzc1Nw==','MzU5NzgwMTgwMQ==','MzI3MTA5MTkwNQ==','Mzg5NjcyMzgyOA==','MjM5NjY4Mzk5OQ==','MzI1MDAwNDY1NA==','MjM5MTA5ODYzNQ==','MzAwNzA3MDAzMw==','MzkzMjUyNTk1OA==','MzAwNzA3MDAzMw==','MzI4NDY5MjkwNA==','MzIzNjgyOTE1Ng==','MzI2MjA0MzEwNA==','MzI0MjE5MTc0OA==','Mzg2NjExNDI2Mw==',]#line:92
def ftime ():#line:95
    O0000O00OO0OOOO0O =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:96
    return O0000O00OO0OOOO0O #line:97
def debugger (O0OO0OOOOO0000000 ):#line:100
    if debug :#line:101
        print (O0OO0OOOOO0000000 )#line:102
def printlog (OOO0OO0O0OOOOOO00 ):#line:105
    if printf :#line:106
        print (OOO0OO0O0OOOOOO00 )#line:107
def send (O00O0O00O0OOOOOOO ,title ='通知',url =None ):#line:110
    if not url :#line:111
        O0O0O0O00O00OO00O ={"msgtype":"text","text":{"content":f"{title}\n\n{O00O0O00O0OOOOOOO}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:118
    else :#line:119
        O0O0O0O00O00OO00O ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O00O0O00O0OOOOOOO ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:124
    OO000OO000O0O00O0 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:125
    O00O0OOOO000OOO0O =requests .post (OO000OO000O0O00O0 ,data =json .dumps (O0O0O0O00O00OO00O )).json ()#line:126
    if O00O0OOOO000OOO0O .get ('errcode')!=0 :#line:127
        print ('消息发送失败，请检查key和发送格式')#line:128
        return False #line:129
    return O00O0OOOO000OOO0O #line:130
def push (OOOOO000OOO0000O0 ,OO00O0OOOO000O000 ,OO0O0000OO00O00OO ,uid =None ):#line:133
    if uid :#line:134
        uids .append (uid )#line:135
    O00OO0O00O00OOO00 ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',OOOOO000OOO0000O0 ).replace ('url',OO0O0000OO00O00OO )#line:137
    O00O0000OOO000OO0 ={"appToken":appToken ,"content":O00OO0O00O00OOO00 ,"summary":OO00O0OOOO000O000 ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":OO0O0000OO00O00OO ,"verifyPay":False }#line:147
    OOOO0OOOOO0O0OO00 ='http://wxpusher.zjiecode.com/api/send/message'#line:148
    O0OO0OO00OOO0OO0O =requests .post (url =OOOO0OOOOO0O0OO00 ,json =O00O0000OOO000OO0 ).json ()#line:149
    if O0OO0OO00OOO0OO0O .get ('code')!=1000 :#line:150
        print (O0OO0OO00OOO0OO0O .get ('msg'),O0OO0OO00OOO0OO0O )#line:151
    return O0OO0OO00OOO0OO0O #line:152
def getmpinfo (O0000O0O0OOOOO00O ):#line:155
    if not O0000O0O0OOOOO00O or O0000O0O0OOOOO00O =='':#line:156
        return False #line:157
    OOOO0OOO0OO00O000 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:159
    O0OOOO00000O0O0O0 =requests .get (O0000O0O0OOOOO00O ,headers =OOOO0OOO0OO00O000 )#line:160
    OOOO0OOO00O00OOO0 =etree .HTML (O0OOOO00000O0O0O0 .text )#line:161
    O00OO00O00O0O0OO0 =OOOO0OOO00O00OOO0 .xpath ('//meta[@*="og:title"]/@content')#line:162
    if O00OO00O00O0O0OO0 :#line:163
        O00OO00O00O0O0OO0 =O00OO00O00O0O0OO0 [0 ]#line:164
    OOOOOO00O0000O000 =OOOO0OOO00O00OOO0 .xpath ('//meta[@*="og:url"]/@content')#line:165
    if OOOOOO00O0000O000 :#line:166
        OOOOOO00O0000O000 =OOOOOO00O0000O000 [0 ].encode ().decode ()#line:167
    try :#line:168
        OO000OOO0O00OOO0O =re .findall (r'biz=(.*?)&',O0000O0O0OOOOO00O )#line:169
    except :#line:170
        OO000OOO0O00OOO0O =re .findall (r'biz=(.*?)&',OOOOOO00O0000O000 )#line:171
    if OO000OOO0O00OOO0O :#line:172
        OO000OOO0O00OOO0O =OO000OOO0O00OOO0O [0 ]#line:173
    else :#line:174
        return False #line:175
    O00OOO0O000OOOO00 =OOOO0OOO00O00OOO0 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:176
    if O00OOO0O000OOOO00 :#line:177
        O00OOO0O000OOOO00 =O00OOO0O000OOOO00 [0 ].strip ()#line:178
    OO0O0OO0OO00OOO00 =re .findall (r"user_name.DATA'\) : '(.*?)'",O0OOOO00000O0O0O0 .text )or OOOO0OOO00O00OOO0 .xpath ('//span[@class="profile_meta_value"]/text()')#line:180
    if OO0O0OO0OO00OOO00 :#line:181
        OO0O0OO0OO00OOO00 =OO0O0OO0OO00OOO00 [0 ]#line:182
    OOO000OOOOO0O0000 =re .findall (r'createTime = \'(.*)\'',O0OOOO00000O0O0O0 .text )#line:183
    if OOO000OOOOO0O0000 :#line:184
        OOO000OOOOO0O0000 =OOO000OOOOO0O0000 [0 ][5 :]#line:185
    O00O00O00OOO000OO =f'{OOO000OOOOO0O0000}|{O00OO00O00O0O0OO0}|{OO000OOO0O00OOO0O}|{O00OOO0O000OOOO00}|{OO0O0OO0OO00OOO00}'#line:186
    OO0OO0OOOO0OOOOO0 ={'biz':OO000OOO0O00OOO0O ,'text':O00O00O00OOO000OO }#line:187
    return OO0OO0OOOO0OOOOO0 #line:188
class YDZ :#line:191
    def __init__ (OOO0O0O0OOOOOO00O ,OOOO0O00OO0OO0O0O ):#line:192
        OOO0O0O0OOOOOO00O .name =OOOO0O00OO0OO0O0O .get ('name')#line:193
        OOO0O0O0OOOOOO00O .s =requests .session ()#line:194
        OOO0O0O0OOOOOO00O .ck =OOOO0O00OO0OO0O0O .get ('ck')#line:195
        OOO0O0O0OOOOOO00O .msg =''#line:196
        OOO0O0O0OOOOOO00O .s .headers ={'Proxy-Connection':'keep-alive','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8431 Flue','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9','a_h_n':f'http%3A%2F%2F5851535337.udqyeba.cn%2F%3Fjgwq%3D3340348%26goid%3Ditrb/{OOO0O0O0OOOOOO00O.ck}','cookie':f'7bfe3c8f4d51851={OOO0O0O0OOOOOO00O.ck}'}#line:203
    def init (O00O0OO0O0O0O00OO ):#line:205
        try :#line:206
            O000OOO0O0O00O00O ='http://5851599460.udqyeba.cn/?jgwq=3340348&goid=itrb'#line:207
            OO0O0O0OO0000O00O =O00O0OO0O0O0O00OO .s .get (O000OOO0O0O00O00O ).text #line:208
            OO0O0O0OO0000O00O =re .sub ('\s','',OO0O0O0OO0000O00O )#line:210
            O00O0OO0O0O0O00OO .nickname =re .findall (r'nname=\'(.*?)\',',OO0O0O0OO0000O00O )[0 ]#line:211
            OO000O000000O00OO =re .findall (r'uid=\'(\d+)\'',OO0O0O0OO0000O00O )[0 ]#line:212
            O00O0OO0OOOO000OO =f'http://58515{random.randint(10000, 99999)}.udqyeba.cn/?jgwq={OO000O000000O00OO}&goid=itrb/{O00O0OO0O0O0O00OO.ck}'#line:213
            O00O0OO0O0O0O00OO .s .headers .update ({'a_h_n':O00O0OO0OOOO000OO })#line:214
            return True #line:215
        except :#line:216
            printlog (f'{O00O0OO0O0O0O00OO.name} 账号信息获取错误，请检查ck有效性')#line:217
            O00O0OO0O0O0O00OO .msg +='账号信息获取错误，请检查ck有效性\n'#line:218
            return False #line:219
    def getinfo (O000OOO0O0O0O0OOO ):#line:221
        O0000OO000O000O00 ='http://wxr.jjyii.com/user/getinfo?v=3'#line:222
        O00OO00OO000OOO0O =O000OOO0O0O0O0OOO .s .get (O0000OO000O000O00 ).json ()#line:223
        debugger (f'getinfo2 {O00OO00OO000OOO0O}')#line:224
        OOO0OOO0OOOO0000O =O00OO00OO000OOO0O .get ('data')#line:225
        O000OOO0O0O0O0OOO .count =OOO0OOO0OOOO0000O .get ('count')#line:226
        O000OOO0O0O0O0OOO .gold =OOO0OOO0OOOO0000O .get ('balance')#line:227
        OOOOO0OO000OOO00O =OOO0OOO0OOOO0000O .get ('hm')#line:228
        O000OOO0OOOOO0O00 =OOO0OOO0OOOO0000O .get ('hs')#line:229
        printlog (f'账号:{O000OOO0O0O0O0OOO.nickname},当前金币{O000OOO0O0O0O0OOO.gold}，今日已读{O000OOO0O0O0O0OOO.count}')#line:230
        O000OOO0O0O0O0OOO .msg +=f'账号:{O000OOO0O0O0O0OOO.nickname},当前金币{O000OOO0O0O0O0OOO.gold}，今日已读{O000OOO0O0O0O0OOO.count}\n'#line:231
        if OOOOO0OO000OOO00O !=0 or O000OOO0OOOOO0O00 !=0 :#line:232
            printlog (f'{O000OOO0O0O0O0OOO.nickname} 本轮次已结束，{OOOOO0OO000OOO00O}分钟后可继续任务')#line:233
            O000OOO0O0O0O0OOO .msg +='本轮次已结束，{hm}分钟后可继续任务\n'#line:234
            return False #line:235
        return True #line:236
    def read (O0000O00OO0O000O0 ):#line:238
        OO00O0O00OO00OO0O ='http://wxr.jjyii.com/r/get?v=10'#line:239
        OO0O00OO000OOO00O ={'o':f'http://58517{random.randint(10000, 99999)}.ulzqwjf.cn/?a=gt','goid':'itrb','_v':'3890','t':'quick'}#line:241
        OOO000OO000O000O0 =0 #line:242
        OO0OOOO0O0OOOOOOO =0 #line:243
        while OOO000OO000O000O0 <30 and OO0OOOO0O0OOOOOOO <5 :#line:244
            if not O0000O00OO0O000O0 .getinfo ():#line:245
                break #line:246
            O000OO00O0OOO00OO =O0000O00OO0O000O0 .s .post (OO00O0O00OO00OO0O ,data =OO0O00OO000OOO00O ).json ()#line:247
            debugger (f'read {O000OO00O0OOO00OO}')#line:248
            O0000OO0O0O0O00OO =O000OO00O0OOO00OO .get ('data').get ('url')#line:249
            if not O0000OO0O0O0O00OO :#line:250
                printlog (f'{O0000O00OO0O000O0.nickname} 没有获取到阅读链接，正在重试')#line:251
                O0000O00OO0O000O0 .msg +='没有获取到阅读链接，正在重试\n'#line:252
                time .sleep (5 )#line:253
                OO0OOOO0O0OOOOOOO +=1 #line:254
                continue #line:255
            OOOO0OOO00OO0O00O =getmpinfo (O0000OO0O0O0O00OO )#line:256
            try :#line:257
                printlog (f'{O0000O00OO0O000O0.nickname} 正在阅读 {OOOO0OOO00OO0O00O["text"]}')#line:258
                O0000O00OO0O000O0 .msg +=f'正在阅读 {OOOO0OOO00OO0O00O["text"]}\n'#line:259
            except :#line:260
                printlog (f'{O0000O00OO0O000O0.nickname} 正在阅读 {OOOO0OOO00OO0O00O["biz"]}')#line:261
                O0000O00OO0O000O0 .msg +=f'正在阅读 {OOOO0OOO00OO0O00O["biz"]}\n'#line:262
            if 'chksm='in O0000OO0O0O0O00OO or (OOOO0OOO00OO0O00O ["biz"]in checklist ):#line:263
                printlog (f'{O0000O00OO0O000O0.nickname} 正在阅读检测文章，发送通知，暂停60秒')#line:264
                O0000O00OO0O000O0 .msg +='正在阅读检测文章，发送通知，暂停60秒\n'#line:265
                if sendable :#line:266
                    send (f'{O0000O00OO0O000O0.nickname}\n点击阅读检测文章',f'{O0000O00OO0O000O0.name} 阅读赚过检测',O0000OO0O0O0O00OO )#line:267
                if pushable :#line:268
                    push (f'{O0000O00OO0O000O0.nickname}\n点击阅读检测文章\n{OOOO0OOO00OO0O00O["text"]}',f'{O0000O00OO0O000O0.name} 阅读赚过检测',O0000OO0O0O0O00OO )#line:269
                time .sleep (60 )#line:270
            OO0OO00O0O00O000O =random .randint (7 ,10 )#line:271
            O0000O00OO0O000O0 .msg +='模拟阅读{t}秒\n'#line:272
            time .sleep (OO0OO00O0O00O000O )#line:273
            OOOOO0OOOO00OO000 ='http://wxr.jjyii.com/r/ck'#line:274
            O00OOOOO000000OOO ={'Accept':'application/json, text/javascript, */*; q=0.01','Origin':'http://5851780833.ebrmrwy.cn','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',}#line:277
            O0000O00OO0O000O0 .s .headers .update (O00OOOOO000000OOO )#line:278
            O000OO00O0OOO00OO =O0000O00OO0O000O0 .s .post (OOOOO0OOOO00OO000 ,data ={'t':'quick'}).json ()#line:279
            debugger (f'check {O000OO00O0OOO00OO}')#line:280
            OOOO00OO0OOO000O0 =O000OO00O0OOO00OO .get ('data').get ('gold')#line:281
            if OOOO00OO0OOO000O0 :#line:282
                printlog (f'{O0000O00OO0O000O0.nickname} 阅读成功，获得金币{OOOO00OO0OOO000O0}')#line:283
                O0000O00OO0O000O0 .msg +=f'阅读成功，获得金币{OOOO00OO0OOO000O0}\n'#line:284
            OOO000OO000O000O0 +=1 #line:285
    def cash (OO00O00OO0O0OO0O0 ):#line:287
        if OO00O00OO0O0OO0O0 .gold <txbz :#line:288
            printlog (f'{OO00O00OO0O0OO0O0.nickname} 你的金币不多了')#line:289
            OO00O00OO0O0OO0O0 .msg +='你的金币不多了\n'#line:290
            return False #line:291
        O0O0OOO00O00O0OO0 =int (OO00O00OO0O0OO0O0 .gold /1000 )*1000 #line:292
        printlog (f'{OO00O00OO0O0OO0O0.nickname} 本次提现：{O0O0OOO00O00O0OO0}')#line:293
        OO00O00OO0O0OO0O0 .msg +=f'本次提现：{O0O0OOO00O00O0OO0}\n'#line:294
        OOOO0O0OO00OO00O0 ='http://wxr.jjyii.com/mine/cash'#line:295
        OOOO0O000O000OOOO =OO00O00OO0O0OO0O0 .s .post (OOOO0O0OO00OO00O0 )#line:296
        if OOOO0O000O000OOOO .json ().get ('code')==1 :#line:297
            printlog (f'{OO00O00OO0O0OO0O0.nickname} 提现成功')#line:298
            OO00O00OO0O0OO0O0 .msg +='提现成功\n'#line:299
        else :#line:300
            debugger (OOOO0O000O000OOOO .text )#line:301
            printlog (f'{OO00O00OO0O0OO0O0.nickname} 提现失败')#line:302
            OO00O00OO0O0OO0O0 .msg +='提现失败\n'#line:303
    def run (O0OOOOOO0O00O000O ):#line:305
        if O0OOOOOO0O00O000O .init ():#line:306
            O0OOOOOO0O00O000O .read ()#line:307
        O0OOOOOO0O00O000O .cash ()#line:308
        if not printf :#line:309
            print (O0OOOOOO0O00O000O .msg )#line:310
def yd (OO0OO00OO0O0OOOOO ):#line:313
    while not OO0OO00OO0O0OOOOO .empty ():#line:314
        OO0OO0O0OO00O00OO =OO0OO00OO0O0OOOOO .get ()#line:315
        O00OO0OOO000O0000 =YDZ (OO0OO0O0OO00O00OO )#line:316
        O00OO0OOO000O0000 .run ()#line:317
def get_ver ():#line:320
    OO0O000000OO00OOO ='kydz V0.1.6'#line:321
    O0O00OO0OOOO0O000 ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:324
    O0OOOO0OO0OOOOOOO =requests .get ('https://ghproxy.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json',headers =O0O00OO0OOOO0O000 ).json ()#line:326
    OO00O000OO000O0OO =OO0O000000OO00OOO .split (' ')[1 ]#line:327
    OOO00000OOO00000O =O0OOOO0OO0OOOOOOO .get ('version').get (OO0O000000OO00OOO .split (' ')[0 ])#line:328
    O00O0OOOO0000OOOO =f"当前版本 {OO00O000OO000O0OO}，仓库版本 {OOO00000OOO00000O}"#line:329
    if OO00O000OO000O0OO <OOO00000OOO00000O :#line:330
        O00O0OOOO0000OOOO +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:331
    return O00O0OOOO0000OOOO #line:332
def main ():#line:335
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:336
    O0OOOO0000O0O0OOO =os .getenv ('ydzck')#line:337
    if not O0OOOO0000O0O0OOO :#line:338
        print ('仔细阅读脚本上方注释，配置好ydzck')#line:339
        return False #line:340
    try :#line:341
        O0OOOO0000O0O0OOO =ast .literal_eval (O0OOOO0000O0O0OOO )#line:342
    except :#line:343
        pass #line:344
    OO00O00OOOOOO0OO0 =[]#line:345
    OOO00O0OO000O000O =Queue ()#line:346
    for OOOOO0O0OOOO0OOO0 ,O00OOOO000OOOO00O in enumerate (O0OOOO0000O0O0OOO ):#line:347
        printlog (f'{O00OOOO000OOOO00O}\n以上是账号{OOOOO0O0OOOO0OOO0}的ck，请核对是否正确，如不正确，请检查ck填写格式')#line:348
        OOO00O0OO000O000O .put (O00OOOO000OOOO00O )#line:349
    for OOOOO0O0OOOO0OOO0 in range (max_workers ):#line:350
        OO0OOOO0OOO0O0OOO =threading .Thread (target =yd ,args =(OOO00O0OO000O000O ,))#line:351
        OO0OOOO0OOO0O0OOO .start ()#line:352
        OO00O00OOOOOO0OO0 .append (OO0OOOO0OOO0O0OOO )#line:353
        time .sleep (30 )#line:354
    for O000OOO000OO00O00 in OO00O00OOOOOO0OO0 :#line:355
        O000OOO000OO00O00 .join ()#line:356
if __name__ =='__main__':#line:359
    main ()#line:360
