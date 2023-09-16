# -*- coding: utf-8 -*-
# k小阅阅阅读多线程版
# Author: kk
# date：2023/9/5 16:38
"""
仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
小阅阅阅读入口：https://wi56108.ejzik.top:10267/yunonline/v1/auth/0489574c00307cdb933067188854e498?codeurl=wi56108.ejzik.top:10267&codeuserid=2&time=1694865029
阅读文章抓出ysm_uid 建议手动阅读5篇左右再使用脚本，不然100%黑！！！2小时一次
推送检测文章   将多个账号检测文章推送至将多个账号检测文章推送至目标微信目标微信，手动点击链接完成检测阅读
key为企业微信webhook机器人后面的 key
===============================================================
青龙面板，在配置文件里添加
export qwbotkey="key"
export xyyck="[{'name':'xxx','ck':'ysm_uid=xxx'},{'name':'xxx','ck':'ysm_uid=xxx'},]"
---------------------------------------------------------------
单账号留一个大括号，多账号增加大括号，注意格式
===============================================================
电脑或手机运行在下面添加
===============================================================
"""
from io import StringIO
import threading
import ast
import json
import os
import random
import re
import requests
from lxml import etree
import time
import concurrent.futures as futures
from urllib.parse import urlparse, parse_qs

key = os.getenv('qwbotkey')  # 青龙面板运行，其它情况在最前面加#
# key = ''  # 电脑或手机运行,删除前面的#
if not key:
    print('没有获取到机器人key')
    exit()

xyyck = os.getenv('xyyck')  # 青龙面板
# xyyck = []  # 电脑或手机，参照上方说明添加
if not xyyck:
    print('没有获取到CK')
    exit()

max_workers = 5  # 想要同时几个号做任务填数字几,不填或填写错误默认为3

checkDict = {
    'MzkxNTE3MzQ4MQ==': ['香姐爱旅行', 'gh_54a65dc60039'],
    'Mzg5MjM0MDEwNw==': ['我本非凡', 'gh_46b076903473'],
    'MzUzODY4NzE2OQ==': ['多肉葡萄2020', 'gh_b3d79cd1e1b5'],
    'MzkyMjE3MzYxMg==': ['Youhful', 'gh_b3d79cd1e1b5'],
    'MzkxNjMwNDIzOA==': ['少年没有乌托邦3', 'gh_b3d79cd1e1b5'],
    'Mzg3NzUxMjc5Mg==': ['星星诺言', 'gh_b3d79cd1e1b5'],
    'Mzg4NTcwODE1NA==': ['斑马还没睡123', 'gh_b3d79cd1e1b5'],
    'Mzk0ODIxODE4OQ==': ['持家妙招宝典', 'gh_b3d79cd1e1b5'],
    'Mzg2NjUyMjI1NA==': ['Lilinng', 'gh_b3d79cd1e1b5'],
    'MzIzMDczODg4Mw==': ['有故事的同学Y', 'gh_b3d79cd1e1b5'],
    'Mzg5ODUyMzYzMQ==': ['789也不行', 'gh_b3d79cd1e1b5'],
    'MzU0NzI5Mjc4OQ==': ['皮蛋瘦肉猪', 'gh_58d7ee593b86'],
    'Mzg5MDgxODAzMg==': ['北北小助手', 'gh_58d7ee593b86'],
    'Mzk0ODUyNzQ1Nw==': ['轻松生活派', 'gh_82e314240d4e']
}


def send(msg, title=None, url=None):
    imgurl = f'https://gitee.com/kxs2018/images/raw/master/{random.randint(1, 170)}.jpg'
    if title and url:
        data = {
            "msgtype": "news",
            "news": {"articles": [{"title": title, "description": msg, "url": url, "picurl": imgurl}]}}
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
    ctt = re.findall(r'createTime = \'(.*)\'',res.text)
    if ctt:
        ctt = ctt[0][-5:]
    text = f'{ctt}|{title}|{biz}|{username}|{id}'
    mpinfo = {'biz': biz, 'text': text}
    return mpinfo


def ts():
    return str(int(time.time())) + '000'


