class Dog(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
        
    # 通过类属性的方式，给对象添加 property 属性
    name = property(get_name, set_name)
    
        
if __name__ == '__main__':
    dog = Dog('大黄', 2)
    print(dog.name)
    dog.name = 'abc'
    print(dog.name)
    