import collections


def part2(input_filepath="input"):
    with open(input_filepath) as f:
        data = map(int, f.readline().split(","))
    fish_population = collections.defaultdict(int)
    for fish_age in data:
        fish_population[fish_age] += 1

    days = 256
    for day in range(days):
        new_fish_population = collections.defaultdict(int)
        for population_age, population_size in fish_population.items():
            if population_age == 0:
                new_fish_population[6] += population_size
                new_fish_population[8] += population_size
            else:
                new_fish_population[population_age - 1] += population_size
        fish_population = new_fish_population

    total_fish_population = sum(fish_population.values())
    return total_fish_population


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part2("test_input"), 26984457539)

    print(f"The result is {part2()}")
