__author__ = 'Matt'

def animate_yard(input, num_cycles):
    light_grid = init_light_grid(input)
    for i in range(num_cycles):
        light_grid = update_light_grid(light_grid)
    return sum([sum(row) for row in light_grid])


def init_light_grid(input):
    return [[c == '#' for c in line] for line in input.splitlines()]


def update_light_grid(light_grid):
    new_grid = [[False for light in row] for row in light_grid]

    for i in range(len(light_grid)):
        for j in range(len(light_grid[i])):
            adjacent_lights = []

            for i_adjacent in create_range(i, len(light_grid)):
                for j_adjacent in create_range(j, len(light_grid[i])):
                    if not (i == i_adjacent and j == j_adjacent):
                        adjacent_lights.append(light_grid[i_adjacent][j_adjacent])

            neighbors_on = sum(adjacent_lights)

            if light_grid[i][j] and neighbors_on in [2, 3]:
                new_grid[i][j] = True
            elif not light_grid[i][j] and neighbors_on == 3:
                new_grid[i][j] = True
    return new_grid


def create_range(cur_val, max_val):
    if cur_val == 0:
        val_range = range(cur_val, (cur_val + 1) + 1)
    elif cur_val == max_val - 1:
        val_range = range(cur_val - 1, cur_val + 1)
    else:
        val_range = range(cur_val - 1, (cur_val + 1) + 1)
    return val_range


light_grid_string = ".#.#.#\n" \
                    "...##.\n" \
                    "#....#\n" \
                    "..#...\n" \
                    "#.#..#\n" \
                    "####..\n"


print "Example 1 test: " + str(animate_yard(light_grid_string, 4))
print "Final result: " + str(animate_yard((open("./input")).read(), 100))
