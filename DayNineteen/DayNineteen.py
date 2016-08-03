import re

from itertools import groupby


def find_distinct_molecules(machine_definition):
    (machine_definition, starting_molecule) = machine_definition.split("\n\n")
    return len(perform_replacements(starting_molecule, parse_replacements(machine_definition)))


def parse_replacements(replacements_string):
    replacements = [line.split(" => ") for line in replacements_string.splitlines()]
    replacements = groupby(replacements, key=lambda replacement: replacement[0])
    return {key: [v[1] for v in value] for key, value in replacements}


def perform_replacements(starting_molecule, replacements):
    result_set = set()
    molecule = re.findall('[A-Z][a-z]*', starting_molecule)
    for atom_index in range(len(molecule)):
        if molecule[atom_index] not in replacements: continue
        for replacement in replacements[molecule[atom_index]]:
            new_molecule = list(molecule)
            new_molecule[atom_index] = replacement
            result_set.add(''.join(new_molecule))
    return result_set


test_machine_data = "H => HO\n" \
                    "H => OH\n" \
                    "O => HH\n" \
                    "\n" \
                    "HOH"

print "Example 1 test: " + str(find_distinct_molecules(test_machine_data))
print "Final result: " + str(find_distinct_molecules((open("./input")).read()))
