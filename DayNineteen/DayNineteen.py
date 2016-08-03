import re

from itertools import groupby


def fabricate_molecule(machine_definition):
    (machine_definition, desired_molecule) = machine_definition.split("\n\n")
    replacements = parse_replacements(machine_definition)

    result_set = {desired_molecule}
    count = 0
    while 'e' not in result_set:
        count += 1
        new_result_set = set()
        for molecule in result_set:
            new_result_set = new_result_set.union(perform_reverse_replacements(molecule, replacements))

        result_set = new_result_set
    return count


def find_distinct_molecules(machine_definition):
    (machine_definition, starting_molecule) = machine_definition.split("\n\n")
    return len(perform_replacements(starting_molecule, parse_replacements(machine_definition)))


def parse_replacements(replacements_string):
    replacements = [line.split(" => ") for line in replacements_string.splitlines()]
    replacements = groupby(replacements, key=lambda replacement: replacement[0])
    return {key: [v[1] for v in value] for key, value in replacements}


def perform_replacements(starting_molecule, replacements):
    result_set = set()
    molecule = re.findall('[A-Z][a-z]*', starting_molecule) if starting_molecule != 'e' else ['e']
    for atom_index in range(len(molecule)):
        if molecule[atom_index] not in replacements: continue
        for replacement in replacements[molecule[atom_index]]:
            new_molecule = list(molecule)
            new_molecule[atom_index] = replacement
            result_set.add(''.join(new_molecule))
    return result_set


def perform_reverse_replacements(ending_molecule, replacements):
    result_set = set()
    for atom in replacements:
        for replacement in replacements[atom]:
            replacement_indices = [i for i in range(len(ending_molecule)) if ending_molecule.startswith(replacement, i)]
            for replacement_index in replacement_indices:
                res = ending_molecule[:replacement_index] + ending_molecule[replacement_index:].replace(replacement,
                                                                                                        atom, 1)
                if 'e' not in res or 'e' == res:
                    result_set.add(res)
    return result_set


test_machine_data = "e => H\n" \
                    "e => O\n" \
                    "H => HO\n" \
                    "H => OH\n" \
                    "O => HH\n" \
                    "\n" \
                    "HOH"

print "Example 1 test: " + str(find_distinct_molecules(test_machine_data))
print "Final result: " + str(find_distinct_molecules((open("./input")).read()))

print "Part 2 Example 1 test: " + str(fabricate_molecule(test_machine_data))


# Part 2:
# While brute force works to solve the example problem the final problem is too complicated - the result takes a very
# long time to process.  I looked to google to find a better solution:
#
# Each atom replacement with length > 2 follows the following pattern:
# X Rn [] Ar        -       Where X is a single atom and [] is a group
# Also note that Y only occurs in these sequences, so potential patters can be:
# X Rn [] Ar        X Rn [X]Y[X] Ar       X Rn [X]Y[X]Y[X] Ar
# Also note that Y does not occur in replacements with length 2 and always appears between Rn and Ar
#
# If no Rn or Ar were in the final string the number of steps would be:
#   Number of Atoms - 1
# since each step would add one atom (starting at 'e')
#
# Any time we add an Rn / Ar pair we add at least two other atoms.
# We can think of this as doing a standard two atom replacement with two bonus atoms (Rn and Ar)
#
# If we have a Y in the sequence we get two additional atoms on top of our Rn / Ar bonus (per Y)
#
# That yields the following equation:
# number of steps = (Number of atoms - 1) - (Number of Rn's and Ar's) - (Number of Y's * 2)
def solve_number_of_steps_equation(input_string):
    (machine_definition, desired_molecule) = input_string.split("\n\n")
    desired_molecule_list = re.findall('[A-Z][a-z]*', desired_molecule)

    element_count = len(desired_molecule_list)
    rn_count = desired_molecule_list.count('Rn')
    ar_count = desired_molecule_list.count('Ar')
    y_count = desired_molecule_list.count('Y')

    return element_count - 1 - (rn_count + ar_count) - 2 * y_count


print "Part 2 Final result: " + str(solve_number_of_steps_equation(open("./input").read()))
