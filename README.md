# 撸毛之微信阅读系列

> 加入每天赚单文件版，添加debug开关，默认为开。关闭只需将代码开头的debug=1改成0即可。

> 每天赚更新检测号

> 加入多线程单文件版脚本2个，无需繁琐设置，可自定义同时进行的任务数量。

> 为防止重新拉库搞乱配置，现已将config.py重命名为config.sample.py，新拉库的同学需要把config.sample.py重命名为config.py

> 花花、元宝、智慧等脚本已修复。
> 
> 星空暂时先不要跑，9.15下午开始平台更改了参数，已有大量账号被封。

### 安装部署
1. 青龙面板（推荐）：添加定时任务或订阅，名字随便，命令如下，国内网不好可以加代理如https://ghproxy.com/。定时随意。添加后立即运行一次。
```
 ql repo https://github.com/kxs2018/yuedu.git "" "" "qwbot|config|getmpinfo" "main" "py|md|txt"
```

2. 本地运行：【需安装python，手机可安装qpython，方法自行百度】用下方命令clone本项目到本地
```
git clone https://github.com/kxs2018/yuedu.git
```
   
##### 拉好代码后应`pip install -r requirements.txt` 或添加python依赖

### 合集活动入口

- 星空阅读阅读(kxkyd.py)：http://mr1693793443666.tozkjzl.cn/ox/index.html?mid=QR8YRLQNZ


- 元宝阅读(k元宝阅读.py)：http://mr134905063.znooqoqzk.cloud/coin/index.html?mid=CS5T87Q98


- 花花阅读(k花花阅读.py)：http://mr136777793.gfizovt.cn/user/index.html?mid=CR4RAD4JZ
  
- 人人帮(k人人帮.py)：http://ebb.nianshuiyong.cloud/user/index.html?mid=1694991329391673344
  
- 智慧阅读(k智慧阅读.py)：http://mr1694397085936.qmpcsxu.cn/oz/index.html?mid=2K4E46TVL


- 充值购买阅读(kczgm.py)：http://2502567.pkab.tz6pstg20fnm.cloud/?p=2502567


- 美添赚(kmtzyd.py)：http://tg.1694892404.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=168552


- 小阅阅阅读(kxyy.py)：https://wi56108.ejzik.top:10267/yunonline/v1/auth/0489574c00307cdb933067188854e498?codeurl=wi56108.ejzik.top:10267&codeuserid=2&time=1694865029

### 脚本说明
##### 特别说明：元宝花花星空人人帮智慧共用一个检测账号，几个都跑很容易黑号。单条文章收益花花是元宝星空智慧的1.5倍，检测频率现在改成一样了，建议先跑满花花，收益更大。
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

#### 仓库推荐：[小羊毛](https://github.com/kxs2018/xiaoym)

#### 有问题欢迎联系 [惜之酱](https://t.me/xizhijiang)    [tg频道](https://t.me/+uyR92pduL3RiNzc1)

## 特别声明
> 本仓库发布的脚本及其中涉及的任何解锁和解密分析脚本，仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断。

> 本项目内所有资源文件，禁止任何公众号、自媒体进行任何形式的转载、发布。

> 本人对任何脚本问题概不负责，包括但不限于由任何脚本错误导致的任何损失或损害。

> 间接使用脚本的任何用户，包括但不限于建立VPS或在某些行为违反国家/地区法律或相关法规的情况下进行传播, 本人对于由此引起的任何隐私泄漏或其他后果概不负责。

> 请勿将本仓库的任何内容用于商业或非法目的，否则后果自负。

> 如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。

> 任何以任何方式查看此项目的人或直接或间接使用该项目的任何脚本的使用者都应仔细阅读此声明。本人保留随时更改或补充此免责声明的权利。一旦使用并复制了任何相关脚本或Script项目的规则，则视为您已接受此免责声明。

> 您必须在下载后的24小时内从计算机或手机中完全删除以上内容.

> 您使用或者复制了本仓库且本人制作的任何脚本，则视为 已接受 此声明，请仔细阅读!
