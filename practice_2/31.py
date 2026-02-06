n, l, r = map(int, input().split())
a = list(map(int, input().split()))

l -= 1
r -= 1

for i in range((r - l + 1) // 2):
    a[l + i], a[r - i] = a[r - i], a[l + i]

for x in a:
    print(x, end=" ")
