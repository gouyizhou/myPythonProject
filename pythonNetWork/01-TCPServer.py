# coding:utf-8
import socket
import threading
import time

def dealClient(sock, addr):
    # 接收数据
    print("Accept new connection from %s:%s..." % addr)
    sock.send(b"Hello I'm server!")
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        # 无数据或者编码不正确
        if not data or data.decode('utf-8') == "exit":
            break
        print("--->>%s!" % data.decode("utf-8"))
        sock.send((b'Loop_Msg: %s' % data.decode('utf-8').encode('utf-8')))
    # 关闭Socket
    sock.close()
    print("Connection from %s:%s closed." % addr)


if __name__ == '__main__':
    addr ='127.0.0.1'
    port = 9999
    # 创建Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((addr, port))
    s.listen(5)
    print("Waiting for connection...")
    while True:
        # 新连接
        sock ,addrs = s.accept()
        # 创建线程处理TCP连接
        t = threading.Thread(target=dealClient, args=(sock ,addrs))
        t.start()