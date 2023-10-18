# -*- coding: utf-8 -*-
# k_jetta
# Author: 惜之酱
"""
new Env("捷达APP签到");
抓包serviceui-yy-ui.jconnect.faw-vw.com，请求头中的token值
export jettack="name#token&name1#token1#ua"
name方便自己辨别账号，随便填，ua可选参数，填抓包的user-agent值
多账号&连接或换行
通知默认关闭，如需开启，复制青龙的notify.py到脚本所在文件夹
"""
import os
import requests
import multiprocessing
import datetime

"""通知开关"""
notify = 0
"""1开0关"""

def get_msg ():#line:1
    OOOOOO00O00O0O000 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:3
    O0O0OO00O000O000O =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OOOOOO00O00O0O000 ).json ()#line:4
    return O0O0OO00O000O000O #line:5
_OO0O0OO0OOOO00OO0 =get_msg ()#line:8
def load_notify ():#line:11
    global send #line:12
    try :#line:13
        from notify import send #line:14
        print ("加载通知服务成功！")#line:15
    except :#line:16
        send =False #line:17
        print ('加载通知服务失败')#line:18
def ftime ():#line:21
    OO0OO0OO00OO0OO00 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:22
    return OO0OO0OO00OO0OO00 #line:23
def get_info ():#line:26
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*20 )#line:28
    O0OOOO0OO00O000OO ='v1.1'#line:29
    OO0000OOO0O000O0O =_OO0O0OO0OOOO00OO0 ['version']['捷达']#line:30
    print (f'当前版本{O0OOOO0OO00O000OO}，仓库版本{OO0000OOO0O000O0O}')#line:31
    if O0OOOO0OO00O000OO <OO0000OOO0O000O0O :#line:32
        print ('请到仓库下载最新版本k_jetta.py')#line:33
    print ("="*25 )#line:34
    return True #line:35
