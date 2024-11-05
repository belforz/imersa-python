#!/usr/bin/env python3
age_input = int(input("Digite sua idade: "))


if age_input > 100:
    print("Sinto muito mais sua idade já ultrapassou o limite")

else:
    i = 10
    print(f"Sua idade atualmente é {age_input}")
    while age_input + i <= 120:
         new_age = age_input + i
         print(f"Em {i} anos, sua idade será: {new_age}")
         i+=10

