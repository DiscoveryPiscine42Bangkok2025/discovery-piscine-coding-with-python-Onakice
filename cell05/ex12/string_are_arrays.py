#!/usr/bin/env python
import sys

z_out = ""

if len(sys.argv) != 2:
    print("none")
else:
    for i in sys.argv[1]:
        if i == "z":
            z_out+=i
    if z_out == "":
        print("none")
    else: 
        print(z_out)