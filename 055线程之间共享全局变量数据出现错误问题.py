import threading
import time

g_num = 0


def task():
    # 修改全局变量的值，需要使用 global 声明
    global g_num
    for i in range(1000000):
        g_num += 1
    print(threading.current_thread().name, g_num)
        

if __name__ == '__main__':
    thread_1 = threading.Thread(target=task)
    thread_2 = threading.Thread(target=task)
    
    thread_1.start()
    thread_2.start()
    
"""
注意：
    += 1的操作分为三步执行（1、从全局读取g_num的值；2、对g_num 进行 +1 操作；3、将加1后的结果赋给 g_num），
    由于线程的执行是随机的，可能在任何的一步执行结束之后，失去 CPU，会保存当前执行步骤等再次获得CPU之后，继续执行。
    
过程分析：
    1. 线程1 获得 CPU 资源，从全局变量读取到的数据值1000
    2. 此时，线程1失去 CPU，线程会记录当前执行的步骤
    3. 线程2获得 CPU 资源，从全局变量中取值1000
    4. 线程2进行加1操作
    5. 线程2将1001 的值赋值给 g_num
    ......
    6. 线程2执行了1000次之后，失去CPU资源，g_num 的值为 2000
    7. 线程1 获得CPU，从上次失去CPU的地方继续执行（1000）
    8. 线程1 加 1= 1001
    9. 线程1 将1001赋值给g_num
"""
    
    