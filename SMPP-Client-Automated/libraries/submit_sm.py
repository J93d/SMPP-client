#!/usr/bin/env python

from struct import pack
from random import randint
from time import sleep

from .deliver_sm import deliver_sm
from .smpp_socket import smpp_socket
from .gsm_encoding import gsm_encoding
import logging

logger=logging.getLogger(__name__)

def submit_sm(
        source_addr,
        destination_addr,
        service_type = str(""),
        source_addr_ton = int(0),
        source_addr_npi = int(0),
        dest_addr_ton = int(0),
        dest_addr_npi = int(0),
        e_class = int(0),
        protocol_id = int(0),
        priority_flag = int(0),
        schedule_delivery_time = str(""),
        validity_period = str(""),
        r_dr = int(0),
        replace_if_present_flag = int(0),
        dcs = int(0),
        sm_default_msg_id=int(0),
        payload=str('sar'),
        encoding=str('default'),
        msg=str("Hello World!")
        ):
    
    command_id = 0x00000004
    command_status = 0x00000000
    service_type = service_type.encode()
    source_addr_ton = pack(">B",int(source_addr_ton))
    source_addr_npi = pack(">B",int(source_addr_npi))
    source_addr = source_addr.encode()
    dest_addr_ton = pack(">B",int(dest_addr_ton))
    dest_addr_npi = pack(">B",int(dest_addr_npi))
    destination_addr = destination_addr.encode()
    esm_class = pack(">B",int(e_class))
    protocol_id = pack(">B",int(protocol_id))    
    priority_flag = pack(">B",int(priority_flag))
    schedule_delivery_time = schedule_delivery_time.encode()
    validity_period = validity_period.encode()
    registered_delivery=pack(">B",int(r_dr))
    replace_if_present_flag=pack(">B",int(replace_if_present_flag))
    data_coding=pack(">B",int(dcs))
    sm_default_msg_id=pack(">B",int(sm_default_msg_id))
    payload=payload.lower()
    encoding=encoding.lower()

    msg=msg

    if encoding=="Latin":
        msg_encoded=msg.encode('iso-8859-1')
    elif encoding=="GSM":
        msg_encoded=gsm_encoding(msg)
    elif encoding=="Unicode":
        msg_encoded=msg.encode('utf-16-be')
    else:
        logger.error("Encoding type error.")
    
    #UDH message
    if payload=='udh':                                                         
        if len(msg_encoded)<=152:
            sequence_number=randint(1,65536)
            short_message=msg_encoded
            sm_length=pack(">B",len(short_message))
            command_length=33+len(service_type)+len(source_addr)+len(destination_addr)+len(schedule_delivery_time)+len(validity_period)+len(short_message)
            data=pack('!4I',command_length,command_id,command_status,sequence_number)
            data=(data+service_type+b'\x00'+source_addr_ton+source_addr_npi+source_addr+b'\x00'+dest_addr_ton+dest_addr_npi+destination_addr+b'\x00'+esm_class+protocol_id+priority_flag+schedule_delivery_time+b'\x00'+validity_period+b'\x00'+registered_delivery+replace_if_present_flag+data_coding+sm_default_msg_id+sm_length+short_message)
            if int(r_dr)==1:
                msg_sent=smpp_socket.send_data(data)
                if msg_sent==True:
                    logger.debug('SubmitSM sent successfully')
                else:
                    logger.error('SubmitSM not sent. Reason: {}'.format(msg_sent))
                sleep(5)
                status=deliver_sm()
                if status:
                    logger.debug('DeliverSM Received and Response sent')
                else:
                    logger.error('DeliverSM not received.')
            else:
                msg_sent=smpp_socket.send_data(data)
                if msg_sent==True:
                    logger.debug('SubmitSM sent successfully')
                else:
                    logger.error('SubmitSM not sent. Reason: {}'.format(msg_sent))
        #UDH Multipart    
        elif len(msg_encoded)>152:
            esm_class=pack(">B",(int(e_class)+64))
            sequence_number=randint(1,65536)       
            temp_msg_wrapd=[]

            for i in range(0,len(msg_encoded),152):
                if len(msg_encoded)<(i+152):
                    temp_msg_wrapd.append(msg_encoded[i:])
                else:
                    temp_msg_wrapd.append(msg_encoded[i:(i+152)])

            if len(temp_msg_wrapd)>255:
                logger.error('Too Long Message')
                return None
            udh_length=pack(">B",5)
            ieid=pack(">H",3)
            msg_identifier=pack(">B",randint(0,255))
            for i, short_message in enumerate(temp_msg_wrapd):
                logger.debug(f"Short message: {short_message}")
                sm_length=pack(">B",(len(short_message)+int(6)))

                msg_parts=pack(">B",len(temp_msg_wrapd))
                msg_part_num=pack(">B",(i+1))

                command_length=39+len(service_type)+len(source_addr)+len(destination_addr)+len(schedule_delivery_time)+len(validity_period)+len(short_message)
                data=pack('!4I',command_length,command_id,command_status,sequence_number)
                data=(data+service_type+b'\x00'+source_addr_ton+source_addr_npi+source_addr+b'\x00'+dest_addr_ton+dest_addr_npi+destination_addr+b'\x00'+esm_class+protocol_id+priority_flag+schedule_delivery_time+b'\x00'+validity_period+b'\x00'+registered_delivery+replace_if_present_flag+data_coding+sm_default_msg_id+sm_length+udh_length+ieid+msg_identifier+msg_parts+msg_part_num+short_message)
                msg_sent=smpp_socket.send_data(data)
                if msg_sent==True:
                    logger.debug('SubmitSM sent successfully')
                else:
                    logger.error('SubmitSM not sent. Reason: {}'.format(msg_sent))
                if int(r_dr)==1:
                    logger.info("Waiting for Delivery Report...")
                    sleep(5)
                    for i in range(0,len(temp_msg_wrapd))
                        status=deliver_sm()
                        if status:
                            logger.debug('DeliverSM Received and Response sent')
                        else:
                            logger.error('DeliverSM not received.')
    #SAR Message
    elif payload=='sar':
        if len(msg_encoded)<=252:
            sequence_number=randint(1,65536)
            short_message=msg_encoded
            sm_length=pack(">B",len(short_message))
            command_length=33+len(service_type)+len(source_addr)+len(destination_addr)+len(schedule_delivery_time)+len(validity_period)+len(short_message)
            data=pack('!4I',command_length,command_id,command_status,sequence_number)
            data=(data+service_type+b'\x00'+source_addr_ton+source_addr_npi+source_addr+b'\x00'+dest_addr_ton+dest_addr_npi+destination_addr+b'\x00'+esm_class+protocol_id+priority_flag+schedule_delivery_time+b'\x00'+validity_period+b'\x00'+registered_delivery+replace_if_present_flag+data_coding+sm_default_msg_id+sm_length+short_message)
            msg_sent=smpp_socket.send_data(data)
            if msg_sent==True:
                logger.debug('SubmitSM sent successfully')
            else:
                logger.error('SubmitSM not sent. Reason: {}'.format(msg_sent))
            sleep(5)
            if int(r_dr)==1:                
                status=deliver_sm()
                if status:
                    logger.debug('DeliverSM Received and Response sent')
                else:
                    logger.error('DeliverSM not received.')
        #SAR Multipart
        elif len(msg_encoded)>252:
            sequence_number=randint(1,65536)
            temp_msg_wrapd=[]

            for i in range(0,len(msg_encoded),252):
                if len(msg_encoded)<(i+252):
                    temp_msg_wrapd.append(msg_encoded[i:])
                else:
                    temp_msg_wrapd.append(msg_encoded[i:(i+252)])
            if len(temp_msg_wrapd)>255:
                logger.error('Too Long Message')
                return None
            sar_seq=randint(1,255)
            for i, short_message in enumerate(temp_msg_wrapd):
                sm_length=pack(">B",(len(short_message)))
                ####################################optional parameters################################
                #sar_msg_ref_num
                tag1=pack(">H",524)
                length1=pack(">H",2)
                ref1=pack(">H",sar_seq)
                sar_msg_ref_num=(tag1+length1+ref1)
                #sar_segment_seqnum
                tag2=pack(">H",527)
                length2=pack(">H",1)
                seq2=pack(">B",(i+1))
                sar_segment_seqnum=(tag2+length2+seq2)
                #sar_total_segments
                tag3=pack(">H",526)
                length3=pack(">H",1)
                size3=pack(">B",len(temp_msg_wrapd))
                sar_total_segments=(tag3+length3+size3)

                command_length=49+len(service_type)+len(source_addr)+len(destination_addr)+len(schedule_delivery_time)+len(validity_period)+len(short_message)
                data=pack('!4I',command_length,command_id,command_status,sequence_number)
                data=(data+service_type+b'\x00'+source_addr_ton+source_addr_npi+source_addr+b'\x00'+dest_addr_ton+dest_addr_npi+destination_addr+b'\x00'+esm_class+protocol_id+priority_flag+schedule_delivery_time+b'\x00'+validity_period+b'\x00'+registered_delivery+replace_if_present_flag+data_coding+sm_default_msg_id+sm_length+short_message+sar_msg_ref_num+sar_segment_seqnum+sar_total_segments)        
                msg_sent=smpp_socket.send_data(data)
                if msg_sent==True:
                    logger.debug('SubmitSM sent successfully')
                else:
                    logger.error('SubmitSM not sent. Reason: {}'.format(msg_sent))
                sleep(5)
            if int(r_dr)==1:
                logger.info("Waiting for Delivery Report...")
                for i in range(0,len(temp_msg_wrapd))
                    status=deliver_sm()
                    if status:
                        logger.debug('DeliverSM Received and Response sent')
                    else:
                        logger.error('DeliverSM not received.')
    #Payload
    elif payload=='payload':
        sequence_number=randint(1,65536)
        short_message=msg_encoded
        sm_length=pack(">B",0)
        command_length=37+len(service_type)+len(source_addr)+len(destination_addr)+len(schedule_delivery_time)+len(validity_period)+len(short_message)
        ##################################Payload Parameter##################################
        tag=pack('>H',1060)
        length=pack('>H',len(short_message))
        data=pack('!4I',command_length,command_id,command_status,sequence_number)
        data=(data+service_type+b'\x00'+source_addr_ton+source_addr_npi+source_addr+b'\x00'+dest_addr_ton+dest_addr_npi+destination_addr+b'\x00'+esm_class+protocol_id+priority_flag+schedule_delivery_time+b'\x00'+validity_period+b'\x00'+registered_delivery+replace_if_present_flag+data_coding+sm_default_msg_id+sm_length+tag+length+short_message)
        msg_sent=smpp_socket.send_data(data)
        if msg_sent==True:
            logger.debug('SubmitSM sent successfully')
        else:
            logger.error('SubmitSM not sent. Reason: {}'.format(msg_sent))
        sleep(5)
        if int(r_dr)==1:
            status=deliver_sm()
            if status:
                logger.debug('DeliverSM Received and Response sent')
            else:
                logger.error('DeliverSM not received.')
    else:
        logger.error("Payload type error.")
