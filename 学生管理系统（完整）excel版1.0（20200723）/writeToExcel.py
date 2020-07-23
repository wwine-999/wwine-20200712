#!/usr/bin/env python3

'''
    交互的输入学生信息，保存到excel表格
    当文件存在创建
    不存在，创建
'''

import pandas as pd


def ipt():
    # 输入姓名和年龄，并把姓名和年龄分别保存到name_list和age_list列表里边,然后在把name_list和age_list放到d字典里边，读取原excel内容，然后在和本次要输入的内容一起写入excel表格
    name = input('请输入你的姓名:')
    age = input('请输入你的年龄:')
    name_list = []
    age_list = []
    name_list.append(name)
    age_list.append(age)
    d = {'name': name_list, 'age': age_list}
    f1 = pd.DataFrame(pd.read_excel('test.xlsx'))
    f2 = pd.DataFrame(d)
    pd.concat([f1, f2]).to_excel('test.xlsx', index=False)
    print(pd.read_excel('test.xlsx'))


def r():
    d = pd.DataFrame(pd.read_excel('test.xlsx'))
    a = d.T.to_dict()
    # print(a)
    return a


def mycontinue(func):
    # 判断用户是否继续某个功能
    key = input('是否要继续进行此功能y/n:')
    if key == 'n':
        main()
    if key == 'y':
        func()


def INPUT():
    # 输入所需要的信息，把他们以列表形式放入字典，有excel表格追加进入excel表格，没有excel表格创建并添加
    name = input('请输入你的姓名:')
    age = input('请输入你的年龄:')
    Linux = input('请输入你的Linux成绩:')
    PHP = input('请输入你的PHP成绩:')
    Python = input('请输入你的Python成绩:')
    name_list = []
    age_list = []
    Linux_list = []
    PHP_list = []
    Python_list = []
    name_list.append(name)
    age_list.append(age)
    Linux_list.append(Linux)
    PHP_list.append(PHP)
    Python_list.append(Python)
    try:
        a = r()
        ID = a[len(a)-1]['sid'] + 1
        d = ({'name': name_list, 'age': age_list, 'Linux': Linux_list,
              'PHP': PHP_list, 'Python': Python_list, 'sid': ID})
        # print(d)
        f1 = pd.DataFrame(pd.read_excel('test.xlsx'))
        f2 = pd.DataFrame(d)
        pd.concat([f1, f2]).to_excel('test.xlsx', index=False)
        # print(pd.read_excel('test.xlsx'))
        print('添加成功')
    except BaseException:
        print('添加成功')
        d = ({'name': name_list, 'age': age_list, 'Linux': Linux_list,
              'PHP': PHP_list, 'Python': Python_list, 'sid': 1})
        f1 = pd.DataFrame(d)
        f1.to_excel('test.xlsx', index=False)
    mycontinue(INPUT)


def show():
    # 取出每个学生信息的以字典形式，如果文件不存在或为空返回主菜单，存在不为空格式化输出学生信息
    try:
        print(pd.read_excel('test.xlsx'))
        # title = '{:^12}{:^1}\t{:^6}{:^15}{:^15}'
        # data = '{:^14}{:^1}\t{:^6}{:^15}{:^15}'
        # print(title.format('姓名', 'Linux', 'Python', 'PHP', '学号'))
        # a = r()
        # print(a)
        # for i in a:
        #    # print(i)
        #    name = a[i]['name']
        #    # print(name)
        #    Linux = a[i]['Linux']
        #    # print(Linux)
        #    Python = a[i]['Python']
        #    # print(Python)
        #    PHP = a[i]['PHP']
        #    # print(PHP)
        #    sid = a[i]['sid']
        #    print(data.format(name, Linux, Python, PHP, sid))
    except BaseException:
        print('文件不存在或内容为空,返回主菜单')
        main()


