import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8888))

try:
    while True:
        message = input("Введите сообщения (или 'exit' для выхода):")
        if message.lower == "exit":
            break
        client_socket.send(message.encode('utf-8'))
        response = client_socket.recv(1024)
        print(f"Ответ сервера: {response.decode("utf-8")}")
finally:
    client_socket.close()

input()