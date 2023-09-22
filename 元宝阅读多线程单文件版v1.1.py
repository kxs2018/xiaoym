# -*- coding: utf-8 -*-
# 元宝阅读多线程单文件版
# Author: kk
# date：2023/9/18 20:45
"""
元宝阅读入口：http://mr139508131.cwejqylmo.cloud/coin/index.html?mid=CS5T87Q98
http://u.cocozx.cn/api/ox/info
抓包 info接口的请求体中的un和token参数

注意：脚本变量使用的单引号、双引号、逗号都是英文状态的
注意：脚本变量使用的单引号、双引号、逗号都是英文状态的
注意：脚本变量使用的单引号、双引号、逗号都是英文状态的
------------------------------------------------------
内置推送企业微信群机器人
参考 https://github.com/kxs2018/yuedu/blob/main/获取企业微信群机器人key.md 获取key，并关注插件！！！

青龙配置文件
export aiock="[{'un': 'xxxx', 'token': 'xxxxx','name':'彦祖'},{'un': 'xxxx', 'token': 'xxxxx','name':'彦祖'},{'un': 'xxxx', 'token': 'xxxxx','name':'彦祖'},]"

export qwbotkey="abcdefg"
------------------------------------------------------
no module named lxml 解决方案
1. 配置文件搜索 PipMirror，如果网址包含douban的，请改为下方的网址
PipMirror="https://pypi.tuna.tsinghua.edu.cn/simple"
2. 依赖管理-python 添加 lxml
3. 如果装不上，①请ssh连接到服务器 ②docker exec -it ql bash (ql是青龙容器的名字，不会问百度) ③pip install pip -U
4. 再装不上依赖就放弃吧
------------------------------------------------------
提现标准默认是3000
达到标准自动提现
"""
import json
from random import randint
import os
import time
import requests
import ast
import re
try:
    from lxml import etree
except:
    print('请仔细阅读脚本上方注释中的“no module named lxml 解决方案”')
    exit()
import datetime
import threading
from queue import Queue

"""实时打印日志开关"""
printf = 1
"""1为开，0为关"""

"""debug模式开关"""
debug = 0
"""1为开，打印调试日志；0为关，不打印"""

"""线程数量设置"""
max_workers = 3
"""设置为3，即最多有3个任务同时进行"""

qwbotkey = os.getenv('qwbotkey')
aiock = os.getenv('aiock')

if not qwbotkey or not aiock:
    print('请仔细阅读脚本开头的注释并配置好参数')
    exit()


def ftime():
    t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return t


def printlog(text):
    if printf:
        print(text)


def debugger(text):
    if debug:
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
    text = f'{ctt}|{title}'
    mpinfo = {'biz': biz, 'text': text}
    return mpinfo


