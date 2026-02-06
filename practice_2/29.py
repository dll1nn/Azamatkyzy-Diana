n = int(input())
a = input().split()
s=[]
max = int(a[0])
min = int(a[0])

for x in a:
    x = int(x)
    if max < x:
        max = x
    elif min > x:
        min = x

for x in a:
    x = int(x)
    if x == max:
        x = min
    s.append(x)
    
for x in s:
    print(x, end=" ")
