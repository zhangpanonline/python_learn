"""
方法一
try：
    可能发生异常的代码
except  (异常的类型1, 异常的类型2, ...) as 变量名：
    发生异常执行的代码
    print(变量名)
"""

print('其他代码')
num = input('请输入一个数字')

try:
    num = 10 / int(num)
    print('结果：', num)
except (ZeroDivisionError, ValueError) as err:
    print('你输入的有误，请再次输入', err)

print('其他代码')
