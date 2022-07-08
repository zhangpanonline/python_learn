# 字典 dict 使用 {} 定义

my_dict = {'a': 1}
# eg:
# print(my_dict['a'])  # 1
# print(my_dict.get('a'))  # 1

# eg:
# print(my_dict['b'])  # KeyError: 'b'
# print(my_dict.get('b'))  # None
# print(my_dict.get('b', '默认值'))  # 默认值

# 获取字典长度
# print(len(my_dict))  # 1

# 字典中添加、修改数据
# 添加数据 eg:
my_dict['b'] = 18
# print(my_dict.get('b'))  # 18
# 修改数据 eg:
my_dict['b'] = 19
# print((my_dict.get('b')))  # 19

# !!! 字典中的 key 值，1 和 1.0 是同一个key

# 删除字典
# eg:
del my_dict['a']
# print(my_dict)  # {'b': 19}
result = my_dict.pop('b')
# print(result, my_dict)  # 19 {}

# 清空字典
my_dict = {'a': 'a', 'b': 'b'}
my_dict.clear()
# print(my_dict)  # {}

# 删除字典，不能再使用这个字典
my_dict = {'a': 'a', 'b': 'b'}
del my_dict
# print(my_dict)  # NameError: name 'my_dict' is not defined

# 字典的遍历
my_dict = {'name': 'hangman', 'age': 18, 'sex': 'man'}

# for 循环体直接遍历字典，遍历的是字典的key值
# for key in my_dict:
#    # print(key, my_dict[key])
# name hangman
# age 18
# sex man

# 字典.keys() 获取字典中所有的key值，得到的类型是 dict_keys，该类型具有的特点是
# 1、可以使用list() 进行类型转换
# 2、可以使用for循环进行遍历
# result = my_dict.keys()
# print(result, type(result))  # dict_keys(['name', 'age', 'sex']) <class 'dict_keys'>

# 同字典.keys()，也有 字典.values() 方法

# 字典.items() 获取所有的键值对，类型是 dict_items
# eg:
# result = my_dict.items()
# print(result, type(result))  # dict_items([('name', 'hangman'), ('age', 18), ('sex', 'man')]) <class 'dict_items'>
# for item in my_dict.items():
#    print(item[0], item[1])
# name hangman
# age 18
# sex man

# 拆包
# eg:
# for k, v in my_dict.items():
#    print(k, v)
# name hangman
# age 18
# sex man
