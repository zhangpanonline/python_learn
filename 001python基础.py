import keyword  # 导包，keyword 是系统中已经定好的关键字
import random

a = 1_000  # 十进制整数
print('十进制整数===>', a)
b = 0xf_f  # 十六进制整数
print('十六进制整数===>', b)

c = 1.23e-10  # 科学计数法表示的浮点数
print('科学计数法表示的浮点数===>', c)

d = r'\\\t\\'  # r''表示''内部的字符串默认不转义
print("r''表示''内部的字符串默认不转义===>", d)

e = '''
line1
line2
line3
'''  # Python允许用'''...'''的格式表示多行内容
print("Python允许用'''...'''的格式表示多行内容===>", e)

f = None  # 空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值
print("None 值===>", f)

PI = 3.1415926  # 在Python中，通常用全部大写的变量名表示常量
print('在Python中，通常用全部大写的变量名表示常量===>', PI)

print('使用type()函数查看变量的类型===>', type(True))

print("系统中的关键字===>", keyword.kwlist)

# 格式化输出，格式化占位符, %s 字符串 %d int %f float
# %.nf 保留n位小数
name = "hangman"
age = 18
height = 18.0
print("格式化输出===>", "我的名字是%s，年龄是%d，身高是%.2fcm" % (name, age, height))

print("格式化输出%===>", "及格人数占比%d%%" % 50)

# python3.6 开始支持 f-string，占位符统一使用{} 占位
print("python3.6开始支持f-string ===>", f"我的名字是{name}，年龄是{age}，身高是{height}cm")

print("print end参数 ===>", 'hello', end="_*_")
print("world")

name = input("请输入用户名：")
print(name)

# 类型转换
# int(x [,base]) float(x) str(x)
# eval() 还原原来的数据类型，去掉字符串的引号
# num = 99
# print(eval('num'), eval('100'), type(eval('100')), eval('3.14'), type(eval('3.14')))

# 逻辑运算符  and or not

print(random.randint(1, 3), random.random(), random.randrange(1, 100, 1))

# 三目运算 变量 = 表达式1 if 判断条件 else 表达式2

# range(n) 会生成 [0, n) 的数据列
# for i in range(5):
#     print(i)

