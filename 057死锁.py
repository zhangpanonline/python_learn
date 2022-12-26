import threading
g_list = [1, 2, 3, 4, 5]
mutex = threading.Lock()


def func(index):
    mutex.acquire()
    if index >= len(g_list):
        print(threading.current_thread().name, '下标越界')
        # 没有解锁，直接返回，剩余的线程都在这里等待，死锁
        # mutex.release()  # 解决办法：在这里释放锁，避免死锁
        return
    print(threading.current_thread().name, g_list[index])
    mutex.release()
    
    
if __name__ == '__main__':
    for i in range(10):
        sub_thread = threading.Thread(target=func, args=(i,))
        sub_thread.start()




