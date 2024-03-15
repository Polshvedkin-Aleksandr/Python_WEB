from multiprocessing import Process
import sys
from time import time


def work(params):
    res = []
    for i in range(params):
        if not params%(i+1):
            res.append(i+1)
    print(res)
    return res
def factorize_multi(sp):
    for i in sp:
        pr = Process(target=work, args=(i, ))
        pr.start()
        process.append(pr)
def factorize(number):
    res = []
    for ch in number:
        r=work(ch)
        res.append(r)
    return res


if __name__ == '__main__':
    process = []
    sp=[128, 255, 99999, 10651060]
    start=time()
    factorize_multi(sp)
    finish=time()
    print(f'Time asynchron::{finish-start}')

    [print(pr.exitcode, end=" ") for pr in process]
    print('')
    [pr.join() for pr in process]
    [print(pr.exitcode, end=" ") for pr in process]
    print('')

    start=time()
    factorize(sp)
    finish=time()
    print(f'Time synchron::{finish-start}')
