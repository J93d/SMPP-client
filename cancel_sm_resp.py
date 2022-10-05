from struct import unpack
from error_codes import error_codes

def cancel_sm_resp(buffer):
    l=list(unpack('!I',buffer[8:12]))
    status=error_codes(int(l[0]))
    print("CancelSM Status: ",status)