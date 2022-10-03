def logging_decorator(function):
    def wrapper(*args):
        args_collection = []
        for arg in args:
            args_collection.append(arg)
        print(f"{function.__name__} function was called with arguments: {args_collection}, with output: {function()}")
    return wrapper

@logging_decorator
def multiply(a, b, c):
    return a*b*c
@logging_decorator
def sum(a, b):
    return a+b

multiply(1, 2, 3)
sum(2, 2)
