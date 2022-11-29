"""
什么是多态？
    在需要使用父类对象的地方，也可是使用子类对象，得到不同的结果 --- 多态
    比如，在函数中，我需要调用某一个父类对象的方法，那么我们也可以在这个地方调用子类对象的方法
    
实现步骤：
    1. 子类继承父类
    2. 子类重写父类中的同名方法
    3. 定义一个共同的方法，参数为父类对象，在方法中调用子类和父类同名的方法
"""


class Dog(object):
    def __init__(self, name):
        self.name = name
        
    def play(self):
        print(f'小狗{self.name}在快乐的玩耍...')
        
        
class XTQ(Dog):
    def play(self):
        print(f'{self.name}在天上追云彩...')
        
    
def play_width_dog(obj_dog):
    obj_dog.play()
    
    
dog = Dog('大黄')
play_width_dog(dog)

xtq = XTQ('小黑')
play_width_dog(xtq)

