# -*- coding: utf-8 -*-
# k_hqcsh
"""
先运行脚本，有问题再到群里问
new Env('好奇车生活');
"""
"""通知开关"""
notify = 0
"""1为开，0为关，打开后需复制青龙的notify.py到同级文件夹"""

q1 = {'id': '647894196522340352', 'jf': 188, 'money': 1.08}  # 188积分 1.08元
q2 = {'id': '622187839353806848', 'jf': 288, 'money': 1.88}  # 288积分 1.88元
q3 = {'id': '622187928306601984', 'jf': 588, 'money': 3.88}  # 588积分 3.88元
q4 = {'id': '622188100122075136', 'jf': 888, 'money': 5.88}  # 888积分 5.88元
"""抢红包设置"""
q = q1
""""""
import os  # line:19
import requests  # line:20
import time  # line:21
import datetime  # line:22
import multiprocessing  # line:23


def get_msg ():#line:26
    OOOO00O0O0000O00O ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:28
    OOOOOOO00OOO00OOO =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OOOO00O0O0000O00O ).json ()#line:29
    return OOOOOOO00OOO00OOO #line:30
_OO0OOOOO00000O00O =get_msg ()#line:33
def ftime ():#line:36
    O000O000OO0O000OO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:37
    return O000O000OO0O000OO #line:38
