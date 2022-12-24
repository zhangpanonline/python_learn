import multiprocessing
import time

def func():
    for i in range(5):
        print(i)
        time.sleep(0.5)
    print('子进程的代码结束')
    
    
if __name__ == '__main__':
    sub_process = multiprocessing.Process(target=func)
    
    # 方案二：将子进程设置为 daemon 进程
    sub_process.daemon = True  # 这个子进程会随着主进程的结束而结束
    
    sub_process.start()
    time.sleep(1)  # 1 秒结束
    print('主进程代码结束，理论上程序应该结束')
    
    # 方案一：进程对象.terminate() 终止进程的执行
    # sub_process.terminate()
    

    