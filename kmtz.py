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
debug = 0
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


def ftime ():#line:102
    O00000O0000O00OOO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:103
    return O00000O0000O00OOO #line:104
def debugger (O00O00OOOOOOO0O00 ):#line:107
    if debug :#line:108
        print (O00O00OOOOOOO0O00 )#line:109
def printlog (OO000000OO000O000 ):#line:112
    if printf :#line:113
        print (OO000000OO000O000 )#line:114
def send (OOOO0000O0000OOOO ,title ='通知',url =None ):#line:117
    if not url :#line:118
        O00O00O000O00O00O ={"msgtype":"text","text":{"content":f"{title}\n\n{OOOO0000O0000OOOO}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:125
    else :#line:126
        O00O00O000O00O00O ={"msgtype":"news","news":{"articles":[{"title":title ,"description":OOOO0000O0000OOOO ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:131
    OOOOO0OOO00OOO0OO =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:132
    O000O0OO00OO000OO =requests .post (OOOOO0OOO00OOO0OO ,data =json .dumps (O00O00O000O00O00O )).json ()#line:133
    if O000O0OO00OO000OO .get ('errcode')!=0 :#line:134
        print ('消息发送失败，请检查key和发送格式')#line:135
        return False #line:136
    return O000O0OO00OO000OO #line:137
def push (O0OOOO000O0OO0OO0 ,O0O0OO00O0O000O0O ,url ='',uid =None ):#line:140
    if uid :#line:141
        uids .append (uid )#line:142
    OOOOO0O0O0O0OOOOO ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',O0OOOO000O0OO0OO0 ).replace ('url',url )#line:144
    O0000O0OOOO0O00O0 ={"appToken":appToken ,"content":OOOOO0O0O0O0OOOOO ,"summary":O0O0OO00O0O000O0O ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:154
    OOO00000O00O000OO ='http://wxpusher.zjiecode.com/api/send/message'#line:155
    O0O0O0O0OOOOO0OOO =requests .post (url =OOO00000O00O000OO ,json =O0000O0OOOO0O00O0 ).json ()#line:156
    if O0O0O0O0OOOOO0OOO .get ('code')!=1000 :#line:157
        print (O0O0O0O0OOOOO0OOO .get ('msg'),O0O0O0O0OOOOO0OOO )#line:158
    return O0O0O0O0OOOOO0OOO #line:159
def getmpinfo (O0O000O0OO00O0OO0 ):#line:162
    if not O0O000O0OO00O0OO0 or O0O000O0OO00O0OO0 =='':#line:163
        return False #line:164
    OOOOOOOOO000000O0 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:166
    OOO0OO0000O000OO0 =requests .get (O0O000O0OO00O0OO0 ,headers =OOOOOOOOO000000O0 )#line:167
    OO0OOOO0OO0O0O00O =etree .HTML (OOO0OO0000O000OO0 .text )#line:168
    O00O0O0O0O0000OOO =OO0OOOO0OO0O0O00O .xpath ('//meta[@*="og:title"]/@content')#line:169
    if O00O0O0O0O0000OOO :#line:170
        O00O0O0O0O0000OOO =O00O0O0O0O0000OOO [0 ]#line:171
    if 'biz'in O0O000O0OO00O0OO0 :#line:172
        OOOOO0O0OOO00O00O =re .findall (r'biz=(.*?)&',O0O000O0OO00O0OO0 )#line:173
    else :#line:174
        OOOO00OO00000OOO0 =OO0OOOO0OO0O0O00O .xpath ('//meta[@*="og:url"]/@content')[0 ]#line:175
        OOOOO0O0OOO00O00O =re .findall (r'biz=(.*?)&',str (OOOO00OO00000OOO0 ))#line:176
    if OOOOO0O0OOO00O00O :#line:177
        OOOOO0O0OOO00O00O =OOOOO0O0OOO00O00O [0 ]#line:178
    else :#line:179
        return False #line:180
    O0OO00OOO0OO0OO00 =OO0OOOO0OO0O0O00O .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:181
    if O0OO00OOO0OO0OO00 :#line:182
        O0OO00OOO0OO0OO00 =O0OO00OOO0OO0OO00 [0 ].strip ()#line:183
    OO0000OOOOOO000OO =re .findall (r"user_name.DATA'\) : '(.*?)'",OOO0OO0000O000OO0 .text )or OO0OOOO0OO0O0O00O .xpath ('//span[@class="profile_meta_value"]/text()')#line:185
    if OO0000OOOOOO000OO :#line:186
        OO0000OOOOOO000OO =OO0000OOOOOO000OO [0 ]#line:187
    O0000OO0OO00OOOOO =re .findall (r'createTime = \'(.*)\'',OOO0OO0000O000OO0 .text )#line:188
    if O0000OO0OO00OOOOO :#line:189
        O0000OO0OO00OOOOO =O0000OO0OO00OOOOO [0 ][5 :]#line:190
    OO0OO0000O00OOOOO =f'{O0000OO0OO00OOOOO}|{O00O0O0O0O0000OOO}|{OOOOO0O0OOO00O00O}|{O0OO00OOO0OO0OO00}|{OO0000OOOOOO000OO}'#line:191
    O00OOO00000OOO0O0 ={'biz':OOOOO0O0OOO00O00O ,'text':OO0OO0000O00OOOOO }#line:192
    return O00OOO00000OOO0O0 #line:193
class MTZYD :#line:196
    def __init__ (O00O0OOO00000O0O0 ,OOO0O00O0O00OOOO0 ):#line:197
        O00O0OOO00000O0O0 .name =OOO0O00O0O00OOOO0 ['name']#line:198
        O00O0OOO00000O0O0 .uid =OOO0O00O0O00OOOO0 .get ('uid')#line:199
        O00O0OOO00000O0O0 .s =requests .session ()#line:200
        O00O0OOO00000O0O0 .s .headers ={'Authorization':OOO0O00O0O00OOOO0 ['ck'],'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Accept':'*/*','Origin':'http://61695315208.tt.bendishenghuochwl1.cn','Referer':'http://61695315208.tt.bendishenghuochwl1.cn/','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh',}#line:210
        O00O0OOO00000O0O0 .msg =''#line:211
    def user_info (O0O000OO0000O00O0 ):#line:213
        OO00OOOOO000OOO0O ='http://api.mengmorwpt1.cn/h5_share/user/info'#line:214
        O000OOOOO0000O0O0 =O0O000OO0000O00O0 .s .post (OO00OOOOO000OOO0O ,json ={"openid":0 }).json ()#line:215
        debugger (f'userinfo {O000OOOOO0000O0O0}')#line:216
        if O000OOOOO0000O0O0 .get ('code')==200 :#line:217
            O0O000OO0000O00O0 .nickname =O000OOOOO0000O0O0 .get ('data').get ('nickname')#line:218
            O0O000OO0000O00O0 .points =O000OOOOO0000O0O0 .get ('data').get ('points')-O000OOOOO0000O0O0 .get ('data').get ('withdraw_points')#line:219
            O000OOOOO0000O0O0 =O0O000OO0000O00O0 .s .post ('http://api.mengmorwpt1.cn/h5_share/user/sign',json ={"openid":0 })#line:220
            debugger (f'签到 {O000OOOOO0000O0O0.json()}')#line:221
            O0OO0O0O000O00OO0 =O000OOOOO0000O0O0 .json ().get ('message')#line:222
            O0O000OO0000O00O0 .msg +=f'\n账号：{O0O000OO0000O00O0.nickname},现有积分：{O0O000OO0000O00O0.points}，{O0OO0O0O000O00OO0}\n'+'-'*50 +'\n'#line:223
            printlog (f'{O0O000OO0000O00O0.nickname}:现有积分：{O0O000OO0000O00O0.points}，{O0OO0O0O000O00OO0}')#line:224
            OO00OOOOO000OOO0O ='http://api.mengmorwpt1.cn/h5_share/user/up_profit_ratio'#line:225
            OO0OOO0O0OOO00OOO ={"openid":0 }#line:226
            try :#line:227
                O000OOOOO0000O0O0 =O0O000OO0000O00O0 .s .post (OO00OOOOO000OOO0O ,json =OO0OOO0O0OOO00OOO ).json ()#line:228
                if O000OOOOO0000O0O0 .get ('code')==500 :#line:229
                    raise #line:230
                O0O000OO0000O00O0 .msg +=f'代理升级：{O000OOOOO0000O0O0.get("message")}\n'#line:231
            except :#line:232
                OO00OOOOO000OOO0O ='http://api.mengmorwpt1.cn/h5_share/user/task_reward'#line:233
                for O00OOO0O0O0OOOOOO in range (0 ,8 ):#line:234
                    OO0OOO0O0OOO00OOO ={"type":O00OOO0O0O0OOOOOO ,"openid":0 }#line:235
                    O000OOOOO0000O0O0 =O0O000OO0000O00O0 .s .post (OO00OOOOO000OOO0O ,json =OO0OOO0O0OOO00OOO ).json ()#line:236
                    if '积分未满'in O000OOOOO0000O0O0 .get ('message'):#line:237
                        break #line:238
                    if O000OOOOO0000O0O0 .get ('code')!=500 :#line:239
                        O0O000OO0000O00O0 .msg +='主页奖励积分：'+O000OOOOO0000O0O0 .get ('message')+'\n'#line:240
                    O00OOO0O0O0OOOOOO +=1 #line:241
                    time .sleep (0.5 )#line:242
            return True #line:243
        else :#line:244
            O0O000OO0000O00O0 .msg +='获取账号信息异常，检查cookie是否失效\n'#line:245
            printlog (f'{O0O000OO0000O00O0.name}:获取账号信息异常，检查cookie是否失效')#line:246
            if sendable :#line:247
                send (f'{O0O000OO0000O00O0.name} 每天赚获取账号信息异常，检查cookie是否失效','每天赚账号异常通知')#line:248
            if pushable :#line:249
                push (f'{O0O000OO0000O00O0.name} 每天赚获取账号信息异常，检查cookie是否失效','每天赚账号异常通知',uid =O0O000OO0000O00O0 .uid )#line:250
            return False #line:251
    def get_read (OOO0OO0O0000OOOOO ):#line:253
        OO000OO00O0OOO00O ='http://api.mengmorwpt1.cn/h5_share/daily/get_read'#line:254
        OO00O00OOOOOO0OO0 ={"openid":0 }#line:255
        O000OOO0OOOO0000O =0 #line:256
        while O000OOO0OOOO0000O <10 :#line:257
            OO0O00O0O000OO0O0 =OOO0OO0O0000OOOOO .s .post (OO000OO00O0OOO00O ,json =OO00O00OOOOOO0OO0 ).json ()#line:258
            debugger (f'getread {OO0O00O0O000OO0O0}')#line:259
            if OO0O00O0O000OO0O0 .get ('code')==200 :#line:260
                OOO0OO0O0000OOOOO .link =OO0O00O0O000OO0O0 .get ('data').get ('link')#line:261
                return True #line:262
            elif '获取失败'in OO0O00O0O000OO0O0 .get ('message'):#line:263
                time .sleep (15 )#line:264
                O000OOO0OOOO0000O +=1 #line:265
                continue #line:266
            else :#line:267
                OOO0OO0O0000OOOOO .msg +=OO0O00O0O000OO0O0 .get ('message')+'\n'#line:268
                printlog (f'{OOO0OO0O0000OOOOO.nickname}:{OO0O00O0O000OO0O0.get("message")}')#line:269
                return False #line:270
    def gettaskinfo (O0OOOOO0000OO0OO0 ,O000OOO000OO000O0 ):#line:272
        for OO0O0OOO00O000OOO in O000OOO000OO000O0 :#line:273
            if OO0O0OOO00O000OOO .get ('url'):#line:274
                return OO0O0OOO00O000OOO #line:275
    def dotasks (OOOOO0000OOOO0OO0 ):#line:277
        OOOO000OOOO000O0O ={'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Origin':'http://nei594688.594688be.com.byymmmcm3.cn','Referer':'http://nei594688.594688be.com.byymmmcm3.cn/','Accept-Encoding':'gzip, deflate',}#line:284
        O00O0O00000O0O0OO =1 #line:285
        while True :#line:286
            OOO0O00OO00O0O00O ={"href":OOOOO0000OOOO0OO0 .link }#line:287
            OOOOO0OO000OOOOO0 ='https://api.wanjd.cn/wxread/articles/tasks'#line:288
            O000OOOO00O000OOO =requests .post (OOOOO0OO000OOOOO0 ,headers =OOOO000OOOO000O0O ,json =OOO0O00OO00O0O00O ).json ()#line:289
            O0OO0OO0OOO0O0OO0 =O000OOOO00O000OOO .get ('data')#line:290
            debugger (f'tasks {O0OO0OO0OOO0O0OO0}')#line:291
            OO0000000O0000OO0 =[OO0OO0O0OO0O0OO0O ['is_read']for OO0OO0O0OO0O0OO0O in O0OO0OO0OOO0O0OO0 ]#line:292
            if 0 not in OO0000000O0000OO0 :#line:293
                break #line:294
            if O000OOOO00O000OOO .get ('code')!=200 :#line:295
                OOOOO0000OOOO0OO0 .msg +=O000OOOO00O000OOO .get ('message')+'\n'#line:296
                printlog (f'{OOOOO0000OOOO0OO0.nickname}:{O000OOOO00O000OOO.get("message")}')#line:297
                break #line:298
            else :#line:299
                O0000OOOO00O0OO0O =OOOOO0000OOOO0OO0 .gettaskinfo (O000OOOO00O000OOO ['data'])#line:300
                if not O0000OOOO00O0OO0O :#line:301
                    break #line:302
                OO0000000000OO000 =O0000OOOO00O0OO0O .get ('url')#line:303
                O000OO0000OO0000O =O0000OOOO00O0OO0O ['id']#line:304
                debugger (O000OO0000OO0000O )#line:305
                OOO0O00OO00O0O00O .update ({"id":O000OO0000OO0000O })#line:306
                OO00O0OO000OOO0OO =getmpinfo (OO0000000000OO000 )#line:307
                try :#line:308
                    OOOOO0000OOOO0OO0 .msg +='正在阅读 '+OO00O0OO000OOO0OO ['text']+'\n'#line:309
                    printlog (f'{OOOOO0000OOOO0OO0.nickname}:正在阅读{OO00O0OO000OOO0OO["text"]}')#line:310
                except :#line:311
                    OOOOO0000OOOO0OO0 .msg +='获取文章信息失败\n'#line:312
                    printlog (f'{OOOOO0000OOOO0OO0.nickname}:获取文章信息失败')#line:313
                    break #line:314
                if len (str (O000OO0000OO0000O ))<5 :#line:315
                    if O00O0O00000O0O0OO ==3 :#line:316
                        if sendable :#line:317
                            send ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',f'{OOOOO0000OOOO0OO0.nickname} 美添赚检测',)#line:320
                        if pushable :#line:321
                            push ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',f'{OOOOO0000OOOO0OO0.nickname} 美添赚检测',)#line:324
                        break #line:325
                    if sendable :#line:326
                        send (OO00O0OO000OOO0OO .get ('text'),f'{OOOOO0000OOOO0OO0.nickname} 美添赚过检测',OO0000000000OO000 )#line:327
                    if pushable :#line:328
                        push (f'{OOOOO0000OOOO0OO0.name}\n点击阅读检测文章\n{OO00O0OO000OOO0OO["text"]}',f'{OOOOO0000OOOO0OO0.nickname} 美添赚过检测',OO0000000000OO000 ,uid =OOOOO0000OOOO0OO0 .uid )#line:330
                    OOOOO0000OOOO0OO0 .msg +='发送通知，暂停50秒\n'#line:331
                    printlog (f'{OOOOO0000OOOO0OO0.nickname}:发送通知，暂停50秒')#line:332
                    O00O0O00000O0O0OO +=1 #line:333
                    time .sleep (50 )#line:334
                O0OO0OO0O0OOO00OO =random .randint (7 ,10 )#line:335
                time .sleep (O0OO0OO0O0OOO00OO )#line:336
                OOOOO0OO000OOOOO0 ='https://api.wanjd.cn/wxread/articles/three_read'#line:337
                O000OOOO00O000OOO =requests .post (OOOOO0OO000OOOOO0 ,headers =OOOO000OOOO000O0O ,json =OOO0O00OO00O0O00O ).json ()#line:338
                if O000OOOO00O000OOO .get ('code')==200 :#line:339
                    OOOOO0000OOOO0OO0 .msg +='阅读成功'+'\n'+'-'*50 +'\n'#line:340
                    printlog (f'{OOOOO0000OOOO0OO0.nickname}:阅读成功')#line:341
                if O000OOOO00O000OOO .get ('code')!=200 :#line:342
                    OOOOO0000OOOO0OO0 .msg +=O000OOOO00O000OOO .get ('message')+'\n'+'-'*50 +'\n'#line:343
                    printlog (f'{OOOOO0000OOOO0OO0.nickname}:{O000OOOO00O000OOO.get("message")}')#line:344
                    break #line:345
        OOOOO0OO000OOOOO0 ='https://api.wanjd.cn/wxread/articles/check_success'#line:346
        OOO0O00OO00O0O00O ={'type':1 ,'href':OOOOO0000OOOO0OO0 .link }#line:347
        O000OOOO00O000OOO =requests .post (OOOOO0OO000OOOOO0 ,headers =OOOO000OOOO000O0O ,json =OOO0O00OO00O0O00O ).json ()#line:348
        debugger (f'check {O000OOOO00O000OOO}')#line:349
        OOOOO0000OOOO0OO0 .msg +=O000OOOO00O000OOO .get ('message')+'\n'#line:350
        printlog (f'{OOOOO0000OOOO0OO0.nickname}:{O000OOOO00O000OOO.get("message")}')#line:351
    def withdraw (O0OOO0OOOO000OO0O ):#line:353
        if O0OOO0OOOO000OO0O .points <txbz :#line:354
            O0OOO0OOOO000OO0O .msg +=f'没有达到你设置的提现标准{txbz}\n'#line:355
            printlog (f'{O0OOO0OOOO000OO0O.nickname}:没有达到你设置的提现标准{txbz}')#line:356
            return False #line:357
        O00OOOOO00OOOO00O ='http://api.mengmorwpt1.cn/h5_share/user/withdraw'#line:358
        OOOO00OO0OOOOO000 =O0OOO0OOOO000OO0O .s .post (O00OOOOO00OOOO00O ).json ()#line:359
        O0OOO0OOOO000OO0O .msg +='提现结果'+OOOO00OO0OOOOO000 .get ('message')+'\n'#line:360
        printlog (f'{O0OOO0OOOO000OO0O.nickname}:提现结果 {OOOO00OO0OOOOO000.get("message")}')#line:361
        if OOOO00OO0OOOOO000 .get ('code')==200 :#line:362
            if sendable :#line:363
                send (f'{O0OOO0OOOO000OO0O.name} 已提现到红包，请在服务通知内及时领取','每天赚提现通知')#line:364
            if pushable :#line:365
                push (f'{O0OOO0OOOO000OO0O.name} 已提现到红包，请在服务通知内及时领取','每天赚提现通知',uid =O0OOO0OOOO000OO0O .uid )#line:366
    def run (O0OO0O000O0OO0O0O ):#line:368
        O0OO0O000O0OO0O0O .msg +='*'*50 +f'\n账号：{O0OO0O000O0OO0O0O.name}开始任务\n'#line:369
        printlog (f'账号：{O0OO0O000O0OO0O0O.name}开始任务')#line:370
        if not O0OO0O000O0OO0O0O .user_info ():#line:371
            return False #line:372
        if O0OO0O000O0OO0O0O .get_read ():#line:373
            O0OO0O000O0OO0O0O .dotasks ()#line:374
            O0OO0O000O0OO0O0O .user_info ()#line:375
        O0OO0O000O0OO0O0O .withdraw ()#line:376
        printlog (f'账号：{O0OO0O000O0OO0O0O.name}:任务结束')#line:377
        if not printf :#line:378
            print (O0OO0O000O0OO0O0O .msg .strip ())#line:379
            print (f'账号：{O0OO0O000O0OO0O0O.name}任务结束')#line:380
def yd (OO0OOOOO0000O0OOO ):#line:383
    while not OO0OOOOO0000O0OOO .empty ():#line:384
        O000000O0O00000O0 =OO0OOOOO0000O0OOO .get ()#line:385
        OO0OO00O00O0O0O00 =MTZYD (O000000O0O00000O0 )#line:386
        OO0OO00O00O0O0O00 .run ()#line:387
def get_ver ():#line:390
    OOOO000OOOOOO00OO ='kmtz V1.8'#line:391
    OO0OOO0O0OOO0O0O0 ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:394
    O00O0OOO0O0O0OOO0 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OO0OOO0O0OOO0O0O0 ).json ()#line:396
    O000O00OOOO00OO00 =OOOO000OOOOOO00OO .split (' ')[1 ]#line:397
    O000O0OO0000OO00O =O00O0OOO0O0O0OOO0 .get ('version').get ('kmtzV2')#line:398
    O0OO000OOO00O0OO0 =f"当前版本 {O000O00OOOO00OO00}，此版本将不再维护。仓库版本kmtzV2 {O000O0OO0000OO00O}"#line:399
    if O000O00OOOO00OO00 <O000O0OO0000OO00O :#line:400
        O0OO000OOO00O0OO0 +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:401
    return O0OO000OOO00O0OO0 #line:402
def main ():#line:405
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:406
    O000OO0000OO00O0O =os .getenv ('mtzck')#line:407
    if not O000OO0000OO00O0O :#line:408
        print ('请仔细阅读上方注释并配置好key和ck')#line:409
        exit ()#line:410
    try :#line:411
        O000OO0000OO00O0O =ast .literal_eval (O000OO0000OO00O0O )#line:412
    except :#line:413
        O000OO0000OO00O0O =O000OO0000OO00O0O .split ('&')#line:414
    O0O00O0OO00O0O000 =Queue ()#line:415
    O000O000O0OO0OO00 =[]#line:416
    for OO0OO0O0O0OOOO0O0 ,OO0OO00OO00OOO0O0 in enumerate (O000OO0000OO00O0O ,start =1 ):#line:417
        printlog (f'{OO0OO00OO00OOO0O0}\n以上是账号{OO0OO0O0O0OOOO0O0}的ck，如不正确，请检查ck填写格式')#line:418
        if isinstance (OO0OO00OO00OOO0O0 ,dict ):#line:419
            O0O00O0OO00O0O000 .put (OO0OO00OO00OOO0O0 )#line:420
        else :#line:421
            O0O00O0OO00O0O000 .put (ast .literal_eval (OO0OO00OO00OOO0O0 ))#line:422
    for OO0OO0O0O0OOOO0O0 in range (max_workers ):#line:423
        OOOO0000000OOO00O =threading .Thread (target =yd ,args =(O0O00O0OO00O0O000 ,))#line:424
        OOOO0000000OOO00O .start ()#line:425
        O000O000O0OO0OO00 .append (OOOO0000000OOO00O )#line:426
        time .sleep (20 )#line:427
    for O00O0OO00O00000O0 in O000O000O0OO0OO00 :#line:428
        O00O0OO00O00000O0 .join ()#line:429
if __name__ =='__main__':#line:432
    main ()#line:433
