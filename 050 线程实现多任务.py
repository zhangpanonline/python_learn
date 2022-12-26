# 1. 导入模块
import threading
import time


def sing():
    print('sing：', threading.current_thread().name)
    for i in range(5):
        print('sing=========')
        time.sleep(0.1)
        
        
def dance():
    print('dance：', threading.current_thread().name)
    for i in range(5):
        print('dance************')
        time.sleep(0.1)


if __name__ == '__main__':
    print('main：', threading.current_thread().name)
    # 2. 创建线程对象
    thread_sing = threading.Thread(target=sing)
    thread_dance = threading.Thread(target=dance)

    # 3. 启动线程
    thread_sing.start()
    thread_dance.start()
