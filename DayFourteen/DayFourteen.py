import re


def get_point_leader_at_time(speed_data_string, time):
    speed_data = parse_speed_data(speed_data_string)
    scores = dict.fromkeys(speed_data.keys(), 0)

    for second in range(1, time + 1):
        (leaders, position) = get_leaders_at_time(speed_data, second)
        for leader in leaders:
            scores[leader] += 1
    leader = max(scores, key=scores.get)
    return leader, scores[leader]


def get_leader_at_time(speed_data_string, time):
    speed_data = parse_speed_data(speed_data_string)
    return get_leaders_at_time(speed_data, time)


def get_leaders_at_time(speed_data, time):
    position_data = {}
    for racer in speed_data.keys():
        position_data[racer] = get_distance_travelled(speed_data[racer], time)
    max_distance = max(position_data.values())
    leaders = [key for (key, value) in position_data.items() if value == max_distance]
    return leaders, max_distance


def parse_speed_data(speed_data_string):
    res = {}
    for line in speed_data_string.splitlines():
        match = re.search("(.*) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", line)
        racer = match.group(1)
        res[racer] = {"speed": int(match.group(2)),
                      "stamina": int(match.group(3)),
                      "rest": int(match.group(4))}
    return res


def get_distance_travelled(racer_data, time):
    cycle_time = racer_data["stamina"] + racer_data["rest"]
    distance_per_cycle = racer_data["speed"] * racer_data["stamina"]

    number_of_full_cycles = time / cycle_time
    last_cycle_time = time % cycle_time
    last_cycle_travel_time = racer_data["stamina"] if last_cycle_time > racer_data["stamina"] else last_cycle_time
    last_cycle_distance = racer_data["speed"] * last_cycle_travel_time

    return number_of_full_cycles * distance_per_cycle + last_cycle_distance


test_input = "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.\n" \
             "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."

print "Example 1 test: " + str(get_leader_at_time(test_input, 1000))
print "Final result: " + str(get_leader_at_time((open("./input")).read(), 2503))

print "Example 2 test: " + str(get_point_leader_at_time(test_input, 1000))
print "Part 2 Final result:" + str(get_point_leader_at_time((open("./input")).read(), 2503))
