import socket

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = "localhost"
PORT = 8000

socket.connect((HOST,PORT))

data = socket.recv(1024)

print data

socket.send("Hoþbulduk!!")

socket.close()
