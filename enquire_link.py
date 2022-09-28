#!/usr/bin/env python

from struct import pack
from random import randint

def enquire_link():
#f=open(r'/home/ipsm/Py_Scripts/SMPP_Client/send','a+')
    command_length=16
    command_id=0x00000015
    command_status=0x00000000
    sequence_number=randint(1,65535)
    data=pack('!4I',command_length,command_id,command_status,sequence_number)
#data=data+','
#f.write(data)
#f.close()
