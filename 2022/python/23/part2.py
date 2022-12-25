from copy import deepcopy

from move_elves import move_elves, parse_input, rotate_dirs, DIRS


def part2(input_filepath="../../data/23/input"):
    elves = parse_input(input_filepath)
    dirs = deepcopy(DIRS)

    # print_grid(elves)
    updated = True
    result = 1
    while move_elves(elves, dirs):
        result += 1
        rotate_dirs(dirs)
        # print_grid(elves)

    return result


if __name__ == "__main__":
    import unittest

    X = 20
    tc = unittest.TestCase()
    tc.assertEqual(part2("../../data/23/test_input"), X)

    print(f"The result is {part2()}")
