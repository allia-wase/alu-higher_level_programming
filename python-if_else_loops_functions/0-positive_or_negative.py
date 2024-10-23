#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)  # This line generates a random signed number

# Check the value of the number and print the appropriate message
if number > 0:
        print(f"{number} is positive")
    elif number == 0:
            print(f"{number} is zero")
        else:
                print(f"{number} is negative")
