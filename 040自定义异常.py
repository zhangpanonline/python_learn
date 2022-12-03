"""
程序代码为什么会报错？
    因为不符合语法，python 的作者在代码中使用了 if 判断如果除数为 0，
    就会在代码中抛出错误

抛出异常：
    raise 异常对象  # 当程序代码遇到 raise 的时候，程序就报错了

异常对象 = 异常类(参数)

抛出自定义异常：
    1. 自定义异常类，继承 Exception 或者 BaseException
    2. 选择书写，定义 __init__ 方法，定义 __str__ 方法
    3. 在合适的时机抛出异常对象即可
"""


# 1. 定义异常类，密码长度不足的异常
class PasswordLengthError(Exception):
    pass


def get_password():
    password = input('请输入密码：')
    if len(password) >= 6:
        print('密码长度合格')
    else:
        # 抛出异常
        raise PasswordLengthError('密码长度不足6位')
    
    
try:
    get_password()
except Exception as err:
    print(err)
