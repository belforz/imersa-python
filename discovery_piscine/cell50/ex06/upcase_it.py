#!/usr/bin/env python3
import sys

if len(sys.argv[1:]) !=1:
    print("None")
    quit()

else:

    variable_upcase = sys.argv[1]
    print(variable_upcase.upper())