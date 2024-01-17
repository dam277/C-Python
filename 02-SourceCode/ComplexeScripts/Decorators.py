# def execution(func):
#     def wrapper(*args, **kwargs):
#         print(args, kwargs)
#         print("Executing function:", func.__name__)
#         result = func(*args, **kwargs)
#         print("Function execution complete.")
#         return result
#     return wrapper

# Permision decorator
def permission(permission_required):
    # Decorator function
    def decorator(func, *args, **kwargs):
        # Wrapper function
        def wrapper(test):
            print("Checking permission...")
            if permission_required == "admin":
                print("Permission granted.")
                return func(test)
            else:
                print("Permission denied.")
        return wrapper
    return decorator

# Decorator function
def decorator(func):
    # Wrapper function
    def wrapper(*args, **kwargs):
        # Wrap the function and execute it
        print("Executing function:", func.__name__)
        result = func(*args, **kwargs)
        print("Function execution complete.")
        return result
    return wrapper

@permission("admin")
@decorator
def my_function(test):
    print("Inside my_function")
    return test

print(my_function("test"))
