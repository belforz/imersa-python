#!/usr/bin/env python3


import sys

# Check if there are exactly two arguments
if len(sys.argv) != 3:
    print("none")
else:
    try:
        # Convert arguments to integers
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        
        # Construct the array using range
        array = list(range(start, end + 1))
        
        # Print the array
        print(array)
    except ValueError:
        # If conversion fails, print "none"
        print("none")

