# -*- coding: utf-8 -*-
# kydz
# Author: kk
# date：2023/9/24 18:19
"""
仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
入口：http://5851278349.buemxve.cn/?jgwq=3340348&goid=itrb
http://5851278349.buemxve.cn/?jgwq=3340348&goid=itrb 抓包这个链接 抓出唯一一个cookie 把7bfe3c8f4d51851的值
或者http://wxr.jjyii.com/user/getinfo?v=3 a_h_n值/后面的字符串 填入ck
建议手动阅读几篇再使用脚本！！！
推送检测文章   将多个账号检测文章推送至将多个账号检测文章推送至目标微信目标微信，手动点击链接完成检测阅读
key为企业微信webhook机器人后面的 key
===============================================================
青龙面板，在配置文件里添加
export qwbotkey="key"
export ydzck="[{'name':'xxx','ck':'xxx'},{'name':'xxx','ck':'xxx'}]"
===============================================================
no module named lxml 解决方案
1. 配置文件搜索 PipMirror，如果网址包含douban的，请改为下方的网址
PipMirror="https://pypi.tuna.tsinghua.edu.cn/simple"
2. 依赖管理-python 添加 lxml
3. 如果装不上，①请ssh连接到服务器 ②docker exec -it ql bash (ql是青龙容器的名字，docker ps可查询) ③pip install pip -U
===============================================================
"""
import threading
import ast
import hashlib
import json
import os
import random
import re
import time
from queue import Queue
import requests
import datetime
from lxml import etree
from urllib.parse import unquote, urlparse, parse_qs

"""实时日志开关"""
printf = 1
"""1为开，0为关"""

"""debug模式开关"""
debug = 1
"""1为开，打印调试日志；0为关，不打印"""

"""线程数量设置"""
max_workers = 5
"""设置为5，即最多有5个任务同时进行"""

"""设置提现标准"""
txbz = 8000  # 不低于3000，平台标准为3000
"""设置为8000，即为8毛起提"""

qwbotkey = os.getenv('qwbotkey')
ydzck = os.getenv('ydzck')

checklist = ['MzU2OTczNzcwNg==', 'MzU5NTczMzA0MQ==', 'MzUwOTk5NDI0MQ==', 'MjM5Mjc5NjMyMw==', 'MzIxNjEzMDg2OQ==',
             'MzUyMzk1MTAyNg==', 'MzI0MjE5MTc0OA==', 'MzU1ODI4MjI4Nw==', 'Mzg4OTA1MzI0Ng==', 'Mzg2MTI0Mzc1Nw==',
             'MzU5NzgwMTgwMQ==', 'MzI3MTA5MTkwNQ==', 'Mzg5NjcyMzgyOA==', 'MjM5NjY4Mzk5OQ==', 'MzI1MDAwNDY1NA==',
             'MjM5MTA5ODYzNQ==', 'MzAwNzA3MDAzMw==', 'MzkzMjUyNTk1OA==']


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
    if not url:
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


