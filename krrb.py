# -*- coding: utf-8 -*-
# 人人帮
# Author: kk
# date：2023/8/25 16:35
"""
入口：http://ebb.maisucaiya.cloud/user/index.html?mid=1702983440137322496
如微信打不开，可复制到浏览器打开
抓包 http://ebb10.twopinkone.cloud/user/index.html?mid=1702983440137322496
cookie里的un token uid值

内置推送企业微信群机器人
参考 https://github.com/kxs2018/yuedu/blob/main/获取企业微信群机器人key.md 获取key，并关注插件！！！

export rrbck="[{'un': 'xxxx', 'token': 'xxxxx','uid':'xxxx'}]"
export qwbotkey="abcdefg"
------------------------------------------------------
no module named lxml 解决方案
1. 配置文件搜索 PipMirror，如果网址包含douban的，请改为下方的网址
PipMirror="https://pypi.tuna.tsinghua.edu.cn/simple"
2. 依赖管理-python 添加 lxml
3. 如果装不上，①请ssh连接到服务器 ②docker exec -it ql bash (ql是青龙容器的名字，不会就问百度) ③pip install pip -U
4. 再装不上依赖就放弃吧
------------------------------------------------------
提现标准默认是5000
达到标准自动提现到支付宝，请提前绑定支付宝
支付宝绑双账号方法：1.提前在支付宝设置好邮箱 2.手机号可以绑一号，邮箱可以绑一号
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

"""实时日志开关"""
printf = 1
"""1为开，0为关"""

"""debug模式开关"""
debug = 0
"""1为开，打印调试日志；0为关，不打印"""

"""线程数量设置"""
max_workers = 3
"""设置为3，即最多有3个任务同时进行"""

"""设置提现标准"""
txbz = 5000  # 不低于5000，平台的提现标准为5000
"""设置为5000，即为5毛起提"""

qwbotkey = os.getenv('qwbotkey')
rrbck = os.getenv('rrbck')
if not qwbotkey or not rrbck:
    print('请仔细阅读脚本开头的注释并配置好qwbotkey和rrbck')
    exit()


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
    text = f'{ctt} {title}'
    mpinfo = {'biz': biz, 'text': text}
    return mpinfo


class RRBYD:
    def __init__(self, ck):
        self.ck = ck
        self.headers = {'Host': 'ebb.vinse.cn',
                        'un': self.ck['un'],
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue',
                        'uid': self.ck['uid'],
                        'platform': '0',
                        'token': self.ck['token'],
                        'Origin': 'http://ebb10.twopinkone.cloud',
                        'Referer': 'http://ebb10.twopinkone.cloud/', }
        self.msg = ''

    def userinfo(self):
        url = 'http://ebb.vinse.cn/api/user/info'
        res = requests.post(url, headers=self.headers, json={"pageSize": 10}).json()
        debugger(f'userinfo {res}')
        if res.get('code') != 0:
            self.msg += f'{self.ck["un"]} cookie失效' + '\n'
            printlog(f'{self.ck["un"]} cookie失效')
            return 0
        result = res.get('result')
        self.nickname = result.get('nickName')[0:3] + '****' + result.get('nickName')[-4:]
        bean_now = result.get('integralCurrent')
        bean_total = result.get('integralTotal')
        self.msg += f'用户：{self.nickname},当前共有帮豆{bean_now}，总共获得帮豆{bean_total}\n'
        printlog(f'{self.nickname},当前共有帮豆{bean_now}，总共获得帮豆{bean_total}')
        return bean_now

    def sign(self):
        url = 'http://ebb.vinse.cn/api/user/sign'
        res = requests.post(url, headers=self.headers, json={"pageSize": 10}).json()
        debugger(f'sign {res}')
        if res.get('code') == 0:
            self.msg += f'签到成功，获得帮豆{res.get("result").get("point")}' + '\n'
            printlog(f'{self.nickname}:签到成功，获得帮豆{res.get("result").get("point")}')
        elif res.get('code') == 99:
            self.msg += res.get('msg') + '\n'
        else:
            self.msg += '签到错误' + '\n'

    def reward(self):
        url = 'http://ebb.vinse.cn/api/user/receiveOneDivideReward'
        res = requests.post(url, headers=self.headers, json={"pageSize": 10}).json()
        if res.get('code') == 0:
            self.msg += f"领取一级帮豆：{res.get('msg')}\n"
            printlog(f"{self.nickname}:领取一级帮豆：{res.get('msg')}")
        url = 'http://ebb.vinse.cn/api/user/receiveTwoDivideReward'
        res = requests.post(url, headers=self.headers, json={"pageSize": 10}).json()
        if res.get('code') == 0:
            self.msg += f"领取二级帮豆：{res.get('msg')}" + '\n'
            printlog(f"{self.nickname}:领取二级帮豆：{res.get('msg')}")

    def getentry(self):
        headers = {'Host': 'u.cocozx.cn',
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue",
                   "Origin": "http://ebb10.twopinkone.cloud",
                   "Sec-Fetch-Site": "cross-site",
                   "Sec - Fetch - Mode": "cors",
                   "Sec - Fetch - Dest": "empty"
                   }
        url = f'https://u.cocozx.cn/ipa/read/getEntryUrl?fr=ebb0726&uid={self.ck["uid"]}'
        res = requests.get(url, headers=headers).json()
        debugger(f'getentry {res}')
        result = res.get('result')
        if res.get('code') == 0:
            entryurl = result.get('url')
            self.entryurl = re.findall(r'(http://.*?)/', entryurl)[0]
        else:
            self.msg += "阅读链接获取失败" + '\n'
            printlog(f"{self.nickname}:阅读链接获取失败")

    def read(self):
        headers = {
            "Origin": self.entryurl,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue",
            "Host": "u.cocozx.cn"
        }
        for group in range(1, 3):
            data = {"fr": "ebb0726", "uid": self.ck['uid'], "group": group, "un": '', "token": '', "pageSize": 20}
            url = 'http://u.cocozx.cn/ipa/read/read'
            while True:
                res = requests.post(url, headers=headers, json=data)
                debugger("read " + res.text)
                result = res.json().get('result')
                taskurl = result.get('url')
                if result['status'] == 10:
                    mpinfo = getmpinfo(taskurl)
                    self.msg += '-' * 50 + '\n开始阅读 ' + mpinfo.get('text') + '\n'
                    printlog(f"{self.nickname}:\n开始阅读  {mpinfo.get('text')}")
                    biznow = mpinfo.get('biz')
                    if biznow == 'Mzg2Mzk3Mjk5NQ==':
                        self.msg += '正在阅读检测文章\n发送通知，暂停50秒\n'
                        printlog(f"{self.nickname}:正在阅读检测文章\n发送通知，暂停50秒")
                        send(title=mpinfo['text'], msg=f'{self.nickname}  人人帮阅读正在读检测文章', url=taskurl)
                        time.sleep(50)
                    t = randint(7, 10)
                    time.sleep(t)
                    self.submit(group)
                elif result['status'] == 60:
                    self.msg += '文章已经全部读完了\n'
                    printlog(f"{self.nickname}:文章已经全部读完了")
                    break
                elif result['status'] == 30:
                    time.sleep(2)
                    continue
                elif result['status'] == 50:
                    self.msg += '阅读失效\n'
                    printlog(f"{self.nickname}:阅读失效")
                    break
                else:
                    break
            time.sleep(2)

    def submit(self, group):
        url = 'http://u.cocozx.cn/ipa/read/submit'
        headers = {
            "Origin": self.entryurl,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue",
            "Host": "u.cocozx.cn"
        }
        data = {"fr": "ebb0726", "uid": self.ck['uid'], "group": group, "un": '', "token": '', "pageSize": 20}
        res = requests.post(url, headers=headers, json=data).json()
        debugger(f"submit {res}")
        result = res.get('result')
        daycount = result.get("dayCount")
        dayMax = result.get("dayMax")
        progress = result.get("progress")
        self.msg += f"今日已阅读{daycount}，本轮剩余{progress}，单日最高{dayMax}\n"
        printlog(f"{self.nickname}:今日已阅读{daycount}，本轮剩余{progress}，单日最高{dayMax}")

    def tx(self):
        global txje
        bean_now = self.userinfo()
        if bean_now < txbz:
            self.msg += '帮豆不够提现标准，明儿请早\n'
            printlog(f"{self.nickname}:帮豆不够提现标准，明儿请早")
            return
        elif 5000 <= bean_now < 10000:
            txje = 5000
        elif 10000 <= bean_now < 50000:
            txje = 10000
        elif 50000 <= bean_now < 100000:
            txje = 50000
        elif bean_now >= 100000:
            txje = 100000
        url = f"http://ebb.vinse.cn/apiuser/aliWd"
        params = {"val": txje, "pageSize": 10}
        r = requests.post(url, headers=self.headers, json=params).json()
        if r.get('code') == 0:
            send(f'{self.nickname} 人人帮提现支付宝{txje / 10000}元', title='人人帮阅读提现到账')

    def run(self):
        self.msg += '=' * 50 + '\n'
        if self.userinfo():
            self.sign()
            self.reward()
            self.getentry()
            time.sleep(1)
            self.read()
            self.tx()
        if not printf:
            print(self.msg.strip())


def yd(q):
    while not q.empty():
        ck = q.get()
        api = RRBYD(ck)
        api.run()


def get_ver():
    ver = 'krrb V1.1.2'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
    res = requests.get('https://ghproxy.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json', headers=headers).json()
    v1 = ver.split(' ')[1]
    v2 = res.get('version').get(ver.split(' ')[0])
    msg = f"当前版本 {v1}，仓库版本 {v2}"
    if v1 < v2:
        msg += '\n' + '请到https://github.com/kxs2018/xiaoym下载最新版本'
    return msg


if __name__ == '__main__':
    print("-" * 50 + f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n' + '-' * 50)
    try:
        rrbck = ast.literal_eval(rrbck)
    except:
        pass
    q = Queue()
    threads = []
    for i in rrbck:
        printlog(f'{i}\n以上是{i["un"]}的ck，请核对是否正确，如不正确，请检查ck填写格式')
        q.put(i)
    for i in range(max_workers):
        t = threading.Thread(target=yd, args=(q,))
        t.start()
        threads.append(t)
        time.sleep(30)
    for thread in threads:
        thread.join()
