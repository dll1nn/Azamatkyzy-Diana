n = int(input())
a = input().split()
s = []

for x in a:
    x=int(x)
    s.append(x)
s.sort(reverse=True)

for x in s:
    print(x, end=" ")