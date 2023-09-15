# -*- coding: utf-8 -*-
# QywxNotify
# Author: kk
# date：2023/8/22 14:53
import json
import os
import random
import requests
import config

qwbotkey = config.qwbotkey
imgurl = f''  # f'https://xxxx.com/{random.randint(1, 170)}.jpg' 可选项，每次通知随机图片


def qwbot(digest, title=None, url=None):
    if not title and not url:
        data = {
            "msgtype": "text",
            "text": {
                "content": digest,
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
                        "description": digest,
                        "url": url,
                        "picurl": imgurl
                    }
                ]
            }
        }
    whurl = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qwbotkey}'
    resp = requests.post(whurl, data=json.dumps(data))
    resp.raise_for_status()
    return resp.json()


def send(digest, title=None, url=None):
    if qwbotkey:
        qw = qwbot(digest, title, url=url)
        return qw


if __name__ == '__main__':
    a = send(digest='这是一个测试', title='测试', url='https://192.168.1.1')
