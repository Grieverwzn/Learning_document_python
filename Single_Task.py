import time
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool
from functools import partial


def add(x, y):
    print(datetime.now(), "enter add func...")
    time.sleep(2)
    print(datetime.now(), "leave add func...")
    return x+y

print(list(map(add, [1,2,3], [4,5,6])))