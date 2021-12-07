import collections


def sum_of_n(n):
    return n * (n + 1) // 2


def part2(input_filepath="input"):
    with open(input_filepath) as f:
        positions = list(map(int, f.readline().split(",")))

    counts = collections.Counter(positions)
    max_pos = max(positions)
    min_pos = min(positions)

    total_costs = [0] * (max_pos - min_pos)
    for pos, weight in counts.items():
        pos_costs = list(range(pos, 0, -1)) + list(range(0, max_pos - pos, 1))
        pos_costs = [weight * sum_of_n(x) for x in pos_costs]
        total_costs = list(map(sum, zip(total_costs, pos_costs)))

    result = min(total_costs)

    return result


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part2("test_input"), 168)

    print(f"The result is {part2()}")
