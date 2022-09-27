#!/usr/bin/env python
import asyncio
import socket
import sys
import sys,os

from generic_nack import *
from bind_receiver import *  
from bind_transmitter import *
from query_sm import *
from submit_sm import *
from deliver_sm import *
from unbind import *
from replace_sm import *
from cancel_sm import *
from bind_transceiver import *
#from enquire_link import *
from submit_multi import *
from data_sm import *
from error_response import *
from submit_sm_load import *




def main():
    n,n1=0,0

    print('Welcome to SMPP Client!\n')        
    try:
        socket1=socket.socket()
    except:
        print('Socker Error')
    
    while n1<=0:
        try:
            host=input('Enter the IP address: ')
            port=input('Enter the port: ')
            socket1.connect((host,int(port)))
            print('Connected')
            n1+=1
        except:
            print('Connect Failed')
        
    while n<=0:
            
        print('1. Select 1 for Bind as Receiver.\n2. Select 2 for Bind as Transmitter.\n3. Select 3 for Bind as Transreceiver.\n4. Select 4 to Send SubmitSM\n5. Select 5 to Exit.')
        option=input()
        
        if int(option)==1:
            bind_receiver(socket1)
        elif int(option)==2:
            bind_transmitter(socket1)
        elif int(option)==3:
            bind_transceiver(socket1)
        elif int(option)==4:
            print('1. Select 1 to send to single recipient.\n2. Select 2 to multiple recipient')
            temp=(input())
            if temp=='1':
                submit_sm(socket1)
            elif temp =='2':
                submit_sm_load(socket1)
        elif int(option)==5:
            unbind(socket1)
            socket1.close()
            n+=1
        else:
            print("Wrong Input")

if __name__ == "__main__":
    main()