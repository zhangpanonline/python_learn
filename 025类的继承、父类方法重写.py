class Animal(object):
    def fn(self):
        print('父类方法')
        
    def fn1(self, msg):
        print(msg)
    def fn2(self, msg):
        print(msg)
    def fn3(self, msg):
        print(msg)
        
        
class Dog(Animal):
    def f1(self):
        # 父类名.方法名(self, 其他参数)
        Animal.fn1(self, '第一种调用父类方法')
    def f2(self):
        # super(类A, self).方法名(参数)
        super(Dog, self).fn2('第二种调用父类方法')
    def f3(self):
        # super().方法名(参数) <==> super(当前类, self).方法名()
        super().fn3('第三种调用父类方法')


dog = Dog()
dog.fn()
dog.f1()
dog.f2()
dog.f3()
