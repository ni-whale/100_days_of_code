import time


def speed_calc_decorator(function):
    def wrapper_function():
        time_before_start = time.time()
        function()
        time_after_finish = time.time()
        print(f"Time of running '{function.__name__}' = {time_after_finish - time_before_start}")
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
