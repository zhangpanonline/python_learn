# 1. 导入 gevent
import gevent


def sing(singer, song):
    for i in range(5):
        print(f'{singer}正在{song}||||||||||||')
        # gevent 遇到 I/O 耗时阻塞操作，会切换协程
        gevent.sleep(0.1)  # 切换协程
        
        
def dance(dancer, dance):
    for i in range(8):
        print(f'{dancer}正在{dance}------------')
        gevent.sleep(0.1)


if __name__ == '__main__':
    # 2. 创建协程对象
    g1 = gevent.spawn(sing, '张三', '唱歌')
    g2 = gevent.spawn(dance, '李四', '跳舞')
    # 3. 阻塞等待协程对象 join，gevent 遇到 I/O 耗时阻塞操作时才会切换
    g1.join()
    g2.join()
    