# -*- coding: utf-8 -*-
# kczgm
# Author: kk
# date：2023/9/4 11:45
"""
活动入口,微信打开：http://2502567.pkab.tz6pstg20fnm.cloud/?p=2502567
运行前先按照config.py的要求填好设置
"""

import hashlib

import requests

import config
import time
from check import testsend
from getmpinfo import getmpinfo
from qwbot import send

'_____________________________________________________________'
'下面这段如果运行过check.py成功发送消息后可以注释或删除'
# 每次运行会检测推送，如果配置正确，可以注释或删除这块代码
if not testsend():
    print('没有获取到机器人key，请检查config.py里有没有设置qwbotkey')
    exit()
'上面这段如果运行过check.py成功发送消息后可以注释或删除'
'______________________________________________________________'
# 获取 czgmck 环境变量值
czgmck = config.czgmck

if czgmck is None:
    print('你没有填入czgmck，咋运行？')
    exit()
else:

    # 输出有几个账号
    num_of_accounts = len(czgmck)
    print(f"获取到 {num_of_accounts} 个账号")

    # 遍历所有账号
    for i in czgmck:
        cookie = 'gfsessionid=' + i['ck']
        name = i['name']
        # 输出当前正在执行的账号
        print(f"\n=======开始执行账号{name}=======")
        current_time = str(int(time.time()))

        # 计算 sign
        sign_str = f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={current_time}'
        sha256_hash = hashlib.sha256(sign_str.encode())
        sign = sha256_hash.hexdigest()
        url = "http://2477726.neavbkz.jweiyshi.r0ffky3twj.cloud/share"
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 9; V1923A Build/PQ3B.190801.06161913; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36 MMWEBID/5635 MicroMessenger/8.0.40.2420(0x28002837) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64",
            "Cookie": cookie
        }

        data = {
            "time": current_time,
            "sign": sign
        }
        response = requests.get(url, headers=headers, json=data).json()
        share_link = response['data']['share_link'][0]
        url = "http://2477726.neavbkz.jweiyshi.r0ffky3twj.cloud/read/info"
        response = requests.get(url, headers=headers, json=data)
        response = response.json()
        if response['code'] == 0:
            remain = response['data']['remain']
            read = response['data']['read']
            print(f"ID:{name}-----钢镚余额:{remain}\n今日阅读量::{read}\n推广链接:{share_link}")
        else:
            print(response['message'])

        print("============开始执行阅读文章============")
        for i in range(30):
            # 计算 sign
            sign_str = f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={current_time}'
            sha256_hash = hashlib.sha256(sign_str.encode())
            sign = sha256_hash.hexdigest()
            url = "http://2477726.9o.10r8cvn6b1.cloud/read/task"
            response = requests.get(url, headers=headers, json=data).json()
            if response['code'] != 0:
                print(response['message'])
                break
            else:
                try:
                    link = response['data']['link']
                    print(f"开始阅读{getmpinfo(link)['text']}")
                    time.sleep(10)
                    url = "http://2477726.9o.10r8cvn6b1.cloud/read/finish"
                    response = requests.post(url, headers=headers, data=data).json()
                    if response['code'] == 0:
                        if response['data']['check'] is False:
                            gain = response['data']['gain']
                            read = response['data']['read']
                            remain = response['data']['remain']
                            print(f"阅读文章成功，获得钢镚[{gain}]，已读{read}\n" + '-' * 50)
                        else:
                            print("check=True,准备执行")
                            url = "http://2477726.9o.10r8cvn6b1.cloud/read/task"
                            response = requests.get(url, headers=headers, json=data).json()
                            if 'data' in response and 'link' in response['data']:
                                link = response['data']['link']
                                print("已将该文章推送至微信请在60s内点击链接完成阅读--60s后继续运行")
                                message = f"出现检测文章！！！请在60s内点击链接完成阅读"
                                send(message, f'{name} 钢镚阅读检测', link)
                                time.sleep(60)
                                url = "http://2477726.9o.10r8cvn6b1.cloud/read/finish"
                                headers = {
                                    "User-Agent": "Mozilla/5.0 (Linux; Android 9; V1923A Build/PQ3B.190801.06161913; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36 MMWEBID/5635 MicroMessenger/8.0.40.2420(0x28002837) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64",
                                    "Cookie": cookie
                                }
                                data = {
                                    "time": current_time,
                                    "sign": sign
                                }
                                response = requests.post(url, headers=headers, data=data).json()
                                if response['code'] == 0:
                                    if response['data']['check'] is False:
                                        gain = response['data']['gain']
                                        print(f"阅读文章成功---获得钢镚[{gain}]" + '-' * 50)
                                    else:
                                        print(f"过检测失败，请尝试重新运行" + '-' * 50)
                                        break
                                else:
                                    print(f"{response['message']}")
                                    break
                    else:
                        print(f"{response['message']}")
                        break

                except KeyError:
                    print(f"获取文章失败,错误未知{response}")
                    break
        print(f"============开始微信提现============")
        url = "http://2477726.84.8agakd6cqn.cloud/withdraw/wechat"

        response = requests.get(url, headers=headers, json=data).json()
        if response['code'] == 0:
            print(response['message'])
        elif response['code'] == 1:
            print(response['message'])
        else:
            print(f"错误未知{response}")
