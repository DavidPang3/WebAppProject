class Request:

    def __init__(self, request: bytes):
        # TODO: parse the bytes of the request and populate the following instance variables

        self.body = b""
        self.method = ""
        self.path = ""
        self.http_version = ""
        self.headers = {}
        self.cookies = {}

        separatefirst = request.split(b'\r\n\r\n')

        requesttransform = separatefirst[0].decode()

        lines = requesttransform.splitlines()
                                        #GET / HTTP/1.1,    Host: localhost:8080,    Connection: keep-alive,    Cookie: key=cookie1; key=cookie2; key=cookie3;    ,pseudobody 

        for eachline in lines:
            print(f"eachline: {eachline}")
            if eachline:
                if ':' in eachline:
                    if 'Cookie' in eachline:
                        spliteachline = eachline.split(':', 1)
                        self.headers[spliteachline[0].strip()] = spliteachline[1].strip()
                        spliteachline2 = spliteachline[1].split('; ')
                        for linez in spliteachline2:
                            spliteachline3 = linez.split('=')
                            self.cookies[spliteachline3[0].strip()] = spliteachline3[1].strip()
                    else:
                        splitheaderline = eachline.split(':', 1)
                        self.headers[splitheaderline[0].strip()] = splitheaderline[1].strip()

                else:
                    self.method, self.path, self.http_version = eachline.split()

        if separatefirst[1]:
            self.body = separatefirst[1]



def test2():
    request = Request(b'POST /path1231 HTTP/1.1\r\n Host:       localhost:8080   \r\n   Connection:  keep-alive \r\n  headerasdiunasoudn:    asdasd \r\n   asodunasdheader2:asdoaisnd \r\n  header3forbettertesting:VALUE!!!\r\n   Cookie: id1    = thisdobeacookie; id2=   thisanothercookie; id3   =   thisathirdcookie\r\n\r\nHELLO WORLD!!!')
    assert request.method == 'POST'
    assert request.path == '/path1231'
    assert request.http_version == 'HTTP/1.1'
    assert request.body == b"HELLO WORLD!!!"
    assert request.headers["Host"] == "localhost:8080"
    assert "Host" in request.headers
    assert request.cookies["id1"] == "thisdobeacookie" 
    assert request.cookies["id2"] == "thisanothercookie"
    #print(f"method = {request.method}\n")
    #print(f"path = {request.path}\n")
    #print(f"http_version = {request.http_version}\n")
    #print(f"amount of bytes in body = {request.body}\n")
    #print(f"headers = {request.headers}\n")
    #print(f"cookies = {request.cookies}\n")

def test1():
    request = Request(b'GET / HTTP/1.1\r\nHost: localhost:8080\r\nConnection: keep-alive\r\n\r\n')
    assert request.method == "GET"
    assert "Host" in request.headers
    assert request.headers["Host"] == "localhost:8080"  # note: The leading space in the header value must be removed
    assert request.body == b""  # There is no body for this request.
    #print(f"amount of bytes in body = {request.body}")
    # When parsing POST requests, the body must be in bytes, not str
    # This is the start of a simple way (ie. no external libraries) to test your code.
    # It's recommended that you complete this test and add others, including at least one
    # test using a POST request. Also, ensure that the types of all values are correct

if __name__ == '__main__':
    test2()
    test1()






#docker compose up --build --force-recreate rebuild and restart
#docker compose up run your app
#-d for detached mode
#docker compose restart (restart without rebuilding)

#http headers can only contain ASCII and end with /r/n/r/n
#get string length by converting to bytes then getting the length look at lecture 9/9
#lecture 9/11 is for learning objective 3 the first 2 learning objectives i should know now yipee