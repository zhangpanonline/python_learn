# 1. 导包
import multiprocessing
import time

# 定义全局变量
g_list = ['a']


# 2.1 定义任务函数，添加数据，修改全局变量的值
def add_data():
    for i in range(5):
        g_list.append(i)
        print('添加数据：', i)
        time.sleep(0.1)
    # 数据添加完成
    print('add_data：', g_list)
    
    
# 2.2 定义任务函数，读取全局变量
def read_data():
    print('read_data：', g_list)


if __name__ == '__main__':
    # 3 创建进程对象
    process_add = multiprocessing.Process(target=add_data)
    process_read = multiprocessing.Process(target=read_data)
    
    process_add.start()
    # 进程对象.join()  阻塞等待进程执行完成
    # 1. 谁阻塞等待？ 代码书写在哪个进程，哪个进程阻塞等待
    # 2. 阻塞等待谁执行完成？ 哪个进程对象.join() 就是等待哪个进程执行完成
    process_add.join()  # 1. 主进程阻塞等待; 2. 等待 add 进程执行结束
    process_read.start()
