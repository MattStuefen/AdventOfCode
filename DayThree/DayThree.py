def calculate_number_of_houses_visited(input_data):
    coordinates = (0, 0)
    house_map = {}
    add_house_to_map(house_map, coordinates)

    for c in input_data:
        coordinates = update_coordinates(c, coordinates)
        add_house_to_map(house_map, coordinates)

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
