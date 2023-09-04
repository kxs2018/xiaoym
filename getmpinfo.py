# -*- coding: utf-8 -*-
# getmpinfo
# Author: kk
# date：2023/8/31 18:45
import re
from lxml import etree
import requests


def getmpinfo(link:str):
    if not link or link == '':
        return False
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; ANY-AN00 Build/HONORANY-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230701 MMWEBID/2833 MicroMessenger/8.0.40.2420(0x28002855) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'}
    res = requests.get(link, headers=headers)
    html = etree.HTML(res.text)
    # print(res.text)
    title = html.xpath('//meta[@*="og:title"]/@content')[0]
    url = html.xpath('//meta[@*="og:url"]/@content')[0]
    biz = re.findall(r'biz=(.*?)&', url)[0]
    username = html.xpath('//div[@class="wx_follow_nickname"]/text()|//strong[@role="link"]/text()|//*[@href]/text()')
    # print(username)
    username = username[0].strip()
    id = re.findall(r"user_name.DATA'\) : '(.*?)'", res.text) or html.xpath(
        '//span[@class="profile_meta_value"]/text()')
    id = id[0]
    text = f'公众号：{biz}|文章:{title}|帐号:{username}|id:{id}'
    mpinfo = {'biz': biz, 'text': text}
    # print(mpinfo)
    return mpinfo


if __name__ == '__main__':
    # link = 'https://mp.weixin.qq.com/s/JP4qeSANMYqYM4PQ0OG_Mg'
    # link = 'http://mp.weixin.qq.com/s?__biz=MzI0MDA2ODU0Ng==&mid=2651618628&idx=1&sn=06fd7a8faf97be7d9d74a7d878a9e16e&chksm=f2d8afe9c5af26ffe9fecfba0c64ae6fe508680571a4d283dce7109d56fe532495db346dfcc1#rd'
    link = 'https://mp.weixin.qq.com/s/7fUk_tmgx2EZqCCHIIav9w'
    getmpinfo(link)
