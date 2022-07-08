# 定义空列表
# eg:
my_list = []
my_list = list()


# 定义带数据元素的列表
# eg:
my_list = [1, 3.14, True]


# 求列表长度 len()
# eg:
# print(len(my_list))  # 3


# 列表支持下标和切片操作
# 下标操作和字符串中不同的是：列表可以使用下标修改列表中的数据


# 列表的遍历
# eg:
# for i in my_list: 
#     print(i)

# j = 0
# while j < len(my_list):
#     print(my_list[j])
#     j += 1


# 向原列表中添加数据，不会返回新列表
# append() 尾部追加
# insert(下标，数据) 指定下标处添加数据
# extend(可迭代对象) 会将可迭代对象(字符串、列表)中的数据逐个添加到原列表的末尾
# eg:
# my_list.extend('hello')
# print(my_list)  # [1, 3.14, True, 'h', 'e', 'l', 'l', 'o']
# my_list.extend(['1', '2'])
# print(my_list)  # [1, 3.14, True, 'h', 'e', 'l', 'l', 'o', '1', '2']

    
# 列表中数据查询操作
# index() 根据数据值，查找元素所在下标，找到返回元素的下标，没有找到，程序报错
# eg:
# print(my_list.index(3.14))  # 1
# print(my_list.index(3.1)) # ValueError: 3.1 is not in list

# count() 统计出现的次数
# eg:
# print(my_list.count(3.14))  # 1
# print(my_list.count(1))  # 2  这里将True当做正数1处理了

# in / not in 判断是否存在，存在是True，不存在是False，一般和 if 结合使用


# 删除
# 1. 根据元素的数据值删除 remove(数据值)，直接删除原列表中的数据
# eg:
# my_list.remove(4) # ValueError: list.remove(x): x not in list
# print(my_list.remove(1))  # None
# print(my_list)  # [3.14, True]
# 2. 根据下标删除
# 2.1 my_list.pop(index) 删除下标为index的元素，默认删除最后一个元素，返回删除的内容
# 2.2 del 列表[下标]
# # eg:
# del my_list[1]
# print(my_list)  # [1, True]


# 排序
my_list = [1, 5, 3, 7, 9, 6]
# 列表.sort()  默认对原列表从小到达排序
# eg:
# my_list.sort()
# print(my_list)  # [1, 3, 5, 6, 7, 9]
# my_list.sort(reverse=True)  # 从大到小排序
# print(my_list)  # [9, 7, 6, 5, 3, 1]
# sorted(列表, reverse=False) 排序，不会对原列表进行排序，会得到一个新的列表
# print(sorted(my_list))  # [1, 3, 5, 6, 7, 9]


# 逆置
# 返回新列表
#: eg
my_list1 = ['a', 'b', 'c', 'd', 'e']
my_list2 = my_list1[::-1]
# print(my_list1)  # ['a', 'b', 'c', 'd', 'e']
# print(my_list2)  # ['e', 'd', 'c', 'b', 'a']
# 对原列表进行逆置
# eg:
# my_list1.reverse()
# print((my_list1))  # ['e', 'd', 'c', 'b', 'a']


# 元组
# 不同点：列表使用[]定义，元组使用()定义，列表中的数据可以修改，元组中的数据不能修改
# 元组支持下标和切片操作
my_tuple = ('a', 'b', 'c')
# eg：
# print(my_tuple[1])  # b
# print(my_tuple[::-1])  # ('c', 'b', 'a')


# 定义只有一个元素的元组，数据元素后面必须有一个逗号
# print((1), type((1)))  # 1 <class 'int'>
# print((1,), type((1,)))  # (1,) <class 'tuple'>
