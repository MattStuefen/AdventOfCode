import json


def extract_numeric_values(arg, is_part2=False):
    if type(arg) is list:
        total = 0
        for value in arg:
            total += extract_numeric_values(value, is_part2)
        return total
    elif type(arg) is dict:
        if is_part2 and 'red' in arg.values():
            return 0
        else:
            return extract_numeric_values(arg.values(), is_part2)
    elif type(arg) is int or ((type(arg) is str) and arg.lstrip('-').isdigit()):
        return int(arg)
    else:
        return 0


test_input = '[' \
             '  [1,2,3],' \
             '  {"a":2,"b":4},' \
             '  [[[3]]],' \
             '  {"a":{"b":4},"c":-1},' \
             '  {"a":[-1,1]},' \
             '  [-1,{"a":1}],' \
             '  [],' \
             '  {}' \
             ']'

print "Example 1 test: " + str(extract_numeric_values(json.loads(test_input)))
print "Final result: " + str(extract_numeric_values(json.load(open("./input"))))
print "Part2 Final result: " + str(extract_numeric_values(json.load(open("./input")), True))
