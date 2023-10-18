# -*- coding: utf-8 -*-
# k_jetta
# Author: 惜之酱
"""
new Env("捷达APP签到");
抓包serviceui-yy-ui.jconnect.faw-vw.com，请求头中的token值
export jettack="name#token&name1#token1#ua"
name方便自己辨别账号，随便填，ua可选参数，填抓包的user-agent值
"""
import os
import requests
import multiprocessing
import datetime

"""通知开关"""
notify = 1
"""1开0关"""

def get_msg ():#line:1
    O00O000O00O00O00O ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:3
    O0OO0000O0O00O000 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O00O000O00O00O00O ).json ()#line:4
    return O0OO0000O0O00O000 #line:5
_O000O00OOO0O0000O =get_msg ()#line:8
def load_notify ():#line:11
    global send #line:12
    try :#line:13
        from notify import send #line:14
        print ("加载通知服务成功！")#line:15
    except :#line:16
        send =False #line:17
        print ('加载通知服务失败')#line:18
def ftime ():#line:21
    OOOOOOO0O0OO0OO00 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:22
    return OOOOOOO0O0OO0OO00 #line:23
def get_info ():#line:26
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*20 )#line:28
    O0O00OOOOOOO0O0O0 ='v1.0'#line:29
    OO00OOO0O0O00000O =_O000O00OOO0O0000O ['version']['捷达']#line:30
    print (f'当前版本{O0O00OOOOOOO0O0O0}，仓库版本{OO00OOO0O0O00000O}')#line:31
    if O0O00OOOOOOO0O0O0 <OO00OOO0O0O00000O :#line:32
        print ('请到仓库下载最新版本k_jetta.py')#line:33
    print ("="*25 )#line:34
    return True #line:35
class JETTA :#line:38
    def __init__ (OO00O0OOO0O00O00O ,O00OO0OOO00O00OO0 ):#line:39
        OO00O0OOO0O00O00O .index =O00OO0OOO00O00OO0 .split ('#')[0 ]#line:40
        OO00O0OOO0O00O00O .token =O00OO0OOO00O00OO0 .split ('#')[1 ]#line:41
        OO00O0OOO0O00O00O .msg =''#line:42
        OO00O0OOO0O00O00O .ua =O00OO0OOO00O00OO0 .split ('#')[2 ]if len (O00OO0OOO00O00OO0 .split ('#'))==3 else 'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36'#line:44
        OO00O0OOO0O00O00O .s =requests .session ()#line:45
        OO00O0OOO0O00O00O .s .headers ={'Host':'service-yy.jconnect.faw-vw.com','Connection':'keep-alive','Pragma':'no-cache','Cache-Control':'no-cache','Accept':'application/json, text/plain, */*','User-Agent':OO00O0OOO0O00O00O .ua ,'token':OO00O0OOO0O00O00O .token ,'Origin':'https://serviceui-yy-ui.jconnect.faw-vw.com','X-Requested-With':'com.fawvw.ebo','Sec-Fetch-Site':'same-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://serviceui-yy-ui.jconnect.faw-vw.com/','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'}#line:53
    def getUserInfo (OOO0OO0OOO00OO000 ):#line:55
        O0000O000OOOO00OO ='https://service-yy.jconnect.faw-vw.com/redpackbank/user/getUserInfo'#line:56
        OOOOO000OO0O0OO0O =OOO0OO0OOO00OO000 .s .get (O0000O000OOOO00OO ).json ()#line:57
        if OOOOO000OO0O0OO0O .get ('status')=='FAILED':#line:58
            print (f'账号【{OOO0OO0OOO00OO000.index}】：登录失败，{OOOOO000OO0O0OO0O.get("errorMessage")}')#line:59
            OOO0OO0OOO00OO000 .msg +=f'账号【{OOO0OO0OOO00OO000.index}】：登录失败，{OOOOO000OO0O0OO0O.get("errorMessage")}\n'#line:60
            return False #line:61
        else :#line:62
            OO000OOOO00O00O0O =OOOOO000OO0O0OO0O ['data']['detail']['allPrize']#line:63
            print (f"账号【{OOO0OO0OOO00OO000.index}】：登录成功，红包余额{OO000OOOO00O00O0O}")#line:64
            OOO0OO0OOO00OO000 .msg +=f"账号【{OOO0OO0OOO00OO000.index}】：登录成功，红包余额{OO000OOOO00O00O0O}\n"#line:65
            return True #line:66
    def getPrize (OOOO00OO00O0OOO0O ):#line:68
        O0OO00O00O0OO00OO ='https://service-yy.jconnect.faw-vw.com/redpackbank/prize/getPrize'#line:69
        O00OOO0OO0OO0OOO0 =OOOO00OO00O0OOO0O .s .get (O0OO00O00O0OO00OO ).json ()#line:70
        if O00OOO0OO0OO0OOO0 .get ('status')=='FAILED':#line:71
            print (f'账号【{OOOO00OO00O0OOO0O.index}】：{O00OOO0OO0OO0OOO0.get("errorMessage")}')#line:72
            OOOO00OO00O0OOO0O .msg +=f'账号【{OOOO00OO00O0OOO0O.index}】：{O00OOO0OO0OO0OOO0.get("errorMessage")}\n'#line:73
        else :#line:74
            OOO0O00O000OOOOO0 =O00OOO0OO0OO0OOO0 ['data']['data']['todayPrize']#line:75
            print (f"账号【{OOOO00OO00O0OOO0O.index}】：签到获得{OOO0O00O000OOOOO0}")#line:76
            OOOO00OO00O0OOO0O .msg +=f"账号【{OOOO00OO00O0OOO0O.index}】：签到获得{OOO0O00O000OOOOO0}\n"#line:77
    def run (O00OO0OOO0O0OO000 ):#line:79
        if O00OO0OOO0O0OO000 .getUserInfo ():#line:80
            O00OO0OOO0O0OO000 .getPrize ()#line:81
        return O00OO0OOO0O0OO000 .msg #line:82
def jd_signin (OO0O0OO0O00OOO0O0 ,OOO000000O00OOOO0 ):#line:85
    O0O000O0000OOO0OO =JETTA (OOO000000O00OOOO0 )#line:86
    return O0O000O0000OOO0OO .run ()#line:87
def main ():#line:90
    OOOOOOO00000O00O0 =get_info ()#line:91
    OO0O0OO0OOOO00OOO =os .getenv ('jettack')#line:92
    if not OO0O0OO0OOOO00OOO :#line:93
        print ('没有获取到jettack')#line:94
    print (f'共获取到{len(OO0O0OO0OOOO00OOO)}个账号')#line:95
    OO0O0O0O000O0O00O =f'共获取到{len(OO0O0OO0OOOO00OOO)}个账号\n\n'#line:96
    if not OOOOOOO00000O00O0 :#line:97
        exit ()#line:98
    with multiprocessing .Pool ()as OO0O0OOOO000O000O :#line:99
        OOO0O00O00O0000O0 =OO0O0OOOO000O000O .starmap (jd_signin ,enumerate (OO0O0OO0OOOO00OOO ))#line:100
        OO0O0O0O000O0O00O +='\n'.join (OOO0O00O00O0000O0 )#line:101
    if notify :#line:102
        load_notify ()#line:103
        if send :#line:104
            send ('捷达APP签到通知',OO0O0O0O000O0O00O +f'\n本通知by：https://github.com/kxs2018/xiaoym\ntg讨论群：https://t.me/xizhiaigroup\n通知时间：{ftime()}')#line:106
if __name__ =='__main__':#line:109
    main ()#line:110
