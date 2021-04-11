import socket
msg="Hello server its me client "
msg=msg.encode()
servaddr=(('localhost',1234))
c=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
c.sendto(msg,servaddr)
msg1=c.recvfrom(1024)
print("Message from Server")
print(msg1[0].decode())
