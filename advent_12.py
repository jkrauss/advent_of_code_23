from itertools import combinations

rows = [r.strip() for r in list(open('input_12.txt'))]
rows = [r.split(' ') for r in rows]

codes, counts = list(zip(*rows))
counts = [list(map(int, c.split(','))) for c in counts]

# ex, ex_count = '??##?', [4]
# ex, ex_count = '???????##?????#?#?', [9, 6]
# ex, ex_count = '???#??????', [1, 1, 1]

total = 0
for ex, ex_count in zip(codes, counts):
    # print()
    # print(ex, ex_count)

    sub_count = 0
    quest_count = sum(ex_count) - ex.count('#')
    quest_list = [i for i, c in enumerate(ex) if c == '?']
    ex = ex.replace('?', '.')
    quest_combos = [c for c in combinations(quest_list, quest_count)]
    for combo in quest_combos:
        ex_combo = ex
        for pos in combo:
            ex_combo = ex_combo[:pos] + '#' + ex_combo[pos+1:]
        combo_count = ex_combo.split('.')
        combo_count = [len(s) for s in combo_count if s]
        if combo_count == ex_count:
            total += 1
            sub_count += 1
    # print(sub_count)

print(f'Part 1: {total}')