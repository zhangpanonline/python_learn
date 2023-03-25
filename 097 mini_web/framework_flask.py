import time

# flask 中路由的处理，使用装饰器的方式实现，当定义一个试图函数之后，就将这个视图函数的路由进行添加
route_list = []


def my_route(filename):
    def decorator(fn):
        def inner(*args, **kwargs):
            return fn(*args, **kwargs)
        # 添加路由
        route_list.append((filename, inner))
        return inner
    return decorator


@my_route('/index.html')
def index():
    """
    处理首页
    """
    # 1. 读取模板中的 HTML 页面
    with open('template/index.html', 'r', encoding='utf-8') as f:
        data = f.read()
    # 2. 获取数据库中的数据
    # 3. 将 HTML 和数据进行整合
    data = data.replace('{%content%}', time.ctime())
    # 4. 将处理的结构进行返回
    # 处理的结果是 200 3xx 4xx
    status = '200 OK\r\n'
    # 响应头
    header = 'Server:PY\r\nName:index\r\n'
    return status, header, data.encode()


@my_route('/center.html')
def center():
    """
    处理center页面
    """
    # 1. 读取模板中的 HTML 页面
    with open('template/center.html', 'r', encoding='utf-8') as f:
        data = f.read()

    # 2. 获取数据库中的数据
    # 3. 将 HTML 和数据进行整合
    data = data.replace('{%content%}', time.ctime())
    # 4. 将处理的结构进行返回
    # 处理的结果是 200 3xx 4xx
    status = '200 OK\r\n'
    # 响应头
    header = 'Server:PY\r\nName:center\r\n'
    return status, header, data.encode()


def not_found():
    with open('static/404.html', 'rb') as f:
        data = f.read()
    status = '404 Not FOUND\r\n'
    header = 'Server:PY\r\nName:404\r\n'
    return status, header, data


# 定义框架代码
def handle_client_request(env):
    # 1. 获取要处理的资源
    file_name = env['filename']
    for route in route_list:
        if route[0] == file_name:
            return route[1]()
    return not_found()
        
    