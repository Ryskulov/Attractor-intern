from http.server import HTTPServer

from handler import MyHandler

PORT_NUMBER = 8080

try:

    server = HTTPServer(('', PORT_NUMBER), MyHandler)
    print('Started httpserver on port ', PORT_NUMBER)

    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()
