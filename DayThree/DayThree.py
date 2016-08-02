def calculate_number_of_houses_visited(input_data, robo_santa_enabled=False):
    coordinates = (0, 0)
    robo_coordinates = (0, 0)

    house_map = {}
    add_house_to_map(house_map, coordinates)

    count = 0
    for c in input_data:
        if count % 2 == 0:
            coordinates = update_coordinates(c, coordinates)
            add_house_to_map(house_map, coordinates)
        else:
            robo_coordinates = update_coordinates(c, robo_coordinates)
            add_house_to_map(house_map, robo_coordinates)

        count += 1 if robo_santa_enabled else 0

    return sum_houses_in_map(house_map)


def add_house_to_map(house_map, (x, y)):
    if x not in house_map:
        house_map[x] = set()
    house_map[x].add(y)


def update_coordinates(c, (x, y)):
    if c == "^":
        return x, y + 1
    elif c == "v":
        return x, y - 1
    elif c == ">":
        return x + 1, y
    elif c == "<":
        return x - 1, y
    else:
        return x, y


def sum_houses_in_map(house_map):
    total_houses = 0
    for row_of_houses in house_map.values():
        total_houses += len(row_of_houses)
    return total_houses


print "Example 1 test: " + str(calculate_number_of_houses_visited(">"))
print "Example 2 test: " + str(calculate_number_of_houses_visited("^>v<"))
print "Example 3 test: " + str(calculate_number_of_houses_visited("^v^v^v^v^v"))
print "Final result: " + str(calculate_number_of_houses_visited((open("./input")).read()))

print "Part 2 Example 1 test: " + str(calculate_number_of_houses_visited("^>", True))
print "Part 2 Example 2 test: " + str(calculate_number_of_houses_visited("^>v<", True))
print "Part 2 Example 3 test: " + str(calculate_number_of_houses_visited("^v^v^v^v^v", True))
print "Part 2 Final result: " + str(calculate_number_of_houses_visited((open("./input")).read(), True))