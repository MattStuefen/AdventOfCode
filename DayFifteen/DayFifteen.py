import re


def find_optimal_cookie_recipe(ingredients_list_string, calorie_requirement=None):
    ingredients_list = parse_ingredients(ingredients_list_string)

    all_combinations = create_ingredient_combinations(len(ingredients_list.keys()), 100)
    scores = calculate_all_scores(all_combinations, ingredients_list, calorie_requirement)

    return max(scores.values())


def parse_ingredients(ingredients_list_string):
    res = {}
    for line in ingredients_list_string.splitlines():
        match = re.search("(.*): capacity (.*), durability (.*), flavor (.*), texture (.*), calories (.*)", line)
        ingredient = match.group(1)
        res[ingredient] = {"capacity": int(match.group(2)),
                           "durability": int(match.group(3)),
                           "flavor": int(match.group(4)),
                           "texture": int(match.group(5)),
                           "calories": int(match.group(6))}
    return res


def create_ingredient_combinations(available_ingredients_count, max_quantity):
    if available_ingredients_count == 1: return [[max_quantity]]
    res = []
    for i in range(max_quantity):
        combos = create_ingredient_combinations(available_ingredients_count - 1, max_quantity - i)
        for combo in combos:
            res.append([i] + combo)
    return res


def calculate_all_scores(all_combinations, ingredients_list, calorie_requirement):
    scores = {}
    for combination in all_combinations:
        scores[str(combination)] = calculate_score(combination, ingredients_list, calorie_requirement)
    return scores


def calculate_score(combination, ingredients_list, calorie_requirement):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0
    for ingredient in ingredients_list:
        quantity = combination[ingredients_list.keys().index(ingredient)]
        capacity += quantity * ingredients_list[ingredient]['capacity']
        durability += quantity * ingredients_list[ingredient]['durability']
        flavor += quantity * ingredients_list[ingredient]['flavor']
        texture += quantity * ingredients_list[ingredient]['texture']
        calories += quantity * ingredients_list[ingredient]['calories']
        
    # Part two indicates that a recipe must have exactly 500 calories - so if it doesn't, let's set score to 0 here.
    if calorie_requirement is not None and calories != calorie_requirement or \
                    capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
        score = 0
    else:
        score = capacity * durability * flavor * texture
    return score


test_input = "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8\n" \
             "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"

print "Example 1 test: " + str(find_optimal_cookie_recipe(test_input))
print "Final result: " + str(find_optimal_cookie_recipe((open("./input")).read()))

print "Part 2 Example 1 test: " + str(find_optimal_cookie_recipe(test_input, 500))
print "Part 2 Final result: " + str(find_optimal_cookie_recipe((open("./input")).read(), 500))
