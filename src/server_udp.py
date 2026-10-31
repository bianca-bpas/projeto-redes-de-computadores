import socket
import threading

def app(data,addr):
    ...
 
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("172.20.0.4", 10002))
print("Server UDP ativo")

while True:
    data, addr = s.recvfrom(1024)
    msg = data.decode('utf-8')
    thread = threading.Thread(target=app,args=(msg,addr))
    thread.start()