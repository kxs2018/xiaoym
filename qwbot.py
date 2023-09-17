# -*- coding: utf-8 -*-
# QywxNotify
# Author: kk
# date：2023/8/22 14:53
import json
import os
import random
import requests
import config
import datetime
qwbotkey = config.qwbotkey



def format_time():
    t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return t


def send(msg, title='通知', url=None):
    if not url:
        data = {
            "msgtype": "text",
            "text": {
                "content": f"{title}\n\n{msg}\n\n本通知by：https://github.com/kxs2018/yuedu\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{format_time()}",
                # "mentioned_list": ["@all"],
            }
        }
    else:
        data = {
            "msgtype": "news",
            "news": {
                "articles": [
                    {
                        "title": title,
                        "description": msg,
                        "url": url,
                        "picurl": 'https://i.ibb.co/7b0WtQH/17-32-15-2a67df71228c73f35ca47cabaa826f17-eb5ce7b1e.png'
                    }
                ]
            }
        }
    whurl = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'
    resp = requests.post(whurl, data=json.dumps(data)).json()
    if resp.get('errcode') != 0:
        print('消息发送失败，请检查key和发送格式')
        return False
    return resp


if __name__ == '__main__':
    a = send(digest='这是一个测试', title='测试', url='https://192.168.1.1')
