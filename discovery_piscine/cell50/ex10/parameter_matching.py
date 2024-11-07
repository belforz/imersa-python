#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("None")
    quit()

parameter = sys.argv[1]


user_input = input("Por favor digite a palavra: ")

if user_input == parameter:
    print("Bom trabalho!")
else:
    print("Não, desculpe...")

