def find_sue(sue_list_string, mfcsam_data):
    # Assume first perfect match is the real sue:
    sue_list = parse_sue_list(sue_list_string)
    for sue in sue_list:
        is_correct_sue = True

        for item in sue:
            is_correct_sue &= sue[item] == mfcsam_data[item]

        if is_correct_sue:
            return sue_list.index(sue) + 1
    return None

def parse_sue_list(sue_list_string):
    res = []
    for line in sue_list_string.splitlines():
        sues_items = {}

        # Cut off sue number since they are listed in order
        line = line[line.index(':') + 2:]
        for item in line.split(','):
            (item_name, quantity) = item.strip().split(":")
            sues_items[item_name] = int(quantity)

        res.append(sues_items)
    return res


mfcsam_output = {"children": 3,
                 "cats": 7,
                 "samoyeds": 2,
                 "pomeranians": 3,
                 "akitas": 0,
                 "vizslas": 0,
                 "goldfish": 5,
                 "trees": 3,
                 "cars": 2,
                 "perfumes": 1}

print "test" + str(find_sue((open("./input")).read(), mfcsam_output))
