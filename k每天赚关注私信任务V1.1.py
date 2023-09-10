# -*- coding: utf-8 -*-
# 每天赚关注私信任务V1.1
# Author: kk
# date：2023/9/7 16:24
"""
每天赚 入口：http://tg.1694070002.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=113565
关注私信任务v1.1，一天上限10，含检测号，遇到检测号会跳过，无需推送。
因为遇到过第一次跳过检测号，几小时之后再次运行能补上这一次，建议一天运行2次，间隔长一些。
附带个人主页签到、领取赠送积分、提升代理等功能。
uid为以后不能跳过检测号时增加推送的wxpusher的uid，填不填无所谓。
配置设置下面两种二选一（使用https://github.com/kxs2018/yuedu仓库脚本无需再配置）
（1）青龙(2.16.1)配置文件里添加，其它版本可能要删除三对单引号
export mtzck='''[{"name": "", "ck": ""，"uid":""},
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
 name随便填，方便自己辨认，ck填入抓包数据，兼容A佬每天赚mtzconfig设置
"""

import time
import requests
import os
import ast

try:
    import config
except:
    pass


class MTZDZ:
    def __init__(self, cg):
        self.name = cg['name']
        self.headers = {            
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
        self.s.headers.update({'Authorization': cg['ck']})

    def user_info(self):
        u = 'http://api.mengmorwpt1.cn/h5_share/user/info'
        r = self.s.post(u, json={"openid": 0})
        # print('userinfo '+r.text)
        rj = r.json()
        if rj.get('code') == 200:
            self.nickname = rj.get('data').get('nickname')
            self.points = rj.get('data').get('points') - rj.get('data').get('withdraw_points')
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
        i = 1
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
            # print('huoke ', res)
            if res.get('code') != 200:
                print(res.get('message'))
                return False
            else:
                print(f'第{i}次任务 成功,获得积分20')
                i += 1

    def run(self):
        self.user_info()
        self.huoke_comment()


if __name__ == '__main__':
    mtzck = os.getenv('mtzck') or os.getenv('mtzconfig')
    if not mtzck:
        try:
            mtzck = config.mtzck or config.mtzconfig
        except:
            print('没有找到ck配置，退出')
            exit()
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
