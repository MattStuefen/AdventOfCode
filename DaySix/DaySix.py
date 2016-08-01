import re


def process_instructions(instructions):
    light_grid = [[False for j in range(1000)] for i in range(1000)]
    for instruction_string in instructions.splitlines():
        instruction = parse_instruction(instruction_string)
        execute_instruction(light_grid, instruction)

    # return the number of lights that are lit
    return sum([sum(row) for row in light_grid])


def parse_instruction(instruction):
    match = re.search("(.*) (\d+),(\d+) through (\d+),(\d+)", instruction)
    command = get_command_function(match.group(1))
    start = (int(match.group(2)), int(match.group(3)))
    end = (int(match.group(4)), int(match.group(5)))
    return command, start, end


def get_command_function(command):
    if command == "turn on":
        return lambda x: True
    elif command == "toggle":
        return lambda x: not x
    elif command == "turn off":
        return lambda x: False


def execute_instruction(grid, (func, (x1, y1), (x2, y2))):
    for light_row in grid[x1:x2 + 1]:
        light_row[y1:y2 + 1] = [func(val) for val in light_row[y1:y2 + 1]]


test_instructions = "turn on 0,0 through 999,999\n" \
                    "toggle 0,0 through 999,0\n" \
                    "turn off 499,499 through 500,500"

print "Example 1 test: " + str(process_instructions(test_instructions))
print "Final result: " + str(process_instructions((open("./input")).read()))
