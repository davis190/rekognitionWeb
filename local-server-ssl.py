# openssl req -new -x509 -keyout yourpemfile.pem -out yourpemfile.pem -days 365 -nodes
# echo 127.0.0.1 localhost >> /etc/hosts

import BaseHTTPServer, SimpleHTTPServer
import ssl

httpd = BaseHTTPServer.HTTPServer(('localhost', 4443), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, server_side=True, certfile='yourpemfile.pem')
httpd.serve_forever()