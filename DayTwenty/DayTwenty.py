def find_first_house_with_enough_presents(calc_num_of_presents, desired_num_presents, starting_house=0):
    # Brute force through all possible houses until reaching the house with the desired number of presents
    # To speed things up we can start with a higher house number, and change the difference in house number (although
    # there is a chance we could miss the correct house if we don't make a good choice...)
    house_number = starting_house - 1
    num_of_presents = 0
    while num_of_presents < desired_num_presents:
        house_number += 1
        num_of_presents = calc_num_of_presents(house_number)
    return house_number

# These functions calculate the number of presents at a given house per the rules given in the description
part_one = lambda house: sum([elf for elf in range(1, house + 1) if (house % elf) == 0]) * 10
part_two = lambda house: sum([elf for elf in range(1, house + 1) if ((house % elf) == 0) and (house <= 50 * elf)]) * 11

print "Final result: " + str(find_first_house_with_enough_presents(part_one, 29000000, 665280))
print "Part 2 Final result: " + str(find_first_house_with_enough_presents(part_two, 29000000, 705600))
