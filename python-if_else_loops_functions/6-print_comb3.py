#!/usr/bin/python3

for i in range(1, 10):
        for j in range(i + 1, 10):
                    print("{:02}{:02}".format(i, j), end=", " if not (i == 8 and j == 9) else "")
                    print()  # To add a newline at the end
