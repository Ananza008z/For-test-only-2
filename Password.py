import string
dict = {}
for char in  range(26):
    dict[char+1] = string.ascii_letters[char]
print(dict)
def loop(x, end):
    if x < end:
        A, B, L = [int(c) for c in input('Enter A,B and L ==> ').split()]
        code = [int(c) for c in input('Enter code : ').split()]
        ans_lst = []
        if len(code) == L:
            for k in range(L):
                for i in range(26):
                    if ((A*i)+B)%37 == code[k]:ans_lst.append(dict[i+1])
            print('Your Message is :', ''.join(ans_lst))
            print('\n=====================')
            return loop(x+1)
        else:
            print('Worng Code input')
            return loop(x)
    else: return

N = int(input('Enter Number : '))
loop(0, N)