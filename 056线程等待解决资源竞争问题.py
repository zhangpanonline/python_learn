import threading
import time

g_num = 0


def task():
    # 修改全局变量的值，需要使用 global 声明
    global g_num
    for i in range(10000000):
        g_num += 1
    print(threading.current_thread().name, g_num)


if __name__ == '__main__':
    thread_1 = threading.Thread(target=task)
    thread_2 = threading.Thread(target=task)

    thread_1.start()
    # 解决方案：让线程1先执行，执行结束后再执行线程2
    thread_1.join()
    thread_2.start()

