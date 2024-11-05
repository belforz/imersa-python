#!/usr/bin/env python3

name_input = input("Digite algo para mostrar maisculo e minusculo e invertido: \n")
name_input_uppercase = name_input.upper()
name_input_uppercaselow = name_input.lower()
name_input_swapcase = name_input.swapcase()

print(f"Seu nome em Upper é assim: \n {name_input_uppercase} \n e em minusculo é assim:\n {name_input_uppercaselow} e de modo invertido: \n {name_input_swapcase}")