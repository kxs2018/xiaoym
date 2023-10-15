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
    O000O0O00OO0OO0O0 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:25
    OOOO0OOOOO0OO0OO0 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O000O0O00OO0OO0O0 ).json ()#line:26
    return OOOO0OOOOO0OO0OO0 #line:27
_OOOOO0O00OOOO00OO =get_msg ()#line:30
def ftime ():#line:33
    O00OOO00O0OOOO00O =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:34
    return O00OOO00O0OOOO00O #line:35
class CYLM :#line:38
    def __init__ (OO0O00OOOO00OOOOO ,OO0O0OOOOOO00000O ):#line:39
        OO0O00OOOO00OOOOO .account =OO0O0OOOOOO00000O .split ('#')[0 ]#line:40
        OO0O00OOOO00OOOOO .un =OO0O00OOOO00OOOOO .account [:3 ]+'*'+OO0O00OOOO00OOOOO .account [-4 :]#line:41
        OO0O00OOOO00OOOOO .password =OO0O0OOOOOO00000O .split ('#')[1 ]#line:42
        OO0O00OOOO00OOOOO .s =requests .session ()#line:43
        OO0O00OOOO00OOOOO .s .headers ={'os':'android','Content-Type':'application/x-www-form-urlencoded',}#line:44
        OO0O00OOOO00OOOOO .msg =''#line:45
    def get_token (O00O000000O0O00OO ):#line:47
        try :#line:48
            with open ('cylm.json','r',encoding ='utf-8')as OO0O0OOO0OO0000O0 :#line:49
                O000OO0000O0OO00O =json .loads (OO0O0OOO0OO0000O0 .read ())#line:50
        except :#line:51
            O000OO0000O0OO00O ={}#line:52
        O00O0O0OO0OO00OO0 =O000OO0000O0OO00O .get (O00O000000O0O00OO .account )#line:53
        if not O00O0O0OO0OO00OO0 :#line:54
            print (f'【{O00O000000O0O00OO.un}】:没有从本地获取到token，正在登录')#line:55
            O00O0O0OO0OO00OO0 =O00O000000O0O00OO .login ()#line:56
            O000OO0000O0OO00O .update ({O00O000000O0O00OO .account :O00O0O0OO0OO00OO0 })#line:57
            with open ('cylm.json','w',encoding ='utf-8')as OO0O0OOO0OO0000O0 :#line:58
                OO0O0OOO0OO0000O0 .write (json .dumps (O000OO0000O0OO00O ))#line:59
        return O00O0O0OO0OO00OO0 #line:60
    def login (OOOOOOOO00OO0O0O0 ):#line:62
        O00000OOOO000OOO0 ='https://52.yyyy.run/api/user/login'#line:63
        O0O00000OO0OO0O00 =f'account={OOOOOOOO00OO0O0O0.account}&password={OOOOOOOO00OO0O0O0.password}'#line:64
        O00O0000000OOO0O0 =OOOOOOOO00OO0O0O0 .s .post (O00000OOOO000OOO0 ,data =O0O00000OO0OO0O00 ).json ()#line:65
        if O00O0000000OOO0O0 .get ('code')==1 :#line:67
            O0O00O0000O0OOOO0 =O00O0000000OOO0O0 .get ('data')['userinfo']['token']#line:68
            OOOO000O0O0OOOOOO =O00O0000000OOO0O0 .get ('data')['userinfo']['nickname']#line:69
            print (f'【{OOOOOOOO00OO0O0O0.un}】:{OOOO000O0O0OOOOOO},{O00O0000000OOO0O0.get("msg")}')#line:70
            OOOOOOOO00OO0O0O0 .msg +=f'【{OOOOOOOO00OO0O0O0.un}】:{OOOO000O0O0OOOOOO},{O00O0000000OOO0O0.get("msg")}\n'#line:71
            return O0O00O0000O0OOOO0 #line:72
        else :#line:73
            print (f'【{OOOOOOOO00OO0O0O0.un}】:{O00O0000000OOO0O0.get("msg")}')#line:74
            OOOOOOOO00OO0O0O0 .msg +=f'【{OOOOOOOO00OO0O0O0.un}】:{O00O0000000OOO0O0.get("msg")}\n'#line:75
            print (f'【{OOOOOOOO00OO0O0O0.un}】:请检查账号密码是否填写错误')#line:76
            return False #line:77
    def get_signinfo (OOO00000OOO0O0OO0 ):#line:79
        OO00OOOOOO0000000 =OOO00000OOO0O0OO0 .get_token ()#line:80
        OO00O0O0O00000000 ='https://52.yyyy.run/api/sign/userSignData'#line:81
        OOO00000OOO0O0OO0 .s .headers .update ({'token':OO00OOOOOO0000000 })#line:82
        O0OOO0OO00O0000OO =OOO00000OOO0O0OO0 .s .post (OO00O0O0O00000000 ).json ()#line:83
        if O0OOO0OO00O0000OO .get ('code')!=1 :#line:85
            print (f'【{OOO00000OOO0O0OO0.un}】：token失效，正在重新获取')#line:86
            OO00OOOOOO0000000 =OOO00000OOO0O0OO0 .login ()#line:87
            OOO00000OOO0O0OO0 .s .headers .update ({'token':OO00OOOOOO0000000 })#line:88
            O0OOO0OO00O0000OO =OOO00000OOO0O0OO0 .s .post (OO00O0O0O00000000 ).json ()#line:89
        OOOOO0O00OO0O0000 =O0OOO0OO00O0000OO .get ('data')#line:90
        '''"coin":0.8,"all_coin":0.8,"today_coin":0.8,"yesterday_coin":0,"today_sign":2,"agent_coin":0,"score_text":"积分"'''#line:91
        OOO0O00OOOO0OO0O0 =OOOOO0O00OO0O0000 .get ('coin')#line:92
        OOO00000OOO0O0OO0 .today_sign =OOOOO0O00OO0O0000 .get ('today_sign')#line:93
        OO00O00O0O0O000O0 =OOOOO0O00OO0O0000 .get ('today_coin')#line:94
        O0OOOO0OO0O0OO0OO =OOOOO0O00OO0O0000 .get ('all_coin')#line:95
        print (f'【{OOO00000OOO0O0OO0.un}】:今日签到{OOO00000OOO0O0OO0.today_sign}次,获得积分{OO00O00O0O0O000O0},现有积分{OOO0O00OOOO0OO0O0},累计获得积分{O0OOOO0OO0O0OO0OO}')#line:96
        OOO00000OOO0O0OO0 .msg +=f'【{OOO00000OOO0O0OO0.un}】:今日签到{OOO00000OOO0O0OO0.today_sign}次,获得积分{OO00O00O0O0O000O0},现有积分{OOO0O00OOOO0OO0O0},累计获得积分{O0OOOO0OO0O0OO0OO}\n'#line:97
    def signin (OO0OO00O0OOO00O00 ):#line:99
        for O0OOO00OOOOOOOO0O in range (3 -int (OO0OO00O0OOO00O00 .today_sign )):#line:100
            OO0O0OOO0OO00O0O0 ='https://52.yyyy.run/api/sign/getSignAd'#line:101
            O0O00O0O0OO000O00 =OO0OO00O0OOO00O00 .s .post (OO0O0OOO0OO00O0O0 ).json ()#line:102
            OO0OO0O0OO000000O =O0O00O0O0OO000O00 .get ('data')['task_id']#line:103
            time .sleep (random .randint (16 ,18 ))#line:104
            OO0O0OOO0OO00O0O0 ='https://52.yyyy.run/api/sign/signTimeEnd'#line:105
            O0O000O0O0O0OOOO0 ={'task_id':OO0OO0O0OO000000O }#line:106
            O0O00O0O0OO000O00 =OO0OO00O0OOO00O00 .s .post (OO0O0OOO0OO00O0O0 ,data =O0O000O0O0O0OOOO0 ).json ()#line:107
            print (f'【{OO0OO00O0OOO00O00.un}】:第{O0OOO00OOOOOOOO0O + 1}次，{O0O00O0O0OO000O00.get("msg")}')#line:109
            time .sleep (1 )#line:110
    def get_info (OOOO0O000OO00OO00 ):#line:112
        O0OO000OOOO00OOO0 ='https://52.yyyy.run/api/user/index'#line:113
        OOO00OOOO0000OOO0 =OOOO0O000OO00OO00 .s .post (O0OO000OOOO00OOO0 ).json ()#line:114
        O00OO0OO0OOOO0OO0 =OOO00OOOO0000OOO0 .get ('data')#line:116
        OOOO0O000OO00OO00 .money =O00OO0OO0OOOO0OO0 .get ('money')#line:117
        OO00OOO00O000OOO0 =O00OO0OO0OOOO0OO0 .get ('all_money')#line:118
        OOOOOOO0OOO0O0O0O =O00OO0OO0OOOO0OO0 .get ('income_money')#line:119
        print (f'【{OOOO0O000OO00OO00.un}】:现有金币{OOOO0O000OO00OO00.money}，income_money {OOOOOOO0OOO0O0O0O},总共获得金币{OO00OOO00O000OOO0}')#line:120
        OOOO0O000OO00OO00 .msg +=f'【{OOOO0O000OO00OO00.un}】:现有金币{OOOO0O000OO00OO00.money}，income_money {OOOOOOO0OOO0O0O0O},总共获得金币{OO00OOO00O000OOO0}\n'#line:121
    def with_draw (O000O0O0OOO00OO0O ):#line:123
        if O000O0O0OOO00OO0O .money >=1 :#line:124
            O000O0O0OOO00OO0O .s .headers .update ({'Referer':'http://52.yyyy.run/pages/user/myWithdrawal.html','Origin':'http://52.yyyy.run',})#line:126
            O0OO00O000OO000O0 ='http://52.yyyy.run/api/user/postWith'#line:127
            OO0OOOO0OO0OO0O00 =int (O000O0O0OOO00OO0O .money )#line:128
            O0000OO00OOOOOO0O ={'num':OO0OOOO0OO0OO0O00 }#line:129
            OO0000OO0OO0OO000 =O000O0O0OOO00OO0O .s .post (O0OO00O000OO000O0 ,data =O0000OO00OOOOOO0O ).json ()#line:130
            print (f'【{O000O0O0OOO00OO0O.un}】:提现金额 {OO0OOOO0OO0OO0O00},提现结果 {OO0000OO0OO0OO000.get("msg")}')#line:131
            O000O0O0OOO00OO0O .msg +=f'【{O000O0O0OOO00OO0O.un}】:提现金额 {OO0OOOO0OO0OO0O00},提现结果 {OO0000OO0OO0OO000.get("msg")}\n'#line:132
        else :#line:133
            print (f'【{O000O0O0OOO00OO0O.un}】:提现 你的金币不多了')#line:134
            O000O0O0OOO00OO0O .msg +=f'【{O000O0O0OOO00OO0O.un}】:提现 你的金币不多了\n'#line:135
    def run (O0O0O00O0O000OO0O ):#line:137
        O0O0O00O0O000OO0O .get_signinfo ()#line:138
        if O0O0O00O0O000OO0O .today_sign <3 :#line:139
            O0O0O00O0O000OO0O .signin ()#line:140
        O0O0O00O0O000OO0O .get_info ()#line:141
        O0O0O00O0O000OO0O .with_draw ()#line:142
        return O0O0O00O0O000OO0O .msg #line:143
