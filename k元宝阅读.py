# -*- coding: utf-8 -*-
# k元宝阅读
# Author: kk
# date：2023/9/4 16:15

"""
元宝阅读：http://mr134905063.znooqoqzk.cloud/coin/index.html?mid=CS5T87Q98
定时运行每15-30分钟一次
自动提现，如遇网络问题够提现标准，会推送消息手动提现
运行前先按照config.py的要求填好设置
"""
import ast
from random import randint
import requests
import config
import time
from check import testsend
from getmpinfo import getmpinfo
from qwbot import send

'_____________________________________________________________'
'下面这段如果运行过check.py成功发送消息后可以注释或删除'
# 每次运行会检测推送，如果配置正确，可以注释或删除这块代码
if not testsend():
    print('没有获取到机器人key，请检查config.py里有没有设置qwbotkey')
    exit()
'上面这段如果运行过check.py成功发送消息后可以注释或删除'
'______________________________________________________________'
ck = config.aiock
if ck is None:
    print('你没有填入aiock，咋运行？')
    exit()
else:
    # 输出有几个账号
    num_of_accounts = len(ck)
    print(f"获取到 {num_of_accounts} 个账号")

checkDict = {
    'Mzg2Mzk3Mjk5NQ==': ['wz', ''],
}


class Allinone:
    def __init__(self, ck, mode=None):
        self.name = ck['name']
        self.mode = mode
        self.s = requests.session()
        self.url = f"http://u.cocozx.cn/api/{self.mk_path()}"
        self.payload = {"un": ck['un'], "token": ck['token'], "pageSize": 20}
        self.readhost = self.get_readhost()
        self.s.headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                          'Content-Type': 'application/json; charset=UTF-8',
                          'Host': 'u.cocozx.cn',
                          'Connection': 'keep-alive',
                          'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309070f) XWEB/8391 Flue",
                          }

    def mk_path(self):
        global upath
        if self.mode == 'hh':
            upath = "user"
        elif self.mode == 'yb':
            upath = "coin"
        elif self.mode == 'xk':
            upath = "ox"
        elif self.mode == 'zh':
            upath = 'oz'
        return upath

    def get_readhost(self):
        url = self.url + '/getReadHost'
        res = self.s.post(url, json=self.payload).json()
        # print('readhome ', res)
        readhost = res.get('result')['host']
        return readhost

    def get_info(self):
        self.s.headers.update({'Origin': self.readhost, 'Referer': self.readhost, })
        data = {**self.payload, **{'code': 'CS5T87Q98'}}
        try:
            response = self.s.post(self.url + "/info", json=data).json()
            result = response.get("result")
            # print('get_info ', response)
            us = result.get('us')
            if us == 2:
                print(f'账号：{self.name}已被封')
                raise Exception(f'账号：{self.name}已被封')
            print(
                f"""账号:{self.name}，今日阅读次数:{result["dayCount"]}，当前元宝:{result["moneyCurrent"]}，累计阅读次数:{result["doneWx"]}""",
                flush=True)
            money = int(result["moneyCurrent"])
            self.huid = result.get('uid')
            print(f'邀请链接：{self.readhost}/{self.mk_path()}/index.html?mid={self.huid}\n' + '-' * 50)
            return money
        except:
            return False

    def psmoneyc(self):
        data = {**self.payload, **{'mid': self.huid}}
        try:
            response = self.s.post(self.url + "/psmoneyc", json=data).json()
            print(f"感谢下级送来的{response['result']['val']}花儿", flush=True)
        except:
            pass
        return

    def get_status(self):
        res = self.s.post(self.url + "/read", json=self.payload).json()
        # print('getstatus ', res)
        self.status = res.get("result").get("status")
        if self.status == 40:
            print("文章还没有准备好\n" + '-' * 50, flush=True)
            return
        elif self.status == 50:
            print("阅读失效\n" + '-' * 50, flush=True)
            return
        elif self.status == 60:
            print("已经全部阅读完了\n" + '-' * 50, flush=True)
            return
        elif self.status == 70:
            print("下一轮还未开启\n" + '-' * 50, flush=True)
            return
        elif self.status == 10:
            taskurl = res["result"]["url"]
            print('-' * 50 + "\n阅读链接获取成功", flush=True)
            return taskurl

    def submit(self):
        self.s.headers.update({'Content-Length': '103', 'Accept-Encoding': 'gzip, deflate',
                               'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'})
        data = {**{'type': 1}, **self.payload}
        response = self.s.post(self.url + "/submit?zx=&xz=1", json=data)
        result = response.json().get('result')
        # print('submit ' + response.text)
        cs = result["progress"]
        print(f"阅读成功,获得元宝{result['val']}，当前剩余次数:{cs}", flush=True)

    def read(self):
        while True:
            taskurl = self.get_status()
            if not taskurl:
                if self.status == 30:
                    time.sleep(3)
                    continue
                break
            mpinfo = getmpinfo(taskurl)
            print('开始阅读 ' + mpinfo['text'])
            t = randint(7, 10)
            if mpinfo['biz'] == "Mzg2Mzk3Mjk5NQ==":
                print('当前正在阅读检测文章')
                send(mpinfo['text'], f'{self.name}  {self.mode}阅读正在读检测文章', taskurl)
                time.sleep(50)
            print(f'模拟阅读{t}秒')
            time.sleep(t)
            self.submit()

    def tixian(self):
        money = self.get_info()
        if 10000 <= money < 49999:
            txe = "10000"
        elif 50000 <= money < 100000:
            txe = "50000"
        elif 3000 <= money < 10000:
            txe = "3000"
        elif money >= 100000:
            txe = "100000"
        else:
            print('不够提现标准')
            return False
        print("提现金额:" + txe)
        if self.mode == "hh":
            tx_moshi = "/wd"
        else:
            tx_moshi = "/wdmoney"
        data = {**self.payload，**{"val": txe}}
        try:
            response = self.s.post(self.url + tx_moshi,json=data)
            print(response.text)
        except:
            send(f'花花阅读可提现额 {int(txe) / 10000}元，点这提现', title=f'{self.name} 花花阅读提现通知',
                 url='{self.readhost}/{self.mk_path()}/index.html?mid=CS5T87Q98')

    def run(self):
        print('=' * 50)
        if self.get_info():
            if self.mode == 'hh':
                self.psmoneyc()
            self.read()
            self.tixian()
        print('=' * 50)


if __name__ == '__main__':
    if ck is None:
        print('请检查变量名称是否填写正确')
        exit(0)
    try:
        ck = ast.literal_eval(ck)
    except:
        pass
    for index, cg in enumerate(ck):
        try:
            api = Allinone(cg, 'yb')
            api.run()
            if cg != ck[-1]:
                time.sleep(5)
        except Exception as e:
            print(e)
            continue
