

import sys

args_com_ism = []

for palavra in sys.argv[1:]:
    if not palavra.endswith("ism"):
        palavra_com_ism = palavra + "ism"
    else:
        palavra_com_ism = palavra
        if palavra_com_ism not in args_com_ism:
            args_com_ism.append(palavra_com_ism)


