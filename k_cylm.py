# -*- coding: utf-8 -*-
# k_cylm
"""
先运行脚本，有问题再到群里问
new Env('创娱联盟签到');
提现需绑定支付宝，请提前绑定
支付宝提前设置好登录邮箱，一个支付宝可绑2个号
"""
notify = 0  # 推送通知开关，1为开，0为关
max_workers = 5  # 设置线程数，设置为5，即最多有5个账号在跑任务

import requests
import time
import json
import multiprocessing
import os
import random
import datetime

def get_msg ():#line:23
    OO00000OO0O000O0O ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:25
    O0O0OOOOOO000O0OO =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OO00000OO0O000O0O ).json ()#line:26
    return O0O0OOOOOO000O0OO #line:27
_O00O0OO0OOO00OOOO =get_msg ()#line:30
def ftime ():#line:33
    O00O0OOO000OO00O0 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:34
    return O00O0OOO000OO00O0 #line:35
class CYLM :#line:38
    def __init__ (OOOOO0OOO0OO00000 ,O0OO00000OOOO0O00 ):#line:39
        OOOOO0OOO0OO00000 .account =O0OO00000OOOO0O00 .split ('#')[0 ]#line:40
        OOOOO0OOO0OO00000 .un =OOOOO0OOO0OO00000 .account [:3 ]+'*'+OOOOO0OOO0OO00000 .account [-4 :]#line:41
        OOOOO0OOO0OO00000 .password =O0OO00000OOOO0O00 .split ('#')[1 ]#line:42
        OOOOO0OOO0OO00000 .s =requests .session ()#line:43
        OOOOO0OOO0OO00000 .s .headers ={'os':'android','Content-Type':'application/x-www-form-urlencoded',}#line:44
        OOOOO0OOO0OO00000 .msg =''#line:45
    def get_token (O0O00OOOOO0OOOO0O ):#line:47
        try :#line:48
            with open ('cylm.json','r',encoding ='utf-8')as O0OOO00OOOO0O000O :#line:49
                OO00O00O0O0OO0O00 =json .loads (O0OOO00OOOO0O000O .read ())#line:50
        except :#line:51
            OO00O00O0O0OO0O00 ={}#line:52
        OO00O0OOOOO00O0OO =OO00O00O0O0OO0O00 .get (O0O00OOOOO0OOOO0O .account )#line:53
        if not OO00O0OOOOO00O0OO :#line:54
            print (f'【{O0O00OOOOO0OOOO0O.un}】:没有从本地获取到token，正在登录')#line:55
            OO00O0OOOOO00O0OO =O0O00OOOOO0OOOO0O .login ()#line:56
            OO00O00O0O0OO0O00 .update ({O0O00OOOOO0OOOO0O .account :OO00O0OOOOO00O0OO })#line:57
            with open ('cylm.json','w',encoding ='utf-8')as O0OOO00OOOO0O000O :#line:58
                O0OOO00OOOO0O000O .write (json .dumps (OO00O00O0O0OO0O00 ))#line:59
        return OO00O0OOOOO00O0OO #line:60
    def login (O000O00O0000O00OO ):#line:62
        O0OOOOO0OO000OO0O ='https://52.yyyy.run/api/user/login'#line:63
        O000O000O0OO0OO00 =f'account={O000O00O0000O00OO.account}&password={O000O00O0000O00OO.password}'#line:64
        OOOO0O00OOO0O0OOO =O000O00O0000O00OO .s .post (O0OOOOO0OO000OO0O ,data =O000O000O0OO0OO00 ).json ()#line:65
        if OOOO0O00OOO0O0OOO .get ('code')==1 :#line:67
            O00OO00O0O000O0OO =OOOO0O00OOO0O0OOO .get ('data')['userinfo']['token']#line:68
            O00OO0000O0OOO000 =OOOO0O00OOO0O0OOO .get ('data')['userinfo']['nickname']#line:69
            print (f'【{O000O00O0000O00OO.un}】:{O00OO0000O0OOO000},{OOOO0O00OOO0O0OOO.get("msg")}')#line:70
            O000O00O0000O00OO .msg +=f'【{O000O00O0000O00OO.un}】:{O00OO0000O0OOO000},{OOOO0O00OOO0O0OOO.get("msg")}\n'#line:71
            return O00OO00O0O000O0OO #line:72
        else :#line:73
            print (f'【{O000O00O0000O00OO.un}】:{OOOO0O00OOO0O0OOO.get("msg")}')#line:74
            O000O00O0000O00OO .msg +=f'【{O000O00O0000O00OO.un}】:{OOOO0O00OOO0O0OOO.get("msg")}\n'#line:75
            print (f'【{O000O00O0000O00OO.un}】:请检查账号密码是否填写错误')#line:76
            return False #line:77
    def get_signinfo (O00O000OO000000O0 ):#line:79
        OOO00OO0000000000 =O00O000OO000000O0 .get_token ()#line:80
        OO000OOO0OO00OO00 ='https://52.yyyy.run/api/sign/userSignData'#line:81
        O00O000OO000000O0 .s .headers .update ({'token':OOO00OO0000000000 })#line:82
        O00O0OOOO00OOOO00 =O00O000OO000000O0 .s .post (OO000OOO0OO00OO00 ).json ()#line:83
        if O00O0OOOO00OOOO00 .get ('code')!=1 :#line:85
            print (f'【{O00O000OO000000O0.un}】：token失效，正在重新获取')#line:86
            OOO00OO0000000000 =O00O000OO000000O0 .login ()#line:87
            O00O000OO000000O0 .s .headers .update ({'token':OOO00OO0000000000 })#line:88
            O00O0OOOO00OOOO00 =O00O000OO000000O0 .s .post (OO000OOO0OO00OO00 ).json ()#line:89
        OO0O0OOOO00O00OO0 =O00O0OOOO00OOOO00 .get ('data')#line:90
        '''"coin":0.8,"all_coin":0.8,"today_coin":0.8,"yesterday_coin":0,"today_sign":2,"agent_coin":0,"score_text":"积分"'''#line:91
        OOOO00000O0O0OOO0 =OO0O0OOOO00O00OO0 .get ('coin')#line:92
        O00O000OO000000O0 .today_sign =OO0O0OOOO00O00OO0 .get ('today_sign')#line:93
        O0O000O0O0O0O0OO0 =OO0O0OOOO00O00OO0 .get ('today_coin')#line:94
        OO0OO0O0O0OOOOO00 =OO0O0OOOO00O00OO0 .get ('all_coin')#line:95
        print (f'【{O00O000OO000000O0.un}】:今日签到{O00O000OO000000O0.today_sign}次,获得积分{O0O000O0O0O0O0OO0},现有积分{OOOO00000O0O0OOO0},累计获得积分{OO0OO0O0O0OOOOO00}')#line:96
        O00O000OO000000O0 .msg +=f'【{O00O000OO000000O0.un}】:今日签到{O00O000OO000000O0.today_sign}次,获得积分{O0O000O0O0O0O0OO0},现有积分{OOOO00000O0O0OOO0},累计获得积分{OO0OO0O0O0OOOOO00}\n'#line:97
    def signin (O00000OOO00OOO00O ):#line:99
        for OOOO00O00OOOO000O in range (3 -int (O00000OOO00OOO00O .today_sign )):#line:100
            O00O00O0O0O0OOO0O ='https://52.yyyy.run/api/sign/getSignAd'#line:101
            O0O0OO0O0O0000OO0 =O00000OOO00OOO00O .s .post (O00O00O0O0O0OOO0O ).json ()#line:102
            O0O00OOOO00OO00O0 =O0O0OO0O0O0000OO0 .get ('data')['task_id']#line:103
            time .sleep (random .randint (16 ,18 ))#line:104
            O00O00O0O0O0OOO0O ='https://52.yyyy.run/api/sign/signTimeEnd'#line:105
            O00OO0O0O000OOO0O ={'task_id':O0O00OOOO00OO00O0 }#line:106
            O0O0OO0O0O0000OO0 =O00000OOO00OOO00O .s .post (O00O00O0O0O0OOO0O ,data =O00OO0O0O000OOO0O ).json ()#line:107
            print (f'【{O00000OOO00OOO00O.un}】:第{OOOO00O00OOOO000O + 1}次，{O0O0OO0O0O0000OO0.get("msg")}')#line:109
            time .sleep (1 )#line:110
    def get_info (O0O0O000O0OOO000O ):#line:112
        OOOOO00O00O00O000 ='https://52.yyyy.run/api/user/index'#line:113
        OO0OOOOO00OOO00OO =O0O0O000O0OOO000O .s .post (OOOOO00O00O00O000 ).json ()#line:114
        O000O0000OO0O00O0 =OO0OOOOO00OOO00OO .get ('data')#line:116
        O0O0O000O0OOO000O .money =O000O0000OO0O00O0 .get ('all_money')#line:117
        print (f'【{O0O0O000O0OOO000O.un}】:现有金币{O0O0O000O0OOO000O.money}')#line:118
        O0O0O000O0OOO000O .msg +=f'【{O0O0O000O0OOO000O.un}】:现有金币{O0O0O000O0OOO000O.money}\n'#line:119
    def with_draw (O0OOOOOO0O0OO0000 ):#line:121
        if O0OOOOOO0O0OO0000 .money >=1 :#line:122
            O0OOOOOO0O0OO0000 .s .headers .update ({'Referer':'http://52.yyyy.run/pages/user/myWithdrawal.html','Origin':'http://52.yyyy.run',})#line:124
            O000O00O00OO0O0O0 ='http://52.yyyy.run/api/user/postWith'#line:125
            O00O00O00000O0O0O =int (O0OOOOOO0O0OO0000 .money )#line:126
            O0000O00O000OO000 ={'num':O00O00O00000O0O0O }#line:127
            O0OO00O0O0OO0O0O0 =O0OOOOOO0O0OO0000 .s .post (O000O00O00OO0O0O0 ,data =O0000O00O000OO000 ).json ()#line:128
            print (f'【{O0OOOOOO0O0OO0000.un}】:提现金额 {O00O00O00000O0O0O},提现结果 {O0OO00O0O0OO0O0O0.get("msg")}')#line:129
            O0OOOOOO0O0OO0000 .msg +=f'【{O0OOOOOO0O0OO0000.un}】:提现金额 {O00O00O00000O0O0O},提现结果 {O0OO00O0O0OO0O0O0.get("msg")}\n'#line:130
        else :#line:131
            print (f'【{O0OOOOOO0O0OO0000.un}】:提现 你的金币不多了')#line:132
            O0OOOOOO0O0OO0000 .msg +=f'【{O0OOOOOO0O0OO0000.un}】:提现 你的金币不多了\n'#line:133
    def run (OOO00000000O000OO ):#line:135
        OOO00000000O000OO .get_signinfo ()#line:136
        if OOO00000000O000OO .today_sign <3 :#line:137
            OOO00000000O000OO .signin ()#line:138
        OOO00000000O000OO .get_info ()#line:139
        OOO00000000O000OO .with_draw ()#line:140
        return OOO00000000O000OO .msg #line:141
