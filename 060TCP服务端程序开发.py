import socket


if __name__ == '__main__':
    # 1. 创建 socket 对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 绑定 ip 和 port  bind((ip, port) 元组类型)
    server_socket.bind(('', 9000))  # 第一个参数为空，表示绑定服务器中任意的一个网卡
    # 3. 设置监听，参数代表同时最大可以连接服务器的客户端数，连接成功后，就不再占用这个名额了
    server_socket.listen(128)
    # 4. 阻塞等待客户端的连接，返回一个元组（新的socket，(客户端的IP, 端口)）
    print('等待连接中......')
    new_socket, ip_port = server_socket.accept()
    print(f'客户端：{ip_port} 上线了......')
    # 5. 新的 socket 收信息，阻塞等待
    buf = new_socket.recv(4096)
    try:
        print('接收到的信息为：', buf.decode('utf-8'))
    except UnicodeDecodeError:
        print('接收到的信息为：', buf.decode('gbk'))
    # 6. 新的 socket 发信息
    send_data = '信息已收到'.encode('gbk')
    new_socket.send(send_data)
    # 7. 关闭
    new_socket.close()
    server_socket.close()
