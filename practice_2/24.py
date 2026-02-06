n = int(input())
a = input().split()

s = 0

for x in a:
    if int(x) > 0:
        s += 1
        
print(s)
