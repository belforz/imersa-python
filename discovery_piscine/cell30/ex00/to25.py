#!/usr/bin/env python3


number_input = int(input("Digite um número até 25: \n"))

if 1 <= number_input <= 25:
    while number_input <= 25:
        print("Dentro do loop. Esse índice é: ", number_input)
        number_input += 1  
    print("Erro")
