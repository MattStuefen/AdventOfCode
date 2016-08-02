def count_nice_strings(input_data):
    nice_count = 0
    for line in input_data.splitlines():
        if is_nice(line):
            nice_count += 1
    return nice_count


def is_nice(input):
    letter_sandwich = False
    pair_set = False

    for i in range(len(input) - 1):
        letter_sandwich |= (i != (len(input) - 2)) and input[i] == input[i+2]
        pair_set |= (input[i:i+2] in input[0:i]) or (input[i:i+2] in input[i+2:len(input)])

    return pair_set and letter_sandwich


print "Example 1 test: " + str(is_nice("qjhvhtzxzqqjkmpb"))
print "Example 2 test: " + str(is_nice("xxyxx"))
print "Example 3 test: " + str(is_nice("uurcxstgmygtbstg"))
print "Example 4 test: " + str(is_nice("ieodomkazucvgmuy"))
print "Niceness total: " + str(count_nice_strings((open("./input")).read()))
