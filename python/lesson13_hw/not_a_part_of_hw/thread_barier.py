import time
import threading
import random


def barier_t(barrier):
    slp = random.randint(10, 15)
    print(f"Thead {threading.currentThread().getName()} has started in {time.ctime()}")
    time.sleep(slp)

    barrier.wait()
    print(f"Thead {threading.currentThread().getName()} achived barrier at {time.ctime()}")


bar = threading.Barrier(5)
for i in range(10):
    threading.Thread(target=barier_t, args=(bar,), name=f"Thread-{i}").start()