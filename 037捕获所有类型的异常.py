"""
try:
    pass
except: # 缺点：不能获取异常的描述信息
    发生异常执行的代码
    
=============================

try:
    pass
except Exception as err: # err异常的描述信息
    发生异常执行的代码
    print(err)
    
=============================

Exception 是常见异常的父类
"""

print('其他代码')
num = input('请输入一个数字')

try:
    num = 10 / int(num)
    print('结果：', num)
except Exception as err:
    print('你输入的有误，请再次输入', err)

print('其他代码')
