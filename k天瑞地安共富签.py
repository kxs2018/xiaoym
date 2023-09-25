# -*- coding: utf-8 -*-
# 天瑞地安共富签
# Author: kk
# date：2023/9/25 11:59
"""
本脚本适用于天瑞地安APP共富签
连签奖励
抓包 https://crm.rabtv.cn，在请求体内找到Authorization的值（Bearer xxxxxxxxxx）
青龙配置文件添加：
-------------------------------------
多个账号增加大括号即可
export trdack="[{'ck':'Bearer xxxxxxxxxx'},{'ck':'Bearer xxxxxxxxxx'}]"

=====================抽奖没有授权的临时解决方案======================
抓包 https://guess.rabtv.cn，同样在请求体内找到Authorization的值（Bearer xxxxxxxxxx）
写入gck。示例：
export trdack="[{'ck':'Bearer xxxxxxxxxx','gck':'Bearer xxxxxxxxxx'}]"
ck是https://crm.rabtv.cn的Authorization的值，gck是https://guess.rabtv.cn的Authorization的值
====================================================================

推送配置：
-------------------------------------
export qwbotkey="xxx"
参考 https://github.com/kxs2018/yuedu/blob/main/获取企业微信群机器人key.md 获取key，并关注插件！！！
-------------------------------------
"""
import datetime  # line:27
import json  # line:28
import time  # line:29
import requests  # line:30
from random import randint  # line:31
import os  # line:32
import ast  # line:33


def ftime():  # line:36
    O0O0O0OO00000O000 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # line:37
    return O0O0O0OO00000O000  # line:38


def send(O0000OO00OOOOOOO0, title='通知', url=None):  # line:41
    OO0OOO00OO0000000 = os.getenv('qwbotkey')  # line:42
    if not url:  # line:43
        O000OOOO0O0OO00OO = {"msgtype": "text", "text": {
            "content": f"{title}\n\n{O0000OO00OOOOOOO0}\n\n本通知by：https://github.com/kxs2018/xiaoym\n[点击加入惜之酱tg频道](https://t.me/+uyR92pduL3RiNzc1)\n通知时间：{ftime()}", }}  # line:50
    else:  # line:51
        O000OOOO0O0OO00OO = {"msgtype": "news", "news": {"articles": [
            {"title": title, "description": O0000OO00OOOOOOO0, "url": url,
             "picurl": 'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'}]}}  # line:56
    O0OO00O00OOO00O0O = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={OO0OOO00OO0000000}'  # line:57
    OO0O0000O0000O000 = requests.post(O0OO00O00OOO00O0O, data=json.dumps(O000OOOO0O0OO00OO)).json()  # line:58
    if OO0O0000O0000O000.get('errcode') != 0:  # line:59
        print('消息发送失败，请检查key和发送格式')  # line:60
        return False  # line:61
    return OO0O0000O0000O000  # line:62


