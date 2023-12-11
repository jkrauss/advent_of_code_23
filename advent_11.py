from itertools import combinations

rows = [r.strip() for r in list(open('input_11.txt'))]


def expand(lst):
    all_empty = []
    for i, r in enumerate(lst):
        if len(set(r)) == 1:
            all_empty.append(i)
    return all_empty


all_empty_rows = expand(rows)
cols = list(zip(*rows))
all_empty_cols = expand(cols)

# print(f'Empty rows: {all_empty_rows}')
# print(f'Empty cols: {all_empty_cols}')

# retrieve coordinates of all '#'s
coords = []
for i, r in enumerate(rows):
    for j, c in enumerate(r):
        if c == '#':
            coords.append((j, i))


def space_dist(c1, c2, expanse=1
               , expanded_rows=all_empty_rows
               , expanded_cols=all_empty_cols):
    """Return the distance between two coordinates in space"""

    # "space expansion"
    y_between = [*range(c1[1], c2[1])] if c1[1] < c2[1] else [*range(c2[1], c1[1])]
    expand_y = [y for y in y_between if y in expanded_rows]
    x_between = [*range(c1[0], c2[0])] if c1[0] < c2[0] else [*range(c2[0], c1[0])]
    expand_x = [x for x in x_between if x in expanded_cols]

    x_dist = abs(c2[0] - c1[0]) + len(expand_x) * (expanse-1)
    y_dist = abs(c2[1] - c1[1]) + len(expand_y) * (expanse-1)
    return x_dist + y_dist


# Part 1
# Sum the distances between all pairs of coordinates
sum_of_distances = 0
for c1, c2 in combinations(coords, 2):
    sum_of_distances += space_dist(c1, c2, expanse=2)

print(f'Part 1: {sum_of_distances}')
# Part 1: 9233514

# Part 2
# Sum the distances between all pairs of coordinates
sum_of_distances = 0
for c1, c2 in combinations(coords, 2):
    sum_of_distances += space_dist(c1, c2, expanse=1000000)

print(f'Part 2: {sum_of_distances}')
# Part 2: 363293506944






