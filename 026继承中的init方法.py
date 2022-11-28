# 1. 定义Dog类
class Dog(object):
    def __init__(self, name):
        # 添加属性
        self.age = 0
        self.name = name
        
    def __str__(self):
        return f'年龄为{self.age}，名字为{self.name}'
        
        
# 2. 定义XTQ类继承DOG类
class XTQ(Dog):
    # !!! 子类重写了父类的 __init__ 方法，所以不会再调用父类的 __init__ 方法
    # def __init__(self, name, color):
    
    # !!! 下面才是正确的写法：如果子类重写了父类的 init 方法，在子类中中需要调用父类的 init 放法，给对象添加从父类继承的属性
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    
    def __str__(self):
        return f'年龄为{self.age}，名字为{self.name}，毛色为{self.color}'
    

xtq = XTQ('小黑', '黑色')
print(xtq)
