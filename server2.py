import socket
s=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
s.bind(('localhost',1234))
msg="Hello client its server here"
msg=msg.encode()
print('Waiting for connection')
while True:
	msg1=s.recvfrom(1024)
	print("Message from Client")
	print(msg1[0].decode())
	print("Address of Client")
	print(msg1[1])
	s.sendto(msg,msg1[1])
