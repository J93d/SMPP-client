#!/usr/bin/env python

#standard libraries
from struct import unpack
import ipaddress
#custom libraries
from .bind_receiver_resp import bind_receiver_resp
from .bind_transceiver_resp import bind_transceiver_resp
from .bind_transmitter_resp import bind_transmitter_resp
from .cancel_sm_resp import cancel_sm_resp
from .enquire_link_resp import enquire_link_resp
from .query_sm_resp import query_sm_resp
from .replace_sm_resp import replace_sm_resp
from .submit_multi_resp import submit_multi_resp
from .submit_sm_resp import submit_sm_resp
from .unbind_resp import unbind_resp
from .deliver_sm import deliver_sm

import logging
logger = logging.getLogger(__name__)


class smpp_socket:

    def __init__(self, address=(),data=bytearray(),close=0):
        self.address=address
        self.data=data
        self.close=close

    def conn(address):
        import socket
        global sock_conn
        try:
            if ipaddress.ip_address(address[0]).version == 4:
                sock_conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            elif ipaddress.ip_address(address[0]).version == 6:
                sock_conn=socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
            else:
                return "IP format is wrong"
            sock_conn.settimeout(5)
            try:
                sock_conn.connect((address))
                return True
            except Exception as e:
                return e
        except Exception as e:
            return e

    def send_data(data):
        try:
            sock_conn.send(data)
            try:
                buffer=sock_conn.recv(500)
                if len(buffer)>0:
                    while len(buffer) >= 4:
                        packet_length = int.from_bytes(buffer[:4], 'big')
                        packet = buffer[:packet_length]
                        command_id = list(unpack('!I',packet[4:8]))
                        if command_id[0]==2147483649:
                            bind_receiver_resp(packet)          #Done
                            return True
                        elif command_id[0]==2147483650:
                            bind_transmitter_resp(packet)          #Done
                            return True
                        elif command_id[0]==2147483651:
                            query_sm_resp(packet)
                            return True
                        elif command_id[0]==2147483652:
                            submit_sm_resp(packet)
                            return True
                        elif command_id[0]==2147483654:
                            unbind_resp(packet)          #Done
                            return True
                        elif command_id[0]==2147483655:
                            replace_sm_resp(packet)
                            return True
                        elif command_id[0]==2147483656:
                            cancel_sm_resp(packet)
                            return True
                        elif command_id[0]==2147483657:
                            bind_transceiver_resp(packet)          #Done
                            return True
                        elif command_id[0]==2147483669:
                            enquire_link_resp(packet)
                            return True
                        elif command_id[0]==2147483681:
                            submit_multi_resp(packet)
                            return True
                        elif command_id[]==5:
                            delr_data=deliver_sm(packet)
                            socket.conn.send(dlr_data)
                            logger.error("DeliverSM Response sent.")
                        else:
                            return str("Umknown data received")
                        buffer = buffer[packet_length:]
                else:
                    return str("No response received")
            except Exception as e:
                    return e
        except Exception as e:
            return e
    def receive_data():
        try:
            data=sock_conn.recv(1000)
            return data
        except Exception as e:
            return e
    def disconnect(close):
        try:
            sock_conn.close()
        except Exception as e:
            return e
