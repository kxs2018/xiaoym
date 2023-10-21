# -*- coding: utf-8 -*-
# k_nhy.py
# Author: 惜之酱
"""
new Env('农好优');
"""
"""推送通知开关"""
notify = 0
"""1为开，0为关"""

import os
import requests
from multiprocessing import Pool
import datetime
def get_msg ():#line:15
    O00OOOOO00000O0OO ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:17
    O00000O00000O0OO0 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O00OOOOO00000O0OO ).json ()#line:18
    return O00000O00000O0OO0 #line:19
_OO0OO0OOOO0O0O0OO =get_msg ()#line:22
try :#line:24
    from bs4 import BeautifulSoup #line:25
except :#line:26
    print (_OO0OO0OOOO0O0O0OO .get ('help')['bs4'])#line:27
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
    OOOOOOOO0OO0OO0O0 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:42
    return OOOOOOOO0OO0OO0O0 #line:43
class NHY :#line:46
    def __init__ (OOOOOO0O00O0O0OO0 ,OO0OOO0O00O00O0O0 ,OO00OO000OOO00O0O ):#line:47
        OOOOOO0O00O0O0OO0 .index =OO0OOO0O00O00O0O0 #line:48
        OOOOOO0O00O0O0OO0 .phone =OO00OO000OOO00O0O .split ('#')[0 ]#line:49
        OOOOOO0O00O0O0OO0 .psw =OO00OO000OOO00O0O .split ('#')[1 ]#line:50
        OOOOOO0O00O0O0OO0 .s =requests .session ()#line:51
        OOOOOO0O00O0O0OO0 .s .headers ={'Accept':'application/json, text/javascript, */*; q=0.01','X-Requested-With':'XMLHttpRequest','User-Agent':'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36  XiaoMi/MiuiBrowser/10.8.1 LT-APP/45/104','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',}#line:56
        OOOOOO0O00O0O0OO0 .msg ='='*50 +'\n'#line:57
    def login (OOO0OOOO0O0OOOO00 ):#line:59
        try :#line:60
            OO00O0O0OO000O000 =f"username={OOO0OOOO0O0OOOO00.phone}&password={OOO0OOOO0O0OOOO00.psw}&xieyi=on"#line:61
            OOO00O00O0O0O000O ='http://wap.nonghaoyou.cn/Public/login'#line:62
            O00000O0OOOO00O0O =OOO0OOOO0O0OOOO00 .s .post (OOO00O00O0O0O000O ,data =OO00O0O0OO000O000 ).json ()#line:63
            O00OOO00000O00O00 =f'账号{OOO0OOOO0O0OOOO00.index}：{O00000O0OOOO00O0O.get("info")}'#line:64
            print (O00OOO00000O00O00 )#line:65
            OOO0OOOO0O0OOOO00 .msg +=O00OOO00000O00O00 +'\n'#line:66
            return True #line:67
        except :#line:68
            O00OOO00000O00O00 =f'账号{OOO0OOOO0O0OOOO00.index}：登录失败，请检查账号密码填写是否正确'#line:69
            print (O00OOO00000O00O00 )#line:70
            OOO0OOOO0O0OOOO00 .msg +=O00OOO00000O00O00 +'\n'#line:71
            return False #line:72
    def get_info (O0O000O0O0000O00O ):#line:74
        OO0OOO000OOOOO00O ='http://wap.nonghaoyou.cn/Member/index'#line:75
        O0O0O00OO00OOOOOO =O0O000O0O0000O00O .s .get (OO0OOO000OOOOO00O ).text #line:76
        O00OOOOOO0OO00000 =BeautifulSoup (O0O0O00OO00OOOOOO ,'html.parser')#line:77
        O0O0OOO0OOOOOO0O0 =O00OOOOOO0OO00000 .find ('a',href ="info_edit").text #line:78
        OO0O0O000O00O0OO0 =O00OOOOOO0OO00000 .find_all ('div',class_ ='my-number')#line:79
        OO00O0O0OO000O00O =OO0O0O000O00O0OO0 [0 ].text #line:80
        OOO0O0OO0OOOOOOOO =OO0O0O000O00O0OO0 [1 ].text #line:81
        O00O0O0OOOO0O0O00 =OO0O0O000O00O0OO0 [2 ].text #line:82
        O0OO0O0O00O00O00O =f'账号{O0O000O0O0000O00O.index}：{O0O0OOO0OOOOOO0O0},余额{OO00O0O0OO000O00O},积分{OOO0O0OO0OOOOOOOO},预估收益{O00O0O0OOOO0O0O00}'#line:83
        print (O0OO0O0O00O00O00O )#line:84
        O0O000O0O0000O00O .msg +=O0OO0O0O00O00O00O +'\n'#line:85
    def signin (O0OOO0000O00O00OO ):#line:87
        O0O0OO000OO000000 ={'uid':'11951'}#line:88
        OO000OO00OO0O0000 ='http://wap.nonghaoyou.cn/Member/ad_video_api'#line:89
        for O0OO0O00OOOO0OOO0 in range (1 ,11 ):#line:90
            OOO0O0000O0O0OOOO =O0OOO0000O00O00OO .s .post (OO000OO00OO0O0000 ,data =O0O0OO000OO000000 ).json ()#line:91
            O000OOOO000000O00 =f'账号{O0OOO0000O00O00OO.index}：第{O0OO0O00OOOO0OOO0}次{OOO0O0000O0O0OOOO.get("info")}'#line:92
            print (O000OOOO000000O00 )#line:93
            O0OOO0000O00O00OO .msg +=O000OOOO000000O00 +'\n'#line:94
        O0OOO0000O00O00OO .msg +=f'账号{O0OOO0000O00O00OO.index}：签到完成\n'#line:95
    def run (O0O0OOO0OOO00O00O ):#line:97
        if O0O0OOO0OOO00O00O .login ():#line:98
            O0O0OOO0OOO00O00O .get_info ()#line:99
            O0O0OOO0OOO00O00O .signin ()#line:100
            O0O0OOO0OOO00O00O .get_info ()#line:101
        return O0O0OOO0OOO00O00O .msg #line:102
