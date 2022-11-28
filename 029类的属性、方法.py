"""
实例方法：类中默认定义的方法，就是实例方法，第一个参数为 self，表示实例对象
类方法：使用 @classmethod 装饰的方法，称为类方法，第一个参数是 cls ，代表的是类对象自己

什么情况定义为实例方法，什么情况定义为类方法：
    1. 如果在方法中使用了实例属性，那么该方法必须定义为实例方法
    2. 不需要使用实例属性，但是需要使用类属性，可以将这方法定义为类方法
"""


class Dog(object):
    class_name = 'dog'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def play(self):
        print(f'小狗{self.name}在快乐的玩耍...')
        
    def get_class_name1(self):  # 是实例方法，因为没有使用实例属性，所以可以定义为类方法
        return self.class_name
    
    @classmethod  # 定义了一个类方法
    def get_class_name2(cls):
        return cls.class_name
    
    
dog = Dog('小黑', 18)
dog.play()
print(dog.get_class_name1())
print(dog.get_class_name2())
