# coding:utf-8
import socket
addr = '127.0.0.1'
port = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Hello', b'world!']:
    s.sendto(data,(addr, port))
    print(s.recv(1024).decode('utf-8'))
s.close()