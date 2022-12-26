import socket
import threading


def handle_client_request(n_socket, client_ip_port):
    while True:
        buf = n_socket.recv(4096)
        if buf:
            try:
                print(f'接收到{client_ip_port}的信息为：', buf.decode('utf-8'))
            except UnicodeDecodeError:
                print(f'接收到{client_ip_port}的信息为：', buf.decode('gbk'))
            send_data = '信息已收到'.encode('gbk')
            n_socket.send(send_data)
        else:
            print(f'客户端 {client_ip_port} 已下线')
            break
    n_socket.close()


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind(('', 9000))
    server_socket.listen(128)
    print('等待连接中......')
    # 循环等待客户端的连接
    while True:
        new_socket, ip_port = server_socket.accept()
        print(f'客户端：{ip_port} 上线了......')
        # 创建线程，执行任务
        sub_thread = threading.Thread(target=handle_client_request, args=(new_socket, ip_port))
        # 启动线程
        sub_thread.start()
    server_socket.close()  # 关闭监听的 socket
