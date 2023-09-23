# -*- coding: utf-8 -*-
# 泉站订水
# Author: kk
# date：2023/9/16 13:05
"""
入口：#小程序://泉站订水/pK1FZkwN2CYIbYe
复制到微信打开
time：2023.9.8
cron: 12 7,17 * * *
new Env('泉站签到');
每日签到0.2 满1元自动提现
抓包域名: admin.dtds888.com  请求体里面的token 提现需要填入微信实名姓名
环境变量: qztoken=token的值#姓名
多账号新建变量或者用 & 分开
"""
import json
import requests
from datetime import datetime
import os

qwbotkey = os.getenv('qwbotkey')
qztoken = os.getenv("qztoken")

def ftime():
    t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return t


def send(msg, title='通知', url=None):
    if not url:
        data = {
            "msgtype": "text",
            "text": {
                "content": f"{title}\n\n{msg}\n\n本通知by：https://github.com/kxs2018/xiaoym\n惜之酱tg频道:https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",
                # "mentioned_list": ["@all"],
            }
        }
    else:
        data = {"msgtype": "news",
                "news": {"articles":
                             [{"title": title, "description": msg, "url": url,
                               "picurl": 'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'
                               }]}}
    whurl = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'
    resp = requests.post(whurl, data=json.dumps(data)).json()
    if resp.get('errcode') != 0:
        print('消息发送失败，请检查key和发送格式')
        return False
    return resp


class QZQD:
    def __init__(self, ck):
        self.token = ck.split('#')[0]  # 账号的token
        self.name = ck.split('#')[1] if ck.split('#')[1] else None  # 用户名字
        self.nicename = None
        self.ye = None  # 余额
        self.ts = None  # 时间戳
        self.msg = ''  # 推送消息
        # 请求头
        self.headers = {
            "Host": "admin.dtds888.com",
            "Connection": "keep-alive",
            "Content-Length": "505",
            "charset": "utf-8",
            "User-Agent": "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/9516 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/3gnet Language/zh_CN ABI/arm64 MiniProgramEnv/android",
            "content-type": "application/json",
            "Accept-Encoding": "gzip, compress, br, deflate",
            "Referer": "https://servicewechat.com/wxcee27346cf362ba6/24/page-frame.html"
        }
        # 请全体
        self.data = {
            'deviceType': 'wxapp',
            'timestamp': self.ts,
            'noncestr': '',
            'token': self.token,
            'sign': '',
            'version': 1.00
        }

    def login(self):
        """登录获取用户信息"""
        try:
            # 设置当前时间戳
            self.ts = int(datetime.now().timestamp())

            # 请求用户信息的url
            url = "https://admin.dtds888.com/api/index/user/index"

            # 请求
            response = requests.post(url, headers=self.headers, json=self.data)

            # 获取请求返回的响应
            if response.status_code == 200:
                # 获取用户昵称
                nickname = response.json()['data']['user']['user_nickname']
                self.nickname = nickname
                xx = f'{self.nickname}: 登录成功！'
                print(xx)
                self.msg += xx + '\n'
                # 获取余额
                return True
            else:
                print(f'登录失败')
                print(response.json())
                return False
        except Exception as e:
            print(f'登录异常：{e}')
            return False

    def sign(self):
        """签到"""
        try:
            self.ts = int(datetime.now().timestamp())
            url = "https://admin.dtds888.com/api/index/user/SignIn"
            response = requests.post(url, headers=self.headers, json=self.data)
            jg = response.json()
            if '成功' in jg['msg']:
                xx = f"{self.nickname}: {jg['msg']}"
                print(xx)
                self.msg += xx + '\n'
            elif '重复' in jg['msg']:
                xx = f"{self.nickname}: {jg['msg']}"
                print(xx)
                self.msg += xx + '\n'
            else:
                print(jg)
        except Exception as e:
            print(f'签到异常：{e}')
            return False

    def money(self):
        """查询余额"""
        try:
            # 设置当前时间戳
            self.ts = int(datetime.now().timestamp())

            # 请求用户信息的url
            url = "https://admin.dtds888.com/api/index/user/index"

            # 请求
            response = requests.post(url, headers=self.headers, json=self.data)

            # 获取请求返回的响应
            if response.status_code == 200:
                ye = response.json()['data']['user']['balance']
                self.ye = ye
                xx = f'余额: {self.ye}'
                print(xx)
                self.msg += xx + '\n'
            else:
                print(f'登录失败')
                print(response.json())
        except Exception as e:
            print(f'获取余额异常：{e}')

    def tx(self):
        """提现"""
        try:
            self.ts = int(datetime.now().timestamp())
            data = {
                'money': '1',  # 提现金额
                'name': self.name,  # 提现名字
                'deviceType': 'wxapp',
                'timestamp': self.ts,
                'noncestr': '',
                'token': self.token,
                'sign': '',
                'version': '1.00'
            }

            url = 'https://admin.dtds888.com/api/index/user/cashPost'
            if self.ye >= '1':
                response = requests.post(url, headers=self.headers, json=data)
                msg = response.json()['msg']
                xx = f'提现: {msg}'
                print(xx)
                self.msg += xx + '\n'
            else:
                xx = "提现: 钱包余额不足"
                print(xx)
                self.msg += xx + '\n'
        except Exception as e:
            print(f'提现异常：{e}')
            self.msg += f'提现异常：{e}'

    def run(self):
        if self.login():
            self.sign()
            self.money()
            if not self.name:
                print('没有设置姓名，不执行提现')
                self.msg += '没有设置姓名，不执行提现\n'
            else:
                self.tx()
            return self.msg


if __name__ == '__main__':
    token_list = qztoken.split('&')
    msgbox = []
    # 遍历列表
    for token in token_list:
        qd = QZQD(token)
        msg = qd.run()
        msgbox.append(msg)
    a = send('\n'.join(msgbox), "泉站签到通知")
    if a.get('errcode') == 0:
        print('企业微信群消息推送成功')
    print("-" * 50 + '\nhttps://github.com/kxs2018/xiaoym\nBy:惜之酱\n' + '-' * 50)
