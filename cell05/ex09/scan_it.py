#!/usr/bin/env python
import sys

def count_overlapping(s, sub):
    if not sub:
        return 0
    count = 0
    i = 0
    while True:
        i = s.find(sub, i)
        if i == -1 :
            break
        count += 1
        i += 1
    return count 

def main():
    
    args = sys.argv[1:]
    if len(args) != 2:
        print("none")
        return

    keyword, text = args
    c = count_overlapping(text, keyword)
    if c == 0:
        print("none")
    else:
        print(c)
    
if __name__ == "__main__":
    main()
