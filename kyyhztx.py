# -*- coding: utf-8 -*-
# kyyhztx
# Author: kk
# date：2023/9/25 23:53
import os #line:5
import requests #line:6
import threading #line:7
from queue import Queue #line:8
import time #line:9

"""实时日志开关"""#line:11
printf =1 #line:12
"""1为开，0为关，默认关"""#line:13

"""调试日志开关"""#line:15
debug =0 #line:16
"""1为开，0为关，默认关"""#line:17

"""设置线程数量"""#line:19
max_workers =5 #line:20
"""设置多少，最多有多少个号在同时任务"""#line:21

"""设置提现标准"""
txbz =30 #line:24
"""设置为50，即为5毛起提"""#line:25
def printlog (text ):#line:28
    if printf :#line:29
        print (text )#line:30
class YYHZ :#line:33
    def __init__ (self ,index ,ck ):#line:34
        self .index =index #line:35
        self .msg =''#line:36
        self .cwd =None #line:37
        self .s =requests .session ()#line:38
        self .s .headers ={'Host':'x.moonbox.site','Connection':'keep-alive','Accept':'application/json','Cache-Control':'no-cache','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8431 Flue','FastAuthorization':'','Content-Type':'application/json','Sec-Fetch-Site':'same-origin','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh;q=0.9',"cookie":f'app-token={ck}'}#line:45
    def withdrawinfo (self ):#line:47
        OOO0OO0OO0O0O000O ='https://x.moonbox.site/api/account/withdraw/info'#line:48
        OOOO0O00000O0O0OO =self .s .get (OOO0OO0OO0O0O000O ).json ()#line:49
        if OOOO0O00000O0O0OO .get ('code')==1 :#line:50
            self .cwd =OOOO0O00000O0O0OO .get ('data').get ('canWithdrawDou')#line:51
            O0000O0O0000OOO0O =OOOO0O00000O0O0OO .get ('data').get ('freezeDou')#line:52
            printlog (f'账号账号{self.index}:可提现豆子{self.cwd}，冻结豆子{O0000O0O0000OOO0O}')#line:53
            self .msg +=f'可提现豆子{self.cwd}，冻结豆子{O0000O0O0000OOO0O}\n'#line:54
            if self .cwd <txbz :#line:55
                printlog (f'账号{self.index}:可提现豆子小于{txbz}，不提现')#line:56
                self .msg +=f'可提现豆子小于{txbz}，不提现\n'#line:57
                return False #line:58
            return True #line:59
        else :#line:60
            printlog (f'账号{self.index}:获取提现信息错误，未认证手机，认证手机后重新抓包')#line:61
            self .msg +=f'获取提现信息错误，未认证手机，认证手机后重新抓包\n'#line:62
            return False #line:63
    def withdraw (self ):#line:65
        O00OO0OOO0OO000O0 ='https://x.moonbox.site/api/account/cash/withdraw'#line:66
        OO000OOO000O0O000 ={"dou":self .cwd }#line:67
        O0OO00OO000OO0O00 =self .s .post (O00OO0OOO0OO000O0 ,json =OO000OOO000O0O000 ).json ()#line:68
        if O0OO00OO000OO0O00 .get ('data'):#line:69
            printlog (f'账号{self.index}: 提现成功，提现金额{self.cwd / 100}元，耐心等待审核到账')#line:70
            self .msg +=f'提现成功，提现金额{self.cwd / 100}元，耐心等待审核到账\n'#line:71
        else :#line:72
            printlog (f'账号{self.index}: 提现失败,原因：{O0OO00OO000OO0O00.get("msg")}')#line:73
            self .msg +=f'提现失败,原因：{O0OO00OO000OO0O00.get("msg")}\n'#line:74
    def run (self ):#line:76
        if self .withdrawinfo ():#line:77
            self .withdraw ()#line:78
        if not printf :#line:79
            print (self .msg .strip ())#line:80
def yd (q ):#line:83
    while not q .empty ():#line:84
        O000000000O0000OO ,OO0O0000O00O0O00O =q .get ()#line:85
        OOO000000OO0OO00O =YYHZ (O000000000O0000OO ,OO0O0000O00O0O00O )#line:86
        OOO000000OO0OO00O .run ()#line:87
def get_ver ():#line:90
    OO00OO00OO00O0000 ='kyyhztx V1.0'#line:91
    O0O0OOOO0OO0OO0O0 ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:94
    O0OO00O0OOOO0OOOO =requests .get ('https://ghproxy.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json',headers =O0O0OOOO0OO0OO0O0 ).json ()#line:96
    O00OO00OOO000OO0O =OO00OO00OO00O0000 .split (' ')[1 ]#line:97
    O0OOOOO0OOOO00O0O =O0OO00O0OOOO0OOOO .get ('version').get (OO00OO00OO00O0000 .split (' ')[0 ])#line:98
    O0OOOOO00O0OO00OO =f"当前版本 {O00OO00OOO000OO0O}，仓库版本 {O0OOOOO0OOOO00O0O}"#line:99
    if O00OO00OOO000OO0O <O0OOOOO0OOOO00O0O :#line:100
        O0OOOOO00O0OO00OO +='\n'+'请到https://github.com/kxs2018/xiaoym下载最新版本'#line:101
    return O0OOOOO00O0OO00OO #line:102
def main ():#line:105
    print ("-"*50 +f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n'+'-'*50 )#line:106
    O000OO0O0OO0OO000 =os .getenv ('yyhzck')#line:107
    O000OO0O0OO0OO000 =O000OO0O0OO0OO000 .split ('&')#line:108
    OO00O00OO0OO0000O =Queue ()#line:109
    OO0000000O000O000 =[]#line:110
    for OO000O000O0OO0OOO ,OO0O00OO00O0OOOO0 in enumerate (O000OO0O0OO0OO000 ,start =1 ):#line:111
        printlog (f'{OO0O00OO00O0OOOO0}\n以上是账号 {OO000O000O0OO0OOO}的ck，请核对是否正确，如不正确，请检查ck填写格式')#line:112
        OO00O00OO0OO0000O .put ([OO000O000O0OO0OOO ,OO0O00OO00O0OOOO0 ])#line:113
    for OO0O0OOOOO0O00OOO in range (max_workers ):#line:114
        O0000OOO0000O0000 =threading .Thread (target =yd ,args =(OO00O00OO0OO0000O ,))#line:115
        O0000OOO0000O0000 .start ()#line:116
        OO0000000O000O000 .append (O0000OOO0000O0000 )#line:117
        time .sleep (5 )#line:118
    for O000OOOOO00OO000O in OO0000000O000O000 :#line:119
        O000OOOOO00OO000O .join ()#line:120
if __name__ =='__main__':#line:123
    main ()#line:124
