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


def get_msg ():#line:24
    OOO0OOOOOOOOOOO0O ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:26
    O000000OOO0OO0O0O =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OOO0OOOOOOOOOOO0O ).json ()#line:27
    return O000000OOO0OO0O0O #line:28
_O0000OO0O0OO0000O =get_msg ()#line:31
def ftime ():#line:34
    O0O00OOOOOOOO00OO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:35
    return O0O00OOOOOOOO00OO #line:36
class HQCSH :#line:39
    def __init__ (O00O00O000O0OOOO0 ,O0O0OOO00O0000OO0 ):#line:40
        OOOOO0O0O0O00000O =O0O0OOO00O0000OO0 .split (';')#line:41
        if ''in OOOOO0O0O0O00000O :#line:42
            OOOOO0O0O0O00000O .pop ('')#line:43
        O00O00O000O0OOOO0 .name =OOOOO0O0O0O00000O [0 ].split ('=')[1 ]#line:44
        O00O00O000O0OOOO0 .aid =OOOOO0O0O0O00000O [1 ].split ('=')[1 ]#line:45
        O00O00O000O0OOOO0 .headers ={'accountId':O00O00O000O0OOOO0 .aid ,'tenantId':'619669306447261696','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/6763',}#line:48
        O00O00O000O0OOOO0 .msg =''#line:49
        O00O00O000O0OOOO0 .jf =None #line:50
    def sign (O0O0O000OO0OOOO00 ):#line:52
        OO00000OO0O0O0000 =datetime .datetime .now ().time ()#line:53
        if datetime .time (7 )<=OO00000OO0O0O0000 <datetime .time (23 ):#line:54
            OO0O0O0O0O0O0OOOO ="https://channel.cheryfs.cn/archer/activity-api/signinact/signin"#line:55
            O0OOOOO0OO000OOOO ={'activityId':'620810406813786113'}#line:56
            O0O0O000OO0OOOO00 .headers .update (O0OOOOO0OO000OOOO )#line:57
            OOO00OO00OO0OO0O0 =requests .get (OO0O0O0O0O0O0OOOO ,headers =O0O0O000OO0OOOO00 .headers )#line:58
            if OOO00OO00OO0OO0O0 .json ()['success']:#line:60
                if OOO00OO00OO0OO0O0 .json ()['result']['success']:#line:61
                    print (f"【{O0O0O000OO0OOOO00.name}】：登录成功,签到成功")#line:62
                    O0O0O000OO0OOOO00 .msg =f"【{O0O0O000OO0OOOO00.name}】：登录成功,签到成功\n"#line:63
                print (f"【{O0O0O000OO0OOOO00.name}】：登录成功,{OOO00OO00OO0OO0O0.json()['result']['message']}")#line:64
                O0O0O000OO0OOOO00 .msg =f"【{O0O0O000OO0OOOO00.name}】：登录成功,{OOO00OO00OO0OO0O0.json()['result']['message']}\n"#line:65
                return True #line:66
            else :#line:67
                print (f"【{O0O0O000OO0OOOO00.name}】：登录失败,{OOO00OO00OO0OO0O0.json()['message']}")#line:68
                O0O0O000OO0OOOO00 .msg =f"【{O0O0O000OO0OOOO00.name}】：登录失败,{OOO00OO00OO0OO0O0.json()['message']}\n"#line:69
                return False #line:70
        else :#line:71
            print (f'【{O0O0O000OO0OOOO00.name}】:当前不再签到时间段')#line:72
            O0O0O000OO0OOOO00 .msg +=f'【{O0O0O000OO0OOOO00.name}】:当前不再签到时间段\n'#line:73
            return False #line:74
    def get_jf (O0000OO0OO0OO00O0 ):#line:76
        OOOOOO00O0O0OOOO0 ='https://channel.cheryfs.cn/archer/activity-api/common/accountPointLeft?pointId=620415610219683840'#line:77
        OO0O00O00OO00O0OO ={'activityId':'621911913692942337'}#line:78
        O0000OO0OO0OO00O0 .headers .update (OO0O00O00OO00O0OO )#line:79
        O0000OO0OO00O0OOO =requests .get (OOOOOO00O0O0OOOO0 ,headers =O0000OO0OO0OO00O0 .headers ).json ()#line:80
        O0000OO0OO0OO00O0 .jf =O0000OO0OO00O0OOO .get ('result')#line:81
        print (f'【{O0000OO0OO0OO00O0.name}】:现有积分{O0000OO0OO0OO00O0.jf}')#line:82
        O0000OO0OO0OO00O0 .msg +=f'【{O0000OO0OO0OO00O0.name}】:现有积分{O0000OO0OO0OO00O0.jf}\n'#line:83
    def qianghb (O0OO000OOOOO00O0O ):#line:85
        O0OOO0000OO0OO0O0 =f'https://channel.cheryfs.cn/archer/activity-api/pointsmall/exchangeCard?pointsMallCardId={q["id"]}&exchangeCount=1&mallOrderInputVoStr=%7B%22person%22:%22%22,%22phone%22:%22%22,%22province%22:%22%22,%22city%22:%22%22,%22area%22:%22%22,%22address%22:%22%22,%22remark%22:%22%22%7D&channel=1&exchangeType=0&exchangeNeedPoints=188&exchangeNeedMoney=0&cardGoodsItemIds='#line:86
        O0O0000OOO000OO0O ={'activityId':'621950054462152705'}#line:87
        OOO000OOO00OO0000 =datetime .datetime .now ().time ()#line:88
        if datetime .time (18 )<=OOO000OOO00OO0000 <datetime .time (22 ):#line:89
            OOOO00O0OOO00O0OO =0 #line:90
            while OOOO00O0OOO00O0OO <5 :#line:91
                O0OO000OOOOO00O0O .headers .update (O0O0000OOO000OO0O )#line:92
                OOOO00O0OOO00O0OO +=1 #line:93
                try :#line:94
                    OOO0O0OO0O0O000O0 =requests .get (O0OOO0000OO0OO0O0 ,headers =O0OO000OOOOO00O0O .headers ).json ()#line:95
                    if not OOO0O0OO0O0O000O0 .get ('result').get ('success'):#line:96
                        print (f"【{O0OO000OOOOO00O0O.name}】:抢红包 {OOO0O0OO0O0O000O0.get('result').get('errMsg')}")#line:97
                        time .sleep (60 )#line:98
                        continue #line:99
                    else :#line:100
                        OO00OO0OO0OOOO0OO =O0OO000OOOOO00O0O .jf #line:101
                        print (f"【{O0OO000OOOOO00O0O.name}】:抢红包 {OOO0O0OO0O0O000O0.get('result').get('errMsg')}")#line:102
                        O0OO000OOOOO00O0O .get_jf ()#line:103
                        if OO00OO0OO0OOOO0OO >O0OO000OOOOO00O0O .jf :#line:104
                            print (f'【{O0OO000OOOOO00O0O.name}】:抢到红包了，请前往个人中心-我的礼包查看')#line:105
                            O0OO000OOOOO00O0O .msg +=f'【{O0OO000OOOOO00O0O.name}】:抢到红包了，请前往个人中心-我的礼包查看\n'#line:106
                            break #line:107
                        else :#line:108
                            time .sleep (60 )#line:109
                            continue #line:110
                except :#line:111
                    print (f'【{O0OO000OOOOO00O0O.name}】:抢红包 请求异常，正在重试')#line:112
                    time .sleep (60 )#line:113
                    continue #line:114
        else :#line:115
            print (f'【{O0OO000OOOOO00O0O.name}】:当前不是抢红包的时间段')#line:116
            O0OO000OOOOO00O0O .msg +=f'【{O0OO000OOOOO00O0O.name}】:当前不是抢红包的时间段\n'#line:117
    def run (O0O00OOO000O00O00 ):#line:119
        if O0O00OOO000O00O00 .sign ():#line:120
            O0O00OOO000O00O00 .get_jf ()#line:121
            if O0O00OOO000O00O00 .jf >=188 :#line:122
                O0O00OOO000O00O00 .qianghb ()#line:123
            else :#line:124
                print (f'【{O0O00OOO000O00O00.name}】:积分不足以抢红包')#line:125
                O0O00OOO000O00O00 .msg +=f'【{O0O00OOO000O00O00.name}】:积分不足以抢红包\n'#line:126
        return O0O00OOO000O00O00 .msg #line:127
