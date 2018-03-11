from netaddr import IPAddress
import socket
import sys
import ipaddress
import time


def FindAgent():
	PORT = 50007          # Port use to find Agent

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
	try :
		HOST = str(ipaddress.ip_network(u'192.168.10.0/24')[-1])
	except ValueError as e :
		"""e = sys.exc_info()[0]  # Find Exception you need"""
		print e

	# UDP client
	MESSAGE = "Authen"
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	for x in range(0,2):
		sock.sendto(MESSAGE, (HOST, PORT))
	ListenClient()

def ListenClient():
	# Listen Client sent data
	HOST = socket.gethostbyname(socket.gethostname())
	PORT = 50008
	# TCP socket
	
	# Create Socket
	print "Create Socket"
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error, e:
		print "Error creating socket: %s" %e
		sys.exit(1)

	# Bind
	print "Bind"
	try:
		s.bind((HOST, PORT))
	except socket.error, e:
		print "Error bind: %s" %e
		sys.exit(1)

	# Listen
	print "Listen"
	try:
		s.listen(10)
	except socket.error, e:
		print "Error listen: %s" %e
		sys.exit(1)
	
	# Accept data from client
	print "Accept data from client"
	try:
		conn, addr = s.accept()
		print conn
		print addr
	except socket.error, e:
		print "Error listen: %s" %e
		sys.exit(1)
	
	s.close()

FindAgent()