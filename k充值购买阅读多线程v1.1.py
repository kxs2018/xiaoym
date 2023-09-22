# -*- coding: utf-8 -*-
# k充值购买阅读
"""
仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
充值购买阅读入口：http://2502807.jl.sgzzlb.sg6gdkelit8js.cloud/?p=2502807
阅读文章抓出gfsessionid

推送检测文章   将多个账号检测文章推送至将多个账号检测文章推送至目标微信目标微信，手动点击链接完成检测阅读

qwbotkey为企业微信webhook机器人后面的 key
参考 https://github.com/kxs2018/yuedu/blob/main/获取企业微信群机器人key.md 获取key，并关注插件！！！
===============================================================
青龙面板，在配置文件里添加
export qwbotkey="qwbotkey"
export czgmck="[{'name':'xxx','ck':'gfsessionid=xxx'},{'name':'xxx','ck':'gfsessionid=xxx'},]"
---------------------------------------------------------------
no module named lxml 解决方案
1. 配置文件搜索 PipMirror，如果网址包含douban的，请改为下方的网址
PipMirror="https://pypi.tuna.tsinghua.edu.cn/simple"
2. 依赖管理-python 添加 lxml
3. 如果装不上，①请ssh连接到服务器 ②docker exec -it ql bash (ql是青龙容器的名字，不会就问百度) ③pip install pip -U
4. 再装不上依赖就放弃吧
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
import datetime

try:
    from lxml import etree
except:
    print('请仔细阅读脚本上方注释中的“no module named lxml 解决方案”')
    exit()
import time

"""实时日志开关"""
printf = 1
"""1为开，0为关"""

"""debug模式开关"""
debug = 0
"""1为开，打印调试日志；0为关，不打印"""

"""线程数量设置"""
max_workers = 5
"""设置为5，即最多有5个任务同时进行"""

qwbotkey = os.getenv('qwbotkey')
czgmck = os.getenv('czgmck')
if not qwbotkey or not czgmck:
    print('请仔细阅读上方注释，并配置好qwbotkey和czgmck')
    exit()

checklist = ['MzkyMzI5NjgxMA==', 'MzkzMzI5NjQ3MA==',
             'Mzg5NTU4MzEyNQ==', 'Mzg3NzY5Nzg0NQ==',
             'MzU5OTgxNjg1Mg==', 'Mzg4OTY5Njg4Mw==',
             'MzI1ODcwNTgzNA==', "Mzg2NDY5NzU0Mw==", ]


def ftime():
    t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return t


def debugger(text):
    if debug:
        print(text)


def printlog(text):
    if printf:
        print(text)


def send(msg, title='通知', url=None):
    if not title or not url:
        data = {
            "msgtype": "text",
            "text": {
                "content": f"{title}\n\n{msg}\n\n本通知by：https://github.com/kxs2018/xiaoym\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",
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


def getmpinfo(link):
    if not link or link == '':
        return False
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}
    res = requests.get(link, headers=headers)
    html = etree.HTML(res.text)
    # print(res.text)
    title = html.xpath('//meta[@*="og:title"]/@content')
    if title:
        title = title[0]
    url = html.xpath('//meta[@*="og:url"]/@content')
    if url:
        url = url[0].encode().decode()
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
    ctt = re.findall(r'createTime = \'(.*)\'', res.text)
    if ctt:
        ctt = ctt[0][5:]
    text = f'{ctt}|{title}|{biz}|{username}|{id}'
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
        self.sio = StringIO()

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
            debugger(f'readfinfo {res.text}')
            try:
                result = res.json()
                self.remain = result.get("data").get("remain")
                msg = f'今日已经阅读了{result.get("data").get("read")}篇文章，今日总金币{result.get("data").get("gold")}，剩余{self.remain}\n邀请链接：{self.get_share_link()}'
                printlog(f'{self.name}:{msg}')
                self.sio.write(msg + '\n')
                return True
            except:
                printlog(f'{self.name}:{res.text}')
                self.sio.write(res.text + '\n')
                return False
        except:
            printlog(f'{self.name}:获取用户信息失败，账号异常，请检查你的ck')
            self.sio.write('获取用户信息失败，账号异常，请检查你的ck\n')
            send('{self.name}:获取用户信息失败，账号异常，请检查你的ck', '钢镚阅读ck失效通知')
            return False

    def task_finish(self):
        url = "http://2502567.oz6lsvinhxxa.xcgh.aqk84n5fq0rg.cloud/read/finish"
        data = {
            "time": str(int(time.time())),
            "sign": self.sha_256(str(int(time.time())))
        }
        res = self.sec.post(url, data=data).json()
        debugger(f'finish {res}')
        self.sio.write(f'finish  {res}\n')
        if res.get('code') != 0:
            printlog(f'{self.name}:{res.get("message")}')
            self.sio.write(res.get('message') + '\n')
            return False
        elif res['data']['check'] is False:
            gain = res['data']['gain']
            read = res['data']['read']
            self.sio.write(f"阅读文章成功，获得钢镚[{gain}]，已读{read}\n")
            printlog(f'{self.name}: 阅读文章成功，获得钢镚[{gain}]，已读{read}')
            return True

    def read(self):
        while True:
            self.sio.write('-' * 50 + '\n')
            url = f'http://2502567.oz6lsvinhxxa.xcgh.aqk84n5fq0rg.cloud/read/task'
            data = {
                "time": str(int(time.time())),
                "sign": self.sha_256(str(int(time.time())))
            }
            res = self.sec.get(url, data=data).json()
            debugger(f'read {res}')
            if res.get('code') != 0:
                self.sio.write(res['message'] + '\n')
                printlog(f'{self.name}:{res["message"]}')
                return False
            else:
                uncode_link = res.get('data').get('link')
                printlog(f'{self.name}:获取到阅读链接成功')
                self.sio.write(f'获取到阅读链接成功\n')
                link = uncode_link.encode().decode()
                mpinfo = getmpinfo(link)
                biz = mpinfo['biz']
                self.sio.write(f'开始阅读 ' + mpinfo['text'] + '\n')
                printlog(f'{self.name}:开始阅读 ' + mpinfo['text'])
                if biz in checklist:
                    self.sio.write("正在阅读检测文章，发送通知，暂停50秒\n")
                    printlog(f'{self.name}:正在阅读检测文章，发送通知，暂停50秒')
                    send(mpinfo['text'], f'{self.name}钢镚阅读检测', url=link)
                    time.sleep(50)
                t = random.randint(7, 10)
                self.sio.write(f'本次模拟阅读{t}秒\n')
                time.sleep(t)
                self.task_finish()

    def withdraw(self):
        if self.remain < 10000:
            self.sio.write('没有达到提现标准\n')
            printlog(f'{self.name}:没有达到提现标准')
            return False
        url = f'http://2502567.oz6lsvinhxxa.xcgh.aqk84n5fq0rg.cloud/withdraw/wechat'
        data = {"time": str(int(time.time())),
                "sign": self.sha_256(str(int(time.time())))}
        res = self.sec.get(url, data=data).json()
        self.sio.write(f"提现结果：{res.get('message')}\n")
        printlog(f'{self.name}:提现结果  {res.get("message")}')

    def run(self):
        self.sio.write('=' * 50 + f'\n账号：{self.name}开始任务\n')
        if self.read_info():
            self.read()
            self.read_info()
            self.withdraw()
            msg = self.sio.getvalue()
            if not printf:
                print(msg)


def yd(q):
    while not q.empty():
        ck = q.get()
        api = CZGM(ck)
        api.run()


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
        time.sleep(20)
    for thread in threads:
        thread.join()
    print("-" * 50 + '\nhttps://github.com/kxs2018/xiaoym\nBy:惜之酱\n' + '-' * 50)
