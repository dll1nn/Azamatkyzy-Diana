n = int(input())
a = input().split()

max = int(a[0])

for x in a:
    x = int(x)
    if x > max:
        max = x
        
print(max)