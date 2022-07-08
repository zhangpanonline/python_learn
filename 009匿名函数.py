# 1.午餐无返回值
def func1():
    print("hello")
    
    
func1()

(lambda:
 print('hello lambda'))()


f1 = lambda: print('hello lambda')
f1()


# 2.无参有返回值
def func2():
    return 1 + 2


print(func2())

f2 = lambda: 1 + 2
print(f2())


# 3.有参无返回值
def func3(name):
    print(name)
    
    
func3('hangman')

f3 = lambda name: print(name)


f3('hello')


# 4. 有参数有返回值
def func4(*args):
    return args


print(func4(1, 2, 3))

f4 = lambda *args: args


print(f4(1, 2, 3))
