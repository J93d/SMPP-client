#!/usr/bin/env python

from time import sleep
import os
import sys
import logging
from logging.handlers import RotatingFileHandler
import logging.config
import select
import openpyxl

from .libraries.bind_receiver import bind_receiver  
from .libraries.bind_transmitter import bind_transmitter
from .libraries.query_sm import query_sm
from .libraries.submit_sm import submit_sm
from .libraries.unbind import unbind
from .libraries.replace_sm import replace_sm
from .libraries.cancel_sm import cancel_sm
from .libraries.bind_transceiver import bind_transceiver
from .libraries.submit_multi import submit_multi
from .libraries.data_sm import data_sm
from .libraries.submit_sm_load import submit_sm_load
from .libraries.smpp_socket import smpp_socket
from .libraries.enquire_link import enquire_link

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
        while n > 0:
            try:
                workbook = openpyxl.load_workbook('Testcases.xlsx')
            except Exception as e:
                logger.error(f"Opening Workbook failed with exception: {e}")

            sheet = workbook["Sheet1"]
            headers = [cell.value for cell in sheet[1][1:]]
            for row_index, cell in enumerate(sheet.iter_rows(min_row=2, min_col=1, values_only=True), start=2):
                print(f"{row_index}: {cell[0]}")

            
    except KeyboardInterrupt:
        try:
            smpp_socket.disconnect(close=1)
            sys.exit(1)
        except Exception as e:
            logger.warning("Exception in socket disconnection: {}".format(e))

