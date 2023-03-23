# 在函数中书写了 yield 关键字，这个函数就是生成器
def func():
    for i in range(5):
        print(f'第 {i + 1} 次循环开始')
        # yield 关键字作用
        #   1. 类似 return，会将后面跟的内容进行返回；
        #   2. 函数代码遇到 yield，函数会暂停执行，等待下一次 next() 再继续执行
        yield 100 + i
        print(f'第 {i + 1} 次循环结束')
        
        
if __name__ == '__main__':
    # 1. 创建一个生成器对象
    my_gen = func()
    print(my_gen, type(my_gen))
    # res = next(my_gen)
    # print(res)
    # res = next(my_gen)
    # print(res)
    for v in my_gen:
        print(v)
    
        