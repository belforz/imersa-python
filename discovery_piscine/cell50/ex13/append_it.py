#!/usr/bin/env python3
import sys

args_com_ism = []

if len(sys.argv) <= 1:
    print("none")
else:
    for palavra in sys.argv[1:]:
        if not palavra.endswith("ism"):
            palavra_com_ism = palavra + "ism"
        else:
            palavra_com_ism = palavra
        if palavra_com_ism not in args_com_ism:
            print(palavra_com_ism)
            args_com_ism.append(palavra_com_ism)