def cy_signin (O0000000OOO000000 ):#line:146
    O0000OOOO0O000O0O =CYLM (O0000000OOO000000 )#line:147
    return O0000OOOO0O000O0O .run ()#line:148
def load_notify ():#line:151
    global send #line:152
    try :#line:153
        from notify import send #line:154
        print ("加载通知服务成功！")#line:155
        return True #line:156
    except :#line:157
        print ('加载通知服务失败,请复制一份青龙notify.py到同级文件夹')#line:158
        return False #line:159
def get_info ():#line:162
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:164
    print ('入口\nhttps://52.yyyy.run//index/wechat/login/share_id/1904\n默认不推送通知，如需推送，将脚本开头的notify改为1，复制青龙的notify.py到脚本所在文件夹并设置好相关参数')#line:166
    O0O0OO00O00O000OO ='V0.1'#line:167
    O0OOOO0000O0O0O00 =_OOOOO0O00OOOO00OO ['version']['创娱联盟']#line:168
    print (f'当前版本{O0O0OO00O00O000OO}，仓库版本{O0OOOO0000O0O0O00}')#line:169
    if O0O0OO00O00O000OO <O0OOOO0000O0O0O00 :#line:170
        print ('请到仓库下载最新版本')#line:171
    print ("="*25 )#line:172
