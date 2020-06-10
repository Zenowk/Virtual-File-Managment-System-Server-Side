# first of all import the socket library 
import socket
import os.path
from _thread import *
from fileSystem.datStream import datStream	
import pickle		 

# next create a socket object 
s = socket.socket()		 
print ("Socket successfully created")

# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 95				

# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 
s.bind(('', port))		 
print ("socket binded to %s" %(port) )

# put the socket into listening mode 
s.listen(5)	 
print ("socket is listening") 
# a forever loop until we interrupt it or 
# an error occurs 

i=0

def datApi(c):
    ds= datStream() 
    if(os.path.isfile("file.dat")): 
        print("exists")   
        dire = ds.loadData()
        print (dire)
    else:
        dire = 0 
            # send a thank you message to the client. 
    d=c.recv(8192)
    try:
        if(d.decode()=="GET datFile"):
            print(d.decode())
            c.send(pickle.dumps(dire))
            print('Request Serviced')     
    except:    
        if (d != b''):
            
            data=pickle.loads(d)
            ds=datStream()
            ds.dump(data) 
            print('Data Saved!')  
            # Close the connection with the client 
    c.close()
   
while True:
    # Establish connection with client. 
    c, addr = s.accept()	 
    print ('Got connection from', addr )
    start_new_thread(datApi, (c,))
     
   


  
 

