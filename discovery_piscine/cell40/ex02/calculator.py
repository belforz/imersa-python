#!/usr/bin/env python3

number1 = input("Digite o primeiro número: ")
number2 = input("Digite o segundo número: ")

multi = int(number1) * int(number2)
div = int(number1) / int(number2)
soma = int(number1) + int(number2)
minus = int(number1) - int(number2)

print(f"O resultado dessa aplicação em soma: {soma}")
print(f"O resultado dessa aplicação em multiplicação: {multi}")
print(f"O resultado dessa aplicação em subtração: {minus}")
print("O resultado dessa aplicação em divisão: {:.2f}".format(div))

