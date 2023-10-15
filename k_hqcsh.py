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
    O0OOO00O00O0O0000 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:28
    OO0O000O00O0O00O0 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O0OOO00O00O0O0000 ).json ()#line:29
    return OO0O000O00O0O00O0 #line:30
_OOOO0OO0O0O000OO0 =get_msg ()#line:33
def ftime ():#line:36
    O00OOO0OOO000OO0O =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:37
    return O00OOO0OOO000OO0O #line:38
class HQCSH :#line:41
    def __init__ (O0O000O00O0O0O0OO ,O0OOOO000OO00O0OO ):#line:42
        O0O00OOOOO0O000OO =O0OOOO000OO00O0OO .split (';')#line:43
        if ''in O0O00OOOOO0O000OO :#line:44
            O0O00OOOOO0O000OO .pop ('')#line:45
        O0O000O00O0O0O0OO .name =O0O00OOOOO0O000OO [0 ].split ('=')[1 ]#line:46
        O0O000O00O0O0O0OO .aid =O0O00OOOOO0O000OO [1 ].split ('=')[1 ]#line:47
        O0O000O00O0O0O0OO .headers ={'accountId':O0O000O00O0O0O0OO .aid ,'tenantId':'619669306447261696','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/6763',}#line:50
        O0O000O00O0O0O0OO .msg =''#line:51
        O0O000O00O0O0O0OO .jf =None #line:52
    def sign (OO00OOOOO0OO0OOOO ):#line:54
        O000O00OO0O0OO0OO =datetime .datetime .now ().time ()#line:55
        if datetime .time (7 )<=O000O00OO0O0OO0OO <datetime .time (23 ):#line:56
            OO00O0O00O0OO0OOO ="https://channel.cheryfs.cn/archer/activity-api/signinact/signin"#line:57
            OO000O00O0OO00O00 ={'activityId':'620810406813786113'}#line:58
            OO00OOOOO0OO0OOOO .headers .update (OO000O00O0OO00O00 )#line:59
            O000O0O00OO00OOOO =requests .get (OO00O0O00O0OO0OOO ,headers =OO00OOOOO0OO0OOOO .headers )#line:60
            if O000O0O00OO00OOOO .json ()['success']:#line:62
                if O000O0O00OO00OOOO .json ()['result']['success']:#line:63
                    print (f"【{OO00OOOOO0OO0OOOO.name}】：登录成功,签到成功")#line:64
                    OO00OOOOO0OO0OOOO .msg =f"【{OO00OOOOO0OO0OOOO.name}】：登录成功,签到成功\n"#line:65
                print (f"【{OO00OOOOO0OO0OOOO.name}】：登录成功,{O000O0O00OO00OOOO.json()['result']['message']}")#line:66
                OO00OOOOO0OO0OOOO .msg =f"【{OO00OOOOO0OO0OOOO.name}】：登录成功,{O000O0O00OO00OOOO.json()['result']['message']}\n"#line:67
                return True #line:68
            else :#line:69
                print (f"【{OO00OOOOO0OO0OOOO.name}】：登录失败,{O000O0O00OO00OOOO.json()['message']}")#line:70
                OO00OOOOO0OO0OOOO .msg =f"【{OO00OOOOO0OO0OOOO.name}】：登录失败,{O000O0O00OO00OOOO.json()['message']}\n"#line:71
                return False #line:72
        else :#line:73
            print (f'【{OO00OOOOO0OO0OOOO.name}】:当前不再签到时间段')#line:74
            OO00OOOOO0OO0OOOO .msg +=f'【{OO00OOOOO0OO0OOOO.name}】:当前不再签到时间段\n'#line:75
            return False #line:76
    def get_jf (OOOO00O0OO000OO00 ):#line:78
        O00000O0O00000O00 ='https://channel.cheryfs.cn/archer/activity-api/common/accountPointLeft?pointId=620415610219683840'#line:79
        OO000O0OOOOO0OOO0 ={'activityId':'621911913692942337'}#line:80
        OOOO00O0OO000OO00 .headers .update (OO000O0OOOOO0OOO0 )#line:81
        OOOO0O00000O0OOOO =requests .get (O00000O0O00000O00 ,headers =OOOO00O0OO000OO00 .headers ).json ()#line:82
        OOOO00O0OO000OO00 .jf =OOOO0O00000O0OOOO .get ('result')#line:83
        print (f'【{OOOO00O0OO000OO00.name}】:现有积分{OOOO00O0OO000OO00.jf}')#line:84
        OOOO00O0OO000OO00 .msg +=f'【{OOOO00O0OO000OO00.name}】:现有积分{OOOO00O0OO000OO00.jf}\n'#line:85
    def qianghb (O0O0O0000OO0O0OOO ):#line:87
        O0OO0OOOOOOO00O0O =f'https://channel.cheryfs.cn/archer/activity-api/pointsmall/exchangeCard?pointsMallCardId={q["id"]}&exchangeCount=1&mallOrderInputVoStr=%7B%22person%22:%22%22,%22phone%22:%22%22,%22province%22:%22%22,%22city%22:%22%22,%22area%22:%22%22,%22address%22:%22%22,%22remark%22:%22%22%7D&channel=1&exchangeType=0&exchangeNeedPoints=188&exchangeNeedMoney=0&cardGoodsItemIds='#line:88
        O0OO000O0000O00OO ={'activityId':'621950054462152705'}#line:89
        O0O0O0000OO0O0OOO .headers .update (O0OO000O0000O00OO )#line:90
        O0O0OOOOOO0O0000O =datetime .datetime .now ().time ()#line:91
        if datetime .time (18 )<=O0O0OOOOOO0O0000O <datetime .time (22 ):#line:92
            OO0O0O000O000000O =0 #line:93
            while OO0O0O000O000000O <5 :#line:94
                OO0O0O000O000000O +=1 #line:95
                try :#line:96
                    OO0O0OOO00OOOOOO0 =requests .get (O0OO0OOOOOOO00O0O ,headers =O0O0O0000OO0O0OOO .headers ).json ()#line:97
                    if not OO0O0OOO00OOOOOO0 .get ('result').get ('success'):#line:98
                        print (f"【{O0O0O0000OO0O0OOO.name}】:抢红包 {OO0O0OOO00OOOOOO0.get('result').get('errMsg')}")#line:99
                        time .sleep (60 )#line:100
                        continue #line:101
                    else :#line:102
                        O00000O00OOO00O00 =O0O0O0000OO0O0OOO .jf #line:103
                        O0O0O0000OO0O0OOO .get_jf ()#line:104
                        if O00000O00OOO00O00 >O0O0O0000OO0O0OOO .jf :#line:105
                            print (f'【{O0O0O0000OO0O0OOO.name}】:抢到红包了，请前往个人中心-我的礼包查看')#line:106
                            O0O0O0000OO0O0OOO .msg +=f'【{O0O0O0000OO0O0OOO.name}】:抢到红包了，请前往个人中心-我的礼包查看\n'#line:107
                        break #line:108
                except :#line:109
                    print (f'【{O0O0O0000OO0O0OOO.name}】:抢红包 请求异常，正在重试')#line:110
                    time .sleep (60 )#line:111
                    continue #line:112
        else :#line:113
            print (f'【{O0O0O0000OO0O0OOO.name}】:当前不是抢红包的时间段')#line:114
            O0O0O0000OO0O0OOO .msg +=f'【{O0O0O0000OO0O0OOO.name}】:当前不是抢红包的时间段\n'#line:115
    def run (O000OOOOOOO00OOO0 ):#line:117
        if O000OOOOOOO00OOO0 .sign ():#line:118
            O000OOOOOOO00OOO0 .get_jf ()#line:119
            if O000OOOOOOO00OOO0 .jf >=q ['jf']:#line:120
                O000OOOOOOO00OOO0 .qianghb ()#line:121
            else :#line:122
                print (f'【{O000OOOOOOO00OOO0.name}】:积分不足以抢{q["money"]}元红包')#line:123
                O000OOOOOOO00OOO0 .msg +=f'【{O000OOOOOOO00OOO0.name}】:积分不足以抢{q["money"]}元红包\n'#line:124
        return O000OOOOOOO00OOO0 .msg #line:125
