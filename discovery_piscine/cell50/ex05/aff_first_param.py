#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
    print("None")
    quit()
else:
    save_len = sys.argv[1:]
    print("A sua string: ", save_len)
