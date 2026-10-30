import socket
import threading

def app(msg,addr):
    ...

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("172.20.0.2", 10000))

while True:
    print("Server DNS ativo")
    data, addr = s.recvfrom(1024)
    msg = data.decode('utf-8')
    thread = threading.Thread(target=app,args=(msg,addr))
    thread.start()

