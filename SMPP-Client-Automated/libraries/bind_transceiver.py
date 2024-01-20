#!/usr/bin/env python

from struct import pack
from random import randint

from .smpp_socket import smpp_socket
import logging

logger=logging.getLogger(__name__)

def bind_transceiver(system_id,password,system_type=str(""),addr_ton=int(1),addr_npi=int(1)):
    command_id=0x00000009
    command_status=0x00000000
    sequence_number=randint(1,65536)
    system_id=system_id.encode('utf-8')
    password=password.encode('utf-8')
    system_type=system_type.encode('utf-8')
    interface_version=pack(">b",5)
    addr_ton=pack(">b",int(addr_ton))
    addr_npi=pack(">b",int(addr_npi))
    
    command_length=len(system_id)+len(password)+len(system_type)+23
    data=pack('!4I',command_length,command_id,command_status,sequence_number)
    data=(data+system_id+b'\x00'+password+b'\x00'+system_type+b'\x00'+interface_version+addr_ton+addr_npi+b'\x00')
    bind_sent=smpp_socket.send_data(data)
    if bind_sent==True:
        logger.debug('Bind Transceiver sent successfully')
    else:
        logger.error('Bind Transceiver not sent. Reason: {}'.format(bind_sent))