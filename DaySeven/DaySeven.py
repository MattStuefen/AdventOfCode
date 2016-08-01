import re

COMMAND_INDEX = 0
ARG1_INDEX = 1
ARG2_INDEX = 2
FINAL_VALUE_INDEX = 3


def run_logic(instructions):
    signals = instructions_to_map(instructions)

    # This loops though the signal dictionary and updates symbolic signal values with numeric values until there
    # are no more signals without numeric values
    done = False
    while not done:
        done = True
        for signal in signals.keys():
            source = signals[signal]

            if source[FINAL_VALUE_INDEX] is not None:
                continue
            done = False

            source[ARG1_INDEX] = replace_signal_source_with_value(signals, source[ARG1_INDEX])
            source[ARG2_INDEX] = replace_signal_source_with_value(signals, source[ARG2_INDEX])
            source[FINAL_VALUE_INDEX] = calculate_final_value(source[COMMAND_INDEX],
                                                              source[ARG1_INDEX],
                                                              source[ARG2_INDEX])

    return signals


def instructions_to_map(instructions):
    # Create a map of signal definitions
    signals = {}
    for instruction_string in instructions.splitlines():
        match = re.search("(.*) -> (.*)", instruction_string)
        destination = match.group(2)
        source = match.group(1)
        signals[destination] = parse_signal_definition(source)
    return signals


def parse_signal_definition(source_definition):
    # This function breaks down the data source string (i.e. the left side of the argument) into it's components:
    # command_name, arg1, arg2, final_value
    source_components = source_definition.split(' ')
    if len(source_components) == 1:
        # This is a set command - it should be in the form '123 -> x'
        # The data source will be a single integer constant
        return ["SET", source_components[0], None, None]
    elif len(source_components) == 2:
        # This is a NOT command - it should be in the form 'NOT x -> y'
        return [source_components[0], source_components[1], None, None]
    else:
        # This is the standard form of a command, which is written 'x CMD y -> z'
        return [source_components[1], source_components[0], source_components[2], None]


def replace_signal_source_with_value(signals, arg):
    if type(arg) is str:
        if arg.isdigit():
            arg = int(arg)
        elif signals[arg][FINAL_VALUE_INDEX] is not None:
            # Populate our input arg with another signals final value
            arg = signals[arg][FINAL_VALUE_INDEX]

    return arg


def calculate_final_value(command, arg1, arg2):
    if (type(arg1) is int) and ((arg2 is None) or (type(arg2) is int)):
        return get_command_function(command)(arg1, arg2)


def get_command_function(command):
    # Return a function with signature command(value_dictionary, arg1, arg2)
    if command == "SET":
        return lambda x, y: x
    elif command == "NOT":
        return lambda x, y: ~x
    elif command == "AND":
        return lambda x, y: x & y
    elif command == "OR":
        return lambda x, y: x | y
    elif command == "LSHIFT":
        return lambda x, y: x << y
    elif command == "RSHIFT":
        return lambda x, y: x >> y


test_instructions = "123 -> x\n" \
                    "456 -> y\n" \
                    "x AND y -> d\n" \
                    "x OR y -> e\n" \
                    "x LSHIFT 2 -> f\n" \
                    "y RSHIFT 2 -> g\n" \
                    "NOT x -> h\n" \
                    "NOT y -> i"

print "Example 1 test: " + str(run_logic(test_instructions))
print "Final result: " + str(run_logic((open("./input")).read())['a'])
