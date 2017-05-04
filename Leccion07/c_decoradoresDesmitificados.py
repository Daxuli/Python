"""

"""
import time
import Leccion07.cache as cache  # cambiar si hace falta


def factorial(n):
    """Return n! (the factorial of n): n! = n * (n-1)!"""
    if n < 2:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Return nth fibonacci number: fib(n) = fib(n-1) + fib(n-2)"""
    if n < 2:  # fib(0) = 0; fib(1) = 1; fib(2) = 1  no considera numeros negativos
            return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_cache_v1(n):
    """
    Return nth fibonacci number: fib(n) = fib(n-1) + fib(n-2) using cache if available
    Metodo desaconsejado, ya que si no lo hemos corrido antes tarda como fibonacci y solo guarda fib(n)
    """
    fib = cache.get_key(n)
    if fib is None:
        fib = fibonacci(n)
        cache.set_key(n, fib)
    return fib


def fibonacci_cache_v2(n):
    """Return nth fibonacci number: fib(n) = fib(n-1) + fib(n-2) using cache if available"""
    if n < 2:
        return n
    fib = cache.get_key(n)
    if fib is None:
        fib = fibonacci_cache_v2(n - 1) + fibonacci_cache_v2(n - 2)
        cache.set_key(n, fib)
    return fib


def memoize_any_function(func_to_memoize):
    """
    Return a wrapped version of the function using memoization. 
    Educational only. Mixes results if used on different functions.

    Not to be confused with Memorization

    Memoization or memoisation is an optimization technique used primarily to speed up computer programs by storing 
    the results of expensive function calls and returning the cached result when the same inputs occur again.
    """

    def memoized_version_of_func(n):
        """Wrapper using memoization"""
        res = cache.get_key(n)
        if res is None:
            res = func_to_memoize(n)  # Call the real function
            cache.set_key(n, res)
        return res

    return memoized_version_of_func


@memoize_any_function
def fibonacci_crec(n):
    """"Return nth fibonacci number: fib(n) = fib(n-1) + fib(n-2)"""
    if n < 2:
        return n
    fib1 = 0
    fib2 = 1
    for i in range(2, n+1):
        temp = fib2
        fib2 += fib1
        fib1 = temp
        cache.set_key(i, fib2)
    return fib2


@memoize_any_function
def factorial_cache(n):
    """Return n! (the factorial of n): n! = n * (n-1)!"""
    if n < 2:
        return 1
    return n * factorial(n - 1)

    # funciones
# ********************************************************************************
# ********************************************************************************
print("Factorial:", list(map(factorial, range(10))))
print("Fibonacci:", list(map(fibonacci, range(10))))
print("---------------------------------------------------------------")

# --------------------------------------------------------------------
start = time.time()
fibonacci(35)
print("fib(35):")
print(" -Elapsed time sin cache: %s s" % (time.time() - start))

# Si invertimos el orden de ejecucion entre v1 y v2: v2 sigue siendo instantaneo; v1 ya tiene cache y tb tarda 0
start = time.time()
fibonacci_cache_v1(35)
print(" -Elapsed time con cache v1: %s s" % (time.time() - start))

start = time.time()
fibonacci_cache_v2(35)
print(" -Elapsed time con cache v2: %.6e s" % (time.time() - start))

# Usando decorador sobre fibonacci_crec
start = time.time()
fibonacci_crec(35)
print(" -Elapsed time con decorador: %.6e s" % (time.time() - start))
print("---------------------------------------------------------------")

# --------------------------------------------------------------------
print("calculamos fibonacci con cache")
print("fib(4)=", fibonacci_crec(4))

print("si calculamos factorial con cache")
print("4!=", factorial_cache(4))
print("nos lo da mal, coge el de fibonacci")
