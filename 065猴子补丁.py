from gevent import monkey
import gevent
import time

# 使用 gevent 中模块替换系统中的模块（例如：替换系统中的 time 模块）
monkey.patch_all()


def sing(singer, song):
    for i in range(5):
        print(f'{singer}正在{song}||||||||||||')
        time.sleep(0.1)
        
        
def dance(dancer, dance):
    for i in range(8):
        print(f'{dancer}正在{dance}------------')
        time.sleep(0.1)


if __name__ == '__main__':
    g1 = gevent.spawn(sing, '张三', '唱歌')
    g2 = gevent.spawn(dance, '李四', '跳舞')
    g1.join()
    g2.join()
    