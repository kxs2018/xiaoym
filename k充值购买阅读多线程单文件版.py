# -*- coding: utf-8 -*-
# k充值购买阅读
"""
仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
充值购买阅读入口：http://2502567.pkab.tz6pstg20fnm.cloud/?p=2502567
阅读文章抓出gfsessionid 建议手动阅读5篇左右再使用脚本，不然100%黑！！！
推送检测文章   将多个账号检测文章推送至将多个账号检测文章推送至目标微信目标微信，手动点击链接完成检测阅读
key为企业微信webhook机器人后面的 key
===============================================================
青龙面板，在配置文件里添加
export qwbotkey="key"
export czydck="[{'name':'xxx','ck':'gfsessionid=xxx'},{'name':'xxx','ck':'gfsessionid=xxx'},]"
---------------------------------------------------------------
单账号留一个大括号，多账号增加大括号
===============================================================
电脑或手机运行在下面添加
===============================================================
"""
from io import StringIO
import threading
import ast
import hashlib
import json
import os
import random
import re
from queue import Queue
import requests
from lxml import etree
import time

key = os.getenv('qwbotkey')  # 青龙面板运行，其它情况在最前面加#
# key = ''  # 电脑或手机运行,删除前面的#
if not key:
    print('没有获取到机器人key')
    exit()

czgmck = os.getenv('czgmck')  # 青龙面板
# czgmck = [
#     {'name': '', 'ck': 'gfsessionid='},
#     {'name': '', 'ck': 'gfsessionid='},
#     {'name': '', 'ck': 'gfsessionid=o-'},
#     {'name': '', 'ck': 'gfsessionid=o8'},
#     {'name': '', 'ck': 'gfsessionid=o-0fdw'},
# ]  # 电脑或手机，参照上方说明添加
if not czgmck:
    print('没有获取到CK')
    exit()

max_workers = 5  # 想要同时几个号做任务填数字几

checkDict = {
    'MzkyMzI5NjgxMA==': ['每天趣闻事', ''],
    'MzkzMzI5NjQ3MA==': ['欢闹青春', ''],
    'Mzg5NTU4MzEyNQ==': ['推粉宝助手', ''],
    'Mzg3NzY5Nzg0NQ==': ['新鲜事呦', ''],
    'MzU5OTgxNjg1Mg==': ['动感比特', ''],
    'Mzg4OTY5Njg4Mw==': ['邻居趣事闻', 'gh_60ba451e6ad7'],
    'MzI1ODcwNTgzNA==': ['麻辣资讯', 'gh_1df5b5259cba'],
}


def send(msg, title=None, url=None):
    if title and url:
        data = {
            "msgtype": "news",
            "news": {"articles": [{"title": title, "description": msg, "url": url, "picurl": 'imgurl'}]}}
    else:
        data = {"msgtype": "text",
                "text": {"content": msg, }}
    whurl = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}'
    resp = requests.post(whurl, data=json.dumps(data)).json()
    if resp.get('errcode') != 0:
        print('消息发送失败，请检查key和发送格式')
        return False


def getmpinfo(link):
    if not link or link == '':
        return False
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}
    res = requests.get(link, headers=headers)
    html = etree.HTML(res.text)
    title = html.xpath('//meta[@*="og:title"]/@content')
    if title:
        title = title[0]
    url = html.xpath('//meta[@*="og:url"]/@content')
    if url:
        url = url[0]
    biz = re.findall(r'biz=(.*?)&', link) or re.findall(r'biz=(.*?)&', url)
    if biz:
        biz = biz[0]
    username = html.xpath('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')
    if username:
        username = username[0].strip()
    id = re.findall(r"user_name.DATA'\) : '(.*?)'", res.text) or html.xpath(
        '//span[@class="profile_meta_value"]/text()')
    if id:
        id = id[0]
    text = f'{title}|{biz}|帐号:{username}|id:{id}'
    mpinfo = {'biz': biz, 'text': text}
    return mpinfo


