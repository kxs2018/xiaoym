# -*- coding: utf-8 -*-
"""
用来把config.py转换成config.yaml，配置更方便
"""
import config
import subprocess

try:
    import yaml
except:
    process = subprocess.Popen(['pip', 'install', 'PyYAML'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode == 0:
        print("PyYAML已成功安装")
    else:
        print("安装失败：")
        print(error.decode('utf-8'))
names = dir(config)
names = [name for name in names if not name.startswith(('__', '_')) and not callable(getattr(config, name))]
conf = {}
for name in names:
    conf.update({name: getattr(config, name)})
print(conf)
with open('1config.yaml', 'w') as fi:
    yaml.safe_dump(conf, fi, encoding='utf-8', allow_unicode=True)
