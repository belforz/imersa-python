#!/usr/bin/env python3

import math

number_input = float(input("Digite um número: "))

if 0 <number_input <1:
     rounded_number = 1

elif number_input - math.floor(number_input) <= 0.5:
    rounded_number = math.floor(number_input)
else:
    rounded_number = math.ceil(number_input)

print(f"Esse número sem as vírgulas é {rounded_number}")


