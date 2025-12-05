# Problem 3: Cache Return Values
# Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the functions.

import time

def cache(func):
    cache_result = {}
    def wrapper(*args):
        if args in cache_result:
            return cache_result[args]
        result = func(*args)
        cache_result[args] = result
        return result
    return wrapper

@cache
def long_running_func(a, b):
    time.sleep(4)
    return a + b

print(long_running_func(2, 4))
print(long_running_func(2, 4))
print(long_running_func(4, 4))
print(long_running_func(3, 4))
print(long_running_func(4, 4))
