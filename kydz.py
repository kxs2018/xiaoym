# -*- coding: utf-8 -*-
# kydz
# Author: kk
# date：2023/9/24 18:19
"""
仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
入口：http://5851278349.buemxve.cn/?jgwq=3340348&goid=itrb
http://5851278349.buemxve.cn/?jgwq=3340348&goid=itrb 抓包这个链接 抓出唯一一个cookie 把7bfe3c8f4d51851的值
或者http://wxr.jjyii.com/user/getinfo?v=3 a_h_n值/后面的字符串 填入ck
建议手动阅读几篇再使用脚本！！！
推送检测文章   将多个账号检测文章推送至将多个账号检测文章推送至目标微信目标微信，手动点击链接完成检测阅读
key为企业微信webhook机器人后面的 key
===============================================================
青龙面板，在配置文件里添加
export qwbotkey="key"
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
debug = 1
"""1为开，打印调试日志；0为关，不打印"""

"""线程数量设置"""
max_workers = 3
"""设置为5，即最多有5个任务同时进行"""

"""设置提现标准"""
txbz = 3000  # 不低于3000，平台标准为3000
"""设置为8000，即为8毛起提"""

qwbotkey =os .getenv ('qwbotkey')#line:55
if not qwbotkey :#line:56
    print ('请仔细阅读脚本上方注释，配置好qwbotkey')#line:57
    exit ()#line:58
checklist =['MzU2OTczNzcwNg==','MzU5NTczMzA0MQ==','MzUwOTk5NDI0MQ==','MjM5Mjc5NjMyMw==','MzIxNjEzMDg2OQ==','MzUyMzk1MTAyNg==','MzI0MjE5MTc0OA==','MzU1ODI4MjI4Nw==','Mzg4OTA1MzI0Ng==','Mzg2MTI0Mzc1Nw==','MzU5NzgwMTgwMQ==','MzI3MTA5MTkwNQ==','Mzg5NjcyMzgyOA==','MjM5NjY4Mzk5OQ==','MzI1MDAwNDY1NA==','MjM5MTA5ODYzNQ==','MzAwNzA3MDAzMw==','MzkzMjUyNTk1OA==']#line:63
def ftime ():#line:66
    OO0O0OOOO0O00O0OO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:67
    return OO0O0OOOO0O00O0OO #line:68
def debugger (O000OOO0O0O0OOOOO ):#line:71
    if debug :#line:72
        print (O000OOO0O0O0OOOOO )#line:73
def printlog (OO0O0O0O000O0OO00 ):#line:76
    if printf :#line:77
        print (OO0O0O0O000O0OO00 )#line:78
def send (OOOO0O00O0O000OO0 ,title ='通知',url =None ):#line:81
    if not url :#line:82
        O00O0OOOO0OO00O0O ={"msgtype":"text","text":{"content":f"{title}\n\n{OOOO0O00O0O000OO0}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",}}#line:89
    else :#line:90
        O00O0OOOO0OO00O0O ={"msgtype":"news","news":{"articles":[{"title":title ,"description":OOOO0O00O0O000OO0 ,"url":url ,"picurl":'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}#line:95
    OO0OOO0OOOO000OO0 =f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'#line:96
    OOOO000OO0O0O0OOO =requests .post (OO0OOO0OOOO000OO0 ,data =json .dumps (O00O0OOOO0OO00O0O )).json ()#line:97
    if OOOO000OO0O0O0OOO .get ('errcode')!=0 :#line:98
        print ('消息发送失败，请检查key和发送格式')#line:99
        return False #line:100
    return OOOO000OO0O0O0OOO #line:101
def getmpinfo (OOO000O0O0O0O00OO ):#line:104
    if not OOO000O0O0O0O00OO or OOO000O0O0O0O00OO =='':#line:105
        return False #line:106
    O0OO0O0O00O0O0O00 ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}#line:108
    O00OO0O000OO0O000 =requests .get (OOO000O0O0O0O00OO ,headers =O0OO0O0O00O0O0O00 )#line:109
    OO0OOOO00O0OO0O0O =etree .HTML (O00OO0O000OO0O000 .text )#line:110
    O00O0O0000OO000OO =OO0OOOO00O0OO0O0O .xpath ('//meta[@*="og:title"]/@content')#line:111
    if O00O0O0000OO000OO :#line:112
        O00O0O0000OO000OO =O00O0O0000OO000OO [0 ]#line:113
    OOO0OO000OOO000O0 =OO0OOOO00O0OO0O0O .xpath ('//meta[@*="og:url"]/@content')#line:114
    if OOO0OO000OOO000O0 :#line:115
        OOO0OO000OOO000O0 =OOO0OO000OOO000O0 [0 ].encode ().decode ()#line:116
    try :#line:117
        OOOO0O0OOO0OOO0OO =re .findall (r'biz=(.*?)&',OOO000O0O0O0O00OO )#line:118
    except :#line:119
        OOOO0O0OOO0OOO0OO =re .findall (r'biz=(.*?)&',OOO0OO000OOO000O0 )#line:120
    if OOOO0O0OOO0OOO0OO :#line:121
        OOOO0O0OOO0OOO0OO =OOOO0O0OOO0OOO0OO [0 ]#line:122
    else :#line:123
        return False #line:124
    OO00O0000O0OO0O00 =OO0OOOO00O0OO0O0O .xpath ('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')#line:125
    if OO00O0000O0OO0O00 :#line:126
        OO00O0000O0OO0O00 =OO00O0000O0OO0O00 [0 ].strip ()#line:127
    OO0O0000O0OOOO00O =re .findall (r"user_name.DATA'\) : '(.*?)'",O00OO0O000OO0O000 .text )or OO0OOOO00O0OO0O0O .xpath ('//span[@class="profile_meta_value"]/text()')#line:129
    if OO0O0000O0OOOO00O :#line:130
        OO0O0000O0OOOO00O =OO0O0000O0OOOO00O [0 ]#line:131
    OOO00000OO00O0O00 =re .findall (r'createTime = \'(.*)\'',O00OO0O000OO0O000 .text )#line:132
    if OOO00000OO00O0O00 :#line:133
        OOO00000OO00O0O00 =OOO00000OO00O0O00 [0 ][5 :]#line:134
    OOOO00OOO0OO000OO =f'{OOO00000OO00O0O00}|{O00O0O0000OO000OO}|{OOOO0O0OOO0OOO0OO}|{OO00O0000O0OO0O00}|{OO0O0000O0OOOO00O}'#line:135
    OOO0O000OOOO0000O ={'biz':OOOO0O0OOO0OOO0OO ,'text':OOOO00OOO0OO000OO }#line:136
    return OOO0O000OOOO0000O #line:137
class YDZ :#line:140
    def __init__ (O0000OOO00O000OO0 ,OOOOO0O000O0000OO ):#line:141
        O0000OOO00O000OO0 .name =OOOOO0O000O0000OO .get ('name')#line:142
        O0000OOO00O000OO0 .s =requests .session ()#line:143
        O0000OOO00O000OO0 .ck =OOOOO0O000O0000OO .get ('ck')#line:144
        O0000OOO00O000OO0 .msg =''#line:145
        O0000OOO00O000OO0 .s .headers ={'Proxy-Connection':'keep-alive','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8431 Flue','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9','a_h_n':f'http%3A%2F%2F5851535337.udqyeba.cn%2F%3Fjgwq%3D3340348%26goid%3Ditrb/{O0000OOO00O000OO0.ck}','cookie':f'7bfe3c8f4d51851={O0000OOO00O000OO0.ck}'}#line:152
    def init (OOO0OOO0O0O0000O0 ):#line:154
        try :#line:155
            OOOO000OOOO0O0O0O ='http://5851599460.udqyeba.cn/?jgwq=3340348&goid=itrb'#line:156
            O0O0O0OOO00OO0O00 =OOO0OOO0O0O0000O0 .s .get (OOOO000OOOO0O0O0O ).text #line:157
            O0O0O0OOO00OO0O00 =re .sub ('\s','',O0O0O0OOO00OO0O00 )#line:159
            OOO0OOO0O0O0000O0 .nickname =re .findall (r'nname=\'(.*?)\',',O0O0O0OOO00OO0O00 )[0 ]#line:160
            O0000O000O00O0000 =re .findall (r'uid=\'(\d+)\'',O0O0O0OOO00OO0O00 )[0 ]#line:161
            OO00OOOO000000O00 =f'http://58515{random.randint(10000, 99999)}.udqyeba.cn/?jgwq={O0000O000O00O0000}&goid=itrb/{OOO0OOO0O0O0000O0.ck}'#line:162
            OOO0OOO0O0O0000O0 .s .headers .update ({'a_h_n':OO00OOOO000000O00 })#line:163
            return True #line:164
        except :#line:165
            printlog (f'{OOO0OOO0O0O0000O0.name} 账号信息获取错误，请检查ck有效性')#line:166
            OOO0OOO0O0O0000O0 .msg +='账号信息获取错误，请检查ck有效性\n'#line:167
            return False #line:168
    def getinfo (OO0O0O000O00O0OO0 ):#line:170
        O00O0OOO0O0O0O0OO ='http://wxr.jjyii.com/user/getinfo?v=3'#line:171
        OO000OOO0OOOO0000 =OO0O0O000O00O0OO0 .s .get (O00O0OOO0O0O0O0OO ).json ()#line:172
        debugger (f'getinfo2 {OO000OOO0OOOO0000}')#line:173
        OO00O0000OOOOOOOO =OO000OOO0OOOO0000 .get ('data')#line:174
        OO0O0O000O00O0OO0 .count =OO00O0000OOOOOOOO .get ('count')#line:175
        OO0O0O000O00O0OO0 .gold =OO00O0000OOOOOOOO .get ('balance')#line:176
        OOOOO00000OOO0OOO =OO00O0000OOOOOOOO .get ('hm')#line:177
        O00OO0O00O00O000O =OO00O0000OOOOOOOO .get ('hs')#line:178
        printlog (f'账号:{OO0O0O000O00O0OO0.nickname},当前金币{OO0O0O000O00O0OO0.gold}，今日已读{OO0O0O000O00O0OO0.count}')#line:179
        OO0O0O000O00O0OO0 .msg +=f'账号:{OO0O0O000O00O0OO0.nickname},当前金币{OO0O0O000O00O0OO0.gold}，今日已读{OO0O0O000O00O0OO0.count}\n'#line:180
        if OOOOO00000OOO0OOO !=0 or O00OO0O00O00O000O !=0 :#line:181
            printlog (f'{OO0O0O000O00O0OO0.nickname} 本轮次已结束，{OOOOO00000OOO0OOO}分钟后可继续任务')#line:182
            OO0O0O000O00O0OO0 .msg +='本轮次已结束，{hm}分钟后可继续任务\n'#line:183
            return False #line:184
        return True #line:185
    def read (O0O00O00O0OOOO00O ):#line:187
        OOO00O0OO0OOO00OO ='http://wxr.jjyii.com/r/get?v=10'#line:188
        OO0O00O00O0OO0000 ={'o':f'http://58517{random.randint(10000, 99999)}.ulzqwjf.cn/?a=gt','goid':'itrb','_v':'3890','t':'quick'}#line:190
        OO0O0O000O0000O0O =0 #line:191
        O00000OOOOO0000O0 =0 #line:192
        while OO0O0O000O0000O0O <30 and O00000OOOOO0000O0 <5 :#line:193
            if not O0O00O00O0OOOO00O .getinfo ():#line:194
                break #line:195
            O000000O00O000000 =O0O00O00O0OOOO00O .s .post (OOO00O0OO0OOO00OO ,data =OO0O00O00O0OO0000 ).json ()#line:196
            debugger (f'read {O000000O00O000000}')#line:197
            OO000O0000O0OOO00 =O000000O00O000000 .get ('data').get ('url')#line:198
            if not OO000O0000O0OOO00 :#line:199
                printlog (f'{O0O00O00O0OOOO00O.nickname} 没有获取到阅读链接，正在重试')#line:200
                O0O00O00O0OOOO00O .msg +='没有获取到阅读链接，正在重试\n'#line:201
                time .sleep (5 )#line:202
                O00000OOOOO0000O0 +=1 #line:203
                continue #line:204
            O0OO000000OO0OO0O =getmpinfo (OO000O0000O0OOO00 )#line:205
            try :#line:206
                printlog (f'{O0O00O00O0OOOO00O.nickname} 正在阅读 {O0OO000000OO0OO0O["text"]}')#line:207
                O0O00O00O0OOOO00O .msg +=f'正在阅读 {O0OO000000OO0OO0O["text"]}\n'#line:208
            except :#line:209
                printlog (f'{O0O00O00O0OOOO00O.nickname} 正在阅读 {O0OO000000OO0OO0O["biz"]}')#line:210
                O0O00O00O0OOOO00O .msg +=f'正在阅读 {O0OO000000OO0OO0O["biz"]}\n'#line:211
            if O0OO000000OO0OO0O ['biz']in checklist or ('chksm='in OO000O0000O0OOO00 ):#line:212
                print ('biz ',O0OO000000OO0OO0O ['biz']in checklist )#line:213
                print ('链接 ','chksm='in OO000O0000O0OOO00 )#line:214
                printlog (f'{O0O00O00O0OOOO00O.nickname} 正在阅读检测文章，发送通知，暂停50秒')#line:215
                O0O00O00O0OOOO00O .msg +='正在阅读检测文章，发送通知，暂停50秒\n'#line:216
                send (f'{O0O00O00O0OOOO00O.nickname}\n点击阅读检测文章',f'{O0O00O00O0OOOO00O.name} 阅读赚过检测',OO000O0000O0OOO00 )#line:217
                time .sleep (60 )#line:218
            OO0O0O000O000OOOO =random .randint (7 ,10 )#line:219
            O0O00O00O0OOOO00O .msg +='模拟阅读{t}秒\n'#line:220
            time .sleep (OO0O0O000O000OOOO )#line:221
            O0O000000O0OOOO0O ='http://wxr.jjyii.com/r/ck'#line:222
            O0OOOO0000OO0000O ={'Accept':'application/json, text/javascript, */*; q=0.01','Origin':'http://5851780833.ebrmrwy.cn','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',}#line:225
            O0O00O00O0OOOO00O .s .headers .update (O0OOOO0000OO0000O )#line:226
            O000000O00O000000 =O0O00O00O0OOOO00O .s .post (O0O000000O0OOOO0O ,data ={'t':'quick'}).json ()#line:227
            debugger (f'check {O000000O00O000000}')#line:228
            O00O0OOOO0OOO00O0 =O000000O00O000000 .get ('data').get ('gold')#line:229
            if O00O0OOOO0OOO00O0 :#line:230
                printlog (f'{O0O00O00O0OOOO00O.nickname} 阅读成功，获得金币{O00O0OOOO0OOO00O0}')#line:231
                O0O00O00O0OOOO00O .msg +=f'阅读成功，获得金币{O00O0OOOO0OOO00O0}\n'#line:232
            OO0O0O000O0000O0O +=1 #line:233
    def cash (OOO000000O00OOO00 ):#line:235
        if OOO000000O00OOO00 .gold <txbz :#line:236
            printlog (f'{OOO000000O00OOO00.nickname} 你的金币不多了')#line:237
            OOO000000O00OOO00 .msg +='你的金币不多了\n'#line:238
            return False #line:239
        O00OOOO000O000000 =int (OOO000000O00OOO00 .gold /1000 )*1000 #line:240
        printlog (f'{OOO000000O00OOO00.nickname} 本次提现：{O00OOOO000O000000}')#line:241
        OOO000000O00OOO00 .msg +=f'本次提现：{O00OOOO000O000000}\n'#line:242
        O0O00000OO0OOO000 ='http://wxr.jjyii.com/mine/cash'#line:243
        O00OOOO00O0OO0OO0 =OOO000000O00OOO00 .s .post (O0O00000OO0OOO000 )#line:244
        if O00OOOO00O0OO0OO0 .json ().get ('code')==1 :#line:245
            printlog (f'{OOO000000O00OOO00.nickname} 提现成功')#line:246
            OOO000000O00OOO00 .msg +='提现成功\n'#line:247
        else :#line:248
            debugger (O00OOOO00O0OO0OO0 .text )#line:249
            printlog (f'{OOO000000O00OOO00.nickname} 提现失败')#line:250
            OOO000000O00OOO00 .msg +='提现失败\n'#line:251
    def run (OOO0OOOO0000000OO ):#line:253
        if OOO0OOOO0000000OO .init ():#line:254
            OOO0OOOO0000000OO .read ()#line:255
        OOO0OOOO0000000OO .cash ()#line:256
        if not printf :#line:257
            print (OOO0OOOO0000000OO .msg )#line:258
def yd (O000OO0000O00OOO0 ):#line:261
    while not O000OO0000O00OOO0 .empty ():#line:262
        OOO0OOO0O00O0O0O0 =O000OO0000O00OOO0 .get ()#line:263
        O0O00000000OOOO0O =YDZ (OOO0OOO0O00O0O0O0 )#line:264
        O0O00000000OOOO0O .run ()#line:265
def get_ver ():#line:268
    OOO00OOOOO0OO0O0O ='kydz V0.1.3'#line:269
    O00O00O000OOOO0O0 ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:272
    OO00O0000OOO00O0O =requests .get ('https://ghproxy.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json',headers =O00O00O000OOOO0O0 ).json ()#line:274
    OO0OO00OO0OO000OO =OOO00OOOOO0OO0O0O .split (' ')[1 ]#line:275
    O00O0O00OOOO0O0OO =OO00O0000OOO00O0O .get ('version').get (OOO00OOOOO0OO0O0O .split (' ')[0 ])#line:276
    OOO0O00OOOOOOOOOO =f"当前版本 {OO0OO00OO0OO000OO}，仓库版本 {O00O0O00OOOO0O0OO}"#line:277
    if OO0OO00OO0OO000OO <O00O0O00OOOO0O0OO :#line:278
        OOO0O00OOOOOOOOOO +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:279
    return OOO0O00OOOOOOOOOO #line:280
def main ():#line:283
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:284
    O0000OO00O0OOO0O0 =os .getenv ('ydzck')#line:285
    if not O0000OO00O0OOO0O0 :#line:286
        print ('仔细阅读脚本上方注释，配置好ydzck')#line:287
        return False #line:288
    try :#line:289
        O0000OO00O0OOO0O0 =ast .literal_eval (O0000OO00O0OOO0O0 )#line:290
    except :#line:291
        pass #line:292
    OO000OOOOO00OOOOO =[]#line:293
    OO00OOOO0OO00OO00 =Queue ()#line:294
    for O00O000O0OOOOOOOO ,O000OO00OOO00OO00 in enumerate (O0000OO00O0OOO0O0 ):#line:295
        printlog (f'{O000OO00OOO00OO00}\n以上是账号{O00O000O0OOOOOOOO}的ck，请核对是否正确，如不正确，请检查ck填写格式')#line:296
        OO00OOOO0OO00OO00 .put (O000OO00OOO00OO00 )#line:297
    for O00O000O0OOOOOOOO in range (max_workers ):#line:298
        OOO000O000O000O00 =threading .Thread (target =yd ,args =(OO00OOOO0OO00OO00 ,))#line:299
        OOO000O000O000O00 .start ()#line:300
        OO000OOOOO00OOOOO .append (OOO000O000O000O00 )#line:301
        time .sleep (30 )#line:302
    for O0000OO0O0OO0O000 in OO000OOOOO00OOOOO :#line:303
        O0000OO0O0OO0O000 .join ()#line:304
if __name__ =='__main__':#line:307
    main ()#line:308
