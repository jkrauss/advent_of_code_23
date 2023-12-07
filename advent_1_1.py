import os

find_these = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
replace_these = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def find_first_digit(line):
    found_index = 999999
    found_digit = ''
    for digit in find_these:
        if digit in line:
            ix = line.index(digit)
            if ix < found_index:
                found_index = ix
                found_digit = digit
    found_digit = replace_these[find_these.index(found_digit)]
    if found_digit == '':
        raise ValueError('No digit found')
    return found_digit


def find_last_digit(line):
    found_index = -1
    found_digit = ''
    for digit in find_these:
        if digit in line:
            ix = line.index(digit)
            if ix > found_index:
                found_index = ix
                found_digit = digit
    found_digit = replace_these[find_these.index(found_digit)]
    if found_digit == '':
        raise ValueError('No digit found')
    return found_digit

with open('./advent_1_input.txt') as f:
    content = f.readlines()

    sum, first, last, number = 0,0,0,0
for line in content:
    # find the first and last digit in the line
    first = find_first_digit(line)
    last = find_last_digit(line)
    print(line, first, last, first+last)
    number = int(first+last)
    sum += number
print(sum)