from __future__ import division
import multiprocessing
import platform
import psutil
import subprocess
import datetime
from uptime import uptime
import threading
import socket
import sys
import argparse


General = subprocess.check_output('systeminfo')[1:].split("\n")
		
def OS():
	print ("Operating System Information")
	oslist = General[0:23] + General[29:31]
	return oslist

def CPU():
	print ("CPU Information")
	lp = str(multiprocessing.cpu_count()) # Logical processors
	cc = str(psutil.cpu_count(logical=False)) # CPU Cores
	cn = platform.processor() # Chip Name
	pn = str(len(list(psutil.process_iter()))) # Processes Numbers
	ut = str(datetime.timedelta(seconds=uptime())) # Uptime
	so = str(threading.active_count()) # Socket
	CPUlist = [lp,cc,cn,pn,ut,so]
	return CPUlist

def DISK():
	print ("DISK Information")
	disk_results = psutil.disk_partitions()
	DISKlist = {}
	id = 0
	for disk in disk_results:
		info = []
		info.append(disk.device)
		info.append(disk.mountpoint)
		info.append(disk.fstype)
		id += 1
		DISKlist.update({str(id):info})
	return DISKlist

def MEMORY():
	mem = psutil.virtual_memory()
	MEMORYlist = []
	for m in mem:
		if m > 100 :
			MEMORYlist.append( str(round(m/1073741824, 2)) + "Gb" )
		else :
			MEMORYlist.append( str(m) + "%")
	return MEMORYlist

def NETWORK():
	netstr = ''
	for interface, snics in psutil.net_if_addrs().items():
		for snic in snics:
			if snic.family == -1 :
				mac = snic.address
			if snic.family == 2 :
				netstr += interface + ',' + snic.address + ',' + snic.netmask + ',' + mac + ','

	netstr = netstr.split(',')[:-1]
	return netstr

def FWStatus() :
	FW = []
	result = subprocess.check_output('netsh advfirewall show allprofiles state').split()
	for x in result[5::6]:
		FW.append(x)
	return FW

def ListenServer():
	# Listen init signal from Server to send data

	HOST = '192.168.10.111'                 # Symbolic name meaning all available interfaces
	PORT = 50007              # Arbitrary non-privileged port

	"""
	# TCP socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(1)
	s.accept()
	s.close()"""

	# UDP Socket
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((HOST, PORT))
	data, addr = s.recvfrom(1024)
	if data == 'Authen':
		SocketConnect(addr[0])

def SocketConnect(HOST):
	# Connect to Server to send data
	print HOST
	PORT = 50008              # The same port as used by the server

	# Create Socket
	print "Create Socket"
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error, e:
		print "Error creating socket: %s" %e
		sys.exit(1)

	# Connect
	print "Connect"
	try:
		s.connect((HOST, PORT))
	except socket.error, e:
		print "Connection error: %s" %e
		sys.exit(1)

	# Send Data
	print "Send Data"
	try:
		s.sendall('Hello, world')
	except socket.error, e:
		print "Error sending data: %s" % e
		sys.exit(1)


	# Close Socket
	s.close()
	print "Close Socket"

#SocketConnect('192.168.10.222')
ListenServer()