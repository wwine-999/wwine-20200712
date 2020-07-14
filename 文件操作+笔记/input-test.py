#!/usr/bin/env python3

def f1():
    sname = input('请输入你的姓名:')
    gen = input('请输入你的性别:')
    age = input('请输入你的年龄:')
    with open('database/a.txt','a+') as f:
        s = f.read()
        if 's' == "":
            f.write(',')
        d = {'姓名':sname,'性别':gen,'年龄':age}
        f.write(str(d))
    test()
def add():
    import shutil
    shutil.rmtree('database')
    import os
    os.mkdir('database')
    os.mknod('database/a.txt')

def test():
    n = input('请输入:')
    if n == '1':
        import sys
        sys.exit(0)
    else:
        f1()
test()
