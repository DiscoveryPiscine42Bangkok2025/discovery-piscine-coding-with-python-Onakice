#!/usr/bin/env python
inp = int(input("Please tell me your age: "))
print(f"You are currently {inp} years old.")
for i in range(1,4):
    i=i*10
    print(f"In {i} years, you'll be {inp+i} years old.")