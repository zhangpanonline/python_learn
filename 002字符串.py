# 字符串可以用单、双、三引号包裹
# print('hello', "hello", '''hello''')


s = "hello"


# 字符串可以和数字相乘
# eg:
# print(s * 3)


# 通过下标获取字符串字符 -1 表示最后一个字符
# eg:
# print(s[-2])


# len()
# eg:
# print(s[len(s) - 1])


# 切片语法： 新变量 = 原变量[start:end:step]，start：起始下标 end：结束下标(不包括，默认len()) step：步长，默认1
# start 和 end 都不写，但是冒号需要写
# eg:
# print(s[1:])  # ello
# print(s[:2])  # e
# print(s[::2])  # hlo
# print(s[:])  # hello
# print(s[-4:-1])  # ell
# print(s[3: 1])  # None
# print(s[3:1:-1])  # ll
# print(s[::-1])  # 字符串的反转/逆置  olleh


# find() 在字符串中查找是否存在某个字符串
# index = s.find(str, start, end)
# str: 要在 s 中查找的内容
# start：开始位置，默认0
# end：结束位置，默认len()
# 返回值：下标，没有返回-1
# eg:
# print(s.find('l', 3))  # 3


# rfind() 同 find() 只是从目标字符串右边开始查找


# index() 在字符串中查找是否存在某个字符串
# index = s.index(str, start, end) 如果找到返回下标，没找到则会[!!!报错]
# eg:
# print(s.index('h'))  # 0
# print(s.index('a'))  # ValueError: substring not found


# rindex() 同 index() 只是从目标字符串右边开始查找


# count(str, start, end) 统计出现的次数
# eg:
# print(s.count('l'))  # 2


# result = s.replace(old_str, new_str, count)
# 将 s 中的 old_str 替换成 new_str，总共替换 count 次，默认全部替换，返回一个新字符串，不会改变原字符串


# split() & rsplit()
# arr = s.split(str, count)  将 s 字符串按照 str 进行切割
# str: 按照什么内容切割字符串，默认空白字符(空格、tab键\t、换行\n)
# count：切割几次，默认全部切割
# 返回值：列表[]
# eg:
# print(s.split('l', 1))  # ['he', 'lo']
# print(s.rsplit('l', 1))  # ['hel', 'o']


# res = my_str.join(可迭代对象)
# 可迭代对象：str、列表(需要列表中每一项为字符串类型)
# 将my_str 这个字符串添加到可迭代对象的两个元素之间
# 返回值：一个新的字符串
# eg:
# print('_'.join(s))  # h_e_l_l_o
# print('_*_'.join(s))  # h_*_e_*_l_*_l_*_o
# print("_".join(['a', 'b']))  # a_b


# res = my_str.capitalize()   # 字符串首个字符大写
# res = my_str.upper()  # 字符串所有字符变大写
# res = my_str.lower()  # 字符串所有字符变小写
# res = my_str.title()  # 字符串每个单词首字母大写
# .islower()  .startswith()  .center(length)  .ljust(length)  .rjust(length)
# .lstrip()  去除左边空格
# .rstrip()
# .strip()


# my_str.partition(str)
print(s.partition('l'))  # ('he', 'l', 'lo')
