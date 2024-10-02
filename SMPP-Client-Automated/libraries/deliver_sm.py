from struct import pack, unpack
from .error_codes import error_codes
from .generic_nack import generic_nack
import logging

logger=logging.getLogger(__name__)
    
def deliver_sm(buffer):
    try:
        logger.debug("Length of buffer: {}".format(len(buffer)))
        sequence_number=int("".join([str(i) for i in list(unpack('!I',buffer[12:16]))]))
        index=buffer.find(b'\x00',19)
        originator_address=buffer[19:index].decode()
        index1=buffer.find(b'\x00',(index+3))
        destination_address=buffer[(index+3):index1].decode()
        text_length=int("".join([str(i) for i in list(unpack('>B',buffer[(index1+10):(index1+11)]))]))
        message=buffer[(index1+11):(index1+11+text_length)].decode()
        logger.error("DeliverSM Received")
        logger.info(f"Originator Address: {originator_address}, Destination Address: {destination_address}, Message: {message}")
    except Exception as e:
        logger.error("DeliverSM could not be parsed. Sending Generic Nack.")
        data=generic_nack()
        return data
    data=pack('!4I',int(17),0x80000005,0x00000000,int(sequence_number))
    data=data+b'\x00'
    return data
