import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8888))

server_socket.listen(1)
print("Сервер заущен на 127.0.0.1:8888, ожидаем подключения...")

client_socket, client_address = server_socket.accept()
print(f"Подключился клиент с адреса {client_address}")

data = client_socket.recv(1024)
print(f"Получено сообщение: {data.decode('utf-8')}")

client_socket.close()
server_socket.close()
print("Сервер завершил работу.")

input()