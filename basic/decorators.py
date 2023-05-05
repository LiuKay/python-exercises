def my_decorator(func):
    def wrapper():
        print("before func")
        func()
        print("after func")
    return wrapper


@my_decorator
def my_function():
    print("func is invoked!")



def memorize(func):
    cache={}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper
    
@memorize
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
    
my_function() # no args
print(fibonacci(10)) # with args