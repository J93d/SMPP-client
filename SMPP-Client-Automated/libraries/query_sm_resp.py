from struct import unpack
from .error_codes import error_codes
import logging

logger=logging.getLogger(__name__)

def query_sm_resp(buffer):
    l=list(unpack('!I',buffer[8:12]))
    status=error_codes(int(l[0]))
    if status=="ESME_ROK":
        logger.info("QuerySM Status: {}".format(status))
    else:
        try:
            sequence_number=int("".join([str(i) for i in list(unpack('!I',buffer[12:16]))]))
            index=buffer.find(b'\x00',16)
            message_id=buffer[16:index].decode()
            index1=buffer.find(b'\x00',index)
            final_date=''
            if (index1-index)>1:
                final_date=buffer[index:index1].decode()
            else:
                pass
            message_state=int("".join([str(i) for i in list(unpack('!I',buffer[(index1+2):(index1+3)]))]))
            message_state_list=["SCHEDULED","ENROUTE","DELIVERED","EXPIRED","DELETED","UNDELIVERABLE"]
            try:
                error_code=int(buffer[(index1+3):(index1+4)].decode())
            except Exception as e:
                error_code=0
            logger.info("Message ID: {}, Final date: {}, Message State: {}, Error Code: {}".format(message_id,final_date,message_state_list[message_state],error_code))
        except Exception as e:
            logger.error("Exception occured: {}".format(e))