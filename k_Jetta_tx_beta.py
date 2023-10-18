# -*- coding: utf-8 -*-
# k_Jetta 提现测试版
"""
new Env("捷达APP签到");
抓包捷达APP serviceui-yy-ui.jconnect.faw-vw.com，请求头中的token值，填入jetta_ck的app_token项
抓包微信端提现链接 serviceui-yy-ui.jconnect.faw-vw.com，请求头中的token值，填入jetta_ck的wx_token项
export jetta_ck="[{'name':'德华','app_token':'xxxx','wx_token':'xxxxx'},{'name':'彦祖','app_token':'ccc','wx_token':'xxxxx'}]"
name方便自己辨别账号，随便填
通知默认关闭，如需开启，复制青龙的notify.py到脚本所在文件夹
"""
"""通知开关"""
notify = 0
"""1开0关"""

import os
import requests
import multiprocessing
import datetime


def get_msg():  # line:1
    OO00OOO000OOOO0O0 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}  # line:3
    O00OOOO00O00OO000 = requests.get('https://jihulab.com/xizhiai/xiaoym/-/raw/main/ver.json',
                                     headers=OO00OOO000OOOO0O0).json()  # line:4
    return O00OOOO00O00OO000  # line:5


_O0OO00OO000OOO0O0 = get_msg()  # line:8


def load_notify():  # line:11
    global send  # line:12
    try:  # line:13
        from notify import send  # line:14
        print("加载通知服务成功！")  # line:15
    except:  # line:16
        send = False  # line:17
        print('加载通知服务失败')  # line:18


def ftime():  # line:21
    OOO0OOOOO0O000O00 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # line:22
    return OOO0OOOOO0O000O00  # line:23


def get_info():  # line:26
    print(
        "=" * 25 + f'\ngithub仓库：https://github.com/kxs2018/xiaoym\n极狐仓库（国内可访问）:https://jihulab.com/xizhiai/xiaoym\nBy:惜之酱\n' + '-' * 20)  # line:28
    OOOO0OOOO000O0O0O = 'v1.1'  # line:29
    O0OOO00OO00000O0O = _O0OO00OO000OOO0O0['version']['捷达']  # line:30
    print(f'当前版本{OOOO0OOOO000O0O0O}，仓库版本{O0OOO00OO00000O0O}')  # line:31
    if OOOO0OOOO000O0O0O < O0OOO00OO00000O0O:  # line:32
        print('请到仓库下载最新版本k_jetta.py')  # line:33
    print("=" * 25)  # line:34
    return True  # line:35


