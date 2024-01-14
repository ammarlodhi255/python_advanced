# LEGB: Local, Enclosing, Global, and Bulit-ins. The order of these scopes defines where python tries to find a variable when you try to access it.

# Global and Local:
x = 'global x'

def func():
    # global x
    x = 'local x'
    print(x)

func()
print(x)

# Enclosing:
def outer():
    x = 'outer x'

    def inner():
        # x = 'inner x'
        print(x)

    inner()
    print(x)

outer()


# Built-ins:
import builtins

# Names that are pre-defined in python are called built-ins. You can override these with your definitions.
print(dir(builtins)) 
