n = int(input())
a = list(map(int, input().split()))

m = 0
s = a[0]

for x in a:
    c = 0
    for y in a:
        if y == x:
            c += 1

    if c > m or (c == m and x < s):
        m = c
        s = x

print(s)
