import threading
import time

def get_data(data):
    while True:
        print(f"{threading.current_thread().name} thread started. -- {data}")
        time.sleep(1)


# thr1 = threading.Thread(target=get_data, args=(str(time.time()),), name="thr1")
# thr1.start()

thr2 = threading.Thread(target=get_data, args=(str(time.time()),), name="thr2", daemon=True)
thr2.start()

time.sleep(3)
print("program finished")