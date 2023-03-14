import time
import threading

start = time.perf_counter()

def do_something(sec):
    print(f'sleeping for {sec} seconds..')
    time.sleep(sec)
    print('slept..')

# do_something()
# do_something()

# t1 = threading.Thread(target=do_something,args=[1])
# t2 = threading.Thread(target=do_something,args=[4])

# t1.start()
# t2.start()

# t1.join()
# t2.join()


threads = []
for _ in range (5):
    t = threading.Thread(target=do_something,args=[3])
    t.start()
    threads.append(t)
    
#To stop all threads
for thread in threads:
    thread.join()


finish = time.perf_counter()
print(f'finished in {round(finish-start,5)} seconds')