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
    OO0O00O00OOOO00O0 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:23
    OO0000OO00O00O000 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OO0O00O00OOOO00O0 ).json ()#line:24
    return OO0000OO00O00O000 #line:25
_O00000O000O0OOO00 =get_msg ()#line:28
def ftime ():#line:31
    OOOOO0OO000OO000O =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:32
    return OOOOO0OO000OO000O #line:33
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
def gen_string (O000OOO0O00O0000O ):#line:48
    OOOO000000OOO0OO0 =string .ascii_lowercase +string .digits #line:49
    O0O0O00OO0OO0OO0O =''.join (random .choice (OOOO000000OOO0OO0 )for OO0OOO0O0OO0O000O in range (O000OOO0O00O0000O ))#line:50
    return O0O0O00OO0OO0OO0O #line:51
def gen_requestid ():#line:54
    O0OO00O0O0OOO0O00 =f'{gen_string(8)}-{gen_string(4)}-{gen_string(4)}-{gen_string(4)}-{gen_string(12)}'#line:55
    return O0OO00O0O0OOO0O00 #line:56
def sha_256 (OOOOO00OOO0OOO000 ):#line:59
    O00O0OOO000OOO000 =hashlib .sha256 ()#line:60
    O00O0OOO000OOO000 .update (OOOOO00OOO0OOO000 .encode ('utf-8'))#line:61
    OO0OOO0O00OOOOO00 =O00O0OOO000OOO000 .hexdigest ()#line:62
    return OO0OOO0O00OOOOO00 #line:63
def is_morning ():#line:66
    O000OO0OO00OO0OOO =datetime .datetime .now ().hour #line:67
    return True if O000OO0OO00OO0OOO <12 else False #line:68
