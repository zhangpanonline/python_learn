import socket


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind(('', 9000))
    server_socket.listen(128)
    print('等待连接中......')
    new_socket, ip_port = server_socket.accept()
    print(f'客户端：{ip_port} 上线了......')
    # 当对方的 socket close 之后，自己的 socket 不再阻塞了，recv 接收的内容是空字符串，长度为0
    buf = new_socket.recv(4096)
    if buf: 
        try:
            print('接收到的信息为：', buf.decode('utf-8'))
        except UnicodeDecodeError:
            print('接收到的信息为：', buf.decode('gbk'))
        send_data = '信息已收到'.encode('gbk')
        new_socket.send(send_data)
    else:
        print(f'客户端 {ip_port} 已下线')
    new_socket.close()
    server_socket.close()
