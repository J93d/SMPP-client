from multiprocessing.connection import Client

c=Client(('localhost',5000))

c.send('what')