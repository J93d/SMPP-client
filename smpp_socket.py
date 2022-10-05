#!/usr/bin/env python

from struct import unpack
from bind_receiver_resp import bind_receiver_resp
from bind_transceiver_resp import bind_transceiver_resp
from bind_transmitter_resp import bind_transmitter_resp
from cancel_sm_resp import cancel_sm_resp
from deliver_sm import deliver_sm
from enquire_link_resp import enquire_link_resp
from query_sm_resp import query_sm_resp
from replace_sm_resp import replace_sm_resp
from submit_multi_resp import submit_multi_resp
from submit_sm_resp import submit_sm_resp
from unbind_resp import unbind_resp


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
            buffer=sock_conn.recv(100)
            length=0
            while length<len(buffer):
                len1=list(unpack('!I',buffer[length:length+4]))[0]
                l=list(unpack('!I',buffer[length+4:length+8]))
                if l[0]==2147483649:
                    bind_receiver_resp(buffer[length:len1])          #Done
                elif l[0]==2147483650:
                    bind_transmitter_resp(buffer[length:len1])          #Done
                elif l[0]==2147483651:
                    query_sm_resp(buffer[length:len1])
                elif l[0]==2147483652:
                    submit_sm_resp(buffer[length:len1])
                elif l[0]==2147483654:
                    unbind_resp(buffer[length:len1])          #Done
                elif l[0]==2147483655:
                    replace_sm_resp(buffer[length:len1])
                elif l[0]==2147483656:
                    cancel_sm_resp(buffer[length:len1])
                elif l[0]==2147483657:
                    bind_transceiver_resp(buffer[length:len1])          #Done
                elif l[0]==2147483669:
                    enquire_link_resp(buffer[length:len1])
                elif l[0]==2147483681:
                    submit_multi_resp(buffer[length:len1])
                elif l[0]==5:
                    deliver_sm(buffer[length:len1])
                else:
                    pass
                length=length+len1+1
            
        except sock_conn.timeout:
            print("Timed Out")
    
    def disconnect(close):
        sock_conn.close()

