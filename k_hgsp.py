# -*- coding: utf-8 -*-
"""
new Env('火锅并发版');
变量 hgsp_cookie 账号和密码以@隔开 账号@密码
多账号以&隔开 账号1@密码1&账号2@密码2
入口：http://dss95.ovzz.cn/20
教程：https://lovepet.space/index.php/archives/56/
"""
try:
    from config import hgsp_config  # 可自行在config.py添加设置
except:
    hgsp_config = {
        'hgsp_wd': 0,  # 自动提现设置 1开启自动提现，0关
        'hgsp_ex': 0,  # 自动兑换储蓄金 1开，0关
        'VIDEO_F' : 24, # 视频次数
        'last_coin': 2000, # 保留金币数量，防止想要实名的时候没有金币
        'max_workers':5,  # 并发数量设置
    }
    """可以把hgsp_config这段添加到config.py"""

hgsp_ex = hgsp_config['hgsp_ex']
hgsp_wd = hgsp_config['hgsp_wd']
VIDEO_F = hgsp_config['VIDEO_F']
last_coin = hgsp_config['last_coin']
max_workers = hgsp_config['max_workers']

import requests
import time
import os
import sys
import threading
from queue import Queue

class HgSp():   
    def __init__(self,index, account, video_f=VIDEO_F):
        account = account.split('@')
        self.index = index
        self.video_f = video_f
        self.coin = None
        self.today_coin = None
        self.balance = None
        self.s = requests.Session()
        self.s.headers = {
            'os': 'android',
            'Version-Code': '1',
            'Client-Version': '1.0.2',
            'datetime': '2023-11-12 04:40:19.023',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'www.huoguo.video',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.12.13',
        }
        self.data = {
            'login': account[0],
            'type': '2',
            'verifiable_code': '',
            'password': account[1]
        }

    # 登录
    def login(self):
        time.sleep(0.5)
        login_response = self.s.post('http://www.huoguo.video/api/v2/auth/login', 
                                           data=self.data).json()
        if "access_token" in login_response:
            token = login_response['access_token']
            del self.s.headers['Content-Type']
            self.s.headers['Authorization'] = f"Bearer {token}"
            response = self.s.get('http://www.huoguo.video/api/v2/user').json()
            print(f"账号【{self.index}】【登录成功】当前用户:{response['name']}")
            return True
        else:
            print(f"账号【{self.index}】{login_response['message']}")
            return False

    # 观看视频
    def watch_video(self):
        time.sleep(0.5)
        for i in range(self.video_f):
            response = self.s.get('http://www.huoguo.video/api/v2/hgb/recive').json()
            print(f'账号【{self.index}】【观看视频】{response["message"]}')
            if '火锅币' not in response['message']:
                break
            time.sleep(10)            
            url = "http://www.huoguo.video/api/v2/hgb/store-view"
            data = {
                    'duration': 200
                }
            response =self.s.post(url, data=data).json()
            ttime = response['message']   
            time.sleep(5)         
            if response['message']=='今日已完成':
                continue
            print(f"账号【{self.index}】【刷时长】{ttime}")            
        self.get_today_info()

    # 获取今日信息
    def get_today_info(self):
        response = self.s.get('http://www.huoguo.video/api/v2/hgb/detail').json()
        self.coin = response['coin']
        self.today_coin = response['today_coin']
        print(f"账号【{self.index}】【观看视频】今日获得火锅币:{self.today_coin},当前总火锅币:{self.coin}")

    # 兑换储蓄金
    def exchange_saving(self):
        time.sleep(0.5)
        data = {'count': float(self.coin) - last_coin}
        response = self.s.post('http://www.huoguo.video/api/v2/hgb/exchange-savings', 
                                     data=data).json()
        if "amount" in response:
            print(f"账号【{self.index}】【兑储蓄金】获得储蓄金{response['amount']}")
        else:
            print(f"账号【{self.index}】【兑储蓄金】{response['message']}")

    # 释放储蓄金
    def open_gold(self):
        time.sleep(2)
        url = "http://www.huoguo.video/api/v2/hgb/open"
        response = self.s.get(url).json()
        amount = response.get('amount')
        if amount:
            print(f"账号【{self.index}】【释放金币】今日释放{amount}")
        else:
            print(f"账号【{self.index}】【释放金币】{response['message']}")


    # 查询信息
    def get_info(self):
        response = self.s.get('http://www.huoguo.video/api/v2/hgb/piggy').json()
        self.balance = response['balance']
        print(f"账号【{self.index}】【查询信息】当前总储蓄金:{response['saving']} 可提现余额为：{response['balance']}")

    # 提现
    def withdraw(self):
        time.sleep(0.5)
        balance_float = float(self.balance)
        amount = "{:.2f}".format(balance_float)
        data = {'amount': amount}
        response = self.s.post("http://www.huoguo.video/api/v2/wallet/withdraw", 
                                     data=data).json()
        print(response)


    def run(self):
        if self.login():
            self.watch_video()
            self.get_info()
            if hgsp_ex:
                self.exchange_saving()
            self.open_gold()
            if hgsp_wd:
                self.withdraw()
def hg(q):
    while not q.empty():
        index,account = q.get()
        a = HgSp(index,account)
        a.run()


# 主程序
def main():
    a = os.getenv("hgsp_cookie")    
    if not a:
        print('没有获取到账号!')
        return
    account_list = a.split('&')
    print(f'⭐⭐获取到{len(account_list)}个账号')
    threads=[]
    q = Queue()
    for index, account in enumerate(account_list, start=1):
        q.put([index,account])
    for i in range(max_workers):
        t = threading.Thread(target=hg, args=(q,))
        t.start()
        threads.append(t)
        time.sleep(0.5)
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
    sys.exit()
