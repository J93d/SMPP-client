#!/usr/bin/env python

from struct import pack
from random import randint
from .smpp_socket import smpp_socket
import logging

logger=logging.getLogger(__name__)

def enquire_link():
    command_length=16
    command_id=0x00000015
    command_status=0x00000000
    sequence_number=randint(1,65535)
    data=pack('!4I',command_length,command_id,command_status,sequence_number)
    el_sent=smpp_socket.send_data(data)
    if el_sent==True:
        logger.debug('Enquire Link sent successfully')
    else:
        logger.error('Enquire Link not sent. Reason: {}'.format(el_sent))