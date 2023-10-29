# -*- coding: utf-8 -*-
# k_ghdy
# Author: 惜之酱
"""
先运行脚本，三次之后再有问题到群里问
new Env('歌画东阳');
"""
import ast #line:8
import hashlib #line:9
import random #line:10
import string #line:11
from queue import Queue #line:12
from urllib .parse import urlparse #line:13
import threading #line:14
import time #line:15
import requests #line:16
import os #line:17
import datetime #line:18
def get_msg ():#line:21
    OOO0O0OO0O000O000 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:23
    OO0O0OO0O00OOO0O0 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OOO0O0OO0O000O000 ).json ()#line:24
    return OO0O0OO0O00OOO0O0 #line:25
_O00OOOOOO00O0O0OO =get_msg ()#line:28
def ftime ():#line:31
    O0O0O0O000000O0O0 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:32
    return O0O0O0O000000O0O0 #line:33
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
def gen_string (OO00OOO0000O0O0O0 ):#line:48
    OO00OOOOOO0O00OOO =string .ascii_lowercase +string .digits #line:49
    OO00O0OOO0000OOOO =''.join (random .choice (OO00OOOOOO0O00OOO )for O00OO0O0OO0000000 in range (OO00OOO0000O0O0O0 ))#line:50
    return OO00O0OOO0000OOOO #line:51
def gen_requestid ():#line:54
    O0000OO0O0O0OO000 =f'{gen_string(8)}-{gen_string(4)}-{gen_string(4)}-{gen_string(4)}-{gen_string(12)}'#line:55
    return O0000OO0O0O0OO000 #line:56
def sha_256 (OOOO0O00O0O0O0O0O ):#line:59
    OOO0O0O000O0O00O0 =hashlib .sha256 ()#line:60
    OOO0O0O000O0O00O0 .update (OOOO0O00O0O0O0O0O .encode ('utf-8'))#line:61
    OOO0OOO00OOOOO0OO =OOO0O0O000O0O00O0 .hexdigest ()#line:62
    return OOO0OOO00OOOOO0OO #line:63
def is_morning ():#line:66
    O00O0000O00O0O0OO =datetime .datetime .now ().hour #line:67
    return True if O00O0000O00O0O0OO <12 else False #line:68
