#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number == 0:
    message = "is zero"
elif number > 0:
    message = "is positive"
else:
    message = "is negative"
print(f"{number} {message}")