def nhysignin (O00OO000OO0OOOO00 ,O0OOOOO00O0O000O0 ):#line:105
    O0OOO0O0OO0O000O0 =NHY (O00OO000OO0OOOO00 ,O0OOOOO00O0O000O0 )#line:106
    return O0OOO0O0OO0O000O0 .run ()#line:107
def get_info ():#line:110
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:112
    print ('入口http://wap.nonghaoyou.cn/Public/reg/recom/131242，注册时填写邀请码131242\n需实名认证，谨慎注册 ' '平台商品偏贵，小心被反薅\n脚本只签到，用户自行做任务等造成损失，本人概不负责\n默认不推送通知，如需推送，将脚本开头的notify改为1，复制青龙的notify.py到脚本所在文件夹并设置好相关参数')#line:115
    O0O0O0OO00O0OOOOO ='V1.0'#line:116
    OOO0000O00O0OO000 =_OO0OO0OOOO0O0O0OO ['version']['knhy']#line:117
    print (f'当前版本{O0O0O0OO00O0OOOOO}，仓库版本{OOO0000O00O0OO000}')#line:118
    if O0O0O0OO00O0OOOOO <OOO0000O00O0OO000 :#line:119
        print ('请到仓库下载最新版本')#line:120
def main ():#line:123
    get_info ()#line:124
    OO0O00O0OOO00O00O =os .getenv ('nhyck')#line:125
    if not OO0O00O0OOO00O00O :#line:126
        print (_OO0OO0OOOO0O0O0OO ['msg']['农好优'])#line:127
        print ('='*25 )#line:128
        exit ()#line:129
    print ('='*25 )#line:130
    if notify :#line:131
        load_notify ()#line:132
    OO0O00O0OOO00O00O =OO0O00O0OOO00O00O .split ('&')#line:133
    with Pool ()as OOOOOOOO0O0OOOO0O :#line:134
        O0OOOOOOOO0OO00OO =[O0O00O00OO00OOOO0 for O0O00O00OO00OOOO0 in OOOOOOOO0O0OOOO0O .starmap (nhysignin ,list (enumerate (OO0O00O0OOO00O00O ,start =1 )))]#line:135
    O0OOOOOOOO0OO00OO =''.join (O0OOOOOOOO0OO00OO )+'\n本通知by：https://github.com/kxs2018/xiaoym\ntg讨论群：https://t.me/xiaoymgroup\n通知时间：{ftime()}'#line:136
    if notify and send :#line:137
        send ('农好优签到信息',O0OOOOOOOO0OO00OO )#line:138
if __name__ =='__main__':#line:141
    main ()#line:142