class GHDY :#line:71
    def __init__ (OO0OO0O0OOOO0000O ,OOO0O0OO0OOO00O00 ,OO00O0OOO00OOOOO0 ):#line:72
        OO0OO0O0OOOO0000O .index =OOO0O0OO0OOO00O00 #line:73
        OO0OO0O0OOOO0000O .sessionid =OO00O0OOO00OOOOO0 .get ('sessionid')#line:74
        OO0OO0O0OOOO0000O .accountid =OO00O0OOO00OOOOO0 .get ('accountid')#line:75
        OO0OO0O0OOOO0000O .id_list =[]#line:76
        OO0OO0O0OOOO0000O .headers ={'X-SESSION-ID':OO0OO0O0OOOO0000O .sessionid ,'X-TENANT-ID':'49','User-Agent':'5.0.9.0.2;00000000-6634-51c0-0000-00000f8829df;HONOR ANY-AN00;Android;13;Release','X-ACCOUNT-ID':OO0OO0O0OOOO0000O .accountid ,'Cache-Control':'no-cache','Host':'vapp.tmuyun.com','Connection':'Keep-Alive','Accept-Encoding':'gzip'}#line:80
        OO0OO0O0OOOO0000O ._headers ={'user-agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36;xsb_dongyang;xsb_dongyang;5.0.9.0.2;native_app;6.5.0','Host':'fijdzpur.act.tmuact.com','Connection':'keep-alive','Pragma':'no-cache','Cache-Control':'no-cache','Accept':'application/json, text/plain, */*','X-Requested-With':'XMLHttpRequest','Content-Type':'application/x-www-form-urlencoded','Origin':'https://fijdzpur.act.tmuact.com','Sec-Fetch-Site':'same-origin','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://fijdzpur.act.tmuact.com/money/index/index.html','Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'}#line:89
        OO0OO0O0OOOO0000O .msg =''#line:90
        OO0OO0O0OOOO0000O .name =''#line:91
    def gen_dict (OO0OO0OO0OO00OO0O ,OOO00O0OO0000O0O0 ):#line:93
        O00O0O000O0OOOOO0 =urlparse (OOO00O0OO0000O0O0 ).path #line:94
        O00O00000O000000O =int (time .time ()*1000 )#line:95
        O0OOOO000OO0OO000 =gen_requestid ()#line:96
        OO0O0O00O0000O0OO =f'{O00O0O000O0OOOOO0}&&{OO0OO0OO0OO00OO0O.sessionid}&&{O0OOOO000OO0OO000}&&{O00O00000O000000O}&&FR*r!isE5W&&49'#line:97
        OOO000O00O0O0OOOO ={'X-TIMESTAMP':str (O00O00000O000000O ),'X-REQUEST-ID':O0OOOO000OO0OO000 ,'X-SIGNATURE':sha_256 (OO0O0O00O0000O0OO )}#line:98
        return OOO000O00O0O0OOOO #line:99
    def userinfo (OO0OOO0O0000000OO ):#line:101
        O0OO0O00O0OO00OO0 ="https://vapp.tmuyun.com/api/user_mumber/account_detail"#line:102
        OO00OO0OO000O0OOO =OO0OOO0O0000000OO .gen_dict (O0OO0O00O0OO00OO0 )#line:103
        OOO00OO000O0O0O00 ={**OO0OOO0O0000000OO .headers ,**OO00OO0OO000O0OOO }#line:104
        OOO00000OOO00OOOO =requests .get (O0OO0O00O0OO00OO0 ,headers =OOO00OO000O0O0O00 ).json ()#line:105
        if OOO00000OOO00OOOO .get ('code')==0 :#line:106
            OO0OOO0O0000000OO .name =OOO00000OOO00OOOO .get ('data').get ('rst').get ('nick_name')#line:107
            print (f'【{OO0OOO0O0000000OO.name}】:✅登录成功')#line:108
            OO0OOO0O0000000OO .msg +=f'【{OO0OOO0O0000000OO.name}】:✅登录成功\n'#line:109
            return True #line:110
        else :#line:111
            print (f'【账号{OO0OOO0O0000000OO.index}】:❌登录失败')#line:112
            OO0OOO0O0000000OO .msg +=f'【账号{OO0OOO0O0000000OO.index}】:❌登录失败\n'#line:113
            return False #line:114
    def tx (O0O0000O00OO0OOOO ):#line:116
        O000O00OO0OO0OO00 ="https://wallet.act.tmuact.com/activity/api.php"#line:117
        OO0O0000O000OOO00 ={'m':'front','subm':'money_wallet','action':'commonchange','account_id':O0O0000O00OO0OOOO .accountid ,'session_id':O0O0000O00OO0OOOO .sessionid ,'app':'XSB_DONGYANG'}#line:119
        OOO000OO00O0O000O =requests .post (O000O00OO0OO0OO00 ,headers =O0O0000O00OO0OOOO ._headers ,data =OO0O0000O000OOO00 ).json ()#line:120
        O00OO0OO0O0OO0O0O =OOO000OO00O0O000O ["msg"]#line:121
        if OOO000OO00O0O000O .get ('status'):#line:122
            print (f'【{O0O0000O00OO0OOOO.name}】:✅{OOO000OO00O0O000O["msg"]}')#line:123
            O0O0000O00OO0OOOO .msg +=f'【{O0O0000O00OO0OOOO.name}】:✅{OOO000OO00O0O000O["msg"]}\n'#line:124
        else :#line:125
            print (f'【{O0O0000O00OO0OOOO.name}】:❌{O00OO0OO0O0OO0O0O}')#line:126
            O0O0000O00OO0OOOO .msg +=f'【{O0O0000O00OO0OOOO.name}】:❌{O00OO0OO0O0OO0O0O}\n'#line:127
    def get_article (O00O0O0OO00OOO0O0 ):#line:129
        OOOOO00OOO00O000O ='https://vapp.tmuyun.com/api/article/channel_list'#line:130
        OO0O00OO00O0O0O00 =O00O0O0OO00OOO0O0 .gen_dict (OOOOO00OOO00O000O )#line:131
        O00OO000OOOOO0OO0 ={**O00O0O0OO00OOO0O0 .headers ,**OO0O00OO00O0O0O00 }#line:132
        O00000OOO00OOO000 ={'channel_id':'6254f12dfe3fc10794f7b25c','isDiFangHao':'false','is_new':'true','list_count':'0','size':'20'}#line:134
        O00O0OOOO0000O0O0 =requests .get (OOOOO00OOO00O000O ,headers =O00OO000OOOOO0OO0 ,params =O00000OOO00OOO000 ).json ()#line:135
        if O00O0OOOO0000O0O0 .get ('code')==0 :#line:136
            OOO00O0000OO0000O =O00O0OOOO0000O0O0 .get ('data').get ('article_list')#line:137
            OOOOOOO00OOO000OO =[OOO0O0O00OO00OOOO ['id']for OOO0O0O00OO00OOOO in OOO00O0000OO0000O ]#line:138
            while len (O00O0O0OO00OOO0O0 .id_list )<8 :#line:139
                O0OOO0OOOOO000000 =random .choice (OOOOOOO00OOO000OO )#line:140
                O00O0O0OO00OOO0O0 .id_list .append (O0OOO0OOOOO000000 )#line:141
                OOOOOOO00OOO000OO .remove (O0OOO0OOOOO000000 )#line:142
        elif '不存在'in O00O0OOOO0000O0O0 ['message']:#line:143
            O000OO00OOO0O00OO =f'【{O00O0O0OO00OOO0O0.name}】:⛔️文章加载失败 {O00O0OOOO0000O0O0["message"]}'#line:144
            O00O0O0OO00OOO0O0 .msg +=O000OO00OOO0O00OO +'\n'#line:145
            print (O000OO00OOO0O00OO )#line:146
        else :#line:147
            O000OO00OOO0O00OO =f'【{O00O0O0OO00OOO0O0.name}】:❌请求异常 {O00O0OOOO0000O0O0["message"]}'#line:148
            print (O000OO00OOO0O00OO )#line:149
            O00O0O0OO00OOO0O0 .msg +=O000OO00OOO0O00OO +'\n'#line:150
    def read (O000OOOOOO0O0000O ):#line:152
        OO0O00O0OOO0000O0 ='https://vapp.tmuyun.com/api/article/detail'#line:153
        O0OOOOOO000OO0000 =O000OOOOOO0O0000O .gen_dict (OO0O00O0OOO0000O0 )#line:154
        O0000000O0000O0O0 ={**O000OOOOOO0O0000O .headers ,**O0OOOOOO000OO0000 }#line:155
        for OO0OO0O000O0OOOO0 in O000OOOOOO0O0000O .id_list :#line:156
            OO00OO0OO0O000O0O ={'id':OO0OO0O000O0OOOO0 }#line:157
            OO0OOO0O0000OOO0O =requests .get (OO0O00O0OOO0000O0 ,params =OO00OO0OO0O000O0O ,headers =O0000000O0000O0O0 ).json ()#line:158
            if OO0OOO0O0000OOO0O ['code']==0 :#line:159
                print (f'【{O000OOOOOO0O0000O.name}】:✅浏览《{OO0OOO0O0000OOO0O["data"]["article"]["list_title"]}》成功')#line:160
                time .sleep (random .randint (3 ,8 ))#line:161
            elif '不存在'in OO0OOO0O0000OOO0O ['message']:#line:162
                print (f'【{O000OOOOOO0O0000O.name}】:⛔️浏览失败 {OO0OOO0O0000OOO0O["message"]}')#line:163
                O000OOOOOO0O0000O .msg +=f'【{O000OOOOOO0O0000O.name}】:⛔️浏览失败 {OO0OOO0O0000OOO0O["message"]}\n'#line:164
            else :#line:165
                print (f'【{O000OOOOOO0O0000O.name}】:❌浏览异常 {OO0OOO0O0000OOO0O["message"]}')#line:166
                O000OOOOOO0O0000O .msg +=f'【{O000OOOOOO0O0000O.name}】:❌浏览异常 {OO0OOO0O0000OOO0O["message"]}\n'#line:167
        OOOOO0O0O00OO0O00 =f'【{O000OOOOOO0O0000O.name}】:✅浏览完成，登录APP抽红包吧！'#line:168
        print (OOOOO0O0O00OO0O00 )#line:169
        O000OOOOOO0O0000O .msg +=OOOOO0O0O00OO0O00 +'\n'#line:170
    def run (O0OOOO0O0OO000O00 ):#line:172
        if O0OOOO0O0OO000O00 .userinfo ():#line:173
            O0OOOO0O0OO000O00 .tx ()#line:174
            # if is_morning ():#line:175
            O0OOOO0O0OO000O00 .get_article ()#line:176
            O0OOOO0O0OO000O00 .read ()#line:177
        return O0OOOO0O0OO000O00 .msg #line:178
