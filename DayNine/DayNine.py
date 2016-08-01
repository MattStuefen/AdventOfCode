import re
import itertools


def solve_traveling_santa_problem(input_data):
    distance_between_points = parse_input(input_data)
    route_lengths = calculate_distance_for_each_path(distance_between_points)

    min_route = min(route_lengths, key=route_lengths.get)
    return min_route, route_lengths[min_route]


def parse_input(input_data):
    # Create distance lookup dictionary
    distance_between_points = {}
    for line in input_data.splitlines():
        match = re.search("(.*) to (.*) = (\d+)", line)

        point_a = match.group(1)
        point_b = match.group(2)
        distance = int(match.group(3))

        # Add distance in both directions to make lookup go smoother
        add_distance_to_dictionary(distance_between_points, point_a, point_b, distance)
        add_distance_to_dictionary(distance_between_points, point_b, point_a, distance)
    return distance_between_points


def add_distance_to_dictionary(location_map, point_a, point_b, distance):
    if point_a not in location_map:
        location_map[point_a] = {}
    location_map[point_a][point_b] = distance


def calculate_route_distance(distance_between_points, path):
    distance = 0
    for location_index in range(len(path) - 1):
        point_a = path[location_index]
        point_b = path[location_index + 1]
        distance += distance_between_points[point_a][point_b]
    return distance


def calculate_distance_for_each_path(distance_between_points):
    paths = {}
    locations = distance_between_points.keys()
    for path in itertools.permutations(locations, len(locations)):
        paths[path] = calculate_route_distance(distance_between_points, path)
    return paths


test_strings = "London to Dublin = 464\n" \
               "London to Belfast = 518\n" \
               "Dublin to Belfast = 141\n"

print "Example 1 test: " + str(solve_traveling_santa_problem(test_strings))
print "Final result: " + str(solve_traveling_santa_problem((open("./input")).read()))
