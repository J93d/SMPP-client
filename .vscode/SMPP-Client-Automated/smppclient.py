#!/usr/bin/env python


from time import sleep
import os
import sys
import logging
from logging.handlers import RotatingFileHandler

from generic_nack import *
from bind_receiver import *  
from bind_transmitter import *
from query_sm import *
from submit_sm import *
from unbind import *
from replace_sm import *
from cancel_sm import *
from bind_transceiver import *
from submit_multi import *
from data_sm import *
from submit_sm_load import *
from smpp_socket import smpp_socket

log_formatter=logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_file='smpp_client.log'

file_handler=RotatingFileHandler(log_file, maxBytes=1e6, backupCount=3)
file_handler.setFormatter(log_formatter)
file_handler.setLevel(logging.INFO)

logging.basicConfig(
    level=logging.DEBUG
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        file_handler
    ]
)
stream_handler=next(handler for handler in logging.getLogger().handlers if isinstance(handler, logging.StreamHandler))

n=0

print('Welcome to SMPP Client!\n')
host=input('Enter the IP address: ')
port=input('Enter the port: ')

address=(host,int(port))

smpp_socket.conn(address)


        
while n<=0:
        
    print('1. Select 1 for Bind as Receiver.\n2. Select 2 for Bind as Transmitter.\n3. Select 3 for Bind as Transreceiver.\n4. Select 4 to Send SubmitSM\n5. Select 5 to Exit.')
    option=input()
    
    if int(option)==1:
        bind_receiver()
    elif int(option)==2:
        bind_transmitter()
    elif int(option)==3:
        bind_transceiver()
    elif int(option)==4:
        print('1. Select 1 to send to single recipient.\n2. Select 2 to multiple recipient')
        temp=(input())
        if temp=='1':
            submit_sm()
        elif temp =='2':
            submit_sm_load()
    elif int(option)==5:
        unbind()
        sleep(2)
        smpp_socket.disconnect(close=1)
        n+=1
    else:
        print("Wrong Input")
	
