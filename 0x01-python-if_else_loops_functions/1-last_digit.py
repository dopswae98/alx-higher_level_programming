#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
converted_to_string = str(number)
last_digit_to_int = int(converted_to_string[-1])
if last_digit_to_int > 5:
    message = "and is greater than 5"
elif last_digit_to_int == 0:
    message = "and is 0"
elif last_digit_to_int < 6 and  not 0:
    message = "and is less than 6 and not 0"
print(f"Last digit of {converted_to_string} is {converted_to_string[-1]} {message}")
