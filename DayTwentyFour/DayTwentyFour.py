import itertools


def find_min_quantum_entanglement(packages):
    packages = sorted(packages, reverse=True)
    group_weight = sum(packages) / 3

    smallest_groups = find_smallest_groups(group_weight, packages)
    entanglements = [reduce(lambda x, y: x * y, group) for group in smallest_groups]

    return min(entanglements)


def find_smallest_groups(group_weight, packages):
    for i in range(len(packages)):
        working_combos = []
        for combo in itertools.combinations(packages, i):
            if sum(combo) == group_weight and check_other_groups(packages, combo):
                working_combos.append(combo)
        if len(working_combos) > 0:
            return working_combos
    return []


def check_other_groups(packages, first_group):
    remaining_packages = [package for package in packages if package not in first_group]
    for i in range(len(remaining_packages)):
        for combo in itertools.combinations(remaining_packages, i):
            if sum(combo) == (sum(remaining_packages) - sum(combo)):
                return True
    return False


test_packages = range(1, 5 + 1) + range(7, 11 + 1)
print "Example 1 test: " + str(find_min_quantum_entanglement(test_packages))

input_packages = [int(line) for line in open("./input").read().splitlines()]
print "Final result: " + str(find_min_quantum_entanglement(input_packages))
