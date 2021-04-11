import socket
import threading
import time

HEADER = 1024
PORT = 33000
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST,PORT)
FORMAT = "utf-8"
DISCONNECT_MSG = "BYE"

CLIENT = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
CLIENT.connect(ADDR)

def receive():
	while True:
		try:
			msg = CLIENT.recv(HEADER).decode(FORMAT)
			print(msg)
		except OSError:
			break

def send():
	my_name = input("")
	name = my_name.encode(FORMAT)
	CLIENT.send(name)
	
	while True:
		msg = input(f"")
		if msg != DISCONNECT_MSG:
			msg = msg.encode(FORMAT)
			CLIENT.send(msg)
		else:
			msg = msg.encode(FORMAT)
			CLIENT.send(msg)
			CLIENT.close()
			break

def main():
	RECV_THREAD = threading.Thread(target = receive)
	RECV_THREAD.start()
	
	SEND_THREAD = threading.Thread(target = send)
	SEND_THREAD.start()
	
	time.sleep(1)
	while threading.activeCount() > 1:
		pass


if __name__ == "__main__":
	main()
	
server.close()
