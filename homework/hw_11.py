from datetime import datetime


def decor(func):
    def wrap(*args, **kwargs):
        func(*args, **kwargs)
        print(f"function: {func.__name__}, time of call: {datetime.now()}")

    return wrap


class MyCustomException(Exception):
    pass


try:
    print(1 / 1)
except TypeError:
    raise MyCustomException("Custom exception is occured")


class ConManager:

    def __enter__(self):
        print("=" * 10)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None and issubclass(exc_type, Exception):
            print(exc_type)
            print(exc_val)
            print(exc_tb)
        print("=" * 10)
        return True


with ConManager():
    zhaba

try:
    print("=" * 10)
    print(1 / 0)
except Exception as fail:
    print(fail)
else:
    print("everything is fine")
finally:
    print("=" * 10)
