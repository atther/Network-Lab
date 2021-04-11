import socket
c=socket.socket()
c.connect(('localhost',1234))
msg="Hello server its me client "
msg=msg.encode()
c.send(msg)
print("Message from Server ")
print(c.recv(1024).decode())

