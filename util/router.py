class Router:

    def __init__(self):
        self.routes = []

    def add_route(self, method, path, action, exact_path=False):
        self.method = method
        self.path = path
        self.boolean = exact_path
        self.function = action

        

    def route_request(self, request, handler):
        pass

def test1():
    router = Router
    print(f"routes: {router.routes}")


if __name__ == '__main__':
    test1()
