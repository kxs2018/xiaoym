# -*- coding: utf-8 -*-
# k每天赚阅读单文件版
# Author: kk
# date：2023/9/17 10:38
"""
每天赚入口：http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552
通过企业微信机器人推送检测文章到企业微信群，请务必用微信关注微信插件并配置好机器人key
export qwbotkey="xxxxxxxxx"
参考https://github.com/kxs2018/yuedu/blob/main/获取企业微信群机器人key.md 获取key，并关注插件！！！
打开活动入口，抓包的任意接口headers中的Authorization参数，填入ck。

单账户填写样式(这里只是样式，不要填这里)
export mtzck="[{'name': 'xxx', 'ck': 'share:login:xxxx'},]"
多账户填写样式，几个账号填几个，不要多填。(这里只是样式，不要填这里)
export mtzck="[{'name': 'xxx', 'ck': 'share:login:xxxx'},{'name': 'xxx', 'ck': 'share:login:xxxx'}]"

参数解释
name:账号名，你可以随便填，用来推送时分辨哪一个账号
ck:账号的ck,抓包的任意接口headers中的Authorization参数，格式为share:login:xxxx
------------------------------------------------------------------------
运行提示 no module named lxml 解决方法
1. 在配置文件找到
## 安装python依赖时指定pip源
PipMirror="https://pypi.tuna.tsinghua.edu.cn/simple"
如果这条链接包含douban的，换成和上面一样的
2. 依赖-python 添加lxml
3. 如果装不上，尝试升级pip：①ssh连接到服务器 ②docker exec -it ql bash ③pip install pip -U
ql是青龙容器的名字，docker ps可查询
"""

import json
import os
import random
import requests
import re
import time
import ast

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
debug = 1
"""1为开，打印调试日志；0为关，不打印"""

"""线程数量设置"""
max_workers = 5
"""填入数字，设置同时跑任务的数量"""

"""设置提现标准"""
txbz = 1000  # 不低于1000，平台的提现标准为1000
"""设置为1000，即为1元起提"""

qwbotkey = os.getenv('qwbotkey')
mtzck = os.getenv('mtzck')

if not qwbotkey or not mtzck:
    print('请仔细阅读上方注释并配置好key和ck')
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


