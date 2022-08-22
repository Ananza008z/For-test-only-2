import math

n = int(input('Enter Number : '))
taxi = []
for customer in range(n):
    a = str(input(f'Enter taxi{customer+1} : '))
    taxi.append(a)
ans_lst = []
for cal in range(n):
    conv = str(taxi[cal])
    if int(taxi[cal][len(taxi[cal])-1]) < 5:
        conv = conv.replace(conv[len(conv)-1], '0', 1)
        ans_lst.append(conv)
    elif int(taxi[cal][len(taxi[cal])-1]) == 5:
        ans_lst.append(taxi[cal])
    elif int(taxi[cal][len(taxi[cal])-1]) > 5:
        taxi[cal] = int((math.ceil(int(taxi[cal])/10))*10)
        ans_lst.append(taxi[cal])

print('\n=====================\n')
for show in range(len(ans_lst)):
    print(f'Taxi Fee{show+1} is :',end = ' ')
    print(ans_lst[show])