def main ():#line:175
    get_info()
    OOO0OO0OO0OOO0O00 =os .getenv ('cylmck')#line:176
    if not OOO0OO0OO0OOO0O00 :#line:177
        print (_OOOOO0O00OOOO00OO .get ('msg')['创娱联盟'])#line:178
        exit ()#line:179
    O000OO0O0OO0O0OO0 =OOO0OO0OO0OOO0O00 .replace ('&','\n').split ('\n')#line:180
    O0O0O0OOOOO0OOO00 =[]#line:181
    with multiprocessing .Pool (max_workers )as OOO0OOO0OOOOOO000 :#line:182
        for OOO0OO0OO0OOO0O00 in O000OO0O0OO0O0OO0 :#line:183
            O0O0O0OOOOO0OOO00 .append (OOO0OOO0OOOOOO000 .apply_async (cy_signin ,args =(OOO0OO0OO0OOO0O00 ,)).get ())#line:184
    OO00OO0000O000000 ='\n'.join (O0O0O0OOOOO0OOO00 )#line:185
    if notify :#line:186
        if load_notify ():#line:187
            send ('创娱联盟签到通知',OO00OO0000O000000 +f'\n本通知by：https://github.com/kxs2018/xiaoym\ntg讨论群：https://t.me/xizhiaigroup\n通知时间：{ftime()}')#line:189
if __name__ =='__main__':#line:192
    main ()#line:193
