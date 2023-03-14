class Dog(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    # @property 装饰器，装饰的方法是 获取属性的方法
    # 还会创建一个新的装饰器，@age.setter 设置属性使用的
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        self.__age = new_age
    
        
if __name__ == '__main__':
    dog = Dog('大黄', 2)
    print(dog.age)
    dog.age = 'abc'
    print(dog.age)
    