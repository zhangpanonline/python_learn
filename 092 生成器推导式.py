# 列表推导式，快速的生成一组数据，一次性将数据全部生成的
# 变量 = [生成数据的规则 for i in xx]  每循环一次，会向列表中根据生成数据的规则添加数据
my_list1 = [i for i in range(5)]
my_list2 = ['hello' + str(i) for i in range(5)]
print(my_list1)
print(my_list2)
print('===============')

# 生成器推导式的语法和列表推导式非常像，只是将 [] 变为 ()，
# 差异：生成器存储的生成数据的规则，使用一个数据就生成一个数据，
# 好处：是节省内存
my_gen = (i for i in range(2))
print(my_gen)
# 从生成器中获取数据，next(生成器)
print(next(my_gen))
print(next(my_gen))
# 当生成数据的规则不满足之后会发生 StopIteration 异常
# print(next(my_gen))
print('===============')
# 获取生成器中的数据，比较好用的方法是 for 循环，因为 python 在 for循环内部 已经封装好了 StopIteration 的异常处理
for i in ('hello' for i in range(2)):
    print(i)
    

