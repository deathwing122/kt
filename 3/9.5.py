import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('jsonplaceholder.typicode.com', 80))

request = (
    "GET /posts/1 HTTP/1.1 \r\n"
    "Host: jsonplaceholder.typicode.com\r\n"
    "Connection: close\r\n"
    "\r\n"
)

sock.send(request.encode())

response = b''
while True:
    chunk = sock.recv(4096)
    if not chunk:
        break
    response += chunk
sock.close()

header_end = response.find(b"\r\n\r\n")
if header_end != -1:
    body =response[header_end+4:]
else:
    body = response

print(body.decode())