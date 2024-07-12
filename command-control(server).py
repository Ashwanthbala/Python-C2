import socket
import threading,time

ip_address = '127.0.0.1'
port = 5555

def handle_connection(connection,address):
  msg = connection.recv(1024).decode()
  while msg != 'quit':
    print(msg)
    connection.send(msg.encode())
    msg = connection.recv(1024).decode()
  close_connection(connection)

def close_connection(connection):
  connection.close()

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((ip_address,port))
server_socket.listen(5)

while True:
  client_socket, address = server_socket.accept()
  print("Listening")
  t=threading.Thread(target=handle_connection,args=(client_socket,address))
  t.start()

