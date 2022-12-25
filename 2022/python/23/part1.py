from copy import deepcopy

from move_elves import parse_input, move_elves, rotate_dirs, print_grid, DIRS


def part1(input_filepath="../../data/23/input"):
    elves = parse_input(input_filepath)
    dirs = deepcopy(DIRS)

    # print_grid(elves)
    for _ in range(10):
        move_elves(elves, dirs)
        rotate_dirs(dirs)
        # print_grid(elves)

    x = [e[0] for e in sorted(elves)]
    y = [e[1] for e in sorted(elves)]
    result = (max(x) - min(x) + 1) * (max(y) - min(y) + 1) - len(elves)

    return result


if __name__ == "__main__":
    import unittest

    X = 110
    tc = unittest.TestCase()
    tc.assertEqual(part1("../../data/23/test_input"), X)

    print(f"The result is {part1()}")
