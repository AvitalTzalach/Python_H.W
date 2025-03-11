import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        total_time = end - start
        print(f"Function '{func.__name__}' took {total_time} seconds to run")
        return result
    return wrapper


@timer_decorator
def my_function(*args, **kwargs):
    time.sleep(1)
    print("finished---")


#my_function()


def cache(cache_dict):
    def decorator(func):
        def wrapper(*args, **kwargs):
            key = f"{func.__name__}{args}"
            if key in cache_dict:
                result = cache_dict[key]
            else:
                result = func(*args, **kwargs)
                cache_dict[key] = result
            return result
        return wrapper
    return decorator

cache_dict = {}

@cache(cache_dict)
@timer_decorator
def fibonacci(n):
    a, b = 0, 1
    time.sleep(2)
    for _ in range(n):
        a, b = b, a + b
    return b

print(fibonacci(1000))
print(fibonacci(1000))
print(fibonacci(30))
print(fibonacci(20))
print(fibonacci(30))