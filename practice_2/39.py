n = int(input())

diana = {}

for i in range(n):
    s, k = input().split()
    k = int(k)

    if s in diana:
        diana[s] += k
    else:
        diana[s] = k

m = sorted(diana)

for a in m:
    print(a, diana[a])
