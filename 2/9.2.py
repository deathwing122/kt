import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8888))

message = "Hello, server!"
client_socket.send(message.encode('utf-8'))

client_socket.close()
print("Сообщние отправлено")
