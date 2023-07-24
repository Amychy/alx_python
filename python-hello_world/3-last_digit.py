#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_absolute = ((abs(number)) % 10)
    if last_absolute == 0:
        last_digit = last_absolute
    else:
        last_digit = last_absolute * -1
else:
    last_digit = (number % 10)

if last_digit > 5:
    size = "and is greater than 5"
elif last_digit == 0:
    size = "and is 0"
elif last_digit < 6:
    size = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, last_digit, size))