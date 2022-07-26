import os.path


def show_menu():
    print('1. 添加学生')
    print('2. 删除学生')
    print('3. 修改学生信息')
    print('4. 查询单个学生信息')
    print('5. 查询所有学生信息')
    print('6. 退出系统')


stu_list = []


def insert_student():
    name = input("请输入name：")
    for stu in stu_list:
        if stu['name'] == name:
            print("====学生信息 已存在==========")
            return

    age = input("请输入age：")
    gender = input("请输入sex：")
    stu_dict = {'name': name, 'age': int(age), 'gender': gender}
    stu_list.append(stu_dict)
    print("=============学生信息添加成功=============")


def show_all_info():
    if len(stu_list):
        for stu in stu_list:
            print(f'姓名：{stu["name"]}，年龄：{stu["age"]}，性别：{stu["gender"]}')
    else:
        print("=======没有学生信息=========")


def save():
    # 1. 打开文件
    f = open('file/student.txt', 'w')
    f.write(str(stu_list))
    f.close()


def load_file():
    global stu_list
    if os.path.exists('file/student.txt'):
        f = open('file/student.txt', 'r', encoding='utf-8')
        buf = f.read()
        if buf:
            stu_list = eval(buf)
        f.close()


def main():
    load_file()
    while True:
        show_menu()
        opt = input("请输入用来选择的操作编号：")
        if opt == '1':
            insert_student()
        elif opt == '2':
            print('2. 删除学生')
        elif opt == '3':
            print('3. 修改学生信息')
        elif opt == '4':
            print('4. 查询单个学生信息')
        elif opt == '5':
            show_all_info()
        elif opt == '6':
            print('欢迎下次使用本系统......')
            save()
            break
        else:
            print("输入有误，请再次输入")

        input("......回车键继续操作......")


main()
