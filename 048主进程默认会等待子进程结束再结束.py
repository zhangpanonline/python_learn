import multiprocessing
import time

def func():
    for i in range(5):
        print(i)
        time.sleep(0.5)
    print('子进程的代码结束')
    
    
if __name__ == '__main__':
    sub_process = multiprocessing.Process(target=func)
    sub_process.start()
    time.sleep(1)  # 1 秒结束
    print('主进程代码结束，理论上程序应该结束')
    