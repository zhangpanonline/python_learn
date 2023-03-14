# 定义类装饰器


# 1. 定义类，书写 init 方法，等价外层函数
class LoginCheck(object):
    def __init__(self, fn):
        self.__fn = fn
    
    # 2. 书写 __call__ 方法，等价于内层函数
    def __call__(self, *args, **kwargs):
        # 3. 书写添加的新功能
        print('请先登录...')
        # 4. 调用原函数
        res = self.__fn(*args, **kwargs)
        return res 


@LoginCheck  # comment = LoginCheck(comment); comment() 会自动调用 __call__ 方法
def comment(info):
    print(info)
    
    
if __name__ == '__main__':
    comment('hello')  # 调用 __call__ 方法
    