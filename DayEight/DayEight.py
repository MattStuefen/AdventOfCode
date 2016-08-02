import re

def find_excess_string_length(input_data):
    total_part1 = 0
    total_part2 = 0

    for line in input_data.splitlines():
        total_part1 += len(line)
        total_part1 -= len(line[1:-1].decode('string_escape'))

        total_part2 += len('"' + re.escape(line) + '"')
        total_part2 -= len(line)

    return total_part1, total_part2


test_strings = "\"\"\n" \
               "\"abc\"\n" \
               "\"aaa\\\"aaa\"\n" \
               "\"\\x27\"\n"

print "Example 1 test: " + str(find_excess_string_length(test_strings))
print "Final result: " + str(find_excess_string_length((open("./input")).read()))
