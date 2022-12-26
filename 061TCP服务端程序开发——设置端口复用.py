import socket


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口复用
    # setsockopt 设置端口权限
    # 第一个参数：level 设置哪个级别的 socket socket.SOL_SOCKET 当前的socket
    # 第二个参数：optname 设置什么内容（权限） socket.SO_REUSEADDR 端口复用
    # 第三个参数：value 设置什么值，True
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind(('', 9000))
    server_socket.listen(128)
    print('等待连接中......')
    new_socket, ip_port = server_socket.accept()
    print(f'客户端：{ip_port} 上线了......')
    buf = new_socket.recv(4096)
    try:
        print('接收到的信息为：', buf.decode('utf-8'))
    except UnicodeDecodeError:
        print('接收到的信息为：', buf.decode('gbk'))
    send_data = '信息已收到'.encode('gbk')
    new_socket.send(send_data)
    new_socket.close()
    server_socket.close()
