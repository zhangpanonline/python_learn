import socket

if __name__ == '__main__':
    # 1. 创建 socket 对象（`socket.socket(ip 类型，协议)`）
    # ipv4：socket.AF_INET；ipv6: socket.AF_INET6
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 固定写法
    # 2. 和服务器建立连接（`socket对象.connect((服务器ip地址，端口号))`） 类型是元祖
    client_socket.connect(('10.10.22.114', 8080))
    print('客户端建立连接成功......')
    # 3. 发送信息（`socket对象.send(发送的信息) 参数类型bytes`）
    send_data = '你好服务器，我是客户端......'.encode('gbk')
    client_socket.send(send_data)
    # 4. 接受对方发送的信息（`socket对象.recv(一次接收多少字节的数据)`）
    # 如果对方没有发送信息，recv 函数会在此阻塞等待
    buf = client_socket.recv(4096)
    try:
        print(buf.decode('utf-8'))
    except UnicodeDecodeError:
        print(buf.decode('gbk'))
    # 5. 关闭连接（`socket对象.close()`）
    client_socket.close()
