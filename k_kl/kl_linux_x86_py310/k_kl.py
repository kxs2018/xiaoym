"""
先运行脚本，有问题再到群里问 https://t.me/xiaoymgroup
new Env('可乐阅读');
"""

import kl
import platform  
  
os_info = f'操作系统：{platform.system()} {platform.release()} CPU架构：{platform.machine()} Python版本:{platform.python_version()}'
print(os_info)
print('构建环境 操作系统：Linux 4.19.0-25-amd64 CPU架构：x86_64 Python版本:3.10.13')
print('如不能运行，请尝试一样的环境')
kl.main()