class CZGM:
    def __init__(self, ck):
        self.name = ck['name']
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 9; V1923A Build/PQ3B.190801.06161913; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36 MMWEBID/5635 MicroMessenger/8.0.40.2420(0x28002837) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64",
            "Cookie": ck['ck']
        }
        self.sec = requests.session()
        self.sec.headers = self.headers
        self.sio = StringIO(f'{self.name} 阅读记录\n\n')

    @staticmethod
    def sha_256(ts):
        text = f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={ts}'
        hash = hashlib.sha256()
        hash.update(text.encode())
        t = hash.hexdigest()
        return t

    def get_share_link(self):
        url = 'http://2502567.oz6lsvinhxxa.xcgh.aqk84n5fq0rg.cloud/share'
        data = {
            "time": str(int(time.time())),
            "sign": self.sha_256(str(int(time.time())))
        }
        res = self.sec.get(url, data=data).json()
        share_link = res['data']['share_link'][0]
        return share_link

    def read_info(self):
        try:
            url = f'http://2502567.oz6lsvinhxxa.xcgh.aqk84n5fq0rg.cloud/read/info'
            data = {
                "time": str(int(time.time())),
                "sign": self.sha_256(str(int(time.time())))
            }
            res = self.sec.get(url, data=data)
            # print('readfinfo ',res.text)
            try:
                result = res.json()
                self.remain = result.get("data").get("remain")

                msg = f'今日已经阅读了{result.get("data").get("read")}篇文章，今日总金币{result.get("data").get("gold")}，剩余{self.remain}\n邀请链接：{self.get_share_link()}'
                print(msg)
                self.sio.write(msg + '\n')
                return True
            except:
                print(res.text)
                self.sio.write(res.text + '\n')
                return False
        except:
            print(f'获取用户信息失败，账号异常，请检查你的ck')
            self.sio.write('获取用户信息失败，账号异常，请检查你的ck\n')
            return False

    def task_finish(self):
        url = "http://2502567.oz6lsvinhxxa.xcgh.aqk84n5fq0rg.cloud/read/finish"
        data = {
            "time": str(int(time.time())),
            "sign": self.sha_256(str(int(time.time())))
        }
        res = self.sec.post(url, data=data).json()
        print('finish ', res)
        self.sio.write(f'finish  {res}\n')
        if res.get('code') != 0:
            print(res.get('message'))
            self.sio.write(res.get('message') + '\n')
            return False
        elif res['data']['check'] is False:
            gain = res['data']['gain']
            read = res['data']['read']
            self.sio.write(f"阅读文章成功，获得钢镚[{gain}]，已读{read}\n")
            print(f"{self.name} 阅读文章成功，获得钢镚[{gain}]，已读{read}")
            return True

    def read(self):
        while True:
            print('-' * 50)
            self.sio.write('-' * 50 + '\n')
            url = f'http://2502567.oz6lsvinhxxa.xcgh.aqk84n5fq0rg.cloud/read/task'
            data = {
                "time": str(int(time.time())),
                "sign": self.sha_256(str(int(time.time())))
            }
            res = self.sec.get(url, data=data).json()
            print(f'read {res}')
            if res.get('code') != 0:
                self.sio.write(res['message'] + '\n')
                print(res['message'])
                return False
            else:
                uncode_link = res.get('data').get('link')
                print(f'获取到阅读链接成功')
                self.sio.write(f'获取到阅读链接成功\n')
                link = uncode_link.encode().decode()
                mpinfo = getmpinfo(link)
                biz = mpinfo['biz']
                self.sio.write(f'开始阅读 ' + mpinfo['text'] + '\n')
                print(f'开始阅读 ' + mpinfo['text'])
                if checkDict.get(biz) is not None:
                    self.sio.write("check=True,准备执行\n")
                    print("check=True,准备执行")
                    self.sio.write("已将该文章推送至微信请在50s内点击链接完成阅读--50s后继续运行\n")
                    print("已将该文章推送至微信请在50s内点击链接完成阅读--50s后继续运行")
                    send(mpinfo['text'], f'{self.name}钢镚阅读检测', url=link)
                    time.sleep(50)
                t = random.randint(7, 10)
                self.sio.write(f'本次模拟阅读{t}秒\n')
                print(f'本次模拟阅读', t, '秒')
                time.sleep(t)
                self.task_finish()

    def withdraw(self):
        if self.remain < 10000:
            self.sio.write('没有达到提现标准\n')
            print('没有达到提现标准')
            return False
        url = f'http://2502567.oz6lsvinhxxa.xcgh.aqk84n5fq0rg.cloud/withdraw/wechat'
        data = {
            "time": str(int(time.time())),
            "sign": self.sha_256(str(int(time.time())))
        }
        res = self.sec.get(url, data=data).json()
        self.sio.write(f"提现结果：{res.get('message')}\n")
        print('提现结果', res.get('message'))

    def run(self):
        self.sio.write('=' * 50 + f'\n账号：{self.name}开始任务\n')
        if self.read_info():
            self.read()
            self.read_info()
            self.withdraw()
            msg = self.sio.getvalue()
            print(msg)
            print(f'账号：{self.name} 本轮任务结束\n' + '=' * 50)


def yd(q):
    while not q.empty():
        ck = q.get()
        try:
            api = CZGM(ck)
            api.run()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    threads = []
    try:
        czgmck = ast.literal_eval(czgmck)
    except:
        pass
    q = Queue()
    for i in czgmck:
        q.put(i)
    for i in range(max_workers):
        t = threading.Thread(target=yd, args=(q,))
        t.start()
        threads.append(t)
        time.sleep(10)
    for thread in threads:
        thread.join()
