# -*- coding: utf-8 -*-
# kybyd
# Author: kk
# date：2023/9/4 16:15

"""
元宝阅读：http://mr1693635846547.kgtpecv.cn/coin/index.html?mid=5U4W6ZWPT
定时运行每15-30分钟一次
自动提现，如遇网络问题够提现标准，会推送消息手动提现
运行前先按照config.py的要求填好设置
"""
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
aiock = config.aiock
if aiock is None:
    print('你没有填入aiock，咋运行？')
    exit()
else:
    # 输出有几个账号
    num_of_accounts = len(aiock)
    print(f"获取到 {num_of_accounts} 个账号")

checkDict = {
    'Mzg2Mzk3Mjk5NQ==': ['wz', ''],
}


class Allinone:
    def __init__(self, ck, mode=None):
        self.name = ck['name']
        self.mode = mode
        self.url = f"http://u.cocozx.cn/api/{self.mk_path()}"
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'User-Agent': "Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
            'Content-Type': 'application/json; charset=UTF-8',
            'Host': 'u.cocozx.cn',
            'Content-Length': '112',
            'Connection': 'keep-alive', }
        self.payload = {"un": ck['un'], "token": ck['token'], "pageSize": "20"}

    def mk_path(self):
        if self.mode == 'hh':
            upath = "user"
            print("[----------开始运行模式花花----------------]")
        elif self.mode == 'yb':
            upath = "coin"
            print("[-----------开始运行模式元宝----------------]")
        elif self.mode == 'xk':
            upath = "ox"
            print("[-----------开始运行模式星空----------------]")
        return upath

    def get_status(self):
        res = requests.post(self.url + "/read", headers=self.headers, json=self.payload)
        response = res.json()
        if response["result"]["status"] == 30:
            print("重新运行尝试一下", flush=True)
            return
        elif response["result"]["status"] == 40:
            print("文章还没有准备好", flush=True)
            return
        elif response["result"]["status"] == 50:
            print("阅读失效", flush=True)
            return
        elif response["result"]["status"] == 60:
            print("已经全部阅读完了", flush=True)
            return
        elif response["result"]["status"] == 70:
            print("下一轮还未开启", flush=True)
            return
        elif response["result"]["status"] == 10:
            taskurl = response["result"]["url"]
            print('-' * 50 + "\n阅读链接获取成功", flush=True)
            return taskurl

    def get_info(self):
        try:
            data={**self.payload,**{'code':'5U4W6ZWPT'}}
            response = requests.post(self.url + "/info", headers=self.headers, json=data)
            result = response.json().get("result")
            print(
                f"""[---------账户名:{self.name}-----------]\n[---------今日阅读次数:{result["dayCount"]} -----------]\n[---------当前鱼儿:{result["moneyCurrent"]} -----------]\n[---------累计阅读次数:{result["doneWx"]}----------–]""",
                flush=True)
            money = int(result["moneyCurrent"])
            print("当前鱼儿:%s" % str(money))
            return money
        except:
            print('获取信息失败，ck可能失效')
            return False

    def hh_td(self):
        try:
            response = requests.post(self.url + "/psmoneyc", headers=self.headers, json=self.payload).json()["result"]
            print("花花:感谢下级送来的%s鱼儿" % response, flush=True)
        except:
            pass
        return

    def submit(self):
        response = requests.post(self.url + "/submit", headers=self.headers, json=self.payload)
        result = response.json().get('result')
        cs = result["progress"]
        print(f"阅读成功,获得元宝{result['val']}当前剩余次数:{cs}", flush=True)
        return cs

    def read(self):
        while True:
            taskurl = self.get_status()
            if not taskurl:
                break
            mpinfo = getmpinfo(taskurl)
            print('开始阅读 ' + mpinfo['text'])
            t = randint(7, 10)
            if mpinfo['biz'] == "Mzg2Mzk3Mjk5NQ==":
                print('当前正在阅读检测文章')
                send(mpinfo['text'], self.name + self.mode + '阅读正在读检测文章', taskurl)
                time.sleep(50)
            print(f'模拟阅读{t}秒')
            time.sleep(t)
            self.submit()
            time.sleep(2)

    def tixian(self):
        money = self.get_info()
        if 3000 <= money < 10000:
            txe = "3000"
        elif 10000 <= money < 50000:
            txe = "10000"
        elif 50000 <= money < 100000:
            txe = "50000"
        elif money >= 100000:
            txe = "100000"
        else:
            print('不够提现标准，明儿请早')
            return False
        print("提现金额:" + txe)
        if self.mode == "hh":
            tx_moshi = "/wd"
        else:
            tx_moshi = "/wdmoney"
        try:
            response = requests.post(self.url + tx_moshi, headers=self.headers, json=self.payload.update({"val": txe}))
            print(response.json().get('msg'))
        except Exception as e:
            print(e)
            send(f'{self.name} 星空提现{int(txe)/10000}元失败，需手动提现')

    def run(self):
        self.get_info()
        if self.mode == 'hh':
            self.hh_td()
        self.read()
        self.tixian()


if __name__ == '__main__':
    for i in aiock:
        try:
            print('=' * 50 + f'\n账号{i["name"]}开始任务'+'='*50)
            api = Allinone(i, 'yb')
            api.run()
            time.sleep(5)
        except Exception as e:
            print(e)
            continue
