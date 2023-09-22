# -*- coding: utf-8 -*-
# k小阅阅阅读多线程版
# Author: kk
# date：2023/9/5 16:38
"""
仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
小阅阅阅读入口：https://wi83860.aiskill.top:10251/yunonline/v1/auth/0489574c00307cdb933067188854e498?codeurl=wi83860.aiskill.top:10251&codeuserid=2&time=1695092177
阅读文章抓出ysm_uid 建议手动阅读5篇左右再使用脚本，不然100%黑！！！
推送检测文章   将多个账号检测文章推送至将多个账号检测文章推送至目标微信目标微信，手动点击链接完成检测阅读
key为企业微信webhook机器人后面的 key
===============================================================
青龙面板，在配置文件里添加
export qwbotkey="key"
export xyyck="[{'name':'xxx','ck':'xxx'},{'name':'xxx','ck':'xxx'},]"
===============================================================
no module named lxml 解决方案
1. 配置文件搜索 PipMirror，如果网址包含douban的，请改为下方的网址
PipMirror="https://pypi.tuna.tsinghua.edu.cn/simple"
2. 依赖管理-python 添加 lxml
3. 如果装不上，①请ssh连接到服务器 ②docker exec -it ql bash (ql是青龙容器的名字，docker ps可查询) ③pip install pip -U
===============================================================
"""
import datetime
from io import StringIO
import threading
import ast
import json
import os
import random
import re
from queue import Queue
import requests

try:
    from lxml import etree
except:
    print('请仔细阅读脚本上方注释中的“no module named lxml 解决方案”')
    exit()
import time
from urllib.parse import urlparse, parse_qs

"""实时日志开关"""
printf = 0
"""1为开，0为关"""

"""debug模式开关"""
debug = 1
"""1为开，打印调试日志；0为关，不打印"""

"""线程数量设置"""
max_workers = 5
"""设置为5，即最多有5个任务同时进行"""

qwbotkey = os.getenv('qwbotkey')
xyyck = os.getenv('xyyck')
if not qwbotkey or not xyyck:
    print('请仔细阅读上方注释并设置好key和ck')
    exit()

checklist = ['MzkxNTE3MzQ4MQ==', 'Mzg5MjM0MDEwNw==', 'MzUzODY4NzE2OQ==', 'MzkyMjE3MzYxMg==',
             'MzkxNjMwNDIzOA==', 'Mzg3NzUxMjc5Mg==', 'Mzg4NTcwODE1NA==', 'Mzk0ODIxODE4OQ==',
             'Mzg2NjUyMjI1NA==', 'MzIzMDczODg4Mw==', 'Mzg5ODUyMzYzMQ==', 'MzU0NzI5Mjc4OQ==',
             'Mzg5MDgxODAzMg==']


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


def ts():
    return str(int(time.time())) + '000'


