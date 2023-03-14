def make_tag(tag):
    def decorator(fn):
        def inner(*args, **kwargs):
            result = fn(*args, **kwargs)
            return "<" + tag + ">" + result + "</" + tag + ">"
        return inner
    return decorator


# 1. 先进行函数调用，返回的是装饰器
# 2. 对原函数进行装饰
@make_tag('div')  # 装饰器工厂函数  @decorator
@make_tag('p')
def comment(info):
    return info


if __name__ == '__main__':
    print(comment('hello world'))
