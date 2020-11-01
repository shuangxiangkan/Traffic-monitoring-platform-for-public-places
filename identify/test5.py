from threading import Lock, Thread
import time

lock = Lock()
g = 0


def add_one():
    """
    Just used for demonstration. It’s bad to use the ‘global’
    statement in general.
    """
    global g
    while True:
        lock.acquire()
        time.sleep(1)
        g += 1
        print("thread-1:", g)
        lock.release()



def add_two():
    global g
    while True:
        lock.acquire()
        time.sleep(1)
        g += 2
        print("thread-2:",g)
        lock.release()


threads = []
for func in [add_one, add_two]:
    threads.append(Thread(target=func))
    threads[-1].start()

# for thread in threads:
#     """
#     Waits for threads to complete before moving on with the main
#     script.
#     """
    # thread.join()

# print(g)