#!/usr/bin/env python

from struct import pack
from random import randint

from .smpp_socket import smpp_socket
import logging

logger=logging.getLogger(__name__)

def bind_transceiver():
    command_id=0x00000009
    command_status=0x00000000
    sequence_number=randint(1,65536)
    system_id=input('*Enter SystemID: ').encode('utf-8')
    password=input('*Enter Password: ').encode('utf-8')
    system_type=input('Enter System Type: ').encode('utf-8')
    temp_ton=input('Enter Type of Nymber (TON)(Default 1): ')
    temp_npi=input('Enter Numbering Plan Indicator (NPI)(Default 1): ')
    interface_version=pack(">b",3)
    
    if temp_ton:
        addr_ton=pack(">b",int(temp_ton))
    else:
        addr_ton=pack(">b",1)

    if temp_npi:
        addr_npi=pack(">b",int(temp_npi))
    else:
        addr_npi=pack(">b",1)
    
    command_length=len(system_id)+len(password)+len(system_type)+23
    data=pack('!4I',command_length,command_id,command_status,sequence_number)
    data=(data+system_id+b'\x00'+password+b'\x00'+system_type+b'\x00'+interface_version+addr_ton+addr_npi+b'\x00')
    bind_sent=smpp_socket.send_data(data)
    if bind_sent==True:
        logger.debug('Bind Transceiver sent successfully')
    else:
        logger.error('Bind Transceiver not sent. Reason: {}'.format(bind_sent))