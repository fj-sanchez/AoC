def part2(input_filepath="input"):
    with open(input_filepath) as f:
        data = list(map(int, f.readlines()))

    return result


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part2("test_input"), X)

    print(f"The result is {part2()}")
