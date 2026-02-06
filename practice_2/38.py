n = int(input())

a = []
for i in range(n):
    a.append(input())

f = {}

for i in range(n):
    if a[i] not in f:
        f[a[i]] = i + 1

u = sorted(f)

for s in u:
    print(s, f[s])
