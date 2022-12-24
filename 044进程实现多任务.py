# 1. 导包
import multiprocessing
import time


def sing():
    for i in range(5):  # 代码只运行5次，时间太短，在一个时间片内就执行结束
        print('sing**********************')
        # 手动让进程失去 CPU 资源
        time.sleep(0.1)  # 让进程休眠 0.1 秒，进入阻塞态，失去 CPU


def dance():
    for i in range(5):
        print('dance############################')
        time.sleep(0.1)
        
        
if __name__ == '__main__':
    # sing()
    # dance()
    # 2. 创建进程对象 multiprocessing.Process(任务函数名)
    # target 指定进程执行的任务，既函数名字，不能加括号
    process_sing = multiprocessing.Process(target=sing)
    process_dance = multiprocessing.Process(target=dance)
    # 3. 启动进程对象 进程对象.start()
    process_sing.start()
    process_dance.start()
    