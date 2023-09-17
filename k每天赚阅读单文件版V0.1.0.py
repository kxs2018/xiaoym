# -*- coding: utf-8 -*-
# k每天赚阅读单文件版
# Author: kk
# date：2023/9/17 10:38
"""
每天赚入口：http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552
通过企业微信机器人推送检测文章到企业微信群，请务必用微信关注微信插件并配置好机器人key
export qwbotkey=''
参考https://github.com/kxs2018/yuedu/blob/main/获取企业微信群机器人key.md 获取key，并关注插件！！！
打开活动入口，抓包的任意接口headers中的Authorization参数，填入ck。
单账户填写样式(这里只是样式，不要填这里)
export mtzck=[{"name": "xxx", "ck": "share:login:xxxx"},
]
多账户填写样式，几个账号填几个，不要多填。(这里只是样式，不要填这里)
export mtzck=[{"name": "xxx", "ck": "share:login:xxxx"},
    {"name": "xxx", "ck": "share:login:xxxx"},
    {"name": "xxx", "ck": "share:login:xxxx"},]
如有报错的，请尝试用单引号包住中括号，如：
export mtzck='''[{"name": "xxx", "ck": "share:login:xxxx"},]'''
参数解释
name:账号名，你可以随便填，用来推送时分辨哪一个账号
ck:账号的ck,抓包的任意接口headers中的Authorization参数，格式为share:login:xxxx
"""
import json
import os
import random
import requests
import re
import time
import ast
from lxml import etree
import datetime

"""debug模式开关"""
debug = 1
"""1为开，打印调试日志；0为关，不打印"""

qwbotkey = os.getenv('qwbotkey')
mtzck = os.getenv('mtzck')

if not qwbotkey or not mtzck:
    print('凡人，你还没准备好')
    exit()

checklist = ['MzkzNjI3NDAwOA==', 'Mzg5MTcxNjk3Mg==', 'MzA3NTQzOTg1OA==', 'MzkzMTI2Nzk1NQ==', ]


def ftime():
    t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return t


def debugger(text):
    if debug:
        print(text)


