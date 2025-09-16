#!/usr/bin/env python
import sys

count = 0

if len(sys.argv) < 2:
    print("none")
else:
    print(f"parameters: {len(sys.argv)-1}")
    for i in sys.argv[1:]:
        temp = ""
        temp+=i
        for j in temp:
            count+=1
        print(f"{i} : {count}")
        count = 0
