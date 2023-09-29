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
    O0OOO00OO00O000OO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:103
    return O0OOO00OO00O000OO #line:104
def debugger (O0O0O0OOO00O0OO0O ):#line:107
    if debug :#line:108
        print (O0O0O0OOO00O0OO0O )#line:109
def printlog (O0000O00OO000O000 ):#line:112
    if printf :#line:113
        print (O0000O00OO000O000 )#line:114
def send (O0OOO0O0O0OOOOOOO ,title ='通知',url =None ):#line:117
    if not url :#line:118
        O0OO0000O00O0OO0O ={"msgtype":"text","text":{"content":f"{title}\n\n{O0OOO0O0O0OOOOOOO}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:125
    else :#line:126
        O0OO0000O00O0OO0O ={"msgtype":"news","news":{"articles":[{"title":title ,"description":O0OOO0O0O0OOOOOOO ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:131
    OOO00O0OO0OOOOOO0 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:132
    OO0OOOO00O0O0OOOO =requests .post (OOO00O0OO0OOOOOO0 ,data =json .dumps (O0OO0000O00O0OO0O )).json ()#line:133
    if OO0OOOO00O0O0OOOO .get ('errcode')!=0 :#line:134
        print ('消息发送失败，请检查key和发送格式')#line:135
        return False #line:136
    return OO0OOOO00O0O0OOOO #line:137
def push (OO0000O0O00OOOO00 ,OOOO0O00OO0OOO0OO ,url ='',uid =None ):#line:140
    if uid :#line:141
        uids .append (uid )#line:142
    O00O0OO000O000OOO ="<font size=4>[msg](url)</font>\n\n<font size=3>本通知by：https://github.com/kxs2018/xiaoym\n\n[点击加入作者tg频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace ('msg',OO0000O0O00OOOO00 ).replace ('url',url )#line:144
    OO00OO0OOOOOO0000 ={"appToken":appToken ,"content":O00O0OO000O000OOO ,"summary":OOOO0O00OO0OOO0OO ,"contentType":3 ,"topicIds":topicids ,"uids":uids ,"url":url ,"verifyPay":False }#line:154
    O0O0O0OOO00000O00 ='http://wxpusher.zjiecode.com/api/send/message'#line:155
    O0O0OOOO0000OO000 =requests .post (url =O0O0O0OOO00000O00 ,json =OO00OO0OOOOOO0000 ).json ()#line:156
    if O0O0OOOO0000OO000 .get ('code')!=1000 :#line:157
        print (O0O0OOOO0000OO000 .get ('msg'),O0O0OOOO0000OO000 )#line:158
    return O0O0OOOO0000OO000 #line:159
def getmpinfo (OOO0O0000O00OO00O ):#line:162
    if not OOO0O0000O00OO00O or OOO0O0000O00OO00O =='':#line:163
        return False #line:164
    OO00OOO0O000OOO00 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:166
    O000O00O00OOOO00O =requests .get (OOO0O0000O00OO00O ,headers =OO00OOO0O000OOO00 )#line:167
    OOOO00OO0O000OO00 =etree .HTML (O000O00O00OOOO00O .text )#line:168
    O0OO0OO0O00OOOOOO =OOOO00OO0O000OO00 .xpath ('//meta[@*="og:title"]/@content')#line:169
    if O0OO0OO0O00OOOOOO :#line:170
        O0OO0OO0O00OOOOOO =O0OO0OO0O00OOOOOO [0 ]#line:171
    OOO0O0000OOO00OOO =OOOO00OO0O000OO00 .xpath ('//meta[@*="og:url"]/@content')#line:172
    if OOO0O0000OOO00OOO :#line:173
        OOO0O0000OOO00OOO =OOO0O0000OOO00OOO [0 ].encode ().decode ()#line:174
    O000OO0O00O00OOOO =re .findall (r'biz=(.*?)&',OOO0O0000O00OO00O )or re .findall (r'biz=(.*?)&',OOO0O0000OOO00OOO )#line:175
    if O000OO0O00O00OOOO :#line:176
        O000OO0O00O00OOOO =O000OO0O00O00OOOO [0 ]#line:177
    OOO00000OOO00OOOO =OOOO00OO0O000OO00 .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:178
    if OOO00000OOO00OOOO :#line:179
        OOO00000OOO00OOOO =OOO00000OOO00OOOO [0 ].strip ()#line:180
    OOO0OO0O0000O0000 =re .findall (r"user_name.DATA'\) : '(.*?)'",O000O00O00OOOO00O .text )or OOOO00OO0O000OO00 .xpath ('//span[@class="profile_meta_value"]/text()')#line:182
    if OOO0OO0O0000O0000 :#line:183
        OOO0OO0O0000O0000 =OOO0OO0O0000O0000 [0 ]#line:184
    O00OO00O0O00O000O =re .findall (r'createTime = \'(.*)\'',O000O00O00OOOO00O .text )#line:185
    if O00OO00O0O00O000O :#line:186
        O00OO00O0O00O000O =O00OO00O0O00O000O [0 ][5 :]#line:187
    O00O000OOO0OOOOOO =f'{O00OO00O0O00O000O}|{O0OO0OO0O00OOOOOO}|{O000OO0O00O00OOOO}|{OOO00000OOO00OOOO}|{OOO0OO0O0000O0000}'#line:188
    OO0O0OO0O0O0000O0 ={'biz':O000OO0O00O00OOOO ,'text':O00O000OOO0OOOOOO }#line:189
    return OO0O0OO0O0O0000O0 #line:190
class MTZYD :#line:193
    def __init__ (OOOO0O0O0O0000000 ,OOOOO00000000O00O ):#line:194
        OOOO0O0O0O0000000 .name =OOOOO00000000O00O ['name']#line:195
        OOOO0O0O0O0000000 .uid =OOOOO00000000O00O .get ('uid')#line:196
        OOOO0O0O0O0000000 .s =requests .session ()#line:197
        OOOO0O0O0O0000000 .s .headers ={'Authorization':OOOOO00000000O00O ['ck'],'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Accept':'*/*','Origin':'http://61695315208.tt.bendishenghuochwl1.cn','Referer':'http://61695315208.tt.bendishenghuochwl1.cn/','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh',}#line:207
        OOOO0O0O0O0000000 .msg =''#line:208
    def user_info (OOO00O0O0OO000OOO ):#line:210
        O0OO00O00OO0O0OO0 ='http://api.mengmorwpt1.cn/h5_share/user/info'#line:211
        OO0O00000OO00OO00 =OOO00O0O0OO000OOO .s .post (O0OO00O00OO0O0OO0 ,json ={"openid":0 }).json ()#line:212
        debugger (f'userinfo {OO0O00000OO00OO00}')#line:213
        if OO0O00000OO00OO00 .get ('code')==200 :#line:214
            OOO00O0O0OO000OOO .nickname =OO0O00000OO00OO00 .get ('data').get ('nickname')#line:215
            OOO00O0O0OO000OOO .points =OO0O00000OO00OO00 .get ('data').get ('points')-OO0O00000OO00OO00 .get ('data').get ('withdraw_points')#line:216
            OO0O00000OO00OO00 =OOO00O0O0OO000OOO .s .post ('http://api.mengmorwpt1.cn/h5_share/user/sign',json ={"openid":0 })#line:217
            debugger (f'签到 {OO0O00000OO00OO00.json()}')#line:218
            O00OOO0000O0OO000 =OO0O00000OO00OO00 .json ().get ('message')#line:219
            OOO00O0O0OO000OOO .msg +=f'\n账号：{OOO00O0O0OO000OOO.nickname},现有积分：{OOO00O0O0OO000OOO.points}，{O00OOO0000O0OO000}\n'+'-'*50 +'\n'#line:220
            printlog (f'{OOO00O0O0OO000OOO.nickname}:现有积分：{OOO00O0O0OO000OOO.points}，{O00OOO0000O0OO000}')#line:221
            O0OO00O00OO0O0OO0 ='http://api.mengmorwpt1.cn/h5_share/user/up_profit_ratio'#line:222
            OOO0OOO0OO00O0OOO ={"openid":0 }#line:223
            try :#line:224
                OO0O00000OO00OO00 =OOO00O0O0OO000OOO .s .post (O0OO00O00OO0O0OO0 ,json =OOO0OOO0OO00O0OOO ).json ()#line:225
                if OO0O00000OO00OO00 .get ('code')==500 :#line:226
                    raise #line:227
                OOO00O0O0OO000OOO .msg +=f'代理升级：{OO0O00000OO00OO00.get("message")}\n'#line:228
            except :#line:229
                O0OO00O00OO0O0OO0 ='http://api.mengmorwpt1.cn/h5_share/user/task_reward'#line:230
                for OOO0OOO00OOO0O000 in range (0 ,8 ):#line:231
                    OOO0OOO0OO00O0OOO ={"type":OOO0OOO00OOO0O000 ,"openid":0 }#line:232
                    OO0O00000OO00OO00 =OOO00O0O0OO000OOO .s .post (O0OO00O00OO0O0OO0 ,json =OOO0OOO0OO00O0OOO ).json ()#line:233
                    if '积分未满'in OO0O00000OO00OO00 .get ('message'):#line:234
                        break #line:235
                    if OO0O00000OO00OO00 .get ('code')!=500 :#line:236
                        OOO00O0O0OO000OOO .msg +='主页奖励积分：'+OO0O00000OO00OO00 .get ('message')+'\n'#line:237
                    OOO0OOO00OOO0O000 +=1 #line:238
                    time .sleep (0.5 )#line:239
            return True #line:240
        else :#line:241
            OOO00O0O0OO000OOO .msg +='获取账号信息异常，检查cookie是否失效\n'#line:242
            printlog (f'{OOO00O0O0OO000OOO.name}:获取账号信息异常，检查cookie是否失效')#line:243
            if sendable :#line:244
                send (f'{OOO00O0O0OO000OOO.name} 每天赚获取账号信息异常，检查cookie是否失效','每天赚账号异常通知')#line:245
            if pushable :#line:246
                push (f'{OOO00O0O0OO000OOO.name} 每天赚获取账号信息异常，检查cookie是否失效','每天赚账号异常通知',uid =OOO00O0O0OO000OOO .uid )#line:247
            return False #line:248
    def get_read (O00O0000O0OOO0O0O ):#line:250
        O0000O0OOO0000O00 ='http://api.mengmorwpt1.cn/h5_share/daily/get_read'#line:251
        O0O00O0OOO00000O0 ={"openid":0 }#line:252
        OOO0OOOOO0O00O0OO =0 #line:253
        while OOO0OOOOO0O00O0OO <10 :#line:254
            O0000O0000OO00O0O =O00O0000O0OOO0O0O .s .post (O0000O0OOO0000O00 ,json =O0O00O0OOO00000O0 ).json ()#line:255
            debugger (f'getread {O0000O0000OO00O0O}')#line:256
            if O0000O0000OO00O0O .get ('code')==200 :#line:257
                O00O0000O0OOO0O0O .link =O0000O0000OO00O0O .get ('data').get ('link')#line:258
                return True #line:259
            elif '获取失败'in O0000O0000OO00O0O .get ('message'):#line:260
                time .sleep (15 )#line:261
                OOO0OOOOO0O00O0OO +=1 #line:262
                continue #line:263
            else :#line:264
                O00O0000O0OOO0O0O .msg +=O0000O0000OO00O0O .get ('message')+'\n'#line:265
                printlog (f'{O00O0000O0OOO0O0O.nickname}:{O0000O0000OO00O0O.get("message")}')#line:266
                return False #line:267
    def gettaskinfo (O0OO00O000O0O0O00 ,OO000O000000O00O0 ):#line:269
        for OO00000OO0O00000O in OO000O000000O00O0 :#line:270
            if OO00000OO0O00000O .get ('url'):#line:271
                return OO00000OO0O00000O #line:272
    def dotasks (OO0OOO0OOOO0OOO00 ):#line:274
        OO0OOOO0OOOO0000O ={'User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','content-type':'application/json','Origin':'http://nei594688.594688be.com.byymmmcm3.cn','Referer':'http://nei594688.594688be.com.byymmmcm3.cn/','Accept-Encoding':'gzip, deflate',}#line:281
        O00OO0OO0O00OO0OO =1 #line:282
        while True :#line:283
            O0O0000OO0OO0000O ={"href":OO0OOO0OOOO0OOO00 .link }#line:284
            OOO000OOO000000O0 ='https://api.wanjd.cn/wxread/articles/tasks'#line:285
            O0OO00OO00O0OOOO0 =requests .post (OOO000OOO000000O0 ,headers =OO0OOOO0OOOO0000O ,json =O0O0000OO0OO0000O ).json ()#line:286
            O00000O0O0O000O0O =O0OO00OO00O0OOOO0 .get ('data')#line:287
            debugger (f'tasks {O00000O0O0O000O0O}')#line:288
            O0OOO0O0OOO0O0OOO =[O00OOO0OOOO00OOOO ['is_read']for O00OOO0OOOO00OOOO in O00000O0O0O000O0O ]#line:289
            if 0 not in O0OOO0O0OOO0O0OOO :#line:290
                break #line:291
            if O0OO00OO00O0OOOO0 .get ('code')!=200 :#line:292
                OO0OOO0OOOO0OOO00 .msg +=O0OO00OO00O0OOOO0 .get ('message')+'\n'#line:293
                printlog (f'{OO0OOO0OOOO0OOO00.nickname}:{O0OO00OO00O0OOOO0.get("message")}')#line:294
                break #line:295
            else :#line:296
                O0OOO00OO000000O0 =OO0OOO0OOOO0OOO00 .gettaskinfo (O0OO00OO00O0OOOO0 ['data'])#line:297
                if not O0OOO00OO000000O0 :#line:298
                    break #line:299
                O00OOOOO0O0O000O0 =O0OOO00OO000000O0 .get ('url')#line:300
                O00OO0OO0OOO0000O =O0OOO00OO000000O0 ['id']#line:301
                debugger (O00OO0OO0OOO0000O )#line:302
                O0O0000OO0OO0000O .update ({"id":O00OO0OO0OOO0000O })#line:303
                O0O0OOO0O0OO0O000 =getmpinfo (O00OOOOO0O0O000O0 )#line:304
                try :#line:305
                    OO0OOO0OOOO0OOO00 .msg +='正在阅读 '+O0O0OOO0O0OO0O000 ['text']+'\n'#line:306
                    printlog (f'{OO0OOO0OOOO0OOO00.nickname}:正在阅读{O0O0OOO0O0OO0O000["text"]}')#line:307
                except :#line:308
                    OO0OOO0OOOO0OOO00 .msg +='正在阅读 '+O0O0OOO0O0OO0O000 ['biz']+'\n'#line:309
                    printlog (f'{OO0OOO0OOOO0OOO00.nickname}:正在阅读 {O0O0OOO0O0OO0O000["biz"]}')#line:310
                if len (str (O00OO0OO0OOO0000O ))<5 :#line:311
                    if O00OO0OO0O00OO0OO ==3 :#line:312
                        if sendable :#line:313
                            send ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',f'{OO0OOO0OOOO0OOO00.nickname} 美添赚检测',)#line:316
                        if pushable :#line:317
                            push ('检测已经三次了，可能账号触发了平台的风险机制，此次任务结束',f'{OO0OOO0OOOO0OOO00.nickname} 美添赚检测',)#line:320
                        raise Exception #line:321
                    if sendable :#line:322
                        send (O0O0OOO0O0OO0O000 .get ('text'),f'{OO0OOO0OOOO0OOO00.nickname} 美添赚过检测',O00OOOOO0O0O000O0 )#line:323
                    if pushable :#line:324
                        push (f'{OO0OOO0OOOO0OOO00.name}\n点击阅读检测文章\n{O0O0OOO0O0OO0O000["text"]}',f'{OO0OOO0OOOO0OOO00.nickname} 美添赚过检测',O00OOOOO0O0O000O0 ,uid =OO0OOO0OOOO0OOO00 .uid )#line:326
                    OO0OOO0OOOO0OOO00 .msg +='发送通知，暂停50秒\n'#line:327
                    printlog (f'{OO0OOO0OOOO0OOO00.nickname}:发送通知，暂停50秒')#line:328
                    O00OO0OO0O00OO0OO +=1 #line:329
                    time .sleep (50 )#line:330
                OO00O00OOOOOOO0OO =random .randint (7 ,10 )#line:331
                time .sleep (OO00O00OOOOOOO0OO )#line:332
                OOO000OOO000000O0 ='https://api.wanjd.cn/wxread/articles/three_read'#line:333
                O0OO00OO00O0OOOO0 =requests .post (OOO000OOO000000O0 ,headers =OO0OOOO0OOOO0000O ,json =O0O0000OO0OO0000O ).json ()#line:334
                if O0OO00OO00O0OOOO0 .get ('code')==200 :#line:335
                    OO0OOO0OOOO0OOO00 .msg +='阅读成功'+'\n'+'-'*50 +'\n'#line:336
                    printlog (f'{OO0OOO0OOOO0OOO00.nickname}:阅读成功')#line:337
                if O0OO00OO00O0OOOO0 .get ('code')!=200 :#line:338
                    OO0OOO0OOOO0OOO00 .msg +=O0OO00OO00O0OOOO0 .get ('message')+'\n'+'-'*50 +'\n'#line:339
                    printlog (f'{OO0OOO0OOOO0OOO00.nickname}:{O0OO00OO00O0OOOO0.get("message")}')#line:340
                    break #line:341
        OOO000OOO000000O0 ='https://api.wanjd.cn/wxread/articles/check_success'#line:342
        O0O0000OO0OO0000O ={'type':1 ,'href':OO0OOO0OOOO0OOO00 .link }#line:343
        O0OO00OO00O0OOOO0 =requests .post (OOO000OOO000000O0 ,headers =OO0OOOO0OOOO0000O ,json =O0O0000OO0OO0000O ).json ()#line:344
        debugger (f'check {O0OO00OO00O0OOOO0}')#line:345
        OO0OOO0OOOO0OOO00 .msg +=O0OO00OO00O0OOOO0 .get ('message')+'\n'#line:346
        printlog (f'{OO0OOO0OOOO0OOO00.nickname}:{O0OO00OO00O0OOOO0.get("message")}')#line:347
    def withdraw (OO0OOOOOO0O00OO0O ):#line:349
        if OO0OOOOOO0O00OO0O .points <txbz :#line:350
            OO0OOOOOO0O00OO0O .msg +=f'没有达到你设置的提现标准{txbz}\n'#line:351
            printlog (f'{OO0OOOOOO0O00OO0O.nickname}:没有达到你设置的提现标准{txbz}')#line:352
            return False #line:353
        OOO0O0OO0O0OOO0OO ='http://api.mengmorwpt1.cn/h5_share/user/withdraw'#line:354
        OO0OO0OO0OO000OOO =OO0OOOOOO0O00OO0O .s .post (OOO0O0OO0O0OOO0OO ).json ()#line:355
        OO0OOOOOO0O00OO0O .msg +='提现结果'+OO0OO0OO0OO000OOO .get ('message')+'\n'#line:356
        printlog (f'{OO0OOOOOO0O00OO0O.nickname}:提现结果 {OO0OO0OO0OO000OOO.get("message")}')#line:357
        if OO0OO0OO0OO000OOO .get ('code')==200 :#line:358
            if sendable :#line:359
                send (f'{OO0OOOOOO0O00OO0O.name} 已提现到红包，请在服务通知内及时领取','每天赚提现通知')#line:360
            if pushable :#line:361
                push (f'{OO0OOOOOO0O00OO0O.name} 已提现到红包，请在服务通知内及时领取','每天赚提现通知',uid =OO0OOOOOO0O00OO0O .uid )#line:362
    def run (O0OOO0O0000OOOO00 ):#line:364
        O0OOO0O0000OOOO00 .msg +='*'*50 +f'\n账号：{O0OOO0O0000OOOO00.name}开始任务\n'#line:365
        printlog (f'账号：{O0OOO0O0000OOOO00.name}开始任务')#line:366
        if not O0OOO0O0000OOOO00 .user_info ():#line:367
            return False #line:368
        if O0OOO0O0000OOOO00 .get_read ():#line:369
            O0OOO0O0000OOOO00 .dotasks ()#line:370
            O0OOO0O0000OOOO00 .user_info ()#line:371
        O0OOO0O0000OOOO00 .withdraw ()#line:372
        printlog (f'账号：{O0OOO0O0000OOOO00.name}:任务结束')#line:373
        if not printf :#line:374
            print (O0OOO0O0000OOOO00 .msg .strip ())#line:375
            print (f'账号：{O0OOO0O0000OOOO00.name}任务结束')#line:376
def yd (OO0O0O0OOO0O0O00O ):#line:379
    while not OO0O0O0OOO0O0O00O .empty ():#line:380
        OO0OOO0000000OO0O =OO0O0O0OOO0O0O00O .get ()#line:381
        O0OO00OO000O00OOO =MTZYD (OO0OOO0000000OO0O )#line:382
        O0OO00OO000O00OOO .run ()#line:383
def get_ver ():#line:386
    O0O0O00O0OO00OO00 ='kmtz V1.7'#line:387
    O0OO00000O00O000O ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:390
    OOOO00O00O0OO000O =requests .get ('https://ghproxy.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json',headers =O0OO00000O00O000O ).json ()#line:392
    O00OOOOO000O0OOO0 =O0O0O00O0OO00OO00 .split (' ')[1 ]#line:393
    OOO0OOO0O00OO0O00 =OOOO00O00O0OO000O .get ('version').get (O0O0O00O0OO00OO00 .split (' ')[0 ])#line:394
    OO0OOO0OO0O000OOO =f"当前版本 {O00OOOOO000O0OOO0}，仓库版本 {OOO0OOO0O00OO0O00}"#line:395
    if O00OOOOO000O0OOO0 <OOO0OOO0O00OO0O00 :#line:396
        OO0OOO0OO0O000OOO +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:397
    return OO0OOO0OO0O000OOO #line:398
def main ():#line:401
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:402
    O0OOOO0000OOOO0O0 =os .getenv ('mtzck')#line:403
    if not O0OOOO0000OOOO0O0 :#line:404
        print ('请仔细阅读上方注释并配置好key和ck')#line:405
        exit ()#line:406
    try :#line:407
        O0OOOO0000OOOO0O0 =ast .literal_eval (O0OOOO0000OOOO0O0 )#line:408
    except :#line:409
        O0OOOO0000OOOO0O0 =O0OOOO0000OOOO0O0 .split ('&')#line:410
    O00O0000O0OO00OOO =Queue ()#line:411
    OOO00OOOOOO0OOO00 =[]#line:412
    for O0000000O0OO0O0O0 ,OO0OO0O00OO00O00O in enumerate (O0OOOO0000OOOO0O0 ,start =1 ):#line:413
        printlog (f'{OO0OO0O00OO00O00O}\n以上是账号{O0000000O0OO0O0O0}的ck，如不正确，请检查ck填写格式')#line:414
        if isinstance (OO0OO0O00OO00O00O ,dict ):#line:415
            O00O0000O0OO00OOO .put (OO0OO0O00OO00O00O )#line:416
        else :#line:417
            O00O0000O0OO00OOO .put (ast .literal_eval (OO0OO0O00OO00O00O ))#line:418
    for O0000000O0OO0O0O0 in range (max_workers ):#line:419
        OO000O00OOOO0OOOO =threading .Thread (target =yd ,args =(O00O0000O0OO00OOO ,))#line:420
        OO000O00OOOO0OOOO .start ()#line:421
        OOO00OOOOOO0OOO00 .append (OO000O00OOOO0OOOO )#line:422
        time .sleep (20 )#line:423
    for OO0OOOOO0O0O0000O in OOO00OOOOOO0OOO00 :#line:424
        OO0OOOOO0O0O0000O .join ()#line:425
if __name__ =='__main__':#line:428
    main ()#line:429
