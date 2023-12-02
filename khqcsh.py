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
    O0OOO0OO00OO00O00 ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:26
    OO0OO00OO0O000O00 =requests .get ('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',headers =O0OOO0OO00OO00O00 ).json ()#line:27
    return OO0OO00OO0O000O00 #line:28
_O00000O00O0OO0O0O =get_msg ()#line:31
def ftime ():#line:34
    O0O0O00OO0OOOO0O0 =datetime .datetime .now ().strftime ('%Y-%m-%d %H:%M:%S')#line:35
    return O0O0O00OO0OOOO0O0 #line:36
class HQCSH :#line:39
    def __init__ (OO000OOO00OOOO000 ,OOO0O0OOOO000OOO0 ):#line:40
        O00O0OOO00OO00O00 =OOO0O0OOOO000OOO0 .split (';')#line:41
        if ''in O00O0OOO00OO00O00 :#line:42
            O00O0OOO00OO00O00 .pop ('')#line:43
        OO000OOO00OOOO000 .name =O00O0OOO00OO00O00 [0 ].split ('=')[1 ]#line:44
        OO000OOO00OOOO000 .aid =O00O0OOO00OO00O00 [1 ].split ('=')[1 ]#line:45
        OO000OOO00OOOO000 .headers ={'accountId':OO000OOO00OOOO000 .aid ,'tenantId':'619669306447261696','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/6763',}#line:48
        OO000OOO00OOOO000 .msg =''#line:49
        OO000OOO00OOOO000 .jf =None #line:50
    def sign (OO0O00OOOO000O000 ):#line:52
        O0OOOOOO00000O00O =datetime .datetime .now ().time ()#line:53
        if datetime .time (7 )<=O0OOOOOO00000O00O <datetime .time (23 ):#line:54
            OOO0OO00O0O000OOO ="https://channel.cheryfs.cn/archer/activity-api/signinact/signin"#line:55
            OOO0O0OO000O00O00 ={'activityId':'620810406813786113'}#line:56
            OO0O00OOOO000O000 .headers .update (OOO0O0OO000O00O00 )#line:57
            O0OOO0OO0OOO0OO0O =requests .get (OOO0OO00O0O000OOO ,headers =OO0O00OOOO000O000 .headers )#line:58
            if O0OOO0OO0OOO0OO0O .json ()['success']:#line:60
                if O0OOO0OO0OOO0OO0O .json ()['result']['success']:#line:61
                    print (f"【{OO0O00OOOO000O000.name}】：登录成功,签到成功")#line:62
                    OO0O00OOOO000O000 .msg =f"【{OO0O00OOOO000O000.name}】：登录成功,签到成功\n"#line:63
                else :#line:64
                    print (f"【{OO0O00OOOO000O000.name}】：登录成功,{O0OOO0OO0OOO0OO0O.json()['result']['message']}")#line:65
                    OO0O00OOOO000O000 .msg =f"【{OO0O00OOOO000O000.name}】：登录成功,{O0OOO0OO0OOO0OO0O.json()['result']['message']}\n"#line:66
                return True #line:67
            else :#line:68
                print (f"【{OO0O00OOOO000O000.name}】：登录失败,{O0OOO0OO0OOO0OO0O.json()['message']}")#line:69
                OO0O00OOOO000O000 .msg =f"【{OO0O00OOOO000O000.name}】：登录失败,{O0OOO0OO0OOO0OO0O.json()['message']}\n"#line:70
                return False #line:71
        else :#line:72
            print (f'【{OO0O00OOOO000O000.name}】：当前不在签到时间段')#line:73
            OO0O00OOOO000O000 .msg +=f'【{OO0O00OOOO000O000.name}】：当前不在签到时间段\n'#line:74
            return False #line:75
    def get_jf (O0O0OOO0O00000O0O ):#line:77
        OO0O0O00000O0O0O0 ='https://channel.cheryfs.cn/archer/activity-api/common/accountPointLeft?pointId=620415610219683840'#line:78
        OO0O0OOOOO0000000 ={'activityId':'621911913692942337'}#line:79
        O0O0OOO0O00000O0O .headers .update (OO0O0OOOOO0000000 )#line:80
        O0OO0OO00OO0O000O =requests .get (OO0O0O00000O0O0O0 ,headers =O0O0OOO0O00000O0O .headers ).json ()#line:81
        O0O0OOO0O00000O0O .jf =O0OO0OO00OO0O000O .get ('result')#line:82
        print (f'【{O0O0OOO0O00000O0O.name}】：现有积分{O0O0OOO0O00000O0O.jf}')#line:83
        O0O0OOO0O00000O0O .msg +=f'【{O0O0OOO0O00000O0O.name}】：现有积分{O0O0OOO0O00000O0O.jf}\n'#line:84
    def qianghb (OOOOO0O00O0O0000O ):#line:86
        O0OO0O00O0O00OO0O =f'https://channel.cheryfs.cn/archer/activity-api/pointsmall/exchangeCard?pointsMallCardId={q["id"]}&exchangeCount=1&mallOrderInputVoStr=%7B%22person%22:%22%22,%22phone%22:%22%22,%22province%22:%22%22,%22city%22:%22%22,%22area%22:%22%22,%22address%22:%22%22,%22remark%22:%22%22%7D&channel=1&exchangeType=0&exchangeNeedPoints=188&exchangeNeedMoney=0&cardGoodsItemIds='#line:87
        OO0O0O0O00OO000OO ={'activityId':'621950054462152705'}#line:88
        OOOOO0O00O0O0000O .headers .update (OO0O0O0O00OO000OO )#line:89
        OOOO0O000O00OOO00 =datetime .datetime .now ().time ()#line:90
        if datetime .time (18 )<=OOOO0O000O00OOO00 <datetime .time (22 ):#line:91
            O00O00O00OOO00O0O =0 #line:92
            while O00O00O00OOO00O0O <10 :#line:93
                O00O00O00OOO00O0O +=1 #line:94
                try :#line:95
                    O00OOO0O0OO0OOO0O =requests .get (O0OO0O00O0O00OO0O ,headers =OOOOO0O00O0O0000O .headers ).json ()#line:96
                    if not O00OOO0O0OO0OOO0O .get ('result').get ('success'):#line:97
                        print (f"【{OOOOO0O00O0O0000O.name}】：抢红包 {O00OOO0O0OO0OOO0O.get('result').get('errMsg')}")#line:98
                        time .sleep (30 )#line:99
                        continue #line:100
                    else :#line:101
                        time .sleep (1 )#line:102
                        OO00000O0OOO0O00O =f"https://channel.cheryfs.cn/archer/activity-api/pointsmall/exchangeCardResult?resultKey={O00OOO0O0OO0OOO0O['result']['id']}"#line:103
                        OOO0O0OOO0OO00O0O =requests .get (OO00000O0OOO0O00O ,headers =OOOOO0O00O0O0000O .headers ).json ()#line:104
                        if OOO0O0OOO0OO00O0O ['result']['errMsg']=='成功':#line:105
                            print (f"【{OOOOO0O00O0O0000O.name}】：{OOO0O0OOO0OO00O0O.json()['result']['errMsg']}，请前往个人中心-我的礼包查看")#line:106
                            OOOOO0O00O0O0000O .msg +=f"【{OOOOO0O00O0O0000O.name}】：{OOO0O0OOO0OO00O0O.json()['result']['errMsg']}，请前往个人中心-我的礼包查看\n"#line:107
                            break #line:108
                        else :#line:109
                            time .sleep (30 )#line:110
                            continue #line:111
                except :#line:112
                    print (f'【{OOOOO0O00O0O0000O.name}】：抢红包 请求异常，正在重试')#line:113
                    time .sleep (30 )#line:114
                    continue #line:115
        else :#line:116
            print (f'【{OOOOO0O00O0O0000O.name}】：当前不是抢红包的时间段')#line:117
            OOOOO0O00O0O0000O .msg +=f'【{OOOOO0O00O0O0000O.name}】：当前不是抢红包的时间段\n'#line:118
    def run (O00000OO0000OOOOO ):#line:120
        if O00000OO0000OOOOO .sign ():#line:121
            O00000OO0000OOOOO .get_jf ()#line:122
            if O00000OO0000OOOOO .jf >=188 :#line:123
                O00000OO0000OOOOO .qianghb ()#line:124
                O00000OO0000OOOOO .get_jf ()#line:125
            else :#line:126
                print (f'【{O00000OO0000OOOOO.name}】：积分不足')#line:127
                O00000OO0000OOOOO .msg +=f'【{O00000OO0000OOOOO.name}】：积分不足\n'#line:128
        return O00000OO0000OOOOO .msg #line:129
