def logger(fn):
    def inner(*args, **kwargs):
        print(f'{fn.__name__} enter ...')
        result = fn(*args, **kwargs)
        print(f'{fn.__name__} leave ...')
        return result
    return inner


@logger
def func(info):
    return info


@logger
def my_sum(a, b):
    return a + b


if __name__ == '__main__':
    print(func('hello'))
    print(my_sum(10, 20))
    