def login_check(fn):
    def inner():
        print('登录验证...')
        fn()
    return inner


@login_check
def comment():
    print('进行评论...')


if __name__ == '__main__':
    comment()  # 7
    
    
