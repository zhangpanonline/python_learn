# 声明使用外部的变量 nonlocal
def outer(num):
    a = 1
    
    def inner(num1):
        nonlocal a
        a = 2
        print(num1 + num)
    return inner


if __name__ == '__main__':
    fn = outer(100)
    fn(10)
    fn(20)
    