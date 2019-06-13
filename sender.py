#!/usr/bin/python2

import  socket 
recv_ip="127.0.0.1"
recv_port=4444  #    0 - 1024  -- you can check free udp port netstat -nulp

#  creating  udp socket
#               ip type v4 ,  uDp  
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while 4 >  3  :
    msg=raw_input("plz  enter your message :   ")
#  sending  data  to target  
    s.sendto(msg,(recv_ip,recv_port)) 
    #  recv data  from  recv  
    print(s.recvfrom(10))




