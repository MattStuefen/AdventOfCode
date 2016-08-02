def calc_total_wrapping_paper_and_ribbon():
    total_wrapping_paper = 0
    total_ribbon = 0

    input_data = (open("./input")).read()
    for line in input_data.splitlines():
        dimensions = line.split('x')
        dimensions = [int(c) for c in dimensions]
        total_wrapping_paper += calc_wrapping_paper_for_present(dimensions[0], dimensions[1], dimensions[2])
        total_ribbon += calc_ribbon_for_present(dimensions[0], dimensions[1], dimensions[2])

    return total_wrapping_paper, total_ribbon


def calc_wrapping_paper_for_present(l, w, h):
    side_one = l * w
    side_two = l * h
    side_three = w * h
    smallest_area = min([side_one, side_two, side_three])
    return 2 * (side_one + side_two + side_three) + smallest_area


def calc_ribbon_for_present(l, w, h):
    min_perimeter_sides = [l,w,h]
    min_perimeter_sides.remove(max(min_perimeter_sides))
    return 2*(min_perimeter_sides[0] + min_perimeter_sides[1]) + l*h*w


print "Example 1 test: " + str((calc_wrapping_paper_for_present(2, 3, 4), calc_ribbon_for_present(2, 3, 4)))
print "Example 2 test: " + str((calc_wrapping_paper_for_present(1, 1, 10), calc_ribbon_for_present(1, 1, 10)))

print "Final result: " + str(calc_total_wrapping_paper_and_ribbon())
