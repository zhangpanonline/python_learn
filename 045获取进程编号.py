import multiprocessing
import time
import os
# os.getpid()  获取当前进程id
# os.getppid()  获取当前进程的父id
# os.kill(进程id, 9)  杀死指定进程


def sing():
    print('>>>>>>>>>>>>>>>>>>>>', multiprocessing.current_process().name, os.getpid(), os.getppid())
    for i in range(5): 
        print('sing**********************')
        time.sleep(0.1) 


def dance():
    print('>>>>>>>>>>>>>>>>>>>>', multiprocessing.current_process().name, os.getpid(), os.getppid())
    for i in range(5):
        print('dance############################')
        time.sleep(0.1)
        # os.kill(os.getpid(), 9)
        os.kill(multiprocessing.current_process().pid, 9)


if __name__ == '__main__':
    # 获取当前的进程对象
    print('>>>>>>>>>>>>>>>>>>>>', multiprocessing.current_process().name, os.getpid(), os.getppid())

    process_sing = multiprocessing.Process(target=sing, name='sing')
    process_dance = multiprocessing.Process(target=dance)

    process_sing.start()
    process_dance.start()
