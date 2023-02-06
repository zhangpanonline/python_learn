import socket
import threading


def handle_client_req(new_socket, ip_port):
    while True:
        buf = new_socket.recv(4096)
        if buf:
            try:
                print(f'接收到{ip_port}的信息为：', buf.decode('utf-8'))
            except UnicodeDecodeError:
                pass
            send_data = '信息已收到'.encode('gbk')
            new_socket.send(send_data)
        else:
            pass
    new_socket.close()


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind(('', 8888))
    server_socket.listen(128)
    while True:
        new_socket, ip_port = server_socket.accept()
        sub_thread = threading.Thread(target=handle_client_req, args=(new_socket, ip_port))
        sub_thread.start()
    server_socket.close()