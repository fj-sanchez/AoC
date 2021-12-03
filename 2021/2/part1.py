import collections


def part1(input_filepath="input"):
    with open(input_filepath) as f:
        input_pairs = map(lambda line: tuple(line.split()), f.readlines())

        data = collections.defaultdict(int)
        for move, value in input_pairs:
            data[move] += int(value)
    vertical = data.get("down", 0) - data.get("up", 0)
    horizontal = data.get("forward", 0)

    return vertical*horizontal


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part1("test_input"), 150)

    print(f"The result is {part1()}")
