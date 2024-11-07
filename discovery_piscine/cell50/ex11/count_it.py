#!/usr/bin/env python3

import sys

if len(sys.argv) <= 1:
    print("None")
    quit()

print(f"Parameters: {len(sys.argv) - 1}\n")

for param in sys.argv[1:]:
    print(f"Parameter: {param} (length: {len(param)})\n")
