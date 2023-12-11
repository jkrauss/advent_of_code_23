data = list(open('input_10.txt'))

# Find the starting 'S'
x = -1
for i, e in enumerate(data):
    if 'S' in e:
        x = e.index('S')
        y = i
        break
print(f'Start at ({x},{y})')  # 63 118


m = {
    '|': {(0, 1): (0, 1), (0, -1): (0, -1)},
    '-': {(1, 0): (1, 0), (-1, 0): (-1, 0)},
    'L': {(0, 1): (1, 0), (-1, 0): (0, -1)},
    'J': {(0, 1): (-1, 0), (1, 0): (0, -1)},
    '7': {(0, -1): (-1, 0), (1, 0): (0, 1)},
    'F': {(0, -1): (1, 0), (-1, 0): (0, 1)},
}


def step(pos, d):
    old_d = d
    pos = [a_i + b_i for a_i, b_i in zip(pos, d)]
    next = data[pos[1]][pos[0]]
    if next == 'S':
        d = (0, 0)
        angle = 0
    else:
        d = m[next][d]
        angle = (d[0] * old_d[1]) - (d[1] * old_d[0])
    return pos, d, angle


# Part 1
steps = 0
pos = [x, y]
#d = (0, -1)
d = (0, 1)
while True:
    pos, d, _ = step(pos, d)
    if d == (0, 0):
        print(f'Final position: {pos}')
        break
    steps += 1

if steps % 2 == 0:
    print(f'Part 1: {int(steps/2)}')
else:
    print(f'Part 1: {int((steps+1)/2)}')
print('#' * 80)
# Part 2
pos = [x, y]
d = (0, 1)  # original: d = (0, -1)

# First pass: find the path and determine direction of rotation
path = []
total_angle = 0 # positive is left around, negative is right around
while True:
    pos, d, angle = step(pos, d)
    total_angle += angle
    path.append(pos) 
    if d == (0, 0):
        break
# print(f'Final position: {pos}')
# print(f'Total angle: {total_angle}')
# print(f'Path: {path}')

# second pass: walk along the path and "explore" the inner points


def explore(points):
    # print(f'points[-1] : {points[-1]}')
    if data[points[-1][1]][points[-1][0]] != '.' or points[-1] in path:
        return points
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_point = [a_i + b_i for a_i, b_i in zip(points[-1], d)]
        #print(f'new_point: {new_point}')
        if data[new_point[1]][new_point[0]] != '.' or new_point in path or new_point in points:
            continue
        points.append(new_point)
        next = explore(points)
        if next is not None:
            return points + next 
        else:
            return points


pos = [x, y]
d = (0, 1)  # original: d = (0, -1)
result = [] 

while True:
    pos, d, angle = step(pos, d)
    if total_angle> 0:  # left around
        match d:
            case (0, -1):
                dx = (-1, 0)
            case (0, 1):
                dx = (1, 0)
            case (1, 0):
                dx = (0, -1)
            case (-1, 0):
                dx = (0, 1)

    ex = [pos[0]+dx[0], pos[1]+dx[1]]
    #print(f'Pos: {pos}, d: {d}, angle: {angle}, ex: {ex}')
    dupe_result = explore([ex])
    [result.append(x) for x in dupe_result if x not in result] 

    if d == (0, 0):
        break


print(result)
#print(data[ex[1]][ex[0]])