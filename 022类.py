class Dog(object):
    def play(self):
        print(f'self: {id(self)}')
      
        
# 创建对象
dog = Dog()
dog.play()
print(f'{id(dog)}')
