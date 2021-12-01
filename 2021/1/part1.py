import operator


def part1(input_filepath="input"):
    with open(input_filepath) as f:
        data = list(map(int, f.readlines()))

    result = sum(map(operator.lt, data[:-1], data[1:]))

    return result


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part1("test_input"), 7)

    print(f"The result is {part1()}")
