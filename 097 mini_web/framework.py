import time
import json
# 数组转json
# my_list = [{'key': 'value'}]
# json.dumps(my_list, ensure_ascii=False)


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
    if file_name == '/index.html':
        return index()
    elif file_name == '/center.html':
        return center()
    else:
        return not_found()
        
    