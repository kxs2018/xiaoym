# -*- coding: utf-8 -*-
# k_ghdy
# Author: 惜之酱
"""
先运行脚本，三次之后再有问题到群里问
new Env('歌画东阳');
"""
import ast
import hashlib
import random
import string
from queue import Queue
from urllib.parse import urlparse
import threading
import time
import requests
import os
import datetime
def get_msg ():#line:21
    OOO0O0O00O0OOOO0O ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:23
    O00O000O0000OO00O =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OOO0O0O00O0OOOO0O ).json ()#line:24
    return O00O000O0000OO00O #line:25
_O0OO000O0OO000000 =get_msg ()#line:28
def ftime ():#line:31
    OO00000O00O0OOOOO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:32
    return OO00000O00O0OOOOO #line:33
def load_notify ():#line:36
    global send #line:37
    try :#line:38
        from notify import send #line:39
        print ("加载通知服务成功！")#line:40
        return True #line:41
    except :#line:42
        send =False #line:43
        print ('加载通知服务失败')#line:44
        return False #line:45
def gen_string (OO00OO0OOOOO000O0 ):#line:48
    O0OO0000OOO0O0O00 =string .ascii_lowercase +string .digits #line:49
    OOO0O0O00000000OO =''.join (random .choice (O0OO0000OOO0O0O00 )for OO0O00OO000O0O000 in range (OO00OO0OOOOO000O0 ))#line:50
    return OOO0O0O00000000OO #line:51
def gen_requestid ():#line:54
    OOO000OOOOOO0O0O0 =f'{gen_string(8)}-{gen_string(4)}-{gen_string(4)}-{gen_string(4)}-{gen_string(12)}'#line:55
    return OOO000OOOOOO0O0O0 #line:56
def sha_256 (OOO00OOO0OO0000OO ):#line:59
    OOOO00O0O0OO00O0O =hashlib .sha256 ()#line:60
    OOOO00O0O0OO00O0O .update (OOO00OOO0OO0000OO .encode ('utf-8'))#line:61
    OOO0000O0O0O00OOO =OOOO00O0O0OO00O0O .hexdigest ()#line:62
    return OOO0000O0O0O00OOO #line:63
def is_morning ():#line:66
    OO00O0000000OO000 =datetime .datetime .now ().hour #line:67
    return True if OO00O0000000OO000 <12 else False #line:68
