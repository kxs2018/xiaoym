# -*- coding: utf-8 -*-
# k每天赚
# Author: kk
# date：2023/9/26
"""
每天赚入口：http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552
推送检测文章
1.通过企业微信机器人推送到企业微信群，请务必用微信关注微信插件并配置好机器人key
export qwbotkey="xxxxxxxxx"
参考https://github.com/kxs2018/yuedu/blob/main/获取企业微信群机器人key.md 获取key，并关注插件！！！
2.wxpusher公众号
参考https://wxpusher.zjiecode.com/docs/#/ 获取apptoken、topicids、uids，填入pushconfig
export pushconfig="{'appToken': 'AT_pCenRjs', 'uids': ['UID_9MZ','UID_T4xlqWx9x'], 'topicids': [''],}"
单发时无需设置uids topicids，留空，在mtzck中配置uid

打开活动入口，抓包的任意接口headers中的Authorization参数，填入ck。
单账户填写样式(这里只是样式，不要填这里)
export mtzck="[{'name': 'xxx', 'ck': 'share:login:xxxx'},]"
多账户填写样式，几个账号填几个，不要多填。(这里只是样式，不要填这里)
export mtzck="[{'name': 'xxx', 'ck': 'share:login:xxxx','uid':'UID_9MZ'},{'name': 'xxx', 'ck': 'share:login:xxxx'}]"
其中uid为wxpusher单对单发送通知专用，群发和企业微信无需配置

V1.6起支持逐个账号添加到环境变量
如我有2个账号，新建一个变量名mtzck 值为{"name": "1", "ck": "share:login:xxxx","uid":"UID_9MZ"}
再新建一个变量mtzck 值为{"name": "2", "ck": "share:login:xxxx","uid":"UID_9MZ"}


参数解释
name:账号名，你可以随便填，用来推送时分辨哪一个账号
ck:账号的ck,抓包的任意接口headers中的Authorization参数，格式为share:login:xxxx
------------------------------------------------------------------------
运行提示 no module named lxml 解决方法
1. 在配置文件找到
## 安装python依赖时指定pip源
PipMirror="https://pypi.tuna.tsinghua.edu.cn/simple"
如果这条链接包含douban的，换成和上面一样的
2. 依赖-python 添加lxml
3. 如果装不上，尝试升级pip：①ssh连接到服务器 ②docker exec -it ql bash ③pip install pip -U
ql是青龙容器的名字，docker ps可查询
"""

import json
import os
import random
import requests
import re
import time
import ast

try:
    from lxml import etree
except:
    print('请仔细阅读脚本上方注释中的“no module named lxml 解决方案”')
    exit()
import datetime
import threading
from queue import Queue

"""实时日志开关"""
printf = 1
"""1为开，0为关"""

"""debug模式开关"""
debug = 1
"""1为开，打印调试日志；0为关，不打印"""

"""线程数量设置"""
max_workers = 5
"""填入数字，设置同时跑任务的数量"""

"""设置提现标准"""
txbz = 1000  # 不低于1000，平台的提现标准为1000
"""设置为1000，即为1元起提"""

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


def ftime ():#line:102
    O0OOOO0O0O00OOOOO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:103
    return O0OOOO0O0O00OOOOO #line:104
def debugger (OO00000O000OOOOOO ):#line:107
    if debug :#line:108
        print (OO00000O000OOOOOO )#line:109
def printlog (O0OO000OO0O00O0OO ):#line:112
    if printf :#line:113
        print (O0OO000OO0O00O0OO )#line:114
