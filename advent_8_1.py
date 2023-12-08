from functools import cmp_to_key


if __name__ == "__main__":
    data = list(open('input_8.txt'))

    instructions = data[0].strip()

    nodes = {}
    for line in data[2:]:
        line = line.strip()
        nodes[line[:3]] = {'L': line[7:10], 'R': line[12:15]}

    pos = 'AAA'
    cursor = 0
    steps = 0
    while pos != 'ZZZ':
#    while steps < 5:
        print(f"{pos} : {instructions[cursor]} --> {nodes[pos][instructions[cursor]]}")
        pos = nodes[pos][instructions[cursor]]
        cursor += 1
        if cursor == len(instructions):
            cursor = 0
        steps += 1
    print(f"Part 1: {steps}")