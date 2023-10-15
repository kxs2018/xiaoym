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
    O0000OO0O0O00000O ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:25
    O0OO0O00OO0O00OOO =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O0000OO0O0O00000O ).json ()#line:26
    return O0OO0O00OO0O00OOO #line:27
_OO000OO0OOOOOO000 =get_msg ()#line:30
def ftime ():#line:33
    OOO00OOO0OOOO0O0O =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:34
    return OOO00OOO0OOOO0O0O #line:35
class CYLM :#line:38
    def __init__ (O0000OO00OO000OO0 ,OO0000OO0000O0O0O ):#line:39
        O0000OO00OO000OO0 .account =OO0000OO0000O0O0O .split ('#')[0 ]#line:40
        O0000OO00OO000OO0 .un =O0000OO00OO000OO0 .account [:3 ]+'*'+O0000OO00OO000OO0 .account [-4 :]#line:41
        O0000OO00OO000OO0 .password =OO0000OO0000O0O0O .split ('#')[1 ]#line:42
        O0000OO00OO000OO0 .s =requests .session ()#line:43
        O0000OO00OO000OO0 .s .headers ={'os':'android','Content-Type':'application/x-www-form-urlencoded',}#line:44
        O0000OO00OO000OO0 .msg =''#line:45
    def get_token (O000O0OO000000O00 ):#line:47
        try :#line:48
            with open ('cylm.json','r',encoding ='utf-8')as OO0O0OOO0OO000OOO :#line:49
                O00OO000OOO0O000O =json .loads (OO0O0OOO0OO000OOO .read ())#line:50
        except :#line:51
            O00OO000OOO0O000O ={}#line:52
        O0000O00O0OO000O0 =O00OO000OOO0O000O .get (O000O0OO000000O00 .account )#line:53
        if not O0000O00O0OO000O0 :#line:54
            print (f'【{O000O0OO000000O00.un}】:没有从本地获取到token，正在登录')#line:55
            O0000O00O0OO000O0 =O000O0OO000000O00 .login ()#line:56
            O00OO000OOO0O000O .update ({O000O0OO000000O00 .account :O0000O00O0OO000O0 })#line:57
            with open ('cylm.json','w',encoding ='utf-8')as OO0O0OOO0OO000OOO :#line:58
                OO0O0OOO0OO000OOO .write (json .dumps (O00OO000OOO0O000O ))#line:59
        return O0000O00O0OO000O0 #line:60
    def login (OO0OOO00O000O0O0O ):#line:62
        O0O0OOOO0O0O000OO ='https://52.yyyy.run/api/user/login'#line:63
        O0000O0O00O000000 =f'account={OO0OOO00O000O0O0O.account}&password={OO0OOO00O000O0O0O.password}'#line:64
        OOOO0000OOO0OO0O0 =OO0OOO00O000O0O0O .s .post (O0O0OOOO0O0O000OO ,data =O0000O0O00O000000 ).json ()#line:65
        if OOOO0000OOO0OO0O0 .get ('code')==1 :#line:67
            O000000O00O00OOOO =OOOO0000OOO0OO0O0 .get ('data')['userinfo']['token']#line:68
            OOO00O0O0OO0O000O =OOOO0000OOO0OO0O0 .get ('data')['userinfo']['nickname']#line:69
            print (f'【{OO0OOO00O000O0O0O.un}】:{OOO00O0O0OO0O000O},{OOOO0000OOO0OO0O0.get("msg")}')#line:70
            OO0OOO00O000O0O0O .msg +=f'【{OO0OOO00O000O0O0O.un}】:{OOO00O0O0OO0O000O},{OOOO0000OOO0OO0O0.get("msg")}\n'#line:71
            return O000000O00O00OOOO #line:72
        else :#line:73
            print (f'【{OO0OOO00O000O0O0O.un}】:{OOOO0000OOO0OO0O0.get("msg")}')#line:74
            OO0OOO00O000O0O0O .msg +=f'【{OO0OOO00O000O0O0O.un}】:{OOOO0000OOO0OO0O0.get("msg")}\n'#line:75
            print (f'【{OO0OOO00O000O0O0O.un}】:请检查账号密码是否填写错误')#line:76
            return False #line:77
    def get_signinfo (OOO00000O00OO00OO ):#line:79
        O0O0O00OOOO00O00O =OOO00000O00OO00OO .get_token ()#line:80
        O0OOOO000OO0O000O ='https://52.yyyy.run/api/sign/userSignData'#line:81
        OOO00000O00OO00OO .s .headers .update ({'token':O0O0O00OOOO00O00O })#line:82
        O0OOOO000OO0O0O0O =OOO00000O00OO00OO .s .post (O0OOOO000OO0O000O ).json ()#line:83
        if O0OOOO000OO0O0O0O .get ('code')!=1 :#line:85
            print (f'【{OOO00000O00OO00OO.un}】：token失效，正在重新获取')#line:86
            O0O0O00OOOO00O00O =OOO00000O00OO00OO .login ()#line:87
            OOO00000O00OO00OO .s .headers .update ({'token':O0O0O00OOOO00O00O })#line:88
            O0OOOO000OO0O0O0O =OOO00000O00OO00OO .s .post (O0OOOO000OO0O000O ).json ()#line:89
        O0O0O0O0O0O0O000O =O0OOOO000OO0O0O0O .get ('data')#line:90
        '''"coin":0.8,"all_coin":0.8,"today_coin":0.8,"yesterday_coin":0,"today_sign":2,"agent_coin":0,"score_text":"积分"'''#line:91
        OOO0000O0OOOOOO0O =O0O0O0O0O0O0O000O .get ('coin')#line:92
        OOO00000O00OO00OO .today_sign =O0O0O0O0O0O0O000O .get ('today_sign')#line:93
        OO0O0O0O00O000O0O =O0O0O0O0O0O0O000O .get ('today_coin')#line:94
        O0OOO00O00O00O0OO =O0O0O0O0O0O0O000O .get ('all_coin')#line:95
        print (f'【{OOO00000O00OO00OO.un}】:今日签到{OOO00000O00OO00OO.today_sign}次,获得积分{OO0O0O0O00O000O0O},现有积分{OOO0000O0OOOOOO0O},累计获得积分{O0OOO00O00O00O0OO}')#line:96
        OOO00000O00OO00OO .msg +=f'【{OOO00000O00OO00OO.un}】:今日签到{OOO00000O00OO00OO.today_sign}次,获得积分{OO0O0O0O00O000O0O},现有积分{OOO0000O0OOOOOO0O},累计获得积分{O0OOO00O00O00O0OO}\n'#line:97
    def signin (O0O000000OOOOOO0O ):#line:99
        for OOOO0OOO0O00000OO in range (3 -int (O0O000000OOOOOO0O .today_sign )):#line:100
            O0OOO0OOO00OO0OOO ='https://52.yyyy.run/api/sign/getSignAd'#line:101
            O00O00000000OO0O0 =O0O000000OOOOOO0O .s .post (O0OOO0OOO00OO0OOO ).json ()#line:102
            O00000O0OOOOO0O0O =O00O00000000OO0O0 .get ('data')['task_id']#line:103
            time .sleep (random .randint (16 ,18 ))#line:104
            O0OOO0OOO00OO0OOO ='https://52.yyyy.run/api/sign/signTimeEnd'#line:105
            O0O0O0O00O00OO00O ={'task_id':O00000O0OOOOO0O0O }#line:106
            O00O00000000OO0O0 =O0O000000OOOOOO0O .s .post (O0OOO0OOO00OO0OOO ,data =O0O0O0O00O00OO00O ).json ()#line:107
            print (f'【{O0O000000OOOOOO0O.un}】:第{OOOO0OOO0O00000OO + 1}次，{O00O00000000OO0O0.get("msg")}')#line:109
            time .sleep (1 )#line:110
    def get_info (OO000OOOOO0OO0OO0 ):#line:112
        OO00000OO0O0O000O ='https://52.yyyy.run/api/user/index'#line:113
        O000OOOO000O0O0OO =OO000OOOOO0OO0OO0 .s .post (OO00000OO0O0O000O ).json ()#line:114
        OO0O0OO0OO00OO000 =O000OOOO000O0O0OO .get ('data')#line:116
        OO000OOOOO0OO0OO0 .money =OO0O0OO0OO00OO000 .get ('money')#line:117
        O0OOO0OO000O0O00O =OO0O0OO0OO00OO000 .get ('all_money')#line:118
        OO0OOOOOOOO00OO0O =OO0O0OO0OO00OO000 .get ('income_money')#line:119
        print (f'【{OO000OOOOO0OO0OO0.un}】:现有金币{OO000OOOOO0OO0OO0.money}，income_money {OO0OOOOOOOO00OO0O},总共获得金币{O0OOO0OO000O0O00O}')#line:120
        OO000OOOOO0OO0OO0 .msg +=f'【{OO000OOOOO0OO0OO0.un}】:现有金币{OO000OOOOO0OO0OO0.money}，income_money {OO0OOOOOOOO00OO0O},总共获得金币{O0OOO0OO000O0O00O}\n'#line:121
    def with_draw (OOOO00OOOOOOOO0O0 ):#line:123
        if OOOO00OOOOOOOO0O0 .money >=1 :#line:124
            OOOO00OOOOOOOO0O0 .s .headers .update ({'Referer':'http://52.yyyy.run/pages/user/myWithdrawal.html','Origin':'http://52.yyyy.run',})#line:126
            OOOO0OO0000O00O0O ='http://52.yyyy.run/api/user/postWith'#line:127
            OO00O0O0OOOO0OOOO =int (OOOO00OOOOOOOO0O0 .money )#line:128
            O00OO00OOO0O00OO0 ={'num':OO00O0O0OOOO0OOOO }#line:129
            O0OO00O0O00OOO0O0 =OOOO00OOOOOOOO0O0 .s .post (OOOO0OO0000O00O0O ,data =O00OO00OOO0O00OO0 ).json ()#line:130
            print (f'【{OOOO00OOOOOOOO0O0.un}】:提现金额 {OO00O0O0OOOO0OOOO},提现结果 {O0OO00O0O00OOO0O0.get("msg")}')#line:131
            OOOO00OOOOOOOO0O0 .msg +=f'【{OOOO00OOOOOOOO0O0.un}】:提现金额 {OO00O0O0OOOO0OOOO},提现结果 {O0OO00O0O00OOO0O0.get("msg")}\n'#line:132
        else :#line:133
            print (f'【{OOOO00OOOOOOOO0O0.un}】:提现 你的金币不多了')#line:134
            OOOO00OOOOOOOO0O0 .msg +=f'【{OOOO00OOOOOOOO0O0.un}】:提现 你的金币不多了\n'#line:135
    def run (OO0OO0O0000OOOO00 ):#line:137
        OO0OO0O0000OOOO00 .get_signinfo ()#line:138
        if OO0OO0O0000OOOO00 .today_sign <3 :#line:139
            OO0OO0O0000OOOO00 .signin ()#line:140
        OO0OO0O0000OOOO00 .get_info ()#line:141
        OO0OO0O0000OOOO00 .with_draw ()#line:142
        return OO0OO0O0000OOOO00 .msg #line:143