def ghdy (O000OOO0000OOO0OO ,OO00OO0O00O000000 ):#line:181
    while not O000OOO0000OOO0OO .empty ():#line:182
        O00O00OOO0OOOOOO0 ,OOOOOO0O0OOOO0OOO =O000OOO0000OOO0OO .get ()#line:183
        OO00O000OOO00O00O =GHDY (O00O00OOO0OOOOOO0 ,OOOOOO0O0OOOO0OOO )#line:184
        OO00OO0O00O000000 .put (OO00O000OOO00O00O .run ())#line:185
def get_info ():#line:188
    print ("="*50 +f'\n✅github仓库：https://github.com/kxs2018/xiaoym\n✅极狐仓库:https://jihulab.com/xizhiai/xiaoym\n✅By:惜之酱\t\thttp://t.me/xiaoymgroup\n'+'-'*50 )#line:190
    print (f"✅{_O00OOOOOO00O0O0OO.get('msg')['歌画东阳']}")#line:191
    O0OOOOO0O00O00OOO ='v1.3'#line:192
    O0000OOOO00O000O0 =_O00OOOOOO00O0O0OO ['version']['歌画东阳']#line:193
    print ('-'*50 +f'\n当前版本{O0OOOOO0O00O00OOO}，仓库版本{O0000OOOO00O000O0}\n✅{_O00OOOOOO00O0O0OO["update_log"]["歌画东阳"]}')#line:194
    if O0OOOOO0O00O00OOO <O0000OOOO00O000O0 :#line:195
        print ('⛔️请到仓库下载最新版本k_ghdy.py')#line:196
    print ("="*50 )#line:197
    return True #line:198
