# -*- coding: utf-8 -*-
# k_trda
# Author: 惜之酱
import datetime #line:5
import time #line:6
import requests #line:7
import os #line:8
from queue import Queue #line:9
import threading #line:10
def ftime ():#line:13
    OOOOO0OOOO000O00O =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:14
    return OOOOO0OOOO000O00O #line:15
class TRDA :#line:18
    def __init__ (O00O0OO0000O00O0O ,O0000OO0O00O00O0O ):#line:19
        O00O0OO0000O00O0O .ck =O0000OO0O00O00O0O .split ('#')[0 ]#line:20
        O00O0OO0000O00O0O .aid =O0000OO0O00O00O0O .split ('#')[1 ]#line:21
        O00O0OO0000O00O0O .s =requests .session ()#line:22
        O00O0OO0000O00O0O .s .headers ={"Authorization":f'Bearer {O00O0OO0000O00O0O.ck}',"User-Agent":"Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36;xsb_ruian;xsb_ruian;2.31.742;native_app",}#line:25
        O00O0OO0000O00O0O .msg =''#line:26
    def user_info (OO000O0O00OOO00O0 ):#line:28
        O00OO0000OO0O0OO0 ='https://crm.rabtv.cn/v2/index/userInfo'#line:29
        OOO0O00OOO000O00O =OO000O0O00OOO00O0 .s .post (O00OO0000OO0O0OO0 ).json ()#line:30
        if OOO0O00OOO000O00O .get ('code')==1 :#line:32
            OO000O0O00OOO00O0 .un =OOO0O00OOO000O00O .get ('data').get ('username')#line:33
            O0O00OO00O00O0O00 =OOO0O00OOO000O00O .get ('data').get ('common_user').get ('money')#line:34
            O0O0OOO0OOOOO00OO =''.join (OOO0O00OOO000O00O .get ('data').get ('continue_sign_num'))#line:35
            while O0O0OOO0OOOOO00OO .startswith ('0')and len (O0O0OOO0OOOOO00OO )>1 :#line:36
                O0O0OOO0OOOOO00OO =O0O0OOO0OOOOO00OO [1 :]#line:37
            OO0OOOO0O0OO000O0 =OOO0O00OOO000O00O .get ('data').get ('total_sign_num')#line:38
            O0OOO0O000O0OOOOO =f'【{OO000O0O00OOO00O0.un}】：当前红包{O0O00OO00O00O0O00}元，已连续签到{O0O0OOO0OOOOO00OO}天，总签到{OO0OOOO0O0OO000O0}天'#line:39
            print (O0OOO0O000O0OOOOO )#line:40
            OO000O0O00OOO00O0 .msg +=f'{O0OOO0O000O0OOOOO}\n '#line:41
            return True #line:42
        else :#line:43
            print (OOO0O00OOO000O00O .get ('msg'))#line:44
            return False #line:45
    @staticmethod #line:47
    def gettype (O0000O0OO000OOOOO ):#line:48
        O000OO00000O000O0 ={'redbag':'红包','score':'积分'}#line:49
        O0OO00000O0OOO000 =O000OO00000O000O0 .get (O0000O0OO000OOOOO )#line:50
        return O0OO00000O0OOO000 if O0OO00000O0OOO000 else O0000O0OO000OOOOO #line:51
    def signin (OOOOO00OOO0OO00OO ):#line:53
        global msg #line:54
        OO0OO00OO00OOOO0O ='https://crm.rabtv.cn/v2/index/signIn'#line:55
        O00OO0OOOOO00OO0O =OOOOO00OOO0OO00OO .s .post (OO0OO00OO00OOOO0O ).json ()#line:56
        if O00OO0OOOOO00OO0O .get ('code')==0 :#line:58
            msg =O00OO0OOOOO00OO0O .get ("msg")#line:59
            if 'plz-check-mobile'in msg :#line:60
                if send :#line:61
                    send (f'{OOOOO00OOO0OO00OO.un} 天瑞地安需验证手机，请登录APP验证手机')#line:62
        elif O00OO0OOOOO00OO0O .get ('code')==1 :#line:63
            OO000O00OOOOO0O0O =O00OO0OOOOO00OO0O .get ('data')['type']#line:64
            O0OO000O00O0OO00O =O00OO0OOOOO00OO0O .get ('data').get (OO000O00OOOOO0O0O )#line:65
            OOOO00OO000O0O0O0 =O00OO0OOOOO00OO0O .get ('data').get ('continue_sign_num')#line:66
            msg =f'签到成功，获得{O0OO000O00O0OO00O}{OOOOO00OOO0OO00OO.gettype(OO000O00OOOOO0O0O)}，连续签到{OOOO00OO000O0O0O0}天'#line:67
        msg =f'【{OOOOO00OOO0OO00OO.un}】：{msg}'#line:68
        print (msg )#line:69
        OOOOO00OOO0OO00OO .msg +=f'{msg}\n '#line:70
    def task_add (O000O000OO0O0O000 ):#line:72
        O00OOOOOOO0O0O0O0 ='https://crm.rabtv.cn/read/task/add'#line:73
        O0O0O00OOOO00O00O =f'account_id={O000O000OO0O0O000.aid}&task_child_id={1}'#line:74
        OOOO0OOO00000OOOO =O000O000OO0O0O000 .s .post (O00OOOOOOO0O0O0O0 ,data =O0O0O00OOOO00O00O ).json ()#line:75
        O0000OO000O0O0O0O =OOOO0OOO00000OOOO .get ('msg')#line:76
        O000O000OO0O0O000 .msg +=f'{O0000OO000O0O0O0O}\n '#line:77
        print (f'【{O000O000OO0O0O000.un}】：task_child_id_1 {O0000OO000O0O0O0O}')#line:78
        for OOOO00000000OO000 in range (6 ,22 ):#line:79
            O0O0O00OOOO00O00O =f'account_id={O000O000OO0O0O000.aid}&task_child_id={OOOO00000000OO000}'#line:80
            OOOO0OOO00000OOOO =O000O000OO0O0O000 .s .post (O00OOOOOOO0O0O0O0 ,data =O0O0O00OOOO00O00O ).json ()#line:81
            # print (OOOO0OOO00000OOOO )#line:82
            O0000OO000O0O0O0O =OOOO0OOO00000OOOO .get ('msg')#line:83
            O000O000OO0O0O000 .msg +=f'{O0000OO000O0O0O0O}\n '#line:84
            print (f'【{O000O000OO0O0O000.un}】：task_child_id_{OOOO00000000OO000} {O0000OO000O0O0O0O}')#line:85
            if OOOO0OOO00000OOOO .get ('code')==1 :#line:86
                if OOOO00000000OO000 in [12 ,16 ,20 ]:#line:87
                    time .sleep (900 )#line:88
                elif OOOO00000000OO000 in [7 ,8 ,9 ]:#line:89
                    time .sleep (25 )#line:90
                else :#line:91
                    time .sleep (300 )#line:92
    def run (OOOOO0O0O00OOOOO0 ):#line:94
        if OOOOO0O0O00OOOOO0 .user_info ():#line:95
            OOOOO0O0O00OOOOO0 .signin ()#line:96
            OOOOO0O0O00OOOOO0 .task_add ()#line:97
        return OOOOO0O0O00OOOOO0 .msg #line:98
