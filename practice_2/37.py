n = int(input())

diana = {}

for i in range(n):
    x = input()
    if x in diana:
        diana[x] += 1
    else:
        diana[x] = 1

s = 0
for x in diana:
    if diana[x] == 3:
        s += 1

print(s)
