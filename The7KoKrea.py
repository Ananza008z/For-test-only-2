lst = []
for i in range(9):
    x = int(input())
    lst.append(x)

fake_lst = sum(lst) - 100
for j in range(9):
    for k in range(j+1, 9):
        if lst[j] + lst[k] == fake_lst:
            lst.remove(lst[j])
            lst.remove(lst[k-1])
            break
    if len(lst) < 9:
        break
for a in lst:
    print(a)