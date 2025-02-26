import time
from threading import Thread, BoundedSemaphore, currentThread
from random import randint

max_connections = 5
pool = BoundedSemaphore(max_connections)

def thread_t():
    spl = randint(1, 6)
    with pool:
        print(f"{currentThread().name} - sleeping for {spl} seconds ")
        time.sleep(spl)


for i in range(20):
    Thread(target=thread_t).start()