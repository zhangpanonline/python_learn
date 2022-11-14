"""
__init__
调用时机：在创建对象之后，会立即调用
作用：
    1. 用来给对象添加属性，给对象属性一个初始值（构造函数）
    2. 代码的业务需求，每创建一个对象，都需要执行的代码可以写在 __init__ 中
"""


class Dog(object):
    def __init__(self, name, age):
        print('创建对象会自动调用__init__方法', name)
        self.name = name
        self.age = age


d1 = Dog('大黄', 14)
d2 = Dog('二狗子', 16)


"""
__str__
调用时机：
    1. print(对象)，会自动调用 __str__ 方法，打印输出的结果是 __str__ 方法的返回值
    2. str(对象)  类型转换，将自定义对象转换为字符串的时候，会自动调用
应用：
    1. 打印对象的时候，输出一些属性信息
    2. 需要将对象转换为字符串类型的时候
注意点：
    方法必须返回一个字符串，只有 self 一个参数
"""


class Dog1(object):
    def __str__(self):
        return '我是__str__方法'


print(d1)  # 没有定义 __str__ 方法，print(对象)默认输出对象的引用地址
print(str(d1))  # 没有定义 __str__ 方法，类型转换也是引用地址
print(Dog1())
print(str(Dog1()))


"""
__del__
调用时机：对象在内存中被销毁删除的时候（引用计数为0）
    1. 程序代码运行结束
    2. 使用`del变量`，将这个对象的引用计数变为0，会自动调用 __del__ 方法
引用计数：是python内存管理的一种机制，是指一块内存，有多少个变量在引用
应用场景：对象被删除销毁的时候，要书写的代码可以写在 __del__ 中
"""


class Dog2(object):
    def __del__(self):
        print('__del__ 方法被调用了')
    
    
d3 = Dog2()

print('删除之前')
del d3
print('删除之后')


