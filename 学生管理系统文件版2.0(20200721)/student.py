#!/usr/bin/env python3
import os


def base():
    # 判断路径和文件是否存在，不存在创建，存在以列表形式返回文件中的学生信息
    if not os.path.isdir('/data'):
        os.makedirs('/data')
    if not os.path.isfile('/data/database'):
        os.mknod('/data/database')
    with open('/data/database') as f:
        return f.readlines()


def adding(data):
    # 向文件内写入内容,删除用户时实现自增减
    with open('/data/database', 'a+') as d:
        d.write(str(data)+'\n')
        # print('追加成功')


def mycontinue(func):
    # 判断用户是否继续某个功能
    key = input('是否要继续进行此功能y/n:')
    if key == 'n':
        main()
    if key == 'y':
        func()


def isnull(f):
    # 如果文件为空返回主菜单
    if f == []:
        print('数据文件为空')
        main()


def add():
    # 向文件添加学生信息，如果文件为空学生的学号和序号从1开始
    # 如果文件不为空，序号和学号实现字增加
    # print(f)
    f = [eval(i) for i in base()]
    if f != []:
        # print(f)
        ID = int(f[-1]['ID']) + 1
        # print(ID)
        sid = int(f[-1]['sid']) + 1
        # print(sid)
    else:
        ID = 1
        sid = 1
    name = input('请输入学生姓名:')
    Linux = input('请输入学生Linux成绩:')
    Python = input('请输入学生Python成绩:')
    PHP = input('请输入学生php成绩')
    stu_info = ({'ID': ID, 'name': name, 'Linux': Linux,
                 'Python': Python, 'PHP': PHP, 'sid': sid})
    # print(stu_info)
    adding(stu_info)
    mycontinue(add)


def show():
    # 取出每个学生信息的字段值，如果文件为空，直接返回主菜单，格式化输出学生信息
    f = [eval(i) for i in base()]
    isnull(f)
    title = '{:^14}{:^1}\t{:^6}{:^15}{:^6}{:^10}'
    data = '{:^14}{:^1}\t{:^6}{:^15}{:^5}{:^11}'
    print(title.format('ID', '姓名', 'Linux', 'Python', 'PHP', '学号'))
    # print(f)
    for i in f:
        ID = i['ID']
        name = i['name']
        Linux = i['Linux']
        Python = i['Python']
        PHP = i['PHP']
        sid = i['sid']
        print(data.format(ID, name, Linux, Python, PHP, sid))


def delete():
    # 获取文件内容以列表形式返回，输入要删除的学生姓名和学号，判断是否在文件中，在文件中删除,不再文件中不返回删除成功
    f = [eval(i) for i in base()]
    isnull(f)
    name = input('请输入需要修改信息学生的姓名:')
    sid = int(input('请输入需要修改学生信息的学号:'))
    for i in f:
        if i['name'] == name and sid == i['sid']:
            f.remove(i)
            # print(f)
            print('删除成功')
            d = open('/data/database', 'w')
            d.close()
            if f != []:
                for i in range(len(f)):
                    f[i]['ID'] = i + 1
                    # print(f)
                    adding(f[i])
    if f != []:
        mycontinue(delete)
    else:
        main()


def deletes():
    f = [eval(i) for i in base()]
    isnull(f)
    with open('/data/database', 'w') as d:
        name = input('请输入需要修改信息学生的姓名:')
        sid = int(input('请输入需要修改学生信息的学号:'))
        for i in f:
            if i['name'] == name and sid == i['sid']:
                global ID
                ID = i['ID']
                # print(ID)
            else:
                if i['ID'] > ID:
                    i['ID'] = i['ID'] - 1
                d.write(str(i))


def modfiy():
    # 获取到文件信息以列表形式保存，如果文件为空返回主菜单，输入要修改学生信息的学生的姓名和学号，在选择修改那一科成绩，然后在遍历列表，取出每一项，保存列表中的每一项
    f = [eval(i) for i in base()]
    isnull(f)
    name = input('请输入需要修改信息的学生姓名:')
    sid = int(input('请输入需要修改信息的学生学号:'))
    for i in f:
        # print(i)
        if name == i['name'] and i['sid'] == sid:
            # print('aa')
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
            key = input(('请输入你要修改的成绩:'))
            if key == '1':
                Linux = input('请输入Linux成绩:')
                i['Linux'] = Linux
            if key == '2':
                Python = input('请输入Python成绩:')
                i['Python'] = Python
            if key == '3':
                PHP = input('请输入PHP成绩:')
                i['PHP'] = PHP

    with open('/data/database', 'w') as d:
        for i in range(len(f)):
            d.write(str(f[i])+'\n')
    mycontinue(modfiy)


def query():
    # 以列表形式返回文件内容，如果文件为空，直接返回主菜单.输入姓名和学号，如果学生在数据文件中，返回格式化学生信息，不再文件中不返回任何学生信息
    f = [eval(i) for i in base()]
    isnull(f)
    name = input('请输入学生姓名:')
    sid = int(input('请输入学生学号:'))
    title = '{:^14}{:^1}\t{:^6}{:^15}{:^6}{:^10}'
    data = '{:^14}{:^1}\t{:^6}{:^15}{:^5}{:^11}'
    print(title.format('ID', '姓名', 'Linux', 'Python', 'PHP', '学号'))
    for i in f:
        if name == i['name'] and i['sid'] == sid:
            ID = i['ID']
            name = i['name']
            Linux = i['Linux']
            Python = i['Python']
            PHP = i['PHP']
            sid = i['sid']
            print(data.format(ID, name, Linux, Python, PHP, sid))
    mycontinue(query)


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
             |              3.删除（1）             |
             |              4.删除（2）             |
             |              5.修改                  |
             |              6.查询                  |
             |                                      |
             ————————————————————————————————————————
             ''')
        key = input('请输入功能序号:')
        if key == '0':
            import sys
            sys.exit(0)
        if key == '1':
            add()
        if key == '2':
            show()
        if key == '3':
            deletes()
        if key == '4':
            delete()
        if key == '5':
            modfiy()
        if key == '6':
            query()


main()
