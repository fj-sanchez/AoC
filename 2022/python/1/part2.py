def part1(input_filepath="../../data/1/input"):
    with open(input_filepath) as f:
        calories = {}
        ix = 1
        for line in f.readlines():
            if line == "\n":
                ix += 1
                continue
            calories[ix] = calories.setdefault(ix, 0) + int(line)

    result = sum(sorted(calories.values(), reverse=True)[:3])
    return result


if __name__ == "__main__":
    import unittest

    X = 45000
    tc = unittest.TestCase()
    tc.assertEqual(part1("../../data/1/test_input"), X)

    print(f"The result is {part1()}")
