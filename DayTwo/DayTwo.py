def calc_wrapping_paper_for_present(l, w, h):
    side_one = l * w
    side_two = l * h
    side_three = w * h
    smallest_area = min([side_one, side_two, side_three])
    return 2 * (side_one + side_two + side_three) + smallest_area


def calc_total_wrapping_paper():
    total = 0

    input_data = (open("./input")).read()
    for line in input_data.splitlines():
        dimensions = line.split('x')
        dimensions = [int(c) for c in dimensions]
        total += calc_wrapping_paper_for_present(dimensions[0], dimensions[1], dimensions[2])

    return total


print "Example 1 test: " + str(calc_wrapping_paper_for_present(2, 3, 4))
print "Example 2 test: " + str(calc_wrapping_paper_for_present(1, 1, 10))
print "Final result: " + str(calc_total_wrapping_paper())
