import time
import concurrent.futures

start = time.perf_counter()

def do_something(sec):
    print(f'sleeping for {sec} seconds..')
    time.sleep(sec)
    return('slept..')

with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(do_something,1)
    # f2 = executor.submit(do_something,1)

    results = [executor.submit(do_something,1) for _ in range(4)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())



# threads = []
# for _ in range (5):
#     t = threading.Thread(target=do_something,args=[3])
#     t.start()
#     threads.append(t)
    
# #To stop all threads
# for thread in threads:
#     thread.join()


finish = time.perf_counter()
print(f'finished in {round(finish-start,5)} seconds')