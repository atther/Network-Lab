import socket
import threading

clients = {}
addresses = {}

HEADER = 1024
PORT = 33000
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST,PORT)
FORMAT= "utf-8"
DISCONNECT_MSG = "BYE"

SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
SERVER.bind(ADDR)

def accept_connections():
	while True:
		conn, client_addr = SERVER.accept()
		print(f"New Connection {client_addr} connected.")
		conn.send(bytes("Enter name to start the chat",FORMAT))
		addresses[conn] = client_addr
		thread=threading.Thread(target=handle_client,args=(conn,))
		thread.start()

def handle_client(conn):
	name = conn.recv(HEADER).decode(FORMAT)
	welcome = (f"Welcome {name}, if u ever want to quit, type {DISCONNECT_MSG} for clean disconnection.")
	conn.send(bytes(welcome,FORMAT))
	msg = f"{name} has joined the chat room!"
	broadcast(bytes(msg,FORMAT))
	clients[conn] = name
	
	while True:
		client_msg = conn.recv(HEADER)
		
		if client_msg != (bytes("DISCONNECT_MSG",FORMAT)):
			broadcast(client_msg, name + ": ")
		else:
			conn.close()
			del clients[conn]
			broadcast(bytes(f"{name} has left the chatroom! ",FORMAT))
			break

def broadcast(msg , prefix=""):
	for sock in clients:
		sock.send(bytes(prefix,FORMAT) + msg)

if __name__ == "__main__":
	SERVER.listen(4)
	print("Waiting for connection...")
	ACCEPT_THREAD = threading.Thread(target = accept_connections)
	ACCEPT_THREAD.start()
	ACCEPT_THREAD.join()
	SERVER.close()