def hq (O0OO0OOOOO0OOO0OO ,O000OO0O000O0O00O ):#line:132
    OOOO00OO0O0OO0000 =HQCSH (O000OO0O000O0O00O )#line:133
    return OOOO00OO0O0OO0000 .run ()#line:134
def load_notify ():#line:137
    global send #line:138
    try :#line:139
        from notify import send #line:140
        print ("加载通知服务成功！")#line:141
        return True #line:142
    except :#line:143
        print ('加载通知服务失败,请复制一份青龙notify.py到同级文件夹')#line:144
        return False #line:145
def get_info ():#line:148
    print ("="*25 +f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n'+'-'*50 )#line:150
    print ('好奇车生活小程序签到+抢红包\n默认不推送通知，如需推送，将脚本开头的notify改为1，复制青龙的notify.py到脚本所在文件夹并设置好相关参数')#line:152
    print (_O00000O00O0OO0O0O .get ('msg')['好奇车生活'])#line:153
    OO00O0O0OOO000OOO ='v1.3'#line:154
    O0O00OOOO0O0O0O00 =_O00000O00O0OO0O0O ['version']['好奇车生活']#line:155
    print (f'当前版本{OO00O0O0OOO000OOO}，仓库版本{O0O00OOOO0O0O0O00}')#line:156
    if OO00O0O0OOO000OOO <O0O00OOOO0O0O0O00 :#line:157
        print ('请到仓库下载最新版本')#line:158
    print (_O00000O00O0OO0O0O .get ("update_log")['好奇车生活'])#line:159
    print ("="*25 )#line:160
def main ():#line:163
    get_info ()#line:164
    O00O00OO00O0O0O00 =os .getenv ('hqcshck')#line:165
    if not O00O00OO00O0O0O00 :#line:166
        print (_O00000O00O0OO0O0O .get ('msg')['好奇车生活'])#line:167
        exit ()#line:168
    OO0O00000OO00OOO0 =O00O00OO00O0O0O00 .replace ('&','\n').split ('\n')#line:169
    print (f'共获取到{len(OO0O00000OO00OOO0)}个账号')#line:170
    with multiprocessing .Pool ()as O0OO00O000000O0OO :#line:171
        O0OOO00O0O0O000OO =list (O0OO00O000000O0OO .starmap (hq ,enumerate (OO0O00000OO00OOO0 )))#line:172
    O0O00O0OOO0OO0O0O ='\n'.join (O0OOO00O0O0O000OO )#line:173
    if notify :#line:174
        if load_notify ():#line:175
            send ('好奇车生活签到通知',O0O00O0OOO0OO0O0O +f'\n本通知by：https://github.com/kxs2018/xiaoym\ntg讨论群：https://t.me/xiaoymgroup\n通知时间：{ftime()}')#line:177
if __name__ =='__main__':#line:180
    main ()#line:181
