#!/usr/bin/env python3

#导入必要模块
import os 
import shutil 
from shutil import ignore_patterns,copystat,copy2,copytree

def copy(src,dst,files=ignore_patterns('*.txt')):
    if not os.path.exists(dst): # 判断目标目录是否存在
        os.makedirs(dst)
        print('创建成功')
    name = os.listdir(dst)
    if src in name:
        paths = os.path.join(dst,src)
        if os.stat(paths).st_mtime - os.stat(src).st_mtime <1:
            if os.path.isfile(src):
                shutil.copy2(src,dst)
            else:
                shutil.copytree(src,paths,ignore=files)
            print('复制成功')
        else:
            print('文件不是最新')
    else:
        if os.path.isfile(src):
            shutil.copy2(src,dst)
        else:
            shutil.copytree(src,paths,ignore=files)
        print('复制成功')

src = input('请输入你的源文件或目录:')
dst = input('请输入人你的目标目录:')
copy(src,dst)
