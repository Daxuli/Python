import time


def fibonacci(n):
    if n < 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


start = time.time()
print(fibonacci(5))
print("Ha tardado %.3e s" % (time.time()-start))
