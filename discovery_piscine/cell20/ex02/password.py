#!/usr/bin/env python3

import getpass

password_acess = "Python_is_awesome"
password = getpass.getpass("Digite uma senha antes de EXECUTAR: \n" )

if password == password_acess:
    print("Acesso garantido com sucesso")
else:
    print("Acesso negado")