class GHDY :#line:71
    def __init__ (OO0OOO0O0O0O00OOO ,O0OO000OOO0O0O000 ,O00O0O000O00000OO ):#line:72
        OO0OOO0O0O0O00OOO .index =O0OO000OOO0O0O000 #line:73
        OO0OOO0O0O0O00OOO .sessionid =O00O0O000O00000OO .get ('sessionid')#line:74
        OO0OOO0O0O0O00OOO .accountid =O00O0O000O00000OO .get ('accountid')#line:75
        OO0OOO0O0O0O00OOO .id_list =[] #line:76
        OO0OOO0O0O0O00OOO .headers ={'X-SESSION-ID':OO0OOO0O0O0O00OOO .sessionid ,'X-TENANT-ID':'49','User-Agent':'5.0.9.0.2;00000000-6634-51c0-0000-00000f8829df;HONOR ANY-AN00;Android;13;Release','X-ACCOUNT-ID':OO0OOO0O0O0O00OOO .accountid ,'Cache-Control':'no-cache','Host':'vapp.tmuyun.com','Connection':'Keep-Alive','Accept-Encoding':'gzip'}#line:80
        OO0OOO0O0O0O00OOO ._headers ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36;xsb_dongyang;xsb_dongyang;5.0.9.0.2;native_app;6.5.0','Host':'fijdzpur.act.tmuact.com','Connection':'keep-alive','Pragma':'no-cache','Cache-Control':'no-cache','Accept':'application/json, text/plain, */*','X-Requested-With':'XMLHttpRequest','Content-Type':'application/x-www-form-urlencoded','Origin':'https://fijdzpur.act.tmuact.com','Sec-Fetch-Site':'same-origin','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://fijdzpur.act.tmuact.com/money/index/index.html','Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'}#line:89
        OO0OOO0O0O0O00OOO .msg =''#line:90
        OO0OOO0O0O0O00OOO .name =''#line:91
    def gen_dict (O000OO0O0OO0OOO0O ,O0OOOO000000OOOO0 ):#line:93
        OO000OOOOO00O0O0O =urlparse (O0OOOO000000OOOO0 ).path #line:94
        OOOOOO0O0OOOOOOOO =int (time .time ()*1000 )#line:95
        OO0O0OOOO00O00O00 =gen_requestid ()#line:96
        OO0O0OO0000OO0O0O =f'{OO000OOOOO00O0O0O}&&{O000OO0O0OO0OOO0O.sessionid}&&{OO0O0OOOO00O00O00}&&{OOOOOO0O0OOOOOOOO}&&FR*r!isE5W&&49'#line:97
        OOO00OO0O0000000O ={'X-TIMESTAMP':str (OOOOOO0O0OOOOOOOO ),'X-REQUEST-ID':OO0O0OOOO00O00O00 ,'X-SIGNATURE':sha_256 (OO0O0OO0000OO0O0O )}#line:98
        return OOO00OO0O0000000O #line:99
    def userinfo (O0O00O0OOO0OO0OO0 ):#line:101
        O000OOOOO00OOO0OO ="https://vapp.tmuyun.com/api/user_mumber/account_detail"#line:102
        O00OOOOO00OOO0O00 =O0O00O0OOO0OO0OO0 .gen_dict (O000OOOOO00OOO0OO )#line:103
        OOO0O00000000O0OO ={**O0O00O0OOO0OO0OO0 .headers ,**O00OOOOO00OOO0O00 }#line:104
        OO0O00000O0O0O00O =requests .get (O000OOOOO00OOO0OO ,headers =OOO0O00000000O0OO ).json ()#line:105
        if OO0O00000O0O0O00O .get ('code')==0 :#line:106
            O0O00O0OOO0OO0OO0 .name =OO0O00000O0O0O00O .get ('data').get ('rst').get ('nick_name')#line:107
            print (f'【{O0O00O0OOO0OO0OO0.name}】:✅登录成功')#line:108
            O0O00O0OOO0OO0OO0 .msg +=f'【{O0O00O0OOO0OO0OO0.name}】:✅登录成功\n'#line:109
            return True #line:110
        else :#line:111
            print (f'【账号{O0O00O0OOO0OO0OO0.index}】:❌登录失败')#line:112
            O0O00O0OOO0OO0OO0 .msg +=f'【账号{O0O00O0OOO0OO0OO0.index}】:❌登录失败\n'#line:113
            return False #line:114
    def tx (OO000OOOO0O0OOO0O ):#line:116
        OO00000000O0OOO00 ="https://wallet.act.tmuact.com/activity/api.php"#line:117
        O0OOOOO0O00OOO0O0 ={'m':'front','subm':'money_wallet','action':'commonchange','account_id':OO000OOOO0O0OOO0O .accountid ,'session_id':OO000OOOO0O0OOO0O .sessionid ,'app':'XSB_DONGYANG'}#line:119
        OO000O00OOOOOOOOO =requests .post (OO00000000O0OOO00 ,headers =OO000OOOO0O0OOO0O ._headers ,data =O0OOOOO0O00OOO0O0 ).json ()#line:120
        OOOO0O0O0O0000O00 =OO000O00OOOOOOOOO ["msg"]#line:121
        if OO000O00OOOOOOOOO .get ('status'):#line:122
            print (f'【{OO000OOOO0O0OOO0O.name}】:✅{OO000O00OOOOOOOOO["msg"]}')#line:123
            OO000OOOO0O0OOO0O .msg +=f'【{OO000OOOO0O0OOO0O.name}】:✅{OO000O00OOOOOOOOO["msg"]}\n'#line:124
        else :#line:125
            print (f'【{OO000OOOO0O0OOO0O.name}】:❌{OOOO0O0O0O0000O00}')#line:126
            OO000OOOO0O0OOO0O .msg +=f'【{OO000OOOO0O0OOO0O.name}】:❌{OOOO0O0O0O0000O00}\n'#line:127
    def get_article (OOO000O0OO00OOO00 ):#line:129
        O0O0OOO000O00O0OO ='https://vapp.tmuyun.com/api/article/channel_list'#line:130
        O0O0O0000O00OO0O0 =OOO000O0OO00OOO00 .gen_dict (O0O0OOO000O00O0OO )#line:131
        OO0O00000O0000O0O ={**OOO000O0OO00OOO00 .headers ,**O0O0O0000O00OO0O0 }#line:132
        OO0000O00OO0OOOO0 ={'channel_id':'6254f12dfe3fc10794f7b25c','isDiFangHao':'false','is_new':'true','list_count':'0','size':'20'}#line:134
        O0000O0OOOO00OO0O =requests .get (O0O0OOO000O00O0OO ,headers =OO0O00000O0000O0O ,params =OO0000O00OO0OOOO0 ).json ()#line:135
        if O0000O0OOOO00OO0O .get ('code')==0 :#line:136
            O00OO0OO0OOO0O00O =O0000O0OOOO00OO0O .get ('data').get ('article_list')#line:137
            O00O0OOO0000O000O =[O000OOO00000OO0OO ['id']for O000OOO00000OO0OO in O00OO0OO0OOO0O00O ]#line:138
            while len (OOO000O0OO00OOO00 .id_list )<5 :#line:139
                O0OO0000O0OO0OO0O =random .choice (O00O0OOO0000O000O )#line:140
                OOO000O0OO00OOO00 .id_list .append (O0OO0000O0OO0OO0O )#line:141
                O00O0OOO0000O000O .remove (O0OO0000O0OO0OO0O )#line:142
        elif '不存在'in O0000O0OOOO00OO0O ['message']:#line:143
            OOO00O0OO0O0O0000 =f'【{OOO000O0OO00OOO00.name}】:⛔️文章加载失败 {O0000O0OOOO00OO0O["message"]}'#line:144
            OOO000O0OO00OOO00 .msg +=OOO00O0OO0O0O0000 +'\n'#line:145
            print (OOO00O0OO0O0O0000 )#line:146
        else :#line:147
            OOO00O0OO0O0O0000 =f'【{OOO000O0OO00OOO00.name}】:❌请求异常 {O0000O0OOOO00OO0O["message"]}'#line:148
            print (OOO00O0OO0O0O0000 )#line:149
            OOO000O0OO00OOO00 .msg +=OOO00O0OO0O0O0000 +'\n'#line:150
    def read (OOOOO00O00O00O0OO ):#line:152
        OO0OOOOO0O000O0OO ='https://vapp.tmuyun.com/api/article/detail'#line:153
        OO0O0O0OO0O000000 =OOOOO00O00O00O0OO .gen_dict (OO0OOOOO0O000O0OO )#line:154
        OO0OOO0000O0O000O ={**OOOOO00O00O00O0OO .headers ,**OO0O0O0OO0O000000 }#line:155
        for OO00OOOOO00OOOO0O in OOOOO00O00O00O0OO .id_list :#line:156
            O0O00O0O0OO00O000 ={'id':OO00OOOOO00OOOO0O }#line:157
            OOO0OO0OOO0OOO0O0 =requests .get (OO0OOOOO0O000O0OO ,params =O0O00O0O0OO00O000 ,headers =OO0OOO0000O0O000O ).json ()#line:158
            if OOO0OO0OOO0OOO0O0 ['code']==0 :#line:159
                print (f'【{OOOOO00O00O00O0OO.name}】:✅浏览《{OOO0OO0OOO0OOO0O0["data"]["article"]["list_title"]}》成功')#line:160
                time .sleep (random .randint (3 ,8 ))#line:161
            elif '不存在'in OOO0OO0OOO0OOO0O0 ['message']:#line:162
                print (f'【{OOOOO00O00O00O0OO.name}】:⛔️浏览失败 {OOO0OO0OOO0OOO0O0["message"]}')#line:163
                OOOOO00O00O00O0OO .msg +=f'【{OOOOO00O00O00O0OO.name}】:⛔️浏览失败 {OOO0OO0OOO0OOO0O0["message"]}\n'#line:164
            else :#line:165
                print (f'【{OOOOO00O00O00O0OO.name}】:❌浏览异常 {OOO0OO0OOO0OOO0O0["message"]}')#line:166
                OOOOO00O00O00O0OO .msg +=f'【{OOOOO00O00O00O0OO.name}】:❌浏览异常 {OOO0OO0OOO0OOO0O0["message"]}\n'#line:167
        O0OO00OOOOO00O0OO =f'【{OOOOO00O00O00O0OO.name}】:✅浏览完成，登录APP抽红包吧！'#line:168
        print (O0OO00OOOOO00O0OO )#line:169
        OOOOO00O00O00O0OO .msg +=O0OO00OOOOO00O0OO +'\n'#line:170
    def run (OO00O0O000O0000OO ):#line:172
        if OO00O0O000O0000OO .userinfo ():#line:173
            OO00O0O000O0000OO .tx ()#line:174
            if is_morning ():#line:175
                OO00O0O000O0000OO .get_article ()#line:176
                OO00O0O000O0000OO .read ()#line:177
        return OO00O0O000O0000OO .msg #line:178
def ghdy (OOOOOOO000000O000 ,O0000OOOOO00O0O0O ):#line:181
    while not OOOOOOO000000O000 .empty ():#line:182
        O0OOOO0O0OO0OOOO0 ,OOO0O00OO000O00O0 =OOOOOOO000000O000 .get ()#line:183
        O0O000OOO0O0O0000 =GHDY (O0OOOO0O0OO0OOOO0 ,OOO0O00OO000O00O0 )#line:184
        O0000OOOOO00O0O0O .put (O0O000OOO0O0O0000 .run ())#line:185
def get_info ():#line:188
    print ("="*50 +f'\n✅github仓库：https://github.com/kxs2018/xiaoym\n✅极狐仓库:https://jihulab.com/xizhiai/xiaoym\n✅By:惜之酱\t\thttp://t.me/xiaoymgroup\n'+'-'*50 )#line:190
    print (f"✅{_O0OO000O0OO000000.get('msg')['歌画东阳']}")#line:191
    OO0000OOO00O00OO0 ='v1.1'#line:192
    O000OO000O0OO0OOO =_O0OO000O0OO000000 ['version']['歌画东阳']#line:193
    print ('-'*50 +f'\n当前版本{OO0000OOO00O00OO0}，仓库版本{O000OO000O0OO0OOO}\n✅{_O0OO000O0OO000000["update_log"]["歌画东阳"]}')#line:194
    if OO0000OOO00O00OO0 <O000OO000O0OO0OOO :#line:195
        print ('⛔️请到仓库下载最新版本k_xyy.py')#line:196
    print ("="*50 )#line:197
    return True #line:198
def main ():#line:201
    O00000OO0OOO0OO0O =get_info ()#line:202
    OO0OOO0OOOO0OOOOO =os .getenv ('ghdyck')#line:203
    try :#line:204
        OO0OOO0OOOO0OOOOO =ast .literal_eval (OO0OOO0OOOO0OOOOO )#line:205
    except :#line:206
        pass #line:207
    if not OO0OOO0OOOO0OOOOO :#line:208
        print ('❌没有获取到ck，程序退出')#line:209
        exit ()#line:210
    if not load_notify ():#line:211
        print ('❌加载通知模块失败，请复制青龙的notify.py到同级文件夹，并做好相关参数设置')#line:212
    print (f'✅共获取到{len(OO0OOO0OOOO0OOOOO)}个账号，如与实际不符，请检查ck填写格式')#line:213
    if not O00000OO0OOO0OO0O :#line:214
        exit ()#line:215
    OO000O0O00OOOOO00 =Queue ()#line:216
    O00O0O00OOOO000O0 =Queue ()#line:217
    OO000OO00000OOO0O =[]#line:218
    OO0000O00OOOO0OOO =[]#line:219
    for O000O0OO0O00O0O0O ,OOOO0000OOOO00OO0 in enumerate (OO0OOO0OOOO0OOOOO ,start =1 ):#line:220
        OO000O0O00OOOOO00 .put ([O000O0OO0O00O0O0O ,OOOO0000OOOO00OO0 ])#line:221
    for O000O0OO0O00O0O0O in range (len (OO0OOO0OOOO0OOOOO )):#line:222
        OO00O0OO0O0OOO0O0 =threading .Thread (target =ghdy ,args =(OO000O0O00OOOOO00 ,O00O0O00OOOO000O0 ))#line:223
        OO00O0OO0O0OOO0O0 .start ()#line:224
        OO000OO00000OOO0O .append (OO00O0OO0O0OOO0O0 )#line:225
    for O0OOOO00O0OO000OO in OO000OO00000OOO0O :#line:226
        O0OOOO00O0OO000OO .join ()#line:227
    while not O00O0O00OOOO000O0 .empty ():#line:228
        OO0000O00OOOO0OOO .append (O00O0O00OOOO000O0 .get ())#line:229
    OO0O0O0O0O0O00OOO ='\n'.join (OO0000O00OOOO0OOO )+f'\n本通知by：https://github.com/kxs2018/xiaoym\ntg讨论群：https://t.me/xizhiaigroup\n通知时间：{ftime()}'#line:231
    if send :#line:232
        send ('歌画东阳抽红包通知',OO0O0O0O0O0O00OOO )#line:233
if __name__ =='__main__':#line:236
    main ()#line:237