def hq (OO0O00000OOOO0O00 ):#line:128
    O0OO00O0OOOO0O0OO =HQCSH (OO0O00000OOOO0O00 )#line:129
    return O0OO00O0OOOO0O0OO .run ()#line:130
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
    print (_OOOO0OO0O0O000OO0 .get ('msg')['好奇车生活'])#line:149
    OO000OO0000OOO000 ='V1.0'#line:150
    O00O00O0OO0OOOO00 =_OOOO0OO0O0O000OO0 ['version']['好奇车生活']#line:151
    print (f'当前版本{OO000OO0000OOO000}，仓库版本{O00O00O0OO0OOOO00}')#line:152
    if OO000OO0000OOO000 <O00O00O0OO0OOOO00 :#line:153
        print ('请到仓库下载最新版本')#line:154
    print (_OOOO0OO0O0O000OO0 .get ("update_log")['好奇车生活'])#line:155
    print ("="*25 )#line:156
def main ():#line:159
    get_info ()#line:160
    OO0OO0O00OOO00O00 =os .getenv ('hqcshck')#line:161
    if not OO0OO0O00OOO00O00 :#line:162
        print (_OOOO0OO0O0O000OO0 .get ('msg')['好奇车生活'])#line:163
        exit ()#line:164
    OO000O000O0O00OO0 =OO0OO0O00OOO00O00 .replace ('&','\n').split ('\n')#line:165
    print (f'共获取到{len(OO000O000O0O00OO0)}个账号')#line:166
    O00O000O00O0O00OO =[]#line:167
    with multiprocessing .Pool ()as O00OO000O0OOO0OOO :#line:168
        for O0O0OOO00OOO0O0O0 in OO000O000O0O00OO0 :#line:169
            O00O000O00O0O00OO .append (O00OO000O0OOO0OOO .apply_async (hq ,args =(O0O0OOO00OOO0O0O0 ,)).get ())#line:170
    O00OOOOO000O00000 ='\n'.join (O00O000O00O0O00OO )#line:171
    if notify :#line:172
        if load_notify ():#line:173
            send ('好奇车生活签到通知',O00OOOOO000O00000 +f'\n本通知by：https://github.com/kxs2018/xiaoym\ntg讨论群：https://t.me/xizhiaigroup\n通知时间：{ftime()}')#line:175
if __name__ =='__main__':#line:178
    main ()#line:179
