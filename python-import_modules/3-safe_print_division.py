#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        if result is not None:
            print("{} / {} = {}".format(a, b, result))

# Test the function
a = 10
b = 2
safe_print_division(a, b)

c = 5
d = 0
safe_print_division(c, d)
