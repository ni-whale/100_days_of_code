def loggin_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {function(*args)}")

    return wrapper


@loggin_decorator
def a_function(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


a_function(1, 2, 3, 4, 5)
