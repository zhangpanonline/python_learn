import threading
import time


def fn():
    for i in range(5):
        print(i)
        time.sleep(0.5)
    print('子线程代码结束')
    
    
if __name__ == '__main__':
    # 想让子线程随主线程结束而结束，可以将子线程设置为 daemon
    # 方法一：在创建线程对象的时候设置
    # sub_thread = threading.Thread(target=fn, daemon=True)
    sub_thread = threading.Thread(target=fn)
    # 方法二：创建对象之后进行设置
    sub_thread.daemon = True
    sub_thread.start()
    time.sleep(1)
    print('主线程的代码结束')
        