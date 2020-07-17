#!/usr/bin/env python3

import sys

alist = [{'name':'wwine','success':'18','class':'4','id':'1'},{'name':'tom','success':'18','class':'4','id':'2'}]    # 姓名 年龄 班级 学号

def add():
    count = int(alist[-1]['id'])
    ID = str(count + 1)
    name = input('请输入你的名字:')
    success = input('请输入你的成绩:')
    onlist = {'name':name,'success':success,'class':'4','id':ID}
    alist.append(onlist)
    print('添加成功')
    test()

def zs():
    print(  '_'*38+" ")
    print(" "*1+'姓名'," "*3+'成绩',' '*3+'班级',' '*3+'学号',)
    print(  '_'*38+" ")
    for i in range(len(alist)):
        print(" "*1+alist[i].get('name')," "*4+alist[i].get('success'),' '*4+alist[i].get('class'),' '*4+alist[i].get('id'))
        print(  '_'*38+" ")

def query():
    print('''
    |----------成绩查询系统----------|
    |        请输入学号你要怎么查询  |
    |        1.姓名查询              |
    |        2.学号查询              |
    |        默认学号查询            |
    |--------------------------------|
    ''')

    num = input('请输入:')
    if num == '1':
        name = input('请输入你的姓名:')
        for i in range(len(alist)):
            if alist[i]['name'] == name:
                print(  '_'*38+" ")
                print(" "*1+'姓名'," "*3+'成绩',' '*3+'班级',' '*3+'学号',)
                print(  '_'*38+" ")
                print(" "*1+alist[i].get('name')," "*4+alist[i].get('success'),' '*4+alist[i].get('class'),' '*4+alist[i].get('id'))
                print(  '_'*38+" ")
                test()
        print('学生不存在')
    else:
        ID = input('请输入你的学号:')
        for i in range(len(alist)):
            if alist[i]['id'] == ID:
                print(  '_'*38+" ")
                print(" "*1+'姓名'," "*3+'成绩',' '*3+'班级',' '*3+'学号',)
                print(  '_'*38+" ")
                print(" "*1+alist[i].get('name')," "*4+alist[i].get('success'),' '*4+alist[i].get('class'),' '*4+alist[i].get('id'))
                print(  '_'*38+" ")
                test()
        print('学生不存在')





def delt():
    while True:
        zs()
        name = input('请输入要用户名:')
        Id = input('请输入你的学号:')
        for i in range(len(alist)):
            if  name == alist[i]['name'] and Id == alist[i]['id'] :
                global n
                n = i
                print('已删除用户',alist[i]['name'])
                del alist[i]
                for i in range(len(alist)):
                    if i >= n:
                        num=int(alist[i]['id'])
                        alist[i]['id']= str(num - 1)
                test()
    print('输入用户名不存在请重新输入')

def xg():
    zs()
    name = input('请输入你要修改的学生姓名:')
    for i in range(len(alist)):
        if alist[i]['name'] == name:
            while True:
                print('''
               |----------成绩修改系统---------|
               |         1.姓名                |
               |         2.成绩                |
               |         3.班级                |
               |         4.学号                |
               |-------------------------------|
                        ''')
                zs()
                num = input('请输入:')
                if num == '1':
                    s = input('请输入你要修改的内容:')
                    alist[i]['name'] = s
                    test()
                elif num == '2':
                    s = input('请输入你要修改的内容:')
                    alist[i]['success'] = s
                    test()
                elif num == '3':
                    s = input('请输入你要修改的内容:')
                    alist[i]['class'] = s
                    test()
                elif num == '4':
                    s = input('请输入你要修改的内容:')
                    alist[i]['class'] = s
                    test()
            else:
                print('你输入的序号不在列表里，请重新输入')




def test():
    print('''
    |---------学生成绩系统----------|
    |       请输入输入序号          |
    |       1.添加学生信息          |
    |       2.展示学生信息          |
    |       3.删除学生信息          |
    |       4.修改学生信息          | 
    |       5.查询某个学生信息      |
    |       0.退出系统              |
    |-------------------------------|
            ''')
    n = input('请输入:')
    if n == '1':
        add()
    elif n == '2':
        zs()
        test()
    elif n == '3':
        delt()
    elif n == '4':
        xg()
    elif n == '5':
        query()
    elif n == '0':
        sys.exit(0)
    else:
        test()


test()
