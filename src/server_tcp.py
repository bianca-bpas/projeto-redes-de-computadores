import socket
import threading

reg = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
reg.bind(("172.20.0.3", 10001))
reg_msg = "reg server-tcp.com 172.20.0.3 10001"
reg.sendto(reg_msg.encode("utf-8"),("172.20.0.2", 10000))

resp, _ = reg.recvfrom(1024)
reg.close()

def app(data):
    ...

def connection(conn,addr):
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            msg = data.decode('utf-8')
            app(data)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("172.20.0.3", 10001))
s.listen()
print("Server TCP ativo")

while True:
    conn, addr = s.accept()
    thread = threading.Thread(target=connection,args=(conn,addr))
    thread.start()

