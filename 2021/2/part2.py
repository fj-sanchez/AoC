import collections


def part2(input_filepath="input"):
    with open(input_filepath) as f:
        input_pairs = [(move, int(value)) for move, value in map(lambda line: tuple(line.split()), f.readlines())]

        aim = 0
        position = 0
        depth = 0
        for move, value in input_pairs:
            if move == "forward":
                position += value
                depth += value*aim
            else:
                aim += value * (1 if move == "down" else -1)

    return position*depth


if __name__ == "__main__":
    import unittest

    tc = unittest.TestCase()
    tc.assertEqual(part2("test_input"), 900)

    print(f"The result is {part2()}")
