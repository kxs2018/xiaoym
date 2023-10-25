# -*- coding: utf-8 -*-
# k_trda
# Author: 惜之酱
import datetime #line:5
import random #line:6
import time #line:8
import requests #line:9
import os #line:10
from queue import Queue #line:11
import threading #line:12
def ftime ():#line:15
    O00O0OOOOO0OOO0OO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:16
    return O00O0OOOOO0OOO0OO #line:17
class TRDA :#line:20
    def __init__ (OOO0OOOO00OOO0OO0 ,O0O0OO0O0OO000O00 ):#line:21
        OOO0OOOO00OOO0OO0 .ck =O0O0OO0O0OO000O00 .split ('#')[0 ]#line:22
        OOO0OOOO00OOO0OO0 .aid =O0O0OO0O0OO000O00 .split ('#')[1 ]#line:23
        OOO0OOOO00OOO0OO0 .s =requests .session ()#line:24
        OOO0OOOO00OOO0OO0 .s .headers ={"Authorization":f'Bearer {OOO0OOOO00OOO0OO0.ck}',"User-Agent":"Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36;xsb_ruian;xsb_ruian;2.31.742;native_app",}#line:27
        OOO0OOOO00OOO0OO0 .msg =''#line:28
    def user_info (O0O0O00O00OOOOO0O ):#line:30
        O0OOOO0OO00OOO0OO ='https://crm.rabtv.cn/v2/index/userInfo'#line:31
        OO0OO0OOOO0OO00O0 =O0O0O00O00OOOOO0O .s .post (O0OOOO0OO00OOO0OO ).json ()#line:32
        if OO0OO0OOOO0OO00O0 .get ('code')==1 :#line:34
            O0O0O00O00OOOOO0O .un =OO0OO0OOOO0OO00O0 .get ('data').get ('username')#line:35
            OOO00O0O000OOO00O =OO0OO0OOOO0OO00O0 .get ('data').get ('common_user').get ('money')#line:36
            OO0O0OOOO0OOOOOO0 =''.join (OO0OO0OOOO0OO00O0 .get ('data').get ('continue_sign_num'))#line:37
            while OO0O0OOOO0OOOOOO0 .startswith ('0')and len (OO0O0OOOO0OOOOOO0 )>1 :#line:38
                OO0O0OOOO0OOOOOO0 =OO0O0OOOO0OOOOOO0 [1 :]#line:39
            O0OO00OO0O0O000OO =OO0OO0OOOO0OO00O0 .get ('data').get ('total_sign_num')#line:40
            OO0O00O00OOO00OOO =f'[{ftime()[-8:]}]【{O0O0O00O00OOOOO0O.un}】：当前红包{OOO00O0O000OOO00O}元，已连续签到{OO0O0OOOO0OOOOOO0}天，总签到{O0OO00OO0O0O000OO}天'#line:41
            print (OO0O00O00OOO00OOO )#line:42
            O0O0O00O00OOOOO0O .msg +=f'{OO0O00O00OOO00OOO}\n'#line:43
            return True #line:44
        else :#line:45
            print (OO0OO0OOOO0OO00O0 .get ('msg'))#line:46
            return False #line:47
    @staticmethod #line:49
    def gettype (O0O000OO0O0000O0O ):#line:50
        OOO00OO00O0O00000 ={'redbag':'红包','score':'积分'}#line:51
        O0O000O0O0000OOOO =OOO00OO00O0O00000 .get (O0O000OO0O0000O0O )#line:52
        return O0O000O0O0000OOOO if O0O000O0O0000OOOO else O0O000OO0O0000O0O #line:53
    def signin (OOOO0O0O0O0OO0OO0 ):#line:55
        global msg #line:56
        OOOOOOO0OOOOO0O0O ='https://crm.rabtv.cn/v2/index/signIn'#line:57
        O00000O0OO0OOOO0O =OOOO0O0O0O0OO0OO0 .s .post (OOOOOOO0OOOOO0O0O ).json ()#line:58
        if O00000O0OO0OOOO0O .get ('code')==0 :#line:60
            msg =O00000O0OO0OOOO0O .get ("msg")#line:61
            if 'plz-check-mobile'in msg :#line:62
                if send :#line:63
                    send (f'{OOOO0O0O0O0OO0OO0.un} 天瑞地安需验证手机，请登录APP验证手机')#line:64
        elif O00000O0OO0OOOO0O .get ('code')==1 :#line:65
            OO00OO00OO00OO00O =O00000O0OO0OOOO0O .get ('data')['type']#line:66
            O0OOOO000O0OOOO00 =O00000O0OO0OOOO0O .get ('data').get (OO00OO00OO00OO00O )#line:67
            O000O000OOOO00O0O =O00000O0OO0OOOO0O .get ('data').get ('continue_sign_num')#line:68
            msg =f'签到成功，获得{O0OOOO000O0OOOO00}{OOOO0O0O0O0OO0OO0.gettype(OO00OO00OO00OO00O)}，连续签到{O000O000OOOO00O0O}天'#line:69
        msg =f'[{ftime()[-8:]}]【{OOOO0O0O0O0OO0OO0.un}】：{msg}'#line:70
        print (msg )#line:71
        OOOO0O0O0O0OO0OO0 .msg +=f'{msg}\n'#line:72
    def task_add (OO0O000OOO00OOO00 ):#line:74
        O000O00O0OO0O00O0 ='https://crm.rabtv.cn/read/task/add'#line:75
        O00O0OO00OOOOO0O0 =f'account_id={OO0O000OOO00OOO00.aid}&task_child_id={1}'#line:76
        OOOOOO00OO0OO0OO0 =OO0O000OOO00OOO00 .s .post (O000O00O0OO0O00O0 ,data =O00O0OO00OOOOO0O0 ).json ()#line:77
        OOO00O0O000OO000O =OOOOOO00OO0OO0OO0 .get ('msg')#line:78
        print (f'[{ftime()[-8:]}]【{OO0O000OOO00OOO00.un}】：task_1 {OOO00O0O000OO000O}')#line:79
        for O0O0OO0O0OOO0OOOO in range (2 ,22 ):#line:80
            O00O0OO00OOOOO0O0 =f'account_id={OO0O000OOO00OOO00.aid}&task_child_id={O0O0OO0O0OOO0OOOO}'#line:81
            OOOOOO00OO0OO0OO0 =OO0O000OOO00OOO00 .s .post (O000O00O0OO0O00O0 ,data =O00O0OO00OOOOO0O0 ).json ()#line:82
            OOO00O0O000OO000O =OOOOOO00OO0OO0OO0 .get ('msg')#line:83
            print (f'[{ftime()[-8:]}]【{OO0O000OOO00OOO00.un}】：task_id_{O0O0OO0O0OOO0OOOO} {OOO00O0O000OO000O}')#line:84
            if OOOOOO00OO0OO0OO0 .get ('code')==1 :#line:85
                if O0O0OO0O0OOO0OOOO in [3 ,4 ,5 ,6 ]:#line:86
                    time .sleep (12 )#line:87
                elif O0O0OO0O0OOO0OOOO in [7 ,8 ,9 ]:#line:88
                    time .sleep (25 )#line:89
                elif O0O0OO0O0OOO0OOOO in [12 ,16 ,20 ]:#line:90
                    time .sleep (900 )#line:91
                else :#line:92
                    time .sleep (300 )#line:93
        OO0O000OOO00OOO00 .msg +=f'【{OO0O000OOO00OOO00.un}】：阅读值任务已完成'#line:94
    def run (OOO00O000OOO00OO0 ):#line:96
        if OOO00O000OOO00OO0 .user_info ():#line:97
            OOO00O000OOO00OO0 .signin ()#line:98
            OOO00O000OOO00OO0 .task_add ()#line:99
        return OOO00O000OOO00OO0 .msg #line:100