def hq (OO0O000OOO0OOOOOO ):#line:130
    OOO000000O00OOO00 =HQCSH (OO0O000OOO0OOOOOO )#line:131
    return OOO000000O00OOO00 .run ()#line:132
def load_notify ():#line:135
    global send #line:136
    try :#line:137
        from notify import send #line:138
        print ("加载通知服务成功！")#line:139
        return True #line:140
    except :#line:141
        print ('加载通知服务失败,请复制一份青龙notify.py到同级文件夹')#line:142
        return False #line:143
def get_info ():#line:146
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:148
    print ('好奇车生活小程序签到+抢红包\n默认不推送通知，如需推送，将脚本开头的notify改为1，复制青龙的notify.py到脚本所在文件夹并设置好相关参数')#line:150
    print (_O0000OO0O0OO0000O .get ('msg')['好奇车生活'])#line:151
    O0O0OO0OOOO0000O0 ='v1.1'#line:152
    O00O0O00OO00OO0O0 =_O0000OO0O0OO0000O ['version']['好奇车生活']#line:153
    print (f'当前版本{O0O0OO0OOOO0000O0}，仓库版本{O00O0O00OO00OO0O0}')#line:154
    if O0O0OO0OOOO0000O0 <O00O0O00OO00OO0O0 :#line:155
        print ('请到仓库下载最新版本')#line:156
    print (_O0000OO0O0OO0000O .get ("update_log")['好奇车生活'])#line:157
    print ("="*25 )#line:158
def main ():#line:161
    get_info ()#line:162
    OO00O0O0000000OO0 =os .getenv ('hqcshck')#line:163
    if not OO00O0O0000000OO0 :#line:164
        print (_O0000OO0O0OO0000O .get ('msg')['好奇车生活'])#line:165
        exit ()#line:166
    O0OO00O0O0O0O00OO =OO00O0O0000000OO0 .replace ('&','\n').split ('\n')#line:167
    print (f'共获取到{len(O0OO00O0O0O0O00OO)}个账号')#line:168
    OOO0O0O00000O000O =[]#line:169
    with multiprocessing .Pool ()as O0O0OO0O0OOO00O00 :#line:170
        for OOOO0OOOO0O0O000O in O0OO00O0O0O0O00OO :#line:171
            OOO0O0O00000O000O .append (O0O0OO0O0OOO00O00 .apply_async (hq ,args =(OOOO0OOOO0O0O000O ,)).get ())#line:172
    OO0O00000O0O000OO ='\n'.join (OOO0O0O00000O000O )#line:173
    if notify :#line:174
        if load_notify ():#line:175
            send ('好奇车生活签到通知',OO0O00000O0O000OO +f'\n本通知by：https://github.com/kxs2018/xiaoym\ntg讨论群：https://t.me/xizhiaigroup\n通知时间：{ftime()}')#line:177
if __name__ =='__main__':#line:180
    main ()#line:181
