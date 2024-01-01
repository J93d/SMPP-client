#!/usr/bin/env python

from struct import pack
from random import randint

from smpp_socket import smpp_socket

def cancel_sm():
    command_id=0x00000004
    command_status=0x00000000
    sequence_number=randint(1,65536)
    s_type=input("Enter the Service Type (Default NULL): ")
    
    if s_type:
        service_type=s_type.encode()
    else:
        service_type=str('CMT').encode()
    
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
    
    d_ton=input('Enter Destination Type of Nymber (TON)(Default 1): ')
    
    if d_ton:
        dest_addr_ton=pack(">B",int(d_ton))
    else:
        dest_addr_ton=pack(">B",1)
        
    d_npi=input('Enter Destination Numbering Plan Indicator (NPI)(Default 1): ')
    
    if d_npi:
        dest_addr_npi=pack(">B",int(d_npi))
    else:
        dest_addr_npi=pack(">B",1)
        
    destination_addr=input('Enter Destination Address: ').encode()

    command_length=20+len(service_type)+len(source_addr)+len(destination_addr)+len(message_id)
    data=pack('!4I',command_length,command_id,command_status,sequence_number)
    data=(data+service_type+b'\x00'+message_id+b'\x00'+source_addr_ton+source_addr_npi+source_addr+b'\x00'+dest_addr_ton+dest_addr_npi+destination_addr+b'\x00')
    smpp_socket.send_data(data)
