
# This path is provided as an example of how to use the router
import json
from pymongo import MongoClient
import uuid

mongo_client = MongoClient("mongo")
db = mongo_client["cse312"]
chat_collection = db["chat"]


def injection(message):
    newstring = ""
    for index in message:
        if(index == '&'):
            newstring += "&amp"
        elif(index == '<'):
            newstring += "&lt"
        elif(index == '>'):
            newstring += "&gt"
        else:
            newstring += index
    return newstring


class functions:
   
    def data_get(request, handler):
        all_data = chat_collection.find({})
        chat_history = []
        
        for message in all_data:
            chat_history.append({
                "message": message["message"],
                "username": message["username"],
                "id": message["id"]
            })
            
        messageresponse = json.dumps(chat_history)
        response = f'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: {len(messageresponse.encode("utf-8"))}\r\n\r\n{messageresponse}'
        handler.request.sendall(response.encode())

        
    def data_post(request, handler):
        unique_id = str(uuid.uuid4())
        body = request.body.decode('utf-8')
        holder = json.loads(body)
        message = holder["message"]
        parsedmessage = injection(message)
        chat_collection.insert_one({"username": "Guest", "message": parsedmessage, "id": unique_id}) 

        messageresponse = "Successfully Sent!"
        response = f'HTTP/1.1 200 OK\r\n Content-Type: text/plain\r\n Content-Length: {len(messageresponse.encode("utf-8"))}\r\n\r\n{messageresponse}'
        handler.request.sendall(response.encode())

    def data_delete(request, handler):
        id = request.path.split("/")[2]
        print(f"id = {id}")
        chat_collection.delete_one({"id": id})
        response = "HTTP/1.1 204 No Content\r\nContent-Length: 0\r\nContent-Type: text/plain; charset=utf-8\r\n\r\n"
        handler.request.sendall(response.encode())


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

    def send_404(request, handler):
        message = "The requested conted does not exist!! Try another pathway!"
        response = f'HTTP/1.1 404 Not Found\r\n Content-Type: text/plain\r\n Content-Length: {len(message)}\r\n\r\n{message}'
        handler.request.sendall(response.encode())
