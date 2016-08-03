def run(input_string, desired_total):
    containers_list = [int(line) for line in input_string.splitlines()]
    containers = dict([i, containers_list[i]] for i in range(len(containers_list)))
    return find_container_sets(containers, desired_total)


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


print "Example 1 test: " + str(len(run("20\n15\n10\n5\n5", 25)))
print "Final result: " + str(len(run(open("./input").read(), 150)))
