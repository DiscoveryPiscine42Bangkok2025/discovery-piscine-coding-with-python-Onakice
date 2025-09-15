#!/usr/bin/env python
s = input("Enter a number: ").strip()

try:
    x = float(s)
except ValueError:
    print("not a number")
else:
    print("This number is an integer." if x.is_integer() else "This number is an decimal.")