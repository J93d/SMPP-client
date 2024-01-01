from struct import pack, unpack
from error_codes import error_codes
from smpp_socket import *
import logging

logger=logging.getLogger(__name__)

def dlr_parser(buffer,i):
    buffer=buffer
    logger.debug("Length of buffer: {}".format(len(buffer)))
    msg_length=int("".join([str(i) for i in list(unpack('!I',buffer[0:4]))]))
    sequence_number=int("".join([str(i) for i in list(unpack('!I',buffer[12:16]))]))
    index=buffer.find(b'\x00',19)
    originator_address=buffer[19:index].decode()
    index1=buffer.find(b'\x00',(index+3))
    destination_address=buffer[(index+3):index1].decode()
    text_length=int("".join([str(i) for i in list(unpack('>B',buffer[(index1+10):(index1+11)]))]))
    message=buffer[(index1+11):(index1+11+text_length)].decode()
    logger.info("Delivery data: {}".format(message))

    data=pack('!4I',int(17),0x80000005,0x00000000,int(sequence_number))
    data=data+b'\x00'
    dlr_resp=smpp_socket.send_data(data)
    logger.debug("Iterator: {}".format(i))  #I tried to return the i value but return is always NoneType leaving this for future changes

    if type(dlr_resp)!=bool or type(dlr_resp)!=str:
        logger.info('Delivery report response sent')
        return True
    else:
        logger.error("Delivery Response not sent. Error: {}".format(dlr_resp))
        return False
    
    i=i+1

    if msg_length<len(buffer):
        logger.debug("In Recurrsion.")
        dlr_parser(buffer[msg_length:],i)
    else:
        logger.debug("Out of Recurssion loop.")
        return True
    
def deliver_sm(buffer):
    buffer=smpp_socket.receive_data()
    i=0
    logger.debug("Buffer type: {}".format(type(buffer)))
    if type(buffer)==bytes:
        status=dlr_parser(buffer,i)
        if status:
            return True
        else:
            return False
    else:
        return False