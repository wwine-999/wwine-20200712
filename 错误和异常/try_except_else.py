#!/usr/bin/env python3

def f():
    try:
        n = int(input('请输入被除数:'))
        y = int(input('请输入除数:'))
        jg = n/y
    except Exception:
        print('除数不能为0')

    else:
        print(n, '除以', y, '等于', jg)


f()
