import threading
import time


def sing(singer, name):
    print('sing：', threading.current_thread().name)
    for i in range(5):
        print(f'{singer}：{name}=========')
        time.sleep(0.1)
        
        
def dance(dancer, name):
    print('dance：', threading.current_thread().name)
    for i in range(5):
        print(f'{dancer}：{name}************')
        time.sleep(0.1)


if __name__ == '__main__':
    print('main：', threading.current_thread().name)
    thread_sing = threading.Thread(target=sing, args=('张三', 'sing'))
    thread_dance = threading.Thread(target=dance, kwargs={'dancer': '李四', 'name': 'dance'})

    thread_sing.start()
    thread_dance.start()
