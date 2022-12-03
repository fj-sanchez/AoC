def part2(input_filepath="../../data/3/input"):
    with open(input_filepath) as f:
        data = f.read().splitlines()

    def group_by_n(l, n=3):
            for i in range(0, len(l), n):
                yield l[i : i + n]

    total = 0
    for group in group_by_n(data):
        intersection = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
        assert len(intersection) == 1
        item = intersection.pop()

        if "a" <= item <= "z":
            total += ord(item) - 96
        else:
            total += ord(item) - 38

    return total


if __name__ == "__main__":
    import unittest

    X = 70
    tc = unittest.TestCase()
    tc.assertEqual(part2("../../data/3/test_input"), X)

    print(f"The result is {part2()}")
