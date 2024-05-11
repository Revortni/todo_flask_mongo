

def hello_decorator(func):
    def wrapper(*arg, **kwargs):
        print("hello from decorator")
        returned_val = func(*arg, **kwargs)
        print("bye from decorator")

        return returned_val

    return wrapper


@hello_decorator
def bark():
    print("Woof Woof")
    return ":P"


print(bark())
