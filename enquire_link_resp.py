from struct import unpack
from error_codes import error_codes
import logging

logger=logging.getLogger(__name__)

def enquire_link_resp(buffer):
    l=list(unpack('!I',buffer[8:12]))
    status=error_codes(int(l[0]))
    logger.info("Bind Status: {}".format(status))