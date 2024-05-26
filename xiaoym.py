# -*- coding: utf-8 -*-

"""
先运行脚本，有问题再到群里问 https://t.me/xiaoymgroup
new Env('');
"""
import platform
import sys
import os
import subprocess


def check_environment(file_name):
    python_info, os_info, cpu_info = sys.version_info, platform.system().lower(), platform.machine().lower()
    print(
        f"Python版本: {python_info.major}.{python_info.minor}.{python_info.micro}, 操作系统类型: {os_info}, 处理器架构: {cpu_info}")
    pyinfo = f'py{python_info.major}{python_info.minor}'
    if (python_info.minor in [9, 10, 11, 12]) and os_info in ['linux', 'windows'] and cpu_info in ['x86_64', 'aarch64',
                                                                                                   'amd64']:
        print("符合运行要求")
        check_so_file(file_name, pyinfo, os_info, cpu_info)
    else:
        if not (python_info.minor in [9, 10, 11, 12]):
            print("不符合要求: Python版本不是3.9 3.10 3.11 3.12")
        if cpu_info not in ['x86_64', 'aarch64', 'amd64']:
            print("不符合要求: 处理器架构不是x86_64 aarch64  amd64")


def check_so_file(filename, pyinfo, sys_info, cpu_info):
    if sys_info == 'windows':
        file_name = 'xiaoym.pyd'
    if sys_info == 'linux':
        file_name = 'xiaoym.so'
    if os.path.exists(file_name):
        print(f"{file_name} 存在")
        import xiaoym
        xiaoym.main(filename)
    else:
        print(f"不存在{file_name}文件,准备下载文件")
        url = f'https://gitlab.com/xizhiai/xiaoym/-/raw/master/'
        download_so_file(filename, pyinfo, sys_info, cpu_info, main_url=url)


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


def download_so_file(filename, pyinfo, sys_info, cpu_info, main_url):
    if sys_info == 'windows':
        file_name = f'xiaoym.{pyinfo}_{cpu_info}_{sys_info}.pyd'
        f_name = 'xiaoym.pyd'
    if sys_info == 'linux':
        file_name = f'xiaoym.{pyinfo}_{cpu_info}_{sys_info}.so'
        f_name = 'xiaoym.so'
    url = main_url + file_name
    print(url)
    command = ['curl', '-#', '-o', f_name, url]
    result = run_command(command)
    if result == 0:
        print(f"下载完成：{f_name},调用check_so_file函数")
        check_so_file(filename, pyinfo, sys_info, cpu_info)
    else:
        print(f"下载失败：{f_name}")


if __name__ == '__main__':
    check_environment('ddz')  # 点点:ddz，猫猫:mm 月月：xyy 每天赚:mtz 可乐：kl 可乐专属：kldyd 鱼儿：yu （每天赚暂未支持）
