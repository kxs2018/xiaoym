# -*- coding: utf-8 -*-
# k_小兔快跑.py
# Author: 惜之酱
"""
new Env('小兔快跑');
"""
import datetime
import random
import time
from multiprocessing import Pool
import requests
import os

"""通知开关"""
notify = 0
"""1为开，0为关"""
def get_msg ():#line:16
    OOO0OO00OOOOO00OO ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:18
    O000O0O0OOOO000O0 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OOO0OO00OOOOO00OO ).json ()#line:19
    return O000O0O0OOOO000O0 #line:20
_O000O00O0OOO0000O =get_msg ()#line:23
def ftime ():#line:26
    O0O000O00000OO0O0 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:27
    return O0O000O00000OO0O0 #line:28
class RABBIT :#line:31
    def __init__ (OO0OOOO00O00O0O00 ,O00OOO000OO0OO0O0 ,O00000O0000OO0OO0 ):#line:32
        OO0OOOO00O00O0O00 .index =O00OOO000OO0OO0O0 #line:33
        OO0OOOO00O00O0O00 .s =requests .session ()#line:34
        OO0OOOO00O00O0O00 .msg =''#line:35
        OO0OOOO00O00O0O00 .taskurl ='https://cluster.qifeixian.com/api/activity-center/v1/rabbit/finish/task'#line:36
        OO0OOOO00O00O0O00 .headers ={'Host':'cluster.qifeixian.com','Connection':'keep-alive','sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"','Accept':'application/json, text/plain, */*','x-ds-key':O00000O0000OO0OO0 ,'Content-Type':'application/json','sec-ch-ua-mobile':'?0','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8447','sec-ch-ua-platform':'"Windows"','Origin':'https://www.qifeixian.com','Sec-Fetch-Site':'same-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://www.qifeixian.com/','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh;q=0.9'}#line:49
    def init (OO0O00OOOO000000O ):#line:51
        O00OOOO0OOO0O000O ='https://cluster.qifeixian.com/api/activity-center/v1/rabbit/init'#line:52
        OOOO00O0000OOOOOO =OO0O00OOOO000000O .s .get (O00OOOO0OOO0O000O ,headers =OO0O00OOOO000000O .headers ).json ()#line:53
        if OOOO00O0000OOOOOO .get ('code')!=10000 :#line:55
            print (f'账号{OO0O00OOOO000000O.index} 登录失败，请检查ck有效性')#line:56
            OO0O00OOOO000000O .msg +=f'账号{OO0O00OOOO000000O.index} 登录失败，请检查ck有效性\n'#line:57
            return False #line:58
        O0OO00000OO0O000O =OOOO00O0000OOOOOO .get ('data').get ('user').get ('userId')#line:59
        if O0OO00000OO0O000O :#line:60
            print (f'账号{OO0O00OOOO000000O.index} 登录成功')#line:61
            OO0O00OOOO000000O .msg +=f'账号{OO0O00OOOO000000O.index} 登录成功\n'#line:62
            return True #line:63
    def signin (OOO00000OO0O0O0OO ):#line:65
        OOO00O0O0OO00O0O0 ={"type":"day_sign"}#line:66
        OOO0OO00OOO0O000O =OOO00000OO0O0O0OO .s .post (OOO00000OO0O0O0OO .taskurl ,headers =OOO00000OO0O0O0OO .headers ,json =OOO00O0O0OO00O0O0 ).json ()#line:67
        if OOO0OO00OOO0O000O .get ('code')==10000 :#line:68
            print (f'账号{OOO00000OO0O0O0OO.index} 签到：{OOO0OO00OOO0O000O.get("data").get("message")}')#line:69
            OOO00000OO0O0O0OO .msg +=f'账号{OOO00000OO0O0O0OO.index} 签到：{OOO0OO00OOO0O000O.get("data").get("message")}\n'#line:70
    def browse_shop (O0OOO00OOO0O00OO0 ):#line:72
        OOO0OO00O0OO00O0O ={"type":"day_browse_shop"}#line:73
        O0O000O0O000O0000 =O0OOO00OOO0O00OO0 .s .post (O0OOO00OOO0O00OO0 .taskurl ,headers =O0OOO00OOO0O00OO0 .headers ,json =OOO0OO00O0OO00O0O ).json ()#line:74
        OOO0OOOOOOOO0OOOO =O0O000O0O000O0000 .get ('data')#line:75
        if O0O000O0O000O0000 .get ('code')==10000 :#line:76
            if OOO0OOOOOOOO0OOOO .get ('code')==10000 :#line:77
                print (f'账号{O0OOO00OOO0O00OO0.index} 浏览商城任务完成')#line:78
                O0OOO00OOO0O00OO0 .msg +=f'账号{O0OOO00OOO0O00OO0.index} 浏览商城任务完成\n'#line:79
            else :#line:80
                print (f'账号{O0OOO00OOO0O00OO0.index} 浏览商城:{OOO0OOOOOOOO0OOOO.get("message")}')#line:81
                O0OOO00OOO0O00OO0 .msg +=f'账号{O0OOO00OOO0O00OO0.index} 浏览商城:{OOO0OOOOOOOO0OOOO.get("message")}\n'#line:82
    def browse_bk (OOO0OOOO00O0000O0 ):#line:84
        OOOO0O000OO0O00O0 ={"type":"day_browse_bk"}#line:85
        OOO00OOOO0O000O00 =OOO0OOOO00O0000O0 .s .post (OOO0OOOO00O0000O0 .taskurl ,headers =OOO0OOOO00O0000O0 .headers ,json =OOOO0O000OO0O00O0 ).json ()#line:86
        OO0O00O00OO0OO0O0 =OOO00OOOO0O000O00 .get ('data')#line:87
        if OOO00OOOO0O000O00 .get ('code')==10000 :#line:88
            if OO0O00O00OO0OO0O0 .get ('code')==10000 :#line:89
                print (f'账号{OOO0OOOO00O0000O0.index} 浏览爆款任务完成')#line:90
            else :#line:91
                print (f'账号{OOO0OOOO00O0000O0.index} 浏览爆款:{OO0O00O00OO0OO0O0.get("message")}')#line:92
    def lottery (O00O00O0O0OOOOOOO ):#line:94
        OO00OO0000000O00O ='https://cluster.qifeixian.com/api/activity-center/v1/lottery/user-info'#line:95
        OOOO00O0OO0OOO00O =O00O00O0O0OOOOOOO .s .get (OO00OO0000000O00O ,headers =O00O00O0O0OOOOOOO .headers ).json ()#line:96
        OOOOO0OO0000O00O0 =OOOO00O0OO0OOO00O .get ('data')#line:97
        O00OOO0OOOO0OOO00 ='https://cluster.qifeixian.com/api/activity-center/v1/lottery'#line:98
        if OOOO00O0OO0OOO00O .get ('code')==10000 :#line:99
            O000OOO0O0OOOOO00 =OOOOO0OO0000O00O0 .get ('count').get ('total')#line:100
            O0OOO0O00OOO0OO00 =OOOOO0OO0000O00O0 .get ('count').get ('user_today_count')#line:101
            O0O0000OO00000OOO =OOOOO0OO0000O00O0 .get ('balance')/100 #line:102
            print (f'账号{O00O00O0O0OOOOOOO.index} 单日总抽奖次数{O000OOO0O0OOOOO00}，已抽奖次数{O0OOO0O00OOO0OO00}，剩余fb {int(O0O0000OO00000OOO)}')#line:103
            O00O00O0O0OOOOOOO .msg +=f'账号{O00O00O0O0OOOOOOO.index} 单日总抽奖次数{O000OOO0O0OOOOO00}，已抽奖次数{O0OOO0O00OOO0OO00}，剩余fb {int(O0O0000OO00000OOO)}\n'#line:104
            if int (O0O0000OO00000OOO /50 )<1 or O0OOO0O00OOO0OO00 >=O000OOO0O0OOOOO00 :#line:105
                print (f'账号{O00O00O0O0OOOOOOO.index} fb或可抽奖次数不足，跳过抽奖')#line:106
                O00O00O0O0OOOOOOO .msg +=f'账号{O00O00O0O0OOOOOOO.index} fb或可抽奖次数不足，跳过抽奖'#line:107
            else :#line:108
                for OO000OO0O0OO0O0OO in range (min (int (O0O0000OO00000OOO /50 ),O000OOO0O0OOOOO00 -O0OOO0O00OOO0OO00 )):#line:109
                    OOOO00O0OO0OOO00O =O00O00O0O0OOOOOOO .s .post (O00OOO0OOOO0OOO00 ,headers =O00O00O0O0OOOOOOO .headers ).json ()#line:110
                    print (f'账号{O00O00O0O0OOOOOOO.index} 第{OO000OO0O0OO0O0OO + 1}次 {OOOO00O0OO0OOO00O["data"]["data"]["prize"]["name"]}')#line:111
                    O00O00O0O0OOOOOOO .msg +=f'账号{O00O00O0O0OOOOOOO.index} 第{OO000OO0O0OO0O0OO + 1}次 {OOOO00O0OO0OOO00O["data"]["data"]["prize"]["name"]}\n'#line:112
                    time .sleep (8 )#line:113
    def tx (O00OOO0OOO0OOOOOO ):#line:115
        pass #line:116
    def run (OOO000OOO0O0O00OO ):#line:118
        if OOO000OOO0O0O00OO .init ():#line:119
            OOO000OOO0O0O00OO .signin ()#line:120
            OOO000OOO0O0O00OO .browse_shop ()#line:121
            OOO000OOO0O0O00OO .browse_bk ()#line:122
            OOO000OOO0O0O00OO .lottery ()#line:123
            OOO000OOO0O0O00OO .tx ()#line:124
        return OOO000OOO0O0O00OO .msg #line:125
