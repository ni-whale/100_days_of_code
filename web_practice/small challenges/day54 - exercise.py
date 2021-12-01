import time
# current_time = time.time()
# print(current_time)

def speed_calc_decorator(function):
  def inner():
    current_time = time.time()
    function()
    after_time = time.time()
    result = after_time - current_time
    print(f"{function.__name__} run speed: {result}")
  return inner

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
