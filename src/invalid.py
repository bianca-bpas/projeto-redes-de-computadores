import socket

res = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
res.bind(("172.20.0.7",10005))
msg_res = "res google.com"
res.sendto(msg_res.encode('utf-8'),("172.20.0.2",10000))
data, _ = res.recvfrom(1024)

resp = data.decode('utf-8')
res.close()

if resp == "NOT FOUND":
    ...

#debugging
print(resp)