import socketserver
from util.request import Request
from util.router import Router
from util.hello_path import functions

class MyTCPHandler(socketserver.BaseRequestHandler):

    def __init__(self, request, client_address, server):
        self.router = Router()
        self.router.add_route("GET", "/", functions.send_home, True)
        self.router.add_route("GET", "/public/style.css", functions.send_css, True)
        self.router.add_route("GET", "/public/functions.js", functions.send_javascript, True)
        self.router.add_route("GET", "/public/webrtc.js", functions.send_webjavascript, True)
        self.router.add_route("GET", "/public/image/eagle.jpg", functions.send_image_eagle, True)
        self.router.add_route("GET", "/public/image/cat.jpg", functions.send_image_cat, True)
        self.router.add_route("GET", "/public/image/dog.jpg", functions.send_image_dog, True)
        self.router.add_route("GET", "/public/image/elephant-small.jpg", functions.send_image_smallelephant, True)
        self.router.add_route("GET", "/public/image/elephant.jpg", functions.send_image_elephant, True)
        self.router.add_route("GET", "/public/image/flamingo.jpg", functions.send_image_flamingo, True)
        self.router.add_route("GET", "/public/image/kitten.jpg", functions.send_image_kitten, True)
        self.router.add_route("GET", "/public/favicon.ico", functions.send_ico, True)

        self.router.add_route("GET", "/chat-messages", functions.data_get, False)
        self.router.add_route("POST", "/chat-messages", functions.data_post, False)
        self.router.add_route("DELETE", "/chat-messages", functions.data_delete, False)
        
        self.router.add_route("GET", "/", functions.send_404, False)
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