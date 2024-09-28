import socketserver
from util.request import Request
from util.router import Router
from util.hello_path import hello_path

#request to response
def send_home(request, handler):
        response = "HTTP/1.1 200 OK\r\nContent-Length: 10\r\nContent-Type: text/plain; charset=utf-8\r\n\r\nhellomydud"
        handler.request.sendall(response.encode())

class MyTCPHandler(socketserver.BaseRequestHandler):

    def __init__(self, request, client_address, server):
        self.router = Router()
        self.router.add_route("GET", "/", send_home, True)
        super().__init__(request, client_address, server)

    def handle(self):
        received_data = self.request.recv(2048)
        print(self.client_address)
        print("--- received data ---")
        print(received_data)
        print("--- end of data ---\n\n")
        request = Request(received_data)
        self.router.route_request(request, self)

def main():
    host = "0.0.0.0"
    port = 8080
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.TCPServer((host, port), MyTCPHandler) 
    print("Listening on port " + str(port))
    server.serve_forever()


if __name__ == "__main__":
    main()