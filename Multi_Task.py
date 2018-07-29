import time
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool

def add(x, y):
    print(datetime.now(), "enter add func...")
    time.sleep(2)
    print(datetime.now(), "leave add func...")
    return x+y


def add_wrap(args):
    return add(*args)


if __name__ == "__main__":
    pool = ThreadPool(4) # 池的大小为4
    print(pool.map(add_wrap, [(1,2),(3,4),(5,6)]))
    #close the pool and wait for the worker to exit
    pool.close()
    pool.join()