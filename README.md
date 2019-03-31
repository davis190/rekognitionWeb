# Setup

1. You need to run the server using SSL. You can do that locally with a python web server and a cert.
```
openssl req -new -x509 -keyout yourpemfile.pem -out yourpemfile.pem -days 365 -nodes

echo 127.0.0.1 localhost >> /etc/hosts

python local-server-ssl.py
```