class TRDA:  # line:65
    def __init__(OO00O00OOO00O00OO, O0OO000O00OOO0O0O):  # line:66
        OO00O00OOO00O00OO.ck = O0OO000O00OOO0O0O.get('ck')  # line:67
        OO00O00OOO00O00OO.gck = O0OO000O00OOO0O0O.get('gck')  # line:68
        OO00O00OOO00O00OO.s = requests.session()  # line:69
        OO00O00OOO00O00OO.s.headers = {"Authorization": OO00O00OOO00O00OO.ck,
                                       "User-Agent": "Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36;xsb_ruian;xsb_ruian;2.31.742;native_app", }  # line:72
        OO00O00OOO00O00OO.msg = ''  # line:73

    def user_info(O0O00O0O0O0000O00):  # line:75
        OO00000OOO0O0O0OO = 'https://crm.rabtv.cn/v2/index/userInfo'  # line:76
        OOOOOO00OOOO000O0 = O0O00O0O0O0000O00.s.post(OO00000OOO0O0O0OO).json()  # line:77
        if OOOOOO00OOOO000O0.get('code') == 1:  # line:79
            O0O00O0O0O0000O00.un = OOOOOO00OOOO000O0.get('data').get('username')  # line:80
            OO0OOOOOOO00O0000 = OOOOOO00OOOO000O0.get('data').get('common_user').get('money')  # line:81
            OO00O0O0O000O0OOO = ''.join(OOOOOO00OOOO000O0.get('data').get('continue_sign_num'))  # line:82
            if OO00O0O0O000O0OOO.startswith('0'):  # line:83
                OO00O0O0O000O0OOO = OO00O0O0O000O0OOO[1:]  # line:84
            O00OO00000OO0O0O0 = OOOOOO00OOOO000O0.get('data').get('total_sign_num')  # line:85
            OOOO0OOOOO0O0O0OO = f'【{O0O00O0O0O0000O00.un}】：当前红包{OO0OOOOOOO00O0000}元，已连续签到{OO00O0O0O000O0OOO}天，总签到{O00OO00000OO0O0O0}天'  # line:86
            print(OOOO0OOOOO0O0O0OO)  # line:87
            O0O00O0O0O0000O00.msg += f'{OOOO0OOOOO0O0O0OO}\n '  # line:88
            return True  # line:89
        else:  # line:90
            print(OOOOOO00OOOO000O0.get('msg'))  # line:91
            return False  # line:92

    @staticmethod  # line:94
    def gettype(OO0O0O0000OOO000O):  # line:95
        O0O00OOOO00O0O000 = {'redbag': '红包', 'score': '积分'}  # line:96
        OOOO0O0OOOO000000 = O0O00OOOO00O0O000.get(OO0O0O0000OOO000O)  # line:97
        return OOOO0O0OOOO000000 if OOOO0O0OOOO000000 else OO0O0O0000OOO000O  # line:98

    def signin(O0OOO000OO000O0O0):  # line:100
        global msg  # line:101
        OO00O0OO00OO00O00 = 'https://crm.rabtv.cn/v2/index/signIn'  # line:102
        O000O00O00000O0OO = O0OOO000OO000O0O0.s.post(OO00O0OO00OO00O00).json()  # line:103
        if O000O00O00000O0OO.get('code') == 0:  # line:105
            msg = O000O00O00000O0OO.get("msg")  # line:106
            if 'plz-check-mobile' in msg:  # line:107
                send(f'{O0OOO000OO000O0O0.un} 天瑞地安签到需验证手机，请手动签到')  # line:108
        elif O000O00O00000O0OO.get('code') == 1:  # line:109
            O0O0000OOO0OOOOOO = O000O00O00000O0OO.get('data')['type']  # line:110
            OO00O0O000OO0000O = O000O00O00000O0OO.get('data').get(O0O0000OOO0OOOOOO)  # line:111
            O0O0OO0OO00OO00OO = O000O00O00000O0OO.get('data').get('continue_sign_num')  # line:112
            msg = f'签到成功，获得{OO00O0O000OO0000O}{O0OOO000OO000O0O0.gettype(O0O0000OOO0OOOOOO)}，连续签到{O0O0OO0OO00OO00OO}天'  # line:113
        msg = f'【{O0OOO000OO000O0O0.un}】：{msg}'  # line:114
        print(msg)  # line:115
        O0OOO000OO000O0O0.msg += f'{msg}\n '  # line:116

    def chou(OOO0OO00OO00000OO):  # line:118
        if OOO0OO00OO00000OO.gck:  # line:119
            OOO0OO00OO00000OO.s.headers["Authorization"] = OOO0OO00OO00000OO.gck  # line:120
        OOOOOOO000O00O00O = 'https://guess.rabtv.cn/v1/task/do'  # line:121
        for OOO00OO000OOOOO0O in range(1, 5):  # line:122
            O0OO00OOOOOOOO000 = {'id': OOO00OO000OOOOO0O}  # line:123
            OO0OO0OOOO0O0OOO0 = OOO0OO00OO00000OO.s.get(OOOOOOO000O00O00O, data=O0OO00OOOOOOOO000).json()  # line:124
            print('task_current ', OO0OO0OOOO0O0OOO0)  # line:125
            if OO0OO0OOOO0O0OOO0.get('done'):  # line:126
                OOO00OOO00O0O0OO0 = f'[任务{OOO00OO000OOOOO0O}]抽奖完成，获得红包{OO0OO0OOOO0O0OOO0.get("v")}元'  # line:127
                OOO0OO00OO00000OO.msg += OOO00OOO00O0O0OO0 + '\n'  # line:128
                print(OOO00OOO00O0O0OO0)  # line:129
            elif OO0OO0OOOO0O0OOO0.get('code') == 0:  # line:130
                OOO00OOO00O0O0OO0 = f'[任务{OOO00OO000OOOOO0O}]：{OO0OO0OOOO0O0OOO0.get("msg")}'  # line:131
                OOO0OO00OO00000OO.msg += OOO00OOO00O0O0OO0 + '\n'  # line:132
                print(OOO00OOO00O0O0OO0)  # line:133
            time.sleep(randint(3, 6))  # line:134

    def run(OO00O0OO000O0O0OO):  # line:136
        if OO00O0OO000O0O0OO.user_info():  # line:137
            OO00O0OO000O0O0OO.signin()  # line:138
            OO00O0OO000O0O0OO.chou()  # line:139
            OO00O0OO000O0O0OO.msg += '连签奖励请手动领取\n'  # line:140
            print('连签奖励请手动领取')  # line:141
            OO00O0OO000O0O0OO.msg += '-' * 20 + '\n'  # line:142
            return OO00O0OO000O0O0OO.msg  # line:143


