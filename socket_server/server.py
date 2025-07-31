

import socket

HOST = '0.0.0.0'
PORT = 5002

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
# 	s.bind((HOST, PORT))
#	s.listen()
#	print(f"Socket server listening on {PORT}")
#	while True:
#		conn, addr = s.accept()
#		with conn:
#			print(f"Connected by {addr}")
#			data = conn.recv(1024)
#			if data:
#				conn.sendall(b"PONG from Socket")

s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)
while True:
	conn, addr = s.accept()
	data = conn.recv(1024)
	if data:
		conn.sendall(b"PONG")
	conn.close()
