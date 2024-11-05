#!/usr/bin/env python3

number1 = int(input("Digite o primeiro numero: "))
number2 = int(input("Digite o segundo numero: "))

multi = number1 * number2
div = number1 / number2
sum = number1 + number2
minus = number1 - number2

print(f"O resultado dessa aplicação em soma {sum}")
print(f"O resultado dessa aplicação em multiplicação {multi}")
print(f"O resultado dessa aplicação em subtração {minus}")
print("O resultado dessa aplicação em divisão: {:.2f}".format(div))