class GHDY :#line:71
    def __init__ (O0O0O0O0OO0O0O000 ,OO0OO0O00OOOOO0OO ,O0O0OOO0O0O0OOO0O ):#line:72
        O0O0O0O0OO0O0O000 .index =OO0OO0O00OOOOO0OO #line:73
        O0O0O0O0OO0O0O000 .sessionid =O0O0OOO0O0O0OOO0O .get ('sessionid')#line:74
        O0O0O0O0OO0O0O000 .accountid =O0O0OOO0O0O0OOO0O .get ('accountid')#line:75
        O0O0O0O0OO0O0O000 .id_list =None #line:76
        O0O0O0O0OO0O0O000 .headers ={'X-SESSION-ID':O0O0O0O0OO0O0O000 .sessionid ,'X-TENANT-ID':'49','User-Agent':'5.0.9.0.2;00000000-6634-51c0-0000-00000f8829df;HONOR ANY-AN00;Android;13;Release','X-ACCOUNT-ID':O0O0O0O0OO0O0O000 .accountid ,'Cache-Control':'no-cache','Host':'vapp.tmuyun.com','Connection':'Keep-Alive','Accept-Encoding':'gzip'}#line:80
        O0O0O0O0OO0O0O000 ._headers ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36;xsb_dongyang;xsb_dongyang;5.0.9.0.2;native_app;6.5.0','Host':'fijdzpur.act.tmuact.com','Connection':'keep-alive','Pragma':'no-cache','Cache-Control':'no-cache','Accept':'application/json, text/plain, */*','X-Requested-With':'XMLHttpRequest','Content-Type':'application/x-www-form-urlencoded','Origin':'https://fijdzpur.act.tmuact.com','Sec-Fetch-Site':'same-origin','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://fijdzpur.act.tmuact.com/money/index/index.html','Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'}#line:89
        O0O0O0O0OO0O0O000 .msg =''#line:90
        O0O0O0O0OO0O0O000 .name =''#line:91
    def gen_dict (OOO0OO0O00OO0OO0O ,O00O00O0O0OOOOO0O ):#line:93
        O0OOOOO0OOO00O0O0 =urlparse (O00O00O0O0OOOOO0O ).path #line:94
        OO0OOO000OOOOO0OO =int (time .time ()*1000 )#line:95
        OOO0OOO0O0O000OO0 =gen_requestid ()#line:96
        O0O00OO000O0O0O00 =f'{O0OOOOO0OOO00O0O0}&&{OOO0OO0O00OO0OO0O.sessionid}&&{OOO0OOO0O0O000OO0}&&{OO0OOO000OOOOO0OO}&&FR*r!isE5W&&49'#line:97
        OOO000OOOOOO0O00O ={'X-TIMESTAMP':str (OO0OOO000OOOOO0OO ),'X-REQUEST-ID':OOO0OOO0O0O000OO0 ,'X-SIGNATURE':sha_256 (O0O00OO000O0O0O00 )}#line:98
        return OOO000OOOOOO0O00O #line:99
    def userinfo (OOOOOO0000O00OO0O ):#line:101
        O0000OO00000OO0O0 ="https://vapp.tmuyun.com/api/user_mumber/account_detail"#line:102
        O00OOO0O000OOO00O =OOOOOO0000O00OO0O .gen_dict (O0000OO00000OO0O0 )#line:103
        OOOO00OOOO000O00O ={**OOOOOO0000O00OO0O .headers ,**O00OOO0O000OOO00O }#line:104
        OOO00O00000O0000O =requests .get (O0000OO00000OO0O0 ,headers =OOOO00OOOO000O00O ).json ()#line:105
        if OOO00O00000O0000O .get ('code')==0 :#line:106
            OOOOOO0000O00OO0O .name =OOO00O00000O0000O .get ('data').get ('rst').get ('nick_name')#line:107
            print (f'【{OOOOOO0000O00OO0O.name}】:✅登录成功')#line:108
            OOOOOO0000O00OO0O .msg +=f'【{OOOOOO0000O00OO0O.name}】:✅登录成功\n'#line:109
            return True #line:110
        else :#line:111
            print (f'【账号{OOOOOO0000O00OO0O.index}】:❌登录失败')#line:112
            OOOOOO0000O00OO0O .msg +=f'【账号{OOOOOO0000O00OO0O.index}】:❌登录失败\n'#line:113
            return False #line:114
    def tx (OOO000OO0OO00000O ):#line:116
        O0OO00O00OO0OO0OO ="https://wallet.act.tmuact.com/activity/api.php"#line:117
        OOOO0OOO0OOOOOO0O ={'m':'front','subm':'money_wallet','action':'commonchange','account_id':OOO000OO0OO00000O .accountid ,'session_id':OOO000OO0OO00000O .sessionid ,'app':'XSB_DONGYANG'}#line:119
        OOO00O000O0OO00O0 =requests .post (O0OO00O00OO0OO0OO ,headers =OOO000OO0OO00000O ._headers ,data =OOOO0OOO0OOOOOO0O ).json ()#line:120
        OOO0O00OOO0OO0OO0 =OOO00O000O0OO00O0 ["msg"]#line:121
        if OOO00O000O0OO00O0 .get ('status'):#line:122
            print (f'【{OOO000OO0OO00000O.name}】:✅{OOO00O000O0OO00O0["msg"]}')#line:123
            OOO000OO0OO00000O .msg +=f'【{OOO000OO0OO00000O.name}】:✅{OOO00O000O0OO00O0["msg"]}\n'#line:124
        else :#line:125
            print (f'【{OOO000OO0OO00000O.name}】:❌{OOO0O00OOO0OO0OO0}')#line:126
            OOO000OO0OO00000O .msg +=f'【{OOO000OO0OO00000O.name}】:❌{OOO0O00OOO0OO0OO0}\n'#line:127
    def get_article (OO0OOOOOOOOOO0OOO ):#line:129
        O0OO0000O0O00000O ='https://vapp.tmuyun.com/api/article/channel_list'#line:130
        OOOOOO0OO00OOOOO0 =OO0OOOOOOOOOO0OOO .gen_dict (O0OO0000O0O00000O )#line:131
        OOOOOO000O0OO000O ={**OO0OOOOOOOOOO0OOO .headers ,**OOOOOO0OO00OOOOO0 }#line:132
        O00OOO0O000O0OOO0 ={'channel_id':'6254f12dfe3fc10794f7b25c','isDiFangHao':'false','is_new':'true','list_count':'0','size':'20'}#line:134
        O0O0OO000O0O00O0O =requests .get (O0OO0000O0O00000O ,headers =OOOOOO000O0OO000O ,params =O00OOO0O000O0OOO0 ).json ()#line:135
        if O0O0OO000O0O00O0O .get ('code')==0 :#line:136
            O000OO0000OO0O0O0 =O0O0OO000O0O00O0O .get ('data').get ('article_list')#line:137
            O0O0OO0OOO00OOOOO =[O0OO000OO00OO00OO ['id']for O0OO000OO00OO00OO in O000OO0000OO0O0O0 ]#line:138
            OO0OOOOOOOOOO0OOO .id_list =[random .choice (O0O0OO0OOO00OOOOO )for OO00O0OO00000O000 in range (5 )]#line:139
            if OO0OOOOOOOOOO0OOO .id_list :#line:140
                print (f"✅【{OO0OOOOOOOOOO0OOO.name}】:文章加载成功")#line:141
        elif '不存在'in O0O0OO000O0O00O0O ['message']:#line:142
            OOOO0O0OO0O00000O =f'【{OO0OOOOOOOOOO0OOO.name}】:⛔️文章加载失败 {O0O0OO000O0O00O0O["message"]}'#line:143
            OO0OOOOOOOOOO0OOO .msg +=OOOO0O0OO0O00000O +'\n'#line:144
            print (OOOO0O0OO0O00000O )#line:145
        else :#line:146
            OOOO0O0OO0O00000O =f'【{OO0OOOOOOOOOO0OOO.name}】:❌请求异常 {O0O0OO000O0O00O0O["message"]}'#line:147
            print (OOOO0O0OO0O00000O )#line:148
            OO0OOOOOOOOOO0OOO .msg +=OOOO0O0OO0O00000O +'\n'#line:149
    def read (O00000000OOO0O0O0 ):#line:151
        O0000O0O000O0OO0O ='https://vapp.tmuyun.com/api/article/detail'#line:152
        O0O0O000OO00OO000 =O00000000OOO0O0O0 .gen_dict (O0000O0O000O0OO0O )#line:153
        O0OOOOOO0O00OO00O ={**O00000000OOO0O0O0 .headers ,**O0O0O000OO00OO000 }#line:154
        for O0O00000OOOOOOO0O in O00000000OOO0O0O0 .id_list :#line:155
            OOOO0000OOO0OO0O0 ={'id':O0O00000OOOOOOO0O }#line:156
            O00OO000O0O0O0O0O =requests .get (O0000O0O000O0OO0O ,params =OOOO0000OOO0OO0O0 ,headers =O0OOOOOO0O00OO00O ).json ()#line:157
            if O00OO000O0O0O0O0O ['code']==0 :#line:158
                print (f'【{O00000000OOO0O0O0.name}】:✅浏览《{O00OO000O0O0O0O0O["data"]["article"]["list_title"]}》成功')#line:159
                time .sleep (random .randint (3 ,8 ))#line:160
            elif '不存在'in O00OO000O0O0O0O0O ['message']:#line:161
                print (f'【{O00000000OOO0O0O0.name}】:⛔️浏览失败 {O00OO000O0O0O0O0O["message"]}')#line:162
                O00000000OOO0O0O0 .msg +=f'【{O00000000OOO0O0O0.name}】:⛔️浏览失败 {O00OO000O0O0O0O0O["message"]}\n'#line:163
            else :#line:164
                print (f'【{O00000000OOO0O0O0.name}】:❌浏览异常 {O00OO000O0O0O0O0O["message"]}')#line:165
                O00000000OOO0O0O0 .msg +=f'【{O00000000OOO0O0O0.name}】:❌浏览异常 {O00OO000O0O0O0O0O["message"]}\n'#line:166
        O00O00O0O0O000OO0 =f'【{O00000000OOO0O0O0.name}】:✅浏览完成，登录APP抽红包吧！'#line:167
        print (O00O00O0O0O000OO0 )#line:168
        O00000000OOO0O0O0 .msg +=O00O00O0O0O000OO0 +'\n'#line:169
    def run (O000O0OO0OO00O000 ):#line:171
        if O000O0OO0OO00O000 .userinfo ():#line:172
            O000O0OO0OO00O000 .tx ()#line:173
            if is_morning ():#line:174
                O000O0OO0OO00O000 .get_article ()#line:175
                O000O0OO0OO00O000 .read ()#line:176
        return O000O0OO0OO00O000 .msg #line:177
def ghdy (OOOO00O00OO0O0OOO ,OOOO0O0O0OO0OOOOO ):#line:180
    while not OOOO00O00OO0O0OOO .empty ():#line:181
        OOO000O000O00OOOO ,OO0OO00OO0O000O0O =OOOO00O00OO0O0OOO .get ()#line:182
        OOO00OO0O0OOO00OO =GHDY (OOO000O000O00OOOO ,OO0OO00OO0O000O0O )#line:183
        OOOO0O0O0OO0OOOOO .put (OOO00OO0O0OOO00OO .run ())#line:184
def get_info ():#line:187
    print ("="*50 +f'\n✅github仓库：https://github.com/kxs2018/xiaoym\n极狐仓库:https://jihulab.com/xizhiai/xiaoym\n✅By:惜之酱\t\thttp://t.me/xiaoymgroup\n'+'-'*50 )#line:189
    print (f"✅{_O00000O000O0OOO00.get('msg')['歌画东阳']}")#line:190
    OO00OO0OOOO00O000 ='v1.0'#line:191
    OOOOO00O00O000OOO =_O00000O000O0OOO00 ['version']['歌画东阳']#line:192
    print ('-'*50 +f'\n当前版本{OO00OO0OOOO00O000}，仓库版本{OOOOO00O00O000OOO}\n✅{_O00000O000O0OOO00["update_log"]["歌画东阳"]}')#line:193
    if OO00OO0OOOO00O000 <OOOOO00O00O000OOO :#line:194
        print ('⛔️请到仓库下载最新版本k_xyy.py')#line:195
    print ("="*50 )#line:196
    return True #line:197
def main ():#line:200
    OO0000000OOO000OO =get_info ()#line:201
    O00O0000OOO00000O =os .getenv ('ghdyck')#line:202
    try :#line:203
        O00O0000OOO00000O =ast .literal_eval (O00O0000OOO00000O )#line:204
    except :#line:205
        pass #line:206
    if not O00O0000OOO00000O :#line:207
        print ('❌没有获取到ck，程序退出')#line:208
        exit ()#line:209
    if not load_notify ():#line:210
        print ('❌加载通知模块失败，请复制青龙的notify.py到同级文件夹，并做好相关参数设置')#line:211
    print (f'✅共获取到{len(O00O0000OOO00000O)}个账号，如与实际不符，请检查ck填写格式')#line:212
    if not OO0000000OOO000OO :#line:213
        exit ()#line:214
    OO0OOOO000OO00O0O =Queue ()#line:215
    OO000OOO00000000O =Queue ()#line:216
    O0O000OO0O000O0O0 =[]#line:217
    O0000O00000OO0000 =[]#line:218
    for OOOO000O0OO000OO0 ,O0OOOO00OO000O0OO in enumerate (O00O0000OOO00000O ,start =1 ):#line:219
        OO0OOOO000OO00O0O .put ([OOOO000O0OO000OO0 ,O0OOOO00OO000O0OO ])#line:220
    for OOOO000O0OO000OO0 in range (len (O00O0000OOO00000O )):#line:221
        OOOO0OO000O0OOOOO =threading .Thread (target =ghdy ,args =(OO0OOOO000OO00O0O ,OO000OOO00000000O ))#line:222
        OOOO0OO000O0OOOOO .start ()#line:223
        O0O000OO0O000O0O0 .append (OOOO0OO000O0OOOOO )#line:224
    for OO0OOOO0000O00OO0 in O0O000OO0O000O0O0 :#line:225
        OO0OOOO0000O00OO0 .join ()#line:226
    while not OO000OOO00000000O .empty ():#line:227
        O0000O00000OO0000 .append (OO000OOO00000000O .get ())#line:228
    O00O0O0O0OOO0O00O ='\n'.join (O0000O00000OO0000 )+f'\n本通知by：https://github.com/kxs2018/xiaoym\ntg讨论群：https://t.me/xiaoymgroup\n通知时间：{ftime()}'#line:230
    if send :#line:231
        send ('歌画东阳抽红包通知',O00O0O0O0OOO0O00O )#line:232
    else:
        print (O00O0O0O0OOO0O00O )
if __name__ =='__main__':#line:235
    main ()#line:236
