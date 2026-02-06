n = int(input())
a = input().split()

max = int(a[0])
s = 1

for i in range(1, n):
    x = int(a[i])
    if x > max:
        max = x
        s = i + 1

print(s)
