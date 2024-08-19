import socket

class reverseShell:
	HOST = "localhost"
	PORT = 5000
	BUFF_SIZE = 2048
	
	def __init__(self):
		#create tcp socket
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM,socket.IPPROTO_TCP)
		self.s.bind((self.HOST, self.PORT))
		# listen connection
		self.s.listen()
		print(f'[+] Listeninng on {self.HOST}:{self.PORT}')
		self.client_socket,self.client_address = self.s.accept()
		print(f'[+] Acceppted connection: {self.client_address[0]}:{self.client_address[1]}')
		self.main()
	def sned_msg(self,msg):
		msg = bytes(f'{msg}','utf-8')
		send = self.client_socket.sendall(msg)
		#return none if sendall if sucessful
		return send

	def recv_msg(self):
		recv = self.client_socket.recv(self.BUFF_SIZE)
		# return value if is a byte object repsenting the data received
		return recv

	def main(self):
		self.send_msg('hello world')