def cy_signin (O00OOOOO0O0OO0000 ):#line:144
    OO0O00OOO00OO0O0O =CYLM (O00OOOOO0O0OO0000 )#line:145
    return OO0O00OOO00OO0O0O .run ()#line:146
def load_notify ():#line:149
    global send #line:150
    try :#line:151
        from notify import send #line:152
        print ("加载通知服务成功！")#line:153
        return True #line:154
    except :#line:155
        print ('加载通知服务失败,请复制一份青龙notify.py到同级文件夹')#line:156
        return False #line:157
def get_info ():#line:160
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:162
    print ('入口\nhttps://52.yyyy.run//index/wechat/login/share_id/1904\n默认不推送通知，如需推送，将脚本开头的notify改为1，复制青龙的notify.py到脚本所在文件夹并设置好相关参数')#line:164
    O000O00OO0O0OO00O ='V0.1.2'#line:165
    OOO0O0OOOO00OOOO0 =_O00O0OO0OOO00OOOO ['version']['创娱联盟']#line:166
    print (f'当前版本{O000O00OO0O0OO00O}，仓库版本{OOO0O0OOOO00OOOO0}')#line:167
    print (_O00O0OO0OOO00OOOO .get ("update_log")['创娱联盟'])#line:168
    if O000O00OO0O0OO00O <OOO0O0OOOO00OOOO0 :#line:169
        print ('请到仓库下载最新版本')#line:170
    print ("="*25 )#line:171
