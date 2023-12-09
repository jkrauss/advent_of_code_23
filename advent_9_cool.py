from itertools import pairwise

data = [[*map(int, line.split())] for line in open('input_9.txt')]


def predict(nums):
    diffs = [b - a for a, b in pairwise(nums)]
    return nums[-1] + (predict(diffs) if any(diffs) else 0)


print('part 1:', sum(map(predict, data)))
print('part 2:', sum(predict(num[::-1]) for num in data))
