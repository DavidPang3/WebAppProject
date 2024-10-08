class Router:

    def __init__(self):
        self.routes = []


#method: GET, path: / , action: sendhtml, exact_path = false or true

    def add_route(self, method, path, action, exact_path=False):
        self.routes.append({'method':method, 'path':path, 'action':action, 'exact_path':exact_path})

    def route_request(self, request, handler):
        for index in self.routes:
            if index['exact_path'] == True:
                if index['method'] == request.method and index['path'] == request.path:
                    index['action'](request, handler)
                    return
             
            elif index['exact_path'] == False:
                if index['method']==request.method and request.path.startswith(index['path']):
                    index['action'](request, handler)
                    return

        response = 'HTTP/1.1 404 Not Found\r\n Content-Type: text/plain\r\n Content-Length: 36\r\n\r\nThe requested content does not exist'
        handler.request.sendall(response.encode())
        return
    