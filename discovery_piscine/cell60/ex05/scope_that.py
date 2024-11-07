#!/usr/bin/env python3


def add_one(number):
    number += 1
    return number

my_variable = 5

print("Before calling add_one:", my_variable)


add_one(my_variable)

print("After calling add_one:", my_variable)
my_variable = add_one(my_variable)
print(my_variable)
