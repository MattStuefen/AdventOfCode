def look_and_say(number_sequence, remaining_iterations):
    if remaining_iterations == 0:
        return number_sequence

    prev_char = None
    char_count = 0
    result = ""

    for char in number_sequence:
        if prev_char is None:
            prev_char = char
            char_count = 1
        elif prev_char == char:
            char_count += 1
        else:
            result += str(char_count) + prev_char
            prev_char = char
            char_count = 1
    result += str(char_count) + prev_char

    return look_and_say(result, remaining_iterations - 1)


print "Example 1 test: " + look_and_say('1', 5)
print "Final result: " + str(len(look_and_say('3113322113', 40)))
print "Part 2 Final result: " + str(len(look_and_say('3113322113', 50)))
