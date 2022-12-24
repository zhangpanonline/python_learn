import multiprocessing
import time


def sing(singer, name):
    for i in range(5):
        print(f'{singer}：{name}**********************')
        time.sleep(0.1)


def dance(dancer, name):
    for i in range(5):
        print(f'{dancer}：{name}############################')
        time.sleep(0.1)
        
        
if __name__ == '__main__':
    # 进程传参：
    #       args 传参 实参是元祖类型
    #       kwargs 传参 实参是字典
    process_sing = multiprocessing.Process(target=sing, args=('张三', 'sing'))
    process_dance = multiprocessing.Process(target=dance, kwargs={'dancer': '李四', 'name': 'song'})

    process_sing.start()
    process_dance.start()
    
