from math import lcm


if __name__ == "__main__":
    data = list(open('input_8.txt'))

    instructions = data[0].strip()

    nodes = {}
    for line in data[2:]:
        line = line.strip()
        nodes[line[:3]] = {'L': line[7:10], 'R': line[12:15]}

    # Simultaneously start on every node that ends with A. How many steps does it take 
    # before you're only on nodes that end with Z?

    pos = [k for k in nodes.keys() if k[2] == 'A']
    cursor = 0
    steps = 0
    cycles = []
#    while not all([p[2] == 'Z' for p in pos]):
#    while steps < 5:
    while True:
        ins = instructions[cursor]
        for i, p in enumerate(pos):
            pos[i] = nodes[p][ins]
            if pos[i][2] == 'Z':
                cycles.append(steps+1)
        cursor += 1
        if cursor == len(instructions):
            cursor = 0
        steps += 1
        if len(cycles) == len(pos):
            break
    steps = lcm(*cycles)

    print(f"Part 2: {steps}")

#10668805667831
