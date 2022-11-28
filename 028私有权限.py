"""
私有属性：
    定义：在方法和属性前加上两个下划线，就变为私有
        1. 不能在类外部通过对象直接访问和使用，只能在类内部访问和使用
        2. 不能被子类继承
    目的：保证数据的相对安全
    想要访问和使用私有属性：定义一个公有的方法，通过这个方法使用
私有方法：同私有属性
"""


class People(object):
    def __init__(self):
        # python中的私有本质是修改属性的名字，在创建对象的时候，会自动的修改属性名
        # 在属性名的前边加上 _类名前缀
        self.__ICBC_money = 0
        
    # 定义公有的方法，提供接口，修改私有属性
    def get_money(self):
        return self.__ICBC_money
    
    def set_money(self, money):
        self.__ICBC_money += money
        
    
xw = People()
# print(xw.__ICBC_money)  # AttributeError: 'People' object has no attribute '__ICBC_money'
xw.__ICBC_money = 1000  # ！！！ 这样写不是修改私有属性，而是重新添加一个公有属性
# print(xw.__ICBC_money)  # 1000

# 查看对象具有的属性信息：实例对象.__dict__
print(xw.__dict__)  # {'_People__ICBC_money': 0, '__ICBC_money': 1000}

print(xw.get_money())
xw.set_money(1000)
print(xw.get_money())
xw.set_money(-500)
print(xw.get_money())