class HQCSH :#line:41
    def __init__ (OO0O00OO0OO0OOO0O ,OOO00O00O0O0O0OOO ):#line:42
        OOO0OO0000OOO0O0O =OOO00O00O0O0O0OOO .split (';')#line:43
        if ''in OOO0OO0000OOO0O0O :#line:44
            OOO0OO0000OOO0O0O .pop ('')#line:45
        OO0O00OO0OO0OOO0O .name =OOO0OO0000OOO0O0O [0 ].split ('=')[1 ]#line:46
        OO0O00OO0OO0OOO0O .aid =OOO0OO0000OOO0O0O [1 ].split ('=')[1 ]#line:47
        OO0O00OO0OO0OOO0O .headers ={'accountId':OO0O00OO0OO0OOO0O .aid ,'tenantId':'619669306447261696','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/6763',}#line:50
        OO0O00OO0OO0OOO0O .msg =''#line:51
        OO0O00OO0OO0OOO0O .jf =None #line:52
    def sign (O0OOO0O00O0O000OO ):#line:54
        O000000OO0O000O00 =datetime .datetime .now ().time ()#line:55
        if datetime .time (7 )<=O000000OO0O000O00 <datetime .time (23 ):#line:56
            OO0000000O0O0O000 ="https://channel.cheryfs.cn/archer/activity-api/signinact/signin"#line:57
            OOO0OOOOOOOOO0000 ={'activityId':'620810406813786113'}#line:58
            O0OOO0O00O0O000OO .headers .update (OOO0OOOOOOOOO0000 )#line:59
            OO00O0OOOOOO0OO0O =requests .get (OO0000000O0O0O000 ,headers =O0OOO0O00O0O000OO .headers )#line:60
            if OO00O0OOOOOO0OO0O .json ()['success']:#line:62
                if OO00O0OOOOOO0OO0O .json ()['result']['success']:#line:63
                    print (f"【{O0OOO0O00O0O000OO.name}】：登录成功,签到成功")#line:64
                    O0OOO0O00O0O000OO .msg =f"【{O0OOO0O00O0O000OO.name}】：登录成功,签到成功\n"#line:65
                print (f"【{O0OOO0O00O0O000OO.name}】：登录成功,{OO00O0OOOOOO0OO0O.json()['result']['message']}")#line:66
                O0OOO0O00O0O000OO .msg =f"【{O0OOO0O00O0O000OO.name}】：登录成功,{OO00O0OOOOOO0OO0O.json()['result']['message']}\n"#line:67
                return True #line:68
            else :#line:69
                O0OOO0O00O0O000OO .msg =f"【{O0OOO0O00O0O000OO.name}】：登录失败,{OO00O0OOOOOO0OO0O.json()['message']}\n"#line:70
                return False #line:71
        else :#line:72
            print (f'【{O0OOO0O00O0O000OO.name}】:当前不再签到时间段')#line:73
            O0OOO0O00O0O000OO .msg +=f'【{O0OOO0O00O0O000OO.name}】:当前不再签到时间段\n'#line:74
            return False #line:75
    def get_jf (OO0OOOO000O0OO000 ):#line:77
        O0OOO00O0O0O00O0O ='https://channel.cheryfs.cn/archer/activity-api/common/accountPointLeft?pointId=620415610219683840'#line:78
        O000O0O0O0O0OOO00 ={'activityId':'621911913692942337'}#line:79
        OO0OOOO000O0OO000 .headers .update (O000O0O0O0O0OOO00 )#line:80
        O0O0OOOO0OOO0O000 =requests .get (O0OOO00O0O0O00O0O ,headers =OO0OOOO000O0OO000 .headers ).json ()#line:81
        OO0OOOO000O0OO000 .jf =O0O0OOOO0OOO0O000 .get ('result')#line:82
        print (f'【{OO0OOOO000O0OO000.name}】:现有积分{OO0OOOO000O0OO000.jf}')#line:83
        OO0OOOO000O0OO000 .msg +=f'【{OO0OOOO000O0OO000.name}】:现有积分{OO0OOOO000O0OO000.jf}\n'#line:84
    def qianghb (OO0OOOO0OO0000OO0 ):#line:86
        OO0OOOOOO0000O0O0 =f'https://channel.cheryfs.cn/archer/activity-api/pointsmall/exchangeCard?pointsMallCardId={q["id"]}&exchangeCount=1&mallOrderInputVoStr=%7B%22person%22:%22%22,%22phone%22:%22%22,%22province%22:%22%22,%22city%22:%22%22,%22area%22:%22%22,%22address%22:%22%22,%22remark%22:%22%22%7D&channel=1&exchangeType=0&exchangeNeedPoints=188&exchangeNeedMoney=0&cardGoodsItemIds='#line:87
        O00OOOOOO0O00O00O ={'activityId':'621950054462152705'}#line:88
        OO0OOOO0OO0000OO0 .headers .update (O00OOOOOO0O00O00O )#line:89
        O0OO00OO00O0O0O0O =datetime .datetime .now ().time ()#line:90
        if datetime .time (18 )<=O0OO00OO00O0O0O0O <datetime .time (22 ):#line:91
            OOO0O0O0000000O00 =0 #line:92
            while OOO0O0O0000000O00 <5 :#line:93
                OOO0O0O0000000O00 +=1 #line:94
                try :#line:95
                    O0OOOO00O00O0OO00 =requests .get (OO0OOOOOO0000O0O0 ,headers =OO0OOOO0OO0000OO0 .headers ).json ()#line:96
                    if not O0OOOO00O00O0OO00 .get ('result').get ('success'):#line:97
                        print (f"【{OO0OOOO0OO0000OO0.name}】:抢红包 {O0OOOO00O00O0OO00.get('result').get('errMsg')}")#line:98
                        time .sleep (60 )#line:99
                        continue #line:100
                    else :#line:101
                        OOO0O0OO00O00O00O =OO0OOOO0OO0000OO0 .jf #line:102
                        OO0OOOO0OO0000OO0 .get_jf ()#line:103
                        if OOO0O0OO00O00O00O >OO0OOOO0OO0000OO0 .jf :#line:104
                            print (f'【{OO0OOOO0OO0000OO0.name}】:抢到红包了，请前往个人中心-我的礼包查看')#line:105
                            OO0OOOO0OO0000OO0 .msg +=f'【{OO0OOOO0OO0000OO0.name}】:抢到红包了，请前往个人中心-我的礼包查看\n'#line:106
                        break #line:107
                except :#line:108
                    print (f'【{OO0OOOO0OO0000OO0.name}】:抢红包 请求异常，正在重试')#line:109
                    time .sleep (60 )#line:110
                    continue #line:111
        else :#line:112
            print (f'【{OO0OOOO0OO0000OO0.name}】:当前不是抢红包的时间段')#line:113
            OO0OOOO0OO0000OO0 .msg +=f'【{OO0OOOO0OO0000OO0.name}】:当前不是抢红包的时间段\n'#line:114
    def run (O0OO00000OOOO0O00 ):#line:116
        if O0OO00000OOOO0O00 .sign ():#line:117
            O0OO00000OOOO0O00 .get_jf ()#line:118
            if O0OO00000OOOO0O00 .jf >=q ['jf']:#line:119
                O0OO00000OOOO0O00 .qianghb ()#line:120
            else :#line:121
                print (f'【{O0OO00000OOOO0O00.name}】:积分不足以抢{q["money"]}元红包')#line:122
                O0OO00000OOOO0O00 .msg +=f'【{O0OO00000OOOO0O00.name}】:积分不足以抢{q["money"]}元红包\n'#line:123
        return O0OO00000OOOO0O00 .msg #line:124
