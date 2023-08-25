# -*- coding: utf-8 -*-
# QywxNotify
# Author: kk
# date：2023/8/22 14:53
import json
import random
import requests
import os

"""
只要填入了机器人key，会优先使用机器人通知，除非返回错误码
机器人只能发到群里，应用则可以通过指定touser来实现定点发送，比如在企业微信帐号为kk的用户，通过以下几种方式可以单独对他发通知
1. 填写wqam时，touser一项写kk
2. __init__函数里，person=None改为person='kk'
3. __init__函数,self.touser = 'kk'
4. 别的模块调用时，
from qwapp import qwapp
qwapp('kk').send(我是参数)
——————————————————————————————————————————————————
通知形式：给send()添加不同数量的参数可实现不同形式的通知
1. 添加一个参数digest时，发送文字(text)信息
2. 添加两个参数digest,title时，机器人发送的是news，应用发送的是textcard，可以点击，但是会跳转到404页面
3. 添加三个参数digest,title,url时，机器人发送的是news，应用发送的是textcard，点击后可以跳转到url，如果在下方imgurl填入了图片链接，机器人发的信息会显示正方形图片
4. 添加三个参数digest,title,content时，机器人不会发送消息，即返回错误码，应用发送的是图文消息mpnews
5. 添加四个参数digest,title,url,content时，机器人最多填3个参数，即不会理会content，机器人发送的是news，点击跳转到url，应用发送图文消息，点击显示content，左下角有一个阅读原文跳转到url
"""

qwam = " "  # 填写企业微信corpid,corpsecret,touser,agentid  用半角逗号连接
qbkey = " " # 企业微信群机器人key https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxxxxx
imgurl = ' '  #填入图片链接，可通过修改文件名并使用f'https://xxxx.com/{random.randint(1, 170)}.jpg' 来达到每次通知随机图片的效果


class qwapp:
    def __init__(self, person=None):
        self.qwam = qwam.split(',')
        if len(self.qwam) >= 4:
            self.corpid = self.qwam[0]
            self.corpsecret = self.qwam[1]
            self.agentid = self.qwam[3]
            self.touser = person if person else self.qwam[2]
            self.access_token = self.__get_access_token()

    def __get_access_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        params = {
            'corpid': self.corpid,
            'corpsecret': self.corpsecret
        }
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        resp_json = resp.json()
        if 'access_token' in resp_json.keys():
            return resp_json['access_token']
        else:
            raise Exception('检查 corpid 和 corpsecret 是否正确 \n' + resp.text)

    def get_ShortTimeMedia(self):
        media_url = f'https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={self.access_token}&type=file'
        f = requests.get(imgurl).content
        r = requests.post(media_url, files={'file': f}, json=True)
        return json.loads(r.text)['media_id']

    def send(self, digest, title=None, url=None, content=None):
        at_url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={self.access_token}'
        data = {
            "touser": self.touser,
            "agentid": self.agentid,
            "safe": 0,
            "enable_id_trans": 0,
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800
        }
        if content is not None:
            content = '<pre>' + content + '</pre>'
            data["msgtype"] = 'mpnews'
            data["mpnews"] = {
                "articles": [
                    {
                        "title": title,
                        "thumb_media_id": self.get_ShortTimeMedia(),
                        "author": "惜之AI",
                        "content_source_url": url,
                        "content": content,
                        "digest": digest
                    }
                ]
            }
        elif title is None:
            data["msgtype"] = "text"
            data["text"] = {
                "content": digest
            }
        else:
            data["msgtype"] = "textcard"
            data["textcard"] = {
                "title": title,
                "description": digest,
                "url": url}
        resp = requests.post(at_url, data=json.dumps(data))
        resp.raise_for_status()
        return resp.json()


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
    whurl = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qbkey}'
    resp = requests.post(whurl, data=json.dumps(data))
    resp.raise_for_status()
    return resp.json()


def send(digest, title=None, url=None, content=None):
    if qbkey:
        qw = qwbot(digest, title, url=url)
        if qw.get('errcode') == 0:
            return
    qwapp().send(digest, title, content, url)


if __name__ == '__main__':
    send(digest='这是一个测试', title='测试', content='真一个测试', url='http://192.168.1.1')
