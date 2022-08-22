a = [int(n) for n in input().split()]
a.sort()
a.reverse()
if a[0] == a[1] and a[2] == a[3]:
    print(a[0] * a[2])
elif a[2] == a[1]:
    print(a[2]*a[3])
elif a[2] != a[1]:
    print(a[1] *a[3])
