# Determine which games would have been possible if the bag had been loaded with only 
# 12 red cubes, 13 green cubes, and 14 blue cubes. 
# What is the sum of the IDs of those games?

import os

with open('./input_2.txt') as f:
    content = f.readlines()
    games = {}
    for line in content:
        game,vals = line.split(':')
        vals = vals.strip()
        draws = vals.split(';')
        draws = [[elem.strip() for elem in x.split(',')] for x in draws]
        games[game] = draws
#    print(games)

game_table = []

for gamekey, game in games.items():
    game_id = int(gamekey.split(' ')[1])
    for draw in game:
        row = [game_id,0,0,0] # 0:game_id, 1:red, 2:green, 3:blue
        for elem in draw: # red, blue, green
            count, color = elem.split(' ')
            if color == 'red':
                row[1] += int(count)
            elif color == 'green':
                row[2] += int(count)
            elif color == 'blue':
                row[3] += int(count)
        game_table.append(row)
# print(game_table)

# 12 red cubes, 13 green cubes, and 14 blue
max_red = 12
max_green = 13
max_blue = 14

# find all games that would have been possible if the bag had been loaded with only
# max_red red cubes, max_green green cubes, and max_blue blue cubes

# make a list 1..100
game_index = [x for x in range(1,101)]
for game in game_table:
    if game[1] > max_red or game[2] > max_green or game[3] > max_blue:
        game_index.remove(game[0]) if game[0] in game_index else None

sum_ids = 0
for game in game_index:
    sum_ids += game
print(f"The answer to the first part is {sum_ids}")

###########################################################

# Part 2
# For each game, determine the minimum number of red, green, and blue cubes that would have been needed to make it possible.
game_index = [x for x in range(1,101)]
power_sum = 0
for game in game_index:
    draws = []
    for draw in game_table:
        if draw[0] == game:
            draws.append(draw)
    # print(game, draws)

    min_red = 0
    min_green = 0
    min_blue = 0
    for draw in draws:
        if draw[1] > min_red:
            min_red = draw[1]
        if draw[2] > min_green:
            min_green = draw[2]
        if draw[3] > min_blue:
            min_blue = draw[3]
    print(game, min_red, min_green, min_blue)
    power = min_red*min_green*min_blue
    power_sum += power
print(f"The answer to the second part is {power_sum}")
    



