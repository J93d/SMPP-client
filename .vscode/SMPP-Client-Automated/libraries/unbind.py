#!/usr/bin/env python

from struct import pack
from random import randint

from smpp_socket import smpp_socket
import logging

logger=logging.getLogger(__name__)

def unbind():
    command_length=16
    command_id=0x00000006
    command_status=0x00000000
    sequence_number=randint(1,4294967294)
    data=pack('!4I',command_length,command_id,command_status,sequence_number)
    unbind_sent=smpp_socket.send_data(data)
    if unbind_sent==True:
        logger.debug('Unbind sent successfully')
    else:
        logger.error('Unbind not sent. Reason: {}'.format(unbind_sent))