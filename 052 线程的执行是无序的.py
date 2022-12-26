import threading
import time


def fn():
    time.sleep(1)
    print(threading.current_thread().name)


if __name__ == '__main__':
    # 循环创建多个线程，start 之后，都处于就绪态
    # cpu 调度哪个线程，那个线程就会执行
    for i in range(10):
        sub_thread = threading.Thread(target=fn)
        sub_thread.start()
        