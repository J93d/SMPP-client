#!/usr/bin/env python

#def smpp_socket(address=(),data=bytearray(),close=0):
#    import socket
#    if address:
#        try:
#            socket=socket.socket()
#        except:
#            print('Not Connected')
#        
#        try:
#            socket.connect((address))
#            print('Connected')
#        except:
#            print('Connect Failed')
#    elif data:
#        socket.send(data)
#        try:
#            buffer=socket.recv(300)
#        except socket.timeout:
#            print("Timed Out")
#    elif close:
#        socket.close()

class smpp_socket:
    import socket
    def __init__(self, address=(),data=bytearray(),close=0):
        self.address=address
        self.data=data
        self.close=close

    def conn(address):
        global socket
        try:
            socket=socket.socket()
        except:
            print('Not Connected')
        
        try:
            socket.connect((address))
            print('Connected')
        except:
            print('Connect Failed')

    def send_data(data):
        socket.send(data)
        try:
            buffer=socket.recv(300)
        except socket.timeout:
            print("Timed Out")
    
    def disconnect(close):
        socket.close()

