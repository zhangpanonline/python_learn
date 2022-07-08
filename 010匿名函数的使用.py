def my_calc(a, b, func):
    """
    进行四则运算
    :param a: 第一个数据
    :param b: 第二个数据
    :param func: 函数，要进行的运算
    :return: 运算的结果
    """
    num = func(a, b)
    print(num)


def add(a, b): return a + b


my_calc(10, 20, add)
my_calc(10, 20, lambda a, b: a - b)
my_calc(10, 20, lambda a, b: a * b)
my_calc(10, 20, lambda a, b: a / b)
my_calc(10, 20, lambda a, b: a + b ** 2)

