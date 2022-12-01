def part1(input_filepath="input"):
    with open(input_filepath) as f:
        data = list(map(int, f.readlines()))

    return data


if __name__ == "__main__":
    import unittest

    X = []
    tc = unittest.TestCase()
    tc.assertEqual(part1("test_input"), X)

    print(f"The result is {part1()}")
