"""
使用 @staticmethod 装饰的方法，称为静态方法，对参数没有特殊要求，可有可无
使用条件：
    不需要使用实例属性，同时也不需要使用类属性，此时可以定义为静态方法
"""


class Dog(object):
    
    @staticmethod
    def show_info():
        print('这是一个静态方法')
        

dog = Dog()
# 对象.方法名
dog.show_info()
# 类名.方法名
Dog.show_info()
