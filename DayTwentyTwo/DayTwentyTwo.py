def find_min_mana(base_player_stats, base_boss_stats, spells):
    final_cost = None
    final_spells = []
    scenarios = [{"Player": dict(base_player_stats),
                  "Boss": dict(base_boss_stats),
                  "Effects": [],
                  "Spells": [],
                  "ManaSpent": 0}]

    while len(scenarios) != 0:
        new_scenarios = []
        for scenario in scenarios:
            for spell in spells:
                new_scenario = copy_scenario(scenario)
                new_scenario["ManaSpent"] += spell["Cost"]
                new_scenario["Spells"].append(spell["Name"])

                # Only check if we know there is a chance of this being the smallest cost
                if final_cost is None or new_scenario["ManaSpent"] < final_cost:
                    result = fight(new_scenario["Player"], new_scenario["Boss"], new_scenario["Effects"], spell)
                    if result is None:
                        new_scenarios.append(new_scenario)
                    elif result:
                        # Won the fight:
                        final_cost = new_scenario["ManaSpent"]
                        final_spells = list(new_scenario["Spells"])

        scenarios = new_scenarios

    return final_cost, final_spells


def copy_scenario(scenario):
    copy = {"Player": dict(scenario["Player"]),
            "Boss": dict(scenario["Boss"]),
            "Effects": [dict(effect) for effect in scenario["Effects"]],
            "Spells": list(scenario["Spells"]),
            "ManaSpent": scenario["ManaSpent"]}
    return copy


def fight(player, boss, effects, spell):
    if spell["Cost"] > player["Mana"]:
        return False

    # Apply effects:
    apply_effect(boss, player, effects)

    # Can't cast the same effect twice so 'lose' if we did
    if spell["Name"] in [effect["Name"] for effect in effects]:
        return False

    player["Mana"] -= spell["Cost"]
    if spell["Timer"] == 0:
        boss['Hit Points'] -= spell["Damage"]
        player['Hit Points'] += spell["Heal"]
    else:
        # If we've casted an effect
        effects.append(dict(spell))

    if boss['Hit Points'] <= 0:
        return True

    # Bosses Turn:
    apply_effect(boss, player, effects)

    player['Hit Points'] -= calculate_damage(boss, player)
    if player['Hit Points'] <= 0:
        return False


def apply_effect(boss, player, effects):
    expired_effects = []
    player["Armor"] = 0
    for effect in effects:
        boss['Hit Points'] -= effect["Damage"]
        player['Hit Points'] += effect["Heal"]
        player['Mana'] += effect["ManaRegen"]
        player["Armor"] += effect["Armor"]
        effect['Timer'] -= 1
        if effect['Timer'] == 0:
            expired_effects.append(effect)

    # Remove expired effects
    for effect in expired_effects:
        effects.remove(effect)


def calculate_damage(fighter_a, fighter_b):
    damage = fighter_a['Damage'] - fighter_b['Armor']
    if damage <= 0:
        damage = 1
    return damage


spell_data = [{"Name": "Magic Missile", "Cost": 53, "Damage": 4, "Heal": 0, "Armor": 0, "ManaRegen": 0, "Timer": 0},
              {"Name": "Drain", "Cost": 73, "Damage": 2, "Heal": 2, "Armor": 0, "ManaRegen": 0, "Timer": 0},
              {"Name": "Shield", "Cost": 113, "Damage": 0, "Heal": 0, "Armor": 7, "ManaRegen": 0, "Timer": 6},
              {"Name": "Poison", "Cost": 173, "Damage": 3, "Heal": 0, "Armor": 0, "ManaRegen": 0, "Timer": 6},
              {"Name": "Recharge", "Cost": 229, "Damage": 0, "Heal": 0, "Armor": 0, "ManaRegen": 101, "Timer": 5}]

test_spell_data = [{"Name": "Test", "Cost": 53, "Damage": 40, "Heal": 0, "Armor": 0, "ManaRegen": 0, "Timer": 0},
                   {"Name": "Test", "Cost": 10, "Damage": 40, "Heal": 0, "Armor": 0, "ManaRegen": 0, "Timer": 2}]

boss_stats = {line.split(': ')[0]: int(line.split(': ')[1]) for line in open("./input").read().splitlines()}
player_stats = {'Hit Points': 50, 'Armor': 0, 'Mana': 500}

print "Final result: " + str(find_min_mana(player_stats, boss_stats, spell_data))