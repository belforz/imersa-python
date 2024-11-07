#!/usr/bin/env python3
import sys

def encontrar_z(frase):
    encontrou_z = False
    for caractere in frase:
        if caractere.lower() == 'z':
            encontrou_z = True
            print("z")
    
    if not encontrou_z:
        print("Não encontrou z")

if len(sys.argv) != 2:
    print("Número de parâmetros inválido")
else:
    encontrar_z(sys.argv[1])