def send (O000O0O00OO0OOO0O ,title ='通知',url =None ):#line:117
    if not url :#line:118
        O00O000O0000OO00O ={"msgtype":"text","text":{"content":f"{title}\n\n{O000O0O00OO0OOO0O}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:125
    else :#line:126
        O00O000O0000OO00O ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O000O0O00OO0OOO0O ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:131
    OOO00OOOO00OO0000 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:132
    OO0OOOO0OOOO00OOO =requests .post (OOO00OOOO00OO0000 ,data =json .dumps (O00O000O0000OO00O )).json ()#line:133
    if OO0OOOO0OOOO00OOO .get ('errcode')!=0 :#line:134
        print ('消息发送失败，请检查key和发送格式')#line:135
        return False #line:136
    return OO0OOOO0OOOO00OOO #line:137
def push (OOO00OO0O0O0O00O0 ,O0OOO000000O000O0 ,url ='',uid =None ):#line:140
    if uid :#line:141
        uids .append (uid )#line:142
    OOO00O0OO0000OO0O ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',OOO00OO0O0O0O00O0 ).replace ('url',url )#line:144
    OOO00O0O000O00OO0 ={"appToken":appToken ,"content":OOO00O0OO0000OO0O ,"summary":O0OOO000000O000O0 ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:154
    OO00000OOOO0O000O ='http://wxpusher.zjiecode.com/api/send/message'#line:155
    O0OO0000OO00OOO0O =requests .post (url =OO00000OOOO0O000O ,json =OOO00O0O000O00OO0 ).json ()#line:156
    if O0OO0000OO00OOO0O .get ('code')!=1000 :#line:157
        print (O0OO0000OO00OOO0O .get ('msg'),O0OO0000OO00OOO0O )#line:158
    return O0OO0000OO00OOO0O #line:159
def getmpinfo (O00OO0000O000O0OO ):#line:162
    if not O00OO0000O000O0OO or O00OO0000O000O0OO =='':#line:163
        return False #line:164
    O000O00OOOO00O00O ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:166
    O0O0OO00OOOOOO00O =requests .get (O00OO0000O000O0OO ,headers =O000O00OOOO00O00O )#line:167
    OOO00O000O0OO00O0 =etree .HTML (O0O0OO00OOOOOO00O .text )#line:168
    O0OO0OO00O000O0O0 =OOO00O000O0OO00O0 .xpath ('//meta[@*="og:title"]/@content')#line:169
    if O0OO0OO00O000O0O0 :#line:170
        O0OO0OO00O000O0O0 =O0OO0OO00O000O0O0 [0 ]#line:171
    O0O00OO0000000000 =OOO00O000O0OO00O0 .xpath ('//meta[@*="og:url"]/@content')#line:172
    if O0O00OO0000000000 :#line:173
        O0O00OO0000000000 =O0O00OO0000000000 [0 ].encode ().decode ()#line:174
    O0O000OOO0O0O00OO =re .findall (r'biz=(.*?)&',O00OO0000O000O0OO )or re .findall (r'biz=(.*?)&',O0O00OO0000000000 )#line:175
    if O0O000OOO0O0O00OO :#line:176
        O0O000OOO0O0O00OO =O0O000OOO0O0O00OO [0 ]#line:177
    O0000OOO0OO0O0OOO =OOO00O000O0OO00O0 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:178
    if O0000OOO0OO0O0OOO :#line:179
        O0000OOO0OO0O0OOO =O0000OOO0OO0O0OOO [0 ].strip ()#line:180
    O0O00OOO0000OO000 =re .findall (r"user_name.DATA'\) : '(.*?)'",O0O0OO00OOOOOO00O .text )or OOO00O000O0OO00O0 .xpath ('//span[@class="profile_meta_value"]/text()')#line:182
    if O0O00OOO0000OO000 :#line:183
        O0O00OOO0000OO000 =O0O00OOO0000OO000 [0 ]#line:184
    OO0000O0OO000O000 =re .findall (r'createTime = \'(.*)\'',O0O0OO00OOOOOO00O .text )#line:185
    if OO0000O0OO000O000 :#line:186
        OO0000O0OO000O000 =OO0000O0OO000O000 [0 ][5 :]#line:187
    OO000OOO0OOO00000 =f'{OO0000O0OO000O000}|{O0OO0OO00O000O0O0}|{O0O000OOO0O0O00OO}|{O0000OOO0OO0O0OOO}|{O0O00OOO0000OO000}'#line:188
    O0OO0OOOO0OOO000O ={'biz':O0O000OOO0O0O00OO ,'text':OO000OOO0OOO00000 }#line:189
    return O0OO0OOOO0OOO000O #line:190
class MTZYD :#line:193
    def __init__ (O00O00000OOOOOOO0 ,O00OOO0OOO0OOO000 ):#line:194
        O00O00000OOOOOOO0 .name =O00OOO0OOO0OOO000 ['name']#line:195
        O00O00000OOOOOOO0 .uid =O00OOO0OOO0OOO000 .get ('uid')#line:196
        O00O00000OOOOOOO0 .s =requests .session ()#line:197
        O00O00000OOOOOOO0 .s .headers ={'Authorization':O00OOO0OOO0OOO000 ['ck'],'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Accept':'*/*','Origin':'http://61695315208.tt.bendishenghuochwl1.cn','Referer':'http://61695315208.tt.bendishenghuochwl1.cn/','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh',}#line:207
        O00O00000OOOOOOO0 .msg =''#line:208
    def user_info (OO000O000OO00O0OO ):#line:210
        O0O00OO0000OOO0OO ='http://api.mengmorwpt1.cn/h5_share/user/info'#line:211
        OOO000OOO0OO00OOO =OO000O000OO00O0OO .s .post (O0O00OO0000OOO0OO ,json ={"openid":0 }).json ()#line:212
        debugger (f'userinfo {OOO000OOO0OO00OOO}')#line:213
        if OOO000OOO0OO00OOO .get ('code')==200 :#line:214
            OO000O000OO00O0OO .nickname =OOO000OOO0OO00OOO .get ('data').get ('nickname')#line:215
            OO000O000OO00O0OO .points =OOO000OOO0OO00OOO .get ('data').get ('points')-OOO000OOO0OO00OOO .get ('data').get ('withdraw_points')#line:216
            OOO000OOO0OO00OOO =OO000O000OO00O0OO .s .post ('http://api.mengmorwpt1.cn/h5_share/user/sign',json ={"openid":0 })#line:217
            debugger (f'签到 {OOO000OOO0OO00OOO.json()}')#line:218
            OOOOO00OO0OO0OOO0 =OOO000OOO0OO00OOO .json ().get ('message')#line:219
            OO000O000OO00O0OO .msg +=f'\n账号：{OO000O000OO00O0OO.nickname},现有积分：{OO000O000OO00O0OO.points}，{OOOOO00OO0OO0OOO0}\n'+'-'*50 +'\n'#line:220
            printlog (f'{OO000O000OO00O0OO.nickname}:现有积分：{OO000O000OO00O0OO.points}，{OOOOO00OO0OO0OOO0}')#line:221
            O0O00OO0000OOO0OO ='http://api.mengmorwpt1.cn/h5_share/user/up_profit_ratio'#line:222
            OOOOOO0O000OO000O ={"openid":0 }#line:223
            try :#line:224
                OOO000OOO0OO00OOO =OO000O000OO00O0OO .s .post (O0O00OO0000OOO0OO ,json =OOOOOO0O000OO000O ).json ()#line:225
                if OOO000OOO0OO00OOO .get ('code')==500 :#line:226
                    raise #line:227
                OO000O000OO00O0OO .msg +=f'代理升级：{OOO000OOO0OO00OOO.get("message")}\n'#line:228
            except :#line:229
                O0O00OO0000OOO0OO ='http://api.mengmorwpt1.cn/h5_share/user/task_reward'#line:230
                for OOOOO000O0O0OOOO0 in range (0 ,8 ):#line:231
                    OOOOOO0O000OO000O ={"type":OOOOO000O0O0OOOO0 ,"openid":0 }#line:232
                    OOO000OOO0OO00OOO =OO000O000OO00O0OO .s .post (O0O00OO0000OOO0OO ,json =OOOOOO0O000OO000O ).json ()#line:233
                    if '积分未满'in OOO000OOO0OO00OOO .get ('message'):#line:234
                        break #line:235
                    if OOO000OOO0OO00OOO .get ('code')!=500 :#line:236
                        OO000O000OO00O0OO .msg +='主页奖励积分：'+OOO000OOO0OO00OOO .get ('message')+'\n'#line:237
                    OOOOO000O0O0OOOO0 +=1 #line:238
                    time .sleep (0.5 )#line:239
            return True #line:240
        else :#line:241
            OO000O000OO00O0OO .msg +='获取账号信息异常，检查cookie是否失效\n'#line:242
            printlog (f'{OO000O000OO00O0OO.name}:获取账号信息异常，检查cookie是否失效')#line:243
            if sendable :#line:244
                send (f'{OO000O000OO00O0OO.name} 每天赚获取账号信息异常，检查cookie是否失效','每天赚账号异常通知')#line:245
            if pushable :#line:246
                push (f'{OO000O000OO00O0OO.name} 每天赚获取账号信息异常，检查cookie是否失效','每天赚账号异常通知',uid =OO000O000OO00O0OO .uid )#line:247
            return False #line:248
    def get_read (OOO00000O0000OOOO ):#line:250
        O00OOO00O0OO000OO ='http://api.mengmorwpt1.cn/h5_share/daily/get_read'#line:251
        O0OO00O00OO00O0O0 ={"openid":0 }#line:252
        O00O000OOO000O0OO =0 #line:253
        while O00O000OOO000O0OO <10 :#line:254
            O0000OOO0O0OO0000 =OOO00000O0000OOOO .s .post (O00OOO00O0OO000OO ,json =O0OO00O00OO00O0O0 ).json ()#line:255
            debugger (f'getread {O0000OOO0O0OO0000}')#line:256
            if O0000OOO0O0OO0000 .get ('code')==200 :#line:257
                OOO00000O0000OOOO .link =O0000OOO0O0OO0000 .get ('data').get ('link')#line:258
                return True #line:259
            elif '获取失败'in O0000OOO0O0OO0000 .get ('message'):#line:260
                time .sleep (15 )#line:261
                O00O000OOO000O0OO +=1 #line:262
                continue #line:263
            else :#line:264
                OOO00000O0000OOOO .msg +=O0000OOO0O0OO0000 .get ('message')+'\n'#line:265
                printlog (f'{OOO00000O0000OOOO.nickname}:{O0000OOO0O0OO0000.get("message")}')#line:266
                return False #line:267
    def gettaskinfo (O0000OO0000O00O00 ,OOOO0O00O0OO00OOO ):#line:269
        for O0OOOOOO0O0O0O00O in OOOO0O00O0OO00OOO :#line:270
            if O0OOOOOO0O0O0O00O .get ('url'):#line:271
                return O0OOOOOO0O0O0O00O #line:272
    def dotasks (OOOOOOO00OO0O00O0 ):#line:274
        O00O0000OO00O0O0O ={'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Origin':'http://nei594688.594688be.com.byymmmcm3.cn','Referer':'http://nei594688.594688be.com.byymmmcm3.cn/','Accept-Encoding':'gzip, deflate',}#line:281
        OOO000O0OOOO00O0O =1 #line:282
        while True :#line:283
            OOOOOOO00000O00OO ={"href":OOOOOOO00OO0O00O0 .link }#line:284
            OOO0OO00OO0O0000O ='https://api.wanjd.cn/wxread/articles/tasks'#line:285
            OO000OO0OOOO00OO0 =requests .post (OOO0OO00OO0O0000O ,headers =O00O0000OO00O0O0O ,json =OOOOOOO00000O00OO ).json ()#line:286
            O000O0O0000O000O0 =OO000OO0OOOO00OO0 .get ('data')#line:287
            debugger (f'tasks {O000O0O0000O000O0}')#line:288
            O0O0O00O0OOO0OO0O =[O0OOOOOOOOO00OOOO ['is_read']for O0OOOOOOOOO00OOOO in O000O0O0000O000O0 ]#line:289
            if 0 not in O0O0O00O0OOO0OO0O :#line:290
                break #line:291
            if OO000OO0OOOO00OO0 .get ('code')!=200 :#line:292
                OOOOOOO00OO0O00O0 .msg +=OO000OO0OOOO00OO0 .get ('message')+'\n'#line:293
                printlog (f'{OOOOOOO00OO0O00O0.nickname}:{OO000OO0OOOO00OO0.get("message")}')#line:294
                break #line:295
            else :#line:296
                O0O0OOO0O00OO0000 =OOOOOOO00OO0O00O0 .gettaskinfo (OO000OO0OOOO00OO0 ['data'])#line:297
                if not O0O0OOO0O00OO0000 :#line:298
                    break #line:299
                OOO0O000OO0O0O0OO =O0O0OOO0O00OO0000 .get ('url')#line:300
                OO0000OO00OO0O0OO =O0O0OOO0O00OO0000 ['id']#line:301
                debugger (OO0000OO00OO0O0OO )#line:302
                OOOOOOO00000O00OO .update ({"id":OO0000OO00OO0O0OO })#line:303
                OOOOO0O0O0O0O000O =getmpinfo (OOO0O000OO0O0O0OO )#line:304
                try :#line:305
                    OOOOOOO00OO0O00O0 .msg +='正在阅读 '+OOOOO0O0O0O0O000O ['text']+'\n'#line:306
                    printlog (f'{OOOOOOO00OO0O00O0.nickname}:正在阅读{OOOOO0O0O0O0O000O["text"]}')#line:307
                except :#line:308
                    OOOOOOO00OO0O00O0 .msg +='正在阅读 '+OOOOO0O0O0O0O000O ['biz']+'\n'#line:309
                    printlog (f'{OOOOOOO00OO0O00O0.nickname}:正在阅读 {OOOOO0O0O0O0O000O["biz"]}')#line:310
                if len (str (OO0000OO00OO0O0OO ))<5 :#line:311
                    if OOO000O0OOOO00O0O ==3 :#line:312
                        if sendable :#line:313
                            send ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',f'{OOOOOOO00OO0O00O0.nickname} 美添赚检测',)#line:316
                        if pushable :#line:317
                            push ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',f'{OOOOOOO00OO0O00O0.nickname} 美添赚检测',)#line:320
                        raise Exception #line:321
                    if sendable :#line:322
                        send (OOOOO0O0O0O0O000O .get ('text'),f'{OOOOOOO00OO0O00O0.nickname} 美添赚过检测',OOO0O000OO0O0O0OO )#line:323
                    if pushable :#line:324
                        push (f'{OOOOOOO00OO0O00O0.name}\n点击阅读检测文章\n{OOOOO0O0O0O0O000O["text"]}',f'{OOOOOOO00OO0O00O0.nickname} 美添赚过检测',OOO0O000OO0O0O0OO ,uid =OOOOOOO00OO0O00O0 .uid )#line:326
                    OOOOOOO00OO0O00O0 .msg +='发送通知，暂停50秒\n'#line:327
                    printlog (f'{OOOOOOO00OO0O00O0.nickname}:发送通知，暂停50秒')#line:328
                    OOO000O0OOOO00O0O +=1 #line:329
                    time .sleep (50 )#line:330
                O0OOO00OOO00O0OOO =random .randint (7 ,10 )#line:331
                time .sleep (O0OOO00OOO00O0OOO )#line:332
                OOO0OO00OO0O0000O ='https://api.wanjd.cn/wxread/articles/three_read'#line:333
                OO000OO0OOOO00OO0 =requests .post (OOO0OO00OO0O0000O ,headers =O00O0000OO00O0O0O ,json =OOOOOOO00000O00OO ).json ()#line:334
                if OO000OO0OOOO00OO0 .get ('code')==200 :#line:335
                    OOOOOOO00OO0O00O0 .msg +='阅读成功'+'\n'+'-'*50 +'\n'#line:336
                    printlog (f'{OOOOOOO00OO0O00O0.nickname}:阅读成功')#line:337
                if OO000OO0OOOO00OO0 .get ('code')!=200 :#line:338
                    OOOOOOO00OO0O00O0 .msg +=OO000OO0OOOO00OO0 .get ('message')+'\n'+'-'*50 +'\n'#line:339
                    printlog (f'{OOOOOOO00OO0O00O0.nickname}:{OO000OO0OOOO00OO0.get("message")}')#line:340
                    break #line:341
        OOO0OO00OO0O0000O ='https://api.wanjd.cn/wxread/articles/check_success'#line:342
        OOOOOOO00000O00OO ={'type':1 ,'href':OOOOOOO00OO0O00O0 .link }#line:343
        OO000OO0OOOO00OO0 =requests .post (OOO0OO00OO0O0000O ,headers =O00O0000OO00O0O0O ,json =OOOOOOO00000O00OO ).json ()#line:344
        debugger (f'check {OO000OO0OOOO00OO0}')#line:345
        OOOOOOO00OO0O00O0 .msg +=OO000OO0OOOO00OO0 .get ('message')+'\n'#line:346
        printlog (f'{OOOOOOO00OO0O00O0.nickname}:{OO000OO0OOOO00OO0.get("message")}')#line:347
    def withdraw (OO0O00OOOO0O00OO0 ):#line:349
        if OO0O00OOOO0O00OO0 .points <txbz :#line:350
            OO0O00OOOO0O00OO0 .msg +=f'没有达到你设置的提现标准{txbz}\n'#line:351
            printlog (f'{OO0O00OOOO0O00OO0.nickname}:没有达到你设置的提现标准{txbz}')#line:352
            return False #line:353
        OO0OOO0O0O0O0O0O0 ='http://api.mengmorwpt1.cn/h5_share/user/withdraw'#line:354
        O00OOOOOOO0OO0000 =OO0O00OOOO0O00OO0 .s .post (OO0OOO0O0O0O0O0O0 ).json ()#line:355
        OO0O00OOOO0O00OO0 .msg +='提现结果'+O00OOOOOOO0OO0000 .get ('message')+'\n'#line:356
        printlog (f'{OO0O00OOOO0O00OO0.nickname}:提现结果 {O00OOOOOOO0OO0000.get("message")}')#line:357
        if O00OOOOOOO0OO0000 .get ('code')==200 :#line:358
            if sendable :#line:359
                send (f'{OO0O00OOOO0O00OO0.name} 已提现到红包，请在服务通知内及时领取','每天赚提现通知')#line:360
            if pushable :#line:361
                push (f'{OO0O00OOOO0O00OO0.name} 已提现到红包，请在服务通知内及时领取','每天赚提现通知',uid =OO0O00OOOO0O00OO0 .uid )#line:362
    def run (OO00O0000OOOOOOOO ):#line:364
        OO00O0000OOOOOOOO .msg +='*'*50 +f'\n账号：{OO00O0000OOOOOOOO.name}开始任务\n'#line:365
        printlog (f'账号：{OO00O0000OOOOOOOO.name}开始任务')#line:366
        if not OO00O0000OOOOOOOO .user_info ():#line:367
            return False #line:368
        if OO00O0000OOOOOOOO .get_read ():#line:369
            OO00O0000OOOOOOOO .dotasks ()#line:370
            OO00O0000OOOOOOOO .user_info ()#line:371
        OO00O0000OOOOOOOO .withdraw ()#line:372
        printlog (f'账号：{OO00O0000OOOOOOOO.name}:任务结束')#line:373
        if not printf :#line:374
            print (OO00O0000OOOOOOOO .msg .strip ())#line:375
            print (f'账号：{OO00O0000OOOOOOOO.name}任务结束')#line:376
def yd (O0OO0O00000O0O0O0 ):#line:379
    while not O0OO0O00000O0O0O0 .empty ():#line:380
        O0OO00O0000O0000O =O0OO0O00000O0O0O0 .get ()#line:381
        O0O00OOOOOOOO0OO0 =MTZYD (O0OO00O0000O0000O )#line:382
        O0O00OOOOOOOO0OO0 .run ()#line:383
def get_ver ():#line:386
    OO00O00O00O0OO0OO ='kmtz V1.6'#line:387
    O0O0O000O00O0O0OO ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:390
    O0OO0O0O0O0OOO00O =requests .get ('https://ghproxy.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json',headers =O0O0O000O00O0O0OO ).json ()#line:392
    O000O000OOOO000OO =OO00O00O00O0OO0OO .split (' ')[1 ]#line:393
    OOO00OO00OOO0OO00 =O0OO0O0O0O0OOO00O .get ('version').get (OO00O00O00O0OO0OO .split (' ')[0 ])#line:394
    OOOO0O0OO0OOOOOO0 =f"当前版本 {O000O000OOOO000OO}，仓库版本 {OOO00OO00OOO0OO00}"#line:395
    if O000O000OOOO000OO <OOO00OO00OOO0OO00 :#line:396
        OOOO0O0OO0OOOOOO0 +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:397
    return OOOO0O0OO0OOOOOO0 #line:398
def main ():#line:401
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:402
    OO00000OOOO0OO0OO =os .getenv ('mtzck')#line:403
    if not OO00000OOOO0OO0OO :#line:404
        print ('请仔细阅读上方注释并配置好key和ck')#line:405
        exit ()#line:406
    try :#line:407
        OO00000OOOO0OO0OO =OO00000OOOO0OO0OO .split ('&')#line:408
    except :#line:409
        OO00000OOOO0OO0OO =ast .literal_eval (OO00000OOOO0OO0OO )#line:410
    OO00OO0000O0000O0 =Queue ()#line:411
    OOOO00O0O0O0OOOOO =[]#line:412
    for O000O0OOOOOOOO000 ,OO0O00O0OO000OOO0 in enumerate (OO00000OOOO0OO0OO ,start =1 ):#line:413
        printlog (f'{OO0O00O0OO000OOO0}\n以上是账号{O000O0OOOOOOOO000}的ck，如不正确，请检查ck填写格式')#line:414
        if isinstance (OO0O00O0OO000OOO0 ,dict ):#line:415
            OO00OO0000O0000O0 .put (OO0O00O0OO000OOO0 )#line:416
        else :#line:417
            OO00OO0000O0000O0 .put (ast .literal_eval (OO0O00O0OO000OOO0 ))#line:418
    for O000O0OOOOOOOO000 in range (max_workers ):#line:419
        OOO00O0O0O00O00OO =threading .Thread (target =yd ,args =(OO00OO0000O0000O0 ,))#line:420
        OOO00O0O0O00O00OO .start ()#line:421
        OOOO00O0O0O0OOOOO .append (OOO00O0O0O00O00OO )#line:422
        time .sleep (20 )#line:423
    for OOOOO0O0O00O0OOO0 in OOOO00O0O0O0OOOOO :#line:424
        OOOOO0O0O00O0OOO0 .join ()#line:425
if __name__ =='__main__':#line:428
    main ()#line:429