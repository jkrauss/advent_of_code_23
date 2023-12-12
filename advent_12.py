from itertools import combinations

rows = [r.strip() for r in list(open('input_12.txt'))]

for i, r in enumerate(rows[:5]):
    print(i, r)