def main ():#line:174
    get_info ()#line:175
    OOO0O000OOOO00O0O =os .getenv ('cylmck')#line:176
    if not OOO0O000OOOO00O0O :#line:177
        print (_O00O0OO0OOO00OOOO .get ('msg')['创娱联盟'])#line:178
        exit ()#line:179
    O0OO0OO0OO000000O =OOO0O000OOOO00O0O .replace ('&','\n').split ('\n')#line:180
    OO0OOO0O000OOOO00 =[]#line:181
    with multiprocessing .Pool (max_workers )as OOOO0OO0000OO0OOO :#line:182
        for OOO0O000OOOO00O0O in O0OO0OO0OO000000O :#line:183
            OO0OOO0O000OOOO00 .append (OOOO0OO0000OO0OOO .apply_async (cy_signin ,args =(OOO0O000OOOO00O0O ,)).get ())#line:184
    OOO0O00OO0O0O00OO ='\n'.join (OO0OOO0O000OOOO00 )#line:185
    if notify :#line:186
        if load_notify ():#line:187
            send ('创娱联盟签到通知',OOO0O00OO0O0O00OO +f'\n本通知by：https://github.com/kxs2018/xiaoym\ntg讨论群：https://t.me/xizhiaigroup\n通知时间：{ftime()}')#line:189
if __name__ =='__main__':#line:192
    main ()#line:193
