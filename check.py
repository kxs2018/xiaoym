# -*- coding: utf-8 -*-
# check
# Author: kk
# date：2023/9/4 11:23
import hashlib
import requests
import config
import time
from qwbot import send
import json


def sha_256(text):
    hash = hashlib.sha256()
    hash.update(text.encode())
    t = hash.hexdigest()
    return t


def testsend():
    a = send(digest='这是一个测试', title='测试', url='https://192.168.1.1')
    if a.json().get('errcode') != 0:
        print('没有获取到机器人key，请检查config.py里有没有设置qwbotkey')
        exit()
        return False
    return True


print('测试参数有效性')
print('测试key(显示数字代表有效)')
print('测试推送')
testsend()
print('请已实际推送结果为准')
print('-' * 50)

name = config.czgmck[0].get('name')
ck = config.czgmck[0].get('ck')


def user_info():
    headers = {
        'Host': '2478987.jilixczlz.ix47965in5.cloud',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh',
        'Cookie': f'gfsessionid={ck}',
    }
    ts = int(time.time())
    text = f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={ts}'
    sign = sha_256(text)
    u = f'http://2478987.jilixczlz.ix47965in5.cloud/user/info?time={ts}&sign={sign}'
    r = requests.get(u, headers=headers)
    rj = r.json()
    if rj.get('code') == 0:
        print(f'用户UID:{rj.get("data").get("uid")}')
    else:
        print(f'获取用户信息失败，ck没用填对')
        print(rj)


print('只检测充值购买参数,如果这个没问相信你其他的也不会填错,脚本选择第一个用户测试')
user_info()
time.sleep(5)
