"""
方法一
try：
    可能发生异常的代码
except  (异常的类型1, 异常的类型2, ...)：
    发生异常执行的代码
    
方法二
try:
    可能发生异常的代码
except 异常类型1：
    发生异常1执行的代码
except 异常类型2：
    发生异常2执行的代码
......
"""

print('其他代码')
num = input('请输入一个数字')

# try:
#     num = 10 / int(num)
#     print('结果：', num)
# except (ZeroDivisionError, ValueError):
#     print('你输入的有误，请再次输入')

try:
    num = 10 / int(num)
    print('结果：', num)
except ZeroDivisionError:
    print('输入有误，请再次输入')
except ValueError:
    print('输入有误，请输入数字')

print('其他代码')
