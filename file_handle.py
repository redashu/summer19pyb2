#!/usr/bin/python3

#  creating  a file 
'''
f=open('hello.txt','w')
f.write("hello world this is file writer")
f.write('\n')
f.write("hello world ")
f.close()
#  read operation 
f=open('hello.txt','r')   
data=f.read()
print(data)
f.close()

#   read and write  both    w+
f=open('hello1.txt','w+')  #  this is will create a file first  
f.write("hiiiiiii ")
f.write('\n')
f.write('ok')
f.seek(0)  #  move cursor  position 
print(f.read())
f.close()
'''

#   read and write  both    r+
f=open('hello1.txt','r+')  #  this is will create a file first  
f.write('python')
#print(f.read())
#print("plzzzzzzzzzzz")
#f.write('linux')
#print(f.read())
f.close()

f=open('hello1.txt','a')  #  append only  
f.write('python')
f.close()

f=open('hello1.txt','a+')  #read  and append both
f.write('python')
f.close()
