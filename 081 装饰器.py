def login_check(fn):  # 1
    def inner():  # 4
        print('登录验证...')  # 8
        fn()  # 9
    return inner  # 5


def comment():  # 2
    print('进行评论...')  # 10


comment = login_check(comment)  # 3

if __name__ == '__main__':  # 6
    comment()  # 7
    
    