def cy_signin (O00OO0OOO0000OOO0 ):#line:146
    O00OO000O0O00O00O =CYLM (O00OO0OOO0000OOO0 )#line:147
    return O00OO000O0O00O00O .run ()#line:148
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
    OO0OO0OO0O00OOOO0 ='V0.1'#line:167
    O00000O0O0O0OOO00 =_OO000OO0OOOOOO000 ['version']['创娱联盟']#line:168
    print (f'当前版本{OO0OO0OO0O00OOOO0}，仓库版本{O00000O0O0O0OOO00}')#line:169
    if OO0OO0OO0O00OOOO0 <O00000O0O0O0OOO00 :#line:170
        print ('请到仓库下载最新版本')#line:171
    print ("="*25 )#line:172
def main ():#line:175
    OOOOOOOOOO0OO00O0 =os .getenv ('cylmck')#line:176
    O00OO000O0O0O0O0O =OOOOOOOOOO0OO00O0 .replace ('&','\n').split ('\n')#line:177
    O0O0O000O00O0OO0O =[]#line:178
    with multiprocessing .Pool (max_workers )as O00O0OOO00O0OOOO0 :#line:179
        for OOOOOOOOOO0OO00O0 in O00OO000O0O0O0O0O :#line:180
            O0O0O000O00O0OO0O .append (O00O0OOO00O0OOOO0 .apply_async (cy_signin ,args =(OOOOOOOOOO0OO00O0 ,)).get ())#line:181
    OO0O0O00O0O00O0OO ='\n'.join (O0O0O000O00O0OO0O )#line:182
    if notify :#line:183
        if load_notify ():#line:184
            send ('创娱联盟签到通知',OO0O0O00O0O00O0OO +f'\n本通知by：https://github.com/kxs2018/xiaoym\ntg讨论群：https://t.me/xizhiaigroup\n通知时间：{ftime()}')#line:186
if __name__ =='__main__':#line:189
    main ()#line:190

