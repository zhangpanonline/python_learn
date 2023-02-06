import socket
import threading


class WebHttpServer(object):
    
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.server_socket.bind(('', 8888))
        self.server_socket.listen(128)
        
    def __del__(self):
        self.server_socket.close()
        
    def start(self):
        while True:
            new_socket, ip_port = self.server_socket.accept()
            print(f'{ip_port} 连接了...')
            sub_thread = threading.Thread(target=self.handle_client_request, args=(new_socket, ip_port))
            sub_thread.start()
        
    @staticmethod
    def handle_client_request(new_socket, client_ip_port):
        buf = new_socket.recv(4096)
        if buf:
            file_name = buf.decode('gbk').split(' ', 2)[1]
            if file_name == '/':
                file_name = '/index1.html'
            response_line = 'HTTP/1.1 200 OK\r\n'
            try:
                f = open('static' + file_name, 'rb')
            except FileNotFoundError:
                f = open('static/404.html', 'rb')
                response_line = 'HTTP/1.1 404 NOT FOUND\r\n'
            data = f.read()
            f.close()
            response = (response_line + '\r\n').encode('gbk') + data
            new_socket.send(response)
        else:
            print(f'{client_ip_port} 下线了...')
        new_socket.close()
        
        
if __name__ == '__main__':
    server = WebHttpServer()
    server.start()
    
