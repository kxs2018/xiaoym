# -*- coding: utf-8 -*-
# 每天赚关注私信任务V1.0
# Author: kk
# date：2023/9/7 16:24
"""
每天赚 入口：http://tg.1694070002.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=113565
关注私信任务v1.0，一天上限10，含检测号，一天跑一次足矣。跳过最后一个检测号，无需推送。
附带个人主页签到、领取赠送积分、提升代理等功能。
uid为以后不能跳过检测号时增加推送的wxpusher的uid，填不填无所谓。
配置设置下面两种二选一
（1）青龙配置文件里添加
export mtzck = '''[{"name": "", "ck": ""，"uid":""},
             {"name": "", "ck": "","uid":""},
             {"name": "", "ck": "share:login:","uid":""},
             {"name": "", "ck": ""},
             {"name": "", "ck": "share:login:748948791515454518e7645f368ca"},"uid":""]'''
 （2）青龙环境变量添加
 名称：mtzck
 值：[{"name": "", "ck": ""},
             {"name": "", "ck": ""},
             {"name": "", "ck": "share:login:"},
             {"name": "", "ck": ""},
             {"name": "惜之酱", "ck": "share:login:748948791515454518e7645f368ca"}]
 name随便填，方便自己辨认，ck填入抓包数据，如需与其它脚本同步使用配置，请自行修改参数名
"""

import time
import requests
import os
import ast


class MTZDZ:
    def __init__(self, cg):
        self.name = cg['name']
        self.headers = {
            'Authorization': cg['ck'],
            'User-Agent': 'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
            'content-type': 'application/json',
            'Accept': '*/*',
            'Origin': 'http://31694066159.tt.bendishenghuochwl1.cn',
            'Referer': 'http://31694066159.tt.bendishenghuochwl1.cn/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh',
        }
        self.s = requests.session()
        self.s.headers = self.headers

    def user_info(self):
        u = 'http://api.mengmorwpt1.cn/h5_share/user/info'
        r = self.s.post(u, json={"openid": 0})
        # print('userinfo '+r.text)
        rj = r.json()
        if rj.get('code') == 200:
            self.nickname = rj.get('data').get('nickname')
            self.points = rj.get('data').get('points')
            res = requests.post('http://api.mengmorwpt1.cn/h5_share/user/sign', headers=self.headers,
                                json={"openid": 0})
            msg = res.json().get('message')
            print(f'当前账号：{self.nickname},积分：{self.points}，签到：{msg}')
            url = 'http://api.mengmorwpt1.cn/h5_share/user/up_profit_ratio'
            payload = {"openid": 0}
            try:
                res = self.s.post(url, json=payload).json()
                # print(res)
                if res.get('code') == 500:
                    raise
                print(f'代理升级：{res.get("message")}')
            except:
                url = 'http://api.mengmorwpt1.cn/h5_share/user/task_reward'
                for i in range(0, 8):
                    payload = {"type": i, "openid": 0}
                    res = self.s.post(url, json=payload).json()
                    if '积分未满' in res.get('message'):
                        break
                    if res.get('code') != 500:
                        print('主页奖励积分：' + res.get('message'))
                    i += 1
                    time.sleep(0.5)
        else:
            print('获取账号信息异常，检查cookie是否失效')
            return False

    def huoke_comment(self):
        while True:
            url = 'http://api.mengmorwpt1.cn/h5_share/daily/get_huoke_comment'
            data = {"openid": 0}
            res = self.s.post(url, json=data).json()
            # print(f'gethuoke {res}')
            if res.get('code') != 200:
                print(res.get('message'))
                return False
            link = res.get('data').get('link')
            copyContent = res.get('data').get('copyContent')
            task_id = res.get('data').get('task_id')
            is_need_create = res.get('data').get('is_need_create')
            data1 = {"task_id": task_id, "link": link, "copyContent": "", "is_need_create": is_need_create, "openid": 0}
            if not task_id or len(str(task_id)) < 5:
                print('这是检测号,跳过')
                # send(f'{self.name}每天赚发私信检测\n{link}\n\n{copyContent}')
                return False
            time.sleep(10)
            url = 'http://api.mengmorwpt1.cn/h5_share/daily/huoke_comment'
            res = self.s.post(url, json=data1).json()
            print('huoke ',res)
            if res.get('code') != 200:
                print(res.get('message'))
                return False

    def run(self):
        self.user_info()
        self.huoke_comment()


if __name__ == '__main__':
    mtzck = os.getenv('mtzck')
    try:
        mtzck = ast.literal_eval(mtzck)
    except:
        pass
    for i in mtzck:
        try:
            dz = MTZDZ(i)
            dz.run()
        except Exception as e:
            print(e)
            continue
