import re
import itertools


def get_max_happiness(seating_data_string):
    seating_data = parse_seating_data(seating_data_string)
    possible_seating_arrangements = find_possible_seating_arrangements(seating_data)
    optimal_seating_arrangement = max(possible_seating_arrangements, key=possible_seating_arrangements.get)
    return optimal_seating_arrangement, possible_seating_arrangements[optimal_seating_arrangement]


def parse_seating_data(seating_data):
    res = {}
    for line in seating_data.splitlines():
        match = re.search("(.*) would (.*) (\d+) happiness units by sitting next to (.*).", line)
        person_one = match.group(1)
        person_two = match.group(4)
        happiness_effect = int(match.group(3)) if match.group(2) == "gain" else -1 * int(match.group(3))
        if person_one not in res:
            res[person_one] = {}
        res[person_one][person_two] = happiness_effect
    return res


def find_possible_seating_arrangements(seating_data):
    arrangements = {}
    for arrangement in itertools.permutations(seating_data, len(seating_data)):
        arrangements[arrangement] = calculate_happiness(seating_data, arrangement)
    return arrangements


def calculate_happiness(seating_data, arrangement):
    total = 0
    for i in range(len(arrangement)):
        if i < (len(arrangement) - 1):
            total += seating_data[arrangement[i]][arrangement[i + 1]]
            total += seating_data[arrangement[i + 1]][arrangement[i]]
        else:
            total += seating_data[arrangement[i]][arrangement[0]]
            total += seating_data[arrangement[0]][arrangement[i]]
    return total


test_data = "Alice would gain 54 happiness units by sitting next to Bob.\n" \
            "Alice would lose 79 happiness units by sitting next to Carol.\n" \
            "Alice would lose 2 happiness units by sitting next to David.\n" \
            "Bob would gain 83 happiness units by sitting next to Alice.\n" \
            "Bob would lose 7 happiness units by sitting next to Carol.\n" \
            "Bob would lose 63 happiness units by sitting next to David.\n" \
            "Carol would lose 62 happiness units by sitting next to Alice.\n" \
            "Carol would gain 60 happiness units by sitting next to Bob.\n" \
            "Carol would gain 55 happiness units by sitting next to David.\n" \
            "David would gain 46 happiness units by sitting next to Alice.\n" \
            "David would lose 7 happiness units by sitting next to Bob.\n" \
            "David would gain 41 happiness units by sitting next to Carol."

print "Example 1 test: " + str(get_max_happiness(test_data))
print "Final result: " + str(get_max_happiness((open("./input")).read()))
print "Part 2 Final result: " + str(get_max_happiness((open("./input_part2")).read()))
