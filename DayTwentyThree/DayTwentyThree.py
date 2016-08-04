def process_instructions(input_code, starting_a=0):
    instructions = [line.split(' ') for line in input_code.replace(',', '').splitlines()]
    registers = {'a': starting_a, 'b': 0}
    i = 0
    while i < len(instructions):
        i += process_instruction(instructions[i], registers)
    return registers


def process_instruction(instruction, registers):
    index_offset = functions[instruction[0]](registers, instruction[1:])
    if index_offset is None:
        return 1
    return int(index_offset)


functions = {"hlf": lambda regs, r: regs.update({r[0]: regs[r[0]] / 2}),
             "tpl": lambda regs, r: regs.update({r[0]: regs[r[0]] * 3}),
             "inc": lambda regs, r: regs.update({r[0]: regs[r[0]] + 1}),
             "jmp": lambda regs, offset: offset[0],
             "jie": lambda regs, args: args[1] if regs[args[0]] % 2 == 0 else None,
             "jio": lambda regs, args: args[1] if regs[args[0]] == 1 else None}

test_input = "inc a\n" \
             "jio a, +2\n" \
             "tpl a\n" \
             "inc a"

print "Example 1 test: " + str(process_instructions(test_input))
print "Final result: " + str(process_instructions(open("./input").read()))
print "Part 2 Final result: " + str(process_instructions(open("./input").read(), 1))