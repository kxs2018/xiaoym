# -*- coding: utf-8 -*-
# kxyy
# Author: kk
# date：2023/9/4 16:28


"""
活动入口,微信打开：http://2502567.pkab.tz6pstg20fnm.cloud/?p=2502567
运行前先按照config.py的要求填好设置
建议定时运行每一个半小时一次 
（青龙面板）创建两个任务 一个设置为0 8-23/3 * * *，另一个设置为30 9-23/3 * * *
达到标准，自动提现
"""
import random
import re
from urllib.parse import urlparse, parse_qs
import requests
import config
import time
from getmpinfo import getmpinfo
from qwbot import send
from check import testsend

'_____________________________________________________________'
'下面这段如果运行过check.py成功发送消息后可以注释或删除'
# 每次运行会检测推送，如果配置正确，可以注释或删除这块代码
if not testsend():
    print('没有获取到机器人key，请检查config.py里有没有设置qwbotkey')
    exit()
'上面这段如果运行过check.py成功发送消息后可以注释或删除'
'______________________________________________________________'

# 获取 czgmck 环境变量值
xyyck = config.xyyck

if xyyck is None:
    print('你没有填入xyyck，咋运行？')
    exit()

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
}


def ts():
    return str(int(time.time())) + '000'


class XYY:
    def __init__(self, ck):
        self.name = ck['name']
        self.ysm_uid = ck['ck']
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
        self.lastbiz = ''

    def user_info(self):
        r = ''
        try:
            u = f'http://1692416143.3z2rpa.top/yunonline/v1/gold?unionid={self.ysm_uid}&time={ts()}000'
            r = self.sec.get(u)
            rj = r.json()
            self.remain = rj.get("data").get("last_gold")
            print(
                f'今日已经阅读了{rj.get("data").get("day_read")}篇文章,剩余{rj.get("data").get("remain_read")}未阅读，今日获取金币{rj.get("data").get("day_gold")}，剩余{self.remain}')
            return True
        except:
            print(r.text)
            print(f'获取用户信息失败,gfsessionid无效，请检测gfsessionid是否正确')
            send('获取用户信息失败,gfsessionid无效', f'{self.name} 小月月账户失效')
            return False

    def getKey(self):
        u = 'http://1692416143.3z2rpa.top/yunonline/v1/wtmpdomain'
        p = f'unionid={self.ysm_uid}'
        r = requests.post(u, headers=self.headers, data=p)
        rj = r.json()
        domain = rj.get('data').get('domain')
        pp = parse_qs(urlparse(domain).query)
        hn = urlparse(domain).netloc
        uk = pp.get('uk')[0]
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
            print('-' * 50)
            rj = r.json()
            if rj.get('errcode') == 0:
                link = rj.get('data').get('link')
                wxlink = self.jump(link)
                mpinfo = getmpinfo(wxlink)
                if mpinfo:
                    print('开始阅读 ' + mpinfo['text'])
                if not mpinfo:
                    send(title=f'{self.name} 小阅阅阅读过检测', url=wxlink, digest='文章获取失败')
                    return False
                if checkDict.get(mpinfo['biz']) is not None:
                    send(title=f'{self.name} 小阅阅阅读过检测', url=wxlink, digest=f"验证帐号：{mpinfo['text']}")
                    print('遇到检测文章，已发送到微信，手动阅读，暂停50秒')
                    time.sleep(50)
                self.lastbiz = mpinfo['biz']
                tsm = random.randint(7, 10)
                print(f'本次模拟读{tsm}秒')
                time.sleep(tsm)
                u1 = f'https://nsr.zsf2023e458.cloud/yunonline/v1/get_read_gold?uk={uk}&time={tsm}&timestamp={ts()}'
                requests.get(u1, headers=h)

            elif rj.get('errcode') == 405:
                print('阅读重复')
                time.sleep(1.5)
            elif rj.get('errcode') == 407:
                print(rj.get('msg'))
                return True
            else:
                print('未知情况')
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
        Location = r.headers.get('Location')
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
            print('signid获取失败，本次不提现')
            return
        if int(self.remain) < 3000:
            print('没有达到提现标准')
            return False
        gold = int(int(self.remain) / 1000) * 1000
        print('本次提现金币', gold)
        if gold:
            u1 = 'http://1692429080.3z2rpa.top/yunonline/v1/user_gold'
            p1 = f'unionid={self.ysm_uid}&request_id={signid}&gold={gold}'
            r = self.sec.post(u1, data=p1)
            print(f'gold {r.json()}')
            u = f'http://1692422733.3z2rpa.top/yunonline/v1/withdraw'
            p = f'unionid={self.ysm_uid}&signid={signid}&ua=0&ptype=0&paccount=&pname='
            r = self.sec.post(u, headers=self.headers, data=p)
            print('提现结果', r.json())

    def run(self):
        if not self.user_info():
            return False
        self.read()
        time.sleep(0.5)
        self.withdraw()


if __name__ == '__main__':
    print(f'获取到{len(xyyck)}个账号')
    for i in xyyck:
        try:
            print('=' * 50 + f'\n帐号:{i["name"]} 开始任务\n' + '=' * 50)
            api = XYY(i)
            api.run()
        except Exception as e:
            print(e)
            continue
