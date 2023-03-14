def make_p(fn):
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        return "<p>" + result + "</p>"
    return inner


def make_div(fn):
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        return "<div>" + result + "</div>"
    return inner


# 多个装饰器装饰同一个函数，装饰顺序是就近原则
@make_div
@make_p
def comment(info):
    return info


if __name__ == '__main__':
    print(comment('hello world'))
    