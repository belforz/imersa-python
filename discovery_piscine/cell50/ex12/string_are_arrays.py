#!/usr/bin/env python3

def encontrar_z(frase):
  encontrar_z = False

  for caractere in frase:
    if caractere.lower() == 'z':
      encontrar_z = True
      print(caractere)
      
    
    if not encontrar_z:
      print("Não encontrou z")
frase_input = input("Digite a frase que contenha Z para a exibição de z's: ")
encontrar_z(frase_input)
    

