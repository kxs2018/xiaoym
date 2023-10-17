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
    OO0OOOO000O0OOOO0 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:26
    OOO0O0O00000OO000 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =OO0OOOO000O0OOOO0 ).json ()#line:27
    return OOO0O0O00000OO000 #line:28
_OO0OO000OO00OO0OO =get_msg ()#line:31
def ftime ():#line:34
    O00OOOO0000OO0OOO =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:35
    return O00OOOO0000OO0OOO #line:36
class HQCSH :#line:39
    def __init__ (OO00O000OO000O00O ,OO00OO00O000O00OO ):#line:40
        O00OOO0O0OO0O00OO =OO00OO00O000O00OO .split (';')#line:41
        if ''in O00OOO0O0OO0O00OO :#line:42
            O00OOO0O0OO0O00OO .pop ('')#line:43
        OO00O000OO000O00O .name =O00OOO0O0OO0O00OO [0 ].split ('=')[1 ]#line:44
        OO00O000OO000O00O .aid =O00OOO0O0OO0O00OO [1 ].split ('=')[1 ]#line:45
        OO00O000OO000O00O .headers ={'accountId':OO00O000OO000O00O .aid ,'tenantId':'619669306447261696','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/6763',}#line:48
        OO00O000OO000O00O .msg =''#line:49
        OO00O000OO000O00O .jf =None #line:50
    def sign (OOOO00OO000OO0000 ):#line:52
        O0OOOOOO0OOOO0000 =datetime .datetime .now ().time ()#line:53
        if datetime .time (7 )<=O0OOOOOO0OOOO0000 <datetime .time (23 ):#line:54
            O0O00OOOO0000OOOO ="https://channel.cheryfs.cn/archer/activity-api/signinact/signin"#line:55
            OO0O00OO0O00O0000 ={'activityId':'620810406813786113'}#line:56
            OOOO00OO000OO0000 .headers .update (OO0O00OO0O00O0000 )#line:57
            OO0O000OO00O0000O =requests .get (O0O00OOOO0000OOOO ,headers =OOOO00OO000OO0000 .headers )#line:58
            if OO0O000OO00O0000O .json ()['success']:#line:60
                if OO0O000OO00O0000O .json ()['result']['success']:#line:61
                    print (f"【{OOOO00OO000OO0000.name}】：登录成功,签到成功")#line:62
                    OOOO00OO000OO0000 .msg =f"【{OOOO00OO000OO0000.name}】：登录成功,签到成功\n"#line:63
                else :#line:64
                    print (f"【{OOOO00OO000OO0000.name}】：登录成功,{OO0O000OO00O0000O.json()['result']['message']}")#line:65
                    OOOO00OO000OO0000 .msg =f"【{OOOO00OO000OO0000.name}】：登录成功,{OO0O000OO00O0000O.json()['result']['message']}\n"#line:66
                return True #line:67
            else :#line:68
                print (f"【{OOOO00OO000OO0000.name}】：登录失败,{OO0O000OO00O0000O.json()['message']}")#line:69
                OOOO00OO000OO0000 .msg =f"【{OOOO00OO000OO0000.name}】：登录失败,{OO0O000OO00O0000O.json()['message']}\n"#line:70
                return False #line:71
        else :#line:72
            print (f'【{OOOO00OO000OO0000.name}】：当前不在签到时间段')#line:73
            OOOO00OO000OO0000 .msg +=f'【{OOOO00OO000OO0000.name}】：当前不在签到时间段\n'#line:74
            return False #line:75
    def get_jf (OO00O00O0OOO0OO0O ):#line:77
        O0OO0OOO0OOOO00OO ='https://channel.cheryfs.cn/archer/activity-api/common/accountPointLeft?pointId=620415610219683840'#line:78
        OOOOO0OO0O0OOOO0O ={'activityId':'621911913692942337'}#line:79
        OO00O00O0OOO0OO0O .headers .update (OOOOO0OO0O0OOOO0O )#line:80
        O0O000000OO0OO0O0 =requests .get (O0OO0OOO0OOOO00OO ,headers =OO00O00O0OOO0OO0O .headers ).json ()#line:81
        OO00O00O0OOO0OO0O .jf =O0O000000OO0OO0O0 .get ('result')#line:82
        print (f'【{OO00O00O0OOO0OO0O.name}】：现有积分{OO00O00O0OOO0OO0O.jf}')#line:83
        OO00O00O0OOO0OO0O .msg +=f'【{OO00O00O0OOO0OO0O.name}】：现有积分{OO00O00O0OOO0OO0O.jf}\n'#line:84
    def qianghb (O00OO0O000OO0OOOO ):#line:86
        O00O000O0O0OOOO0O =f'https://channel.cheryfs.cn/archer/activity-api/pointsmall/exchangeCard?pointsMallCardId={q["id"]}&exchangeCount=1&mallOrderInputVoStr=%7B%22person%22:%22%22,%22phone%22:%22%22,%22province%22:%22%22,%22city%22:%22%22,%22area%22:%22%22,%22address%22:%22%22,%22remark%22:%22%22%7D&channel=1&exchangeType=0&exchangeNeedPoints=188&exchangeNeedMoney=0&cardGoodsItemIds='#line:87
        OOO00OO000OO0O0O0 ={'activityId':'621950054462152705'}#line:88
        OO00OOOO0000OOO0O =datetime .datetime .now ().time ()#line:89
        if datetime .time (18 )<=OO00OOOO0000OOO0O <datetime .time (22 ):#line:90
            OOOOO000OOOO0O000 =0 #line:91
            while OOOOO000OOOO0O000 <10 :#line:92
                O00OO0O000OO0OOOO .headers .update (OOO00OO000OO0O0O0 )#line:93
                OOOOO000OOOO0O000 +=1 #line:94
                try :#line:95
                    OO00O000OO00O0000 =requests .get (O00O000O0O0OOOO0O ,headers =O00OO0O000OO0OOOO .headers ).json ()#line:96
                    if not OO00O000OO00O0000 .get ('result').get ('success'):#line:97
                        print (f"【{O00OO0O000OO0OOOO.name}】：抢红包 {OO00O000OO00O0000.get('result').get('errMsg')}")#line:98
                        time .sleep (30 )#line:99
                        continue #line:100
                    else :#line:101
                        O000O0OOO0O0O00OO =O00OO0O000OO0OOOO .jf #line:102
                        print (f"【{O00OO0O000OO0OOOO.name}】：抢红包 {OO00O000OO00O0000.get('result').get('errMsg')}")#line:103
                        O00OO0O000OO0OOOO .get_jf ()#line:104
                        if O000O0OOO0O0O00OO >O00OO0O000OO0OOOO .jf :#line:105
                            print (f'【{O00OO0O000OO0OOOO.name}】：抢到红包了，请前往个人中心-我的礼包查看')#line:106
                            O00OO0O000OO0OOOO .msg +=f'【{O00OO0O000OO0OOOO.name}】：抢到红包了，请前往个人中心-我的礼包查看\n'#line:107
                            break #line:108
                        else :#line:109
                            time .sleep (30 )#line:110
                            continue #line:111
                except :#line:112
                    print (f'【{O00OO0O000OO0OOOO.name}】：抢红包 请求异常，正在重试')#line:113
                    time .sleep (30 )#line:114
                    continue #line:115
        else :#line:116
            print (f'【{O00OO0O000OO0OOOO.name}】：当前不是抢红包的时间段')#line:117
            O00OO0O000OO0OOOO .msg +=f'【{O00OO0O000OO0OOOO.name}】：当前不是抢红包的时间段\n'#line:118
    def run (O000O0O000O00O000 ):#line:120
        if O000O0O000O00O000 .sign ():#line:121
            O000O0O000O00O000 .get_jf ()#line:122
            if O000O0O000O00O000 .jf >=188 :#line:123
                O000O0O000O00O000 .qianghb ()#line:124
            else :#line:125
                print (f'【{O000O0O000O00O000.name}】：积分不足以抢{q["money"]}元红包')#line:126
                O000O0O000O00O000 .msg +=f'【{O000O0O000O00O000.name}】：积分不足以抢{q["money"]}元红包\n'#line:127
        return O000O0O000O00O000 .msg #line:128
