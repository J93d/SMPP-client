#!/usr/bin/env python

from struct import pack
from random import randint
from textwrap import wrap

from .smpp_socket import smpp_socket
from .gsm_encoding import gsm_encoding

import logging
logger = logging.getLogger(__name__)

def replace_sm():
    command_id=0x00000007
    command_status=0x00000000

    message_id=input("Enter the messaged ID to be replaced: ").encode()
            
    o_ton=input('Enter Source Type of Number (TON)(Default 0): ')
    
    if o_ton:
        source_addr_ton=pack(">B",int(o_ton))
    else:
        source_addr_ton=pack(">B",0)
        
    o_npi=input('Enter Source Numbering Plan Indicator (NPI)(Default 0): ')
    
    if o_npi:
        source_addr_npi=pack(">B",int(o_npi))
    else:
        source_addr_npi=pack(">B",0)
        
    source_addr=input('Enter Source Address: ').encode()
    
    schedule_delivery_time=input('Enter Scheduled Delivery Time(Default NULL): ').encode()
    
    validity_period=input('Enter Validity Period(Default NULL): ').encode()
    
    r_dr=input('Enter Registered Delivery Required(Default 0): ')
    
    if r_dr:
        registered_delivery=pack(">B",int(r_dr))
    else:
        registered_delivery=pack(">B",0)
    
    default_mid=input('Enter Default Message ID(Default 0): ')

    if default_mid:
        sm_default_msg_id=pack(">B",int(default_mid))
    else:
        sm_default_msg_id=pack(">B",0)

    msg=input('Enter your message: ')
    
    if encoding == "Latin":
        msg_encoded=msg.encode('iso-8859-1')
    elif encoding == "GSM":
        msg_encoded=gsm_encoding(msg)
    elif encoding == "Unicode":
        msg_encoded=msg.encode('utf-16-be')
        
    # Only payload message is supported and also DCS option unavailable, hence unicode cannot be properly encoded

    sequence_numer=randint(1,65536)
    short_message=msg_encoded
    sm_length=pack(">B",0)
    command_length=29+len(message_id)+len(source_addr)+len(schedule_delivery_time)+len(validity_period)+len(short_message)
    ###################################payload parameters#######################################
    #message_payload
    tag=pack(">H",1060)
    length=pack(">H",len(short_message))
    data=pack('!4I',command_length,command_id,command_status,sequence_number)
    data=(data+message_id+b'\x00'+source_addr_ton+source_addr_npi+source_addr+b'\x00'+schedule_delivery_time+b'\x00'+validity_period+b'\x00'+registered_delivery+sm_default_msg_id+sm_length+tag+length+short_message)
    msg_sent=smpp_socket.send_data(data)
    if msg_sent is True:
        logger.debug('SubmitSM sent successfully.')
    else:
        logger.error(f'SubmitSM not sent. Reason: {msg_sent}')