def main ():#line:201
    O00OOO0OOOOO0OO00 =get_info ()#line:202
    OOO00OOO0O0OOO0O0 =os .getenv ('ghdyck')#line:203
    try :#line:204
        OOO00OOO0O0OOO0O0 =ast .literal_eval (OOO00OOO0O0OOO0O0 )#line:205
    except :#line:206
        pass #line:207
    if not OOO00OOO0O0OOO0O0 :#line:208
        print ('❌没有获取到ck，程序退出')#line:209
        exit ()#line:210
    if not load_notify ():#line:211
        print ('❌加载通知模块失败，请复制青龙的notify.py到同级文件夹，并做好相关参数设置')#line:212
    print (f'✅共获取到{len(OOO00OOO0O0OOO0O0)}个账号，如与实际不符，请检查ck填写格式')#line:213
    if not O00OOO0OOOOO0OO00 :#line:214
        exit ()#line:215
    O0OO000OOOOO000O0 =Queue ()#line:216
    O00O00OOOO0OO00O0 =Queue ()#line:217
    OOOOOO0OOOOO0OO0O =[]#line:218
    O0OO00OO0OO0OO00O =[]#line:219
    for OOOO0O000OO000OO0 ,OOO0000O0OO00OOOO in enumerate (OOO00OOO0O0OOO0O0 ,start =1 ):#line:220
        O0OO000OOOOO000O0 .put ([OOOO0O000OO000OO0 ,OOO0000O0OO00OOOO ])#line:221
    for OOOO0O000OO000OO0 in range (len (OOO00OOO0O0OOO0O0 )):#line:222
        O0OO00OOO0OO0000O =threading .Thread (target =ghdy ,args =(O0OO000OOOOO000O0 ,O00O00OOOO0OO00O0 ))#line:223
        O0OO00OOO0OO0000O .start ()#line:224
        OOOOOO0OOOOO0OO0O .append (O0OO00OOO0OO0000O )#line:225
    for OOOO00O00O00O0OOO in OOOOOO0OOOOO0OO0O :#line:226
        OOOO00O00O00O0OOO .join ()#line:227
    while not O00O00OOOO0OO00O0 .empty ():#line:228
        O0OO00OO0OO0OO00O .append (O00O00OOOO0OO00O0 .get ())#line:229
    OOO0OO0OO000O0000 ='\n'.join (O0OO00OO0OO0OO00O )+f'\n本通知by：https://github.com/kxs2018/xiaoym\ntg讨论群：https://t.me/xiaoymgroup\n通知时间：{ftime()}'#line:231
    if send :#line:232
        send ('歌画东阳抽红包通知',OOO0OO0OO000O0000 )#line:233
if __name__ =='__main__':#line:236
    main ()#line:237
