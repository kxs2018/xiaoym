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
    O00OO0OO0O000O0OO ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:28
    O0O0000OO00000O0O =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O00OO0OO0O000O0OO ).json ()#line:29
    return O0O0000OO00000O0O #line:30
_O000O0O0O00OOOO00 =get_msg ()#line:33
def ftime ():#line:36
    O00OOO00OO0OO0O00 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:37
    return O00OOO00OO0OO0O00 #line:38
class HQCSH :#line:41
    def __init__ (OOOO0O0O0OO000O00 ,OOOO00O0O0OO000OO ):#line:42
        O0OO0O0O00O0O00OO =OOOO00O0O0OO000OO .split (';')#line:43
        if ''in O0OO0O0O00O0O00OO :#line:44
            O0OO0O0O00O0O00OO .pop ('')#line:45
        OOOO0O0O0OO000O00 .name =O0OO0O0O00O0O00OO [0 ].split ('=')[1 ]#line:46
        OOOO0O0O0OO000O00 .aid =O0OO0O0O00O0O00OO [1 ].split ('=')[1 ]#line:47
        OOOO0O0O0OO000O00 .headers ={'accountId':OOOO0O0O0OO000O00 .aid ,'tenantId':'619669306447261696','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/6763',}#line:50
        OOOO0O0O0OO000O00 .msg =''#line:51
        OOOO0O0O0OO000O00 .jf =None #line:52
    def sign (O00O0OOO0O00OOO00 ):#line:54
        O0O0O000O0O00OO0O =datetime .datetime .now ().time ()#line:55
        if datetime .time (7 )<=O0O0O000O0O00OO0O <datetime .time (23 ):#line:56
            OO00OOOO0OOOO0000 ="https://channel.cheryfs.cn/archer/activity-api/signinact/signin"#line:57
            OO00000000OOOOOOO ={'activityId':'620810406813786113'}#line:58
            O00O0OOO0O00OOO00 .headers .update (OO00000000OOOOOOO )#line:59
            OO000OOOO0O0OOO0O =requests .get (OO00OOOO0OOOO0000 ,headers =O00O0OOO0O00OOO00 .headers )#line:60
            if OO000OOOO0O0OOO0O .json ()['success']:#line:62
                if OO000OOOO0O0OOO0O .json ()['result']['success']:#line:63
                    print (f"【{O00O0OOO0O00OOO00.name}】：登录成功,签到成功")#line:64
                    O00O0OOO0O00OOO00 .msg =f"【{O00O0OOO0O00OOO00.name}】：登录成功,签到成功\n"#line:65
                print (f"【{O00O0OOO0O00OOO00.name}】：登录成功,{OO000OOOO0O0OOO0O.json()['result']['message']}")#line:66
                O00O0OOO0O00OOO00 .msg =f"【{O00O0OOO0O00OOO00.name}】：登录成功,{OO000OOOO0O0OOO0O.json()['result']['message']}\n"#line:67
                return True #line:68
            else :#line:69
                print (f"【{O00O0OOO0O00OOO00.name}】：登录失败,{OO000OOOO0O0OOO0O.json()['message']}")#line:70
                O00O0OOO0O00OOO00 .msg =f"【{O00O0OOO0O00OOO00.name}】：登录失败,{OO000OOOO0O0OOO0O.json()['message']}\n"#line:71
                return False #line:72
        else :#line:73
            print (f'【{O00O0OOO0O00OOO00.name}】:当前不再签到时间段')#line:74
            O00O0OOO0O00OOO00 .msg +=f'【{O00O0OOO0O00OOO00.name}】:当前不再签到时间段\n'#line:75
            return False #line:76
    def get_jf (OO0O00OOO00000O0O ):#line:78
        OOOOO000000000OOO ='https://channel.cheryfs.cn/archer/activity-api/common/accountPointLeft?pointId=620415610219683840'#line:79
        OO000O000O0O0O00O ={'activityId':'621911913692942337'}#line:80
        OO0O00OOO00000O0O .headers .update (OO000O000O0O0O00O )#line:81
        OOOO0O00O00O00000 =requests .get (OOOOO000000000OOO ,headers =OO0O00OOO00000O0O .headers ).json ()#line:82
        OO0O00OOO00000O0O .jf =OOOO0O00O00O00000 .get ('result')#line:83
        print (f'【{OO0O00OOO00000O0O.name}】:现有积分{OO0O00OOO00000O0O.jf}')#line:84
        OO0O00OOO00000O0O .msg +=f'【{OO0O00OOO00000O0O.name}】:现有积分{OO0O00OOO00000O0O.jf}\n'#line:85
    def qianghb (O00OOO0OO0O0O00OO ):#line:87
        O0OO0OOOO00O0O00O =f'https://channel.cheryfs.cn/archer/activity-api/pointsmall/exchangeCard?pointsMallCardId={q["id"]}&exchangeCount=1&mallOrderInputVoStr=%7B%22person%22:%22%22,%22phone%22:%22%22,%22province%22:%22%22,%22city%22:%22%22,%22area%22:%22%22,%22address%22:%22%22,%22remark%22:%22%22%7D&channel=1&exchangeType=0&exchangeNeedPoints=188&exchangeNeedMoney=0&cardGoodsItemIds='#line:88
        OO00OOOOO000OO000 ={'activityId':'621950054462152705'}#line:89
        O00OOO0OO0O0O00OO .headers .update (OO00OOOOO000OO000 )#line:90
        OOO0OO0OO00OOO000 =datetime .datetime .now ().time ()#line:91
        if datetime .time (18 )<=OOO0OO0OO00OOO000 <datetime .time (22 ):#line:92
            OO0OO000O00OOOOOO =0 #line:93
            while OO0OO000O00OOOOOO <5 :#line:94
                OO0OO000O00OOOOOO +=1 #line:95
                try :#line:96
                    OOOOO0O0O0O0000OO =requests .get (O0OO0OOOO00O0O00O ,headers =O00OOO0OO0O0O00OO .headers ).json ()#line:97
                    if not OOOOO0O0O0O0000OO .get ('result').get ('success'):#line:98
                        print (f"【{O00OOO0OO0O0O00OO.name}】:抢红包 {OOOOO0O0O0O0000OO.get('result').get('errMsg')}")#line:99
                        time .sleep (60 )#line:100
                        continue #line:101
                    else :#line:102
                        OO00OOOOO000OOOOO =O00OOO0OO0O0O00OO .jf #line:103
                        O00OOO0OO0O0O00OO .get_jf ()#line:104
                        if OO00OOOOO000OOOOO >O00OOO0OO0O0O00OO .jf :#line:105
                            print (f'【{O00OOO0OO0O0O00OO.name}】:抢到红包了，请前往个人中心-我的礼包查看')#line:106
                            O00OOO0OO0O0O00OO .msg +=f'【{O00OOO0OO0O0O00OO.name}】:抢到红包了，请前往个人中心-我的礼包查看\n'#line:107
                        break #line:108
                except :#line:109
                    print (f'【{O00OOO0OO0O0O00OO.name}】:抢红包 请求异常，正在重试')#line:110
                    time .sleep (60 )#line:111
                    continue #line:112
        else :#line:113
            print (f'【{O00OOO0OO0O0O00OO.name}】:当前不是抢红包的时间段')#line:114
            O00OOO0OO0O0O00OO .msg +=f'【{O00OOO0OO0O0O00OO.name}】:当前不是抢红包的时间段\n'#line:115
    def run (O0O0OOOOO0OOO0000 ):#line:117
        if O0O0OOOOO0OOO0000 .sign ():#line:118
            O0O0OOOOO0OOO0000 .get_jf ()#line:119
            if O0O0OOOOO0OOO0000 .jf >=q ['jf']:#line:120
                O0O0OOOOO0OOO0000 .qianghb ()#line:121
            else :#line:122
                print (f'【{O0O0OOOOO0OOO0000.name}】:积分不足以抢{q["money"]}元红包')#line:123
                O0O0OOOOO0OOO0000 .msg +=f'【{O0O0OOOOO0OOO0000.name}】:积分不足以抢{q["money"]}元红包\n'#line:124
        return O0O0OOOOO0OOO0000 .msg #line:125
