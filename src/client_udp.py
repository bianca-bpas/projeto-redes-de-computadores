import socket

res = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
res.bind(("172.20.0.6",10004))
msg_res = "res server-udp.com"
res.sendto(msg_res.encode('utf-8'),("172.20.0.2",10000))
data, _ = res.recvfrom(1024)

resp = data.decode('utf-8').split()
addr = tuple(resp)

res.close()

#debugging
print(addr)
