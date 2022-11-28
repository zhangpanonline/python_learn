# 如果一个类有两个及以上的父类，就把这种继承关系称为多继承

class Dog(object):
    def bark(self):
        print('汪汪叫...')
        
    def eat(self):
        print('啃骨头...')
        
        
class God(object):
    def play(self):
        print('在云中飘一会...')
        
    def eat(self):
        print('吃蟠桃仙丹...')
        
        
# 多继承
class XTQ(God, Dog):

    def eat(self):
        # !!! 调用指定父类中的方法
        # 方法一   类名.方法名(self, 参数)
        #     Dog.eat(self)
        # 方法二 super(类A，self).方法名(参数) 类A的父类(继承顺序链中的下一个类)中的方法
        # super(XTQ, self).eat()  # God 类中的方法
        # super(God, self).eat()  # 调用Dog类中的方法
        # super(Dog, self).eat()  # 调用的object类中的方法，报错
         pass


xtq = XTQ()
xtq.bark()
xtq.play()
# ！！！ 两个父类都存在 eat 方法，子类对象调用的是第一个父类中的方法
xtq.eat()

# 类名.__mro__ 可以查看当前类的继承顺序性，也叫做方法的调用顺序
print(XTQ.__mro__)