def hq (O0OO0O0O00O000OOO ):#line:128
    O0OO00O0OO0OOO0OO =HQCSH (O0OO0O0O00O000OOO )#line:129
    return O0OO00O0OO0OOO0OO .run ()#line:130
def load_notify ():#line:133
    global send #line:134
    try :#line:135
        from notify import send #line:136
        print ("加载通知服务成功！")#line:137
        return True #line:138
    except :#line:139
        print ('加载通知服务失败,请复制一份青龙notify.py到同级文件夹')#line:140
        return False #line:141
def get_info ():#line:144
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:146
    print ('好奇车生活小程序签到+抢红包\n默认不推送通知，如需推送，将脚本开头的notify改为1，复制青龙的notify.py到脚本所在文件夹并设置好相关参数')#line:148
    O000O00000OO00O00 ='V1.0'#line:149
    O0O0OOOO00O00000O =_O000O0O0O00OOOO00 ['version']['好奇车生活']#line:150
    print (f'当前版本{O000O00000OO00O00}，仓库版本{O0O0OOOO00O00000O}')#line:151
    if O000O00000OO00O00 <O0O0OOOO00O00000O :#line:152
        print ('请到仓库下载最新版本')#line:153
    print(_O000O0O0O00OOOO00.get("update_log")['好奇车生活'])
    print ("="*25 )#line:154
def main ():#line:157
    get_info ()#line:158
    O000OO000OO0OO000 =os .getenv ('hqcshck')#line:160
    if not O000OO000OO0OO000 :#line:161
        print (_O000O0O0O00OOOO00 .get ('msg')['好奇车生活'])#line:162
        exit ()#line:163
    O0OOOOOO00OO0O0OO =O000OO000OO0OO000 .replace ('&','\n').split ('\n')#line:164
    OOOOO00O00OOO0000 =[]#line:165
    with multiprocessing .Pool ()as OO00O000O00OO0000 :#line:166
        for O0OO000O00OO0O000 in O0OOOOOO00OO0O0OO :#line:167
            OOOOO00O00OOO0000 .append (OO00O000O00OO0000 .apply_async (hq ,args =(O0OO000O00OO0O000 ,)).get ())#line:168
    O0OO00OO00O000OOO ='\n'.join (OOOOO00O00OOO0000 )#line:169
    if notify :#line:170
        if load_notify ():#line:171
            send ('好奇车生活签到通知',O0OO00OO00O000OOO +f'\n本通知by：https://github.com/kxs2018/xiaoym\ntg讨论群：https://t.me/xizhiaigroup\n通知时间：{ftime()}')#line:173
if __name__ =='__main__':#line:176
    main ()#line:177
