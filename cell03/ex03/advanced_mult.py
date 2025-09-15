#!/usr/bin/env python
for i in range(11):
    print(f"Table de {i}: ", end="")
    for j in range(11):
        print(f"{i*j}", end=" ")
    print()