#!/usr/bin/python2

import  socket 
recv_ip="127.0.0.1"
recv_port=4444  #    0 - 1024  -- you can check free udp port netstat -nulp

#  creating  udp socket
#               ip type v4 ,  uDp  
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  fitting    ip and port  with udp socket 
s.bind((recv_ip,recv_port))

#   recv  data  from  sender  
while  4  >  2  :
    data=s.recvfrom(100)  
    print("message  from sender  ",data[0])
    print("sender IP + port --socket  ",data[1])
    #  reply to sender  
    rply=raw_input("type your rply  : ")
    s.sendto(rply,data[1])


s.close()





