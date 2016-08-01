def find_excess_string_length(input_data):
    total = 0
    for line in input_data.splitlines():
        total += len(line)
        total -= len(line[1:-1].decode('string_escape'))

    return total


test_strings = "\"\"\n" \
               "\"abc\"\n" \
               "\"aaa\\\"aaa\"\n" \
               "\"\\x27\"\n"

print "Example 1 test: " + str(find_excess_string_length(test_strings))
print "Final result: " + str(find_excess_string_length((open("./input")).read()))
