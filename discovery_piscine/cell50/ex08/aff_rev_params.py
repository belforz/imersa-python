#!/usr/bin/env python3
import sys

if len(sys.argv[1:]) <2 :
    print("None")
    quit()

else:

    invert_case = sys.argv[1:][::-1]
    print(invert_case)