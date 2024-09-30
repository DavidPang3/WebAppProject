
# This path is provided as an example of how to use the router

class functions:
        
    def hello_path(request, handler):
            response = "HTTP/1.1 200 OK\r\nContent-Length: 5\r\nContent-Type: text/plain; charset=utf-8\r\n\r\nhello"
            handler.request.sendall(response.encode())

    def send_home(request, handler):
        visitcount = int(request.cookies.get('visit_count', 0))
        visitcount += 1
        cookieinsert = f"visit_count={visitcount}; Max-Age=3600"
        file_path = open('public/index.html', 'r')
        html_content = file_path.read()
        html_content = html_content.replace("{{visits}}", str(visitcount))
        response = f"HTTP/1.1 200 OK\r\nX-Content-Type-Options: nosniff\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: {len(html_content.encode('utf-8'))}\r\nSet-Cookie: {cookieinsert}\r\n\r\n{html_content}"
        handler.request.sendall(response.encode('utf-8'))

    def send_css(request, handler):
        file_path = open('public/style.css', 'r')
        css_content = file_path.read()
        response = f"HTTP/1.1 200 OK\r\nX-Content-Type-Options: nosniff\r\nContent-Type: text/css; charset=utf-8\r\nContent-Length: {len(css_content.encode('utf-8'))}\r\n\r\n{css_content}"
        handler.request.sendall(response.encode('utf-8'))

    def send_javascript(request, handler):
        file_path = open('public/functions.js', 'r')
        javascript_content = file_path.read()
        response = f"HTTP/1.1 200 OK\r\nX-Content-Type-Options: nosniff\r\nContent-Type: application/javascript; charset=utf-8\r\nContent-Length: {len(javascript_content.encode('utf-8'))}\r\n\r\n{javascript_content}"
        handler.request.sendall(response.encode('utf-8'))

    def send_webjavascript(request, handler):
        file_path = open('public/webrtc.js', 'r')
        javascript_webcontent = file_path.read()
        response = f"HTTP/1.1 200 OK\r\nX-Content-Type-Options: nosniff\r\nContent-Type: application/javascript; charset=utf-8\r\nContent-Length: {len(javascript_webcontent.encode('utf-8'))}\r\n\r\n{javascript_webcontent}"
        handler.request.sendall(response.encode('utf-8'))

    def send_image_eagle(request, handler):
        file_path = open('public/image/eagle.jpg', 'rb')
        image_content = file_path.read()
        response = f"HTTP/1.1 200 OK\r\nX-Content-Type-Options: nosniff\r\nContent-Type: image/jpeg;\r\nContent-Length: {len(image_content)}\r\n\r\n"
        handler.request.sendall(response.encode('utf-8'))
        handler.request.sendall(image_content)

    def send_image_cat(request, handler):
        file_path = open('public/image/cat.jpg', 'rb')
        image_content = file_path.read()
        response = f"HTTP/1.1 200 OK\r\nX-Content-Type-Options: nosniff\r\nContent-Type: image/jpeg;\r\nContent-Length: {len(image_content)}\r\n\r\n"
        handler.request.sendall(response.encode('utf-8'))
        handler.request.sendall(image_content)

    def send_image_dog(request, handler):
        file_path = open('public/image/dog.jpg', 'rb')
        image_content = file_path.read()
        response = f"HTTP/1.1 200 OK\r\nX-Content-Type-Options: nosniff\r\nContent-Type: image/jpeg;\r\nContent-Length: {len(image_content)}\r\n\r\n"
        handler.request.sendall(response.encode('utf-8'))
        handler.request.sendall(image_content)

    def send_image_smallelephant(request, handler):
        file_path = open('public/image/elephant-small.jpg', 'rb')
        image_content = file_path.read()
        response = f"HTTP/1.1 200 OK\r\nX-Content-Type-Options: nosniff\r\nContent-Type: image/jpeg;\r\nContent-Length: {len(image_content)}\r\n\r\n"
        handler.request.sendall(response.encode('utf-8'))
        handler.request.sendall(image_content)

    def send_image_elephant(request, handler):
        file_path = open('public/image/elephant.jpg', 'rb')
        image_content = file_path.read()
        response = f"HTTP/1.1 200 OK\r\nX-Content-Type-Options: nosniff\r\nContent-Type: image/jpeg;\r\nContent-Length: {len(image_content)}\r\n\r\n"
        handler.request.sendall(response.encode('utf-8'))
        handler.request.sendall(image_content)

    def send_image_flamingo(request, handler):
        file_path = open('public/image/flamingo.jpg', 'rb')
        image_content = file_path.read()
        response = f"HTTP/1.1 200 OK\r\nX-Content-Type-Options: nosniff\r\nContent-Type: image/jpeg;\r\nContent-Length: {len(image_content)}\r\n\r\n"
        handler.request.sendall(response.encode('utf-8'))
        handler.request.sendall(image_content)

    def send_image_kitten(request, handler):
        file_path = open('public/image/kitten.jpg', 'rb')
        image_content = file_path.read()
        response = f"HTTP/1.1 200 OK\r\nX-Content-Type-Options: nosniff\r\nContent-Type: image/jpeg;\r\nContent-Length: {len(image_content)}\r\n\r\n"
        handler.request.sendall(response.encode('utf-8'))
        handler.request.sendall(image_content)

    def send_ico(request, handler):
        file_path = open('public/favicon.ico', 'rb')
        image_content = file_path.read()
        response = f"HTTP/1.1 200 OK\r\nX-Content-Type-Options: nosniff\r\nContent-Type: image/x-icon;\r\nContent-Length: {len(image_content)}\r\n\r\n"
        handler.request.sendall(response.encode('utf-8'))
        handler.request.sendall(image_content)