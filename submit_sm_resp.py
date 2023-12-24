from email import message
from struct import pack, unpack
from error_codes import error_codes
import logging

logger=logging.getLogger(__name__)

def submit_sm_resp(buffer):
    l=list(unpack('!I',buffer[8:12]))
    status=error_codes(int(l[0]))
    sequence=int(list(unpack('!I',buffer[12:16]))[0])
    message_id=buffer[16:].decode()
    logger.info("Status: {}, Sequence: {}, Message ID: {}".format(status,sequence,message_id))