def get_msg ():#line:101
    O000O0O000O0O0O00 ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:104
    O0OOOOOOOOOO0O0O0 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O000O0O000O0O0O00 ).json ()#line:105
    return O0OOOOOOOOOO0O0O0 #line:106
def gfsignin (O00O0O0O000OO0OOO ,O0O00OOO00O00OO0O ):#line:109
    while not O00O0O0O000OO0OOO .empty ():#line:110
        OO000O0000OO000OO =O00O0O0O000OO0OOO .get ()#line:111
        O0O0O00O00O000000 =TRDA (OO000O0000OO000OO )#line:112
        O0O00OOO00O00OO0O .put (O0O0O00O00O000000 .run ())#line:113
def load_notify ():#line:116
    global send #line:117
    try :#line:118
        from notify import send #line:119
        print ("加载通知服务成功！")#line:120
        return True #line:121
    except :#line:122
        print ('加载通知服务失败,请复制一份青龙notify.py到同级文件夹')#line:123
        return False #line:124
def main ():#line:127
    print ("="*50 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\ttg群：https://t.me/xiaoymgroup\n'+'-'*50 )#line:129
    _OO00O0O0000OO00O0 =get_msg ()#line:130
    OOO0OO000OO00OOO0 ="V2.0"#line:131
    OOOOO00O00O0OO0OO =_OO00O0O0000OO00O0 .get ('version').get ('天瑞地安')#line:132
    print (f"当前版本 {OOO0OO000OO00OOO0}，仓库版本 {OOOOO00O00O0OO0OO}")#line:133
    print (_OO00O0O0000OO00O0 .get ('update_log')['天瑞地安'])#line:134
    if OOO0OO000OO00OOO0 <OOOOO00O00O0OO0OO :#line:135
        print ('请到仓库下载最新版本k_trda.py')#line:136
    print (_OO00O0O0000OO00O0 .get ('msg')['天瑞地安'])#line:137
    O00O00000OO00OO00 =os .getenv ('trdav2ck')#line:138
    if not O00O00000OO00OO00 :#line:139
        print ('没有获取到ck，程序退出')#line:140
        exit ()#line:141
    load_notify ()#line:142
    O00O00000OO00OO00 =O00O00000OO00OO00 .replace ('&','\n').split ('\n')#line:143
    OOO0OO00OOOOOO00O =['']#line:144
    OOO0OOO00OOO0O000 =Queue ()#line:145
    O00OO0O0OOOOOO0OO =Queue ()#line:146
    OOOO0OOO0000000OO =[]#line:147
    print (f'共获取到{len(O00O00000OO00OO00)}个账号，如不正确，请检查ck填写格式')#line:148
    for OOOO00000O00000O0 ,OO000OO0OOOO0OO00 in enumerate (O00O00000OO00OO00 ,start =1 ):#line:149
        OOO0OOO00OOO0O000 .put (OO000OO0OOOO0OO00 )#line:150
    for OOOO00000O00000O0 in range (5 ):#line:151
        O000000O00O00OO00 =threading .Thread (target =gfsignin ,args =(OOO0OOO00OOO0O000 ,O00OO0O0OOOOOO0OO ))#line:152
        O000000O00O00OO00 .start ()#line:153
        OOOO0OOO0000000OO .append (O000000O00O00OO00 )#line:154
    for OO0O000OOO0OO000O in OOOO0OOO0000000OO :#line:155
        OO0O000OOO0OO000O .join ()#line:156
    while not O00OO0O0OOOOOO0OO .empty ():#line:157
        OOO0OO00OOOOOO00O .append (O00OO0O0OOOOOO0OO .get ())#line:158
    OO0O0OO00000O0O0O ='\n'.join (OOO0OO00OOOOOO00O )+f'\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg讨论群：https://t.me/xiaoymgroup\n通知时间：{ftime()}'#line:160
    if send :#line:161
        send ('天瑞地安共富签通知',OO0O0OO00000O0O0O )#line:162
if __name__ =='__main__':#line:165
    main ()#line:166
