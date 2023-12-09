data = [[int(x) for x in line.split(' ')] for line in list(open('input_9.txt'))]
# [line.reverse() for line in data] # Part 2 : reverse list of numbers
total = 0
for seq in data:
    diff_list, diffs = [seq[-1]], [1]
    while any(diffs):
        diffs = []
        for i in range(1, len(seq)):
            diffs.append(seq[i] - seq[i-1])
        diff_list.append(diffs[-1])
        seq = diffs
    for i in range(len(diff_list)-1,0, -1): # traverse list backwards and add n+1 to n 
        diff_list[i-1] += diff_list[i] # in order to predict the next number in the sequence
    total += diff_list[0]
print(f"Total sum: {total}")