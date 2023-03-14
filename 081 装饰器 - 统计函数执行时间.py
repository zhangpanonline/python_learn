import time


def calc_time(fn):
    def inner():
        start = time.time()  # 记录当前时间的秒数
        fn()
        end = time.time()
        print(f'函数执行耗时：{end - start}, {end}')
    return inner


@calc_time
def func():
    for i in range(10):
        print(i)
        time.sleep(0.3)
    print('函数执行结束')


if __name__ == '__main__':
    func()
    
    
