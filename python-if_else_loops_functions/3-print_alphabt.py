#!/usr/bin/python3

for letter in range(97, 123):  # ASCII values for 'a' to 'z'
        if chr(letter) not in ['e', 'q']:
                    print("{}".format(chr(letter)), end="")

