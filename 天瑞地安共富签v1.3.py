# -*- coding: utf-8 -*-
# 天瑞地安共富签
# Author: kk
# date：2023/9/14 11:59
"""
本脚本适用于天瑞地安APP共富签
连签奖励
抓包 https://crm.rabtv.cn，在请求体内找到Authorization的值（Bearer xxxxxxxxxx）
青龙配置文件添加：
-------------------------------------
export trdack=[{'ck':'Bearer xxxxxxxxxx'},{'ck':'Bearer xxxxxxxxxx'}]
多个账号增加大括号即可，报错可尝试用双引号把中括号包起来
export trdack="[{'ck':'Bearer xxxxxxxxxx'}]"
-------------------------------------
推送配置：
-------------------------------------
export pushconfig={"apptoken":"","topicids":[123456],"uids"=["uid_xxxxxx"]}
报错可尝试用单引号把大括号包起来
相关参数在https://wxpusher.zjiecode.com/admin/main找
文档https://wxpusher.zjiecode.com/docs/#/
-------------------------------------
"""

import time
import requests
from random import randint
import os
import ast


def push(msg, title='通知', uid=None):
    pushconfig = os.getenv('pushconfig')
    try:
        pushconfig = ast.literal_eval(pushconfig)
    except:
        pass
    if not pushconfig:
        return
    appToken = pushconfig['appToken']
    topicids = pushconfig['topicids']
    uids = pushconfig['uids']
    if uid:
        uids.append(uid)
    content = "# title \n\n<font size=4>msg\n\n通知by:\thttps://github.com/kxs2018/xiaoym\n[加入惜之酱的频道](https://t.me/+uyR92pduL3RiNzc1)</font>".replace('msg',
                                                                                                                 msg).replace(
        'title', title)
    body = {
        "appToken": appToken,
        "content": content,
        "summary": title,  # 消息摘要，显示在微信聊天页面或者模版消息卡片上，限制长度100，可以不传，不传默认截取content前面的内容。
        "contentType": 3,  # 内容类型 1表示文字  2表示html(只发送body标签内部的数据即可，不包括body标签) 3表示markdown
        # "topicIds": topicids,  # 发送目标的topicId，是一个数组！！！，也就是群发，使用uids单发的时候， 可以不传。
        "uids": uids,  # 发送目标的UID，是一个数组。注意uids和topicIds可以同时填写，也可以只填写一个。
        "url": 'url',  # 原文链接，可选参数
        "verifyPay": False  # 是否验证订阅时间，true表示只推送给付费订阅用户，false表示推送的时候，不验证付费，不验证用户订阅到期时间，用户订阅过期了，也能收到。
    }
    urlpust = 'http://wxpusher.zjiecode.com/api/send/message'
    res = requests.post(url=urlpust, json=body).json()
    if res.get('code') != 1000:
        print(res.get('msg'), res)
    return res


class TRDA:
    def __init__(self, ck):
        self.s = requests.session()
        self.s.headers = {"Authorization": ck['ck'],
                          "User-Agent": "Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36;xsb_ruian;xsb_ruian;2.31.742;native_app",
                          }  # user-agent 可换成自己的
        self.msg = ''

    def user_info(self):
        url = 'https://crm.rabtv.cn/v2/index/userInfo'
        res = self.s.post(url).json()
        print('userinfo ', res)
        if res.get('code') == 1:
            self.un = res.get('data').get('beauty_mobile')
            money = res.get('data').get('common_user').get('money')
            num = ''.join(res.get('data').get('continue_sign_num'))
            if num.startswith('0'):
                num=num[1:]
            total_sign_num = res.get('data').get('total_sign_num')
            m = f'【{self.un}】：当前红包{money}元，已连续签到{num}天，总签到{total_sign_num}天'
            print(m)
            self.msg += f'{m}\n '
            return True
        else:
            print(res.get('msg'))
            return False

    def signin(self):
        global msg
        sign_url = 'https://crm.rabtv.cn/v2/index/signIn'
        res = self.s.post(sign_url).json()
        print('signin ',res)
        if res.get('code') == 0:
            msg = res.get("msg")
            if 'plz-check-mobile' in msg:
                push(f'{self.un} 天瑞地安签到需验证手机，请手动签到')
        elif res.get('code') == 1:
            ptype = res.get('data')['type']
            p = res.get('data').get(ptype)
            num = res.get('data').get('continue_sign_num')
            if ptype == 'score':
                msg = f'签到成功，获得{p}积分，连续签到{num}天'
            else:
                msg = f'签到成功，获得{p} {ptype}，连续签到{num}天'
        msg = f'【{self.un}】：{msg}'
        print(msg)
        self.msg += f'{msg}\n '

    def get_prize(self):
        pids = [124201, 125288, 127559]
        url = 'https://crm.rabtv.cn/v2/user/getPrizeV'
        for pid in pids:
            res = self.s.post(url, data={'id': pid}).json()
            print(f'getprize ', res)
            if res.get('code') == 0:
                continue
            elif res.get('code') == 1:
                ptype = res.get('data')['type']
                p = res.get('data').get(ptype)
                m = f'【{self.un}】：连续签到奖励，获得{p} {ptype}'
                print(m)
                self.msg += f'{m}\n '

    def chou(self):
        url = 'https://guess.rabtv.cn/v1/task/do'
        for i in range(1, 5):
            data = {'id': i}
            res = self.s.get(url, data=data).json()
            print('task_current ', res)
            if res.get('done'):
                m = f'[任务{i}]抽奖完成，获得红包{res.get("v")}元'
                self.msg += m + '\n'
                print(m)
            elif res.get('code') == 0:
                m = f'[任务{i}]：{res.get("msg")}'
                self.msg += m + '\n'
                print(m)
            time.sleep(randint(3, 6))

    def run(self):
        if self.user_info():
            self.signin()
            self.get_prize()
            self.chou()
            self.msg += '-' * 20 + '\n'
            return self.msg


def ran_time():
    t1 = randint(3, 10)
    t2 = randint(3, 10)
    t1 **= 1.5
    t2 **= 2
    t = randint(int(t1 * 8), t2 * 15) if int(t1 * 8) < t2 * 15 else randint(t2 * 15, int(t1 * 8))
    return t


if __name__ == '__main__':
    msg = ''
    # trdack = os.getenv('trdack')
    trdack = [
        {"ck": "Bearer 5105169cb11ff02a9e232f8a54cf9240"},
        # {"ck": "Bearer zalqi1eoa2e32txzm3xfzpusqn3ct0n5"},
    ]
    try:
        trdack = ast.literal_eval(trdack)
    except:
        pass
    t = int(ran_time() / 10)
    print(f'{t}秒后开始签到')
    # time.sleep(t)
    for i, j in enumerate(trdack, start=1):
        try:
            api = TRDA(j)
            msg += api.run()
            if j != trdack[-1]:
                t = ran_time()
                print(f'{t}后进行下一个签到')
                # time.sleep(t)
        except Exception as e:
            print(f'第{i}个账号签到错误\n\n{e}')
            msg += f'第{i}个账号签到错误\n\n{e}'
            continue
    # push(msg, title=f'天瑞地安共富签信息', uid=None)  # 在pushconfig设定的uid之外，还可添加额外的uid，只需把None替换成'uid_xxxx'