class YDZ:
    def __init__(self, ck):

        self.s = requests.session()
        self.ck = ck.get('ck')
        self.msg = ''
        self.s.headers = {'Proxy-Connection': 'keep-alive',
                          'Upgrade-Insecure-Requests': '1',
                          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8431 Flue',
                          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                          'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
                          'a_h_n': f'http%3A%2F%2F5851535337.udqyeba.cn%2F%3Fjgwq%3D3340348%26goid%3Ditrb/{self.ck}',
                          'cookie': f'7bfe3c8f4d51851={self.ck}'}

    def init(self):
        try:
            url = 'http://5851599460.udqyeba.cn/?jgwq=3340348&goid=itrb'
            res = self.s.get(url).text
            # debugger(f'info {res}')
            res = re.sub('\s', '', res)
            self.nickname = re.findall(r'nname=\'(.*?)\',', res)[0]
            uid = re.findall(r'uid=\'(\d+)\'', res)[0]
            a_h_n = f'http://5851{random.randint(500000, 599999)}.udqyeba.cn/?jgwq={uid}&goid=itrb/{self.ck}'
            self.s.headers.update({'a_h_n': a_h_n})
            return True
        except:
            printlog(f'{self.nickname} 账号信息获取错误，请检查ck有效性')
            self.msg += '账号信息获取错误，请检查ck有效性\n'
            return False

    def getinfo(self):
        infourl = 'http://wxr.jjyii.com/user/getinfo?v=3'
        res = self.s.get(infourl).json()
        debugger(f'getinfo2 {res}')
        data = res.get('data')
        self.count = data.get('count')
        self.gold = data.get('balance')
        hm = data.get('hm')
        hs = data.get('hs')
        printlog(f'账号:{self.nickname},当前金币{self.gold}，今日已读{self.count}')
        self.msg += f'账号:{self.nickname},当前金币{self.gold}，今日已读{self.count}\n'
        if hm != 0 or hs != 0:
            printlog(f'{self.nickname} 本轮次已结束，{hm}分钟后可继续任务')
            self.msg += '本轮次已结束，{hm}分钟后可继续任务\n'
            return False

    def read(self):
        url = 'http://wxr.jjyii.com/r/get?v=10'
        data = {'o': 'http://5851786000.ulzqwjf.cn/?a=gt', 'goid': 'itrb', '_v': '3890', 't': 'quick'}
        i = 0
        k = 0
        while i < 30 and k < 5:
            if not self.getinfo():
                break
            res = self.s.post(url, data=data).json()
            debugger(f'read {res}')
            taskurl = res.get('data').get('url')
            # hm = res.get('data').get('hm')
            # if hm:
            #     printlog(f'{self.nickname} 下一轮阅读将在{hm}分钟后到来')
            #     self.msg += f'下一轮阅读将在{hm}分钟后到来\n'
            #     break
            if not taskurl:
                printlog(f'{self.nickname} 没有获取到阅读链接，正在重试')
                self.msg += '没有获取到阅读链接，正在重试\n'
                time.sleep(5)
                k += 1
                continue
            mpinfo = getmpinfo(taskurl)
            try:
                printlog(f'{self.nickname} 正在阅读 {mpinfo["text"]}')
                self.msg += f'正在阅读 {mpinfo["text"]}\n'
            except:
                printlog(f'{self.nickname} 正在阅读 {mpinfo["biz"]}')
                self.msg += f'正在阅读 {mpinfo["biz"]}\n'
            if mpinfo['biz'] in checklist or self.count == 1:
                printlog(f'{self.nickname} 正在阅读检测文章，发送通知，暂停50秒')
                self.msg += '正在阅读检测文章，发送通知，暂停50秒\n'
                send(f'{self.nickname}\n点击阅读检测文章', f'{self.nickname} 阅读赚过检测', taskurl)
                time.sleep(50)
            t = random.randint(7, 10)
            self.msg += '模拟阅读{t}秒\n'
            time.sleep(t)
            ckurl = 'http://wxr.jjyii.com/r/ck'
            d1 = {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Origin': 'http://5851780833.ebrmrwy.cn',
                  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                  }
            self.s.headers.update(d1)
            res = self.s.post(ckurl, data={'t': 'quick'}).json()
            debugger(f'check {res}')
            gold = res.get('data').get('gold')
            if gold:
                printlog(f'{self.nickname} 阅读成功，获得金币{gold}')
                self.msg += f'阅读成功，获得金币{gold}\n'
            i += 1

    def cash(self):
        if self.gold < txbz:
            printlog(f'{self.nickname} 你的金币不多了')
            self.msg += '你的金币不多了\n'
            return False
        gold = int(self.gold / 1000) * 1000
        printlog(f'{self.nickname} 本次提现：{gold}')
        self.msg += f'本次提现：{gold}\n'
        url = 'http://wxr.jjyii.com/mine/cash'
        res = self.s.post(url)
        if res.json().get('code') == 1:
            printlog(f'{self.nickname} 提现成功')
            self.msg += '提现成功\n'
        else:
            debugger(res.text)
            printlog(f'{self.nickname} 提现失败')
            self.msg += '提现失败\n'

    def run(self):
        if self.init():
            self.read()
        self.cash()
        if not printf:
            print(self.msg)


def yd(q):
    while not q.empty():
        ck = q.get()
        api = YDZ(ck)
        api.run()


def get_ver():
    ver = 'kydz V0.1.1'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
    res = requests.get('https://ghproxy.com/https://raw.githubusercontent.com/kxs2018/xiaoym/main/ver.json',
                       headers=headers).json()
    v1 = ver.split(' ')[1]
    v2 = res.get('version').get(ver.split(' ')[0])
    msg = f"当前版本 {v1}，仓库版本 {v2}"
    if v1 < v2:
        msg += '\n' + '请到https://github.com/kxs2018/xiaoym下载最新版本'
    return msg


if __name__ == '__main__':
    print("-" * 50 + f'\nhttps://github.com/kxs2018/xiaoym\tBy:惜之酱\n{get_ver()}\n' + '-' * 50)
    try:
        ydzck = ast.literal_eval(ydzck)
    except:
        pass
    threads = []
    q = Queue()
    for i in ydzck:
        print(i)
        q.put(i)
    for i in range(max_workers):
        t = threading.Thread(target=yd, args=(q,))
        t.start()
        threads.append(t)
        time.sleep(20)  # 设置并发延迟
    for thread in threads:
        thread.join()
