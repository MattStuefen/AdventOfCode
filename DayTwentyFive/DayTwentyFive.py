def get_code_by_grid_location(row, col):
    code = 20151125
    for i in range(2, get_code_index_by_grid_location(row, col) + 1):
        code *= 252533
        code %= 33554393
    return code


def get_code_index_by_grid_location(row, col):
    x = 1
    for i in range(row + col - 1):
        x += i
    return x + col - 1


example_indices = [str([get_code_index_by_grid_location(i, j) for j in range(1, 7)]) for i in range(1, 7)]
example_codes = [str([get_code_by_grid_location(i, j) for j in range(1, 7)]) for i in range(1, 7)]
print "Example 1 test:\n" + "\n".join(example_indices) + "\n\n" + "\n".join(example_codes)

print "Final result: " + str(get_code_by_grid_location(2981, 3075))
