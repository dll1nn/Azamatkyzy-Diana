import sys

input = sys.stdin.readline

n = int(input())
diana = {}

for c in range(n):
    p = input().split()

    if p[0] == "set":
        diana[p[1]] = p[2]
    else:  
        k = p[1]
        if k in diana:
            print(diana[k])
        else:
            print(f"KE: no key {k} found in the document")
