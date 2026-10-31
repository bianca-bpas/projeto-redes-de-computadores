import socket
import threading

#ver se pode ter algum problema com race condition
mapping = {}

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("172.20.0.2", 10000))
print("Server DNS ativo")

def app(data,addr):
    msg = data.decode('utf-8')
    op = msg.split()
    if op[0] == "reg" and len(op) == 4:
        #perguntar se precrisa tratar entradas erradas(tem algo sobre na especificação)
        name, ip, port = op[1:]
        mapping[name] = ((ip,port))
        resp = "OK"
        s.sendto(resp.encode('utf-8'),addr)
        #debugging
        print(mapping)
    elif op[0] == "res" and len(op) == 2:
        name = op[1]  
        if name not in mapping:
            resp = "NOT FOUND"
            s.sendto(resp.encode('utf-8'),addr)
        else:
            resp = f"{mapping[name][0]} {mapping[name][1]}"
            s.sendto(resp.encode('utf-8'),addr)
    else:
        s.sendto("INVALID INPUT")
            

while True:
    data, addr = s.recvfrom(1024)
    thread = threading.Thread(target=app,args=(data,addr))
    thread.start()

