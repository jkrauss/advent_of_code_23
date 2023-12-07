import math as m, re

board = list(open('input_4.txt'))
# chars = {(r, c): [] for r in range(140) for c in range(140)
#                     if board[r][c] not in '01234566789.'}
# print(board)
row = board[0]

points = 0
for row in board:
    k,v = row.split(':')
    row = [k]+v.split('|')
    for i in (1,2):
        row[i] = row[i].strip().split(' ')
        row[i] = [x for x in row[i] if x != '' and x != ' ']
        row[i] = [int(x) for x in row[i]]
    points += int(m.pow(2, len([x for x in row[2] if x in row[1]])-1))

print(f"The solution to step 1 is {points}")

res = []
for i, row in enumerate(board):
    k,v = row.split(':')
    row = [i+1, 1]+v.split('|')
    for i in (2,3):
        row[i] = row[i].strip().split(' ')
        row[i] = [x for x in row[i] if x != '' and x != ' ']
        row[i] = [int(x) for x in row[i]]
    row += [len([x for x in row[3] if x in row[2]])]
    res.append(row)
    # row: 0:index, 1:number of cards I own, 2:list of winning numbers
    # , 3:list of numbers I have, 4:number of matches
#print(res[0:1])

count_all = 0
last_index = len(res)-1
for i, row in enumerate(res):
    count_all += row[1]
    print(i, row[1], row[4], count_all)
    print(range(i+1, i+1+row[4]))
    for j in range(i+1, i+1+row[4]):
        if j <= last_index:
            res[j][1] += row[1]

print(f"The solution to step 2 is {count_all}")