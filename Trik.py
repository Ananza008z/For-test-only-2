ball = ['1', '0', '0']

readline = [c for c in input()]

for loop1 in readline:
    if loop1 == 'A':
        order1 = [1, 0, 2]
        ball = [ball[n] for n in order1]
    if loop1 == 'B':
        order2 = [0, 2, 1]
        ball = [ball[n] for n in order2]
    if loop1 == 'C':
        order3 = [2, 1, 0]
        ball = [ball[n] for n in order3]

print(int(ball.index('1'))+1)