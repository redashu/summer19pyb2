#!/usr/bin/python3

import  socket
import  time

#  creating   UDP  socket with  ipv4  &  this is sender side

#socket.socket()   #  by default TCP 

#  to create UDP socket 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#  recv ip and port  
r_ip="192.168.10.100"
r_port=9900

while True:
#  now sending message to  receiver 
    data=input("plz enter your command  :-- > ")
#  lets convert into byte like  object
    newdata=data.encode('ascii')
    s.sendto(newdata,(r_ip,r_port))
#  here sendto is  sending  data &  ip -port of sender 
    print("###############")
    print("###############")
    print(s.recvfrom(100)[0])
    print("_________________")
    print("_________________")
#  this will recv ack from  receiver 





