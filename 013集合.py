# 集合 set 定义使用 {}，{数据， 数据}
# 1. 集合中的数据必须是不可变类型
my_set = {1, 3.14, True, 'hello', (1, 2)}
print(my_set)
# my_set = {[1, 2}  # 代码报错
# 2. 集合是可变类型
my_set.remove(1)
my_set.add(100)
# 3. 集合是无序的（数据的添加顺序和输出顺序是否一致）
# 4. 集合中的数据没有重复数据（去重）
my_list = [1, 1, 2, 3]
my_list = list(set(my_list))
print(my_list)


# 集合、列表、元组 三者之间可以互相转化

