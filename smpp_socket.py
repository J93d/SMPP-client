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
        from multiprocessing.connection import Client
        multi_connect=Client(('localhost',9459), authkey=b'passowrd')
        sock_conn.send(data)
        try:
            buffer=sock_conn.recv(300)
            multi_connect.send(buffer)
        except sock_conn.timeout:
            print("Timed Out")
    
    def disconnect(close):
        sock_conn.close()

