# -*- coding: utf-8 -*-
# 天瑞地安共富签
# Author: kk
# date：2023/9/14 11:59
"""
本脚本适用于天瑞地安APP共富签
连签奖励
抓包 https://crm.rabtv.cn，在请求体内找到Authorization的值（Bearer xxxxxxxxxx）
青龙配置文件添加：
-------------------------------------
多个账号增加大括号即可
export trdack="[{'ck':'Bearer xxxxxxxxxx'},{'ck':'Bearer xxxxxxxxxx'}]"
-------------------------------------
推送配置：
-------------------------------------
export qwbotkey="xxx"
参考 https://github.com/kxs2018/yuedu/blob/main/获取企业微信群机器人key.md 获取key，并关注插件！！！
-------------------------------------
"""
import datetime
import json
import time
import requests
from random import randint
import os
import ast


def ftime():
    t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return t


def send(msg, title='通知', url=None):
    if not url:
        data = {
            "msgtype": "text",
            "text": {
                "content": f"{title}\n\n{msg}\n\n本通知by：https://github.com/kxs2018/xiaoym\n[点击加入惜之酱tg频道](https://t.me/+uyR92pduL3RiNzc1)\n通知时间：{ftime()}",
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


class TRDA:
    def __init__(self, ck):
        self.s = requests.session()
        self.s.headers = {"Authorization": ck['ck'],
                          "User-Agent": "Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36;xsb_ruian;xsb_ruian;2.31.742;native_app",
                          }  # user-agent 可换成自己的
        self.msg = ''

    def user_info(self):
        url = 'https://crm.rabtv.cn/v2/index/userInfo'
        res = self.s.post(url).json()
        # print('userinfo ', res)
        if res.get('code') == 1:
            self.un = res.get('data').get('username')
            money = res.get('data').get('common_user').get('money')
            num = ''.join(res.get('data').get('continue_sign_num'))
            if num.startswith('0'):
                num = num[1:]
            total_sign_num = res.get('data').get('total_sign_num')
            m = f'【{self.un}】：当前红包{money}元，已连续签到{num}天，总签到{total_sign_num}天'
            print(m)
            self.msg += f'{m}\n '
            return True
        else:
            print(res.get('msg'))
            return False

    @staticmethod
    def gettype(type):
        typedict = {'redbag': '红包', 'score': '积分'}
        typec = typedict.get(type)
        return typec if typec else type

    def signin(self):
        global msg
        sign_url = 'https://crm.rabtv.cn/v2/index/signIn'
        res = self.s.post(sign_url).json()
        # print('signin ', res)
        if res.get('code') == 0:
            msg = res.get("msg")
            if 'plz-check-mobile' in msg:
                send(f'{self.un} 天瑞地安签到需验证手机，请手动签到')
        elif res.get('code') == 1:
            ptype = res.get('data')['type']
            p = res.get('data').get(ptype)
            num = res.get('data').get('continue_sign_num')
            msg = f'签到成功，获得{p}{self.gettype(ptype)}，连续签到{num}天'

        msg = f'【{self.un}】：{msg}'
        print(msg)
        self.msg += f'{msg}\n '

    def get_prize(self):
        pids = [124201, 125288, 127559, 131076]
        url = 'https://crm.rabtv.cn/v2/user/getPrizeV'
        for pid in pids:
            res = self.s.post(url, data={'id': pid}).json()
            # print(f'getprize ', res)
            if res.get('code') == 0:
                continue
            elif res.get('code') == 1:
                ptype = res.get('data')['type']
                p = res.get('data').get(ptype)
                m = f'【{self.un}】：连续签到奖励，获得{p} {self.gettype(ptype)}'
                print(m)
                self.msg += f'{m}\n '

    def chou(self):
        url = 'https://guess.rabtv.cn/v1/task/do'
        for i in range(1, 5):
            data = {'id': i}
            res = self.s.get(url, data=data).json()
            print('task_current ', res)
            if res.get('done'):
                m = f'[任务{i}]抽奖完成，获得红包{res.get("v")}元'
                self.msg += m + '\n'
                print(m)
            elif res.get('code') == 0:
                m = f'[任务{i}]：{res.get("msg")}'
                self.msg += m + '\n'
                print(m)
            time.sleep(randint(3, 6))

    def run(self):
        if self.user_info():
            self.signin()
            self.get_prize()
            self.chou()
            self.msg += '-' * 20 + '\n'
            return self.msg


def ran_time():
    t1 = randint(3, 10)
    t2 = randint(3, 10)
    t1 **= 1.5
    t2 **= 2
    t = randint(int(t1 * 8), t2 * 15) if int(t1 * 8) < t2 * 15 else randint(t2 * 15, int(t1 * 8))
    return t


def get_ver():
    ver = 'k天瑞地安共富签 V1.3.2'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
    res = requests.get('https://gcore.jsdelivr.net/gh/kxs2018/xiaoym@main/ver.json', headers=headers).json()
    v1 = ver.split(' ')[1]
    v2 = res.get('version').get(ver.split(' ')[0])
    msg = f"当前版本 {v1}，仓库版本 {v2}"
    if v1 < v2:
        msg += '\n' + '请到https://github.com/kxs2018/xiaoym下载最新版本'
    return msg


if __name__ == '__main__':
    print("-" * 50 + f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n' + '-' * 50)
    msg = ''
    qwbotkey = os.getenv('qwbotkey')
    trdack = os.getenv('trdack')
    try:
        trdack = ast.literal_eval(trdack)
    except:
        pass
    t = int(ran_time() / 10)
    print(f'{t}秒后开始签到')
    time.sleep(t)
    for i, j in enumerate(trdack, start=1):
        try:
            api = TRDA(j)
            msg += api.run()
            if j != trdack[-1]:
                t = ran_time()
                print(f'{t}后进行下一个签到')
                time.sleep(t)
        except Exception as e:
            print(f'第{i}个账号签到错误\n\n{e}')
            msg += f'第{i}个账号签到错误\n\n{e}'
            continue
    send(msg, title=f'天瑞地安共富签信息')
