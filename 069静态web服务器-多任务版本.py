import socket
import threading


def handle_client_request():
    pass


if __name__ == "__name__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind('', 8888)
    server_socket.listen(128)
    while True:
        new_socket, ip_port = server_socket.accept()
        sub_thread = threading.Thread(target=handle_client_request, args=(new_socket, ip_port))
        sub_thread.start()
        
    server_socket.close()
    