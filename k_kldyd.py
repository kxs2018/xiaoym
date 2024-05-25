# -*- coding: utf-8 -*-
"""
new Env('可乐专属阅读');
cron:6 9 1 1 1
使用此脚本会随机从你的ck里选取一定数量的ck为作者助力阅读，每5个抽选一个，2-4个算5个
如介意，请勿使用此脚本
"""

# -*- coding: utf-8 -*-

"""
先运行脚本，有问题再到群里问 https://t.me/xiaoymgroup
new Env('点点');
"""
import platform
import sys
import os
import subprocess
import importlib

def check_environment(file_name):
    python_info, os_info, cpu_info = sys.version_info, platform.system().lower(), platform.machine().lower()
    print(
        f"Python版本: {python_info.major}.{python_info.minor}.{python_info.micro}, 操作系统类型: {os_info}, 处理器架构: {cpu_info}")
    if (python_info.minor in [10]) and os_info in ['linux', 'windows'] and cpu_info in ['x86_64', 'aarch64', 'amd64']:
        print("符合运行要求")
        check_so_file(file_name, os_info, cpu_info)
    else:
        if not (python_info.minor in [10]):
            print("不符合要求: Python版本不是3.10")
        if cpu_info not in ['x86_64', 'aarch64', 'amd64']:
            print("不符合要求: 处理器架构不是x86_64 aarch64  amd64")


def check_so_file(filename, sys_info, cpu_info):
    if sys_info == 'windows':
        file_name = filename + '.pyd'
    if sys_info == 'linux':
        file_name = filename + '.so'
    if os.path.exists(file_name):
        print(f"{file_name} 存在")
        try:
            module = importlib.import_module(filename)
            module.main()
        except Exception as e:
            print(e)
    else:
        print(f"不存在{file_name}文件,准备下载文件")
        url = f'https://gitlab.com/xizhiai/xiaoym/-/raw/master/{filename}'
        download_so_file(filename, sys_info, cpu_info, main_url=url)


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
    if sys_info == 'windows':
        file_name = f'{filename}.{cpu_info}_{sys_info}.pyd'
        f_name = filename +'.pyd'
    if sys_info == 'linux':
        file_name = f'{filename}.{cpu_info}_{sys_info}.so'
        f_name = filename +'.so'
    url = main_url + '/' + file_name
    print(url)
    command = ['curl', '-#', '-o', f_name, url]
    result = run_command(command)
    if result == 0:
        print(f"下载完成：{filename},调用check_so_file函数")
        check_so_file(filename, sys_info, cpu_info)
    else:
        print(f"下载失败：{filename}")


if __name__ == '__main__':
    check_environment('kldyd')
