import threading
import time

g_list = []


def add_data():
    for i in range(5):
        g_list.append(i)
        print('添加数据：', i)
        time.sleep(0.1)
    print('add_data', g_list)
    
    
def read():
    print('read：', g_list)
    
    
if __name__ == '__main__':
    thread_add = threading.Thread(target=add_data)
    thread_read = threading.Thread(target=read)
    
    thread_add.start()
    thread_add.join()
    thread_read.start()
    