class Allinone:
    def __init__(self, ck):
        self.name = ck['name']
        self.s = requests.session()
        self.payload = {"un": ck['un'], "token": ck['token'], "pageSize": 20}
        self.s.headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                          'Content-Type': 'application/json; charset=UTF-8',
                          'Host': 'u.cocozx.cn',
                          'Connection': 'keep-alive',
                          'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",
                          'Accept-Encoding': 'gzip, deflate'}
        self.msg = ''

    def get_info(self):
        data = {**self.payload, **{'code': 'CS5T87Q98'}}
        try:
            response = self.s.post("http://u.cocozx.cn/api/coin/info", json=data).json()
            result = response.get("result")
            debugger(f'get_info {response}')
            us = result.get('us')
            if us == 2:
                self.msg += f'账号：{self.name}已被封\n'
                printlog(f'账号：{self.name}已被封')
                return False

            self.msg += f"""账号:{self.name}，今日阅读次数:{result["dayCount"]}，当前元宝:{result["moneyCurrent"]}，累计阅读次数:{result["doneWx"]}\n"""
            printlog(
                f"""账号:{self.name}，今日阅读次数:{result["dayCount"]}，当前元宝:{result["moneyCurrent"]}，累计阅读次数:{result["doneWx"]}""")
            money = int(result["moneyCurrent"])
            self.huid = result.get('uid')
            return money
        except:
            return False

    def get_readhost(self):
        url = "http://u.cocozx.cn/api/coin/getReadHost"
        res = self.s.post(url, json=self.payload).json()
        debugger(f'readhome {res}')
        self.readhost = res.get('result')['host']
        self.msg += f'邀请链接：{self.readhost}/oz/index.html?mid={self.huid}\n'
        printlog(f"{self.name}:邀请链接：{self.readhost}/oz/index.html?mid={self.huid}")

    def get_status(self):
        res = self.s.post("http://u.cocozx.cn/api/coin/read", json=self.payload).json()
        debugger(f'getstatus {res}')
        self.status = res.get("result").get("status")
        if self.status == 40:
            self.msg += "文章还没有准备好\n"
            printlog(f"{self.name}:文章还没有准备好")
            return
        elif self.status == 50:
            self.msg += "阅读失效\n"
            printlog(f"{self.name}:阅读失效")
            return
        elif self.status == 60:
            self.msg += "已经全部阅读完了\n"
            printlog(f"{self.name}:已经全部阅读完了")
            return
        elif self.status == 70:
            self.msg += "下一轮还未开启\n"
            printlog(f"{self.name}:下一轮还未开启")
            return
        elif self.status == 10:
            taskurl = res["result"]["url"]
            self.msg += '-' * 50 + "\n阅读链接获取成功\n"
            printlog(f"{self.name}: 阅读链接获取成功")
            return taskurl

    def submit(self):
        data = {**{'type': 1}, **self.payload}
        response = self.s.post("http://u.cocozx.cn/api/coin/submit?zx=&xz=1", json=data)
        result = response.json().get('result')
        debugger('submit ' + response.text)
        self.msg += f"阅读成功,获得元宝{result['val']}，当前剩余次数:{result['progress']}\n"
        printlog(f"{self.name}:阅读成功,获得元宝{result['val']}，当前剩余次数:{result['progress']}")

    def read(self):
        while True:
            taskurl = self.get_status()
            if not taskurl:
                if self.status == 30:
                    time.sleep(3)
                    continue
                break
            mpinfo = getmpinfo(taskurl)
            self.msg += '开始阅读 ' + mpinfo['text'] + '\n'
            printlog(f'{self.name}:开始阅读 ' + mpinfo['text'])
            t = randint(7, 10)
            if mpinfo['biz'] == "Mzg2Mzk3Mjk5NQ==":
                self.msg += '正在阅读检测文章\n'
                printlog(f'{self.name}:正在阅读检测文章')
                send(title=mpinfo['text'], msg=f'{self.name}  元宝阅读过检测', url=taskurl)
                time.sleep(50)
            printlog(f'模拟阅读{t}秒')
            time.sleep(t)
            self.submit()

    def tixian(self):
        money = self.get_info()
        if 10000 <= money < 49999:
            txe = 10000
        elif 50000 <= money < 100000:
            txe = 50000
        elif 3000 <= money < 10000:
            txe = 3000
        elif money >= 100000:
            txe = 100000
        else:
            self.msg += '你的元宝已不足\n'
            printlog(f'{self.name}你的元宝已不足')
            return False
        self.msg += f"提现金额:{txe}\n"
        printlog(f'{self.name}提现金额:{txe}')
        url = "http://u.cocozx.cn/api/coin/wdmoney"
        data = {**self.payload, **{"val": txe}}
        try:
            res = self.s.post(url, json=data).json()
            self.msg += f'提现结果：{res.get("msg")}\n'
            printlog(f'{self.name}提现结果：{res.get("msg")}')
        except:
            self.msg += f"自动提现不成功，发送通知手动提现\n"
            printlog(f"{self.name}:自动提现不成功，发送通知手动提现")
            send(f'可提现金额 {int(txe) / 10000}元，点击提现', title=f'惜之酱提醒您 {self.name} 元宝阅读可以提现了',
                 url=f'{self.readhost}/coin/index.html?mid=CS5T87Q98')

    def run(self):
        if self.get_info():
            self.get_readhost()
            self.read()
            self.tixian()
        if not printf:
            print(self.msg.strip())


def yd(q):
    while not q.empty():
        ck = q.get()
        api = Allinone(ck)
        api.run()


if __name__ == '__main__':
    try:
        aiock = ast.literal_eval(aiock)
    except:
        pass
    q = Queue()
    threads = []
    for i in aiock:
        q.put(i)
    for i in range(max_workers):
        t = threading.Thread(target=yd, args=(q,))
        t.start()
        threads.append(t)
        time.sleep(30)  # 每隔30秒，加入一个账号开始阅读
    for thread in threads:
        thread.join()
    print("-" * 50 + '\nhttps://github.com/kxs2018/xiaoym\nBy:惜之酱\n' + '-' * 50)
