from functools import cmp_to_key

# On each line, the calibration value can be found by combining 
# the first digit and the last digit (in that order) 
# to form a single two-digit number
# What is the sum of all of the calibration values?

if __name__ == "__main__":

    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    data = list(open('input_1.txt'))
    data = [l.strip() for l in data]
    
    results = []
    for line in data:
        # first
        positions = len(digits)*[1000]
        for i, digit in enumerate(digits):
            if digit in line:
                positions[i] = line.index(digit)
        first = positions.index(min(positions))

        # last
        positions = len(digits)*[1000]
        for i, digit in enumerate(digits):
            start_ix = 0
            while digit in line[start_ix:]:
                positions[i] = line.index(digit, start_ix)
                start_ix = positions[i] + 1
        try:
            last = positions.index(max([p for p in positions if p < 1000]))
        except ValueError as e:
            print(f"Line: {line}")
            print(f"Positions: {positions}")
            print(f"Max-arg: {[p for p in positions if p < 1000]}")
            raise e

        i_first, i_last = digits.index(digits[first]), digits.index(digits[last])
        val = int(values[i_first] + values[i_last])
        print(f"First: {digits[first]}, Last: {digits[last]}, Value: {val}")
        results.append(val)
    print(f"Sum: {sum(results)}")
