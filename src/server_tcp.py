import socket
import threading

reg = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
reg.bind(("172.20.0.3", 10001))
reg_msg = "reg server-tcp.com 172.20.0.3 10001"
reg.sendto(reg_msg.encode("utf-8"),("172.20.0.2", 10000))

resp, _ = reg.recvfrom(1024)
reg.close()

"""
ADD a b 
SUB a b
MUL a b
DIV a b 
POW a b 
MOD a b 

SQRT a
"""

def app(msg):
    op = msg.split()
    if op[0] == "ADD":
        a,b = op[1:]
        a = int(a);b=int(b)
        return str(a+b)
    elif op[0] == "SUB":
        a,b = op[1:]
        a = int(a);b=int(b)
        return str(a-b)
    elif op[0] == "MUL":
        a,b = op[1:]
        a = int(a);b=int(b)
        return str(a*b)
    elif op[0] == "DIV":
        a,b = op[1:]
        a = int(a);b=int(b)
        return str(a/b)
    elif op[0] == "POW":
        a,b = op[1:]
        a = int(a);b=int(b)
        return str(a**b)
    elif op[0] == "MOD":
        a,b = op[1:]
        a = int(a);b=int(b)
        return str(a%b)
    elif op[0] == "SQRT":
        a= op[1]
        a = int(a)
        return str(a**0.5)


def connection(conn,addr):
    with conn:
        buffer = ""
        while True:
            data = conn.recv(1024)
            if not data:
                break
            payload = data.decode('utf-8')
            buffer += payload
            if "\n" in buffer:
                msg, buffer = buffer.split("\n",1)
                resp = app(msg)
                conn.sendall(resp.encode("utf-8"))
            

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("172.20.0.3", 10001))
s.listen()
print("Server TCP ativo")

while True:
    conn, addr = s.accept()
    thread = threading.Thread(target=connection,args=(conn,addr))
    thread.start()

