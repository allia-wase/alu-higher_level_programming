#!/usr/bin/python3
import sys

# Use the first argument as the number, default to 0
try:
        number = int(sys.argv[1]) if len(sys.argv) > 1 else 0
except ValueError:
        print("Error: Argument must be an integer.")
            sys.exit(1)

            # Print the output
            print(f"{number} Battery street")

