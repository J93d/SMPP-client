#!/usr/bin/env python

from struct import pack
from random import randint

def unbind(socket):
    command_length=16
    command_id=0x00000006
    command_status=0x00000000
    sequence_number=randint(1,4294967294)
    data=pack('!4I',command_length,command_id,command_status,sequence_number)
    socket.send(data)

    #return data
