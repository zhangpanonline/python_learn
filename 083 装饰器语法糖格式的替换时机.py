def outer(fn):
    print('1...')
    
    def inner():
        print('2...')
        fn()
    return inner


# 替换时机是 原函数定义之后，就会进行
@outer
def comment():
    print('3....')


if __name__ == '__main__':
    print('4...')
    comment()
    
    
