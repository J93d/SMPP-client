#!/usr/bin/env python

from multiprocessing.connection import Listener

listener=Listener(('localhost',9459),authkey=b'password')
conn=listener.accept()
while True:
    msg = conn.recv()
    print(msg)
    # do something with msg
    if msg == 'close':
        conn.close()
        break
listener.close()