class JETTA:  # line:38
    def __init__(OO00OO0000O0000OO, OOOOOOOO0O0O0O00O):  # line:39
        OO00OO0000O0000OO.app_token = OOOOOOOO0O0O0O00O.get('app_token')  # line:40
        OO00OO0000O0000OO.name = OOOOOOOO0O0O0O00O.get('name')  # line:41
        OO00OO0000O0000OO.wx_token = OOOOOOOO0O0O0O00O.get('wx_token')  # line:42
        OO00OO0000O0000OO.msg = ''  # line:43
        OO00OO0000O0000OO.headers = {'Host': 'service-yy.jconnect.faw-vw.com', 'Connection': 'keep-alive',
                                     'Pragma': 'no-cache', 'Cache-Control': 'no-cache',
                                     'Accept': 'application/json, text/plain, */*',
                                     'User-Agent': 'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36',
                                     'token': OO00OO0000O0000OO.app_token,
                                     'Origin': 'https://serviceui-yy-ui.jconnect.faw-vw.com',
                                     'X-Requested-With': 'com.fawvw.ebo', 'Sec-Fetch-Site': 'same-site',
                                     'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty',
                                     'Referer': 'https://serviceui-yy-ui.jconnect.faw-vw.com/',
                                     'Accept-Encoding': 'gzip, deflate',
                                     'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'}  # line:51

    def getUserInfo(O000O00O00O00O0O0):  # line:53
        O00O0O00O00000000 = 'https://service-yy.jconnect.faw-vw.com/redpackbank/user/getUserInfo'  # line:54
        OO00OOO000O000O0O = requests.get(O00O0O00O00000000, headers=O000O00O00O00O0O0.headers).json()  # line:55
        if OO00OOO000O000O0O.get('status') == 'FAILED':  # line:56
            print(f'账号【{O000O00O00O00O0O0.name}】：登录失败，{OO00OOO000O000O0O.get("errorMessage")}')  # line:57
            O000O00O00O00O0O0.msg += f'账号【{O000O00O00O00O0O0.name}】：登录失败，{OO00OOO000O000O0O.get("errorMessage")}\n'  # line:58
            return False  # line:59
        else:  # line:60
            O00O00OO0OO0OOO0O = OO00OOO000O000O0O['data']['detail']['allPrize']  # line:61
            print(f"账号【{O000O00O00O00O0O0.name}】：登录成功，红包余额{O00O00OO0OO0OOO0O}")  # line:62
            O000O00O00O00O0O0.msg += f"账号【{O000O00O00O00O0O0.name}】：登录成功，红包余额{O00O00OO0OO0OOO0O}\n"  # line:63
            return True  # line:64

    def getPrize(OO0OO0OO00000O0O0):  # line:66
        O000OOOO0OOOO0OOO = 'https://service-yy.jconnect.faw-vw.com/redpackbank/prize/getPrize'  # line:67
        O0O0O0O0OOOOO000O = requests.get(O000OOOO0OOOO0OOO, headers=OO0OO0OO00000O0O0.headers).json()  # line:68
        if O0O0O0O0OOOOO000O.get('status') == 'FAILED':  # line:69
            print(f'账号【{OO0OO0OO00000O0O0.name}】：{O0O0O0O0OOOOO000O.get("errorMessage")}')  # line:70
            OO0OO0OO00000O0O0.msg += f'账号【{OO0OO0OO00000O0O0.name}】：{O0O0O0O0OOOOO000O.get("errorMessage")}\n'  # line:71
        else:  # line:72
            O000O00OO00O00OO0 = O0O0O0O0OOOOO000O['data']['todayPrize']  # line:73
            print(f"账号【{OO0OO0OO00000O0O0.name}】：签到获得{O000O00OO00O00OO0}")  # line:74
            OO0OO0OO00000O0O0.msg += f"账号【{OO0OO0OO00000O0O0.name}】：签到获得{O000O00OO00O00OO0}\n"  # line:75

    @staticmethod  # line:77
    def is_date_18():  # line:78
        OOOO00O00O0O0O00O = datetime.datetime.now().day  # line:79
        return False if OOOO00O00O0O0O00O != 18 else True  # line:80

    def withdraw(OOOOOO0OO0O00000O):  # line:82
        if OOOOOO0OO0O00000O.wx_token:  # line:83
            O0O000OO000OOO0OO = 'https://service-yy.jconnect.faw-vw.com/redpackbank/prize/withdrawal'  # line:84
            OOOOOO0OO0O00000O.headers.update({'token': OOOOOO0OO0O00000O.wx_token,
                                              'User-Agent': 'Mozilla/5.0 (Linux; Android 13; M2011K2C Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5307 MMWEBSDK/20230701 MMWEBID/2351 MicroMessenger/8.0.40.2420(0x28002858) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64'})  # line:86
            OOOOO00OOO00000O0 = requests.get(O0O000OO000OOO0OO, headers=OOOOOO0OO0O00000O.headers).json()  # line:87
            if OOOOO00OOO00000O0.get('status') == 'FAILED':  # line:88
                print(f'账号【{OOOOOO0OO0O00000O.name}】：{OOOOO00OOO00000O0.get("errorMessage")}')  # line:89
                OOOOOO0OO0O00000O.msg += f'账号【{OOOOOO0OO0O00000O.name}】：{OOOOO00OOO00000O0.get("errorMessage")}\n'  # line:90
            else:  # line:91
                print(OOOOO00OOO00000O0)  # line:92
        else:  # line:93
            print(f"账号【{OOOOOO0OO0O00000O.name}】：未获取到微信端token，不执行提现")  # line:94
            OOOOOO0OO0O00000O.msg += f"账号【{OOOOOO0OO0O00000O.name}】：未获取到微信端token，不执行提现\n"  # line:95
            return  # line:96

    def run(OO00O000OO0O00O00):  # line:98
        if OO00O000OO0O00O00.getUserInfo():  # line:99
            OO00O000OO0O00O00.getPrize()  # line:100
            if OO00O000OO0O00O00.is_date_18():  # line:101
                OO00O000OO0O00O00.withdraw()  # line:102
        return OO00O000OO0O00O00.msg  # line:103


def jd_signin(O000000OOOO0OO0O0, O0OOO0O000000OO00):  # line:106
    O0OO0OO00000000O0 = JETTA(O0OOO0O000000OO00)  # line:107
    return O0OO0OO00000000O0.run()  # line:108


def main():  # line:111
    O000OOOO000O0000O = get_info()  # line:112
    OO0000OO0OO0O0O0O = os.getenv('jetta_ck')  # line:113
    if not OO0000OO0OO0O0O0O:  # line:114
        print('没有获取到jettack，程序退出')  # line:115
        exit()  # line:116
    OO0000OO0OO0O0O0O = OO0000OO0OO0O0O0O.replace('&', '\n').split('\n')  # line:117
    print(f'共获取到{len(OO0000OO0OO0O0O0O)}个账号')  # line:118
    O0OOO0OOOOOO0O0OO = f'共获取到{len(OO0000OO0OO0O0O0O)}个账号\n\n'  # line:119
    if not O000OOOO000O0000O:  # line:120
        exit()  # line:121
    with multiprocessing.Pool(5) as O00OO00OOOOO000O0:  # line:122
        OO00OOOOOOO00OO0O = O00OO00OOOOO000O0.starmap(jd_signin, enumerate(OO0000OO0OO0O0O0O))  # line:123
        O0OOO0OOOOOO0O0OO += '\n'.join(OO00OOOOOOO00OO0O)  # line:124
    if notify:  # line:125
        load_notify()  # line:126
        if send:  # line:127
            send('捷达APP签到通知',
                 O0OOO0OOOOOO0O0OO + f'\n本通知by：https://github.com/kxs2018/xiaoym\ntg讨论群：https://t.me/xizhiaigroup\n通知时间：{ftime()}')  # line:129


if __name__ == '__main__':  # line:132
    main()  # line:133
