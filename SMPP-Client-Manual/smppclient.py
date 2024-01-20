#!/usr/bin/env python


from time import sleep
import os
import sys
import logging
from logging.handlers import RotatingFileHandler
import logging.config
import select

from libraries.bind_receiver import bind_receiver  
from libraries.bind_transmitter import bind_transmitter
from libraries.query_sm import query_sm
from libraries.submit_sm import submit_sm
from libraries.unbind import unbind
from libraries.replace_sm import replace_sm
from libraries.cancel_sm import cancel_sm
from libraries.bind_transceiver import bind_transceiver
from libraries.submit_multi import submit_multi
from libraries.data_sm import data_sm
from libraries.submit_sm_load import submit_sm_load
from libraries.smpp_socket import smpp_socket
from libraries.enquire_link import enquire_link

logging.config.fileConfig('logging_config.ini')

class FunctionNameFilter(logging.Filter):
    def filter(self, record):
        record.funcName = record.funcName if record.funcName else "N/A"
        return True

logger = logging.getLogger(__name__)
for handler in logger.handlers:
    handler.addFilter(FunctionNameFilter())

def get_user_input(timeout=5):
    #Use select to wait for input or timeout
    rlist,_,_=select.select([sys.stdin],[],[],timeout)

    if rlist:
        user_input=int(input())
        return user_input
    else:
        return None

if __name__=="__main__":
    n=0

    print('Welcome to SMPP Client!\n')
    try:
        host=input('Enter the IP address: ')
        port=input('Enter the port: ')
    except KeyboardInterrupt:
        logger.error("KeyboardInterrupt caught. exiting gracefully.")
        sys.exit(1)

    address=(host,int(port))

    try:
        status_sock_conn=smpp_socket.conn(address)
    except Exception as e:
        logger.error("Socket connection failed with exception: {}".format(e))
        sys.exit(1)

    if status_sock_conn == True:
        logger.info("SMPP Connection successfully created")
    else:
        logger.error("SMPP Connection failed with exception: {}".format(status_sock_conn))
        sys.exit(1)


    try:
        while n<=0:

            print('1. Select 1 for Bind as Receiver.\n2. Select 2 for Bind as Transmitter.\n3. Select 3 for Bind as Transreceiver.\n4. Select 4 to Send SubmitSM\n5. Select 5 to Exit.')
            option=get_user_input()

            while option is None:
                try:
                    enquire_link()
                except Exception as e:
                    logger.error("Exception occurred for EnquiryLink: {}".format(e))
                option=get_user_input()

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
    except KeyboardInterrupt:
        try:
            smpp_socket.disconnect(close=1)
            sys.exit(1)
        except Exception as e:
            logger.warning("Exception in socket disconnection: {}".format(e))

