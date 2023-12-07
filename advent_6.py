import math as m
from functools import reduce

if __name__ == "__main__":  # confirms that the code is under main function
    # data = list(open('input_6.txt'))
    
    # Part 1
    # Time:        45     97     72     95
    # Distance:   305   1062   1110   1695
    time_and_distance = [
        [45, 305],
        [97, 1062],
        [72, 1110],
        [95, 1695]
    ]

    # Part 2
    # Time:        45977295
    # Distance:   305106211101695
    time_and_distance = [
        [45977295, 305106211101695]
    ]

    def distance(button_time, time):
        return (time - button_time)*button_time
    def ways_to_win(time, record_distance):
        ways = 0
        options = [t for t in range(1, time)]
        for option in options:
            if distance(option, time) > record_distance:
                ways += 1
        return ways
    solutions = [ways_to_win(t, d) for t, d in time_and_distance]

    sol1 = reduce(lambda x, y: x*y, solutions)
    sol2 = 1
    for s in solutions:
        sol2 *= s
    print(sol1)
    print(sol2)
