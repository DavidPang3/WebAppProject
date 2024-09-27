class Request:

    def __init__(self, request: bytes):
        # TODO: parse the bytes of the request and populate the following instance variables

        self.body = b""
        self.method = ""
        self.path = ""
        self.http_version = ""
        self.headers = {}
        self.cookies = {}

        self.body.decode


def test1():
    request = Request(b'GET / HTTP/1.1\r\nHost: localhost:8080\r\nConnection: keep-alive\r\n\r\n')
    assert request.method == "GET"
    assert "Host" in request.headers
    assert request.headers["Host"] == "localhost:8080"  # note: The leading space in the header value must be removed
    assert request.body == b""  # There is no body for this request.
    # When parsing POST requests, the body must be in bytes, not str

    # This is the start of a simple way (ie. no external libraries) to test your code.
    # It's recommended that you complete this test and add others, including at least one
    # test using a POST request. Also, ensure that the types of all values are correct


if __name__ == '__main__':
    test1()








#docker compose up --build --force-recreate rebuild and restart
#docker compose up run your app
#-d for detached mode
#docker compose restart (restart without rebuilding)

#http headers can only contain ASCII and end with /r/n/r/n
#get string length by converting to bytes then getting the length look at lecture 9/9
#lecture 9/11 is for learning objective 3 the first 2 learning objectives i should know now yipee