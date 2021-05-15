# coding:utf-8
import socket
if __name__ == '__main__':
    addr = '127.0.0.1'
    port = 9999
    # 创建套接字
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接到目的地址和端口
    s.connect((addr, port))
    # 接收消息
    print('-->>'+s.recv(1024).decode('utf-8'))
    # 发送消息
    s.send(b"Hello I'm Client!")
    print('-->>'+s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    # 关闭连接
    s.close()