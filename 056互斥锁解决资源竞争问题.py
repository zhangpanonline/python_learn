import threading
import time

# 1. 创建互斥锁
mutex = threading.Lock()

g_num = 0

# 这种加锁，保证加1操作执行完整
def task1():
    # 修改全局变量的值，需要使用 global 声明
    global g_num
    for i in range(10000000):
        # 2. 上锁，请求锁
        mutex.acquire()
        g_num += 1
        # 3. 解锁
        mutex.release()
        
    print(threading.current_thread().name, g_num)


# 这种加锁，保证10000000次的加1操作执行完成
def task2():
    # 修改全局变量的值，需要使用 global 声明
    global g_num
    # 2. 上锁，请求锁
    mutex.acquire()
    for i in range(10000000):
        g_num += 1

    # 3. 解锁
    mutex.release()
    print(threading.current_thread().name, g_num)


if __name__ == '__main__':
    thread_1 = threading.Thread(target=task2)
    thread_2 = threading.Thread(target=task2)

    thread_1.start()
    thread_2.start()

