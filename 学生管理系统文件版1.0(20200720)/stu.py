#!/usr/bin/env /python3
import os
# 添加学生信息


def data():
    # 判断文件是否存在,不存在创建
    if not os.path.isfile('database'):
        os.mknod('database')
        # print('创建成功')
    with open('database', 'r') as f:
        return f.readlines()    # 打开文件，并以列表形式返回


def add():
    def d():
        # 序号实现自增减
        for i in range(len(alist)):
            ID = 1 + i
            alist[i]['ID'] = ID
        # 打开并写入文件
        with open('database', 'w') as d:
            for i in alist:
                wri = i
                writed = str(wri)+"\n"
                d.write(writed)
        d.close()
    f = data()
    # 判断文件是否为空
    alist = [eval(i) for i in f]  # 把列表中的字符串，转换为字典
    make = True
    while make:
        if alist == []:
            # 文件为空，序号和学号都为1
            ID = 1
            stuid = 1
        else:
            # 文件不为空
            ID = int(alist[-1]['ID']) + 1   # 序号字增加
            stuid = int(alist[-1]['stuid']) + 1  # 学号字增加
        name = input('请输入你的姓名:')
        age = input('请输入你的年龄:')
        wri = {'ID': ID, 'name': name, 'age': age, 'stuid': stuid}  # 生成新字典
        alist.append(wri)
        k = input('是否继续添加y/n:')
        if k == 'y':
            make = True
        elif k == 'n':
            make = False
            d()


# 展示学生信息
def show():
    f = data()   # 获取文件内容
    # 判断文件是否为空
    if f != []:    # 不为空按正常流程继续进行
        print(" "*6, "-"*40)
        # 打印表头
        print(" "*12, '序号', " "*2, '姓名', " "*2, '年龄', " "*2, '学号')
        print(" "*6, "-"*40)
        # 把文件内容从字符串转化为字典并放在列表里
        alist = [eval(i) for i in f]
        # 获取alist列表的每一项,并循环 ID = i['ID']    # 取出序号 name = i['name']    # 取出姓名
        for i in alist:
            age = i['age']    # 取出年龄
            stuid = i['stuid']    # 取出学号
            ID = i['ID']
            name = i['name']
            # 打印输入取出的每一项
            print(" "*12, ID, " "*5, name, " "*4, age, " "*4, stuid)
        print(" "*6, "-"*40)
    else:    # 如果为空，返回数据为空
        print('数据为空')
        main()

# 删除学生信息


def delete():
    def d():
        # 序号实现自增减
        for i in range(len(alist)):
            ID = 1 + i
            alist[i]['ID'] = ID
        # 打开并写入文件
        with open('database', 'w') as d:
            for i in alist:
                wri = i
                writed = str(wri)+"\n"
                d.write(writed)
        d.close()
        main()

    f = data()  # 获取文件内容
    show()    # 调取show函数
    alist = [eval(i) for i in f]    # 把列表中的每一项转化为字典
    if alist == []:
        print('数据为空返回主菜单')
        main()
    for i in range(len(alist)):    # 遍历alist列表
        name = input('请输入要删除的名字:')  # 输入要删除学生的姓名
        stuid = int(input('请输入学号:'))    # 输入要删除学生的学号
        # 判断输入的学生姓名和学号是否存在
        if alist[i]['name'] == name and alist[i]['stuid'] == stuid:
            del alist[i]    # 存在删除
            print('删除成功')
            d()
    # 判断是否继续删除
    keys = input('是否继续删除y/n:')
    if keys == 'y':
        delete()
    elif keys == 'n':
        main()


def modfiy():    # 创建修改数据的函数
    def d():
        # 序号实现自增减
        for i in range(len(alist)):
            ID = 1 + i
            alist[i]['ID'] = ID
        # 打开并写入文件
        with open('database', 'w') as d:
            for i in alist:
                wri = i
                writed = str(wri)+"\n"
                d.write(writed)
        d.close()
        main()
    f = data()    # 获取列表元素
    show()    # 展示列表元素
    # print('a')
    alist = [eval(i) for i in f]    # 把文件内容转换为字典并放在列表里边
    # print('a')
    make = True    # 制定循环条件
    while make:    # 进入循环
        name = input('请输入你要修改学生的姓名:')    # 输入要修改学生的姓名
        sid = input('请输入你要修改学生的学号:')   # 输入修改学生的id
        for i in alist:    # 获取alist列表的每一项
            # 判断学生是否在数据内
            if name in i['name'] and sid in str(i['stuid']):
                # 如果存在则输入要修改的选项
                print('''
       ————————————————————————————————————————
       |                                      |
       |         输入修改选项的序号           |
       |               1.姓名                 |
       |               2.年龄                 |
       |               3.学号                 |
       |                                      |
       ————————————————————————————————————————
       ''')
                k = input('请输入')    # 输入修改的选项
                if k == '1':    # 如果输入的是1，修改学生姓名
                    sname = input('请输入修改后的姓名:')    # 输入修改后的姓名
                    i['name'] = sname    # 修改列表
                    print(alist)
                elif k == '2':   # 如果输入2，修改学生年龄
                    age = input('请输入修改后的年龄:')    # 输入修改后的学生年龄
                    i['age'] = age    # 修改列表
                    print(alist)
                elif k == '3':
                    sids = input('请输入修改后的学生学号:')    # 修改后的学号
                    i['stuid'] = sids    # 修改后的列表
                    print(alist)
        # 判断是否继续输入
        keys = input('是否继续修改y/n:')
        if keys == 'y':
            make = True
        elif keys == 'n':
            make = False
    d()


def search():
    f = data()    # 获取列表元素
    alist = [eval(i) for i in f]    # 把文件内容转换为字典并放在列表里边
    if alist == []:
        print('数据为空')
        main()
    make = True
    while make:
        print('''
       ————————————————————————————————————————
       |                                      |
       |              查询方式                |
       |                                      |
       |              1.姓名                  |
       |              2.学号                  |
       |                                      |
       ————————————————————————————————————————
       ''')
        k = input('请输入:')
        # print(k)
        if k == '1':
            name = input('请输入学生姓名:')
            sid = 0
        elif k == '2':
            name = ''
            sid = int(input('请输入学生学号:'))
        print(" "*6, "-"*40)
        # 打印表头
        print(" "*12, '序号', " "*2, '姓名', " "*2, '年龄', " "*2, '学号')
        for i in alist:
            if name == i['name'] or sid == i['stuid']:
                age = i['age']    # 取出年龄
                stuid = i['stuid']    # 取出学号
                ID = i['ID']
                name = i['name']
                # 打印输入取出的每一项
                print(" "*12, ID, " "*5, name, " "*4, age, " "*4, stuid)

        print(" "*6, "-"*40)
        keys = input('是否继续查询y/n:')
        if keys == 'y':
            make = True
        elif keys == 'n':
            make = False
    main()


def main():
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
    key = input('请输入:')
    if key == '1':
        add()
        main()
    elif key == '0':
        import sys
        sys.exit(0)
    elif key == '2':
        show()
        main()
    elif key == '3':
        delete()
    elif key == '4':
        modfiy()
    elif key == '5':
        search()
    else:
        main()


main()
