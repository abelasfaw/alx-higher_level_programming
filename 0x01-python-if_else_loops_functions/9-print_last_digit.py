#!/usr/bin/python3
def last_digit(number):
    if number < 0:
        last_digit = ((number * -1) % 10)
    else:
        last_digit = number % 10
    return last_digit
def print_last_digit(number):
    last = last_digit(number)
    print(last, end = "")
    return last
