import socket


def handle_client_request(n_socket, client_ip_port):
    # 5. 接收信息（请求报文）
    buf = n_socket.recv(809600)  # buf 是请求报文
    print(str(buf))

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