def tz (OOO0OO0O0OO000O00 ,O00000000O00000OO ):#line:128
    try :#line:129
        OO0O000O0O00000O0 =RABBIT (OOO0OO0O0OO000O00 ,O00000000O00000OO )#line:130
        return OO0O000O0O00000O0 .run ()#line:131
    except Exception as OO00OOO0O00OOO000 :#line:132
        return f'账号{OOO0OO0O0OO000O00} 发生错误 {OO00OOO0O00OOO000}'#line:133
def load_notify ():#line:136
    global send #line:137
    try :#line:138
        from notify import send #line:139
        print ("加载通知服务成功！")#line:140
    except :#line:141
        send =False #line:142
        print ('加载通知服务失败')#line:143
def ts ():#line:146
    return random .randint (1 ,500 )#line:147
def get_info ():#line:150
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:152
    print ('入口\n#小程序://起飞线/Vsj2XGb0YkQ4NoA\n默认不推送通知，如需推送，将脚本开头的notify改为1，复制青龙的notify.py到脚本所在文件夹并设置好相关参数')#line:154
    OO00OO0OOO0O0OOOO ='V1.0'#line:155
    OO00O0OO0OO0O0OOO =_O000O00O0OOO0000O ['version']['k_小兔快跑']#line:156
    print (f'当前版本{OO00OO0OOO0O0OOOO}，仓库版本{OO00O0OO0OO0O0OOO}')#line:157
    if OO00OO0OOO0O0OOOO <OO00O0OO0OO0O0OOO :#line:158
        print ('请到仓库下载最新版本')#line:159

