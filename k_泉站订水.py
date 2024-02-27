# -*- coding: utf-8 -*-
# 泉站订水
# date：2024/1/2
"""
入口：#小程序://泉站订水/pK1FZkwN2CYIbYe
复制到微信打开
time：2024/1/2
cron: 12 7,17 * * *
new Env('泉站签到');
抓包域名: microuser.quanzhan888.com  请求头Authcode  Authorization
环境变量: qztoken = Authcode#Authorization
多账号新建变量或者用 & 分开
"""
import json
import requests
from datetime import datetime
import os
## qztoken = Authcode#Sign#Authorization#name1
qwbotkey = os.getenv('qwbotkey')
qztoken = os.getenv('qztoken')

def ftime():
    t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return t
def send(msg, title='通知', url=None):
    if not url:
        data = {
            "msgtype": "text",
            "text": {
                "content": f"{title}\n\n{msg}\n通知时间：{ftime()}",
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
        ## qztoken = Authcode#Authorization#name1
        self.authcode = ck.split('#')[0]  # 账号的authcode
        self.authorization = ck.split('#')[1]  # 账号的authorization
        #self.name = ck.split('#')[2] if ck.split('#')[2] else None  # 用户名字
        self.nicename = None
        self.ye = None  # 余额
        self.ts = None  # 时间戳
        self.msg = ''  # 推送消息
        # 请求头
        self.headers = {
            "Host": "microuser.quanzhan888.com",
            "Connection": "keep-alive",
            "Content-Length": "2",
            "Product": "shop",
            "content-type": "application/x-www-form-urlencoded",
            "charset": "utf-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819)XWEB/8519",
            "Platform": "wx",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://servicewechat.com/wxcee27346cf362ba6/28/page-frame.html",
            'Authcode': self.authcode,
            'Sign': '99914b932bd37a50b983c5e7c90ae93b',
            'Authorization': self.authorization,
            'timestamp': self.ts
        }
        self.data = {
        }

    def login(self):
        """登录获取用户信息"""
        try:
            # 设置当前时间戳
            self.ts = int(datetime.now().timestamp())
            # 请求用户信息的url
            url = "https://microuser.quanzhan888.com/user/get-user"
            # 请求
            response = requests.post(url, headers=self.headers, json=self.data)
            # 获取请求返回的响应
            if response.json()['code'] == 0:
                # 获取用户昵称、余额
                nickname = response.json()['data']['nickname']
                ye = response.json()['data']['total_balance']
                self.nickname = nickname
                self.ye = ye
                xx = f'{self.nickname}: 登录成功！当前红包余额: {self.ye}'
                print(xx)
                self.msg += xx + '\n'
                return True
            else:
                print(f'登录失败')
                print(response.json())
                return False
        except Exception as e:
            print(f'登录异常：{e}')
            self.msg += f'登录异常：{e}\n'
            return False

    def signing(self):
        """签到"""
        try:
            self.ts = int(datetime.now().timestamp())
            url = "https://microuser.quanzhan888.com/user/do-sign"
            response = requests.post(url, headers=self.headers, json=self.data)
            jg = response.json()
            if response.json()['code'] == 0:
                xx = f"{self.nickname}: 签到成功！"
                print(xx)
                self.msg += xx + '\n'
            else:
                print(jg)
        except Exception as e:
            print(f'签到异常：{e}')
            self.msg += (f'签到异常：{e}\n')
            return False

    def run(self):
        if self.login():
            self.signing()
        return self.msg

if __name__ == '__main__':
    print('本脚本由群友“肥七”更新')
    ck_list = qztoken.split('&')
    msgbox = []
    # 遍历列表
    for ck in ck_list:
        qd = QZQD(ck)
        msg = qd.run()
        msgbox.append(msg)
    if qwbotkey:
        a = send('\n'.join(msgbox), "泉站签到通知")
        if a.get('errcode') == 0:
            print('企业微信群消息推送成功')
