import student


class StudentManagerSystem(object):
    def __init__(self):
        self.__stu_dicts = {}
        
    def __save(self):
        f = open('student.txt', 'w', encoding='utf-8')
        for stu in self.__stu_dicts.values():
            f.write(str(stu) + '\n')
        f.close()
        
    def __load_info(self):
        try:
            f = open('student.txt', 'r', encoding='utf-8')
            buf_list = f.readlines()
            for buf in buf_list:
                buf = buf.strip()  # 去除 \n
                info_list = buf.split(',')
                stu = student.Student(*info_list)
                self.__stu_dicts[stu.stu_id] = stu
            f.close()
        except Exception:
            pass
        
    @staticmethod
    def show_menu():
        print('1. 添加学生')
        print('2. 删除学生')
        print('3. 修改学生信息')
        print('4. 查询单个学生信息')
        print('5. 查询所有学生信息')
        print('6. 退出系统')
        
    def __insert_student(self):
        stu_id = input('请输入学生学号：')
        if stu_id in self.__stu_dicts:
            print('学生信息已存在！')
            return
        
        name = input('请输入学生名字：')
        age = input('请输入学生年龄：')
        gender = input('请输入学生性别：')
        stu = student.Student(stu_id, name, age, gender)
        self.__stu_dicts[stu_id] = stu
        
    def __remove_student(self):
        stu_id = input('请输入学号：')
        if stu_id in self.__stu_dicts:
            name = self.__stu_dicts[stu_id].name
            del self.__stu_dicts[stu_id]
            print(f'学生{name}信息已删除！')
        else:
            print('学生信息不存在！')
            
    def __modify_student(self):
        stu_id = input('请输入学号：')
        if stu_id in self.__stu_dicts:
            stu = self.__stu_dicts[stu_id]
            stu.age = input('请输入修改后的年龄：')
            print(f'学生{stu.name}信息已修改！')
        else:
            print('学生信息不存在！')
            
    def __search_student(self):
        stu_id = input('请输入学号：')
        if stu_id in self.__stu_dicts:
            print(self.__stu_dicts[stu_id])
        else:
            print('学生信息不存在！')
        
    def __show_all_info(self):
        for stu in self.__stu_dicts.values():
            print(stu)
        
    def start(self):
        self.__load_info()
        while True:
            self.show_menu()
            opt = input('请输入用来选择的操作编号：')
            if opt == '1':
                print('添加学生')
                self.__insert_student()
            elif opt == '2':
                print('删除学生')
                self.__remove_student()
            elif opt == '3':
                print('修改学生信息')
                self.__modify_student()
            elif opt == '4':
                print('查询单个学生信息')
                self.__search_student()
            elif opt == '5':
                print('查询所有学生信息')
                self.__show_all_info()
            elif opt == '6':
                print('退出系统')
                self.__save()
                break
            else:
                print('输入有误，请再次输入')
                continue
            
            input('......回车键继续操作......')
            