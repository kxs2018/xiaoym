"""
先运行脚本，有问题再到群里问 https://t.me/xiaoymgroup
new Env('鱼儿阅读-x86');
"""

import platform  
  
os_info = f'操作系统：{platform.system()} {platform.release()} CPU架构：{platform.machine()} Python版本:{platform.python_version()}'
print(os_info)
print('构建环境 操作系统：Windows 10 CPU架构：AMD64 Python版本:3.11.5')
print('如不能运行，请尝试一样的环境')
import yu
yu.main()
