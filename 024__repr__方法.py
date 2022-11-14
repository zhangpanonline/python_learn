my_list = ['hello', 'python', 'cpp']


class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f'{self.name}, {self.age}'
    
    def __repr__(self):
        # repr 方法和 str 方法类似，也是必须返回一个字符串
        return f'{self.name}' 
    
    
my_list1 = [Dog('d1', 1), Dog('d2', 2), Dog('d3', 3)]
print(my_list)
print(my_list1)