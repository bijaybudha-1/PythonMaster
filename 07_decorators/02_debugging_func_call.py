# Problem 2: Debugging Function Call
# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args, **kwargs):
        args_result = ', '.join(str(arg) for arg in args)
        kwargs_result = ', '.join(f'{key}: {value}' for key, value in kwargs.items())
        print(f'Calling {func.__name__}, with args: {args_result} and kwargs: {kwargs_result}')
        return func(*args, **kwargs)
    return wrapper

@debug
def greet(name, greeting='Hello'):
    print(f'{name}, {greeting}')

greet('Bijay', greeting='Hello')