def get_msg ():#line:103
    O00O00O000O0OOOO0 ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:106
    OOO0OO0OOOOO00O0O =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O00O00O000O0OOOO0 ).json ()#line:107
    return OOO0OO0OOOOO00O0O #line:108
def gfsignin (OO0O0O0O0OO0O0O00 ,O00OO0O00OO00O0OO ):#line:111
    while not OO0O0O0O0OO0O0O00 .empty ():#line:112
        O0O0OO000000OOOO0 =OO0O0O0O0OO0O0O00 .get ()#line:113
        OOOOO000OOOO00O0O =TRDA (O0O0OO000000OOOO0 )#line:114
        O00OO0O00OO00O0OO .put (OOOOO000OOOO00O0O .run ())#line:115
def load_notify ():#line:118
    global send #line:119
    try :#line:120
        from notify import send #line:121
        print ("加载通知服务成功！")#line:122
        return True #line:123
    except :#line:124
        print ('加载通知服务失败,请复制一份青龙notify.py到同级文件夹')#line:125
        return False #line:126
def main ():#line:129
    print ("="*50 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\ttg群：https://t.me/xiaoymgroup\n'+'-'*50 )#line:131
    _O000O0O0000OOO0OO =get_msg ()#line:132
    OOO0O0000O0000OOO ="V2.0"#line:133
    O0OOO0000O0OOOOOO =_O000O0O0000OOO0OO .get ('version').get ('天瑞地安')#line:134
    print (f"当前版本 {OOO0O0000O0000OOO}，仓库版本 {O0OOO0000O0OOOOOO}")#line:135
    print (_O000O0O0000OOO0OO .get ('update_log')['天瑞地安'])#line:136
    if OOO0O0000O0000OOO <O0OOO0000O0OOOOOO :#line:137
        print ('请到仓库下载最新版本k_trda.py')#line:138
    print (_O000O0O0000OOO0OO .get ('msg')['天瑞地安'])#line:139
    OO00OO00O0O0OO00O =os .getenv ('trdav2ck')#line:140
    if not OO00OO00O0O0OO00O :#line:141
        print ('没有获取到ck，程序退出')#line:142
        exit ()#line:143
    load_notify ()#line:144
    OO00OO00O0O0OO00O =OO00OO00O0O0OO00O .replace ('&','\n').split ('\n')#line:145
    OO00OOOO0O0000O0O =[]#line:146
    OOOOOO0000O0OOO0O =Queue ()#line:147
    O0OOOO00O0O000OO0 =Queue ()#line:148
    OOOOO0OOOO0O0O000 =[]#line:149
    print (f'共获取到{len(OO00OO00O0O0OO00O)}个账号，如不正确，请检查ck填写格式')#line:150
    for OOOO0OO000O000OO0 ,O0OOOOO0O00000000 in enumerate (OO00OO00O0O0OO00O ,start =1 ):#line:151
        OOOOOO0000O0OOO0O .put (O0OOOOO0O00000000 )#line:152
    for OOOO0OO000O000OO0 in range (5 ):#line:153
        O0O0O0OO0OOOO0000 =threading .Thread (target =gfsignin ,args =(OOOOOO0000O0OOO0O ,O0OOOO00O0O000OO0 ))#line:154
        O0O0O0OO0OOOO0000 .start ()#line:155
        OOOOO0OOOO0O0O000 .append (O0O0O0OO0OOOO0000 )#line:156
        O0O0O0OOO00O00OOO =random .randint (10 ,300 )#line:157
        time .sleep (O0O0O0OOO00O00OOO )#line:158
        print (f'下一个账号在{O0O0O0OOO00O00OOO}秒后开始任务')#line:159
    for O00O00OOO0O00OO0O in OOOOO0OOOO0O0O000 :#line:160
        O00O00OOO0O00OO0O .join ()#line:161
    while not O0OOOO00O0O000OO0 .empty ():#line:162
        OO00OOOO0O0000O0O .append (O0OOOO00O0O000OO0 .get ())#line:163
    OOO000O000OOOOO00 =('\n'+'='*20 +'\n').join (OO00OOOO0O0000O0O )+f'\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg讨论群：https://t.me/xiaoymgroup\n通知时间：{ftime()}'#line:165
    if send :#line:166
        send ('天瑞地安共富签通知',OOO000O000OOOOO00 )#line:167
if __name__ =='__main__':#line:170
    main ()#line:171