def main ():#line:163
    get_info ()#line:164
    O000O0OO00OO000O0 =os .getenv ('qfxck')#line:165
    if not O000O0OO00OO000O0 :#line:166
        print (_O000O00O0OOO0000O ['msg']['小兔快跑'])#line:167
        print ('='*25 )#line:168
        exit ()#line:169
    print ('='*25 )#line:170
    O000O0OO00OO000O0 =O000O0OO00OO000O0 .split ('&')#line:171
    if notify :#line:172
        load_notify ()#line:173
    print (f'共获取到{len(O000O0OO00OO000O0)}个账号')#line:174
    with Pool ()as O00O00000OOOO0O00 :#line:175
        OOOOOOOOOO00OO0O0 =[]#line:176
        print (f'任务将在{ts()}秒后开始')#line:177
        time .sleep (ts ())#line:178
        for OO0O0OOOOO00O0OO0 ,OO0O0O0O0O00000OO in enumerate (O000O0OO00OO000O0 ,start =1 ):#line:179
            OO0OO0OO0O0O0O0O0 =O00O00000OOOO0O00 .apply_async (tz ,args =(OO0O0OOOOO00O0OO0 ,OO0O0O0O0O00000OO )).get ()#line:180
            OOOOOOOOOO00OO0O0 .append (OO0OO0OO0O0O0O0O0 )#line:181
        O0O00000O00OO0OOO ='\n'.join (OOOOOOOOOO00OO0O0 )+f'\n本通知by：https://github.com/kxs2018/xiaoym\ntg讨论群：https://t.me/xizhiaigroup\n通知时间：{ftime()}'#line:183
        if notify and send :#line:184
            send ('小兔快跑通知',O0O00000O00OO0OOO )#line:185
if __name__ =='__main__':#line:188
    main ()#line:189
