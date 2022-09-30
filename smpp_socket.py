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

    def __init__(self, address=(),data=bytearray(),close=0):
        self.address=address
        self.data=data
        self.close=close

    def conn(address):
        import socket
        global sock_conn
        try:
            sock_conn=socket.socket()
        except:
            print('Not Connected')
        
        try:
            sock_conn.connect((address))
            print('Connected')
        except:
            print('Connect Failed')

    def send_data(data):
        sock_conn.send(data)
        try:
            buffer=sock_conn.recv(300)
        except sock_conn.timeout:
            print("Timed Out")
    
    def disconnect(close):
        sock_conn.close()

