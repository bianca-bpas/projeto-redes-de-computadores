import socket
import threading

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

