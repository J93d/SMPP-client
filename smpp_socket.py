#!/usr/bin/env python

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
        from struct import unpack
        sock_conn.send(data)
        try:
            buffer=sock_conn.recv(100)
            l=list(unpack('!I',buffer[4:8]))
            if l[0]==‭2147483649‬,‭2147483650‬,‭2147483651,‭2147483652,‭2147483654,‭2147483655
        except sock_conn.timeout:
            print("Timed Out")
    
    def disconnect(close):
        sock_conn.close()

