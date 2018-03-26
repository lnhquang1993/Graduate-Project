from netaddr import IPAddress
import socket
import sys
import ipaddress
import time
import pickle
import SocketServer

#def FindAgent():
#	PORT = 50007		  # Port use to find Agent

"""
	# TCP client
	# Create Socket
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error, e:
		print "Error creating socket: %s" %e
		sys.exit(1)

	# Connect
	try:
		s.connect((HOST, PORT))
		print "Find Client : " + HOST
		s.close()
	except socket.error, e:
		print "Connection error: %s" %e
		pass		#Skip to next host
	"""

	#Find broadcast address

"""IPAddress("255.255.255.0").netmask_bits() 		#Convert Subnet Mask to Prefix Length, Result is 24"""
	#try :
	#	HOST = str(ipaddress.ip_network(u'192.168.10.0/24')[-1])
	#except ValueError as e :
	#	"""e = sys.exc_info()[0]  # Find Exception you need"""
	#	print e

	# UDP client
	#MESSAGE = "Authen"
	#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	#for x in range(0,2):
	#	sock.sendto(MESSAGE, (HOST, PORT))
	#ListenClient()
	

"""def ListenClient():

	# Listen Client sent data
	HOST = socket.gethostbyname(socket.gethostname())
	PORT = 50008
	# TCP socket
	
	# Create Socket
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error, e:
		print "Error creating socket: %s" %e
		sys.exit(1)

	# Bind
	try:
		s.bind((HOST, PORT))
	except socket.error, e:
		print "Error bind: %s" %e
		sys.exit(1)


	# Listen
	try:
		s.listen(10)
	except socket.error, e:
		print "Error listen: %s" %e
		sys.exit(1)

	# Accept connect from client
	try:
		conn, addr = s.accept()
	except socket.error, e:
		print "Error accept: %s" %e
		sys.exit(1)


	# Receive data from client
	try:
		data = conn.recv(4096)
	except socket.error, e:
		print "Error receive: %s" %e
		sys.exit(1)
	temp_list = pickle.loads(data).values()

	NETWORK = temp_list[0]
	FIREWALL = temp_list[1]
	MEMORY = temp_list[2]
	DISK = temp_list[3]
	OS = temp_list[4]
	CPU = temp_list[5]

	return NETWORK[0], FIREWALL, MEMORY[0], DISK[0], OS[0], CPU[0]"""

class MyTCPHandler(SocketServer.BaseRequestHandler):

	def handle(self):
		# self.request is the TCP socket connected to the client
		try:
			self.data = self.request.recv(4096)
		except socket.error, e:
			print "Error receive: %s" %e
			sys.exit(1)

		temp_list = pickle.loads(self.data).values()
		NETWORK = temp_list[0]
		FIREWALL = temp_list[1]
		MEMORY = temp_list[2]
		DISK = temp_list[3]
		OS = temp_list[4]
		CPU = temp_list[5]

		print self.client_address[0]
		print NETWORK[0], FIREWALL, MEMORY[0], DISK[0], OS[0], CPU[0]

	#def cleandata(raw_list):



if __name__ == "__main__":
	HOST = socket.gethostbyname(socket.gethostname())
	PORT = 40009
	server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
	server.serve_forever()
