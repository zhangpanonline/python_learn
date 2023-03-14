# 实现了 __enter__ 和 __exit__ 这两个方法的类
class File(object):  # 实现文件的操作
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        
    # 使用 with 语句，会自动进入上文方法
    def __enter__(self):
        print('1. 进入了上文方法')
        self.fp = open(self.filename, self.mode, encoding='utf-8')
        return self.fp
        
    # with 语句执行完成之后，会自动调用
    # with 语句中，即使发生异常，也会进入 __exit__ 中
    # 返回值分两种情况：
    #    1. 如果返回False 或者 None，代表发生异常以后，会继续向外传递
    #    2. 如果返回 True,代表异常不再向外传递
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('3. 离开了上下文方法')
        # exc_type 异常的类型
        # exc_val  异常的信息
        # exc_tb   异常对象
        if exc_type:
            print(exc_type)
            print(exc_val)
            print(exc_tb)
        else:
            print('没有发生异常')
        self.fp.close()
        return True
    
    
if __name__ == '__main__':
    with File('test.txt', 'r') as f:
        print('2. 我是with语句中的代码')
        print(1/0)
        
    