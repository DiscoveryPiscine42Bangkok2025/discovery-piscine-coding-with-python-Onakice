#!/usr/bin/env python
my_arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = []
for i in my_arr:
    if i+2 > 5:
        new_arr.append(i+2)
new_arr = set(new_arr)
print(f"{my_arr}\n{new_arr}")