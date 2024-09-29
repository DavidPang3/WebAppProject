import socketserver
from util.request import Request
from util.router import Router
from util.hello_path import hello_path

#request to response

def send_home(request, handler):
    file_path = open('public/index.html', 'r')
    html_content = file_path.read()
    response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: {len(html_content.encode('utf-8'))}\r\nConnection: close\r\n\r\n{html_content}"
    handler.request.sendall(response.encode('utf-8'))
    
def send_css(request, handler):
    file_path = open('public/style.css', 'r')
    css_content = file_path.read()
    response = f"HTTP/1.1 200 OK\r\nContent-Type: text/css; charset=utf-8\r\nContent-Length: {len(css_content)}\r\nConnection: close\r\n\r\n{css_content}"
    handler.request.sendall(response.encode('utf-8'))

def send_javascript(request, handler):
    javascript = ""
    handler.request.sendall(javascript.encode())

def send_images(request, handler):
    images = ""
    handler.request.sendall(images.encode())



class MyTCPHandler(socketserver.BaseRequestHandler):

    def __init__(self, request, client_address, server):
        self.router = Router()
        self.router.add_route("GET", "/", send_home, True)
        #self.router.add_route("GET", "styles.css", send_css, True)
        #self.router.add_route("GET", "/", send_javascript, True)
        #self.router.add_route("GET", "/", send_images, True)
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