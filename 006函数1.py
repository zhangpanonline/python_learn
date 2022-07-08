# def 函数名():
#       函数代码(函数体)
c = 10


def func(a=1, b=2):
    """
    这里是函数说明文档
    :return: 
    """
    global c
    c = 100
    return a, b, c


# print(func())

# 可以使用 id() 查看变量的引用
# print(id(c))  # 3163241409104


# 在形参前边加上一个*，该形参变为不定长元组形参，可以接收所有的位置实参
# 在形参前边加上两个**，该形参变为不定长字典形参，可以接收所有的关键字实参，类型是字典
def func(*args, **kwargs):
    print(args)
    print(kwargs)