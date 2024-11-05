#!/usr/bin/env python3
numero = int(input("Digite o um numero de 1 a 10: \n"))
multiplicador = 1 

while multiplicador <=10:
        resultado = numero * multiplicador
        print(f"{multiplicador} x {numero}  =  {resultado}")
        multiplicador += 1

