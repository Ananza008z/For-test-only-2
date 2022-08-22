import random

def bin(lst1, req):
    lst1.sort()
    print(lst1)
    L, R = 0, len(lst1)-1
    while L <= R:
        mid = int((L+R)/2)
        if req == lst1[mid]: return 'Found at', mid, lst1[mid]
        elif req < lst1[mid]: R = mid -1
        elif req > lst[mid]: L = mid + 1
    return 'What is that Number...?'
lst = [1, 45, 23, 64, 34, 75, 34, 13, 86, 67]
num1 = int(input())
sorted = (bin(lst, num1))
print(sorted)