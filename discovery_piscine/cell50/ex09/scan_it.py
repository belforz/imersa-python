#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 3:
    print("None")
    quit()

variable_one = sys.argv[1]
variable_two = sys.argv[2]
matches = re.findall(re.escape(variable_one), variable_two)

if matches:
    print(len(matches))
    
else:
    print("None")
    
    