def hq (OOOO0OOOO00OO0OO0 ,O0O0OO0O00OO00O00 ):#line:131
    OOO00O0OO000O00O0 =HQCSH (O0O0OO0O00OO00O00 )#line:132
    return OOO00O0OO000O00O0 .run ()#line:133
def load_notify ():#line:136
    global send #line:137
    try :#line:138
        from notify import send #line:139
        print ("加载通知服务成功！")#line:140
        return True #line:141
    except :#line:142
        print ('加载通知服务失败,请复制一份青龙notify.py到同级文件夹')#line:143
        return False #line:144
def get_info ():#line:147
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:149
    print ('好奇车生活小程序签到+抢红包\n默认不推送通知，如需推送，将脚本开头的notify改为1，复制青龙的notify.py到脚本所在文件夹并设置好相关参数')#line:151
    print (_OO0OO000OO00OO0OO .get ('msg')['好奇车生活'])#line:152
    OOO00OO00O0000O0O ='v1.2'#line:153
    OO0OOOO0O0O00O000 =_OO0OO000OO00OO0OO ['version']['好奇车生活']#line:154
    print (f'当前版本{OOO00OO00O0000O0O}，仓库版本{OO0OOOO0O0O00O000}')#line:155
    if OOO00OO00O0000O0O <OO0OOOO0O0O00O000 :#line:156
        print ('请到仓库下载最新版本')#line:157
    print (_OO0OO000OO00OO0OO .get ("update_log")['好奇车生活'])#line:158
    print ("="*25 )#line:159
def main ():#line:162
    get_info ()#line:163
    O00000O0O0O00OO0O =os .getenv ('hqcshck')#line:164
    if not O00000O0O0O00OO0O :#line:165
        print (_OO0OO000OO00OO0OO .get ('msg')['好奇车生活'])#line:166
        exit ()#line:167
    O0OO00OOO000O0O0O =O00000O0O0O00OO0O .replace ('&','\n').split ('\n')#line:168
    print (f'共获取到{len(O0OO00OOO000O0O0O)}个账号')#line:169
    with multiprocessing .Pool ()as O0000OO00OOO0O000 :#line:170
        O0OO00O0OO000OOO0 =list (O0000OO00OOO0O000 .starmap (hq ,enumerate (O0OO00OOO000O0O0O )))#line:171
    OOOOO0O00OO0000OO ='\n'.join (O0OO00O0OO000OOO0 )#line:172
    if notify :#line:173
        if load_notify ():#line:174
            send ('好奇车生活签到通知',OOOOO0O00OO0000OO +f'\n本通知by：https://github.com/kxs2018/xiaoym\ntg讨论群：https://t.me/xizhiaigroup\n通知时间：{ftime()}')#line:176
if __name__ =='__main__':#line:179
    main ()#line:180
