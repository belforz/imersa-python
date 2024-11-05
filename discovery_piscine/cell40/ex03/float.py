#!/usr/bin/env python3


# isFloatNumber = True
number_input = input('Digite um número: ')

try: 
    valor = float(number_input)
    if valor.is_integer():
        print(f"O numero {number_input} é inteiro")
    else:
        print(f"O numero é float") 
except ValueError:
    print(f"O numero é desconhecido")