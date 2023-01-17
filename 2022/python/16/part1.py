def part1(input_filepath="../../data/0/input"):
    with open(input_filepath) as f:
        data = list(map(int, f.readlines()))

    return data


if __name__ == "__main__":
    import unittest

    X = []
    tc = unittest.TestCase()
    tc.assertEqual(part1("../../data/0/test_input"), X)

    print(f"The result is {part1()}")
