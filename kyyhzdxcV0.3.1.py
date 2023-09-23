# -*- coding: utf-8 -*-
# 悦悦互助
# Author: kk
# date：2023/9/20 13:27
"""
入口 https://x.moonbox.site/?rSxik7B66347#/?recommend=HU1CXW006K0
抓包 cookie里的apptoken值
export yyhzck="D1C13xxxxA7091D49CB3DFBxxxxxxxxxxxx6CB7032FDxxxxxxx"
多账号用&分隔
提现需先行绑定手机，“我的”页面“神秘功能”会变成提现
"""
import os
import random
import requests
import threading
from queue import Queue
import time

"""实时日志开关"""
printf = 1
"""1为开，0为关，默认关"""

"""调试日志开关"""
debug = 0
"""1为开，0为关，默认关"""

"""设置线程数量"""
max_workers = 5
"""设置多少，最多有多少个号在同时任务"""

"""设置提现标准"""
txbz = 50  # 不低于30，平台的提现标准为30
"""设置为50，即为5毛起提"""

def debugger(text):
    if debug:
        print(text)


def printlog(text):
    if printf:
        print(text)


class YYHZ:
    def __init__(self, index, ck):
        self.index = index
        self.msg = ''
        self.cwd = None
        self.s = requests.session()
        self.s.headers = {'Host': 'x.moonbox.site', 'Connection': 'keep-alive', 'Accept': 'application/json',
                          'Cache-Control': 'no-cache',
                          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8431 Flue',
                          'FastAuthorization': '', 'Content-Type': 'application/json', 'Sec-Fetch-Site': 'same-origin',
                          'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Accept-Encoding': 'gzip, deflate, br',
                          'Accept-Language': 'zh-CN,zh;q=0.9',
                          "cookie": f'app-token={ck}'}

    def userinfo(self):
        url = 'https://x.moonbox.site/api/user/info'
        res = self.s.get(url).json()
        debugger(f'userinfo {res}')
        data = res.get('data')
        if not data:
            printlog(f'账号{self.index} ck失效，请重新获取ck')
            self.msg += f'账号{self.index} ck失效，请重新获取ck\n'
            return False
        self.nickname = data.get('nickname')
        balance = data.get('balance')
        recommendCode = data.get('recommendCode')
        printlog(f"账号：{self.nickname}，现有豆豆{balance}，邀请码：{recommendCode}")
        self.msg += f"账号：{self.nickname}，现有豆豆{balance}，邀请码：{recommendCode}\n"
        return True

    def read(self):
        for i in range(30):
            url = "https://x.moonbox.site/api/article/read"
            data = {
                "articleId": 344,
                "articleUser": 114,
                "bigTop": 0,
                "publishId": 349,
                "viewNum": "146",
                "readType": 0,
                "channel": "0",
                "readerDate": 1695174062000,
                "seconds": 34
            }
            response = self.s.post(url, json=data).json()
            debugger(f'read {response}')
            if response['code'] == 0:
                printlog(f"{self.nickname} {response['msg']}")
                self.msg += f"{self.nickname} {response['msg']}\n"
                break
            elif response['code'] == 1:
                printlog(f"{self.nickname} 阅读成功，获得豆豆{response['data']}\t\tx {i + 1}")
                self.msg += f"{self.nickname} 阅读成功，获得豆豆{response['data']}\t\tx {i + 1}\n"
                t = random.randint(6, 10)
                time.sleep(t)

    def withdrawinfo(self):
        url = 'https://x.moonbox.site/api/account/withdraw/info'
        res = self.s.get(url).json()
        debugger(f'withdrawinfo {res}')
        if res.get('code') == 1:
            self.cwd = res.get('data').get('canWithdrawDou')
            frz = res.get('data').get('freezeDou')
            printlog(f'{self.nickname}:可提现豆子{self.cwd}，冻结豆子{frz}')
            self.msg += f'可提现豆子{self.cwd}，冻结豆子{frz}\n'
            if self.cwd < txbz:
                printlog(f'{self.nickname}:可提现豆子小于{txbz}，不提现')
                self.msg += f'可提现豆子小于{txbz}，不提现\n'
                return False
            return True
        else:
            printlog(f'{self.nickname}:获取提现信息错误，未认证手机，认证手机后重新抓包')
            self.msg += f'获取提现信息错误，未认证手机，认证手机后重新抓包\n'
            return False

    def withdraw(self):
        url = 'https://x.moonbox.site/api/account/cash/withdraw'
        data = {"dou": self.cwd}
        res = self.s.post(url, json=data).json()
        debugger(f'withdraw {res}')
        if res.get('data'):
            printlog(f'{self.nickname} 提现成功，提现金额{self.cwd / 100}元，耐心等待审核到账')
            self.msg += f'提现成功，提现金额{self.cwd / 100}元，耐心等待审核到账\n'
        else:
            printlog(f'{self.nickname} 提现失败,原因：{res.get("msg")}')
            self.msg += f'提现失败,原因：{res.get("msg")}\n'

    def run(self):
        self.msg += "*" * 50 + '\n'
        if not self.userinfo():
            return False
        self.read()
        if self.withdrawinfo():
            self.withdraw()
        if not printf:
            print(self.msg.strip())


def yd(q):
    while not q.empty():
        num, ck = q.get()
        api = YYHZ(num, ck)
        api.run()


if __name__ == '__main__':
    yyhzck = os.getenv('yyhzck')
    yyhzck = yyhzck.split('&')
    q = Queue()
    threads = []
    for num, c in enumerate(yyhzck, start=1):
        print(num, c)
        q.put([num, c])
    for i in range(max_workers):
        t = threading.Thread(target=yd, args=(q,))
        t.start()
        threads.append(t)
        time.sleep(5)
    for thread in threads:
        thread.join()
    print("-" * 50 + '\nhttps://github.com/kxs2018/xiaoym\nBy:惜之酱\n' + '-' * 50)
