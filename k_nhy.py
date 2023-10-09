# -*- coding: utf-8 -*-
# k_nhy.py
# Author: 惜之酱
"""推送通知开关"""
notify = 0
"""1为开，0为关"""

import os
import requests
from multiprocessing import Pool
import datetime
def get_msg ():#line:15
    O0000OOOOOOO000OO ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:17
    O000O0O0O0O0OO0O0 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O0000OOOOOOO000OO ).json ()#line:18
    return O000O0O0O0O0OO0O0 #line:19
_O0OOOOOOO0O0OO00O =get_msg ()#line:22
try :#line:24
    from bs4 import BeautifulSoup #line:25
except :#line:26
    print (_O0OOOOOOO0O0OO00O .get ('help')['bs4'])#line:27
    exit ()#line:28
def load_notify ():#line:31
    global send #line:32
    try :#line:33
        from notify import send #line:34
        print ("加载通知服务成功！")#line:35
    except :#line:36
        send =False #line:37
        print ('加载通知服务失败')#line:38
def ftime ():#line:41
    OOOO0O000O0O00O00 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:42
    return OOOO0O000O0O00O00 #line:43
class NHY :#line:46
    def __init__ (OOO00OO00O00O00OO ,O0O0O00O000OO00O0 ,O0O00O00O0O00OO0O ):#line:47
        OOO00OO00O00O00OO .index =O0O0O00O000OO00O0 #line:48
        OOO00OO00O00O00OO .phone =O0O00O00O0O00OO0O .split ('#')[0 ]#line:49
        OOO00OO00O00O00OO .psw =O0O00O00O0O00OO0O .split ('#')[1 ]#line:50
        OOO00OO00O00O00OO .s =requests .session ()#line:51
        OOO00OO00O00O00OO .s .headers ={'Accept':'application/json, text/javascript, */*; q=0.01','X-Requested-With':'XMLHttpRequest','User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36  XiaoMi/MiuiBrowser/10.8.1 LT-APP/45/104','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',}#line:56
        OOO00OO00O00O00OO .msg ='='*50 +'\n'#line:57
    def login (O0O0OO0000OOO0O00 ):#line:59
        try :#line:60
            O0O000OO0O0OOO0OO =f"username={O0O0OO0000OOO0O00.phone}&password={O0O0OO0000OOO0O00.psw}&xieyi=on"#line:61
            OO00O00OO00OOOO00 ='http://wap.nonghaoyou.cn/Public/login'#line:62
            O00OO00OOOOOOO00O =O0O0OO0000OOO0O00 .s .post (OO00O00OO00OOOO00 ,data =O0O000OO0O0OOO0OO ).json ()#line:63
            O0O0OO00O00O0OOO0 =f'账号{O0O0OO0000OOO0O00.index}：{O00OO00OOOOOOO00O.get("info")}'#line:64
            print (O0O0OO00O00O0OOO0 )#line:65
            O0O0OO0000OOO0O00 .msg +=O0O0OO00O00O0OOO0 +'\n'#line:66
            return True #line:67
        except :#line:68
            O0O0OO00O00O0OOO0 =f'账号{O0O0OO0000OOO0O00.index}：登录失败，请检查账号密码填写是否正确'#line:69
            print (O0O0OO00O00O0OOO0 )#line:70
            O0O0OO0000OOO0O00 .msg +=O0O0OO00O00O0OOO0 +'\n'#line:71
            return False #line:72
    def get_info (OO00OOOOO0OO00O00 ):#line:74
        O0OO0OOO0OOO00OO0 ='http://wap.nonghaoyou.cn/Member/index'#line:75
        OOO0O00O0O0OO0OOO =OO00OOOOO0OO00O00 .s .get (O0OO0OOO0OOO00OO0 ).text #line:76
        O0O000OOOOO0OO00O =BeautifulSoup (OOO0O00O0O0OO0OOO ,'html.parser')#line:77
        O0O00O000OOO0000O =O0O000OOOOO0OO00O .find ('a',href ="info_edit").text #line:78
        O00OOOOO0O00OO0OO =O0O000OOOOO0OO00O .find_all ('div',class_ ='my-number')#line:79
        OO00O00OO0O00O00O =O00OOOOO0O00OO0OO [0 ].text #line:80
        O00O0OO0OO000O0O0 =O00OOOOO0O00OO0OO [1 ].text #line:81
        OOO00O000O0O000OO =O00OOOOO0O00OO0OO [2 ].text #line:82
        OOOO00000O0O00O0O =f'账号{OO00OOOOO0OO00O00.index}：{O0O00O000OOO0000O},余额{OO00O00OO0O00O00O},积分{O00O0OO0OO000O0O0},预估收益{OOO00O000O0O000OO}'#line:83
        print (OOOO00000O0O00O0O )#line:84
        OO00OOOOO0OO00O00 .msg +=OOOO00000O0O00O0O +'\n'#line:85
    def signin (OOOO0OO0000OOOOOO ):#line:87
        O0OO00O0O0OOO0O0O ={'uid':'11951'}#line:88
        O00O00O0OOOOOOOOO ='http://wap.nonghaoyou.cn/Member/ad_video_api'#line:89
        for OO0O0000000OOOO0O in range (1 ,11 ):#line:90
            OO0O0O0O00O00OOO0 =OOOO0OO0000OOOOOO .s .post (O00O00O0OOOOOOOOO ,data =O0OO00O0O0OOO0O0O ).json ()#line:91
            O00O0O00OOOOO0O0O =f'账号{OOOO0OO0000OOOOOO.index}：第{OO0O0000000OOOO0O}次{OO0O0O0O00O00OOO0.get("info")}'#line:92
            print (O00O0O00OOOOO0O0O )#line:93
            OOOO0OO0000OOOOOO .msg +=O00O0O00OOOOO0O0O +'\n'#line:94
        OOOO0OO0000OOOOOO .msg +=f'账号{OOOO0OO0000OOOOOO.index}：签到完成\n'#line:95
    def run (O000O0000OOO0000O ):#line:97
        if O000O0000OOO0000O .login ():#line:98
            O000O0000OOO0000O .get_info ()#line:99
            O000O0000OOO0000O .signin ()#line:100
            O000O0000OOO0000O .get_info ()#line:101
        return O000O0000OOO0000O .msg #line:102
