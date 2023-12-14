from itertools import combinations

#rows = [r.strip() for r in list(open('input_14.txt'))]
rows = list(list(r.strip()) for r in open('input_14.txt'))

# iterate through rows from last to first
# for i,r in enumerate(rows):
#     print(i, r)

def roll_rock(i,j, direction='n'):
    if direction == 'n':
        i_next, j_next = i-1, j
    elif direction == 's':
        i_next, j_next = i+1, j
    elif direction == 'w':
        i_next, j_next = i, j-1
    elif direction == 'e':
        i_next, j_next = i, j+1
    # print('next: ', i_next, j_next)
    if rows[i_next][j_next] == '.':
        rows[i][j] = '.'
        rows[i_next][j_next] = 'O'
#        if i_next >= 0 and j_next >= 0 and i_next < len(rows)-1 and j_next < len(rows[0])-1:
        if i_next in range(len(rows)) and j_next in range(len(rows[0])):
            roll_rock(i_next, j_next, direction)
for glr in range(1000):
    for cnt in range(100):
        for i in range(1, len(rows), 1):
            for j, c in enumerate(rows[i]):
                if c == 'O':
                    roll_rock(i,j, direction='n')
    for cnt in range(100):
        for i in range(1, len(rows), 1):
            for j, c in enumerate(rows[i]):
                if c == 'O':
                    roll_rock(i,j, direction='w')
    # for cnt in range(100):
    #     for i in range(1, len(rows), 1):
    #         for j, c in enumerate(rows[i]):
    #             if c == 'O':
    #                 roll_rock(i,j, direction='s')
    # for cnt in range(100):
    #     for i in range(1, len(rows), 1):
    #         for j, c in enumerate(rows[i]):
    #             if c == 'O':
    #                 roll_rock(i,j, direction='e')



# print('#'*80)
# # iterate through rows from last to first
# for i,r in enumerate(rows):
#     print(i, ''.join([str(e) for e in r]))

# count the number of 'O' in the rows
w_max = len(rows)
print(sum([r.count('O')*(w_max-i) for i,r in enumerate(rows)]))

