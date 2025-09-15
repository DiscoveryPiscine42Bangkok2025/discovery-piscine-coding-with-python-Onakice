#!/usr/bin/env python
import sys
if len(sys.argv) != 2:
    print("none")
else:
    inp = input("What was the parameter? ")
    if inp == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")