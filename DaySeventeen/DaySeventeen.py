import ast


def run(input_string, desired_total):
    containers_list = [int(line) for line in input_string.splitlines()]
    containers = dict([i, containers_list[i]] for i in range(len(containers_list)))

    container_sets = find_container_sets(containers, desired_total)

    return len(container_sets), find_number_of_min_sets(container_sets)


def find_container_sets(containers, desired_total, cur_sum=0, cur_container_set=[]):
    unique_container_sets = set()
    for container_id in (set(containers.keys()) - set(cur_container_set)):
        new_sum = cur_sum + containers[container_id]

        containers = dict(containers)
        del containers[container_id]

        if new_sum < desired_total:
            new_sets = find_container_sets(containers, desired_total, new_sum, cur_container_set + [container_id])
            unique_container_sets = unique_container_sets.union(new_sets)
        elif new_sum == desired_total:
            unique_container_sets.add(str(sorted(cur_container_set + [container_id])))

    return unique_container_sets


def find_number_of_min_sets(container_sets):
    # Convert sets from string to lists
    container_sets = [ast.literal_eval(container_set) for container_set in container_sets]
    # Find min length among all container sets
    min_length = min([len(container_set) for container_set in container_sets])
    # Create array of booleans where a True indicates that the length at that index of the container set is the minimum
    min_length_array = [(len(container_set) == min_length) for container_set in container_sets]
    # Sum boolean array (True = 1, False = 0)
    return sum(min_length_array)


print "Example 1 test: " + str(run("20\n15\n10\n5\n5", 25))
print "Final result: " + str(run(open("./input").read(), 150))