def delete():
    # 获取文件内容以字典形式，输入要删除的学生姓名和学号，判断是否在文件中，在文件中删除,不再文件中不返回删除成功，然后遍历字典，存入文件，剩余最后一条数据不可删除
    try:
        name = input('请输入删除学生的姓名:')
        sid = int(input('请输入删除学生的学号:'))
        a = r()
        n = [i for i in a if a[i]['name'] == name and sid == a[i]['sid']]
        if n == []:
            print('输入错误')
            mycontinue(delete)
        n = n[0]
        del a[n]
        print('删除成功')
        # print(a)
        name_list = []
        age_list = []
        Linux_list = []
        PHP_list = []
        Python_list = []
        sid_list = []
        # print('123')
        for i in a:
            name = a[i]['name']
            age = a[i]['age']
            Linux = a[i]['Linux']
            PHP = a[i]['PHP']
            Python = a[i]['Python']
            sid = a[i]['sid']
            name_list.append(name)
            age_list.append(age)
            Linux_list.append(Linux)
            PHP_list.append(PHP)
            Python_list.append(Python)
            sid_list.append(sid)
            # print(name_list)
            # print(age_list)
            # print(Linux_list)
            # print(PHP_list)
            # print(Python_list)
            # print(sid_list)
        d = ({'name': name_list, 'age': age_list, 'Linux': Linux_list,
              'PHP': PHP_list, 'Python': Python_list, 'sid': sid_list})
        # print(d)
        f1 = pd.DataFrame(d)
        # print(f1)
        f1.to_excel('test.xlsx', index=False)
    except BaseException:
        print('剩余最后一条数据不可删除')
        main()
    mycontinue(delete)


def modfiy():
    # 输入要修改信息的学生姓名和学号，如果不存在该学生，返回学生不存在，返回主菜单，存在进入选择修个成绩界面，修改完成后写入excel表格
    name = input('请输入删除学生的姓名:')
    sid = int(input('请输入删除学生的学号:'))
    a = r()
    n = [i for i in a if a[i]['name'] == name and sid == a[i]['sid']]
    if n == []:
        print('输入错误,获取不到学生信息，返回主菜单')
        mycontinue(delete)
    n = n[0]
    print('''
             ————————————————————————————————————————
             |                                      |
             |             成绩修改                 |
             |                                      |
             |              1.Linux                 |
             |              2.Python                |
             |              3.PHP                   |
             |                                      |
             ————————————————————————————————————————
             ''')
    key = input('请输入你要修改的成绩:')
    if key == '1':
        Linux = int(input('请输入你的Linux成绩:'))
        a[n]['Linux'] = Linux
    if key == '2':
        Python = int(input('请输入你的Python成绩:'))
        a[n]['Python'] = Python
    if key == '3':
        PHP = int(input('请输入你的PHP成绩:'))
        a[n]['PHP'] = PHP
    name_list = []
    age_list = []
    Linux_list = []
    PHP_list = []
    Python_list = []
    sid_list = []
    for i in a:
        name = a[i]['name']
        age = a[i]['age']
        Linux = a[i]['Linux']
        PHP = a[i]['PHP']
        Python = a[i]['Python']
        sid = a[i]['sid']
        name_list.append(name)
        age_list.append(age)
        Linux_list.append(Linux)
        PHP_list.append(PHP)
        Python_list.append(Python)
        sid_list.append(sid)
    d = ({'name': name_list, 'age': age_list, 'Linux': Linux_list,
          'PHP': PHP_list, 'Python': Python_list, 'sid': sid_list})
    f1 = pd.DataFrame(d)
    f1.to_excel('test.xlsx', index=False)
    mycontinue(modfiy)


def query():
    name = input('请输入删除学生的姓名:')
    sid = int(input('请输入删除学生的学号:'))
    a = r()
    n = [i for i in a if a[i]['name'] == name and sid == a[i]['sid']]
    if n == []:
        print('输入错误,获取不到学生信息，返回主菜单')
        mycontinue(delete)
    n = n[0]
    # print(a[n])
    d = ({'name': [a[n]['name']], 'age': [a[n]['age']],
          'Linux': [a[n]['Linux']], 'PHP': [a[n]['PHP']],
          'Python': [a[n]['Python']], 'sid': [a[n]['sid']]})
    f1 = pd.DataFrame(d)
    print(f1)


def main():
    # 主菜单
    while True:
        print('''
             ————————————————————————————————————————
             |                                      |
             |           学生管理系统文件版         |
             |                                      |
             |              0.结束                  |
             |              1.添加                  |
             |              2.展示                  |
             |              3.删除                  |
             |              4.修改                  |
             |              5.查询                  |
             |                                      |
             ————————————————————————————————————————
             ''')
        key = input('请输入功能序号:')
        if key == '0':
            import sys
            sys.exit(0)
        if key == '1':
            INPUT()
        if key == '2':
            show()
        if key == '3':
            delete()
        if key == '4':
            modfiy()
        if key == '5':
            query()


main()
