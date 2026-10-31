import socket
import threading

reg = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
reg.bind(("172.20.0.4", 10002))
reg_msg = "reg server-udp.com 172.20.0.4 10002"
reg.sendto(reg_msg.encode("utf-8"),("172.20.0.2", 10000))

resp, _ = reg.recvfrom(1024)
#nesse caso tem que fechar obrigatoriamenre, pois o outro socket UDP tem o mesmo ip e porta
reg.close()
 
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("172.20.0.4", 10002))
print("Server UDP ativo")


def app(msg,addr):
    op = msg.split()
    if op[0] == "ADD":
        a, b = op[1:]
        s.sendto(str((int(a)+int(b))).encode("utf-8"),addr)
    elif op[0] == "SUB":
        a, b = op[1:]
        s.sendto(str((int(a)-int(b))).encode("utf-8"),addr)
    elif op[0] == "MUL":
        a, b = op[1:]
        s.sendto(str((int(a)*int(b))).encode("utf-8"),addr)
    elif op[0] == "DIV":
        a, b = op[1:]
        s.sendto(str((int(a)/int(b))).encode("utf-8"),addr)
    elif op[0] == "POW":
        a, b = op[1:]
        s.sendto(str((int(a)**int(b))).encode("utf-8"),addr)
    elif op[0] == "MOD":
        a, b = op[1:]
        s.sendto(str((int(a)%int(b))).encode("utf-8"),addr)
    elif op[0] == "SQRT":
        a = op[1]
        s.sendto(str((int(a)**0.5)).encode("utf-8"),addr)

    
while True:
    data, addr = s.recvfrom(1024)
    msg = data.decode('utf-8')
    thread = threading.Thread(target=app,args=(msg,addr))
    thread.start()