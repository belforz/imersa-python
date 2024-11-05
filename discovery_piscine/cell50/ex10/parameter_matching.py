#!/usr/bin/env python3



def parameter_matching(parameter, valid_values=[0,1]):
    try:
        parameter = int(parameter)
    except ValueError:
        print("Por favor, digite um número inteiro.")
        return

    
    if parameter == 0:
        print("Bom trabalho!")
    elif parameter == 1:
        print("Não é isso, desculpe!")
    else:
        print("Nada")

parameter_entry = int(input("Digite um argumento de 0 ou 1: "))

parameter_matching(parameter_entry,valid_values=[0,1])