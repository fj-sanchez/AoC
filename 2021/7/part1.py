import statistics

def part1(input_filepath="input"):
    with open(input_filepath) as f:
        positions = list(map(int, f.readline().split(",")))

    median = statistics.median(positions)
    result = sum(abs(pos-median) for pos in positions)

    return result


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part1("test_input"), 37)

    print(f"The result is {part1()}")
