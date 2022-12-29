import socket


def handle_client_request(n_socket, client_ip_port):
    # 5. 接收信息（请求报文）
    buf = n_socket.recv(4096)  # buf 是请求报文
    if buf:
        print(buf.decode('gbk'))
        # 6. 发送信息（响应报文）
        # 6.1 响应行
        response_line = 'HTTP/1.1 200 OK\r\n'
        # 6.2 响应头
        response_header = 'Server:PY\r\nName:Py42\r\n'
        # 6.3 空行 \r\n
        # 6.4 响应体(具体的页面数据)，返回 index.html 的页面
        f = open('static/index1.html', 'rb')  # 读取到的是 bytes 类型
        data = f.read()
        f.close()
        # 6.5 合成响应体
        response = (response_line + response_header + '\r\n').encode('gbk') + data
        n_socket.send(response)
    else:
        print(f'{client_ip_port} 下线了...')
    # 7. 关闭连接
    n_socket.close()


if __name__ == '__main__':
    # 1. 创建 socket 对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口复用
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 2. 绑定`IP`和端口 `bind`
    server_socket.bind(("", 8989))
    # 3. 设置监听
    server_socket.listen(128)
    # 4. 阻塞等待客户端连接
    while True:
        new_socket, ip_port = server_socket.accept()
        print(f'{ip_port} 已连接...')
        handle_client_request(new_socket, ip_port)
    