#!/usr/bin/env python3

input1 = int(input("Digite um numero: \n"))

input2 = int(input("Digite um (segundo) numero: \n"))

multi = input1 * input2

print("O seu resultado é: ", multi)


if multi < 0:
    print("Esse resultado é negativo")
elif multi > 0:
    print("Esse resultado é positivo")
elif multi == 0:
    print("Esse resultado é negativo e positivo")
else:
    print("Sei lá")

