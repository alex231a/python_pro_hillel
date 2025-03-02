import threading
import time
from queue import Queue

counter = [0]
lock = threading.Lock()
queue = Queue()
queue.put(0)

def inc():
    lock.acquire()
    c = counter[0]
    time.sleep(0.1)
    counter[0] = c + 1
    lock.release()

def inc_queue():
    c = queue.get()
    time.sleep(0.1)
    queue.put(c+1)

# threads = []
# for _ in range(10):
#     thread = threading.Thread(target=inc, daemon=True)
#     threads.append(thread)
#     thread.start()
# for thread in threads:
#     thread.join()
# print(counter)

threads = []
for _ in range(100):
    thread = threading.Thread(target=inc_queue, daemon=True)
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()

print(queue.qsize())
print(queue.get_nowait())

print(time.perf_counter())