import socket

res = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
res.bind(("172.20.0.5",10003))
msg_res = "res server-tcp.com"
res.sendto(msg_res.encode('utf-8'),("172.20.0.2",10000))
data, _ = res.recvfrom(1024)

resp = data.decode('utf-8').split()
addr = (resp[0],int(resp[1]))

res.close()

#debugging
print(addr)

#add buffer aqui tbm
tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp.bind(("172.20.0.5",10003))
tcp.connect(addr)

tcp.sendall(("ADD 7 8\n").encode("utf-8"))
data = tcp.recv(1024)
resp = data.decode("utf-8")
print(resp)

tcp.sendall(("MOD 40 7\n").encode("utf-8"))
data = tcp.recv(1024)
resp = data.decode("utf-8")
print(resp)

tcp.sendall(("SQRT 9\n").encode("utf-8"))
data = tcp.recv(1024)
resp = data.decode("utf-8")
print(resp)