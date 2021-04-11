import pandas as pandas
from sys import _getframe
import builtins


class MyClass:
    pass


def foo():
    a = 1
    b = MyClass()
    c = [1, 2, 3]
    d = pandas.read_csv("my_file.csv")
    print_vars()


def print_vars():
    frame = _getframe(1)
    local_vars = frame.f_locals
    builtin_types = {getattr(builtins, d) for d in dir(builtins) if isinstance(getattr(builtins, d), type)}
    for var_name, value in local_vars.items():
        print(f"{var_name}: {type(value) in builtin_types}")


if __name__ == "__main__":
    foo()
