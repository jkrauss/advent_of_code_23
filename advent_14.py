from itertools import combinations

#rows = [r.strip() for r in list(open('input_14.txt'))]
rows = list(list(r.strip()) for r in open('input_14.txt'))

# iterate through rows from last to first
for i,r in enumerate(rows):
    print(i, r)

def roll_rock(i,j, direction='n'):
    if direction == 'n':
        ix, jey = i-1, j
    elif direction == 's':
        ix, jey = i+1, j
    elif direction == 'w':
        ix, jey = i, j-1
    elif direction == 'e':
        ix, jey = i, j+1

    if rows[ix][jey] == '.':
        rows[i][j] = '.'
        rows[ix][jey] = 'O'
        roll_rock(ix, jey, direction)

# iterate through rows from last to first
for i in range(len(rows)-1, 0, -1):
    #print(i, rows[i])
    for j, c in enumerate(rows[i]):
        if c == 'O':
            roll_rock(i,j)
print('#'*80)
# iterate through rows from last to first
for i,r in enumerate(rows):
    print(i, r)

# count the number of 'O' in the rows
w_max = len(rows)
print(sum([r.count('O')*(w_max-i) for i,r in enumerate(rows)]))

