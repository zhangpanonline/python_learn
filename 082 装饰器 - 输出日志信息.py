def logger(fn):
    def inner():
        print(f'{fn.__name__} enter')
        fn()
        print(f'{fn.__name__} leave')
    return inner


@logger
def comment():
    print('评论功能')
    
    
if __name__ == '__main__':
    comment()