def hq (OOO000O0OOOO0O0OO ):#line:127
    OO0O0O0OOOOO00OOO =HQCSH (OOO000O0OOOO0O0OO )#line:128
    return OO0O0O0OOOOO00OOO .run ()#line:129
def load_notify ():#line:132
    global send #line:133
    try :#line:134
        from notify import send #line:135
        print ("加载通知服务成功！")#line:136
        return True #line:137
    except :#line:138
        print ('加载通知服务失败,请复制一份青龙notify.py到同级文件夹')#line:139
        return False #line:140
def get_info ():#line:143
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:145
    print ('好奇车生活小程序签到+抢红包\n默认不推送通知，如需推送，将脚本开头的notify改为1，复制青龙的notify.py到脚本所在文件夹并设置好相关参数')#line:147
    OO00O00O000OO000O ='V1.0'#line:148
    OOOO0OOOO00O00000 =_OO0OOOOO00000O00O ['version']['好奇车生活']#line:149
    print (f'当前版本{OO00O00O000OO000O}，仓库版本{OOOO0OOOO00O00000}')#line:150
    if OO00O00O000OO000O <OOOO0OOOO00O00000 :#line:151
        print ('请到仓库下载最新版本')#line:152
    print ("="*25 )#line:153
def main ():#line:156
    get_info ()#line:157
    print (_OO0OOOOO00000O00O .get ("update_log")['好奇车生活'])#line:158
    OO000OO0O0O000000 =os .getenv ('hqcshck')#line:159
    if not OO000OO0O0O000000 :#line:160
        print (_OO0OOOOO00000O00O .get ('msg')['好奇车生活'])#line:161
        exit ()#line:162
    OOOOO000OO0O0OOO0 =OO000OO0O0O000000 .replace ('&','\n').split ('\n')#line:163
    O0O00O0O0O000OO00 =[]#line:164
    with multiprocessing .Pool ()as OO00000000O00OO00 :#line:165
        for OOO0O000OO0O0O00O in OOOOO000OO0O0OOO0 :#line:166
            O0O00O0O0O000OO00 .append (OO00000000O00OO00 .apply_async (hq ,args =(OOO0O000OO0O0O00O ,)).get ())#line:167
    O00OOO00OOO0OO00O ='\n'.join (O0O00O0O0O000OO00 )#line:168
    if notify :#line:169
        if load_notify ():#line:170
            send ('好奇车生活签到通知',O00OOO00OOO0OO00O +f'\n本通知by：https://github.com/kxs2018/xiaoym\ntg讨论群：https://t.me/xizhiaigroup\n通知时间：{ftime()}')#line:172
if __name__ =='__main__':#line:175
    main ()#line:176
