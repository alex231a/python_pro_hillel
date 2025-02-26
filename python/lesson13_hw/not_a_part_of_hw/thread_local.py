import threading
import time

data = threading.local()

def get():
    print(data.value)

def t1():
    data.value = 111
    get()

def t2():
    data.value = 222
    get()

t1 = threading.Thread(target=t1).start()
t2 = threading.Thread(target=t2).start()
