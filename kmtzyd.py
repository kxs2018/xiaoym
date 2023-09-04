# -*- coding: utf-8 -*-
# kmtzyd
# Author: kk
# date：2023/9/4 17:28
"""
美添赚
活动入口,微信打开：http://tg.1693634614.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=113565
运行前先按照config.py的要求填好设置
自动检测，并推送
达到标准自动提现
"""
import random
import requests
import config
import time
from getmpinfo import getmpinfo
from qwbot import send
from check import testsend

'_____________________________________________________________'
'下面这段如果运行过check.py成功发送消息后可以注释或删除'
# 每次运行会检测推送，如果配置正确，可以注释或删除这块代码
if not testsend():
    print('没有获取到机器人key，请检查config.py里有没有设置qwbotkey')
    exit()
'上面这段如果运行过check.py成功发送消息后可以注释或删除'
'______________________________________________________________'

checkDict = [
    'MzkzNjI3NDAwOA==',
]
mtzck = config.mtzck
if mtzck is None:
    print('你没有填入mtzck，咋运行？')
    exit()


class MTZYD:
    def __init__(self, cg):
        self.headers = {
            'Authorization': cg,
            'User-Agent': 'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
            'content-type': 'application/json',
            'Accept': '*/*',
            'Origin': 'http://71692693186.tt.bendishenghuochwl1.cn',
            'Referer': 'http://71692693186.tt.bendishenghuochwl1.cn/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh',
        }

    def user_info(self):
        u = 'http://api.mengmorwpt1.cn/h5_share/user/info'
        r = requests.post(u, headers=self.headers, json={"openid": 0})
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
                res = requests.post(url, headers=self.headers, json=payload).json()
                if res.get('code') == 500:
                    raise
                print(f'代理升级：{res.get("message")}')
            except:
                url = 'http://api.mengmorwpt1.cn/h5_share/user/task_reward'
                for i in range(0, 8):
                    payload = {"type": i, "openid": 0}
                    res = requests.post(url, headers=self.headers, json=payload).json()
                    if '积分未满' in res.get('message'):
                        break
                    if res.get('code') != 500:
                        print('主页奖励积分：' + res.get('message'))
                    time.sleep(0.5)
            return True
        else:
            print('获取账号信息异常，检查cookie是否失效')
            return False

    def read_info(self):
        u = f'http://api.mengmorwpt1.cn/h5_share/daily/get_read'
        r = requests.post(u, headers=self.headers, json={"openid": 0})
        print('readinfo ' + r.text)
        rj = r.json()
        if rj.get('code') == 200:
            self.link = rj.get('data').get('link')
            return True
        elif rj.get('code') == 500:
            print(rj.get('message'))
            return False
        else:
            print('获取阅读链接异常异常')
            return False

    def gettaskinfo(self, infolist):
        for i in infolist:
            if i.get('url'):
                return i

    def read(self):
        print('阅读开始')
        h = {
            'Host': 'api.wanjd.cn',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'Origin': 'http://uha294070.294070nwq.com.294070u.meitianzhuan2.cn',
            'Referer': 'http://uha294070.294070nwq.com.294070u.meitianzhuan2.cn/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh',
        }
        self.num = None
        pt = 0
        while True:
            if self.num == 0:
                break
            print('-' * 50)
            u1 = 'https://api.wanjd.cn/wxread/articles/tasks'
            p = {'href': self.link}
            r = requests.post(u1, headers=h, data=p)
            print('read '+r.text)
            rj = r.json()
            code = rj.get('code')
            if code == 200:
                if pt == 0:
                    self.num = len(rj.get('data'))
                    pt = 1
                taskinfo = self.gettaskinfo(rj.get('data'))
                url = taskinfo.get('url')
                id = taskinfo.get('id')
                mpinfo = getmpinfo(url)
                print('开始阅读 ' + mpinfo['text'])
                biz = mpinfo['biz']
                if not mpinfo:
                    send(title=f'{self.nickname}美添赚过检测', url=url, digest=f'{url}文章获取失败')
                    return False
                if biz in checkDict:
                    send(title=f'{self.nickname}美添赚过检测', url=url, digest=f'{mpinfo["text"]}\t{url}')
                    print('发送通知，暂停50秒')
                    time.sleep(50)
                tsm = random.randint(6, 10)
                print(f'本次模拟读{tsm}秒')
                time.sleep(tsm)
                u1 = 'https://api.wanjd.cn/wxread/articles/three_read'
                p1 = {'id': id, 'href': self.link}
                r = requests.post(u1, headers=h, data=p1).json()
                if r.get('code') == 200:
                    print('阅读成功')
                self.num -= 1
                if r.get('code') == 500:
                    print(r.get('message'))
                    break
        curl = 'https://api.wanjd.cn/wxread/articles/check_success'
        cp = {'type': 1, 'href': self.link}
        requests.post(curl, headers=h, data=cp)
        print('本次阅读已完成')

    def withdraw(self):
        if self.points < 1000:
            print('没有达到提现标准')
            return False
        u = 'http://api.mengmorwpt1.cn/h5_share/user/withdraw'
        r = requests.post(u, headers=self.headers).json()
        print('提现结果', r.get('message'))

    def run(self):
        if not self.user_info():
            return False
        if self.read_info():
            self.read()
            self.user_info()
        self.withdraw()


if __name__ == '__main__':
    for i in mtzck:
        try:
            print('=' * 50 + f'\n帐号：{i["name"]}开始任务\n' + '=' * 50)
            api = MTZYD(i['ck'])
            api.run()
            print(f'\n帐号：{i["name"]}本次任务完成\n' + '=' * 50)
            time.sleep(5)
        except Exception as e:
            print(e)
            continue
