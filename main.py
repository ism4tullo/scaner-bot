import socket

def scan(ip, port):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	if client.connect_ex((ip, port)):
		pass
	else:
		print(port - 'open')

ip = socket.gethostbyname("tuit.ru")
for i in range(80):
	scan(ip, i)