class JETTA :#line:38
    def __init__ (O000OOO0OO0000O00 ,O0O000OO00000O00O ):#line:39
        O000OOO0OO0000O00 .index =O0O000OO00000O00O .split ('#')[0 ]#line:40
        O000OOO0OO0000O00 .token =O0O000OO00000O00O .split ('#')[1 ]#line:41
        O000OOO0OO0000O00 .msg =''#line:42
        O000OOO0OO0000O00 .ua =O0O000OO00000O00O .split ('#')[2 ]if len (O0O000OO00000O00O .split ('#'))==3 else 'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36'#line:44
        O000OOO0OO0000O00 .s =requests .session ()#line:45
        O000OOO0OO0000O00 .s .headers ={'Host':'service-yy.jconnect.faw-vw.com','Connection':'keep-alive','Pragma':'no-cache','Cache-Control':'no-cache','Accept':'application/json, text/plain, */*','User-Agent':O000OOO0OO0000O00 .ua ,'token':O000OOO0OO0000O00 .token ,'Origin':'https://serviceui-yy-ui.jconnect.faw-vw.com','X-Requested-With':'com.fawvw.ebo','Sec-Fetch-Site':'same-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://serviceui-yy-ui.jconnect.faw-vw.com/','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'}#line:53
    def getUserInfo (O0O0OO0OOOO0OO0O0 ):#line:55
        O0OO00O000O00OO0O ='https://service-yy.jconnect.faw-vw.com/redpackbank/user/getUserInfo'#line:56
        O0O000O0OOO0OOOOO =O0O0OO0OOOO0OO0O0 .s .get (O0OO00O000O00OO0O ).json ()#line:57
        if O0O000O0OOO0OOOOO .get ('status')=='FAILED':#line:58
            print (f'账号【{O0O0OO0OOOO0OO0O0.index}】：登录失败，{O0O000O0OOO0OOOOO.get("errorMessage")}')#line:59
            O0O0OO0OOOO0OO0O0 .msg +=f'账号【{O0O0OO0OOOO0OO0O0.index}】：登录失败，{O0O000O0OOO0OOOOO.get("errorMessage")}\n'#line:60
            return False #line:61
        else :#line:62
            O0OOOOO00OO00OO00 =O0O000O0OOO0OOOOO ['data']['detail']['allPrize']#line:63
            print (f"账号【{O0O0OO0OOOO0OO0O0.index}】：登录成功，红包余额{O0OOOOO00OO00OO00}")#line:64
            O0O0OO0OOOO0OO0O0 .msg +=f"账号【{O0O0OO0OOOO0OO0O0.index}】：登录成功，红包余额{O0OOOOO00OO00OO00}\n"#line:65
            return True #line:66
    def getPrize (O00OOO000OOOO0000 ):#line:68
        OOOO00OOO00O00OOO ='https://service-yy.jconnect.faw-vw.com/redpackbank/prize/getPrize'#line:69
        O0OOO00O0O0OOOO00 =O00OOO000OOOO0000 .s .get (OOOO00OOO00O00OOO ).json ()#line:70
        if O0OOO00O0O0OOOO00 .get ('status')=='FAILED':#line:71
            print (f'账号【{O00OOO000OOOO0000.index}】：{O0OOO00O0O0OOOO00.get("errorMessage")}')#line:72
            O00OOO000OOOO0000 .msg +=f'账号【{O00OOO000OOOO0000.index}】：{O0OOO00O0O0OOOO00.get("errorMessage")}\n'#line:73
        else :#line:74
            O00O00OOOOOOOO0OO =O0OOO00O0O0OOOO00 ['data']['todayPrize']#line:75
            print (f"账号【{O00OOO000OOOO0000.index}】：签到获得{O00O00OOOOOOOO0OO}")#line:76
            O00OOO000OOOO0000 .msg +=f"账号【{O00OOO000OOOO0000.index}】：签到获得{O00O00OOOOOOOO0OO}\n"#line:77
    def run (OOO000O00O00O0000 ):#line:79
        if OOO000O00O00O0000 .getUserInfo ():#line:80
            OOO000O00O00O0000 .getPrize ()#line:81
        return OOO000O00O00O0000 .msg #line:82
def jd_signin (O0O00OO00OOO0000O ,O000OO0O000OOOOO0 ):#line:85
    O00OO0000OOO0OOOO =JETTA (O000OO0O000OOOOO0 )#line:86
    return O00OO0000OOO0OOOO .run ()#line:87
def main ():#line:90
    OO0O0OOO0OOO0OOOO =get_info ()#line:91
    O0O00O0OOO000O0OO =os .getenv ('jettack')#line:92
    if not O0O00O0OOO000O0OO :#line:93
        print ('没有获取到jettack，程序退出')#line:94
        exit ()#line:95
    O0O00O0OOO000O0OO =O0O00O0OOO000O0OO .replace ('&','\n').split ('\n')#line:96
    print (f'共获取到{len(O0O00O0OOO000O0OO)}个账号')#line:97
    O00OOOO0OOOO00OO0 =f'共获取到{len(O0O00O0OOO000O0OO)}个账号\n\n'#line:98
    if not OO0O0OOO0OOO0OOOO :#line:99
        exit ()#line:100
    with multiprocessing .Pool (5)as OO00O0OO0OO00000O :#line:101
        OO000O0000O0OOOO0 =OO00O0OO0OO00000O .starmap (jd_signin ,enumerate (O0O00O0OOO000O0OO ))#line:102
        O00OOOO0OOOO00OO0 +='\n'.join (OO000O0000O0OOOO0 )#line:103
    if notify :#line:104
        load_notify ()#line:105
        if send :#line:106
            send ('捷达APP签到通知',O00OOOO0OOOO00OO0 +f'\n本通知by：https://github.com/kxs2018/xiaoym\ntg讨论群：https://t.me/xizhiaigroup\n通知时间：{ftime()}')#line:108
if __name__ =='__main__':#line:111
    main ()#line:112
