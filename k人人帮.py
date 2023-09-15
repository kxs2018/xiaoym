# -*- coding: utf-8 -*-
# 人人帮
# Author: kk
# date：2023/8/25 16:35
"""
人人帮入口：http://ebb.maisucaiya.cloud/user/index.html?mid=1694991329391673344
建议一天跑1-2次
自动提现，如遇网络问题够提现标准，会推送消息手动提现
运行前先按照config.py的要求填好设置
----------------------------------------
"""
from random import randint
import requests
import config
import time
from check import testsend
from getmpinfo import getmpinfo
from qwbot import send
import re

'_____________________________________________________________'
'下面这段如果运行过check.py成功发送消息后可以注释或删除'
# 每次运行会检测推送，如果配置正确，可以注释或删除这块代码
if not testsend():
    print('没有获取到机器人key，请检查config.py里有没有设置qwbotkey')
    exit()
'上面这段如果运行过check.py成功发送消息后可以注释或删除'
'______________________________________________________________'

rrbck = config.rrbck
if rrbck is None:
    print('你没有填入rrbck，咋运行？')
    exit()
else:
    # 输出有几个账号
    num_of_accounts = len(rrbck)
    print(f"获取到 {num_of_accounts} 个账号")

checkDict = {'Mzg2Mzk3Mjk5NQ==': ['wz', ''], }


class rrbyd:
    def __init__(self, ck):
        self.ck = ck
        self.headers = {'Host': 'ebb.vinse.cn',
                        'un': self.ck['un'],
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue',
                        'uid': self.ck['uid'],
                        'platform': '0',
                        'token': self.ck['token'],
                        'Origin': 'http://ebb10.twopinkone.cloud',
                        'Referer': 'http://ebb10.twopinkone.cloud/', }         

    def userinfo(self):
        url = 'http://ebb.vinse.cn/api/user/info'
        res = requests.post(url, headers=self.headers, json={"pageSize": 10}).json()
        # print('userinfo ', res)
        if res.get('code') != 0:
            print(f'{self.ck["un"]} cookie失效'+'\n'+'-'*50)
            return 0
        result = res.get('result')
        self.nickname = result.get('nickName')[0:3] + '****' + result.get('nickName')[-4:]
        self.bean_now = result.get('integralCurrent')
        bean_total = result.get('integralTotal')
        print('='*50+f'\n用户：{self.nickname},当前共有帮豆{self.bean_now}，总共获得帮豆{bean_total}'+'\n'+'-'*50)
        return 1

    def sign(self):
        url = 'http://ebb.vinse.cn/api/user/sign'
        res = requests.post(url, headers=self.headers, json={"pageSize": 10}).json()
        # print('sign ', res)
        if res.get('code') == 0:
            print(f'签到成功，获得帮豆{res.get("result").get("point")}'+'\n'+'-'*50)
        elif res.get('code') == 99:
            print(res.get('msg')+'\n'+'-'*50)
        else:
            print('签到错误'+'\n'+'-'*50)

    def reward(self):
        url = 'http://ebb.vinse.cn/api/user/receiveOneDivideReward'
        res = requests.post(url, headers=self.headers, json={"pageSize": 10}).json()        
        print(f"领取一级帮豆：{res.get('msg')}")
        url = 'http://ebb.vinse.cn/api/user/receiveTwoDivideReward'
        res = requests.post(url, headers=self.headers, json={"pageSize": 10}).json()
        print(f"领取二级帮豆：{res.get('msg')}"+'\n'+'-'*50)

    def getentry(self):
        headers = {'Host': 'u.cocozx.cn',
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue",
                   "Origin": "http://ebb10.twopinkone.cloud",
                   "Sec-Fetch-Site": "cross-site",
                   "Sec - Fetch - Mode": "cors",
                   "Sec - Fetch - Dest": "empty"
                   }
        url = f'https://u.cocozx.cn/ipa/read/getEntryUrl?fr=ebb0726&uid={self.ck["uid"]}'
        res = requests.get(url, headers=headers).json()
        # print('getentry ', res)
        result = res.get('result')
        if res.get('code') == 0:
            entryurl = result.get('url')
            self.entryurl = re.findall(r'(http://.*?)/', entryurl)[0]
            # print(entryurl)
        else:
            print("阅读链接获取失败"+'\n'+'-'*50)

    def read(self):
        headers = {
            "Origin": self.entryurl,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue",
            "Host": "u.cocozx.cn"
        }
        for group in range(1, 4):
            print(f'开始第{group}轮阅读\n'+'-'*50)
            data = {"fr": "ebb0726", "uid": self.ck['uid'], "group": group, "un": '', "token": '', "pageSize": 20}
            url = 'http://u.cocozx.cn/ipa/read/read'
            while True:
                res = requests.post(url, headers=headers, json=data)
                # print("read " + res.text)
                result = res.json().get('result')
                taskurl = result.get('url')
                if result['status'] == 10:
                    print('-' * 50)
                    mpinfo = getmpinfo(taskurl)
                    print('开始阅读 ' + mpinfo.get('text'))
                    biznow = mpinfo.get('biz')
                    if biznow in checkDict.keys():
                        # print(taskurl)
                        print('这是检测文章，正在发送通知\n暂停阅读50秒')
                        send(mpinfo['text'], title=f'{self.nickname} 人人帮检测链接', url=taskurl)
                        time.sleep(50)
                    t = randint(7, 10)
                    print(f'模拟随机阅读{t}秒')
                    time.sleep(t)                    
                    self.submit(group)                    
                elif result['status']==50:
                    print('阅读失效')
                    break
                else:
                    # print(f"group {group} 链接获取失败"+'\n'+'-'*50)
                    break
            time.sleep(3)

    def submit(self, group):
        url = 'http://u.cocozx.cn/ipa/read/submit'
        headers = {
            "Origin": self.entryurl,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue",
            "Host": "u.cocozx.cn"
        }
        data = {"fr": "ebb0726", "uid": self.ck['uid'], "group": group, "un": '', "token": '', "pageSize": 20}
        res = requests.post(url, headers=headers, json=data).json()
        # print("submit " , res)
        result = res.get('result')
        daycount = result.get("dayCount")
        dayMax = result.get("dayMax")
        progress = result.get("progress")
        print(f"今日已阅读{daycount}，本轮剩余{progress}，单日最高{dayMax}")

    def tx(self):
        if 5000 <= self.bean_now < 10000:
            txje = 5000
        elif 10000 <= self.bean_now < 50000:
            txje = 10000
        elif 50000 <= self.bean_now < 100000:
            txje = 50000
        elif self.bean_now >= 100000:
            txje = 100000
        else:
            print('帮豆不够提现标准，明儿请早')
            return
        url = f"http://ebb.vinse.cn/apiuser/aliWd"
        params = {"val": txje, "pageSize": 10}
        r = requests.post(url, headers=self.headers, json=params).json()
        if r.get('code') == 0:
            send(f'{self.nickname} 人人帮提现支付宝{txje / 10000}元')

    def run(self):
        if self.userinfo():
            self.sign()
            time.sleep(1)
            self.reward()
            time.sleep(1.5)
            self.getentry()
            time.sleep(1)
            self.read()
            self.userinfo()
        self.tx()
        print('='*50)


if __name__ == '__main__':
    for i in rrbck:
        try:
            yd = rrbyd(i)
            yd.run()
        except Exception as e:
            print(e)
            continue
