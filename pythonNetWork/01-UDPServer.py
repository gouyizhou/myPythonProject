# coding:utf-8
import socket
# 创建套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定地址和端口
addr = '127.0.0.1'
port = 9999
s.bind((addr,port))
print("Bind UDP on",port)
# 数据处理
while True:
    data, addr = s.recvfrom(1024)
    print(data)
    print(addr)
    print("Receive data from %s:%s" % addr)
    s.sendto(b"Hello, %s!" % data, addr)
