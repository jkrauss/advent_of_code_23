import math as m

if __name__ == "__main__":  # confirms that the code is under main function
    data = list(open('input_5.txt'))

    seeds = data[0].split(':')[1].strip().split(' ')
    seeds = [int(x) for x in seeds]

    seed_to_soil = data[3:13]
    soil_to_fertilizer = data[15:31]
    fertilizer_to_water = data[33:48]
    water_to_light = data[50:95]
    light_to_temperature = data[97:112]
    temperature_to_humidity = data[114:137]
    humidity_to_location = data[139:150]

    names = {'seed_to_soil' : 0
            , 'soil_to_fertilizer' : 1
            , 'fertilizer_to_water' : 2
            , 'water_to_light' : 3
            , 'light_to_temperature' : 4
            , 'temperature_to_humidity' : 5
            , 'humidity_to_location': 6
            }

    maps = []
    for m in [seed_to_soil, soil_to_fertilizer, fertilizer_to_water
            , water_to_light, light_to_temperature
            , temperature_to_humidity, humidity_to_location]:
        m = [row.split(' ') for row in m]
        m = [[int(x.strip()) for x in row] for row in m]
        maps.append(m)
    #print(maps[names['seed_to_soil']][0])

    # Each line within a map contains three numbers: 
    # the destination range start, the source range start, and the range length.
    # What is the lowest location number that corresponds to any of the initial seed numbers?

    # seed = seeds[0]
    # print(f"seed : {seed}")
    # map = maps[names['seed_to_soil']]



    def calculate(seed, map_):
#        print(f"calculating {seed} in map {map}")
        for row in map_:
            if seed >= row[1] and seed < row[1] + row[2]: # >= source range start & < source range start + range length
                seed = row[0] + seed - row[1] # destination range start + (seed - source range start)
                break
        return seed

    def get_lowest_location(seeds):
        print(f"getting lowest location for {len(seeds)} seeds")

        percent = int(len(seeds) / 100)
        if percent == 0:
            percent = 1
        complete_count = 0
        done_count=0
        locations = []
        for seed in seeds:
            for map_ in maps:
                seed = calculate(seed, map_)
            locations.append(seed)
            done_count += 1
            if done_count % percent == 0:
                complete_count += 1
                print(f"{complete_count}% complete")
        #locations.sort()
        #print(locations)
        return min(locations)

    print(f"Part 1: {get_lowest_location(seeds)}")

    # Part 2
    # print(seeds)
    # split seeds into tuples of 2, second entry of every tuple is now the range length
    seeds = [seeds[i:i+2] for i in range(0, len(seeds), 2)]
    #print(seeds)

    superseeds = []
    for seed in seeds:
        print(f"adding seed: {seed} to superseeds")
        for i in range(seed[1]):
            superseeds.append(seed[0] + i)

    print(f"superseeds: {len(superseeds)}")


    num_batches = 8
    batch_size = len(superseeds) // num_batches

    # Divide superseeds into batches
    batches = [superseeds[i:i+batch_size] for i in range(0, len(superseeds), batch_size)]
    # print(batches)

    procs = []

    # instantiating process with arguments
    print(f"starting {num_batches} processes")
    solutions = []
    # manager = Manager()
    # solutions = manager.list()
    for batch in batches:
        # proc = Process(target=get_lowest_location, args=(batch,solutions))
        # procs.append(proc)
        # proc.start()
        solutions.append(get_lowest_location(batch))

    # complete the processes
    # for proc in procs:
    #     proc.join()
    solution = min(solutions)


print(f"Part 2: {solution}")


