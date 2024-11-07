#!/usr/bin/env python3
# def tabuada_completa_while():
#   """Gera a tabuada completa de 1 a 10 utilizando o loop while."""
#   i = 1
#   while i <= 10:
#     j = 1
#     while j <= 10:
#       print(f"{i} x {j} = {i*j}")
#       j += 1
#     print()
#     i += 1

# tabuada_completa_while()
# numero = 1
# while numero <=10:
#     i = 1 import sys


#     print(f"Tabuado do {numero}: ")
#     while i <=10:
#         resultado = numero * i
#         print(f"{numero} x {i} = {resultado} ")
#         i +=1

#     print()
#     numero +=1


numero = 0
while numero <= 10:
    linha = f"Tabela de {numero}: " + " ".join(str(numero * i) for i in range(11))
    print(linha)
    numero += 1