def ran_time():  # line:146
    OOO00OO0OO00O0O0O = randint(3, 10)  # line:147
    O0O00O0OOO00O0O0O = randint(3, 10)  # line:148
    OOO00OO0OO00O0O0O **= 1.5  # line:149
    O0O00O0OOO00O0O0O **= 2  # line:150
    O0O000OOOOO0O0OOO = randint(int(OOO00OO0OO00O0O0O * 8), O0O00O0OOO00O0O0O * 15) if int(
        OOO00OO0OO00O0O0O * 8) < O0O00O0OOO00O0O0O * 15 else randint(O0O00O0OOO00O0O0O * 15,
                                                                     int(OOO00OO0OO00O0O0O * 8))  # line:151
    return O0O000OOOOO0O0OOO  # line:152


def get_ver():  # line:155
    OOOO00O00O0O00O00 = 'k天瑞地安共富签 V1.5'  # line:156
    O0OOOO00O00O00OO0 = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}  # line:159
    OOO000O00OO0O000O = requests.get(
        'https://ghproxy.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json',
        headers=O0OOOO00O00O00OO0).json()  # line:161
    O0000OO000OO0OO0O = OOOO00O00O0O00O00.split(' ')[1]  # line:162
    O0O0OO0O000O000OO = OOO000O00OO0O000O.get('version').get(OOOO00O00O0O00O00.split(' ')[0])  # line:163
    OO00O00000OO0OO00 = f"当前版本 {O0000OO000OO0OO0O}，仓库版本 {O0O0OO0O000O000OO}"  # line:164
    if O0000OO000OO0OO0O < O0O0OO0O000O000OO:  # line:165
        OO00O00000OO0OO00 += '\n' + '请到https://github.com/kxs2018/xiaoym下载最新版本'  # line:166
    return OO00O00000OO0OO00  # line:167


def main():  # line:170
    print("-" * 50 + f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n' + '-' * 50)  # line:171
    OO0O0OO000OOOOO00 = ''  # line:172
    OO0OO00O000OO0OOO = os.getenv('trdack')  # line:173
    try:  # line:174
        OO0OO00O000OO0OOO = ast.literal_eval(OO0OO00O000OO0OOO)  # line:175
    except:  # line:176
        pass  # line:177
    OO0O0O0O00O0OOO00 = int(ran_time() / 10)  # line:178
    print(f'{OO0O0O0O00O0OOO00}秒后开始签到')  # line:179
    time.sleep(OO0O0O0O00O0OOO00)  # line:180
    for OOOO00OOO0OOOOOOO, O00O0OOOOOO0O00OO in enumerate(OO0OO00O000OO0OOO, start=1):  # line:181
        print(
            f'{O00O0OOOOOO0O00OO}\n以上是第{OOOO00OOO0OOOOOOO}个账号的ck，请核对是否正确，如不正确，请检查ck填写格式')  # line:182
        try:  # line:183
            OOOO000OOO000OOO0 = TRDA(O00O0OOOOOO0O00OO)  # line:184
            OO0O0OO000OOOOO00 += OOOO000OOO000OOO0.run()  # line:185
            if O00O0OOOOOO0O00OO != OO0OO00O000OO0OOO[-1]:  # line:186
                OO0O0O0O00O0OOO00 = ran_time()  # line:187
                print(f'{OO0O0O0O00O0OOO00}后进行下一个签到')  # line:188
                time.sleep(OO0O0O0O00O0OOO00)  # line:189
        except Exception as OOO000000O0O0O000:  # line:190
            print(f'第{OOOO00OOO0OOOOOOO}个账号签到错误\n\n{OOO000000O0O0O000}')  # line:191
            OO0O0OO000OOOOO00 += f'第{OOOO00OOO0OOOOOOO}个账号签到错误\n\n{OOO000000O0O0O000}'  # line:192
            continue  # line:193
    send(OO0O0OO000OOOOO00, title=f'天瑞地安共富签信息')  # line:194


if __name__ == '__main__':  # line:197
    main()  # line:198
