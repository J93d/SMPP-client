from struct import pack
import logging

logger=logging.getlogger(__name__)

def generic_nack():
    command_id=0x80000000
    command_status=0x00000008
    sequence_number=0x0000000
    command_length=16
    data=pack('!4I',command_length,command_id,command_status,sequence_number)

    return data
