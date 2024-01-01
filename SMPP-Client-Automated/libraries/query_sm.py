#!/usr/bin/env python

from struct import pack
from random import randint

from .smpp_socket import smpp_socket
import logging

logger=logging.getLogger(__name__)

def query_sm():
    command_id=0x00000003
    command_status=0x00000000
    sequence_number=randint(1,65536)
    
    message_id=input("Enter the messaged ID to be cancelled: ").encode()
    
    o_ton=input('Enter Source Type of Nymber (TON)(Default 1): ')
    
    if o_ton:
        source_addr_ton=pack(">B",int(o_ton))
    else:
        source_addr_ton=pack(">B",1)
        
    o_npi=input('Enter Source Numbering Plan Indicator (NPI)(Default 1): ')
    
    if o_npi:
        source_addr_npi=pack(">B",int(o_npi))
    else:
        source_addr_npi=pack(">B",1)
        
    source_addr=input('Enter Source Address: ').encode()

    command_length=20+len(source_addr)+len(message_id)
    data=pack('!4I',command_length,command_id,command_status,sequence_number)
    data=(data+message_id+b'\x00'+source_addr_ton+source_addr_npi+source_addr+b'\x00')
    enql_sent=smpp_socket.send_data(data)
    if enql_sent==True:
        logger.debug('Bind Receiver sent successfully')
    else:
        logger.error('Bind Receiver not sent. Reason: {}'.format(enql_sent))
