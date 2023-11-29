"""
先运行脚本，有问题再到群里问 https://t.me/xiaoymgroup
new Env('文博大会答题');
cron: 6 6 6 6 6
"""
import platform
import sys
import os
import subprocess


def check_environment(file_name):
    python_info, os_info, cpu_info = sys.version_info, platform.system().lower(), platform.machine().lower() 
    print(f"Python版本: {python_info.major}.{python_info.minor}.{python_info.micro}, 操作系统类型: {os_info}, 处理器架构: {cpu_info}")
    if (python_info.minor in [10]) and os_info in ['linux','windows'] and cpu_info in ['x86_64', 'aarch64', 'amd64']:
        print("符合运行要求")
        check_so_file(file_name, os_info,cpu_info)
    else:
        if not (python_info.minor in [10]):
            print("不符合要求: Python版本不是3.10")
        if cpu_info not in ['x86_64', 'aarch64', 'armv8','amd64']:
            print("不符合要求: 处理器架构不是x86_64 aarch64 amd64")


def check_so_file(filename,sys_info, cpu_info):
    if sys_info == 'windows':
        filename=os.path.splitext(filename)[0]+'.pyd'
    if sys_info == 'linux':
        filename = os.path.splitext(filename)[0]+'.so'
    check_json_file()
    if os.path.exists(filename):
        print(f"{filename} 存在")
        import wbdh
        wbdh.main()
    else:
        print(f"不存在{filename}文件,准备下载文件")
        url = f'https://jihulab.com/xizhiai/xiaoym/-/raw/main/{os.path.splitext(filename)[0]}'
        download_so_file(filename, sys_info, cpu_info,main_url=url)

def check_json_file():
    filename='wbtk.json'
    if os.path.exists(filename):
        print(f"题库文件存在，正在更新")
        os.remove(filename)
    else:print('正在下载题库文件')
    url = 'https://jihulab.com/xizhiai/xiaoym/-/raw/main/wbdh/wbtk.json'
    command = ['curl', '-#', '-o', filename, url]
    # 执行命令并处理输出
    result = run_command(command)
    if result == 0:
        print(f"题库文件wbtk.json下载完成")
    else:        
        print(f"题库文件wbtk.json下载失败")
    
def run_command(command):
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, 
        text=True  
    )
    for line in process.stdout:
        line = line.strip()
        if "%" in line:
            print(line)
    process.wait()
    return process.returncode


def download_so_file(filename, sys_info, cpu_info, main_url):
    file_base_name = os.path.splitext(filename)[0]
    if sys_info == 'windows':
        url = main_url + f'/{file_base_name}.{cpu_info}_{sys_info}.pyd'
    if sys_info == 'linux':
        url = main_url + f'/{file_base_name}.{cpu_info}_{sys_info}.so'
    print(url)
    # print(github_url)
    # 您的命令，使用 -# 参数显示下载进度
    command = ['curl', '-#', '-o', filename, url]
    # 执行命令并处理输出
    result = run_command(command)
    if result == 0:
        print(f"下载完成：{filename},调用check_so_file函数")
        check_so_file(filename,sys_info,cpu_info)
    else:        
        print(f"下载失败：{filename}")
            

if __name__ == '__main__':
    check_environment('wbdh.so')

