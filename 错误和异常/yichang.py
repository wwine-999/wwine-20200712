#!/usr/bin/env python
def f():
    try:
        '''
        这里是没有发生异常执行的代码
        '''
        while True:
            print(2/0)
    except Exception:
        '''
        这里是发生异常执行的代码
        '''
        print('除数不能为0')


def main():
    f()


main()
