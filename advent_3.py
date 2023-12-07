
import os

with open('./input_3.txt') as f:
    content = f.readlines()

rows = []
for line in content:
#    line = line.strip()
    rows.append(line)

# all_symbols = ''
# for row in rows:
#     for char in row:
#         if char not in all_symbols:
#             all_symbols += char
# print(all_symbols)



def coord(x, y):
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if x > 139:
        x = 139
    if y > 139:
        y = 139
    return x, y

def part_one():
    valid_symbols = ['-', '#', '=', '*', '+', '@', '$', '&', '/', '%']
    numbers = []
    for row_ix, row in enumerate(rows):
    #    if row_ix > 2:
    #        continue
        number, checklist, in_number = '', [], False
        row_enum = enumerate(row)
        for char_ix, char in row_enum:
            if char.isdigit():
                if not in_number:
                    x, y = coord(row_ix-1,char_ix-1) # topleft
                    checklist.append(rows[x][y])
                    x, y = coord(row_ix,char_ix-1) # left
                    checklist.append(rows[x][y])
                    x, y = coord(row_ix+1,char_ix-1) # bottomleft
                    checklist.append(rows[x][y])
                x, y = coord(row_ix-1,char_ix) # top
                checklist.append(rows[x][y])
                x, y = coord(row_ix+1,char_ix) # bottom
                checklist.append(rows[x][y])
                in_number = True
                number += char
            else:
                if in_number:
                    in_number = False
                    x, y = coord(row_ix+1,char_ix) # top
                    checklist.append(rows[x][y])
                    x, y = coord(row_ix,char_ix) # middle
                    checklist.append(rows[x][y])
                    x, y = coord(row_ix-1,char_ix) # bottom
                    checklist.append(rows[x][y])
                    if any(symbol in checklist for symbol in valid_symbols):
                        numbers.append(number)
                    number = ''
                    checklist = []

    sum_numbers = 0
    for number in numbers:
        sum_numbers += int(number)
    print(f"The solution to part one is: {sum_numbers}")

#part_one()

def count_digits_in_list(list : list):
    count = 0
    for item in list:
        if item.isdigit():
            count += 1
    return count

def part_two():

    gear = '*'
    total = 0
    for row_ix, row in enumerate(rows):
        # if row_ix > 5:
        #     continue
        checklist = []
        row_enum = enumerate(row)
        for char_ix, char in row_enum:
            if char==gear:
                # first determine if we have at least 2 digits in direct vicinity
                x, y = coord(row_ix-1,char_ix-1) # topleft
                checklist.append(rows[x][y])
                x, y = coord(row_ix,char_ix-1)
                checklist.append(rows[x][y])
                x, y = coord(row_ix+1,char_ix-1)
                checklist.append(rows[x][y])
                x, y = coord(row_ix-1,char_ix)
                checklist.append(rows[x][y])
                x, y = coord(row_ix+1,char_ix)
                checklist.append(rows[x][y])
                x, y = coord(row_ix-1,char_ix+1)
                checklist.append(rows[x][y])
                x, y = coord(row_ix,char_ix+1)
                checklist.append(rows[x][y])
                x, y = coord(row_ix+1,char_ix+1)
                checklist.append(rows[x][y])
                n_digits = count_digits_in_list(checklist)
                if n_digits > 1:
                    # now we can start looking for the number
                    print(f"Found a potential gear at {row_ix}, {char_ix}, with {n_digits} digits in vicinity")

                    numbers = []
                    def grab_number(x, y):
                        number = ''
                        caret = coord(x, y)
                        while rows[caret[0]][caret[1]].isdigit() and caret[1]>0:
                            caret = coord(caret[0],caret[1]-1) # move left until no more digits
                        if not rows[caret[0]][caret[1]].isdigit():
                            caret = caret[0],caret[1]+1 # now on the first digit
                        #number += rows[caret[0]][caret[1]]
                        while rows[caret[0]][caret[1]].isdigit() and caret[1]<139:
                            number += rows[caret[0]][caret[1]]
                            caret = coord(caret[0],caret[1]+1)
                        if number != '':
                            # print(f"Found number: {number} at {caret[0]}, {caret[1]}")
                            numbers.append(int(number))
                        return caret[1] # the endposition of the number
                    for rs in [row_ix-1, row_ix, row_ix+1]:
                        for cs in [char_ix-1, char_ix, char_ix+1]:
                            if rows[rs][cs].isdigit():
                                print(f"Found a digit at {rs}, {cs}")
                                caret = grab_number(rs, cs)
                                if caret > char_ix:
                                    break
                    if len(numbers) == 2:
                        print(f"Found gear at {row_ix}, {char_ix}, with numbers {numbers}")
                        total += numbers[0] * numbers[1]
            checklist = []
    print(f"The solution to part two is: {total}")

part_two()