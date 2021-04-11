import socket
s=socket.socket()
s.bind(('localhost',1234))
s.listen(3)
print('Waiting for connection')
while True:
	c,addr=s.accept()
	print("Connected with client of address",addr)
	d=c.recv(1024).decode()
	print("Message from Client\n",d)
	#print()
	msg="Hello client its server here"
	msg=msg.encode()
	c.send(msg)
	c.close()
