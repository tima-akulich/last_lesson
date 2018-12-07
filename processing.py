from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Process
import time

from threads import foo_print_a, foo_print_b


def factorial(n):
    result = 1
    for i in range(1, n + 1, 1):
        result *= i
    return result


if __name__ == '__main__':
    # start = time.time()
    # factorial(100000)
    # factorial(100000)
    # print('END:', time.time() - start)

    print('/' * 40)

    start = time.time()
    with ProcessPoolExecutor(4) as pool:
        pool.map(factorial, (100000, ))
        pool.map(factorial, (100000, ))
        pool.map(factorial, (100000, ))
    print('END:', time.time() - start)