class XYY:
    def __init__(self, cg):
        self.name = cg['name']
        self.ysm_uid = cg['ck']
        self.sec = requests.session()
        self.sec.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': f'ysm_uid={self.ysm_uid};',
        }
        self.sio = StringIO(f'{self.name} 小阅阅阅读记录\n\n')

    def user_info(self):
        try:
            url = f'http://1692416143.3z2rpa.top/yunonline/v1/gold?unionid={self.ysm_uid}&time={ts()}000'
            res = self.sec.get(url).json()
            debugger(f'userinfo {res}')
            self.remain = res.get("data").get("last_gold")
            msg = f'今日已经阅读了{res.get("data").get("day_read")}篇文章,剩余{res.get("data").get("remain_read")}未阅读，今日获取金币{res.get("data").get("day_gold")}，剩余{self.remain}'
            printlog(f'{self.name}:{msg}')
            self.sio.write(msg + '\n')
            remain_read = res.get("data").get("remain_read")
            if remain_read == 0:
                return False
            return True
        except:
            printlog(f'{self.name}:获取用户信息失败,gfsessionid无效，请检测gfsessionid是否正确')
            self.sio.write(f'获取用户信息失败,gfsessionid无效，请检测gfsessionid是否正确\n')
            send(f'{self.name} 获取用户信息失败,账户失效', '小阅阅账号失效通知')
            return False

    def getKey(self):
        url = 'http://1692416143.3z2rpa.top/yunonline/v1/wtmpdomain'
        data = f'unionid={self.ysm_uid}'
        res = self.sec.post(url, data=data).json()
        debugger(f'getkey {res}')
        domain = res.get('data').get('domain')
        self.uk = re.findall(r'uk=(.*?)&', domain)[0]
        host = re.findall(r'(http.*?)/yuedu', domain)[0]
        self.headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
            'Origin': host,
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh',
        }

    def read(self):
        time.sleep(3)
        self.params = {'uk': self.uk}
        while True:
            url = f'https://nsr.zsf2023e458.cloud/yunonline/v1/do_read'
            res = requests.get(url, headers=self.headers, params=self.params)
            self.sio.write('-' * 50 + '\n')
            debugger(f'read1 {res.text}')
            res = res.json()
            if res.get('errcode') == 0:
                link = res.get('data').get('link')
                wxlink = self.jump(link)
                if 'mp.weixin' in wxlink:
                    mpinfo = getmpinfo(wxlink)
                    biz = mpinfo['biz']
                    self.sio.write('开始阅读 ' + mpinfo['text'] + '\n')
                    printlog(f'{self.name}:开始阅读 ' + mpinfo['text'])
                    if biz in checklist:
                        send(msg=f"{mpinfo['text']}", title=f'{self.name} 小阅阅阅读过检测', url=wxlink)
                        self.sio.write('遇到检测文章，已发送到微信，手动阅读，暂停50秒\n')
                        printlog(f'{self.name}:遇到检测文章，已发送到微信，手动阅读，暂停50秒')
                        time.sleep(50)
                else:
                    self.sio.write(f'{self.name} 小阅阅跳转到 {wxlink}\n')
                    printlog(f'{self.name}: 小阅阅跳转到 {wxlink}')
                tsm = random.randint(7, 10)
                self.sio.write(f'本次模拟读{tsm}秒\n')
                time.sleep(tsm)
                url = f'https://nsr.zsf2023e458.cloud/yunonline/v1/get_read_gold?uk={self.uk}&time={tsm}&timestamp={ts()}'
                requests.get(url, headers=self.headers)
            elif res.get('errcode') == 405:
                printlog(f'{self.name}:阅读重复')
                self.sio.write('阅读重复\n')
                time.sleep(1.5)
            elif res.get('errcode') == 407:
                printlog(f'{self.name}:{res.get("msg")}')
                self.sio.write(res.get('msg') + '\n')
                return True
            else:
                printlog(f'{self.name}:{res.get("msg")}')
                self.sio.write(res.get("msg") + '\n')
                time.sleep(1.5)

    def jump(self, link):
        host = urlparse(link).netloc
        headers = {
            'Host': host,
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh',
            'Cookie': f'ysm_uid={self.ysm_uid}',
        }
        res = requests.get(link, headers=headers, allow_redirects=False)
        debugger(f'jump {res.text}')
        Location = res.headers.get('Location')
        return Location

    def get_signid(self):
        res = self.sec.get('http://1692416143.3z2rpa.top/')
        htmltext = re.sub('\s', '', res.text)
        signidl = re.findall('\)\|\|"(.*?)";', htmltext)
        if not signidl:
            return False
        signid = signidl[0]
        return signid

    def withdraw(self):
        signid = self.get_signid()
        if not signid:
            printlog(f'{self.name}:signid获取失败，本次不提现')
            self.sio.write('signid获取失败，本次不提现\n')
            return
        if int(self.remain) < 3000:
            # print('没有达到提现标准')
            self.sio.write('没有达到提现标准\n')
            return False
        gold = int(int(self.remain) / 1000) * 1000
        self.sio.write(f'本次提现金币{gold}\n')
        printlog(f'{self.name}:本次提现金币{gold}')
        if gold:
            url = 'http://1692422733.3z2rpa.top/yunonline/v1/user_gold'
            data = f'unionid={self.ysm_uid}&request_id={signid}&gold={gold}'
            self.sec.post(url, data=data)
            url = f'http://1692422733.3z2rpa.top/yunonline/v1/withdraw'
            data = f'unionid={self.ysm_uid}&signid={signid}&ua=0&ptype=0&paccount=&pname='
            res = self.sec.post(url, data=data)
            self.sio.write(f"提现结果 {res.json()['msg']}")
            printlog(f'{self.name}:提现结果 {res.json()["msg"]}')

    def run(self):
        self.sio.write('=' * 50 + f'\n账号：{self.name}开始任务\n')
        printlog(f'账号：{self.name}开始任务\n')
        if not self.user_info():
            return False
        self.getKey()
        self.read()
        time.sleep(0.5)
        self.withdraw()
        msg = self.sio.getvalue()
        printlog(f'账号：{self.name} 本轮任务结束\n')
        if not printf:
            print(f'{msg}\n')


def yd(q):
    while not q.empty():
        ck = q.get()
        api = XYY(ck)
        api.run()


if __name__ == '__main__':
    try:
        xyyck = ast.literal_eval(xyyck)
    except:
        pass
    threads = []
    q = Queue()
    for i in xyyck:
        q.put(i)
    for i in range(max_workers):
        t = threading.Thread(target=yd, args=(q,))
        t.start()
        threads.append(t)
        time.sleep(20)  # 设置并发延迟
    for thread in threads:
        thread.join()
    print("-" * 50 + '\nhttps://github.com/kxs2018/xiaoym\nBy:惜之酱\n' + '-' * 50)