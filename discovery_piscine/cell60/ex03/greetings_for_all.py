#!/usr/bin/env python3

def mk_default():
    print("Olá, caro estranho!")

def mk_string(string):
    print(f"Olá, {string} ")

def greetings_all(foo=""):
    if isinstance(foo,str) and foo:
        mk_string(foo)
    elif foo != "":
        
        print("Erro")
    else: 
        mk_default()

greetings_all("Alexandra")
greetings_all("Wil")
greetings_all("")
greetings_all(42)

