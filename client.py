import socket

ip_address = '127.0.0.1'
port = 5555

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect((ip_address,port))

msg = input("Enter message to send: ")

while msg != 'quit':
    client_socket.send(msg.encode())
    msg = client_socket.recv(1024).decode()
    print(msg)
    msg = input("Enter message to send: ")


client_socket.close()