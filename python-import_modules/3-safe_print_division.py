#!/usr/bin/python3
def safe_print_division(a, b):
    result = None

    if b != 0:
        result = a / b

    print("Inside result: {}".format(result))
    return result

# Test the function
a = 10
b = 2
safe_print_division(a, b)

c = 5
d = 0
safe_print_division(c, d)
