from time import time
from multiprocessing import cpu_count
def work(number):
    res = []
    for i in range(number):
        if not number%(i+1):
            res.append(i+1)
    #print(res)
    return res


def factorize(*number):
    res = []
    for ch in number:
        print (f'{ch}::')
        res.append(work(ch))
    return res
    raise NotImplementedError() # Remove after implementation

print(f'CORE: {cpu_count()}')
start=time()
a, b, c, d  = factorize(128, 255, 99999, 10651060)
finish=time()
print(f'Time::{finish-start}')

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

