def logger(fn):
    def inner(*args, **kwargs):
        print(f'{fn.__name__} enter')
        fn(*args, **kwargs)
        print(f'{fn.__name__} leave')
    return inner


@logger
def comment():
    print('评论功能')
    
    
@logger
def func(n1, n2, n3):
    print(n1, n2, n3)
    
    
if __name__ == '__main__':
    comment()
    func(10, 11, n3=12)
    