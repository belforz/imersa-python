#!/usr/bin/env python3


number_input = int(input("Digite um numero até 25: "))

if 1 <= number_input <= 25:

    while  number_input <25:

        number_input += 1
        print("Esse indice atual é: ", number_input)
        

else:
    print("Erro")
