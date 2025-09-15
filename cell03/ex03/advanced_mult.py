#!/usr/bin/env python
import sys

i = 0
if len(sys.argv) > 1:
    print("none")
else :
    while i <= 10 :
        print(f"Table de {i}: ", end="")
        j = 0
        while j <= 10:
            print(f"{i*j}", end=" ")
            j+=1
        print()
        i+=1