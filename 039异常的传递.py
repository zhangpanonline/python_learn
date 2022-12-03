"""
异常传递：当一行代码发生异常后，会向外层将这个异常进行传递，直到被捕获或者程序报错为止
经常遇到的情况：
    1. try 嵌套
"""
print('pass')
num = input('请输入数字')
try:
    try:
        num = 10 / int(num)
    except ZeroDivisionError:
        print('发生异常')
    finally:
        print('内层try执行完成')
    print(f'计算的结果：{num}')
except Exception as err:
    print(err)
print('pass')
