n = int(input())
a = input().split()

diana = {}

for i in a:
    i = int(i)
    if i in diana:
        diana[i] += 1
        print("NO")

    else:
        diana[i] = 1
        print("YES")


