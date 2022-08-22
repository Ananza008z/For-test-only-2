import math

level = int(input())
print('-'*int((level-1)/2) + '*' + '-'*int((level-1)/2)) if(level % 2 != 0) else print('-'*int((level-2)/2) + '*' + '-'*int((level-2)/2))
lst = []
ConvLevel = level - 1 if(level%2 == 0) else level
x = ConvLevel + 1
for Top in range((math.floor(ConvLevel/2)), 0, -1):
    sublst = []
    out = '-'*ConvLevel
    sublst.append([c for c in out])
    sublst[0][x-Top-1] = '*'
    sublst[0][Top-1] = '*'
    lst.append(sublst[0])
if level % 2 != 0:
    for toppart in lst:
        print(''.join(toppart))
    for bottompart in range(len(lst)-2, -1, -1):
        print(''.join(lst[bottompart]))
    print('-'*int((level-1)/2) + '*' + '-'*int((level-1)/2))
else:
    for toppart in lst:
        print(''.join(toppart))
    for bottompart in range(len(lst)-1, -1, -1):
        print(''.join(lst[bottompart]))
    print('-'*int(math.ceil(level-1)/2) + '*' + '-'*int(math.ceil(level-1)/2))

 #Too fnk long!!!!   