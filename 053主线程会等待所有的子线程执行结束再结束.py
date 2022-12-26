import threading
import time


def fn():
    for i in range(5):
        print(i)
        time.sleep(0.5)
    print('子线程代码结束')
    
    
if __name__ == '__main__':
    sub_thread = threading.Thread(target=fn)
    sub_thread.start()
    time.sleep(1)
    print('主线程的代码结束')
        