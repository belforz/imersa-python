#!/usr/bin/env python3

input1 = int(input("Digite um numero: \n"))

input2 = int(input("Digite um (segundo) numero: \n"))

multi = input1 * input2

print("O seu resultado é: ", multi)


if multi < 0:
    print("Esse resultado é negativo")
    print(f"{input1} x {input2} = {multi}" )
elif multi > 0:
    print("Esse resultado é positivo")
    print(f"{input1} x {input2} = {multi}" )
else:
    print(f"{input1} x {input2} = {multi}" )


