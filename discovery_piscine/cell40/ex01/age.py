#!/usr/bin/env python3
age_input = int(input("Digite sua idade: "))

i = 10
print(f"Sua idade atualmente é {age_input}")
while age_input + i <= 120:
         new_age = age_input + i
         print(f"Em {i} anos, sua idade será: {new_age}")
         i+=10

