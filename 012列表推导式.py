# 列表推导式，为了快速的生成一个列表
# 1. 变量 = [生成数据的规则 for 临时变量 in xxx]
# 每循环一次，就会创建一个数据

my_list = [i for i in range(5)]
# print(my_list)  # [0, 1, 2, 3, 4]

myList1 = ['hello' for i in range(5)]
# print(myList1)  # ['hello', 'hello', 'hello', 'hello', 'hello']

my_list2 = [f'num:{i}' for i in range(5)]
# print(my_list2)  # ['num:0', 'num:1', 'num:2', 'num:3', 'num:4']


# 2. 变量 = [生成数据的规则 for 临时变量 in xxx if xxx]
# 每循环一次，并且if条件为True，生成一个数据

my_list3 = [i for i in range(5) if i % 2 == 0]
# print(my_list3)  # [0, 2, 4]


# 3. 变量 = [生成数据的规则 for 临时变量 in xxx for j in xxx]
# 第二个for循环每循环一次，生成一个数据
my_list4 = [(i, j) for i in range(3) for j in range(3)]
# print(my_list4)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]


# 补充：字典推导
# 变量 = {生成字典的规则 for 临时变量 in xxx}
my_dict = {f"name{i}": i for i in range(3)}
# print(my_dict)  # {'name0': 0, 'name1': 1, 'name2': 2}

my_dict = {f"name{i}": j for i in range(3) for j in range(3)}
# print(my_dict)  # {'name0': 2, 'name1': 2, 'name2': 2}

my_dict = {f"name{i}{j}": j for i in range(3) for j in range(3)}
print(my_dict)  # {'name00': 0, 'name01': 1, 'name02': 2, 'name10': 0, 'name11': 1, 'name12': 2, 'name20': 0, 'name21': 1, 'name22': 2}

