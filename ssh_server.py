#!/usr/bin/python3

import  socket
import  time
import  subprocess

#  creating   UDP  socket with  ipv4  &  this is rec side

#socket.socket()   #  by default TCP 

#  to create UDP socket 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#  recv ip and port  
r_ip="192.168.10.100"
r_port=9900

#  now  binding  both  port and ip 
s.bind((r_ip,r_port))

while True:
#  to recv data from sender
	recv_data=s.recvfrom(100)
#  here  recvfrom  will recv  data and ip port of sender 
	print(recv_data[0])   #  this means data
	print(recv_data[1])   #  address of sender 
	print("@@@@@@@@@@@@@@@@@")
	print("sending  output  to sender ")
	result=subprocess.getstatusoutput(recv_data[0])

	#  check the success rate
	if  result[0] ==  0  :

		s.sendto(result[1].encode('ascii'),recv_data[1])  #  sending output to sender 

	else :
		s.sendto("command not found ".encode('ascii'),recv_data[1])  #  sending output to sender 



