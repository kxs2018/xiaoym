import kl
import platform  
  
# 获取操作系统信息  
os_info = f'操作系统：{platform.system()} {platform.release()} CPU架构：{platform.machine()} Python版本:{platform.python_version()}'
print(os_info)
print('构建环境 操作系统：Linux 5.15.138-ophub CPU架构：aarch64 Python版本:3.10.12')
print('如不能运行，请尝试一样的环境')
kl.main()
