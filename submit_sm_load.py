#!/usr/bin/env python

from struct import pack
from random import randint
from textwrap import wrap
import time

def submit_sm_load(socket):
    command_id=0x00000004
    command_status=0x00000000
    s_type=input("Enter the Service Type (Default NULL): ")
    
    if s_type:
        service_type=s_type.encode()
    else:
        service_type=str('CMT').encode()
    
    o_ton=input('Enter Source Type of Nymber (TON)(Default 1): ')
    
    if o_ton:
        source_addr_ton=pack(">b",int(o_ton))
    else:
        source_addr_ton=pack(">b",1)
        
    o_npi=input('Enter Source Numbering Plan Indicator (NPI)(Default 1): ')
    
    if o_npi:
        source_addr_npi=pack(">b",int(o_npi))
    else:
        source_addr_npi=pack(">b",1)
        
    source_addr=input('Enter Source Address: ').encode()
        
    d_ton=input('Enter Destination Type of Nymber (TON)(Default 1): ')
    
    if d_ton:
        dest_addr_ton=pack(">b",int(d_ton))
    else:
        dest_addr_ton=pack(">b",1)
        
    d_npi=input('Enter Destination Numbering Plan Indicator (NPI)(Default 1): ')
    
    if d_npi:
        dest_addr_npi=pack(">b",int(d_npi))
    else:
        dest_addr_npi=pack(">b",1)
        
    #d_addr=input('Enter the csv file path: ')
    #
    #with open(d_addr, 'rb') as f:
    #    reader = csv.reader(f)
    #    num_list = list(reader)
    #    d_addr=num_list[0]
    
    d_addr1=int(input('Enter the start point of range: '))
    d_range=int(input('Enter the range: '))
    tps_in=int(input('Enter the MPS: '))
    load_duration=int(input('Enter the duration for load(in sec): '))
    
    e_class=input('Enter ESM class(Default 0): ')
    
    if e_class:
        esm_class=pack(">b",int(e_class))
    else:
        esm_class=pack(">b",0)
        
    pid=input('Enter Protocol ID(Default 0): ')
    
    if pid:
        protocol_id=pack(">b",int(pid))
    else:
        protocol_id=pack(">b",0)
    
    pri_flag=input('Enter Priority Flag(Default 0): ')
    
    if pri_flag:
        priority_flag=pack(">b",int(pri_flag))
    else:
        priority_flag=pack(">b",0)
    
    schedule_delivery_time=input('Enter Scheduled Delivery Time(Default NULL): ').encode()
    
    validity_period=input('Enter Validity Period(Default NULL): ').encode()
    
    r_dr=input('Enter Registered Delivery Required(Default 0): ')
    
    if r_dr:
        registered_delivery=pack(">b",int(r_dr))
    else:
        registered_delivery=pack(">b",0)
    
    rep_present=input('Set Replace if Present Flag(Default 0): ')
    
    if rep_present:
        replace_if_present_flag=pack(">b",int(rep_present))
    else:
        replace_if_present_flag=pack(">b",0)
    
    dcs=input('Enter Data Coding Scheme(Default 0): ')
    
    if dcs:
        data_coding=pack(">b",int(dcs))
    else:
        data_coding=pack(">b",0)
    
    default_mid=input('Enter Default Message ID(Default 0): ')
    
    if default_mid:
        sm_default_msg_id=pack(">b",int(default_mid))
    else:
        sm_default_msg_id=pack(">b",0)
        
    msg=input('Enter your message: ')
    start_time=time.time()
    #for j in d_addr:
    variable_1=0
    multi_submit=0
    while time.time()<=(start_time+load_duration):
        d_addr=d_addr1
        for j in range(0,d_range,tps_in):
            for x in range(d_addr,d_addr+tps_in):
                d_addr=d_addr+1
                if e_class:
                    if len(msg)<=150:
                        destination_addr=str(x).encode()
                        sequence_number=randint(1,65536)
                        short_message=msg+str(j).encode()
                        sm_length=pack(">b",len(short_message))
                        command_length=33+len(service_type)+len(source_addr)+len(destination_addr)+len(schedule_delivery_time)+len(validity_period)+len(short_message)
                        data=pack('!4I',command_length,command_id,command_status,sequence_number)
                        socket.send(data+service_type+b'\x00'+source_addr_ton+source_addr_npi+source_addr+b'\x00'+dest_addr_ton+dest_addr_npi+destination_addr+b'\x00'+esm_class+protocol_id+priority_flag+schedule_delivery_time+b'\x00'+validity_period+b'\x00'+registered_delivery+replace_if_present_flag+data_coding+sm_default_msg_id+sm_length+short_message)
                        if multi_submit==9:
                            try:
                                socket.recv(300)
                            except socket.timeout:
                                print('Timed Out')
                            multi_submit=0
                        else:
                            multi_submit+=1

                        variable_1=variable_1+1
                    elif len(msg)>150:
                        esm_class=pack(">B",64)
                        destination_addr=str(x).encode()
                        sequence_number=randint(1,65536)
                        temp_msg_wrapd=wrap(msg,width=159)
                        if len(temp_msg_wrapd)>255:
                            print('Too Long Message')
                            return None
                        udh_length=pack(">B",5)
                        ieid=pack(">H",3)
                        msg_identifier=pack(">B",randint(0,255))
                        for i in range(0,len(temp_msg_wrapd)):
                            short_message=temp_msg_wrapd[i].encode()
                            sm_length=pack(">B",(len(short_message)+int(6)))
                            msg_parts=pack(">B",len(temp_msg_wrapd))
                            msg_part_num=pack(">B",(i+1))

                            command_length=39+len(service_type)+len(source_addr)+len(destination_addr)+len(schedule_delivery_time)+len(validity_period)+len(short_message)
                            data=pack('!4I',command_length,command_id,command_status,sequence_number)
                            socket.send(data+service_type+b'\x00'+source_addr_ton+source_addr_npi+source_addr+b'\x00'+dest_addr_ton+dest_addr_npi+destination_addr+b'\x00'+esm_class+protocol_id+priority_flag+schedule_delivery_time+b'\x00'+validity_period+b'\x00'+registered_delivery+replace_if_present_flag+data_coding+sm_default_msg_id+sm_length+udh_length+ieid+msg_identifier+msg_parts+msg_part_num+short_message)#+sar_msg_ref_num+sar_segment_seqnum+sar_total_segments)
                            socket.recv(2024)
                            variable_1=variable_1+1
                else:
                    if len(msg)<=255:
                        destination_addr=str(x).encode()
                        sequence_number=randint(1,65536)
                        short_message=msg.encode()
                        sm_length=pack(">b",len(short_message))
                        command_length=33+len(service_type)+len(source_addr)+len(destination_addr)+len(schedule_delivery_time)+len(validity_period)+len(short_message)
                        data=pack('!4I',command_length,command_id,command_status,sequence_number)
                        socket.send(data+service_type+b'\x00'+source_addr_ton+source_addr_npi+source_addr+b'\x00'+dest_addr_ton+dest_addr_npi+destination_addr+b'\x00'+esm_class+protocol_id+priority_flag+schedule_delivery_time+b'\x00'+validity_period+b'\x00'+registered_delivery+replace_if_present_flag+data_coding+sm_default_msg_id+sm_length+short_message)
                        if multi_submit==9:
                            try:
                                socket.recv(300)
                            except socket.timeout:
                                print('Timed Out')
                            multi_submit=0
                        else:
                            multi_submit+=1

                        variable_1=variable_1+1
                    elif len(msg)>255:
                        destination_addr=str(x).encode()
                        sequence_number=randint(1,65536)
                        temp_msg_wrapd=wrap(msg,width=255)
                        if len(temp_msg_wrapd)>255:
                            print('Too Long Message')
                            return None
                        sar_seq=randint(1,255)
                        for i in range(0,len(temp_msg_wrapd)):
                            short_message=temp_msg_wrapd[i].encode()
                            sm_length=pack(">B",(len(short_message)))
                            ####################################optional parameters################################
                            ##sar_msg_ref_num
                            tag1=pack(">H",524)
                            length1=pack(">H",2)
                            ref1=pack(">H",sar_seq)
                            sar_msg_ref_num=(tag1+length1+ref1)
                            ##sar_segment_seqnum
                            tag2=pack(">H",527)
                            length2=pack(">H",1)
                            seq2=pack(">B",(i+1))
                            sar_segment_seqnum=(tag2+length2+seq2)
                            ##sar_total_segments
                            tag3=pack(">H",526)
                            length3=pack(">H",1)
                            size3=pack(">B",len(temp_msg_wrapd))
                            sar_total_segments=(tag3+length3+size3)

                            command_length=49+len(service_type)+len(source_addr)+len(destination_addr)+len(schedule_delivery_time)+len(validity_period)+len(short_message)
                            data=pack('!4I',command_length,command_id,command_status,sequence_number)
                            socket.send(data+service_type+b'\x00'+source_addr_ton+source_addr_npi+source_addr+b'\x00'+dest_addr_ton+dest_addr_npi+destination_addr+b'\x00'+esm_class+protocol_id+priority_flag+schedule_delivery_time+b'\x00'+validity_period+b'\x00'+registered_delivery+replace_if_present_flag+data_coding+sm_default_msg_id+sm_length+short_message+sar_msg_ref_num+sar_segment_seqnum+sar_total_segments)
                            socket.recv(2024)
                            variable_1=variable_1+1

            #socket.recv(5120)
            time.sleep(1.0-((time.time()-start_time)%1.0))
            #print(1.0-((time.time()-start_time)%1.0))
    print(variable_1)
