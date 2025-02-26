import threading
import time

locker = threading.Lock()
value = 0

def inc_value():
    global value
    while True:
        locker.acquire()
        value += 1
        time.sleep(0.01)
        print(value)
        locker.release()

for _ in range(5):
    threading.Thread(target=inc_value).start()
