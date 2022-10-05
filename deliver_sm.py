from struct import pack, unpack
from error_codes import error_codes
from smpp_socket import *


def deliver_sm(buffer):
    sequence_number=list(unpack('!I',buffer[8:12]))
    #=buffer[]
    

    #DeliverSM resp send
    data=pack('!4I',int(17),0x80000005,0x00000000,sequence_number)
    smpp_socket.send_data(data)