def nhysignin (OOOOO000OO0O0O0O0 ,O0000OO00OOO000OO ):#line:105
    OOOO000O0OO00OO0O =NHY (OOOOO000OO0O0O0O0 ,O0000OO00OOO000OO )#line:106
    return OOOO000O0OO00OO0O .run ()#line:107
def get_info ():#line:110
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:112
    print ('入口http://wap.nonghaoyou.cn/Public/reg/recom/131242，注册时填写邀请码131242\n需实名认证，谨慎注册 ' '平台商品偏贵，小心被反薅\n脚本只签到，用户自行做任务等造成损失，本人概不负责\n默认不推送通知，如需推送，将脚本开头的notify改为1，复制青龙的notify.py到脚本所在文件夹并设置好相关参数')#line:115
    O0O0000OOO0OOOOO0 ='V1.0'#line:116
    O0O0O0OO000OO0OO0 =_O0OOOOOOO0O0OO00O ['version']['knhy']#line:117
    print (f'当前版本{O0O0000OOO0OOOOO0}，仓库版本{O0O0O0OO000OO0OO0}')#line:118
    if O0O0000OOO0OOOOO0 <O0O0O0OO000OO0OO0 :#line:119
        print ('请到仓库下载最新版本')#line:120
def main ():#line:123
    OOO0OO00OOO0O0O0O =os .getenv ('nhyck')#line:124
    if not OOO0OO00OOO0O0O0O :#line:125
        print (_O0OOOOOOO0O0OO00O ['msg']['农好优'])#line:126
        print ('='*25 )#line:127
        exit ()#line:128
    print ('='*25 )#line:129
    if notify :#line:130
        load_notify ()#line:131
    OOO0OO00OOO0O0O0O =OOO0OO00OOO0O0O0O .split ('&')#line:132
    with Pool ()as O0O0O0OO0O0O0O0OO :#line:133
        O0OOO0O0O0000OO00 =[O000O0OOOOOOOO0O0 for O000O0OOOOOOOO0O0 in O0O0O0OO0O0O0O0OO .starmap (nhysignin ,list (enumerate (OOO0OO00OOO0O0O0O ,start =1 )))]#line:134
    O0OOO0O0O0000OO00 =''.join (O0OOO0O0O0000OO00 )+'\n本通知by：https://github.com/kxs2018/xiaoym\ntg讨论群：https://t.me/xizhiaigroup\n通知时间：{ftime()}'#line:135
    if notify and send :#line:136
        send ('农好优签到信息',O0OOO0O0O0000OO00 )#line:137
if __name__ =='__main__':#line:140
    main ()#line:141