class MTZYD:
    def __init__(self, cg):
        self.name = cg['name']
        self.s = requests.session()
        self.s.headers = {
            'Authorization': cg['ck'],
            'User-Agent': 'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
            'content-type': 'application/json',
            'Accept': '*/*',
            'Origin': 'http://61695315208.tt.bendishenghuochwl1.cn',
            'Referer': 'http://61695315208.tt.bendishenghuochwl1.cn/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh',
        }
        self.msg = ''

    def user_info(self):
        url = 'http://api.mengmorwpt1.cn/h5_share/user/info'
        res = self.s.post(url, json={"openid": 0}).json()
        debugger(f'userinfo {res}')
        if res.get('code') == 200:
            self.nickname = res.get('data').get('nickname')
            self.points = res.get('data').get('points') - res.get('data').get('withdraw_points')
            res = self.s.post('http://api.mengmorwpt1.cn/h5_share/user/sign', json={"openid": 0})
            debugger(f'签到 {res.json()}')
            msg = res.json().get('message')
            self.msg += f'\n账号：{self.nickname},现有积分：{self.points}，{msg}\n' + '-' * 50 + '\n'
            printlog(f'{self.nickname}:现有积分：{self.points}，{msg}')
            url = 'http://api.mengmorwpt1.cn/h5_share/user/up_profit_ratio'
            payload = {"openid": 0}
            try:
                res = self.s.post(url, json=payload).json()
                if res.get('code') == 500:
                    raise
                self.msg += f'代理升级：{res.get("message")}\n'
            except:
                url = 'http://api.mengmorwpt1.cn/h5_share/user/task_reward'
                for i in range(0, 8):
                    payload = {"type": i, "openid": 0}
                    res = self.s.post(url, json=payload).json()
                    if '积分未满' in res.get('message'):
                        break
                    if res.get('code') != 500:
                        self.msg += '主页奖励积分：' + res.get('message') + '\n'
                    i += 1
                    time.sleep(0.5)
            return True
        else:
            self.msg += '获取账号信息异常，检查cookie是否失效\n'
            printlog(f'{self.name}:获取账号信息异常，检查cookie是否失效')
            send(f'{self.name} 每天赚获取账号信息异常，检查cookie是否失效', '每天赚账号异常通知')
            return False

    def get_read(self):
        url = 'http://api.mengmorwpt1.cn/h5_share/daily/get_read'
        data = {"openid": 0}
        i = 0
        while i < 10:
            res = self.s.post(url, json=data).json()
            debugger(f'getread {res}')
            if res.get('code') == 200:
                self.link = res.get('data').get('link')
                return True
            elif '获取失败' in res.get('message'):
                time.sleep(15)
                i += 1
                continue
            else:
                self.msg += res.get('message') + '\n'
                printlog(f'{self.nickname}:{res.get("message")}')
                return False

    def gettaskinfo(self, infolist):
        for i in infolist:
            if i.get('url'):
                return i

    def dotasks(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
            'content-type': 'application/json',
            'Origin': 'http://nei594688.594688be.com.byymmmcm3.cn',
            'Referer': 'http://nei594688.594688be.com.byymmmcm3.cn/',
            'Accept-Encoding': 'gzip, deflate',
        }
        while True:
            data = {"href": self.link}
            url = 'https://api.wanjd.cn/wxread/articles/tasks'
            res = requests.post(url, headers=headers, json=data).json()
            tasklist = res.get('data')
            debugger(f'tasks {tasklist}')
            ls = [i['is_read'] for i in tasklist]
            if 0 not in ls:
                break
            if res.get('code') != 200:
                self.msg += res.get('message') + '\n'
                printlog(f'{self.nickname}:{res.get("message")}')
                break
            else:
                taskinfo = self.gettaskinfo(res['data'])
                if not taskinfo:
                    break
                taskurl = taskinfo.get('url')
                taskid = taskinfo['id']
                debugger(taskid)
                data.update({"id": taskid})
                mpinfo = getmpinfo(taskurl)
                try:
                    self.msg += '正在阅读 ' + mpinfo['text'] + '\n'
                    printlog(f'{self.nickname}:正在阅读{mpinfo["text"]}')
                except:
                    self.msg += '正在阅读 ' + mpinfo['biz'] + '\n'
                    printlog(f'{self.nickname}:正在阅读 {mpinfo["biz"]}')
                if len(str(taskid)) < 5:
                    send(title=f'{self.nickname} 美添赚过检测', url=taskurl, msg=mpinfo.get('text'))
                    self.msg += '发送通知，暂停50秒\n'
                    printlog(f'{self.nickname}:发送通知，暂停50秒')
                    time.sleep(50)
                tsm = random.randint(7, 10)
                time.sleep(tsm)
                url = 'https://api.wanjd.cn/wxread/articles/three_read'
                res = requests.post(url, headers=headers, json=data).json()
                if res.get('code') == 200:
                    self.msg += '阅读成功' + '\n' + '-' * 50 + '\n'
                    printlog(f'{self.nickname}:阅读成功')
                if res.get('code') != 200:
                    self.msg += res.get('message') + '\n' + '-' * 50 + '\n'
                    printlog(f'{self.nickname}:{res.get("message")}')
                    break
        url = 'https://api.wanjd.cn/wxread/articles/check_success'
        data = {'type': 1, 'href': self.link}
        res = requests.post(url, headers=headers, json=data).json()
        debugger(f'check {res}')
        self.msg += res.get('message') + '\n'
        printlog(f'{self.nickname}:{res.get("message")}')

    def withdraw(self):
        if self.points < txbz:
            self.msg += f'没有达到你设置的提现标准{txbz}\n'
            printlog(f'{self.nickname}:没有达到你设置的提现标准{txbz}')
            return False
        u = 'http://api.mengmorwpt1.cn/h5_share/user/withdraw'
        r = self.s.post(u).json()
        self.msg += '提现结果' + r.get('message') + '\n'
        printlog(f'{self.nickname}:提现结果 {r.get("message")}')
        if r.get('code') == 200:
            send(f'{self.name} 已提现到红包，请在服务通知内及时领取', title='每天赚提现通知')

    def run(self):
        self.msg += '*' * 50 + f'\n账号：{self.name}开始任务\n'
        printlog(f'账号：{self.name}开始任务')
        if not self.user_info():
            return False
        if self.get_read():
            self.dotasks()
            self.user_info()
        self.withdraw()
        printlog(f'账号：{self.name}:任务结束')
        if not printf:
            print(self.msg.strip())
            print(f'账号：{self.name}任务结束')


def yd(q):
    while not q.empty():
        ck = q.get()
        api = MTZYD(ck)
        api.run()


def get_ver():
    ver = 'kmtz V1.4.2'
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
        mtzck = ast.literal_eval(mtzck)
    except:
        pass
    q = Queue()
    threads = []
    for i in mtzck:
        printlog(i)
        q.put(i)
    for i in range(max_workers):
        t = threading.Thread(target=yd, args=(q,))
        t.start()
        threads.append(t)
        time.sleep(20)
    for thread in threads:
        thread.join()
