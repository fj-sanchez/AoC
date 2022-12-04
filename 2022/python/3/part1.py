def part1(input_filepath="../../data/3/input"):
    with open(input_filepath) as f:
        data = f.read().splitlines()

    total = 0
    for line in data:
        half_len = len(line) // 2
        intersection = set(line[:half_len]).intersection(set(line[half_len:]))
        assert len(intersection) == 1
        item = intersection.pop()

        if "a" <= item <= "z":
            total += ord(item) - 96
        else:
            total += ord(item) - 38

    return total


if __name__ == "__main__":
    import unittest

    X = 157
    tc = unittest.TestCase()
    tc.assertEqual(part1("../../data/3/test_input"), X)

    print(f"The result is {part1()}")
