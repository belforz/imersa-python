#!/usr/bin/env python3

import sys


if len(sys.argv[1:]) == 0:
    print("None")
    quit()

def downcase_all(variable_upcase):
    print(variable_upcase.lower())

downcase_all(sys.argv[1])

    
    