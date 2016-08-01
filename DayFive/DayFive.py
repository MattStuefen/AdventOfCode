def count_nice_strings(input_data):
    nice_count = 0
    for line in input_data.splitlines():
        if is_nice(line):
            nice_count += 1
    return nice_count


def is_nice(input):
    vowels = ('a', 'e', 'i', 'o', 'u')
    bad_strings = ('ab', 'cd', 'pq', 'xy')
    prev_char = None
    vowel_count = 0
    double_letter = False
    contains_bad_string = False

    for c in input:
        if c in vowels:
            vowel_count += 1

        if prev_char == c:
            double_letter = True

        if prev_char and (prev_char + c) in bad_strings:
            contains_bad_string = True

        prev_char = c

    return (vowel_count >= 3) and double_letter and not contains_bad_string


print "Example 1 test: " + str(is_nice("ugknbfddgicrmopn"))
print "Example 2 test: " + str(is_nice("aaa"))
print "Example 3 test: " + str(is_nice("jchzalrnumimnmhp"))
print "Example 4 test: " + str(is_nice("haegwjzuvuyypxyu"))
print "Example 5 test: " + str(is_nice("dvszwmarrgswjxmb"))
print "Niceness total: " + str(count_nice_strings((open("./input")).read()))