def send(msg, title='通知', url=None):
    if not title or not url:
        data = {
            "msgtype": "text",
            "text": {
                "content": f"{title}\n\n{msg}\n\n本通知by：https://github.com/kxs2018/yuedu\ntg频道：https://t.me/+uyR92pduL3RiNzc1\n通知时间：{ftime()}",
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
    text = f'{ctt}|{title}|{biz}|{username}|{id}'
    mpinfo = {'biz': biz, 'text': text}
    return mpinfo


class MTZYD:
    def __init__(self, cg):
        self.name = cg['name']
        self.headers = {
            'Authorization': cg['ck'],
            'User-Agent': 'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
            'content-type': 'application/json',
            'Accept': '*/*',
            'Origin': 'http://71692693186.tt.bendishenghuochwl1.cn',
            'Referer': 'http://71692693186.tt.bendishenghuochwl1.cn/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh',
        }
        self.s = requests.session()
        self.s.headers = self.headers

    def user_info(self):
        u = 'http://api.mengmorwpt1.cn/h5_share/user/info'
        r = self.s.post(u, json={"openid": 0})
        # print('userinfo '+r.text)
        rj = r.json()
        if rj.get('code') == 200:
            self.nickname = rj.get('data').get('nickname')
            self.points = rj.get('data').get('points') - rj.get('data').get('withdraw_points')
            res = self.s.post('http://api.mengmorwpt1.cn/h5_share/user/sign', json={"openid": 0})
            debugger(f'签到 {res.json()}')
            msg = res.json().get('message')
            print(f'\n账号：{self.nickname},现有积分：{self.points}，{msg}')
            print('-' * 50)
            url = 'http://api.mengmorwpt1.cn/h5_share/user/up_profit_ratio'
            payload = {"openid": 0}
            try:
                res = self.s.post(url, json=payload).json()
                # print(res)
                if res.get('code') == 500:
                    raise
                print(f'代理升级：{res.get("message")}')
            except:
                url = 'http://api.mengmorwpt1.cn/h5_share/user/task_reward'
                for i in range(0, 8):
                    payload = {"type": i, "openid": 0}
                    res = self.s.post(url, json=payload).json()
                    # print(res)
                    if '积分未满' in res.get('message'):
                        break
                    if res.get('code') != 500:
                        print('主页奖励积分：' + res.get('message'))
                    i += 1
                    time.sleep(0.5)
            return True
        else:
            print('获取账号信息异常，检查cookie是否失效')
            send(f'{self.name} 每天赚获取账号信息异常，检查cookie是否失效', '每天赚账号异常通知')
            return False

    def get_read(self):
        url = 'http://api.mengmorwpt1.cn/h5_share/daily/get_read'
        data = {"openid": 0}
        res = self.s.post(url, json=data).json()
        debugger(f'getread {res}')
        if res.get('code') == 200:
            self.link = res.get('data').get('link')
            return True
        else:
            print(res.get('message'))
            print('-' * 50)
            return False

    def gettaskinfo(self, infolist):
        for i in infolist:
            if i.get('url'):
                return i

    def dotasks(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
            'content-type': 'application/json',
            'Origin': 'http://71692693186.tt.bendishenghuochwl1.cn',
            'Referer': 'http://71692693186.tt.bendishenghuochwl1.cn/',
            'Accept-Encoding': 'gzip, deflate',
        }
        while True:
            data = {"href": self.link}
            url = 'https://api.wanjd.cn/wxread/articles/tasks'
            res = requests.post(url, headers=headers, json=data).json()
            debugger(f'tasks {res}')
            tasklist = res.get('data')
            ls = [i['is_read'] for i in tasklist]
            if 0 not in ls:
                break
            if res.get('code') != 200:
                print(res.get('message'))
                break
            else:
                taskinfo = self.gettaskinfo(res['data'])
                if not taskinfo:
                    break
                taskurl = taskinfo.get('url')
                taskid = taskinfo['id']
                data.update({"id": taskid})
                mpinfo = getmpinfo(taskurl)
                biz = mpinfo['biz']
                try:
                    print('正在阅读 ', mpinfo['text'])
                except:
                    print('正在阅读 ', mpinfo['biz'])
                if biz in checklist:
                    send(title=f'{self.nickname} 美添赚过检测', url=taskurl, msg=mpinfo.get('text'))
                    print('发送通知，暂停50秒')
                    time.sleep(50)
                tsm = random.randint(7, 10)
                time.sleep(tsm)
                url = 'https://api.wanjd.cn/wxread/articles/three_read'
                res = requests.post(url, headers=headers, json=data).json()
                debugger(f'threeread {res}')
                if res.get('code') == 200:
                    print('阅读成功' + '\n' + '-' * 50)
                if res.get('code') != 200:
                    print(res.get('message') + '\n' + '-' * 50)
                    break
        url = 'https://api.wanjd.cn/wxread/articles/check_success'
        data = {'type': 1, 'href': self.link}
        res = requests.post(url, headers=headers, json=data).json()
        print(res.get('message'))        

    def withdraw(self):
        if self.points < 1000:
            print('没有达到提现标准')
            return False
        u = 'http://api.mengmorwpt1.cn/h5_share/user/withdraw'
        r = self.s.post(u).json()
        print('提现结果', r.get('message'))
        if r.get('code') == 200:
            send(f'{self.name} 已提现到红包，请在服务通知内及时领取', title='每天赚提现通知')

    def run(self):
        print('*' * 50)
        if not self.user_info():
            return False
        if self.get_read():
            self.dotasks()
            self.user_info()
        self.withdraw()
        print('*' * 50)


if __name__ == '__main__':
    try:
        mtzck = ast.literal_eval(mtzck)
    except:
        pass
    for i in mtzck:
        try:
            yd = MTZYD(i)
            yd.run()
        except Exception as e:
            print(e)
            continue