class XYY:
    def __init__(self, cg):
        self.name = cg['name']
        self.ysm_uid = cg['ck']
        self.headers = {
            'Host': '1692416143.3z2rpa.top',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'http://1692416143.3z2rpa.top/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': f'ysm_uid={self.ysm_uid};',
        }
        self.sec = requests.session()
        self.sec.headers = self.headers
        self.sio = StringIO(f'{self.name} 小阅阅阅读记录\n\n')

    def user_info(self):
        r = ''
        try:
            u = f'http://1692416143.3z2rpa.top/yunonline/v1/gold?unionid={self.ysm_uid}&time={ts()}000'
            r = self.sec.get(u)
            # print('userinfo '+r.text)
            rj = r.json()
            self.remain = rj.get("data").get("last_gold")
            # print(
            #     f'今日已经阅读了{rj.get("data").get("day_read")}篇文章,剩余{rj.get("data").get("remain_read")}未阅读，今日获取金币{rj.get("data").get("day_gold")}，剩余{self.remain}')
            self.sio.write(
                f'今日已经阅读了{rj.get("data").get("day_read")}篇文章,剩余{rj.get("data").get("remain_read")}未阅读，今日获取金币{rj.get("data").get("day_gold")}，剩余{self.remain}\n')
            return True
        except:
            print(r.text)
            # print(f'获取用户信息失败,gfsessionid无效，请检测gfsessionid是否正确')
            self.sio.write(f'获取用户信息失败,gfsessionid无效，请检测gfsessionid是否正确\n')
            send(f'获取用户信息失败,{self.name} 小月月账户失效')
            return False

    def getKey(self):
        u = 'http://1692416143.3z2rpa.top/yunonline/v1/wtmpdomain'
        p = f'unionid={self.ysm_uid}'
        r = requests.post(u, headers=self.headers, data=p)
        # print(f'getkey {r.text}')
        rj = r.json()
        domain = rj.get('data').get('domain')
        pp = parse_qs(urlparse(domain).query)
        hn = urlparse(domain).netloc
        uk = pp.get('uk')[0]
        # print('get key is ', uk)
        h = {
            'Host': 'nsr.zsf2023e458.cloud',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
            'Origin': f'https://{hn}',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh',
        }
        return uk, h

    def read(self):
        uk, h = self.getKey()
        time.sleep(3)
        self.params = {'uk': uk}
        while True:
            u = f'https://nsr.zsf2023e458.cloud/yunonline/v1/do_read'
            r = requests.get(u, headers=h, params=self.params)
            self.sio.write('-' * 50 + '\n')
            # print('-' * 50)
            # print(f'read1 {r.json()}')
            rj = r.json()
            if rj.get('errcode') == 0:
                link = rj.get('data').get('link')
                wxlink = self.jump(link)
                if 'mp.weixin' in wxlink:                    
                    mpinfo = getmpinfo(wxlink)
                    if mpinfo:
                        self.sio.write('开始阅读 ' + mpinfo['text'] + '\n')
                        # print('开始阅读 ' + mpinfo['text'])
                    if not mpinfo:
                        send(title=f'{self.name} 小阅阅阅读过检测', url=wxlink, msg='文章获取失败')
                        return False
                    if checkDict.get(mpinfo['biz']) is not None:
                        send(title=f'{self.name} 小阅阅阅读过检测', url=wxlink, msg=f"{mpinfo['text']}")
                        self.sio.write('遇到检测文章，已发送到微信，手动阅读，暂停50秒\n')
                        # print('遇到检测文章，已发送到微信，手动阅读，暂停50秒')
                        time.sleep(50)
                else:
                    print(f'{self.name} 小阅阅跳转到 {wxlink}')
                tsm = random.randint(7, 10)
                # print(f'本次模拟读{tsm}秒')
                # self.sio.write(f'本次模拟读{tsm}秒\n')
                time.sleep(tsm)
                u1 = f'https://nsr.zsf2023e458.cloud/yunonline/v1/get_read_gold?uk={uk}&time={tsm}&timestamp={ts()}'
                requests.get(u1, headers=h)
            elif rj.get('errcode') == 405:
                # print('阅读重复')
                self.sio.write('阅读重复\n')
                time.sleep(1.5)
            elif rj.get('errcode') == 407:
                # print(rj.get('msg'))
                self.sio.write(rj.get('msg') + '\n')
                return True
            else:
                # print('未知情况')
                self.sio.write('未知情况\n')
                time.sleep(1.5)

    def jump(self, link):
        hn = urlparse(link).netloc
        h = {
            'Host': hn,
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh',
            'Cookie': f'ysm_uid={self.ysm_uid}',
        }
        r = requests.get(link, headers=h, allow_redirects=False)
        # print(r.status_code)
        Location = r.headers.get('Location')
        # print(Location)
        return Location

    def get_signid(self):
        r = self.sec.get('http://1692416143.3z2rpa.top/')
        htmltext = r.text
        res1 = re.sub('\s', '', htmltext)
        signidl = re.findall('\)\|\|"(.*?)";', res1)
        if not signidl:
            return False
        signid = signidl[0]
        return signid

    def withdraw(self):
        signid = self.get_signid()
        if not signid:
            # print('signid获取失败，本次不提现')
            self.sio.write('signid获取失败，本次不提现\n')
            return
        if int(self.remain) < 10000:
            # print('没有达到提现标准')
            self.sio.write('没有达到提现标准\n')
            return False
        gold = int(int(self.remain) / 1000) * 1000
        self.sio.write(f'本次提现金币{gold}\n')
        # print('本次提现金币', gold)
        if gold:
            u1 = 'http://1692429080.3z2rpa.top/yunonline/v1/user_gold'
            p1 = f'unionid={self.ysm_uid}&request_id={signid}&gold={gold}'
            r = self.sec.post(u1, data=p1)
            # print(f'gold {r.json()}')
            u = f'http://1692422733.3z2rpa.top/yunonline/v1/withdraw'
            p = f'unionid={self.ysm_uid}&signid={signid}&ua=0&ptype=0&paccount=&pname='
            r = self.sec.post(u, headers=self.headers, data=p)
            self.sio.write(f"提现结果{r.json()['msg']}")
            # print('提现结果', r.json()['msg'])

    def run(self):
        self.sio.write('=' * 50 + f'\n账号：{self.name}开始任务\n')
        if not self.user_info():
            return False
        self.read()
        time.sleep(0.5)
        self.user_info()
        self.withdraw()
        msg = self.sio.getvalue()
        print(msg)
        print(f'账号：{self.name} 本轮任务结束\n' + '=' * 50)


def yd(ck):
    try:
        api = XYY(ck)
        api.run()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    try:
        xyyck = ast.literal_eval(xyyck)
    except:
        pass
    threads = []    
    max_workers = 3 if not int(max_workers) else int(max_workers) 
    with futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        for i in xyyck:
            t = threading.Thread(target=yd, args=(i,))
            t.start()
            threads.append(t)
            executor.submit(t)
    for thread in threads:
        thread.join()
