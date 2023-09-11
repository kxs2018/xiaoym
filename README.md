# 撸毛之微信阅读系列

### 安装部署
1. 青龙面板（推荐）：添加定时任务或订阅，名字随便，命令如下，国内网不好可以加代理如https://ghproxy.com/。定时随意。添加后立即运行一次。
```
 ql repo https://github.com/kxs2018/yuedu.git
```

2. 本地运行：【需安装python，手机可安装qpython，方法自行百度】用下方命令clone本项目到本地
```
git clone https://github.com/kxs2018/yuedu.git
```
   
##### 拉好代码后应`pip install -r requirements.txt` 或添加python依赖

### 合集活动入口

- 星空阅读阅读(kxkyd.py)：http://mr1693793443666.tozkjzl.cn/ox/index.html?mid=QR8YRLQNZ


- 元宝阅读(kybyd.py)：http://mr1693635846547.kgtpecv.cn/coin/index.html?mid=5U4W6ZWPT


- 花花阅读(k花花阅读.py)：http://mr1693635317854.stijhqm.cn/user/index.html?mid=FK73K93DA
  
- 人人帮(k人人帮.py)：http://ebb.nianshuiyong.cloud/user/index.html?mid=1694991329391673344
  
- 智慧阅读(k智慧阅读.py)：http://mr1694397085936.qmpcsxu.cn/oz/index.html?mid=QX5E9WLGS


- 充值购买阅读(kczgm.py)：http://2502567.pkab.tz6pstg20fnm.cloud/?p=2502567


- 美添赚(kmtzyd.py)：http://tg.1693634614.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=113565


- 小阅阅阅读(kxyy.py)：https://wi40796.sxcwpe.top:10259/yunonline/v1/auth/0489574c00307cdb933067188854e498?codeurl=wi40796.sxcwpe.top:10259&codeuserid=2&time=1693635112

### 脚本说明
##### 特别说明：元宝花花星空人人帮智慧共用一个检测账号，几个都跑很容易黑号。单条文章收益花花是元宝星空智慧的1.5倍，但是检测频率是其它的3倍以上，建议具体看个人取舍。
##### 人人帮一天30篇文章1条检测，跑满收益是0.6，建议跑满。
- kxxx.py是活动脚本，添加到青龙面板是建议使用英文字母，例如czgm.py，否则有无法运行的可能。
- config.py是配置文件，请勿改名。
- qwbot.py是推送模块文件，请勿改名。
- getmpinfo.py是微信文章解析模块文件，请勿改名。
- check.py是手动测试文件，手动测试你填写的参数是否正确
- requirements.txt是依赖文件，没有依赖脚本跑不起来

### 配置config.py

   请按内附说明填写相关配置

### 运行前准备

- 电脑运行请先安装python，手机运行使用QPython软件，运行前使用命令pip3 install -r requirements.txt添加依赖
- 青龙运行请先复制requirements.txt里的所有内容，添加到青龙面板依赖菜单python选项，
  (不会请先问百度)
  <img src="https://i.ibb.co/YkvPSfw/11-14-22-1a2c3190414bbb47831b867cdc7974e8-508d11540.png" alt="image-20230904111421402" style="zoom:50%;" />

### 运行

- 把全部脚本放在同一层级的目录运行
- 运行前可先执行check.py，检测参数是否正确
- 电脑双击选择python执行或在阅读脚本目录打开cmd/powershell运行python kxxxx.py
- 手机请自行百度QPython软件使用方法
- 青龙可以禁用任务，可手动点击执行
### [多线程版](https://github.com/kxs2018/yddxc)
##### 有问题欢迎联系 [惜之酱](https://t.me/xizhijiang) [tg频道](https://t.me/+uyR92pduL3RiNzc1)
