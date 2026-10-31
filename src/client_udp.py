import socket

res = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
res.bind(("172.20.0.6",10004))
msg_res = "res server-udp.com"
res.sendto(msg_res.encode('utf-8'),("172.20.0.2",10000))
data, _ = res.recvfrom(1024)

resp = data.decode('utf-8').split()
addr = (resp[0],int(resp[1]))

res.close()

#debugging
print(addr)

udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp.bind(("172.20.0.6",10004))

udp.sendto(("ADD 7 8").encode("utf-8"),addr)
data, _ = udp.recvfrom(1024)
resp = data.decode("utf-8")
print(resp)

udp.sendto(("MOD 40 7").encode("utf-8"),addr)
data, _ = udp.recvfrom(1024)
resp = data.decode("utf-8")
print(resp)

udp.sendto(("SQRT 9").encode("utf-8"),addr)
data, _ = udp.recvfrom(1024)
resp = data.decode("utf-8")
print(resp)