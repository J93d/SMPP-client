#!/usr/bin/env python

from multiprocessing.connection import Listener

def receiver():
    conn=Listener(('localhost',5000))
    buffer=bytearray()
    print('Test')
    while len(buffer)<25:
        print(len(buffer))
        client = conn.accept()
        buffer = client.recv()
        print(buffer)
    return buffer

def main():
    print('test1')
    test=receiver()
    print(test)

if __name__=="__main__":
    main()