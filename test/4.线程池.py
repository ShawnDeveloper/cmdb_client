import time
from concurrent.futures import ThreadPoolExecutor

def task(i):
    time.sleep(1)
    print(i)

pool =  ThreadPoolExecutor(10)

for i in range(88):
    pool.submit(task,i)