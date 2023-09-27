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
    OOOO000O0OOO000O0 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:98
    return OOOO000O0OOO000O0 #line:99
def debugger (OOO0O0OOO000O000O ):#line:102
    if debug :#line:103
        print (OOO0O0OOO000O000O )#line:104
def printlog (O00O0OOOOOO0OO000 ):#line:107
    if printf :#line:108
        print (O00O0OOOOOO0OO000 )#line:109
def send (OO00000OOO0OOOO00 ,title ='通知',url =None ):#line:112
    if not url :#line:113
        O0O0000OO00000O00 ={"msgtype":"text","text":{"content":f"{title}\n\n{OO00000OOO0OOOO00}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:120
    else :#line:121
        O0O0000OO00000O00 ={"msgtype":"news","news":{"articles":[{"title":title ,"description":OO00000OOO0OOOO00 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:126
    O000000OO0000OO00 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:127
    O0OO00OOOOOO00000 =requests .post (O000000OO0000OO00 ,data =json .dumps (O0O0000OO00000O00 )).json ()#line:128
    if O0OO00OOOOOO00000 .get ('errcode')!=0 :#line:129
        print ('消息发送失败，请检查key和发送格式')#line:130
        return False #line:131
    return O0OO00OOOOOO00000 #line:132
def push (O00000O0OO0OO00OO ,O0O000000O00OO0OO ,OO00OOOOOO000O0O0 ,uid =None ):#line:135
    if uid :#line:136
        uids .append (uid )#line:137
    OOOO0OOO000OOO0O0 ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',O00000O0OO0OO00OO ).replace ('url',OO00OOOOOO000O0O0 )#line:139
    OO0O0O0OOO0OO000O ={"appToken":appToken ,"content":OOOO0OOO000OOO0O0 ,"summary":O0O000000O00OO0OO ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":OO00OOOOOO000O0O0 ,"verifyPay":False }#line:149
    O000O0O0OOOOO0OOO ='http://wxpusher.zjiecode.com/api/send/message'#line:150
    OOOO0OO00O0O0OOO0 =requests .post (url =O000O0O0OOOOO0OOO ,json =OO0O0O0OOO0OO000O ).json ()#line:151
    if OOOO0OO00O0O0OOO0 .get ('code')!=1000 :#line:152
        print (OOOO0OO00O0O0OOO0 .get ('msg'),OOOO0OO00O0O0OOO0 )#line:153
    return OOOO0OO00O0O0OOO0 #line:154
def getmpinfo (OOO0OOOOOO0O00OO0 ):#line:157
    if not OOO0OOOOOO0O00OO0 or OOO0OOOOOO0O00OO0 =='':#line:158
        return False #line:159
    O00OO0O000OO000OO ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:161
    O0OO0O0000O000OOO =requests .get (OOO0OOOOOO0O00OO0 ,headers =O00OO0O000OO000OO )#line:162
    OOOO0OOOOOOOOO0O0 =etree .HTML (O0OO0O0000O000OOO .text )#line:163
    O00O0000OO0O0O000 =OOOO0OOOOOOOOO0O0 .xpath ('//meta[@*="og:title"]/@content')#line:164
    if O00O0000OO0O0O000 :#line:165
        O00O0000OO0O0O000 =O00O0000OO0O0O000 [0 ]#line:166
    O0OO00OO000O00O00 =OOOO0OOOOOOOOO0O0 .xpath ('//meta[@*="og:url"]/@content')#line:167
    if O0OO00OO000O00O00 :#line:168
        O0OO00OO000O00O00 =O0OO00OO000O00O00 [0 ].encode ().decode ()#line:169
    try :#line:170
        O0000OO0OOOO00000 =re .findall (r'biz=(.*?)&',OOO0OOOOOO0O00OO0 )#line:171
    except :#line:172
        O0000OO0OOOO00000 =re .findall (r'biz=(.*?)&',O0OO00OO000O00O00 )#line:173
    if O0000OO0OOOO00000 :#line:174
        O0000OO0OOOO00000 =O0000OO0OOOO00000 [0 ]#line:175
    else :#line:176
        return False #line:177
    OOO000O000000O0O0 =OOOO0OOOOOOOOO0O0 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:178
    if OOO000O000000O0O0 :#line:179
        OOO000O000000O0O0 =OOO000O000000O0O0 [0 ].strip ()#line:180
    O00OO0O00O000O00O =re .findall (r"user_name.DATA'\) : '(.*?)'",O0OO0O0000O000OOO .text )or OOOO0OOOOOOOOO0O0 .xpath ('//span[@class="profile_meta_value"]/text()')#line:182
    if O00OO0O00O000O00O :#line:183
        O00OO0O00O000O00O =O00OO0O00O000O00O [0 ]#line:184
    O0000O00OOOO00OOO =re .findall (r'createTime = \'(.*)\'',O0OO0O0000O000OOO .text )#line:185
    if O0000O00OOOO00OOO :#line:186
        O0000O00OOOO00OOO =O0000O00OOOO00OOO [0 ][5 :]#line:187
    O00O0OO0O00OOOO0O =f'{O0000O00OOOO00OOO}|{O00O0000OO0O0O000}|{O0000OO0OOOO00000}|{OOO000O000000O0O0}|{O00OO0O00O000O00O}'#line:188
    OOOOO000OO00OO0OO ={'biz':O0000OO0OOOO00000 ,'text':O00O0OO0O00OOOO0O }#line:189
    return OOOOO000OO00OO0OO #line:190
class YDZ :#line:193
    def __init__ (O0OOO0OO00O00OOOO ,O000OO00O0OO00OO0 ):#line:194
        O0OOO0OO00O00OOOO .uid =O000OO00O0OO00OO0 .get ('uid')#line:195
        O0OOO0OO00O00OOOO .name =O000OO00O0OO00OO0 .get ('name')#line:196
        O0OOO0OO00O00OOOO .s =requests .session ()#line:197
        O0OOO0OO00O00OOOO .ck =O000OO00O0OO00OO0 .get ('ck')#line:198
        O0OOO0OO00O00OOOO .msg =''#line:199
        O0OOO0OO00O00OOOO .s .headers ={'Proxy-Connection':'keep-alive','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8431 Flue','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9','a_h_n':f'http%3A%2F%2F5851535337.udqyeba.cn%2F%3Fjgwq%3D3340348%26goid%3Ditrb/{O0OOO0OO00O00OOOO.ck}','cookie':f'7bfe3c8f4d51851={O0OOO0OO00O00OOOO.ck}'}#line:206
    def init (OO0O00O00OO0O00OO ):#line:208
        try :#line:209
            O0OO0OOOOOO0OO0O0 ='http://5851599460.udqyeba.cn/?jgwq=3340348&goid=itrb'#line:210
            OO0O0O0OOOO0OOOO0 =OO0O00O00OO0O00OO .s .get (O0OO0OOOOOO0OO0O0 ).text #line:211
            OO0O0O0OOOO0OOOO0 =re .sub ('\s','',OO0O0O0OOOO0OOOO0 )#line:213
            OO0O00O00OO0O00OO .nickname =re .findall (r'nname=\'(.*?)\',',OO0O0O0OOOO0OOOO0 )[0 ]#line:214
            O0OOOOO00OOOOO00O =re .findall (r'uid=\'(\d+)\'',OO0O0O0OOOO0OOOO0 )[0 ]#line:215
            O000OOOO0O0OOOOOO =f'http://58515{random.randint(10000, 99999)}.udqyeba.cn/?jgwq={O0OOOOO00OOOOO00O}&goid=itrb/{OO0O00O00OO0O00OO.ck}'#line:216
            OO0O00O00OO0O00OO .s .headers .update ({'a_h_n':O000OOOO0O0OOOOOO })#line:217
            return True #line:218
        except :#line:219
            printlog (f'{OO0O00O00OO0O00OO.name} 账号信息获取错误，请检查ck有效性')#line:220
            OO0O00O00OO0O00OO .msg +='账号信息获取错误，请检查ck有效性\n'#line:221
            return False #line:222
    def getinfo (OO00O000O0OOO00O0 ):#line:224
        O0000O0O0OOO00O0O ='http://wxr.jjyii.com/user/getinfo?v=3'#line:225
        OO00O000O00OO0000 =OO00O000O0OOO00O0 .s .get (O0000O0O0OOO00O0O ).json ()#line:226
        debugger (f'getinfo2 {OO00O000O00OO0000}')#line:227
        OO000OOOO0000O0OO =OO00O000O00OO0000 .get ('data')#line:228
        OO00O000O0OOO00O0 .count =OO000OOOO0000O0OO .get ('count')#line:229
        OO00O000O0OOO00O0 .gold =OO000OOOO0000O0OO .get ('balance')#line:230
        OO0O0OO0OOO0O000O =OO000OOOO0000O0OO .get ('hm')#line:231
        O0O00000OOO0OOOO0 =OO000OOOO0000O0OO .get ('hs')#line:232
        printlog (f'账号:{OO00O000O0OOO00O0.nickname},当前金币{OO00O000O0OOO00O0.gold}，今日已读{OO00O000O0OOO00O0.count}')#line:233
        OO00O000O0OOO00O0 .msg +=f'账号:{OO00O000O0OOO00O0.nickname},当前金币{OO00O000O0OOO00O0.gold}，今日已读{OO00O000O0OOO00O0.count}\n'#line:234
        if OO0O0OO0OOO0O000O !=0 or O0O00000OOO0OOOO0 !=0 :#line:235
            printlog (f'{OO00O000O0OOO00O0.nickname} 本轮次已结束，{OO0O0OO0OOO0O000O}分钟后可继续任务')#line:236
            OO00O000O0OOO00O0 .msg +='本轮次已结束，{hm}分钟后可继续任务\n'#line:237
            return False #line:238
        return True #line:239
    def read (OO0OOO00OOO00O000 ):#line:241
        O0OOO0OO0OO00OO0O ='http://wxr.jjyii.com/r/get?v=10'#line:242
        O0000O00OOO0OO00O ={'o':f'http://58517{random.randint(10000, 99999)}.ulzqwjf.cn/?a=gt','goid':'itrb','_v':'3890','t':'quick'}#line:244
        O000OO00O00OOOOO0 =0 #line:245
        O0OO0O0000OOO000O =0 #line:246
        while O000OO00O00OOOOO0 <30 and O0OO0O0000OOO000O <5 :#line:247
            if not OO0OOO00OOO00O000 .getinfo ():#line:248
                break #line:249
            OOO000OOOO0OO0O0O =OO0OOO00OOO00O000 .s .post (O0OOO0OO0OO00OO0O ,data =O0000O00OOO0OO00O ).json ()#line:250
            debugger (f'read {OOO000OOOO0OO0O0O}')#line:251
            if OOO000OOOO0OO0O0O .get ('data').get ('uiv'):#line:252
                printlog (f'{OO0OOO00OOO00O000.nickname} 号已黑，明天继续')#line:253
                OO0OOO00OOO00O000 .msg +=f'号已黑，明天继续\n'#line:254
                break #line:255
            OO0OO0OOO00000OOO =OOO000OOOO0OO0O0O .get ('data').get ('url')#line:256
            if not OO0OO0OOO00000OOO :#line:257
                printlog (f'{OO0OOO00OOO00O000.nickname} 没有获取到阅读链接，正在重试')#line:258
                OO0OOO00OOO00O000 .msg +='没有获取到阅读链接，正在重试\n'#line:259
                time .sleep (5 )#line:260
                O0OO0O0000OOO000O +=1 #line:261
                continue #line:262
            O00OO0OOOOOO000O0 =getmpinfo (OO0OO0OOO00000OOO )#line:263
            try :#line:264
                printlog (f'{OO0OOO00OOO00O000.nickname} 正在阅读 {O00OO0OOOOOO000O0["text"]}')#line:265
                OO0OOO00OOO00O000 .msg +=f'正在阅读 {O00OO0OOOOOO000O0["text"]}\n'#line:266
            except :#line:267
                printlog (f'{OO0OOO00OOO00O000.nickname} 正在阅读 {O00OO0OOOOOO000O0["biz"]}')#line:268
                OO0OOO00OOO00O000 .msg +=f'正在阅读 {O00OO0OOOOOO000O0["biz"]}\n'#line:269
            if 'chksm'in OO0OO0OOO00000OOO or (O00OO0OOOOOO000O0 ["biz"]in checklist ):#line:270
                printlog (f'{OO0OOO00OOO00O000.nickname} 正在阅读检测文章，发送通知，暂停60秒')#line:271
                OO0OOO00OOO00O000 .msg +='正在阅读检测文章，发送通知，暂停60秒\n'#line:272
                if sendable :#line:273
                    send (f'{OO0OOO00OOO00O000.nickname}\n点击阅读检测文章',f'{OO0OOO00OOO00O000.name} 阅读赚过检测',OO0OO0OOO00000OOO )#line:274
                if pushable :#line:275
                    push (f'{OO0OOO00OOO00O000.nickname}\n点击阅读检测文章\n{O00OO0OOOOOO000O0["text"]}',f'{OO0OOO00OOO00O000.name} 阅读赚过检测',OO0OO0OOO00000OOO ,OO0OOO00OOO00O000 .uid )#line:276
                time .sleep (60 )#line:277
            O0O0O000OO000O0O0 =random .randint (7 ,10 )#line:278
            OO0OOO00OOO00O000 .msg +='模拟阅读{t}秒\n'#line:279
            time .sleep (O0O0O000OO000O0O0 )#line:280
            OOO00O0O00O00000O ='http://wxr.jjyii.com/r/ck'#line:281
            O00O000O0OO00O0OO ={'Accept':'application/json, text/javascript, */*; q=0.01','Origin':'http://5851780833.ebrmrwy.cn','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',}#line:284
            OO0OOO00OOO00O000 .s .headers .update (O00O000O0OO00O0OO )#line:285
            OOO000OOOO0OO0O0O =OO0OOO00OOO00O000 .s .post (OOO00O0O00O00000O ,data ={'t':'quick'}).json ()#line:286
            debugger (f'check {OOO000OOOO0OO0O0O}')#line:287
            O000OOOOOO000O0OO =OOO000OOOO0OO0O0O .get ('data').get ('gold')#line:288
            if O000OOOOOO000O0OO :#line:289
                printlog (f'{OO0OOO00OOO00O000.nickname} 阅读成功，获得金币{O000OOOOOO000O0OO}')#line:290
                OO0OOO00OOO00O000 .msg +=f'阅读成功，获得金币{O000OOOOOO000O0OO}\n'#line:291
            O000OO00O00OOOOO0 +=1 #line:292
    def cash (OO0000OO00O0O00OO ):#line:294
        if OO0000OO00O0O00OO .gold <txbz :#line:295
            printlog (f'{OO0000OO00O0O00OO.nickname} 你的金币不多了')#line:296
            OO0000OO00O0O00OO .msg +='你的金币不多了\n'#line:297
            return False #line:298
        O0OOO0O0OOO000OOO =int (OO0000OO00O0O00OO .gold /1000 )*1000 #line:299
        printlog (f'{OO0000OO00O0O00OO.nickname} 本次提现：{O0OOO0O0OOO000OOO}')#line:300
        OO0000OO00O0O00OO .msg +=f'本次提现：{O0OOO0O0OOO000OOO}\n'#line:301
        OOO00OO000OO000O0 ='http://wxr.jjyii.com/mine/cash'#line:302
        OOOOOOO0O0OOOOO00 =OO0000OO00O0O00OO .s .post (OOO00OO000OO000O0 )#line:303
        if OOOOOOO0O0OOOOO00 .json ().get ('code')==1 :#line:304
            printlog (f'{OO0000OO00O0O00OO.nickname} 提现成功')#line:305
            OO0000OO00O0O00OO .msg +='提现成功\n'#line:306
        else :#line:307
            debugger (OOOOOOO0O0OOOOO00 .text )#line:308
            printlog (f'{OO0000OO00O0O00OO.nickname} 提现失败')#line:309
            OO0000OO00O0O00OO .msg +='提现失败\n'#line:310
    def run (O000O0OOOOOOOOOO0 ):#line:312
        if O000O0OOOOOOOOOO0 .init ():#line:313
            O000O0OOOOOOOOOO0 .read ()#line:314
        O000O0OOOOOOOOOO0 .cash ()#line:315
        if not printf :#line:316
            print (O000O0OOOOOOOOOO0 .msg )#line:317
def yd (O0000O0000O0OOO00 ):#line:320
    while not O0000O0000O0OOO00 .empty ():#line:321
        OO00000O0OO00OO0O =O0000O0000O0OOO00 .get ()#line:322
        OO0O000OOO0000O0O =YDZ (OO00000O0OO00OO0O )#line:323
        OO0O000OOO0000O0O .run ()#line:324
def get_ver ():#line:327
    OO0O0OO0OOOO0OO00 ='kydz V0.1.7'#line:328
    OO00O0OOOOOO00000 ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:331
    OOO000000OOOOOOOO =requests .get ('https://ghproxy.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json',headers =OO00O0OOOOOO00000 ).json ()#line:333
    O00OO0OO000OOOOO0 =OO0O0OO0OOOO0OO00 .split (' ')[1 ]#line:334
    O000000000000000O =OOO000000OOOOOOOO .get ('version').get (OO0O0OO0OOOO0OO00 .split (' ')[0 ])#line:335
    O0O0OO0O00O00O0O0 =f"当前版本 {O00OO0OO000OOOOO0}，仓库版本 {O000000000000000O}"#line:336
    if O00OO0OO000OOOOO0 <O000000000000000O :#line:337
        O0O0OO0O00O00O0O0 +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:338
    return O0O0OO0O00O00O0O0 #line:339
def main ():#line:342
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:343
    O000O0OO0OOOO00OO =os .getenv ('ydzck')#line:344
    if not O000O0OO0OOOO00OO :#line:345
        print ('仔细阅读脚本上方注释，配置好ydzck')#line:346
        return False #line:347
    try :#line:348
        O000O0OO0OOOO00OO =ast .literal_eval (O000O0OO0OOOO00OO )#line:349
    except :#line:350
        pass #line:351
    OO00OO00O0000OOO0 =[]#line:352
    O00O0OO0OO0OOOOOO =Queue ()#line:353
    for O0O00OO00O0000OO0 ,OOO00O000OOO0O0O0 in enumerate (O000O0OO0OOOO00OO ):#line:354
        printlog (f'{OOO00O000OOO0O0O0}\n以上是账号{O0O00OO00O0000OO0}的ck，请核对是否正确，如不正确，请检查ck填写格式')#line:355
        O00O0OO0OO0OOOOOO .put (OOO00O000OOO0O0O0 )#line:356
    for O0O00OO00O0000OO0 in range (max_workers ):#line:357
        OO00O00O00OO0O00O =threading .Thread (target =yd ,args =(O00O0OO0OO0OOOOOO ,))#line:358
        OO00O00O00OO0O00O .start ()#line:359
        OO00OO00O0000OOO0 .append (OO00O00O00OO0O00O )#line:360
        time .sleep (30 )#line:361
    for OOOOO000O00OO0000 in OO00OO00O0000OOO0 :#line:362
        OOOOO000O00OO0000 .join ()#line:363
if __name__ =='__main__':#line:366
    main ()#line:367
